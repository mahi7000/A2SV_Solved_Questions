class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_paths = []

        for path in paths:
            path = path.split()
            directory = path[0]
            for i in range(1, len(path)):
                file_paths.append(directory + "/" + path[i])

        content_path = defaultdict(list)

        for files in file_paths:
            path, content = files.split('(')

            content_path[content].append(path)

        duplicate_files = []
        for content in content_path:
            if len(content_path[content]) > 1:
                duplicate_files.append(content_path[content])

        return duplicate_files       
