/** @odoo-module **/
import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class IssabelSystrayButton extends Component {
    static template = "issabel_api_log.SystrayButton";
    
    setup() {
        super.setup();
        this.orm = useService("orm");
       
    }
   

    async odoo_debug(num) {
       
        let cleanUrl = window.location.origin + window.location.pathname+'?debug=1';
           window.open(cleanUrl ,'_self');
        
        
      
       
    }

}
registry.category("systray").add("odoo_debug.systray", { Component: IssabelSystrayButton }, { sequence: 1 });

