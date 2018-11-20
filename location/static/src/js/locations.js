odoo.define('location.gpslocation', function(require) {
    var form_widget = require('web.FormRenderer');
    var rpc = require('web.rpc');
    
    form_widget.include({
        _addOnClickAction: function($el, node) {
            var self = this;
            $el.click(function() {
                console.log("Function Called")
                var x = document.getElementById("adel");
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showPosition);
                } else {
                    alert("Geolocation is not supported by this browser.")
                }
                function showPosition(position) {                    
                    var records = rpc.query({
                        model: self.state['model'],
                        method: 'get_gps_location',
                        args: [position.coords.latitude, position.coords.longitude, self.state['res_id']],
                    });
                }
            });
        },
    });       
});
