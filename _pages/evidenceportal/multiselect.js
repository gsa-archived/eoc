class CustomSelect {
  constructor(containerId, options) {
    this.container = document.getElementById(containerId);
    this.allOptions = options;
    this.availableOptions = [...options]; // Track available options
    this.selectedOptions = [];
    this.isOpen = false;
    this.init();
  }

  init() {
    this.container.innerHTML = `
            <div class="select-box">
                <div class="selected-options">Select...</div>
               <div class="icon-container">
                    <span class="clear-selection" style="display:none">×</span>
                    <span class="divider"></span>
                    <span class="dropdown-icon">
                    <svg height="20" width="20" viewBox="0 0 20 20" aria-hidden="true" focusable="false" class="css-8mmkcg"><path d="M4.516 7.548c0.436-0.446 1.043-0.481 1.576 0l3.908 3.747 3.908-3.747c0.533-0.481 1.141-0.446 1.574 0 0.436 0.445 0.408 1.197 0 1.615-0.406 0.418-4.695 4.502-4.695 4.502-0.217 0.223-0.502 0.335-0.787 0.335s-0.57-0.112-0.789-0.335c0 0-4.287-4.084-4.695-4.502s-0.436-1.17 0-1.615z"></path></svg>
                    </span>
                </div>
            </div>
            <div class="options-container">
                <input type="text" class="search-box" placeholder="Search..." autofocus="true">
                <div class="options-list"></div>
            </div>
        `;

    this.selectBox = this.container.querySelector(".select-box");
    this.optionsContainer = this.container.querySelector(".options-container");
    this.optionsList = this.container.querySelector(".options-list");
    this.searchBox = this.container.querySelector(".search-box");
    this.clearSelection = this.container.querySelector(".clear-selection");
    this.selectedOptionsContainer =
      this.container.querySelector(".selected-options");

    this.renderOptions();

    this.selectBox.addEventListener("click", () => this.toggleDropdown());
    this.searchBox.addEventListener("input", (e) =>
      this.filterOptions(e.target.value)
    );
    document.addEventListener("click", (e) => this.closeDropdownOutside(e));
    this.clearSelection.addEventListener("click", (e) =>
      this.clearAllSelections(e)
    );
  }

  renderOptions() {
    this.optionsList.innerHTML = "";

    if (this.availableOptions.length === 0) {
      const noOptionsDiv = document.createElement("div");
      noOptionsDiv.classList.add("no-options");
      noOptionsDiv.textContent = "No options remaining";
      this.optionsList.appendChild(noOptionsDiv);
    } else {
      this.availableOptions.forEach((option) => {
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
    if (this.isOpen) {
      this.optionsContainer.classList.add("show");
      this.searchBox.focus();
    } else {
      this.optionsContainer.classList.remove("show");
    }
  }

  filterOptions(query) {
    const options = this.optionsList.querySelectorAll(".option");
    options.forEach((option) => {
      if (option.textContent.toLowerCase().includes(query.toLowerCase())) {
        option.style.display = "block";
      } else {
        option.style.display = "none";
      }
    });
  }

  selectOption(value) {
    if (!this.selectedOptions.includes(value)) {
      this.selectedOptions.push(value);
      this.availableOptions = this.availableOptions.filter(
        (opt) => opt !== value
      ); // Remove from available options
      this.updateSelectedOptions();
      this.renderOptions();
      this.clearSelection.style.display = "inline";
    }
  }

  updateSelectedOptions() {
    this.selectedOptionsContainer.innerHTML = "";
    this.selectedOptions.forEach((option) => {
      const div = document.createElement("div");
      div.classList.add("selected-option");
      div.innerHTML = `${option} <span class="remove-option">×</span>`;
      div
        .querySelector(".remove-option")
        .addEventListener("click", () => this.removeOption(option));
      this.selectedOptionsContainer.appendChild(div);
    });
  }

  removeOption(value) {
    this.selectedOptions = this.selectedOptions.filter((opt) => opt !== value);
    this.availableOptions.push(value); // Add back to available options
    this.updateSelectedOptions();
    this.renderOptions();
  }

  closeDropdownOutside(event) {
    if (!this.container.contains(event.target)) {
      this.optionsContainer.classList.remove("show");
      this.isOpen = false;
    }
  }
}

// Example usage with multiple select instances:
new CustomSelect("select1", [
  "Housing",
  "Workforce Development",
  "State and Local Governments",
]);

new CustomSelect("select2", [
  "National Institution of Health",
  "Department of the Treasury",
]);

function getSelectedValue(containerId) {
  var selectBox = document.querySelector(`#${containerId} .select-box`);
  return selectBox.textContent.trim();
}
