def classification_return(value):
    if value == 1:
        return 'defaulter'
    
    return 'non defaulter'


def clusterization_return(value):
    data = {}
    data['risks'] = {}

    low_risk = 16.98
    medium_risk = 36.14
    high_risk = 9.85

    if value == 0:
        data['groupName'] = 'Low risk of fraud'
        data['risk'] = low_risk
    
    elif value == 1:
        data['groupName'] = 'Medium risk of fraud'
        data['risk'] = medium_risk

    else:
        data['groupName'] = 'High risk of fraud'
        data['risk'] = high_risk

    

    return data
    
