import hfpy_utils
import swimclub

def gethtmloutput(file_name, swimmer, age, distance, stroke, times, average, converts):
    title = f"{swimmer} (under {age}) {distance} {stroke}"
    html = ""
    html += f"<!DOCTYPE html>"
    html += f"<html>"
    html += f"<head>"
    html += f"<title>{title}</title>"
    html += f"</head>"
    html += f"<body><h3>{title}</h3>"

    ##create bars for each swimmer
    converts.reverse()
    times.reverse()

    svgs = ""
    max_swim_swimmer = max(converts)
    for count, convert in enumerate(converts):
        bar_width = hfpy_utils.convert2range(convert,0,max_swim_swimmer,0,350)
        svgs += f"<svg height='30' width='400'>"
        svgs += f"<rect height='30' width='{bar_width}' style='fill:rgb(0,0,255);' />"
        svgs += f"</svg>{count} -> {times[count]}<br />"
    footer = f"<p>Average Time {average}</p>"    
    html += svgs + footer + f"</body>"
    html += f"</html>"
    return html

def getswimmerdetails(swimmer_name, swimmer_files):
    swimmer_details_list = []
    for file in swimmer_files:
        swimmer_details = swimclub.read_swim_data(file)
        swimmer_details_list.append(swimmer_details)
    return swimmer_details_list


def gethtmloutputforswimmer(swimmer_name, swimmer_details_list):
    #swimmer, age, distance, stroke, times, average, converts
    html = ""
    html += f"<!DOCTYPE html>"
    html += f"<html>"

    for detail in swimmer_details_list:
        swimmer, age, distance, stroke, times, average, converts = detail
        title = f"{swimmer} (under {age}) {distance} {stroke}"
        html += f"<head>"
        html += f"<title>{title}</title>"
        html += f"</head>"
        html += f"<body><h3>{title}</h3>"

        ##create bars for each swimmer
        converts.reverse()
        times.reverse()

        svgs = ""
        max_swim_swimmer = max(converts)
        for count, convert in enumerate(converts):
            bar_width = hfpy_utils.convert2range(convert,0,max_swim_swimmer,0,350)
            svgs += f"<svg height='30' width='400'>"
            svgs += f"<rect height='30' width='{bar_width}' style='fill:rgb(0,0,255);' />"
            svgs += f"</svg>{count} -> {times[count]}<br />"
        footer = f"<p>Average Time {average}</p>"    
        html += svgs + footer + f"</body>"
    
    html += f"</html>"
    return html