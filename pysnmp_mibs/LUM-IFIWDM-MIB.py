# SNMP MIB module (LUM-IFIWDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFIWDM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:49 2025
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

(lumIfIwdmMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfIwdmMIB",
    "lumModules")

(DisplayStringWithNA,
 EnabledDisabledWithNA,
 FaultStatusWithNA,
 MgmtNameString,
 SignalFormat,
 SignalStatusWithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "DisplayStringWithNA",
    "EnabledDisabledWithNA",
    "FaultStatusWithNA",
    "MgmtNameString",
    "SignalFormat",
    "SignalStatusWithNA",
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

lumIfIwdmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 63)
)
if mibBuilder.loadTexts:
    lumIfIwdmMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-09-30 00:00",
         "2016-06-14 00:00",
         "2015-12-22 00:00",
         "2015-01-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfIwdmConfs_ObjectIdentity = ObjectIdentity
lumIfIwdmConfs = _LumIfIwdmConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1)
)
_LumIfIwdmGroups_ObjectIdentity = ObjectIdentity
lumIfIwdmGroups = _LumIfIwdmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 1)
)
_LumIfIwdmCompl_ObjectIdentity = ObjectIdentity
lumIfIwdmCompl = _LumIfIwdmCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 2)
)
_LumIfIwdmMIBObjects_ObjectIdentity = ObjectIdentity
lumIfIwdmMIBObjects = _LumIfIwdmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2)
)
_IfIwdmGeneral_ObjectIdentity = ObjectIdentity
ifIwdmGeneral = _IfIwdmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 1)
)
_IfIwdmGeneralConfigLastChangeTime_Type = DateAndTime
_IfIwdmGeneralConfigLastChangeTime_Object = MibScalar
ifIwdmGeneralConfigLastChangeTime = _IfIwdmGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 1, 1),
    _IfIwdmGeneralConfigLastChangeTime_Type()
)
ifIwdmGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmGeneralConfigLastChangeTime.setStatus("current")
_IfIwdmGeneralStateLastChangeTime_Type = DateAndTime
_IfIwdmGeneralStateLastChangeTime_Object = MibScalar
ifIwdmGeneralStateLastChangeTime = _IfIwdmGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 1, 2),
    _IfIwdmGeneralStateLastChangeTime_Type()
)
ifIwdmGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmGeneralStateLastChangeTime.setStatus("current")
_IfIwdmGeneralIfIwdmRsTableSize_Type = Unsigned32
_IfIwdmGeneralIfIwdmRsTableSize_Object = MibScalar
ifIwdmGeneralIfIwdmRsTableSize = _IfIwdmGeneralIfIwdmRsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 1, 3),
    _IfIwdmGeneralIfIwdmRsTableSize_Type()
)
ifIwdmGeneralIfIwdmRsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmGeneralIfIwdmRsTableSize.setStatus("current")
_IfIwdmGeneralIfIwdmRsConfigLastChangeTime_Type = DateAndTime
_IfIwdmGeneralIfIwdmRsConfigLastChangeTime_Object = MibScalar
ifIwdmGeneralIfIwdmRsConfigLastChangeTime = _IfIwdmGeneralIfIwdmRsConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 1, 4),
    _IfIwdmGeneralIfIwdmRsConfigLastChangeTime_Type()
)
ifIwdmGeneralIfIwdmRsConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmGeneralIfIwdmRsConfigLastChangeTime.setStatus("current")
_IfIwdmGeneralIfIwdmRsStateLastChangeTime_Type = DateAndTime
_IfIwdmGeneralIfIwdmRsStateLastChangeTime_Object = MibScalar
ifIwdmGeneralIfIwdmRsStateLastChangeTime = _IfIwdmGeneralIfIwdmRsStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 1, 5),
    _IfIwdmGeneralIfIwdmRsStateLastChangeTime_Type()
)
ifIwdmGeneralIfIwdmRsStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmGeneralIfIwdmRsStateLastChangeTime.setStatus("current")
_IfIwdmGeneralIfIwdmMsTableSize_Type = Unsigned32
_IfIwdmGeneralIfIwdmMsTableSize_Object = MibScalar
ifIwdmGeneralIfIwdmMsTableSize = _IfIwdmGeneralIfIwdmMsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 1, 6),
    _IfIwdmGeneralIfIwdmMsTableSize_Type()
)
ifIwdmGeneralIfIwdmMsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmGeneralIfIwdmMsTableSize.setStatus("current")
_IfIwdmGeneralIfIwdmMsConfigLastChangeTime_Type = DateAndTime
_IfIwdmGeneralIfIwdmMsConfigLastChangeTime_Object = MibScalar
ifIwdmGeneralIfIwdmMsConfigLastChangeTime = _IfIwdmGeneralIfIwdmMsConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 1, 7),
    _IfIwdmGeneralIfIwdmMsConfigLastChangeTime_Type()
)
ifIwdmGeneralIfIwdmMsConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmGeneralIfIwdmMsConfigLastChangeTime.setStatus("current")
_IfIwdmGeneralIfIwdmMsStateLastChangeTime_Type = DateAndTime
_IfIwdmGeneralIfIwdmMsStateLastChangeTime_Object = MibScalar
ifIwdmGeneralIfIwdmMsStateLastChangeTime = _IfIwdmGeneralIfIwdmMsStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 1, 8),
    _IfIwdmGeneralIfIwdmMsStateLastChangeTime_Type()
)
ifIwdmGeneralIfIwdmMsStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmGeneralIfIwdmMsStateLastChangeTime.setStatus("current")
_IfIwdmGeneralIfIwdmPathTableSize_Type = Unsigned32
_IfIwdmGeneralIfIwdmPathTableSize_Object = MibScalar
ifIwdmGeneralIfIwdmPathTableSize = _IfIwdmGeneralIfIwdmPathTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 1, 9),
    _IfIwdmGeneralIfIwdmPathTableSize_Type()
)
ifIwdmGeneralIfIwdmPathTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmGeneralIfIwdmPathTableSize.setStatus("current")
_IfIwdmGeneralIfIwdmPathConfigLastChangeTime_Type = DateAndTime
_IfIwdmGeneralIfIwdmPathConfigLastChangeTime_Object = MibScalar
ifIwdmGeneralIfIwdmPathConfigLastChangeTime = _IfIwdmGeneralIfIwdmPathConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 1, 10),
    _IfIwdmGeneralIfIwdmPathConfigLastChangeTime_Type()
)
ifIwdmGeneralIfIwdmPathConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmGeneralIfIwdmPathConfigLastChangeTime.setStatus("current")
_IfIwdmGeneralIfIwdmPathStateLastChangeTime_Type = DateAndTime
_IfIwdmGeneralIfIwdmPathStateLastChangeTime_Object = MibScalar
ifIwdmGeneralIfIwdmPathStateLastChangeTime = _IfIwdmGeneralIfIwdmPathStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 1, 11),
    _IfIwdmGeneralIfIwdmPathStateLastChangeTime_Type()
)
ifIwdmGeneralIfIwdmPathStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmGeneralIfIwdmPathStateLastChangeTime.setStatus("current")
_IfIwdmRsList_ObjectIdentity = ObjectIdentity
ifIwdmRsList = _IfIwdmRsList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2)
)
_IfIwdmRsTable_Object = MibTable
ifIwdmRsTable = _IfIwdmRsTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifIwdmRsTable.setStatus("current")
_IfIwdmRsEntry_Object = MibTableRow
ifIwdmRsEntry = _IfIwdmRsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1)
)
ifIwdmRsEntry.setIndexNames(
    (0, "LUM-IFIWDM-MIB", "ifIwdmRsIndex"),
)
if mibBuilder.loadTexts:
    ifIwdmRsEntry.setStatus("current")
