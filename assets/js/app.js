// Add your custom javascript here
console.log("Hi from Federalist");

(function() {
    // Attach the listener in the capture phase
    document.addEventListener(
      'click',
      function(event) {
        let element = event.target;
        while (element && element !== document) {
          if (element.tagName === 'A') {
            const href = element.getAttribute('href');
            
            if (href && !href.startsWith('javascript:')) {
              event.preventDefault();
              event.stopImmediatePropagation();
              window.location.href = window.location.origin + href;
            }
            break;
          }
          element = element.parentElement;
        }
      },
      true
    );
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
