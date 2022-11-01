def Total_money_we_have_is(friendsAndCash):
    total_money= 0
    for v in friendsAndCash.values():
        cash = int(v[:-1])      #Убираю знак доллара и привожу число из str в int
        total_money += cash
    return total_money

def maximum_cash(friendsAndCash):
    maxi_cash = 0
    for k, v in friendsAndCash.items():
        cash = int(v[:-1])
        if maxi_cash < cash:
           maxi_cash = cash
           name_friend = k
    return name_friend
    
def modified_friendsAndCash(friendsAndCash):
    modified_dict = {}
    for k, v in friendsAndCash.items():
        modified_dict[v] = k
    return modified_dict


friends = input("Введите имена друзей: ").split()
cash_friends = input("Введите наличные деньги друзей в '$': ").split()
friendsAndCash = dict(zip(friends, cash_friends))
print(Total_money_we_have_is(friendsAndCash))
print(maximum_cash(friendsAndCash))
print(modified_friendsAndCash(friendsAndCash))