# Fish Species Prediction ML

This Repository contains a jupyter notebook file which shows the creation and training of a logistic regression model, the [fish-market dataset](https://www.kaggle.com/aungpyaeap/fish-market) used and the flask front-end.

## How to use

* You can import the .ipnyb notebook in jupyter notebook, google colabs or any compatible platform to execute the cells within it.
* You can use any ide (e.g. pycharm) to open the flask app and use cmd to run the application.

NOTE: set the application to FlaskApp.py before running the flask app. using the following lines in windows cmd:
```
set FLASK_APP=FlaskApp
flask run
```
(use the stack overflow answer as reference to run the flask app. [Link](https://stackoverflow.com/a/57400523/6795246) )

## Tools used
* Python 3.7 (Language used)
* Flask (To create a web application)
* scikit-learn (For logistic regression model)
* html/css (for basic front-end page)

## Testing

The flask app has been hosted on Heroku and is ready for testing. Click the [link](https://fish-species-prediction-ml.herokuapp.com/) to test the app hosted on Heroku
