with open('blog_list.txt' , 'r') as file:
    file_data = file.read()
# print(file_data)

my_list = file_data.split('----------------\n')
# print(my_list)

new_list = []

# datani bosluqlara ve \n'lere gore ayiririq
for i in my_list:
    temporary_list = []
    if len(i) !=0:
        id,title,author_name= i.strip().split("\n")                 
        # print(id,title,author_name)


# temporary liste ':' ve bosluga gore ayirdigimiz datani elave edirik
        temporary_list.append(id.split(': ')[1])
        temporary_list.append(title.split(': ')[1])
        temporary_list.append(author_name.split(': ')[1])
        # print(temporary_list)


# yuxarida new_list yaradiriq ve datalari ora append edirik
        new_list.append(temporary_list)
print(new_list)



