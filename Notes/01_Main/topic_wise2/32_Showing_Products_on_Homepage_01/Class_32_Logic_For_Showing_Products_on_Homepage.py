"""
-> now we have do display all the product in the homepage
-> Logic for showing Products:
    => No of Slides:
        *) There are 4 items in one slide
        *) If we have n items we will have n//4+1 slides if n is not divisible by 4
        *) but if n is divisible by 4 we have n//4 slides
        *) So the formula fo rno of slides will be 
        *) (n//4)+ceil((n/4)-(n//4)) where cil is least integer function

        -> NOTE: n//4 : is the float division operation in python
    
    => Python Logic:
        *) We will sidplay the first item by default and give it the active tag
        *) The next items will be fetch uisng a for loop
        *) We wil fetch all the details from the database and will show them in the homepage
        *) Later we will do the same thing category-wise
"""
