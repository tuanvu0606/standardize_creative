var adDiv;

var stepDelay = 29;
var step = 1;
var stepCount = 0;
var newEF = 1;
var fps = 50;
var now;
var then = Date.now();
var interval = 1000/fps;
var delta;

var getUriParams = function() {
		var query_string = {}
		var query = window.location.search.substring(1);
		var parmsArray = query.split('&');
		if(parmsArray.length <= 0) return query_string;
		for(var i = 0; i < parmsArray.length; i++) {
			var pair = parmsArray[i].split('=');
			var val = decodeURIComponent(pair[1]);
			if (val != '' && pair[0] != '') query_string[pair[0]] = val;
		}
		return query_string;
	}();



function IsImageOk(img) { 

if (!img.complete) { 
  return false; 
}

return true; 
}


function checkImages() { 
var ok = 1;
var sum = document.images.length;
var ss = 0;
for (var i = 0; i < document.images.length; i++) { 
  if (!IsImageOk(document.images[i])) {
  
  }  else ss++;
} 


if (sum==ss) ok = 1; else ok = 0;
return ok;
}

window.onload = function() {
  var iid = setInterval(function(){
    if (checkImages()) {
	   clearInterval(iid);
	   startAd();
	}
  }, 100);

  
};


function startAd() {
    adDiv = document.getElementById("ad");

    addEventListeners();

	step = 2;
	
	if(typeof requestAnimationFrame === 'undefined') newEF = 0;

	if (newEF) requestAnimationFrame(fun1); else
	setTimeout(fun1, interval);

	function fun1() {
		now = Date.now();
		delta = now - then;
		
		//console.log(interval+" "+delta+" "+newEF);
		
		if (delta > interval || !newEF) {         
			then = now - (delta % interval);
			
			enterFrame();
			
			if (!newEF) setTimeout(fun1,interval);
	   }
	   
	   if (newEF) requestAnimationFrame(fun1); 
	}
	
	init();
}

function addEventListeners() {
    document.getElementById("inv-button").addEventListener("click", clickthrough);
}

function clickthrough() {
    console.log("click");
    window.open( clickTag,"_blank");
}



var tweens = new Array();
var x = 0;
	var delay = 2.9;
	var delay3 = 1.4;
	var delay2 = 1;
	var loop1 = 1;
	var rpos = 170;

function init() {
    var i;


	var tl = new TimelineLite({
		onComplete: function() {
			if (loop1) {
				TweenMax.delayedCall(2,function() {
					TweenMax.fromTo("#bg2,#wave2",.6,{},{opacity:1,ease:Power1.easeInOut, onComplete: function() {
						TweenMax.set("#bg2,#wave2",{opacity:0});
						tl.restart();
						loop1--;
					}});
				});
			}
		}
	});

	
	document.getElementById("ad").style.display = "block"; 
	
	TweenMax.set("#h1,#h2,#h3,#h4,#h5",{transformOrigin:"46% 50%"});
	
	TweenMax.set("#hro",{left:292,top:-18,transformOrigin: "11px 91px",opacity:1,scale:.8});
	
	TweenMax.set("#hro",{rotation:-180,y:-100,x:-55,scale:1.2});
	TweenMax.set("#hr",{rotation:-180});

	
	tl
	  .fromTo("#love",.9,{left:0},{opacity:1,ease:Power1.easeInOut},'.0')
	  .fromTo("#textd",.9,{left:0},{opacity:1,ease:Power1.easeInOut},'-=.7')
	  .fromTo("#heart",.9,{scale:.5},{opacity:1,scale:1,ease:Back.easeInOut},'-=.5')
	  .fromTo("#feb1,#feb2",.6,{scale:5,x:-100,y:-100,left:10},{x:0,y:0,opacity:1,scale:1,ease:Power4.easeInOut},'-=.2')
	  .fromTo("#h1",.5,{scale:.2},{opacity:1,scale:1,ease:Power2.easeOut},'-=.2')
	  .fromTo("#h2",.5,{scale:.2},{opacity:1,scale:1,ease:Power2.easeOut},'-=.49')
	  .fromTo("#h3",.5,{scale:.2},{opacity:1,scale:1,ease:Power2.easeOut},'-=.5')
	  .fromTo("#h4",.5,{scale:.2},{opacity:1,scale:1,ease:Power2.easeOut},'-=.49')
	  .fromTo("#h5",.5,{scale:.2},{opacity:1,scale:1,ease:Power2.easeOut},'-=.49')
	  .to("#feb1",.6,{rotation:360,ease:Power2.easeInOut},'-=.5')
	  
	  .fromTo("#a1",.4,{},{opacity:1,ease:Power1.easeInOut},'+=.0')
	  .to("#a1",.3,{opacity:0},'+=.7')
	  .fromTo("#b1",.6,{},{opacity:1,ease:Power1.easeInOut},'-=.3')
	  .to("#b1",.3,{opacity:0},'+=.7')
	  
      .to("#hro",2,{scale:.8,y:0,x:0,rotation:-360*3+180,ease:Linear.easeNone},"+=0")
	  .to("#hr",2,{rotation:-360*3+180,ease:Linear.easeNone},"-=2")
      .to("#hro",1.2,{scale:.8,y:0,rotation:-360*3,ease:Power2.easeOut},"+=0")
	  .to("#hr",1.6,{rotation:-360*3,ease:Power2.easeOut},"-=1.2")
	  
	  .fromTo("#a1",.6,{},{opacity:1,ease:Power1.easeInOut},'+=.0')
	  .to("#a1",.3,{opacity:0},'+=.7')
	  .fromTo("#b1",.6,{},{opacity:1,ease:Power1.easeInOut},'-=.5')
	  .to("#b1",.3,{opacity:0},'+=.7')
	;
}

function repeat() {
  var i;
  for (i=0;i<tweens.length;i++){
    tweens[i].pause(0);
  }
  
  
}

function enterFrame() {
}
