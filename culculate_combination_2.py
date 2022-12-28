# coding: utf-8

def main():
    max = 20 # X人から選ぶ
    comb_list = cul_comb(max)
    print(comb_list)
    
# X人のメンバーから2人を選ぶ組み合わせを列挙するプログラム
def cul_comb(max):
    comb_list = []
    for i in range(max - 1):
        for j in range(i+1,max):
            comb_list.append([i,j])
    
    return comb_list

if __name__ == "__main__":
    main()