import mysql.connector
import auth_data


auth_data= auth_data.auth_data()
def search(action_name,data):

    cnx = mysql.connector.connect(user=str(auth_data[0]), password=str(auth_data[1]),
                                  host=str(auth_data[2]),
                                  database='market')
    cursor = cnx.cursor()

    query = ("SELECT "+ data +" FROM "+ action_name)
    cursor.execute(query)

    values_to_return = []
    for current_cursor in cursor:
        values_to_return.append(current_cursor)

    cursor.close()
    cnx.close()
    return values_to_return


def get_all_actions():
    cnx = mysql.connector.connect(user=str(auth_data[0]), password=str(auth_data[1]),
                                  host=str(auth_data[2]),
                                  database='market')
    cursor = cnx.cursor()
    query = ("SHOW TABLES;")
    cursor.execute(query)

    values_to_return = []
    for current_cursor in cursor:
        values_to_return.append(current_cursor)

    cursor.close()
    cnx.close()
    return values_to_return


