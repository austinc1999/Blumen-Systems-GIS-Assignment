from flask import Flask, request
from flask_restful import Resource, Api
from arcgis.gis import GIS
from arcgis.features import FeatureLayer
from arcgis.geometry import filters

app = Flask(__name__)
api = Api(app)
gis = GIS()


@app.route('/')
class PadExtract(Resource):
    def __init__(self):
        self.feature_layer = FeatureLayer(
            "https://services1.arcgis.com/Hp6G80Pky0om7QvQ/arcgis/rest/services/PAD_US/FeatureServer/0"
        )
        self.polygons = []

    def compute(self, name):
        result = {}
        total = 0
        for poly in self.polygons:
            area = poly["Area"]
            total += area
            if poly[name] in result:
                result[poly[name]] += area
            else:
                result[poly[name]] = area

        for key, val in result.items():
            result[key] = val / total
        return result

    def get(self):
        args = request.args
        type_arg = args.get('type')
        data = request.get_json()
        self.get_data(data)
        if type_arg is None:
            manager_result = self.compute("Manager")
            desig_result = self.compute("Designation")
            feature_result = self.compute("Feature")
            result = {'Manager_result': manager_result,
                    'Designation Result': desig_result,
                    'feature_result': feature_result
                    }, 200  # return data with 200

        elif type_arg == "manager":
            manager_result = self.compute("Manager")
            result = {'Manager_Result': manager_result,
                   }, 200  # return data with 200

        elif type_arg == "designation":
            desig_result = self.compute("Designation")
            result = {'Designation_Result': desig_result,
                    }, 200  # return data with 200

        elif type_arg == "feature":
            feature_result = self.compute("Feature")
            result = {'Feature_Class_Result': feature_result,
                    }, 200  # return data with 200

        else:
            result = {"Unexpected Argument": type_arg}, 400  # return error with 400
        return result

    def get_data(self, data):
        # Grab first geometry, can add additional functionality for all polygons later
        geometry = data['features'][0]["geometry"]
        intersects_filter = filters.intersects(geometry)
        results = self.feature_layer.query(
            geometry_filter=intersects_filter
        ).features
        for poly in results:
            poly_dict = {
                "Manager": poly.attributes["Mang_Type"],
                "Designation": poly.attributes["Des_Tp"],
                "Feature": poly.attributes["FeatClass"],
                "Area": poly.attributes["GIS_Acres"]}
            self.polygons.append(poly_dict)

    @staticmethod
    def post():
        return "Permission Denied", 401  # Not implemented so we can just return 401


api.add_resource(PadExtract, '/padus')  # '/padus' is our entry point

if __name__ == '__main__':
    app.run()
