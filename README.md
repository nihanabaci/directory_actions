# EndpointInterview

## Hierarchical File System

The Hierarchical File System is an application that allows users to manage directories in a hierarchical structure.

## Features

- Create directories
- Move directories to different locations
- Delete directories
- List directories and their hierarchical structure

### Prerequisites

- Python 3.x

## How to clone the application

- Run ```git clone git@github.com:nihanabaci/directory_actions.git```

### How to run the application


Note: this application takes in the input given in the instructions as an array of strings

- Go inside directory_actions folder
- Run ```pip install -e .``` to execute code in ```setup.py``` to help find all relevant packages
- Run ```python main.py```


### How to run the tests

- Go inside directory_actions folder
- Run ```python tst/test_directory.py```
- Run ```python tst/test_filesystem.py```
- Run ```python tst/test_main.py```

### How to change the input

If you just want to change the input and see the printed output
- Go to ```main.py```
- Edit the ```commands``` variable to desired input
- Follow the steps for ```How to run the application```

If you want to change the input and test it against a desired output
- Go to ```tst/test_main.py```
- Inside ```test_process_commands``` function, you can change the ```commands```variable for the desired input and the ```expected_output``` variable for the desired output
- Follow the steps for ```How to run the tests```

### Debugging potential errors

If received ```ModuleNotFoundError```

- Go inside directory_actions folder
- Run ```pip install -e .``` to execute code in ```setup.py``` to help find all relevant packages
- Repeat the ```How to run the application``` or ```How to run the tests``` steps
