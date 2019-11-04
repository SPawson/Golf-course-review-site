document.addEventListener('DOMContentLoaded', function () {
  //Initialises the mobile nav bar
  var nav = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(nav);

  //Initialises the collapsible text box elements
  var collaps = document.querySelectorAll('.collapsible');
  var instances = M.Collapsible.init(collaps);

  //Initialises the drop down boxes
  var dropDowns = document.querySelectorAll('select');
  var instances = M.FormSelect.init(dropDowns);

});