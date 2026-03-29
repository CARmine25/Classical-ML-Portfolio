import csv
with open("dataset.csv","r",newline='') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    fieldnames=csv_reader.fieldnames

    rows=[]
    for line in csv_reader:
        rows.append(line)
    
    #    for column in fieldnames:
#        print(column)

data = {}

for column in fieldnames:
    data[column] = []

for row in rows:
    for column in fieldnames:
        data[column].append(row[column])
    
del data["ocean_proximity"]

#print(list(data.keys()))
#print(len(data["longitude"]))
#print(data["longitude"][:5])


def missing_value(column_name):
    
    non_missing_values=[]
    values=[]
    count_empty=0
    count_number=0
    for value in rows:
        x=value[column_name]
        values.append(x)

    for input in values:
        if input=='':
            count_empty+=1
            pass
        else:
            non_missing_values.append(float(input))
            count_number+=1
    total=sum(non_missing_values)
    mean=total/count_number

    for i in range(len(data[column_name])):
       
        if data[column_name][i]=='':
            data[column_name][i]=mean

    print(data["total_bedrooms"].count('')) 

    for column in data:
        data[column] = [float(x) for x in data[column]]   
    print(data["total_bedrooms"][:5])
#    return{
#        "non_missing_values": values,
#        "count of missing_values" : count_empty,
#        "count of non_empty" : count_number
#    }


result=missing_value("total_bedrooms")
print(result)



