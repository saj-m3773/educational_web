$(function() {
    "use strict";

    var o = function() {
        var o = 390,
            n = (window.innerHeight > 0 ? window.innerHeight : this.screen.height) - 1;
        n -= o, 1 > n && (n = 1), n > o && $(".page-wrapper").css("min-height", n + "px")
    };
	
    $(window).ready(o), $(window).on("resize", o), $(function() {
        $('[data-toggle="tooltip"]').tooltip()
    }), $(function() {
        $('[data-toggle="popover"]').popover()
    }), jQuery(document).on("click", ".nav-dropdown", function(o) {
        o.stopPropagation()
    }), jQuery(document).on("click", ".navbar-nav > .dropdown", function(o) {
        o.stopPropagation()
    }), $(".dropdown-submenu").click(function() {
        $(".dropdown-submenu > .dropdown-menu").toggleClass("show")
    }), $("body").trigger("resize");
    var n = $(window);
    n.on("load", function() {
        var o = n.scrollTop(),
            e = $(".topbar");
        o > 100 ? e.addClass("fixed-header animated slideInDown") : e.removeClass("fixed-header animated slideInDown")
    }), $(window).scroll(function() {
        $(window).scrollTop() >= 200 ? ($(".topbar").addClass("fixed-header animated slideInDown"), $(".bt-top").addClass("visible")) : ($(".topbar").removeClass("fixed-header animated slideInDown"), $(".bt-top").removeClass("visible"))
    }), AOS.init(), $(".bt-top").on("click", function(o) {
        o.preventDefault(), $("html,body").animate({
            scrollTop: 0
        }, 700)
    })
	
	// Testimonials
	$("#testimonials").owlCarousel({
		nav: !0,
		dots: !0,
		items: 1,
		center: !0,
		loop: !0,
		navText: ['<i class="fa fa-arrow-left"></i>', '<i class="fa fa-arrow-right"></i>'],
		responsive: {
			1700: {
				stagePadding: 620,
				margin:120
			},
			1430: {
				stagePadding: 320,
				margin:100
			},
			1025: {
				stagePadding: 300,
				margin:80
			},
			768: {
				stagePadding: 150,
				margin:50
			},
			0: {
				stagePadding: 0,
				margin: 0
			}
		}
	})
	
	// Testimonials 2
	$("#testimonials-two").owlCarousel({
		nav: !0,
		dots: !0,
		items: 1,
		center: !0,
		loop: !0,
		navText: ['<i class="fa fa-arrow-left"></i>', '<i class="fa fa-arrow-right"></i>'],
		responsive: {
			1700: {
				stagePadding: 620,
				margin:120
			},
			1430: {
				stagePadding: 320,
				margin:100
			},
			1025: {
				stagePadding:280,
				margin:10
			},
			768: {
				stagePadding: 150,
				margin:50
			},
			0: {
				stagePadding: 0,
				margin: 0
			}
		}
	})
	
	// Company Brand
	$("#company-brand").owlCarousel({
		loop:true,
		autoplay:true,
		nav:false,
		dots:false,
		margin:0,
		responsiveClass:true,
		responsive:{
			0:{
				items:2,
				nav:false
			},
			600:{
				items:3,
				nav:false
			},
			1000:{
				items:6,
				nav:false,
				loop:false
			}
		}
	})

	
	// Ratting
	 $('.rating-opt').start(function(cur){
		console.log(cur);
		 $('#info').text(cur);
	});
	
		    /****---- Portfolio Start ----****/

		$('#portfolio').imagesLoaded(function () {
			$('.portfolio-gallary').isotope({
				itemSelector: '.port-item',
				percentPosition: true,
				masonry: {
					columnWidth: '.port-item'
				}
			});

			$('.portfolio-sort ul li').on("click", function () {
				$('.portfolio-sort ul li').removeClass('active');
				$(this).addClass('active');

				var selector = $(this).attr('data-filter');
				$('.portfolio-gallary').isotope({
					filter: selector
				});
				return false;
			});


			 $('.blog-isotope').imagesLoaded(function () {
				var $blogisotope = $('.blog-isotope').isotope({
					itemSelector: '.blog-iso-item',
					percentPosition: true,
					masonry: {
						columnWidth: '.blog-iso-item'
					}
				});
			});


		});


    /****---- Portfolio End ----****/
	
	/****----- Counter ---------*/
	$('.count').each(function () {
		$(this).prop('Counter',0).animate({
			Counter: $(this).text()
		}, {
			duration: 4000,
			easing: 'swing',
			step: function (now) {
				$(this).text(Math.ceil(now));
			}
		});
	});
	
});



