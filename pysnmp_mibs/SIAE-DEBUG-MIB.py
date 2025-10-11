# SNMP MIB module (SIAE-DEBUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siaemic/SIAE-DEBUG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:13:06 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(AlarmSeverityCode,
 AlarmStatus,
 alarmTrap) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "AlarmSeverityCode",
    "AlarmStatus",
    "alarmTrap")

(equipIpSnmpAgentAddress,) = mibBuilder.importSymbols(
    "SIAE-EQUIP-MIB",
    "equipIpSnmpAgentAddress")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

debug = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41)
)
if mibBuilder.loadTexts:
    debug.setRevisions(
        ("2015-03-23 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _DebugMibVersion_Type(Integer32):
    """Custom type debugMibVersion based on Integer32"""
    defaultValue = 1


_DebugMibVersion_Type.__name__ = "Integer32"
_DebugMibVersion_Object = MibScalar
debugMibVersion = _DebugMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 1),
    _DebugMibVersion_Type()
)
debugMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugMibVersion.setStatus("current")
_DeviceTable_Object = MibTable
deviceTable = _DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 2)
)
if mibBuilder.loadTexts:
    deviceTable.setStatus("current")
_DeviceEntry_Object = MibTableRow
deviceEntry = _DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 2, 1)
)
deviceEntry.setIndexNames(
    (0, "SIAE-DEBUG-MIB", "deviceId"),
)
if mibBuilder.loadTexts:
    deviceEntry.setStatus("current")
_DeviceId_Type = Integer32
_DeviceId_Object = MibTableColumn
deviceId = _DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 2, 1, 1),
    _DeviceId_Type()
)
deviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceId.setStatus("current")


class _DeviceType_Type(Integer32):
    """Custom type deviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serial", 1),
          ("parallel", 2),
          ("delete", 3))
    )


_DeviceType_Type.__name__ = "Integer32"
_DeviceType_Object = MibTableColumn
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 2, 1, 2),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")


class _DeviceLabel_Type(DisplayString):
    """Custom type deviceLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DeviceLabel_Type.__name__ = "DisplayString"
_DeviceLabel_Object = MibTableColumn
deviceLabel = _DeviceLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 2, 1, 3),
    _DeviceLabel_Type()
)
deviceLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceLabel.setStatus("current")


class _DeviceStartAddressBase_Type(OctetString):
    """Custom type deviceStartAddressBase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DeviceStartAddressBase_Type.__name__ = "OctetString"
_DeviceStartAddressBase_Object = MibTableColumn
deviceStartAddressBase = _DeviceStartAddressBase_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 2, 1, 4),
    _DeviceStartAddressBase_Type()
)
deviceStartAddressBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceStartAddressBase.setStatus("current")


class _DeviceStartAddressOffset_Type(OctetString):
    """Custom type deviceStartAddressOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DeviceStartAddressOffset_Type.__name__ = "OctetString"
_DeviceStartAddressOffset_Object = MibTableColumn
deviceStartAddressOffset = _DeviceStartAddressOffset_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 2, 1, 5),
    _DeviceStartAddressOffset_Type()
)
deviceStartAddressOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceStartAddressOffset.setStatus("current")


class _DeviceEndAddressBase_Type(OctetString):
    """Custom type deviceEndAddressBase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DeviceEndAddressBase_Type.__name__ = "OctetString"
_DeviceEndAddressBase_Object = MibTableColumn
deviceEndAddressBase = _DeviceEndAddressBase_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 2, 1, 6),
    _DeviceEndAddressBase_Type()
)
deviceEndAddressBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceEndAddressBase.setStatus("current")


class _DeviceEndAddressOffset_Type(OctetString):
    """Custom type deviceEndAddressOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DeviceEndAddressOffset_Type.__name__ = "OctetString"
_DeviceEndAddressOffset_Object = MibTableColumn
deviceEndAddressOffset = _DeviceEndAddressOffset_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 2, 1, 7),
    _DeviceEndAddressOffset_Type()
)
deviceEndAddressOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceEndAddressOffset.setStatus("current")
_MemoryTable_Object = MibTable
memoryTable = _MemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3)
)
if mibBuilder.loadTexts:
    memoryTable.setStatus("current")
