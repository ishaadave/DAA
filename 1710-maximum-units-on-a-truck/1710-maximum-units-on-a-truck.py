class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        units = 0

        for boxes, units_per_box in boxTypes:
            take = min(boxes, truckSize)

            units += take * units_per_box
            truckSize -= take

            if truckSize == 0:
                break

        return units