_IfIwdmRsIndex_Type = Unsigned32
_IfIwdmRsIndex_Object = MibTableColumn
ifIwdmRsIndex = _IfIwdmRsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 1),
    _IfIwdmRsIndex_Type()
)
ifIwdmRsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmRsIndex.setStatus("current")
_IfIwdmRsName_Type = MgmtNameString
_IfIwdmRsName_Object = MibTableColumn
ifIwdmRsName = _IfIwdmRsName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 2),
    _IfIwdmRsName_Type()
)
ifIwdmRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmRsName.setStatus("current")


class _IfIwdmRsTraceTransmitted_Type(DisplayStringWithNA):
    """Custom type ifIwdmRsTraceTransmitted based on DisplayStringWithNA"""
    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IfIwdmRsTraceTransmitted_Type.__name__ = "DisplayStringWithNA"
_IfIwdmRsTraceTransmitted_Object = MibTableColumn
ifIwdmRsTraceTransmitted = _IfIwdmRsTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 3),
    _IfIwdmRsTraceTransmitted_Type()
)
ifIwdmRsTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIwdmRsTraceTransmitted.setStatus("current")


class _IfIwdmRsTraceReceived_Type(DisplayStringWithNA):
    """Custom type ifIwdmRsTraceReceived based on DisplayStringWithNA"""
    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IfIwdmRsTraceReceived_Type.__name__ = "DisplayStringWithNA"
