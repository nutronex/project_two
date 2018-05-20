
$("left-side-sub-panel").hide() ;
    function toggle_main_panel(){
        $('#left-side-main-panel').hide();
        $('#left-side-sub-panel').show()
    };



var foo = new Vue({
         delimiters:['${', '}'],
        el:"#test",
        data:{name:"shit",
            show_bus_line:false,
            show_bus_stop:false,
            cbdata:"default",
            buslines:bus_lines,
            busstops:bus_stops,
        },
methods:{

    toggle_side:function(){ 
        $("#left-side-main-panel").show();
        $("#left-side-sub-panel").hide() ;
        this.show_bus_stop=this.show_bus_line=false },

    bus_line_callback:function(id){

        axios.get("/bus/"+id).then(function(x){
            foo.cbdata=x.data; 

            foo.show_bus_line=true;
            toggle_main_panel();
            m=new google.maps.Map(document.getElementById("gmap"), 
                                  {  center : new google.maps.LatLng(17.132582, 96.141762),zoom:12})

            current_feature = m.data.loadGeoJson('/getpath/'+id);
            }).catch(function(x){console.log(x)});
        },

    bus_stop_callback:function(name){
        axios.get("/bus_stop/"+name).then(function(x){
            foo.cbdata=x.data;
            foo.show_bus_stop=true;
            lat = foo.cbdata['lat'];
            lng = foo.cbdata['lng'];
            if(lat>90){ tmp =lat;lat=lng;lng=tmp}
              m=new google.maps.Map(document.getElementById("gmap"), 
                                  {  center : new google.maps.LatLng(lat, lng),zoom:15})
              var mk=new google.maps.Marker({
                  position:{lat,lng},
                  map:m,
                  title:foo.cbdata['name']})

            google.maps.event.addListener(mk,'click',function(){
                (new google.maps.InfoWindow({
                    content:"<b>"+foo.cbdata['name']+"</b><br>"
                    })).open(m,mk);
                })

            
            
            toggle_main_panel();
            }).catch(function(x){console.log(x)});
        }


}
        });
