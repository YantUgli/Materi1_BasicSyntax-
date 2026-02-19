country = "MY"
match country:
    case "ID":
        print("indonesia")
    case "SG":
        print("singapore")
    case "MY":
        print("malaysia")
    case _:
        print("unknown country")