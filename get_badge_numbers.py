from datetime import datetime

def get_badge_numbers(file_name,with_fired_status):

    try:
        # get officers file
        officers_file = open(file_name, mode="r", encoding="utf-8")

        # load to list
        badges_numbers_list = []
        off_list = officers_file.read().splitlines()

        # get badges numbers
        for officer in off_list:
            line = officer.split('|')

            # add true/false value whether officer is still employed
            if with_fired_status:
                officer = [line[0]]

                if line[8] == "":
                    officer.append(True)
                    officer.append(None)
                else:
                    # get fired date
                    fired_date = datetime.strptime(line[8],'%Y-%m-%d').date()
                    officer.append(False)
                    officer.append(fired_date)
                badges_numbers_list.append(officer)
            else:
                badges_numbers_list.append(line[0])

        officers_file.close()
        return badges_numbers_list

    except FileNotFoundError:
        print("Couldn't find a file")

#get_badge_numbers("police_officers_t1",True)
