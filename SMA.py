import mySqlConnector as sql
import smalgo as algorithm_SMA
import matplotlib.pyplot as plt
vector_for_all_results_sma_success = []


def SMA(scope,*values):
    counter = 0
    vector=[]
    sma_vector=[]
    sum=0
    for number in values:
        vector.append(float(values[counter][0]))
        counter+=1

    counter=1
    sum = 0.0
    condition=1
    array_counter=0
    length=vector.__len__()
    index_start = 0
    index_stop = scope
    while(condition):

        tmp=vector[index_start:index_stop]
        array_counter+=1
        for x in tmp:
            sum+=x
            counter+=1
            if(counter>scope):
                SMA=sum/scope
                counter=1
                index_start+=1
                index_stop+=1
                sma_vector.append(SMA)
                SMA=0.0
                sum=0.0
        if(index_stop>length):
            return sma_vector

    return sma_vector


def main_SMA(low_value,high_value):

    all_actions= sql.get_all_actions()
    all_actions = str(all_actions).split('\'')[1::2]
    global vector_for_all_results_sma_success;
    for it in all_actions:
        print("===================>" + it + "<===================")
        if((it == "DROP") or (it=="OPONEO.PL")):
            print("SKIP DROP AND OPONEO.PL")
        else:
            values_for_current_action= sql.search(it,"close")
            values_for_current_action_list = [list(elem) for elem in values_for_current_action]
            all_dates = sql.search(it, "date")
            all_dates = [list(elem) for elem in all_dates]
            vector_SMA_low = 0.0
            vector_SMA_high = 0.0
            vector_SMA_low = SMA(low_value,*values_for_current_action_list)
            vector_SMA_high = SMA(high_value,*values_for_current_action_list)

            if((len(vector_SMA_high) < high_value)):
                print("do nothing")
            else:
                value = algorithm_SMA.smaalgo(vector_SMA_low,vector_SMA_high,all_dates,it,values_for_current_action_list)
                print("<- END - > " + str(value))
                vector_for_all_results_sma_success.append(value);

    #generate succes of sma tactics
    plt.plot(vector_for_all_results_sma_success, linestyle='-', marker='o')
    plt.ylabel('SMA tactics')
    plt.grid(True)
    plt.show()

    #generate plot percent growth
    table = algorithm_SMA.get_percent_growth()
    plt.plot(table, linestyle='-', marker='o')
    plt.ylabel('Percent growth')
    plt.grid(True)
    plt.show()

main_SMA(15, 45)



