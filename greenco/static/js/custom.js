$(document).ready(function () {

    // increment and decreament quantity

    $(".increment-btn").click(function (e) { 
        e.preventDefault();
        let qty = $(this).closest('.product_data').find('.qty_input').val()
        
        let value =parseInt(qty,10)

        value = isNaN(value) ? 0 :value;

        if (value < 10) {
            value ++ ;
            $(this).closest('.product_data').find('.qty_input').val(value);

        }
        
    });
    $(".decrement-btn").click(function (e) { 
        e.preventDefault();
        let qty = $(this).closest(".product_data").find('.qty_input').val()

        let value = parseInt(qty,10)
        value = isNaN(value) ? 0 :value;

        if (value > 1){
            value -- ;
            $(this).closest(".product_data").find(".qty_input").val(value);
        }
    });

    // Add to cart

    $(".add_to_cart").click(function (e) { 
        e.preventDefault();
        let prod_id = $(".prod_id").val()
        console.log(prod_id)
        let prod_qty = $(".qty_input").val()
        console.log(prod_qty)
        let token = $('input[name=csrfmiddlewaretoken]').val()
        let btn=$(this)
        $.ajax({
            type: "POST",
            url: "/products/add-to-cart/",
            data: {
                'id':prod_id,
                'qty':prod_qty,
                csrfmiddlewaretoken:token,
            },
            
            beforeSend:function(){
                $(btn.html('adding'))

            },
            dataType: "json",
            success: function (response) {
                $(btn.html('Cart added'))
                // alertify.success(response.status) 
                alert(response.status)               
            },
            error: function(xhr, errmsg, err) {
                // Handle errors
                console.log(xhr.status + ': ' + xhr.responseText);
            }
        });



    });

    // add to wishlist

    $(".add_to_wishlist").click(function (e) { 
        e.preventDefault();
        let prod_id = $(".prod_id").val()
        console.log(prod_id)
        let token = $('input[name=csrfmiddlewaretoken]').val()
        let btn = $(this)
        $.ajax({
            type: "POST",
            url: "/products/add_to_wishlist/",
            data: {
                'id':prod_id,
                csrfmiddlewaretoken:token
            },
            dataType: "json",
            beforeSend:function(){
                $(btn.html('adding'))
            },
            success: function (response) {
                $(btn.html('wishlist added'))
                alert(response.status)

            }
        });
    });

    // update cart qty

    $(".changeqty").click(function (e) { 
        e.preventDefault();
        let prod_id = $(".prod_id").val()
        let qty=$(".qty_input").val()
        let token = $('input[name=csrfmiddlewaretoken]').val()
        console.log(prod_id,qty,token)
        // let btn =$(this)
        $.ajax({
            type: "POST",
            url: "/products/update_cart/",
            data:{
                'id':prod_id,
                'qty':qty,
                csrfmiddlewaretoken:token
            } ,
            dataType: "json",
            success: function (response) {
                alert(response.status)   
                alertify.success('{{msg}}')            
            },
            // error: function(xhr, errmsg, err) {
            //     // Handle errors
            //     console.log(xhr.status + ': ' + xhr.responseText);
            // }
        });


    });

});


