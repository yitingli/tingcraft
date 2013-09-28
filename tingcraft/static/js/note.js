(function($){
    $('#show-create-note').on('click', function(){
        console.log('OK');
        CKEDITOR.config.width = 600;
        CKEDITOR.replace('create-content', {toolbar : 'Basic'});
        $('#show-create-note').addClass('hidden');
        $('#create-note').removeClass('hidden');
        $('#create-content').removeClass('hidden');
        console.log('OK');
    });
    $('#create-note').on('click', function(){
        var data = {};
        data['board'] = $('#noteboard-title').attr('data-id');
        data['content'] = CKEDITOR.instances['create-content'].getData();
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: '/api/noteboard/note/create/',
            data: JSON.stringify(data),
            success: function(res) {
                var html = '<div class="note-container left">' +
                                '<div class="content"><p>' + data['content'] + '</p></div>' +
                                '<div class="gray right small"><p>' + res.created + '</p></div>' +
                                '<span class="clear-right"></span>' +
                            '</div>';
                $('#note-list-container').prepend(html);
            },
            error: function(res) {
            }
        });
    });
})(jQuery);
