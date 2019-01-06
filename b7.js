document.getElementById("car1").addEventListener("mouseover",myFunc2);
document.getElementById("car2").addEventListener("mouseover",myFunc3);

function myFunc2()
{
    var myObj,i,x=" ",y=" ";
    document.getElementById("MenuTable").removeAttribute("hidden");
    myObj={
        "name":"Ferrari",
        "features":["name=Ferrari","model=fera7","price=2cr","year=2016"]
    };
    x=myObj.name;
    for(i in myObj.features){
        y+=myObj.features[i]+"&nbsp";
    }
    document.getElementById("item1").innerHTML=x;
    document.getElementById("item2").innerHTML=y;
}
function myFunc3()
{
    var myObj,i,x=" ",y=" ";
    document.getElementById("MenuTable").removeAttribute("hidden");
    myObj={
        "name":"Audi",
        "features":["name=Audi","model=audiQ7","price=2cr","year=2016"]
    };
    x=myObj.name;
    for(i in myObj.features){
        y+=myObj.features[i]+"&nbsp";
    }
    document.getElementById("item1").innerHTML=x;
    document.getElementById("item2").innerHTML=y;
}