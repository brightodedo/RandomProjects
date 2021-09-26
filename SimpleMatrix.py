class Matrix:

    def __init__(self, no_row, no_column):
        self.no_column = no_column
        self.no_row = no_row
        for i in range(self.no_row):
            exec("self.row" + str(i) + " = " + str([0] * no_column))

    def __str__(self):
        for i in range(self.no_row):
            exec("print(self.row"+str(i)+")")
        return ""

    def getNumberOfColumns(self):
        return self.no_column

    def getNumberOfRows(self):
        return self.no_row

    def getColumn(self, n):
        if n > self.no_column or n < 1:
            raise IndexError("No such column exists")
        else:
            col = [0] * self.no_row
            for i in range(self.no_row):
                exec("col["+str(i)+"] = self.row"+str(i)+"[" + str(n-1) + "]")
            return col

    def getRow(self, n):
        if n > self.no_row or n < 1:
            raise IndexError("Now such row exists")
        else:
            exec("self.disposable = self.row"+str(n-1)+"")
            return self.disposable

    def setRow(self, m, n):
        """ m is the row to be set; n is a row;"""
        if len(n) != self.no_column:
            raise IndexError("DimensionError: Dimensions are wrong")
        else:
            exec("self.row"+str(m-1)+" = n")

    def setColumn(self, m, n):
        """ m is the column to be set; n is the column"""
        if len(n) != self.no_row:
            raise IndexError("DimensionError: Dimesions are wrong")
        else:
            for i in range(len(n)):
                exec("self.row"+str(i)+"["+str(m-1)+"] = n["+str(i)+"]")

    def __add__(self, other):
        """Adds one matrix to another and returns the value"""
        # check if they are the same time
        if not isinstance(other, Matrix):
            raise TypeError(
                "TypeError: Can not add matrix type to another type")
        # check if their dimensions are the same then add
        elif (self.no_column == other.no_column) and (self.no_row == other.no_row):
            c = Matrix(self.no_row, self.no_column)
            for i in range(self.no_row):
                self.disposable = [0] * self.no_column
                for j in range(self.no_column):
                    exec("self.disposable["+str(j)+"] = self.row"+str(i) +
                         "["+str(j)+"] + other.row"+str(i)+"["+str(j)+"]")
                c.setRow(i+1, self.disposable)
            return c
        # else return dimensionerror
        else:
            raise ArithmeticError(
                "DimensionError: Dimensions are not the same")

    def __sub__(self, other):
        """Adds one matrix to another and returns the value"""
        # check if they are the same time
        if not isinstance(other, Matrix):
            raise TypeError(
                "TypeError: Can not add matrix type to another type")
        # check if their dimensions are the same then add
        elif (self.no_column == other.no_column) and (self.no_row == other.no_row):
            c = Matrix(self.no_row, self.no_column)
            for i in range(self.no_row):
                self.disposable = [0] * self.no_column
                for j in range(self.no_column):
                    exec("self.disposable["+str(j)+"] = self.row"+str(i) +
                         "["+str(j)+"] - other.row"+str(i)+"["+str(j)+"]")
                c.setRow(i+1, self.disposable)
            return c
        # else return dimensionerror
        else:
            raise ArithmeticError(
                "DimensionError: Dimensions are not the same")

    def __mul__(self, other):
        """multiplies to matrixes"""
        # check if other is a matrix object
        if not isinstance(other, Matrix):
            raise TypeError(
                "TypeError: Can not add matrix type to another type")
        # check if dimensions are not right
        if self.no_column != other.no_row:
            raise ArithmeticError(
                "DimensionError: Dimesions do not match for this operation")
        # runs if dimensions are right
        else:
            c = Matrix(self.no_row, other.no_column)
            for i in range(self.no_row):
                stage = [0] * other.no_column
                for j in range(other.no_column):
                    curr_col = other.getColumn(j+1)
                    self.disposable = 0
                    for k in range(self.no_column):
                        exec("self.disposable = self.disposable + (self.row" +
                             str(i)+"["+str(k)+"] * curr_col["+str(k)+"])")
                    stage[j] = self.disposable
                c.setRow(i+1, stage)
            return c
