A simple agent to run Gridlab-D simulations (under fncs control).
The gla package contains the code of the agent, to be started by the riaps_gla.py script.
The script takes 2 arguments: the model directory and the base name of the model file. 
The sample folder contains an example called APP - these files are needed 
to run the agent. The files have follow the naming convention `(basename + {.glm,.gll,.yaml,})` 
which are the problem-specific files plus a file called gla.yaml for global settings.

The agent launches the simulator and acts as a broker for clients that can 
(1) subscribe to selected messages (that are published by the simulation model)
(2) publish messages that make changes to the simulation model during execution.

An example client is in the script test_client.py -- this is compatible with the loadshed model.

Pre-requisite: the rpyc_registry must be running so that the client(s) can connect to the agent.

For a device implementation compatible with this agent, see the device/GridlabD.py - this needs to be copied
into the app's folder. 

