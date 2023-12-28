// Инициализация AngularJS приложения
var app = angular.module('myApp', ['ngRoute']); // Добавлен ngRoute для работы с маршрутами

// Добавление контроллера 'ShopController' к модулю 'myApp'
app.controller('ShopController', function($scope, $http) {
      // Получение данных о продуктах из бэкенда (предполагается, что у вас есть API для получения продуктов)
      $http.get('/shop').then(function(response) {
        // Установка полученных данных о продуктах в область видимости контроллера
        $scope.products = response.data;
      }, function(error) {
        console.error('Error fetching products:', error);
      });
});
