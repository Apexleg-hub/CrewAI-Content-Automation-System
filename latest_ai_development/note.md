uv pip install crewai



1. Installation
Ensure you have Python >=3.10 <3.14 installed on your system. CrewAI uses UV for dependency management and package handling, offering a seamless setup and execution experience.

First, install CrewAI:

uv pip install crewai

If you want to install the 'crewai' package along with its optional features that include additional tools for agents, you can do so by using the following command:

uv pip install 'crewai[tools]'

________________________________
uv tool install crewai

________________________________
The command above installs the basic package and also adds extra components which require more dependencies to function.

###################################3

Troubleshooting Dependencies
If you encounter issues during installation or usage, here are some common solutions:

Common Issues
ModuleNotFoundError: No module named 'tiktoken'

Install tiktoken explicitly: uv pip install 'crewai[embeddings]'
If using embedchain or other tools: uv pip install 'crewai[tools]'
Failed building wheel for tiktoken

Ensure Rust compiler is installed (see installation steps above)
For Windows: Verify Visual C++ Build Tools are installed
Try upgrading pip: uv pip install --upgrade pip
If issues persist, use a pre-built wheel: uv pip install tiktoken --prefer-binary



################

You can now start developing your crew by editing the files in the src/my_project folder. The main.py file is the entry point of the project, the crew.py file is where you define your crew, the agents.yaml file is where you define your agents, and the tasks.yaml file is where you define your tasks.

To customize your project, you can:
Modify src/my_project/config/agents.yaml to define your agents.
Modify src/my_project/config/tasks.yaml to define your tasks.
Modify src/my_project/crew.py to add your own logic, tools, and specific arguments.
Modify src/my_project/main.py to add custom inputs for your agents and tasks.
Add your environment variables into the .env file.

