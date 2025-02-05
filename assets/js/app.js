// Add your custom javascript here
console.log("Hi from Federalist");

(function(){
    let forcedUrl = null;
    let locked = false;
    function buildForcedUrl(href) {
      href = href.trim();
      return href.indexOf(window.location.origin) === 0 ? href : window.location.origin + href;
    }
    const originalAssign = window.location.assign;
    const originalReplace = window.location.replace;
    window.location.assign = function(url){
      if(locked && forcedUrl){
        originalReplace.call(window.location, forcedUrl);
      } else {
        originalAssign.call(window.location, url);
      }
    };
    window.location.replace = function(url){
      if(locked && forcedUrl){
        originalReplace.call(window.location, forcedUrl);
      } else {
        originalReplace.call(window.location, url);
      }
    };
    document.addEventListener("click", function(e){
      let el = e.target;
      while(el && el !== document){
        if(el.tagName === "A"){
          if(el.getAttribute("aria-label") === "Evidence Project Portal" && el.getAttribute("tabindex") === "0"){
            forcedUrl = "https://evaluation.gov/evidenceportal";
            locked = true;
            e.preventDefault();
            e.stopImmediatePropagation();
            el.setAttribute("href", forcedUrl);
            window.location.replace(forcedUrl);
            return;
          }
          let href = el.getAttribute("href");
          if(href){
            forcedUrl = buildForcedUrl(href);
            locked = true;
            e.preventDefault();
            e.stopImmediatePropagation();
            window.location.replace(forcedUrl);
            return;
          }
        }
        el = el.parentElement;
      }
    }, true);
    setInterval(function(){
      if(locked && forcedUrl && window.location.href !== forcedUrl){
        window.location.replace(forcedUrl);
      }
    }, 100);
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
