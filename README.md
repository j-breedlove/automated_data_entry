
# Zillow Property Scraper and Form Filler

This project scrapes property listings from Zillow using BeautifulSoup and then automatically fills out a Google Form using Selenium.

## Installation

### Using pipenv (Recommended)

1. Clone the repository:
```
git clone [YOUR REPOSITORY LINK]
cd [YOUR REPOSITORY DIRECTORY]
```

2. Initialize and activate the virtual environment with `pipenv`:
```
pipenv --three
pipenv shell
```

3. Install the required packages:
```
pipenv install selenium==3.141.0 urllib3==1.26.5 requests webdriver_manager python-dotenv
```

### Manual Installation

1. Clone the repository:
```
git clone [YOUR REPOSITORY LINK]
cd [YOUR REPOSITORY DIRECTORY]
```

2. Install the required packages:
```
pip install selenium==3.141.0 urllib3==1.26.5 requests webdriver_manager python-dotenv
```

## Configuration

1. Create a `.env` file in the root directory.
2. Add the following environment variables:
```
FORM_LINK=[YOUR GOOGLE FORM LINK]
GOOGLE_USERNAME=[YOUR GOOGLE USERNAME]
GOOGLE_PASSWORD=[YOUR GOOGLE PASSWORD]
```

## Running the Script

To execute the script, simply run:
```
python main.py
```

## Troubleshooting

### AttributeError related to 'capabilities'

If you encounter an error related to 'capabilities', consider downgrading your Selenium version:
```
pipenv install selenium==3.141.0
```

### Timeout Value Error with urllib3

If you receive a timeout-related error with `urllib3`, ensure you're using version `1.26.5`:
```
pipenv install urllib3==1.26.5
```

### Compatibility with Python 3.11

This project was developed and tested primarily with Python versions 3.9 and 3.10. If you're using Python 3.11, some packages might not yet be fully compatible. Consider switching to an older Python version if you encounter persistent issues.
