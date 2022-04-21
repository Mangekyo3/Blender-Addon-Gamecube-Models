from ..Node import Node

# Archive Header
class ArchiveHeader(Node):
    class_name = "Archive Header"
    fields = [
        ('file_size', 'uint'),
        ('data_size', 'uint'),
        ('relocations_count', 'uint'),
        ('public_nodes_count', 'uint'),
        ('external_nodes_count', 'uint')
    ]

    # Parse struct from binary file.
    @classmethod
    def fromBinary(cls, parser, address):
        return parser.parseStruct(cls, address, None, False)

    # Tells the builder how to write this node's data to the binary file.
    # Returns the offset the builder was at before it started writing its own data.
    def writeBinary(self, builder):
        return builder.writeStruct(self)

    # Make approximation HSD struct from blender data.
    @classmethod
    def fromBlender(cls, blender_obj):
        pass

    # Make approximation Blender object from HSD data.
    def toBlender(self, context):
        pass