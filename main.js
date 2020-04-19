var firebaseConfig = 
{
    apiKey: "AIzaSyAtQBV3Dcq2YZ_3tm_5OaxGC1lBZgtv7EE",
    authDomain: "hackon-755ba.firebaseapp.com",
    databaseURL: "https://hackon-755ba.firebaseio.com",
    projectId: "hackon-755ba",
    storageBucket: "hackon-755ba.appspot.com",
    messagingSenderId: "197816078794",
    appId: "1:197816078794:web:296fd45866352452073f33",
    measurementId: "G-HKBX8JZKVF"
};

  firebase.initializeApp(firebaseConfig);

var UsersRef=firebase.database().ref('Users');

document.getElementById('reg').addEventListener('submit', submitForm);

//Submit form
function submitForm(e)
{  e.preventDefault();

	var name=getValue('name');
	var id=getValue('id');
	var email=getValue('email');
	var pass=getValue('pass');
	var gender=getValue('gender');
	var age=getValue('age');
	var location=getValue('location');

    saveData(name, id, email, pass, gender, age, location);

    document.querySelector('.alert').style.display='block';

    setTimeout(function()
    {  document.querySelector('.alert').style.display='none';
    }, 5000);
}

function getValue(id)
{  return document.getElementById(id).value;
}

function saveData(name, id, email, pass, gender, age, location)
{  var newUserRef = UsersRef.push();
   newUserRef.set(
   {
	Name: name,
	Username: id,
	Email: email,
	Password: pass,
	Gender: gender,
	Age: age,
	Location: location
   });
}
