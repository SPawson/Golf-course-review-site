function checkState(){
    if (this.classlist.contains("disabled")){
        this.disabled = true;
        console.log("clicked")
    }
    else{
        this.disabled = false;
    }

}

document.addEventListener('DOMContentLoaded', function() {
    //Add mouse click event to each star element
    var chevron_next = document.getElementsByClassName("chev-next")[0];
    var chevron_prev = document.getElementsByClassName("chev-prev")[0];
    
    chevron_next.addEventListener("click",checkState,false);
    chevron_prev.addEventListener("click",checkState,false);



    

});

