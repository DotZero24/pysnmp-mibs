# SNMP MIB module (LUM-IFBASIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFBASIC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:26 2025
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

(lumIfBasicMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfBasicMIB",
    "lumModules")

(AdminStatusWithNA,
 AutoAlarmStatus,
 CommandString,
 ConnectorType,
 DisplayStringWithNA,
 EnabledDisabledWithNA,
 FaultStatusWithNA,
 InterfaceStatus,
 InterfaceType,
 Layer,
 MgmtNameString,
 OperStatusWithNA,
 OpticalLayerMappingType,
 PhysicalLayerMappingType,
 ResetWithNA,
 SignalDirection,
 SignalFormat,
 SignalStatusWithNA,
 Time7200min,
 Time7200minNo0,
 TribPortIdType,
 TruthValueWithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "AdminStatusWithNA",
    "AutoAlarmStatus",
    "CommandString",
    "ConnectorType",
    "DisplayStringWithNA",
    "EnabledDisabledWithNA",
    "FaultStatusWithNA",
    "InterfaceStatus",
    "InterfaceType",
    "Layer",
    "MgmtNameString",
    "OperStatusWithNA",
    "OpticalLayerMappingType",
    "PhysicalLayerMappingType",
    "ResetWithNA",
    "SignalDirection",
    "SignalFormat",
    "SignalStatusWithNA",
    "Time7200min",
    "Time7200minNo0",
    "TribPortIdType",
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

lumIfBasicMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 46)
)
if mibBuilder.loadTexts:
    lumIfBasicMIBModule.setRevisions(
        ("2018-12-31 00:00",
         "2018-06-29 00:00",
         "2017-06-15 00:00",
         "2016-11-30 00:00",
         "2016-11-04 00:00",
         "2016-01-31 00:00",
         "2015-12-22 00:00",
         "2015-10-30 00:00",
         "2014-09-30 00:00",
         "2014-05-16 00:00",
         "2013-11-15 00:00",
         "2012-11-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfBasicConfs_ObjectIdentity = ObjectIdentity
lumIfBasicConfs = _LumIfBasicConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1)
)
_LumIfBasicGroups_ObjectIdentity = ObjectIdentity
lumIfBasicGroups = _LumIfBasicGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1)
)
_LumIfBasicCompl_ObjectIdentity = ObjectIdentity
lumIfBasicCompl = _LumIfBasicCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 2)
)
_LumIfBasicMIBObjects_ObjectIdentity = ObjectIdentity
lumIfBasicMIBObjects = _LumIfBasicMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2)
)
_IfBasicGeneral_ObjectIdentity = ObjectIdentity
ifBasicGeneral = _IfBasicGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 1)
)
_IfBasicGeneralConfigLastChangeTime_Type = DateAndTime
_IfBasicGeneralConfigLastChangeTime_Object = MibScalar
ifBasicGeneralConfigLastChangeTime = _IfBasicGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 1, 1),
    _IfBasicGeneralConfigLastChangeTime_Type()
)
ifBasicGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicGeneralConfigLastChangeTime.setStatus("current")
_IfBasicGeneralStateLastChangeTime_Type = DateAndTime
_IfBasicGeneralStateLastChangeTime_Object = MibScalar
ifBasicGeneralStateLastChangeTime = _IfBasicGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 1, 2),
    _IfBasicGeneralStateLastChangeTime_Type()
)
ifBasicGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicGeneralStateLastChangeTime.setStatus("current")
_IfBasicGeneralIfBasicIfTableSize_Type = Unsigned32
_IfBasicGeneralIfBasicIfTableSize_Object = MibScalar
ifBasicGeneralIfBasicIfTableSize = _IfBasicGeneralIfBasicIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 1, 3),
    _IfBasicGeneralIfBasicIfTableSize_Type()
)
ifBasicGeneralIfBasicIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicGeneralIfBasicIfTableSize.setStatus("current")
_IfBasicGeneralIfBasicIfConfigLastChangeTime_Type = DateAndTime
_IfBasicGeneralIfBasicIfConfigLastChangeTime_Object = MibScalar
ifBasicGeneralIfBasicIfConfigLastChangeTime = _IfBasicGeneralIfBasicIfConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 1, 4),
    _IfBasicGeneralIfBasicIfConfigLastChangeTime_Type()
)
ifBasicGeneralIfBasicIfConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicGeneralIfBasicIfConfigLastChangeTime.setStatus("current")
_IfBasicGeneralIfBasicIfStateLastChangeTime_Type = DateAndTime
_IfBasicGeneralIfBasicIfStateLastChangeTime_Object = MibScalar
ifBasicGeneralIfBasicIfStateLastChangeTime = _IfBasicGeneralIfBasicIfStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 1, 5),
    _IfBasicGeneralIfBasicIfStateLastChangeTime_Type()
)
ifBasicGeneralIfBasicIfStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicGeneralIfBasicIfStateLastChangeTime.setStatus("current")
_IfBasicGeneralIfBasicAdminTableSize_Type = Unsigned32
_IfBasicGeneralIfBasicAdminTableSize_Object = MibScalar
ifBasicGeneralIfBasicAdminTableSize = _IfBasicGeneralIfBasicAdminTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 1, 6),
    _IfBasicGeneralIfBasicAdminTableSize_Type()
)
ifBasicGeneralIfBasicAdminTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicGeneralIfBasicAdminTableSize.setStatus("current")
_IfBasicGeneralIfBasicAdminConfigLastChangeTime_Type = DateAndTime
_IfBasicGeneralIfBasicAdminConfigLastChangeTime_Object = MibScalar
ifBasicGeneralIfBasicAdminConfigLastChangeTime = _IfBasicGeneralIfBasicAdminConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 1, 7),
    _IfBasicGeneralIfBasicAdminConfigLastChangeTime_Type()
)
ifBasicGeneralIfBasicAdminConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicGeneralIfBasicAdminConfigLastChangeTime.setStatus("current")
_IfBasicGeneralIfBasicAdminStateLastChangeTime_Type = DateAndTime
_IfBasicGeneralIfBasicAdminStateLastChangeTime_Object = MibScalar
ifBasicGeneralIfBasicAdminStateLastChangeTime = _IfBasicGeneralIfBasicAdminStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 1, 8),
    _IfBasicGeneralIfBasicAdminStateLastChangeTime_Type()
)
ifBasicGeneralIfBasicAdminStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicGeneralIfBasicAdminStateLastChangeTime.setStatus("current")
_IfBasicGeneralIfBasicSignalTableSize_Type = Unsigned32
_IfBasicGeneralIfBasicSignalTableSize_Object = MibScalar
ifBasicGeneralIfBasicSignalTableSize = _IfBasicGeneralIfBasicSignalTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 1, 9),
    _IfBasicGeneralIfBasicSignalTableSize_Type()
)
ifBasicGeneralIfBasicSignalTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicGeneralIfBasicSignalTableSize.setStatus("current")
_IfBasicGeneralIfBasicSignalConfigLastChangeTime_Type = DateAndTime
_IfBasicGeneralIfBasicSignalConfigLastChangeTime_Object = MibScalar
ifBasicGeneralIfBasicSignalConfigLastChangeTime = _IfBasicGeneralIfBasicSignalConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 1, 10),
    _IfBasicGeneralIfBasicSignalConfigLastChangeTime_Type()
)
ifBasicGeneralIfBasicSignalConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicGeneralIfBasicSignalConfigLastChangeTime.setStatus("current")
_IfBasicGeneralIfBasicSignalStateLastChangeTime_Type = DateAndTime
_IfBasicGeneralIfBasicSignalStateLastChangeTime_Object = MibScalar
ifBasicGeneralIfBasicSignalStateLastChangeTime = _IfBasicGeneralIfBasicSignalStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 1, 11),
    _IfBasicGeneralIfBasicSignalStateLastChangeTime_Type()
)
ifBasicGeneralIfBasicSignalStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicGeneralIfBasicSignalStateLastChangeTime.setStatus("current")
_IfBasicIfList_ObjectIdentity = ObjectIdentity
ifBasicIfList = _IfBasicIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 2)
)
_IfBasicIfTable_Object = MibTable
ifBasicIfTable = _IfBasicIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifBasicIfTable.setStatus("current")
_IfBasicIfEntry_Object = MibTableRow
ifBasicIfEntry = _IfBasicIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 2, 1, 1)
)
ifBasicIfEntry.setIndexNames(
    (0, "LUM-IFBASIC-MIB", "ifBasicIfIndex"),
)
if mibBuilder.loadTexts:
    ifBasicIfEntry.setStatus("current")
