// add student API SYSTEM   
let Stnbutton1 = document.getElementById('Stnbutton1');
Stnbutton1.addEventListener('click',function(){
        let msg = document.querySelector('.mssg');
        let SN = document.getElementById('SN').value;
        let FirstName = document.getElementById('FirstName').value;
        let LastName = document.getElementById('LastName').value;
        let year = document.getElementById('year').value;
        fetch('/Student/postSerialVal/',{
            body:JSON.stringify({
            SN:SN,
            FirstName:FirstName,
            LastName:LastName,
            year:year
            })
            ,method:'POST',}).then(res => res.json()).then(data=>{
            msg.style.display='grid';
            if(data.e){
                msg.style.backgroundColor='rgba(255, 0, 43, 0.5)';
                msg.innerHTML=data.e;
                setTimeout(()=>{
                    msg.style.display='none';
                },3000)
            }
            else{
                let SN = document.getElementById('SN');
                let FirstName = document.getElementById('FirstName');
                let LastName = document.getElementById('LastName');
                let year = document.getElementById('year');
                SN.value='';
                FirstName.value='';
                LastName.value='';
                year.value='1';
                msg.style.backgroundColor='var(--bs-border)';
                msg.innerHTML=data.s;
                setTimeout(()=>{
                    msg.style.display='none';
                },3000)
                }
        })})