var crowdtask = (function(){
    var version = "1.0";
    var url_root = '/apps/api/';

    function apps_list(){
        return $.ajax({
            url: url_root + 'applications' 
        });
    }

    return {
        "version": version,
        "apps_list" : apps_list
    }
}
)();

crowdtask.form = (function(){

    var text_tpl = 
            "<label for='{{field_id}}'>{{label}}" +
            "<input type='text' id='{{field_id}}' name='{{field_name}}'>" +
            "</label>";

    function generate_field(data, idx){
        switch (data.type){
            default:
                return text_field(data, idx);
        }
    }

    function text_field(data, idx){
        return Mustache.render(text_tpl, {
            field_id: "dynamic_" + data.type + "_" + idx,
            label: "Enter your opinion",
            field_name: data.type + "_" + idx
        });
    }

    return {
        text_field: text_tpl,
        get_field: generate_field
    }
}
)();
