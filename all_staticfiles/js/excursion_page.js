function openModal(imageUrl) {
    const modal = document.getElementById("photoModal");
    const modalImage = document.getElementById("modalImage");
    modalImage.src = imageUrl;
    modal.style.display = "flex";
}

function closeModal() {
    document.getElementById("photoModal").style.display = "none";
}

let currentIndex = 0;

function updateCarousel() {
    const photos = document.querySelectorAll('.excursion-photo');
    const photoWrapper = document.querySelector('.photo-wrapper');
    const totalPhotos = photos.length;

    // Перемещаем обертку влево для показа текущей фотографии
    photoWrapper.style.transform = `translateX(-${currentIndex * 100}%)`;
}

function nextPhoto() {
    const photos = document.querySelectorAll('.excursion-photo');
    if (currentIndex < photos.length - 1) {
        currentIndex++;
    } else {
        currentIndex = 0; // Зацикливаем карусель
    }
    updateCarousel();
}

function prevPhoto() {
    const photos = document.querySelectorAll('.excursion-photo');
    if (currentIndex > 0) {
        currentIndex--;
    } else {
        currentIndex = photos.length - 1; // Зацикливаем карусель
    }
    updateCarousel();
}
