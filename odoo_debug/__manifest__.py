{   
    'name': 'Debug Mode Toggle Button in Systray',
    'version': '19.0.1.0.0',
    'license': 'OPL-1',
    'support': 'https://www.github.com/abomsalam20',
    'summary': 'Debug Mode Toggle Button in Systray',
    'description': """
        Odoo Debug Button

        - One click to enable/disable Developer Mode
        - Supports debug, debug=assets, debug=superuser
        - Always visible bug icon in systray
        - No configuration needed
        """,
    'author': "SW - Mostafa Abomsalam",
    'category': 'Tools',
    'images': ['static/description/icon.png'],
    'website': "https://www.github.com/abomsalam20",
    'depends': ['base'],
    'assets': {
        'web.assets_backend': [
            
    
            'odoo_debug/static/src/js/systray_button.js',
            'odoo_debug/static/src/xml/systray_button.xml',
          
        ],
    },
    'images': [
        'static/description/icon.png',  
    ],
     
    # بعض نسخ Odoo 19 بتحتاج السطر ده
    'icon': 'static/description/icon.png',

    # always loaded
    'data': [
        'security/ir.model.access.csv',
      
     
   

    ],
   
    'demo': [
        'demo/demo.xml',
    ],
    
}


