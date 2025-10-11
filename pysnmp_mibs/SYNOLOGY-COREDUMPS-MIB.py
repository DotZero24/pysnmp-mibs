# SNMP MIB module (SYNOLOGY-COREDUMPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-COREDUMPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:58:24 2025
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

synologyCoredump = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 201)
)
if mibBuilder.loadTexts:
    synologyCoredump.setRevisions(
        ("2016-05-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_CoredumpTable_Object = MibTable
coredumpTable = _CoredumpTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 201, 1)
)
if mibBuilder.loadTexts:
    coredumpTable.setStatus("current")
_CoredumpEntry_Object = MibTableRow
coredumpEntry = _CoredumpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 201, 1, 1)
)
coredumpEntry.setIndexNames(
    (0, "SYNOLOGY-COREDUMPS-MIB", "coredumpInfoIndex"),
)
if mibBuilder.loadTexts:
    coredumpEntry.setStatus("current")


class _CoredumpInfoIndex_Type(Integer32):
    """Custom type coredumpInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CoredumpInfoIndex_Type.__name__ = "Integer32"
_CoredumpInfoIndex_Object = MibTableColumn
coredumpInfoIndex = _CoredumpInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 201, 1, 1, 1),
    _CoredumpInfoIndex_Type()
)
coredumpInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coredumpInfoIndex.setStatus("current")
_CoredumpFilePath_Type = OctetString
_CoredumpFilePath_Object = MibTableColumn
coredumpFilePath = _CoredumpFilePath_Object(
    (1, 3, 6, 1, 4, 1, 6574, 201, 1, 1, 2),
    _CoredumpFilePath_Type()
)
coredumpFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coredumpFilePath.setStatus("current")
_CoredumpTimestamp_Type = Integer32
_CoredumpTimestamp_Object = MibTableColumn
coredumpTimestamp = _CoredumpTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6574, 201, 1, 1, 3),
    _CoredumpTimestamp_Type()
)
coredumpTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coredumpTimestamp.setStatus("current")
_SynologyCoredumpConformance_ObjectIdentity = ObjectIdentity
synologyCoredumpConformance = _SynologyCoredumpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 201, 2)
)
_SynologyCoredumpCompliances_ObjectIdentity = ObjectIdentity
synologyCoredumpCompliances = _SynologyCoredumpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 201, 2, 1)
)
_SynologyCoredumpGroups_ObjectIdentity = ObjectIdentity
synologyCoredumpGroups = _SynologyCoredumpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 201, 2, 2)
)

# Managed Objects groups

synologyCoredumpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 201, 2, 2, 1)
)
synologyCoredumpGroup.setObjects(
      *(("SYNOLOGY-COREDUMPS-MIB", "coredumpFilePath"),
        ("SYNOLOGY-COREDUMPS-MIB", "coredumpTimestamp"))
)
if mibBuilder.loadTexts:
    synologyCoredumpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

synologyCoredumpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 201, 2, 1, 1)
)
synologyCoredumpCompliance.setObjects(
    ("SYNOLOGY-COREDUMPS-MIB", "synologyCoredumpGroup")
)
if mibBuilder.loadTexts:
    synologyCoredumpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-COREDUMPS-MIB",
    **{"synology": synology,
       "synologyCoredump": synologyCoredump,
       "coredumpTable": coredumpTable,
       "coredumpEntry": coredumpEntry,
       "coredumpInfoIndex": coredumpInfoIndex,
       "coredumpFilePath": coredumpFilePath,
       "coredumpTimestamp": coredumpTimestamp,
       "synologyCoredumpConformance": synologyCoredumpConformance,
       "synologyCoredumpCompliances": synologyCoredumpCompliances,
       "synologyCoredumpCompliance": synologyCoredumpCompliance,
       "synologyCoredumpGroups": synologyCoredumpGroups,
       "synologyCoredumpGroup": synologyCoredumpGroup}
)
