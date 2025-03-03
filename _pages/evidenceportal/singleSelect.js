class SimpleSelect {
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
                    <span class="selected-text">${this.placeholder}</span>
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
