import xlrd
import datetime
from math import radians, cos, sin, asin, sqrt


class Parser:

    """
    def __new__(cls, *args, **kwargs):
        if len(args) < 1 and len(kwargs) < 1:
            print("Need Filenames")
            return None
        else:
            return super(Parser, cls).__new__(cls)
    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.start_row=6
        self.start_col=1
        self.start_date_row=self.start_row+1
        self.start_date_col=self.start_col+1
        self.space_size=5

    def find_sheet_index_by_bus_num(self, bus_num):
        excel_file = xlrd.open_workbook(self.file_name)
        # print(excel_file.sheet_names())  # 시트목록을 출력(list형식)

        sheet_names=excel_file.sheet_names()
        is_founded=False
        sheet_idx=0

        for sheet_name in sheet_names:
            if bus_num in sheet_name:
                is_founded=True
                break
            sheet_idx+=1

        if is_founded:
            return sheet_idx
        else:
            return -1

    def find_bus(self, bus_num):
        excel_file = xlrd.open_workbook(self.file_name)
        pass


    """
        주어진 file_name에 있는 시간표를 객체화한다 
    """
    def create_bus_timetable(self, file_name):
        """
        doc doc doc 
        :param file_name: 
        :return: 
        """
        excel_file = xlrd.open_workbook(file_name)
        total_sheets=excel_file.nsheets

        for sheet_idx in range(total_sheets):
            sheet = excel_file.sheet_by_index(sheet_idx)

            rows = sheet.nrows
            cols = sheet.ncols

            print("*" * 20)
            print("read sheet {name}".format(name=sheet.name))
            print("*" * 20)

            for row_idx in range(rows):
                for col_idx in range(cols):
                    cell_value = sheet.cell_value(row_idx, col_idx)

                    if isinstance(cell_value, float) and col_idx is not self.start_col:

                        date_tuple = xlrd.xldate_as_tuple(cell_value, excel_file.datemode)
                        bus_time = datetime.datetime(2017, 11, 1, date_tuple[3], date_tuple[4], date_tuple[5])

                        print(bus_time.strftime('%H:%M'), end=" " * 4)

                    elif row_idx == self.start_row:
                        print(cell_value.replace("\n", ""), end=" " * 2)

                    else:
                        print(cell_value, end=" " * self.space_size)

                print("\n")

    '''
        excel sheet index의 데이터를 읽어온다 
    '''
    def print_bus_time_table(self, index):
        excel_file = xlrd.open_workbook(self.file_name)
        sheet=excel_file.sheet_by_index(index)

        rows=sheet.nrows
        cols=sheet.ncols

        print("*" * 20)
        for row_idx in range(rows):
            for col_idx in range(cols):
                cell_value = sheet.cell_value(row_idx, col_idx)

                if isinstance(cell_value, float) and col_idx is not self.start_col:

                    date_tuple= xlrd.xldate_as_tuple(cell_value, excel_file.datemode)
                    bus_time=datetime.datetime(2017,11,1, date_tuple[3], date_tuple[4], date_tuple[5])

                    print(bus_time.strftime('%H:%M'), end=" "*4)

                elif row_idx == self.start_row:
                    print(cell_value.replace("\n", ""), end=" "*2)

                else:
                    print(cell_value, end=" "*self.space_size)

            print("\n")

    def calculate_distance(self, lon1, lat1, lon2, lat2):
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        # Radius of earth in kilometers is 6371
        km = 6371* c
        return km

if __name__ == '__main__':
    parser=Parser('/Users/voiceloco/Downloads/jejuPublic.xlsx')
    print(parser.file_name)

