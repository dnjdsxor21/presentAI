const noLoginBtn = document.querySelector('#nologin');
if (noLoginBtn) {
noLoginBtn.addEventListener('click', function(e){
    e.preventDefault();
    window.location.href="/projects";
});
}

const signupBtn = document.querySelector('#signup');
if (signupBtn) {
signupBtn.addEventListener('click', function(e){
    e.preventDefault();
    window.location.href="/signup";
});
}

// const client = supabase.createClient(supabaseURL, supabaseKEY);

// const loginBtn = document.querySelector('#login');
// loginBtn.addEventListener('click', async function(e){
//     e.preventDefault();
//     const loginEmail = document.querySelector('#login-email');
//     const loginPasswd = document.querySelector('#login-password');
    
//     var formData = new FormData();
//     formData.append('email',loginEmail.textContent);
//     formData.append('password', loginPasswd.textContent);
//     await fetch('/login', {
//         method: 'POST',
//         body: formData // 여기서 formData는 파일을 포함한 
//     }).then(data => console.log(data));
// });

// const googleBtn = document.querySelector('#google');
// googleBtn.addEventListener('click', async function(e) {
    
//     const { data, error } = await client.auth.signInWithOAuth({
//         provider: 'google'
//     })
// });
