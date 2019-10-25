Example files for a typical GLA configuration.
==============================================

These are meant as illustration (although they are from a working example).
APP is the name of application - should be replaced by an appropriate name.

- APP.glm:	A valid GridlabD model file. Must have the fncs_msg object that declares
 			the published/subscibed data points.
- APP.gll:	List of the data points to be recorder in the InfluxDB server
- APP.yaml:	Configuration file for the fncs/broker that declares all the topics (i.e.messages) published by the broker.
  - The file contains the APP name - this should be updated as needed,
  - The messages must be published in the GridlabD model.     
- gla.yaml:	Global configuration for the simulation engine and the InfluxDB. 
