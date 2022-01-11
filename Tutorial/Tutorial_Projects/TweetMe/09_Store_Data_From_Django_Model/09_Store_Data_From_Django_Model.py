"""
    -> now we will test these things being stored for that we will type:
        -> .\manage.py shell
            -> from tweets.models import Tweet
            -> obj = Tweet()
            -> obj.abc =123
            -> obj.abc

            -> obj.content = "hello world"
            -> obj.save()
                    -> because we had created content models so django will save value to the database

            -> to see the data from the terminal:
                -> exit() first:
                -> .\manage.py shell
                -> from tweets.models import Tweet
                -> obj = Tweet.objects.get(id=1)
                -> obj.content
"""
