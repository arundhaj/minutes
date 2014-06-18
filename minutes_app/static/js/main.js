// Get all items
var items_discussed_input = $("#items_discussed_input"),
    items_discussed_preview = $('#items_discussed_preview'),
    decisions_made_input = $("#decisions_made_input"),
    decisions_made_preview = $('#decisions_made_preview'),
    action_items_input = $("#action_items_input"),
    action_items_preview = $('#action_items_preview');

// Load for the first time during page load
$(document).ready(function() {
	if($.trim(items_discussed_input.val()).length > 0){
		items_discussed_preview.html(marked(items_discussed_input.val()));
	}
	if($.trim(decisions_made_input.val()).length > 0){
		decisions_made_preview.html(marked(decisions_made_input.val()));
	}
	if($.trim(action_items_input.val()).length > 0){
		action_items_preview.html(marked(action_items_input.val()));
	}

	items_discussed_input.hide();
    decisions_made_input.hide();
    action_items_input.hide();
    items_discussed_preview.show();
    decisions_made_preview.show();
    action_items_preview.show();
});

$("#momFormSubmitButton").bind('click', function(event) {
    var title = $("#id_title");
    var email = $("#id_email");

    var emailRegEx = /^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
    var validTitle = true, validEmail = true;

    if($.trim(title.val()).length == 0) {
    	validTitle = false;
    }
    
    title.attr("stat", !validTitle ? "error" : "normal");
    
//    if($.trim(email.val()).length == 0 || !emailRegEx.test(email.val())) {
//        validEmail = false;
//    }

//    email.attr("stat", !validEmail ? "error" : "normal");
    
    if(!validTitle) {
    	return;
    }

    $("#momForm").submit();
});

$("#momFormNewButton").bind('click', function(event) {
	window.location.replace("/");
});

$("#momFormPrintButton").bind('click', function(event) {
	window.print();
});

$("#momFormEmailButton").bind('click', function(event) {
	alert('yet to implement.');
});

$("#momFormDeleteButton").bind('click', function(event) {
	alert('yet to implement.');
});

// http://www.malot.fr/bootstrap-datetimepicker/index.php
$(".form_datetime").datetimepicker(
	{
		format: 'yyyy-mm-dd hh:ii',
		autoclose: true,
        todayBtn: true,
    }
);

/*
var items_discussed_delay = null;
items_discussed_input.off('keyup').on('keyup', function(e) {
    var el = $(this);
    if (items_discussed_delay) clearTimeout(items_discussed_delay);
    items_discussed_delay = setTimeout(function() {
        items_discussed_preview.html(marked(el.val()));
    }, 200);
});

var decisions_made_delay = null;
decisions_made_input.off('keyup').on('keyup', function(e) {
    var el = $(this);
    if (decisions_made_delay) clearTimeout(decisions_made_delay);
    decisions_made_delay = setTimeout(function() {
        decisions_made_preview.html(marked(el.val()));
    }, 200);
});

var action_items_delay = null;
action_items_input.off('keyup').on('keyup', function(e) {
    var el = $(this);
    if (action_items_delay) clearTimeout(action_items_delay);
    action_items_delay = setTimeout(function() {
        action_items_preview.html(marked(el.val()));
    }, 200);
});
*/

$(".marktip").popover({ 
    title: "<div style='color:black;'>Markdown quick help</div",
    html: true,
    content: "<div style='color:black;'># header <br />*italics* <br />**bold** <br />* list1 <br />* list2</div>"
});

var input, preview;
$("#items_discussed_preview").dblclick(function(e) {
    input = items_discussed_input;
    preview = items_discussed_preview;
    items_discussed_input.show();
    items_discussed_input.focus();
    items_discussed_preview.hide();

    e.stopPropagation();
});

$("#decisions_made_preview").dblclick(function(e) {
    input = decisions_made_input;
    preview = decisions_made_preview;
    decisions_made_input.show();
    decisions_made_input.focus();
    decisions_made_preview.hide();

    e.stopPropagation();
});

$("#action_items_preview").dblclick(function(e) {
    input = action_items_input;
    preview = action_items_preview;
    action_items_input.show();
    action_items_input.focus();
    action_items_preview.hide();
});

$(document.body).mousedown(function(event) {
    var target = $(event.target);
    if (input!= null && !target.parents().andSelf().is(input)) { // Clicked outside
        input.hide();
        preview.html(marked(input.val()));
        preview.show();
        input = preview = null;
    }
});