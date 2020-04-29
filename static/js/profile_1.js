
var parsed_data = JSON.parse(myData)
var startTime, endTime;
startTime = new Date();


var counter = localStorage.getItem('counter');
if (counter === 'undefined')
    counter = 1;
    //TODO: create a json file with the relevant profile numbers



function next_page(){

    var score = document.getElementById("myRange").value;
    var current_profile = parsed_data.mylist[parsed_data.pointer-1]

    // save the response time
    endTime = new Date();
    var timeDiff = endTime - startTime; //in ms
    timeDiff /= 1000;


    var obj = new Object();
    obj.u_i = parsed_data.u_i;
    obj.profile_idx = parsed_data.pointer; //this is the index of the profile (DB column)
    obj.profile  = current_profile;
    obj.score = score;
    obj.response_time = timeDiff
    var data_to_send= JSON.stringify(obj);

    counter++;
    localStorage.setItem('counter',counter);
    postData('/save_data', data_to_send)
}


// sends json (data) to the server (app.py)
function postData(url, data) {
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
        profiles_list = parsed_data.mylist
        pointer = [parsed_data.pointer]
        next_page = profiles_list[pointer]
//        alert("next page is: " + next_page)
        jsoned_data = JSON.stringify(parsed_data)
        window.location.href='/profiles/' + next_page +'?param=' + jsoned_data
    })
    .catch(error => console.error(error));
}

  $(document).ready( function() {
  $('.step').each(function(index, element) {
    // element == this
    $(element).not('.active').addClass('done');
    $('.done').html('<i class="icon-ok"></i>');
    if($(this).is('.active')) {
      return false;
    }
  });
});

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