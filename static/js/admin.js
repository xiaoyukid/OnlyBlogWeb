/**
 * Created by Administrator on 13-11-7.
 */
$(document).ready(function(){
    $('#more').click(showOrHide);
    $('#allowtab').allowtab();
});

function showOrHide(){
    if ($('#new').css('display') == 'none'){
        $('#new').css('display', 'block');
        $('#more').css('background-color', '#ab3720');
    } else {
        $('#new').css('display', 'none');
        $('#more').css('background-color', '#d84c31');
    }
}
