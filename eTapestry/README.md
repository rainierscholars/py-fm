# eTapestry FileMaker Scripts
This directory contains scripts that integrate FileMaker with eTapestry API

### Machine setup:
1. Follow instructions [here](https://docs.python-guide.org/starting/install3/osx/) to install Python and other required tools (pipenv, etc.).

### Test API connection:
1. Follow instructions [here](https://www.blackbaud.com/support/howto/coveo/etapestry/etapapi.html) to get set up with a 
sandbox or production environment for eTapestry API.
2. You'll get an email with instructions on how to get the database ID and API key. When you get them, save them to
`ETAPESTRY_DATABASE_ID` and `ETAPESTRY_API_KEY` environment variables the machine you'll be running the test script on.
3. Run `pipenv run python test.py`