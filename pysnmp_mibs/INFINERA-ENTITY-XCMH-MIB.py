# SNMP MIB module (INFINERA-ENTITY-XCMH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-XCMH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:01 2025
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
 InfnEqptType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnCorrelatedRedunStatus",
    "InfnEqptType")

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

xcmhMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmhTable_Object = MibTable
xcmhTable = _XcmhTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1)
)
if mibBuilder.loadTexts:
    xcmhTable.setStatus("current")
_XcmhEntry_Object = MibTableRow
xcmhEntry = _XcmhEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1, 1)
)
xcmhEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    xcmhEntry.setStatus("current")
_XcmhMoId_Type = DisplayString
_XcmhMoId_Object = MibTableColumn
xcmhMoId = _XcmhMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1, 1, 1),
    _XcmhMoId_Type()
)
xcmhMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmhMoId.setStatus("current")
_XcmhProvType_Type = InfnEqptType
_XcmhProvType_Object = MibTableColumn
xcmhProvType = _XcmhProvType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1, 1, 2),
    _XcmhProvType_Type()
)
xcmhProvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmhProvType.setStatus("current")
_XcmhRedundancyStatus_Type = InfnCorrelatedRedunStatus
_XcmhRedundancyStatus_Object = MibTableColumn
xcmhRedundancyStatus = _XcmhRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1, 1, 3),
    _XcmhRedundancyStatus_Type()
)
xcmhRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmhRedundancyStatus.setStatus("current")
_XcmhBrandingFault_Type = TruthValue
_XcmhBrandingFault_Object = MibTableColumn
xcmhBrandingFault = _XcmhBrandingFault_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1, 1, 4),
    _XcmhBrandingFault_Type()
)
xcmhBrandingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmhBrandingFault.setStatus("current")
_XcmhRowStatus_Type = RowStatus
_XcmhRowStatus_Object = MibTableColumn
xcmhRowStatus = _XcmhRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1, 1, 5),
    _XcmhRowStatus_Type()
)
xcmhRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmhRowStatus.setStatus("current")
_XcmhConformance_ObjectIdentity = ObjectIdentity
xcmhConformance = _XcmhConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 3)
)
_XcmhCompliances_ObjectIdentity = ObjectIdentity
xcmhCompliances = _XcmhCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 3, 1)
)
_XcmhGroups_ObjectIdentity = ObjectIdentity
xcmhGroups = _XcmhGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 3, 2)
)

# Managed Objects groups

xcmhGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 3, 2, 1)
)
xcmhGroup.setObjects(
      *(("INFINERA-ENTITY-XCMH-MIB", "xcmhBrandingFault"),
        ("INFINERA-ENTITY-XCMH-MIB", "xcmhMoId"),
        ("INFINERA-ENTITY-XCMH-MIB", "xcmhProvType"),
        ("INFINERA-ENTITY-XCMH-MIB", "xcmhRedundancyStatus"),
        ("INFINERA-ENTITY-XCMH-MIB", "xcmhBrandingFault"),
        ("INFINERA-ENTITY-XCMH-MIB", "xcmhRowStatus"))
)
if mibBuilder.loadTexts:
    xcmhGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xcmhCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 3, 1, 1)
)
xcmhCompliance.setObjects(
    ("INFINERA-ENTITY-XCMH-MIB", "xcmhGroup")
)
if mibBuilder.loadTexts:
    xcmhCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-XCMH-MIB",
    **{"xcmhMIB": xcmhMIB,
       "xcmhTable": xcmhTable,
       "xcmhEntry": xcmhEntry,
       "xcmhMoId": xcmhMoId,
       "xcmhProvType": xcmhProvType,
       "xcmhRedundancyStatus": xcmhRedundancyStatus,
       "xcmhBrandingFault": xcmhBrandingFault,
       "xcmhRowStatus": xcmhRowStatus,
       "xcmhConformance": xcmhConformance,
       "xcmhCompliances": xcmhCompliances,
       "xcmhCompliance": xcmhCompliance,
       "xcmhGroups": xcmhGroups,
       "xcmhGroup": xcmhGroup}
)
