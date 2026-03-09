# Setup

First, we will install pip with the following command:
 
`sudo apt install python3-pip`

Then, we will install python-venv with the following command:

`sudo apt install python3-venv`

Then install the required cross-compilation tools with the following command:

`sudo apt-get install gcc-aarch64-linux-gnu`

Activate the virtual environment with the following command:

`source venv/bin/activate`

Then, we will install the `RPi` library with the following command:

`pip3 install python3-dev RPi.GPIO`