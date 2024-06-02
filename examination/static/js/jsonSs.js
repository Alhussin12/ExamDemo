function DeleteStudent(){
let DeleteStudent = document.querySelectorAll('[data-delete]');
DeleteStudent.forEach((e)=>{
    e.onclick= function(){
        studentId = e.getAttribute('data-delete')
        if (confirm("do you want to delete students!!!")) {

                fetch(`/Student/deleteStudent/`, {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify({studentId:studentId})})
                .then(res=>res.json).then(data=>{ console.log(aaa());})

        }
    }
})
}
//Show student filter system with pageinatino
const form = document.querySelector('.formSs');
const firstNameInput = document.getElementById('firstNameSs');
const lastNameInput = document.getElementById('lastNameSs');
const yearInput = document.getElementById('yearSs');
const SerialInput = document.getElementById('serialSs');
let countStudent= 0;
let nb = document.getElementById('nextBtn');
let pb = document.getElementById('backBtn');
let valueOfPage =document.getElementById('valueOfPage');
let toPage =document.querySelector('.toPage');
let resaultSs =document.querySelector('.resaultSs')
let vess =10;

function loads(){
        if (vess <= 10)
            pb.setAttribute('disabled','true')
            
        let sta = document.getElementById('tableStudentADD');
        const firstName = '';
        const lastName = '';
        const year = '';
        const serial = '';
        const data = {
        firstName: firstName,
        lastName: lastName,
        year: year,
        serial:serial,
        };
        fetch(`/Student/showStudentFilter/${vess}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)})
        .then(res=> res.json())
        .then(data => {
            sta.innerHTML='';
            countStudent = Math.ceil(data.size/10)*10;
            toPage.innerHTML=Math.ceil(data.size/10);
            resaultSs.innerHTML=data.size;
            data.s.forEach(e=>{
                url = document.location.href +'/'+String(e.id)
                sta.innerHTML=sta.innerHTML+`
                <tr>
                    <td>${e.year}</td>
                    <td>${e.firstName}</td>
                    <td>${e.lastName}</td>
                    <td>${e.id}</td>
                    <td>
                    <div class="modifyTableBtn">
                        <button>
                            <a href="${url}">
                            <svg fill="white" width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>eye</title> <path d="M0 16q0.064 0.128 0.16 0.352t0.48 0.928 0.832 1.344 1.248 1.536 1.664 1.696 2.144 1.568 2.624 1.344 3.136 0.896 3.712 0.352 3.712-0.352 3.168-0.928 2.592-1.312 2.144-1.6 1.664-1.632 1.248-1.6 0.832-1.312 0.48-0.928l0.16-0.352q-0.032-0.128-0.16-0.352t-0.48-0.896-0.832-1.344-1.248-1.568-1.664-1.664-2.144-1.568-2.624-1.344-3.136-0.896-3.712-0.352-3.712 0.352-3.168 0.896-2.592 1.344-2.144 1.568-1.664 1.664-1.248 1.568-0.832 1.344-0.48 0.928zM10.016 16q0-2.464 1.728-4.224t4.256-1.76 4.256 1.76 1.76 4.224-1.76 4.256-4.256 1.76-4.256-1.76-1.728-4.256zM12 16q0 1.664 1.184 2.848t2.816 1.152 2.816-1.152 1.184-2.848-1.184-2.816-2.816-1.184-2.816 1.184l2.816 2.816h-4z"></path> </g></svg>
                            </a>
                            </button>
                            <button data-delete='${e.id}' class='studentSelete'>
                            <a>
                            <svg height="16px" width="16px" version="1.1" id="_x32_" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512" xml:space="preserve" fill="#ffffff" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g> <path class="st0" d="M439.114,69.747c0,0,2.977,2.1-43.339-11.966c-41.52-12.604-80.795-15.309-80.795-15.309l-2.722-19.297 C310.387,9.857,299.484,0,286.642,0h-30.651h-30.651c-12.825,0-23.729,9.857-25.616,23.175l-2.722,19.297 c0,0-39.258,2.705-80.778,15.309C69.891,71.848,72.868,69.747,72.868,69.747c-10.324,2.849-17.536,12.655-17.536,23.864v16.695 h200.66h200.677V93.611C456.669,82.402,449.456,72.596,439.114,69.747z"></path> <path class="st0" d="M88.593,464.731C90.957,491.486,113.367,512,140.234,512h231.524c26.857,0,49.276-20.514,51.64-47.269 l25.642-327.21H62.952L88.593,464.731z M342.016,209.904c0.51-8.402,7.731-14.807,16.134-14.296 c8.402,0.51,14.798,7.731,14.296,16.134l-14.492,239.493c-0.51,8.402-7.731,14.798-16.133,14.288 c-8.403-0.51-14.806-7.722-14.296-16.125L342.016,209.904z M240.751,210.823c0-8.42,6.821-15.241,15.24-15.241 c8.42,0,15.24,6.821,15.24,15.241v239.492c0,8.42-6.821,15.24-15.24,15.24c-8.42,0-15.24-6.821-15.24-15.24V210.823z M153.833,195.608c8.403-0.51,15.624,5.894,16.134,14.296l14.509,239.492c0.51,8.403-5.894,15.615-14.296,16.125 c-8.403,0.51-15.624-5.886-16.134-14.288l-14.509-239.493C139.026,203.339,145.43,196.118,153.833,195.608z"></path> </g> </g></svg>
                            </a>
                        </button>
                    </div>
                </td>
                </tr>`
            })
            DeleteStudent()
        })
}
loads()
    function DeleteStudent(){
        let DeleteStudent = document.querySelectorAll('[data-delete]');
        DeleteStudent.forEach((e)=>{
            e.onclick= function(){
                studentId = e.getAttribute('data-delete')
                let msg = document.querySelector('.mssg');
                if (confirm("Do You Want To Delete Students If u Delete it You will Delete the Statstic of the student !!!")) {
                        let sta = document.getElementById('tableStudentADD');
                        fetch(`/Student/deleteStudent/`, {
                        method: 'POST',
                        headers: {
                        'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({studentId:studentId})})
                        .then(res=>res.json()).then(data=>{
                            msg.style.display='grid';
                            msg.style.backgroundColor='rgba(255, 0, 43, 0.5)';
                            msg.innerHTML=data.s;
                            setTimeout(()=>{
                                msg.style.display='none';
                            },3000)
                            loads()
                        })
                }
            }
        })
        }
form.addEventListener('keyup', (event) => {
let sta = document.getElementById('tableStudentADD');
    const firstName = firstNameInput.value;
    const lastName = lastNameInput.value;
    const year = yearInput.value;
    const serial = SerialInput.value;
    const data = {
        firstName: firstName,
        lastName: lastName,
        year: year,
        serial:serial,
      };
      fetch(`/Student/showStudentFilter/${vess}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)})
        .then(res=> res.json())
        .then(data => {
            sta.innerHTML='';
            countStudent = Math.ceil(data.size/10)*10;
            toPage.innerHTML=Math.ceil(data.size/10);
            resaultSs.innerHTML=data.size;
            data.s.forEach(e=>{
                url = document.location.href +'/'+String(e.id)
                sta.innerHTML=sta.innerHTML+`
                <tr>
                    <td>${e.year}</td>
                    <td>${e.firstName}</td>
                    <td>${e.lastName}</td>
                    <td>${e.id}</td>
                    <td>
                    <div class="modifyTableBtn">
                        <button>
                            <a href="${url}">
                            <svg fill="white" width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>eye</title> <path d="M0 16q0.064 0.128 0.16 0.352t0.48 0.928 0.832 1.344 1.248 1.536 1.664 1.696 2.144 1.568 2.624 1.344 3.136 0.896 3.712 0.352 3.712-0.352 3.168-0.928 2.592-1.312 2.144-1.6 1.664-1.632 1.248-1.6 0.832-1.312 0.48-0.928l0.16-0.352q-0.032-0.128-0.16-0.352t-0.48-0.896-0.832-1.344-1.248-1.568-1.664-1.664-2.144-1.568-2.624-1.344-3.136-0.896-3.712-0.352-3.712 0.352-3.168 0.896-2.592 1.344-2.144 1.568-1.664 1.664-1.248 1.568-0.832 1.344-0.48 0.928zM10.016 16q0-2.464 1.728-4.224t4.256-1.76 4.256 1.76 1.76 4.224-1.76 4.256-4.256 1.76-4.256-1.76-1.728-4.256zM12 16q0 1.664 1.184 2.848t2.816 1.152 2.816-1.152 1.184-2.848-1.184-2.816-2.816-1.184-2.816 1.184l2.816 2.816h-4z"></path> </g></svg>
                            </a>
                            </button>
                            <button data-delete='${e.id}' class='studentSelete'>
                            <a>
                            <svg height="16px" width="16px" version="1.1" id="_x32_" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512" xml:space="preserve" fill="#ffffff" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g> <path class="st0" d="M439.114,69.747c0,0,2.977,2.1-43.339-11.966c-41.52-12.604-80.795-15.309-80.795-15.309l-2.722-19.297 C310.387,9.857,299.484,0,286.642,0h-30.651h-30.651c-12.825,0-23.729,9.857-25.616,23.175l-2.722,19.297 c0,0-39.258,2.705-80.778,15.309C69.891,71.848,72.868,69.747,72.868,69.747c-10.324,2.849-17.536,12.655-17.536,23.864v16.695 h200.66h200.677V93.611C456.669,82.402,449.456,72.596,439.114,69.747z"></path> <path class="st0" d="M88.593,464.731C90.957,491.486,113.367,512,140.234,512h231.524c26.857,0,49.276-20.514,51.64-47.269 l25.642-327.21H62.952L88.593,464.731z M342.016,209.904c0.51-8.402,7.731-14.807,16.134-14.296 c8.402,0.51,14.798,7.731,14.296,16.134l-14.492,239.493c-0.51,8.402-7.731,14.798-16.133,14.288 c-8.403-0.51-14.806-7.722-14.296-16.125L342.016,209.904z M240.751,210.823c0-8.42,6.821-15.241,15.24-15.241 c8.42,0,15.24,6.821,15.24,15.241v239.492c0,8.42-6.821,15.24-15.24,15.24c-8.42,0-15.24-6.821-15.24-15.24V210.823z M153.833,195.608c8.403-0.51,15.624,5.894,16.134,14.296l14.509,239.492c0.51,8.403-5.894,15.615-14.296,16.125 c-8.403,0.51-15.624-5.886-16.134-14.288l-14.509-239.493C139.026,203.339,145.43,196.118,153.833,195.608z"></path> </g> </g></svg>
                            </a>
                        </button>
                    </div>
                </td>
                </tr>`
            })
            DeleteStudent()
        })
})

