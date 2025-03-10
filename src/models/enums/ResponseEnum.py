from enum import Enum

class ResponseSignal(Enum):
  FILE_TYPE_NOT_SUPPORTED = "File Type Not Supported"
  FILE_SIZE_NOT_SUPPORTED = "File Size Not Supported"
  FILE_UPLOAD_SUCCESS = "Upload is Success"
  FILE_UPLOAD_FILED = "file upload filed"