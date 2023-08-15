from flask import Flask, render_template, request
import pickle
import numpy as np


# Load the Random Forest CLassifier model
wine_model_name = 'artifacts/wine_qualitiy_model.pkl'
air_model_name = 'artifacts/air_qualitiy_model.pkl'
water_model_name = 'artifacts/water_potability_model.pkl'

wine_predict = pickle.load(open(wine_model_name, 'rb'))
air_predict = pickle.load(open(air_model_name, 'rb'))
water_predict = pickle.load(open(water_model_name, 'rb'))

app = Flask(__name__)



@app.route('/')
def home():
	return render_template('index.html')


@app.route('/wineQualitiy',methods=['POST','GET'])
def wineQualitiy():
	if request.method == 'GET':
		return render_template('wineQualitiy.html')
	else:
		if request.method == 'POST':
			fixed_acidity=float(request.form['fixed_acidity'])
			volatile_acidity=float(request.form['volatile_acidity'])
			citric_acid=float(request.form['citric_acid'])
			residual_sugar=float(request.form['residual_sugar'])
			chlorides=float(request.form['chlorides'])
			free_sulphur_dioxide=float(request.form['free_sulphur_dioxide'])
			total_sulphur_dioxide=float(request.form['total_sulphur_dioxide'])
			density=float(request.form['density'])
			ph=float(request.form['ph'])
			sulphates=float(request.form['sulphates'])
			alcohol=float(request.form['alcohol'])

			data=np.array([[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,
                        chlorides,free_sulphur_dioxide,
                        total_sulphur_dioxide,density,ph,sulphates,alcohol]])
			
			prediction=wine_predict.predict(data)[0]

			print(prediction)         
			return render_template('wineResult.html', prediction=prediction)

@app.route('/airQualitiy',methods=['POST','GET'])
def airQualitiy():
	if request.method == 'GET':
		return render_template('airQualitiy.html')
	else:
		if request.method == 'POST':
			SOi=float(request.form['SOi'])
			Noi=float(request.form['Noi'])
			Rpi=float(request.form['Rpi'])
			SPMi=float(request.form['SPMi'])

			data=np.array([[SOi,Noi,Rpi,SPMi]])
			prediction=air_predict.predict(data)[0]
			print(prediction)         
			return render_template('airResult.html', prediction=prediction)

@app.route('/waterQualitiy',methods=['POST','GET'])
def waterQualitiy():
	if request.method == 'GET':
		return render_template('waterQualitiy.html')
	else:
		if request.method == 'POST':
			ph=float(request.form['ph'])
			Hardness=float(request.form['Hardness'])
			Solids=float(request.form['Solids'])
			Chloramines=float(request.form['Chloramines'])
			Sulfate=float(request.form['Sulfate'])
			Conductivity=float(request.form['Conductivity'])
			Organic_carbon=float(request.form['Organic_carbon'])
			Trihalomethanes=float(request.form['Trihalomethanes'])
			Turbidity=float(request.form['Turbidity'])

			data=np.array([[ph,Hardness,Solids,Chloramines,
                        Sulfate,Conductivity,
                        Organic_carbon,Trihalomethanes,Turbidity]])
			prediction=water_predict.predict(data)[0]
			print(prediction)

			return render_template('waterResult.html', prediction=prediction)

if __name__ == '__main__':
	app.run(debug=True)