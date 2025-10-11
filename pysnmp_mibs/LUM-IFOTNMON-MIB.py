# SNMP MIB module (LUM-IFOTNMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFOTNMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:01 2025
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

(lumIfOtnMonMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfOtnMonMIB",
    "lumModules")

(DisplayStringWithNA,
 EnabledDisabledWithNA,
 FaultStatusWithNA,
 MgmtNameString,
 OtnAlarmMode,
 OtnDirectionWithNA,
 OtnTIMDetModeWithNA,
 OtnTypeWithNA,
 SignalStatusWithNA,
 TcmMode,
 TcmNumber,
 TruthValueWithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "DisplayStringWithNA",
    "EnabledDisabledWithNA",
    "FaultStatusWithNA",
    "MgmtNameString",
    "OtnAlarmMode",
    "OtnDirectionWithNA",
    "OtnTIMDetModeWithNA",
    "OtnTypeWithNA",
    "SignalStatusWithNA",
    "TcmMode",
    "TcmNumber",
    "TruthValueWithNA",
    "Unsigned32WithNA")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumIfOtnMonMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 55)
)
if mibBuilder.loadTexts:
    lumIfOtnMonMIBModule.setRevisions(
        ("2017-06-22 00:00",
         "2016-11-30 00:00",
         "2016-11-04 00:00",
         "2015-05-29 00:00",
         "2014-09-30 00:00",
         "2014-05-16 00:00",
         "2013-11-15 00:00",
         "2013-05-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfOtnMonConfs_ObjectIdentity = ObjectIdentity
lumIfOtnMonConfs = _LumIfOtnMonConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1)
)
_LumIfOtnMonGroups_ObjectIdentity = ObjectIdentity
lumIfOtnMonGroups = _LumIfOtnMonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 1)
)
_LumIfOtnMonCompl_ObjectIdentity = ObjectIdentity
lumIfOtnMonCompl = _LumIfOtnMonCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 2)
)
_LumIfOtnMonMIBObjects_ObjectIdentity = ObjectIdentity
lumIfOtnMonMIBObjects = _LumIfOtnMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2)
)
_IfOtnMonGeneral_ObjectIdentity = ObjectIdentity
ifOtnMonGeneral = _IfOtnMonGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1)
)
_IfOtnMonGeneralConfigLastChangeTime_Type = DateAndTime
_IfOtnMonGeneralConfigLastChangeTime_Object = MibScalar
ifOtnMonGeneralConfigLastChangeTime = _IfOtnMonGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 1),
    _IfOtnMonGeneralConfigLastChangeTime_Type()
)
ifOtnMonGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralConfigLastChangeTime.setStatus("current")
_IfOtnMonGeneralStateLastChangeTime_Type = DateAndTime
_IfOtnMonGeneralStateLastChangeTime_Object = MibScalar
ifOtnMonGeneralStateLastChangeTime = _IfOtnMonGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 2),
    _IfOtnMonGeneralStateLastChangeTime_Type()
)
ifOtnMonGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralStateLastChangeTime.setStatus("current")
_IfOtnMonGeneralIfOtnMonSmTableSize_Type = Unsigned32
_IfOtnMonGeneralIfOtnMonSmTableSize_Object = MibScalar
ifOtnMonGeneralIfOtnMonSmTableSize = _IfOtnMonGeneralIfOtnMonSmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 3),
    _IfOtnMonGeneralIfOtnMonSmTableSize_Type()
)
ifOtnMonGeneralIfOtnMonSmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralIfOtnMonSmTableSize.setStatus("current")
_IfOtnMonGeneralIfOtnMonSmConfigLastChangeTime_Type = DateAndTime
_IfOtnMonGeneralIfOtnMonSmConfigLastChangeTime_Object = MibScalar
ifOtnMonGeneralIfOtnMonSmConfigLastChangeTime = _IfOtnMonGeneralIfOtnMonSmConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 4),
    _IfOtnMonGeneralIfOtnMonSmConfigLastChangeTime_Type()
)
ifOtnMonGeneralIfOtnMonSmConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralIfOtnMonSmConfigLastChangeTime.setStatus("current")
_IfOtnMonGeneralIfOtnMonSmStateLastChangeTime_Type = DateAndTime
_IfOtnMonGeneralIfOtnMonSmStateLastChangeTime_Object = MibScalar
ifOtnMonGeneralIfOtnMonSmStateLastChangeTime = _IfOtnMonGeneralIfOtnMonSmStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 5),
    _IfOtnMonGeneralIfOtnMonSmStateLastChangeTime_Type()
)
ifOtnMonGeneralIfOtnMonSmStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralIfOtnMonSmStateLastChangeTime.setStatus("current")
_IfOtnMonGeneralIfOtnMonTcmTableSize_Type = Unsigned32
_IfOtnMonGeneralIfOtnMonTcmTableSize_Object = MibScalar
ifOtnMonGeneralIfOtnMonTcmTableSize = _IfOtnMonGeneralIfOtnMonTcmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 6),
    _IfOtnMonGeneralIfOtnMonTcmTableSize_Type()
)
ifOtnMonGeneralIfOtnMonTcmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralIfOtnMonTcmTableSize.setStatus("current")
_IfOtnMonGeneralIfOtnMonTcmConfigLastChangeTime_Type = DateAndTime
_IfOtnMonGeneralIfOtnMonTcmConfigLastChangeTime_Object = MibScalar
ifOtnMonGeneralIfOtnMonTcmConfigLastChangeTime = _IfOtnMonGeneralIfOtnMonTcmConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 7),
    _IfOtnMonGeneralIfOtnMonTcmConfigLastChangeTime_Type()
)
ifOtnMonGeneralIfOtnMonTcmConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralIfOtnMonTcmConfigLastChangeTime.setStatus("current")
_IfOtnMonGeneralIfOtnMonTcmStateLastChangeTime_Type = DateAndTime
_IfOtnMonGeneralIfOtnMonTcmStateLastChangeTime_Object = MibScalar
ifOtnMonGeneralIfOtnMonTcmStateLastChangeTime = _IfOtnMonGeneralIfOtnMonTcmStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 8),
    _IfOtnMonGeneralIfOtnMonTcmStateLastChangeTime_Type()
)
ifOtnMonGeneralIfOtnMonTcmStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralIfOtnMonTcmStateLastChangeTime.setStatus("current")
_IfOtnMonGeneralIfOtnMonPmTableSize_Type = Unsigned32
_IfOtnMonGeneralIfOtnMonPmTableSize_Object = MibScalar
ifOtnMonGeneralIfOtnMonPmTableSize = _IfOtnMonGeneralIfOtnMonPmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 9),
    _IfOtnMonGeneralIfOtnMonPmTableSize_Type()
)
ifOtnMonGeneralIfOtnMonPmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralIfOtnMonPmTableSize.setStatus("current")
_IfOtnMonGeneralIfOtnMonPmConfigLastChangeTime_Type = DateAndTime
_IfOtnMonGeneralIfOtnMonPmConfigLastChangeTime_Object = MibScalar
ifOtnMonGeneralIfOtnMonPmConfigLastChangeTime = _IfOtnMonGeneralIfOtnMonPmConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 10),
    _IfOtnMonGeneralIfOtnMonPmConfigLastChangeTime_Type()
)
ifOtnMonGeneralIfOtnMonPmConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralIfOtnMonPmConfigLastChangeTime.setStatus("current")
_IfOtnMonGeneralIfOtnMonPmStateLastChangeTime_Type = DateAndTime
_IfOtnMonGeneralIfOtnMonPmStateLastChangeTime_Object = MibScalar
ifOtnMonGeneralIfOtnMonPmStateLastChangeTime = _IfOtnMonGeneralIfOtnMonPmStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 11),
    _IfOtnMonGeneralIfOtnMonPmStateLastChangeTime_Type()
)
ifOtnMonGeneralIfOtnMonPmStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralIfOtnMonPmStateLastChangeTime.setStatus("current")
_IfOtnMonGeneralIfOtnMonTraceTableSize_Type = Unsigned32
_IfOtnMonGeneralIfOtnMonTraceTableSize_Object = MibScalar
ifOtnMonGeneralIfOtnMonTraceTableSize = _IfOtnMonGeneralIfOtnMonTraceTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 12),
    _IfOtnMonGeneralIfOtnMonTraceTableSize_Type()
)
ifOtnMonGeneralIfOtnMonTraceTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralIfOtnMonTraceTableSize.setStatus("current")
_IfOtnMonGeneralIfOtnMonTraceConfigLastChangeTime_Type = DateAndTime
_IfOtnMonGeneralIfOtnMonTraceConfigLastChangeTime_Object = MibScalar
ifOtnMonGeneralIfOtnMonTraceConfigLastChangeTime = _IfOtnMonGeneralIfOtnMonTraceConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 13),
    _IfOtnMonGeneralIfOtnMonTraceConfigLastChangeTime_Type()
)
ifOtnMonGeneralIfOtnMonTraceConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralIfOtnMonTraceConfigLastChangeTime.setStatus("current")
_IfOtnMonGeneralIfOtnMonTraceStateLastChangeTime_Type = DateAndTime
_IfOtnMonGeneralIfOtnMonTraceStateLastChangeTime_Object = MibScalar
ifOtnMonGeneralIfOtnMonTraceStateLastChangeTime = _IfOtnMonGeneralIfOtnMonTraceStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 1, 14),
    _IfOtnMonGeneralIfOtnMonTraceStateLastChangeTime_Type()
)
ifOtnMonGeneralIfOtnMonTraceStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonGeneralIfOtnMonTraceStateLastChangeTime.setStatus("current")
_IfOtnMonSmList_ObjectIdentity = ObjectIdentity
ifOtnMonSmList = _IfOtnMonSmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 2)
)
_IfOtnMonSmTable_Object = MibTable
ifOtnMonSmTable = _IfOtnMonSmTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifOtnMonSmTable.setStatus("current")
_IfOtnMonSmEntry_Object = MibTableRow
ifOtnMonSmEntry = _IfOtnMonSmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 2, 1, 1)
)
ifOtnMonSmEntry.setIndexNames(
    (0, "LUM-IFOTNMON-MIB", "ifOtnMonSmIndex"),
)
if mibBuilder.loadTexts:
    ifOtnMonSmEntry.setStatus("current")
