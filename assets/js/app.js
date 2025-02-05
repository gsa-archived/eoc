// Add your custom javascript here
console.log("Hi from Federalist");

(function(){
    let forcedUrl = null;
    function buildForcedUrl(href){
      href = href.trim();
      return href.indexOf(window.location.origin) === 0 ? href : window.location.origin + href;
    }
    function disableEverything(){
      EventTarget.prototype.addEventListener = function(){};
      EventTarget.prototype.removeEventListener = function(){};
      window.setTimeout = function(){};
      window.setInterval = function(){};
      window.requestAnimationFrame = function(){};
      document.onclick = null;
      document.onmousedown = null;
      document.onmouseup = null;
      document.onmousemove = null;
      ['click','dblclick','mousedown','mouseup','mousemove','touchstart','touchmove','touchend','keydown','keyup','keypress','wheel','scroll','contextmenu'].forEach(ev => {
        window.addEventListener(ev, e => { e.stopImmediatePropagation(); e.preventDefault(); }, true);
        document.addEventListener(ev, e => { e.stopImmediatePropagation(); e.preventDefault(); }, true);
      });
      if(document.documentElement){
        document.documentElement.innerHTML = '';
      }
    }
    document.addEventListener('click', e => {
      let el = e.target;
      while(el && el !== document){
        if(el.tagName === 'A'){
          const href = el.getAttribute('href');
          if(href && !href.startsWith('javascript:')){
            e.preventDefault();
            e.stopImmediatePropagation();
            forcedUrl = buildForcedUrl(href);
            disableEverything();
            window.location.replace(forcedUrl);
          }
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
