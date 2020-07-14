import argparse
import single_2_current_number_of_deaths
import single_2_current_number_of_positive_cases
import single_2_current_number_of_negative_cases
import single_2_current_number_of_tested_people
import single_2_current_number_of_hospitalized_people
import single_2_current_number_of_people_in_icu
import single_2_current_number_of_recovered_people


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-deaths", action="store_true")
	parser.add_argument("-positive", action="store_true")
	parser.add_argument("-negative", action="store_true")
	parser.add_argument("-tested", action="store_true")
	parser.add_argument("-hospitalized", action="store_true")
	parser.add_argument("-icu", action="store_true")
	parser.add_argument("-recovered", action="store_true")
	args = parser.parse_args()

	print("""
-----------------------------------------------------------------------------------------------
>
Here are the statistic options, and their corresponding commands. Run any of them.
Remember, you chose one statistic and two states.
>

1. Current number of DEATHS
-  Command: python3 main_2.py -deaths

2. Current number of POSITIVE CASES
-  Command: python3 main_2.py -positive

3. Current number of NEGATIVE CASES
-  Command: python3 main_2.py -negative

4. Current number of TESTED PEOPLE
-  Command: python3 main_2.py -tested

5. Current number of HOSPITALIZED PEOPLE
-  Command: python3 main_2.py -hospitalized

6. Current number of PEOPLE IN THE ICU
-  Command: python3 main_2.py -icu

7. Current number of RECOVERED PEOPLE
-  Command: python3 main_2.py -recovered

-----------------------------------------------------------------------------------------------
	""")
	if not (args.deaths or args.positive or args.negative or args.tested or args.hospitalized or args.icu or
			args.recovered):
		print("""Enter command below
		""")
	elif args.deaths:
		single_2_current_number_of_deaths.main()
	elif args.positive:
		single_2_current_number_of_positive_cases.main()
	elif args.negative:
		single_2_current_number_of_negative_cases.main()
	elif args.tested:
		single_2_current_number_of_tested_people.main()
	elif args.hospitalized:
		single_2_current_number_of_hospitalized_people.main()
	elif args.recovered:
		single_2_current_number_of_people_in_ICU.main()
	else:
		print("\n\nMake sure you entered the command correctly!\n\n")


if __name__ == "__main__":
	main()
