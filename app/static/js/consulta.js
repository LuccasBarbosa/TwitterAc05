$(document).ready(function() {

    function limpa_formulário_cep() {
        $("#logradouro").val("");
    }
    
    $("#cep").blur(function() {

        var cep = $(this).val().replace(/\D/g, '');

        if (cep != "") {

            var validacep = /^[0-9]{8}$/;

            if(validacep.test(cep)) {

                $("#logradouro").val("...");

                $.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {

                    if (!("erro" in dados)) {
                        $("#logradouro").val(dados.logradouro);
                    }
                    else {
                        limpa_formulário_cep();
                        alert("CEP não encontrado.");
                    }
                });
            }
            else {
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        }
        else {
            limpa_formulário_cep();
        }
    });
});