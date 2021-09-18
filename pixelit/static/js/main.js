(function ($) {
 "use strict";
 
// $(document).ready(function(){
    $(".search_btn").click(function(){
        $('.course-search').fadeIn(100);
    });
	$(".close_searchBar").click(function(){
        $(this).parent().fadeOut(100);
    });
	$(".profile_drop_btn").click(function(){
        $('.profile_dropDown').slideToggle(300);
    });
	// $(".close_searchBar").click(function(){
    //     $(this).parent().fadeOut(100);
    // });
// });

// Login & Registration 

	$('.input_group input').focus(function() {
		$(this).parent().children('span.underline').css({
			"transform": "scale(1)"
		})
	});

	$('.input_group input').blur(function() {
			$(this).parent().children('span.underline').css({
				"transform": "scale(0, 1)"
			})
		});

	$('input').after('<span class="underline"></span>')

/*--------------------------
mobile-menu
---------------------------- */	
//$('#mobile-menu').mmenu();

/*---------------------
menu-stick
--------------------- */
var s = $("#sticker");
var pos = s.position();					   
$(window).on('scroll',function() {
	var windowpos = $(window).scrollTop();
	if (windowpos > pos.top) {
	s.addClass("stick");
	} else {
		s.removeClass("stick");	
	}
});
/*--------------------------
scrollUp
---------------------------- */	
$.scrollUp({
	scrollText: '<i class="fa fa-angle-up"></i>',
	easingType: 'linear',
	scrollSpeed: 900,
	animation: 'slide'
});
/*--------------------------
course-carousel
---------------------------- */
$(".course-carousel").slick({
  dots: true,
  arrows:true,
  infinite: true,
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 4,
  autoPlay: true,
  adaptiveHeight: true,
  prevArrow: '<i class="fa fa-angle-left"></i>',
  nextArrow: '<i class="fa fa-angle-right"></i>',
	responsive: [
		{
			breakpoint: 1169,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 3
			}
		},
		{
			breakpoint: 769,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 2,
			}
		},
		{
			breakpoint: 481,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1,
			}
		},
	]
});
/*----------------------------
 cart-plus-minus-button
------------------------------ */  
$(".qtybutton").on("click", function() {
	var $button = $(this);
	var oldValue = $button.parent().find("input").val();

	if ($button.text() == "+") {
	  var newVal = parseFloat(oldValue) + 1;
	} else {
		// Don't allow decrementing below zero
		if (oldValue > 0) {
			var newVal = parseFloat(oldValue) - 1;
		} else {
			newVal = 0;
		}
	}
	
	$button.parent().find("input").val(newVal);
});
})(jQuery); 