# NetEngine - Hack The Planet Educator Edition

NetEngine is terminal emulator game engine designed to allow students to explore some of the basic principles of network based reconnaissance tools, Linux and possibly foriegn language studies.

The premise is that the engine is completely dynamic and configurable by an editable configuration soure so that different scenarios, tools, users, and network configurations can be created to allow for different learning objectives or critical analysis or even possibly assessment.

### Installation:
`git clone https://github.com/jaywon/net-engine.git`

### Usage:
`python netengine.py`

Enter available commands to explore the given configurable environment and determine next steps in an objective to gain root on any machine on the network.

(NOTE: Demo has no implementation for configuring or gaining root, conceptual engine prototype only)

#### Available Commands:
- `man` - Show the man page for a given tool
- `tools` - Show the list of tools available on a machine
- `ifconfig` - Show the network interface configuration on a machine
- `users` - Show the users on a system
- `history` - Show history of a user on a system
- `language` - Set the language currently in use
- `exit` - Exit the game

### Configurable Addons:
- `nc` - TBD
- `ssh` - Access another server on the network
- `nmap` - Show other servers on the network
- `wireshark` - TBD

Problems solved:
- Real-world labs are timely and have liablity scenarios for teaching real-world skills
- Existing man pages can be dense for beginning learners
- Provisioning or working within existing educational infrastructure is challenging, only needs Python installed
- Tools with a one path scenario provide limited usage and implementation
- ESL students may get left behind in the details of self-learning
- Students teaching may have high level knowledge of technology but not time, knowledge, or resources for actual network configuration

Features:
- Configurable network and per operating system scenarios
- Multi-lingual documentation and gameplay suppor
- Easy firewall configuration
- Easy network configuration
- Easy user/group configuration
- Configurable documentation for tools

Contribution:
A million things could/would/should be done, looking for ideas and supporters.

Fork and pull request bruh...
