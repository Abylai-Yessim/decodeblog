const categoriesToggle = document.querySelector('.categories-toggle');
const categoriesDropdown = document.querySelector('.categories-dropdown');


categoriesToggle.addEventListener('click', () => {

  if (categoriesDropdown.style.display === 'none' || !categoriesDropdown.style.display) {
    categoriesDropdown.style.display = 'block';
  } else {
    categoriesDropdown.style.display = 'none';
  }
});

document.addEventListener('DOMContentLoaded', function () {
    const dropdownTrigger = document.querySelector('[data-dropdown="dropdown"]');
    const dropdownMenu = dropdownTrigger.querySelector('.dropdown');
    const editLink = dropdownMenu.querySelector('.edit-link');
    const deleteLink = dropdownMenu.querySelector('.delete-link');
  
    dropdownTrigger.addEventListener('click', function () {
      
      if (dropdownMenu.style.display === 'block') {
        dropdownMenu.style.display = 'none';
        editLink.style.display = 'none';
        deleteLink.style.display = 'none';
      } else {
        dropdownMenu.style.display = 'block';
        editLink.style.display = 'block';
        deleteLink.style.display = 'block';
      }
    });
  });
  
