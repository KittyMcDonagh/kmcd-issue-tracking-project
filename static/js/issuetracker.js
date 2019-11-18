$(document).ready(function() {
    $('.dropdown-item').on('click', function() {

        event.preventDefault();
        let issueType = $(this).data('value');

        $.post({
            url: "{% url 'jq_get_issues' %}",
            data: {
                csrfmiddlewaretoken: "{{csrf_token}}",
                issueType: issueType
            },
            success: function(data) {
                console.log(data);
            },
            traditional: true
        }).done();
    })
});
