"""Định nghĩa một class có tên là Vietnam, với static method là printNationality."""


class Vietnam(object):
    @staticmethod
    def printNationality():
        print("Vietnam")

VietnamVodich = Vietnam()
VietnamVodich.printNationality()
Vietnam.printNationality()