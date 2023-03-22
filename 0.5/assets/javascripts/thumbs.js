const currentScript = document.currentScript;
document.addEventListener("DOMContentLoaded", (event) => {
  const parentContainer = currentScript.nextElementSibling;
  parentContainer.style.display = "flex";
  parentContainer.style["flex-wrap"] = "wrap";
  parentContainer.style.justifyContent = "center";
});
