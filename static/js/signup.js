const noLoginBtn = document.querySelector('#nologin');
if (noLoginBtn) {
noLoginBtn.addEventListener('click', function(e){
    e.preventDefault();
    window.location.href="/projects";
});
}
// const client = supabase.createClient(supabaseURL, supabaseKEY);



// const signupBtn = document.querySelector('#signup');
// signupBtn.addEventListener('click', async function(e){
//     const signupEmail = document.querySelector('#signup-email');
//     const signupPasswd = document.querySelector('#signup-passwd'); 


//     const { data, error } = await client.auth.signUp({
//         email: signupEmail.value,
//         password: signupPasswd.value,
//     })
// });

// const googleBtn = document.querySelector('#google');
// googleBtn.addEventListener('click', async function(e) {
    
//     const { data, error } = await client.auth.signInWithOAuth({
//         provider: 'google'
//     })
// });
