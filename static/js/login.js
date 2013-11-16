/**
 * Created by Administrator on 13-11-7.
 */
$(document).ready(function(){
    $('#password').focus(function(){
        focus_handler('password');
    });

    $('#password').keypress(function(){
        if(event.keyCode == 13){
            $('#btn').click();
        }
    });

    $('#password').blur(function(){
        isValid('password');
    });

    if ($.cookie('password') != null){
        $('#password').val($.cookie('password'));
    }

    $('#password').focus();

    $('#btn').click(login);
});


function isValid(id){
    if ($('#' + id).val() == ''){
        $('#' + id).css('border', '1px solid red');
        $('#' + id).css('border-left', '1px solid #dddddd');
        $('#' + id + '_tip').css('border', '1px solid red');
        $('#' + id + '_tip').css('border-right-width', '0');
    }
}

function focus_handler(id){
    $('#' + id).css('border', '1px solid #dddddd');
    $('#' + id).css('border-left', '1px solid #dddddd');
    $('#' + id + '_tip').css('border', '1px solid #dddddd');
    $('#' + id + '_tip').css('border-right-width', '0');
}

function login(){
    var password = $('#password').val();
    if(password != ''){
        $('form').submit();
    } else {
        $('.msg').html('密码不可为空！');
    }
}
