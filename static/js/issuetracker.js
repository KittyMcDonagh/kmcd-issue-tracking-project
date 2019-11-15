$('#issues-filter').change(function(event) {
	let selectedOption = $(this).find(":selected").val() // or .text()
	$.post({
		url: "{% url 'your_backend_view_name' %}",
		data: {
			csrfmiddlewaretoken: "{{ csrf_token }}",
			selectedOption: selectedOption
		},
		success: function(data) {
			$('#someElement').html('These are your issues: ' + data.issues)
			// This is where you change your HTML without reloading.
			// The returned data from the success function is JSON
			// coming back from your backend
		},
		traditional: true
	}).done();
});