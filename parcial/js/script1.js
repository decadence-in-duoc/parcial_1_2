//carrito
let num = 0
let nombres = ['DIEZ','VEINTE','TREINTA','CUARENTA','CINCUENTA','SESENTA','SETENTA','OCHENTA','NOVENTA','CIEN']
let precios = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
$(document).ready(function(){
    // añadir la funcionalidad de click al boton enviar
    $("#enviar").click(function(){
        var url="catalogo.html"
        $.get(url, function(data){
                var msg = '<tr>'
                msg += '<td>' + num + '</td>'
                msg += '<td>' + nombres[num] + '</td>'
                msg += '<td>' + precios[num] + '</td>'
                msg += '<td><input type="button" class="borrar btn btn-danger" value="Eliminar" /></td>'
                msg += '</tr>'
                $("#categorias").append(msg)
                num++
                if(num % 10 == 0) num = 0            
        })

    });

    // añado un nuevo click por cada boton borrar
    $(document).on('click', '.borrar', function() {
        $(this).closest('tr').remove();
    });
    
});
