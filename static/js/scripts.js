
document.addEventListener('DOMContentLoaded', function() {
  //Initialises the mobile nav bar
  var nav = document.querySelectorAll('.sidenav');
  var navInstances = M.Sidenav.init(nav);

  //parallax initialisation
  $('.parallax').parallax();

  //Slider initialise
  var sliderElement = document.querySelectorAll('.slider');
  var instances = M.Slider.init(sliderElement, options);

  //Initialises index image carousel
  let options = {
    //fullWidth: true,
    height:580,
    indicators: false,
    interval: 6000
  };

  //Initialises the collapsible text box elements
  var collaps = document.querySelectorAll('.collapsible');
  var collapsInstances = M.Collapsible.init(collaps);

  //Initialises the drop down boxes
  var dropDowns = document.querySelectorAll('select');
  var dropDownsInstances = M.FormSelect.init(dropDowns);

  //carousel on the home page
  var slider = M.Carousel.init({
    fullWidth: true
  });

});