def get_bookings(body):
    name = body.get("name")
    email = body.get("email")
    phone = body.get("phone")
    destination = body.get("destination")
    date = body.get("date")
    special_note = body.get("special_note")
    return name , email, phone, destination, date, special_note