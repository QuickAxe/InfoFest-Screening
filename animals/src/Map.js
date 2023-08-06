import React, { useRef, useEffect } from "react";
import { loadModules } from "esri-loader";





function Map() {
    const MapEl = useRef(null)
    useEffect(
        () => {
            let view;
            loadModules(["esri/views/MapView", "esri/WebMap", "esri/layers/GeoJSONLayer"], {
                css: true
            }).then(([MapView, WebMap, GeoJSONLayer]) => {
                const webmap = new WebMap({
                    basemap: 'streets-vector'
                })
                view = new MapView({
                    map: webmap,
                    center: [-1.08,53.95 ],
                    zoom: 10,
                    //use the refernce as the container
                    container: MapEl.current
                })
                // create a geojson layer from geojson feature collection
                
                

                const geojsonlayer = new GeoJSONLayer(
                       {url: 'https://opendata.arcgis.com/datasets/10c3ba27f60540bebc809d53234c70be_58.geojson' // harcoded geoJSON data
                    }
                    )

                webmap.add(geojsonlayer)
            })
            return () => {
                if (!!view) {
                    view.destroy()
                    view = null
                }
            }
        }
    )
    return (<div style={{ height: 800 }} ref={MapEl}></div>);

}
export default Map