_IfIwdmRsTraceReceived_Object = MibTableColumn
ifIwdmRsTraceReceived = _IfIwdmRsTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 4),
    _IfIwdmRsTraceReceived_Type()
)
ifIwdmRsTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmRsTraceReceived.setStatus("current")


class _IfIwdmRsTraceExpected_Type(DisplayStringWithNA):
    """Custom type ifIwdmRsTraceExpected based on DisplayStringWithNA"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IfIwdmRsTraceExpected_Type.__name__ = "DisplayStringWithNA"
_IfIwdmRsTraceExpected_Object = MibTableColumn
ifIwdmRsTraceExpected = _IfIwdmRsTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 5),
    _IfIwdmRsTraceExpected_Type()
)
ifIwdmRsTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIwdmRsTraceExpected.setStatus("current")


class _IfIwdmRsTraceAlarmMode_Type(EnabledDisabledWithNA):
    """Custom type ifIwdmRsTraceAlarmMode based on EnabledDisabledWithNA"""
    defaultValue = 1


_IfIwdmRsTraceAlarmMode_Type.__name__ = "EnabledDisabledWithNA"
_IfIwdmRsTraceAlarmMode_Object = MibTableColumn
ifIwdmRsTraceAlarmMode = _IfIwdmRsTraceAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 6),
    _IfIwdmRsTraceAlarmMode_Type()
)
ifIwdmRsTraceAlarmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmRsTraceAlarmMode.setStatus("current")
_IfIwdmRsTraceTraceMismatch_Type = FaultStatusWithNA
_IfIwdmRsTraceTraceMismatch_Object = MibTableColumn
ifIwdmRsTraceTraceMismatch = _IfIwdmRsTraceTraceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 7),
    _IfIwdmRsTraceTraceMismatch_Type()
)
ifIwdmRsTraceTraceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmRsTraceTraceMismatch.setStatus("current")


class _IfIwdmRsUpId_Type(Unsigned32):
    """Custom type ifIwdmRsUpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IfIwdmRsUpId_Type.__name__ = "Unsigned32"
_IfIwdmRsUpId_Object = MibTableColumn
ifIwdmRsUpId = _IfIwdmRsUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 8),
    _IfIwdmRsUpId_Type()
)
ifIwdmRsUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmRsUpId.setStatus("current")
_IfIwdmRsLossOfFrame_Type = FaultStatusWithNA
_IfIwdmRsLossOfFrame_Object = MibTableColumn
ifIwdmRsLossOfFrame = _IfIwdmRsLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 9),
    _IfIwdmRsLossOfFrame_Type()
)
ifIwdmRsLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmRsLossOfFrame.setStatus("current")
_IfIwdmRsConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfIwdmRsConnIfBasicIfIndex_Object = MibTableColumn
ifIwdmRsConnIfBasicIfIndex = _IfIwdmRsConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 10),
    _IfIwdmRsConnIfBasicIfIndex_Type()
)
ifIwdmRsConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmRsConnIfBasicIfIndex.setStatus("current")
_IfIwdmRsTxSignalStatus_Type = SignalStatusWithNA
_IfIwdmRsTxSignalStatus_Object = MibTableColumn
ifIwdmRsTxSignalStatus = _IfIwdmRsTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 11),
    _IfIwdmRsTxSignalStatus_Type()
)
ifIwdmRsTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmRsTxSignalStatus.setStatus("current")
_IfIwdmRsRxSignalStatus_Type = SignalStatusWithNA
_IfIwdmRsRxSignalStatus_Object = MibTableColumn
ifIwdmRsRxSignalStatus = _IfIwdmRsRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 12),
    _IfIwdmRsRxSignalStatus_Type()
)
ifIwdmRsRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmRsRxSignalStatus.setStatus("current")


