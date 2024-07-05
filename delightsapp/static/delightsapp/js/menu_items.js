function addForm() {
  var totalForms = document.getElementById('id_recipe_requirements-TOTAL_FORMS');
  if (!totalForms) {
    console.error('Cannot find element with ID id_recipe_requirements-TOTAL_FORMS');
    return;
  }
  var formCount = parseInt(totalForms.value);
  var formsetDiv = document.getElementById('recipe-requirements-formset');
  var newFormDiv = document.createElement('div');
  newFormDiv.classList.add('form-row');
  newFormDiv.innerHTML = `
    <p>
      <label for="id_recipe_requirements-${formCount}-ingredient">Ingredient:</label>
      <input type="text" name="recipe_requirements-${formCount}-ingredient" id="id_recipe_requirements-${formCount}-ingredient">
    </p>
    <p>
      <label for="id_recipe_requirements-${formCount}-quantity">Quantity:</label>
      <input type="text" name="recipe_requirements-${formCount}-quantity" id="id_recipe_requirements-${formCount}-quantity">
    </p>
  `;
  formsetDiv.appendChild(newFormDiv);
  totalForms.value = formCount + 1;
}
