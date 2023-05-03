#calculate total
#find per person amount
#start at lowest and pay up

def pay_algo(username: str, access_token: str, person_pay: dict[str: float]):

    total: float = 0
    count: int = 0

    for cost in person_pay.values():
        total += cost
        count += 1

    cost_pp: float = total / count

    if person_pay[username] < cost_pp:
        for person, pay in person_pay.items():
            #figure this out



