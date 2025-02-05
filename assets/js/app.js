// Add your custom javascript here
console.log("Hi from Federalist");

(function(){
    let forcedUrl = null;
    let special = false;
    const forcedSpecialUrl = "https://evaluation.gov/evidenceportal";
    
    function buildForcedUrl(href) {
      href = href.trim();
      return href.indexOf(window.location.origin) === 0 ? href : window.location.origin + href;
    }
    
    function enforceForcedUrl() {
      if(special) {
        if(window.location.href !== forcedSpecialUrl) {
          window.history.replaceState({}, '', forcedSpecialUrl);
          window.location.replace(forcedSpecialUrl);
        }
      } else {
        if(forcedUrl && window.location.href !== forcedUrl) {
          window.history.replaceState({}, '', forcedUrl);
          window.location.replace(forcedUrl);
        }
      }
    }
    
    const observer = new MutationObserver(function(mutations) {
      enforceForcedUrl();
      mutations.forEach(function(mutation) {
        if(mutation.addedNodes) {
          mutation.addedNodes.forEach(function(node) {
            if(node.nodeType === Node.ELEMENT_NODE && node.tagName === "META" && node.getAttribute("http-equiv") && node.getAttribute("http-equiv").toLowerCase() === "refresh"){
              node.parentNode && node.parentNode.removeChild(node);
            }
          });
        }
      });
    });
    
    observer.observe(document.documentElement, {
      childList: true,
      subtree: true,
      attributes: true
    });
    
    window.addEventListener("popstate", enforceForcedUrl);
    window.addEventListener("load", enforceForcedUrl);
    
    document.addEventListener("click", function(e) {
      let el = e.target;
      while(el && el !== document) {
        if(el.tagName === "A"){
          if(el.getAttribute("aria-label") === "Evidence Project Portal" && el.getAttribute("tabindex") === "0"){
            special = true;
            forcedUrl = forcedSpecialUrl;
          } else {
            special = false;
            let href = el.getAttribute("href");
            if(href) forcedUrl = buildForcedUrl(href);
          }
          e.preventDefault();
          e.stopImmediatePropagation();
          if(forcedUrl) {
            window.history.replaceState({}, '', forcedUrl);
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
