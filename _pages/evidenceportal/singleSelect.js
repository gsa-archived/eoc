/* class SimpleSelect {
  constructor(containerId, options, placeholder = "Select an option") {
    this.container = document.getElementById(containerId);
    this.options = options;
    this.filteredOptions = [...options];
    this.selectedOption = null;
    this.isOpen = false;
    this.placeholder = placeholder;
    this.init();
  }

  init() {
    this.container.innerHTML = `
            <div class="custom-select">
                <div class="select-box">
                    <span class="selected-text" tabindex="0">${this.placeholder}</span>
                    <span class="arrow">
                    <svg height="20" width="20" viewBox="0 0 20 20" aria-hidden="true" focusable="false" class="css-8mmkcg"><path d="M4.516 7.548c0.436-0.446 1.043-0.481 1.576 0l3.908 3.747 3.908-3.747c0.533-0.481 1.141-0.446 1.574 0 0.436 0.445 0.408 1.197 0 1.615-0.406 0.418-4.695 4.502-4.695 4.502-0.217 0.223-0.502 0.335-0.787 0.335s-0.57-0.112-0.789-0.335c0 0-4.287-4.084-4.695-4.502s-0.436-1.17 0-1.615z"></path></svg>
                    </span>
                </div>
                <div class="options-container">
                    <input type="text" class="search-box" placeholder="Search...">
                    <div class="options-list"></div>
                </div>
            </div>
        `;

    this.selectBox = this.container.querySelector(".select-box");
    this.optionsContainer = this.container.querySelector(".options-container");
    this.optionsList = this.container.querySelector(".options-list");
    this.searchBox = this.container.querySelector(".search-box");
    this.selectedText = this.container.querySelector(".selected-text");

    this.selectBox.addEventListener("click", () => this.toggleDropdown());
    this.searchBox.addEventListener("input", () => this.filterOptions());
    document.addEventListener("click", (e) => this.handleOutsideClick(e));

    this.renderOptions();
  }

  renderOptions() {
    this.optionsList.innerHTML = "";
    if (this.filteredOptions.length === 0) {
      this.optionsList.innerHTML = `<div class="no-options">No options available</div>`;
    } else {
      this.filteredOptions.forEach((option) => {
        const div = document.createElement("div");
        div.classList.add("option");
        div.textContent = option;
        div.setAttribute("data-value", option);
        div.addEventListener("click", () => this.selectOption(option));
        this.optionsList.appendChild(div);
      });
    }
  }

  toggleDropdown() {
    this.isOpen = !this.isOpen;
    this.optionsContainer.classList.toggle("show", this.isOpen);
    this.searchBox.focus();
  }

  filterOptions() {
    const searchValue = this.searchBox.value.toLowerCase();
    this.filteredOptions = this.options.filter((option) =>
      option.toLowerCase().includes(searchValue)
    );
    this.renderOptions();
  }

  selectOption(value) {
    this.selectedOption = value;
    this.selectedText.textContent = value;
    this.toggleDropdown(); // Close dropdown
  }

  handleOutsideClick(event) {
    if (!this.container.contains(event.target)) {
      this.optionsContainer.classList.remove("show");
      this.isOpen = false;
    }
  }
}

// Initialize multiple dropdowns
new SimpleSelect(
  "dropdown1",
  [
    "Date Posted: Oldest to Newest",
    "Date Posted: Newest to Oldest",
    "Opportunity Closes: Oldest to Newest",
    "Opportunity Closes: Newest to Oldest",
  ],
  "Select..."
);
 */

class SimpleSelect {
  constructor(containerId, options, placeholder = "Select an option") {
    this.container = document.getElementById(containerId);
    this.options = options;
    this.filteredOptions = [...options];
    this.selectedOption = null;
    this.isOpen = false;
    this.placeholder = placeholder;
    this.highlightedIndex = -1; // Tracks the highlighted option
    this.init();
  }

