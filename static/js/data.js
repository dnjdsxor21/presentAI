const addBtn = document.querySelector('#add-button');
const modalCancel = document.querySelector('#modal-cancel');
addBtn.addEventListener('click', function(e) {
    e.preventDefault();
    const modalFile = document.querySelector('#modal-file');
    modalFile.classList.remove('hidden');
});
modalCancel.addEventListener('click', function(e) {
    e.preventDefault();
    const modalFile = document.querySelector('#modal-file');
    modalFile.classList.add('hidden');
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