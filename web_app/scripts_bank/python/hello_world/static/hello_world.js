// filling data to the input elements based on selection of predefined hosts
$(function() {
    $('#submit_form').click(function() {
        // start showing loading animation
        $.LoadingOverlay("show", {
                        image       : "",
                        fontawesome : "fa fa-cog fa-spin"
                        })
        $.ajax({
            url: window.location.pathname, // url: /vmware/get_vmrc_links
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                $.LoadingOverlay("hide");
//                alert(response.result);
                if (response.error != "") {
                    $('#output_div').html(response.error)
                } else {
                    $('#output_div').html(response.return_message)
                }
            }
        });
    });
});
