function myFunction() {
  const topNav = document.getElementById("myTopnav")

  if (topNav.className === "topnav") {
    topNav.className += " responsive"
  } else {
    topNav.className = "topnav"
  }
}

function closeSideMenu() {
  const sideMenu = document.getElementById("sidemenu-button")

  sideMenu.checked = false
}
