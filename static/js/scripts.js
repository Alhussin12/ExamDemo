
// ### Map ###
function initMap() {
    const uluru = { lat: 34.7125228, lng: 36.7069045 };
    const elements=document.getElementById("map")
    const map = new google.maps.Map(elements, {
      zoom: 16,
      minZoom:16,
      maxZoom:16,
    //   scrollWheel:false,
      center: uluru,
      draggable:false,
      disableDefaultUI:true,
      mapTypeId:google.maps.MapTypeId.SATELLITE,//SATELLITE,HYBRID,ROADMAP
    })}
window.initMap=initMap;
// endMap


// ### Search buttom minWidth animations ###
let searchInputButtonMin =document.querySelector('.searchInputButtonMin');
let searchInput=document.querySelector('.searchInput');
var z=1;
searchInputButtonMin.onclick=function(){
    if(z==1){
        searchInput.style.left='50%';
        searchInput.style.transition='all .5s';
        z--;}
     else{
        searchInput.style.left='-50%';
        searchInput.style.transition='all .5s';
        z++;}};
    window.onresize=function(){
        if(window.innerWidth>900)
        searchInput.style.left='-50%';
        searchInput.style.transition='none';
        z=1;}
// endSearchButtonMinAnimation

// ### leftbar in mine animation ###
let minBar=document.querySelector('.minBar');
let leftBar=document.querySelector('.leftBar');
let leftBarCont=document.querySelector('.leftBarCont');
let bodys=document.getElementById('body');
let leftBarText=document.querySelector('.leftBarText');
minBar.onclick=function(e){

    if(window.innerWidth<900){
        if(this.getAttribute('data-value')==1){
            bodys.style.overflowY='hidden';
            leftBar.style.left='0px';
            leftBar.style.transition='all 0.5s';
            leftBarCont.style.width='100%';
            leftBarCont.style.transition='all 1s';
            minBar.style.left='250px';
            minBar.style.transition='all 0.5s';
             this.setAttribute('data-value',0);}
        
        else{
            bodys.style.overflowY='scroll';
            leftBar.style.left='-250px';
            leftBar.style.transition='all 0.5s';
            leftBarCont.style.width='0%';
            leftBarCont.style.transition='all 1s';
            minBar.style.left='0px';
            minBar.style.transition='all 0.5s';
            this.setAttribute('data-value','1');}}
    window.addEventListener("resize", myScript);
    function myScript(){
        if(window.innerWidth<900 ){
            leftBar.style.left='-250px';
            leftBarCont.style.width='0%';
            leftBar.style.transition='none';
            leftBarCont.style.transition='none';
            minBar.style.left='0px';
            minBar.setAttribute('data-value','1');}
        else{
            leftBar.style.left='0px';
            leftBar.style.transition='none';
            leftBarCont.style.width='0%';
            leftBarCont.style.transition='none';
            minBar.setAttribute('data-value','1');}}}