_IfBasicIfIndex_Type = Unsigned32
_IfBasicIfIndex_Object = MibTableColumn
ifBasicIfIndex = _IfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 2, 1, 1, 1),
    _IfBasicIfIndex_Type()
)
ifBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicIfIndex.setStatus("current")
_IfBasicIfName_Type = MgmtNameString
_IfBasicIfName_Object = MibTableColumn
ifBasicIfName = _IfBasicIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 2, 1, 1, 2),
    _IfBasicIfName_Type()
)
ifBasicIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicIfName.setStatus("current")
_IfBasicIfTxSignalStatus_Type = SignalStatusWithNA
_IfBasicIfTxSignalStatus_Object = MibTableColumn
ifBasicIfTxSignalStatus = _IfBasicIfTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 2, 1, 1, 3),
    _IfBasicIfTxSignalStatus_Type()
)
ifBasicIfTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicIfTxSignalStatus.setStatus("current")
_IfBasicIfRxSignalStatus_Type = SignalStatusWithNA
_IfBasicIfRxSignalStatus_Object = MibTableColumn
ifBasicIfRxSignalStatus = _IfBasicIfRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 2, 1, 1, 4),
    _IfBasicIfRxSignalStatus_Type()
)
ifBasicIfRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicIfRxSignalStatus.setStatus("current")


