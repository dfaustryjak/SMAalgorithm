import PlotlyDrawer as own_drawer
import matplotlib.pyplot as plt

success_events=0.0
events=0.0
percent_growth=[]

def get_percent_growth():
    return  percent_growth

def smaalgo(vector_15,vector_45,dates,name,close_price_vector):
    global success_events
    global events
    vector_45_sma = vector_45
    vector_15_sma = vector_15[-len(vector_45_sma):]
    close_price_vector = close_price_vector[-len(vector_45_sma):]
    dates = dates[-len(vector_45_sma):]

    for iterator in range(0,len(dates)):
        to_break_value = iterator + 2
        if(to_break_value>len(vector_45_sma)):
            break
        if (to_break_value > len(vector_15_sma)):
            break
        tmp_1_15_sma = vector_15_sma[iterator]
        tmp_2_15_sma = vector_15_sma[iterator + 1]
        tmp_1_45_sma = vector_45_sma[iterator]
        tmp_2_45_sma = vector_45_sma[iterator + 1]

        if ((tmp_1_15_sma < tmp_1_45_sma) and (tmp_2_15_sma > tmp_2_45_sma)):
            # print(dates[iterator])
            # print("Actual close price is : " + str(float(close_price_vector[iterator][0])))

            # print("COUNT SUCCESS OF ALL EVENTS")
            events+=1
            close_price=0.0
            avg_close_price=0.0
            counter_avg = 0
            for current_date_of_event in range(0,7):
                counter_avg+=1
                if((len(close_price_vector))>iterator+current_date_of_event):
                    close_price+=float(close_price_vector[iterator+current_date_of_event][0])
                    # print(str(current_date_of_event) + ").-  " + str(float(close_price_vector[iterator+current_date_of_event][0])))
                    avg_bottom = iterator+current_date_of_event
                    if (counter_avg > 0):
                        avg_close_price=close_price/counter_avg

            # print("AVG ).-> " + str(avg_close_price))
            percent_result = (avg_close_price * 100)/float(close_price_vector[iterator][0])
            percent_result = percent_result - 100.0
            # print("Percent result ).-> " + str(percent_result))
            percent_growth.append(percent_result)

            if(avg_close_price>float(close_price_vector[iterator][0])):
                # print("==================== OK ====================" )
                # print("ALL EVENTS : " +  str(events))
                success_events += 1
                # print("SUCCES OF TACTIC -> " + str(success_events/events))
                return success_events/events





