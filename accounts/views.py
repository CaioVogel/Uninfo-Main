from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Profile


@login_required
def profile(request):
    user = request.user
    if not hasattr(user, 'profile'):
        # If the profile does not exist, you can create it or redirect to a profile creation page
        Profile.objects.get_or_create(user=user)  # Automatically create a profile if it doesn't exist
        # Alternatively, you can redirect to a profile creation form
        # return redirect('profile_creation_view')  # Uncomment this line if you have a creation form

    return render(request, 'profile.html', {'user': user})