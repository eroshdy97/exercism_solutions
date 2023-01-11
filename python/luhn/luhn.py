class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1:
            return False
        
        nums = []
        for char in self.card_num:
            if char.isdigit():
                nums.append(int(char))
            else:
                return False

        nums.reverse()
        for i in range(len(nums)):
            if i % 2 == 1:
                nums[i] = nums[i] * 2 if nums[i] <= 4 else nums[i] * 2 - 9
        nums.reverse()
        return sum(nums) % 10 == 0