_IfOtnMonSmIndex_Type = Unsigned32
_IfOtnMonSmIndex_Object = MibTableColumn
ifOtnMonSmIndex = _IfOtnMonSmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 2, 1, 1, 1),
    _IfOtnMonSmIndex_Type()
)
ifOtnMonSmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonSmIndex.setStatus("current")
_IfOtnMonSmName_Type = MgmtNameString
_IfOtnMonSmName_Object = MibTableColumn
ifOtnMonSmName = _IfOtnMonSmName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 2, 1, 1, 2),
    _IfOtnMonSmName_Type()
)
ifOtnMonSmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonSmName.setStatus("current")
_IfOtnMonSmConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfOtnMonSmConnIfBasicIfIndex_Object = MibTableColumn
ifOtnMonSmConnIfBasicIfIndex = _IfOtnMonSmConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 2, 1, 1, 3),
    _IfOtnMonSmConnIfBasicIfIndex_Type()
)
ifOtnMonSmConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonSmConnIfBasicIfIndex.setStatus("current")
_IfOtnMonSmTxSignalStatus_Type = SignalStatusWithNA
_IfOtnMonSmTxSignalStatus_Object = MibTableColumn
ifOtnMonSmTxSignalStatus = _IfOtnMonSmTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 2, 1, 1, 4),
    _IfOtnMonSmTxSignalStatus_Type()
)
ifOtnMonSmTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonSmTxSignalStatus.setStatus("current")
_IfOtnMonSmRxSignalStatus_Type = SignalStatusWithNA
_IfOtnMonSmRxSignalStatus_Object = MibTableColumn
ifOtnMonSmRxSignalStatus = _IfOtnMonSmRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 2, 1, 1, 5),
    _IfOtnMonSmRxSignalStatus_Type()
)
ifOtnMonSmRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonSmRxSignalStatus.setStatus("current")
_IfOtnMonSmBackwardDefectIndication_Type = FaultStatusWithNA
_IfOtnMonSmBackwardDefectIndication_Object = MibTableColumn
ifOtnMonSmBackwardDefectIndication = _IfOtnMonSmBackwardDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 2, 1, 1, 6),
    _IfOtnMonSmBackwardDefectIndication_Type()
)
ifOtnMonSmBackwardDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonSmBackwardDefectIndication.setStatus("current")
_IfOtnMonSmIncomingAlignmentError_Type = FaultStatusWithNA
_IfOtnMonSmIncomingAlignmentError_Object = MibTableColumn
ifOtnMonSmIncomingAlignmentError = _IfOtnMonSmIncomingAlignmentError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 2, 1, 1, 7),
    _IfOtnMonSmIncomingAlignmentError_Type()
)
ifOtnMonSmIncomingAlignmentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonSmIncomingAlignmentError.setStatus("current")
_IfOtnMonSmBackwardIncomingAlignmentError_Type = FaultStatusWithNA
_IfOtnMonSmBackwardIncomingAlignmentError_Object = MibTableColumn
ifOtnMonSmBackwardIncomingAlignmentError = _IfOtnMonSmBackwardIncomingAlignmentError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 2, 1, 1, 8),
    _IfOtnMonSmBackwardIncomingAlignmentError_Type()
)
ifOtnMonSmBackwardIncomingAlignmentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonSmBackwardIncomingAlignmentError.setStatus("current")
_IfOtnMonTcmList_ObjectIdentity = ObjectIdentity
ifOtnMonTcmList = _IfOtnMonTcmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3)
)
_IfOtnMonTcmTable_Object = MibTable
ifOtnMonTcmTable = _IfOtnMonTcmTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifOtnMonTcmTable.setStatus("current")
_IfOtnMonTcmEntry_Object = MibTableRow
ifOtnMonTcmEntry = _IfOtnMonTcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1)
)
ifOtnMonTcmEntry.setIndexNames(
    (0, "LUM-IFOTNMON-MIB", "ifOtnMonTcmIndex"),
)
if mibBuilder.loadTexts:
    ifOtnMonTcmEntry.setStatus("current")
_IfOtnMonTcmIndex_Type = Unsigned32
_IfOtnMonTcmIndex_Object = MibTableColumn
ifOtnMonTcmIndex = _IfOtnMonTcmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 1),
    _IfOtnMonTcmIndex_Type()
)
ifOtnMonTcmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmIndex.setStatus("current")
_IfOtnMonTcmName_Type = MgmtNameString
_IfOtnMonTcmName_Object = MibTableColumn
ifOtnMonTcmName = _IfOtnMonTcmName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 2),
    _IfOtnMonTcmName_Type()
)
ifOtnMonTcmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmName.setStatus("current")
_IfOtnMonTcmConnOduIndex_Type = Unsigned32WithNA
_IfOtnMonTcmConnOduIndex_Object = MibTableColumn
ifOtnMonTcmConnOduIndex = _IfOtnMonTcmConnOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 3),
    _IfOtnMonTcmConnOduIndex_Type()
)
ifOtnMonTcmConnOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmConnOduIndex.setStatus("current")


