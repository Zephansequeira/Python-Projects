// const response = await fetch("weather.json");
// const weather = await response.json();

const weather = {
  location: "Mumbai,India",
  Temp: "27.7\u00b0C",
  Humidity: "78",
  Rain: "23",
};

const button = document.getElementById("checkWeatherBtn");
button.addEventListener("click", updateWeatherUI);

console.log(weather);

function updateWeatherUI() {
  document.getElementById("location").textContent = weather.location;
  document.getElementById("temperature").textContent = weather.Temp;
  document.getElementById("humidity").textContent = `${weather.Humidity}%`;
  document.getElementById("rainChance").textContent = `${weather.Rain}%`;
}
