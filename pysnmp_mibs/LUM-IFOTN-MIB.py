# SNMP MIB module (LUM-IFOTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFOTN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:09 2025
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

(lumIfOtnMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfOtnMIB",
    "lumModules")

(CommandString,
 FaultStatusWithNA,
 MgmtNameString,
 SignalStatusWithNA,
 TruthValueWithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "FaultStatusWithNA",
    "MgmtNameString",
    "SignalStatusWithNA",
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

lumIfOtnMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 50)
)
if mibBuilder.loadTexts:
    lumIfOtnMIBModule.setRevisions(
        ("2018-06-29 00:00",
         "2017-12-15 00:00",
         "2017-06-15 00:00",
         "2016-11-30 00:00",
         "2015-01-23 00:00",
         "2014-09-30 00:00",
         "2014-05-16 00:00",
         "2013-11-15 00:00",
         "2013-05-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfOtnConfs_ObjectIdentity = ObjectIdentity
lumIfOtnConfs = _LumIfOtnConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1)
)
_LumIfOtnGroups_ObjectIdentity = ObjectIdentity
lumIfOtnGroups = _LumIfOtnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1)
)
_LumIfOtnCompl_ObjectIdentity = ObjectIdentity
lumIfOtnCompl = _LumIfOtnCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 2)
)
_LumIfOtnMIBObjects_ObjectIdentity = ObjectIdentity
lumIfOtnMIBObjects = _LumIfOtnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2)
)
_IfOtnGeneral_ObjectIdentity = ObjectIdentity
ifOtnGeneral = _IfOtnGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1)
)
_IfOtnGeneralConfigLastChangeTime_Type = DateAndTime
_IfOtnGeneralConfigLastChangeTime_Object = MibScalar
ifOtnGeneralConfigLastChangeTime = _IfOtnGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 1),
    _IfOtnGeneralConfigLastChangeTime_Type()
)
ifOtnGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralConfigLastChangeTime.setStatus("current")
_IfOtnGeneralStateLastChangeTime_Type = DateAndTime
_IfOtnGeneralStateLastChangeTime_Object = MibScalar
ifOtnGeneralStateLastChangeTime = _IfOtnGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 2),
    _IfOtnGeneralStateLastChangeTime_Type()
)
ifOtnGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralStateLastChangeTime.setStatus("current")
_IfOtnGeneralIfOtnOtuTableSize_Type = Unsigned32
_IfOtnGeneralIfOtnOtuTableSize_Object = MibScalar
ifOtnGeneralIfOtnOtuTableSize = _IfOtnGeneralIfOtnOtuTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 3),
    _IfOtnGeneralIfOtnOtuTableSize_Type()
)
ifOtnGeneralIfOtnOtuTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralIfOtnOtuTableSize.setStatus("current")
_IfOtnGeneralIfOtnOtuConfigLastChangeTime_Type = DateAndTime
_IfOtnGeneralIfOtnOtuConfigLastChangeTime_Object = MibScalar
ifOtnGeneralIfOtnOtuConfigLastChangeTime = _IfOtnGeneralIfOtnOtuConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 4),
    _IfOtnGeneralIfOtnOtuConfigLastChangeTime_Type()
)
ifOtnGeneralIfOtnOtuConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralIfOtnOtuConfigLastChangeTime.setStatus("current")
_IfOtnGeneralIfOtnOtuStateLastChangeTime_Type = DateAndTime
_IfOtnGeneralIfOtnOtuStateLastChangeTime_Object = MibScalar
ifOtnGeneralIfOtnOtuStateLastChangeTime = _IfOtnGeneralIfOtnOtuStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 5),
    _IfOtnGeneralIfOtnOtuStateLastChangeTime_Type()
)
ifOtnGeneralIfOtnOtuStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralIfOtnOtuStateLastChangeTime.setStatus("current")
_IfOtnGeneralIfOtnOduTableSize_Type = Unsigned32
_IfOtnGeneralIfOtnOduTableSize_Object = MibScalar
ifOtnGeneralIfOtnOduTableSize = _IfOtnGeneralIfOtnOduTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 6),
    _IfOtnGeneralIfOtnOduTableSize_Type()
)
ifOtnGeneralIfOtnOduTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralIfOtnOduTableSize.setStatus("current")
_IfOtnGeneralIfOtnOduConfigLastChangeTime_Type = DateAndTime
_IfOtnGeneralIfOtnOduConfigLastChangeTime_Object = MibScalar
ifOtnGeneralIfOtnOduConfigLastChangeTime = _IfOtnGeneralIfOtnOduConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 7),
    _IfOtnGeneralIfOtnOduConfigLastChangeTime_Type()
)
ifOtnGeneralIfOtnOduConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralIfOtnOduConfigLastChangeTime.setStatus("current")
_IfOtnGeneralIfOtnOduStateLastChangeTime_Type = DateAndTime
_IfOtnGeneralIfOtnOduStateLastChangeTime_Object = MibScalar
ifOtnGeneralIfOtnOduStateLastChangeTime = _IfOtnGeneralIfOtnOduStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 8),
    _IfOtnGeneralIfOtnOduStateLastChangeTime_Type()
)
ifOtnGeneralIfOtnOduStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralIfOtnOduStateLastChangeTime.setStatus("current")
_IfOtnGeneralIfOtnOpuTableSize_Type = Unsigned32
_IfOtnGeneralIfOtnOpuTableSize_Object = MibScalar
ifOtnGeneralIfOtnOpuTableSize = _IfOtnGeneralIfOtnOpuTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 9),
    _IfOtnGeneralIfOtnOpuTableSize_Type()
)
ifOtnGeneralIfOtnOpuTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralIfOtnOpuTableSize.setStatus("current")
_IfOtnGeneralIfOtnOpuConfigLastChangeTime_Type = DateAndTime
_IfOtnGeneralIfOtnOpuConfigLastChangeTime_Object = MibScalar
ifOtnGeneralIfOtnOpuConfigLastChangeTime = _IfOtnGeneralIfOtnOpuConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 10),
    _IfOtnGeneralIfOtnOpuConfigLastChangeTime_Type()
)
ifOtnGeneralIfOtnOpuConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralIfOtnOpuConfigLastChangeTime.setStatus("current")
_IfOtnGeneralIfOtnOpuStateLastChangeTime_Type = DateAndTime
_IfOtnGeneralIfOtnOpuStateLastChangeTime_Object = MibScalar
ifOtnGeneralIfOtnOpuStateLastChangeTime = _IfOtnGeneralIfOtnOpuStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 11),
    _IfOtnGeneralIfOtnOpuStateLastChangeTime_Type()
)
ifOtnGeneralIfOtnOpuStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralIfOtnOpuStateLastChangeTime.setStatus("current")
_IfOtnGeneralIfOtnTpTableSize_Type = Unsigned32
_IfOtnGeneralIfOtnTpTableSize_Object = MibScalar
ifOtnGeneralIfOtnTpTableSize = _IfOtnGeneralIfOtnTpTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 12),
    _IfOtnGeneralIfOtnTpTableSize_Type()
)
ifOtnGeneralIfOtnTpTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralIfOtnTpTableSize.setStatus("current")
_IfOtnGeneralIfOtnTpConfigLastChangeTime_Type = DateAndTime
_IfOtnGeneralIfOtnTpConfigLastChangeTime_Object = MibScalar
ifOtnGeneralIfOtnTpConfigLastChangeTime = _IfOtnGeneralIfOtnTpConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 13),
    _IfOtnGeneralIfOtnTpConfigLastChangeTime_Type()
)
ifOtnGeneralIfOtnTpConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralIfOtnTpConfigLastChangeTime.setStatus("current")
_IfOtnGeneralIfOtnTpStateLastChangeTime_Type = DateAndTime
_IfOtnGeneralIfOtnTpStateLastChangeTime_Object = MibScalar
ifOtnGeneralIfOtnTpStateLastChangeTime = _IfOtnGeneralIfOtnTpStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 1, 14),
    _IfOtnGeneralIfOtnTpStateLastChangeTime_Type()
)
ifOtnGeneralIfOtnTpStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnGeneralIfOtnTpStateLastChangeTime.setStatus("current")
_IfOtnOtuList_ObjectIdentity = ObjectIdentity
ifOtnOtuList = _IfOtnOtuList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 2)
)
_IfOtnOtuTable_Object = MibTable
ifOtnOtuTable = _IfOtnOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifOtnOtuTable.setStatus("current")
_IfOtnOtuEntry_Object = MibTableRow
ifOtnOtuEntry = _IfOtnOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 2, 1, 1)
)
ifOtnOtuEntry.setIndexNames(
    (0, "LUM-IFOTN-MIB", "ifOtnOtuIndex"),
)
if mibBuilder.loadTexts:
    ifOtnOtuEntry.setStatus("current")