class _IfOtnMonTcmAlarmMode_Type(OtnAlarmMode):
    """Custom type ifOtnMonTcmAlarmMode based on OtnAlarmMode"""
    defaultValue = 0


_IfOtnMonTcmAlarmMode_Type.__name__ = "OtnAlarmMode"
_IfOtnMonTcmAlarmMode_Object = MibTableColumn
ifOtnMonTcmAlarmMode = _IfOtnMonTcmAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 4),
    _IfOtnMonTcmAlarmMode_Type()
)
ifOtnMonTcmAlarmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmAlarmMode.setStatus("current")


class _IfOtnMonTcmMode_Type(TcmMode):
    """Custom type ifOtnMonTcmMode based on TcmMode"""
    defaultValue = 1


_IfOtnMonTcmMode_Type.__name__ = "TcmMode"
_IfOtnMonTcmMode_Object = MibTableColumn
ifOtnMonTcmMode = _IfOtnMonTcmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 5),
    _IfOtnMonTcmMode_Type()
)
ifOtnMonTcmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmMode.setStatus("current")


class _IfOtnMonTcmTcmNumber_Type(TcmNumber):
    """Custom type ifOtnMonTcmTcmNumber based on TcmNumber"""
    defaultValue = 0


_IfOtnMonTcmTcmNumber_Type.__name__ = "TcmNumber"
_IfOtnMonTcmTcmNumber_Object = MibTableColumn
ifOtnMonTcmTcmNumber = _IfOtnMonTcmTcmNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 6),
    _IfOtnMonTcmTcmNumber_Type()
)
ifOtnMonTcmTcmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmTcmNumber.setStatus("current")
_IfOtnMonTcmTxSignalStatus_Type = SignalStatusWithNA
_IfOtnMonTcmTxSignalStatus_Object = MibTableColumn
ifOtnMonTcmTxSignalStatus = _IfOtnMonTcmTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 7),
    _IfOtnMonTcmTxSignalStatus_Type()
)
ifOtnMonTcmTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmTxSignalStatus.setStatus("current")
_IfOtnMonTcmRxSignalStatus_Type = SignalStatusWithNA
_IfOtnMonTcmRxSignalStatus_Object = MibTableColumn
ifOtnMonTcmRxSignalStatus = _IfOtnMonTcmRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 8),
    _IfOtnMonTcmRxSignalStatus_Type()
)
ifOtnMonTcmRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmRxSignalStatus.setStatus("current")
_IfOtnMonTcmBackwardDefectIndication_Type = FaultStatusWithNA
_IfOtnMonTcmBackwardDefectIndication_Object = MibTableColumn
ifOtnMonTcmBackwardDefectIndication = _IfOtnMonTcmBackwardDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 9),
    _IfOtnMonTcmBackwardDefectIndication_Type()
)
ifOtnMonTcmBackwardDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmBackwardDefectIndication.setStatus("current")
_IfOtnMonTcmBackwardIncomingAlignmentError_Type = FaultStatusWithNA
_IfOtnMonTcmBackwardIncomingAlignmentError_Object = MibTableColumn
ifOtnMonTcmBackwardIncomingAlignmentError = _IfOtnMonTcmBackwardIncomingAlignmentError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 10),
    _IfOtnMonTcmBackwardIncomingAlignmentError_Type()
)
ifOtnMonTcmBackwardIncomingAlignmentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmBackwardIncomingAlignmentError.setStatus("current")
_IfOtnMonTcmRxAlarmIndicationSignal_Type = FaultStatusWithNA
_IfOtnMonTcmRxAlarmIndicationSignal_Object = MibTableColumn
ifOtnMonTcmRxAlarmIndicationSignal = _IfOtnMonTcmRxAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 11),
    _IfOtnMonTcmRxAlarmIndicationSignal_Type()
)
ifOtnMonTcmRxAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmRxAlarmIndicationSignal.setStatus("current")
_IfOtnMonTcmRxOpenConnectionIndication_Type = FaultStatusWithNA
_IfOtnMonTcmRxOpenConnectionIndication_Object = MibTableColumn
ifOtnMonTcmRxOpenConnectionIndication = _IfOtnMonTcmRxOpenConnectionIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 12),
    _IfOtnMonTcmRxOpenConnectionIndication_Type()
)
ifOtnMonTcmRxOpenConnectionIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmRxOpenConnectionIndication.setStatus("current")
_IfOtnMonTcmRxLockedDefectIndication_Type = FaultStatusWithNA
_IfOtnMonTcmRxLockedDefectIndication_Object = MibTableColumn
ifOtnMonTcmRxLockedDefectIndication = _IfOtnMonTcmRxLockedDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 13),
    _IfOtnMonTcmRxLockedDefectIndication_Type()
)
ifOtnMonTcmRxLockedDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmRxLockedDefectIndication.setStatus("current")
_IfOtnMonTcmLossOfTandemConnection_Type = FaultStatusWithNA
_IfOtnMonTcmLossOfTandemConnection_Object = MibTableColumn
ifOtnMonTcmLossOfTandemConnection = _IfOtnMonTcmLossOfTandemConnection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 14),
    _IfOtnMonTcmLossOfTandemConnection_Type()
)
ifOtnMonTcmLossOfTandemConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmLossOfTandemConnection.setStatus("current")
_IfOtnMonTcmIncomingAlignmentError_Type = FaultStatusWithNA
_IfOtnMonTcmIncomingAlignmentError_Object = MibTableColumn
ifOtnMonTcmIncomingAlignmentError = _IfOtnMonTcmIncomingAlignmentError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 15),
    _IfOtnMonTcmIncomingAlignmentError_Type()
)
ifOtnMonTcmIncomingAlignmentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmIncomingAlignmentError.setStatus("current")


class _IfOtnMonTcmSwitchCriteria_Type(EnabledDisabledWithNA):
    """Custom type ifOtnMonTcmSwitchCriteria based on EnabledDisabledWithNA"""
    defaultValue = 1


_IfOtnMonTcmSwitchCriteria_Type.__name__ = "EnabledDisabledWithNA"
_IfOtnMonTcmSwitchCriteria_Object = MibTableColumn
ifOtnMonTcmSwitchCriteria = _IfOtnMonTcmSwitchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 3, 1, 1, 16),
    _IfOtnMonTcmSwitchCriteria_Type()
)
ifOtnMonTcmSwitchCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTcmSwitchCriteria.setStatus("current")
_IfOtnMonPmList_ObjectIdentity = ObjectIdentity
ifOtnMonPmList = _IfOtnMonPmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4)
)
_IfOtnMonPmTable_Object = MibTable
ifOtnMonPmTable = _IfOtnMonPmTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ifOtnMonPmTable.setStatus("current")
_IfOtnMonPmEntry_Object = MibTableRow
ifOtnMonPmEntry = _IfOtnMonPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1)
)
ifOtnMonPmEntry.setIndexNames(
    (0, "LUM-IFOTNMON-MIB", "ifOtnMonPmIndex"),
)
if mibBuilder.loadTexts:
    ifOtnMonPmEntry.setStatus("current")
