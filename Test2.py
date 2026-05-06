import numpy as np

def main():
    print("=== ตัวอย่างการใช้งาน NumPy ===\n")

    # 1. การสร้าง Array
    print("1. การสร้าง Array 1 มิติ และ 2 มิติ (Matrix)")
    arr_1d = np.array([10, 20, 30, 40, 50])
    arr_2d = np.array([[1, 2, 3], 
                       [4, 5, 6]])
    
    print("Array 1 มิติ:")
    print(arr_1d)
    print("\nArray 2 มิติ:")
    print(arr_2d)
    print("-" * 30)

    # 2. การคำนวณทางคณิตศาสตร์ (Broadcasting)
    print("2. การบวก/คูณ ทุกค่าใน Array พร้อมกัน")
    added_arr = arr_1d + 5
    multiplied_arr = arr_1d * 2
    
    print(f"ค่าเดิม: {arr_1d}")
    print(f"บวก 5:   {added_arr}")
    print(f"คูณ 2:   {multiplied_arr}")
    print("-" * 30)

    # 3. การหาค่าสถิติเบื้องต้น
    print("3. การหาค่าเฉลี่ย (Mean) และค่าสูงสุด (Max)")
    data = np.array([15, 22, 8, 42, 19, 33])
    
    mean_val = np.mean(data)
    max_val = np.max(data)
    min_val = np.min(data)
    
    print(f"ข้อมูล: {data}")
    print(f"ค่าเฉลี่ย: {mean_val:.2f}")
    print(f"ค่าสูงสุด: {max_val}")
    print(f"ค่าต่ำสุด: {min_val}")
    print("-" * 30)

    # 4. การคูณเมทริกซ์ (Dot Product)
    print("4. การคูณ Matrix (Dot Product)")
    matrix_a = np.array([[1, 2], 
                         [3, 4]])
    matrix_b = np.array([[5, 6], 
                         [7, 8]])
    
    dot_result = np.dot(matrix_a, matrix_b)
    # หรือใช้สัญลักษณ์ @ แทน np.dot() ก็ได้: matrix_a @ matrix_b
    
    print("ผลลัพธ์การคูณ Matrix A และ B:")
    print(dot_result)
    print("=" * 30)

if __name__ == "__main__":
    main()