class _IfIwdmRsRate_Type(SignalFormat):
    """Custom type ifIwdmRsRate based on SignalFormat"""
    defaultValue = 75


_IfIwdmRsRate_Type.__name__ = "SignalFormat"
_IfIwdmRsRate_Object = MibTableColumn
ifIwdmRsRate = _IfIwdmRsRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 2, 1, 1, 13),
    _IfIwdmRsRate_Type()
)
ifIwdmRsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmRsRate.setStatus("current")
_IfIwdmMsList_ObjectIdentity = ObjectIdentity
ifIwdmMsList = _IfIwdmMsList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 3)
)
_IfIwdmMsTable_Object = MibTable
ifIwdmMsTable = _IfIwdmMsTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifIwdmMsTable.setStatus("current")
_IfIwdmMsEntry_Object = MibTableRow
ifIwdmMsEntry = _IfIwdmMsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 3, 1, 1)
)
ifIwdmMsEntry.setIndexNames(
    (0, "LUM-IFIWDM-MIB", "ifIwdmMsIndex"),
)
if mibBuilder.loadTexts:
    ifIwdmMsEntry.setStatus("current")
_IfIwdmMsIndex_Type = Unsigned32
_IfIwdmMsIndex_Object = MibTableColumn
ifIwdmMsIndex = _IfIwdmMsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 3, 1, 1, 1),
    _IfIwdmMsIndex_Type()
)
ifIwdmMsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmMsIndex.setStatus("current")
_IfIwdmMsName_Type = MgmtNameString
_IfIwdmMsName_Object = MibTableColumn
ifIwdmMsName = _IfIwdmMsName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 3, 1, 1, 2),
    _IfIwdmMsName_Type()
)
ifIwdmMsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmMsName.setStatus("current")
_IfIwdmMsAlarmIndicationSignal_Type = FaultStatusWithNA
_IfIwdmMsAlarmIndicationSignal_Object = MibTableColumn
ifIwdmMsAlarmIndicationSignal = _IfIwdmMsAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 3, 1, 1, 3),
    _IfIwdmMsAlarmIndicationSignal_Type()
)
ifIwdmMsAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmMsAlarmIndicationSignal.setStatus("current")
_IfIwdmMsBackwardDefectIndication_Type = FaultStatusWithNA
_IfIwdmMsBackwardDefectIndication_Object = MibTableColumn
ifIwdmMsBackwardDefectIndication = _IfIwdmMsBackwardDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 3, 1, 1, 4),
    _IfIwdmMsBackwardDefectIndication_Type()
)
ifIwdmMsBackwardDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmMsBackwardDefectIndication.setStatus("current")


