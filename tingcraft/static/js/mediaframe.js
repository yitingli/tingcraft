(function($){
    $('.media-rate').on('click', function(){
        var id = $('#mediaframe-detail-container').attr('data-id');
        var url = '/api/mediaframe/' + id + '/rate/';
        var rate_btn = $('.media-rate');
        rate_btn.addClass('hidden');
        var t = $('#media-rate-info');
        t.html('Loading...');
        var rating = $('#media-rating');
        var data = {};
        data['rating'] = $(this).attr('data-rating');

        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: url,
            data: JSON.stringify(data),
            success: function(data) {
                setTimeout(function() {
                    t.html('');
                    rate_btn.removeClass('hidden');
                    rating.html(data.rating);
                }, 500);
            },
            error: function(res) {
            }
        });
    });
})(jQuery);
