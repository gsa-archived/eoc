// Add your custom javascript here
console.log("Hi from Federalist");

(function() {

    let forcedUrl = null;
  
    function buildForcedUrl(href) {
      href = href.trim();
  
      if (href.indexOf(window.location.origin) === 0) {
        return href;
      }
      return window.location.origin + href;
    }
  
    const originalAssign  = window.location.assign;
    const originalReplace = window.location.replace;
    const originalPush    = history.pushState;
    const originalReplaceState = history.replaceState;
  
    window.location.assign = function(url) {
      forcedUrl = buildForcedUrl(url);
      console.log("[Override] location.assign intercepted. Forcing URL:", forcedUrl);
      originalReplace.call(window.location, forcedUrl);
    };
  
    window.location.replace = function(url) {
      forcedUrl = buildForcedUrl(url);
      console.log("[Override] location.replace intercepted. Forcing URL:", forcedUrl);
      originalReplace.call(window.location, forcedUrl);
    };
  
    history.pushState = function(state, title, url) {
      if (url) {
        forcedUrl = buildForcedUrl(url);
        console.log("[Override] history.pushState intercepted. Forcing URL:", forcedUrl);
        originalReplace.call(window.location, forcedUrl);
      } else {
  
        originalPush.apply(history, arguments);
      }
    };
  
    history.replaceState = function(state, title, url) {
      if (url) {
        forcedUrl = buildForcedUrl(url);
        console.log("[Override] history.replaceState intercepted. Forcing URL:", forcedUrl);
        originalReplace.call(window.location, forcedUrl);
      } else {
        originalReplaceState.apply(history, arguments);
      }
    };
  
    document.addEventListener('click', function(event) {
      let el = event.target;
  
      while (el && el !== document) {
        if (el.tagName === 'A') {
          const href = el.getAttribute('href');
          if (href && !href.startsWith('javascript:')) {
            event.preventDefault();
            event.stopImmediatePropagation();
            forcedUrl = buildForcedUrl(href);
            console.log("[Override] Click intercepted. Forcing navigation to:", forcedUrl);
  
            originalReplace.call(window.location, forcedUrl);
          }
          break;
        }
        el = el.parentElement;
      }
    }, true);
  
    const observer = new MutationObserver((mutationsList) => {
  
      if (forcedUrl && window.location.href !== forcedUrl) {
        console.log("[Override] MutationObserver: Detected location change. Forcing back to:", forcedUrl);
        originalReplace.call(window.location, forcedUrl);
      }
  
      mutationsList.forEach((mutation) => {
        if (mutation.type === 'childList') {
          mutation.addedNodes.forEach((node) => {
            if (node.nodeType === Node.ELEMENT_NODE) {
              const el = node;
              if (
                el.tagName === 'META' &&
                el.getAttribute('http-equiv') &&
                el.getAttribute('http-equiv').toLowerCase() === 'refresh'
              ) {
                console.log("[Override] MutationObserver: Removing injected meta refresh tag.");
                el.parentNode && el.parentNode.removeChild(el);
              }
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
  
    window.addEventListener('popstate', function() {
      if (forcedUrl && window.location.href !== forcedUrl) {
        console.log("[Override] popstate event detected. Forcing URL:", forcedUrl);
        originalReplace.call(window.location, forcedUrl);
      }
    });
  
    setInterval(() => {
      if (forcedUrl && window.location.href !== forcedUrl) {
        console.log("[Override] setInterval check: Detected URL mismatch. Forcing URL:", forcedUrl);
        originalReplace.call(window.location, forcedUrl);
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
