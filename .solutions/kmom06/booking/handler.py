#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Handler module - holds all the functions
"""
# from month import Month
from calendar import Calendar
from team import Team
# from sport import Sport
from match import Match

class Handler():
    """
    Handler Class
    """

    def __init__(self):
        self.calendar = Calendar()
        self.all_teams = []
        self.all_matches = []

    def list_calendar(self):
        """
        List all days in chosen month
        """
        while True:
            print("\n#### Calendar ####\n")
            print(self.calendar)

            try:
                choice = int(input("Choose month (0 to exit): "))
                break
            except ValueError:
                print("That's not an integer!")
                input("\nPress enter to choose again.")

        if choice == 0:
            print("\nExits back to main menu")
        else:
            month_holder = self.calendar.get_month(choice)
            print("\n#### " + month_holder.name + " ####\n")
            for day in month_holder.days_in_month:
                print(day)

    def book_day(self, the_match):
        """
        Book a day in the month
        """
        while True:
            try:
                mon = int(input("Enter month (1-12): "))
                day = int(input("Enter day (1-30/31): "))
                break
            except ValueError:
                print("\nNot an integer.")
                input("\nPress enter to choose again.")
        if not self.calendar.get_month(mon).get_day(day).booked:
            self.calendar.get_month(mon).get_day(day).book(the_match)
            print("\nMatch booked " + str(day) + "/" + str(mon) + "\n" + str(the_match))
        else:
            print("\nDate occupied. Choose another.")


    def create_team(self):
        """
        Create new team
        """
        self.list_teams()
        while True:
            try:
                t_name = input("\nTeam name: ")
                break
            except ValueError:
                print("\nThat was not an alternative. Try again.")

        self.all_teams.append(Team(t_name))


        print("\nTeam", t_name, "created.")


    def list_teams(self):
        """
        List all teams
        """
        counter = 1
        print("\n#### Teams ####\n")
        for team in self.all_teams:
            print(str(counter) + ": " + str(team))
            counter += 1

    def create_match(self):
        """
        Creates a match on a special date
        """

        new_sport = input("Type of sport? ")

        self.list_teams()

        while True:
            try:
                team1 = int(input("Choose first team: "))
                team2 = int(input("Choose second team: "))
                break
            except ValueError:
                print("Not an int. Try again.")

        new_match = Match(new_sport, (self.all_teams[team1-1], self.all_teams[team2-1]))

        self.book_day(new_match)

    def list_matches(self):
        """
        Lists all booked matches
        """
        counter = 1
        print_this = "\n#### All booked matches ####\n"

        for month in self.calendar.months:
            for day in month.days_in_month:
                if day.is_booked():
                    print_this += "\n" + str(counter) + ". " +\
month.name + " " + str(day.number) + "\n" +\
str(day.match) + "\n"
                    counter += 1

        print(print_this)
