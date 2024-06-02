const prevBtns = document.querySelectorAll('.step-perv-btn');
const nextBtns = document.querySelectorAll('.step-next-btn');
const progress = document.querySelector('.progress');
const formSteps = document.querySelectorAll('.form-step');
const progSteps = document.querySelectorAll('.prog-step');
let formStepNum = 0;
nextBtns.forEach(e=>{
    e.addEventListener('click',()=>{
        formStepNum++;
        updateProgressBar();
        updateFormSteps();
    })
})
prevBtns.forEach(e=>{
    e.addEventListener('click',()=>{
        formStepNum--;
        updateProgressBar();
        updateFormSteps();
    })
})

function updateFormSteps(){
    formSteps.forEach((e)=>{
        e.classList.contains('form-step-active') &&
        e.classList.remove('form-step-active')

    })
    formSteps[formStepNum].classList.add('form-step-active')
}

function updateProgressBar(){
    progSteps.forEach((pro,inx)=>{
        if(inx < formStepNum +1)
            pro.classList.add('prog-step-active')
        else
            pro.classList.remove('prog-step-active')
        let proActive = document.querySelectorAll('.prog-step-active');
        progress.style.width=(( proActive.length -1)/(formSteps.length -1) * 100) + '%';
    })

}