const wrapperLocation = document.querySelector(".wrapper-location"),
selectBtn = wrapperLocation.querySelector(".select-btn"),
searchInp = wrapperLocation.querySelector("input"),
options = wrapperLocation.querySelector(".options");

let countries = ["Camperdown", "Darlington", "Chippendale", "Hornsby", "Epping", "Strathfield", "Burwood", "Chatswood"]

function addCountry() {
    options.innerHTML = "";
    countries.forEach(country => {
        let li = `<li onclick="updateName(this)">${country}</li>`;
        options.insertAdjacentHTML("beforeend", li);
    });
}
addCountry();

function updateName(selectedLi) {
    searchInp.value = "";
    addCountry();
    wrapperLocation.classList.remove("active");
    selectBtn.firstElementChild.innerText = selectedLi.innerText;
}

searchInp.addEventListener("keyup", () => {
    let arr= [];
    let searchedVal = searchInp.value.toLowerCase();
    arr = countries.filter(data => {
        return data.toLowerCase().startsWith(searchedVal);
    }).map(data => `<li onclick="updateName(this)">${data}</li>`).join("");
    options.innerHTML = arr;
});

selectBtn.addEventListener("click", () => {
    wrapperLocation.classList.toggle("active");
});


const wrapperService = document.querySelector(".wrapper-service"),
serviceBtn = wrapperService.querySelector(".service-btn"),
searchInpService = wrapperService.querySelector("input"),
optionsService = wrapperService.querySelector(".options");

let services = ["Basic Cut", "Blowdry", "Wash and Cut", "Perm", "Bleach", "Dye", "Straighten", "Curl"]

function addService() {
    optionsService.innerHTML = "";
    services.forEach(service => {
        let li = `<li onclick="updateServiceName(this)">${service}</li>`;
        optionsService.insertAdjacentHTML("beforeend", li);
    });
}
addService();

function updateServiceName(selectedLi) {
    searchInpService.value = "";
    addService();
    wrapperService.classList.remove("active");
    serviceBtn.firstElementChild.innerText = selectedLi.innerText;
}

searchInpService.addEventListener("keyup", () => {
    let arr= [];
    let searchedVal = searchInpService.value.toLowerCase();
    arr = services.filter(data => {
        return data.toLowerCase().startsWith(searchedVal);
    }).map(S_data => `<li onclick="updateServiceName(this)">${S_data}</li>`).join("");
    optionsService.innerHTML = arr;
});

serviceBtn.addEventListener("click", () => {
    wrapperService.classList.toggle("active");
});