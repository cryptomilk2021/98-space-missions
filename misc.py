import pandas as pd

def scrub_it():
    df = pd.read_csv('mission_launches.csv')

    # create Origin column, create one word Origin place for clean plotting, scrub data
    df['Origin'] = df['Location']
    # scrub data in Origin
    for i in range(len(df['Origin'])):
        a_string = df['Origin'][i]
        filtered_characters = list(s for s in a_string if s.isprintable())
        filtered_string = ''.join(filtered_characters)
        temp = filtered_string.split()
        if temp[-1] == 'Facility':
            df['Origin'][i] = 'USA'
        elif temp[-1] == 'Zealand':
            df['Origin'][i] = 'New Zealand'
        elif temp[-1] == 'Canaria':
            df['Origin'][i] = 'Spain'
        elif temp[-1] == 'Site':
            # print(df['Origin'][i])
            # df['Origin'][i] = 'Spain'
            df['Origin'][i] = 'Iran'
        elif temp[-1] == 'Ocean':
            # print(df['Origin'][i])
            df['Origin'][i] = 'USA'
        elif temp[-1] == 'Sea':
            # print(df['Origin'][i])
            df['Origin'][i] = 'Russia'
        elif temp[-1] == 'Kazakhstan':
            # print(df['Origin'][i])
            df['Origin'][i] = 'Russia'
        elif temp[-1] == 'Kenya':
            # print(df['Origin'][i])
            df['Origin'][i] = 'Italy'
        else:
            df['Origin'][i] = temp[-1]

    return df