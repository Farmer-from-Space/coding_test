class Solution:
    def reorderLogFiles(self, logs):
        Llogs, Dlogs = [], []
        for i in logs:
            if list(i.split(" "))[1].isalpha():
                Llogs.append(i)
            else:
                Dlogs.append(i)
        
        Llogs = sorted(Llogs, key = lambda x: (x.split(' ')[1:],x.split(' ')[0]))
        return Llogs+Dlogs