$(document).ready(function(){
    $("button").click(function(){
        var eID = this.id;
        $("#chart"+eID).toggle();
    })
    $.getJSON("https://joshvarg.github.io/test.json", function(data){
        $("#test").add("p").text(data.People[0].name);
    }).fail(function(){
        console.log("error");
    });
});