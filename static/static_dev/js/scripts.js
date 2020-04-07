$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(e) {
        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('name');
        var product_price = submit_btn.data('price');
        console.log(product_id);
        console.log(product_name);

        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
            var csrf_token = $ ('#from_buying_product [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;

            var url = form.attr("action");

            $.ajax ({
                url:url,
                type:'POST',
                data:data,
                cache:true,
                success:function(data){
                    console.log("ok");
                    console.log(data.products_total__nmb)
                },
                error:function(){
                    console.log("error");
                }
            })



        $('.basket-items ul').append('<li>'+product_name+', '+ nmb + 'шт. ' + 'по ' + product_price + ' руб'+
        '<span class="delete-item"> X </span>'+
        '</li>');
    });


    function showingBasket(){
        $('.basket-items').toggleClass('d-none');
    }
    function showing(){
        $('.side-back').toggleClass('d-none');
    }

    $('.nav-link').on('click', function(){
        showingBasket();
    })

    $(document).on('click', '.delete-item', function(){
        $(this).closest('li').remove();
    })


    $('.side-back').mouseover('click', function(){
        showing();
    })


})