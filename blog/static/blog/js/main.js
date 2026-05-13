// Grab elements
const elementSelector = selector =>{
    const element = document.querySelector(selector);
    if(element){
        return element;
    }else{
        throw new Error(`Please enter correct selector  ${selector} does not exist`);
    }
}



//Nav styles on scroll

// Open menu & search pop-up
const menuToggleIcon = elementSelector(".menu-toggle");
const toggleMenu = ()=>{
    const mobileMenu = elementSelector("#menu");
    mobileMenu.classList.toggle("activated");
    menuToggleIcon.classList.toggle("activated");
};

menuToggleIcon.addEventListener('click',toggleMenu);

// Open/Close search form popup
const formOpenBtn = elementSelector(".search-open-btn");
const formCloseBtn = elementSelector(".search-btn-close");
const searchContainer = elementSelector(".search-container");

formOpenBtn.addEventListener('click',()=> {searchContainer.classList.add("activated")});
formCloseBtn.addEventListener('click',()=> {searchContainer.classList.remove("activated")});

// -- Close the search form popup on ESC keypress
window.addEventListener('keyup',(event)=>{
    if(event.key==="Escape"){
       searchContainer.classList.remove("activated") 
    }
    
});

// Switch theme/add to local storage
const bodyElement = document.body;

const themeBtn = elementSelector("#theme-toggle-btn");
const currentTheme = localStorage.getItem('currentTheme');

if(currentTheme){
    bodyElement.classList.add('light-theme');
}

themeBtn.addEventListener("click",()=>{
    bodyElement.classList.toggle("light-theme")
    if (bodyElement.classList.contains("light-theme")){

        localStorage.setItem('currentTheme','themeActive');

    }else{
        localStorage.removeItem('currentTheme')
    }
});

// Swiper

const swiper = new Swiper('.swiper',{
    slidesPerView: 1,
    spaceBetween: 20,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev"
    },

    pagination: {
        el: ".swiper-pagination"
    },

   
    breakpoints: {
        // 700px and up shoes 2 slides
        700: {
          slidesPerView: 2
        },
        // 1200px and up shoes 3 slides
        1200: {
            slidesPerView: 3
        }

        
    }



});