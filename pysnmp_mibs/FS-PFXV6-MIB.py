# SNMP MIB module (FS-PFXV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-PFXV6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:24 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

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

fsPFXv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134)
)
if mibBuilder.loadTexts:
    fsPFXv6MIB.setRevisions(
        ("2015-01-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPFXv6MIBObjects_ObjectIdentity = ObjectIdentity
fsPFXv6MIBObjects = _FsPFXv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1)
)
_FsPFXv6Table_Object = MibTable
fsPFXv6Table = _FsPFXv6Table_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 1)
)
if mibBuilder.loadTexts:
    fsPFXv6Table.setStatus("current")
_FsPFXv6Entry_Object = MibTableRow
fsPFXv6Entry = _FsPFXv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 1, 1)
)
fsPFXv6Entry.setIndexNames(
    (0, "FS-PFXV6-MIB", "fsPFXv6Name"),
)
if mibBuilder.loadTexts:
    fsPFXv6Entry.setStatus("current")


class _FsPFXv6Name_Type(DisplayString):
    """Custom type fsPFXv6Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsPFXv6Name_Type.__name__ = "DisplayString"
_FsPFXv6Name_Object = MibTableColumn
fsPFXv6Name = _FsPFXv6Name_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 1, 1, 1),
    _FsPFXv6Name_Type()
)
fsPFXv6Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6Name.setStatus("current")
_FsPFXv6Total_Type = Integer32
_FsPFXv6Total_Object = MibTableColumn
fsPFXv6Total = _FsPFXv6Total_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 1, 1, 2),
    _FsPFXv6Total_Type()
)
fsPFXv6Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6Total.setStatus("current")
_FsPFXv6Rejects_Type = Integer32
_FsPFXv6Rejects_Object = MibTableColumn
fsPFXv6Rejects = _FsPFXv6Rejects_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 1, 1, 3),
    _FsPFXv6Rejects_Type()
)
fsPFXv6Rejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6Rejects.setStatus("current")
_FsPFXv6Accepts_Type = Integer32
_FsPFXv6Accepts_Object = MibTableColumn
fsPFXv6Accepts = _FsPFXv6Accepts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 1, 1, 4),
    _FsPFXv6Accepts_Type()
)
fsPFXv6Accepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6Accepts.setStatus("current")
_FsPFXv6Frees_Type = Integer32
_FsPFXv6Frees_Object = MibTableColumn
fsPFXv6Frees = _FsPFXv6Frees_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 1, 1, 5),
    _FsPFXv6Frees_Type()
)
fsPFXv6Frees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6Frees.setStatus("current")


class _FsPFXv6Userate_Type(Integer32):
    """Custom type fsPFXv6Userate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsPFXv6Userate_Type.__name__ = "Integer32"
_FsPFXv6Userate_Object = MibTableColumn
fsPFXv6Userate = _FsPFXv6Userate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 1, 1, 6),
    _FsPFXv6Userate_Type()
)
fsPFXv6Userate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6Userate.setStatus("current")
_FsPFXv6IfTable_Object = MibTable
fsPFXv6IfTable = _FsPFXv6IfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 2)
)
if mibBuilder.loadTexts:
    fsPFXv6IfTable.setStatus("current")
_FsPFXv6IfEntry_Object = MibTableRow
fsPFXv6IfEntry = _FsPFXv6IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 2, 1)
)
fsPFXv6IfEntry.setIndexNames(
    (0, "FS-PFXV6-MIB", "fsPFXv6IfIfIndex"),
)
if mibBuilder.loadTexts:
    fsPFXv6IfEntry.setStatus("current")
_FsPFXv6IfIfIndex_Type = IfIndex
_FsPFXv6IfIfIndex_Object = MibTableColumn
fsPFXv6IfIfIndex = _FsPFXv6IfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 2, 1, 1),
    _FsPFXv6IfIfIndex_Type()
)
fsPFXv6IfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6IfIfIndex.setStatus("current")


class _FsPFXv6IfName_Type(DisplayString):
    """Custom type fsPFXv6IfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsPFXv6IfName_Type.__name__ = "DisplayString"
_FsPFXv6IfName_Object = MibTableColumn
fsPFXv6IfName = _FsPFXv6IfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 2, 1, 2),
    _FsPFXv6IfName_Type()
)
fsPFXv6IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6IfName.setStatus("current")
_FsPFXv6IfTotal_Type = Integer32
_FsPFXv6IfTotal_Object = MibTableColumn
fsPFXv6IfTotal = _FsPFXv6IfTotal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 2, 1, 3),
    _FsPFXv6IfTotal_Type()
)
fsPFXv6IfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6IfTotal.setStatus("current")
_FsPFXv6IfRejects_Type = Integer32
_FsPFXv6IfRejects_Object = MibTableColumn
fsPFXv6IfRejects = _FsPFXv6IfRejects_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 2, 1, 4),
    _FsPFXv6IfRejects_Type()
)
fsPFXv6IfRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6IfRejects.setStatus("current")
_FsPFXv6IfAccepts_Type = Integer32
_FsPFXv6IfAccepts_Object = MibTableColumn
fsPFXv6IfAccepts = _FsPFXv6IfAccepts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 2, 1, 5),
    _FsPFXv6IfAccepts_Type()
)
fsPFXv6IfAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6IfAccepts.setStatus("current")
_FsPFXv6IfFrees_Type = Integer32
_FsPFXv6IfFrees_Object = MibTableColumn
fsPFXv6IfFrees = _FsPFXv6IfFrees_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 2, 1, 6),
    _FsPFXv6IfFrees_Type()
)
fsPFXv6IfFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6IfFrees.setStatus("current")


class _FsPFXv6IfUserate_Type(Integer32):
    """Custom type fsPFXv6IfUserate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsPFXv6IfUserate_Type.__name__ = "Integer32"
