// This is the js code required by Stripe to submit a payment

$(function() {
    $("#payment-form").submit(function() {
        var form = this;
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            
            // 'cvc' is what stripe uses (not 'cvv')
            cvc: $("#id_cvv").val()
        };
        
    Stripe.createToken(card, function(status, response){
        if (status === 200) {
            $("#credit-card-errors").hide();
            $("#id_stripe_id").val(response.id);
            
            // Prevent the credit card details from being submitted to our server
            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');
            
            form.submit();
        } else {
            
            // Error - display the error returned by stripe in our 
            // 'stripe-error-message' div
            
            // Note that stripe provides us with these ids, which we can use
            // in our code, but we cant change them or the api wont work
            // In our html, 'stripe-error-message' is a child of 'credit-card-errors'
            
            $("#stripe-error-message").text(response.error.message);
            $("#credit-card-errors").show();
            $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
    });
});