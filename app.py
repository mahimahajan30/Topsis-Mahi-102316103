from flask import Flask, request
from topsis import calculate_topsis

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        weights = request.form['weights']
        impacts = request.form['impacts']

        file.save("input.csv")

        calculate_topsis("input.csv", weights, impacts, "output.csv")

        return "✅ Result generated! Check output.csv"

    return '''
    <h2>TOPSIS Calculator</h2>
    <form method="post" enctype="multipart/form-data">
        Upload CSV: <input type="file" name="file"><br><br>
        Weights: <input type="text" name="weights"><br><br>
        Impacts: <input type="text" name="impacts"><br><br>
        <input type="submit">
    </form>
    '''
    
app.run()
