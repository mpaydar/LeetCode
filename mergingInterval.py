


intervals= [[1,5], [2,3] ,[4,6],[7,8],[8,10],[12,15]]

def mergeIntervalStack (interval_arrays):
    stack_interval_representation = []

    for i in range(len(interval_arrays)):
        if len(stack_interval_representation) >0:
            top_element=stack_interval_representation[len(stack_interval_representation)-1]
            incoming_end = interval_arrays[i][0]
            incoming_start = interval_arrays[i][0]
            currentEndOnStack= top_element[1]
            current_start=top_element[0]
            if incoming_end<currentEndOnStack :
                merged_interval=merge(top_element,interval_arrays[i])
                stack_interval_representation.pop()
                stack_interval_representation.append(merged_interval)



            elif current_start > incoming_start and  incoming_end> currentEndOnStack:
                merged_interval=merge(top_element,interval_arrays[i])
                stack_interval_representation.pop()
                stack_interval_representation.append(merged_interval)

            elif current_start > incoming_start and incoming_end >= currentEndOnStack:
                merged_interval = merge(top_element, interval_arrays[i])
                stack_interval_representation.pop()
                stack_interval_representation.append(merged_interval)

            elif currentEndOnStack >= incoming_start:
                merged_interval = merge(top_element, interval_arrays[i])
                stack_interval_representation.pop()
                stack_interval_representation.append(merged_interval)

            else:
                stack_interval_representation.append(interval_arrays[i])


        else:
            stack_interval_representation.append(interval_arrays[i])

    print(stack_interval_representation)


def merge (a,b):
    min_start= min(a[0],b[0])
    end_start=max(a[1],b[1])
    merge_temp_interval = [min_start,end_start]
    return merge_temp_interval

mergeIntervalStack(intervals)