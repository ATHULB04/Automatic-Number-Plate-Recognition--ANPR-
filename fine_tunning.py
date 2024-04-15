def correcting(license_plate):
    if license_plate[2] in ['O', 'I', 'J', 'A', 'G', 'S']:
        if license_plate[2] == 'O':
            license_plate = license_plate[:2] + '0' + license_plate[3:]
        elif license_plate[2] == 'I':
            license_plate = license_plate[:2] + '1' + license_plate[3:]
        elif license_plate[2] == 'J':
            license_plate = license_plate[:2] + '3' + license_plate[3:]
        elif license_plate[2] == 'A':
            license_plate = license_plate[:2] + '4' + license_plate[3:]
        elif license_plate[2] == 'G':
            license_plate = license_plate[:2] + '6' + license_plate[3:]
        elif license_plate[2] == 'S':
            license_plate = license_plate[:2] + '5' + license_plate[3:]
    return license_plate


def filtering(number):
    ls=["KL33 5341","KL40 C 5056","KL 35A 4833","KL15 A726"]
    if number in ls:
        return number
    else:
        return "Invalid Numberplate"