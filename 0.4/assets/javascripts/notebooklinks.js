
document.addEventListener("DOMContentLoaded", (event) => {
  if (window.location.href.includes("/examples/")) {
    const elements = document.getElementsByClassName("highlight-ipynb");
    const regex = /(".\/)(.*)(.csv")/g;
    for (let i = 0; i < elements.length; i++) {
      elements[i].innerHTML = elements[i].innerHTML.replace(
        regex,
        '"https://ipyvizzu-story.vizzuhq.com/0.4/examples/$2$3'
      );
    }
  }
});
            