![GitHub Repo stars](https://img.shields.io/github/stars/v2dha/NOvid-20?color=orange)
![GitHub forks](https://img.shields.io/github/forks/v2dha/NOvid-20?color=yellow)
![GitHub contributors](https://img.shields.io/github/contributors/v2dha/NOvid-20)
![GitHub issues](https://img.shields.io/github/issues/v2dha/NOVid-20?color=brown) 
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/v2dha/NOvid-20?color=blue)
![GitHub pull requests](https://img.shields.io/github/issues-pr/v2dha/NOvid-20?color=orange)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/v2dha/NOvid-20)
![APM](https://img.shields.io/apm/l/vim-mode)


<p align="center">
  <img src="https://i.ibb.co/m49w93y/Logo2.jpg" width="350" alt="logo" />
  <h1 align="center">NOvid-20</h1>
  <p align="center">
  One solution to all Covid-19 Queries
  <br/>
  An online doctor and a health assistant, whenever and wherever you need
  <br />
  A solution to foretell the likelihood of being in vicinity of COVID-19 using ML and AI
  <br />
  <br />
  </p>
</p>
<hr>



# Features
* **COVID-19 Predictor** - The predictor model based on machine learning approach analyzes the likelihood of the disease based on various factors.

* **COVID-19 Detector** - With the help of COVID-19 Detector, you can upload your Chest X-Ray image and get a prior prediction of whether you are COVID-19 positive, negative or it's a case of Pneumonia.

* **Chatbot** - An AI assistant will resolve all your queries related to the disease and provide implementable solutions to them.

* **Current situation Overview** - Latest updates and overview of the on-going situation to help you keep track of it.

# Demo
<img src="demo/demo.gif">

# Tech Stack
* For [COVID-19 Predictor](https://github.com/V2dha/NOvid-20/tree/master/server/covid19-predictor), Ensemble Machine Learning classifier was used to classify the symptoms and factors entered by the user. The accuracy achieved by the model is 98.2% using Random Forest. 
* For [COVID-19 Detector](https://github.com/V2dha/NOvid-20/tree/master/server/covid19-detector), Convolutional Neural Networks were used to detect the COVID-19 using Chest X-Ray images with an accuracy of 95%. 
* For both deployment of Predictor and Detector, Flask was used for backend deployment on heroku.
* Main website is a static website hosted using Github Pages with the frontend built using Bootstrap template.
* Chatbot is powered by SnatchBot.

# Contributing

NOvid-20 is fully Open-Source and open for contributions! We request you to respect our contribution guidelines as defined in our [CODE OF CONDUCT](https://github.com/V2dha/NOvid-20/blob/master/CODE_OF_CONDUCT.md) and [CONTRIBUTING GUIDELINES](https://github.com/V2dha/NOvid-20/blob/master/CONTRIBUTING.md). 

# Contributors 

<a href="https://github.com/V2dha/NOvid-20/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=V2dha/NOvid-20" />
</a>
