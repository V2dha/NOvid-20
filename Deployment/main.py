from flask import Flask, render_template, request
app = Flask(__name__)
import pickle


# open a file, where you stored the pickled data
file = open('model.pkl' , 'rb')
clf = pickle.load(file)
file.close()

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        fever = float(myDict["fever"])
        age = int(myDict["age"])
        pain = int(myDict["pain"])
        runnyNose = int(myDict["runnyNose"])
        diffBreath = int(myDict["diffBreath"])
        # Code for inference
        inputFeatures = [fever, pain, age, runnyNose, diffBreath]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        print(infProb)
    
        return render_template('show.html' , inf=round(infProb*100))
    return render_template('index.html')

@app.route("/about_us")
def about_us():
    return render_template('index1.html')

if __name__ == "__main__":
    app.run(debug=True)