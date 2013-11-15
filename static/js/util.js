$(document).ready(function(){
    resize();
    $(window).resize(resize);

});

function showLoad(tipInfo) {
    if ($("#tipDiv").size() == 0){
        var eTip = document.createElement('div');
        eTip.setAttribute('id', 'tipDiv');
        eTip.style.position = 'absolute';
        eTip.style.display = 'none';
        eTip.style.textAlign = 'center';
        eTip.style.border = 'solid 0px #D1D1D1';
        eTip.style.backgroundColor = '#4B981D';
        eTip.style.padding = '0 15px 3px 15px';
        eTip.style.left = ($('html').width() - 190) / 2 + 'px';
        eTip.style.top = '0px';
        eTip.style.width = '190px';
        eTip.innerHTML = '<span class="loading_logo bold">Only RSS</span>&nbsp;&nbsp;'
            +'<span class="loading">' + tipInfo + '</span>';
        try {
            document.body.appendChild(eTip);
        } catch (e) { }
        $("#tipDiv").css("z-index", "99");
    }

    $('#tipDiv').slideDown();
}

function closeLoad() {
    $('#tipDiv').slideUp();
}


function resize(){
    var bottom = 65;
    if ($(window).height() > $('html').height()){
        bottom += $(window).height() - $('html').height();
    }

    var left = ($('html').width() - 940) / 2 + 940;
    $('#gotop').css('left', left);
    $('#gotop').css('bottom', bottom);
}

function showErr(req, msg, errorThrown){
    showMsg("出错了，请重试...");
}

function showMsg(msg) {
    closeLoad();
    if ($("#alertDiv").size() == 0){
        var eTip = document.createElement('div');
        eTip.setAttribute('id', 'alertDiv');
        eTip.style.position = 'absolute';
        eTip.style.display = 'none';
        eTip.style.textAlign = 'center';
        eTip.style.border = 'solid 0px #D1D1D1';
        eTip.style.backgroundColor = '#4B981D';
        eTip.style.padding = '5px 15px';
        eTip.style.left = ($('html').width() - 190) / 2 + 'px';
        eTip.style.top = ($('html').height() / 2) - 50 + 'px';
        eTip.style.height = '50px';
        eTip.style.lineHeight = '50px';
        eTip.style.width = '190px';
        eTip.innerHTML = '<span class="loading">' + msg + '</span>';
        try {
            document.body.appendChild(eTip);
        } catch (e) { }
        $("#alertDiv").css("z-index", "99");
    }

    $('#alertDiv').fadeIn();
    t=setTimeout("$('#alertDiv').fadeOut();clearTimeout(t);",3000)
}

jQuery.cookie = function(name, value, options) {
	if (typeof value != 'undefined') {
		options = options || {};
		if (value === null) {
			value = '';
			options = $.extend({}, options);
			options.expires = -1;
		}
		var expires = '';
		if (options.expires && (typeof options.expires == 'number' || options.expires.toUTCString)) {
			var date;
			if (typeof options.expires == 'number') {
				date = new Date();
				date.setTime(date.getTime() + (options.expires * 24 * 60 * 60 * 1000));
			} else {
				date = options.expires;
			}
			expires = '; expires=' + date.toUTCString();
		}
		var path = options.path ? '; path=' + (options.path) : '';
		var domain = options.domain ? '; domain=' + (options.domain) : '';
		var secure = options.secure ? '; secure' : '';
		document.cookie = [name, '=', encodeURIComponent(value), expires, path, domain, secure].join('');
		} else {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
};

function goTop(){
    $('body').animate({scrollTop: '0px'}, 300);
}

function search(){
    if (event.keyCode == 13){
        var keyword = $('#txtKeyword').val();
        var localUrl = window.location.href;
        var site = localUrl.substr(localUrl.indexOf('//') + 2, localUrl.indexOf('/', 8) - localUrl.indexOf('//') - 2);
        var q = 'site:' + site + ' ' + keyword;
        var url = 'http://www.google.com.hk/search?q=' + q;
        window.open(url);
    }

}