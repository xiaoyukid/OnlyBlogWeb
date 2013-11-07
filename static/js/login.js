/**
 * Created by Administrator on 13-11-7.
 */
$(document).ready(function(){
    $('#username').focus(function(){
        focus_handler('username');
    });
    $('#password').focus(function(){
        focus_handler('password');
    });

    $('#username').keypress(function(){
        if(event.keyCode == 13){
            $('#password').focus();
        }

    });
    $('#password').keypress(function(){
        if(event.keyCode == 13){
            $('#btn').click();
        }
    });

    $('#username').blur(function(){
        isValid('username');
    });

    $('#password').blur(function(){
        isValid('password');
    });

    if ($.cookie('username') != null){
        $('#username').val($.cookie('username'));
    }

    $('#username').focus();

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
    var username = $('#username').val();
    var password = $('#password').val();
    if(username != '' && password != ''){
        $('form').submit();
    } else {
        $('.msg').html('用户名或密码不可为空！');
    }
}
