describe('Specs for mainMod module',function(){
	// 1 . initialize environment
	beforeEach(module('mainMod'));

	describe('Specs for Controller:productsCtrl of mainMod', function(){
		// 2. initialize controller related dependencies
		var ctrl, scope, rootScope;
		beforeEach(inject(function($controller,$rootScope){
			rootScope = $rootScope;
			scope = $rootScope.$new();
			json = '[{"ID":123,"Name":"iPhone6","Price":59999}' +
				',{"ID":456,"Name":"Galaxy6","Price":56999}]';
			ctrl = $controller('productsCtrl', {
				$scope: scope, 
				ProductsJSON: json, 
				$rootScope: rootScope
			});
		}));
		// unit test methods
		it('Scope should be defined with Products collection', 
				function(){
					expect(scope.Products).toBeDefined();
				});
		it('Scope Products should contain 2 products', function() {
				expect(scope.Products.length).toBe(2);
		});
		it('on select the Product should be in rootScope', 
			function() {
				scope.onSelect(scope.Products[0]);
				expect(rootScope.Product.ID)
					.toBe(scope.Products[0].ID);
			});
	});
});