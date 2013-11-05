/**
 * Created by tonghs on 13-11-2.
 */
$(document).ready(function(){

});

function getNext(page){
    var next = page + 1;
    $('#pager').html('正在加载...');
    $.ajax({
        url: '/page/' + next + '/1',
        error: showErr,
        success: function(data){
            var arrObj = JSON.parse(data);
            if (arrObj == null || arrObj.length <= 0){
                $('#pager').html('后面没有了');
                $('#pager').removeAttr('onclick');
            } else {
                for (var i = 0; i < arrObj.length; i++){
                    var id = arrObj[i].id;
                    var title = arrObj[i].title;
                    var content = arrObj[i].content;
                    var category = arrObj[i].category;

                    var post_wrapper=$('<div></div>'); //创建一个父div
                    post_wrapper.attr('class', 'post_wrapper');//添加css样式

                    var post_title=$('<div></div>');//创建一个标题子div
                    post_title.attr('class', 'post post_title');//添加css样式
                    post_title.html('<a href="/post/'+ id +'">' + title + '</a>');//设置div内容
                    post_wrapper.append(post_title);//将子div添加到父div中

                    var post_content=$('<div></div>');//创建一个标题子div
                    post_content.attr('class', 'post post_content');//添加css样式
                    post_content.html(content);//设置div内容
                    post_wrapper.append(post_content);//将子div添加到父div中

                    var post_footer=$('<div></div>');//创建一个标题子div
                    post_footer.attr('class', 'post post_footer');//添加css样式
                    post_footer.html('标签:test &nbsp;&nbsp; 所属:<a href="/category/' + category + '">' + category + '</a>');//设置div内容
                    post_wrapper.append(post_footer);//将子div添加到父div中

                    $('#post').append(post_wrapper);//将父div添加到页面中
                }
                $('#pager').html('下一页');
                $('#pager').attr('onclick', 'getNext(' + next + ')');
            }

        }
    });
}
