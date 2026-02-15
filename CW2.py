header='''BOOK STORE RECEIPT
------------------'''
book1_title='Python Basics'
book1_price=450
book2_title='Data Science Intro'
book2_price=600
total_price=book1_price+book2_price

book1='{}-{} Rs.'
book2='{}-{} Rs.'
total_price_='Total Price={} Rs.'.format(total_price)

thank_you='Thank\tyou\tfor\tshopping\twith\tus!'

receipt=header+'\n'
receipt+=book1.format(book1_title, book1_price)+'\n'
receipt+=book2.format(book2_title, book2_price)+'\n'
receipt+=total_price_+'\n'+thank_you
print(receipt.upper())











