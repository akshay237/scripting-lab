function Calculate()
{
    if(document.getElementById('add').checked)
{
    var m1=parseInt(document.getElementById("m1").value);
    var m2=parseInt(document.getElementById("m2").value);
    var sum=0;
    if(m1>=0&m2>=0)
    {
        sum=m1+m2;
        document.getElementById("result").innerHTML=sum;
    }
    else{
        alert('Invalid Input');
    }
}
else if (document.getElementById('subtarct').checked)
{
    var m1=parseInt(document.getElementById("m1").value);
    var m2=parseInt(document.getElementById("m2").value);
    var sub=0;
    if(m1>=0&m2>=0)
    {
        sub=m1-m2;
        document.getElementById("result").innerHTML=sub;
    }
    else{
        alert('Invalid Input');
    }
}
else if(document.getElementById('multiply').checked)
{
    var m1=parseInt(document.getElementById("m1").value);
    var m2=parseInt(document.getElementById("m2").value);
    var mul=0;
    if(m1>=0&m2>=0)
    {
        mul=m1*m2;
        document.getElementById("result").innerHTML=mul;
    }
    else{
        alert('Invalid Input');
    }
}
else if(document.getElementById('divide').checked)
{
    var m1=parseInt(document.getElementById("m1").value);
    var m2=parseInt(document.getElementById("m2").value);
    var div=0;
    if(m1>=0&m2>=0)
    {
        if(m2==0)
        document.getElementById("result").innerHTML="Divide by zero error";
        else{
        div=m1/m2;
        document.getElementById("result").innerHTML=div;
        }
    }
    else{
        alert('Invalid Input');
    }
}
else{
    alert('Id is not found');
}
}