function valid(){
    // Get form references:
	var name = $("#username").val();
	var pwd = $("#password").val();
	var email = $("#email").val();

    // Flag variable:
	var error = 0;

	if (/^[A-Z \.\-']{2,20}$/i.test(name)) {
		$("#pname").text("");
	} else {
		$("#pname").text("格式錯誤: /^[A-Z \.\-']{2,20}$/");
		error++;
	}

    if (/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{8,16}$/i.test(pwd)) {
		$("#ppwd").text("");
	} else {
		$("#ppwd").text("8-16個字符,至少1個大寫字母,1個小寫字母和1個數字");
		error++;
	}

    if (/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,6}$/.test(email)) {
		$("#pemail").text("");
	} else {
		$("#pemail").text("格式錯誤: /^[\w.-]+@[\w.-]+\.[A-Za-z]{2,6}$/");
		error++;
	}

    if(error>0){
        console.log("error counts: ", error);
    }else{
        console.log("Ajax");
    }
    error = 0;
}

$(document).ready(function(){
    
    checkBox = document.getElementById('checker').addEventListener('click', event => {
        if(event.target.checked) {
            $("#btn").removeAttr("disabled");
        }else{
            $("#btn").attr("disabled", true);
        }
    });

    $("#btn").click(function(){
        valid();
    });
})