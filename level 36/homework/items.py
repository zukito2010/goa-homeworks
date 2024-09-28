shop_items = {
    'nabeghlavi': True,
    'ball': False,
    'candy': True,
    'lantern':False,
    'gum':False ,  
    
    
}



out_of = list(filter(lambda x: not shop_items[x], shop_items))
print(out_of)