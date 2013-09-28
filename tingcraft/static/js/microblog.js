(function($){
    $('#load-more-btn').on('click', function(){
        var user_id = $('#header-profile').attr('data-id');
        var max_id = $('.microblog-container:last').attr('data-id');
        var url_base = window.location.href.split('?')[0];
        $.ajax({
            type: 'GET',
            url: url_base + '?max_id=' + max_id,
            success: function(data) {
                $('#microblog-list-container').append(data);
            },
            error: function(res) {
            }
        });
    });
})(jQuery);
