const serviceWrapper = document.querySelector(".wrapper-service"),
serviceSearch = serviceWrapper.querySelector(".service-form"),
optionsSerivce = serviceWrapper.querySelector(".options");
const hideService = serviceWrapper.querySelector(".hide"),
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
    serviceSearch.firstElementChild.innerText = selectedLi.innerText;
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
    // wrapperLocation.classList.remove("active");
    salonNames.classList.remove("active");
});



const salonNames = document.querySelector(".search-keywords"),
salonSearch = salonNames.querySelector(".search-form"),
optionsSalon = salonNames.querySelector(".options");
const hide = salonNames.querySelector(".hide"),
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
    // wrapperLocation.classList.remove("active");
    serviceWrapper.classList.remove("active");
});