nb.addEventListener('click', (event) => {
    vess=vess+10;
    pb.removeAttribute('disabled')
    let sta = document.getElementById('tableStudentADD');
    valueOfPage.innerHTML=parseInt(valueOfPage.innerHTML)+1;
        const firstName = firstNameInput.value;
        const lastName = lastNameInput.value;
        const year = yearInput.value;
        const serial = SerialInput.value;
        const data = {
            firstName: firstName,
            lastName: lastName,
            year: year,
            serial:serial,
          };
        if (vess >=countStudent)
            nb.setAttribute('disabled','ture')
        fetch(`/Student/showStudentFilter/${vess}`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)})
            .then(res=> res.json())
            .then(data => {
                sta.innerHTML='';
                countStudent = Math.ceil(data.size/10)*10;
                toPage.innerHTML=Math.ceil(data.size/10);
                resaultSs.innerHTML=data.size;
                data.s.forEach(e=>{
                    url = document.location.href +'/'+String(e.id)
                    sta.innerHTML=sta.innerHTML+`
                    <tr>
                        <td>${e.year}</td>
                        <td>${e.firstName}</td>
                        <td>${e.lastName}</td>
                        <td>${e.id}</td>
                        <td>
                        <div class="modifyTableBtn">
                            <button>
                                <a href="${url}">
                                <svg fill="white" width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>eye</title> <path d="M0 16q0.064 0.128 0.16 0.352t0.48 0.928 0.832 1.344 1.248 1.536 1.664 1.696 2.144 1.568 2.624 1.344 3.136 0.896 3.712 0.352 3.712-0.352 3.168-0.928 2.592-1.312 2.144-1.6 1.664-1.632 1.248-1.6 0.832-1.312 0.48-0.928l0.16-0.352q-0.032-0.128-0.16-0.352t-0.48-0.896-0.832-1.344-1.248-1.568-1.664-1.664-2.144-1.568-2.624-1.344-3.136-0.896-3.712-0.352-3.712 0.352-3.168 0.896-2.592 1.344-2.144 1.568-1.664 1.664-1.248 1.568-0.832 1.344-0.48 0.928zM10.016 16q0-2.464 1.728-4.224t4.256-1.76 4.256 1.76 1.76 4.224-1.76 4.256-4.256 1.76-4.256-1.76-1.728-4.256zM12 16q0 1.664 1.184 2.848t2.816 1.152 2.816-1.152 1.184-2.848-1.184-2.816-2.816-1.184-2.816 1.184l2.816 2.816h-4z"></path> </g></svg>
                                </a>
                                </button>
                                <button data-delete='${e.id}' class='studentSelete'>
                                <a>
                                <svg height="16px" width="16px" version="1.1" id="_x32_" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512" xml:space="preserve" fill="#ffffff" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g> <path class="st0" d="M439.114,69.747c0,0,2.977,2.1-43.339-11.966c-41.52-12.604-80.795-15.309-80.795-15.309l-2.722-19.297 C310.387,9.857,299.484,0,286.642,0h-30.651h-30.651c-12.825,0-23.729,9.857-25.616,23.175l-2.722,19.297 c0,0-39.258,2.705-80.778,15.309C69.891,71.848,72.868,69.747,72.868,69.747c-10.324,2.849-17.536,12.655-17.536,23.864v16.695 h200.66h200.677V93.611C456.669,82.402,449.456,72.596,439.114,69.747z"></path> <path class="st0" d="M88.593,464.731C90.957,491.486,113.367,512,140.234,512h231.524c26.857,0,49.276-20.514,51.64-47.269 l25.642-327.21H62.952L88.593,464.731z M342.016,209.904c0.51-8.402,7.731-14.807,16.134-14.296 c8.402,0.51,14.798,7.731,14.296,16.134l-14.492,239.493c-0.51,8.402-7.731,14.798-16.133,14.288 c-8.403-0.51-14.806-7.722-14.296-16.125L342.016,209.904z M240.751,210.823c0-8.42,6.821-15.241,15.24-15.241 c8.42,0,15.24,6.821,15.24,15.241v239.492c0,8.42-6.821,15.24-15.24,15.24c-8.42,0-15.24-6.821-15.24-15.24V210.823z M153.833,195.608c8.403-0.51,15.624,5.894,16.134,14.296l14.509,239.492c0.51,8.403-5.894,15.615-14.296,16.125 c-8.403,0.51-15.624-5.886-16.134-14.288l-14.509-239.493C139.026,203.339,145.43,196.118,153.833,195.608z"></path> </g> </g></svg>
                                </a>
                            </button>
                        </div>
                    </td>
                    </tr>`
                })
                DeleteStudent()
            })
    })
    
