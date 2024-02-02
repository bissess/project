document.addEventListener('DOMContentLoaded', function() {
    const imageContainer = document.getElementById('image-container');
    const input = imageContainer.querySelector('.image input[type="file"]');
    const selectedImage = document.getElementById('selected-image');
    const fileNamePlaceholder = document.getElementById('file-name-placeholder');
    const deleteImageBtn = document.getElementById('delete-image-btn');

    input.addEventListener('change', function() {
        const file = input.files[0];

        if (file) {
            const reader = new FileReader();

            reader.onload = function(e) {
                selectedImage.src = e.target.result;
                selectedImage.style.display = 'block';
                fileNamePlaceholder.textContent = file.name;
                deleteImageBtn.style.display = 'block';
            };

            reader.readAsDataURL(file);
        } else {
            // Сбрасываем значение input типа file
            input.value = '';

            selectedImage.style.display = 'none';
            fileNamePlaceholder.textContent = 'Файл не выбран';
            deleteImageBtn.style.display = 'none';
        }
    });

    function deleteSelectedImage(event) {
        event.preventDefault(); // Предотвращаем стандартное поведение

        // Сбрасываем значение input типа file
        input.value = '';

        // Сбрасываем изображение и имя файла
        selectedImage.style.display = 'none';
        fileNamePlaceholder.textContent = 'Файл не выбран';
    }

    deleteImageBtn.addEventListener('click', deleteSelectedImage);
});
