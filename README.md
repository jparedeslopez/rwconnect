# rwconnect


## Requirements
* Appium (https://github.com/appium/appium-desktop/releases/tag/v1.13.0)
* Python 3.6+ (virtualenv python=python3.6)


## Setup
* Install dependencies from requirements.txt:  
    <code>pip install -r requirements.txt</code>
* Install Appium from the above link.


## Run 
* Open XCode and Compile the app for a simulator.
* After installation, run the app and accept or deny access to Contacts.
* Modify the following fields on tests/configs/ios.config file desired capabilitites: "udid", "deviceName" and "platformVersion"
* Run unittest tests (go to test_auto folder) 
    * Start Appium server   
    * Activate venv  
    * Run <code>python test_runner.py</code>