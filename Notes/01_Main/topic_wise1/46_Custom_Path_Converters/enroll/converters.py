# Creating Custom Url Path Converters


class FourDigitYearConverter:
    regex = '[0-9]{4}'
    # 0-9 mathematical digit, and of 4 digit

    def to_python(self, value):
        # this function will convert url type into the type that we want to python
        # now we will convert it into the integer
        return int(value)

    def to_url(self, value):
        # this function will convert the python type into url type

        # converting value into string
        return f'{value:4d}'
        # 4d: four width of integer

        # another way to convert into url
        return '%4d' % value