class _IfBasicIfUpId_Type(Unsigned32):
    """Custom type ifBasicIfUpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IfBasicIfUpId_Type.__name__ = "Unsigned32"
_IfBasicIfUpId_Object = MibTableColumn
ifBasicIfUpId = _IfBasicIfUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 2, 1, 1, 5),
    _IfBasicIfUpId_Type()
)
ifBasicIfUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicIfUpId.setStatus("current")
_IfBasicIfAid_Type = DisplayString
_IfBasicIfAid_Object = MibTableColumn
ifBasicIfAid = _IfBasicIfAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 2, 1, 1, 6),
    _IfBasicIfAid_Type()
)
ifBasicIfAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicIfAid.setStatus("current")
_IfBasicIfPhysicalLocation_Type = DisplayString
_IfBasicIfPhysicalLocation_Object = MibTableColumn
ifBasicIfPhysicalLocation = _IfBasicIfPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 2, 1, 1, 7),
    _IfBasicIfPhysicalLocation_Type()
)
ifBasicIfPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicIfPhysicalLocation.setStatus("current")
_IfBasicAdminList_ObjectIdentity = ObjectIdentity
ifBasicAdminList = _IfBasicAdminList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3)
)
_IfBasicAdminTable_Object = MibTable
ifBasicAdminTable = _IfBasicAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifBasicAdminTable.setStatus("current")
_IfBasicAdminEntry_Object = MibTableRow
ifBasicAdminEntry = _IfBasicAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1)
)
ifBasicAdminEntry.setIndexNames(
    (0, "LUM-IFBASIC-MIB", "ifBasicAdminIndex"),
)
if mibBuilder.loadTexts:
    ifBasicAdminEntry.setStatus("current")
_IfBasicAdminIndex_Type = Unsigned32
_IfBasicAdminIndex_Object = MibTableColumn
ifBasicAdminIndex = _IfBasicAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 1),
    _IfBasicAdminIndex_Type()
)
ifBasicAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicAdminIndex.setStatus("current")
_IfBasicAdminName_Type = MgmtNameString
_IfBasicAdminName_Object = MibTableColumn
ifBasicAdminName = _IfBasicAdminName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 2),
    _IfBasicAdminName_Type()
)
ifBasicAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifBasicAdminName.setStatus("current")


class _IfBasicAdminDescr_Type(DisplayStringWithNA):
    """Custom type ifBasicAdminDescr based on DisplayStringWithNA"""
    defaultValue = OctetString("")


_IfBasicAdminDescr_Type.__name__ = "DisplayStringWithNA"
_IfBasicAdminDescr_Object = MibTableColumn
ifBasicAdminDescr = _IfBasicAdminDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 3),
    _IfBasicAdminDescr_Type()
)
ifBasicAdminDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicAdminDescr.setStatus("current")
_IfBasicAdminSubrack_Type = Unsigned32WithNA
_IfBasicAdminSubrack_Object = MibTableColumn
ifBasicAdminSubrack = _IfBasicAdminSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 4),
    _IfBasicAdminSubrack_Type()
)
ifBasicAdminSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifBasicAdminSubrack.setStatus("current")
_IfBasicAdminSlot_Type = Unsigned32WithNA
_IfBasicAdminSlot_Object = MibTableColumn
ifBasicAdminSlot = _IfBasicAdminSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 5),
    _IfBasicAdminSlot_Type()
)
ifBasicAdminSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifBasicAdminSlot.setStatus("current")
_IfBasicAdminTxPort_Type = Unsigned32WithNA
_IfBasicAdminTxPort_Object = MibTableColumn
ifBasicAdminTxPort = _IfBasicAdminTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 6),
    _IfBasicAdminTxPort_Type()
)
ifBasicAdminTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifBasicAdminTxPort.setStatus("current")
_IfBasicAdminRxPort_Type = Unsigned32WithNA
_IfBasicAdminRxPort_Object = MibTableColumn
ifBasicAdminRxPort = _IfBasicAdminRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 7),
    _IfBasicAdminRxPort_Type()
)
ifBasicAdminRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifBasicAdminRxPort.setStatus("current")


class _IfBasicAdminAdminStatus_Type(AdminStatusWithNA):
    """Custom type ifBasicAdminAdminStatus based on AdminStatusWithNA"""
    defaultValue = 3


_IfBasicAdminAdminStatus_Type.__name__ = "AdminStatusWithNA"
_IfBasicAdminAdminStatus_Object = MibTableColumn
ifBasicAdminAdminStatus = _IfBasicAdminAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 8),
    _IfBasicAdminAdminStatus_Type()
)
ifBasicAdminAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicAdminAdminStatus.setStatus("current")


class _IfBasicAdminOperStatus_Type(OperStatusWithNA):
    """Custom type ifBasicAdminOperStatus based on OperStatusWithNA"""
    defaultValue = 1


_IfBasicAdminOperStatus_Type.__name__ = "OperStatusWithNA"
_IfBasicAdminOperStatus_Object = MibTableColumn
ifBasicAdminOperStatus = _IfBasicAdminOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 9),
    _IfBasicAdminOperStatus_Type()
)
ifBasicAdminOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicAdminOperStatus.setStatus("current")


class _IfBasicAdminAutoAlarmEnableStatus_Type(AutoAlarmStatus):
    """Custom type ifBasicAdminAutoAlarmEnableStatus based on AutoAlarmStatus"""
    defaultValue = 1


_IfBasicAdminAutoAlarmEnableStatus_Type.__name__ = "AutoAlarmStatus"
_IfBasicAdminAutoAlarmEnableStatus_Object = MibTableColumn
ifBasicAdminAutoAlarmEnableStatus = _IfBasicAdminAutoAlarmEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 10),
    _IfBasicAdminAutoAlarmEnableStatus_Type()
)
ifBasicAdminAutoAlarmEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicAdminAutoAlarmEnableStatus.setStatus("current")


class _IfBasicAdminAutoAlarmEnableReset_Type(ResetWithNA):
    """Custom type ifBasicAdminAutoAlarmEnableReset based on ResetWithNA"""
    defaultValue = 2


_IfBasicAdminAutoAlarmEnableReset_Type.__name__ = "ResetWithNA"
_IfBasicAdminAutoAlarmEnableReset_Object = MibTableColumn
ifBasicAdminAutoAlarmEnableReset = _IfBasicAdminAutoAlarmEnableReset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 11),
    _IfBasicAdminAutoAlarmEnableReset_Type()
)
ifBasicAdminAutoAlarmEnableReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicAdminAutoAlarmEnableReset.setStatus("current")
_IfBasicAdminInterfaceStatus_Type = InterfaceStatus
_IfBasicAdminInterfaceStatus_Object = MibTableColumn
ifBasicAdminInterfaceStatus = _IfBasicAdminInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 12),
    _IfBasicAdminInterfaceStatus_Type()
)
ifBasicAdminInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicAdminInterfaceStatus.setStatus("current")


class _IfBasicAdminIfNo_Type(Unsigned32WithNA):
    """Custom type ifBasicAdminIfNo based on Unsigned32WithNA"""
    defaultValue = 2147483647


_IfBasicAdminIfNo_Type.__name__ = "Unsigned32WithNA"
_IfBasicAdminIfNo_Object = MibTableColumn
ifBasicAdminIfNo = _IfBasicAdminIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 13),
    _IfBasicAdminIfNo_Type()
)
ifBasicAdminIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifBasicAdminIfNo.setStatus("current")


class _IfBasicAdminIfType_Type(InterfaceType):
    """Custom type ifBasicAdminIfType based on InterfaceType"""
    defaultValue = 2147483647


_IfBasicAdminIfType_Type.__name__ = "InterfaceType"
_IfBasicAdminIfType_Object = MibTableColumn
ifBasicAdminIfType = _IfBasicAdminIfType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 14),
    _IfBasicAdminIfType_Type()
)
ifBasicAdminIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifBasicAdminIfType.setStatus("current")


class _IfBasicAdminNotAvailableForUse_Type(TruthValueWithNA):
    """Custom type ifBasicAdminNotAvailableForUse based on TruthValueWithNA"""
    defaultValue = 2147483647


_IfBasicAdminNotAvailableForUse_Type.__name__ = "TruthValueWithNA"
_IfBasicAdminNotAvailableForUse_Object = MibTableColumn
ifBasicAdminNotAvailableForUse = _IfBasicAdminNotAvailableForUse_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 3, 1, 1, 15),
    _IfBasicAdminNotAvailableForUse_Type()
)
ifBasicAdminNotAvailableForUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicAdminNotAvailableForUse.setStatus("current")
_IfBasicSignalList_ObjectIdentity = ObjectIdentity
ifBasicSignalList = _IfBasicSignalList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4)
)
_IfBasicSignalTable_Object = MibTable
ifBasicSignalTable = _IfBasicSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ifBasicSignalTable.setStatus("current")
_IfBasicSignalEntry_Object = MibTableRow
ifBasicSignalEntry = _IfBasicSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1)
)
ifBasicSignalEntry.setIndexNames(
    (0, "LUM-IFBASIC-MIB", "ifBasicSignalIndex"),
)
if mibBuilder.loadTexts:
    ifBasicSignalEntry.setStatus("current")
_IfBasicSignalIndex_Type = Unsigned32
_IfBasicSignalIndex_Object = MibTableColumn
ifBasicSignalIndex = _IfBasicSignalIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 1),
    _IfBasicSignalIndex_Type()
)
ifBasicSignalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalIndex.setStatus("current")
_IfBasicSignalName_Type = MgmtNameString
_IfBasicSignalName_Object = MibTableColumn
ifBasicSignalName = _IfBasicSignalName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 2),
    _IfBasicSignalName_Type()
)
ifBasicSignalName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifBasicSignalName.setStatus("current")


class _IfBasicSignalSignalStructure_Type(Counter64):
    """Custom type ifBasicSignalSignalStructure based on Counter64"""
    defaultValue = 0


_IfBasicSignalSignalStructure_Type.__name__ = "Counter64"
_IfBasicSignalSignalStructure_Object = MibTableColumn
ifBasicSignalSignalStructure = _IfBasicSignalSignalStructure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 3),
    _IfBasicSignalSignalStructure_Type()
)
ifBasicSignalSignalStructure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalSignalStructure.setStatus("current")


class _IfBasicSignalSignalFormat_Type(SignalFormat):
    """Custom type ifBasicSignalSignalFormat based on SignalFormat"""
    defaultValue = 10


_IfBasicSignalSignalFormat_Type.__name__ = "SignalFormat"
_IfBasicSignalSignalFormat_Object = MibTableColumn
ifBasicSignalSignalFormat = _IfBasicSignalSignalFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 4),
    _IfBasicSignalSignalFormat_Type()
)
ifBasicSignalSignalFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicSignalSignalFormat.setStatus("current")
_IfBasicSignalFarEndLoopbackTerminatingLayer_Type = Layer
_IfBasicSignalFarEndLoopbackTerminatingLayer_Object = MibTableColumn
ifBasicSignalFarEndLoopbackTerminatingLayer = _IfBasicSignalFarEndLoopbackTerminatingLayer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 5),
    _IfBasicSignalFarEndLoopbackTerminatingLayer_Type()
)
ifBasicSignalFarEndLoopbackTerminatingLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalFarEndLoopbackTerminatingLayer.setStatus("current")


class _IfBasicSignalFarEndLoopback_Type(EnabledDisabledWithNA):
    """Custom type ifBasicSignalFarEndLoopback based on EnabledDisabledWithNA"""
    defaultValue = 1


_IfBasicSignalFarEndLoopback_Type.__name__ = "EnabledDisabledWithNA"
_IfBasicSignalFarEndLoopback_Object = MibTableColumn
ifBasicSignalFarEndLoopback = _IfBasicSignalFarEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 6),
    _IfBasicSignalFarEndLoopback_Type()
)
ifBasicSignalFarEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicSignalFarEndLoopback.setStatus("current")


class _IfBasicSignalFarEndLoopbackTimeout_Type(Time7200min):
    """Custom type ifBasicSignalFarEndLoopbackTimeout based on Time7200min"""
    defaultValue = 3


_IfBasicSignalFarEndLoopbackTimeout_Type.__name__ = "Time7200min"
_IfBasicSignalFarEndLoopbackTimeout_Object = MibTableColumn
ifBasicSignalFarEndLoopbackTimeout = _IfBasicSignalFarEndLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 7),
    _IfBasicSignalFarEndLoopbackTimeout_Type()
)
ifBasicSignalFarEndLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicSignalFarEndLoopbackTimeout.setStatus("current")
_IfBasicSignalNearEndLoopbackTerminatingLayer_Type = Layer
_IfBasicSignalNearEndLoopbackTerminatingLayer_Object = MibTableColumn
ifBasicSignalNearEndLoopbackTerminatingLayer = _IfBasicSignalNearEndLoopbackTerminatingLayer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 8),
    _IfBasicSignalNearEndLoopbackTerminatingLayer_Type()
)
ifBasicSignalNearEndLoopbackTerminatingLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalNearEndLoopbackTerminatingLayer.setStatus("current")


class _IfBasicSignalNearEndLoopback_Type(EnabledDisabledWithNA):
    """Custom type ifBasicSignalNearEndLoopback based on EnabledDisabledWithNA"""
    defaultValue = 1


_IfBasicSignalNearEndLoopback_Type.__name__ = "EnabledDisabledWithNA"
_IfBasicSignalNearEndLoopback_Object = MibTableColumn
ifBasicSignalNearEndLoopback = _IfBasicSignalNearEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 9),
    _IfBasicSignalNearEndLoopback_Type()
)
ifBasicSignalNearEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicSignalNearEndLoopback.setStatus("current")


class _IfBasicSignalNearEndLoopbackTimeout_Type(Time7200min):
    """Custom type ifBasicSignalNearEndLoopbackTimeout based on Time7200min"""
    defaultValue = 3


_IfBasicSignalNearEndLoopbackTimeout_Type.__name__ = "Time7200min"
_IfBasicSignalNearEndLoopbackTimeout_Object = MibTableColumn
ifBasicSignalNearEndLoopbackTimeout = _IfBasicSignalNearEndLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 10),
    _IfBasicSignalNearEndLoopbackTimeout_Type()
)
ifBasicSignalNearEndLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicSignalNearEndLoopbackTimeout.setStatus("current")
_IfBasicSignalFarEndLoopbackEnabled_Type = FaultStatusWithNA
_IfBasicSignalFarEndLoopbackEnabled_Object = MibTableColumn
ifBasicSignalFarEndLoopbackEnabled = _IfBasicSignalFarEndLoopbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 11),
    _IfBasicSignalFarEndLoopbackEnabled_Type()
)
ifBasicSignalFarEndLoopbackEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalFarEndLoopbackEnabled.setStatus("current")
_IfBasicSignalNearEndLoopbackEnabled_Type = FaultStatusWithNA
_IfBasicSignalNearEndLoopbackEnabled_Object = MibTableColumn
ifBasicSignalNearEndLoopbackEnabled = _IfBasicSignalNearEndLoopbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 12),
    _IfBasicSignalNearEndLoopbackEnabled_Type()
)
ifBasicSignalNearEndLoopbackEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalNearEndLoopbackEnabled.setStatus("current")


class _IfBasicSignalOpticalLayerMapping_Type(OpticalLayerMappingType):
    """Custom type ifBasicSignalOpticalLayerMapping based on OpticalLayerMappingType"""
    defaultValue = 3


_IfBasicSignalOpticalLayerMapping_Type.__name__ = "OpticalLayerMappingType"
_IfBasicSignalOpticalLayerMapping_Object = MibTableColumn
ifBasicSignalOpticalLayerMapping = _IfBasicSignalOpticalLayerMapping_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 13),
    _IfBasicSignalOpticalLayerMapping_Type()
)
ifBasicSignalOpticalLayerMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicSignalOpticalLayerMapping.setStatus("current")
_IfBasicSignalConfigurationMismatch_Type = FaultStatusWithNA
_IfBasicSignalConfigurationMismatch_Object = MibTableColumn
ifBasicSignalConfigurationMismatch = _IfBasicSignalConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 14),
    _IfBasicSignalConfigurationMismatch_Type()
)
ifBasicSignalConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalConfigurationMismatch.setStatus("deprecated")


class _IfBasicSignalActualOpticalLayerMapping_Type(OpticalLayerMappingType):
    """Custom type ifBasicSignalActualOpticalLayerMapping based on OpticalLayerMappingType"""
    defaultValue = 0


_IfBasicSignalActualOpticalLayerMapping_Type.__name__ = "OpticalLayerMappingType"
_IfBasicSignalActualOpticalLayerMapping_Object = MibTableColumn
ifBasicSignalActualOpticalLayerMapping = _IfBasicSignalActualOpticalLayerMapping_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 15),
    _IfBasicSignalActualOpticalLayerMapping_Type()
)
ifBasicSignalActualOpticalLayerMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalActualOpticalLayerMapping.setStatus("current")


class _IfBasicSignalSpeed_Type(Unsigned32WithNA):
    """Custom type ifBasicSignalSpeed based on Unsigned32WithNA"""
    defaultValue = 61440

    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(61440, 1402500),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfBasicSignalSpeed_Type.__name__ = "Unsigned32WithNA"
_IfBasicSignalSpeed_Object = MibTableColumn
ifBasicSignalSpeed = _IfBasicSignalSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 16),
    _IfBasicSignalSpeed_Type()
)
ifBasicSignalSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicSignalSpeed.setStatus("current")


class _IfBasicSignalDirection_Type(SignalDirection):
    """Custom type ifBasicSignalDirection based on SignalDirection"""
    defaultValue = 4


_IfBasicSignalDirection_Type.__name__ = "SignalDirection"
_IfBasicSignalDirection_Object = MibTableColumn
ifBasicSignalDirection = _IfBasicSignalDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 17),
    _IfBasicSignalDirection_Type()
)
ifBasicSignalDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalDirection.setStatus("current")


class _IfBasicSignalFormatConfigurable_Type(Integer32):
    """Custom type ifBasicSignalFormatConfigurable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notApplicable", 2147483647))
    )


