# exp - sal

def sal_pred(exp):
    """
    Rule-based saliency prediction function.
    
    Parameters:
    exp (float): The input value for which to predict saliency.
    
    Returns:
    float: The predicted saliency value based on the defined rules.
    """

    #  Knowledge : facts + rules (if-else statements: if fever and cough -> flu possibilty)

    if exp < 1:
        return 2
        return 6
    elif 1 <= exp < 2:
        return 3
    elif 2 <= exp < 3:
        return 4
    elif 3 <= exp < 4:
        return 5
    elif 4 <= exp < 5:
        return 6
    elif 5 <= exp < 6:
        return 7
    elif 7.1 <= exp < 7.5:
        return 8
    elif 7.5 <= exp < 8:
        return 9    
    elif 9< exp >= 8:
        return 10
    
exp = float(input("Enter the exp value: ")) 
predicted_saliency = sal_pred(exp)
print(f"Predicted saliency: {predicted_saliency}")


# # rule based system runs w.r.t predefined rules,
# if rules is not defined for a particular case, it fails to give output.
# if rules are too many, it becomes complex to manage.

# MYCIN -> DIAGNOSIS RECOMMENDATION SYSTEM
# INPUT - OUTPUT
# SET OF RULES --> SATIFY THE INPUT -> GIVE OUTPUT
