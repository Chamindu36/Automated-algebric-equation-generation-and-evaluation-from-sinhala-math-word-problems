from decimal import Decimal


def sinhala_Value_process(words, numbercounter, numsarray, tagged):
    numcounter = numbercounter
    nums = numsarray

    for i in range(0, len(words)):
        if (words[i] == "දෙගුණයකට" or words[i] == "දෙගුණයක්" or words[i] == "දෙගුණ" or words[i] == "දෙගුණය" or words[
            i] == "දෙකක්" or words[i] == "දෙකක"):
            words[i] = "2"
            temp = ("2", "CD")
            tagged[i] = temp

    for i in range(0, len(words)):
        if (words[i] == "තෙගුණයකට" or words[i] == "තෙගුණයක්" or words[i] == "තෙගුණ"or words[i] == "තිදෙනාට"):
            words[i] = "3"
            temp = ("3", "CD")
            tagged[i] = temp

    for i in range(0, len(words)):
        if (words[i] == "සිව්ගුණයකට" or words[i] == "සිව්ගුණයක්" or words[i] == "සිව්ගුණ" or words[i] == "සතරගුණයකට" or
                words[i] == "සතරගුණයක්" or words[i] == "සතරගුණ"):
            words[i] = "4"
            temp = ("4", "CD")
            tagged[i] = temp

    for i in range(0, len(words)):
        if (words[i] == "පස්ගුණයකට" or words[i] == "පස්ගුණයක්" or words[i] == "පස්ගුණ"):
            words[i] = "5"
            temp = ("5", "CD")
            tagged[i] = temp

    for i in range(0, len(words)):
        if (words[i] == "සයගුණයකට" or words[i] == "සයගුණයක්" or words[i] == "සයගුණ"):
            words[i] = "6"
            temp = ("6", "CD")
            tagged[i] = temp

    for i in range(0, len(words)):
        if (words[i] == "හත්ගුණයකට" or words[i] == "හත්ගුණයක්" or words[i] == "හත්ගුණ"):
            words[i] = "7"
            temp = ("7", "CD")
            tagged[i] = temp

    for i in range(0, len(words)):
        if (words[i] == "අටගුණයකට" or words[i] == "අටගුණයක්" or words[i] == "අටගුණ"):
            words[i] = "8"
            temp = ("8", "CD")
            tagged[i] = temp

    for i in range(0, len(words)):
        if (words[i] == "නවගුණයකට" or words[i] == "නවගුණයක්" or words[i] == "නවගුණ"):
            words[i] = "9"
            temp = ("9", "CD")
            tagged[i] = temp

    for i in range(0, len(words)):
        if (words[i] == "දසගුණයකට" or words[i] == "දසගුණයක්" or words[i] == "දසගුණ"):
            words[i] = "10"
            temp = ("10", "CD")
            tagged[i] = temp

    return words, numcounter, nums, tagged
