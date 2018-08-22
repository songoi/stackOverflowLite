function showContent (element){
    var block = element.nextElementSibling
    if (block.style.display === "block") {
        block.style.display = "none";
    } else {
        block.style.display = "block";
    }
};
    
