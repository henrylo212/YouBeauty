const serviceWrapper = document.querySelector(".wrapper-service"),
serviceSearch = serviceWrapper.querySelector(".service-form"),
optionsSerivce = serviceWrapper.querySelector(".options"),
services_list = serviceWrapper.querySelectorAll("li");
let temp_services = Array.from(services_list);

let services = [];
temp_services.forEach(element => {
    services.push(element.innerHTML.trim())
});

function addService() {
    optionsSerivce.innerHTML = "";
    services.forEach(service => {
        let li = `<li onclick="updateService(this)">${service}</li>`;
        optionsSerivce.insertAdjacentHTML("beforeend", li);
    });
}
addService();

function updateService(selectedLi) {
    serviceSearch.value = "";
    addService();
    serviceWrapper.classList.remove("active");
    serviceSearch.innerHTML = selectedLi;
}

serviceSearch.addEventListener("keyup", () => {
    let arr= [];
    let searchedVal = serviceSearch.value.toLowerCase();
    arr = services.filter(data => {
        return data.toLowerCase().startsWith(searchedVal);
    }).map(data => `<li onclick="updateService(this)">${data}</li>`).join("");
    optionsSerivce.innerHTML = arr;
});

serviceSearch.addEventListener("click", () => {
    serviceWrapper.classList.toggle("active");
    locationWrapper.classList.remove("active");
    salonNames.classList.remove("active");
});



const salonNames = document.querySelector(".search-keywords"),
salonSearch = salonNames.querySelector(".search-form"),
optionsSalon = salonNames.querySelector(".options"),
salon_list = salonNames.querySelectorAll("li");
let temp_salonNames = Array.from(salon_list);

let salon_names = [];
temp_salonNames.forEach(element => {
    salon_names.push(element.innerHTML.trim())
});

function addSalon() {
    optionsSalon.innerHTML = "";
    salon_names.forEach(salon => {
        let li = `<li onclick="updateSalon(this)">${salon}</li>`;
        optionsSalon.insertAdjacentHTML("beforeend", li);
    });
}
addSalon();

function updateSalon(selectedLi) {
    salonSearch.value = "";
    addSalon();
    salonNames.classList.remove("active");
    salonSearch.firstElementChild.innerText = selectedLi.innerText;
}

salonSearch.addEventListener("keyup", () => {
    let arr= [];
    let searchedVal = salonSearch.value.toLowerCase();
    arr = salon_names.filter(data => {
        return data.toLowerCase().startsWith(searchedVal);
    }).map(data => `<li onclick="updateSalon(this)">${data}</li>`).join("");
    optionsSalon.innerHTML = arr;
});

salonSearch.addEventListener("click", () => {
    salonNames.classList.toggle("active");
    serviceWrapper.classList.remove("active");
    locationWrapper.classList.remove("active");
});




const locationWrapper = document.querySelector(".wrapper-location"),
locationSearch = locationWrapper.querySelector(".location-form"),
optionsLocation = locationWrapper.querySelector(".options"),
locations_list = locationWrapper.querySelectorAll("li");
let temp_locations = Array.from(locations_list);

let locations = [];
temp_locations.forEach(element => {
    locations.push(element.innerHTML.trim())
});

function addLocation() {
    optionsLocation.innerHTML = "";
    locations.forEach(location => {
        let li = `<li onclick="updateLocation(this)">${location}</li>`;
        optionsLocation.insertAdjacentHTML("beforeend", li);
    });
}
addLocation();

function updateLocation(selectedLi) {
    locationSearch.value = "";
    addLocation();
    locationWrapper.classList.remove("active");
    locationSearch.firstElementChild.innerText = selectedLi.innerText;
}

locationSearch.addEventListener("keyup", () => {
    let arr= [];
    let searchedVal = locationSearch.value.toLowerCase();
    arr = locations.filter(data => {
        return data.toLowerCase().startsWith(searchedVal);
    }).map(data => `<li onclick="updateLocation(this)">${data}</li>`).join("");
    optionsLocation.innerHTML = arr;
});

locationSearch.addEventListener("click", () => {
    locationWrapper.classList.toggle("active");
    salonNames.classList.remove("active");
    serviceWrapper.classList.remove("active");
});