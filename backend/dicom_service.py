from pynetdicom import AE
from pynetdicom.sop_class import Verification


def dicom_echo(
    pacs_ip: str,
    pacs_port: int,
    calling_ae: str,
    called_ae: str
):
    ae = AE(ae_title=calling_ae)

    ae.add_requested_context(Verification)

    association = ae.associate(
        pacs_ip,
        pacs_port,
        ae_title=called_ae
    )

    if not association.is_established:
        return {
            "success": False,
            "message": "DICOM association failed"
        }

    status = association.send_c_echo()

    association.release()

    if status and status.Status == 0x0000:
        return {
            "success": True,
            "message": "DICOM C-ECHO successful"
        }

    return {
        "success": False,
        "message": "C-ECHO failed"
    }
