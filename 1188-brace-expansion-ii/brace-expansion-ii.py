class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def parse_expr(i):
            result = set()

            while i < len(expression) and expression[i] != '}':
                term, i = parse_term(i)
                result |= term

                if i < len(expression) and expression[i] == ',':
                    i += 1

            return result, i

        def parse_term(i):
            result = {""}

            while i < len(expression) and expression[i] not in '},':
                factor, i = parse_factor(i)
                result = {a + b for a in result for b in factor}

            return result, i

        def parse_factor(i):
            if expression[i] == '{':
                result, i = parse_expr(i + 1)
                return result, i + 1

            return {expression[i]}, i + 1

        result, _ = parse_expr(0)
        return sorted(result)