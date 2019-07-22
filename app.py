from sklearn.metrics import mean_absolute_error


def credit_approval(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_1(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if region == 5:
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_2(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 and region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_3(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 4 or region == 5):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_4(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 3 or region == 4):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_5(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age > 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_6(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 25):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_7(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 1):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_8(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 1:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_9(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_10(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 and region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_11(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 2 or region == 3):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_12(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 1 or region == 2):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_13(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 1):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_14(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend == 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_15(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend < 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_16(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 1):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_17(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 1):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_18(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend >= 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_19(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend < 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount


def credit_approval_bug_20(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend <= 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 0):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount

def credit_approval_bug_21(citizen, state, age, sex, region, income_class, no_depend, marital):
    approved = 0
    amount = 0
    if (region == 5 or region == 6):
        amount = 0
    else:
        if (age < 18):
            amount = 0
        else:
            if (citizen == 0):
                amount = 5000 + 1000*income_class
                if state == 0:
                    if (region == 3 or region == 4):
                        amount = amount*2.00
                    else:
                        amount = amount*1.50
                else:
                    amount = amount*1.10
                if (marital == 0):
                    if (no_depend > 0):
                        amount += 200*no_depend
                    else:
                        amount += 500
                else:
                    amount += 1000
                if (sex == 0):
                    amount += 500
                else:
                    amount += 1000
            else:
                amount = 1000 + 800*income_class
                if (marital == 0):
                    if (no_depend > 2):
                        amount += 100*no_depend
                    else:
                        amount += 100
                else:
                    amount += 300
                if (sex == 1):
                    amount += 100
                else:
                    amount += 200
    if amount == 0:
        approved = 0
    else:
        approved = 1
    return approved, amount

def label(i):
    if i == 0:
        return 0
    if i > 0 and i <= 2000:
        return 1
    if i > 2000 and i <= 4000:
        return 2
    if i > 4000 and i <= 6000:
        return 3
    if i > 6000 and i <= 8000:
        return 4
    if i > 8000 and i <= 10000:
        return 5
    if i > 10000 and i <= 12000:
        return 6
    if i > 12000 and i <= 14000:
        return 7
    if i > 14000 and i <= 16000:
        return 8
    if i > 16000 and i <= 18000:
        return 9


def compare(y_pred, y_bug, low, high):
    low, high = low/10, high/10
    score = abs((y_bug-y_pred)/10)
    if score <= low:
        return 1
    elif score >= high:
        return 0
    else:
        return 10
