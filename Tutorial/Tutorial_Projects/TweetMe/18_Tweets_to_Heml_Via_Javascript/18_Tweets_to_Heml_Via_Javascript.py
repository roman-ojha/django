""" 
    -> .\manage.py shell
    -> from tweets.models import Tweet
    -> Tweet.objects.create(content="Hello world 02")
        -> to add the data to database another way

    => now here we are loading content fetched form django to 'home.html'
        -> const tweetsElement =document.getElementById('tweets');
            xhr.onload=function(){
                        const serverResponse=xhr.response;
                        const listedItems=serverResponse.response
                        var finalTweetStr="";
                        var i;
                        for(i=0;i<listedItems.length;i++){
                            console.log(listedItems[i]);
                            var currentItem = "<h1 class='mb-4'>"+listedItems[i].id+"</h1>"+"<p>"+listedItems[i].content+"</p>";
                            finalTweetStr+=currentItem;
                        }
                        tweetsElement.innerHTML=finalTweetStr;
                    }
"""
