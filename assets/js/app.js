// Add your custom javascript here
console.log("Hi from Federalist");

(function(){
    // Only run if not already on evaluation.gov
  
    const redirectDelay = 100; // milliseconds delay
  
    // This function takes any URL (or href) and extracts everything starting with "evidenceportal"
    // It then returns a new URL with the base "https://evaluation.gov/".
    function buildEvidenceportalUrl(url) {
      const idx = url.indexOf("evidenceportal");
      if (idx === -1) return null;
      const path = url.substring(idx); // e.g. "evidenceportal/completed/" or "evidenceportal/contact"
      return "https://evaluation.gov/" + path;
    }
  
    // This function checks if the current URL contains "evidenceportal"
    // and, if so, builds the new URL and redirects to it (after a brief delay).
    function enforceEvidenceportalRedirect() {
      const currentUrl = window.location.href;
      if (currentUrl.includes("evidenceportal")) {
        const newUrl = buildEvidenceportalUrl(currentUrl);
        if (newUrl && newUrl !== currentUrl) {
          setTimeout(function(){
            window.location.href = newUrl;
          }, redirectDelay);
        }
      }
    }
  
    // Set up event listeners for browser navigation events
    window.addEventListener("popstate", enforceEvidenceportalRedirect);
    window.addEventListener("hashchange", enforceEvidenceportalRedirect);
    window.addEventListener("load", enforceEvidenceportalRedirect);
  
    // Poll periodically in case the URL changes manually or via other scripts.
    setInterval(enforceEvidenceportalRedirect, 200);
  
    // Use a MutationObserver to catch any injected meta refresh tags or DOM changes,
    // and enforce our redirect if any changes occur.
    const observer = new MutationObserver(function(mutations){
      enforceEvidenceportalRedirect();
      mutations.forEach(function(mutation){
        if (mutation.addedNodes) {
          mutation.addedNodes.forEach(function(node) {
            if (node.nodeType === Node.ELEMENT_NODE && node.tagName === "META") {
              const httpEquiv = node.getAttribute("http-equiv");
              if (httpEquiv && httpEquiv.toLowerCase() === "refresh") {
                node.parentNode && node.parentNode.removeChild(node);
              }
            }
          });
        }
      });
    });
    observer.observe(document.documentElement, { childList: true, subtree: true, attributes: true });
  
    // Intercept clicks on any anchor that has "evidenceportal" in its href (except for the special button).
    document.addEventListener("click", function(e){
      let el = e.target;
      while (el && el !== document) {
        if (el.tagName === "A") {
          // Let the special button be handled separately
          if (el.getAttribute("aria-label") === "Evidence Project Portal" && el.getAttribute("tabindex") === "0") {
            return;
          }
          const href = el.getAttribute("href");
          if (href && href.includes("evidenceportal")) {
            e.preventDefault();
            e.stopImmediatePropagation();
            const newUrl = buildEvidenceportalUrl(href);
            if (newUrl) {
              setTimeout(function(){
                window.location.href = newUrl;
              }, redirectDelay);
            }
            return;
          }
        }
        el = el.parentElement;
      }
    }, true);
  
    // Override the special Evidence Project Portal button.
    // It is selected by its attributes: aria-label and tabindex.
    function overrideEvidenceButton(){
      const btn = document.querySelector('a[aria-label="Evidence Project Portal"][tabindex="0"]');
      if (btn) {
        const btnHref = btn.getAttribute("href");
        const newBtnUrl = buildEvidenceportalUrl(btnHref);
        if (newBtnUrl) {
          // Set the href so that "open in new tab" works correctly.
          btn.setAttribute("href", newBtnUrl);
          // Override the click event so that it immediately triggers our forced redirect.
          btn.addEventListener("click", function(e){
            e.preventDefault();
            e.stopImmediatePropagation();
            setTimeout(function(){
              window.location.href = newBtnUrl;
            }, redirectDelay);
          }, true);
        }
      }
    }
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", overrideEvidenceButton);
    } else {
      overrideEvidenceButton();
    }
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
