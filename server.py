from flask import Flask,jsonify,request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/')
def entry():
    return "this server is running for Monthly electricity bill prediction"

@app.route('/getBill',methods=['POST'])
def getBill():
    if request.method == 'POST' :
        data = request.get_json()
        print(data)

        for i in data :
            data[i] = int(data[i])

        input_data = [[data['num_rooms'],data['num_people'],data['housearea'],data['is_ac'],data['is_tv'],data['is_flat'],data['ave_monthly_income'],data['num_children'],data['is_urban']]]
        
        expected_output = model1.predict(input_data)
        return str(abs(expected_output))
    else:
        return "invlalid request"







# calculation of expected electricity bill
import numpy as np
import pandas as pd
from sklearn import datasets

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

data_set = datasets.fetch_openml('Household-monthly-electricity-bill')

data = pd.DataFrame(data_set.data)
data = data.values
training_input = data[:800,:9]
training_output = data[:800,9:10]
training_output = training_output.reshape(800)

testing_input = data[800:,:9]
testing_output = data[800:,9:10]
testing_output = testing_output.reshape(200)
# print(data_set.data['amount_paid'])
# print(training_input[0])



model1 = LinearRegression()

model1.fit(training_input,training_output)

num_rooms = 0
num_people= 0
housearea=0
is_ac=0
is_tv=0
is_flat=0
ave_monthly_income=0
num_children=0
is_urban=0
amount_paid=0

# input_data = [[num_rooms,num_people,housearea,is_ac,is_tv,is_flat,ave_monthly_income,num_children,is_urban]]


# expected_output = model1.predict(input_data)      

# print(expected_output)

# testing_input = [[],[],[]]
# array = ['num_rooms','num_people','housearea','is_ac','is_tv','is_flat','ave_monthy_income','num_children','is_urban','amount_paid']




if __name__ == '__main__' :
    app.run(debug=False,host='0.0.0.0')
