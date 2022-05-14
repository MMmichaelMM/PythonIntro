import pandas as pd
import os
from alive_progress import alive_bar


class ConvertData:
    def __init__(self, file):
        self.file = file

        self.df_data_table = []

        self.signalNames = ['timestamp',
                            'LLDP_LatAccelAuth',
                            'LLDP_LongAccelAuth',
                            'YRP_YawRateAuth',
                            'SWIP_StrgWhlAngAuth',
                            'BGI3P_BrkPedPstnAuth',
                            'RAVP_WhlAngVelRRrAuth',
                            'RAVP_WhlAngVelLRrAuth',
                            'TEGP_TrnsShftLvrPstnAuth',
                            'VSADP_VehSpdAvgDrvnAuth',
                            'ThrPstn']

        self.num_of_can_signals = 11  # 10 signals + 1 timestamp

        def load_data():  # load the data
            df_can = pd.read_csv(self.file)

            return df_can

        self.df_can = load_data()
        self.df_can = self.df_can.shift(-1)

    def retrieve_data(self, str_data, channel_name):
        str_list = str_data.split(' ')

        for x in str_list:
            ind = x.find(channel_name + '=')
            if ind == 0:
                tmp = x.replace(channel_name + '=', '')
                ind = tmp.count('.')
                if ind == 2:
                    data = float(tmp[:-1])
                    return data
                else:
                    data = float(tmp)
                    return data
            else:
                data = ' '

        return data

    def get_can_data(self, time_stamp, str_data):
        data_row = [''] * self.num_of_can_signals
        data_row[0] = time_stamp
        for i in range(1, self.num_of_can_signals):
            data_row[i] = self.retrieve_data(str_data, self.signalNames[i])
        return data_row

    def create_signals_table(self):
        if not os.path.exists('can_table.csv'):
            print('=========== Build Can-Table ==============')
            n_can = len(self.df_can)
            self.df_can_table = pd.DataFrame(columns=self.signalNames)
            with alive_bar(n_can-1, force_tty=True) as bar:
                for i in range(n_can-1):
                    tmp_time_stamp = self.df_can.loc[i].at['timestamp']
                    tmp_val = self.df_can.loc[i].at['values']
                    tmp_row = self.get_can_data(tmp_time_stamp, tmp_val)
                    self.df_can_table.loc[i] = tmp_row
                    bar()

            # directory = os.getcwd()
            self.df_can_table.to_csv('can_table.csv')
        else:
            print('============ Can-Table Exists ==============')
            self.df_can_table = pd.read_csv('can_table.csv')


cd = ConvertData('can_log_short.csv')
cd.create_signals_table()


