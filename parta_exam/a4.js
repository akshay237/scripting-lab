function By2()
{
    var n=parseInt(document.getElementById('m').value);
    var a=0;
    if(!isNaN(n))
    {
        a=n*2;
        alert('No is multiplied by 2');
        document.getElementById('res').innerHTML=a;
    }
    else
     alert('Input is not a number');
}
function ByNum()
{
    var n=parseInt(document.getElementById('m').value);
    var a=0;
    if(!isNaN(n))
    {
        a=n*n;
        alert('No is multiplied by itself');
        document.getElementById('res').innerHTML=a;
    }
    else
     alert('Input is not a number');
}