_MemoryEntry_Object = MibTableRow
memoryEntry = _MemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1)
)
memoryEntry.setIndexNames(
    (0, "SIAE-DEBUG-MIB", "memoryIdNumber"),
)
if mibBuilder.loadTexts:
    memoryEntry.setStatus("current")
_MemoryIdNumber_Type = Integer32
_MemoryIdNumber_Object = MibTableColumn
memoryIdNumber = _MemoryIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 1),
    _MemoryIdNumber_Type()
)
memoryIdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryIdNumber.setStatus("current")


class _MemoryAddressBase_Type(OctetString):
    """Custom type memoryAddressBase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_MemoryAddressBase_Type.__name__ = "OctetString"
_MemoryAddressBase_Object = MibTableColumn
memoryAddressBase = _MemoryAddressBase_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 2),
    _MemoryAddressBase_Type()
)
memoryAddressBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryAddressBase.setStatus("current")


class _MemoryAddressOffset_Type(OctetString):
    """Custom type memoryAddressOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_MemoryAddressOffset_Type.__name__ = "OctetString"
_MemoryAddressOffset_Object = MibTableColumn
memoryAddressOffset = _MemoryAddressOffset_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 3),
    _MemoryAddressOffset_Type()
)
memoryAddressOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryAddressOffset.setStatus("current")


class _MemoryValue_Type(Integer32):
    """Custom type memoryValue based on Integer32"""
    defaultValue = 0


_MemoryValue_Type.__name__ = "Integer32"
_MemoryValue_Object = MibTableColumn
memoryValue = _MemoryValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 4),
    _MemoryValue_Type()
)
memoryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryValue.setStatus("current")


class _MemoryDumpEnable_Type(Integer32):
    """Custom type memoryDumpEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("enableuntiltrigger", 3))
    )


_MemoryDumpEnable_Type.__name__ = "Integer32"
_MemoryDumpEnable_Object = MibTableColumn
memoryDumpEnable = _MemoryDumpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 5),
    _MemoryDumpEnable_Type()
)
memoryDumpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryDumpEnable.setStatus("current")


class _MemoryDumpSize_Type(Integer32):
    """Custom type memoryDumpSize based on Integer32"""
    defaultValue = 50


_MemoryDumpSize_Type.__name__ = "Integer32"
_MemoryDumpSize_Object = MibTableColumn
memoryDumpSize = _MemoryDumpSize_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 6),
    _MemoryDumpSize_Type()
)
memoryDumpSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryDumpSize.setStatus("current")


class _MemoryDump_Type(OctetString):
    """Custom type memoryDump based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32768, 32768),
    )
    fixed_length = 32768


_MemoryDump_Type.__name__ = "OctetString"
_MemoryDump_Object = MibTableColumn
memoryDump = _MemoryDump_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 7),
    _MemoryDump_Type()
)
memoryDump.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDump.setStatus("current")


class _TriggerMemoryAddressBase_Type(OctetString):
    """Custom type triggerMemoryAddressBase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_TriggerMemoryAddressBase_Type.__name__ = "OctetString"
_TriggerMemoryAddressBase_Object = MibTableColumn
triggerMemoryAddressBase = _TriggerMemoryAddressBase_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 8),
    _TriggerMemoryAddressBase_Type()
)
triggerMemoryAddressBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    triggerMemoryAddressBase.setStatus("current")


class _TriggerMemoryAddressOffset_Type(OctetString):
    """Custom type triggerMemoryAddressOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_TriggerMemoryAddressOffset_Type.__name__ = "OctetString"
_TriggerMemoryAddressOffset_Object = MibTableColumn
triggerMemoryAddressOffset = _TriggerMemoryAddressOffset_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 9),
    _TriggerMemoryAddressOffset_Type()
)
triggerMemoryAddressOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    triggerMemoryAddressOffset.setStatus("current")


class _TriggerMemoryValue_Type(Integer32):
    """Custom type triggerMemoryValue based on Integer32"""
    defaultValue = 0


_TriggerMemoryValue_Type.__name__ = "Integer32"
_TriggerMemoryValue_Object = MibTableColumn
triggerMemoryValue = _TriggerMemoryValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 10),
    _TriggerMemoryValue_Type()
)
triggerMemoryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    triggerMemoryValue.setStatus("current")


