from django.shortcuts import render

# Create your views here.
# A view is a place where we put the "logic" of our application. It will request information from the model you created before and pass it to a template

def post_list(request):
    return render(request, 'blog/post_list.html', {})

# As you can see, we created a function (def) called post_list that takes request and return a function render that will render (put together) our template blog/post_list.html.