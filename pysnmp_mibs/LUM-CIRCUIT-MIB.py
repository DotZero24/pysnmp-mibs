# SNMP MIB module (LUM-CIRCUIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-CIRCUIT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:33 2025
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

(lumCircuitMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumCircuitMIB",
    "lumModules")

(FaultStatus,
 MgmtNameString) = mibBuilder.importSymbols(
    "LUM-TC",
    "FaultStatus",
    "MgmtNameString")

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

lumCircuitMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 30)
)
if mibBuilder.loadTexts:
    lumCircuitMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2011-03-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumCircuitConfs_ObjectIdentity = ObjectIdentity
lumCircuitConfs = _LumCircuitConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1)
)
_LumCircuitGroups_ObjectIdentity = ObjectIdentity
lumCircuitGroups = _LumCircuitGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1)
)
_LumCircuitCompl_ObjectIdentity = ObjectIdentity
lumCircuitCompl = _LumCircuitCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 2)
)
_LumCircuitMIBObjects_ObjectIdentity = ObjectIdentity
lumCircuitMIBObjects = _LumCircuitMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2)
)
_CircuitGeneral_ObjectIdentity = ObjectIdentity
circuitGeneral = _CircuitGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 1)
)
_CircuitGeneralConfigLastChangeTime_Type = DateAndTime
_CircuitGeneralConfigLastChangeTime_Object = MibScalar
circuitGeneralConfigLastChangeTime = _CircuitGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 1, 1),
    _CircuitGeneralConfigLastChangeTime_Type()
)
circuitGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitGeneralConfigLastChangeTime.setStatus("current")
_CircuitGeneralStateLastChangeTime_Type = DateAndTime
_CircuitGeneralStateLastChangeTime_Object = MibScalar
circuitGeneralStateLastChangeTime = _CircuitGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 1, 2),
    _CircuitGeneralStateLastChangeTime_Type()
)
circuitGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitGeneralStateLastChangeTime.setStatus("current")
_CircuitGeneralStatusTableSize_Type = Unsigned32
_CircuitGeneralStatusTableSize_Object = MibScalar
circuitGeneralStatusTableSize = _CircuitGeneralStatusTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 1, 3),
    _CircuitGeneralStatusTableSize_Type()
)
circuitGeneralStatusTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitGeneralStatusTableSize.setStatus("current")
_CircuitStatusList_ObjectIdentity = ObjectIdentity
circuitStatusList = _CircuitStatusList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2)
)
_CircuitStatusTable_Object = MibTable
circuitStatusTable = _CircuitStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1)
)
if mibBuilder.loadTexts:
    circuitStatusTable.setStatus("current")
_CircuitStatusEntry_Object = MibTableRow
circuitStatusEntry = _CircuitStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1)
)
circuitStatusEntry.setIndexNames(
    (0, "LUM-CIRCUIT-MIB", "circuitStatusIndex"),
)
if mibBuilder.loadTexts:
    circuitStatusEntry.setStatus("current")


class _CircuitStatusIndex_Type(Unsigned32):
    """Custom type circuitStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CircuitStatusIndex_Type.__name__ = "Unsigned32"
_CircuitStatusIndex_Object = MibTableColumn
circuitStatusIndex = _CircuitStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 1),
    _CircuitStatusIndex_Type()
)
circuitStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitStatusIndex.setStatus("current")
_CircuitStatusName_Type = MgmtNameString
_CircuitStatusName_Object = MibTableColumn
circuitStatusName = _CircuitStatusName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 2),
    _CircuitStatusName_Type()
)
circuitStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitStatusName.setStatus("current")
_CircuitStatusDescription_Type = DisplayString
_CircuitStatusDescription_Object = MibTableColumn
circuitStatusDescription = _CircuitStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 3),
    _CircuitStatusDescription_Type()
)
circuitStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitStatusDescription.setStatus("current")


class _CircuitStatusAdminStatus_Type(Integer32):
    """Custom type circuitStatusAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("inService", 1),
          ("maintenance", 2),
          ("notUsed", 3))
    )


_CircuitStatusAdminStatus_Type.__name__ = "Integer32"
_CircuitStatusAdminStatus_Object = MibTableColumn
circuitStatusAdminStatus = _CircuitStatusAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 4),
    _CircuitStatusAdminStatus_Type()
)
circuitStatusAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitStatusAdminStatus.setStatus("current")


