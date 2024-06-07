var federal = 
    /* color: #ffff99 */
    /* locked: true */
    ee.Geometry.Polygon(
        [[[73.09130716948162, 33.65402414817019],
          [73.18643106439058, 33.55815113085832],
          [73.10071594945155, 33.52165009636611],
          [73.2292077030608, 33.45079553499576],
          [73.33632440227954, 33.587040666289155],
          [73.29720997130939, 33.63589205884609],
          [73.37171668893433, 33.69060473640913],
          [73.34461772206117, 33.728170178670155],
          [73.22783441204517, 33.78586944621174],
          [73.1577901668699, 33.772211630833965],
          [73.10422043539987, 33.792766193030666],
          [73.00536126751392, 33.75847214031203],
          [72.88719599337328, 33.732793589031004],
          [72.8295134595399, 33.72449084584972],
          [72.8075526756964, 33.69789932223653],
          [72.90373773235768, 33.573311392766655]]]);

          Map.centerObject(federal, 6);

          //Time
          var start = ee.Date('2011-01-01');
          var dateRange = ee.DateRange(start, start.advance(11, 'year'));
          
          //TEMP
          var modis = ee.ImageCollection('MODIS/006/MOD11A1');
          var mod11a2 = modis.filterDate(dateRange);
          var modLSTday = mod11a2.select('LST_Day_1km');
          var modLSTc = modLSTday.map(function(img) {
            return img
              .multiply(0.02)
              .subtract(273.15)
              .copyProperties(img, ['system:time_start']);
          });
          var clippedLSTc = modLSTc.mean().clip(federal);
          //VEG
          var Veg = ee.ImageCollection('MODIS/006/MOD13A2').filterDate(dateRange);
          var ndvi = Veg.select('NDVI');
          var ndvi1= ndvi.mean().clip(federal);
          //Precipation
          var dataset =  ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY');
          var pre1 = dataset.filterDate(dateRange);
          var pre2 = pre1.select('precipitation');
          
          var pref1 = pre2.mean().clip(federal);
          var title1 = {
            title: ' Precipitation of federal',
            hAxis: {title: 'Time'},
            vAxis: {title: 'Precipitation (mm)'},
          };
          
          
          
          //Ice
          var dataset = ee.ImageCollection('MODIS/MOD09GA_006_NDSI');
          
          var ice1 = dataset.filterDate(dateRange);
          
          var ice2 = ice1.select('NDSI');
          
          var icef1 = ice2.mean().clip(federal);
          
          
          var title = {
            title: ' NDSI of federal',
            hAxis: {title: 'Time'},
            vAxis: {title: 'Ice precense'},
          };
          
          //Map layers
          var ndviVis = {"min":0,"max":9000,"palette":["FFFFFF","CE7E45","DF923D","F1B555","FCD163","99B718","74A901","66A000","529400","3E8601","207401","056201","004C00","023B01","012E01","011D01","011301"]};
          
          Map.addLayer(ndvi1, ndviVis, 'NDVI');
          Map.addLayer(clippedLSTc, {
            min: 20, max: 40,
            palette: ['blue', 'limegreen', 'yellow', 'darkorange', 'red']},
            'Mean temperature, 2021');
          var precipitationVis = {
            min: 1.0,
            max: 17.0,
            palette: ['001137', '0aab1e', 'e7eb05', 'ff4a2d', 'e90000'],
          };
          Map.addLayer(pref1, precipitationVis, 'Precipitation');
          
          var iceVis = {
            palette: ['000088', '0000FF', '8888FF', 'FFFFFF'],
          };
          Map.addLayer(icef1, iceVis, 'Ice');
          
          //Graphs
          var ts1 = ui.Chart.image.series({
            imageCollection: modLSTc,
            region: federal,
            reducer: ee.Reducer.mean(),
            scale: 1000,
            xProperty: 'system:time_start'})
            .setOptions({
               title: 'Temp of federal Time Series',
               vAxis: {title: 'LST Celsius'}});
          print(ts1);
          
          var ts2 = ui.Chart.image.series({
            imageCollection: ndvi,
            region: federal,
            reducer: ee.Reducer.mean(),
            xProperty: 'system:time_start'})
            .setOptions({
               title: 'Vegitation of federal Time Series',
               vAxis: {title: 'NDVI range'}});
          print(ts2);
          
          var chart = ui.Chart.image.series({
            imageCollection: ice2, 
            region: federal,
            reducer: ee.Reducer.mean(),
            scale: 500,
            xProperty: 'system:time_start'
          }).setOptions(title);
          
          print(chart);
          
          var chart1 = ui.Chart.image.series({
            imageCollection: pre2, 
            region: federal,
            reducer: ee.Reducer.mean(),
            scale: 2500,
            xProperty: 'system:time_start'
          }).setOptions(title1);
          
          print(chart1);
          
          
          
          