# -*- coding=UTF-8 -*-
import xlrd, mysql.connector
import sys, os
sys.path.append('..')
import globalvars


if __name__ == '__main__':
    xls = xlrd.open_workbook('1.xls', 'rb')
    sh = xls.sheets()[0]
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    for row in range(1, sh.nrows):
        if sh.cell(row, 6).value != u'已调入':
            continue
        dob = sh.cell(row, 0).value
        dob = dob[6:14]
        dob = '%s-%s-%s' % (dob[0:4], dob[4:6], dob[6:8])
        dor_y = dob[0:4]
        if sh.cell(row, 2).value == u'男':
            dor = '%s-%s-%s' % (int(dor_y) + 60, dob[5:7], dob[8:10])
        else:
            dor = '%s-%s-%s' % (int(dor_y) + 50, dob[5:7], dob[8:10])
        sql = 'SELECT id FROM dangan WHERE DangAnHao=%s'
        param = (sh.cell(row, 3).value,)
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if cursor.rowcount == 0:
            sql = '''
                INSERT INTO dangan
                VALUES(
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            param = (
                0, sh.cell(row, 3).value, sh.cell(row, 0).value,
                sh.cell(row, 1).value, sh.cell(row, 2).value, dob,
                dor, sh.cell(row, 4).value, sh.cell(row, 5).value,
                sh.cell(row, 6).value, 0, 0
            )
            cursor.execute(sql, param)
        else:
            sql = '''
                UPDATE dangan
                SET
                DangAnHao=%s, ShenFenZheng=%s, XingMing=%s,
                XingBie=%s, RenYuanLeiBie=%s, CunDangRiQi=%s,
                CunDangZhuangTai=%s, ChuShengRiQi=%s, YuTuiXiuRiQi=%s
                WHERE id=%s
            '''
            param = (
                sh.cell(row, 3).value, sh.cell(row, 0).value,
                sh.cell(row, 1).value, sh.cell(row, 2).value,
                sh.cell(row, 4).value, sh.cell(row, 5).value,
                sh.cell(row, 6).value, dob, dor, data[0][0]
            )
            cursor.execute(sql, param)
        print sh.cell(row, 0).value, sh.cell(row, 1).value
    cnx.commit()
    cursor.close()
    cnx.close()