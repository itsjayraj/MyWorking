// mainMod.js
// Define angular module
angular.module('mainMod', ['ngMessages','ui-notification', 'philServices'])
// ------------------ CONTROLLERS
.controller('productsCtrl', 
function($scope, ProductsJSON, $rootScope) {
	$scope.Title = "Top Products";
	$scope.Products = JSON.parse(ProductsJSON);
	// event handler for Select button
	$scope.onSelect = function(product) {
		$rootScope.Product = product;
	};
})
.controller('tabsCtrl',function() { 
	// initial tab
	this.tab = 1;
	// set tab
	this.setTab = function(tabIdx) {
		this.tab = tabIdx;
	};
	// get tab
	this.isTab = function(tabIdx) {
		return ( this.tab === tabIdx );
	};
})
.controller('reviewsCtrl', ['$scope','$rootScope',
		'Notification', function(scope,rtScope,Notification){
		scope.Review = {};
		// event handler for form submission
		scope.save = function() {
			if(angular.isDefined(scope.Review.Rating) &&
						angular.isDefined(rtScope.Product)) {
					rtScope.Product.Reviews.push(scope.Review);
					scope.Review = {};
					Notification.success({message:'Review saved...',
									title:'Status...'});
			}
		};
}]);