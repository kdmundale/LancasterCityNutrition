const login_button = document.getElementById("login_button");
const login_window = document.getElementById("home-login-window");
const home_menu = document.getElementById("home_menu_button");
const drpdn_menu = document.getElementById("home-d");

function view_login_window(){

  if (login_window.style.display == ""){
    login_window.style.display = "block";
  } else if (login_window.style.display == "block") {
    login_window.style.display = "";
  }

}

function dropdown (){
  if (drpdn_menu.style.display == ""){
    drpdn_menu.style.display="flex";
  } else if (drpdn_menu.style.display == "flex") {
    drpdn_menu.style.display = "";
  }
}

document.getElementById("login_button").addEventListener('click', view_login_window);
home_menu.addEventListener('click', dropdown);
