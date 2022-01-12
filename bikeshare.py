import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ' '
    cities = ['new york city', 'washington', 'chicago']

    while True:
        try:
            print("\nAccepted input: City name not case sensitive (for example, washington or WASHINGTON). City name in title case (e.g.                 Washington).")
            city = input("would you like to see data for Chicago, New York or Washington? ").lower()
            if city in cities:
                break
            else:
                print("Sorry, there must have been an error, please enter a valid city")
        except Exception as e:
            ("Sorry, you entered an invalid input")



    # TO DO: get user input for month (all, january, february, ... , june)


    # Create dictionary to store elements in months
    months_dict = { 'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7 }
    month = ' '

    while True:
        try:
            print("\Accepted input: Month name not case sensitive (for example, March or MARCH). Month name in title case (e.g. March).")
            print("\n(If you choose to view data for all months, type 'all', or 'All', or 'ALL')")
            month = input("which month would you like to see data on in january, february, march, april, may, june?").lower()
            if month in months_dict:
                break
            else:
                print("Sorry, there must have been an error, please enter a valid month")
        except Exception as e:
            ("Sorry, you entered an invalid input")


    # get user input for day of week (sunday, monday, tuesday, ... , all)

    # Create dictionary to store elements in days
    days_dict = { 'sunday': 1, 'monday': 2, 'tuesday': 3, 'wednesday': 4, 'thursday': 5, 'friday': 6, 'saturday': 7, 'all': 8 }
    day = ' '

    while True:
        day = input("which particular day of the week would you like to explore? If you do not want data on a particular day, enter             'all'").lower()
        if day in days_dict:
            break
        else:
            print("Sorry, you entered an invalid input")


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

    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # filter by month to create the new dataframe
        df=df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]





    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('The Most Popular Month is {}.'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]

    print('The Most Popular Day of Week is {}.'.format(popular_day_of_week))

    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]

    print('The Most Popular Start Hour is {}.'.format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    frequently_used_start_station = df['Start Station'].mode()[0]

    print('The Most Common Start Station is {}.'.format(frequently_used_start_station))

    # TO DO: display most commonly used end station
    frequently_used_end_station = df['End Station'].mode()[0]

    print('The Most Common End Station is {}.'.format(frequently_used_end_station))



    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    frequent_station_combination = df['Start To End'].mode()[0]

    print('The Most Frequent Combination of both Start and End Station Trip is {}.'.format(frequent_station_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # Converting the trip duration to minutes and seconds format
    minute, second = divmod(total_travel_time, 60)

    # Converting the trip duration to hours and minutes format
    hour, minute = divmod(minute, 60)

    print('The Total Travel Time is {} hours, {} minutes and {} seconds.'.format(hour, minute, second))

    # TO DO: display mean travel time
    average_travel_time = round(df['Trip Duration'].mean())

    # Converting the average travel time to minutes and seconds format
    minute, second = divmod(average_travel_time, 60)

    # Converting the average travel time to hours and minutes format
    hour, minute = divmod(minute, 60)

    print('The Average Travel Time is {} hours, {} minutes and {} seconds.'.format(hour, minute, second))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('The Value Counts For Each User Type is {}.'.format(user_types))


    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('The Gender Counts for each User Type is {}.'.format(gender_counts))

    except Exception as e:
        print('There is no data available for Gender Counts')



    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        print('The Earliest Birth Year is {}.'.format(earliest_year))
        most_recent_year = int(df['Birth Year'].max())
        print('The Most Recent Year of Birth is {}.'.format(most_recent_year))
        most_common_year = int(df['Birth Year'].mode()[0])
        print('The Most Common Year of Birth is {}.'.format(most_common_year))

    except Exception as e:
        print('There is no data available for Birth Year')




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays 5 rows of individual trip data."""

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0

    while True:
        print(df.iloc[0:5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == "yes":
             print(df[start_loc:start_loc + 5])
        elif view_display != "yes":
             break


    print('-'*80)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'yes':
            main()
        elif restart.lower() == 'no':
            return
    else:
        print("Sorry, you entered an invalid input. Please type 'yes' or 'no' ")

    return restart()

if __name__ == "__main__":
	main()
