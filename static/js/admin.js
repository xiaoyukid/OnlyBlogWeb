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

    //保存按钮
    $('#btn_save').click(save);

    //保存快捷键 ctrl + enter
    $('#txt_content').keyup(function(e){
        if (e.ctrlKey && e.which == 13){
            save();
        }
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

function save(){
    $('#btn_save').attr('disabled', true);
    $('#btn_save').attr('value', '保存中...');

    //获取标题和分类
    var titleAndCate = getTitleAndCat($('#txt_title').val());
    var title = titleAndCate.title;
    var cate = titleAndCate.cate;
    //获取内容和标签
    var contentAndTag = getContentAndTag($('#txt_content').val());
    var content = contentAndTag.content;
    var tag = contentAndTag.tag;
    var url = '/add_post';
    var id = $('#post_id').val();
    if (id != ""){
        url = '/update_post'
    }

    $.ajax({
        url: url,
        data: {
            id : id,
            title: title,
            content: content,
            category: cate,
            tag: tag
        },
        success:function(data){
            $('#btn_save').attr('disabled', false);
            $('#btn_save').attr('value', '保存');

            if (data != ''){
                $('#post_id').val(data);
                showMsg('保存成功！');
            }
        },
        error: showErr
    });

}

function getTitleAndCat(title){
    var cate = '未分类';
    var titleAndCate = {
        title: '',
        cat: ''
    };
    var arrStr = title.split('@cat:');
    if (arrStr.length > 0){

        titleAndCate.title = arrStr[0];

        if (arrStr.length < 2 || arrStr[1] == ''){
            titleAndCate.cate = cate;
        } else {
            titleAndCate.cate = arrStr[1].trim();
        }
    }


    return titleAndCate;
}

function getContentAndTag(content){
    var contentAndTag = {
        content: '',
        tag: ''
    };
    var arrStr = content.split('@tag:');
    if (arrStr.length > 0){

        contentAndTag.content = arrStr[0];

        if (arrStr.length < 2){
            contentAndTag.tag = '';
        } else {
            contentAndTag.tag = arrStr[1].trim();
        }
    }

    return contentAndTag
}