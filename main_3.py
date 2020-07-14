import argparse
import single_3_current_number_of_deaths
import single_3_current_number_of_positive_cases
import single_3_current_number_of_negative_cases
import single_3_current_number_of_tested_people
import single_3_current_number_of_hospitalized_people
import single_3_current_number_of_people_in_icu
import single_3_current_number_of_recovered_people


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
Remember, you chose one statistic and three states.
>

1. Current number of DEATHS
-  Command: python3 main_3.py -deaths

2. Current number of POSITIVE CASES
-  Command: python3 main_3.py -positive

3. Current number of NEGATIVE CASES
-  Command: python3 main_3.py -negative

4. Current number of TESTED PEOPLE
-  Command: python3 main_3.py -tested

5. Current number of HOSPITALIZED PEOPLE
-  Command: python3 main_3.py -hospitalized

6. Current number of PEOPLE IN THE ICU
-  Command: python3 main_3.py -icu

7. Current number of RECOVERED PEOPLE
-  Command: python3 main_3.py -recovered

-----------------------------------------------------------------------------------------------
	""")
	if not (args.deaths or args.positive or args.negative or args.tested or args.hospitalized or args.icu or
			args.recovered):
		print("""Enter command below
		""")
	elif args.deaths:
		single_3_current_number_of_deaths.main()
	elif args.positive:
		single_3_current_number_of_positive_cases.main()
	elif args.negative:
		single_3_current_number_of_negative_cases.main()
	elif args.tested:
		single_3_current_number_of_tested_people.main()
	elif args.hospitalized:
		single_3_current_number_of_hospitalized_people.main()
	elif args.icu:
		single_3_current_number_of_people_in_icu.main()
	elif args.recovered:
		single_3_current_number_of_recovered_people.main()
	else:
		print("\n\nMake sure you entered the command correctly!\n\n")


if __name__ == "__main__":
	main()
