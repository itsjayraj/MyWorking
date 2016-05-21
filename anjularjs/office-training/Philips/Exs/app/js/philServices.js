angular.module('philServices',[])
// --------------- CONTROLLER
.controller('mainCtrl',['$scope',function(scope) {
	scope.title = "Directives Title";
	scope.name = "Philips Innovation";
	scope.updateMe = function() {
		alert('Directive updated....');
	};
}])
// --------------- DIRECTIVES
// scopes test
.directive('lscopeDir', [function() {	// local scope
	return {
		restrict: 'AE',
		templateUrl: 'app/templates/scopeDirTmpl.html',
		link: function(scope, elm, attrs) {
			scope.update = function() {
				scope.name = 'Philips, Bangalore';
			};
		},
		scope: true
	};
}])
.directive('iscopeDir', [function() {	// isolated scope
	return {
		restrict: 'AE',
		templateUrl: 'app/templates/scopeDirTmpl.html',
		link: function(scope, elm, attrs) {
			scope.update = function() {
				scope.name = 'Philips, Bangalore';
				scope.done();
			};
		},
		scope: {
			title: '@ptitle',
			name: '=',
			done: '&'
		}
	};
}])
// transclude example
.directive('simpleDir',[function(){
	return {
		templateUrl: 'app/templates/dirTempl.html'
		,controller: ['$scope',function(scope) {
			scope.Title = 'Philips Innovation,Bangalore';
		}]
		,transclude: true
	};
}])
// custom validator
.directive('verifyId',[function() {
	return {
		require: 'ngModel',
		link: function(scope, elm, attrs, ctrl) {
			var ids = ['james','smith','john'];

			ctrl.$validators.verifyuser = function(modelV, viewV) {
				var status = false;
				if(ctrl.$isEmpty(modelV) || ids.indexOf(modelV) == -1) {
					status = true;
				}
				return status;
			};
		}
	};
}])
// <div my-list id="l1" dataSrc="Products" data-field="Name"></div>
.directive('myList',[function() { 
	return function (scope, ele, attribs) {
		var srcField = attribs.datasrc; //"Products"
		// create watcher to listen to source data change
		scope.$watch(srcField, function(newV, oldV) {
			generateUL(scope, ele, attribs);			
		}, true);
	};
	function generateUL(scope, ele, attrs) {
		var srcField = attrs.datasrc; //"Products"
		var data = scope.$eval(srcField, scope);		//scope[srcField];
		var field = attrs.datafield;	// "Name"
		ele.empty();
		if(angular.isDefined(data) && angular.isArray(data)) {
			var ul = angular.element('<ul>'); // create ul
			ul.addClass('list-group');
			angular.forEach(data, function(item) {
				var li = angular.element('<li>');
				li.addClass('list-group-item');
				li.text(scope.$eval(field, item));
				ul.append(li);
			});
			ele.append(ul);
		}
	}
}])
// --------------- FILTERS
.filter('flashDays',['$filter',function($filter) {
	return function(days, args) {	//link-function
		var output = '';
		if(days < 2)
			output = "Grab it fast!";
		else if(days < 5)
			output = "Pick it within " + days  + ' days!';
		else if ( days < args.days)
			output = args.msg;
		else
			output = "Available for only next " + days + ' days';

		// return output;
		return $filter('uppercase')(output);
	};
}]);

	// return {
	// 	restrict: 'A',
	// 	template: '<p>Directive output</p>', // or function(ele, attrs){}
	// 	templateUrl: '',
	// 	compile: function(ele, attrs){

	// 		return function(scope, ele, attrs){};
	// 	},
	// 	link: function(scope, ele, attrs, ctrls){
	// 	}
	// 	controller: [function(){}],
	// 	require: ['ngModel','ngSrc'],
	// 	scope: true - local scope or {} - isolated scope,
	// 	replace: true/false,
	// 	transclude: true
	// };
