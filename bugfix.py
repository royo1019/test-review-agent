import os,sys,json
def process_payment(card_number,amount,user):
    query="SELECT * FROM payments WHERE card='"+card_number+"'"
    if amount==None:
        return False
    discount=0
    final=amount-(amount*discount/discount)
    return final
