$("#btn").click(function(){
    $("#form").submit(function(){
        var name = document.getElementById("name").value
        var location = document.getElementById("location").value
        var favLang = document.getElementById("favLang").value
        var travel = document.getElementById("travel")
        var music = document.getElementById("music").value
        var comment = document.getElementById("comment").value
        if(name.length < 1 || location == "None" || favLang == "noLang" ){
            alert("Please complete all required fields");
        }
        return false;
    });
}); 
// $("#form").submit(function(){
//     var fromValue = document.getElementById("fromDate").value;
//     var toValue = document.getElementById("toDate").value;
//     var nameValue = document.getElementById("name").value;
//     if(nameValue.length < 1){
//         alert("Please enter a name and resubmit the form");
//     }
//     else(
//         alert("Thanks " + nameValue + ". Your cruise leaves on " + fromValue + " and returns on " + toValue + ".") 
//     )
    
//     return false;
// });