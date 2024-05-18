const addBtn = document.querySelectorAll('#add-button, #add-file');
const modalFileCancel = document.querySelector('#modal-file-cancel');
addBtn.forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        const modalFile = document.querySelector('#modal-file');
        modalFile.classList.remove('hidden');
    });
})
modalFileCancel.addEventListener('click', function(e) {
    e.preventDefault();
    const modalFile = document.querySelector('#modal-file');
    modalFile.classList.add('hidden');
})

const addFeedback = document.querySelector('#add-feedback');
const modalFeedbackCancel = document.querySelector('#modal-feedback-cancel');
addFeedback.addEventListener('click', function(e) {
    e.preventDefault();
    const modalFeedback = document.querySelector('#modal-feedback');
    modalFeedback.classList.remove('hidden');
});
modalFeedbackCancel.addEventListener('click', function(e) {
    e.preventDefault();
    const modalFeedback = document.querySelector('#modal-feedback');
    modalFeedback.classList.add('hidden');
})

function tab() {
    const buttons = document.querySelectorAll('#tabs button');
    const tabs = document.querySelectorAll('#tab-add-text, #tab-add-file, #tab-add-youtube');

    buttons.forEach(function(button, index) {
        button.addEventListener('click', function() {
            // 모든 버튼의 색상을 초기화하고, 클릭된 버튼만 색상 변경
            buttons.forEach(btn => {
                btn.classList.remove('color-silver');
                btn.classList.add('color-yellow');
            });
            this.classList.remove('color-yellow');
            this.classList.add('color-silver');

            // 모든 탭을 숨기고, 클릭된 버튼에 해당하는 탭만 보여줌
            tabs.forEach(tab => {
                tab.classList.add('hidden');
            });
            tabs[index].classList.remove('hidden');
        });
    });
}
document.addEventListener('DOMContentLoaded', tab);


const checkAll = document.getElementById('checkAll');
if (checkAll) {
    checkAll.addEventListener('change', function() {
    var checked = this.checked;
    var items = document.querySelectorAll('.checkItem');
    
    items.forEach(function(item) {
        item.checked = checked;
    });
});
}

function rateStar(star) {
    const ratingValue = star.getAttribute('data-value');
    const stars = document.querySelectorAll('.star');
    
    // 별점을 업데이트하기 전에 모든 별의 색상을 초기화합니다.
    stars.forEach(function(star, index) {
        console.log(index);
        if (index < ratingValue) {
            star.classList.add('rated');
        } else {
            star.classList.remove('rated');
        }
    });
    console.log(ratingValue);
}