_IfOtnMonPmIndex_Type = Unsigned32
_IfOtnMonPmIndex_Object = MibTableColumn
ifOtnMonPmIndex = _IfOtnMonPmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 1),
    _IfOtnMonPmIndex_Type()
)
ifOtnMonPmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmIndex.setStatus("current")
_IfOtnMonPmName_Type = MgmtNameString
_IfOtnMonPmName_Object = MibTableColumn
ifOtnMonPmName = _IfOtnMonPmName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 2),
    _IfOtnMonPmName_Type()
)
ifOtnMonPmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmName.setStatus("current")
_IfOtnMonPmConnOduIndex_Type = Unsigned32WithNA
_IfOtnMonPmConnOduIndex_Object = MibTableColumn
ifOtnMonPmConnOduIndex = _IfOtnMonPmConnOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 4),
    _IfOtnMonPmConnOduIndex_Type()
)
ifOtnMonPmConnOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmConnOduIndex.setStatus("current")


class _IfOtnMonPmAlarmMode_Type(OtnAlarmMode):
    """Custom type ifOtnMonPmAlarmMode based on OtnAlarmMode"""
    defaultValue = 1


_IfOtnMonPmAlarmMode_Type.__name__ = "OtnAlarmMode"
_IfOtnMonPmAlarmMode_Object = MibTableColumn
ifOtnMonPmAlarmMode = _IfOtnMonPmAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 5),
    _IfOtnMonPmAlarmMode_Type()
)
ifOtnMonPmAlarmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmAlarmMode.setStatus("current")
_IfOtnMonPmTxSignalStatus_Type = SignalStatusWithNA
_IfOtnMonPmTxSignalStatus_Object = MibTableColumn
ifOtnMonPmTxSignalStatus = _IfOtnMonPmTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 6),
    _IfOtnMonPmTxSignalStatus_Type()
)
ifOtnMonPmTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmTxSignalStatus.setStatus("current")
_IfOtnMonPmRxSignalStatus_Type = SignalStatusWithNA
_IfOtnMonPmRxSignalStatus_Object = MibTableColumn
ifOtnMonPmRxSignalStatus = _IfOtnMonPmRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 7),
    _IfOtnMonPmRxSignalStatus_Type()
)
ifOtnMonPmRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmRxSignalStatus.setStatus("current")
_IfOtnMonPmRxBackwardDefectIndication_Type = FaultStatusWithNA
_IfOtnMonPmRxBackwardDefectIndication_Object = MibTableColumn
ifOtnMonPmRxBackwardDefectIndication = _IfOtnMonPmRxBackwardDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 8),
    _IfOtnMonPmRxBackwardDefectIndication_Type()
)
ifOtnMonPmRxBackwardDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmRxBackwardDefectIndication.setStatus("current")
_IfOtnMonPmRxAlarmIndicationSignal_Type = FaultStatusWithNA
_IfOtnMonPmRxAlarmIndicationSignal_Object = MibTableColumn
ifOtnMonPmRxAlarmIndicationSignal = _IfOtnMonPmRxAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 9),
    _IfOtnMonPmRxAlarmIndicationSignal_Type()
)
ifOtnMonPmRxAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmRxAlarmIndicationSignal.setStatus("current")
_IfOtnMonPmRxOpenConnectionIndication_Type = FaultStatusWithNA
_IfOtnMonPmRxOpenConnectionIndication_Object = MibTableColumn
ifOtnMonPmRxOpenConnectionIndication = _IfOtnMonPmRxOpenConnectionIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 10),
    _IfOtnMonPmRxOpenConnectionIndication_Type()
)
ifOtnMonPmRxOpenConnectionIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmRxOpenConnectionIndication.setStatus("current")
_IfOtnMonPmRxLockedDefectIndication_Type = FaultStatusWithNA
_IfOtnMonPmRxLockedDefectIndication_Object = MibTableColumn
ifOtnMonPmRxLockedDefectIndication = _IfOtnMonPmRxLockedDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 11),
    _IfOtnMonPmRxLockedDefectIndication_Type()
)
ifOtnMonPmRxLockedDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmRxLockedDefectIndication.setStatus("current")
_IfOtnMonPmTxBackwardDefectIndication_Type = FaultStatusWithNA
_IfOtnMonPmTxBackwardDefectIndication_Object = MibTableColumn
ifOtnMonPmTxBackwardDefectIndication = _IfOtnMonPmTxBackwardDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 12),
    _IfOtnMonPmTxBackwardDefectIndication_Type()
)
ifOtnMonPmTxBackwardDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmTxBackwardDefectIndication.setStatus("current")
_IfOtnMonPmTxAlarmIndicationSignal_Type = FaultStatusWithNA
_IfOtnMonPmTxAlarmIndicationSignal_Object = MibTableColumn
ifOtnMonPmTxAlarmIndicationSignal = _IfOtnMonPmTxAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 13),
    _IfOtnMonPmTxAlarmIndicationSignal_Type()
)
ifOtnMonPmTxAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmTxAlarmIndicationSignal.setStatus("current")
_IfOtnMonPmTxOpenConnectionIndication_Type = FaultStatusWithNA
_IfOtnMonPmTxOpenConnectionIndication_Object = MibTableColumn
ifOtnMonPmTxOpenConnectionIndication = _IfOtnMonPmTxOpenConnectionIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 14),
    _IfOtnMonPmTxOpenConnectionIndication_Type()
)
ifOtnMonPmTxOpenConnectionIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmTxOpenConnectionIndication.setStatus("current")
_IfOtnMonPmTxLockedDefectIndication_Type = FaultStatusWithNA
_IfOtnMonPmTxLockedDefectIndication_Object = MibTableColumn
ifOtnMonPmTxLockedDefectIndication = _IfOtnMonPmTxLockedDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 15),
    _IfOtnMonPmTxLockedDefectIndication_Type()
)
ifOtnMonPmTxLockedDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmTxLockedDefectIndication.setStatus("current")


class _IfOtnMonPmUpPortId_Type(Integer32):
    """Custom type ifOtnMonPmUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_IfOtnMonPmUpPortId_Type.__name__ = "Integer32"
_IfOtnMonPmUpPortId_Object = MibTableColumn
ifOtnMonPmUpPortId = _IfOtnMonPmUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 4, 1, 1, 16),
    _IfOtnMonPmUpPortId_Type()
)
ifOtnMonPmUpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonPmUpPortId.setStatus("current")
_IfOtnMonTraceList_ObjectIdentity = ObjectIdentity
ifOtnMonTraceList = _IfOtnMonTraceList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5)
)
_IfOtnMonTraceTable_Object = MibTable
ifOtnMonTraceTable = _IfOtnMonTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ifOtnMonTraceTable.setStatus("current")
_IfOtnMonTraceEntry_Object = MibTableRow
ifOtnMonTraceEntry = _IfOtnMonTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1)
)
ifOtnMonTraceEntry.setIndexNames(
    (0, "LUM-IFOTNMON-MIB", "ifOtnMonTraceIndex"),
)
if mibBuilder.loadTexts:
    ifOtnMonTraceEntry.setStatus("current")
_IfOtnMonTraceIndex_Type = Unsigned32
_IfOtnMonTraceIndex_Object = MibTableColumn
ifOtnMonTraceIndex = _IfOtnMonTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 1),
    _IfOtnMonTraceIndex_Type()
)
ifOtnMonTraceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceIndex.setStatus("current")
_IfOtnMonTraceName_Type = MgmtNameString
_IfOtnMonTraceName_Object = MibTableColumn
ifOtnMonTraceName = _IfOtnMonTraceName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 2),
    _IfOtnMonTraceName_Type()
)
ifOtnMonTraceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOtnMonTraceName.setStatus("current")
_IfOtnMonTraceConnOtnType_Type = OtnTypeWithNA
_IfOtnMonTraceConnOtnType_Object = MibTableColumn
ifOtnMonTraceConnOtnType = _IfOtnMonTraceConnOtnType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 3),
    _IfOtnMonTraceConnOtnType_Type()
)
ifOtnMonTraceConnOtnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceConnOtnType.setStatus("current")
_IfOtnMonTraceConnOtnIndex_Type = Unsigned32WithNA
_IfOtnMonTraceConnOtnIndex_Object = MibTableColumn
ifOtnMonTraceConnOtnIndex = _IfOtnMonTraceConnOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 4),
    _IfOtnMonTraceConnOtnIndex_Type()
)
ifOtnMonTraceConnOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceConnOtnIndex.setStatus("current")


class _IfOtnMonTraceSapiTraceTransmitted_Type(DisplayStringWithNA):
    """Custom type ifOtnMonTraceSapiTraceTransmitted based on DisplayStringWithNA"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IfOtnMonTraceSapiTraceTransmitted_Type.__name__ = "DisplayStringWithNA"
