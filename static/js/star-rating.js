document.addEventListener('DOMContentLoaded', function () {

    //Add mouse click event to each star element
    let stars = document.querySelectorAll('.star');
    stars.forEach(function (star) {
        star.addEventListener('click', setRating);
    });
    let ratingSelector = document.querySelector('.rating');
    if (ratingSelector != null) {
        let rating = parseInt(ratingSelector.getAttribute('value'));
        var selected = stars[rating - 1];
    }
    
    if (selected != null) {
        selected.dispatchEvent(new MouseEvent('click'));
    }
});

//sets the graphical and attribute rating
function setRating(ev) {
    let span = ev.currentTarget;
    let stars = document.querySelectorAll('.star');
    let match = false;
    let num = 0;

    //Looks through each star obj and assigns gold class depending on onj clicked
    stars.forEach(function (star, index) {
        if (match) {
            star.classList.remove('gold-star');
        } else {
            star.classList.add('gold-star');
        }
        if (star == span) {
            match = true;
            num = index + 1;
        }
        let starValue = parseInt(document.querySelector('.rating').getAttribute('value'));
    });
    document.querySelector('.rating').setAttribute('value', num);


}

// code snippets taken from https://www.youtube.com/watch?v=dPCj6Qkq13Y&t=146s