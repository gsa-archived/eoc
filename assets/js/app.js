// Add your custom javascript here
console.log("Hi from Federalist");


(function(){
    console.log('in new');
  
    function overrideEvidenceButton(){
      const btn = document.querySelector('a[aria-label="Evidence Project Portal"][tabindex="0"]');
      if (btn) {
        btn.setAttribute("href", forcedSpecialUrl);
        btn.addEventListener("click", function(e) {
          e.preventDefault();
          e.stopImmediatePropagation();
          setTimeout(() => {
            window.location.href = forcedSpecialUrl;
          }, redirectDelay);
        }, true);
      }
    }
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", overrideEvidenceButton);
    } else {
      overrideEvidenceButton();
    }
  
    document.addEventListener("click", function(e) {
      let el = e.target;
      while (el && el !== document) {
        if (el.tagName === "A") {
          const href = el.getAttribute("href");
          if (href && href.includes("evidenceportal")) {
            e.preventDefault();
            e.stopImmediatePropagation();
            setTimeout(() => {
              window.location.href = forcedSpecialUrl;
            }, redirectDelay);
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