_IfOtnMonTraceSapiTraceTransmitted_Object = MibTableColumn
ifOtnMonTraceSapiTraceTransmitted = _IfOtnMonTraceSapiTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 5),
    _IfOtnMonTraceSapiTraceTransmitted_Type()
)
ifOtnMonTraceSapiTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOtnMonTraceSapiTraceTransmitted.setStatus("current")
_IfOtnMonTraceSapiTraceReceivedByte0_Type = Unsigned32WithNA
_IfOtnMonTraceSapiTraceReceivedByte0_Object = MibTableColumn
ifOtnMonTraceSapiTraceReceivedByte0 = _IfOtnMonTraceSapiTraceReceivedByte0_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 6),
    _IfOtnMonTraceSapiTraceReceivedByte0_Type()
)
ifOtnMonTraceSapiTraceReceivedByte0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceSapiTraceReceivedByte0.setStatus("deprecated")


class _IfOtnMonTraceSapiTraceReceived_Type(DisplayStringWithNA):
    """Custom type ifOtnMonTraceSapiTraceReceived based on DisplayStringWithNA"""
    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IfOtnMonTraceSapiTraceReceived_Type.__name__ = "DisplayStringWithNA"
_IfOtnMonTraceSapiTraceReceived_Object = MibTableColumn
ifOtnMonTraceSapiTraceReceived = _IfOtnMonTraceSapiTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 7),
    _IfOtnMonTraceSapiTraceReceived_Type()
)
ifOtnMonTraceSapiTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceSapiTraceReceived.setStatus("current")


class _IfOtnMonTraceSapiTraceExpected_Type(DisplayStringWithNA):
    """Custom type ifOtnMonTraceSapiTraceExpected based on DisplayStringWithNA"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IfOtnMonTraceSapiTraceExpected_Type.__name__ = "DisplayStringWithNA"
_IfOtnMonTraceSapiTraceExpected_Object = MibTableColumn
ifOtnMonTraceSapiTraceExpected = _IfOtnMonTraceSapiTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 8),
    _IfOtnMonTraceSapiTraceExpected_Type()
)
ifOtnMonTraceSapiTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOtnMonTraceSapiTraceExpected.setStatus("current")


class _IfOtnMonTraceDapiTraceTransmitted_Type(DisplayStringWithNA):
    """Custom type ifOtnMonTraceDapiTraceTransmitted based on DisplayStringWithNA"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IfOtnMonTraceDapiTraceTransmitted_Type.__name__ = "DisplayStringWithNA"
_IfOtnMonTraceDapiTraceTransmitted_Object = MibTableColumn
ifOtnMonTraceDapiTraceTransmitted = _IfOtnMonTraceDapiTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 9),
    _IfOtnMonTraceDapiTraceTransmitted_Type()
)
ifOtnMonTraceDapiTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOtnMonTraceDapiTraceTransmitted.setStatus("current")
_IfOtnMonTraceDapiTraceReceivedByte0_Type = Unsigned32WithNA
_IfOtnMonTraceDapiTraceReceivedByte0_Object = MibTableColumn
ifOtnMonTraceDapiTraceReceivedByte0 = _IfOtnMonTraceDapiTraceReceivedByte0_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 10),
    _IfOtnMonTraceDapiTraceReceivedByte0_Type()
)
ifOtnMonTraceDapiTraceReceivedByte0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceDapiTraceReceivedByte0.setStatus("deprecated")


class _IfOtnMonTraceDapiTraceReceived_Type(DisplayStringWithNA):
    """Custom type ifOtnMonTraceDapiTraceReceived based on DisplayStringWithNA"""
    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IfOtnMonTraceDapiTraceReceived_Type.__name__ = "DisplayStringWithNA"
_IfOtnMonTraceDapiTraceReceived_Object = MibTableColumn
ifOtnMonTraceDapiTraceReceived = _IfOtnMonTraceDapiTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 11),
    _IfOtnMonTraceDapiTraceReceived_Type()
)
ifOtnMonTraceDapiTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceDapiTraceReceived.setStatus("current")


class _IfOtnMonTraceDapiTraceExpected_Type(DisplayStringWithNA):
    """Custom type ifOtnMonTraceDapiTraceExpected based on DisplayStringWithNA"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IfOtnMonTraceDapiTraceExpected_Type.__name__ = "DisplayStringWithNA"
_IfOtnMonTraceDapiTraceExpected_Object = MibTableColumn
ifOtnMonTraceDapiTraceExpected = _IfOtnMonTraceDapiTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 12),
    _IfOtnMonTraceDapiTraceExpected_Type()
)
ifOtnMonTraceDapiTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOtnMonTraceDapiTraceExpected.setStatus("current")


class _IfOtnMonTraceOpSpecificTraceTransmitted_Type(DisplayStringWithNA):
    """Custom type ifOtnMonTraceOpSpecificTraceTransmitted based on DisplayStringWithNA"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IfOtnMonTraceOpSpecificTraceTransmitted_Type.__name__ = "DisplayStringWithNA"
_IfOtnMonTraceOpSpecificTraceTransmitted_Object = MibTableColumn
ifOtnMonTraceOpSpecificTraceTransmitted = _IfOtnMonTraceOpSpecificTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 13),
    _IfOtnMonTraceOpSpecificTraceTransmitted_Type()
)
ifOtnMonTraceOpSpecificTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOtnMonTraceOpSpecificTraceTransmitted.setStatus("current")


class _IfOtnMonTraceOpSpecificTraceReceived_Type(DisplayStringWithNA):
    """Custom type ifOtnMonTraceOpSpecificTraceReceived based on DisplayStringWithNA"""
    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IfOtnMonTraceOpSpecificTraceReceived_Type.__name__ = "DisplayStringWithNA"
_IfOtnMonTraceOpSpecificTraceReceived_Object = MibTableColumn
ifOtnMonTraceOpSpecificTraceReceived = _IfOtnMonTraceOpSpecificTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 14),
    _IfOtnMonTraceOpSpecificTraceReceived_Type()
)
ifOtnMonTraceOpSpecificTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceOpSpecificTraceReceived.setStatus("current")


class _IfOtnMonTraceTraceIdMMDetectionMode_Type(OtnTIMDetModeWithNA):
    """Custom type ifOtnMonTraceTraceIdMMDetectionMode based on OtnTIMDetModeWithNA"""
    defaultValue = 0