class _TriggerMemoryMask_Type(Integer32):
    """Custom type triggerMemoryMask based on Integer32"""
    defaultValue = 255


_TriggerMemoryMask_Type.__name__ = "Integer32"
_TriggerMemoryMask_Object = MibTableColumn
triggerMemoryMask = _TriggerMemoryMask_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 11),
    _TriggerMemoryMask_Type()
)
triggerMemoryMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    triggerMemoryMask.setStatus("current")


class _TriggerEnable_Type(Integer32):
    """Custom type triggerEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_TriggerEnable_Type.__name__ = "Integer32"
_TriggerEnable_Object = MibTableColumn
triggerEnable = _TriggerEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 12),
    _TriggerEnable_Type()
)
triggerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    triggerEnable.setStatus("current")
_TriggerAlarm_Type = AlarmStatus
_TriggerAlarm_Object = MibTableColumn
triggerAlarm = _TriggerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 3, 1, 13),
    _TriggerAlarm_Type()
)
triggerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerAlarm.setStatus("current")


class _TriggerAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type triggerAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_TriggerAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_TriggerAlarmSeverityCode_Object = MibScalar
triggerAlarmSeverityCode = _TriggerAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 4),
    _TriggerAlarmSeverityCode_Type()
)
triggerAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    triggerAlarmSeverityCode.setStatus("current")


class _UploadMemoryAddressBaseStart_Type(OctetString):
    """Custom type uploadMemoryAddressBaseStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_UploadMemoryAddressBaseStart_Type.__name__ = "OctetString"
_UploadMemoryAddressBaseStart_Object = MibScalar
uploadMemoryAddressBaseStart = _UploadMemoryAddressBaseStart_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 5),
    _UploadMemoryAddressBaseStart_Type()
)
uploadMemoryAddressBaseStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadMemoryAddressBaseStart.setStatus("current")


class _UploadMemoryAddressOffsetStart_Type(OctetString):
    """Custom type uploadMemoryAddressOffsetStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_UploadMemoryAddressOffsetStart_Type.__name__ = "OctetString"
_UploadMemoryAddressOffsetStart_Object = MibScalar
uploadMemoryAddressOffsetStart = _UploadMemoryAddressOffsetStart_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 6),
    _UploadMemoryAddressOffsetStart_Type()
)
uploadMemoryAddressOffsetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadMemoryAddressOffsetStart.setStatus("current")


class _UploadMemoryAddressBaseEnd_Type(OctetString):
    """Custom type uploadMemoryAddressBaseEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_UploadMemoryAddressBaseEnd_Type.__name__ = "OctetString"
_UploadMemoryAddressBaseEnd_Object = MibScalar
uploadMemoryAddressBaseEnd = _UploadMemoryAddressBaseEnd_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 7),
    _UploadMemoryAddressBaseEnd_Type()
)
uploadMemoryAddressBaseEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadMemoryAddressBaseEnd.setStatus("current")


class _UploadMemoryAddressOffsetEnd_Type(OctetString):
    """Custom type uploadMemoryAddressOffsetEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_UploadMemoryAddressOffsetEnd_Type.__name__ = "OctetString"
_UploadMemoryAddressOffsetEnd_Object = MibScalar
uploadMemoryAddressOffsetEnd = _UploadMemoryAddressOffsetEnd_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 8),
    _UploadMemoryAddressOffsetEnd_Type()
)
uploadMemoryAddressOffsetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadMemoryAddressOffsetEnd.setStatus("current")


class _UploadDownloadActionRequest_Type(Integer32):
    """Custom type uploadDownloadActionRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upload", 1),
          ("download", 2))
    )


_UploadDownloadActionRequest_Type.__name__ = "Integer32"
_UploadDownloadActionRequest_Object = MibScalar
uploadDownloadActionRequest = _UploadDownloadActionRequest_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 9),
    _UploadDownloadActionRequest_Type()
)
uploadDownloadActionRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadDownloadActionRequest.setStatus("current")


