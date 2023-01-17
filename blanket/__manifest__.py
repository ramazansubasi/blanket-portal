{
    'name':'Blanket',
    'version': '1.5.19',
    'author': 'Autoronics',
    'summary': 'Blanket Home Management System',
    'sequence': 1,
    'description':'This is blanket home management system software suppored in Odoo v15',
    'category':'blanket',
    'website':'https://www.autoronics.com',
    'depends':['base','website'],

    'data':[
        'security/ir.model.access.csv',
        #'security/security.xml',
        'views/all_records_list.xml',
        # 'views/record_item.xml',
        #'views/form_response.xml',
        #'views/sale_order.xml',
        #'views/form_request.xml',
        #'views/car_view.xml',
        #'views/extra.xml',
        #'views/city.xml',
        #'views/snippets/s_booking_widget.xml',
        #'views/snippets/demo/s_cart_product/s_cart_products.xml',
        #'views/snippets/demo/snippets.xml',
        'views/blanket_view.xml',
        # 'views/snippets/s_car_select.xml',
        # 'views/snippets/s_reservation_form.xml',
        # 'reports/blanket_report_views.xml',
        #'data/antalyahermes.xml'
    ],

    'assets': {
        'web.assets_frontend': [
            # 'blanket/static/src/css/intlTelInput.css',
            # 'blanket/static/src/css/jquery-clockpicker.min.css',
            # 'blanket/static/src/css/style.css',
            # 'blanket/static/src/js/jquery-clockpicker.min.js',
            # 'blanket/static/src/js/intlTelInput.min.js',
            # 'blanket/static/src/js/utils.js',
            # 'blanket/static/src/js/reservation.js',
            # 'blanket/static/src/js/script.js',
            'blanket/static/src/js/thunkableWebviewerExtension.js'
        ]
    }

}
