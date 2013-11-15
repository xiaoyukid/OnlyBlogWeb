/**
 * Created by Administrator on 13-11-7.
 */
var editor;
$(document).ready(function(){
    $('#txt_title').focus();

    editor = new Editor();
    editor.render();

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

    //获取分类
    $.get('/get_category', function(data){
        if (data != null){
             //标题召唤模式，使用@cat:召唤分类
            $('#txt_title').atwho({
                at: '@cat:',
                data: eval('(' + data + ')')
            });

        }
    });

//    //获取标签
//    $.get('/get_tag', function(data){
//        if (data != null){
//            //内容召唤模式，使用@tag:召唤标签
//            $('pre').atwho({
//                at: "@tag:",
//                data: eval('(' + data + ')')
//            });
//        }
//    })

    //保存按钮
    $('#btn_save').click(save);
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
    editor.codemirror.save();
    //获取标题和分类
    var titleAndCate = getTitleAndCat($('#txt_title').val());
    var title = titleAndCate.title;
    var cate = titleAndCate.cate;
    //获取内容和标签
    var contentAndTag = getContentAndTag($('#txt_content').val());
    var content = editor.constructor.markdown(contentAndTag.content);
    var tag = contentAndTag.tag;

    if (title == ''){
        return;
    }

    var url = '/add_post';
    var id = $('#post_id').val();
    if (id != ""){
        url = '/update_post'
    }

    $.post(url,  {
            id : id,
            title: title,
            content: content,
            category: cate,
            tag: tag
        }, function(data){
            $('#btn_save').attr('disabled', false);
            $('#btn_save').attr('value', '保存');

            if (data != ''){
                $('#post_id').val(data);
                showMsg('保存成功！');
            }
        }).error(showErr);

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