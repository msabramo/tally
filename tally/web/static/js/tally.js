$(function(){


    var Metric = Backbone.Model.extend({
        urlRoot: '/api/metric',

        parse: function(response){
            console.log(response);
            return response;
        }

    });


    var MetricCollection = Backbone.Collection.extend({
        url: '/api/metrics',

        parse: function(response){
            console.log(response);
            return response.data;
        }

    });


    var AppView = Backbone.View.extend({

        el: $("app")

    });


    var WorkspaceRouter = Backbone.Router.extend({

        routes: {
            "!/metric/record/:slug": 'metric',
            "!/metric/counter/:slug": 'metric'
        },

        counter: function(slug){
            return this.metric(slug, '/api/metric/counter/');
        },

        record: function(slug){
            return this.metric(slug, '/api/metric/record/');
        },

        metric: function(slugi, path){

            $('#chart, #y_axis').html("");
            $('#stat_name').html(slug);

            $.ajax({
                url: path + slug,
                success: function(response){

                    var data = [];

                    _.each(response.data, function(value){

                        data.push({
                            x: parseInt(value[0], 10),
                            y: parseInt(value[1], 10)
                        });

                    });

                    var graph = new Rickshaw.Graph( {
                            element: document.querySelector("#chart"),
                            width: 580,
                            height: 250,
                            renderer: 'stack',
                            series: [ {
                                    data: data,
                                    color: 'steelblue'
                            } ]
                    } );

                    var x_axis = new Rickshaw.Graph.Axis.Time( { graph: graph } );

                    var y_axis = new Rickshaw.Graph.Axis.Y( {
                            graph: graph,
                            orientation: 'left',
                            tickFormat: Rickshaw.Fixtures.Number.formatKMBT,
                            element: document.getElementById('y_axis')
                    });

                    graph.render();

                    var hoverDetail = new Rickshaw.Graph.HoverDetail({
                        graph: graph,
                        formatter: function(series, x, y) {
                            var date = '<span class="date">' + new Date(x * 1000).toUTCString() + '</span>';
                            var swatch = '<span class="detail_swatch" style="background-color: ' + series.color + '"></span>';
                            var content = swatch + series.name + ": " + parseInt(y, 10) + '<br>' + date;
                            return content;
                        }
                    });

                }
            });



        }

    });


    var app = new AppView();
    var router = new WorkspaceRouter();


    Backbone.history.start();

});