class _CircuitStatusOperStatus_Type(Integer32):
    """Custom type circuitStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("incomplete", 1),
          ("down", 2),
          ("degraded", 3),
          ("up", 4))
    )


_CircuitStatusOperStatus_Type.__name__ = "Integer32"
_CircuitStatusOperStatus_Object = MibTableColumn
circuitStatusOperStatus = _CircuitStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 5),
    _CircuitStatusOperStatus_Type()
)
circuitStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitStatusOperStatus.setStatus("current")
_CircuitStatusIncomplete_Type = FaultStatus
_CircuitStatusIncomplete_Object = MibTableColumn
circuitStatusIncomplete = _CircuitStatusIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 6),
    _CircuitStatusIncomplete_Type()
)
circuitStatusIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitStatusIncomplete.setStatus("current")
_CircuitStatusDegraded_Type = FaultStatus
_CircuitStatusDegraded_Object = MibTableColumn
circuitStatusDegraded = _CircuitStatusDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 7),
    _CircuitStatusDegraded_Type()
)
circuitStatusDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitStatusDegraded.setStatus("current")
_CircuitStatusDown_Type = FaultStatus
_CircuitStatusDown_Object = MibTableColumn
circuitStatusDown = _CircuitStatusDown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 8),
    _CircuitStatusDown_Type()
)
circuitStatusDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitStatusDown.setStatus("current")
_L2CircuitStatusList_ObjectIdentity = ObjectIdentity
l2CircuitStatusList = _L2CircuitStatusList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3)
)
_FdfrStatusTable_Object = MibTable
fdfrStatusTable = _FdfrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fdfrStatusTable.setStatus("current")
_FdfrStatusEntry_Object = MibTableRow
fdfrStatusEntry = _FdfrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1)
)
fdfrStatusEntry.setIndexNames(
    (0, "LUM-CIRCUIT-MIB", "fdfrStatusIndex"),
)
if mibBuilder.loadTexts:
    fdfrStatusEntry.setStatus("current")


class _FdfrStatusIndex_Type(Unsigned32):
    """Custom type fdfrStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FdfrStatusIndex_Type.__name__ = "Unsigned32"
_FdfrStatusIndex_Object = MibTableColumn
fdfrStatusIndex = _FdfrStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 1),
    _FdfrStatusIndex_Type()
)
fdfrStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdfrStatusIndex.setStatus("current")
_FdfrStatusDown_Type = FaultStatus
_FdfrStatusDown_Object = MibTableColumn
fdfrStatusDown = _FdfrStatusDown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 2),
    _FdfrStatusDown_Type()
)
fdfrStatusDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdfrStatusDown.setStatus("current")
_FdfrStatusIncomplete_Type = FaultStatus
_FdfrStatusIncomplete_Object = MibTableColumn
fdfrStatusIncomplete = _FdfrStatusIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 3),
    _FdfrStatusIncomplete_Type()
)
fdfrStatusIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdfrStatusIncomplete.setStatus("current")
_FdfrStatusUnexpectedMfdfrType_Type = FaultStatus
_FdfrStatusUnexpectedMfdfrType_Object = MibTableColumn
fdfrStatusUnexpectedMfdfrType = _FdfrStatusUnexpectedMfdfrType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 4),
    _FdfrStatusUnexpectedMfdfrType_Type()
)
fdfrStatusUnexpectedMfdfrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdfrStatusUnexpectedMfdfrType.setStatus("current")
_FdfrStatusDegraded_Type = FaultStatus
_FdfrStatusDegraded_Object = MibTableColumn
fdfrStatusDegraded = _FdfrStatusDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 5),
    _FdfrStatusDegraded_Type()
)
fdfrStatusDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdfrStatusDegraded.setStatus("current")
_FdfrStatusMplsTunnelProtectionFailed_Type = FaultStatus
_FdfrStatusMplsTunnelProtectionFailed_Object = MibTableColumn
fdfrStatusMplsTunnelProtectionFailed = _FdfrStatusMplsTunnelProtectionFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 6),
    _FdfrStatusMplsTunnelProtectionFailed_Type()
)
fdfrStatusMplsTunnelProtectionFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdfrStatusMplsTunnelProtectionFailed.setStatus("current")
_FdfrStatusMplsTunnelProtectionDegraded_Type = FaultStatus
_FdfrStatusMplsTunnelProtectionDegraded_Object = MibTableColumn
fdfrStatusMplsTunnelProtectionDegraded = _FdfrStatusMplsTunnelProtectionDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 7),
    _FdfrStatusMplsTunnelProtectionDegraded_Type()
)
fdfrStatusMplsTunnelProtectionDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdfrStatusMplsTunnelProtectionDegraded.setStatus("current")
_FdfrStatusUnknown_Type = FaultStatus
_FdfrStatusUnknown_Object = MibTableColumn
fdfrStatusUnknown = _FdfrStatusUnknown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 8),
    _FdfrStatusUnknown_Type()
)
fdfrStatusUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdfrStatusUnknown.setStatus("current")

