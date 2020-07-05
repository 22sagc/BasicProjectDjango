function save_patient_details(){

    $.ajax({
            type: 'POST',
            url: '/webapp/patient-registrations/',
            data:  $('#registration_from').serialize(),
            success: function(response){
                if (response.success == 'true'){
                    alert('Data successfully saved.');
                    location.href = '/webapp/patient-details/'
                }
                else{
                    alert('Sorry for inconvenience, an error occurred');
                }
            },
    });

}