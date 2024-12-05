import pytest
import os
import data
import Configfile
import configparser
from Logger import logger as log

def pytest_addoption(parser):
    parser.addoption("--env_local", action="store", default="pr")
    parser.addoption("--trunner", action="store", default="local") 
    # ----toma el valor por defecto a menos que se lo indique por consola

def pytest_configure(config):
    os.environ["env_aux"] = config.getoption("env_local")
    os.environ["trunner"] = config.getoption("trunner")

def load_config(f):
    config = configparser.ConfigParser()
    config.read(f)
    return config

def env_session():
    trunner = os.environ["trunner"]
    if trunner == 'jenkins':
        environment = os.environ["env"]
        print("**** ENVIRONMENT: " + environment + " ****") 
        print ("***** Ejecucion desde JENKINS *****")
        config = load_config(Configfile.CONFIGFILE_JENKINS)
        
    else:
        environment = os.environ["env_aux"]
        print("**** ENVIRONMENT: " + environment + " ****") 
        print ("***** Ejecucion desde LOCAL *****")
        config = load_config(Configfile.CONFIGFILE_LOCAL)
    path = config.get(environment, "path")    
    print ("URL: ", path)
    return path


@pytest.fixture(scope="session")
def generate_token():
    url = env_session()
    # Here the idea is to do a request to the identy to get a non hardcoded token
    token = [data.TOKEN, data.INVALID_TOKEN]
    return token, url 




    
    