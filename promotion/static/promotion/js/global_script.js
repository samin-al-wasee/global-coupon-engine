window.onload = change_class;
window.onresize = change_class;

function change_class(){
    const brand_section = document.getElementById("brands_section");
    const offer_image_column = document.getElementsByClassName("offer_image_column")
    const offer_details_column = document.getElementsByClassName("offer_details_column")
    const fix_image = "col-md-4 align-self-center offer_image_column";
    const unfix_image = "col-md-2 align-self-center offer_image_column";
    const fix_details = "col-md-8 align-self-center offer_details_column";
    const unfix_details = "col-md-6 align-self-center offer_details_column";
    if(document.title.includes("Funscrimp:")){
        if (window.screen.width < 576){
            brand_section.className = "d-flex flex-row p-2";
        }else{
            brand_section.className = "row p-2"
        }
    }
    if(document.title.includes("Offers:")){
        for(let i = 0; i < offer_image_column.length; i++){
            if(window.screen.width < 1200 && window.screen.width > 767){
                offer_image_column[i].className = fix_image;
                offer_details_column[i].className = fix_details;
            }else{
                offer_image_column[i].className = unfix_image;
                offer_details_column[i].className = unfix_details;
            }
        }
    }
}

function live_search_country(){
    const current_search_string = document.getElementById("country_search").value.toLowerCase();
    const countries = document.getElementsByClassName("country_as_search_result");
    const hidden = "row m-2 country_as_search_result d-none"
    const visible = "row m-2 country_as_search_result"
    for(let i = 0; i < countries.length; i++){
        const country_name = countries[i].getAttribute("country_name").toLowerCase();
        if(current_search_string === "" || !(country_name.includes(current_search_string))){
            countries[i].className = hidden;
        }else{
            countries[i].className = visible;
        }
    }
}

function live_search_brands(){
    const current_search_string = document.getElementById("brand_search").value.toLowerCase();
    const brands = document.getElementsByClassName("brand_as_search_result");
    const hidden = "row m-2 brand_as_search_result d-none"
    const visible = "row m-2 brand_as_search_result"
    for(let i = 0; i < brands.length; i++){
        const brand_name = brands[i].getAttribute("brand_name").toLowerCase();
        if(current_search_string === "" || !(brand_name.includes(current_search_string))){
            brands[i].className = hidden;
        }else{
            brands[i].className = visible;
        }
    }
}

function set_value(pressed_button, percentage_back_class, percentage_target_class, type_back_class){
    const percentage_target = document.getElementById("popup_percentage_target");
    percentage_target.innerHTML = pressed_button.getAttribute("c_percentage") + "%";
    const type_target = document.getElementById("popup_type_target");
    type_target.innerHTML = pressed_button.getAttribute("c_type");
    const title_target = document.getElementById("popup_title_target");
    title_target.innerHTML = pressed_button.getAttribute("c_title");
    const details_target = document.getElementById("popup_details_target");
    details_target.innerHTML = pressed_button.getAttribute("c_details");
    const code_target = document.getElementById("popup_code_target");
    code_target.innerHTML = pressed_button.getAttribute("c_code");
    document.getElementById("popup_percentage_back").className = percentage_back_class;
    document.getElementById("popup_percentage_target").parentElement.className = percentage_target_class;
    document.getElementById("popup_type_back").className = type_back_class;
    const link_target = pressed_button.getAttribute("c_link");
    return window.open(link_target);
}

function redirect(id){
    const pressed_button = document.querySelector(`a[coupon_no="${id}"]`);
    set_value(pressed_button, "col-md py-md-5 border border-warning rounded-top align-self-center", "text-center text-warning", "col-md border border-warning bg-warning rounded-bottom align-self-center");
}


function redirect_hidden(id){
    const pressed_button = document.querySelector(`a[coupon_no="${id}"]`);
    const redirect = set_value(pressed_button, "col-md py-md-5 border border-danger rounded-top align-self-center", "text-center text-danger", "col-md border border-danger bg-danger rounded-bottom align-self-center");
    redirect.onload = redirect.close();
}

function set_href_brand_name(target_brand_name, target_brand_url){
    const target_button = document.getElementById("popup_button");
    target_button.setAttribute("href", target_brand_url);
    target_button.innerHTML = "Take me to ";
    target_button.innerHTML += target_brand_name;
}