pb.addEventListener('click', (event) => {
    valueOfPage.innerHTML=parseInt(valueOfPage.innerHTML)-1;
    vess=vess-10;
    nb.removeAttribute('disabled')
    let sta = document.getElementById('tableStudentADD');
    const firstName = firstNameInput.value;
    const lastName = lastNameInput.value;
    const year = yearInput.value;
    const serial = SerialInput.value;
    const data = {
        firstName: firstName,
        lastName: lastName,
        year: year,
        serial:serial,
        };
    if (vess <=10){
        vess=10;
        pb.setAttribute('disabled','true')}
    fetch(`/Student/showStudentFilter/${vess}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)})
            .then(res=> res.json())
            .then(data => {
                sta.innerHTML='';
                countStudent = Math.ceil(data.size/10)*10;
                toPage.innerHTML=Math.ceil(data.size/10);
                resaultSs.innerHTML=data.size;
                data.s.forEach(e=>{
                    url = document.location.href +'/'+String(e.id)
                    sta.innerHTML=sta.innerHTML+`
                    <tr>
                        <td>${e.year}</td>
                        <td>${e.firstName}</td>
                        <td>${e.lastName}</td>
                        <td>${e.id}</td>
                        <td>
                        <div class="modifyTableBtn">
                            <button >
                                <a href="${url}">
                                <svg fill="white" width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>eye</title> <path d="M0 16q0.064 0.128 0.16 0.352t0.48 0.928 0.832 1.344 1.248 1.536 1.664 1.696 2.144 1.568 2.624 1.344 3.136 0.896 3.712 0.352 3.712-0.352 3.168-0.928 2.592-1.312 2.144-1.6 1.664-1.632 1.248-1.6 0.832-1.312 0.48-0.928l0.16-0.352q-0.032-0.128-0.16-0.352t-0.48-0.896-0.832-1.344-1.248-1.568-1.664-1.664-2.144-1.568-2.624-1.344-3.136-0.896-3.712-0.352-3.712 0.352-3.168 0.896-2.592 1.344-2.144 1.568-1.664 1.664-1.248 1.568-0.832 1.344-0.48 0.928zM10.016 16q0-2.464 1.728-4.224t4.256-1.76 4.256 1.76 1.76 4.224-1.76 4.256-4.256 1.76-4.256-1.76-1.728-4.256zM12 16q0 1.664 1.184 2.848t2.816 1.152 2.816-1.152 1.184-2.848-1.184-2.816-2.816-1.184-2.816 1.184l2.816 2.816h-4z"></path> </g></svg>
                                </a>
                                </button>
                                <button data-delete='${e.id}' class='studentSelete'>
                                <a>
                                <svg height="16px" width="16px" version="1.1" id="_x32_" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512" xml:space="preserve" fill="#ffffff" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g> <path class="st0" d="M439.114,69.747c0,0,2.977,2.1-43.339-11.966c-41.52-12.604-80.795-15.309-80.795-15.309l-2.722-19.297 C310.387,9.857,299.484,0,286.642,0h-30.651h-30.651c-12.825,0-23.729,9.857-25.616,23.175l-2.722,19.297 c0,0-39.258,2.705-80.778,15.309C69.891,71.848,72.868,69.747,72.868,69.747c-10.324,2.849-17.536,12.655-17.536,23.864v16.695 h200.66h200.677V93.611C456.669,82.402,449.456,72.596,439.114,69.747z"></path> <path class="st0" d="M88.593,464.731C90.957,491.486,113.367,512,140.234,512h231.524c26.857,0,49.276-20.514,51.64-47.269 l25.642-327.21H62.952L88.593,464.731z M342.016,209.904c0.51-8.402,7.731-14.807,16.134-14.296 c8.402,0.51,14.798,7.731,14.296,16.134l-14.492,239.493c-0.51,8.402-7.731,14.798-16.133,14.288 c-8.403-0.51-14.806-7.722-14.296-16.125L342.016,209.904z M240.751,210.823c0-8.42,6.821-15.241,15.24-15.241 c8.42,0,15.24,6.821,15.24,15.241v239.492c0,8.42-6.821,15.24-15.24,15.24c-8.42,0-15.24-6.821-15.24-15.24V210.823z M153.833,195.608c8.403-0.51,15.624,5.894,16.134,14.296l14.509,239.492c0.51,8.403-5.894,15.615-14.296,16.125 c-8.403,0.51-15.624-5.886-16.134-14.288l-14.509-239.493C139.026,203.339,145.43,196.118,153.833,195.608z"></path> </g> </g></svg>
                                </a>
                            </button>
                        </div>
                    </td>
                    </tr>`
                })
                DeleteStudent()
            })
    })
// Delete spesfoc student

