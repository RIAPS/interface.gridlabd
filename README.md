RIAPS Gridlab-D Interface Agent
===============================

A simple agent to run Gridlab-D simulations (under fncs control), such that RIAPS
apps running can get sensor data from it and interact with the running simulation.

The gla package contains the code of the agent, to be started by the riaps_gla.py script.

The script takes 2 arguments: the model directory and the base name of the model file. 

The sample folder contains an example called APP - these files are needed to run the agent. 
The files have follow the naming convention `(basename + {.glm,.gll,.yaml,})` 
that are the problem-specific files plus a file called gla.yaml for global settings.
For details see sample/README.md

The agent immediately launches the simulator and acts as a broker for clients that can 
(1) subscribe to selected messages (that are published by the simulation model)
(2) publish messages that make changes to the simulation model during execution.

To start:

Pre-requisite: the rpyc_registry must be running so that the client(s) can connect to the agent.

To start the agent (in this directory)
```
   python3 riaps_gla.py sample APP
```

An example client is in the script test_client.py -- this is compatible with the loadshed model (in sample/APP.gml)

For a device implementation compatible with this agent, see the device/GridlabD.py, and the 
docstring at the top of the file. This module needs to be placed in the RIAPS apps' folder. 

For installation please follow the instructions in INSTALL.md

