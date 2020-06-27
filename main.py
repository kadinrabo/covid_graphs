import argparse
import current_number_of_deaths
import current_number_of_positive_cases
import current_number_of_negative_cases
import current_number_of_tested_people
import current_number_of_hospitalized_people
import current_number_of_people_in_ICU
import current_number_of_recovered_people
import current_number_of_people_tested_with_positive_negative_cases
import current_number_of_people_hospitalized_in_icu_and_recovered
import current_number_of_tested_people_and_positive_cases
import current_ratio_of_positive_cases_to_tested_people
import current_ratio_of_deaths_to_positive_cases


print("""
=====================================================================================

WELCOME TO MY GRAPHING PROGRAM :D


INSTRUCTIONS: CHOOSE ONE OF MY PREBUILT GRAPHS AND RUN THE COMMAND.


COMMAND FORMAT: python3 main.py EXT
FOR EXAMPLE, TO GRAPH THE CURRENT NUMBER OF DEATHS, ENTER [python3 main.py -aa] INTO THE COMMAND LINE.


*** STATE CHOICE IS SPECIFIED AFTER THE COMMAND IS RUN ***


EXT   --    GRAPH TYPE

-aa    --   CURRENT NUMBER OF DEATHS (current_number_of_deaths.py)

-bb    --   CURRENT NUMBER OF POSITIVE CASES (current_number_of_positive_cases.py)

-cc    --   CURRENT NUMBER OF NEGATIVE CASES (current_number_of_negative_cases.py)

-dd    --   CURRENT NUMBER OF TESTED PEOPLE (current_number_of_tested_people.py)

-ee    --   CURRENT NUMBER OF HOSPITALIZED PEOPLE (current_number_of_hospitalized_people.py)

-ff    --   CURRENT NUMBER OF PEOPLE IN THE ICU (current_number_of_people_in_ICU.py)

-gg    --   CURRENT NUMBER OF RECOVERED PEOPLE (current_number_of_recovered_people.py)

-hh    --   CURRENT NUMBER OF HOSPITALIZED PEOPLE, IN ICU, AND RECOVERED (current_number_of_people_hospitalized_in_icu_
and_recovered.py)

-ii    --   CURRENT NUMBER OF TESTED PEOPLE AND POSITIVE CASES (current_number_of_tested_people_and_positive_cases.py)

-jj    --   CURRENT RATIO OF POSITIVE CASES TO TESTED PEOPLE (current_ratio_of_positive_cases_to_tested_people.py)

-kk    --   CURRENT RATIO OF DEATHS TO POSITIVE CASES (current_ratio_of_deaths_to_positive_cases.py)

-ll    --   GRAPHS TWO STATES' DEATH COUNT AGAINST EACH OTHER (multiple_states_deaths.py)

""")


parser = argparse.ArgumentParser()
parser.add_argument("-aa", action="store_true")
parser.add_argument("-bb", action="store_true")
parser.add_argument("-cc", action="store_true")
parser.add_argument("-dd", action="store_true")
parser.add_argument("-ee", action="store_true")
parser.add_argument("-ff", action="store_true")
parser.add_argument("-gg", action="store_true")
parser.add_argument("-hh", action="store_true")
parser.add_argument("-ii", action="store_true")
parser.add_argument("-jj", action="store_true")
parser.add_argument("-kk", action="store_true")
parser.add_argument("-ll", action="store_true")
args = parser.parse_args()
if not (args.aa or args.bb or args.cc or args.dd or args.ee or args.ff or args.gg or args.hh or args.ii or args.jj or
		args.kk):
	print("\nENTER COMMAND LINE BELOW \n")
elif args.aa:
	current_number_of_deaths.main()
elif args.bb:
	current_number_of_positive_cases.main()
elif args.cc:
	current_number_of_negative_cases.main()
elif args.dd:
	current_number_of_tested_people.main()
elif args.ee:
	current_number_of_hospitalized_people.main()
elif args.ff:
	current_number_of_people_in_ICU.main()
elif args.gg:
	current_number_of_recovered_people.main()
elif args.hh:
	current_number_of_people_hospitalized_in_icu_and_recovered.main()
elif args.ii:
	current_number_of_tested_people_and_positive_cases.main()
elif args.jj:
	current_ratio_of_positive_cases_to_tested_people.main()
elif args.kk:
	current_ratio_of_deaths_to_positive_cases.main()
else:
	print("\n\nMAKE SURE YOU ENTERED A VALID COMMAND. CHECK INSTRUCTIONS.\n\n")
