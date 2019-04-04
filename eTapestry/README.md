# eTapestry FileMaker Scripts
This directory contains scripts that integrate FileMaker with eTapestry API

### Machine setup:
1. Install Python and :
    - [Mac](https://docs.python-guide.org/starting/install3/osx/)
    - [Windows]https://docs.python-guide.org/starting/install3/win/)
2. Install [VS Code](https://code.visualstudio.com/).
3. Update `python.pythonpath` in `/vscode/settings.json` with the result from running `pipenv --py` command.

### Test API connection:
1. Follow instructions [here](https://www.blackbaud.com/support/howto/coveo/etapestry/etapapi.html) to get set up with a 
sandbox or production environment for eTapestry API.
2. You'll get an email with instructions on how to get the database ID and API key. When you get them, save them to
`ETAPESTRY_DATABASE_ID` and `ETAPESTRY_API_KEY` environment variables the machine you'll be running the test script on.
3. Run `pipenv run python eTapestry/test_api.py`

### Test FileMaker ODBC connection:
1. Install FileMaker ODBC driver from [here](https://support.filemaker.com/s/answerview?language=en_US&anum=12921).
2. Install ODBC Mananger from [here](http://www.odbcmanager.net/).
3. Follow the steps [here](https://community.filemaker.com/thread/180817#comment-717424) to set up and verify the ODBC connection.
4. Update `eTapestry/test_odbc.py` with your local FileMaker configuration. This is a test so you can have use any table you have in FileMaker.
5. Run `pipenv run python eTapestry/test_api.py`