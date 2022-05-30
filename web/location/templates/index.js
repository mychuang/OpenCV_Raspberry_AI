function showPosition(position) {
    $("#lat").val(position.coords.latitude);
    $("#lon").val(position.coords.longitude);

    let date = new Date();
    var m = document.getElementById("msg");

    m.innerHTML = "日期: " + date.toISOString().split('T')[0];
}

//取得 經緯度
function getLocation(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);//有拿到位置就呼叫 showPosition 函式
    } else {
        m.innerHTML = "您的瀏覽器不支援顯示地理位置 API ，請使用其它瀏覽器開啟這個網址";
    }
}

$(document).ready(function(){
    $("#btn").click(function(){
        getLocation();
    });
});