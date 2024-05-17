const editBtn = document.getElementById('edit');
const deleteBtn =document.getElementById('delete');

editBtn.addEventListener('click', async function(e){
    e.preventDefault();
    var data = document.querySelectorAll('#data-form input, #data-form textarea');
    
    var formData = new FormData();
    for(let i=0; i<data.length;i++){
        formData.append(`col${i+1}`, data[i].value);
    }

    if (data.length) {
        const currentPath = window.location.pathname;
        const projectId = currentPath.split('/')[2]; 
        const editUrl = `/projects/${projectId}/edit`;

        await fetch(editUrl, {
            method: 'POST',
            body: formData
        });

        alert('수정 완료');
    }
});

deleteBtn.addEventListener('click', async function(e){
    e.preventDefault();
    var data = document.querySelectorAll('#data-form input, #data-form textarea');

    if (data.length) {
        const currentPath = window.location.pathname;
        const projectId = currentPath.split('/')[2]; 
        const deleteUrl = `/projects/${projectId}/delete`;

        await fetch(deleteUrl, {
            method: 'POST',
        });

        alert('삭제 완료');
        
        window.location.href="/projects";
    }
});

