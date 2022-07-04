import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    months = ['january','febuary','march','april','may','june']
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    cities = ['chicago','new york','washington']
    while True:
        city = input('\nWhich city would you like to analyze?:chicago, new york, washington\n').lower()
        if city not in cities:
            print("\nPlease enter: Chicago, New York or Washington!")
            continue
        else:
            break
            
                 
    while True:
        month = input('\nPlease select a month to filter by or enter none for no filter\n')
        if month not in months:
                print("\nPlease enter a valid month\n")
                continue
        else:
            break

                
    while True:
        day = input('\nPlease select a day to filter by or enter all for all options\n')
        if day not in days:
                print("\nPlease enter a valid day\n") 
                continue
        else:
            break
    
        
    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    return(df)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['Start hour'] = df['Start Time'].dt.hour
    
    pop_month = df['month'].mode()[0]
    print('Most common month:', pop_month)


    pop_day = df['day_of_week'].mode()[0]
    print('Most common day:', pop_day)
    
       
    pop_hour = df['Start hour'].mode()[0]
    print('Most common start time:'.format, (pop_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start_station = df.loc[:,"Start Station"].mode()[0]
    print('\nThe most common start station:', pop_start_station)

    # display most commonly used end station
    pop_end_station = df.loc[:,"End Station"].mode()[0]
    print('\nThe most common end station:', pop_end_station)

    # display most frequent combination of start station and end station trip
    pop_combo_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('\nThe most common combination station of start and end trip:', pop_combo_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df["Trip Duration"] = df["End Time"] - df["Start Time"]
    
    # display total travel time
    total_duration = df['Trip Duration'].sum()
    print('total travel time for your trip:', total_duration)
   
    # display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('Average travel time for your trip:', mean_duration)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The user types are:\n", user_types)

    #referencing a knowledge question helped me with the below: https://knowledge.udacity.com/questions/55524
    # Display counts of gender
    if 'gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print("The types of user by 'Gender' are:\n", user_gender)
    else:
        print('Please reenter your input')

    # 
def birth_year(df):
    """Display earliest, most recent, and most common year of birth."""
          
    earliest_year = df['birth_year'.min()]
    latest_year = df['birth_year'.max()]
    common_year = df['birth_year'.mode()]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(df)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print(df)
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

            
if __name__ == "__main__":
	main()
