# Module 2: Coding of the traffic light state machine for the green light

# Setup required dependencies

We will now start managing our project using a `requirements.txt` file. 
This file will contain all the dependencies for our project. As we add more functionality in
subsequent modules, we will add more dependencies to this file.

We will need to install the `python-statemachine` library with the following command:

In the previous module we installed the following dependencies:

* `python3-dev` 
* `RPi.GPIO`

To this we will now add `python-statemachine`

So, our `requirements.txt` file will now look like this:

```
python3-dev
RPi.GPIO
python-statemachine
```

When we create a new virtual environment, we can install all the dependencies in one go with the following command:

`python3 -m pip install -r requirements.txt`

# Setup the virtual environment

To keep things clear, we will be creating a new virtual environment for each module. This will help us keep track of the dependencies 
for each module. This way, we can keep track of how our project grows from module ot module.

Create a new virtual enviornment with the following command:

`python3 -m venv .venv`

Remember to activate the virtual environment with the following command:
`source .venv/bin/activate`

Install the dependencies with the following command:

`python3 -m pip install -r requirements.txt`

We can also choose to save the requirements with 

`python3 -m pip freeze > requirements.txt`

This helps us keep track of the exact versions of the dependencies we are using.  Why would we want to do that?
In order to ensure that we have repeatable builds.  If we don't specify the versions of the dependencies, we might end 
up with different versions of the dependencies when we install them in the future. This can lead to compatibility 
issues and bugs that are hard to track down. By specifying the versions of the dependencies, we can ensure that we 
have a consistent environment for our project.

The flip side of this is that we might end up with outdated dependencies that have security vulnerabilities. So, it's 
important to keep track of the dependencies and update them regularly. We can use tools like 
[dependabot](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide) to 
help automate this process.

Finally, remember to deactivate (but not just yet) the virtual environment when you are done with the following command:
`deactivate`

To make sure everything is working, we can run the `led_tester.py` script from the previous module with the following
command:

`sudo python3 ../module1/led_tester.py GREEN`

We should see the green LED turn on.







