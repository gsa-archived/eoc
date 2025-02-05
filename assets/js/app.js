// Add your custom javascript here
console.log("Hi from Federalist");

const BASE_URL = 'https://evaluation.gov';

function redirectLinks(link) {
  const rawHref = link.getAttribute("href");
  if (!rawHref) return;
  const normalizedPath = rawHref.startsWith('/') ? rawHref : '/' + rawHref;
  const fallback = BASE_URL + normalizedPath;
  if (link.target === '_blank') window.open(fallback, "_blank");
  else window.location.href = fallback;
}

document.addEventListener("click", (event) => {
  const link = event.target.closest("a");
  if (!link) return;
  event.preventDefault();
  redirectLinks(link);
}, true);


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