class _IfIwdmMsUpId_Type(Unsigned32):
    """Custom type ifIwdmMsUpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IfIwdmMsUpId_Type.__name__ = "Unsigned32"
_IfIwdmMsUpId_Object = MibTableColumn
ifIwdmMsUpId = _IfIwdmMsUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 3, 1, 1, 5),
    _IfIwdmMsUpId_Type()
)
ifIwdmMsUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmMsUpId.setStatus("current")
_IfIwdmMsConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfIwdmMsConnIfBasicIfIndex_Object = MibTableColumn
ifIwdmMsConnIfBasicIfIndex = _IfIwdmMsConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 3, 1, 1, 6),
    _IfIwdmMsConnIfBasicIfIndex_Type()
)
ifIwdmMsConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmMsConnIfBasicIfIndex.setStatus("current")
_IfIwdmMsTxSignalStatus_Type = SignalStatusWithNA
_IfIwdmMsTxSignalStatus_Object = MibTableColumn
ifIwdmMsTxSignalStatus = _IfIwdmMsTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 3, 1, 1, 7),
    _IfIwdmMsTxSignalStatus_Type()
)
ifIwdmMsTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmMsTxSignalStatus.setStatus("current")
_IfIwdmMsRxSignalStatus_Type = SignalStatusWithNA
_IfIwdmMsRxSignalStatus_Object = MibTableColumn
ifIwdmMsRxSignalStatus = _IfIwdmMsRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 3, 1, 1, 8),
    _IfIwdmMsRxSignalStatus_Type()
)
ifIwdmMsRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmMsRxSignalStatus.setStatus("current")


class _IfIwdmMsRate_Type(SignalFormat):
    """Custom type ifIwdmMsRate based on SignalFormat"""
    defaultValue = 75


_IfIwdmMsRate_Type.__name__ = "SignalFormat"
_IfIwdmMsRate_Object = MibTableColumn
ifIwdmMsRate = _IfIwdmMsRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 3, 1, 1, 9),
    _IfIwdmMsRate_Type()
)
ifIwdmMsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmMsRate.setStatus("current")
_IfIwdmPathList_ObjectIdentity = ObjectIdentity
ifIwdmPathList = _IfIwdmPathList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 4)
)
_IfIwdmPathTable_Object = MibTable
ifIwdmPathTable = _IfIwdmPathTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ifIwdmPathTable.setStatus("current")
_IfIwdmPathEntry_Object = MibTableRow
ifIwdmPathEntry = _IfIwdmPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 4, 1, 1)
)
ifIwdmPathEntry.setIndexNames(
    (0, "LUM-IFIWDM-MIB", "ifIwdmPathIndex"),
)
if mibBuilder.loadTexts:
    ifIwdmPathEntry.setStatus("current")
_IfIwdmPathIndex_Type = Unsigned32
_IfIwdmPathIndex_Object = MibTableColumn
ifIwdmPathIndex = _IfIwdmPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 4, 1, 1, 1),
    _IfIwdmPathIndex_Type()
)
ifIwdmPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmPathIndex.setStatus("current")
_IfIwdmPathName_Type = MgmtNameString
_IfIwdmPathName_Object = MibTableColumn
ifIwdmPathName = _IfIwdmPathName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 4, 1, 1, 2),
    _IfIwdmPathName_Type()
)
ifIwdmPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmPathName.setStatus("current")
_IfIwdmPathBackwardDefectIndication_Type = FaultStatusWithNA
_IfIwdmPathBackwardDefectIndication_Object = MibTableColumn
ifIwdmPathBackwardDefectIndication = _IfIwdmPathBackwardDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 4, 1, 1, 3),
    _IfIwdmPathBackwardDefectIndication_Type()
)
ifIwdmPathBackwardDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmPathBackwardDefectIndication.setStatus("current")
_IfIwdmPathClientSignalFailure_Type = FaultStatusWithNA
_IfIwdmPathClientSignalFailure_Object = MibTableColumn
ifIwdmPathClientSignalFailure = _IfIwdmPathClientSignalFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 4, 1, 1, 4),
    _IfIwdmPathClientSignalFailure_Type()
)
ifIwdmPathClientSignalFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmPathClientSignalFailure.setStatus("current")


class _IfIwdmPathUId_Type(Unsigned32):
    """Custom type ifIwdmPathUId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IfIwdmPathUId_Type.__name__ = "Unsigned32"
_IfIwdmPathUId_Object = MibTableColumn
ifIwdmPathUId = _IfIwdmPathUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 4, 1, 1, 5),
    _IfIwdmPathUId_Type()
)
ifIwdmPathUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmPathUId.setStatus("current")
_IfIwdmPathConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfIwdmPathConnIfBasicIfIndex_Object = MibTableColumn
ifIwdmPathConnIfBasicIfIndex = _IfIwdmPathConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 4, 1, 1, 6),
    _IfIwdmPathConnIfBasicIfIndex_Type()
)
ifIwdmPathConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmPathConnIfBasicIfIndex.setStatus("current")
_IfIwdmPathTxSignalStatus_Type = SignalStatusWithNA
_IfIwdmPathTxSignalStatus_Object = MibTableColumn
ifIwdmPathTxSignalStatus = _IfIwdmPathTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 4, 1, 1, 7),
    _IfIwdmPathTxSignalStatus_Type()
)
ifIwdmPathTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmPathTxSignalStatus.setStatus("current")
_IfIwdmPathRxSignalStatus_Type = SignalStatusWithNA
_IfIwdmPathRxSignalStatus_Object = MibTableColumn
ifIwdmPathRxSignalStatus = _IfIwdmPathRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 4, 1, 1, 8),
    _IfIwdmPathRxSignalStatus_Type()
)
ifIwdmPathRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmPathRxSignalStatus.setStatus("current")