_IfBasicSignalFormatConfigurable_Type.__name__ = "Integer32"
_IfBasicSignalFormatConfigurable_Object = MibTableColumn
ifBasicSignalFormatConfigurable = _IfBasicSignalFormatConfigurable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 18),
    _IfBasicSignalFormatConfigurable_Type()
)
ifBasicSignalFormatConfigurable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalFormatConfigurable.setStatus("current")
_IfBasicSignalFormatConfigurationSharedWithInterface_Type = Unsigned32WithNA
_IfBasicSignalFormatConfigurationSharedWithInterface_Object = MibTableColumn
ifBasicSignalFormatConfigurationSharedWithInterface = _IfBasicSignalFormatConfigurationSharedWithInterface_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 19),
    _IfBasicSignalFormatConfigurationSharedWithInterface_Type()
)
ifBasicSignalFormatConfigurationSharedWithInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalFormatConfigurationSharedWithInterface.setStatus("current")


class _IfBasicSignalPhysicalLayerMapping_Type(PhysicalLayerMappingType):
    """Custom type ifBasicSignalPhysicalLayerMapping based on PhysicalLayerMappingType"""
    defaultValue = 1


_IfBasicSignalPhysicalLayerMapping_Type.__name__ = "PhysicalLayerMappingType"
_IfBasicSignalPhysicalLayerMapping_Object = MibTableColumn
ifBasicSignalPhysicalLayerMapping = _IfBasicSignalPhysicalLayerMapping_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 20),
    _IfBasicSignalPhysicalLayerMapping_Type()
)
ifBasicSignalPhysicalLayerMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicSignalPhysicalLayerMapping.setStatus("current")


