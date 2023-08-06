import React, {useRef, useEffect} from "react";
import { loadModules } from "esri-loader";


function Map(){
    const MapEl= useRef(null)
    useEffect(
        ()=>{
            let view;
            loadModules (["esri/views/MapView","esri/WebMap"],{
                css:true
            }).then(([MapView, WebMap])=>{
                const webmap = new WebMap({
                    basemap: 'streets-relief-vector'
                })
                view = new MapView({
                    map:webmap,
                    center:[74,15], 
                    zoom:10,
                    //use the refernce as the container
                    container:MapEl.current
                })
            })
            return()=>{
                if(!!view){
                    view.destroy()
                    view=null
                }
            }
        }
    )
    return  (<div style={{height:800, width:1200}} ref={MapEl}></div>);
    
}
export default Map