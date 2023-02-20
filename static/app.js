function getTransmission () {
    var transmission = document.getElementById('transmission');
    if (transmission.checked) {
        return 1;
    }
    return 0;
}

function PredictMileage() {
    console.log("Prediction started");
    var client_brand = document.getElementById('brand').value;
    var client_engine = document.getElementById('engine').value;
    var client_year = document.getElementById('prod_year').value;
    var client_cap = document.getElementById('engine_cap').value;
    var client_transmission = getTransmission();

    if (client_year > 2020 || client_year < 1990) {
        return console.log('Wrong year!')
    } else {
        // var url = "http://127.0.0.1:5000/prediction"; // local version
        var url = "/api/prediction"; //

        $.post(url, {
            brand: client_brand,
            prod_year: parseInt(client_year),
            engine: client_engine,
            transmission: client_transmission,
            engine_cap: parseFloat(client_cap)
        }, function(data, status){
            console.log(data.prediction)
            document.getElementById("Mileage").value = data.prediction
            console.log(status)
        })}

}

function onPageLoad() {
  console.log( "document loaded" );
  //  var url = "http://127.0.0.1:5000/get_brands"; // Local version
  var url = "/api/get_brands";
  $.get(url, function(data, status) {
      console.log("got response for get_brands request");
      if(data) {
          var new_brands = data.brands;
          var brand = document.getElementById('brand');
          $('#brand').empty();
          for(var i in new_brands) {
              var new_option = new Option(new_brands[i]);
              $('#brand').append(new_option);
          }
      }
  });
}

window.onload = onPageLoad;