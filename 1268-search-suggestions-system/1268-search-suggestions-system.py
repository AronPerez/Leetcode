class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # First we need to sort the products lexographically
        products.sort()
        ans = []
        
        # We want to see if the char in searchWord is at the same index in the product 
        for i, char in enumerate(searchWord):
            products = list(filter(lambda product: product[i] == char if len(product) > i else False, products))
            ans.append(products[:3])
            
        return ans
            
            
        