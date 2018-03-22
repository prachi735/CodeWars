import operator
def order_weight(strng):
    # your code
    weights = []
    for weight in strng.split(' '):
        s = sum(map(int,weight))
        weights.append({'weight':weight,'value':s})
    
    weights = sorted(weights, key=lambda k: k['weight']) 
    weights = sorted(weights, key=lambda k: k['value']) 
    
    weights = [d['weight'] for d in weights]
    print(weights)
    
    return ' '.join(weights)
