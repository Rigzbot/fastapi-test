# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 10:16:58 2022

@author: rishi
"""

# Library imports
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import pickle

# Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello!'}

# Route with a single parameter
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome to Api!': f'{name}'}

#Expose the prediction functionality
@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        'prediction': prediction
    }
    

# Run the api with uvicorn
# Will run on 127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload