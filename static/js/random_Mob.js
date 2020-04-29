var parsed_data = JSON.parse(data)
var user_id= parsed_data.user_id
var device= parsed_data.device
var trans_code= parsed_data.trans



window.onload = function(){

res= ""+ trans_code
document.getElementById("random_field").value = res;
}




function generateBarCode()
        {
            var nric = $('#text').val();
            var url = 'https://api.qrserver.com/v1/create-qr-code/?data=' + nric + '&amp;size=50x50';
            $('#barcode').attr('src', url);
        }


 function go_to_close_page(){

    window.location.href='/close_experiment'

 }
