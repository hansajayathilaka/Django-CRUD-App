$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        console.log(btn.attr('data-url'))
//        debugger;
        $.ajax({
            url: btn.attr('data-url'),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-div').modal('show');
            },
            success: function(data){
                $('#modal-div .modal-content').html(data.html_form);
            }
        });
    };

    var SaveForm = function(){
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function(data){
                if(data.form_is_valid){
                    console.log('data is saved');
                    $('#modal-div').modal('hide');
                    $('#emp-table tbody').html(data.table_data);
                }
                else{
                    $('#modal-div .modal-content').html(data.html_form);
                }
            },
        });
        return false;
    };

//    var DelForm = function(){
//        var form = $(this);
//        debugger;
//        $.ajax({
//            url: form.attr('data-url'),
//            data: form.serialize(),
//            type: form.attr('method'),
//            dataType: 'json',
//            success: function(data){
//                debugger;
//                if(data.instance_is_valid){
//                    console.log('data is deleted');
//                    $('#modal-div').modal('hide');
//                    $('#emp-table tbody').html(data.table_data);
//                }
//                else{
//                    $('#modal-div .modal-content').html(data.html_form);
//                }
//            },
//        })
//        return false;
//    };

    // New Employee
    $('.btn-new-emp').click(ShowForm);
    $('#modal-div').on('submit', '.create-form', SaveForm);

    // Update Employee
    $('#emp-table').on('click', '.btn-edit-emp', ShowForm);
//    $('#emp-table .btn-edit-emp').click(ShowForm);
    $('#modal-div').on('submit', '.update-form', SaveForm);

    // Delete Employee
//    $('#emp-table .btn-del-emp').click(ShowForm);
    $('#emp-table').on('click', '.btn-del-emp', ShowForm);
    $('#modal-div').on('submit', '.delete-form', SaveForm);
});
