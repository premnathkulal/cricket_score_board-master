import styles_f
import json

def disply(dis_ov,over_score_list,total_over_score,count_six, count_four,total_score,wicket):
    styles_f.loading()
    print("\nOVER :", dis_ov)
    print("\n\t\t", over_score_list,"\n")
    print(total_score,"/",wicket,"\t\t\t\t\t\tSIX :",count_six,"\tFOUR :",count_four,"\n")
    styles_f.divider()


def half_match_result():

    with open('player1.json', 'r') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            total_sc = p['total']
            name = p['name']
            six = p['six_c']
            wicket1 = p['wicket']
            four = p['four_c']
        json_file.close()

    styles_f.loading()
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$\t\t\t\t\t\t\t\t\t\t\t\t\t$")
    print("$\t\t\t\tRESULT OF FIRST INNINGS\t\t\t\t$")
    print("$\t\t\t\t\t\t\t\t\t\t\t\t\t$")
    print("$\t\t\t\tTEAM NAME :", name, "\t\t\t\t\t$")
    print("$\t\t\t\tTOTAL SCORE :", total_sc,"/",wicket1,"\t\t\t\t$")
    print("$\t\t\t\tSIX :",six,"\t\t\t\t\t\t\t$")
    print("$\t\t\t\tFOUR :",four, "\t\t\t\t\t\t\t$")
    print("$\t\t\t\t\t\t\t\t\t\t\t\t\t$")
    print("$\t\t\t\tTARGET : ",total_sc+1,"\t\t\t\t\t\t$")
    print("$\t\t\t\t\t\t\t\t\t\t\t\t\t$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


def match_result():
    with open('player1.json', 'r') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            total_sc = p['total']
            name = p['name']
            six = p['six_c']
            wicket1 = p['wicket']
            termf = p['term']
            four = p['four_c']
        json_file.close()

    with open('player2.json', 'r') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            total_sc2 = p['total']
            name2 = p['name']
            six2 = p['six_c']
            wicket2 = p['wicket']
            terms = p['term']
            four2 = p['four_c']
        json_file.close()

    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t$")
    print("$\t\t\t\t\t\t\t\t\t\t\t\tSCORE LIST\t\t\t\t\t\t\t\t\t\t\t\t$")
    print("$\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$\t\t\t\t\t\t\t\t\t\t\t\t\t$\t\t\t\t\t\t\t\t\t\t\t\t\t$")
    print("$\t\t\t\tRESULT OF FIRST INNINGS\t\t\t\t$\t\t\t\tRESULT OF SECOND INNINGS\t\t\t$")

    print("$\t\t\t\t\t\t\t\t\t\t\t\t\t$\t\t\t\t\t\t\t\t\t\t\t\t\t$")
    print("$\t\t\t\tTEAM NAME :", name, "\t\t\t\t\t$\t\t\t\tTEAM NAME :", name2, "\t\t\t\t\t$")
    print("$\t\t\t\tTOTAL SCORE :", total_sc,"/",wicket1,"\t\t\t\t$\t\t\t\tTOTAL SCORE :", total_sc2,"/",wicket2,"\t\t\t\t$")
    print("$\t\t\t\tSIX :", six, "\t\t\t\t\t\t\t$\t\t\t\tSIX :", six2, "\t\t\t\t\t\t\t$")
    print("$\t\t\t\tFOUR :", four, "\t\t\t\t\t\t\t$\t\t\t\tFOUR :", four2, "\t\t\t\t\t\t\t$")
    print("$\t\t\t\t\t\t\t\t\t\t\t\t\t$\t\t\t\t\t\t\t\t\t\t\t\t\t$")
    print("$\t\t\t\t\t\t\t\t\t\t\t\t\t$\t\t\t\t\t\t\t\t\t\t\t\t\t$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t$")

    if(total_sc > total_sc2):
        if termf == 1:
            print("$\t\t\t\t\t\t\t\t\t\t",name,"WIN BY",total_sc-total_sc2,"RUNS\t\t\t\t\t\t\t\t\t\t\t\t$")
        else:
            print("$\t\t\t\t\t\t\t\t\t\t",name,"WIN BY",10-wicket1,"WICKETS\t\t\t\t\t\t\t\t\t\t\t$")

    elif (total_sc2 > total_sc):
        if terms == 1:
            ("$\t\t\t\t\t\t\t\t\t\t",name2,"WIN BY",total_sc2-total_sc,"RUNS\t\t\t\t\t\t\t\t\t\t\t\t$")
        else:
            print("$\t\t\t\t\t\t\t\t\t\t",name2,"WIN BY",10-wicket2,"WICKETS\t\t\t\t\t\t\t\t\t\t\t$")

    else:
        print("$\t\t\t\t\t\t\t\t\t\t\t\tMATCH DRAW\t\t\t\t\t\t\t\t\t\t\t\t$")


    print("$\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")