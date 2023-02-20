from flask import Flask, request, jsonify, render_template
import func
import os

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/api/get_brands')
def get_brands():
    response = jsonify({
        'brands': func.get_brands()
    })
    return response


@app.route(f'/api/prediction', methods=['GET', 'POST'])
def get_prediction():
    brand = request.form['brand']
    prod_year = int(request.form['prod_year'])
    engine = request.form['engine']
    transmission = int(request.form['transmission'])
    engine_cap = float(request.form['engine_cap'])

    print('===============================')
    print('Data to prediction:')
    print(brand, prod_year, engine, transmission, engine_cap)
    print('===============================')

    prediction = jsonify({
        'prediction': func.get_prediction(brand, prod_year, engine, transmission, engine_cap)
    })

    return prediction


if __name__ == '__main__':
    func.load_saved_components()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