_FsPFXv6IfUserate_Object = MibTableColumn
fsPFXv6IfUserate = _FsPFXv6IfUserate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 2, 1, 7),
    _FsPFXv6IfUserate_Type()
)
fsPFXv6IfUserate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFXv6IfUserate.setStatus("current")
_FsSlaacRequestNumber_Type = Counter32
_FsSlaacRequestNumber_Object = MibScalar
fsSlaacRequestNumber = _FsSlaacRequestNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 3),
    _FsSlaacRequestNumber_Type()
)
fsSlaacRequestNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlaacRequestNumber.setStatus("current")
_FsSlaacRequestSuccessNumber_Type = Counter32
_FsSlaacRequestSuccessNumber_Object = MibScalar
fsSlaacRequestSuccessNumber = _FsSlaacRequestSuccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 1, 4),
    _FsSlaacRequestSuccessNumber_Type()
)
fsSlaacRequestSuccessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlaacRequestSuccessNumber.setStatus("current")
_FsPFXv6MIBConformance_ObjectIdentity = ObjectIdentity
fsPFXv6MIBConformance = _FsPFXv6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 2)
)
_FsPFXv6MIBCompliances_ObjectIdentity = ObjectIdentity
fsPFXv6MIBCompliances = _FsPFXv6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 2, 1)
)
_FsPFXv6MIBGroups_ObjectIdentity = ObjectIdentity
fsPFXv6MIBGroups = _FsPFXv6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 2, 2)
)

# Managed Objects groups

fsPFXv6MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 2, 2, 1)
)
fsPFXv6MIBGroup.setObjects(
      *(("FS-PFXV6-MIB", "fsPFXv6Name"),
        ("FS-PFXV6-MIB", "fsPFXv6Total"),
        ("FS-PFXV6-MIB", "fsPFXv6Rejects"),
        ("FS-PFXV6-MIB", "fsPFXv6Accepts"),
        ("FS-PFXV6-MIB", "fsPFXv6Frees"),
        ("FS-PFXV6-MIB", "fsPFXv6Userate"),
        ("FS-PFXV6-MIB", "fsPFXv6IfIfIndex"),
        ("FS-PFXV6-MIB", "fsPFXv6IfName"),
        ("FS-PFXV6-MIB", "fsPFXv6IfTotal"),
        ("FS-PFXV6-MIB", "fsPFXv6IfRejects"),
        ("FS-PFXV6-MIB", "fsPFXv6IfAccepts"),
        ("FS-PFXV6-MIB", "fsPFXv6IfFrees"),
        ("FS-PFXV6-MIB", "fsPFXv6IfUserate"),
        ("FS-PFXV6-MIB", "fsSlaacRequestNumber"),
        ("FS-PFXV6-MIB", "fsSlaacRequestSuccessNumber"))
)
if mibBuilder.loadTexts:
    fsPFXv6MIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsPFXv6MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 134, 2, 1, 1)
)
fsPFXv6MIBCompliance.setObjects(
    ("FS-PFXV6-MIB", "fsPFXv6MIBGroup")
)
if mibBuilder.loadTexts:
    fsPFXv6MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-PFXV6-MIB",
    **{"fsPFXv6MIB": fsPFXv6MIB,
       "fsPFXv6MIBObjects": fsPFXv6MIBObjects,
       "fsPFXv6Table": fsPFXv6Table,
       "fsPFXv6Entry": fsPFXv6Entry,
       "fsPFXv6Name": fsPFXv6Name,
       "fsPFXv6Total": fsPFXv6Total,
       "fsPFXv6Rejects": fsPFXv6Rejects,
       "fsPFXv6Accepts": fsPFXv6Accepts,
       "fsPFXv6Frees": fsPFXv6Frees,
       "fsPFXv6Userate": fsPFXv6Userate,
       "fsPFXv6IfTable": fsPFXv6IfTable,
       "fsPFXv6IfEntry": fsPFXv6IfEntry,
       "fsPFXv6IfIfIndex": fsPFXv6IfIfIndex,
       "fsPFXv6IfName": fsPFXv6IfName,
       "fsPFXv6IfTotal": fsPFXv6IfTotal,
       "fsPFXv6IfRejects": fsPFXv6IfRejects,
       "fsPFXv6IfAccepts": fsPFXv6IfAccepts,
       "fsPFXv6IfFrees": fsPFXv6IfFrees,
       "fsPFXv6IfUserate": fsPFXv6IfUserate,
       "fsSlaacRequestNumber": fsSlaacRequestNumber,
       "fsSlaacRequestSuccessNumber": fsSlaacRequestSuccessNumber,
       "fsPFXv6MIBConformance": fsPFXv6MIBConformance,
       "fsPFXv6MIBCompliances": fsPFXv6MIBCompliances,
       "fsPFXv6MIBCompliance": fsPFXv6MIBCompliance,
       "fsPFXv6MIBGroups": fsPFXv6MIBGroups,
       "fsPFXv6MIBGroup": fsPFXv6MIBGroup}
)
