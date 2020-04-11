var parsed_data = JSON.parse(data)
var user_id= parsed_data.user_id
var device= parsed_data.device
var trans_code= parsed_data.trans


window.onload = function(){

res= ""+ trans_code
document.getElementById("random_field").value = res;
}







//function randomString() {
//    var chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz";
//    var string_length = 10;
//    var randomstring = '';
//    for (var i=0; i<string_length; i++) {
//        var rnum = Math.floor(Math.random() * chars.length);
//        randomstring += chars.substring(rnum,rnum+1);
//    }
//    document.randform.randomfield.value = randomstring;
//}