class _IfBasicSignalFacilityLoopback_Type(EnabledDisabledWithNA):
    """Custom type ifBasicSignalFacilityLoopback based on EnabledDisabledWithNA"""
    defaultValue = 1


_IfBasicSignalFacilityLoopback_Type.__name__ = "EnabledDisabledWithNA"
_IfBasicSignalFacilityLoopback_Object = MibTableColumn
ifBasicSignalFacilityLoopback = _IfBasicSignalFacilityLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 21),
    _IfBasicSignalFacilityLoopback_Type()
)
ifBasicSignalFacilityLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicSignalFacilityLoopback.setStatus("current")


class _IfBasicSignalFacilityLoopbackTimeout_Type(Time7200minNo0):
    """Custom type ifBasicSignalFacilityLoopbackTimeout based on Time7200minNo0"""
    defaultValue = 3


_IfBasicSignalFacilityLoopbackTimeout_Type.__name__ = "Time7200minNo0"
_IfBasicSignalFacilityLoopbackTimeout_Object = MibTableColumn
ifBasicSignalFacilityLoopbackTimeout = _IfBasicSignalFacilityLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 22),
    _IfBasicSignalFacilityLoopbackTimeout_Type()
)
ifBasicSignalFacilityLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicSignalFacilityLoopbackTimeout.setStatus("current")
_IfBasicSignalFacilityLoopbackEnabled_Type = FaultStatusWithNA
_IfBasicSignalFacilityLoopbackEnabled_Object = MibTableColumn
ifBasicSignalFacilityLoopbackEnabled = _IfBasicSignalFacilityLoopbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 23),
    _IfBasicSignalFacilityLoopbackEnabled_Type()
)
ifBasicSignalFacilityLoopbackEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalFacilityLoopbackEnabled.setStatus("current")


class _IfBasicSignalTerminalLoopback_Type(EnabledDisabledWithNA):
    """Custom type ifBasicSignalTerminalLoopback based on EnabledDisabledWithNA"""
    defaultValue = 1


_IfBasicSignalTerminalLoopback_Type.__name__ = "EnabledDisabledWithNA"
_IfBasicSignalTerminalLoopback_Object = MibTableColumn
ifBasicSignalTerminalLoopback = _IfBasicSignalTerminalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 24),
    _IfBasicSignalTerminalLoopback_Type()
)
ifBasicSignalTerminalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicSignalTerminalLoopback.setStatus("current")


class _IfBasicSignalTerminalLoopbackTimeout_Type(Time7200minNo0):
    """Custom type ifBasicSignalTerminalLoopbackTimeout based on Time7200minNo0"""
    defaultValue = 3


