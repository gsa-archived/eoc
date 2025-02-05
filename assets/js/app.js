// Add your custom javascript here
console.log("Hi from Federalist");

function redirectLinks() {
    console.log('Running redirectLinks...');
    
    document.querySelectorAll('a[href*="/preview/gsa/eoc/feature/OMB-3-Release2.0-Demo/"]').forEach(anchor => {
        let href = anchor.href;
        
        if (href.includes('/preview/gsa/eoc/feature/OMB-3-Release2.0-Demo/')) {
            let newHref = href.split('/preview/gsa/eoc/feature/OMB-3-Release2.0-Demo/')[1];
            if (newHref) {
                let updatedHref = `https://evaluation.gov/${newHref}`;
                anchor.href = updatedHref;
                console.log(`Updated href: ${updatedHref}`);
            }
        }
    });
}

// Run after the DOM is loaded
document.addEventListener("DOMContentLoaded", redirectLinks);

// Run again if new elements are added dynamically
const observer = new MutationObserver(() => {
    redirectLinks();
});

observer.observe(document.body, { childList: true, subtree: true });


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
