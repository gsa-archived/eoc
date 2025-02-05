// Add your custom javascript here
console.log("Hi from Federalist");

(function() {
    // This variable stores the URL we want to enforce.
    let forcedUrl = null;
  
    // Helper: Build a URL from the window origin and a relative path (assumes href is relative)
    function buildForcedUrl(href) {
      // Remove any accidental whitespace
      href = href.trim();
      // If href already starts with window.location.origin, assume it's already correct.
      if (href.indexOf(window.location.origin) === 0) {
        return href;
      }
      // Otherwise, force it to use window.location.origin + href.
      return window.location.origin + href;
    }
  
    // Override navigation functions so that any call to them is forced
    const originalAssign = window.location.assign;
    const originalReplace = window.location.replace;
  
    window.location.assign = function(url) {
      forcedUrl = buildForcedUrl(url);
      console.log("[Redirect Override] Intercepted location.assign; forcing URL to:", forcedUrl);
      // Use replace to avoid creating extra history entries.
      originalReplace.call(window.location, forcedUrl);
    };
  
    window.location.replace = function(url) {
      forcedUrl = buildForcedUrl(url);
      console.log("[Redirect Override] Intercepted location.replace; forcing URL to:", forcedUrl);
      originalReplace.call(window.location, forcedUrl);
    };
  
    // Aggressively intercept all clicks in the capture phase
    document.addEventListener('click', function(event) {
      let el = event.target;
  
      // Walk up the DOM tree in case the click is on a child inside an <a> element
      while (el && el !== document) {
        if (el.tagName === 'A') {
          const href = el.getAttribute('href');
          if (href && !href.startsWith('javascript:')) {
            // Stop other listeners and prevent default navigation
            event.preventDefault();
            event.stopImmediatePropagation();
  
            forcedUrl = buildForcedUrl(href);
            console.log("[Redirect Override] Click intercepted; forcing navigation to:", forcedUrl);
            // Use replace to force navigation immediately.
            originalReplace.call(window.location, forcedUrl);
          }
          break; // we've handled the link click
        }
        el = el.parentElement;
      }
    }, true); // capture phase ensures we run before others
  
    // Polling: Every 50ms check if the URL is not what we expect, and if not, reapply it.
    setInterval(function() {
      if (forcedUrl && window.location.href !== forcedUrl) {
        console.log("[Redirect Override] Detected URL change; reverting to forced URL:", forcedUrl);
        // Use replace to override any unwanted changes
        originalReplace.call(window.location, forcedUrl);
      }
    }, 50);
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
