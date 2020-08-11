from databay.record import Record
from databay.outlet import Outlet, metadata


class FileOutlet(Outlet):
    """
    Outlet that writes records to a file.
    """

    FILEPATH:metadata = 'FileOutlet.FILEPATH'
    """Filepath of the file to write to."""

    FILE_MODE:metadata = 'FileOutlet.FILE_MODE'
    """Write mode to use when writing into the file."""

    def __init__(self, default_filepath:str, default_file_mode:str='a'):
        """

        :param default_filepath: Filepath of the default file to write records to.
        :type default_filepath: str

        :param default_file_mode: Default write mode to use when writing into the file.
        :type default_file_mode: str
        """
        super().__init__()
        self.default_filepath = default_filepath
        self.default_file_mode = default_file_mode


    def push(self, records:[Record], update):
        """
        Writes records to a file.

        :type records: list[:any:`Record`]
        :param records: List of records generated by inlets. Each top-level element of this array corresponds to one inlet that successfully returned data. Note that inlets could return arrays too, making this a nested array.

        :type update: :any:`Update`
        :param update: Update object representing the particular Link transfer.
        """
        for record in records:
            filepath = record.metadata.get(self.FILEPATH, self.default_filepath)
            file_mode = record.metadata.get(self.FILE_MODE, self.default_file_mode)

            with open(filepath, file_mode) as f:
                f.write(str(record.payload)+'\n')