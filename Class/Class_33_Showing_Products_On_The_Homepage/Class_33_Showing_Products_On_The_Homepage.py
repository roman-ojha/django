"""
-> now we will going to fetch or show the product in the website fetching from the database
-> now we will go to shop view.py and write some code to fetch product and pass those throught render function

-> after fetching and sending params to the index.html we will write and create for loop inside the index.html like this:
    -> {% for i in range %}
      <li data-target="#demo" data-slide-to="{{i}}"></li>
      {% endfor %}

-> and we will for loop to display the product:
    -> {% for i in product|slice:"1:"%}
        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem">
            <img src="/media/{{i.image}}" class="card-img-top" alt="..." />
            <div class="card-body">
              <h5 class="card-title">{{i.product_name}}</h5>
              <p class="card-text">{{i.desc}}</p>
              <a href="#" class="btn btn-primary">Add To Cart</a>
            </div>
          </div>
        </div>
        {% if forloop.counter|divisibleby:3 and forloop.counter > 0 and not
        forloop.last %}
        </div>
      <div class="carousel-item">{% endif %} {% endfor %}</div>

      -> and show the product data into the website by using {{}}
"""
