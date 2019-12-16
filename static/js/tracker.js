 // The following script manages the Filtering and Pagination of Issues 
 // and Features when selections are made from the dropdown filters




 // ISSUES PROCESSING -------------------------------------------//

 // ===========================
 // Filtering by Issue Filter 
 // ===========================

 // A value has been selected by the user from the Issues Filter 
 // dropdown 

 $('.issue-filter').on('click', function() {

     event.preventDefault();
     let issuesFilter = $(this).data('value');

     console.log("issuesFilter : " + issuesFilter)

     // Clear the contents of the search box, to avoid confusing the user

     document.getElementById('iss-search-val').value = ""

     // Change the value showing in the dropdown box to the new 
     // value selected by the user

     $('#dropdownMenuLink-1').text(issuesFilter);

     // When the user selects a value from the Issues Filter, all the
     // other filters are reset to "ALL"

     // Reset Status Filter to "ALL" and display it in the filter
     // dropdown box

     let statusFilter = "ALL"
     $('#dropdownMenuLink-2').text(statusFilter);

     // Reset Priority Filter to "ALL" and display it in the filter
     // dropdown box

     let priorityFilter = "ALL"
     $('#dropdownMenuLink-3').text(priorityFilter);

     // Reset Client Filter to "ALL". If this is a client-side 
     // user, the Client Code dropdown option wont be displayed on
     // screen. If its a vendor-side user, display "ALL" in the 
     // Client dropdown box

     let clientFilter = "ALL";

     if ($("#dropdownMenuLink-4").length > 0) {

         $('#dropdownMenuLink-4').text(clientFilter);
     }

     // Get the issues requested by the user, as per the filter
     // values, starting with page 1

     // Clear searchValue - it is only set when the user inputs a 
     // value in the search box

     let searchValue = ""

     // Initialise the page number

     let page = 1;

     getIssues(issuesFilter, statusFilter, priorityFilter, clientFilter, page, searchValue);

 });


 // ===========================
 // Filtering Issues by Status Filter
 // ===========================

 // A value has been selected from the Status filter dropdown by the user

 $('.iss-status-filter').on('click', function() {

     event.preventDefault();
     let statusFilter = $(this).data('value');

     // Clear the contents of the search box, to avoid confusing the user

     document.getElementById('iss-search-val').value = ""


     // Change the value showing in the dropdown box to the new 
     // value selected by the user

     $('#dropdownMenuLink-2').text(statusFilter);

     // When the status filter is selected, it will be used in
     // conjunction with the current values of the other 2 filters

     // Get the current value of the Issues Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let issuesFilter = getIssuesFilterValue();

     if (issuesFilter == "") {
         issuesFilter = 'ALL ISSUES'
         $('#dropdownMenuLink-1').text(issuesFilter);
     }

     // Get the current value of the Priority Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let priorityFilter = getPriorityFilterValue();

     console.log("priorityFilter: " + priorityFilter)

     if (priorityFilter == "") {
         priorityFilter = 'ALL'
         console.log("setting priorityFilter to ALL")
         $('#dropdownMenuLink-3').text(priorityFilter);
     }

     // Get the current value of the Client Filter, if it's an
     // option on the screen, otherwise set it to "ALL"
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let clientFilter = getClientFilterValue();

     if (clientFilter == "") {
         clientFilter = 'ALL'
         $('#dropdownMenuLink-4').text(clientFilter);
     }

     // Clear searchValue - it is only set when the user inputs a 
     // value in the search box

     let searchValue = ""

     // Initialise the page number

     let page = 1;

     console.log("in status filter click")
     console.log("statusFilter: " + statusFilter);
     console.log("issuesFilter: " + issuesFilter);
     console.log("priorityFilter: " + priorityFilter);
     console.log("clientFilter: " + clientFilter);

     getIssues(issuesFilter, statusFilter, priorityFilter, clientFilter, page, searchValue);
 });


 // ===========================
 // Filtering Issues by Priority
 // ===========================

 $('.priority-filter').on('click', function() {

     event.preventDefault();

     let priorityFilter = $(this).data('value');
     let priorityFilterText = this.innerText;

     // Clear the contents of the search box, to avoid confusing the user

     document.getElementById('iss-search-val').value = ""


     // A value has been selected from the Priority Filter dropdown 
     // by the user

     // Change the value showing in the dropdown box to the new 
     // value selected by the user

     $('#dropdownMenuLink-3').text(priorityFilterText);

     // When the priority filter is selected, it will be used in
     // conjunction with the current values of the other 2 filters

     // Get the current value of the Issues Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let issuesFilter = getIssuesFilterValue();

     if (issuesFilter == "") {
         issuesFilter = 'ALL ISSUES'
         $('#dropdownMenuLink-1').text(issuesFilter);
     }


     // Get the current value of the Status Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let statusFilter = getStatusFilterValue();

     if (statusFilter == "") {
         statusFilter = 'ALL'
         $('#dropdownMenuLink-2').text(statusFilter);
     }


     // Get the current value of the Client Filter, if it's an
     // option on the screen, otherwise set it to "ALL"
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let clientFilter = getClientFilterValue();

     if (clientFilter == "") {
         clientFilter = "ALL"
         $('#dropdownMenuLink-4').text(clientFilter);
     }

     // Clear searchValue - it is only set when the user inputs a 
     // value in the search box

     let searchValue = ""

     // Initialise the page number

     let page = 1;

     getIssues(issuesFilter, statusFilter, priorityFilter, clientFilter, page, searchValue);
 });


 // ===========================
 // Filtering Issues by Client Filter 
 // ===========================

 // Client Filter has been selected by the user. The Client Filter
 // will only be available when the user is a vendor-side user

 $('.iss-client-filter').on('click', function() {

     event.preventDefault();
     let clientFilter = $(this).data('value');

     // Clear the contents of the search box, to avoid confusing the user

     document.getElementById('iss-search-val').value = "";

     // A value has been selected from the Client Filter dropdown by
     // the user

     // Change the value showing in the dropdown box to the new 
     // value selected by the user

     $('#dropdownMenuLink-4').text(clientFilter);

     // When the client filter is selected, it will be used in
     // conjunction with the current values of the other 2 filters

     // Get the current value of the Issues Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let issuesFilter = getIssuesFilterValue();

     if (issuesFilter == "") {
         issuesFilter = 'ALL ISSUES'
         $('#dropdownMenuLink-1').text(issuesFilter);
     }


     // Get the current value of the Status Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let statusFilter = getStatusFilterValue();

     if (statusFilter == "") {
         statusFilter = 'ALL'
         $('#dropdownMenuLink-2').text(statusFilter);
     }


     // Get the current value of the Priority Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let priorityFilter = getPriorityFilterValue();

     if (priorityFilter == "") {
         priorityFilter = 'ALL'
         $('#dropdownMenuLink-3').text(priorityFilter);
     }


     // Clear searchValue - it is only set when the user inputs a 
     // value in the search box

     let searchValue = "";

     // Initialise the page number

     let page = 1;

     getIssues(issuesFilter, statusFilter, priorityFilter, clientFilter, page, searchValue);
 });


 //==================================================================
 // SEARCH BOX - Searching for Issues where text in the Issue Summary
 // matches the text input in the input box
 //==================================================================

 $('#iss-search-btn').on('click', function() {

     // The user has input a value in the Issues search box 

     event.preventDefault();

     let searchValue = document.getElementById('iss-search-val').value

     console.log("searchValue : " + searchValue);

     // When the user enters a value in the search box, all the filters
     // will be set to spaces, as only the search value will be used
     // to select the issues

     let issuesFilter = ""
     $('#dropdownMenuLink-1').text(issuesFilter);
     let statusFilter = ""
     $('#dropdownMenuLink-2').text(statusFilter);
     let priorityFilter = ""
     $('#dropdownMenuLink-3').text(priorityFilter);
     let clientFilter = "";
     $('#dropdownMenuLink-4').text(clientFilter);

     // Get the issues requested by the user, as per the filter
     // values, starting with page 1

     let page = 1;

     getIssues(issuesFilter, statusFilter, priorityFilter, clientFilter, page, searchValue);

 });


 // ===========================
 // Issues Pagination
 // ===========================

 // The user has clicked on a page number
 // Using "$(document).on . . ." here because the 'iss-page-click' 
 // class is not part of the html when it is first loaded, they are
 // added by js when it displays the filtered data, and therefore the
 // js wont respond to "$('.iss-page-click').on('click', function()"

 $(document).on('click', ".iss-page-click", function() {

     // Get the page number the user clicked on

     var page = $(this).data('value');

     console.log("in iss-page-click");

     console.log("this page: " + page);

     // Get the current values of the filters

     let issuesFilter = getIssuesFilterValue();
     let statusFilter = getStatusFilterValue();
     let priorityFilter = getPriorityFilterValue();
     let clientFilter = getClientFilterValue();
     let searchValue = document.getElementById('iss-search-val').value

     console.log("priorityFilter: " + priorityFilter);

     // Get the issues as per the filter values and page number

     getIssues(issuesFilter, statusFilter, priorityFilter, clientFilter, page, searchValue);
 });


 // ================
 // HELPER FUNCTIONS
 // ================
 // Get the current value of the issues filter

 function getIssuesFilterValue() {

     // Get the current value of the Issues Filter

     let el = document.getElementById("dropdownMenuLink-1");
     let issuesFilter = el.innerText;

     return issuesFilter;

 }

 // Get the current value of the Status Filter

 function getStatusFilterValue() {

     let el = document.getElementById("dropdownMenuLink-2");

     let statusFilter = el.innerText;

     return statusFilter;

 }

 // Get the current value of the Priority Filter
 // The priority in the db is just a number from 1 - 5. But on the 
 // screen a descriptive text is included, e.g. 1 - URGENT. When
 // getting the value of the current priority filter, the '1' must
 // be extracted from the text.

 function getPriorityFilterValue() {

     let el = document.getElementById("dropdownMenuLink-3");
     let priorityFilter = el.innerText

     if (el.innerText != "ALL" & el.innerText != "") {

         let priorityArray = el.innerText.split("");
         console.log("in getPriorityFilterValue.  priorityArray[0,0]: " + priorityArray[0, 0])
         priorityFilter = priorityArray[0, 0];
     }

     console.log("in getPriorityFilterValue. priorityFilter: " + priorityFilter)

     return priorityFilter;

 }


 // Get the current value of the Client Filter, if it's an
 // option on the screen, otherwise set it to "ALL"

 function getClientFilterValue() {

     let clientFilter = "ALL";

     if ($("#dropdownMenuLink-4").length > 0) {

         let el = document.getElementById("dropdownMenuLink-4");

         clientFilter = el.innerText;
     }

     return clientFilter;

 }


 // =================================
 // Get the issues from the database 
 // =================================

 // Get the relevant issues, based on the value of the filters


 function getIssues(issuesFilter, statusFilter, priorityFilter, clientFilter, page, searchValue) {

     console.log("issuesFilter: "+issuesFilter)
     console.log("statusFilter: "+statusFilter)
     console.log("priorityFilter: "+priorityFilter)
     console.log("clientFilter: "+clientFilter)
     console.log("in getIssues(). page = " + page)
     console.log("searchValue: " + searchValue)

     $.post({
         url: "{% url 'get_issues' %}",
         data: {
             csrfmiddlewaretoken: "{{csrf_token}}",
             issuesFilter: issuesFilter,
             statusFilter: statusFilter,
             priorityFilter: priorityFilter,
             clientFilter: clientFilter,
             page: page,
             searchValue: searchValue,

         },

         success: function(data) {


             // Display user message if one is returned
             // If the message is blank, keep the line, but make
             // it invisible on the screen

             var userMessage = data.user_mesg.user_message;

             if (userMessage != "") {
                 console.log("userMessage: " + userMessage)
                 $('.user-message').text(userMessage)
                 $('.user-message').removeClass('blank-line')
             }
             else {
                 $('.user-message').text("blank")
                 $('.user-message').addClass('blank-line')
             }


             // Clear the current contents of the table
             // Output the details of each issue to the table 

             $("tbody").empty();
             $.each(data.issues, function(key, value) {

                 var issueId = value.id;

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
                     "<tr><td class='d-table-cell td-date'>" + inputDate + "</td><td class='d-md-table-cell td-username'>" + user + "</td><td class='d-md-table-cell td-username'>" + assignedUser + "</td><td class='d-md-table-cell td-sw-comp'>" + softwareComponent + "</td><td class='text-center td-priority'>" + priority + "</td><td class='td-summary'>" + summary + "</td><td class='text-center td-status'>" + status + "</td><td class='text-center td-more'><a class='iss-more-icon-style' href=/issue_tracker/" + issueId + "/ " + "><i class='fas fa-ellipsis-h more-icon-style'></i></a></td></tr>"
                 );

                 console.log("input date: " + inputDate + " user:  " + user + " summary: " + summary);

             });


             // Output the pagination parameters for the issues list to the html page

             let listType = "issues"
             outputPaginationValues(data, listType)

         },
         traditional: true
     }).done();
 }

 // The following code managing the issues comments fields 

 $('.iss-comments-form-hide').hide();
 $('.iss-comments-dash-hide').hide();
 console.log("hiding done.....................")


 $('#enable-comments').on('click', function() {
     $('.iss-comments-dash').toggle();
     $('#iss-comments-minus').removeClass('iss-enabled-link');
     $('#iss-comments-minus').addClass('disabled-link');
     $('#iss-comments-plus').addClass('iss-enabled-link');
     $('#iss-comments-plus').removeClass('disabled-link');

     $('#iss-comments-form').hide();

     console.log("toggling done.........................")

 });

 $('#iss-comments-plus').on('click', function() {
     $('#iss-comments-form').show();

     $('#iss-comments-plus').removeClass('iss-enabled-link');
     $('#iss-comments-plus').addClass('disabled-link');
     $('#iss-comments-minus').addClass('iss-enabled-link');
     $('#iss-comments-minus').removeClass('disabled-link');
 });

 $('#iss-comments-minus').on('click', function() {
     $('#iss-comments-form').hide();

     $('#iss-comments-minus').removeClass('iss-enabled-link');
     $('#iss-comments-minus').addClass('disabled-link');
     $('#iss-comments-plus').addClass('iss-enabled-link');
     $('#iss-comments-plus').removeClass('disabled-link');

 });







 // FEATURES PROCESSING -------------------------------------------//

 // The following scripts manage the filtering of features by Features Filter,
 // Status Filter, Paid Filter, and Client Filter (vendor-side users only)

 // ============================
 // Filtering by Features Filter
 // ============================

 // A value has been selected from the  Features Filter dropdown 
 // by the user

 $('.features-filter').on('click', function() {

     event.preventDefault();
     let featuresFilter = $(this).data('value');

     // Clear the contents of the search box, to avoid confusing the user

     document.getElementById('ftr-search-val').value = ""

     console.log("featuresFilter : " + featuresFilter)

     // The user has selected a value from the Features Filter dropdown

     // Change the value showing in the dropdown box to the new 
     // value selected by the user

     $('#dropdownMenuLink-1').text(featuresFilter);

     // When the user selects a value from the Features Filter, all the
     // other filters are reset to "ALL"

     // Reset Status Filter to "ALL" and display it in the filter
     // dropdown box

     let statusFilter = "ALL"
     $('#dropdownMenuLink-2').text(statusFilter);

     // Reset Paid Filter to "ALL" and display it in the filter
     // dropdown box

     let paidFilter = "ALL"
     $('#dropdownMenuLink-3').text(paidFilter);

     // Reset Client Filter to "ALL". If this is a client-side 
     // user, the Client Code dropdown option wont be displayed on
     // screen. If its a vendor-side user, display "ALL" in the 
     // Client dropdown box

     let clientFilter = "ALL";

     if ($("#dropdownMenuLink-4").length > 0) {

         $('#dropdownMenuLink-4').text(clientFilter);
     }

     // Clear searchValue - it is only set when the user inputs a 
     // value in the search box

     let searchValue = ""

     // Get the features requested by the user, as per the filter
     // values, starting with page 1

     let page = 1;

     console.log("about to call getFeatures")

     getFeatures(featuresFilter, statusFilter, paidFilter, clientFilter, page, searchValue);

 });


 // ===========================
 // Filtering by Status Filter
 // ===========================

 // Status filter has been selected by the user

 $('.feat-status-filter').on('click', function() {

     event.preventDefault();
     let statusFilter = $(this).data('value');

     // Clear the contents of the search box, to avoid confusing the user

     document.getElementById('ftr-search-val').value = ""

     // The user has selected a value from the Status Filter dropdown
     // Change the value showing in the dropdown box to the new 
     // value selected by the user

     $('#dropdownMenuLink-2').text(statusFilter);

     // When the status filter is selected, it will be used in
     // conjunction with the current values of the other 2 filters

     // Get the current value of the Features Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let featuresFilter = getFeaturesFilterValue();

     if (featuresFilter == "") {
         featuresFilter = 'ALL FEATURES'
         $('#dropdownMenuLink-1').text(featuresFilter);
     }

     // Get the current value of the Paid Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let paidFilter = getPaidFilterValue();

     if (paidFilter == "") {
         paidFilter = 'ALL'
         $('#dropdownMenuLink-3').text(paidFilter);
     }

     // Get the current value of the Client Filter, if it's an
     // option on the screen, otherwise set it to "ALL"
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let clientFilter = getClientFilterValue();

     if (clientFilter == "") {
         clientFilter = 'ALL'
         $('#dropdownMenuLink-4').text(clientFilter);
     }

     // Clear searchValue - it is only set when the user inputs a 
     // value in the search box

     let searchValue = ""

     // Get the features requested by the user, as per the filter
     // values, starting with page 1

     let page = 1;

     console.log("in status filter click")
     console.log("statusFilter: " + statusFilter);
     console.log("featuresFilter: " + featuresFilter);
     console.log("paidFilter: " + paidFilter);
     console.log("clientFilter: " + clientFilter);

     getFeatures(featuresFilter, statusFilter, paidFilter, clientFilter, page, searchValue);
 });



 // ==================
 // Filtering by Paid
 // ==================

 $('.paid-filter').on('click', function() {

     event.preventDefault();

     let paidFilter = $(this).data('value');
     let paidFilterText = this.innerText;

     // Clear the contents of the search box, to avoid confusing the user

     document.getElementById('ftr-search-val').value = ""

     // The user has selected a value from the Paid Filter dropdown

     // Change the value showing in the dropdown box to the new 
     // value selected by the user

     $('#dropdownMenuLink-3').text(paidFilterText);

     // When the priority filter is selected, it will be used in
     // conjunction with the current values of the other 2 filters

     // Get the current value of the Features Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let featuresFilter = getFeaturesFilterValue();

     if (featuresFilter == "") {
         featuresFilter = 'ALL FEATURES'
         $('#dropdownMenuLink-1').text(featuresFilter);
     }

     // Get the current value of the Status Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let statusFilter = getStatusFilterValue();

     if (statusFilter == "") {
         statusFilter = 'ALL'
         $('#dropdownMenuLink-2').text(statusFilter);
     }


     // Get the current value of the Client Filter, if it's an
     // option on the screen, otherwise set it to "ALL"
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let clientFilter = getClientFilterValue();

     if (clientFilter == "") {
         clientFilter = 'ALL'
         $('#dropdownMenuLink-4').text(clientFilter);
     }

     // Clear searchValue - it is only set when the user inputs a 
     // value in the search box

     let searchValue = ""

     // Get the features requested by the user, as per the filter
     // values, starting with page 1

     let page = 1;

     getFeatures(featuresFilter, statusFilter, paidFilter, clientFilter, page, searchValue);
 });


 // ==========================
 // Filtering by Client Filter 
 // ==========================

 // Client Filter has been selected by the user. The Client Filter
 // will only be available when the user is a vendor-side user

 $('.feat-client-filter').on('click', function() {

     console.log("in .feat-client-filter-------------------")

     event.preventDefault();
     let clientFilter = $(this).data('value');

     // Clear the contents of the search box, to avoid confusing the user

     document.getElementById('ftr-search-val').value = ""

     // The user has selected a value from the Client Filter dropdown

     // Change the value showing in the dropdown box to the new 
     // value selected by the user

     $('#dropdownMenuLink-4').text(clientFilter);

     // When the client filter is selected, it will be used in
     // conjunction with the current values of the other 2 filters

     // Get the current value of the Features Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let featuresFilter = getFeaturesFilterValue();

     if (featuresFilter == "") {
         featuresFilter = 'ALL FEATURES'
         $('#dropdownMenuLink-1').text(featuresFilter);
     }

     // Get the current value of the Status Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let statusFilter = getStatusFilterValue();

     console.log("current value of status filter; " + statusFilter)

     if (statusFilter == "") {
         console.log("statusfilter blank: " + statusFilter)
         statusFilter = 'ALL';
         $('#dropdownMenuLink-2').text(statusFilter);
     }

     console.log("1. statusFilter = " + statusFilter)
     // Get the current value of the Priority Filter
     // It may be blank if the user was previously using the search
     // box - if so, set it to 'ALL'

     let paidFilter = getPaidFilterValue();
     console.log("2. statusFilter = " + statusFilter)

     if (paidFilter == "") {
         paidFilter = 'ALL';
         $('#dropdownMenuLink-3').text(paidFilter);
     }
     console.log("3. statusFilter = " + statusFilter)

     // Clear searchValue - it is only set when the user inputs a 
     // value in the search box

     let searchValue = "";

     // Get the features requested by the user, as per the filter
     // values, starting with page 1

     let page = 1;

     console.log("before getFeatures, statusFilter: " + statusFilter)

     getFeatures(featuresFilter, statusFilter, paidFilter, clientFilter, page, searchValue);
 });


 //==================================================================
 // SEARCH BOX - Searching for Features where text in the Feature Summary
 // matches the text input in the input box
 //==================================================================

 $('#ftr-search-btn').on('click', function() {

     // The user has input a value in the Issues search box 

     event.preventDefault();

     let searchValue = document.getElementById('ftr-search-val').value

     console.log("features searchValue : " + searchValue);

     // When the user enters a value in the search box, all the filters
     // will be set to spaces, as only the search value will be used
     // to select the features

     let featuresFilter = ""
     $('#dropdownMenuLink-1').text(featuresFilter);
     let statusFilter = ""
     $('#dropdownMenuLink-2').text(statusFilter);
     let paidFilter = ""
     $('#dropdownMenuLink-3').text(paidFilter);
     let clientFilter = "";
     $('#dropdownMenuLink-4').text(clientFilter);

     // Get the features requested by the user, as per the filter
     // values, starting with page 1

     let page = 1;

     getFeatures(featuresFilter, statusFilter, paidFilter, clientFilter, page, searchValue);

 });


 // ===========================
 // Features Pagination
 // ===========================

 // The user has clicked on a page number
 // Using "$(document).on . . ." here because the 'feat-page-click' 
 // class is not part of the html when it is first loaded, they are
 // added by js when it displays the filtered data, and therefore the
 // js wont respond to "$('.iss-page-click').on('click', function()"

 $(document).on('click', ".feat-page-click", function() {

         // Get the page number the user clicked on

         var page = $(this).data('value');

         console.log("in feat-page-click");

         console.log("this page: " + page);

         // Get the current values of the filters and the search box

         let featuresFilter = getFeaturesFilterValue();
         let statusFilter = getStatusFilterValue();
         let paidFilter = getPaidFilterValue();
         let clientFilter = getClientFilterValue();
         let searchValue = document.getElementById('ftr-search-val').value

         console.log("paidFilter: " + paidFilter);

         // Get the features as per the filter values and page number

         getFeatures(featuresFilter, statusFilter, paidFilter, clientFilter, page, searchValue);
     }

 );


 // User wants to add a quantity of a specific feature to the cart

 $(document).on('click', ".add-btn-click", function() {

     // Extract the button element just clicked on, and separate the
     // classes into an array. The featureId is the first class
     // e.g. the button element is created like this:
     // <button class='" + featureId + " btn td-add-btn-style td-form-font td-add add-btn-click' type='submit'>
     // So if the feature id = '16', 'classes' below will be = "16 btn td-add-btn-style td-form-font td-add add-btn-click", 
     // where 'i6' is the id of the feature relevant to the Add button just clicked. We want to get the featureId

     var classes = $(this).attr("class").split(" ");

     let featureId = classes[0];

     console.log("addFeatureId = " + featureId);

     // Get the quantity input by the user
     // Each quantity field has an id of "qty_featureId". To find
     // the correct qty field we need to create the 'id'. So if the
     // featureId is '16', the id will be 'qty_16'.

     var qtyId = "qty_" + featureId;

     console.log("qtyId = " + qtyId);

     var qty = document.getElementById((qtyId)).value;

     console.log("qty = " + qty);

     // Add the feature / qty to the cart

     $.post({
         url: "{% url 'add_to_cart_js' %}",

         data: {
             csrfmiddlewaretoken: "{{csrf_token}}",
             featureId: featureId,
             qty: qty

         },

         success: function(data) {

             // We need to update the quantity showing for the cart
             // Get the current value showing in the cart and add the
             // new quantity

             console.log("current value in dom: " + parseInt(document.getElementById('feature_count').innerText));

             var currentQty = parseInt(document.getElementById('feature_count').innerText);

             // If there's nothing in the cart yet - set to zero and
             // enable the cart link

             if (isNaN(currentQty)) {
                 currentQty = 0
                 $('.cart-nav-link').removeClass('disabled-link')
                 $('.cart-nav-link').addClass('cart-enabled-link')
             }

             console.log("currentQty = " + currentQty);

             var newQty = currentQty + parseInt(qty);

             $('#feature_count').text(newQty);

             // Reset the qty field to zero

             document.getElementById((qtyId)).value = 0
         }
     });

 });


 // ================
 // HELPER FUNCTIONS
 // ================

 // Get the current value of the Features Filter

 function getFeaturesFilterValue() {

     // Get the current value of the Features Filter

     let el = document.getElementById("dropdownMenuLink-1");
     let featuresFilter = el.innerText;

     return featuresFilter;

 }


 // Get the current value of the Paid Filter

 function getPaidFilterValue() {

     let el = document.getElementById("dropdownMenuLink-3");
     let paidFilter = el.innerText

     if (el.innerText != "ALL" & el.innerText != "") {

         let paidArray = el.innerText.split("");
         console.log("in getPaidFilterValue.  paidArray[0,0]: " + paidArray[0, 0])
         paidFilter = paidArray[0, 0];
     }

     console.log("in getPaidFilterValue. paidFilter: " + paidFilter)

     return paidFilter;

 }


 // ====================
 // PAGINATION FUNCTION
 // ====================

 // Get the pagination parameters passed from 
 // views.get_features and output them to the html page,
 // so that the user can select the pages

 function outputPaginationValues(data, listType) {

     var has_other_pages = data.pagination_props.has_other_pages;
     var has_prev_page = data.pagination_props.has_prev_page;
     var current_page = data.pagination_props.current_page;
     var has_next_page = data.pagination_props.has_next_page;
     var prev_page_nr = data.pagination_props.prev_page_nr;
     var next_page_nr = data.pagination_props.next_page_nr;
     var page_range = data.pagination_props.page_range;

     // Clear the pagination nav, in case we only have one page

     $("#paginate").empty();

     // NOTE: The html elements weren't rendering correctly when I output the values straight
     // to the <ul> / <li> e.g. it was adding </ul> / </li> in places where I didnt want them. 
     // To get around the problem I output the html elements to a variable first, then output it
     // to the html element. This worked.

     if (has_other_pages) {

         if (has_prev_page) {

             if (listType == "issues") {

                 // Output the class 'iss-page-click' or 'feat-page-click', depending on whether the
                 // list being paginated is for Issues or Features, so that the correct js functions will be 
                 // triggered for each list
                 // Also Output the class 'iss-page-live-link' or 'ftr-page-live-link', depending on whether the
                 // list being paginated is for Issues or Features, so that they will be highlighted with the correct
                 // color or hover

                 var prevPageLink = "<ul class='pagination justify-content-center mt-3'><li class='page-item'><a class='page-link iss-page-live-link iss-page-click' href='#' data-value=" + prev_page_nr + " aria-label='Previous'>&laquo;</a></li>";
             }
             else {
                 prevPageLink = "<ul class='pagination justify-content-center mt-3'><li class='page-item'><a class='page-link ftr-page-live-link feat-page-click' href='#' data-value=" + prev_page_nr + " aria-label='Previous'>&laquo;</a></li>";
             }
         }

         else {
             prevPageLink = "<ul class='pagination justify-content-center mt-3'><li class='page-item'><span class='page-link' aria-label='Next'>&laquo;</span></li>";

         }

         // Output the pagination values to the html page

         var pageLinks = "";
         var i = 0;

         for (i in page_range) {

             if (current_page === page_range[i]) {

                 if (pageLinks == "") {

                     if (listType == "issues") {

                         // Output the class 'iss-selected' or 'ftr-selected' depending on whether this is the
                         // issues list or features list, so that the highlight color for each will be applied

                         pageLinks = "<li class='page-item'><span class='page-link iss-selected'>" + page_range[i] + "<span class='sr-only'>(current)</span></span></li>";
                     }
                     else {
                         pageLinks = "<li class='page-item'><span class='page-link ftr-selected'>" + page_range[i] + "<span class='sr-only'>(current)</span></span></li>";
                     }

                 }
                 else {

                     if (listType == "issues") {

                         // Output the class 'iss-selected' or 'ftr-selected' depending on whether this is the
                         // issues list or features list, so that the highlight color for each will be applied

                         pageLinks = pageLinks + "<li class='page-item'><span class='page-link iss-selected'>" + page_range[i] + "<span class='sr-only'>(current)</span></span></li>";
                     }
                     else {
                         pageLinks = pageLinks + "<li class='page-item'><span class='page-link ftr-selected'>" + page_range[i] + "<span class='sr-only'>(current)</span></span></li>";
                     }
                 }
             }
             else {

                 if (pageLinks == "") {

                     // Output the class 'iss-page-click' or 'feat-page-click', depending on whether the
                     // list being paginated is for Issues or Features, so that the correct js functions will be 
                     // triggered for each list
                     // Also Output the class 'iss-page-live-link' or 'ftr-page-live-link', depending on whether the
                     // list being paginated is for Issues or Features, so that they will be highlighted with the
                     // correct color on hover

                     if (listType == "issues") {
                         pageLinks = "<li class='page-item'><a class='page-link iss-page-live-link iss-page-click' href='#' data-value=" + page_range[i] + ">" + page_range[i] + "</a></li>";
                     }
                     else {
                         pageLinks = "<li class='page-item'><a class='page-link ftr-page-live-link feat-page-click' href='#' data-value=" + page_range[i] + ">" + page_range[i] + "</a></li>";

                     }
                 }
                 else {

                     // Output the class 'iss-page-click' or 'feat-page-click', depending on whether the
                     // list being paginated is for Issues or Features, so that the correct js functions will be 
                     // triggered for each list
                     // Also Output the class 'iss-page-live-link' or 'ftr-page-live-link', depending on whether the
                     // list being paginated is for Issues or Features, so that they will be highlighted with the
                     // correct color on hover

                     if (listType == 'issues') {
                         pageLinks = pageLinks + "<li class='page-item'><a class='page-link iss-page-live-link iss-page-click' href='#' data-value=" + page_range[i] + ">" + page_range[i] + "</a></li>";
                     }
                     else {

                         pageLinks = pageLinks + "<li class='page-item'><a class='page-link ftr-page-live-link feat-page-click' href='#' data-value=" + page_range[i] + ">" + page_range[i] + "</a></li>";
                     }

                 }
             }

         }

         if (has_next_page) {

             // Output the class 'iss-page-click' or 'feat-page-click', depending on whether the
             // list being paginated is for Issues or Features

             if (listType == "issues") {

                 var nextPageLink = "<li class='page-item'><a class='page-link iss-page-live-link iss-page-click' href='#' data-value=" + next_page_nr + ">&raquo;</a></li>";
             }
             else {

                 var nextPageLink = "<li class='page-item'><a class='page-link ftr-page-live-link feat-page-click' href='#' data-value=" + next_page_nr + ">&raquo;</a></li>";
             }

         }
         else {

             nextPageLink = "<li class='page-item'><span class='page-link'>&raquo;</span></li>";

         }

         var pageNav = prevPageLink + pageLinks + nextPageLink + "</ul>";


         $("#paginate").append(
             pageNav
         );
     }
 }


 // =================================
 // Get the features from the database 
 // =================================

 // Get the relevant features, based on the value of the filters

 function getFeatures(featuresFilter, statusFilter, paidFilter, clientFilter, page, searchValue) {

     console.log("in getFeatures(). page = " + page)

     $.post({
         url: "{% url 'get_features' %}",

         data: {
             csrfmiddlewaretoken: "{{csrf_token}}",
             featuresFilter: featuresFilter,
             statusFilter: statusFilter,
             paidFilter: paidFilter,
             clientFilter: clientFilter,
             page: page,
             searchValue: searchValue,

         },

         success: function(data) {

             console.log("after success")

             // Display user message if one is returned
             // If the message is blank, keep the line space, but make
             // it invisible on the screen

             var userMessage = data.user_mesg.user_message;
             console.log("have user_message")

             if (userMessage != "") {
                 console.log("userMessage: " + userMessage);
                 $('.user-message').text(userMessage);
                 $('.user-message').removeClass('blank-line');
             }
             else {
                 $('.user-message').text("blank");
                 $('.user-message').addClass('blank-line');
             }


             // Clear the current contents of the table
             // Output the details of each feature to the table 

             $("tbody").empty();
             $.each(data.features, function(key, value) {

                 console.log("in table body")

                 var featureId = value.id;

                 var inputDate = value.date;
                 var user = value.user;

                 // Initialise 'disabled' to be added to quantity & amount

                 var cartDisabled = "";
                 var cartEnabled = "";

                 if (value.user_type == "C") {
                     var assignedUser = value.assigned_client_user;
                     cartEnabled = " ftr-enabled-link"

                 }
                 else {
                     var assignedUser = value.assigned_vendor_user;

                     // For vendor-side user, quantity & +Add will be disabled

                     cartDisabled = "disabled";
                 }

                 var softwareComponent = value.software_component;
                 var summary = value.summary;
                 var status = value.status;
                 var paid = value.paid;
                 var price = value.price;

                 // Output the Feature Details to the table, including the 'more' icon in the last cell

                 $("tbody").append(
                     "<tr><td class='d-table-cell td-date'>" + inputDate + "</td><td class='d-md-table-cell td-username'>" + assignedUser + "</td><td class='d-md-table-cell td-sw-comp'>" + softwareComponent + "</td><td class='td-summary'>" + summary + "</td><td class='text-center td-status'>" + status + "</td><td class='text-center td-paid'>" + paid + "</td><td class='text-center td-price'>" + price + "</td>" +
                     "<form method='post' class='form-inline' action=/cart/add/" + featureId + "/" + ">" + " {% csrf_token %}" + "<div class='input-group'>" + "<td class='td-qty pr-0 mr-0'>" + "<input id=" + "qty_" + featureId + " name='quantity' type='number' min='1' value='0' max='999' class='form-control td-form-font' placeholder='Quantity'" + cartDisabled + ">" + "</td><td class='pl-0 ml-0'>" + "<button class='" + featureId + " btn td-add-btn-style td-form-font td-add add-btn-click" + cartEnabled + " type='submit'" + cartDisabled + "><i class='fas fa-plus'></i>Add</button>" + "</td></div></form>" + "<td class='text-center td-more'><a class='ftr-more-icon-style' href=/issue_tracker/features/" + featureId + "/ " + "><i class='fas fa-ellipsis-h more-icon-style'></i></a></td></tr>"
                 );

                 console.log("input date: " + inputDate + " user:  " + user + " summary: " + summary);

             });

             // Output the pagination parameters for the features list to the html page

             let listType = "features"
             outputPaginationValues(data, listType);

         },


         traditional: true
     }).done();
 }

 // Next function here
 