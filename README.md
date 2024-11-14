# Zoo Simulator Task

This project simulates a zoo environment with the three animals: monkeys, giraffes, and elephants. The simulation supports health management, feeding, and passing time. This guide will help you set up the project locally on a Windows machine.

## Prerequisites

- Python

- pip

- pytest (for running tests)

## Setup Instructions

### Set Up a Virtual Environment

1. Create the Virtual Environment:

```
python -m venv venv
```

2. Activate the Virtual Environment:

```
venv\Scripts\activate
```

3. Install Pytest

```
pip install pytest
```

### Running the Project

1. Running the Application
   Go into the 'src' folder through the terminal and run the application using:

```
python main.py
```

2. Running the Tests
   Run the tests from the parent folder - not the src folder:

```
pytest
```

### Troubleshooting

- If tests are showing as errors then please re-run pytest. The main.py uses random integers so there can be issues passing test.

- If pytest is not recognised, ensure the virtual environment is activated.

- If you continue having issues with pytest then check if you are in the root folder and re-run. Also the conftest.py file and configure it to suit your machine.

- If Python is not found, check that Python is added to your system’s PATH variable.
