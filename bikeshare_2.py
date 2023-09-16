import time 
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    citys =  ['Chicago','New York','Washington']
    months = ["All","January","February","March","April","May","June","July",
                "August","September","October","November","December"]
    days =   ["All","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    print('Hello! Let\'s explore some US bikeshare data!')
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city= input("Would you like to see data for Chicago, New York, or Washington?\n").title()
        if city in citys :
            break 
        else:
            print("I'm sorry but the input is wrong try again \n # Make sure there in no spaces  \n # Double check the speling \n")


    while True :
        choice= input("If you would like to filter by month Or/And day Enter Yes , if not Enter No ?").title()
        if choice.lower() == 'yes':
            # get user input for month (all, january, february, ... , june)
            while True :
                text= "Now which month would you like to see data for in "+city.title()+"?\n Choose from this list (all, january, february, ... , june) \n"
                month= input(text).title()
                if month in months:
                    break 
                else:
                    print("I'm sorry but the input is wrong try again \n # Make sure there in no spaces  \n # Double check the speling \n ")


            # get user input for day of week (all, monday, tuesday, ... sunday)
            while True:
                day= input("Now which day would you like to see data for? \n"+
                "Choose from this list (all, monday, tuesday, ... sunday) \n").title()
                if day in days :
                    break 
                else:
                    print("I'm sorry but the input is wrong try again \n # Make sure there in no spaces  \n # Double check the speling \n")
            break
        elif choice.lower() == 'no':
            month = 'All'
            day = 'All'
            break
        else:
            print("I'm sorry but the input is wrong try again \n # Make sure there in no spaces  \n # Double check the speling \n")

                    
        
    print('-'*40)
    return city, month, day # ('New York', 'All', 'All')==works 


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months =pd.Series(["January","February","March","April","May","June"],[1,2,3,4,5,6])
    days = pd.Series(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],[1,2,3,4,5,6,7]) 

    # display the most common month
    popular_month_index = df['day_of_week'].mode()[0]#get most commen month 
    popular_month = months[popular_month_index] # translate it to words using the series 
    print('Most Popular month :', popular_month)

    # display the most common day of week
    popular_day_index = df['day_of_week'].mode()[0]
    popular_day = days[popular_day_index]
    print('Most Popular day :', popular_day)

    # display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0] 
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0] 
    print('Most Popular Start Station:', start_station)


    # display most commonly used end station
    end_station = df['End Station'].mode()[0] 
    print('Most Popular End Station:', end_station)


    #display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+ " - AND - "+df['End Station'] 
    popular_combination = df['combination'].mode()[0] 
    print('Most Popular popular combination:', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time=df["Trip Duration"].sum()
    print("The Total Travel Time :" , total_time)


    # display mean travel time
    avg_time=df["Trip Duration"].mean()
    print("The Average Travel Time :" , avg_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The Counts of User Types :\n ",user_types)


    #NOT WASHINGTON 
    if city != 'Washington':
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print("The Counts of User Types :\n ",gender)


        # Display earliest, most recent, and most common year of birth
        #earliest
        earliest =df['Birth Year'].min()
        print("The earliest Birth Year :",earliest)


        #most recent
        recent =df['Birth Year'].max()
        print("The Most Recent Birth Year :",recent)

        #most common
        popular_birth_year = df['Birth Year'].mode()[0] 
        print('Most Popular Start Station:', popular_birth_year)
    else: 
        print("since we dont have data about the 'Gender' and 'Birth Date' in Washington \n we can not dispaly any :( ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)# give back a dic

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        while True :
            raw_data = input('\nwould you like to see the raw data? Enter yes or no.\n')
            if raw_data.lower() == 'yes':   
                print(df.head())
                
                count = 5
                while True :
                    more_data = input('\nwould you like to see 5 more rows of the data? Enter yes or no.\n')
                    if more_data.lower() == 'yes':   
                        print(df.iloc[count : count+5])
                        count+=5
                    elif more_data.lower() == 'no':
                        break
                    else:
                        print("please enter 'yes ' OR 'no'")

                break
            elif raw_data.lower() == 'no':
                break
            else:
                print("please enter 'yes ' OR 'no'")


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'no':
            print("Thank you for using my program :)")
            break
        elif restart.lower() == 'yes':
            print("OK \n ")
        else:
            print("please enter 'yes ' OR 'no'")


        



if __name__ == "__main__":
	main()
