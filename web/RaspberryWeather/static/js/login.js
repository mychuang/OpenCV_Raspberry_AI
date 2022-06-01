function error(err){
    console.log(err.message);

    let date = new Date();
    $.ajax({
        url: "/setRequest",
        type: "POST",
        dataType: "json",
        data: {
            'user': $("#username").val(),
            'lon': '121.02', 
            'lat': '24.84',
            'date': date.toISOString().split('T')[0]
        },
        success: function (data) {
            if(data.hasOwnProperty("msg")){
                console.log(data.msg);
                window.location.href = "/home"
            }
        }
    })
}

var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
}

function showPosition(position) {
    let date = new Date();

    console.log($("#username").val());
    console.log($("#password").val());
    console.log(position.coords.latitude);
    console.log(position.coords.longitude)
    console.log(date.toISOString().split('T')[0])

    $.ajax({
        url: "/setRequest",
        type: "POST",
        dataType: "json",
        data: {
            'pwd': $("#password").val(),
            'user': $("#username").val(),
            'lon': position.coords.longitude, 
            'lat': position.coords.latitude,
            'date': date.toISOString().split('T')[0]
        },
        success: function (data) {
            if(data.hasOwnProperty("msg")){
                console.log(data.msg);
                window.location.href = "/home"
            }
        }
    })
}

$(document).ready(function(){
    $("#btn").click(function(){
        if (navigator.geolocation){
            navigator.geolocation.getCurrentPosition(showPosition, error, options);//有拿到位置就呼叫 showPosition 函式
        }else{
            alert("您的瀏覽器不支援顯示地理位置 API ，請使用其它瀏覽器開啟這個網址");
        }
    });
});