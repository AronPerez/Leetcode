class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        """
        {
            ()
        }

        """
        for s in strs:
            """
            sorted(s)
            ['a', 'e', 't']
            ['a', 'e', 't']
            ['a', 'n', 't']
            ['a', 'e', 't']
            ['a', 'n', 't']
            ['a', 'b', 't']

            -> (tuple(sorted(s)) -> ('a', 'e', 't')
            """
            ans[tuple(sorted(s))].append(s)
            
        """
        ('a', 'e', 't'): ['eat', 'tea', 'ate']
        ('a', 'n', 't'): ['tan', 'nat']
        ('a', 'b', 't'): ['bat']
        """
        return ans.values()
        