_IfOtnOtuIndex_Type = Unsigned32
_IfOtnOtuIndex_Object = MibTableColumn
ifOtnOtuIndex = _IfOtnOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 2, 1, 1, 1),
    _IfOtnOtuIndex_Type()
)
ifOtnOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOtuIndex.setStatus("current")
_IfOtnOtuName_Type = MgmtNameString
_IfOtnOtuName_Object = MibTableColumn
ifOtnOtuName = _IfOtnOtuName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 2, 1, 1, 2),
    _IfOtnOtuName_Type()
)
ifOtnOtuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOtuName.setStatus("current")
_IfOtnOtuConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfOtnOtuConnIfBasicIfIndex_Object = MibTableColumn
ifOtnOtuConnIfBasicIfIndex = _IfOtnOtuConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 2, 1, 1, 3),
    _IfOtnOtuConnIfBasicIfIndex_Type()
)
ifOtnOtuConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOtuConnIfBasicIfIndex.setStatus("current")
_IfOtnOtuTxSignalStatus_Type = SignalStatusWithNA
_IfOtnOtuTxSignalStatus_Object = MibTableColumn
ifOtnOtuTxSignalStatus = _IfOtnOtuTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 2, 1, 1, 4),
    _IfOtnOtuTxSignalStatus_Type()
)
ifOtnOtuTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOtuTxSignalStatus.setStatus("current")
_IfOtnOtuRxSignalStatus_Type = SignalStatusWithNA
_IfOtnOtuRxSignalStatus_Object = MibTableColumn
ifOtnOtuRxSignalStatus = _IfOtnOtuRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 2, 1, 1, 5),
    _IfOtnOtuRxSignalStatus_Type()
)
ifOtnOtuRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOtuRxSignalStatus.setStatus("current")
_IfOtnOtuLossOfFrame_Type = FaultStatusWithNA
_IfOtnOtuLossOfFrame_Object = MibTableColumn
ifOtnOtuLossOfFrame = _IfOtnOtuLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 2, 1, 1, 6),
    _IfOtnOtuLossOfFrame_Type()
)
ifOtnOtuLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOtuLossOfFrame.setStatus("current")
_IfOtnOtuRxAlarmIndicationSignal_Type = FaultStatusWithNA
_IfOtnOtuRxAlarmIndicationSignal_Object = MibTableColumn
ifOtnOtuRxAlarmIndicationSignal = _IfOtnOtuRxAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 2, 1, 1, 7),
    _IfOtnOtuRxAlarmIndicationSignal_Type()
)
ifOtnOtuRxAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOtuRxAlarmIndicationSignal.setStatus("current")
_IfOtnOtuLossOfMultiframe_Type = FaultStatusWithNA
_IfOtnOtuLossOfMultiframe_Object = MibTableColumn
ifOtnOtuLossOfMultiframe = _IfOtnOtuLossOfMultiframe_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 2, 1, 1, 8),
    _IfOtnOtuLossOfMultiframe_Type()
)
ifOtnOtuLossOfMultiframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOtuLossOfMultiframe.setStatus("current")


