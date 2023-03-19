class Parametr_Element {
    constructor(name, value=0) {
        this.element = document.getElementById(name);
        this.text = this.element.innerHTML;
        this.value = value;
    }
    set_value(value) {
        this.value = value;
        if (this.value != null){
            this.element.innerHTML = this.text + ": " + this.value;
        }else{
            this.element.innerHTML = this.text + ": " + '-';
        }
    }

}
const url = ``; 
const url_data = `${url}/api/calcs?i=`;

function initiate_start_params_element(){
    start_params_element["start-fuel"] = new Parametr_Element('start-fuel');
    start_params_element["start-oxy"] = new Parametr_Element('start-oxy');
    start_params_element["start-SH"] = new Parametr_Element('start-SH');
    start_params_element["start-days"] = new Parametr_Element('start-days');
}
function update_start_params_element(){
    start_params_element["start-fuel"].set_value(data.start.fuel);
    start_params_element["start-oxy"].set_value(data.start.oxy);
    start_params_element["start-SH"].set_value(data.start.SH);
    start_params_element["start-days"].set_value(data.start.days);
}


async function get_data_from_api(test){
    let response = await fetch(url_data+String(test));
    if (response.ok){
        let json = await response.json();
        console.log(json);
        data = json.result;
        /*
        data = {
            "start":{
                fuel: 1, oxy: 2, SH: 3, days: 4
            },
            "days_amount": 3,
            "days":[
                {
                    exp: {
                        fuel: -1,
                        oxy: 2, 
                        SH: 3
                    },
                    now: {
                        fuel: 20,
                        oxy: 20, 
                        SH: 30
                    },
                    fire_electro: {
                        fire: 50,
                        electro: 50
                    }
                },
                {
                    exp: {
                        fuel: -2,
                        oxy: 20, 
                        SH: -13
                    },
                    now: {
                        fuel: 18,
                        oxy: 40, 
                        SH: 17
                    },
                    fire_electro: {
                        fire: 70,
                        electro: 30
                    }
                },
                {
                    exp: {
                        fuel: -4352,
                        oxy: 23450, 
                        SH: -13453
                    },
                    now: {
                        fuel: 13458,
                        oxy: 43450, 
                        SH: 13457
                    },
                    fire_electro: {
                        fire: 30,
                        electro: 70
                    }
                },

            ]
        
        }*/
        update_start_params_element();
        
    }
}
var data = {};
var start_params_element = {};
var start_params = {};
var navigation = document.getElementById("nav");

reload();
function draw_nav(){
navigation.innerHTML = '';
for(let i = 0; i < data.days_amount; i++){
    navigation.innerHTML += 
    `
    <button onclick="draw_cards(${i});">${i+1}</button>
    `
    ;
}
}

function draw_cards(i){
    let cur_data = data.days[i];
    let exp_card = document.getElementById('EXP'); 
    let now_card = document.getElementById('NOW'); 
    let fire_electro_card = document.getElementById('FIREELECTRO'); 
    document.getElementById('exp_fuel').innerHTML = `Ядерное топливо: ${cur_data.exp.fuel}`;
    document.getElementById('exp_oxy').innerHTML = `Кислород: ${cur_data.exp.oxy}`;
    //document.getElementById('exp_SH').innerHTML = `SH: ${cur_data.exp.SH}`;
    
    document.getElementById('now_fuel').innerHTML = `Ядерное топливо: ${cur_data.now.fuel}`;
    document.getElementById('now_oxy').innerHTML = `Кислород: ${cur_data.now.oxy}`;
    document.getElementById('now_SH').innerHTML = `SH: ${cur_data.now.SH}`;
    
    document.getElementById('fire').innerHTML = `${cur_data.fire_electro.fire}%`;
    document.getElementById('electro').innerHTML = `${cur_data.fire_electro.electro}%`;
    
    document.getElementById('fire').style.width = `${cur_data.fire_electro.fire}%`;
    document.getElementById('electro').style.width = `${cur_data.fire_electro.electro}%`;
    
    }


function reload(test=NaN){
    
data = {};
start_params_element = {};
start_params = {};
initiate_start_params_element();
get_data_from_api(test); 
draw_nav();
draw_cards(0);


}