// ### DarkMode ###
// function darkMode(ele) {
//     var element = document.getElementById('body');
//     var header = document.querySelector('.navbarCont');
//     var leftbar = document.querySelector('.leftbar');
//     var content = document.querySelector('.content');
//     var profile = document.querySelector('.profile');
//     var leftBarCont = document.querySelector('.leftBarCont');
//     var minLeftRightNav = document.querySelector('.minLeftRightNav');
//     var logoNav = document.querySelector('.logoNav');
//     var buttonMinDarkSvg =document.querySelector('.buttonMinDarkSvg');
//     var minBar = document.querySelector('.minBar');
//     var searchInputForm = document.querySelector('.searchInputForm');
//     var searchButton = document.querySelector('.searchButton');
//     element.classList.toggle('darkBody');
//     if(ele.innerHTML.includes('Dark')){
//          ele.innerHTML=`
//          <div class="pt-2" style="display: flex; ">
//              <svg class='' style=" position:relative; top:2px; margin-right:1px;" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="yellow" class="bi bi-brightness-high-fill" viewBox="0 0 16 16">
//                  <path d="M12 8a4 4 0 1 1-8 0 4 4 0 0 1 8 0zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z"/>
//              </svg>
//              <p style='color:white;' >
//                  Light
//              </p>
//              </div>`;
//          header.style.background="var(--bs-darkPri)";
//          leftbar.style.backgroundColor="var(--bs-darkSec)";
//          content.style.backgroundColor='var(--bs-darkThierd)';
//          profile.style.background='var(--bs-darkThierd)';
//          leftBarCont.style.background='var(--bs-darkThierd)';
//          minLeftRightNav.style.background='var(--bs-darkSec)';
//          logoNav.style.border='5px solid var(--bs-darkPri)';
//          logoNav.style.outline='2px solid var(--bs-border)';
//          buttonMinDarkSvg.style.fill='white';
//          minBar.firstElementChild.style.fill='white';
//          searchInputForm.style.background='var(--bs-gray)';
//          searchButton.style.background='var(--bs-gray)';
//          let Allelements= document.querySelectorAll('*');
//          Allelements.forEach(function(e){
//              e.style.color='white';
//          })}
//     else{
//          header.style.background="var(--bs-prim)";
//          leftbar.style.background="var(--bs-sec)";
//          content.style.backgroundColor='var(--bs-content)';
//          profile.style.background='var(--bs-prim)';
//          leftBarCont.style.background='var(--bs-border)';
//          minLeftRightNav.style.background='var(--bs-sec)';
//          logoNav.style.border='5px solid var(--bs-prim)';
//          logoNav.style.outline='2px solid var(--bs-border)';
//          buttonMinDarkSvg.style.fill='black';
//          minBar.firstElementChild.style.fill='black';
//          searchInputForm.style.background='var(--bs-one)';
//          searchButton.style.background='var(--bs-one)';
//          ele.innerHTML=`  
//              <div class=" pt-2" style="display: flex;">
//                  <svg class="" style="position: relative; top:4px; padding-right: 2px;" xmlns="http://www.w3.org/2000/svg" width="20" height="16" fill="currentColor" class="bi bi-moon-fill" viewBox="0 0 16 16">
//                      <path d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z"/>
//                  </svg>
//                  <p>
//                      Dark
//                  </p>
//              </div>
//              `;
//          let Allelements= document.querySelectorAll('*');
//          Allelements.forEach(function(e){
//              e.style.color='black';
//          })}}
// endDarkMode

// ### subMenu ###
// let lang = document.querySelector('.lang');
// let subMenu=document.querySelector('.subMenu');
// /lang.onmouseover=function(){
//     subMenu.style.display='inline';
//     subMenu.style.opacity='1';
//     subMenu.style.transition='all 1s';
//     subMenu.onmouseover=function(){
//         subMenu.style.display='inline';
//         subMenu.style.opacity='1';
//         subMenu.style.transition='all 1s';}
//     subMenu.onmouseout=function(){
//         subMenu.style.display='none';
//         subMenu.style.opacity='0';
//         subMenu.style.transition='all 1s';}}
// lang.onmouseout=function(){
//     subMenu.style.display='none';
//     subMenu.style.opacity='0';
//     subMenu.style.transition='all 1s'}
// endSubMenu

// ### minLeftRightNav Container ###
let buttonMin=document.querySelector('.buttonMin');
let minLeftRightNav=document.querySelector('.minLeftRightNav');
let leftRightNav=document.querySelector('.leftRightNav');
let logoNav=document.querySelector('.logoNav');

