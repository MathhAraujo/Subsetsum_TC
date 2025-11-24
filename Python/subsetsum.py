import pandas as pd
import time

def subset_sum(numbers, target):
    solutions = []

    def search(index, current_sum, current_list):

        if current_sum == target:
            if current_list not in solutions:
                solutions.append(current_list[:])
            return

        if index >= len(numbers) or current_sum > target:
            return

        current_num = numbers[index]
        current_list.append(current_num)

        search(index + 1, current_sum + current_num, current_list)

        current_list.pop()

        search(index + 1, current_sum, current_list)

        return

    search(0, 0, [])
    return solutions

def execute_file(sample_path, result_path):

    df = pd.read_excel(result_path, engine='openpyxl')

    language_list = []
    input_size_list = []
    target_list = []
    execution_time_list = []


    with open(sample_path) as current_file:
        data = current_file.readlines()
        
        for i in range(int(len(data) / 3)):
            target = int(data[i*3][:-1])
            numbers = []
            for j in data[i*3 + 1][:-1].split(" "):
                numbers.append(int(j))

            language_list.append("Python")
            input_size_list.append(len(numbers))
            target_list.append(target)

            start = time.perf_counter()
            solutions = subset_sum(numbers, target)
            execution_time_list.append(f"{((time.perf_counter() - start)*1000):.4f}")
    
    df_new = pd.DataFrame({
        'language': language_list,
        'input_size': input_size_list,
        'target': target_list,
        'execution_time': execution_time_list
    })

    if not df.empty:
        df_final = pd.concat([df, df_new], ignore_index=True)
    else:
        df_final = df_new


    df_final['execution_time'] = df_final['execution_time'].astype(float).map('{:.4f}'.format)

    df_final.to_excel(result_path, index=False, engine='openpyxl')
    print(f"Dados de '{sample_path}' processados.")
        
execute_file(".\\Input\\small_input.txt", ".\\Results\\results.xlsx")
execute_file(".\\Input\\med_input.txt", ".\\Results\\results.xlsx")
execute_file(".\\Input\\big_input.txt", ".\\Results\\results.xlsx")