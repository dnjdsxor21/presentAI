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
const outlineBtn = document.getElementById('outline-btn');
if (outlineBtn) {
    outlineBtn.addEventListener('click', async function(e){
        e.preventDefault();
        var loading = document.getElementById('loading');
        const currentPath = window.location.pathname;
        const projectId = currentPath.split('/')[2]; 
        const newUrl = `/projects/${projectId}/outline`;

        loading.classList.remove('hidden');

        var formData = new FormData();

        await fetch(newUrl, {
            method: 'POST',
            body: formData // 여기서 formData는 파일을 포함한 FormData 객체입니다.
          })
          .then(response => response.json())
          .then(answers => {
            // messageBox 요소를 찾습니다.
            var outlineBox = document.getElementById('outline-box');
        
            // 질문 목록을 messageBox 내용으로 설정합니다.
            outlineBox.innerHTML = '';
            answers.forEach(answer => {
                var outlineDiv = document.createElement('div');
                outlineDiv.innerHTML = convertBoldText(answer);
                outlineBox.appendChild(outlineDiv);
              });
        
        
        });

        const outlineAnswer = document.getElementById('ai-outline');
        outlineAnswer.classList.remove('hidden', 'opacity-0');
        loading.classList.add('hidden');

    });

}

function convertBoldText(text) {
    // **로 둘러싸인 텍스트를 <strong>으로 변환
    return text.replace(/\*\*(.*?)\*\*/g, "<span class='font-bold'>$1</span>");
  }
