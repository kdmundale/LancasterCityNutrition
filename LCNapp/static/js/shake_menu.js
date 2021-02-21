const menu_1 = document.getElementById('menu_box_a');
const menu_2 = document.getElementById('menu_box_e');
const menu_3 = document.getElementById('menu_box_i');
const menu_4 = document.getElementById('menu_box_m');
const menu_5 = document.getElementById('menu_box_q');
const menu_6 = document.getElementById('menu_box_v');

const menus = [menu_1, menu_2, menu_3, menu_4, menu_5, menu_6];
const menuL = menus.length;

function menu_display(x){
  if (x.style.display=="none") {
    x.style.display = "block";
  } else {
    x.style.display = "block";
  }
}

function menu_hide(x){
  if (x.style.display == "block"){
    x.style.display = "none";
  } else {
    x.style.display = "none";
  }
}

function view_menu(menu){
  for (i=0; i < menuL; i++){
    if (menus[i]== menu){
      menu_display(menu);
    } else {
      menu_hide(menus[i]);
    }
  }
}



document.getElementById('menu_a_button').addEventListener('click', function(){ view_menu(menu_1);});
document.getElementById('menu_e_button').addEventListener('click', function(){ view_menu(menu_2);});
document.getElementById('menu_i_button').addEventListener('click', function(){ view_menu(menu_3);});
document.getElementById('menu_m_button').addEventListener('click', function(){ view_menu(menu_4);});
document.getElementById('menu_q_button').addEventListener('click', function(){ view_menu(menu_5);});
document.getElementById('menu_v_button').addEventListener('click', function(){ view_menu(menu_6);});
