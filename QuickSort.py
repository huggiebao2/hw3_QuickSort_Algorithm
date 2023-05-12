def quick_sort(arr:list, first_index:int, last_index:int) -> None:    
    if first_index < last_index:
        # 以陣列的第一個元素作為基準點
        pivot = first_index                 # pivot 是基準點
        left = first_index                  # left 是左側指標
        right = last_index                  # right 是右側指標

        
        while left < right:

            # 只要左指標沒比基準點大，就往右移動
            while arr[left] <= arr[pivot] and left < last_index:
                left = left + 1
            
            # 只要右指標沒小於等於基準點，就往左移動
            while arr[right] > arr[pivot]:
                right = right - 1
            
            if left < right:
                # 交換左右指標指向的內容
                temp = arr[left]            # temp 拿來做兩者互換的暫時變數
                arr[left] = arr[right]
                arr[right] = temp
                print(arr)
        
        # 基準點和右指標交換
        temp = arr[pivot]                   # temp 拿來做兩者互換的暫時變數
        arr[pivot] = arr[right]
        arr[right] = temp
        print(arr)
        

        # 切成左右兩塊再跑一次
        quick_sort(arr, first_index, right - 1)
        quick_sort(arr, right + 1, last_index)

# 上課範例
def main():
    demo = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
    quick_sort(demo, 0, len(demo)-1)

if __name__ == '__main__':
    main()