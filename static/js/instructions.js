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



