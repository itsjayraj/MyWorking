define(['module-singleton-ex'], function(dom){
    function CreateInput(type){
        var ele  = el.getInstance.create('input');
        ele.type = type;
    };


    var controls = {
        text: function(options){
            var ele = CreateInput("text");
            if(typeof options.value !== "undefined"){
                ele.value = options.value;
            }
            return ele;
        }
        checkbox: function(){
            var ele = CreateInput("checkbox");
            if(typeof options.checked !== "undefined"){
                ele.checked = options.checked;
            }
            return ele;
        }
    };

    return {
        create: function(options){
            var type = options.type ? options,type : undefined;

            if(!type || !controls[type]){
                throw new {
                    message: type + " is not supported."
                }
            }
            controls[type](options);
        }
    }
});