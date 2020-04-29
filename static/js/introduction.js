//extracting the parameter from html
var parsed_data = JSON.parse(data)
var user_id= parsed_data.u_i
var device= parsed_data.u_d

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
    obj.u_i = user_id
    obj.u_d = device
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