_IfBasicSignalTerminalLoopbackTimeout_Type.__name__ = "Time7200minNo0"
_IfBasicSignalTerminalLoopbackTimeout_Object = MibTableColumn
ifBasicSignalTerminalLoopbackTimeout = _IfBasicSignalTerminalLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 25),
    _IfBasicSignalTerminalLoopbackTimeout_Type()
)
ifBasicSignalTerminalLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBasicSignalTerminalLoopbackTimeout.setStatus("current")
_IfBasicSignalTerminalLoopbackEnabled_Type = FaultStatusWithNA
_IfBasicSignalTerminalLoopbackEnabled_Object = MibTableColumn
ifBasicSignalTerminalLoopbackEnabled = _IfBasicSignalTerminalLoopbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 26),
    _IfBasicSignalTerminalLoopbackEnabled_Type()
)
ifBasicSignalTerminalLoopbackEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalTerminalLoopbackEnabled.setStatus("current")


class _IfBasicSignalConnectorType_Type(ConnectorType):
    """Custom type ifBasicSignalConnectorType based on ConnectorType"""
    defaultValue = 2147483647


_IfBasicSignalConnectorType_Type.__name__ = "ConnectorType"
_IfBasicSignalConnectorType_Object = MibTableColumn
ifBasicSignalConnectorType = _IfBasicSignalConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 2, 4, 1, 1, 27),
    _IfBasicSignalConnectorType_Type()
)
ifBasicSignalConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBasicSignalConnectorType.setStatus("current")

# Managed Objects groups

ifBasicGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 1)
)
ifBasicGeneralGroupV1.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicGeneralConfigLastChangeTime"),
        ("LUM-IFBASIC-MIB", "ifBasicGeneralStateLastChangeTime"),
        ("LUM-IFBASIC-MIB", "ifBasicGeneralIfBasicIfTableSize"),
        ("LUM-IFBASIC-MIB", "ifBasicGeneralIfBasicIfConfigLastChangeTime"),
        ("LUM-IFBASIC-MIB", "ifBasicGeneralIfBasicIfStateLastChangeTime"),
        ("LUM-IFBASIC-MIB", "ifBasicGeneralIfBasicAdminTableSize"),
        ("LUM-IFBASIC-MIB", "ifBasicGeneralIfBasicAdminConfigLastChangeTime"),
        ("LUM-IFBASIC-MIB", "ifBasicGeneralIfBasicAdminStateLastChangeTime"),
        ("LUM-IFBASIC-MIB", "ifBasicGeneralIfBasicSignalTableSize"),
        ("LUM-IFBASIC-MIB", "ifBasicGeneralIfBasicSignalConfigLastChangeTime"),
        ("LUM-IFBASIC-MIB", "ifBasicGeneralIfBasicSignalStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifBasicGeneralGroupV1.setStatus("current")

ifBasicIfGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 2)
)
ifBasicIfGroupV1.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicIfIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicIfName"),
        ("LUM-IFBASIC-MIB", "ifBasicIfTxSignalStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicIfRxSignalStatus"))
)
if mibBuilder.loadTexts:
    ifBasicIfGroupV1.setStatus("deprecated")

ifBasicAdminGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 3)
)
ifBasicAdminGroupV1.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicAdminIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminName"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminDescr"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminSubrack"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminSlot"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminTxPort"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminRxPort"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminAdminStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminOperStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminAutoAlarmEnableStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminAutoAlarmEnableReset"))
)
if mibBuilder.loadTexts:
    ifBasicAdminGroupV1.setStatus("deprecated")

ifBasicSignalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 4)
)
ifBasicSignalGroupV1.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicSignalIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalName"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalStructure"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalFormat"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackEnabled"))
)
if mibBuilder.loadTexts:
    ifBasicSignalGroupV1.setStatus("deprecated")

ifBasicSignalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 5)
)
ifBasicSignalGroupV2.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicSignalIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalName"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalStructure"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalFormat"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalOpticalLayerMapping"))
)
if mibBuilder.loadTexts:
    ifBasicSignalGroupV2.setStatus("deprecated")

ifBasicSignalGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 6)
)
ifBasicSignalGroupV3.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicSignalIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalName"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalStructure"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalFormat"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalOpticalLayerMapping"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalConfigurationMismatch"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalActualOpticalLayerMapping"))
)
if mibBuilder.loadTexts:
    ifBasicSignalGroupV3.setStatus("deprecated")

ifBasicSignalGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 7)
)
ifBasicSignalGroupV4.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicSignalIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalName"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalStructure"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalFormat"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalOpticalLayerMapping"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalConfigurationMismatch"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalActualOpticalLayerMapping"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSpeed"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalDirection"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFormatConfigurable"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFormatConfigurationSharedWithInterface"))
)
if mibBuilder.loadTexts:
    ifBasicSignalGroupV4.setStatus("deprecated")

ifBasicIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 8)
)
ifBasicIfGroupV2.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicIfIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicIfName"),
        ("LUM-IFBASIC-MIB", "ifBasicIfTxSignalStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicIfRxSignalStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicIfUpId"))
)
if mibBuilder.loadTexts:
    ifBasicIfGroupV2.setStatus("deprecated")

ifBasicSignalGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 9)
)
ifBasicSignalGroupV5.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicSignalIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalName"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalStructure"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalFormat"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalOpticalLayerMapping"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalConfigurationMismatch"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalActualOpticalLayerMapping"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSpeed"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalDirection"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFormatConfigurable"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFormatConfigurationSharedWithInterface"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalPhysicalLayerMapping"))
)
if mibBuilder.loadTexts:
    ifBasicSignalGroupV5.setStatus("deprecated")

ifBasicSignalGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 10)
)
ifBasicSignalGroupV6.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicSignalIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalName"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalStructure"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalFormat"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalOpticalLayerMapping"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalConfigurationMismatch"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalActualOpticalLayerMapping"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSpeed"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalDirection"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFormatConfigurable"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFormatConfigurationSharedWithInterface"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalPhysicalLayerMapping"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFacilityLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFacilityLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFacilityLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalTerminalLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalTerminalLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalTerminalLoopbackEnabled"))
)
if mibBuilder.loadTexts:
    ifBasicSignalGroupV6.setStatus("deprecated")

ifBasicAdminGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 11)
)
ifBasicAdminGroupV2.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicAdminIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminName"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminDescr"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminSubrack"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminSlot"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminTxPort"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminRxPort"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminAdminStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminOperStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminAutoAlarmEnableStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminAutoAlarmEnableReset"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminInterfaceStatus"))
)
if mibBuilder.loadTexts:
    ifBasicAdminGroupV2.setStatus("deprecated")

ifBasicIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 12)
)
ifBasicIfGroupV3.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicIfIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicIfName"),
        ("LUM-IFBASIC-MIB", "ifBasicIfTxSignalStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicIfRxSignalStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicIfUpId"),
        ("LUM-IFBASIC-MIB", "ifBasicIfAid"),
        ("LUM-IFBASIC-MIB", "ifBasicIfPhysicalLocation"))
)
if mibBuilder.loadTexts:
    ifBasicIfGroupV3.setStatus("current")

ifBasicAdminGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 13)
)
ifBasicAdminGroupV3.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicAdminIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminName"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminDescr"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminSubrack"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminSlot"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminTxPort"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminRxPort"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminAdminStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminOperStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminAutoAlarmEnableStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminAutoAlarmEnableReset"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminInterfaceStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminIfNo"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminIfType"))
)
if mibBuilder.loadTexts:
    ifBasicAdminGroupV3.setStatus("deprecated")

ifBasicSignalGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 14)
)
ifBasicSignalGroupV7.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicSignalIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalName"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalStructure"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSignalFormat"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTerminatingLayer"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFarEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalNearEndLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalOpticalLayerMapping"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalConfigurationMismatch"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalActualOpticalLayerMapping"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalSpeed"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalDirection"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFormatConfigurable"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFormatConfigurationSharedWithInterface"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalPhysicalLayerMapping"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFacilityLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFacilityLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalFacilityLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalTerminalLoopback"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalTerminalLoopbackTimeout"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalTerminalLoopbackEnabled"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalConnectorType"))
)
if mibBuilder.loadTexts:
    ifBasicSignalGroupV7.setStatus("current")

ifBasicAdminGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 1, 15)
)
ifBasicAdminGroupV4.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicAdminIndex"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminName"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminDescr"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminSubrack"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminSlot"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminTxPort"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminRxPort"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminAdminStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminOperStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminAutoAlarmEnableStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminAutoAlarmEnableReset"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminInterfaceStatus"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminIfNo"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminIfType"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminNotAvailableForUse"))
)
if mibBuilder.loadTexts:
    ifBasicAdminGroupV4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfBasicBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 2, 1)
)
lumIfBasicBasicComplV1.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicGeneralGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicIfGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfBasicBasicComplV1.setStatus(
        "deprecated"
    )

lumIfBasicBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 2, 2)
)
lumIfBasicBasicComplV2.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicGeneralGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicIfGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfBasicBasicComplV2.setStatus(
        "deprecated"
    )

lumIfBasicBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 2, 3)
)
lumIfBasicBasicComplV3.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicGeneralGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicIfGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfBasicBasicComplV3.setStatus(
        "deprecated"
    )

lumIfBasicBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 2, 4)
)
lumIfBasicBasicComplV4.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicGeneralGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicIfGroupV2"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalGroupV4"))
)
if mibBuilder.loadTexts:
    lumIfBasicBasicComplV4.setStatus(
        "deprecated"
    )

lumIfBasicBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 2, 5)
)
lumIfBasicBasicComplV5.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicGeneralGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicIfGroupV2"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalGroupV5"))
)
if mibBuilder.loadTexts:
    lumIfBasicBasicComplV5.setStatus(
        "deprecated"
    )

lumIfBasicBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 2, 6)
)
lumIfBasicBasicComplV6.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicGeneralGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicIfGroupV3"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminGroupV2"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalGroupV6"))
)
if mibBuilder.loadTexts:
    lumIfBasicBasicComplV6.setStatus(
        "deprecated"
    )

lumIfBasicBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 2, 7)
)
lumIfBasicBasicComplV7.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicGeneralGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicIfGroupV3"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminGroupV3"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalGroupV7"))
)
if mibBuilder.loadTexts:
    lumIfBasicBasicComplV7.setStatus(
        "deprecated"
    )

lumIfBasicBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46, 1, 2, 8)
)
lumIfBasicBasicComplV8.setObjects(
      *(("LUM-IFBASIC-MIB", "ifBasicGeneralGroupV1"),
        ("LUM-IFBASIC-MIB", "ifBasicIfGroupV3"),
        ("LUM-IFBASIC-MIB", "ifBasicAdminGroupV4"),
        ("LUM-IFBASIC-MIB", "ifBasicSignalGroupV7"))
)
if mibBuilder.loadTexts:
    lumIfBasicBasicComplV8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFBASIC-MIB",
    **{"lumIfBasicMIBModule": lumIfBasicMIBModule,
       "lumIfBasicConfs": lumIfBasicConfs,
       "lumIfBasicGroups": lumIfBasicGroups,
       "ifBasicGeneralGroupV1": ifBasicGeneralGroupV1,
       "ifBasicIfGroupV1": ifBasicIfGroupV1,
       "ifBasicAdminGroupV1": ifBasicAdminGroupV1,
       "ifBasicSignalGroupV1": ifBasicSignalGroupV1,
       "ifBasicSignalGroupV2": ifBasicSignalGroupV2,
       "ifBasicSignalGroupV3": ifBasicSignalGroupV3,
       "ifBasicSignalGroupV4": ifBasicSignalGroupV4,
       "ifBasicIfGroupV2": ifBasicIfGroupV2,
       "ifBasicSignalGroupV5": ifBasicSignalGroupV5,
       "ifBasicSignalGroupV6": ifBasicSignalGroupV6,
       "ifBasicAdminGroupV2": ifBasicAdminGroupV2,
       "ifBasicIfGroupV3": ifBasicIfGroupV3,
       "ifBasicAdminGroupV3": ifBasicAdminGroupV3,
       "ifBasicSignalGroupV7": ifBasicSignalGroupV7,
       "ifBasicAdminGroupV4": ifBasicAdminGroupV4,
       "lumIfBasicCompl": lumIfBasicCompl,
       "lumIfBasicBasicComplV1": lumIfBasicBasicComplV1,
       "lumIfBasicBasicComplV2": lumIfBasicBasicComplV2,
       "lumIfBasicBasicComplV3": lumIfBasicBasicComplV3,
       "lumIfBasicBasicComplV4": lumIfBasicBasicComplV4,
       "lumIfBasicBasicComplV5": lumIfBasicBasicComplV5,
       "lumIfBasicBasicComplV6": lumIfBasicBasicComplV6,
       "lumIfBasicBasicComplV7": lumIfBasicBasicComplV7,
       "lumIfBasicBasicComplV8": lumIfBasicBasicComplV8,
       "lumIfBasicMIBObjects": lumIfBasicMIBObjects,
       "ifBasicGeneral": ifBasicGeneral,
       "ifBasicGeneralConfigLastChangeTime": ifBasicGeneralConfigLastChangeTime,
       "ifBasicGeneralStateLastChangeTime": ifBasicGeneralStateLastChangeTime,
       "ifBasicGeneralIfBasicIfTableSize": ifBasicGeneralIfBasicIfTableSize,
       "ifBasicGeneralIfBasicIfConfigLastChangeTime": ifBasicGeneralIfBasicIfConfigLastChangeTime,
       "ifBasicGeneralIfBasicIfStateLastChangeTime": ifBasicGeneralIfBasicIfStateLastChangeTime,
       "ifBasicGeneralIfBasicAdminTableSize": ifBasicGeneralIfBasicAdminTableSize,
       "ifBasicGeneralIfBasicAdminConfigLastChangeTime": ifBasicGeneralIfBasicAdminConfigLastChangeTime,
       "ifBasicGeneralIfBasicAdminStateLastChangeTime": ifBasicGeneralIfBasicAdminStateLastChangeTime,
       "ifBasicGeneralIfBasicSignalTableSize": ifBasicGeneralIfBasicSignalTableSize,
       "ifBasicGeneralIfBasicSignalConfigLastChangeTime": ifBasicGeneralIfBasicSignalConfigLastChangeTime,
       "ifBasicGeneralIfBasicSignalStateLastChangeTime": ifBasicGeneralIfBasicSignalStateLastChangeTime,
       "ifBasicIfList": ifBasicIfList,
       "ifBasicIfTable": ifBasicIfTable,
       "ifBasicIfEntry": ifBasicIfEntry,
       "ifBasicIfIndex": ifBasicIfIndex,
       "ifBasicIfName": ifBasicIfName,
       "ifBasicIfTxSignalStatus": ifBasicIfTxSignalStatus,
       "ifBasicIfRxSignalStatus": ifBasicIfRxSignalStatus,
       "ifBasicIfUpId": ifBasicIfUpId,
       "ifBasicIfAid": ifBasicIfAid,
       "ifBasicIfPhysicalLocation": ifBasicIfPhysicalLocation,
       "ifBasicAdminList": ifBasicAdminList,
       "ifBasicAdminTable": ifBasicAdminTable,
       "ifBasicAdminEntry": ifBasicAdminEntry,
       "ifBasicAdminIndex": ifBasicAdminIndex,
       "ifBasicAdminName": ifBasicAdminName,
       "ifBasicAdminDescr": ifBasicAdminDescr,
       "ifBasicAdminSubrack": ifBasicAdminSubrack,
       "ifBasicAdminSlot": ifBasicAdminSlot,
       "ifBasicAdminTxPort": ifBasicAdminTxPort,
       "ifBasicAdminRxPort": ifBasicAdminRxPort,
       "ifBasicAdminAdminStatus": ifBasicAdminAdminStatus,
       "ifBasicAdminOperStatus": ifBasicAdminOperStatus,
       "ifBasicAdminAutoAlarmEnableStatus": ifBasicAdminAutoAlarmEnableStatus,
       "ifBasicAdminAutoAlarmEnableReset": ifBasicAdminAutoAlarmEnableReset,
       "ifBasicAdminInterfaceStatus": ifBasicAdminInterfaceStatus,
       "ifBasicAdminIfNo": ifBasicAdminIfNo,
       "ifBasicAdminIfType": ifBasicAdminIfType,
       "ifBasicAdminNotAvailableForUse": ifBasicAdminNotAvailableForUse,
       "ifBasicSignalList": ifBasicSignalList,
       "ifBasicSignalTable": ifBasicSignalTable,
       "ifBasicSignalEntry": ifBasicSignalEntry,
       "ifBasicSignalIndex": ifBasicSignalIndex,
       "ifBasicSignalName": ifBasicSignalName,
       "ifBasicSignalSignalStructure": ifBasicSignalSignalStructure,
       "ifBasicSignalSignalFormat": ifBasicSignalSignalFormat,
       "ifBasicSignalFarEndLoopbackTerminatingLayer": ifBasicSignalFarEndLoopbackTerminatingLayer,
       "ifBasicSignalFarEndLoopback": ifBasicSignalFarEndLoopback,
       "ifBasicSignalFarEndLoopbackTimeout": ifBasicSignalFarEndLoopbackTimeout,
       "ifBasicSignalNearEndLoopbackTerminatingLayer": ifBasicSignalNearEndLoopbackTerminatingLayer,
       "ifBasicSignalNearEndLoopback": ifBasicSignalNearEndLoopback,
       "ifBasicSignalNearEndLoopbackTimeout": ifBasicSignalNearEndLoopbackTimeout,
       "ifBasicSignalFarEndLoopbackEnabled": ifBasicSignalFarEndLoopbackEnabled,
       "ifBasicSignalNearEndLoopbackEnabled": ifBasicSignalNearEndLoopbackEnabled,
       "ifBasicSignalOpticalLayerMapping": ifBasicSignalOpticalLayerMapping,
       "ifBasicSignalConfigurationMismatch": ifBasicSignalConfigurationMismatch,
       "ifBasicSignalActualOpticalLayerMapping": ifBasicSignalActualOpticalLayerMapping,
       "ifBasicSignalSpeed": ifBasicSignalSpeed,
       "ifBasicSignalDirection": ifBasicSignalDirection,
       "ifBasicSignalFormatConfigurable": ifBasicSignalFormatConfigurable,
       "ifBasicSignalFormatConfigurationSharedWithInterface": ifBasicSignalFormatConfigurationSharedWithInterface,
       "ifBasicSignalPhysicalLayerMapping": ifBasicSignalPhysicalLayerMapping,
       "ifBasicSignalFacilityLoopback": ifBasicSignalFacilityLoopback,
       "ifBasicSignalFacilityLoopbackTimeout": ifBasicSignalFacilityLoopbackTimeout,
       "ifBasicSignalFacilityLoopbackEnabled": ifBasicSignalFacilityLoopbackEnabled,
       "ifBasicSignalTerminalLoopback": ifBasicSignalTerminalLoopback,
       "ifBasicSignalTerminalLoopbackTimeout": ifBasicSignalTerminalLoopbackTimeout,
       "ifBasicSignalTerminalLoopbackEnabled": ifBasicSignalTerminalLoopbackEnabled,
       "ifBasicSignalConnectorType": ifBasicSignalConnectorType}
)