buttonMin.onclick=function(){
    minLeftRightNav.innerHTML=leftRightNav.innerHTML;
    if(this.value=="ON"){
        minLeftRightNav.style.left='100%';
        minLeftRightNav.style.transition='all .5s';
        buttonMin.style.transform="rotate(0deg)";
        buttonMin.style.transition='all .8s';
        logoNav.style.top='10px';
        logoNav.style.width='80px';
        logoNav.style.height='80px';
        logoNav.style.transition='top 0.3s,width 0.3s,height 0.3s';
        this.value="OFF";}
    else{
        minLeftRightNav.style.left='0%';
        minLeftRightNav.style.transition='all .5s';
        buttonMin.style.transform="rotate(180deg)";
        buttonMin.style.transition='all .8s';
        logoNav.style.top='4px';
        logoNav.style.width='60px';
        logoNav.style.height='60px';
        logoNav.style.transition='top 0.3s,width 0.3s,height 0.3s';
        this.value="ON";
        }
    function reset(){
        if(innerWidth>900){
            buttonMin.value="ON";
            buttonMin.click();
            logoNav.style.top='0px';
            logoNav.style.width='60px';
            logoNav.style.height='60px';
            logoNav.style.transition='none';}
        else{
            // buttonMin.value="ON";
            // buttonMin.click();
            logoNav.style.width='80px';
            logoNav.style.height='80px';
            logoNav.style.top='10px';
            logoNav.style.transition='none';
        }
    }
    window.addEventListener('resize',reset)
    }

let clientX;
let clientY;

window.addEventListener('touchstart', (e) => {
    clientX = e.touches[0].clientX;
    clientY = e.touches[0].clientY;

    window.addEventListener('touchend', (e) => {
        let deltaX;
        let deltaY;
        deltaX = e.changedTouches[0].clientX - clientX;
        deltaY = e.changedTouches[0].clientY - clientY;

      }, false);
}, false);

// Accordion in left bar
var acc = document.querySelectorAll(".accordion");
var i;
acc.forEach(function(e){
    e.onclick=function(){
        // e.lastElementChild.style.backgroundColor='red';
        // var plusToMult= document.querySelector('.plusToMult');
        console.log('clicked');
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.opacity == 0) {
            e.lastElementChild.style.transform='rotate(45deg)';
            e.lastElementChild.style.transition='transform .3s';
            panel.style.position='relative';
            panel.style.opacity= "1";
            panel.style.visibility="visible";
            panel.style.transition='opacity .5s';} 
        else {
            e.lastElementChild.style.transform='rotate(0deg)';
            e.lastElementChild.style.transition='transform .3s';
            panel.style.position='absolute';
            panel.style.opacity = "0";
            panel.style.visibility="hidden";
            panel.style.transition='opacity .5s';}}
})



//  mobile optimaize hover
let mobileHovers =document.querySelectorAll('.mobileHover');
    for(i in mobileHovers){
        mobileHovers[i].ontouchstart=function(){
            this.style.backgroundColor='var(--bs-Gray)';}}
    for(i in mobileHovers){
        mobileHovers[i].ontouchend=function(){
            this.style.backgroundColor='transparent';}}

// window.addEventListener('touchstart',(e)=>{
//     let toutch=e.touches[0].clientX;
//     let toutch1=e.touches[0].pageX;
//     window.addEventListener('touchend',(e)=>{
//         if( toutch>0 && toutch<250 && e.changedTouches[0].clientX<window.innerWidth )
//             if( minBar.getAttribute('data-value')==1)
//             {
//                 minBar.click();
//                 minBar.style.transform='rotate(180deg)'
//             }
//         })
//                 },false)
// leftBar.addEventListener('touchstart',function(){
//             console.log('ds');
//         },false)
// let zo = [];

// window.addEventListener('touchmove',(e)=>{
//     window.addEventListener('touchstart',(e)=>{
//     if(window.innerWidth/10>e.touches[0].clientX)
//     {   console.log(zo, '  ', 'left')
//         zo.push('left')
//         window.addEventListener('touchend',(e)=>{
//             if(zo.find(element => element=='left')){
//                 if( minBar.getAttribute('data-value')==1)
//                     minBar.click();
//                     z=[]
//                 }
//         })
        
//     }
//     else{
//         zo.push('right');
          
//     }
// })})

// document.documentElement.style.setProperty('--bs-prim','')..s
