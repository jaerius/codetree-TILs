#일단 첫번째 숫자 입력 받는다 => 반복횟수
N = int(input())
#나머지 커맨드를 입력 받는다
commands=[]
for _ in range(N):
    command= input()
    commands.append(command)

#커맨드를 쪼개고, 커맨드에 따라 구현한다
def process_commands(commands):
    dynamic_array = []
    outputs = []

    for command in commands:
        parts = command.split()
        cmd = parts[0]

        if cmd == "push_back":
            dynamic_array.append(int(parts[1]))
        elif cmd == "pop_back":
            dynamic_array.pop()
        elif cmd == "size":
            outputs.append(len(dynamic_array))
        elif cmd == "get":
            k = int(parts[1])
            outputs.append(dynamic_array[k - 1])

    return outputs



    
#해당 내용을 하나씩 출력한다
output = process_commands(commands)
for result in output:
    print(result)