_IfOtnMonTraceTraceIdMMDetectionMode_Type.__name__ = "OtnTIMDetModeWithNA"
_IfOtnMonTraceTraceIdMMDetectionMode_Object = MibTableColumn
ifOtnMonTraceTraceIdMMDetectionMode = _IfOtnMonTraceTraceIdMMDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 15),
    _IfOtnMonTraceTraceIdMMDetectionMode_Type()
)
ifOtnMonTraceTraceIdMMDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOtnMonTraceTraceIdMMDetectionMode.setStatus("current")


class _IfOtnMonTraceTraceAlarmMode_Type(EnabledDisabledWithNA):
    """Custom type ifOtnMonTraceTraceAlarmMode based on EnabledDisabledWithNA"""
    defaultValue = 1


_IfOtnMonTraceTraceAlarmMode_Type.__name__ = "EnabledDisabledWithNA"
_IfOtnMonTraceTraceAlarmMode_Object = MibTableColumn
ifOtnMonTraceTraceAlarmMode = _IfOtnMonTraceTraceAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 16),
    _IfOtnMonTraceTraceAlarmMode_Type()
)
ifOtnMonTraceTraceAlarmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceTraceAlarmMode.setStatus("deprecated")


class _IfOtnMonTraceTIMConsequenceActionsDisabled_Type(TruthValueWithNA):
    """Custom type ifOtnMonTraceTIMConsequenceActionsDisabled based on TruthValueWithNA"""
    defaultValue = 0


_IfOtnMonTraceTIMConsequenceActionsDisabled_Type.__name__ = "TruthValueWithNA"
_IfOtnMonTraceTIMConsequenceActionsDisabled_Object = MibTableColumn
ifOtnMonTraceTIMConsequenceActionsDisabled = _IfOtnMonTraceTIMConsequenceActionsDisabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 17),
    _IfOtnMonTraceTIMConsequenceActionsDisabled_Type()
)
ifOtnMonTraceTIMConsequenceActionsDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceTIMConsequenceActionsDisabled.setStatus("current")
_IfOtnMonTraceTxSignalStatus_Type = SignalStatusWithNA
_IfOtnMonTraceTxSignalStatus_Object = MibTableColumn
ifOtnMonTraceTxSignalStatus = _IfOtnMonTraceTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 18),
    _IfOtnMonTraceTxSignalStatus_Type()
)
ifOtnMonTraceTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceTxSignalStatus.setStatus("current")
_IfOtnMonTraceRxSignalStatus_Type = SignalStatusWithNA
_IfOtnMonTraceRxSignalStatus_Object = MibTableColumn
ifOtnMonTraceRxSignalStatus = _IfOtnMonTraceRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 19),
    _IfOtnMonTraceRxSignalStatus_Type()
)
ifOtnMonTraceRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceRxSignalStatus.setStatus("current")
_IfOtnMonTraceTraceMismatch_Type = FaultStatusWithNA
_IfOtnMonTraceTraceMismatch_Object = MibTableColumn
ifOtnMonTraceTraceMismatch = _IfOtnMonTraceTraceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 20),
    _IfOtnMonTraceTraceMismatch_Type()
)
ifOtnMonTraceTraceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceTraceMismatch.setStatus("current")
_IfOtnMonTraceConnOtnDirection_Type = OtnDirectionWithNA
_IfOtnMonTraceConnOtnDirection_Object = MibTableColumn
ifOtnMonTraceConnOtnDirection = _IfOtnMonTraceConnOtnDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 21),
    _IfOtnMonTraceConnOtnDirection_Type()
)
ifOtnMonTraceConnOtnDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceConnOtnDirection.setStatus("current")


