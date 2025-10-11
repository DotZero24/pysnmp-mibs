# SNMP MIB module (LUM-IFFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFFC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:04 2025
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

(lumIfFcMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfFcMIB",
    "lumModules")

(FaultStatusWithNA,
 MgmtNameString,
 SignalStatusWithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "FaultStatusWithNA",
    "MgmtNameString",
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

lumIfFcMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 59)
)
if mibBuilder.loadTexts:
    lumIfFcMIBModule.setRevisions(
        ("2018-08-01 00:00",
         "2017-06-15 00:00",
         "2015-09-30 00:00",
         "2013-11-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfFcConfs_ObjectIdentity = ObjectIdentity
lumIfFcConfs = _LumIfFcConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 1)
)
_LumIfFcGroups_ObjectIdentity = ObjectIdentity
lumIfFcGroups = _LumIfFcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 1, 1)
)
_LumIfFcCompl_ObjectIdentity = ObjectIdentity
lumIfFcCompl = _LumIfFcCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 1, 2)
)
_LumIfFcMIBObjects_ObjectIdentity = ObjectIdentity
lumIfFcMIBObjects = _LumIfFcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2)
)
_IfFcGeneral_ObjectIdentity = ObjectIdentity
ifFcGeneral = _IfFcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 1)
)
_IfFcGeneralConfigLastChangeTime_Type = DateAndTime
_IfFcGeneralConfigLastChangeTime_Object = MibScalar
ifFcGeneralConfigLastChangeTime = _IfFcGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 1, 1),
    _IfFcGeneralConfigLastChangeTime_Type()
)
ifFcGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcGeneralConfigLastChangeTime.setStatus("current")
_IfFcGeneralStateLastChangeTime_Type = DateAndTime
_IfFcGeneralStateLastChangeTime_Object = MibScalar
ifFcGeneralStateLastChangeTime = _IfFcGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 1, 2),
    _IfFcGeneralStateLastChangeTime_Type()
)
ifFcGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcGeneralStateLastChangeTime.setStatus("current")
_IfFcGeneralIfFcPhysicalTableSize_Type = Unsigned32
_IfFcGeneralIfFcPhysicalTableSize_Object = MibScalar
ifFcGeneralIfFcPhysicalTableSize = _IfFcGeneralIfFcPhysicalTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 1, 3),
    _IfFcGeneralIfFcPhysicalTableSize_Type()
)
ifFcGeneralIfFcPhysicalTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcGeneralIfFcPhysicalTableSize.setStatus("current")
_IfFcGeneralIfFcPhysicalConfigLastChangeTime_Type = DateAndTime
_IfFcGeneralIfFcPhysicalConfigLastChangeTime_Object = MibScalar
ifFcGeneralIfFcPhysicalConfigLastChangeTime = _IfFcGeneralIfFcPhysicalConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 1, 4),
    _IfFcGeneralIfFcPhysicalConfigLastChangeTime_Type()
)
ifFcGeneralIfFcPhysicalConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcGeneralIfFcPhysicalConfigLastChangeTime.setStatus("current")
_IfFcGeneralIfFcPhysicalStateLastChangeTime_Type = DateAndTime
_IfFcGeneralIfFcPhysicalStateLastChangeTime_Object = MibScalar
ifFcGeneralIfFcPhysicalStateLastChangeTime = _IfFcGeneralIfFcPhysicalStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 1, 5),
    _IfFcGeneralIfFcPhysicalStateLastChangeTime_Type()
)
ifFcGeneralIfFcPhysicalStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcGeneralIfFcPhysicalStateLastChangeTime.setStatus("current")
_IfFcPhysicalList_ObjectIdentity = ObjectIdentity
ifFcPhysicalList = _IfFcPhysicalList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2)
)
_IfFcPhysicalTable_Object = MibTable
ifFcPhysicalTable = _IfFcPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifFcPhysicalTable.setStatus("current")
_IfFcPhysicalEntry_Object = MibTableRow
ifFcPhysicalEntry = _IfFcPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1)
)
ifFcPhysicalEntry.setIndexNames(
    (0, "LUM-IFFC-MIB", "ifFcPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ifFcPhysicalEntry.setStatus("current")
_IfFcPhysicalIndex_Type = Unsigned32
_IfFcPhysicalIndex_Object = MibTableColumn
ifFcPhysicalIndex = _IfFcPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 1),
    _IfFcPhysicalIndex_Type()
)
ifFcPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalIndex.setStatus("current")
_IfFcPhysicalName_Type = MgmtNameString
_IfFcPhysicalName_Object = MibTableColumn
ifFcPhysicalName = _IfFcPhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 2),
    _IfFcPhysicalName_Type()
)
ifFcPhysicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalName.setStatus("current")
_IfFcPhysicalConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfFcPhysicalConnIfBasicIfIndex_Object = MibTableColumn
ifFcPhysicalConnIfBasicIfIndex = _IfFcPhysicalConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 3),
    _IfFcPhysicalConnIfBasicIfIndex_Type()
)
ifFcPhysicalConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalConnIfBasicIfIndex.setStatus("current")
_IfFcPhysicalTxSignalStatus_Type = SignalStatusWithNA
_IfFcPhysicalTxSignalStatus_Object = MibTableColumn
ifFcPhysicalTxSignalStatus = _IfFcPhysicalTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 4),
    _IfFcPhysicalTxSignalStatus_Type()
)
ifFcPhysicalTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalTxSignalStatus.setStatus("current")
_IfFcPhysicalRxSignalStatus_Type = SignalStatusWithNA
_IfFcPhysicalRxSignalStatus_Object = MibTableColumn
ifFcPhysicalRxSignalStatus = _IfFcPhysicalRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 5),
    _IfFcPhysicalRxSignalStatus_Type()
)
ifFcPhysicalRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalRxSignalStatus.setStatus("current")
_IfFcPhysicalRemoteLinkFault_Type = FaultStatusWithNA
_IfFcPhysicalRemoteLinkFault_Object = MibTableColumn
ifFcPhysicalRemoteLinkFault = _IfFcPhysicalRemoteLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 6),
    _IfFcPhysicalRemoteLinkFault_Type()
)
ifFcPhysicalRemoteLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalRemoteLinkFault.setStatus("current")
_IfFcPhysicalLocalLinkFault_Type = FaultStatusWithNA
_IfFcPhysicalLocalLinkFault_Object = MibTableColumn
ifFcPhysicalLocalLinkFault = _IfFcPhysicalLocalLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 7),
    _IfFcPhysicalLocalLinkFault_Type()
)
ifFcPhysicalLocalLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalLocalLinkFault.setStatus("current")
_IfFcPhysicalLinkDown_Type = FaultStatusWithNA
_IfFcPhysicalLinkDown_Object = MibTableColumn
ifFcPhysicalLinkDown = _IfFcPhysicalLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 8),
    _IfFcPhysicalLinkDown_Type()
)
ifFcPhysicalLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalLinkDown.setStatus("current")
_IfFcPhysicalPcsLossOfSync_Type = FaultStatusWithNA
_IfFcPhysicalPcsLossOfSync_Object = MibTableColumn
ifFcPhysicalPcsLossOfSync = _IfFcPhysicalPcsLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 9),
    _IfFcPhysicalPcsLossOfSync_Type()
)
ifFcPhysicalPcsLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalPcsLossOfSync.setStatus("current")
_IfFcPhysicalTxPcsLossOfSync_Type = FaultStatusWithNA
_IfFcPhysicalTxPcsLossOfSync_Object = MibTableColumn
ifFcPhysicalTxPcsLossOfSync = _IfFcPhysicalTxPcsLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 10),
    _IfFcPhysicalTxPcsLossOfSync_Type()
)
ifFcPhysicalTxPcsLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalTxPcsLossOfSync.setStatus("current")
_IfFcPhysicalRxHighBitErrorRate_Type = FaultStatusWithNA
_IfFcPhysicalRxHighBitErrorRate_Object = MibTableColumn
ifFcPhysicalRxHighBitErrorRate = _IfFcPhysicalRxHighBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 11),
    _IfFcPhysicalRxHighBitErrorRate_Type()
)
ifFcPhysicalRxHighBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalRxHighBitErrorRate.setStatus("current")
_IfFcPhysicalRxLocalLinkFault_Type = FaultStatusWithNA
_IfFcPhysicalRxLocalLinkFault_Object = MibTableColumn
ifFcPhysicalRxLocalLinkFault = _IfFcPhysicalRxLocalLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 12),
    _IfFcPhysicalRxLocalLinkFault_Type()
)
ifFcPhysicalRxLocalLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalRxLocalLinkFault.setStatus("current")
_IfFcPhysicalTxLocalLinkFault_Type = FaultStatusWithNA
_IfFcPhysicalTxLocalLinkFault_Object = MibTableColumn
ifFcPhysicalTxLocalLinkFault = _IfFcPhysicalTxLocalLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 2, 2, 1, 1, 13),
    _IfFcPhysicalTxLocalLinkFault_Type()
)
ifFcPhysicalTxLocalLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFcPhysicalTxLocalLinkFault.setStatus("current")

