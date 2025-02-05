// Add your custom javascript here
console.log("Hi from Federalist");

(function(){
    const redirectDelay = 100; // Delay in ms to allow the server to capture the event
  
    // Build a new URL by extracting everything from "evidenceportal" onward
    function buildEvidenceportalUrl(url) {
      const idx = url.indexOf("evidenceportal");
      if (idx === -1) return null;
      const newPath = url.substring(idx); // e.g. "evidenceportal/completed/"
      return "https://evaluation.gov/" + newPath;
    }
  
    // Check the current URL; if it contains "evidenceportal", redirect accordingly
    function enforceEvidenceportalRedirect() {
      const currentUrl = window.location.href;
      if (currentUrl.includes("evidenceportal")) {
        const newUrl = buildEvidenceportalUrl(currentUrl);
        if (newUrl && currentUrl !== newUrl) {
          setTimeout(() => {
            window.location.href = newUrl;
          }, redirectDelay);
        }
      }
    }
  
    // Listen for navigation events and periodically enforce the redirect
    window.addEventListener("popstate", enforceEvidenceportalRedirect);
    window.addEventListener("hashchange", enforceEvidenceportalRedirect);
    window.addEventListener("load", enforceEvidenceportalRedirect);
    setInterval(enforceEvidenceportalRedirect, 200);
  
    // Intercept all click events on <a> elements (except for the special button which is left untouched)
    document.addEventListener("click", function(e) {
      let el = e.target;
      while (el && el !== document) {
        if (el.tagName === "A") {
          // Do not intercept the button with the special attributes
          if (el.getAttribute("aria-label") === "Evidence Project Portal" && el.getAttribute("tabindex") === "0") {
            return;
          }
          const href = el.getAttribute("href");
          if (href && href.includes("evidenceportal")) {
            e.preventDefault();
            e.stopImmediatePropagation();
            const newUrl = buildEvidenceportalUrl(href);
            if (newUrl) {
              setTimeout(() => {
                window.location.href = newUrl;
              }, redirectDelay);
            }
            return;
          }
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
