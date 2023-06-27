def monthConv(num_or_str):
    month_dict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }
    reversed_dict = {value: key for key, value in month_dict.items()}
    if type(num_or_str) == str:
        try:
            return month_dict[num_or_str.lower().strip().capitalize()]
        except:
            raise(ValueError(f'input not a month input was {num_or_str}'))
        if num_or_str.lower()=='january':
            return 1
        if num_or_str.lower() =='february':
            return 2
        return "test"
    try:
        return reversed_dict[int(num_or_str)]
    except:
        raise(ValueError(f'input not a month input was {num_or_str}'))
    return "false"

if __name__ == "__main__":
    print(monthConv(2))
    print(monthConv("April"))