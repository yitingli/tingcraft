(function($){
    $('#load-more-btn').on('click', function(){
        var user_id = $('#header-profile').attr('data-id');
        var max_id = $('.microblog-container:last').attr('data-id');
        var url_base = window.location.href.split('?')[0];
        var t = $(this)
        t.removeClass('btn-primary');
        t.html('Loading...');
        $.ajax({
            type: 'GET',
            url: url_base + '?max_id=' + max_id,
            success: function(data) {
                if ($(data).filter('div').length) {
                    setTimeout(function() {
                        $('#microblog-list-container').append(data);
                        t.addClass('btn-primary');
                        t.html('Load More...');
                    }, 500);
                } else {
                    setTimeout(function() {
                        $('#microblog-list-container').append(data);
                        t.html('We have reached the end...');
                    }, 500);
                }
            },
            error: function(res) {
            }
        });
    });
})(jQuery);
