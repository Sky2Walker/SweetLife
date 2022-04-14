$(document).ready(function (){
   let form = $('#form_buying_product');

   form.on('submit', function (e){
       e.preventDefault();
       let num = $('#number').val();

       let submit_btn = $('#submit_btn');
       let product_id = submit_btn.data("product_id");
       let product_name = submit_btn.data("name");
       let product_price = submit_btn.data("price");
        console.log(product_name);
        console.log(num);
        console.log(product_price);

        $('#basket-items ul').append(
            '<li className="header-cart-item flex-w flex-t m-b-12">'+
                '<div className="header-cart-item-img"> <img src="images/item-cart-03.jpg" alt="IMG"> </div>'+

                '<div className="header-cart-item-txt p-t-8"> <a href="#" className="header-cart-item-name m-b-18 hov-cl1 trans-04">'+ product_name+

                    '</a>'+

                    '<span className="header-cart-item-info">'+
								num+ 'x' + '₴' + product_price +
							'</span>'+
                '</div>'+
            '</li>'
        );


        let  data = {};
        console.log(data);
        data.product_id = product_id;
        data.num=num;
        data.product_name=product_name;
         let csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
         data["csrfmiddlewaretoken"] = csrf_token;
        let url  = form.attr("action");
        $.ajax({
            url:url,
            type:'POST',
            data:data,
            cache:true,
            success:function (data){
                console.log('OK');
                }
                })


        })


});