class _IfOtnOtuUpPortId_Type(Integer32):
    """Custom type ifOtnOtuUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_IfOtnOtuUpPortId_Type.__name__ = "Integer32"
_IfOtnOtuUpPortId_Object = MibTableColumn
ifOtnOtuUpPortId = _IfOtnOtuUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 2, 1, 1, 9),
    _IfOtnOtuUpPortId_Type()
)
ifOtnOtuUpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOtuUpPortId.setStatus("current")
_IfOtnOduList_ObjectIdentity = ObjectIdentity
ifOtnOduList = _IfOtnOduList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3)
)
_IfOtnOduTable_Object = MibTable
ifOtnOduTable = _IfOtnOduTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifOtnOduTable.setStatus("current")
_IfOtnOduEntry_Object = MibTableRow
ifOtnOduEntry = _IfOtnOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3, 1, 1)
)
ifOtnOduEntry.setIndexNames(
    (0, "LUM-IFOTN-MIB", "ifOtnOduIndex"),
)
if mibBuilder.loadTexts:
    ifOtnOduEntry.setStatus("current")
_IfOtnOduIndex_Type = Unsigned32
_IfOtnOduIndex_Object = MibTableColumn
ifOtnOduIndex = _IfOtnOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3, 1, 1, 1),
    _IfOtnOduIndex_Type()
)
ifOtnOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOduIndex.setStatus("current")
_IfOtnOduName_Type = MgmtNameString
_IfOtnOduName_Object = MibTableColumn
ifOtnOduName = _IfOtnOduName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3, 1, 1, 2),
    _IfOtnOduName_Type()
)
ifOtnOduName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOtnOduName.setStatus("current")
_IfOtnOduConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfOtnOduConnIfBasicIfIndex_Object = MibTableColumn
ifOtnOduConnIfBasicIfIndex = _IfOtnOduConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3, 1, 1, 3),
    _IfOtnOduConnIfBasicIfIndex_Type()
)
ifOtnOduConnIfBasicIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOtnOduConnIfBasicIfIndex.setStatus("current")


class _IfOtnOduGcc1Terminated_Type(TruthValueWithNA):
    """Custom type ifOtnOduGcc1Terminated based on TruthValueWithNA"""
    defaultValue = 1


_IfOtnOduGcc1Terminated_Type.__name__ = "TruthValueWithNA"
_IfOtnOduGcc1Terminated_Object = MibTableColumn
ifOtnOduGcc1Terminated = _IfOtnOduGcc1Terminated_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3, 1, 1, 4),
    _IfOtnOduGcc1Terminated_Type()
)
ifOtnOduGcc1Terminated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOduGcc1Terminated.setStatus("current")


class _IfOtnOduGcc2Terminated_Type(TruthValueWithNA):
    """Custom type ifOtnOduGcc2Terminated based on TruthValueWithNA"""
    defaultValue = 1


_IfOtnOduGcc2Terminated_Type.__name__ = "TruthValueWithNA"
_IfOtnOduGcc2Terminated_Object = MibTableColumn
ifOtnOduGcc2Terminated = _IfOtnOduGcc2Terminated_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3, 1, 1, 5),
    _IfOtnOduGcc2Terminated_Type()
)
ifOtnOduGcc2Terminated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOduGcc2Terminated.setStatus("current")


class _IfOtnOduUsedTcms_Type(Unsigned32WithNA):
    """Custom type ifOtnOduUsedTcms based on Unsigned32WithNA"""
    defaultValue = 0


_IfOtnOduUsedTcms_Type.__name__ = "Unsigned32WithNA"
_IfOtnOduUsedTcms_Object = MibTableColumn
ifOtnOduUsedTcms = _IfOtnOduUsedTcms_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3, 1, 1, 6),
    _IfOtnOduUsedTcms_Type()
)
ifOtnOduUsedTcms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOtnOduUsedTcms.setStatus("current")
_IfOtnOduTxSignalStatus_Type = SignalStatusWithNA
_IfOtnOduTxSignalStatus_Object = MibTableColumn
ifOtnOduTxSignalStatus = _IfOtnOduTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3, 1, 1, 7),
    _IfOtnOduTxSignalStatus_Type()
)
ifOtnOduTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOduTxSignalStatus.setStatus("current")
_IfOtnOduRxSignalStatus_Type = SignalStatusWithNA
_IfOtnOduRxSignalStatus_Object = MibTableColumn
ifOtnOduRxSignalStatus = _IfOtnOduRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3, 1, 1, 8),
    _IfOtnOduRxSignalStatus_Type()
)
ifOtnOduRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOduRxSignalStatus.setStatus("current")


class _IfOtnOduType_Type(Integer32):
    """Custom type ifOtnOduType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("unused", 1),
          ("odu0", 2),
          ("odu1", 3),
          ("odu2", 4),
          ("odu3", 5),
          ("odu4", 6),
          ("oduFlex", 7),
          ("oduJ2", 8),
          ("odu2e", 9),
          ("notApplicable", 2147483647))
    )


_IfOtnOduType_Type.__name__ = "Integer32"
_IfOtnOduType_Object = MibTableColumn
ifOtnOduType = _IfOtnOduType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3, 1, 1, 9),
    _IfOtnOduType_Type()
)
ifOtnOduType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOtnOduType.setStatus("current")


class _IfOtnOduParentOduIndex_Type(Unsigned32WithNA):
    """Custom type ifOtnOduParentOduIndex based on Unsigned32WithNA"""
    defaultValue = 2147483647