# Managed Objects groups

circuitGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 1)
)
circuitGeneralGroup.setObjects(
      *(("LUM-CIRCUIT-MIB", "circuitGeneralConfigLastChangeTime"),
        ("LUM-CIRCUIT-MIB", "circuitGeneralStateLastChangeTime"),
        ("LUM-CIRCUIT-MIB", "circuitGeneralStatusTableSize"))
)
if mibBuilder.loadTexts:
    circuitGeneralGroup.setStatus("current")

circuitStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 2)
)
circuitStatusGroup.setObjects(
      *(("LUM-CIRCUIT-MIB", "circuitStatusIndex"),
        ("LUM-CIRCUIT-MIB", "circuitStatusName"),
        ("LUM-CIRCUIT-MIB", "circuitStatusDescription"),
        ("LUM-CIRCUIT-MIB", "circuitStatusAdminStatus"),
        ("LUM-CIRCUIT-MIB", "circuitStatusOperStatus"),
        ("LUM-CIRCUIT-MIB", "circuitStatusDegraded"),
        ("LUM-CIRCUIT-MIB", "circuitStatusDown"),
        ("LUM-CIRCUIT-MIB", "circuitStatusIncomplete"))
)
if mibBuilder.loadTexts:
    circuitStatusGroup.setStatus("current")

fdfrStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 3)
)
fdfrStatusGroup.setObjects(
      *(("LUM-CIRCUIT-MIB", "fdfrStatusIndex"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusDown"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusIncomplete"))
)
if mibBuilder.loadTexts:
    fdfrStatusGroup.setStatus("deprecated")

fdfrStatusGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 4)
)
fdfrStatusGroupV2.setObjects(
      *(("LUM-CIRCUIT-MIB", "fdfrStatusIndex"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusDown"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusIncomplete"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusUnexpectedMfdfrType"))
)
if mibBuilder.loadTexts:
    fdfrStatusGroupV2.setStatus("deprecated")

fdfrStatusGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 5)
)
fdfrStatusGroupV3.setObjects(
      *(("LUM-CIRCUIT-MIB", "fdfrStatusIndex"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusDown"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusIncomplete"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusUnexpectedMfdfrType"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusDegraded"))
)
if mibBuilder.loadTexts:
    fdfrStatusGroupV3.setStatus("deprecated")

fdfrStatusGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 6)
)
fdfrStatusGroupV4.setObjects(
      *(("LUM-CIRCUIT-MIB", "fdfrStatusIndex"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusDown"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusIncomplete"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusUnexpectedMfdfrType"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusDegraded"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusMplsTunnelProtectionFailed"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusMplsTunnelProtectionDegraded"))
)
if mibBuilder.loadTexts:
    fdfrStatusGroupV4.setStatus("deprecated")

fdfrStatusGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 7)
)
fdfrStatusGroupV5.setObjects(
      *(("LUM-CIRCUIT-MIB", "fdfrStatusIndex"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusDown"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusIncomplete"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusUnexpectedMfdfrType"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusDegraded"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusMplsTunnelProtectionFailed"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusMplsTunnelProtectionDegraded"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusUnknown"))
)
if mibBuilder.loadTexts:
    fdfrStatusGroupV5.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumCircuitBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 2, 1)
)
lumCircuitBasicComplV1.setObjects(
      *(("LUM-CIRCUIT-MIB", "circuitGeneralGroup"),
        ("LUM-CIRCUIT-MIB", "circuitStatusGroup"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusGroup"))
)
if mibBuilder.loadTexts:
    lumCircuitBasicComplV1.setStatus(
        "deprecated"
    )

lumCircuitBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 2, 2)
)
lumCircuitBasicComplV2.setObjects(
      *(("LUM-CIRCUIT-MIB", "circuitGeneralGroup"),
        ("LUM-CIRCUIT-MIB", "circuitStatusGroup"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusGroupV2"))
)
if mibBuilder.loadTexts:
    lumCircuitBasicComplV2.setStatus(
        "deprecated"
    )

lumCircuitBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 2, 3)
)
lumCircuitBasicComplV3.setObjects(
      *(("LUM-CIRCUIT-MIB", "circuitGeneralGroup"),
        ("LUM-CIRCUIT-MIB", "circuitStatusGroup"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusGroupV3"))
)
if mibBuilder.loadTexts:
    lumCircuitBasicComplV3.setStatus(
        "deprecated"
    )

lumCircuitBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 2, 4)
)
lumCircuitBasicComplV4.setObjects(
      *(("LUM-CIRCUIT-MIB", "circuitGeneralGroup"),
        ("LUM-CIRCUIT-MIB", "circuitStatusGroup"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusGroupV4"))
)
if mibBuilder.loadTexts:
    lumCircuitBasicComplV4.setStatus(
        "deprecated"
    )

lumCircuitBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 2, 5)
)
lumCircuitBasicComplV5.setObjects(
      *(("LUM-CIRCUIT-MIB", "circuitGeneralGroup"),
        ("LUM-CIRCUIT-MIB", "circuitStatusGroup"),
        ("LUM-CIRCUIT-MIB", "fdfrStatusGroupV5"))
)
if mibBuilder.loadTexts:
    lumCircuitBasicComplV5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-CIRCUIT-MIB",
    **{"lumCircuitMIBModule": lumCircuitMIBModule,
       "lumCircuitConfs": lumCircuitConfs,
       "lumCircuitGroups": lumCircuitGroups,
       "circuitGeneralGroup": circuitGeneralGroup,
       "circuitStatusGroup": circuitStatusGroup,
       "fdfrStatusGroup": fdfrStatusGroup,
       "fdfrStatusGroupV2": fdfrStatusGroupV2,
       "fdfrStatusGroupV3": fdfrStatusGroupV3,
       "fdfrStatusGroupV4": fdfrStatusGroupV4,
       "fdfrStatusGroupV5": fdfrStatusGroupV5,
       "lumCircuitCompl": lumCircuitCompl,
       "lumCircuitBasicComplV1": lumCircuitBasicComplV1,
       "lumCircuitBasicComplV2": lumCircuitBasicComplV2,
       "lumCircuitBasicComplV3": lumCircuitBasicComplV3,
       "lumCircuitBasicComplV4": lumCircuitBasicComplV4,
       "lumCircuitBasicComplV5": lumCircuitBasicComplV5,
       "lumCircuitMIBObjects": lumCircuitMIBObjects,
       "circuitGeneral": circuitGeneral,
       "circuitGeneralConfigLastChangeTime": circuitGeneralConfigLastChangeTime,
       "circuitGeneralStateLastChangeTime": circuitGeneralStateLastChangeTime,
       "circuitGeneralStatusTableSize": circuitGeneralStatusTableSize,
       "circuitStatusList": circuitStatusList,
       "circuitStatusTable": circuitStatusTable,
       "circuitStatusEntry": circuitStatusEntry,
       "circuitStatusIndex": circuitStatusIndex,
       "circuitStatusName": circuitStatusName,
       "circuitStatusDescription": circuitStatusDescription,
       "circuitStatusAdminStatus": circuitStatusAdminStatus,
       "circuitStatusOperStatus": circuitStatusOperStatus,
       "circuitStatusIncomplete": circuitStatusIncomplete,
       "circuitStatusDegraded": circuitStatusDegraded,
       "circuitStatusDown": circuitStatusDown,
       "l2CircuitStatusList": l2CircuitStatusList,
       "fdfrStatusTable": fdfrStatusTable,
       "fdfrStatusEntry": fdfrStatusEntry,
       "fdfrStatusIndex": fdfrStatusIndex,
       "fdfrStatusDown": fdfrStatusDown,
       "fdfrStatusIncomplete": fdfrStatusIncomplete,
       "fdfrStatusUnexpectedMfdfrType": fdfrStatusUnexpectedMfdfrType,
       "fdfrStatusDegraded": fdfrStatusDegraded,
       "fdfrStatusMplsTunnelProtectionFailed": fdfrStatusMplsTunnelProtectionFailed,
       "fdfrStatusMplsTunnelProtectionDegraded": fdfrStatusMplsTunnelProtectionDegraded,
       "fdfrStatusUnknown": fdfrStatusUnknown}
)
