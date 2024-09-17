document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('messageModal');
    
    if (modal) {
        modal.style.display = 'flex'; 
        setTimeout(function() {
            modal.style.display = 'none';
        }, 10000); 

        
        window.onclick = function(event) {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        };
    }
});



// Получаем контейнер формы
var formContainer = document.getElementById("contactForm");

// Получаем кнопку, которая открывает форму
var btn = document.getElementById("showForm");

// При нажатии на кнопку показывается форма
btn.onclick = function() {
    formContainer.classList.add("show");
}

// При нажатии вне формы (на фон) форма скрывается
formContainer.onclick = function(event) {
    if (event.target === formContainer) {
        formContainer.classList.remove("show");
    }
}