class _UploadDownloadFTPfile_Type(DisplayString):
    """Custom type uploadDownloadFTPfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UploadDownloadFTPfile_Type.__name__ = "DisplayString"
_UploadDownloadFTPfile_Object = MibScalar
uploadDownloadFTPfile = _UploadDownloadFTPfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 10),
    _UploadDownloadFTPfile_Type()
)
uploadDownloadFTPfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadDownloadFTPfile.setStatus("current")


class _UploadDownloadFTPStatus_Type(Integer32):
    """Custom type uploadDownloadFTPStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("transferring", 1),
          ("completed", 2),
          ("interrupted", 3),
          ("empty", 4))
    )


_UploadDownloadFTPStatus_Type.__name__ = "Integer32"
_UploadDownloadFTPStatus_Object = MibScalar
uploadDownloadFTPStatus = _UploadDownloadFTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 11),
    _UploadDownloadFTPStatus_Type()
)
uploadDownloadFTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uploadDownloadFTPStatus.setStatus("current")


class _UploadDownloadFTPStatusTrapNotification_Type(Integer32):
    """Custom type uploadDownloadFTPStatusTrapNotification based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              34)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 1),
          ("trapEnable", 2),
          ("trapEnableWithACK", 34))
    )


_UploadDownloadFTPStatusTrapNotification_Type.__name__ = "Integer32"
_UploadDownloadFTPStatusTrapNotification_Object = MibScalar
uploadDownloadFTPStatusTrapNotification = _UploadDownloadFTPStatusTrapNotification_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 12),
    _UploadDownloadFTPStatusTrapNotification_Type()
)
uploadDownloadFTPStatusTrapNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadDownloadFTPStatusTrapNotification.setStatus("current")


class _DebugEnable_Type(Integer32):
    """Custom type debugEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DebugEnable_Type.__name__ = "Integer32"
_DebugEnable_Object = MibScalar
debugEnable = _DebugEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 41, 13),
    _DebugEnable_Type()
)
debugEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugEnable.setStatus("current")

# Managed Objects groups


# Notification objects

uploadDownloadFTPStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 4103)
)
uploadDownloadFTPStatusTrap.setObjects(
      *(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-DEBUG-MIB", "uploadDownloadFTPStatus"))
)
if mibBuilder.loadTexts:
    uploadDownloadFTPStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-DEBUG-MIB",
    **{"uploadDownloadFTPStatusTrap": uploadDownloadFTPStatusTrap,
       "debug": debug,
       "debugMibVersion": debugMibVersion,
       "deviceTable": deviceTable,
       "deviceEntry": deviceEntry,
       "deviceId": deviceId,
       "deviceType": deviceType,
       "deviceLabel": deviceLabel,
       "deviceStartAddressBase": deviceStartAddressBase,
       "deviceStartAddressOffset": deviceStartAddressOffset,
       "deviceEndAddressBase": deviceEndAddressBase,
       "deviceEndAddressOffset": deviceEndAddressOffset,
       "memoryTable": memoryTable,
       "memoryEntry": memoryEntry,
       "memoryIdNumber": memoryIdNumber,
       "memoryAddressBase": memoryAddressBase,
       "memoryAddressOffset": memoryAddressOffset,
       "memoryValue": memoryValue,
       "memoryDumpEnable": memoryDumpEnable,
       "memoryDumpSize": memoryDumpSize,
       "memoryDump": memoryDump,
       "triggerMemoryAddressBase": triggerMemoryAddressBase,
       "triggerMemoryAddressOffset": triggerMemoryAddressOffset,
       "triggerMemoryValue": triggerMemoryValue,
       "triggerMemoryMask": triggerMemoryMask,
       "triggerEnable": triggerEnable,
       "triggerAlarm": triggerAlarm,
       "triggerAlarmSeverityCode": triggerAlarmSeverityCode,
       "uploadMemoryAddressBaseStart": uploadMemoryAddressBaseStart,
       "uploadMemoryAddressOffsetStart": uploadMemoryAddressOffsetStart,
       "uploadMemoryAddressBaseEnd": uploadMemoryAddressBaseEnd,
       "uploadMemoryAddressOffsetEnd": uploadMemoryAddressOffsetEnd,
       "uploadDownloadActionRequest": uploadDownloadActionRequest,
       "uploadDownloadFTPfile": uploadDownloadFTPfile,
       "uploadDownloadFTPStatus": uploadDownloadFTPStatus,
       "uploadDownloadFTPStatusTrapNotification": uploadDownloadFTPStatusTrapNotification,
       "debugEnable": debugEnable}
)
