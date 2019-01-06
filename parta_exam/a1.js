function Check()
{
    var num=parseInt(document.getElementById('m').value);
    var result=document.getElementById('res');
    if(!isNaN(num))
    {
        if(num%3==0&&num%7==0)
         alert('NO is divisible by 3 and 7 both');
        else if(num%3==0)
        {
            alert('No is divisible by 3');
            result.value=num/3;
        }
        else if(num%7==0)
        {
            alert('No is divisible by 7');
            result.value=num/7;
        }
        else{
            alert('No is not divisible by 3 and 7');
        }
    }
    else
     alert('Input is not a number');
}