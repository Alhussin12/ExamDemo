let staticForm = document.getElementById('staticForm');
let years = document.getElementById('years')
let sem = document.getElementById('sem')
let pagBtnBack =document.getElementById('backBtn')
let pagBtnNext =document.getElementById('nextBtn')
let v=2;
let dis =0

window.onload = function(){
  if (v<=2)
  {
  pagBtnBack.setAttribute('disabled','true')
  }
  dis =1
  id =document.location.href.split('/')
  id = id[id.length-1]
  const data = {
    years: years.value,
    sem:sem.value,
    id:id,
    dis:dis,
  };
  fetch(`/Student/sStaFilter/${v}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)})
    .then(res=> res.json())
    .then(data => {
      if(data.e)
      {}
      else{
        let resaultSs =document.querySelector('.resaultSs');
        let table = document.getElementById('statisticTable')

        resaultSs.innerHTML=data.size
        to =(Math.ceil(data.size/2)*2)+1
        document.querySelector('.toPage').innerHTML=Math.ceil(data.size/2)
        
        if(v>=to)
          pagBtnNext.setAttribute('disabled','true')
        data.s.forEach(e=>{
          url =document.location.href+`/${e.ec}`
          table.innerHTML=table.innerHTML+`
          <tr>
            <td>${e.year}</td>
            <td>${e.Semineter}</td>
            <td>${e.average_grade}</td>
            <td>${e.success_grades_count}</td>
            <td>${e.grade_count}</td>
            <td>
              <div class="modifyTableBtn">
                <button>
                    <a href="${url}">
                      <svg fill="white" width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>eye</title> <path d="M0 16q0.064 0.128 0.16 0.352t0.48 0.928 0.832 1.344 1.248 1.536 1.664 1.696 2.144 1.568 2.624 1.344 3.136 0.896 3.712 0.352 3.712-0.352 3.168-0.928 2.592-1.312 2.144-1.6 1.664-1.632 1.248-1.6 0.832-1.312 0.48-0.928l0.16-0.352q-0.032-0.128-0.16-0.352t-0.48-0.896-0.832-1.344-1.248-1.568-1.664-1.664-2.144-1.568-2.624-1.344-3.136-0.896-3.712-0.352-3.712 0.352-3.168 0.896-2.592 1.344-2.144 1.568-1.664 1.664-1.248 1.568-0.832 1.344-0.48 0.928zM10.016 16q0-2.464 1.728-4.224t4.256-1.76 4.256 1.76 1.76 4.224-1.76 4.256-4.256 1.76-4.256-1.76-1.728-4.256zM12 16q0 1.664 1.184 2.848t2.816 1.152 2.816-1.152 1.184-2.848-1.184-2.816-2.816-1.184-2.816 1.184l2.816 2.816h-4z"></path> </g></svg>
                    </a>
                </button>
              </div>
            </td>
          </tr>
          `
        })
      }
    })
}

pagBtnBack.onclick=
pagBtnNext.onclick=
staticForm.onkeyup=
  (event) => {
  dis=0
  if(event.target.id == 'nextBtn'){
    document.getElementById('valueOfPage').innerHTML=
    parseInt(document.getElementById('valueOfPage').innerHTML)+1
    pagBtnBack.removeAttribute('disabled')
    v=v+2}
  else if(event.target.id == 'backBtn'){
    pagBtnNext.removeAttribute('disabled')
    document.getElementById('valueOfPage').innerHTML=
    parseInt(document.getElementById('valueOfPage').innerHTML)-1

    v=v-2
    if(v<=2)
      pagBtnBack.setAttribute('disabled','true')
    }
  id =document.location.href.split('/')
  id = id[id.length-1]
  const data = {
    years: years.value,
    sem:sem.value,
    id:id,
    dis:dis,
  };

  fetch(`/Student/sStaFilter/${v}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)})
    .then(res=> res.json())
    .then(data => {
      if(data.e)
      {
        let msg = document.querySelector('.mssg')
        msg.style.display='grid'
        msg.innerHTML=data.e
        setTimeout(function(){
        msg.style.display='none'
        },3000)
      }
      else{
        let table = document.getElementById('statisticTable')
        let resaultSs =document.querySelector('.resaultSs')
        resaultSs.innerHTML=data.size
        to =(Math.ceil(data.size/2)*2)+1
        document.querySelector('.toPage').innerHTML=Math.ceil(data.size/2)
        if(v>=to)
          pagBtnNext.setAttribute('disabled','true')
        else
            pagBtnNext.removeAttribute('disabled')
        table.innerHTML='';
        data.s.forEach(e=>{
          url =document.location.href+`/${e.ec}`
          table.innerHTML=table.innerHTML+`
          <tr>
            <td>${e.year}</td>
            <td>${e.Semineter}</td>
            <td>${e.average_grade}</td>
            <td>${e.success_grades_count}</td>
            <td>${e.grade_count}</td>
            <td>
              <div class="modifyTableBtn">
                <button>
                    <a href="${url}">
                      <svg fill="white" width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>eye</title> <path d="M0 16q0.064 0.128 0.16 0.352t0.48 0.928 0.832 1.344 1.248 1.536 1.664 1.696 2.144 1.568 2.624 1.344 3.136 0.896 3.712 0.352 3.712-0.352 3.168-0.928 2.592-1.312 2.144-1.6 1.664-1.632 1.248-1.6 0.832-1.312 0.48-0.928l0.16-0.352q-0.032-0.128-0.16-0.352t-0.48-0.896-0.832-1.344-1.248-1.568-1.664-1.664-2.144-1.568-2.624-1.344-3.136-0.896-3.712-0.352-3.712 0.352-3.168 0.896-2.592 1.344-2.144 1.568-1.664 1.664-1.248 1.568-0.832 1.344-0.48 0.928zM10.016 16q0-2.464 1.728-4.224t4.256-1.76 4.256 1.76 1.76 4.224-1.76 4.256-4.256 1.76-4.256-1.76-1.728-4.256zM12 16q0 1.664 1.184 2.848t2.816 1.152 2.816-1.152 1.184-2.848-1.184-2.816-2.816-1.184-2.816 1.184l2.816 2.816h-4z"></path> </g></svg>
                    </a>
                </button>
              </div>
            </td>
          </tr>
          `
        })
      }
    })
}