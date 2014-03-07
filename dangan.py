# -*- coding=UTF-8 -*-
from flask.views import MethodView


class DangAn(MethodView):
    def get(self, rec_id):
        from flask import session, redirect, request, render_template
        import globalvars
        import datetime

        if not 'user_id' in session:
            return redirect('/login')
        cat = request.args.get('cat', '0')
        sql = '''
            select
                d.*,
                (
                    select
                        a.code
                    from
                        cm_archieve.access_code a
                    where
                        a.date=%(now_date)s
                        and
                        a.archieve_id=d.ShenFenZheng
                    order by
                        a.id
                        desc
                    limit 1
                ) as code
            FROM
                cm_archieve.dangan d
            WHERE
                d.id=%(archieve_id)s
        '''
        param = {
            'archieve_id': rec_id,
            'now_date': datetime.datetime.now().strftime('%Y-%m-%d')
        }
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        dob = data[0][5].split('-')
        dor = data[0][6].split('-')
        if cat == '0':
            sql = 'SELECT * FROM wenjian WHERE aid=%s'
            param = (rec_id,)
        else:
            sql = 'SELECT * FROM wenjian WHERE aid=%s AND LeiBie=%s'
            param = (rec_id, cat)
        cursor.execute(sql, param)
        data1 = cursor.fetchall()
        globalvars.close_db(cursor, cnx)
        lp1 = '/saomiao/%s' % (rec_id,)
        lp2 = '/luru/%s' % (rec_id,)
        return render_template(
            'dangan.html',
            id = rec_id,
            row = data[0],
            link1 = lp1,
            link2 = lp2,
            fs_root = globalvars.G_FILE_SERVER_ROOT,
            aid = globalvars.get_aid(rec_id),
            data1 = data1,
            dob = dob,
            dor = dor,
            cat = cat,
            User = session['user_name']
        )

    def post(self, rec_id):
        from flask import request, redirect, session
        import globalvars

        idcard = request.form['shenfenzheng']
        name = request.form['xingming']
        if int(idcard[16:17]) % 2 == 1:
            gender = u'男'
        else:
            gender = u'女'
        s, t = 0, 0
        if 'female' in request.form.getlist('check'):
            s = 1
        if 'stow' in request.form.getlist('check'):
            t = 1
        dob = '%s-%s-%s' % (
            request.form['dob-year'],
            request.form['dob-month'],
            request.form['dob-date']
        )
        dor = '%s-%s-%s' % (
            request.form['dor-year'],
            request.form['dor-month'],
            request.form['dor-date']
        )
        sql = '''
            UPDATE dangan
            SET
            ChuShengRiQi=%s,YuTuiXiuRiQi=%s,NvGuanLiGangWei=%s,
            TeShuGongZhong=%s,XingMing=%s,ShenFenZheng=%s,
            XingBie=%s
            WHERE id=%s
        '''
        param = (dob, dor, s, t, name, idcard, gender, rec_id)
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        cnx.commit()
        globalvars.close_db(cursor, cnx)
        globalvars.caozuo_jilu(session['user_id'], u'修改档案信息', rec_id)
        return redirect('/dangan/%s' % (rec_id))


class DeleteArchieve(MethodView):
    def post(self, archieve_id):
        from flask import redirect, request
        from globalvars import connect_db, close_db

        sql = (
            'update '
            'dangan '
            'set '
            'ZhuanChu=%(zhuanchu)s '
            'where '
            'id=%(archieve_id)s '
        )
        param = {
            'zhuanchu': request.form['reason'],
            'archieve_id': archieve_id
        }
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        cnx.commit()
        close_db(cursor, cnx)
        return redirect('/')