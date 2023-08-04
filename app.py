from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def home():
	return render_template('index.html')


@app.route('/wine_qualitiy')
def wineQualitiy():
	return render_template('wineQualitiy.html')

@app.route('/air_qualitiy')
def airQualitiy():
	return render_template('airQualitiy.html')

@app.route('/water_qualitiy')
def waterQualitiy():
	return render_template('waterQualitiy.html')

if __name__ == '__main__':
	app.run(debug=True)