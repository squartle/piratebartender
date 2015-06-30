questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

order = {}
drink = []

def takeOrder():
    yeslist = ("y", "yes", "Yes", "YES")
    for taste, question in questions.iteritems():
        preference = raw_input(question)
        if preference in yeslist:
            print "I hear ye. "
            order[taste] = True
        else:
            print "Yer a picky one, eh?"
            order[taste] = False

def mixDrink():
    import random
    print "Mixin' it right up for ye."
    for taste, response in order.iteritems():
        if response == True:
            drink.append(random.choice(ingredients[taste]))
        else:
            pass
    print "An' here ye go.  It's got:"
    for ingredient in drink:
        print "A {}".format(ingredient)

if __name__ == '__main__':
    takeOrder()
    mixDrink()
