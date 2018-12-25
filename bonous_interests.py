#! usr/bin/python3

interest = input("interest: ");
interest = int(interest);
print ("The interest is :", interest);

if ((interest <= 100000) and (interest > 0)):
    bonous = interest * 0.1;
elif ((interest<200000) and (interest>100000)):
    bonous = 100000 * 0.1 + (interest - 100000) * 0.075;
elif ((interest<400000) and (interest >=200000)):
    bonous = 100000 * 0.175 + (interest - 200000) * 0.05;
elif ((interest>=400000) and (interest < 600000)):
    bonous = 100000 * 0.175 + 200000 * 0.05 + (interest - 400000) * 0.03;
elif ((interest >= 600000) and (interest < 1000000)):
    bonous = 100000 * 0.175 + 200000 * 0.05 + 200000 * 0.03 + (interest - 600000) * 0.015;
else:
    bonous = 100000 * 0.175 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (interest - 1000000) * 0.01;

print ("The bonous is: ",bonous);
