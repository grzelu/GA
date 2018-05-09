 '''   def selection(self,elitism = False):
        new_generation = []
        print(len(self.population_list))
       
        for i in range(0,len(self.population_list)-1 if elitism  else len(self.population_list) ):
            rint = random.randint(0,len(self.population_list)-1)
            rint2 = random.randint(0,len(self.population_list)-1)
            #print (rint,rint2)
            first_parent_idx = rint
            second_parent_idx = rint2
            if self.population_list[first_parent_idx].fitness > self.population_list[second_parent_idx].fitness:
                winner = self.population_list[first_parent_idx]
            else:
                winner = self.population_list[second_parent_idx]
            new_generation.append(winner)
        #if len(new_generation)<len(self.population_list):
        #    new_generation.append(self.population_list[np.argmax('fitness')])
        new_generation.append(self.population_list[np.argmax('fitness')])
        self.new_generation = new_generation'''