_IfOtnOduParentOduIndex_Type.__name__ = "Unsigned32WithNA"
_IfOtnOduParentOduIndex_Object = MibTableColumn
ifOtnOduParentOduIndex = _IfOtnOduParentOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 3, 1, 1, 10),
    _IfOtnOduParentOduIndex_Type()
)
ifOtnOduParentOduIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOtnOduParentOduIndex.setStatus("current")
_IfOtnOpuList_ObjectIdentity = ObjectIdentity
ifOtnOpuList = _IfOtnOpuList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4)
)
_IfOtnOpuTable_Object = MibTable
ifOtnOpuTable = _IfOtnOpuTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ifOtnOpuTable.setStatus("current")
_IfOtnOpuEntry_Object = MibTableRow
ifOtnOpuEntry = _IfOtnOpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1)
)
ifOtnOpuEntry.setIndexNames(
    (0, "LUM-IFOTN-MIB", "ifOtnOpuIndex"),
)
if mibBuilder.loadTexts:
    ifOtnOpuEntry.setStatus("current")
_IfOtnOpuIndex_Type = Unsigned32
_IfOtnOpuIndex_Object = MibTableColumn
ifOtnOpuIndex = _IfOtnOpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1, 1),
    _IfOtnOpuIndex_Type()
)
ifOtnOpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOpuIndex.setStatus("current")
_IfOtnOpuName_Type = MgmtNameString
_IfOtnOpuName_Object = MibTableColumn
ifOtnOpuName = _IfOtnOpuName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1, 2),
    _IfOtnOpuName_Type()
)
ifOtnOpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOpuName.setStatus("current")
_IfOtnOpuConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfOtnOpuConnIfBasicIfIndex_Object = MibTableColumn
ifOtnOpuConnIfBasicIfIndex = _IfOtnOpuConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1, 3),
    _IfOtnOpuConnIfBasicIfIndex_Type()
)
ifOtnOpuConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOpuConnIfBasicIfIndex.setStatus("current")
_IfOtnOpuTxSignalStatus_Type = SignalStatusWithNA
_IfOtnOpuTxSignalStatus_Object = MibTableColumn
ifOtnOpuTxSignalStatus = _IfOtnOpuTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1, 4),
    _IfOtnOpuTxSignalStatus_Type()
)
ifOtnOpuTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOpuTxSignalStatus.setStatus("current")
_IfOtnOpuRxSignalStatus_Type = SignalStatusWithNA
_IfOtnOpuRxSignalStatus_Object = MibTableColumn
ifOtnOpuRxSignalStatus = _IfOtnOpuRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1, 5),
    _IfOtnOpuRxSignalStatus_Type()
)
ifOtnOpuRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOpuRxSignalStatus.setStatus("current")
_IfOtnOpuTxClientMaintenanceIndication_Type = FaultStatusWithNA
_IfOtnOpuTxClientMaintenanceIndication_Object = MibTableColumn
ifOtnOpuTxClientMaintenanceIndication = _IfOtnOpuTxClientMaintenanceIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1, 6),
    _IfOtnOpuTxClientMaintenanceIndication_Type()
)
ifOtnOpuTxClientMaintenanceIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOpuTxClientMaintenanceIndication.setStatus("current")
_IfOtnOpuTxClientSignalFail_Type = FaultStatusWithNA
_IfOtnOpuTxClientSignalFail_Object = MibTableColumn
ifOtnOpuTxClientSignalFail = _IfOtnOpuTxClientSignalFail_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1, 7),
    _IfOtnOpuTxClientSignalFail_Type()
)
ifOtnOpuTxClientSignalFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOpuTxClientSignalFail.setStatus("current")
_IfOtnOpuRxPayloadMismatch_Type = FaultStatusWithNA
_IfOtnOpuRxPayloadMismatch_Object = MibTableColumn
ifOtnOpuRxPayloadMismatch = _IfOtnOpuRxPayloadMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1, 8),
    _IfOtnOpuRxPayloadMismatch_Type()
)
ifOtnOpuRxPayloadMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOpuRxPayloadMismatch.setStatus("current")
_IfOtnOpuTxPayloadMismatch_Type = FaultStatusWithNA
_IfOtnOpuTxPayloadMismatch_Object = MibTableColumn
ifOtnOpuTxPayloadMismatch = _IfOtnOpuTxPayloadMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1, 9),
    _IfOtnOpuTxPayloadMismatch_Type()
)
ifOtnOpuTxPayloadMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOpuTxPayloadMismatch.setStatus("current")
_IfOtnOpuLossOfOpuMultiFrameIdentifier_Type = FaultStatusWithNA
_IfOtnOpuLossOfOpuMultiFrameIdentifier_Object = MibTableColumn
ifOtnOpuLossOfOpuMultiFrameIdentifier = _IfOtnOpuLossOfOpuMultiFrameIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1, 10),
    _IfOtnOpuLossOfOpuMultiFrameIdentifier_Type()
)
ifOtnOpuLossOfOpuMultiFrameIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOpuLossOfOpuMultiFrameIdentifier.setStatus("current")
_IfOtnOpuRxClientMaintenanceIndication_Type = FaultStatusWithNA
_IfOtnOpuRxClientMaintenanceIndication_Object = MibTableColumn
ifOtnOpuRxClientMaintenanceIndication = _IfOtnOpuRxClientMaintenanceIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1, 11),
    _IfOtnOpuRxClientMaintenanceIndication_Type()
)
ifOtnOpuRxClientMaintenanceIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOpuRxClientMaintenanceIndication.setStatus("current")
_IfOtnOpuConnOduIndex_Type = Unsigned32WithNA
_IfOtnOpuConnOduIndex_Object = MibTableColumn
ifOtnOpuConnOduIndex = _IfOtnOpuConnOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 4, 1, 1, 12),
    _IfOtnOpuConnOduIndex_Type()
)
ifOtnOpuConnOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnOpuConnOduIndex.setStatus("current")
_IfOtnTpList_ObjectIdentity = ObjectIdentity
ifOtnTpList = _IfOtnTpList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5)
)
_IfOtnTpTable_Object = MibTable
ifOtnTpTable = _IfOtnTpTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ifOtnTpTable.setStatus("current")
_IfOtnTpEntry_Object = MibTableRow
ifOtnTpEntry = _IfOtnTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1, 1)
)
ifOtnTpEntry.setIndexNames(
    (0, "LUM-IFOTN-MIB", "ifOtnTpIndex"),
)
if mibBuilder.loadTexts:
    ifOtnTpEntry.setStatus("current")
