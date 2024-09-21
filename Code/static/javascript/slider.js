

document.addEventListener("DOMContentLoaded", function() {
    const slider = document.querySelector(".slider"); 
    const arrowButtons = document.querySelectorAll(".card-wrapper i");
    
    const firstCard = slider.querySelector(".salon-card");
    const firstCardWidth = firstCard.offsetWidth;

    let isDragging = false,
        startX,
        startScrollLeft,
        timeoutId;

    const dragStart = (e) => { 
        isDragging = true;
        slider.classList.add("dragging");
        startX = e.pageX;
        startScrollLeft = slider.scrollLeft;  
    };

    const dragging = (e) => {
        if (!isDragging) return;
    
        const newScrollLeft = startScrollLeft - (e.pageX - startX);
    
        if (newScrollLeft <= 0 || newScrollLeft >= 
            slider.scrollWidth - slider.offsetWidth) {
            
            isDragging = false;
            return;
        }
    
        slider.scrollLeft = newScrollLeft;
    };

    const dragStop = () => {
        isDragging = false; 
        slider.classList.remove("dragging");
    };

    const autoPlay = () => {
    
        if (window.innerWidth < 800) return; 
        
        const totalCardWidth = slider.scrollWidth;
        const maxScrollLeft = totalCardWidth - slider.offsetWidth;
        
        if (slider.scrollLeft >= maxScrollLeft) return;

        timeoutId = setTimeout(() => 
            slider.scrollLeft += firstCardWidth, 2500);
    };

    slider.addEventListener("mousedown", dragStart);
    slider.addEventListener("mousemove", dragging);
    document.addEventListener("mouseup", dragStop);
    slider.addEventListener("mouseenter", () => 
        clearTimeout(timeoutId));
    slider.addEventListener("mouseleave", autoPlay);

    arrowButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            slider.scrollLeft += btn.id === "left" ? 
                -firstCardWidth : firstCardWidth;
        });
    });

    autoPlay();
});
