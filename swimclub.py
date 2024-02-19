import statistics

FOLDER = "../Data/swimdata/"


def read_swim_data(filename):

    #Getting the key attributes from file name
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")

    #Going through the first file and extracting times
    with open(FOLDER+filename) as file:
        lines = file.readlines()
        times = lines[0].rstrip().split(",")
        converts = []
        for t in times:
            if t.__contains__(":"):
                mins, rest = t.split(":")
            else:
                mins = 0
                rest = t
            sec,hundredths = rest.split(".")
            total_millisec = int(mins)*60*100 + int(sec)*100 + int(hundredths)
            converts.append(total_millisec)
        
    #Finding average
    average = statistics.mean(converts)

    #Converting average back to the format needed
    #mins_secs, hundredths = str(round(average/100,2)).split(".")
    mins_secs, hundredths = f"{(average/100):.2f}".split(".")
    mins_secs = int(mins_secs)
    mins = mins_secs//60
    seconds = mins_secs-mins*60
    average = f"{mins}:{seconds:0>2}.{hundredths}"

    return swimmer, age, distance, stroke, times, average, converts
