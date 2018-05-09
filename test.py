ch1 = chromosome(5)
ch2 = chromosome(5)

ch1.gene_list[1],ch1.gene_list[2],ch1.gene_list[3] = list_of_cities[1],list_of_cities[2],list_of_cities[3]
ch2.gene_list[1],ch2.gene_list[2],ch2.gene_list[3] = list_of_cities[4],list_of_cities[5],list_of_cities[6]
print (ch1.gene_list)
print (ch2.gene_list)

def _crossover(_ch1,_ch2,idx):
        ch1, ch2 = copy.copy(_ch1), copy.copy(_ch2)
        #print ("1zmiana {} z {}".format(ch1.gene_list,ch2.gene_list))
        print ("ORYGINAL {} z {}".format(_ch1.gene_list,_ch2.gene_list))
        for i in idx:
            ch1gene = ch1.gene_list[i]
            ch2gene = ch2.gene_list[i]
            ch1.gene_list[i] = ch2gene
            ch2.gene_list[i] = ch1gene
        print ("ORYGINAL {} z {}".format(_ch1.gene_list,_ch2.gene_list))
        print ("2wynik {} z {}".format(ch1.gene_list,ch2.gene_list))


_crossover(ch1,ch2,(1,2))