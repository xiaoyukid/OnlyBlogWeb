/**
 * Created by tonghs on 13-11-2.
 */
$(document).ready(function(){
    get_posts(1);
});

function get_posts(current_page){
    ajaxRequest('/get_posts/' + current_page, render_posts);
}

function render_posts(data){
    alert(data);
}