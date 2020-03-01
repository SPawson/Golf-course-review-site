
document.addEventListener('DOMContentLoaded', function() {
  //Initialises the mobile nav bar
  var nav = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(nav);

  //parallax initialisation
  $('.parallax').parallax();


  //Initialises index image carousel
  let options = {
    //fullWidth: true,
    height:500,
    indicators: false,
    interval: 6000
  }

  var element = document.querySelectorAll('.slider');
  var instances = M.Slider.init(element, options);

  // var parallax = document.querySelectorAll('.parallax');
  // var instances = M.Parallax.init(parallax);

  

  //Initialises the collapsible text box elements
  var collaps = document.querySelectorAll('.collapsible');
  var instances = M.Collapsible.init(collaps);

  //Initialises the drop down boxes
  var dropDowns = document.querySelectorAll('select');
  var instances = M.FormSelect.init(dropDowns);

  //var slider = document.querySelectorAll('.carousel');
  //var instances = M.Carousel.init(slider, options);

  var slider = M.Carousel.init({
    fullWidth: true
  });

});