
const questionsBtn = document.querySelector('#generate-questions');
const questionsList = document.querySelector('#ai-questions');
questionsBtn.addEventListener('click', async function(e){
    e.preventDefault();
    var loading = document.getElementById('loading');
    questionsBtn.classList.toggle('cursor-not-allowed');
    loading.classList.toggle('hidden');
    questionsList.classList.add('opacity-0', 'hidden');

    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0]; // 사용자가 선택한 첫 번째 파일을 가져옵니다.

    if (file) {
        var formData = new FormData();
        formData.append('file', file);
    

    //데이터 불러오기
    await fetch('/projects/generate-questions', {
        method: 'POST',
        body: formData // 여기서 formData는 파일을 포함한 FormData 객체입니다.
      })
      .then(response => response.json())
      .then(questions => {
        // messageBox 요소를 찾습니다.
        var questionsBox = document.getElementById('questions-box');
    
        // 질문 목록을 messageBox 내용으로 설정합니다.
        questionsBox.innerHTML = '';
        questions.forEach(question => {
            var questionDiv = document.createElement('div');
            questionDiv.classList.add('bg-blue-200', 'text-black', 'w-full', 'py-2', 'px-4');
            questionDiv.textContent = question;
            questionsBox.appendChild(questionDiv);
          });
    

    questionsList.classList.remove('opacity-0','hidden');
    });

    }
    else {
        questionsList.classList.add('opacity-0', 'hidden');
    }
    
    questionsBtn.classList.toggle('cursor-not-allowed');
    loading.classList.toggle('hidden');
});