  init() {
    this.container.innerHTML = `
      <div class="custom-select">
        <div class="select-box">
          <span class="selected-text" tabindex="0">${this.placeholder}</span>
          <span class="arrow">
            <svg height="20" width="20" viewBox="0 0 20 20" aria-hidden="true" focusable="false" class="css-8mmkcg">
              <path d="M4.516 7.548c0.436-0.446 1.043-0.481 1.576 0l3.908 3.747 3.908-3.747c0.533-0.481 1.141-0.446 1.574 0 0.436 0.445 0.408 1.197 0 1.615-0.406 0.418-4.695 4.502-4.695 4.502-0.217 0.223-0.502 0.335-0.787 0.335s-0.57-0.112-0.789-0.335c0 0-4.287-4.084-4.695-4.502s-0.436-1.17 0-1.615z"></path>
            </svg>
          </span>
        </div>
        <div class="options-container">
          <input type="text" class="search-box" placeholder="Search...">
          <div class="options-list"></div>
        </div>
      </div>
    `;

    this.selectBox = this.container.querySelector(".select-box");
    this.optionsContainer = this.container.querySelector(".options-container");
    this.optionsList = this.container.querySelector(".options-list");
    this.searchBox = this.container.querySelector(".search-box");
    this.selectedText = this.container.querySelector(".selected-text");

    this.selectBox.addEventListener("click", () => this.toggleDropdown());
    this.searchBox.addEventListener("input", () => this.filterOptions());
    document.addEventListener("click", (e) => this.handleOutsideClick(e));

    // Keyboard Events
    this.selectedText.addEventListener("keydown", (e) =>
      this.handleKeyboardEvents(e)
    );
    this.searchBox.addEventListener("keydown", (e) =>
      this.handleKeyboardEvents(e)
    );

    this.renderOptions();
  }

  renderOptions() {
    this.optionsList.innerHTML = "";
    if (this.filteredOptions.length === 0) {
      this.optionsList.innerHTML = `<div class="no-options">No options available</div>`;
    } else {
      this.filteredOptions.forEach((option, index) => {
        const div = document.createElement("div");
        div.classList.add("option");
        div.textContent = option;
        div.setAttribute("data-value", option);
        div.addEventListener("click", () => this.selectOption(option));

        // Highlight the option if it's the currently highlighted one
        if (this.highlightedIndex === index) {
          div.classList.add("highlighted");
        }

        this.optionsList.appendChild(div);
      });
    }
  }

  toggleDropdown() {
    this.isOpen = !this.isOpen;
    this.optionsContainer.classList.toggle("show", this.isOpen);
    if (this.isOpen) {
      this.searchBox.focus(); // Focus on search box when dropdown opens
    } else {
      this.highlightedIndex = -1; // Reset highlighted option when dropdown closes
      this.renderOptions();
    }
  }

  filterOptions() {
    const searchValue = this.searchBox.value.toLowerCase();
    this.filteredOptions = this.options.filter((option) =>
      option.toLowerCase().includes(searchValue)
    );
    this.renderOptions();
  }

  selectOption(value) {
    this.selectedOption = value;
    this.selectedText.textContent = value;
    this.toggleDropdown(); // Close dropdown after selection
    this.highlightedIndex = -1; // Reset highlight after selection
    //console.log(this.selectedOption);
    this.container.dispatchEvent(new CustomEvent("change", { detail: value }));
  }

  handleOutsideClick(event) {
    if (!this.container.contains(event.target)) {
      this.optionsContainer.classList.remove("show");
      this.isOpen = false;
      this.highlightedIndex = -1;
      this.renderOptions();
    }
  }

  // Handles keyboard events like Enter, Arrow Up, and Arrow Down
  handleKeyboardEvents(event) {
    if (!this.isOpen) {
      if (event.key === "Enter") {
        this.toggleDropdown(); // Open dropdown on Enter if it's closed
      }
      return;
    }

    switch (event.key) {
      case "Enter":
        if (this.highlightedIndex !== -1) {
          this.selectOption(this.filteredOptions[this.highlightedIndex]);
        }
        break;

      case "ArrowDown":
        // Move the highlight down
        if (this.highlightedIndex === this.filteredOptions.length - 1) {
          this.highlightedIndex = 0; // Loop back to the first option
        } else {
          this.highlightedIndex++;
        }
        this.renderOptions();
        break;

      case "ArrowUp":
        // Move the highlight up
        if (this.highlightedIndex === 0) {
          this.highlightedIndex = this.filteredOptions.length - 1; // Loop to the last option
        } else {
          this.highlightedIndex--;
        }
        this.renderOptions();
        break;

      case "Escape":
        this.toggleDropdown(); // Close dropdown on Escape
        break;

      default:
        break;
    }
  }
}

// Initialize dropdown
new SimpleSelect(
  "dropdown1",
  [
    "Date Posted: Oldest to Newest",
    "Date Posted: Newest to Oldest",
    "Opportunity Closes: Oldest to Newest",
    "Opportunity Closes: Newest to Oldest",
  ],
  "Select..."
);

/* function getSelectedText(dropdownId) {
  const selectedTextElement = document.querySelector(
    `#${dropdownId} .selected-text`
  );
  if (selectedTextElement) {
    return selectedTextElement.textContent; // Returns the selected text
  } else {
    console.log("Selected text element not found");
    return null;
  }
} */
