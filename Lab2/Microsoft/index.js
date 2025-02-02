const slides = document.querySelectorAll(".carousel_list .carousel_item");
const dots = document.querySelectorAll(".dot")
let slideindex = 0;

initializeSlider();

function initializeSlider(){
    if(slides.length > 0){
        slides[slideindex].classList.add("displaySlide");
        dots[slideindex].classList.add("active");
    }
    
}


function showslide(index){
    if(index > slides.length -1){
        slideindex = 0;
    }

    else if(index < 0){
        slideindex = slides.length - 1;
    }

    slides.forEach(slide =>{
        slide.classList.remove("displaySlide")
    });
    dots.forEach(dot=>{
        dot.classList.remove("active")
    });
    slides[slideindex].classList.add("displaySlide");
    dots[slideindex].classList.add("active");
}

function currentslide(n){
    showslide(slideindex = n);


}

function prevslide(){
    slideindex--;
    showslide(slideindex);
}

function nextslide(){
    slideindex++;
    showslide(slideindex);
}