def getCountryCode(country: str):
    if country.lower() == 'iran':
        return '+98'
    elif country.lower() == 'usa':
        return '+1'
    else:
        return None