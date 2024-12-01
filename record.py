import os

def record1(agent_name,result, total_time, fn=0, gn=0, hn=0, visited=None):
    if os.path.lexists(r"C:\Users\CS0064TX\Desktop\CS50\A_I_course\lab2_code\lab2_code\Normal_map.txt"):
        with open("Normal_map.txt",'a',encoding='utf-8') as f:
            print(f"agent_name{agent_name}\t path: {result}\t total_time: {total_time}\t total_cost:{fn}\t growth: {gn}\t heuristic: {hn}\t first visited 10: {list(visited)[:10]}\t total visited {len(visited)}",file=f)
    else:
        with open("Normal_map.txt",'x',encoding='utf-8') as f:
            print(f"agent_name{agent_name}\t path: {result}\t total_time: {total_time}\t total_cost:{fn}\t growth: {gn}\t heuristic: {hn}\t first visited 10: {list(visited)[:10]}\t total visited {len(visited)}",file=f)


def record2(agent_name,result, total_time, fn=0, gn=0, hn=0, visited=None):
    if os.path.lexists(r"C:\Users\CS0064TX\Desktop\CS50\A_I_course\lab2_code\lab2_code\H_shape_map.txt"):
        with open("H_shape_map.txt",'a',encoding='utf-8') as f:
            print(f"agent_name{agent_name}\t path: {result}\t total_time: {total_time}\t total_cost:{fn}\t growth: {gn}\t heuristic: {hn}\t first visited 10: {list(visited)[:10]}\t total visited {len(visited)}",file=f)
    else:
        with open("H_shape_map.txt",'x',encoding='utf-8') as f:
            print(f"agent_name{agent_name}\t path: {result}\t total_time: {total_time}\t total_cost:{fn}\t growth: {gn}\t heuristic: {hn}\t first visited 10: {list(visited)[:10]}\t total visited {len(visited)}",file=f)

