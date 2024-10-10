document.addEventListener("DOMContentLoaded", function() {
    const initSlider = (sliderClass, leftBtnId, rightBtnId) => {
        const slider = document.querySelector(sliderClass); 
        const leftButton = document.getElementById(leftBtnId);
        const rightButton = document.getElementById(rightBtnId);
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
            if (newScrollLeft <= 0 || newScrollLeft >= slider.scrollWidth - slider.offsetWidth) {
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
            timeoutId = setTimeout(() => {
                const maxScrollLeft = slider.scrollWidth - slider.offsetWidth;
                
                // If we have reached the end, reset to the start
                if (slider.scrollLeft >= maxScrollLeft) {
                    slider.scrollLeft = 0;  // 
                } else {
                    slider.scrollLeft += firstCardWidth;  
                }
            }, 2500); 
        };

        slider.addEventListener("mousedown", dragStart);
        slider.addEventListener("mousemove", dragging);
        document.addEventListener("mouseup", dragStop);
        slider.addEventListener("mouseenter", () => clearTimeout(timeoutId));
        slider.addEventListener("mouseleave", autoPlay);

        leftButton.addEventListener("click", () => {
            slider.scrollLeft -= firstCardWidth;
            clearTimeout(timeoutId);  
            autoPlay(); 
        });

        rightButton.addEventListener("click", () => {
            slider.scrollLeft += firstCardWidth;
            clearTimeout(timeoutId); 
            autoPlay(); 
        });

        autoPlay();
    };

    initSlider(".happy-hour-slider", "happy-hour-left", "happy-hour-right");
    initSlider(".top-salons-slider", "top-salons-left", "top-salons-right");
});
