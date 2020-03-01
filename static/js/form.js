var region = document.getElementById("region-select");
var editCourse = document.getElementById("edit-course-form");
var addCourse = document.getElementById("add-course-form");
var errorElement = document.getElementById("region-error");



if(editCourse != null){
    editCourse.addEventListener("submit", validation, false);
}

if(addCourse != null){
    addCourse.addEventListener("submit", validation, false);
}




function validation(event){
    let messages = [];
    if (region.value == "" || region.value == null){
        messages.push("You must select a region");
    }

    if (messages.length > 0){
        event.preventDefault();
        errorElement.innerHTML = messages.join()
    }


    
}