class _IfIwdmPathRate_Type(SignalFormat):
    """Custom type ifIwdmPathRate based on SignalFormat"""
    defaultValue = 2147483647


_IfIwdmPathRate_Type.__name__ = "SignalFormat"
_IfIwdmPathRate_Object = MibTableColumn
ifIwdmPathRate = _IfIwdmPathRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 2, 4, 1, 1, 9),
    _IfIwdmPathRate_Type()
)
ifIwdmPathRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIwdmPathRate.setStatus("current")

# Managed Objects groups

ifIwdmGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 1, 1)
)
ifIwdmGeneralGroupV1.setObjects(
      *(("LUM-IFIWDM-MIB", "ifIwdmGeneralConfigLastChangeTime"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralStateLastChangeTime"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmRsTableSize"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmRsConfigLastChangeTime"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmRsStateLastChangeTime"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmMsTableSize"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmMsConfigLastChangeTime"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmMsStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifIwdmGeneralGroupV1.setStatus("deprecated")

ifIwdmGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 1, 2)
)
ifIwdmGeneralGroupV2.setObjects(
      *(("LUM-IFIWDM-MIB", "ifIwdmGeneralConfigLastChangeTime"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralStateLastChangeTime"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmRsTableSize"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmRsConfigLastChangeTime"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmRsStateLastChangeTime"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmMsTableSize"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmMsConfigLastChangeTime"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmMsStateLastChangeTime"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmPathTableSize"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmPathConfigLastChangeTime"),
        ("LUM-IFIWDM-MIB", "ifIwdmGeneralIfIwdmPathStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifIwdmGeneralGroupV2.setStatus("current")

ifIwdmRsGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 1, 3)
)
ifIwdmRsGroupV1.setObjects(
      *(("LUM-IFIWDM-MIB", "ifIwdmRsIndex"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsName"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceTransmitted"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceReceived"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceExpected"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceAlarmMode"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceTraceMismatch"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsUpId"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsLossOfFrame"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsConnIfBasicIfIndex"))
)
if mibBuilder.loadTexts:
    ifIwdmRsGroupV1.setStatus("deprecated")

ifIwdmMsGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 1, 4)
)
ifIwdmMsGroupV1.setObjects(
      *(("LUM-IFIWDM-MIB", "ifIwdmMsIndex"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsName"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsAlarmIndicationSignal"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsBackwardDefectIndication"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsUpId"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsConnIfBasicIfIndex"))
)
if mibBuilder.loadTexts:
    ifIwdmMsGroupV1.setStatus("deprecated")

ifIwdmRsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 1, 5)
)
ifIwdmRsGroupV2.setObjects(
      *(("LUM-IFIWDM-MIB", "ifIwdmRsIndex"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsName"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceTransmitted"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceReceived"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceExpected"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceAlarmMode"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceTraceMismatch"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsUpId"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsLossOfFrame"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsConnIfBasicIfIndex"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTxSignalStatus"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsRxSignalStatus"))
)
if mibBuilder.loadTexts:
    ifIwdmRsGroupV2.setStatus("deprecated")

ifIwdmMsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 1, 6)
)
ifIwdmMsGroupV2.setObjects(
      *(("LUM-IFIWDM-MIB", "ifIwdmMsIndex"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsName"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsAlarmIndicationSignal"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsBackwardDefectIndication"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsUpId"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsConnIfBasicIfIndex"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsTxSignalStatus"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsRxSignalStatus"))
)
if mibBuilder.loadTexts:
    ifIwdmMsGroupV2.setStatus("deprecated")

ifIwdmRsGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 1, 7)
)
ifIwdmRsGroupV3.setObjects(
      *(("LUM-IFIWDM-MIB", "ifIwdmRsIndex"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsName"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceTransmitted"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceReceived"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceExpected"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceAlarmMode"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTraceTraceMismatch"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsUpId"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsLossOfFrame"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsConnIfBasicIfIndex"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsTxSignalStatus"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsRxSignalStatus"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsRate"))
)
if mibBuilder.loadTexts:
    ifIwdmRsGroupV3.setStatus("current")

ifIwdmMsGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 1, 8)
)
ifIwdmMsGroupV3.setObjects(
      *(("LUM-IFIWDM-MIB", "ifIwdmMsIndex"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsName"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsAlarmIndicationSignal"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsBackwardDefectIndication"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsUpId"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsConnIfBasicIfIndex"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsTxSignalStatus"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsRxSignalStatus"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsRate"))
)
if mibBuilder.loadTexts:
    ifIwdmMsGroupV3.setStatus("current")

ifIwdmPathGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 1, 9)
)
ifIwdmPathGroupV1.setObjects(
      *(("LUM-IFIWDM-MIB", "ifIwdmPathIndex"),
        ("LUM-IFIWDM-MIB", "ifIwdmPathName"),
        ("LUM-IFIWDM-MIB", "ifIwdmPathUId"),
        ("LUM-IFIWDM-MIB", "ifIwdmPathBackwardDefectIndication"),
        ("LUM-IFIWDM-MIB", "ifIwdmPathClientSignalFailure"),
        ("LUM-IFIWDM-MIB", "ifIwdmPathConnIfBasicIfIndex"),
        ("LUM-IFIWDM-MIB", "ifIwdmPathTxSignalStatus"),
        ("LUM-IFIWDM-MIB", "ifIwdmPathRxSignalStatus"),
        ("LUM-IFIWDM-MIB", "ifIwdmPathRate"))
)
if mibBuilder.loadTexts:
    ifIwdmPathGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfIwdmComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 2, 1)
)
lumIfIwdmComplV1.setObjects(
      *(("LUM-IFIWDM-MIB", "ifIwdmGeneralGroupV1"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsGroupV1"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfIwdmComplV1.setStatus(
        "deprecated"
    )

lumIfIwdmComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 2, 2)
)
lumIfIwdmComplV2.setObjects(
      *(("LUM-IFIWDM-MIB", "ifIwdmGeneralGroupV1"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsGroupV2"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfIwdmComplV2.setStatus(
        "deprecated"
    )

lumIfIwdmComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63, 1, 2, 3)
)
lumIfIwdmComplV3.setObjects(
      *(("LUM-IFIWDM-MIB", "ifIwdmGeneralGroupV2"),
        ("LUM-IFIWDM-MIB", "ifIwdmRsGroupV3"),
        ("LUM-IFIWDM-MIB", "ifIwdmMsGroupV3"),
        ("LUM-IFIWDM-MIB", "ifIwdmPathGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfIwdmComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFIWDM-MIB",
    **{"lumIfIwdmMIBModule": lumIfIwdmMIBModule,
       "lumIfIwdmConfs": lumIfIwdmConfs,
       "lumIfIwdmGroups": lumIfIwdmGroups,
       "ifIwdmGeneralGroupV1": ifIwdmGeneralGroupV1,
       "ifIwdmGeneralGroupV2": ifIwdmGeneralGroupV2,
       "ifIwdmRsGroupV1": ifIwdmRsGroupV1,
       "ifIwdmMsGroupV1": ifIwdmMsGroupV1,
       "ifIwdmRsGroupV2": ifIwdmRsGroupV2,
       "ifIwdmMsGroupV2": ifIwdmMsGroupV2,
       "ifIwdmRsGroupV3": ifIwdmRsGroupV3,
       "ifIwdmMsGroupV3": ifIwdmMsGroupV3,
       "ifIwdmPathGroupV1": ifIwdmPathGroupV1,
       "lumIfIwdmCompl": lumIfIwdmCompl,
       "lumIfIwdmComplV1": lumIfIwdmComplV1,
       "lumIfIwdmComplV2": lumIfIwdmComplV2,
       "lumIfIwdmComplV3": lumIfIwdmComplV3,
       "lumIfIwdmMIBObjects": lumIfIwdmMIBObjects,
       "ifIwdmGeneral": ifIwdmGeneral,
       "ifIwdmGeneralConfigLastChangeTime": ifIwdmGeneralConfigLastChangeTime,
       "ifIwdmGeneralStateLastChangeTime": ifIwdmGeneralStateLastChangeTime,
       "ifIwdmGeneralIfIwdmRsTableSize": ifIwdmGeneralIfIwdmRsTableSize,
       "ifIwdmGeneralIfIwdmRsConfigLastChangeTime": ifIwdmGeneralIfIwdmRsConfigLastChangeTime,
       "ifIwdmGeneralIfIwdmRsStateLastChangeTime": ifIwdmGeneralIfIwdmRsStateLastChangeTime,
       "ifIwdmGeneralIfIwdmMsTableSize": ifIwdmGeneralIfIwdmMsTableSize,
       "ifIwdmGeneralIfIwdmMsConfigLastChangeTime": ifIwdmGeneralIfIwdmMsConfigLastChangeTime,
       "ifIwdmGeneralIfIwdmMsStateLastChangeTime": ifIwdmGeneralIfIwdmMsStateLastChangeTime,
       "ifIwdmGeneralIfIwdmPathTableSize": ifIwdmGeneralIfIwdmPathTableSize,
       "ifIwdmGeneralIfIwdmPathConfigLastChangeTime": ifIwdmGeneralIfIwdmPathConfigLastChangeTime,
       "ifIwdmGeneralIfIwdmPathStateLastChangeTime": ifIwdmGeneralIfIwdmPathStateLastChangeTime,
       "ifIwdmRsList": ifIwdmRsList,
       "ifIwdmRsTable": ifIwdmRsTable,
       "ifIwdmRsEntry": ifIwdmRsEntry,
       "ifIwdmRsIndex": ifIwdmRsIndex,
       "ifIwdmRsName": ifIwdmRsName,
       "ifIwdmRsTraceTransmitted": ifIwdmRsTraceTransmitted,
       "ifIwdmRsTraceReceived": ifIwdmRsTraceReceived,
       "ifIwdmRsTraceExpected": ifIwdmRsTraceExpected,
       "ifIwdmRsTraceAlarmMode": ifIwdmRsTraceAlarmMode,
       "ifIwdmRsTraceTraceMismatch": ifIwdmRsTraceTraceMismatch,
       "ifIwdmRsUpId": ifIwdmRsUpId,
       "ifIwdmRsLossOfFrame": ifIwdmRsLossOfFrame,
       "ifIwdmRsConnIfBasicIfIndex": ifIwdmRsConnIfBasicIfIndex,
       "ifIwdmRsTxSignalStatus": ifIwdmRsTxSignalStatus,
       "ifIwdmRsRxSignalStatus": ifIwdmRsRxSignalStatus,
       "ifIwdmRsRate": ifIwdmRsRate,
       "ifIwdmMsList": ifIwdmMsList,
       "ifIwdmMsTable": ifIwdmMsTable,
       "ifIwdmMsEntry": ifIwdmMsEntry,
       "ifIwdmMsIndex": ifIwdmMsIndex,
       "ifIwdmMsName": ifIwdmMsName,
       "ifIwdmMsAlarmIndicationSignal": ifIwdmMsAlarmIndicationSignal,
       "ifIwdmMsBackwardDefectIndication": ifIwdmMsBackwardDefectIndication,
       "ifIwdmMsUpId": ifIwdmMsUpId,
       "ifIwdmMsConnIfBasicIfIndex": ifIwdmMsConnIfBasicIfIndex,
       "ifIwdmMsTxSignalStatus": ifIwdmMsTxSignalStatus,
       "ifIwdmMsRxSignalStatus": ifIwdmMsRxSignalStatus,
       "ifIwdmMsRate": ifIwdmMsRate,
       "ifIwdmPathList": ifIwdmPathList,
       "ifIwdmPathTable": ifIwdmPathTable,
       "ifIwdmPathEntry": ifIwdmPathEntry,
       "ifIwdmPathIndex": ifIwdmPathIndex,
       "ifIwdmPathName": ifIwdmPathName,
       "ifIwdmPathBackwardDefectIndication": ifIwdmPathBackwardDefectIndication,
       "ifIwdmPathClientSignalFailure": ifIwdmPathClientSignalFailure,
       "ifIwdmPathUId": ifIwdmPathUId,
       "ifIwdmPathConnIfBasicIfIndex": ifIwdmPathConnIfBasicIfIndex,
       "ifIwdmPathTxSignalStatus": ifIwdmPathTxSignalStatus,
       "ifIwdmPathRxSignalStatus": ifIwdmPathRxSignalStatus,
       "ifIwdmPathRate": ifIwdmPathRate}
)
