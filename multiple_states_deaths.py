import requests
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys


def main():
	print("""
		ALABAMA - AL
		ALASKA - AK
		ARIZONA - AZ
		ARKANSAS - AR
		CALIFORNIA - CA
		COLORADO - CO
		CONNECTICUT - CT
		DELAWARE - DE
		FLORIDA - FL
		GEORGIA - GA
		HAWAII - HI
		IDAHO - ID
		ILLINOIS - IL
		INDIANA - INIOWA - IA
		KANSAS - KS
		KENTUCKY - KY
		LOUISIANA - LA
		MAINE - ME
		MARYLAND - MD
		MASSACHUSETTS - MA
		MICHIGAN - MI
		MINNESOTA - MN
		MISSISSIPPI - MS
		MISSOURI - MO
		MONTANA - MT
		NEBRASKA - NE
		NEVADA - NV
		NEW HAMPSHIRE - NH
		NEW JERSEY - NJ
		NEW MEXICO - NM
		NEW YORK - NY
		NORTH CAROLINA - NC
		NORTH DAKOTA - ND
		OHIO - OH
		OKLAHOMA - OK
		OREGON - OR
		PENNSYLVANIA - PA
		RHODE ISLAND - RI
		SOUTH CAROLINA - SC
		SOUTH DAKOTA - SD
		TENNESSEE - TN
		TEXAS - TX
		UTAH - UT
		VERMONT - VT
		VIRGINIA - VA
		WASHINGTON - WA
		WEST VIRGINIA - WV
		WISCONSIN - WI
		WYOMING - WY
		""")

	first_state_choice = input("\nCHOOSE A STATE BY ENTERING STATE ABBREVIATION: ")
	second_state_choice = input("\nCHOOSE ANOTHER STATE BY ENTERING STATE ABBREVIATION: ")
	if first_state_choice == second_state_choice:
		print("Please choose different states. Terminating...")
		sys.exit(1)

	first_url = f'https://covidtracking.com/api/v1/states/{first_state_choice.lower()}/daily.json'
	second_url = f'https://covidtracking.com/api/v1/states/{second_state_choice.lower()}/daily.json'
	f_r = requests.get(first_url)
	s_r = requests.get(second_url)
	if f_r.status_code == 200 and s_r.status_code == 200:
		print("\n---- SUCCESS! ---- \n")
		first_data = f_r.json()
		second_data = s_r.json()
	else:
		print("\n---- ERROR :( ---- \n")
		sys.exit(1)

	dates, first_deaths, second_deaths = [], [], []

	for i in first_data:
		list_date = [i for i in str(i['date'])]
		month = list_date[5]
		month_formatted = ''.join(month)
		day = list_date[6:8]
		day_formatted = ''.join(day)
		date = f"{month_formatted}/{day_formatted}"
		dates.append(date)
		first_deaths.append(i['death'])
	for i in second_data:
		second_deaths.append(i['death'])

	try:
		first_deaths.reverse()
		second_deaths.reverse()
		dates.reverse()
	except TypeError:
		print("Some data points null.")

	dates_list = []
	for k, v in enumerate(dates):
		if k % 10 == 0:
			dates_list.append(v)
		else:
			dates_list.append("")

	plt.style.use('classic')
	fig, ax = plt.subplots()
	ax.plot(dates, first_deaths, c='red', linewidth=5)
	ax.plot(dates, second_deaths, c='blue', linewidth=5)
	ax.set_xticks(dates_list)
	fig.autofmt_xdate()
	plt.grid()
	plt.title(f'Number of COVID-19 related deaths in {first_state_choice.upper()} and {second_state_choice.upper()} '
			  f'since March 2020\n', fontsize=15)
	blue_patch = mpatches.Patch(color='red', label=first_state_choice.upper())
	red_patch = mpatches.Patch(color='blue', label=second_state_choice.upper())
	plt.legend(handles=[blue_patch, red_patch])
	plt.xlabel('Date', fontsize=15)
	plt.ylabel('Deaths', fontsize=15)
	plt.tick_params(axis='both', which='major', labelsize='10')
	plt.show()

	again = input("WOULD YOU LIKE TO CHECK ANOTHER STATE?(y/n) ")
	if again == 'y':
		main()
	elif again == 'n':
		print("\nGOODBYE!\n")
		sys.exit()
	else:
		print("\nGOODBYE!\n")
		sys.exit()


if __name__ == "__main__":
	main()
