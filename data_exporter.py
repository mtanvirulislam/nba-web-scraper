from os.path import abspath

from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType


def main():
    print("\n#######################################################################")
    print("#######################################################################")
    print("######################### NBA Report exporter #########################")
    print("#######################################################################")
    print("#######################################################################\n")

    while (True):

        print(
            "1. Players box scores by a date\
           \n2. Players season statistics for a season\
           \n3. Players advanced season statistics for a season\
           \n4. All Team box scores by a date\
           \n5. Schedule for a season\
           \n6. Exit"
        )
        reportObject = input("\nPlease select a option: ")

        # Players box scores by a date
        if (reportObject == "1"):
            inputDate = input("\nEnter a date (use this format 1-1-2018): ")
            fileName = "all-player-box-report-" + inputDate + ".csv"
            dateList = inputDate.split("-")
            print("Exporting report please wait..........")
            # Call Export function
            client.player_box_scores(
                day=dateList[0],
                month=dateList[1],
                year=dateList[2],
                output_type=OutputType.CSV,
                output_file_path="exported_files/" + fileName
            )
            print("Report exported at: " + abspath("exported_files/" + fileName) + "!!\n\n")

        # Players season statistics for a season
        elif (reportObject == "2"):
            endYear = input("\nEnter season end year: ")
            fileName = "all-player-season-report-" + endYear + ".csv"
            print("Exporting report please wait..........")
            # Call Export function
            client.players_season_totals(
                season_end_year=endYear,
                output_type=OutputType.CSV,
                output_file_path="exported_files/" + fileName
            )
            print("Report exported at: " + abspath("exported_files/" + fileName) + "!!\n\n")


        # Players advanced season statistics for a season
        elif (reportObject == "3"):
            endYear = input("\nEnter season end year: ")
            fileName = "all-player-advanced-season-report-" + endYear + ".csv"
            print("Exporting report please wait..........")
            # Call Export function
            client.players_advanced_season_totals(
                season_end_year=endYear,
                output_type=OutputType.CSV,
                output_file_path="exported_files/" + fileName
            )
            print("Report exported at: " + abspath("exported_files/" + fileName) + "!!\n\n")

        # All Team box scores by a date
        elif (reportObject == "4"):
            inputDate = input("\nEnter a date (use this format 1-1-2018): ")
            fileName = "all-team-report-" + inputDate + ".csv"
            dateList = inputDate.split("-")
            print("Exporting report please wait..........")
            # Call Export function
            client.team_box_scores(
                day=dateList[0],
                month=dateList[1],
                year=dateList[2],
                output_type=OutputType.CSV,
                output_file_path="exported_files/" + fileName
            )
            print("Report exported at: " + abspath("exported_files/" + fileName) + "!!\n\n")

        # Schedule for a season
        elif (reportObject == "5"):
            endYear = input("\nEnter season end year: ")
            fileName = "season-schedule-" + endYear + ".csv"
            print("Exporting report please wait..........")
            # Call Export function
            client.season_schedule(
                season_end_year=endYear,
                output_type=OutputType.CSV,
                output_file_path="exported_files/" + fileName
            )
            print("Report exported at: " + abspath("exported_files/" + fileName) + "!!\n\n")

        # Exit
        elif (reportObject == "6"):
            print("\n#######################################################################")
            print("################################# Bye #################################")
            print("#######################################################################\n")
            break

        # Error
        else:
            print("Invalid option!!\n\n")


################# Main #################

if __name__ == '__main__':
    main()
