const all_user = document.getElementById('all_user');
const most_logins = document.getElementById('most_logins');
const most_shakes = document.getElementById('most_shakes');
const member_phone = document.getElementById('member_phone');

tables= [all_user,most_logins,most_shakes,member_phone];
tableL = tables.length;

function table_display(x){
  if (x.style.display=="none") {
    x.style.display = "block";
  } else {
    x.style.display = "block";
  }
}

function table_hide(x){
  if (x.style.display == "block"){
    x.style.display = "none";
  } else {
    x.style.display = "none";
  }
}

function view_most_logins(){
  for (i=0; i < tableL; i++){
    if (tables[i]== most_logins){
      table_display(tables[i]);
    } else {
      table_hide(tables[i]);
    }
  }
}

function view_all_user(){
  for (i=0; i < tableL; i++){
    if (tables[i]== all_user){
      table_display(tables[i]);
    } else {
      table_hide(tables[i]);
    }
  }
}

function view_most_shakes(){
  for (i=0; i < tableL; i++){
    if (tables[i]== most_shakes){
      table_display(tables[i]);
    } else {
      table_hide(tables[i]);
    }
  }
}

function view_member_phone(){
  for (i=0; i < tableL; i++){
    if (tables[i]== member_phone){
      table_display(tables[i]);
    } else {
      table_hide(tables[i]);
    }
  }
}

document.getElementById('all_user_button').addEventListener('click', view_all_user);
document.getElementById('most_logins_button').addEventListener('click', view_most_logins);
document.getElementById('most_shakes_button').addEventListener('click', view_most_shakes);
document.getElementById('member_phone_button').addEventListener('click', view_member_phone);
