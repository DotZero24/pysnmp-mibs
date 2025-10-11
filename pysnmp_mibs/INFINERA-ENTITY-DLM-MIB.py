# SNMP MIB module (INFINERA-ENTITY-DLM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-DLM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:50 2025
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

dlmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DlmTable_Object = MibTable
dlmTable = _DlmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dlmTable.setStatus("current")
_DlmEntry_Object = MibTableRow
dlmEntry = _DlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 1, 1)
)
dlmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    dlmEntry.setStatus("current")
_DlmMoId_Type = DisplayString
_DlmMoId_Object = MibTableColumn
dlmMoId = _DlmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 1, 1, 1),
    _DlmMoId_Type()
)
dlmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlmMoId.setStatus("current")
_DlmProvEqptType_Type = InfnEqptType
_DlmProvEqptType_Object = MibTableColumn
dlmProvEqptType = _DlmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 1, 1, 2),
    _DlmProvEqptType_Type()
)
dlmProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlmProvEqptType.setStatus("current")
_DlmPicDspVer_Type = DisplayString
_DlmPicDspVer_Object = MibTableColumn
dlmPicDspVer = _DlmPicDspVer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 1, 1, 3),
    _DlmPicDspVer_Type()
)
dlmPicDspVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmPicDspVer.setStatus("current")


class _DlmOperatingMode_Type(InfnOperatingMode):
    """Custom type dlmOperatingMode based on InfnOperatingMode"""
    defaultValue = 2


_DlmOperatingMode_Type.__name__ = "InfnOperatingMode"
_DlmOperatingMode_Object = MibTableColumn
dlmOperatingMode = _DlmOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 1, 1, 4),
    _DlmOperatingMode_Type()
)
dlmOperatingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlmOperatingMode.setStatus("current")
_DlmAvailableTunableOcgNumbers_Type = Integer32
_DlmAvailableTunableOcgNumbers_Object = MibTableColumn
dlmAvailableTunableOcgNumbers = _DlmAvailableTunableOcgNumbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 1, 1, 5),
    _DlmAvailableTunableOcgNumbers_Type()
)
dlmAvailableTunableOcgNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmAvailableTunableOcgNumbers.setStatus("current")
_DlmProvisionedOcgNumber_Type = Integer32
_DlmProvisionedOcgNumber_Object = MibTableColumn
dlmProvisionedOcgNumber = _DlmProvisionedOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 1, 1, 6),
    _DlmProvisionedOcgNumber_Type()
)
dlmProvisionedOcgNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlmProvisionedOcgNumber.setStatus("current")
_DlmInstalledOcgNumber_Type = Integer32
_DlmInstalledOcgNumber_Object = MibTableColumn
dlmInstalledOcgNumber = _DlmInstalledOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 1, 1, 7),
    _DlmInstalledOcgNumber_Type()
)
dlmInstalledOcgNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlmInstalledOcgNumber.setStatus("current")
_DlmRowStatus_Type = RowStatus
_DlmRowStatus_Object = MibTableColumn
dlmRowStatus = _DlmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 1, 1, 8),
    _DlmRowStatus_Type()
)
dlmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlmRowStatus.setStatus("current")
_DlmOpticsFirmwareVer_Type = DisplayString
_DlmOpticsFirmwareVer_Object = MibTableColumn
dlmOpticsFirmwareVer = _DlmOpticsFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 1, 1, 9),
    _DlmOpticsFirmwareVer_Type()
)
dlmOpticsFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmOpticsFirmwareVer.setStatus("current")
_DlmConformance_ObjectIdentity = ObjectIdentity
dlmConformance = _DlmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 3)
)
_DlmCompliances_ObjectIdentity = ObjectIdentity
dlmCompliances = _DlmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 3, 1)
)
_DlmGroups_ObjectIdentity = ObjectIdentity
dlmGroups = _DlmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 3, 2)
)

# Managed Objects groups

dlmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 3, 2, 1)
)
dlmGroup.setObjects(
      *(("INFINERA-ENTITY-DLM-MIB", "dlmAvailableTunableOcgNumbers"),
        ("INFINERA-ENTITY-DLM-MIB", "dlmMoId"),
        ("INFINERA-ENTITY-DLM-MIB", "dlmOperatingMode"),
        ("INFINERA-ENTITY-DLM-MIB", "dlmPicDspVer"),
        ("INFINERA-ENTITY-DLM-MIB", "dlmProvEqptType"),
        ("INFINERA-ENTITY-DLM-MIB", "dlmProvisionedOcgNumber"),
        ("INFINERA-ENTITY-DLM-MIB", "dlmInstalledOcgNumber"),
        ("INFINERA-ENTITY-DLM-MIB", "dlmRowStatus"),
        ("INFINERA-ENTITY-DLM-MIB", "dlmOpticsFirmwareVer"))
)
if mibBuilder.loadTexts:
    dlmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dlmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 4, 3, 1, 1)
)
dlmCompliance.setObjects(
    ("INFINERA-ENTITY-DLM-MIB", "dlmGroup")
)
if mibBuilder.loadTexts:
    dlmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-DLM-MIB",
    **{"dlmMIB": dlmMIB,
       "dlmTable": dlmTable,
       "dlmEntry": dlmEntry,
       "dlmMoId": dlmMoId,
       "dlmProvEqptType": dlmProvEqptType,
       "dlmPicDspVer": dlmPicDspVer,
       "dlmOperatingMode": dlmOperatingMode,
       "dlmAvailableTunableOcgNumbers": dlmAvailableTunableOcgNumbers,
       "dlmProvisionedOcgNumber": dlmProvisionedOcgNumber,
       "dlmInstalledOcgNumber": dlmInstalledOcgNumber,
       "dlmRowStatus": dlmRowStatus,
       "dlmOpticsFirmwareVer": dlmOpticsFirmwareVer,
       "dlmConformance": dlmConformance,
       "dlmCompliances": dlmCompliances,
       "dlmCompliance": dlmCompliance,
       "dlmGroups": dlmGroups,
       "dlmGroup": dlmGroup}
)
