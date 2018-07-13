import pickle
import math


if __name__ == '__main__':
    with open('dict.txt', 'rb') as f:
        dict_ = pickle.load(f)
    data = []
    with open('../NSL-KDD/KDDTrain+_20Percent.arff', 'r') as f: #KDDTest-21 KDDTrain+ KDDTest+ KDDTrain+_20Percent
        for line in f.readlines():
            if line[0] != '@':
                num = len(data)
                data.append([])
                tem = line.strip().split(',')
                for i in range(len(tem)):
                    if i in dict_:
                        data[num].append(dict_[tem[i]]/dict_[i])
                    else:
                        if '.' in tem[i]:
                            data[num].append(float(tem[i]))
                        else:
                            data[num].append(int(tem[i]))
    maxa = []
    mina = []
    for x in data[0]:
        maxa.append(x)
        mina.append(x)
    for line in data:
        for i in range(len(line)):
            maxa[i] = max(maxa[i], line[i])
            mina[i] = min(mina[i], line[i])
    for i in range(len(maxa)):
        if maxa[i] > 10000:
            maxt = mina[i]
            mint = mina[i]
            for j in range(len(data)):
                if data[j][i] > 0:
                    data[j][i] = math.log10(data[j][i])
                    maxt = max(maxt, data[j][i])
                    mint = min(mint, data[j][i])
            maxa[i] = maxt
            mina[i] = mint
    for i in range(len(maxa)):
        if maxa[i] > 1:
            # maxt = mina[i]
            # mint = mina[i]
            for j in range(len(data)):
                if maxa[i]-mina[i] > 0:
                    data[j][i] = (data[j][i]-mina[i])/(maxa[i]-mina[i])
            #         maxt = max(maxt, data[j][i])
            #         mint = max(mint, data[j][i])
            # maxa[i] = maxt
            # mina[i] = mint
    with open('../data/KDDTrain+_20Percent.txt', 'w') as f:    ##KDDTest-21 KDDTrain+ KDDTest+ KDDTrain+_20Percent
        for i in range(len(data)):
            for j in range(len(data[i])):
                f.write(str(data[i][j]))
                if j != len(data[i])-1:
                    f.write(',')
            f.write('\n')

# protocol_type = ['tcp','udp', 'icmp'];
# service = ['aol', 'auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime', 'discard', 'domain', \
# 'domain_u', 'echo', 'eco_i', 'ecr_i', 'efs', 'exec', 'finger', 'ftp', 'ftp_data', 'gopher', \
# 'harvest', 'hostnames', 'http', 'http_2784', 'http_443', 'http_8001', 'imap4', 'IRC', 'iso_tsap', \
# 'klogin', 'kshell', 'ldap', 'link', 'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns', \
# 'netbios_ssn', 'netstat', 'nnsp', 'nntp', 'ntp_u', 'other', 'pm_dump', 'pop_2', 'pop_3', \
# 'printer', 'private', 'red_i', 'remote_job', 'rje', 'shell', 'smtp', 'sql_net', 'ssh', 'sunrpc',\
# 'supdup', 'systat', 'telnet', 'tftp_u', 'tim_i', 'time', 'urh_i', 'urp_i', 'uucp', 'uucp_path', \
# 'vmnet', 'whois', 'X11', 'Z39_50'];
# flag = ['OTH', 'REJ', 'RSTO', 'RSTOS0', 'RSTR', 'S0', 'S1', 'S2', 'S3', 'SF', 'SH'];
# Class = ['normal', 'anomaly'];
# dict = {}
# for i in range(len(protocol_type)):
#     dict[protocol_type[i]] = i+1;
# for i in range(len(service)):
#     dict[service[i]] = i+1;
# for i in range(len(flag)):
#     dict[flag[i]] = i+1;
# for i in range(len(Class)):
#     dict[Class[i]] = i;
# dict[1] = 3;
# dict[2] = 70;
# dict[3] = 11;
# dict[41] = 1;
#
# with open('dict.txt', 'wb') as f:
#     pickle.dump(dict, f);
