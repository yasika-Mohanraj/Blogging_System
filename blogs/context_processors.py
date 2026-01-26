from assignments.models import SocialLink
from .models import Category 
def get_categories(request):
    cats = Category.objects.all()
    return {'categories': cats}

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)
