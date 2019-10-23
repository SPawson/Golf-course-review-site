
document.addEventListener('DOMContentLoaded', function() {
    //Initialises the collapsible text box elements
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems);

    //Initialises the drop down boxes
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
  });