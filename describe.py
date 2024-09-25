import sys

def calculate_percentile(data, percentile):
    sorted_data = sorted(data)

    index = int(percentile * len(sorted_data) / 100.0)

    return sorted_data[index]

def prnt_percentile (data):
    i = 0
    retq1 ="25%     "
    retq2 ="50%     "
    retq3 ="75%     "
    while i < len(features) :
        retq1 += prnt_value(calculate_percentile(data[i], 25), features[i]) + ' '
        retq2 += prnt_value(calculate_percentile(data[i], 50), features[i]) + ' '
        retq3 += prnt_value(calculate_percentile(data[i], 75), features[i]) + ' '
        i += 1
    print (retq1 + '\n' + retq2 + '\n' + retq3)

def prnt_feats(features):
    ret = ""
    for feature in features :
        ret += feature  + "  "
    print("        " + ret)

def prnt_value(val, feature):
    l1 = len(feature)
    l2 = len(str(val))
    ret = ""
    while l2 < l1:
        l2 += 1
        ret += " "
    ret += str(val)
    return ret

def prnt_count(count, features):
    ret = 'count   '
    for feature in features:
        ret += prnt_value(count, feature) + '  '
    print(ret)

def prnt_mean(total, count):
    mean = []
    ret = 'mean    '
    for val in total :
        mean.append(float(val) / float(count))
    i = 0
    while i < len(mean):
        ret += prnt_value(mean[i], features[i]) + '  '
        i += 1
    print(ret)
    return mean
    
def prnt_std(data,mean):
    i = 0
    std = []
    ret = 'std     '
    while i < len(mean):
        sum_squared_diff = sum((float(x) - float(mean[i])) ** 2 for x in data[i])
        variance = sum_squared_diff / (len(data[i]) - 1)
        std.append(variance ** 0.5)
        ret += prnt_value(std[i], features[i]) + ' '
        i += 1
    print(ret)
    return std

def prnt_min(data):
    i = 0
    min = []
    ret = 'min     '
    while i < len(features):
        mintmp = 0
        for elem in data[i] :
            if mintmp == 0 or float(elem) < mintmp :
                mintmp = float(elem)
        min.append(mintmp)
        ret += prnt_value(mintmp, features[i]) + ' '
        i += 1
    print(ret)
    return min

def prnt_max(data):
    i = 0
    max = []
    ret = 'max     '
    while i < len(features):
        maxtmp = 0
        for elem in data[i] :
            if maxtmp == 0 or float(elem) > maxtmp :
                maxtmp = float(elem)
        max.append(maxtmp)
        ret += prnt_value(maxtmp, features[i]) + ' '
        i += 1
    print(ret)
    return max

def prnt_irq(data): # interquartile range
    i = 0
    irq = []
    ret = 'iqr     '
    while i < len(features):
        q1 = float(calculate_percentile(data[i], 25))
        q3 = float(calculate_percentile(data[i], 75))
        iqr_value = q3 - q1
        irq.append(iqr_value)
        ret += prnt_value(iqr_value, features[i]) + ' '
        i += 1
    print(ret)
    return irq


def get_values(data,count):
    total = []
    for line in data:
        i = 0
        while i < len(line):
            if i < len(total):
                total[i] += float(line[i])
            else :
                total.append(float(line[i]))
            i += 1
    mean = prnt_mean(total, count)
    prnt_std(data, mean)
    prnt_min(data)
    prnt_percentile(data)
    prnt_max(data)
    prnt_irq(data)

        
if __name__ == "__main__":
    filePath = sys.argv[1]
    data = []
    with open(filePath, 'r') as file:
        lines = file.readlines()
        features = lines[0].split(',')[6:] # remove les elements non numeriques
        features[12] = features[12][:-1] #remove le \n
        lines.pop(0)
        for line in lines :
            newLine = []
            values = line.split(',')[6:]
            values[12] = values[12][:-1]
            for val in values:
                if len(val) > 0 :
                    newLine.append(val)
            data.append(newLine)
        count = len(data)
        prnt_feats(features)
        prnt_count(count, features)
        get_values(data, count)