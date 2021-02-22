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
        breathingProblem = int(myDict["breathingProblem"])
        fever = int(myDict["fever"])
        dryCough = int(myDict["dryCough"])
        soreThroat = int(myDict["soreThroat"])
        runningNose = int(myDict["runningNose"])
        asthma = int(myDict["asthma"])
        lungDisease = int(myDict["lungDisease"])
        headache = int(myDict["headache"])
        heartDisease = int(myDict["heartDisease"])
        diabetes = int(myDict["diabetes"])
        hypertension = int(myDict["hypertension"])
        fatigue = int(myDict["fatigue"])
        gastrointestinal = int(myDict["gastrointestinal"])
        abroadTravel = int(myDict["abroadTravel"])
        covidContact = int(myDict["covidContact"])
        gathered = int(myDict["gathered"])
        visitPublic = int(myDict["visitPublic"])
        familyPublic = int(myDict["familyPublic"])
        wearingMask = int(myDict["wearingMask"])
        sanitization = int(myDict["sanitization"])
        # Code for inference
        inputFeatures = [breathingProblem, fever, dryCough, soreThroat, runningNose, asthma, lungDisease, headache, heartDisease, diabetes, hypertension, fatigue, gastrointestinal, abroadTravel, covidContact, gathered, visitPublic, familyPublic, wearingMask, sanitization]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        print(infProb)
    
        return render_template('show.html' , inf=round(infProb*100))
    else:
        return render_template('index.html')

@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)