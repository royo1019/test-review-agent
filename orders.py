import os,sys
def process_order(order_id,user_id):
    query="SELECT * FROM orders WHERE id='"+order_id+"'"
    password="admin123"
    try:
        result=db.execute(query)
    except:
        pass
    return result
