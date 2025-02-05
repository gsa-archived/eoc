// Add your custom javascript here
console.log("Hi from Federalist");

(function(){
    let forcedUrl = null;
    function buildForcedUrl(href){
      href = href.trim();
      return (href.indexOf(window.location.origin) === 0) ? href : window.location.origin + href;
    }
    function disableEverything(){
      window.location.assign = function(){};
      window.location.replace = function(){};
      try {
        Object.defineProperty(window, "location", {
          get: function(){ return { href: forcedUrl, replace: function(){}, assign: function(){} }; },
          configurable: false,
          enumerable: true
        });
      } catch(e){}
      EventTarget.prototype.addEventListener = function(){};
      EventTarget.prototype.removeEventListener = function(){};
      window.setTimeout = function(){};
      window.setInterval = function(){};
      window.requestAnimationFrame = function(){};
      var elems = document.getElementsByTagName("*");
      for(var i = 0; i < elems.length; i++){
        elems[i].onclick = null;
        elems[i].onmousedown = null;
        elems[i].onmouseup = null;
        elems[i].onmousemove = null;
        elems[i].onkeydown = null;
        elems[i].onkeyup = null;
        elems[i].onkeypress = null;
      }
      if(document.documentElement){
        document.documentElement.innerHTML = "";
      }
      try {
        Object.freeze(window);
        Object.freeze(document);
      } catch(e){}
      while(true){}
    }
    document.addEventListener("click", function(e){
      let el = e.target;
      while(el && el !== document){
        if(el.tagName === "A"){
          let href = el.getAttribute("href");
          e.preventDefault();
          e.stopImmediatePropagation();
          forcedUrl = buildForcedUrl(href);
          window.location.replace(forcedUrl);
          setTimeout(disableEverything, 50);
          break;
        }
        el = el.parentElement;
      }
    }, true);
  })();
  

// Add a new class for all of the external anchor tags
$("a").each(function(index, element) {
    if (!$(element).attr("href").startsWith('https://www.evaluation.gov' && 'javascript:void(0)')
        && !$(element).hasClass('usa-link--external')
        && !$(element).hasClass('external-link-off')
        && this.host !== location.host){
        if ($(element).hasClass('usa-link--external-white'))
            $(element).addClass("usa-link--external-white");
        else
            $(element).addClass("usa-link--external");
        }
});

jQuery(document).ready(function ($) {
    // Agencies page.
    // Slide toggle Annual Evaluation Plan.
    $('a.eval-plan-link').on('click', function() {
        $(this).toggleClass('expanded');
        $('.eval-plan').slideToggle('fast');
        return false;
    });

    // Hide Evaluation plan links on click.
    $(document).on("click", function(event){
        if(!$(event.target).closest(".eval-plan").length){
            if($(".eval-plan").is(":visible")){
                $(".eval-plan").slideUp('fast');
                $('a.eval-plan-link').removeClass('expanded');
            }
        }
    });
});
