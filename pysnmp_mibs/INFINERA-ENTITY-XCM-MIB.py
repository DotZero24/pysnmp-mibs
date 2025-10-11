# SNMP MIB module (INFINERA-ENTITY-XCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-XCM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:23 2025
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

(entLPPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLPPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(InfnCorrelatedRedunStatus,
 InfnEqptType,
 InfnXcmTimingSrcRedunState) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnCorrelatedRedunStatus",
    "InfnEqptType",
    "InfnXcmTimingSrcRedunState")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

xcmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmTable_Object = MibTable
xcmTable = _XcmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1)
)
if mibBuilder.loadTexts:
    xcmTable.setStatus("current")
_XcmEntry_Object = MibTableRow
xcmEntry = _XcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1)
)
xcmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    xcmEntry.setStatus("current")
_XcmMoId_Type = DisplayString
_XcmMoId_Object = MibTableColumn
xcmMoId = _XcmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1, 1),
    _XcmMoId_Type()
)
xcmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmMoId.setStatus("current")
_XcmProvType_Type = InfnEqptType
_XcmProvType_Object = MibTableColumn
xcmProvType = _XcmProvType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1, 2),
    _XcmProvType_Type()
)
xcmProvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmProvType.setStatus("current")
_XcmRedundancyStatus_Type = InfnCorrelatedRedunStatus
_XcmRedundancyStatus_Object = MibTableColumn
xcmRedundancyStatus = _XcmRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1, 3),
    _XcmRedundancyStatus_Type()
)
xcmRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRedundancyStatus.setStatus("current")
_XcmBrandingFault_Type = TruthValue
_XcmBrandingFault_Object = MibTableColumn
xcmBrandingFault = _XcmBrandingFault_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1, 4),
    _XcmBrandingFault_Type()
)
xcmBrandingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmBrandingFault.setStatus("current")
_XcmRowStatus_Type = RowStatus
_XcmRowStatus_Object = MibTableColumn
xcmRowStatus = _XcmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1, 5),
    _XcmRowStatus_Type()
)
xcmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRowStatus.setStatus("current")
_TimingSrcRedunState_Type = InfnXcmTimingSrcRedunState
_TimingSrcRedunState_Object = MibTableColumn
timingSrcRedunState = _TimingSrcRedunState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1, 6),
    _TimingSrcRedunState_Type()
)
timingSrcRedunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSrcRedunState.setStatus("current")
_XcmConformance_ObjectIdentity = ObjectIdentity
xcmConformance = _XcmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 3)
)
_XcmCompliances_ObjectIdentity = ObjectIdentity
xcmCompliances = _XcmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 3, 1)
)
_XcmGroups_ObjectIdentity = ObjectIdentity
xcmGroups = _XcmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 3, 2)
)

# Managed Objects groups

xcmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 3, 2, 1)
)
xcmGroup.setObjects(
      *(("INFINERA-ENTITY-XCM-MIB", "xcmBrandingFault"),
        ("INFINERA-ENTITY-XCM-MIB", "xcmMoId"),
        ("INFINERA-ENTITY-XCM-MIB", "xcmProvType"),
        ("INFINERA-ENTITY-XCM-MIB", "xcmRedundancyStatus"),
        ("INFINERA-ENTITY-XCM-MIB", "xcmRowStatus"),
        ("INFINERA-ENTITY-XCM-MIB", "timingSrcRedunState"))
)
if mibBuilder.loadTexts:
    xcmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xcmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 3, 1, 1)
)
xcmCompliance.setObjects(
    ("INFINERA-ENTITY-XCM-MIB", "xcmGroup")
)
if mibBuilder.loadTexts:
    xcmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-XCM-MIB",
    **{"xcmMIB": xcmMIB,
       "xcmTable": xcmTable,
       "xcmEntry": xcmEntry,
       "xcmMoId": xcmMoId,
       "xcmProvType": xcmProvType,
       "xcmRedundancyStatus": xcmRedundancyStatus,
       "xcmBrandingFault": xcmBrandingFault,
       "xcmRowStatus": xcmRowStatus,
       "timingSrcRedunState": timingSrcRedunState,
       "xcmConformance": xcmConformance,
       "xcmCompliances": xcmCompliances,
       "xcmCompliance": xcmCompliance,
       "xcmGroups": xcmGroups,
       "xcmGroup": xcmGroup}
)
