const hours = 24;
const now = new DateGetTime();
const stepTime = localStorage.getItem('stepTime');

if (stepTime == null){
    localStorage.getItem('StepTime', now);
}
else {
    if (now - stepTime > hours*60*60*1000){
        localStorage.clear()
        localStorage.setItem('stepTime', now);
    }
}
