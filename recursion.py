"""
Find final referrer
User A refer B, And B refer C. So the final refer for C is A
"""

#key: user, value: referrer
referer_table = {
    "B": "A",
    "C": "B",
    "E": "D",
    "F": "E",
    "G": "F"
}

def find_final_referer(user) -> str:
    """
    In [2]: from recursion import find_final_referer

    In [3]: find_final_referer('A')
    Out[3]: 'A'

    In [4]: find_final_referer('C')
    Out[4]: 'A'

    In [5]: find_final_referer('B')
    Out[5]: 'A'

    In [1]: from recursion import find_final_referer

    In [2]: find_final_referer('G')
    Out[2]: 'D'
    """
    ref = final_refer_from_referer_table(user, referer_table)
    if ref is None:
        return user

    return find_final_referer(ref)


def final_refer_from_referer_table(user, table):
    referrer = table.get(user)
    return referrer


def how_many_steps(stairs):
    """
    There are n steps stairs, and one can walk 1 or 2 steps each time.
    How many ways to walk this n stairs
    """
    if stairs == 1:
        return 1
    if stairs == 2:
        return 2
    
    return how_many_steps(stairs-1) + how_many_steps(stairs-2)
