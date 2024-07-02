import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    with open(f'{input_file_name}.csv') as f :
        reader=csv.reader(f)
        with open(f'{output_file_name}.csv','w',newline='') as result :
            writer=csv.writer(result)
            for row in f:
                row=row.strip().split(',')
                new_row=list()
                for item in row[1:] :
                    new_row.append(float(item))
                row_0=list()
                row_0.append(row[0])    
                ave=mean(new_row)
                list_ave=list()
                list_ave.append(ave)
                last_result=row_0+list_ave
                writer.writerow(last_result)                





def calculate_sorted_averages(input_file_name, output_file_name):
    with open(f'{input_file_name}.csv') as f :
        reader=csv.reader(f)
        dict_result=dict()
        with open(f'{output_file_name}.csv','w',newline='') as final :
            writer=csv.writer(final)
            for row in f:
                row=row.strip().split(',')
                new_row=list()
                for item in row[1:] :
                    new_row.append(float(item))
                row_0=list()
                row_0.append(row[0])    
                ave=mean(new_row)
                list_ave=list()
                list_ave.append(ave)
                last_result=row_0+list_ave
                dict_result[row[0]]=ave
                a=list(set(dict_result.values()))
                a.sort()
                b=list()
                c=list()
                d=list()
                y=list()
                z=list()   
            for item in a  :
                for key,value in dict_result.items() :
                    if item==value :
                        b.append(key)    
                        c.append(item)
                if len(b)>1 :
                    b.sort()
                    for p in b :
                        d.append(p)
                        y.append(c[0])
                        writer.writerow(d+y)
                        d.pop()
                        y.pop()
                    c=list()
                    b=list()    
                else :
                    writer.writerow(b+c)
                    b.pop()
                    c.pop()                    


    


def calculate_three_best(input_file_name, output_file_name):
    with open(f'{input_file_name}.csv') as f :
        reader=csv.reader(f)
        dict_result=dict()
        with open(f'{output_file_name}.csv','w',newline='') as final :
            writer=csv.writer(final)
            for row in f:
                row=row.strip().split(',')
                new_row=list()
                for item in row[1:] :
                    new_row.append(float(item))
                row_0=list()
                row_0.append(row[0])    
                ave=mean(new_row)
                list_ave=list()
                list_ave.append(ave)
                last_result=row_0+list_ave
                dict_result[row[0]]=ave
                a=list(set(dict_result.values()))
                a.sort()
                b=list()
                c=list()
                d=list()
                y=list()
                z=list()
            for m in range(0,3) :
                n=a.pop()
                z.append(n)           
            for item in z  :
                for key,value in dict_result.items() :
                    if item==value :
                        b.append(key)    
                        c.append(item)
                if len(b)>1 :
                    b.sort()
                    for p in b :
                        d.append(p)
                        y.append(c[0])
                        writer.writerow(d+y)
                        d.pop()
                        y.pop()
                    c=list()
                    b=list()    
                else :
                    writer.writerow(b+c)
                    b.pop()
                    c.pop()
    


def calculate_three_worst(input_file_name, output_file_name):
    with open(f'{input_file_name}.csv') as f :
        reader=csv.reader(f)
        dict_result=dict()
        with open(f'{output_file_name}.csv','w',newline='') as final :
            writer=csv.writer(final)
            b=list()
            x=list()
            for row in f:
                list_ave=list()
                new_row=list()
                row=row.strip().split(',')
                for item in row[1:] :
                    new_row.append(float(item))    
                ave=mean(new_row)
                list_ave.append(ave)
                b=b+list_ave
            b.sort()        
            for i in range(0,3) :
                x.append(b[i])
                writer.writerow(x)
                x.pop()
    


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(f'{input_file_name}.csv') as f :
        reader=csv.reader(f)
        dict_result=dict()
        with open(f'{output_file_name}.csv','w',newline='') as final :
            writer=csv.writer(final)
            b=list()
            y=list()
            for row in f:
                list_ave=list()
                new_row=list()
                row=row.strip().split(',')
                for item in row[1:] :
                    new_row.append(float(item))    
                ave=mean(new_row)
                list_ave.append(ave)
                b=b+list_ave
            c=mean(b)
            y.append(c)
            writer.writerow(y) 
calculate_averages('input','Task_1')            
calculate_sorted_averages('input','Task_2')
calculate_three_best('input','Task_3')
calculate_three_worst('input','Task_4')
calculate_average_of_averages('input','Task_5')

    