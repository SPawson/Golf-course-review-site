document.addEventListener('DOMContentLoaded', function() {
    //Add mouse click event to each star element
    var chevron_next = document.getElementsByClassName(".chev-next");
    var chevron_prev = document.getElementsByClassName(".chev-prev");
    
    chevron_next.addEventListener("click",checkState());
    chevron_prev.addEventListener("click",checkState());



    

});

function checkState(this){
        
    if (this.classlist.contains("disabled")){
        this.disabled = true;
    }
    else{
        this.disabled = false;
    }

};