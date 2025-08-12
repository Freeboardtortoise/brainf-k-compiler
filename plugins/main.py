class PluginManager:
    def __init__(self, plugin_arguments):
        # required
        self.memory = []
        self.pointer = []
        self.pc = []
        self.plugins = plugin_arguments
        
        # add custom initialisation
    def update(self, currentCommand):
        # add custom code here V
        
        # required V
        return currentCommand
