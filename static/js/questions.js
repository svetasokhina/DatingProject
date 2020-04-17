
var parsed_data = JSON.parse(myData)

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

function submit_questions(){

    // get answers value
    q1 = document.getElementById("question1").value;
    q2 = document.getElementById("question2").value;
    q3 = document.getElementById("question3").value;
    q4 = document.getElementById("question4").value;
    q5 = document.getElementById("question5").value;
    q6 = document.getElementById("question6").value;
    q7 = document.getElementById("question7").value;
    q8 = document.getElementById("question8").value;
    q9 = document.getElementById("question9").value;
    q10 = document.getElementById("question10").value;
    q11 = document.getElementById("question11").value;
    q12 = document.getElementById("question12").value;

    // vlidate that there is no question (Q) empty
    if (q1 !="" && q1 !="" && q2 !="" && q3 !="" && q4 !="" && q5 !="" && q6 !="" && q7 !="" && q8 !=""
            && q9 !="" && q10 !="" && q11 !="" && q12 !="" ){

            s1_obj = $('input[name="likert1"]:checked');
            s2_obj = $('input[name="likert2"]:checked');
            s3_obj = $('input[name="likert3"]:checked');
            s4_obj = $('input[name="likert4"]:checked');
            s5_obj = $('input[name="likert5"]:checked');
            s6_obj = $('input[name="likert6"]:checked');
            s7_obj = $('input[name="likert7"]:checked');
            s8_obj = $('input[name="likert8"]:checked');

            // validate that thee is no scale question empty
            if(s1_obj.length && s2_obj.length && s3_obj.length && s4_obj.length && s5_obj.length
                && s6_obj.length && s7_obj.length && s8_obj.length){


                var obj = new Object();
                obj.user_id = parsed_data.id
                obj.q1 = q1
                obj.q2 = q2
                obj.q3 = q3
                obj.q4 = q4
                obj.q5 = q5
                obj.q6 = q6
                obj.q7 = q7
                obj.q8 = q8
                obj.q9 = q9
                obj.q10 = q10
                obj.q11 = q11
                obj.q12 = q12

                obj.s1 = s1_obj.val()
                obj.s2 = s2_obj.val()
                obj.s3 = s3_obj.val()
                obj.s4 = s4_obj.val()
                obj.s5 = s5_obj.val()
                obj.s6 = s6_obj.val()
                obj.s7 = s7_obj.val()
                obj.s8 = s8_obj.val()


                //convert object to json string
                var string = JSON.stringify(obj);

                //convert string to Json Object
                console.log(JSON.parse(string)); // this is your requirement.
                send_questions('/save_questions',string)

                }

             else{alert("Please answer all the questions") }

     }else{alert("Please answer all the questions")}

}

// sends json (data) to the server (app.py)
function send_questions(url, data) {

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
        jsoned_data = JSON.stringify(data)
        console.log('finished: ' + jsoned_data )
        window.location.href='/end_of_experiment?param='+ jsoned_data
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