# -*- coding=UTF-8 -*-
from flask.views import MethodView

#统计
#：各用户操作总数对比
#：按月份各用户操作总数曲线
#：按月份各用户扫描总数曲线
#：按月份各用户添加档案总数曲线


class TongJi(MethodView):
    def get(self):
        from flask import render_template, session
        from globalvars import connect_db, close_db
        import datetime

        if not 'user_id' in session:
            return redirect('/login')
        cnx = connect_db()
        cursor = cnx.cursor()
        sql_1 = '''
            select
                u.id,u.mingcheng,count(c.id)
            from
                `cm_archieve`.user u
                left join
                `cm_archieve`.caozuo_jilu c
                on
                u.id=c.yh_id
            group by
                u.id
        '''
        cursor.execute(sql_1)
        result_1 = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template(
            'tongji.html',
            User = session['user_name'],
            counter_1 = result_1,
            sum_1 = len(result_1)
        )


class TongjiMonth(MethodView):
    def get(self):
        from flask import render_template, session, request
        from globalvars import connect_db, close_db
        import datetime

        if not 'user_id' in session:
            return redirect('/login')
        year = request.args.get('year', datetime.datetime.now().strftime('%Y'))
        month = request.args.get('month', datetime.datetime.now().strftime('%m'))
        sql = 'select u.MingCheng, (' + \
            'select count(*) ' + \
            'from cm_archieve.caozuo_jilu c ' + \
            'where c.yh_id=u.id and c.RiQi like "' + \
            year + '-' + month + '%"' + \
            ') as cur_mongth ' + \
            'from cm_archieve.user u'
        param = {
            'month': '%s-%s' % (year, month) + '%'
        }
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template('tongji_month.html',
            counter_1 = res,
            sum_1 = len(res),
            date = '%s-%s' % (year, month))

    def post(self):
        from flask import request, redirect

        year = request.form['year']
        month = request.form['month']

        return redirect('/tongji_month/?year=%s&month=%s' % (year, month))
