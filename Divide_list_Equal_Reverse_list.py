#In a given list divide the list into 3 equal parts chuncks and reverse the list elements
# in each of the list:
sample_list = [1,2,3,4,5,6,7,8,9]
#Taking length of the sample_list
length_list = len(sample_list) #9
#Dividing the sample List and converting it into integer
chunk_size = int(length_list/3) #output 3.0 so converting into integer
#creating a start index for taking 1st Element in the smmple_list
start =0
#creating end index for taking last element in the sample_list
end = chunk_size
#Iterating the range from 1 to 3 times
for i in range(1,4):
    #taking 1st the chunk of list from the sample list
    chuck_list = sample_list[start:end] #[1,2,3]
    #Reverse the reversed is function and converting that again into list
    print(f"Chunk_{i} = {list(reversed(chuck_list))}")
    start = end
    end +=chunk_size





