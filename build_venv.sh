# To build a virtual environment for the project we will use pyenv and pyenv-virtualenv

# check if pyenv is installed
if ! command -v pyenv &> /dev/null
then
    echo "pyenv could not be found"
    exit
fi

# check if python version == 3.11.8 is installed if no install it
if ! pyenv versions | grep -q 3.11.8
then
    pyenv install 3.11.8
fi

# set the local python version to 3.11.8
pyenv local 3.11.8

# create a virtual environment in this project folder with the name "venv"
python -m venv venv

## activate the virtual environment
source venv/bin/activate

# upgrade pip
pip install --upgrade pip

# install the requirements
pip install -r requirements.txt
