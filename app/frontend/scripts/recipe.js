const apiURL = "http://127.0.0.1:8000";

const getRecipes = async () => {
  const res = await fetch(apiURL + "/recipe");
  return await res.json();
};

const createRecipe = async (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const prepTime = document.getElementById("prep-time").value;
  const cookingTime = document.getElementById("cooking-time").value;
  const ingredientsList = document.getElementById("ingredients-list").value;
  const cookingInstructions = document.getElementById(
    "cooking-instructions"
  ).value;
  const difficulty = document.querySelector(
    'input[name="difficulty"]:checked'
  ).value;

  const recipe = {
    name: name,
    prep_time_mins: Number(prepTime),
    cook_time_mins: Number(cookingTime),
    difficulty: difficulty,
    ingredients: ingredientsList,
    instructions: cookingInstructions,
  };

  const res = await fetch(apiURL + "/recipe", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(recipe),
  });

  return await res.json();
};

console.log(getRecipes());
