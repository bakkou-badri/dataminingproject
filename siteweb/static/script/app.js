'use strict';
angular
        .module('app', ['ngDragDrop'])
        .config(['$routeProvider', function($routeProvider){
                $routeProvider
                .when('/', {
                  templateUrl:'../static/draganddrop.html', 
                  controller: 'oneCtrl'}).otherwise({redirectTo:'/'});
        }])
        .controller('oneCtrl', ['$scope','$http','$timeout',function($scope,$http, $timeout) {
                console.log('app is ok');
                $scope.list1 = [];
                $scope.list2 = [];

                $scope.list5 = [
                    { 'title': 'Item 1', 'code_equipe' : '1', 'nom' : 'Lyon','img' : 'static/img/1.png','drag': true },
                    { 'title': 'Item 2', 'code_equipe' : '2', 'nom' : 'Marseille', 'img' : 'static/img/2.png', 'drag': true },
                    { 'title': 'Item 3', 'code_equipe' : '3', 'nom' : 'Rennes','img' : 'static/img/3.png', 'drag': true },
                    { 'title': 'Item 4', 'code_equipe' : '4', 'nom' : 'Lille','img' : 'static/img/4.png',  'drag': true },
                    { 'title': 'Item 5', 'code_equipe' : '5', 'nom' : 'Evian TG','img' : 'static/img/5.png',  'drag': true },
                    { 'title': 'Item 6', 'code_equipe' : '6', 'nom' : 'Montpellier', 'img' : 'static/img/6.png', 'drag': true },
                    { 'title': 'Item 7', 'code_equipe' : '7', 'nom' : 'Nantes','img' : 'static/img/7.png',  'drag': true },
                    { 'title': 'Item 8', 'code_equipe' : '8', 'nom' : 'Ajaccio', 'img' : 'static/img/8.png', 'drag': true },
                    { 'title': 'Item 9', 'code_equipe' : '9', 'nom' : 'Guingamp', 'img' : 'static/img/9.png', 'drag': true },
                    { 'title': 'Item 10', 'code_equipe' : '10', 'nom' : 'Toulouse','img' : 'static/img/10.png',  'drag': true },
                    { 'title': 'Item 11', 'code_equipe' : '11', 'nom' : 'Valenciennes','img' : 'static/img/11.png',  'drag': true },
                    { 'title': 'Item 12', 'code_equipe' : '12', 'nom' : 'St-Etienne','img' : 'static/img/12.png',  'drag': true },
                    { 'title': 'Item 13', 'code_equipe' : '13', 'nom' : 'Bastia', 'img' : 'static/img/13.png', 'drag': true },
                    { 'title': 'Item 14', 'code_equipe' : '14', 'nom' : 'Paris', 'img' : 'static/img/14.png', 'drag': true },
                    { 'title': 'Item 15', 'code_equipe' : '15', 'nom' : 'Sochaux','img' : 'static/img/15.png',  'drag': true },
                    { 'title': 'Item 16', 'code_equipe' : '16', 'nom' : 'Reims', 'img' : 'static/img/16.png', 'drag': true },
                    { 'title': 'Item 17', 'code_equipe' : '17', 'nom' : 'Lorient', 'img' : 'static/img/17.png', 'drag': true },
                    { 'title': 'Item 18', 'code_equipe' : '18', 'nom' : 'Nice', 'img' : 'static/img/18.png', 'drag': true },
                    { 'title': 'Item 19', 'code_equipe' : '19', 'nom' : 'Monaco', 'img' : 'static/img/19.png', 'drag': true },
                    { 'title': 'Item 20', 'code_equipe' : '20', 'nom' : 'Bordeaux', 'img' : 'static/img/20.png', 'drag': true }
                ];
                
                $scope.getPrediction = function(){
                  console.log("get function predection for list 1" + $scope.list1)
                  console.log("get function predection for list 2" + $scope.list2)
                  $http.get('/getPrediction?myParam1='+ JSON.stringify($scope.list1) + 
                            '&myParam2=' + JSON.stringify($scope.list2) ).success(
                                      function(data,status){
                                            console.log('call is ok ' + data);
                                            $scope.resu = [{'res':'50'},
                                                    {'res' : '70'}];
                                      });
                }
                
        }]);
