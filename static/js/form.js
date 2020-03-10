var region = document.getElementById("region-select");
var editCourse = document.getElementById("edit-course-form");
var addCourse = document.getElementById("add-course-form");
var errorElement = document.getElementById("region-error");
var regionSelect = document.getElementById("region");
var textSearch = document.getElementById("review-title");
var minRating = document.getElementById("min-rating");
var searchForm = document.getElementById("search");
var searchError= document.getElementById("search-error")

if(editCourse != null){
    editCourse.addEventListener("submit", courseValidation, false);
}
if(addCourse != null){
    addCourse.addEventListener("submit", courseValidation, false);
}
if(searchForm != null){
    searchForm.addEventListener("submit", searchValidation, false);
}



function courseValidation(event){
    let messages = [];
    if (region.value == "" || region.value == null){
        messages.push("You must select a region");
    }

    if (messages.length > 0){
        event.preventDefault();
        errorElement.innerHTML = messages.join()
    }
    
}


function searchValidation(event){
    let messages = [];
    if ((regionSelect.value == "" || region.value == null) && textSearch.value == "" && (minRating.value == 0 || minRating.value == null)){
        messages.push("You must use at least one filter");
    }

    if (messages.length > 0){
        event.preventDefault();
        searchError.innerHTML = messages.join()
    }
    
}

