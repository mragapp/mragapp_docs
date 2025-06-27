// docs/_static/custom.js

function removeFlyout() {
  const flyout = document.querySelector("readthedocs-flyout");
  if (flyout) {
    flyout.remove();
  }
}

document.addEventListener("DOMContentLoaded", function () {
  removeFlyout();

  // Observe DOM changes and remove the flyout when it appears again
  const observer = new MutationObserver(() => {
    removeFlyout();
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true
  });
});