//--------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------


var typed = new Typed('#typed', {
	strings: ['', 'لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده .'],
	loop:false,
	typeSpeed:45// Default value
  });



// -------------------------------------------------------------------------------------------------
//                                           modal
// -------------------------------------------------------------------------------------------------   

const form = document.getElementById('formModal')
const username = document.getElementById('usernameModal')
const email = document.getElementById('emailModal')
const phone = document.getElementById('phoneModal')
const prices = document.getElementById('pricesModal')
const comment = document.getElementById('commentModal')
const button = document.getElementById('buttonModal')

form.addEventListener('submit' , (e)=>{
	e.preventDefault();

	checkInput();
})

function checkInput(){

	const usernameValue = document.getElementById('usernameModal').value.trim();
    const emailValue = document.getElementById('emailModal').value.trim();
    const phoneValue = document.getElementById('phoneModal').value.trim();
    const pricesValue = document.getElementById('pricesModal').value.trim();
    const commentValue = document.getElementById('commentModal').value.trim();

	if(usernameValue==""){
		setError(username , ' نامی برای خود انتخاب کنید.')
	}else{
		setSuccess(username)
	}

	if(emailValue==""){
		setError(email , ' ایمیل خود را وارد کنید')
	}else if(!isEmail(emailValue)){
		setError(email , 'ایمیل نا معتبر می باشد')
	}else{
		setSuccess(email)
	}

	if(phoneValue==""){
		setError(phone, 'شماره تماس خود را وارد کنید')
	}else{
		setSuccess(phone)
	}

	if(prices.options[0].selected==true){
		setError(prices , 'بودجه خود را وارد کنید.')
	}else{
		setSuccess(prices)
	}





}

function setError(input , message){
	const formControl = input.parentElement;
	const span = formControl.querySelector('span')

	span.innerHTML = message;
	formControl.classList.remove('success');
	formControl.classList.add('error');
}

function setSuccess(input){
	const formControl = input.parentElement;
	formControl.classList.remove('error');
	formControl.classList.add('success');
	const span = formControl.querySelector('span')
	span.innerHTML = "";
}

const pattern =  /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

function isEmail(email){
    return pattern.test(email);
}


form.addEventListener('submit', post);

function post(){

	const usernameValue = document.getElementById('usernameModal').value
    const emailValue = document.getElementById('emailModal').value
    const phoneValue = document.getElementById('phoneModal').value
    const pricesValue = $( "#pricesModal option:selected" ).text();
    const commentValue = document.getElementById('commentModal').value

	if(!usernameValue || !emailValue || !phoneValue || prices.options[0].selected==true || !isEmail(emailValue)){
		
    }else{
		fetch('https://jsonplaceholder.typicode.com/posts' ,{method :'POST',
body : JSON.stringify({name:usernameValue , email:emailValue, phone:phoneValue, 
	prices:pricesValue, comment:commentValue}),
	headers:{'Content-Type': 'application/json'}
 }) 
 buttonModal.style.backgroundColor ='green';
 buttonModal.innerHTML ='درخواستتان با موفقیت ثبت شد'
 //setTimeout(function(){location.reload();},2500);
};
	}
	
	
//------------------------------------------------------------------------------------------------------
                                              //
//------------------------------------------------------------------------------------------------------





	


