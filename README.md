# Data analysis
OpenFoodFactsCategorizer

Description:
Open Food Facts is a food products database "made by everyone, for everyone".
This organisation uses an OCR (Optical Caracter Recognition) system to extract from a photograph the text of a package's list of ingredients.
The aim of this project was to automatically associate to each ingredient list (retrieved by OCR) a product category.


Data Source: Open Food Facts CSV of 800.000 products.

Type of analysis:
- Data Analysis to identify 37 categories of products and their occurences.
- Search for the best Machine Learning model to classify products automaticaly
- Test for Deep Learning scores

This project focus on french products. The model had been trained on french texts from OCR.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for OpenFoodFacts in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/OpenFoodFacts`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "OpenFoodFacts"
git remote add origin git@github.com:{group}/OpenFoodFacts.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
OpenFoodFacts-run
```

# Install

Go to `https://github.com/{group}/OpenFoodFacts` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/OpenFoodFacts.git
cd OpenFoodFacts
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
OpenFoodFacts-run
```

# OCR test

To test our categorizer with new data we have implemented an OCR system.
Please, find the setup in the notebooks folder (OCR_setup.ipynb).

Two OCR system were tested: tesseract and easyocr.

To understand how to custom parameters of teserract see:
https://pypi.org/project/pytesseract/
https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc#config-files-and-augmenting-with-user-data

Easy OCR doesn't need custom config:
https://pypi.org/project/easyocr/


If you wish to use those OCR in production:
- easyocr is very easy to use as it's name suggests, but it's also very heavy and may be to big for plateforms like Heroku (It may exceed
  the slug size).

- To use tesseract in production you will have to change the path.
  For example, our path was pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract' for a local usage and pytesseract.pytesseract.tesseract_cmd = ‘/app/.apt/usr/bin/tesseract’ in production
  To know more see: https://towardsdatascience.com/deploy-python-tesseract-ocr-on-heroku-bbcc39391a8d




