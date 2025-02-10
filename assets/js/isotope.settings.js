// Filter based on two factors + alphabetical sort
// Uses URI hash as trigger allowing direct links etc
// Losely based on: http://isotope.metafizzy.co/filtering.html#url-hash

jQuery(document).ready(function ($) {
    var link = window.location.href;


    if (link.indexOf("/resources/") != -1) {
        var $container = $(".resources");
    } else if (link.indexOf("/news/") != -1) {
        var $container = $(".news");
    }

    if ($container !== undefined) {

        // Filter isotope
        $container.isotope({
            // options
            itemSelector: ".policy",
            layoutMode: "masonry",
            getSortData: {
                date: "p"
            }
        });

        var iso = $container.data('isotope');
        var $filterCount = $('.filter-count');
        function updateFilterCount() {
            if (iso != null) {
                $filterCount.text(iso.filteredItems.length + ' items');
            }
        }

        // Alphabetical sort
        // Sort items alphabetically based on course title
        var sortValue = false;
        $(".sort").on("click", function () {
            // Get current URI hash
            var currentHash = location.hash;
            // If button is currently unchecked:
            if ($(this).hasClass("checked")) {
                // Set sort to false
                sortValue = false;
                // Remove sort attribute in hash
                location.hash = currentHash.replace(/&sort=([^&]+)/i, "");
            } else {
                // Set sortValue to current sort value
                sortValue = $(this).attr("data-sort-value");
                // Add sort attribute to hash
                location.hash = currentHash + "&sort=" + encodeURIComponent(sortValue);
            }
        });

        // Set up filters array with default values
        var filters = {};
        // When a button is pressed, run filterSelect
        $(".filter-list a").on("click", filterSelect);
        // Set the URI hash to the current selected filters
        function filterSelect() {
            // Current hash value
            var hashFilter = getHashFilter();
            // Set filters to current values (important for first run)
            if (link.indexOf("/resources/") != -1) {
                filters["resource"] = hashFilter["resource"];
                filters["role"] = hashFilter["role"];
                filters["content"] = hashFilter["content"];
                filters["year"] = hashFilter["year"];
                filters["historical"] = hashFilter["historical"];
                // data-filter attribute of clicked button
                var currentFilter = $(this).attr("data-filter");
                // Navigation group (subject or role) as object
                var $navGroup = $(this).parents(".filter-list");
        
                // data-filter-group key for the current nav group
                var filterGroup = $navGroup.attr("data-filter-group");
                // If the current data-filter attribute matches the current filter,
                if (currentFilter == hashFilter["resource"] || currentFilter == hashFilter["role"] || currentFilter == hashFilter["content"] || currentFilter == hashFilter["year"] || currentFilter == ".historical") {
                    // Reset group filter as the user has unselected the button
                    filters[filterGroup] = "*";
                } else {
                    // Set data-filter of current button as value with filterGroup as key
                    filters[filterGroup] = $(this).attr("data-filter");
                }
        
                // Toggle historical filter
                if ($(this).attr("id") === "filter-list-not-archived") {
                    filters["historical"] = (hashFilter["historical"] === "true") ? "false" : "true";
                }
        
                // Create new hash
                var newHash = "resource=" + filters["resource"] + "&role=" + filters["role"] + "&content=" + filters["content"] + "&year=" + filters["year"] + "&historical=" + filters["historical"];
                // If sort value exists, add it to hash
                if (sortValue) {
                    newHash = newHash + "&sort=" + encodeURIComponent(sortValue);
                }
                // Apply the new hash to the URI, triggering onHashchange()
                location.hash = newHash;
            } else if (link.indexOf("/news/") != -1) {
                filters["content"] = hashFilter["content"];
                // data-filter attribute of clicked button
                var currentFilter = $(this).attr("data-filter");
        
                // Navigation group (subject or role) as object
                var $navGroup = $(this).parents(".filter-list");
                // data-filter-group key for the current nav group
                var filterGroup = $navGroup.attr("data-filter-group");
                // If the current data-filter attribute matches the current filter,
                if (currentFilter == hashFilter["content"]) {
                    // Reset group filter as the user has unselected the button
                    filters[filterGroup] = "*";
                } else {
                    // Set data-filter of current button as value with filterGroup as key
                    filters[filterGroup] = $(this).attr("data-filter");
                }
                // Create new hash
                var newHash = "content=" + filters["content"];
                // If sort value exists, add it to hash
                if (sortValue) {
                    newHash = newHash + "&sort=" + encodeURIComponent(sortValue);
                }
                location.hash = newHash;
            }
        } // filterSelect

        function onHashChange() {
            // Current hash value
            var hashFilter = getHashFilter();
            // Concatenate subject and role for Isotope filtering
            if (link.indexOf("/resources/") != -1) {
                var theFilter = hashFilter["resource"] + hashFilter["role"] + hashFilter["content"] + hashFilter["year"];
        
                // By default, exclude historical documents unless explicitly enabled
                if (hashFilter["historical"] !== "true") {
                    theFilter += ":not(.historical)";
                    $("#filter-list-not-archived").removeClass("checked").attr("aria-checked", "false");
                } else {
                    $("#filter-list-not-archived").addClass("checked").attr("aria-checked", "true");
                }
        
                if (hashFilter) {
                    // Repaint Isotope container with current filters and sorts
                    $container.isotope({
                        filter: decodeURIComponent(theFilter),
                        sortBy: hashFilter["sorts"]
                    });
        
                    updateFilterCount();
                    // Toggle checked status of sort button
                    if (hashFilter["sorts"]) {
                        $(".sort").addClass("checked");
                    } else {
                        $(".sort").removeClass("checked");
                    }
                    // Toggle checked status of filter buttons
                    $(".filter-list").find(".checked").removeClass("checked").attr("aria-checked", "false");
                    var resourceFilters = hashFilter["resource"].split(",");
                    var roleFilters = hashFilter["role"].split(",");
                    var contentFilters = hashFilter["content"].split(",");
                    var yearFilters = hashFilter["year"].split(",");
                    var historicalFilters = hashFilter["historical"] === "true" ? [".historical"] : [];
                    var allFilters = resourceFilters.concat(roleFilters, contentFilters, yearFilters, historicalFilters);
                    for (filter in allFilters) {
                        $(".filter-list").find("[data-filter='" + allFilters[filter] + "']").addClass("checked").attr("aria-checked", "true");
                    }
                }
                //News Page
            } else if (link.indexOf("/news/") != -1) {
                var theFilter = hashFilter["content"];
        
                if (hashFilter) {
                    // Repaint Isotope container with current filters and sorts
                    $container.isotope({
                        filter: decodeURIComponent(theFilter),
                        sortBy: hashFilter["sorts"]
                    });
        
                    updateFilterCount();
                    // Toggle checked status of sort button
                    if (hashFilter["sorts"]) {
                        $(".sort").addClass("checked");
                    } else {
                        $(".sort").removeClass("checked");
                    }
                    // Toggle checked status of filter buttons
                    $(".filter-list").find(".checked").removeClass("checked").attr("aria-checked", "false");
                    var allFilters = hashFilter["content"].split(",");
                    for (filter in allFilters) {
                        $(".filter-list").find("[data-filter='" + allFilters[filter] + "']").addClass("checked").attr("aria-checked", "true");
                    }
                }
            }
        } // onHahschange

        function getHashFilter() {
            if (link.indexOf("/resources/") != -1) {
                // Get filters (matches) and sort order (sorts)
                var resource = location.hash.match(/resource=([^&]+)/i);
                var role = location.hash.match(/role=([^&]+)/i);
                var content = location.hash.match(/content=([^&]+)/i);
                var year = location.hash.match(/year=([^&]+)/i);
                var historical = location.hash.match(/historical=([^&]+)/i);
                var sorts = location.hash.match(/sort=([^&]+)/i);
        
                // Set up a hashFilter array
                var hashFilter = {};
                // Populate array with matches and sorts using ternary logic
                hashFilter["resource"] = resource ? resource[1] : "*";
                hashFilter["role"] = role ? role[1] : "*";
                hashFilter["content"] = content ? content[1] : "*";
                hashFilter["year"] = year ? year[1] : "*";
                hashFilter["historical"] = historical ? historical[1] : "false"; // Default to false (hidden)
                hashFilter["sorts"] = sorts ? sorts[1] : "";
        
                return hashFilter;
            } else if (link.indexOf("/news/") != -1) {
                // Get filters (matches) and sort order (sorts)
                var content = location.hash.match(/content=([^&]+)/i);
                var sorts = location.hash.match(/sort=([^&]+)/i);
        
                // Set up a hashFilter array
                var hashFilter = {};
                // Populate array with matches and sorts using ternary logic
                hashFilter["content"] = content ? content[1] : "*";
                hashFilter["sorts"] = sorts ? sorts[1] : "";
        
                return hashFilter;
            }
        }
        // getHashFilter

        // When the hash changes, run onHashchange
        window.onhashchange = onHashChange;

        // When the page loads for the first time, run onHashChange
        onHashChange();

    }
});
