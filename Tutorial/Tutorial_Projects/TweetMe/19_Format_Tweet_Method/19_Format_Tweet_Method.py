""" 
    -> here we had added the function :
        ->  function formatTweetElement(tweet) {
            var formattedTweet = "<div class='mb-4 tweet' id='tweet-" + tweet.id + "'><p>" + tweet.content + "</p></div>"
            return formattedTweet
        }
        -> in 'home.html'

    
=> 20) Like Button Rendering
        -> function handleDidLike (tweet_id, currentCount) {
                return 
            }

            function LikeBtn(tweet) {
                return "<button class='btn btn-primary btn-sm' onclick=handleDidLike(" + 
                tweet.id + "," + tweet.likes + ")>" + tweet.likes + " Likes</button>"
            }

=> 21) Rapid Implement of Bootstrap Theme
    -> now here we had added the bootstrap 'navbar.html' and some style in the homepage
"""
