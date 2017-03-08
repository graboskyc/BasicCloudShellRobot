# BasicCloudShellRobot
This is a repository with a proof-of-concept easy implementation of calling Robot Tests (Python Robot Framework) from Quali CloudShell SnQ

# Setup
* Deploy a linux VM (Ubuntu)
* In CloudShell, Add a new Custom Execution Server Type of `Robot` (Job Scheduler -> Edit Execution Server Types -> Add)
* On that VM, start the docker container based on the Dockerfile 
* Note that you may need to modify the config.json... I'm working on that
* Create a Blueprint with a single resource with the resource script HelloWorld.py attached
* Create a job suite for Robot using the above blueprint. Valid tests should be as follows:

![](Images/SnQSS.PNG)

# Deploying docker container
## From source
* `docker build -t gskyqsrobot`
* `docker run -t -i -d -p 2222:22 --name qsrobot gskyqsrobot `

## From Dockerhub
* `docker run -t -i -d -p 2222:22 --name qsrobot graboskyc/qualicsrobot `
