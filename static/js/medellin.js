/**
*Some variables are in spanglish, I'm sorry 
*Eventually I will include a data base to make the process dynamic for each city and avoid to set final value to variables . 
**/

var calcBestCompra = 10;
var calcBestVenta = 0;
var local1 = "interdolar.png";
var local2 = "surcambios.png";
var local3 = "valoresyservicios.png";
var local4 = "divismarket.png";
var local5 = "nutifinanzas.png";
var local6 = "cambiosenvigado.png";
var local7 = "cashCambios.png"
var local8 = "divisasriosur.png"
var local9 = "tropicaldecambios.png"
var jsonLogos = '{"local1":"'+local1+'","local2":"'+local2+'","local3":"'+local3+'","local4":"'+local4+'","local5":"'+local5+'","local6":"'
				+local6+'","local7":"'+local7+'","local8":"'+local8+'","local9":"'+local9+'"}';

$(document).ready(function(){


	$(".exchangeFormat").blur(function(){
		$(".exchangeFormat").formatCurrency({region:'es-CO'});
	});

	showSpiner();
	getTrm();
	getLocals();
	calculateExchange();

});


function getTrm(){
	$.ajax({
        url: '/medellinTrm',
        type: 'POST',
        success: function(response) {
            data = JSON.parse(response);
            best = data.best;
            $("#trm").html("TRM: "+data.trm);
		    	
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function getLocals(){
	$.ajax({
        url: '/medellinLocs',
        type: 'POST',
        success: function(response) {
            data = JSON.parse(response);
            best = data.best;
            calcBestCompra = best.bestCompra;
			calcBestVenta = best.bestVenta;

            $("#bestCompra").html(best.bestCompra+" - <a href='"+best.bestCompraUrl+"' target='_blank'>"+best.bestCompraUrl.replace('http://','')+"</a>");
            $("#bestVenta").html(best.bestVenta+" - <a href='"+best.bestVentaUrl+"' target='_blank'>"+best.bestVentaUrl.replace('http://','')+"</a>");
            var agrego = "";
            var i = 0;
            var logos = JSON.parse(jsonLogos);
            $.each(data.locals, function (index, value) {
            	if(value.error==''){
            		var localNumber = index;
					agrego ="<section class='col-md-6'><article class='box'>"
							+"<header>"
							+"<h4><a target='_blank' href='"+value.url+"' id='a"+localNumber+"'>"+value.url.replace('http://', '')+"</a></h4>"
							+"<table class='locPrices'>"
							+"<thead><tr><th>COMPRA</th><th>VENTA</th></tr></thead>"
							+"<tbody><tr><td id='c"+localNumber+"'>"+value.compra+"</td><td id='v"+localNumber+"'>"+value.venta+"</td></tr>"
							+"</tbody></table></header>"
							+"<a href='#' class='image'><img src='/static/images/dolar/medellin/"+logos[localNumber]+"' alt=''></a>"
							+"</article></section>";	
					i = i+1;
					$(agrego).appendTo("#bodycore");	
            	}
				
		    });
       		hideSpiner();
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function calculateExchange(){
	$("#txtCalcCompra").numeric()
	$("#txtCalcVenta").numeric()

	$( "#txtCalcCompra" ).keyup(function() {

		if (this.value != this.value.replace(/[^0-9\.]/g, '')) {
	       this.value = this.value.replace(/[^0-9\.]/g, '');
	    }else{
	    	if($.trim($("#txtCalcCompra").val())==""){
				$("#calcCompra").html("COP $0");
			}else{
				var userVal = parseInt($("#txtCalcCompra").val());
				toShow = calcBestCompra * userVal; 
				$("#calcCompra").html("COP $"+toShow);
			}	
	    }
		
		
	});
	$( "#txtCalcVenta" ).keyup(function() {
		if($("#txtCalcVenta").val().length>4){
			return false;
		}

		if (this.value != this.value.replace(/[^0-9\.]/g, '')) {
	       this.value = this.value.replace(/[^0-9\.]/g, '');
	    }else{   
			if($.trim($("#txtCalcVenta").val())==""){
				$("#calcVenta").html("COP $0");
			}else{
				var userVal = parseInt($("#txtCalcVenta").val());
				toShow = calcBestVenta * userVal; 
				$("#calcVenta").html("COP $"+toShow);
			}
		}
	});
}