# MYCIN
# STANDFORD
# MULTIPLE DOCTORS
#  CREATE A SUSTEM - DIAGNOSIS
#  mycin - medical diagnosis and treatment recommendation system

#  1970
#  patiet data:
# user data:

# data:
temp = 103
cougn = True
isFever = True
bacteria_type = "streptococci" | "staphylococci" | "pneumococci"
symptoms = ["sore throat", "headache", "nausea"]

# rules:
if temp > 101 and cougn and isFever:
    diagnosis = "Possible bacterial infection"
    if bacteria_type == "streptococci":
        treatment = "Prescribe penicillin"
    elif bacteria_type == "staphylococci":
        treatment = "Prescribe methicillin"
    elif bacteria_type == "pneumococci":
        treatment = "Prescribe amoxicillin"
    else:
        treatment = "Further tests needed to identify bacteria type"

# 1. TRANSPARENCY - EASY TO UNDERSTAND: LOGIC IS CLEAR

# 2 TRAPRENCY - EASY TO UNDERSTAND: LOGIC IS CLEAR

# 4. COMPLEX -? INCREASED RULES -> HARD TO MANAGE ->
# WE CREATE RULE BASED SYSTEMS FOR SMALL PROBLEMS: 
#  --> INCREASE THE COMPLEXITY -> HARD TO MANAGE
#  --> INCREASING THE RULES 
#  --> MAINTAINENCE IS HARD

# AI - LEARN
# RULE BASED SYSTEM - DO NOT LEARN
# ALL -> PROCESSED THROUGH PREDEFINED RULES
# FOR UNKNOWN CASES -> FAILS TO GIVE OUTPUT