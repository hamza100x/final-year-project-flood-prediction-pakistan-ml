var Sindh = 
    /* color: #ff9999 */
    /* locked: true */
    ee.Geometry.Polygon(
        [[[69.36930566940416, 28.491271735833283],
          [68.47941309127916, 28.47195842642833],
          [68.34757715377916, 28.3463359106437],
          [68.12785059127916, 28.21088376360882],
          [67.84220606002916, 27.95887386849454],
          [67.44669824752916, 27.871502096599],
          [67.24894434127916, 27.64789865441828],
          [67.16105371627916, 27.375067747692672],
          [67.15006738815416, 26.856795208062252],
          [67.18302637252916, 26.50339897787297],
          [67.39176660690416, 26.208068833533147],
          [67.44669824752916, 25.823017465134107],
          [67.16105371627916, 25.397017986935314],
          [67.12809473190416, 25.23812034267632],
          [66.98527246627916, 25.03920590911963],
          [66.74357324752916, 24.979468485309294],
          [66.65568262252916, 24.85990659856756],
          [66.85343652877916, 24.84993787926005],
          [67.02921777877916, 24.790108702044094],
          [67.19401270065416, 24.610448167399934],
          [67.28190332565416, 24.420526166703684],
          [67.32584863815416, 24.250353244154304],
          [67.44669824752916, 24.03982500031995],
          [67.60050684127916, 23.87919042293869],
          [67.75431543502916, 23.81890093669589],
          [67.98502832565416, 23.748527794610634],
          [68.21574121627916, 23.68817767030865],
          [68.34757715377916, 23.98964820004025],
          [68.76505762252916, 23.969572000697074],
          [68.77604395065416, 24.29041448712888],
          [69.21054350907603, 24.261840527523468],
          [69.6670214863455, 24.292056581676597],
          [69.71403002286215, 24.216742897925894],
          [69.87081327525628, 24.181436366260744],
          [70.00562342358802, 24.19614369123337],
          [70.07460327137314, 24.29093981141138],
          [70.56141708098181, 24.466418133542536],
          [70.63472428470699, 24.204100054763565],
          [70.8177282272066, 24.302157509305587],
          [70.93492204158476, 24.37989590371818],
          [71.08151843342519, 24.428764003333672],
          [71.0744716593636, 24.677576404550244],
          [70.84043982818369, 25.147951066380926],
          [70.66641732292094, 25.42360166566876],
          [70.62370484096166, 25.699111132383642],
          [70.41165846802771, 25.65034336300033],
          [70.22145618335809, 25.759740585590844],
          [70.05181099656994, 26.06207345751372],
          [70.1535035219853, 26.1936301910018],
          [70.16049507599844, 26.387482471054657],
          [70.1014902865915, 26.541960098456148],
          [69.9993555879304, 26.57509017665521],
          [69.83124811223924, 26.588440729322624],
          [69.4506190063056, 26.83120223284854],
          [69.5704928853013, 27.163223493069317],
          [69.95672415471721, 27.54644972738804],
          [70.08453019526463, 27.71768632998689],
          [70.1595535018085, 27.881185710690666],
          [69.98282645814479, 27.989720403411862],
          [69.82215474802067, 28.31374404351952],
          [69.816603058706, 28.368010725946274],
          [69.73408392749116, 28.465760399532567],
          [69.60189753349103, 28.477599319727837],
          [69.57075317347648, 28.513450205058234],
          [69.51121756623884, 28.51929256412606]]]);

          Map.centerObject(Sindh, 6);

          //Time
          var start = ee.Date('2011-01-01');
          var dateRange = ee.DateRange(start, start.advance(10, 'year'));
          
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
          var clippedLSTc = modLSTc.mean().clip(Sindh);
          //VEG
          var Veg = ee.ImageCollection('MODIS/006/MOD13A2').filterDate(dateRange);
          var ndvi = Veg.select('NDVI');
          var ndvi1= ndvi.mean().clip(Sindh);
          //Precipation
          var dataset =  ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY');
          var pre1 = dataset.filterDate(dateRange);
          var pre2 = pre1.select('precipitation');
          
          var pref1 = pre2.mean().clip(Sindh);
          var title1 = {
            title: ' Precipitation of Sindh',
            hAxis: {title: 'Time'},
            vAxis: {title: 'Precipitation (mm)'},
          };
          
          
          
          //Ice
          var dataset = ee.ImageCollection('MODIS/MOD09GA_006_NDSI');
          
          var ice1 = dataset.filterDate(dateRange);
          
          var ice2 = ice1.select('NDSI');
          
          var icef1 = ice2.mean().clip(Sindh);
          
          
          var title = {
            title: ' NDSI of Sindh',
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
            min: 0.0,
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
            region: Sindh,
            reducer: ee.Reducer.mean(),
            scale: 1000,
            xProperty: 'system:time_start'})
            .setOptions({
               title: 'Temp of Sindh Time Series',
               vAxis: {title: 'LST Celsius'}});
          print(ts1);
          
          var ts2 = ui.Chart.image.series({
            imageCollection: ndvi,
            region: Sindh,
            reducer: ee.Reducer.mean(),
            xProperty: 'system:time_start'})
            .setOptions({
               title: 'Vegitation of Sindh Time Series',
               vAxis: {title: 'NDVI range'}});
          print(ts2);
          
          var chart = ui.Chart.image.series({
            imageCollection: ice2, 
            region: Sindh,
            reducer: ee.Reducer.mean(),
            scale: 500,
            xProperty: 'system:time_start'
          }).setOptions(title);
          
          print(chart);
          
          var chart1 = ui.Chart.image.series({
            imageCollection: pre2, 
            region: Sindh,
            reducer: ee.Reducer.mean(),
            scale: 2500,
            xProperty: 'system:time_start'
          }).setOptions(title1);
          
          print(chart1);
          
          