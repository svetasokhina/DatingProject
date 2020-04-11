//extracting the parameter from html
var parsed_data = JSON.parse(data)
var user_id= parsed_data.user_id
var device= parsed_data.device

function go_to_profiles(){
    var radios = document.getElementsByName('genderS');
    var choice = 0
    for (var i = 0, length = radios.length; i < length; i++) {
      if (radios[i].checked) {
        // do whatever you want with the checked radio
//        alert(radios[i].value);
        choice = radios[i].value
        // only one radio can be logically checked, don't check the rest
        break;
      }
    }

    var obj = new Object();
    obj.user_id = user_id
    obj.user_device = device
    obj.user_choice = choice
    var data_to_send= JSON.stringify(obj);
    res = start_experiment('/profiles', data_to_send)
}


// sends json (data) to the server (app.py)
function start_experiment(url, data) {
    // send post request to the server with the user's choice
    return fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        },
        body: data // must match 'Content-Type' header
    })
    .then(res => res.json())
    .then(data => {
        profiles_list = data.mylist
        next_page = profiles_list[data.pointer]
        jsoned_data = JSON.stringify(data)
        window.location.href='/profiles/' + next_page +'?param='+jsoned_data
    })
    .catch(error => console.error(error));
}



