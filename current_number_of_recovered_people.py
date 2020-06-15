import requests
import matplotlib.pyplot as plt
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

	state_choice = input("\nCHOOSE A STATE BY ENTERING STATE ABBREVIATION: ")

	url = f'https://covidtracking.com/api/v1/states/{state_choice.lower()}/daily.json'
	r = requests.get(url)
	if r.status_code == 200:
		print("\nGRAPHING...\n")
		print("\n---- SUCCESS! ---- \n")
		data = r.json()
	else:
		print("\n---- ERROR :( ---- \n")
		sys.exit(1)

	dates, recovered = [], []

	for i in data:
		list_date = [i for i in str(i['date'])]
		month = list_date[5]
		month_formatted = ''.join(month)
		day = list_date[6:8]
		day_formatted = ''.join(day)
		date = f"{month_formatted}/{day_formatted}"
		dates.append(date)
		recovered.append(i['recovered'])

	try:
		recovered.reverse()
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
	ax.plot(dates, recovered, c='red', linewidth=5)
	ax.set_xticks(dates_list)
	fig.autofmt_xdate()
	plt.grid()
	plt.title(f'Number of people recovered from COVID-19 in {state_choice.upper()} since March 2020\n', fontsize=15)
	plt.xlabel('Date', fontsize=15)
	plt.ylabel('Number of people recovered', fontsize=15)
	plt.tick_params(axis='both', which='major', labelsize='10')
	plt.show()


if __name__ == "__main__":
	main()
