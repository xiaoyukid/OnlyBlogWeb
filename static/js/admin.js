/**
 * Created by Administrator on 13-11-7.
 */
$(document).ready(function(){
    //单击其他地方隐藏菜单
    $(document).click(function(e){
        if (e.target != null && e.target.id != 'other_more'){
            if ($('#other_new').css('display') != 'none'){
                hideOtherMore();
            }
        } else {
            showOrHide();
        }

    });

    //文章内容textarea允许tab键
    $('#txt_content').allowtab();

    //标题和内容召唤模式，使用@召唤分类和标签
    $('#txt_title').atwho({
        at: "@cat:",
        data: ["+1", "-1", "s"]
    });

    $('#txt_content').atwho({
        at: "@tag:",
        data: ["+1", "-1", "smile"]
    });

});

function showOrHide(){
    if ($('#other_new').css('display') == 'none'){
        showOtherMore();
    } else {
        hideOtherMore();
    }
}

function showOtherMore(){
    $('#other_new').css('display', 'block');
    $('#other_more').css('background-color', '#ab3720');
}

function hideOtherMore(){
    $('#other_new').css('display', 'none');
    $('#other_more').css('background-color', '#d84c31');
}
