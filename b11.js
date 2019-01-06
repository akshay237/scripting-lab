document.getElementById("pd").addEventListener("mouseover",myFunc);
var myObj,x=" ",y=" ";
myObj={
    "hname":"Fortis",
    "hlocn":"Banglore"
};
x=myObj.hname;
y=myObj.hlocn;
document.getElementById("hn").innerHTML=x;
document.getElementById("hl").innerHTML=y;

function myFunc()
{
    var myObj,i,x=" ";
    document.getElementById("MenuTable").removeAttribute("hidden");
    myObj={
        "patientdet":["name=Akshay","aadharno=2071897","lab-tests=blood-report"]
    };
    for(i in myObj.patientdet){
        x+=myObj.patientdet[i]+"&nbsp";
    }
    document.getElementById("item1").innerHTML=x;
}
