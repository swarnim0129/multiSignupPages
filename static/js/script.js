// Select all form steps and progress bar elements
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".progress-bar .step");
const progressLines = document.querySelectorAll(".progress-bar .line");

let formStepIndex = 0; // Keep track of the current step

// Handle 'Next' button click event
document.querySelectorAll(".next-btn").forEach((button) => {
  button.addEventListener("click", () => {
    if (formStepIndex < formSteps.length - 1) {  // Ensure not to go out of bounds
      formStepIndex++;
      updateFormSteps();
      updateProgressBar();
    }
  });
});

// Handle 'Previous' button click event
document.querySelectorAll(".prev-btn").forEach((button) => {
  button.addEventListener("click", () => {
    if (formStepIndex > 0) {  // Ensure not to go out of bounds
      formStepIndex--;
      updateFormSteps();
      updateProgressBar();
    }
  });
});

// Update form steps based on the current index
function updateFormSteps() {
  formSteps.forEach((formStep, index) => {
    formStep.classList.toggle("active", index === formStepIndex);
  });
}

// Update the progress bar to highlight current step and completed steps
function updateProgressBar() {
  progressSteps.forEach((progressStep, index) => {
    if (index <= formStepIndex) {
      progressStep.classList.add("active");
    } else {
      progressStep.classList.remove("active");
    }
  });

  progressLines.forEach((line, index) => {
    if (index < formStepIndex) {
      line.classList.add("active");
    } else {
      line.classList.remove("active");
    }
  });
}

// Form submission logic
document.getElementById("multiStepForm").addEventListener("submit", function(event) {
  // Uncomment the following line if you want to handle form submission with JavaScript (e.g., via AJAX)
  // event.preventDefault();

  // For actual submission, comment out the alert and allow default behavior
  // alert("Form Submitted!");

  // If using AJAX, uncomment the following code:
  /*
  event.preventDefault(); // Prevent default form submission

  // Create a FormData object
  const formData = new FormData(this);

  // Send the data using Fetch API
  fetch(this.action, {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(result => {
    console.log(result); // Handle the response
    alert("Form Submitted!");
  })
  .catch(error => console.error('Error:', error));
  */
});
