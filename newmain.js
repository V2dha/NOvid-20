var firebaseConfig = 
{
	apiKey: "AIzaSyA2tKQpPxQf0vKtXLw2Jn7p6aAaSWOdTHU",
    authDomain: "novid-20.firebaseapp.com",
    databaseURL: "https://novid-20.firebaseio.com",
    projectId: "novid-20",
    storageBucket: "novid-20.appspot.com",
    messagingSenderId: "902516162178",
    appId: "1:902516162178:web:e26e5e90e1d3b2f6d33e9b",
    measurementId: "G-00LEMBQSYV"
};
// Initialization
  firebase.initializeApp(firebaseConfig);

//Collection=Tables or Relations
//Reference to Users table/collection

var UsersRef=firebase.database().ref('Users');
  
document.getElementById('reg').addEventListener('submit', submitForm);
  
//Submit form
function submitForm(e)
{  e.preventDefault();

	//Store submitted values in variables
	var name=getValue('name');
	var username=getValue('username');
	var email=getValue('email');
	var phone=getValue('phone');
	var pass=getValue('pass');
	var location=getValue('location');

  //Pass variable values to database
    saveData(name, username, email, phone, pass, location);

/*  //Display message when done
    document.querySelector('.alert').style.display='block';
  
  //Hide alert after 5 seconds
    setTimeout(function()
    {  document.querySelector('.alert').style.display='none';
    }, 5000); */
}

function getValue(id)
{  return document.getElementById(id).value;
}
  
function saveData(name, username, email, phone, pass, location)
{  var newUserRef = UsersRef.push();
   newUserRef.set(
   {	//Set column values to variable values
	Name: name,
	Username: username,
	Email: email,
	Phone: phone,
	Password: pass,
	Location: location
   });
}
