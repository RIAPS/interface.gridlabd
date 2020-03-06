Example files for a typical GLA configuration.
==============================================

These are meant as illustration (although they are from a working example).
APP is the name of application - should be replaced by an appropriate name.

- APP.glm:	A valid GridlabD model file. Must have the fncs_msg object that declares
 			the published/subscribed data points.
- APP.gll:	List of the data points to be recorded in the InfluxDB server.
			The list contains lists of the form:
            [ object, attribute, unit ]
            where the names must match the names in the GridlabD model. 
- APP.yaml:	Configuration file for the fncs/broker (per fncs documentation). 
 			broker: host and port the fncs broker is running on
 			name: application name 
 			time_delta: internale time step for the broker
 			values: message label/topic pairs for all values to be published. Must match the GridlabD model.     
- gla.yaml:	Global configuration of the agent for the simulation engine and the InfluxDB. 
			dbhost:     IP address of the Influxdb server
			dbport:     Port of the InflixDB server 
			dbdrop:     True if the database tables are to be cleared upon stopping the agent. 
			time_pace:  Wall clock time delay between two steps of the sim (in sec)
			time_stop:  Maximum simulation time (in sec)
			time_base:  Lofical start time of the simulation or  'now' (for current time). 
			dbname:     Name of InfluxDB database the logs go to. 
			dbuser:		User name for database
			dbpasswd:	Password for database