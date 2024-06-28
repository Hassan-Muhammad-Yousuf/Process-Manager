class MemoryManager:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks

    def first_fit(self, memory_req):
        """ First-Fit memory allocation """
        for i, block in enumerate(self.memory_blocks):
            if block >= memory_req:
                self.memory_blocks[i] -= memory_req
                return True
        return False

    def best_fit(self, memory_req):
        """ Best-Fit memory allocation """
        best_fit_index = -1
        min_fragmentation = float('inf')
        for i, block in enumerate(self.memory_blocks):
            if block >= memory_req and block - memory_req < min_fragmentation:
                best_fit_index = i
                min_fragmentation = block - memory_req
        
        if best_fit_index != -1:
            self.memory_blocks[best_fit_index] -= memory_req
            return True
        return False

