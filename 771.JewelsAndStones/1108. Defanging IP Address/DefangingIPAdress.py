class Solution:
    def defangIPaddr(self, address: str) -> str:
        defangedAdress = address.replace(".", "[.]")
        return defangedAdress
