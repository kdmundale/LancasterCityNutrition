const all_menu = document.getElementById('all_menu');
const had_menu = document.getElementById('had_menu');
const try_menu = document.getElementById('try_menu');

function view_all_menu(){
  if (all_menu.style.display == "none") {
    all_menu.style.display = "block";
  } else {
    all_menu.style.display = "block";
  }
  if (had_menu.style.display == "block"){
    had_menu.style.display = "none";
  } else {
    had_menu.style.display = "none";
  }
  if (try_menu.style.display == "block"){
    try_menu.style.display = "none";
  } else {
    try_menu.style.display = "none"
  }
  console.log("BANGBANG");
}

function view_had_menu(){
  if (all_menu.style.display == "block") {
    all_menu.style.display = "none";
  } else {
    all_menu.style.display = "none";
  }
  if (had_menu.style.display == "none"){
    had_menu.style.display = "block";
  } else {
    had_menu.style.display = "block";
  }
  if (try_menu.style.display == "block"){
    try_menu.style.display = "none";
  } else {
    try_menu.style.display = "none"
  }
  console.log("BANGBANG!!!!!!!");

}

function view_try_menu(){
  if (all_menu.style.display == "block") {
    all_menu.style.display = "none";
  } else {
    all_menu.style.display = "none";
  }
  if (had_menu.style.display == "block"){
    had_menu.style.display = "none";
  } else {
    had_menu.style.display = "none";
  }
  if (try_menu.style.display == "none"){
    try_menu.style.display = "block";
  } else {
    try_menu.style.display = "block"
  }
  console.log("!!!!!!!");

}


document.getElementById('all').addEventListener('click', view_all_menu);
document.getElementById('had').addEventListener('click', view_had_menu);
document.getElementById('try').addEventListener('click', view_try_menu);
