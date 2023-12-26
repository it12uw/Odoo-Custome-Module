{
  'name': 'Snap QC Shuttle',
  'version': '14.0',
  'author': 'Steven Morison',
  'summary': 'Machine Quality Control For Shuttle',
  'author': 'Steven Morison, stevenmorizon123@gmail.com',
  'category': 'Manufacture',
  'depends': ['base', 'web', 'mesin_unggul'],
  'data': [
 
    'security/ir.model.access.csv',
    'views/view_layout_shuttle.xml',
    'views/view_data_mesin.xml',
    # 'views/view_data_blok.xml',
    # 'views/view_data_line.xml',
    # 'views/view_data_kode_kain.xml'
    'views/view_snap_qc.xml',
    'views/view_snap_qc_pop_up.xml',
    'report/report_menu.xml',
    'report/report_qc_shuttle.xml',
  ],

  'auto_install': False,
  'installable': True,
  'application': True,
}

