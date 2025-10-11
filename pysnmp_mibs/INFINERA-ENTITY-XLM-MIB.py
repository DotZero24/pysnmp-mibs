# SNMP MIB module (INFINERA-ENTITY-XLM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-XLM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:41 2025
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

(InfnEqptType,
 InfnOperatingMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnEqptType",
    "InfnOperatingMode")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

xlmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XlmTable_Object = MibTable
xlmTable = _XlmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    xlmTable.setStatus("current")
_XlmEntry_Object = MibTableRow
xlmEntry = _XlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 1, 1)
)
xlmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    xlmEntry.setStatus("current")
_XlmMoId_Type = DisplayString
_XlmMoId_Object = MibTableColumn
xlmMoId = _XlmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 1, 1, 1),
    _XlmMoId_Type()
)
xlmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xlmMoId.setStatus("current")
_XlmProvEqptType_Type = InfnEqptType
_XlmProvEqptType_Object = MibTableColumn
xlmProvEqptType = _XlmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 1, 1, 2),
    _XlmProvEqptType_Type()
)
xlmProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xlmProvEqptType.setStatus("current")
_XlmPicDspVer_Type = DisplayString
_XlmPicDspVer_Object = MibTableColumn
xlmPicDspVer = _XlmPicDspVer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 1, 1, 3),
    _XlmPicDspVer_Type()
)
xlmPicDspVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xlmPicDspVer.setStatus("current")


class _XlmOperatingMode_Type(InfnOperatingMode):
    """Custom type xlmOperatingMode based on InfnOperatingMode"""
    defaultValue = 2


_XlmOperatingMode_Type.__name__ = "InfnOperatingMode"
_XlmOperatingMode_Object = MibTableColumn
xlmOperatingMode = _XlmOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 1, 1, 4),
    _XlmOperatingMode_Type()
)
xlmOperatingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xlmOperatingMode.setStatus("current")
_XlmAvailableTunableOcgNumbers_Type = Integer32
_XlmAvailableTunableOcgNumbers_Object = MibTableColumn
xlmAvailableTunableOcgNumbers = _XlmAvailableTunableOcgNumbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 1, 1, 5),
    _XlmAvailableTunableOcgNumbers_Type()
)
xlmAvailableTunableOcgNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xlmAvailableTunableOcgNumbers.setStatus("current")
_XlmProvisionedOcgNumber_Type = Integer32
_XlmProvisionedOcgNumber_Object = MibTableColumn
xlmProvisionedOcgNumber = _XlmProvisionedOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 1, 1, 6),
    _XlmProvisionedOcgNumber_Type()
)
xlmProvisionedOcgNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xlmProvisionedOcgNumber.setStatus("current")
_XlmInstalledOcgNumber_Type = Integer32
_XlmInstalledOcgNumber_Object = MibTableColumn
xlmInstalledOcgNumber = _XlmInstalledOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 1, 1, 7),
    _XlmInstalledOcgNumber_Type()
)
xlmInstalledOcgNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xlmInstalledOcgNumber.setStatus("current")
_XlmRowStatus_Type = RowStatus
_XlmRowStatus_Object = MibTableColumn
xlmRowStatus = _XlmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 1, 1, 8),
    _XlmRowStatus_Type()
)
xlmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xlmRowStatus.setStatus("current")
_XlmConformance_ObjectIdentity = ObjectIdentity
xlmConformance = _XlmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 3)
)
_XlmCompliances_ObjectIdentity = ObjectIdentity
xlmCompliances = _XlmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 3, 1)
)
_XlmGroups_ObjectIdentity = ObjectIdentity
xlmGroups = _XlmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 3, 2)
)

# Managed Objects groups

xlmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 3, 2, 1)
)
xlmGroup.setObjects(
      *(("INFINERA-ENTITY-XLM-MIB", "xlmAvailableTunableOcgNumbers"),
        ("INFINERA-ENTITY-XLM-MIB", "xlmMoId"),
        ("INFINERA-ENTITY-XLM-MIB", "xlmOperatingMode"),
        ("INFINERA-ENTITY-XLM-MIB", "xlmPicDspVer"),
        ("INFINERA-ENTITY-XLM-MIB", "xlmProvEqptType"),
        ("INFINERA-ENTITY-XLM-MIB", "xlmOperatingMode"),
        ("INFINERA-ENTITY-XLM-MIB", "xlmAvailableTunableOcgNumbers"),
        ("INFINERA-ENTITY-XLM-MIB", "xlmProvisionedOcgNumber"),
        ("INFINERA-ENTITY-XLM-MIB", "xlmInstalledOcgNumber"),
        ("INFINERA-ENTITY-XLM-MIB", "xlmRowStatus"))
)
if mibBuilder.loadTexts:
    xlmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xlmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 5, 3, 1, 1)
)
xlmCompliance.setObjects(
    ("INFINERA-ENTITY-XLM-MIB", "xlmGroup")
)
if mibBuilder.loadTexts:
    xlmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-XLM-MIB",
    **{"xlmMIB": xlmMIB,
       "xlmTable": xlmTable,
       "xlmEntry": xlmEntry,
       "xlmMoId": xlmMoId,
       "xlmProvEqptType": xlmProvEqptType,
       "xlmPicDspVer": xlmPicDspVer,
       "xlmOperatingMode": xlmOperatingMode,
       "xlmAvailableTunableOcgNumbers": xlmAvailableTunableOcgNumbers,
       "xlmProvisionedOcgNumber": xlmProvisionedOcgNumber,
       "xlmInstalledOcgNumber": xlmInstalledOcgNumber,
       "xlmRowStatus": xlmRowStatus,
       "xlmConformance": xlmConformance,
       "xlmCompliances": xlmCompliances,
       "xlmCompliance": xlmCompliance,
       "xlmGroups": xlmGroups,
       "xlmGroup": xlmGroup}
)
