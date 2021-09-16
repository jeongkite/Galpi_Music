function clip(){
	var url = '';
	var textarea = document.createElement("textarea");
	document.body.appendChild(textarea);
	url = window.document.location.href;
	textarea.value = url;
	textarea.select();
	document.execCommand("copy");
	document.body.removeChild(textarea);
	alert("URL이 복사되었습니다.")
}
function share() { 
    var url = encodeURI(encodeURIComponent(myform.url.value)); 
    var title = encodeURI(myform.title.value); 
    var shareURL = "https://share.naver.com/web/shareView.nhn?url=" + url + "&title=" + title; 
    document.location = shareURL; 
}

function shareTwitter() {
    var sendText = "갈피 : 장례식에 흘러나올 내 인생의 주제곡은?"; // 전달할 텍스트
    var sendUrl = window.document.location.href; // 전달할 URL
    window.open("https://twitter.com/intent/tweet?text=" + sendText + "&url=" + sendUrl);
}

function shareFacebook() {
    var sendUrl = window.document.location.href; // 전달할 URL
    window.open("http://www.facebook.com/sharer/sharer.php?u=" + sendUrl);
}

// lottie animation

var q1 = bodymovin.loadAnimation({
    container: document.getElementById('lottie_1'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    path: '/static/js/animation/01.json'
  });
var q2 = bodymovin.loadAnimation({
	container: document.getElementById('lottie_2'),
	renderer: 'svg',
	loop: false,
	autoplay: true,
	path: '/static/js/animation/02.json'
});
var q3 = bodymovin.loadAnimation({
	container: document.getElementById('lottie_3'),
	renderer: 'svg',
	loop: false,
	autoplay: true,
	path: '/static/js/animation/03.json'
});
var q4 = bodymovin.loadAnimation({
    container: document.getElementById('lottie_4'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    path: '/static/js/animation/04.json'
  });
var q5 = bodymovin.loadAnimation({
	container: document.getElementById('lottie_5'),
	renderer: 'svg',
	loop: false,
	autoplay: true,
	path: '/static/js/animation/05.json'
});
var q6 = bodymovin.loadAnimation({
	container: document.getElementById('lottie_6'),
	renderer: 'svg',
	loop: false,
	autoplay: true,
	path: '/static/js/animation/06.json'
});
var q7 = bodymovin.loadAnimation({
	container: document.getElementById('lottie_7'),
	renderer: 'svg',
	loop: false,
	autoplay: true,
	path: '/static/js/animation/07.json'
});
var q8 = bodymovin.loadAnimation({
    container: document.getElementById('lottie_8'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    path: '/static/js/animation/08.json'
  });
var q9 = bodymovin.loadAnimation({
	container: document.getElementById('lottie_9'),
	renderer: 'svg',
	loop: false,
	autoplay: true,
	path: '/static/js/animation/09.json'
});
var q10 = bodymovin.loadAnimation({
	container: document.getElementById('lottie_10'),
	renderer: 'svg',
	loop: false,
	autoplay: true,
	path: '/static/js/animation/10.json'
});
var q11 = bodymovin.loadAnimation({
	container: document.getElementById('lottie_11'),
	renderer: 'svg',
	loop: false,
	autoplay: true,
	path: '/static/js/animation/11.json'
});
var q12 = bodymovin.loadAnimation({
	container: document.getElementById('lottie_12'),
	renderer: 'svg',
	loop: false,
	autoplay: true,
	path: '/static/js/animation/12.json'
});

var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
       slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    
    slides[slideIndex-1].style.display = "block";  
    setTimeout(showSlides, 3500); // Change image every 2 seconds
}

import Kakao from '@/common/plugins/kakao.min'

if (!Kakao.isInitialized()) {
	Kakao.init('fb1e3cb2e854d47e48e2040c2e1ef859')
}

// createDefaultButton 함수 호출
function sendLinkCustom() {
	Kakao.init("fb1e3cb2e854d47e48e2040c2e1ef859");
	Kakao.Link.sendCustom({
		templateId: 61807
	});
}
//<![CDATA[ 
// // 사용할 앱의 JavaScript 키를 설정해 주세요. 
Kakao.init('fb1e3cb2e854d47e48e2040c2e1ef859'); 
// // 카카오링크 버튼을 생성합니다. 처음 한번만 호출하면 됩니다. 
Kakao.Link.createScrapButton({ 
	container: '#kakao-link-btn',
	requestUrl: 'galpi.me', 
	templateId : 61807
}); 
//]]>
