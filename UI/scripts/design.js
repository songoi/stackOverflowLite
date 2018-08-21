// var hiddenContent = document.getElementsByClassName("collapser");
// var block = document.getElementsByClassName("collapse_content");

function showContent (element){
    var block = element.nextElementSibling
    if (block.style.display === "block") {
        block.style.display = "none";
    } else {
        block.style.display = "block";
    }
};
    

// hiddenContent.addEventListener("click", showContent);


// var coll = document.getElementsByClassName("collapser");
// var i;

// for (i = 0; i < coll.length; i++) {
//   coll[i].addEventListener("click", function() {
//     this.classList.toggle("active");
//     var content = this.nextElementSibling;
//     if (content.style.display === "block") {
//       content.style.display = "none";
//     } else {
//       content.style.display = "block";
//     }
//   });
// }