""" 
    -> so here we are building tweet form 
    -> now here we will create 'forms.py' file inside the 'tweets' application
        -> and then we will add form model in there and include that inside the 'views.py' 
            -> and we will create :
                -> def tweet_create_view(request, *args, **kwargs):
                    form = TweetForm(request.POST or None)
                    print('post data is', request.POST)
                    if form.is_valid():
                        obj = form.save(commit=False)
                        # do other form related logic
                        obj.save()
                        form = TweetForm()
                    return render(request, 'components/form.html', context={"form": form})

    -> and we will create 'form.html' file inside the 'template/components'
"""
