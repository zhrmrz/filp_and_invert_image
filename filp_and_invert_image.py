class Sol:
    def filp_and_invert_image(self,A):
        res=[]
        for row in A:
            res.append([abs(1-val) for val in reversed(row)])
        return res

if __name__ == '__main__':
    p = Sol()
    print(p.filp_and_invert_image(A=[[1,1,0]]))
