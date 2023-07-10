PAD-US API
------------------------------------
This is a readme document for the deliverable of the assignment to build a PAD-US API.
------------------------------------
Assignment Overview

The objective of this coding exercise is to build an API that utilizes the USGS
Protected Area Designations (PAD-US) database to calculate Area of Interest
(AOI) overlaps with different variables. The API allows an application
to provide a geojson AOI and receive the desired protected area overlap for
the given AOI as a response.

------------------------------------
Running the PAD-US API Locally

To run the PAD-US API locally, please follow the instructions below:


1. Clone the repository:
	
	git clone <repository_url>

2. Build the docker image using the Dockerfile (docker build . -t <name of new image>)
	2a: Start and run the docker container (docker run -p 5000:5000 <name of image>). 

3. Now that the flask app is running, you can either send a request using Postman or a custom python script that sends a geojson with the get request. Format the geojson according to the geojson standardized schema. (You can examine the la.geojson for more information). ***Important to note this current functionality only supports one AOI per request.

------------------------------------
API Endpoints

The following are the available endpoints provided by the PAD-US API:

'GET /api/padus?type=manager': 
Calculate the percentage overlap for all different 'Manager Types'
based on the provided AOI.

'GET /api/padus?type=designation': 
Calculate the percentage overlap for all different Designation Types'
based on the provided AOI.

'GET /api/padus?type=feature': 
Calculate the percentage overlap for all different 'Features Classes'
based on the provided AOI.

'GET /api/padus':
Calculate the percentage overlap for all above variables
based on the provided AOI.
