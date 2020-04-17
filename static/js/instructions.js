//extracting the parameter from html
var parsed_data = JSON.parse(data)
console.log(data)
console.log(parsed_data)
console.log(parsed_data.user_id)
console.log(parsed_data.device)

function go_to_agreement(){


        var obj = new Object();
        obj.user_id = parsed_data["user_id"]
        obj.device = parsed_data["device"]
        data_to_agreement= JSON.stringify(obj);
  window.location.href='/open_agreement?param=' +data_to_agreement;
}


function go_to_close_page(){
//    alert('Are you sure you want to close the experiment? If you close this page you will not recieve any payment!')
    var txt;
    var r = confirm("Are you sure you want to close the experiment? If you close this page you will not recieve any payment!");
    if (r == true) {
    txt = "You pressed OK!";
    window.location.href='/close_experiment'
    } else {
    txt = "You pressed Cancel!";
}

 }
