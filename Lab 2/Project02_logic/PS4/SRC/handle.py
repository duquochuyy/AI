from header import *

# clauses la chuoi cac clause
# moi clause chua 1 list literal
# doc du lieu tu file input
def readFile(file_name: str):
    with open(file_name, 'r') as fi:
        # print(file_name)
        clauses = []
        # doc clause alpha -> bo khoang trang -> cat thanh cac literal
        alpha = fi.readline().splitlines()[0].replace(' ', '').split("OR")
        # doc so luong clause cua KB
        num_KB = int(fi.readline())
        # doc tung clause cua KB
        for i in range(num_KB):
            listLiteral = Clause((fi.readline().splitlines()[0].replace(' ', '').split("OR")))
            clauses.append(listLiteral)
        # neu alpha la chuoi cac literal -> cat ra va phu dinh tung literal
        for i in alpha:
            clauses.append(Clause([negation(i)]))
    return clauses

def PL_Resolution(file_name:str, clauses):
    with open(file_name, 'w') as fo:
        entails = False
        while True:
            # luu clause moi tao
            newClauses = []
            for i in range(len(clauses)):
                for j in range(i+1, len(clauses)):
                    # ket hop 2 clause voi nhau
                    clause1 = clauses[i]
                    clause2 = clauses[j]
                    newClause = Clause.merge(clause1, clause2)
                    # tao ra duoc cai moi
                    # khong phai clause vo nghia
                    # clause do chua co trong list clauses hien tai
                    # clause do chua co trong list clauses moi
                    if newClause and newClause.nonsense() and newClause not in clauses and newClause not in newClauses:
                        newClauses.append(newClause)
            # xuat so luong clause ra
            fo.write(str(len(newClauses)) + '\n')
            # KB  not entails alpha
            if newClauses == []:
                entails = False
                break
            else:
                # tiep tuc cong vao va thuc hien
                clauses = clauses + newClauses
                for i in newClauses:
                    fo.write(str(i) + '\n')

            # KB entails alpha
            if Clause([]) in newClauses:
                entails = True
                break

        # in ra ket qua
        if entails == True:
            fo.write("YES")
        else:
            fo.write("NO")

def handleTestCase(file_name: str, numInput):
    # input
    print(file_name)
    clauses = readFile(file_name)
    # create file output
    pathParentOutput = '.\OUTPUT'
    path = pathParentOutput + '\\' + 'out' + numInput
    # PL_Resolution and output
    PL_Resolution(path, clauses)
    

# doc toan bo file input trong folder INPUT
def readFolderInput():
    pathParentInput = os.path.join(os.curdir,'INPUT')
    dir_list = os.listdir(pathParentInput)
    for i in range(len(dir_list)):
        numInput = dir_list[i][dir_list[i].find('put'):]
        path = os.path.join(pathParentInput,dir_list[i])
        handleTestCase(path, numInput)