# Troubleshooting openVulnQuery Installation Issues #

This page is dedicated to resolving common installation issue encountered during installation of openVulnQuery.

#### Mac OS X/ Linux ####
- ##### Permission Denied on installation as mentioned in https://communities.cisco.com/thread/71785 ######

	While installing a Python package, It is recommended to do so in python virtual environment. This keeps all the dependencies seperate
			from global site-packages. `virtualenv` is a tool to create this isolated python environment.
			
    ```sh
    $ pip install virtualenv
    ```
    Now, go to your project folder

    ```sh
    $ cd project_folder
    $ virtualenv venv
    ```
    Here venv is name of your virtual environment
	To activate the virtual environment
	```sh 
	$ source venv/bin/activate
	```
 
	you will see (venv) added on your terminal. 
	This means your virtual environment is active and 
	whatever you install using pip will be contained in that virtual environment     without being installed into your local machine.
	

	```sh
	$ pip install openVulnQuery
	```
	
	You can find more information in this [guide to python page](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
		
		
