from django.http import JsonResponse # You already probably import from django.http, add JsonReponse if so
​
"""
Get the Issues, filtered by the Issues Filter option selected
"""
def get_issues(request, UserDetails, SelectedIssuesFilter):
​
	Issues = [] # This is always going to end up as a list, no need to initialize as string
​
	# If the selection is to get all issues assigned to the logged in user,
	# show the issues assigned to the client user or the vendor user, depending
	# on the user type
​
	if SelectedIssuesFilter == "ASSIGNED TO ME":
​
		if UserDetails.user_type == "C":
​
			# User is on the Client side
​
			try:
				Issues = Issue.objects.filter(assigned_client_user=UserDetails.user_name)
				messages.success(request, "Client Issues successfully retrieved!")
			except:
				messages.error(request, "PROBLEM RETRIEVING CLIENT ISSUES!")
​
		else:
​
			# User is on the Vendor side
​
			try:
				Issues = Issue.objects.filter(assigned_vendor_user=UserDetails.user_name)
				messages.success(request, "Vendor Issues successfully retrieved!")
			except:
				messages.error(request, "PROBLEM RETRIEVING VENDOR ISSUES!")
​
	else:
​
		if SelectedIssuesFilter == "ALL ISSUES":
​
			try:
				Issues = Issue.objects.all()
				messages.success(request, "All Issues successfully retrieved!")
			except:
				messages.error(request, "PROBLEM RETRIEVING ALL ISSUES!")
​
		else:
​
			if SelectedIssuesFilter == "OUR ISSUES ONLY":
​
				# "OUR ISSUES ONLY" is relevant to Client side users only
​
				try:
					Issues = Issue.objects.filter(client_code=UserDetails.vend_client_code)
					messages.success(request, "Our Client Issues successfully retrieved!")
				except:
					messages.error(request, "PROBLEM RETRIEVING OUR CLIENT ISSUES!")
​
			else:
​
				if SelectedIssuesFilter == "OTHER CLIENTS' ISSUES ONLY":
​
					# "OTHER CUSTOMERS' ISSUES ONLY" is relevant to Client side users only
​
					try:
						Issues = Issue.objects.exclude(client_code=UserDetails.vend_client_code)
						messages.success(request, "Our Client Issues successfully retrieved!")
					except:
						messages.error(request, "PROBLEM RETRIEVING OUR CLIENT ISSUES!")
​
	data = []
​
	for issue in Issues:
		data.append({
			"issue": issue,
			"title": issue.title,
			"details": issue.details,
			"client_code": issue.client_code,
			"date": issue.input_date,
			"user": issue.user_name,
			"assigned_client_user": issue.assigned_client_user,
			"assigned_vendor_user": issue.assigned_vendor_user,
			"software_component": issue.software_component,
			"priority": issue.priority,
			"summary": issue.summary,
			"status": issue.status,
			"progress": progress
		})
​
	return JsonResponse(data, safe=False)