"""
In this tutorial we will try to who more then one list of product in home page like:
  1) Man Fashion
  2) Women Fashion
-> so because of the we will going to make a list of list where inside the list we will pust the list of product and there information
-> now go to views.py and write some code for that
-> now after that we will for loop the whole product that we made in previous tutorial in indes.html so that whatever number of category are there in product it will automatically show in the page
-> <div id="demo{{forloop.counter}}" class="carousel slide my-3" data-ride="carousel">
-> here we have use {{forloop.counter}} because id are different and for that we have to create the counter loop so that it would be different
-> <li data-target="#demo{{forloop.parentloop.counter}}" data-slide-to="{{i}}" ></li>
-> and here we have use {{forloop.parentloop.counter}} because from this previously we had use the another for loop so because of the we have to make parentloop rather then that forloop
"""
