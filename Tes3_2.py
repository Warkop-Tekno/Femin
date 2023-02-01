import femin


# Load File
femin.load("data tes 3.h5")

# Change Variable
print(femin.gap)
femin.gap['He'] = 0.92
femin.gap['N2'] = 0.04


# Preview
femin.preview()
