// script.js

document.addEventListener("DOMContentLoaded", function () {
    const multiSelectInput = document.getElementById("multiSelectInput");
    const selectedItemsContainer = document.querySelector(".selected-items");
    const optionsContainer = document.querySelector(".options-container");

    const options = ["India", "Australia", "United States", "Canada", "UK"];

    options.forEach(option => {
        const optionDiv = document.createElement("div");
        optionDiv.classList.add("option");
        optionDiv.textContent = option;
        optionDiv.addEventListener("click", function () {
            addSelectedItem(option);
        });
        optionsContainer.appendChild(optionDiv);
    });

    multiSelectInput.addEventListener("focus", function () {
        optionsContainer.style.display = "block";
    });

    document.addEventListener("click", function (event) {
        if (!multiSelectInput.contains(event.target) && !optionsContainer.contains(event.target)) {
            optionsContainer.style.display = "none";
        }
    });

    function addSelectedItem(value) {
        // Check if the item is already selected
        const alreadySelected = Array.from(selectedItemsContainer.children).some(
            item => item.textContent.replace("x", "").trim() === value
        );

        if (alreadySelected) {
            return; // Do not add the item if it is already selected
        }

        const selectedItemDiv = document.createElement("div");
        selectedItemDiv.classList.add("selected-item");
        selectedItemDiv.textContent = value;

        const removeBtn = document.createElement("span");
        removeBtn.classList.add("remove-btn");
        removeBtn.textContent = "x";
        removeBtn.addEventListener("click", function () {
            selectedItemsContainer.removeChild(selectedItemDiv);
        });

        selectedItemDiv.appendChild(removeBtn);
        selectedItemsContainer.appendChild(selectedItemDiv);
    }
});