# Managed Objects groups

ifFcGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 1, 1, 1)
)
ifFcGeneralGroupV1.setObjects(
      *(("LUM-IFFC-MIB", "ifFcGeneralConfigLastChangeTime"),
        ("LUM-IFFC-MIB", "ifFcGeneralStateLastChangeTime"),
        ("LUM-IFFC-MIB", "ifFcGeneralIfFcPhysicalTableSize"),
        ("LUM-IFFC-MIB", "ifFcGeneralIfFcPhysicalConfigLastChangeTime"),
        ("LUM-IFFC-MIB", "ifFcGeneralIfFcPhysicalStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifFcGeneralGroupV1.setStatus("current")

ifFcPhysicalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 1, 1, 2)
)
ifFcPhysicalGroupV1.setObjects(
      *(("LUM-IFFC-MIB", "ifFcPhysicalIndex"),
        ("LUM-IFFC-MIB", "ifFcPhysicalName"),
        ("LUM-IFFC-MIB", "ifFcPhysicalConnIfBasicIfIndex"),
        ("LUM-IFFC-MIB", "ifFcPhysicalTxSignalStatus"),
        ("LUM-IFFC-MIB", "ifFcPhysicalRxSignalStatus"),
        ("LUM-IFFC-MIB", "ifFcPhysicalRemoteLinkFault"),
        ("LUM-IFFC-MIB", "ifFcPhysicalLocalLinkFault"),
        ("LUM-IFFC-MIB", "ifFcPhysicalLinkDown"),
        ("LUM-IFFC-MIB", "ifFcPhysicalPcsLossOfSync"))
)
if mibBuilder.loadTexts:
    ifFcPhysicalGroupV1.setStatus("deprecated")

ifFcPhysicalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 1, 1, 3)
)
ifFcPhysicalGroupV2.setObjects(
      *(("LUM-IFFC-MIB", "ifFcPhysicalIndex"),
        ("LUM-IFFC-MIB", "ifFcPhysicalName"),
        ("LUM-IFFC-MIB", "ifFcPhysicalConnIfBasicIfIndex"),
        ("LUM-IFFC-MIB", "ifFcPhysicalTxSignalStatus"),
        ("LUM-IFFC-MIB", "ifFcPhysicalRxSignalStatus"),
        ("LUM-IFFC-MIB", "ifFcPhysicalRemoteLinkFault"),
        ("LUM-IFFC-MIB", "ifFcPhysicalLocalLinkFault"),
        ("LUM-IFFC-MIB", "ifFcPhysicalLinkDown"),
        ("LUM-IFFC-MIB", "ifFcPhysicalPcsLossOfSync"),
        ("LUM-IFFC-MIB", "ifFcPhysicalTxPcsLossOfSync"))
)
if mibBuilder.loadTexts:
    ifFcPhysicalGroupV2.setStatus("deprecated")

ifFcPhysicalGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 1, 1, 4)
)
ifFcPhysicalGroupV3.setObjects(
      *(("LUM-IFFC-MIB", "ifFcPhysicalIndex"),
        ("LUM-IFFC-MIB", "ifFcPhysicalName"),
        ("LUM-IFFC-MIB", "ifFcPhysicalConnIfBasicIfIndex"),
        ("LUM-IFFC-MIB", "ifFcPhysicalTxSignalStatus"),
        ("LUM-IFFC-MIB", "ifFcPhysicalRxSignalStatus"),
        ("LUM-IFFC-MIB", "ifFcPhysicalRemoteLinkFault"),
        ("LUM-IFFC-MIB", "ifFcPhysicalLocalLinkFault"),
        ("LUM-IFFC-MIB", "ifFcPhysicalLinkDown"),
        ("LUM-IFFC-MIB", "ifFcPhysicalPcsLossOfSync"),
        ("LUM-IFFC-MIB", "ifFcPhysicalTxPcsLossOfSync"),
        ("LUM-IFFC-MIB", "ifFcPhysicalRxHighBitErrorRate"),
        ("LUM-IFFC-MIB", "ifFcPhysicalRxLocalLinkFault"),
        ("LUM-IFFC-MIB", "ifFcPhysicalTxLocalLinkFault"))
)
if mibBuilder.loadTexts:
    ifFcPhysicalGroupV3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfFcComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 1, 2, 1)
)
lumIfFcComplV1.setObjects(
      *(("LUM-IFFC-MIB", "ifFcGeneralGroupV1"),
        ("LUM-IFFC-MIB", "ifFcPhysicalGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfFcComplV1.setStatus(
        "deprecated"
    )

lumIfFcComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 1, 2, 2)
)
lumIfFcComplV2.setObjects(
      *(("LUM-IFFC-MIB", "ifFcGeneralGroupV1"),
        ("LUM-IFFC-MIB", "ifFcPhysicalGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfFcComplV2.setStatus(
        "deprecated"
    )

lumIfFcComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59, 1, 2, 3)
)
lumIfFcComplV3.setObjects(
      *(("LUM-IFFC-MIB", "ifFcGeneralGroupV1"),
        ("LUM-IFFC-MIB", "ifFcPhysicalGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfFcComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFFC-MIB",
    **{"lumIfFcMIBModule": lumIfFcMIBModule,
       "lumIfFcConfs": lumIfFcConfs,
       "lumIfFcGroups": lumIfFcGroups,
       "ifFcGeneralGroupV1": ifFcGeneralGroupV1,
       "ifFcPhysicalGroupV1": ifFcPhysicalGroupV1,
       "ifFcPhysicalGroupV2": ifFcPhysicalGroupV2,
       "ifFcPhysicalGroupV3": ifFcPhysicalGroupV3,
       "lumIfFcCompl": lumIfFcCompl,
       "lumIfFcComplV1": lumIfFcComplV1,
       "lumIfFcComplV2": lumIfFcComplV2,
       "lumIfFcComplV3": lumIfFcComplV3,
       "lumIfFcMIBObjects": lumIfFcMIBObjects,
       "ifFcGeneral": ifFcGeneral,
       "ifFcGeneralConfigLastChangeTime": ifFcGeneralConfigLastChangeTime,
       "ifFcGeneralStateLastChangeTime": ifFcGeneralStateLastChangeTime,
       "ifFcGeneralIfFcPhysicalTableSize": ifFcGeneralIfFcPhysicalTableSize,
       "ifFcGeneralIfFcPhysicalConfigLastChangeTime": ifFcGeneralIfFcPhysicalConfigLastChangeTime,
       "ifFcGeneralIfFcPhysicalStateLastChangeTime": ifFcGeneralIfFcPhysicalStateLastChangeTime,
       "ifFcPhysicalList": ifFcPhysicalList,
       "ifFcPhysicalTable": ifFcPhysicalTable,
       "ifFcPhysicalEntry": ifFcPhysicalEntry,
       "ifFcPhysicalIndex": ifFcPhysicalIndex,
       "ifFcPhysicalName": ifFcPhysicalName,
       "ifFcPhysicalConnIfBasicIfIndex": ifFcPhysicalConnIfBasicIfIndex,
       "ifFcPhysicalTxSignalStatus": ifFcPhysicalTxSignalStatus,
       "ifFcPhysicalRxSignalStatus": ifFcPhysicalRxSignalStatus,
       "ifFcPhysicalRemoteLinkFault": ifFcPhysicalRemoteLinkFault,
       "ifFcPhysicalLocalLinkFault": ifFcPhysicalLocalLinkFault,
       "ifFcPhysicalLinkDown": ifFcPhysicalLinkDown,
       "ifFcPhysicalPcsLossOfSync": ifFcPhysicalPcsLossOfSync,
       "ifFcPhysicalTxPcsLossOfSync": ifFcPhysicalTxPcsLossOfSync,
       "ifFcPhysicalRxHighBitErrorRate": ifFcPhysicalRxHighBitErrorRate,
       "ifFcPhysicalRxLocalLinkFault": ifFcPhysicalRxLocalLinkFault,
       "ifFcPhysicalTxLocalLinkFault": ifFcPhysicalTxLocalLinkFault}
)
