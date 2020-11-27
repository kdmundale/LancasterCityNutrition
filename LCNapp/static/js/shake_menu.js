const menu_a = document.getElementById('menu_box_a');
const menu_e = document.getElementById('menu_box_e');
const menu_i = document.getElementById('menu_box_i');
const menu_m = document.getElementById('menu_box_m');
const menu_q = document.getElementById('menu_box_q');
const menu_v = document.getElementById('menu_box_v');

const menus = [menu_a, menu_e, menu_i, menu_m, menu_q, menu_v];
const menuL = menus.length;

function menu_display(x){
  console.log("display");
  if (x.style.display=="none") {
    console.log("display!");
    x.style.display = "block";
  } else {
    console.log("display!!");
    x.style.display = "block";
  }
}

function menu_hide(x){
  console.log("hide");
  if (x.style.display == "block"){
    console.log("hide!");
    x.style.display = "none";
  } else {
    console.log("hide!!");
    x.style.display = "none";
  }
}

function view_menu_a(){
  console.log("a");
  for (i=0; i < menuL; i++){
    if (menus[i]== menu_a){
      console.log("a!");
      menu_display(menus[i]);
    } else {
      console.log("a!!");
      menu_hide(menus[i]);
    }
  }
}

function view_menu_e(){
  console.log("e");
  for (i=0; i < menuL; i++){
    if (menus[i]== menu_e){
      console.log("e!");
      menu_display(menus[i]);
    } else {
      console.log("e!!");
      menu_hide(menus[i]);
    }
  }
}

function view_menu_i(){
  for (i=0; i < menuL; i++){
    if (menus[i]== menu_i){
      menu_display(menus[i]);
    } else {
      menu_hide(menus[i]);
    }
  }
}

function view_menu_m(){
  for (i=0; i < menuL; i++){
    if (menus[i]== menu_m){
      menu_display(menus[i]);
    } else {
      menu_hide(menus[i]);
    }
  }
}

function view_menu_q(){
  for (i=0; i < menuL; i++){
    if (menus[i]== menu_q){
      menu_display(menus[i]);
    } else {
      menu_hide(menus[i]);
    }
  }
}

function view_menu_v(){
  for (i=0; i < menuL; i++){
    if (menus[i]== menu_v){
      menu_display(menu_v);
    } else {
      menu_hide(menus[i]);
    }
  }
}

document.getElementById('menu_a_button').addEventListener('click', view_menu_a);
document.getElementById('menu_e_button').addEventListener('click', view_menu_e);
document.getElementById('menu_i_button').addEventListener('click', view_menu_i);
document.getElementById('menu_m_button').addEventListener('click', view_menu_m);
document.getElementById('menu_q_button').addEventListener('click', view_menu_q);
document.getElementById('menu_v_button').addEventListener('click', view_menu_v);
