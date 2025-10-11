# SNMP MIB module (MX-H323-ALIASES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-H323-ALIASES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:41 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(h323,) = mibBuilder.importSymbols(
    "MX-H323-MIB",
    "h323")

(groupIndex,) = mibBuilder.importSymbols(
    "MX-LINE-GROUPING-MIB",
    "groupIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

h323AliasesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15)
)
if mibBuilder.loadTexts:
    h323AliasesMIB.setRevisions(
        ("1903-03-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H323AliasesMIBObjects_ObjectIdentity = ObjectIdentity
h323AliasesMIBObjects = _H323AliasesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1)
)
_H323AliasesIfAliasesTable_Object = MibTable
h323AliasesIfAliasesTable = _H323AliasesIfAliasesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 5)
)
if mibBuilder.loadTexts:
    h323AliasesIfAliasesTable.setStatus("current")
_H323AliasesIfAliasesEntry_Object = MibTableRow
h323AliasesIfAliasesEntry = _H323AliasesIfAliasesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 5, 1)
)
h323AliasesIfAliasesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323AliasesIfAliasesEntry.setStatus("current")


class _H323AliasesGroupIndex_Type(Unsigned32):
    """Custom type h323AliasesGroupIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_H323AliasesGroupIndex_Type.__name__ = "Unsigned32"
_H323AliasesGroupIndex_Object = MibTableColumn
h323AliasesGroupIndex = _H323AliasesGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 5, 1, 5),
    _H323AliasesGroupIndex_Type()
)
h323AliasesGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323AliasesGroupIndex.setStatus("current")


class _H323AliasesConfigured_Type(OctetString):
    """Custom type h323AliasesConfigured based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H323AliasesConfigured_Type.__name__ = "OctetString"
_H323AliasesConfigured_Object = MibTableColumn
h323AliasesConfigured = _H323AliasesConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 5, 1, 10),
    _H323AliasesConfigured_Type()
)
h323AliasesConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AliasesConfigured.setStatus("current")


class _H323AliasesCurrent_Type(OctetString):
    """Custom type h323AliasesCurrent based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H323AliasesCurrent_Type.__name__ = "OctetString"
_H323AliasesCurrent_Object = MibTableColumn
h323AliasesCurrent = _H323AliasesCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 5, 1, 15),
    _H323AliasesCurrent_Type()
)
h323AliasesCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323AliasesCurrent.setStatus("current")
_H323AliasesGroupAliasesTable_Object = MibTable
h323AliasesGroupAliasesTable = _H323AliasesGroupAliasesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 10)
)
if mibBuilder.loadTexts:
    h323AliasesGroupAliasesTable.setStatus("current")
_H323AliasesGroupAliasesEntry_Object = MibTableRow
h323AliasesGroupAliasesEntry = _H323AliasesGroupAliasesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 10, 1)
)
h323AliasesGroupAliasesEntry.setIndexNames(
    (0, "MX-LINE-GROUPING-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    h323AliasesGroupAliasesEntry.setStatus("current")


class _H323GroupAliasesConfigured_Type(OctetString):
    """Custom type h323GroupAliasesConfigured based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H323GroupAliasesConfigured_Type.__name__ = "OctetString"
_H323GroupAliasesConfigured_Object = MibTableColumn
h323GroupAliasesConfigured = _H323GroupAliasesConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 10, 1, 5),
    _H323GroupAliasesConfigured_Type()
)
h323GroupAliasesConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GroupAliasesConfigured.setStatus("current")


class _H323GroupAliasesCurrent_Type(OctetString):
    """Custom type h323GroupAliasesCurrent based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H323GroupAliasesCurrent_Type.__name__ = "OctetString"
_H323GroupAliasesCurrent_Object = MibTableColumn
h323GroupAliasesCurrent = _H323GroupAliasesCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 1, 10, 1, 10),
    _H323GroupAliasesCurrent_Type()
)
h323GroupAliasesCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GroupAliasesCurrent.setStatus("current")
_H323AliasesConformance_ObjectIdentity = ObjectIdentity
h323AliasesConformance = _H323AliasesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 2)
)
_H323AliasesCompliances_ObjectIdentity = ObjectIdentity
h323AliasesCompliances = _H323AliasesCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 2, 1)
)
_H323AliasesGroups_ObjectIdentity = ObjectIdentity
h323AliasesGroups = _H323AliasesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 2, 2)
)

# Managed Objects groups

h323AliasesLineAliasesGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 2, 2, 5)
)
h323AliasesLineAliasesGroupVer1.setObjects(
      *(("MX-H323-ALIASES-MIB", "h323AliasesConfigured"),
        ("MX-H323-ALIASES-MIB", "h323AliasesCurrent"))
)
if mibBuilder.loadTexts:
    h323AliasesLineAliasesGroupVer1.setStatus("current")

h323AliasesGroupAliasesGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 2, 2, 10)
)
h323AliasesGroupAliasesGroupVer1.setObjects(
      *(("MX-H323-ALIASES-MIB", "h323GroupAliasesConfigured"),
        ("MX-H323-ALIASES-MIB", "h323GroupAliasesCurrent"))
)
if mibBuilder.loadTexts:
    h323AliasesGroupAliasesGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h323AliasesBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 15, 2, 1, 5)
)
h323AliasesBasicComplVer1.setObjects(
      *(("MX-H323-ALIASES-MIB", "h323AliasesLineAliasesGroupVer1"),
        ("MX-H323-ALIASES-MIB", "h323AliasesGroupAliasesGroupVer1"))
)
if mibBuilder.loadTexts:
    h323AliasesBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-H323-ALIASES-MIB",
    **{"h323AliasesMIB": h323AliasesMIB,
       "h323AliasesMIBObjects": h323AliasesMIBObjects,
       "h323AliasesIfAliasesTable": h323AliasesIfAliasesTable,
       "h323AliasesIfAliasesEntry": h323AliasesIfAliasesEntry,
       "h323AliasesGroupIndex": h323AliasesGroupIndex,
       "h323AliasesConfigured": h323AliasesConfigured,
       "h323AliasesCurrent": h323AliasesCurrent,
       "h323AliasesGroupAliasesTable": h323AliasesGroupAliasesTable,
       "h323AliasesGroupAliasesEntry": h323AliasesGroupAliasesEntry,
       "h323GroupAliasesConfigured": h323GroupAliasesConfigured,
       "h323GroupAliasesCurrent": h323GroupAliasesCurrent,
       "h323AliasesConformance": h323AliasesConformance,
       "h323AliasesCompliances": h323AliasesCompliances,
       "h323AliasesBasicComplVer1": h323AliasesBasicComplVer1,
       "h323AliasesGroups": h323AliasesGroups,
       "h323AliasesLineAliasesGroupVer1": h323AliasesLineAliasesGroupVer1,
       "h323AliasesGroupAliasesGroupVer1": h323AliasesGroupAliasesGroupVer1}
)
