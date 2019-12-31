from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse
from django.http import JsonResponse 

from datetime import datetime

from app2_user_home.models import Vendor
from app2_user_home.models import Client
from app2_user_home.models import UserDetail
from .models import Feature, FeatureComment, FeaturePaid

from .forms import LogNewFeatureForm, UpdateFeatureForm, FeatureCommentForm


"""
Features home page
"""

def features_home(request):
    
    # Initialise the feature filters
    
    SelectedFeaturesFilter = "ASSIGNED TO ME"
    
    # Set Client Filter to ALL
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter to ALL
    
    SelectedStatusFilter = "ALL"
    
    # set Paid Order to ALL
    
    SelectedPaidOrder = "SORT BY"
    
    # Initialise these details in case user is not set up on the Issue Tracker app
    
    AllClients = ""
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details from re the Issue Tracker app. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details
            
        ClientDetails = get_client(request, UserDetails.vend_client_code)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        
        # Get all clients for Client Dropdown - only available to Vendor-side 
        # users
            
        AllClients = get_all_clients(request)
            
            
    # Get all features
    
    Features = ""
    
    # Get the features assigned to the logged in user only. 
    # A feature can be assigned both to a client-side user and a vendor-side user, 
    # so we need to verify which one it is
    
    if UserDetails.user_type == "C":
            
        # User is on the Client side
        
        try:
            Features = Feature.objects.filter(assigned_client_user=UserDetails.user_id)
        except:
            messages.error(request, "PROBLEM RETRIEVING FEATURES!")
    
    else:
        # User is on the Vendor side
        
        try:
            Features = Feature.objects.filter(assigned_vendor_user=UserDetails.user_id)
        except:
            messages.error(request, "PROBLEM RETRIEVING FEATURES!")
    
    # Final filtering is done here to make sure users only see what they're
    # allowed to see, and they're sorted by date, descending
    
    Features = FinalFilterFeatures(request, Features, UserDetails, SelectedPaidOrder)
                
    
    # For Pagination
    
    page = request.GET.get('page', 1)
    paginator = Paginator(Features, 5)
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
    
    # Pass features back as 'listing'. It will be used to pick up the pagination
    # variables in base.html. The same will be done with the issues list.
    
    listing = features
    list_type = "features"
    searching = 'n'
  
    return render(request, 'featureshome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "all_clients": AllClients,'features': features, 'selected_features_filter':SelectedFeaturesFilter, 'selected_status_filter': SelectedStatusFilter, "selected_paid_order": SelectedPaidOrder, 'selected_client_filter': SelectedClientFilter, "listing":listing, "list_type": list_type, "searching": searching })



"""
This function is called via the javascript in base.html
Get the features, filtered by the features Filter options selected
"""
def get_features(request):
    
    data = []
    
    # Get the user's details relating to the Issue Tracker app - it has
    # already been established that the user's details exist, otherwise they
    # wouldnt have got this far
            
    UserDetails = get_user_iss_trk_details(request)
        
    # Get the filters - passed from the js in base.html
        
    features_filter = request.POST.get('featuresFilter')
    status_filter = request.POST.get('statusFilter')
    paid_order = request.POST.get('paidOrder')
    client_filter = request.POST.get('clientFilter')
    search_value = request.POST.get('searchValue')
    
    # If the user is not using the search box, filter according to the filter
    # values
    
    if not search_value:
        
        # Get all the features from the features database
        
        Features = Feature.objects.all()
        
        # User has requested all features assigned to them?
                
        if features_filter == 'ASSIGNED TO ME':
                    
            # Is this a Client-side user?
                    
            if UserDetails.user_type == "C":
        
                Features = Features.filter(assigned_client_user = UserDetails.user_id)
        			
            else:
                    
                # This is a Vendor-side user
                    
                Features = Features.filter(assigned_vendor_user = UserDetails.user_id)
                    
        else:
                    
            # Has user requested 'Our Features Only'?
            # This option is relevant to Client-side users only'
                    
            if features_filter == 'OUR FEATURES ONLY':
                        
                Features = Features.filter(client_code = UserDetails.vend_client_code)
                                
            else:
                        
                # Has user requested 'Other Clients' features Only?
                    
                if features_filter == "OTHER CLIENTS' FEATURES ONLY":
                
                    Features = Features.exclude(client_code = UserDetails.vend_client_code)
            
        # Filter features further if status filter is set . . .
            
        if status_filter != "ALL":
            Features = Features.filter(status=status_filter)
            
        # . . . or if Client filter is set (client filter is availabe to vendor
        # -side users only)
            
        if client_filter != "ALL":
            
            Features = Features.filter(client_code=client_filter)
            
    else:
        
        # User is using the search box to find features. Select features based on the 
        # value input by the user only - if the value is found in the 'summary' field
        # extract the feature
        
        Features = Feature.objects.filter(summary__icontains=search_value)
        
    # Final filtering is done here to make sure users only see what they're
    # allowed to see, and they're sorted by date, descending, or by paid amount
    
    Features = FinalFilterFeatures(request, Features, UserDetails, paid_order)
    
    user_message = ""
    
    if not Features:
        user_message = "No features found for the selected criteria!"
    
    # For Pagination
    
    page = request.POST.get('page', 1)
    
    paginator = Paginator(Features, 5)
    
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
        
    # Save the pagination parameters for use in the js function in base.html
    # that called 'get_features'
        
    has_other_pages = features.has_other_pages()
    has_prev_page = features.has_previous()
    current_page = features.number
    has_next_page = features.has_next()
    
    prev_page_nr = 0
    if features.has_previous():
        prev_page_nr = features.previous_page_number()
        
    next_page_nr = 0
    if features.has_next():
        next_page_nr = features.next_page_number()
        
    page_range = paginator.page_range
    
    # Create data dictionary to return to the js function (in base.html)
    
    data = {}

    # Return the pagination parameters to js for output to the html file
    
    data["pagination_props"] = {
		"has_other_pages": has_other_pages,
		"has_prev_page": has_prev_page,
		"current_page": current_page,
		"has_next_page": has_next_page,
		"prev_page_nr": prev_page_nr,
		"next_page_nr": next_page_nr,
		"page_range": list(page_range)
	}
	
    # Return the user message also - set above if no features found
    
    data["user_mesg"] = {
        
        "user_message": user_message
	  }
	
	# Return the features to be output to  the html table
	
    data["features"] = []
    
    
    for feature in features:
        
        user_id = feature.user_id
        assigned_client_user = feature.assigned_client_user
        	
        if UserDetails.user_type == "C":
            if feature.client_code != UserDetails.vend_client_code:
    	        user_id = "*********"
    	        assigned_client_user = "*********"
    	    
        data["features"].append({
            
            "id": feature.id,
        	"title": feature.title,
        	"details": feature.details,
        	"client_code": feature.client_code,
            "date": datetime.strftime(feature.input_date, '%d %b %y'),
        	"user": user_id,
        	"assigned_client_user": assigned_client_user,
        	"assigned_vendor_user": feature.assigned_vendor_user,
        	"software_component": feature.software_component,
        	"paid": feature.paid,
        	"price":feature.price,
        	"summary": feature.summary,
        	"status": feature.status,
        	"thumbs_up_count": feature.thumbs_up_count,
        	"user_type": UserDetails.user_type
        	
    })
        
    return JsonResponse(data, safe=False)




"""
Create a view that returns a single Post object based on the Post ID(pk)
and render it to the 'postdetail.html' template or return a 404 error if
the Post is not found.
"""
def feature_details(request, pk, view_comments=None):
    
    # Retrieve the feature
    
    feature = get_object_or_404(Feature, pk=pk)
    
     # Get this feature's comments 
    
    try:
        featurecomments = FeatureComment.objects.filter(feature_id=feature.id)
    except:
        messages.error(request, "No comments for this Feature yet")
    
    # List the feature comments in reverse input order
        
    featurecomments = featurecomments.order_by('-id')
    
    # If the user is on the Client side we need the Client details, otherwise
    # we need the Vendor details
    
    ClientDetails = ""
    VendorDetails = ""
    FeatureClientDetails = ""
    
    # Get the user's details from re the Issue Tracker app. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
    
    FeatureClientDetails = ""
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details, The features Filter
        # values the client user can use, and the filtered Features
            
        ClientDetails = get_client(request, UserDetails.vend_client_code)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        
        FeatureClientDetails = get_feature_client_details(request, feature)
    
    return  render(request, 'featuredetails.html', {'feature': feature, 'featurecomments': featurecomments, 'view_comments': view_comments, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "featureclientdetails": FeatureClientDetails})
    



"""
Get the logged in user's details re the Issue Tracker app. 
These details tells us whether the User is on the Vendor side or 
the Client side.
"""
    
def get_user_iss_trk_details(request):
    
    UserDetails = ""

    try:
        UserDetails = UserDetail.objects.get(user_id=request.user.username)
    except:
        messages.error(request, "Problem retrieving the user's Issue Tracker Details!")
    
    return UserDetails


"""
Get all client-side users - needed for the 'assigned user dropdown' when editing a feature.
"""
    
def get_all_client_users(request, user_client_code):
    
    print("in features get_all_client_users~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    print("user_client_code: "+str(user_client_code))
    
    AllClientUsers = ""

    try:
        AllClientUsers = UserDetail.objects.filter(vend_client_code = user_client_code, user_type = "C")
    except:
        messages.error(request, "Problem retrieving the all client users from Issue Tracker!")
        
    print("AllClientUsers: "+str(AllClientUsers))
    
    return AllClientUsers
    

"""
Get all vendor-side users - needed for the 'assigned user dropdown' when updating a feature.
"""
    
def get_all_vendor_users(request):
    
    AllVendorUsers = ""

    try:
        AllVendorUsers = UserDetail.objects.filter(user_type = "V")
    except:
        messages.error(request, "Problem retrieving the all vendor users from Issue Tracker!")
    
    return AllVendorUsers
    

    
"""
Get the Client details
"""

def get_client(request, get_client_code):

    try:
        ClientDetails = Client.objects.get(client_code=get_client_code)
    except:
        messages.error(request, "Client details not found!")
   
    return  ClientDetails
    

"""
All Client records needed for Client Dropdown if Vendor user is logged in 
"""

def get_all_clients(request):
    
    AllClients = ""

    try:
        AllClients = Client.objects.all()
    except:
        messages.error(request, "Problem retrieving all Client Records!")
   
    return  AllClients
    
    
"""
The logged in user is on the Vendor side - get the Vendor details
"""
def get_vendor(request, UserDetails):
        
        try:
            VendorDetails = Vendor.objects.get(vend_code=UserDetails.vend_client_code)
        except:
            messages.error(request, "Vendor details not found!")
        
        return  VendorDetails
        
        
"""
Get the details of the Client the feature belongs to. This is required for a Vendor
user only. Although Client-side users see other clients' features, they dont see
the details of those clients.
"""
def get_feature_client_details(request, feature):
    
    FeatureClientDetails = ""

    try:
        FeatureClientDetails = Client.objects.get(client_code=feature.client_code)
    except:
        messages.error(request, "Feature Client details not found!")
        
    return FeatureClientDetails


"""
Final filter to make sure users see only what they're allowed to see.
Vendors can only see features when they reach status of 'LOGGED' (i.e. they cannot
see 'DRAFT')
Clients cannot see features of other clients that are of status 'DRAFT' or 'LOGGED'
"""

def FinalFilterFeatures(request, Features, UserDetails, paid_order):
    
    if UserDetails.user_type == "V":
        
        # This is a Vendor-side user
        # Vendors cannot see features until they reach status 'LOGGED'
                
        Features = Features.exclude(status = "DRAFT")
    
    else:
        
        # Client-side users cannot see features of other clients that are still
        # at status 'DRAFT' or 'LOGGED'
        
        # Separating our clients from other clients, so that I can filter other 
        # clients features by status
        
        OurClientsFeatures = Features.filter(client_code = UserDetails.vend_client_code)
        
        OtherClientsFeatures = Features.exclude(client_code = UserDetails.vend_client_code)
        OtherClientsFeatures = OtherClientsFeatures.exclude(status = "DRAFT").exclude(status = "LOGGED")
        
        # Putting the two lists together after filtering other clients features
        
        Features = OurClientsFeatures | OtherClientsFeatures
    
    # Sorting features by date, descending order, or by paid amount if selected
    
    if paid_order != "SORT BY":
        
        if paid_order == "LOWEST TO HIGHEST":
            Features = Features.order_by('paid')
        else:
            Features = Features.order_by('-paid')
            
    else:
        
        Features = Features.order_by('-id')
        
    return Features


"""
Create a view that allows us to log a new feature or edit an existing one 
depending on whether the pk is null or not. 
"""
def new_edit_feature(request, pk=None):
    
    # If the user is on the Client side we need the Client details, otherwise
    # we need the Vendor details
    
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details from re the Issue Tracker app. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # User is on the Client side - otherwise they wouldnt be in this view. 
    # Get the Client Details.
            
    ClientDetails = get_client(request, UserDetails.vend_client_code)
    
    # Get a list of all client-side users, to be used in the Assigned User
    # dropdown list when updating an issue
        
    AssignedUsers = get_all_client_users(request, UserDetails.vend_client_code)
    
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    
    if request.method == "POST":
        
        form = LogNewFeatureForm(request.POST, request.FILES, instance=feature)
        
        print("feature form: "+str(form))
        
        if form.is_valid():
        
            feature = form.save()
            
            view_comments = 'n'
            return redirect(feature_details, feature.pk, view_comments)
        else:
            messages.error(request, "UNABLE TO LOG FEATURE!")
            
    else:
        
        form = LogNewFeatureForm(instance=feature)
    
    return  render(request, 'featurelogging.html', {'form': form, "feature": feature, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "assigned_users": AssignedUsers })


"""
Create a view that allows a vendor-side user to change the status of a featur. 
"""
def update_feature(request, pk=None):
    
    # This view is for vendor-side users only
    
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details from re the issue tracker app. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details, The Issues Filter
        # values the client user can use, and the filtered Issues
            
        ClientDetails = get_client(request, UserDetails.vend_client_code)
        AssignedUsers = get_all_client_users(request, UserDetails.vend_client_code)
        
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        AssignedUsers = get_all_vendor_users(request)
        
    feature = get_object_or_404(Feature, pk=pk)
    
    FeatureClientDetails = get_feature_client_details(request, feature)
    
    
    if request.method == "POST":
        
        form = UpdateFeatureForm(request.POST, request.FILES, instance=feature)
        
        print("featureupdateform=============: "+str(form))
        
        if form.is_valid():
        
            feature = form.save()
            
            view_comments = 'n'
            return redirect(feature_details, feature.pk, view_comments)
        else:
            messages.error(request, "UNABLE TO LOG FEATURE!")
            
    else:
        
        form = UpdateFeatureForm(instance=feature)
    
    return  render(request, 'featureupdate.html', {'form': form, "feature": feature, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "featureclientdetails": FeatureClientDetails, "assigned_users": AssignedUsers})



"""
New Feature comment - get the feature comments form. This view is called when
the user clicks '+' to add a comment. The id of the featue is passed to the view
"""
def new_feature_comment(request, pk=None):
    
    # If the user is on the Client side we need the Client details, otherwise
    # we need the Vendor details
    
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details re the issue tracker app. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details, The Features Filter
        # values the client user can use, and the filtered Features
            
        ClientDetails = get_client(request, UserDetails.vend_client_code)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
    
    # Get the Feature for which the comment is being input
    
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    
    save_feature_id = pk
    
    pk = ""
    
    featurecomment = get_object_or_404(FeatureComment, pk=pk) if pk else None
    
    comments_input = "n"
    view_comments = 'n'
    
    if request.method == "POST":
        
        form = FeatureCommentForm(request.POST, request.FILES, instance=featurecomment)
        
        if form.is_valid():
        
            featurecomment = form.save()
            
            # Redirect to feature_details and pass 'y' to let featuredetails.html
            # know that the comments list is to be displayed
            
            view_comments = 'y'
            
            return redirect(feature_details, featurecomment.feature_id, view_comments)
        else:
        
            messages.error(request, "UNABLE TO LOG FEATURE COMMENT!")
            
    else:
    
        form = FeatureCommentForm()
        
        # Set comments_input to keep the comment form fields open in featuredetails.html
    
        comments_input = "y"
        
        # Set view_comments so that the comments list wont be displayed in 
        # featuredetails.html
        
        view_comments = 'n'
    
    return  render(request, 'featuredetails.html', {'form': form, "feature": feature, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "comments_input": comments_input, "view_comments": view_comments })


"""
FEATURES REPORT - 
For Client-side users - This report will show a total line of the number of features the Client has requested - these will include those
logged by this Client, and those that they flagged as having via the 'thumbs up' and have paid for. They can click the down arrow to see a list of
these features, and click on the chevron icon to see the details of a feature.

For Vendor-side users - This report will show a total line for each client, showing the number of features they have  requested. These will include those
logged by the Client, and those that they flagged as having via the 'thumbs up' and have paid for. They can click the down arrow to see a list of
these issues, and click on the chevron icon to see the details of a feature.

This function is called via the javascript in base.html
"""
def features_report(request):
    
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details from re the issue tracker. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details
            
        ClientDetails = get_client(request, UserDetails.vend_client_code)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
    
    
    # Get the feature paid records, depending on the user type
   
    if UserDetails.user_type == "C":
        
        # For client-side user, get the input and paid features for 
        # the client the user is associated with only
        
        featurepaids = FeaturePaid.objects.filter(client_code = UserDetails.vend_client_code)
        
    else:
                    
        # For vendor-side user, get all Clients paid features
                    
        featurepaids = FeaturePaid.objects.all()
    
    if not featurepaids:
        messages.error(request, "NO FLAGGED FEATURES FOUND!")
        
    # Initialise the top level variables
   
    client_list = []
    clienttotals = []
    client_features = []
   
    # Order feature paid records by client code and create the client list
    
    featurepaids = featurepaids.order_by('client_code')
    
    # We just want one copy of the client code in the list
    
    prev_client = ""
        
    for item in featurepaids:
        if item.client_code != prev_client:
            client_list.append(item.client_code)
            prev_client = item.client_code
    
    # Calculate the total amount paid per client, so as to create a report by
    # client in order of amount paid - highest to lowest
    
    client_total = []
    
    for client in client_list:
        
        total_paid_by_client = 0
        
        # Get the features this client has paid for
        
        featurepaids = FeaturePaid.objects.filter(client_code = client)
        
        # Accumulate the amounts paid per feature
        
        for featurepaid in featurepaids:
            total_paid_by_client += featurepaid.amount_paid
        
        # Create a tuple list with client code and total amount paid
        
        client_total.append((client, total_paid_by_client))
    
    # Sort the client/total list by the total amount (Solution for sorting list 
    # by second parameter (total paid) found on https://www.geeksforgeeks.org/python-list-sort/)
    
    client_total.sort(key=sortTotal, reverse = True)
    
    client_list = []
    
    for item in client_total:
        client_list.append(item[0])
        
    # Loop through the clients and loop through the features, either input or paid
    # by them. Create a total line per client and a line per feature
    
    for client in client_list:
        
        # Initialise client level fields
        
        total_paid = 0
        nr_flagged_features = 0
        features = ""
        
        # Get all the paid records for this client - These will be
        # features that were input by this client, and features that were 'paid for'
        # by this client
        # Order the feature list by amount paid - highest to lowest, and feature id - highest to lowest
        
        featurepaids = FeaturePaid.objects.filter(client_code = client)
        featurepaids = featurepaids.order_by('-amount_paid', '-feature_id')
        
        for featurepaid in featurepaids:
            
            # Accumulate the total paid per feature by this client
            
            total_paid += featurepaid.amount_paid
            
            # Loop through the features for this client or paid by this client
            
            feature = Feature.objects.get(id=featurepaid.feature_id)
            
            # Count the number of features input and / or flagged by this client
            
            nr_flagged_features += 1
            
            # Create a line per feature input and / or paid for by this client
            # Note that the 'client_code' field below is the client who input or 
            # paid for the issue, author is the client who originally input the issue.
            # Both codes are sometimes the same and sometimes not - as when a client
            # pays for another client's feature
            
            # Output the details as required for the report
            
            client_features.append({
                "id": feature.id,
                "client_code": client,
                "author": feature.client_code,
            	"software_component": feature.software_component,
            	"amount_paid": featurepaid.amount_paid,
            	"summary": feature.summary,
            	"details": feature.details,
            	"status": feature.status,
            })
        
        
        # Get the details of the current client
        
        ThisClientDetails = get_client(request, client)
        
        # Create a total record for the current client
         
        clienttotals.append({
            "client_code": client,
            "client_name": ThisClientDetails.client_name,
            "total_paid": total_paid,
            "nr_flagged_features": nr_flagged_features
            })

    return  render(request, 'featurereport.html', {"clienttotals": clienttotals, "features": client_features, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails})

"""
'sortTotal' is the key provided to 'client_total.sort'. 'client_total' is a list of 
tuples (client_code, total_paid_by_client). These are sorted by the amount field 
so as to create a client report in order of amount paid by client - highest to lowest.
"""

    # Sort the (client, total amount) list by the total amount (Solution for sorting list 
    # by second parameter (amount) found on https://www.geeksforgeeks.org/python-list-sort/)
    
def sortTotal(val): 
    return val[1]  
  