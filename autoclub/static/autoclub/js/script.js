let currentIndex = 0;
let slidesContainer;
let totalSlides;
let isAnimating = false;

function showSlide(index) {
    currentIndex = index;

    const translateValue = -currentIndex * 100 + '%';
    slidesContainer.style.transition = 'transform 0.5s ease-in-out';
    slidesContainer.style.transform = 'translateX(' + translateValue + ')';
}

function nextSlide() {
    if (!isAnimating) {
        isAnimating = true;
        currentIndex = (currentIndex + 1) % (totalSlides + 2);
        showSlide(currentIndex);
        setTimeout(() => {
            isAnimating = false;
        }, 500);
    }
}

function prevSlide() {
    if (!isAnimating) {
        isAnimating = true;
        currentIndex = (currentIndex - 1 + totalSlides + 2) % (totalSlides + 2);
        showSlide(currentIndex);
        setTimeout(() => {
            isAnimating = false;
        }, 500);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    slidesContainer = document.querySelector('.slider');
    totalSlides = document.querySelectorAll('.slide').length;

    // Клонируем слайды
    const firstSlideClone = document.querySelector('.slide').cloneNode(true);
    const lastSlideClone = document.querySelector('.slide:last-child').cloneNode(true);

    // Добавляем клонированные слайды в начало и конец слайдера
    slidesContainer.insertBefore(lastSlideClone, slidesContainer.firstElementChild);
    slidesContainer.appendChild(firstSlideClone);

    // Устанавливаем начальное положение после добавления клонов
    slidesContainer.style.transform = 'translateX(' + (-100) + '%)';

    // Auto slide change (uncomment the line below if you want auto sliding)
    setInterval(nextSlide, 5000);

    // Добавляем событие transitionend для обеспечения бесконечного цикла
    slidesContainer.addEventListener('transitionend', function () {
        if (currentIndex === 0) {
            slidesContainer.style.transition = 'none';
            slidesContainer.style.transform = 'translateX(' + (-totalSlides * 100) + '%)';
            setTimeout(() => {
                slidesContainer.style.transition = 'transform 0.5s ease-in-out';
                currentIndex = totalSlides;
            }, 0);
        } else if (currentIndex === totalSlides + 1) {
            slidesContainer.style.transition = 'none';
            slidesContainer.style.transform = 'translateX(-100%)';
            setTimeout(() => {
                slidesContainer.style.transition = 'transform 0.5s ease-in-out';
                currentIndex = 1;
            }, 0);
        }
    });
});
