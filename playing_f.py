
import  random
import json
import  styles_f
import display_results

data_list = [6,3,4,2,1,0,'W','WI','NB']

def playing(team,over,term):
    target = 0
    dis_ov = 0
    over_score_list = []
    data = {}

    if(term != 1):

        with open('player1.json','r') as json_file:
            data = json.load(json_file)
            for p in data['people']:
                target = p['total']+1
            json_file.close()

        outfile = open('player2.json', 'w')

    else :

        outfile =  open('player1.json', 'w')


    count_six = 0
    count_four = 0
    total_score=0
    wicket = 0
    total_over_score = 0
    ball_count = 0


    styles_f.divider()

    if term == 1:
        print("\n##############--- INNINGS 1 STARTED---###############")
    else:
        print("\n##############--- INNINGS 2 STARTED---###############")

    print("\n\t\t\t\tBATING : ",team," ")
    styles_f.divider()

    balls = over*6

    while(balls > 0  and wicket < 10):

        deliv = random.choice(data_list)


        if (deliv == 'W'):
            if(random.choice([6, 7, 8, 9]) == 9 ):
                over_score_list.append(deliv)
                wicket += 1
                balls -= 1
                ball_count+=1


        elif (deliv == 'WI'):
            if (random.choice([6, 7, 8, 9]) == 9):
                over_score_list.append(deliv)
                total_over_score += 1
                total_score+=1

        elif (deliv == 'NB'):
            if (random.choice([6, 7, 8, 9]) == 9):
                over_score_list.append(deliv)
                total_over_score += 1
                total_score += 1

        else:
            if deliv == 6 or deliv == 4:
                if (random.choice([6, 7, 8, 9]) == 9):

                    if(deliv == 6):
                        count_six+=1

                    else:
                        count_four+=1

                    over_score_list.append(deliv)
                    total_over_score += deliv
                    balls -= 1
                    ball_count += 1
                    total_score += deliv
            else:
                over_score_list.append(deliv)
                total_over_score += deliv
                balls -= 1
                ball_count += 1
                total_score += deliv



        if wicket == 10:
            dis_ov += 1
            display_results.disply(dis_ov, over_score_list, total_over_score, count_six, count_four,total_score,wicket)
            over_score_list.clear()
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!--ALLOUT--!!!!!!!!!!!!!!!!!!!!!!\n")
            continue

        elif(ball_count == 6 and wicket != 10):
            if total_score <= target and term != 1:
                dis_ov += 1
                display_results.disply(dis_ov,over_score_list,total_over_score,count_six, count_four,total_score,wicket)
                over_score_list.clear()
                ball_count = 0
                total_over_score=0

            elif term == 1:
                dis_ov += 1
                display_results.disply(dis_ov,over_score_list,total_over_score,count_six, count_four,total_score,wicket)
                over_score_list.clear()
                ball_count = 0
                total_over_score = 0


        elif (term != 1):
            if total_score > target:
                dis_ov += 1
                display_results.disply(dis_ov,over_score_list,total_over_score,count_six, count_four,total_score,wicket)
                over_score_list.clear()
                ball_count = 0
                total_over_score = 0
                break


    data['people'] = ([{
        'name': team,
        'total': total_score,
        'six_c': count_six,
        'four_c': count_four,
        'wicket' : wicket,
        'term' : term
    }])
    json.dump(data, outfile, indent=2)





        
