const newProject = document.querySelector('#sub-header button');
const projectModal = document.querySelector('#modal-project');
newProject.addEventListener('click', function(e) {
    e.preventDefault();
    projectModal.classList.remove('hidden');
});

const cancelModal = document.querySelector('#modal-cancel');
cancelModal.addEventListener('click', function(e){
    e.preventDefault();
    projectModal.classList.add('hidden');
});

const editProject = document.querySelector('#edit-project');
const projectForm = document.querySelector('#project-form');
editProject.addEventListener('click',  async function(e) {
    e.preventDefault();
    projectModal.classList.add('hidden');
    const childrens = projectForm.children;
    let query = "?";
    for(let i=0;i<childrens.length;i++){
        query += `${childrens[i].firstElementChild.dataset.name}=${childrens[i].lastElementChild.value}&`;
    }

    await fetch(`/project/new${query}`,
        {method:'POST'});
    
});

function updateCalendar() {
    const now = new Date(); // 현재 날짜와 시간
    const dayOfWeek = now.getDay(); // 요일을 숫자로 반환 (0=일요일, 1=월요일, ...)
    // const date = now.getDate(); // 현재 날짜
    const month = now.getMonth(); // 현재 월 (0=1월, 1=2월, ...)
    const year = now.getFullYear(); // 현재 연도

    // 월 이름 배열
    const monthNames = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"];

    // 월과 연도 업데이트
    const monthYearDisplay = document.getElementById('calendar-month-year');
    monthYearDisplay.textContent = `${monthNames[month]} ${year}`;

    // 모든 날짜 요소 선택
    const dateElements = document.querySelectorAll('.border-hidden');

    // 현재 요일에 해당하는 요소 찾기
    dateElements.forEach((elem, index) => {
        const today = new Date();
        today.setDate(today.getDate() + (index - dayOfWeek));
        
        const date = today.getDate();

        if (index === dayOfWeek) {
            elem.classList.add('calender-active'); // 현재 요일 표시
            elem.querySelector('p.font-bold').textContent = date; // 현재 날짜로 업데이트
        } else {
            elem.classList.remove('calender-active'); // 다른 요일은 비활성화
            elem.querySelector('p.font-bold').textContent = date;
        }
    });
}

// 페이지 로드 시 현재 날짜 업데이트
document.addEventListener('DOMContentLoaded', updateCalendar);
