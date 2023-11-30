import flask
import pickle 
import pandas as pd 
import os


# Get directory 
script_dir = os.path.dirname(os.path.abspath(__file__))
# Use pickle to load in trained model 
model_path = os.path.join(script_dir, 'random_forest_model.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Initialise the Flask app 
app = flask.Flask(__name__, template_folder='templates')

# Setting up the main route 
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET': 
        return(flask.render_template('index.html'))
    
    if flask.request.method == 'POST':
        bedrooms = float(flask.request.form['bedrooms'])
        bathrooms = float(flask.request.form['bathrooms'])
        sqft_living = float(flask.request.form['sqft_living'])

        input_variables = pd.DataFrame([[bedrooms,bathrooms, sqft_living]],
                                       columns=['bedrooms', 'bathrooms', 'sqft_living'],
                                       dtype=float,
                                       index=['input'])
        
        prediction = model.predict(input_variables)[0]

        return flask.render_template('index.html',
                                     original_input = {'Bedroom(s)': bedrooms,
                                                       'Bathroom(s)': bathrooms,
                                                        'SQFT Living': sqft_living},
                                                        result=prediction
                                                        )
if __name__ == '__main__':
    app.run(debug=True)
                                                        
    