import pydicom
from json import dumps

file_dcm = ["IMG-0001-00001.dcm", "IMG-0001-00002.dcm", "IMG-0001-00003.dcm", "IMG-0001-00004.dcm", "IMG-0001-00005.dcm"]

def rd_file(data):
    ds = pydicom.read_file(data)
    return ds


def card(file):
    ds = rd_file(file)
    result = {'Name': file,
                 'Image Laterality': ds[0x0020,0x0062].value,
                 '?': ds[0x0020,0x0062].value,
                 'View Position':ds[0x0018,0x5101].value,
                 'Modality': ds[0x0008,0x0060].value,
                 'Photometric Interpretation ': ds[0x0028, 0x0004].value}
    jd=dumps(result)
    return jd

for i in file_dcm:
    print(card(i))