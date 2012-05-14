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
            "!/metric/:slug": 'metric'
        },

        metric: function(slug){

            $('#chart, #y_axis').html("");
            $('#stat_name').html(slug);

            $.ajax({
                url: "/api/metric/" + slug,
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
                            renderer: 'area',
                            series: [ {
                                    data: data,
                                    color: 'rgba(96,170,255,0.5)',
                                    stroke: 'rgba(0,0,0,0.15)'
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
                }
            });



        }

    });


    var app = new AppView();
    var router = new WorkspaceRouter();


    Backbone.history.start();

});