class _IfOtnMonTraceUpPortId_Type(Integer32):
    """Custom type ifOtnMonTraceUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_IfOtnMonTraceUpPortId_Type.__name__ = "Integer32"
_IfOtnMonTraceUpPortId_Object = MibTableColumn
ifOtnMonTraceUpPortId = _IfOtnMonTraceUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 2, 5, 1, 1, 22),
    _IfOtnMonTraceUpPortId_Type()
)
ifOtnMonTraceUpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnMonTraceUpPortId.setStatus("current")

# Managed Objects groups

ifOtnMonGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 1, 1)
)
ifOtnMonGeneralGroupV1.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonGeneralConfigLastChangeTime"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralStateLastChangeTime"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralIfOtnMonSmTableSize"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralIfOtnMonSmConfigLastChangeTime"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralIfOtnMonSmStateLastChangeTime"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralIfOtnMonTcmTableSize"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralIfOtnMonTcmConfigLastChangeTime"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralIfOtnMonTcmStateLastChangeTime"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralIfOtnMonPmTableSize"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralIfOtnMonPmConfigLastChangeTime"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralIfOtnMonPmStateLastChangeTime"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralIfOtnMonTraceTableSize"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralIfOtnMonTraceConfigLastChangeTime"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonGeneralIfOtnMonTraceStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifOtnMonGeneralGroupV1.setStatus("current")

ifOtnMonSmGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 1, 2)
)
ifOtnMonSmGroupV1.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonSmIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonSmName"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonSmConnIfBasicIfIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonSmTxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonSmRxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonSmBackwardDefectIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonSmIncomingAlignmentError"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonSmBackwardIncomingAlignmentError"))
)
if mibBuilder.loadTexts:
    ifOtnMonSmGroupV1.setStatus("current")

ifOtnMonTcmGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 1, 3)
)
ifOtnMonTcmGroupV1.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonTcmIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmName"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmConnOduIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmAlarmMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmTcmNumber"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmTxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmRxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmBackwardDefectIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmBackwardIncomingAlignmentError"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmRxAlarmIndicationSignal"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmRxOpenConnectionIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmRxLockedDefectIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmLossOfTandemConnection"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmIncomingAlignmentError"))
)
if mibBuilder.loadTexts:
    ifOtnMonTcmGroupV1.setStatus("deprecated")

ifOtnMonPmGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 1, 4)
)
ifOtnMonPmGroupV1.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonPmIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmName"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmConnOduIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmAlarmMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmTxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxBackwardDefectIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxAlarmIndicationSignal"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxOpenConnectionIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxLockedDefectIndication"))
)
if mibBuilder.loadTexts:
    ifOtnMonPmGroupV1.setStatus("deprecated")

ifOtnMonTraceGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 1, 5)
)
ifOtnMonTraceGroupV1.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonTraceIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceName"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceConnOtnIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceConnOtnType"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceTransmitted"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceReceivedByte0"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceReceived"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceExpected"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceTransmitted"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceReceivedByte0"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceReceived"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceExpected"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceOpSpecificTraceTransmitted"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceOpSpecificTraceReceived"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTraceIdMMDetectionMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTraceAlarmMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTIMConsequenceActionsDisabled"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceRxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTraceMismatch"))
)
if mibBuilder.loadTexts:
    ifOtnMonTraceGroupV1.setStatus("deprecated")

ifOtnMonPmGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 1, 6)
)
ifOtnMonPmGroupV2.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonPmIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmName"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmConnOduIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmAlarmMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmTxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxBackwardDefectIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxAlarmIndicationSignal"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxOpenConnectionIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmTxBackwardDefectIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmTxAlarmIndicationSignal"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmTxOpenConnectionIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmTxLockedDefectIndication"))
)
if mibBuilder.loadTexts:
    ifOtnMonPmGroupV2.setStatus("deprecated")

ifOtnMonTcmGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 1, 7)
)
ifOtnMonTcmGroupV2.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonTcmIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmName"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmConnOduIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmAlarmMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmTcmNumber"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmTxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmRxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmBackwardDefectIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmBackwardIncomingAlignmentError"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmRxAlarmIndicationSignal"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmRxOpenConnectionIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmRxLockedDefectIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmLossOfTandemConnection"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmIncomingAlignmentError"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmSwitchCriteria"))
)
if mibBuilder.loadTexts:
    ifOtnMonTcmGroupV2.setStatus("current")

ifOtnMonTraceGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 1, 8)
)
ifOtnMonTraceGroupV2.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonTraceIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceName"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceConnOtnType"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceConnOtnIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceTransmitted"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceReceivedByte0"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceReceived"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceExpected"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceTransmitted"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceReceivedByte0"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceReceived"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceExpected"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceOpSpecificTraceTransmitted"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceOpSpecificTraceReceived"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTraceIdMMDetectionMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTraceAlarmMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTIMConsequenceActionsDisabled"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceRxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTraceMismatch"))
)
if mibBuilder.loadTexts:
    ifOtnMonTraceGroupV2.setStatus("deprecated")

ifOtnMonTraceGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 1, 9)
)
ifOtnMonTraceGroupV3.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonTraceIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceName"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceConnOtnType"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceConnOtnIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceTransmitted"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceReceivedByte0"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceReceived"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceExpected"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceTransmitted"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceReceivedByte0"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceReceived"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceExpected"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceOpSpecificTraceTransmitted"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceOpSpecificTraceReceived"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTraceIdMMDetectionMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTraceAlarmMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTIMConsequenceActionsDisabled"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceRxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTraceMismatch"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceConnOtnDirection"))
)
if mibBuilder.loadTexts:
    ifOtnMonTraceGroupV3.setStatus("deprecated")

ifOtnMonPmGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 1, 10)
)
ifOtnMonPmGroupV3.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonPmIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmName"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmConnOduIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmAlarmMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmTxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxBackwardDefectIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxAlarmIndicationSignal"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmRxOpenConnectionIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmTxBackwardDefectIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmTxAlarmIndicationSignal"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmTxOpenConnectionIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmTxLockedDefectIndication"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmUpPortId"))
)
if mibBuilder.loadTexts:
    ifOtnMonPmGroupV3.setStatus("current")

ifOtnMonTraceGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 1, 11)
)
ifOtnMonTraceGroupV4.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonTraceIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceName"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceConnOtnType"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceConnOtnIndex"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceTransmitted"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceReceivedByte0"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceReceived"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceSapiTraceExpected"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceTransmitted"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceReceivedByte0"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceReceived"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceDapiTraceExpected"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceOpSpecificTraceTransmitted"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceOpSpecificTraceReceived"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTraceIdMMDetectionMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTraceAlarmMode"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTIMConsequenceActionsDisabled"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceRxSignalStatus"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceTraceMismatch"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceConnOtnDirection"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceUpPortId"))
)
if mibBuilder.loadTexts:
    ifOtnMonTraceGroupV4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfOtnMonComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 2, 1)
)
lumIfOtnMonComplV1.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonGeneralGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonSmGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfOtnMonComplV1.setStatus(
        "deprecated"
    )

lumIfOtnMonComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 2, 2)
)
lumIfOtnMonComplV2.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonGeneralGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonSmGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmGroupV2"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfOtnMonComplV2.setStatus(
        "deprecated"
    )

lumIfOtnMonComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 2, 3)
)
lumIfOtnMonComplV3.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonGeneralGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonSmGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmGroupV2"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmGroupV2"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfOtnMonComplV3.setStatus(
        "deprecated"
    )

lumIfOtnMonComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 2, 4)
)
lumIfOtnMonComplV4.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonGeneralGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonSmGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmGroupV2"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmGroupV2"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfOtnMonComplV4.setStatus(
        "deprecated"
    )

lumIfOtnMonComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55, 1, 2, 5)
)
lumIfOtnMonComplV5.setObjects(
      *(("LUM-IFOTNMON-MIB", "ifOtnMonGeneralGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonSmGroupV1"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTcmGroupV2"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonPmGroupV3"),
        ("LUM-IFOTNMON-MIB", "ifOtnMonTraceGroupV4"))
)
if mibBuilder.loadTexts:
    lumIfOtnMonComplV5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFOTNMON-MIB",
    **{"lumIfOtnMonMIBModule": lumIfOtnMonMIBModule,
       "lumIfOtnMonConfs": lumIfOtnMonConfs,
       "lumIfOtnMonGroups": lumIfOtnMonGroups,
       "ifOtnMonGeneralGroupV1": ifOtnMonGeneralGroupV1,
       "ifOtnMonSmGroupV1": ifOtnMonSmGroupV1,
       "ifOtnMonTcmGroupV1": ifOtnMonTcmGroupV1,
       "ifOtnMonPmGroupV1": ifOtnMonPmGroupV1,
       "ifOtnMonTraceGroupV1": ifOtnMonTraceGroupV1,
       "ifOtnMonPmGroupV2": ifOtnMonPmGroupV2,
       "ifOtnMonTcmGroupV2": ifOtnMonTcmGroupV2,
       "ifOtnMonTraceGroupV2": ifOtnMonTraceGroupV2,
       "ifOtnMonTraceGroupV3": ifOtnMonTraceGroupV3,
       "ifOtnMonPmGroupV3": ifOtnMonPmGroupV3,
       "ifOtnMonTraceGroupV4": ifOtnMonTraceGroupV4,
       "lumIfOtnMonCompl": lumIfOtnMonCompl,
       "lumIfOtnMonComplV1": lumIfOtnMonComplV1,
       "lumIfOtnMonComplV2": lumIfOtnMonComplV2,
       "lumIfOtnMonComplV3": lumIfOtnMonComplV3,
       "lumIfOtnMonComplV4": lumIfOtnMonComplV4,
       "lumIfOtnMonComplV5": lumIfOtnMonComplV5,
       "lumIfOtnMonMIBObjects": lumIfOtnMonMIBObjects,
       "ifOtnMonGeneral": ifOtnMonGeneral,
       "ifOtnMonGeneralConfigLastChangeTime": ifOtnMonGeneralConfigLastChangeTime,
       "ifOtnMonGeneralStateLastChangeTime": ifOtnMonGeneralStateLastChangeTime,
       "ifOtnMonGeneralIfOtnMonSmTableSize": ifOtnMonGeneralIfOtnMonSmTableSize,
       "ifOtnMonGeneralIfOtnMonSmConfigLastChangeTime": ifOtnMonGeneralIfOtnMonSmConfigLastChangeTime,
       "ifOtnMonGeneralIfOtnMonSmStateLastChangeTime": ifOtnMonGeneralIfOtnMonSmStateLastChangeTime,
       "ifOtnMonGeneralIfOtnMonTcmTableSize": ifOtnMonGeneralIfOtnMonTcmTableSize,
       "ifOtnMonGeneralIfOtnMonTcmConfigLastChangeTime": ifOtnMonGeneralIfOtnMonTcmConfigLastChangeTime,
       "ifOtnMonGeneralIfOtnMonTcmStateLastChangeTime": ifOtnMonGeneralIfOtnMonTcmStateLastChangeTime,
       "ifOtnMonGeneralIfOtnMonPmTableSize": ifOtnMonGeneralIfOtnMonPmTableSize,
       "ifOtnMonGeneralIfOtnMonPmConfigLastChangeTime": ifOtnMonGeneralIfOtnMonPmConfigLastChangeTime,
       "ifOtnMonGeneralIfOtnMonPmStateLastChangeTime": ifOtnMonGeneralIfOtnMonPmStateLastChangeTime,
       "ifOtnMonGeneralIfOtnMonTraceTableSize": ifOtnMonGeneralIfOtnMonTraceTableSize,
       "ifOtnMonGeneralIfOtnMonTraceConfigLastChangeTime": ifOtnMonGeneralIfOtnMonTraceConfigLastChangeTime,
       "ifOtnMonGeneralIfOtnMonTraceStateLastChangeTime": ifOtnMonGeneralIfOtnMonTraceStateLastChangeTime,
       "ifOtnMonSmList": ifOtnMonSmList,
       "ifOtnMonSmTable": ifOtnMonSmTable,
       "ifOtnMonSmEntry": ifOtnMonSmEntry,
       "ifOtnMonSmIndex": ifOtnMonSmIndex,
       "ifOtnMonSmName": ifOtnMonSmName,
       "ifOtnMonSmConnIfBasicIfIndex": ifOtnMonSmConnIfBasicIfIndex,
       "ifOtnMonSmTxSignalStatus": ifOtnMonSmTxSignalStatus,
       "ifOtnMonSmRxSignalStatus": ifOtnMonSmRxSignalStatus,
       "ifOtnMonSmBackwardDefectIndication": ifOtnMonSmBackwardDefectIndication,
       "ifOtnMonSmIncomingAlignmentError": ifOtnMonSmIncomingAlignmentError,
       "ifOtnMonSmBackwardIncomingAlignmentError": ifOtnMonSmBackwardIncomingAlignmentError,
       "ifOtnMonTcmList": ifOtnMonTcmList,
       "ifOtnMonTcmTable": ifOtnMonTcmTable,
       "ifOtnMonTcmEntry": ifOtnMonTcmEntry,
       "ifOtnMonTcmIndex": ifOtnMonTcmIndex,
       "ifOtnMonTcmName": ifOtnMonTcmName,
       "ifOtnMonTcmConnOduIndex": ifOtnMonTcmConnOduIndex,
       "ifOtnMonTcmAlarmMode": ifOtnMonTcmAlarmMode,
       "ifOtnMonTcmMode": ifOtnMonTcmMode,
       "ifOtnMonTcmTcmNumber": ifOtnMonTcmTcmNumber,
       "ifOtnMonTcmTxSignalStatus": ifOtnMonTcmTxSignalStatus,
       "ifOtnMonTcmRxSignalStatus": ifOtnMonTcmRxSignalStatus,
       "ifOtnMonTcmBackwardDefectIndication": ifOtnMonTcmBackwardDefectIndication,
       "ifOtnMonTcmBackwardIncomingAlignmentError": ifOtnMonTcmBackwardIncomingAlignmentError,
       "ifOtnMonTcmRxAlarmIndicationSignal": ifOtnMonTcmRxAlarmIndicationSignal,
       "ifOtnMonTcmRxOpenConnectionIndication": ifOtnMonTcmRxOpenConnectionIndication,
       "ifOtnMonTcmRxLockedDefectIndication": ifOtnMonTcmRxLockedDefectIndication,
       "ifOtnMonTcmLossOfTandemConnection": ifOtnMonTcmLossOfTandemConnection,
       "ifOtnMonTcmIncomingAlignmentError": ifOtnMonTcmIncomingAlignmentError,
       "ifOtnMonTcmSwitchCriteria": ifOtnMonTcmSwitchCriteria,
       "ifOtnMonPmList": ifOtnMonPmList,
       "ifOtnMonPmTable": ifOtnMonPmTable,
       "ifOtnMonPmEntry": ifOtnMonPmEntry,
       "ifOtnMonPmIndex": ifOtnMonPmIndex,
       "ifOtnMonPmName": ifOtnMonPmName,
       "ifOtnMonPmConnOduIndex": ifOtnMonPmConnOduIndex,
       "ifOtnMonPmAlarmMode": ifOtnMonPmAlarmMode,
       "ifOtnMonPmTxSignalStatus": ifOtnMonPmTxSignalStatus,
       "ifOtnMonPmRxSignalStatus": ifOtnMonPmRxSignalStatus,
       "ifOtnMonPmRxBackwardDefectIndication": ifOtnMonPmRxBackwardDefectIndication,
       "ifOtnMonPmRxAlarmIndicationSignal": ifOtnMonPmRxAlarmIndicationSignal,
       "ifOtnMonPmRxOpenConnectionIndication": ifOtnMonPmRxOpenConnectionIndication,
       "ifOtnMonPmRxLockedDefectIndication": ifOtnMonPmRxLockedDefectIndication,
       "ifOtnMonPmTxBackwardDefectIndication": ifOtnMonPmTxBackwardDefectIndication,
       "ifOtnMonPmTxAlarmIndicationSignal": ifOtnMonPmTxAlarmIndicationSignal,
       "ifOtnMonPmTxOpenConnectionIndication": ifOtnMonPmTxOpenConnectionIndication,
       "ifOtnMonPmTxLockedDefectIndication": ifOtnMonPmTxLockedDefectIndication,
       "ifOtnMonPmUpPortId": ifOtnMonPmUpPortId,
       "ifOtnMonTraceList": ifOtnMonTraceList,
       "ifOtnMonTraceTable": ifOtnMonTraceTable,
       "ifOtnMonTraceEntry": ifOtnMonTraceEntry,
       "ifOtnMonTraceIndex": ifOtnMonTraceIndex,
       "ifOtnMonTraceName": ifOtnMonTraceName,
       "ifOtnMonTraceConnOtnType": ifOtnMonTraceConnOtnType,
       "ifOtnMonTraceConnOtnIndex": ifOtnMonTraceConnOtnIndex,
       "ifOtnMonTraceSapiTraceTransmitted": ifOtnMonTraceSapiTraceTransmitted,
       "ifOtnMonTraceSapiTraceReceivedByte0": ifOtnMonTraceSapiTraceReceivedByte0,
       "ifOtnMonTraceSapiTraceReceived": ifOtnMonTraceSapiTraceReceived,
       "ifOtnMonTraceSapiTraceExpected": ifOtnMonTraceSapiTraceExpected,
       "ifOtnMonTraceDapiTraceTransmitted": ifOtnMonTraceDapiTraceTransmitted,
       "ifOtnMonTraceDapiTraceReceivedByte0": ifOtnMonTraceDapiTraceReceivedByte0,
       "ifOtnMonTraceDapiTraceReceived": ifOtnMonTraceDapiTraceReceived,
       "ifOtnMonTraceDapiTraceExpected": ifOtnMonTraceDapiTraceExpected,
       "ifOtnMonTraceOpSpecificTraceTransmitted": ifOtnMonTraceOpSpecificTraceTransmitted,
       "ifOtnMonTraceOpSpecificTraceReceived": ifOtnMonTraceOpSpecificTraceReceived,
       "ifOtnMonTraceTraceIdMMDetectionMode": ifOtnMonTraceTraceIdMMDetectionMode,
       "ifOtnMonTraceTraceAlarmMode": ifOtnMonTraceTraceAlarmMode,
       "ifOtnMonTraceTIMConsequenceActionsDisabled": ifOtnMonTraceTIMConsequenceActionsDisabled,
       "ifOtnMonTraceTxSignalStatus": ifOtnMonTraceTxSignalStatus,
       "ifOtnMonTraceRxSignalStatus": ifOtnMonTraceRxSignalStatus,
       "ifOtnMonTraceTraceMismatch": ifOtnMonTraceTraceMismatch,
       "ifOtnMonTraceConnOtnDirection": ifOtnMonTraceConnOtnDirection,
       "ifOtnMonTraceUpPortId": ifOtnMonTraceUpPortId}
)