_IfOtnTpIndex_Type = Unsigned32
_IfOtnTpIndex_Object = MibTableColumn
ifOtnTpIndex = _IfOtnTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1, 1, 1),
    _IfOtnTpIndex_Type()
)
ifOtnTpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnTpIndex.setStatus("current")
_IfOtnTpName_Type = MgmtNameString
_IfOtnTpName_Object = MibTableColumn
ifOtnTpName = _IfOtnTpName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1, 1, 2),
    _IfOtnTpName_Type()
)
ifOtnTpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOtnTpName.setStatus("current")
_IfOtnTpConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfOtnTpConnIfBasicIfIndex_Object = MibTableColumn
ifOtnTpConnIfBasicIfIndex = _IfOtnTpConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1, 1, 3),
    _IfOtnTpConnIfBasicIfIndex_Type()
)
ifOtnTpConnIfBasicIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOtnTpConnIfBasicIfIndex.setStatus("current")
_IfOtnTpUsedTribSlots_Type = Unsigned32WithNA
_IfOtnTpUsedTribSlots_Object = MibTableColumn
ifOtnTpUsedTribSlots = _IfOtnTpUsedTribSlots_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1, 1, 4),
    _IfOtnTpUsedTribSlots_Type()
)
ifOtnTpUsedTribSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnTpUsedTribSlots.setStatus("current")


class _IfOtnTpTribPortId_Type(Unsigned32WithNA):
    """Custom type ifOtnTpTribPortId based on Unsigned32WithNA"""
    defaultValue = 2147483647


_IfOtnTpTribPortId_Type.__name__ = "Unsigned32WithNA"
_IfOtnTpTribPortId_Object = MibTableColumn
ifOtnTpTribPortId = _IfOtnTpTribPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1, 1, 5),
    _IfOtnTpTribPortId_Type()
)
ifOtnTpTribPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOtnTpTribPortId.setStatus("current")
_IfOtnTpRxMultiplexStructureIdentifierMismatch_Type = FaultStatusWithNA
_IfOtnTpRxMultiplexStructureIdentifierMismatch_Object = MibTableColumn
ifOtnTpRxMultiplexStructureIdentifierMismatch = _IfOtnTpRxMultiplexStructureIdentifierMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1, 1, 6),
    _IfOtnTpRxMultiplexStructureIdentifierMismatch_Type()
)
ifOtnTpRxMultiplexStructureIdentifierMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnTpRxMultiplexStructureIdentifierMismatch.setStatus("current")
_IfOtnTpTxSignalStatus_Type = SignalStatusWithNA
_IfOtnTpTxSignalStatus_Object = MibTableColumn
ifOtnTpTxSignalStatus = _IfOtnTpTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1, 1, 7),
    _IfOtnTpTxSignalStatus_Type()
)
ifOtnTpTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnTpTxSignalStatus.setStatus("current")
_IfOtnTpRxSignalStatus_Type = SignalStatusWithNA
_IfOtnTpRxSignalStatus_Object = MibTableColumn
ifOtnTpRxSignalStatus = _IfOtnTpRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1, 1, 8),
    _IfOtnTpRxSignalStatus_Type()
)
ifOtnTpRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnTpRxSignalStatus.setStatus("current")


class _IfOtnTpXcRefOduIndex_Type(Unsigned32WithNA):
    """Custom type ifOtnTpXcRefOduIndex based on Unsigned32WithNA"""
    defaultValue = 2147483647


_IfOtnTpXcRefOduIndex_Type.__name__ = "Unsigned32WithNA"
_IfOtnTpXcRefOduIndex_Object = MibTableColumn
ifOtnTpXcRefOduIndex = _IfOtnTpXcRefOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1, 1, 9),
    _IfOtnTpXcRefOduIndex_Type()
)
ifOtnTpXcRefOduIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOtnTpXcRefOduIndex.setStatus("current")


class _IfOtnTpTribSlotMask_Type(DisplayString):
    """Custom type ifOtnTpTribSlotMask based on DisplayString"""
    defaultValue = OctetString("")


_IfOtnTpTribSlotMask_Type.__name__ = "DisplayString"
_IfOtnTpTribSlotMask_Object = MibTableColumn
ifOtnTpTribSlotMask = _IfOtnTpTribSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1, 1, 10),
    _IfOtnTpTribSlotMask_Type()
)
ifOtnTpTribSlotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOtnTpTribSlotMask.setStatus("current")


class _IfOtnTpTribSlotView_Type(DisplayString):
    """Custom type ifOtnTpTribSlotView based on DisplayString"""
    defaultValue = OctetString("")


_IfOtnTpTribSlotView_Type.__name__ = "DisplayString"
_IfOtnTpTribSlotView_Object = MibTableColumn
ifOtnTpTribSlotView = _IfOtnTpTribSlotView_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 2, 5, 1, 1, 11),
    _IfOtnTpTribSlotView_Type()
)
ifOtnTpTribSlotView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtnTpTribSlotView.setStatus("current")

# Managed Objects groups

ifOtnGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 1)
)
ifOtnGeneralGroupV1.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnGeneralConfigLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralStateLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOtuTableSize"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOtuConfigLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOtuStateLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOduTableSize"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOduConfigLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOduStateLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOpuTableSize"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOpuConfigLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOpuStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifOtnGeneralGroupV1.setStatus("deprecated")

ifOtnOtuGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 2)
)
ifOtnOtuGroupV1.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnOtuIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOtuName"),
        ("LUM-IFOTN-MIB", "ifOtnOtuConnIfBasicIfIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOtuTxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOtuRxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOtuLossOfFrame"),
        ("LUM-IFOTN-MIB", "ifOtnOtuRxAlarmIndicationSignal"),
        ("LUM-IFOTN-MIB", "ifOtnOtuLossOfMultiframe"))
)
if mibBuilder.loadTexts:
    ifOtnOtuGroupV1.setStatus("deprecated")

ifOtnOduGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 3)
)
ifOtnOduGroupV1.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnOduIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOduName"),
        ("LUM-IFOTN-MIB", "ifOtnOduConnIfBasicIfIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOduGcc1Terminated"),
        ("LUM-IFOTN-MIB", "ifOtnOduGcc2Terminated"),
        ("LUM-IFOTN-MIB", "ifOtnOduUsedTcms"),
        ("LUM-IFOTN-MIB", "ifOtnOduTxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOduRxSignalStatus"))
)
if mibBuilder.loadTexts:
    ifOtnOduGroupV1.setStatus("deprecated")

ifOtnOpuGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 4)
)
ifOtnOpuGroupV1.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnOpuIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOpuName"),
        ("LUM-IFOTN-MIB", "ifOtnOpuConnIfBasicIfIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOpuRxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxClientMaintenanceIndication"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxClientSignalFail"))
)
if mibBuilder.loadTexts:
    ifOtnOpuGroupV1.setStatus("deprecated")

ifOtnTpGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 5)
)
ifOtnTpGroupV1.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnTpIndex"),
        ("LUM-IFOTN-MIB", "ifOtnTpName"),
        ("LUM-IFOTN-MIB", "ifOtnTpConnIfBasicIfIndex"),
        ("LUM-IFOTN-MIB", "ifOtnTpUsedTribSlots"),
        ("LUM-IFOTN-MIB", "ifOtnTpTribPortId"),
        ("LUM-IFOTN-MIB", "ifOtnTpRxMultiplexStructureIdentifierMismatch"),
        ("LUM-IFOTN-MIB", "ifOtnTpTxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnTpRxSignalStatus"))
)
if mibBuilder.loadTexts:
    ifOtnTpGroupV1.setStatus("current")

ifOtnOpuGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 6)
)
ifOtnOpuGroupV2.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnOpuIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOpuName"),
        ("LUM-IFOTN-MIB", "ifOtnOpuConnIfBasicIfIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOpuRxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxClientMaintenanceIndication"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxClientSignalFail"),
        ("LUM-IFOTN-MIB", "ifOtnOpuRxPayloadMismatch"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxPayloadMismatch"))
)
if mibBuilder.loadTexts:
    ifOtnOpuGroupV2.setStatus("deprecated")

ifOtnOduGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 7)
)
ifOtnOduGroupV2.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnOduIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOduName"),
        ("LUM-IFOTN-MIB", "ifOtnOduConnIfBasicIfIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOduGcc1Terminated"),
        ("LUM-IFOTN-MIB", "ifOtnOduGcc2Terminated"),
        ("LUM-IFOTN-MIB", "ifOtnOduUsedTcms"),
        ("LUM-IFOTN-MIB", "ifOtnOduTxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOduRxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOduType"),
        ("LUM-IFOTN-MIB", "ifOtnOduParentOduIndex"))
)
if mibBuilder.loadTexts:
    ifOtnOduGroupV2.setStatus("current")

ifOtnOtuGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 8)
)
ifOtnOtuGroupV2.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnOtuIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOtuName"),
        ("LUM-IFOTN-MIB", "ifOtnOtuConnIfBasicIfIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOtuTxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOtuRxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOtuLossOfFrame"),
        ("LUM-IFOTN-MIB", "ifOtnOtuRxAlarmIndicationSignal"),
        ("LUM-IFOTN-MIB", "ifOtnOtuLossOfMultiframe"))
)
if mibBuilder.loadTexts:
    ifOtnOtuGroupV2.setStatus("deprecated")

ifOtnOpuGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 9)
)
ifOtnOpuGroupV3.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnOpuIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOpuName"),
        ("LUM-IFOTN-MIB", "ifOtnOpuConnIfBasicIfIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOpuRxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxClientMaintenanceIndication"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxClientSignalFail"),
        ("LUM-IFOTN-MIB", "ifOtnOpuRxPayloadMismatch"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxPayloadMismatch"),
        ("LUM-IFOTN-MIB", "ifOtnOpuLossOfOpuMultiFrameIdentifier"))
)
if mibBuilder.loadTexts:
    ifOtnOpuGroupV3.setStatus("deprecated")

ifOtnTpGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 10)
)
ifOtnTpGroupV2.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnTpIndex"),
        ("LUM-IFOTN-MIB", "ifOtnTpName"),
        ("LUM-IFOTN-MIB", "ifOtnTpConnIfBasicIfIndex"),
        ("LUM-IFOTN-MIB", "ifOtnTpUsedTribSlots"),
        ("LUM-IFOTN-MIB", "ifOtnTpTribPortId"),
        ("LUM-IFOTN-MIB", "ifOtnTpRxMultiplexStructureIdentifierMismatch"),
        ("LUM-IFOTN-MIB", "ifOtnTpTxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnTpRxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnTpTribSlotMask"),
        ("LUM-IFOTN-MIB", "ifOtnTpTribSlotView"))
)
if mibBuilder.loadTexts:
    ifOtnTpGroupV2.setStatus("current")

ifOtnOtuGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 11)
)
ifOtnOtuGroupV3.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnOtuIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOtuName"),
        ("LUM-IFOTN-MIB", "ifOtnOtuConnIfBasicIfIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOtuTxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOtuRxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOtuLossOfFrame"),
        ("LUM-IFOTN-MIB", "ifOtnOtuRxAlarmIndicationSignal"),
        ("LUM-IFOTN-MIB", "ifOtnOtuLossOfMultiframe"),
        ("LUM-IFOTN-MIB", "ifOtnOtuUpPortId"))
)
if mibBuilder.loadTexts:
    ifOtnOtuGroupV3.setStatus("current")

ifOtnGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 12)
)
ifOtnGeneralGroupV2.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnGeneralConfigLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralStateLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOtuTableSize"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOtuConfigLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOtuStateLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOduTableSize"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOduConfigLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOduStateLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOpuTableSize"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOpuConfigLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnOpuStateLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnTpTableSize"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnTpConfigLastChangeTime"),
        ("LUM-IFOTN-MIB", "ifOtnGeneralIfOtnTpStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifOtnGeneralGroupV2.setStatus("current")

ifOtnOpuGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 1, 13)
)
ifOtnOpuGroupV4.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnOpuIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOpuName"),
        ("LUM-IFOTN-MIB", "ifOtnOpuConnIfBasicIfIndex"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOpuRxSignalStatus"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxClientMaintenanceIndication"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxClientSignalFail"),
        ("LUM-IFOTN-MIB", "ifOtnOpuRxPayloadMismatch"),
        ("LUM-IFOTN-MIB", "ifOtnOpuTxPayloadMismatch"),
        ("LUM-IFOTN-MIB", "ifOtnOpuLossOfOpuMultiFrameIdentifier"),
        ("LUM-IFOTN-MIB", "ifOtnOpuConnOduIndex"))
)
if mibBuilder.loadTexts:
    ifOtnOpuGroupV4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfOtnComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 2, 1)
)
lumIfOtnComplV1.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnGeneralGroupV1"),
        ("LUM-IFOTN-MIB", "ifOtnOtuGroupV1"),
        ("LUM-IFOTN-MIB", "ifOtnOduGroupV1"),
        ("LUM-IFOTN-MIB", "ifOtnOpuGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfOtnComplV1.setStatus(
        "deprecated"
    )

lumIfOtnComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 2, 2)
)
lumIfOtnComplV2.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnGeneralGroupV1"),
        ("LUM-IFOTN-MIB", "ifOtnOtuGroupV2"),
        ("LUM-IFOTN-MIB", "ifOtnOduGroupV2"),
        ("LUM-IFOTN-MIB", "ifOtnOpuGroupV2"),
        ("LUM-IFOTN-MIB", "ifOtnTpGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfOtnComplV2.setStatus(
        "deprecated"
    )

lumIfOtnComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 2, 3)
)
lumIfOtnComplV3.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnGeneralGroupV1"),
        ("LUM-IFOTN-MIB", "ifOtnOtuGroupV2"),
        ("LUM-IFOTN-MIB", "ifOtnOduGroupV2"),
        ("LUM-IFOTN-MIB", "ifOtnOpuGroupV3"),
        ("LUM-IFOTN-MIB", "ifOtnTpGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfOtnComplV3.setStatus(
        "deprecated"
    )

lumIfOtnComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 2, 4)
)
lumIfOtnComplV4.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnGeneralGroupV1"),
        ("LUM-IFOTN-MIB", "ifOtnOtuGroupV3"),
        ("LUM-IFOTN-MIB", "ifOtnOduGroupV2"),
        ("LUM-IFOTN-MIB", "ifOtnOpuGroupV3"),
        ("LUM-IFOTN-MIB", "ifOtnTpGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfOtnComplV4.setStatus(
        "deprecated"
    )

lumIfOtnComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 2, 5)
)
lumIfOtnComplV5.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnGeneralGroupV2"),
        ("LUM-IFOTN-MIB", "ifOtnOtuGroupV3"),
        ("LUM-IFOTN-MIB", "ifOtnOduGroupV2"),
        ("LUM-IFOTN-MIB", "ifOtnOpuGroupV3"),
        ("LUM-IFOTN-MIB", "ifOtnTpGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfOtnComplV5.setStatus(
        "deprecated"
    )

lumIfOtnComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50, 1, 2, 6)
)
lumIfOtnComplV6.setObjects(
      *(("LUM-IFOTN-MIB", "ifOtnGeneralGroupV2"),
        ("LUM-IFOTN-MIB", "ifOtnOtuGroupV3"),
        ("LUM-IFOTN-MIB", "ifOtnOduGroupV2"),
        ("LUM-IFOTN-MIB", "ifOtnOpuGroupV4"),
        ("LUM-IFOTN-MIB", "ifOtnTpGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfOtnComplV6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFOTN-MIB",
    **{"lumIfOtnMIBModule": lumIfOtnMIBModule,
       "lumIfOtnConfs": lumIfOtnConfs,
       "lumIfOtnGroups": lumIfOtnGroups,
       "ifOtnGeneralGroupV1": ifOtnGeneralGroupV1,
       "ifOtnOtuGroupV1": ifOtnOtuGroupV1,
       "ifOtnOduGroupV1": ifOtnOduGroupV1,
       "ifOtnOpuGroupV1": ifOtnOpuGroupV1,
       "ifOtnTpGroupV1": ifOtnTpGroupV1,
       "ifOtnOpuGroupV2": ifOtnOpuGroupV2,
       "ifOtnOduGroupV2": ifOtnOduGroupV2,
       "ifOtnOtuGroupV2": ifOtnOtuGroupV2,
       "ifOtnOpuGroupV3": ifOtnOpuGroupV3,
       "ifOtnTpGroupV2": ifOtnTpGroupV2,
       "ifOtnOtuGroupV3": ifOtnOtuGroupV3,
       "ifOtnGeneralGroupV2": ifOtnGeneralGroupV2,
       "ifOtnOpuGroupV4": ifOtnOpuGroupV4,
       "lumIfOtnCompl": lumIfOtnCompl,
       "lumIfOtnComplV1": lumIfOtnComplV1,
       "lumIfOtnComplV2": lumIfOtnComplV2,
       "lumIfOtnComplV3": lumIfOtnComplV3,
       "lumIfOtnComplV4": lumIfOtnComplV4,
       "lumIfOtnComplV5": lumIfOtnComplV5,
       "lumIfOtnComplV6": lumIfOtnComplV6,
       "lumIfOtnMIBObjects": lumIfOtnMIBObjects,
       "ifOtnGeneral": ifOtnGeneral,
       "ifOtnGeneralConfigLastChangeTime": ifOtnGeneralConfigLastChangeTime,
       "ifOtnGeneralStateLastChangeTime": ifOtnGeneralStateLastChangeTime,
       "ifOtnGeneralIfOtnOtuTableSize": ifOtnGeneralIfOtnOtuTableSize,
       "ifOtnGeneralIfOtnOtuConfigLastChangeTime": ifOtnGeneralIfOtnOtuConfigLastChangeTime,
       "ifOtnGeneralIfOtnOtuStateLastChangeTime": ifOtnGeneralIfOtnOtuStateLastChangeTime,
       "ifOtnGeneralIfOtnOduTableSize": ifOtnGeneralIfOtnOduTableSize,
       "ifOtnGeneralIfOtnOduConfigLastChangeTime": ifOtnGeneralIfOtnOduConfigLastChangeTime,
       "ifOtnGeneralIfOtnOduStateLastChangeTime": ifOtnGeneralIfOtnOduStateLastChangeTime,
       "ifOtnGeneralIfOtnOpuTableSize": ifOtnGeneralIfOtnOpuTableSize,
       "ifOtnGeneralIfOtnOpuConfigLastChangeTime": ifOtnGeneralIfOtnOpuConfigLastChangeTime,
       "ifOtnGeneralIfOtnOpuStateLastChangeTime": ifOtnGeneralIfOtnOpuStateLastChangeTime,
       "ifOtnGeneralIfOtnTpTableSize": ifOtnGeneralIfOtnTpTableSize,
       "ifOtnGeneralIfOtnTpConfigLastChangeTime": ifOtnGeneralIfOtnTpConfigLastChangeTime,
       "ifOtnGeneralIfOtnTpStateLastChangeTime": ifOtnGeneralIfOtnTpStateLastChangeTime,
       "ifOtnOtuList": ifOtnOtuList,
       "ifOtnOtuTable": ifOtnOtuTable,
       "ifOtnOtuEntry": ifOtnOtuEntry,
       "ifOtnOtuIndex": ifOtnOtuIndex,
       "ifOtnOtuName": ifOtnOtuName,
       "ifOtnOtuConnIfBasicIfIndex": ifOtnOtuConnIfBasicIfIndex,
       "ifOtnOtuTxSignalStatus": ifOtnOtuTxSignalStatus,
       "ifOtnOtuRxSignalStatus": ifOtnOtuRxSignalStatus,
       "ifOtnOtuLossOfFrame": ifOtnOtuLossOfFrame,
       "ifOtnOtuRxAlarmIndicationSignal": ifOtnOtuRxAlarmIndicationSignal,
       "ifOtnOtuLossOfMultiframe": ifOtnOtuLossOfMultiframe,
       "ifOtnOtuUpPortId": ifOtnOtuUpPortId,
       "ifOtnOduList": ifOtnOduList,
       "ifOtnOduTable": ifOtnOduTable,
       "ifOtnOduEntry": ifOtnOduEntry,
       "ifOtnOduIndex": ifOtnOduIndex,
       "ifOtnOduName": ifOtnOduName,
       "ifOtnOduConnIfBasicIfIndex": ifOtnOduConnIfBasicIfIndex,
       "ifOtnOduGcc1Terminated": ifOtnOduGcc1Terminated,
       "ifOtnOduGcc2Terminated": ifOtnOduGcc2Terminated,
       "ifOtnOduUsedTcms": ifOtnOduUsedTcms,
       "ifOtnOduTxSignalStatus": ifOtnOduTxSignalStatus,
       "ifOtnOduRxSignalStatus": ifOtnOduRxSignalStatus,
       "ifOtnOduType": ifOtnOduType,
       "ifOtnOduParentOduIndex": ifOtnOduParentOduIndex,
       "ifOtnOpuList": ifOtnOpuList,
       "ifOtnOpuTable": ifOtnOpuTable,
       "ifOtnOpuEntry": ifOtnOpuEntry,
       "ifOtnOpuIndex": ifOtnOpuIndex,
       "ifOtnOpuName": ifOtnOpuName,
       "ifOtnOpuConnIfBasicIfIndex": ifOtnOpuConnIfBasicIfIndex,
       "ifOtnOpuTxSignalStatus": ifOtnOpuTxSignalStatus,
       "ifOtnOpuRxSignalStatus": ifOtnOpuRxSignalStatus,
       "ifOtnOpuTxClientMaintenanceIndication": ifOtnOpuTxClientMaintenanceIndication,
       "ifOtnOpuTxClientSignalFail": ifOtnOpuTxClientSignalFail,
       "ifOtnOpuRxPayloadMismatch": ifOtnOpuRxPayloadMismatch,
       "ifOtnOpuTxPayloadMismatch": ifOtnOpuTxPayloadMismatch,
       "ifOtnOpuLossOfOpuMultiFrameIdentifier": ifOtnOpuLossOfOpuMultiFrameIdentifier,
       "ifOtnOpuRxClientMaintenanceIndication": ifOtnOpuRxClientMaintenanceIndication,
       "ifOtnOpuConnOduIndex": ifOtnOpuConnOduIndex,
       "ifOtnTpList": ifOtnTpList,
       "ifOtnTpTable": ifOtnTpTable,
       "ifOtnTpEntry": ifOtnTpEntry,
       "ifOtnTpIndex": ifOtnTpIndex,
       "ifOtnTpName": ifOtnTpName,
       "ifOtnTpConnIfBasicIfIndex": ifOtnTpConnIfBasicIfIndex,
       "ifOtnTpUsedTribSlots": ifOtnTpUsedTribSlots,
       "ifOtnTpTribPortId": ifOtnTpTribPortId,
       "ifOtnTpRxMultiplexStructureIdentifierMismatch": ifOtnTpRxMultiplexStructureIdentifierMismatch,
       "ifOtnTpTxSignalStatus": ifOtnTpTxSignalStatus,
       "ifOtnTpRxSignalStatus": ifOtnTpRxSignalStatus,
       "ifOtnTpXcRefOduIndex": ifOtnTpXcRefOduIndex,
       "ifOtnTpTribSlotMask": ifOtnTpTribSlotMask,
       "ifOtnTpTribSlotView": ifOtnTpTribSlotView}
)
