// The following script manages the filtering of issues by Issue Filter,
// Status Filter, and Client Filter (vendor-side users only)

// The Issues Filter has been selected by the user

$('.issue-filter').on('click', function() {

    event.preventDefault();
    let issuesFilter = $(this).data('value');

    // Change the value showing in the dropdown box to the new 
    // value selected by the user

    $('#dropdownMenuLink-1').text(issuesFilter);

    // When the user selects a value from the Issues Filter, all the
    // other filters are reset to "ALL"

    // Reset Status Filter to "ALL" and display it in the filter
    // dropdown box

    let statusFilter = "ALL"
    $('#dropdownMenuLink-2').text(statusFilter);

    // Reset Client Filter to "ALL". If this is a client-side 
    // user, the Client Code dropdown option wont be displayed on
    // screen. If its a vendor-side user, display "ALL" in the 
    // Client dropdown box

    let clientFilter = "ALL"

    if ($("#dropdownMenuLink-3").length > 0) {

        $('#dropdownMenuLink-3').text(clientFilter);
    }

    // Get the issues requested by the user, as per the filter
    // values

    getIssues(issuesFilter, statusFilter, clientFilter)

});


// Status filter has been selected by the user

$('.status-filter').on('click', function() {

    event.preventDefault();
    let statusFilter = $(this).data('value');

    // Change the value showing in the dropdown box to the new 
    // value selected by the user

    $('#dropdownMenuLink-2').text(statusFilter);

    // When the status filter is selected, it will be used in
    // conjunction with the current values of the other 2 filters

    // Get the current value of the Issues Filter

    let el = document.getElementById("dropdownMenuLink-1");
    let issuesFilter = el.innerText;


    // Get the current value of the Client Filter, if it's an
    // option on the screen, otherwise set it to "ALL"

    let clientFilter = "ALL"

    if ($("#dropdownMenuLink-3").length > 0) {

        let el2 = document.getElementById("dropdownMenuLink-3");

        clientFilter = el2.innerText;
    }

    // Get the issues requested by the user, as per the filter
    // values

    getIssues(issuesFilter, statusFilter, clientFilter)
});


// Client Filter has been selected by the user. The Client Filter
// will only be available when the user is a vendor-side user

$('.client-filter').on('click', function() {

    event.preventDefault();
    let clientFilter = $(this).data('value');

    // Change the value showing in the dropdown box to the new 
    // value selected by the user

    $('#dropdownMenuLink-3').text(clientFilter);

    // When the client filter is selected, it will be used in
    // conjunction with the current values of the other 2 filters

    // Get the current value of the Issues Filter

    let el = document.getElementById("dropdownMenuLink-1");
    let issuesFilter = el.innerText;

    // Get the current value of the Status Filter

    let el2 = document.getElementById("dropdownMenuLink-2");
    let statusFilter = el2.innerText;

    // Get the issues requested by the user, as per the filter
    // values

    getIssues(issuesFilter, statusFilter, clientFilter);
});


// Get the relevant issues, based on the value of the filters

function getIssues(issuesFilter, statusFilter, clientFilter) {

    $.post({
        url: "{% url 'get_issues'%}",
        data: {
            csrfmiddlewaretoken: "{{csrf_token}}",
            issuesFilter: issuesFilter,
            statusFilter: statusFilter,
            clientFilter: clientFilter,
        },
        success: function(data) {

            // Clear the current contents of the table

            $("tbody").empty();
            $.each(data, function(key, value) {

                var inputDate = value.date;
                var user = value.user;

                if (value.user_type == "C") {
                    var assignedUser = value.assigned_client_user;
                }
                else {
                    var assignedUser = value.assigned_vendor_user;
                }

                var softwareComponent = value.software_component;
                var priority = value.priority;
                var summary = value.summary;
                var status = value.status;

                // Output the Issue Details to the table, including the 'more' icon in the last cell

                $("tbody").append(
                    "<tr><td class='d-table-cell td-date'>" + inputDate + "</td><td class='d-md-table-cell td-username'>" + user + "</td><td class='d-md-table-cell td-username'>" + assignedUser + "</td><td class='d-md-table-cell td-sw-comp'>" + softwareComponent + "</td><td class='text-center td-priority'>" + priority + "</td><td class='td-summary'>" + summary + "</td><td class='text-center td-status'>" + status + "</td><td class='text-center more-icon-cell td-more'><a href='#' ><i class='fas fa-ellipsis-h more-icon-style'></i></a></td></tr>"
                );
            });
        },
        traditional: true
    }).done();
}
