# SNMP MIB module (SYNOLOGY-EBOX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-EBOX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:58:23 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

synologyEbox = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 105)
)
if mibBuilder.loadTexts:
    synologyEbox.setRevisions(
        ("2017-06-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_EboxTable_Object = MibTable
eboxTable = _EboxTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 105, 1)
)
if mibBuilder.loadTexts:
    eboxTable.setStatus("current")
_EboxEntry_Object = MibTableRow
eboxEntry = _EboxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 105, 1, 1)
)
eboxEntry.setIndexNames(
    (0, "SYNOLOGY-EBOX-MIB", "eboxIndex"),
)
if mibBuilder.loadTexts:
    eboxEntry.setStatus("current")
_EboxIndex_Type = Integer32
_EboxIndex_Object = MibTableColumn
eboxIndex = _EboxIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 1),
    _EboxIndex_Type()
)
eboxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eboxIndex.setStatus("current")
_EboxModel_Type = OctetString
_EboxModel_Object = MibTableColumn
eboxModel = _EboxModel_Object(
    (1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 2),
    _EboxModel_Type()
)
eboxModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eboxModel.setStatus("current")
_EboxPower_Type = Integer32
_EboxPower_Object = MibTableColumn
eboxPower = _EboxPower_Object(
    (1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 3),
    _EboxPower_Type()
)
eboxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eboxPower.setStatus("current")
_EboxRedundantPower_Type = Integer32
_EboxRedundantPower_Object = MibTableColumn
eboxRedundantPower = _EboxRedundantPower_Object(
    (1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 4),
    _EboxRedundantPower_Type()
)
eboxRedundantPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eboxRedundantPower.setStatus("current")
_SynologyEboxConformance_ObjectIdentity = ObjectIdentity
synologyEboxConformance = _SynologyEboxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 105, 2)
)
_SynologyEboxCompliances_ObjectIdentity = ObjectIdentity
synologyEboxCompliances = _SynologyEboxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 105, 2, 1)
)
_SynologyEboxGroups_ObjectIdentity = ObjectIdentity
synologyEboxGroups = _SynologyEboxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 105, 2, 2)
)

# Managed Objects groups

synologyEboxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 105, 2, 2, 1)
)
synologyEboxGroup.setObjects(
      *(("SYNOLOGY-EBOX-MIB", "eboxIndex"),
        ("SYNOLOGY-EBOX-MIB", "eboxModel"),
        ("SYNOLOGY-EBOX-MIB", "eboxPower"),
        ("SYNOLOGY-EBOX-MIB", "eboxRedundantPower"))
)
if mibBuilder.loadTexts:
    synologyEboxGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

synologyEboxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 105, 2, 1, 1)
)
synologyEboxCompliance.setObjects(
    ("SYNOLOGY-EBOX-MIB", "synologyEboxGroup")
)
if mibBuilder.loadTexts:
    synologyEboxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-EBOX-MIB",
    **{"synology": synology,
       "synologyEbox": synologyEbox,
       "eboxTable": eboxTable,
       "eboxEntry": eboxEntry,
       "eboxIndex": eboxIndex,
       "eboxModel": eboxModel,
       "eboxPower": eboxPower,
       "eboxRedundantPower": eboxRedundantPower,
       "synologyEboxConformance": synologyEboxConformance,
       "synologyEboxCompliances": synologyEboxCompliances,
       "synologyEboxCompliance": synologyEboxCompliance,
       "synologyEboxGroups": synologyEboxGroups,
       "synologyEboxGroup": synologyEboxGroup}
)
