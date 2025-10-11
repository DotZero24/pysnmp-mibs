# SNMP MIB module (QTECH-PFXV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-PFXV6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:46 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
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

qtechPFXv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134)
)
if mibBuilder.loadTexts:
    qtechPFXv6MIB.setRevisions(
        ("2015-01-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechPFXv6MIBObjects_ObjectIdentity = ObjectIdentity
qtechPFXv6MIBObjects = _QtechPFXv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1)
)
_QtechPFXv6Table_Object = MibTable
qtechPFXv6Table = _QtechPFXv6Table_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 1)
)
if mibBuilder.loadTexts:
    qtechPFXv6Table.setStatus("current")
_QtechPFXv6Entry_Object = MibTableRow
qtechPFXv6Entry = _QtechPFXv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 1, 1)
)
qtechPFXv6Entry.setIndexNames(
    (0, "QTECH-PFXV6-MIB", "qtechPFXv6Name"),
)
if mibBuilder.loadTexts:
    qtechPFXv6Entry.setStatus("current")


class _QtechPFXv6Name_Type(DisplayString):
    """Custom type qtechPFXv6Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechPFXv6Name_Type.__name__ = "DisplayString"
_QtechPFXv6Name_Object = MibTableColumn
qtechPFXv6Name = _QtechPFXv6Name_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 1, 1, 1),
    _QtechPFXv6Name_Type()
)
qtechPFXv6Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6Name.setStatus("current")
_QtechPFXv6Total_Type = Integer32
_QtechPFXv6Total_Object = MibTableColumn
qtechPFXv6Total = _QtechPFXv6Total_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 1, 1, 2),
    _QtechPFXv6Total_Type()
)
qtechPFXv6Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6Total.setStatus("current")
_QtechPFXv6Rejects_Type = Integer32
_QtechPFXv6Rejects_Object = MibTableColumn
qtechPFXv6Rejects = _QtechPFXv6Rejects_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 1, 1, 3),
    _QtechPFXv6Rejects_Type()
)
qtechPFXv6Rejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6Rejects.setStatus("current")
_QtechPFXv6Accepts_Type = Integer32
_QtechPFXv6Accepts_Object = MibTableColumn
qtechPFXv6Accepts = _QtechPFXv6Accepts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 1, 1, 4),
    _QtechPFXv6Accepts_Type()
)
qtechPFXv6Accepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6Accepts.setStatus("current")
_QtechPFXv6Frees_Type = Integer32
_QtechPFXv6Frees_Object = MibTableColumn
qtechPFXv6Frees = _QtechPFXv6Frees_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 1, 1, 5),
    _QtechPFXv6Frees_Type()
)
qtechPFXv6Frees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6Frees.setStatus("current")


class _QtechPFXv6Userate_Type(Integer32):
    """Custom type qtechPFXv6Userate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechPFXv6Userate_Type.__name__ = "Integer32"
_QtechPFXv6Userate_Object = MibTableColumn
qtechPFXv6Userate = _QtechPFXv6Userate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 1, 1, 6),
    _QtechPFXv6Userate_Type()
)
qtechPFXv6Userate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6Userate.setStatus("current")
_QtechPFXv6IfTable_Object = MibTable
qtechPFXv6IfTable = _QtechPFXv6IfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 2)
)
if mibBuilder.loadTexts:
    qtechPFXv6IfTable.setStatus("current")
_QtechPFXv6IfEntry_Object = MibTableRow
qtechPFXv6IfEntry = _QtechPFXv6IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 2, 1)
)
qtechPFXv6IfEntry.setIndexNames(
    (0, "QTECH-PFXV6-MIB", "qtechPFXv6IfIfIndex"),
)
if mibBuilder.loadTexts:
    qtechPFXv6IfEntry.setStatus("current")
_QtechPFXv6IfIfIndex_Type = IfIndex
_QtechPFXv6IfIfIndex_Object = MibTableColumn
qtechPFXv6IfIfIndex = _QtechPFXv6IfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 2, 1, 1),
    _QtechPFXv6IfIfIndex_Type()
)
qtechPFXv6IfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6IfIfIndex.setStatus("current")


class _QtechPFXv6IfName_Type(DisplayString):
    """Custom type qtechPFXv6IfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechPFXv6IfName_Type.__name__ = "DisplayString"
_QtechPFXv6IfName_Object = MibTableColumn
qtechPFXv6IfName = _QtechPFXv6IfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 2, 1, 2),
    _QtechPFXv6IfName_Type()
)
qtechPFXv6IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6IfName.setStatus("current")
_QtechPFXv6IfTotal_Type = Integer32
_QtechPFXv6IfTotal_Object = MibTableColumn
qtechPFXv6IfTotal = _QtechPFXv6IfTotal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 2, 1, 3),
    _QtechPFXv6IfTotal_Type()
)
qtechPFXv6IfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6IfTotal.setStatus("current")
_QtechPFXv6IfRejects_Type = Integer32
_QtechPFXv6IfRejects_Object = MibTableColumn
qtechPFXv6IfRejects = _QtechPFXv6IfRejects_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 2, 1, 4),
    _QtechPFXv6IfRejects_Type()
)
qtechPFXv6IfRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6IfRejects.setStatus("current")
_QtechPFXv6IfAccepts_Type = Integer32
_QtechPFXv6IfAccepts_Object = MibTableColumn
qtechPFXv6IfAccepts = _QtechPFXv6IfAccepts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 2, 1, 5),
    _QtechPFXv6IfAccepts_Type()
)
qtechPFXv6IfAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6IfAccepts.setStatus("current")
_QtechPFXv6IfFrees_Type = Integer32
_QtechPFXv6IfFrees_Object = MibTableColumn
qtechPFXv6IfFrees = _QtechPFXv6IfFrees_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 2, 1, 6),
    _QtechPFXv6IfFrees_Type()
)
qtechPFXv6IfFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6IfFrees.setStatus("current")


class _QtechPFXv6IfUserate_Type(Integer32):
    """Custom type qtechPFXv6IfUserate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechPFXv6IfUserate_Type.__name__ = "Integer32"
_QtechPFXv6IfUserate_Object = MibTableColumn
qtechPFXv6IfUserate = _QtechPFXv6IfUserate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 2, 1, 7),
    _QtechPFXv6IfUserate_Type()
)
qtechPFXv6IfUserate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPFXv6IfUserate.setStatus("current")
_QtechSlaacRequestNumber_Type = Counter32
_QtechSlaacRequestNumber_Object = MibScalar
qtechSlaacRequestNumber = _QtechSlaacRequestNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 3),
    _QtechSlaacRequestNumber_Type()
)
qtechSlaacRequestNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlaacRequestNumber.setStatus("current")
_QtechSlaacRequestSuccessNumber_Type = Counter32
_QtechSlaacRequestSuccessNumber_Object = MibScalar
qtechSlaacRequestSuccessNumber = _QtechSlaacRequestSuccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 1, 4),
    _QtechSlaacRequestSuccessNumber_Type()
)
qtechSlaacRequestSuccessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlaacRequestSuccessNumber.setStatus("current")
_QtechPFXv6MIBConformance_ObjectIdentity = ObjectIdentity
qtechPFXv6MIBConformance = _QtechPFXv6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 2)
)
_QtechPFXv6MIBCompliances_ObjectIdentity = ObjectIdentity
qtechPFXv6MIBCompliances = _QtechPFXv6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 2, 1)
)
_QtechPFXv6MIBGroups_ObjectIdentity = ObjectIdentity
qtechPFXv6MIBGroups = _QtechPFXv6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 2, 2)
)

# Managed Objects groups

qtechPFXv6MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 2, 2, 1)
)
qtechPFXv6MIBGroup.setObjects(
      *(("QTECH-PFXV6-MIB", "qtechPFXv6Name"),
        ("QTECH-PFXV6-MIB", "qtechPFXv6Total"),
        ("QTECH-PFXV6-MIB", "qtechPFXv6Rejects"),
        ("QTECH-PFXV6-MIB", "qtechPFXv6Accepts"),
        ("QTECH-PFXV6-MIB", "qtechPFXv6Frees"),
        ("QTECH-PFXV6-MIB", "qtechPFXv6Userate"),
        ("QTECH-PFXV6-MIB", "qtechPFXv6IfIfIndex"),
        ("QTECH-PFXV6-MIB", "qtechPFXv6IfName"),
        ("QTECH-PFXV6-MIB", "qtechPFXv6IfTotal"),
        ("QTECH-PFXV6-MIB", "qtechPFXv6IfRejects"),
        ("QTECH-PFXV6-MIB", "qtechPFXv6IfAccepts"),
        ("QTECH-PFXV6-MIB", "qtechPFXv6IfFrees"),
        ("QTECH-PFXV6-MIB", "qtechPFXv6IfUserate"),
        ("QTECH-PFXV6-MIB", "qtechSlaacRequestNumber"),
        ("QTECH-PFXV6-MIB", "qtechSlaacRequestSuccessNumber"))
)
if mibBuilder.loadTexts:
    qtechPFXv6MIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechPFXv6MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 134, 2, 1, 1)
)
qtechPFXv6MIBCompliance.setObjects(
    ("QTECH-PFXV6-MIB", "qtechPFXv6MIBGroup")
)
if mibBuilder.loadTexts:
    qtechPFXv6MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-PFXV6-MIB",
    **{"qtechPFXv6MIB": qtechPFXv6MIB,
       "qtechPFXv6MIBObjects": qtechPFXv6MIBObjects,
       "qtechPFXv6Table": qtechPFXv6Table,
       "qtechPFXv6Entry": qtechPFXv6Entry,
       "qtechPFXv6Name": qtechPFXv6Name,
       "qtechPFXv6Total": qtechPFXv6Total,
       "qtechPFXv6Rejects": qtechPFXv6Rejects,
       "qtechPFXv6Accepts": qtechPFXv6Accepts,
       "qtechPFXv6Frees": qtechPFXv6Frees,
       "qtechPFXv6Userate": qtechPFXv6Userate,
       "qtechPFXv6IfTable": qtechPFXv6IfTable,
       "qtechPFXv6IfEntry": qtechPFXv6IfEntry,
       "qtechPFXv6IfIfIndex": qtechPFXv6IfIfIndex,
       "qtechPFXv6IfName": qtechPFXv6IfName,
       "qtechPFXv6IfTotal": qtechPFXv6IfTotal,
       "qtechPFXv6IfRejects": qtechPFXv6IfRejects,
       "qtechPFXv6IfAccepts": qtechPFXv6IfAccepts,
       "qtechPFXv6IfFrees": qtechPFXv6IfFrees,
       "qtechPFXv6IfUserate": qtechPFXv6IfUserate,
       "qtechSlaacRequestNumber": qtechSlaacRequestNumber,
       "qtechSlaacRequestSuccessNumber": qtechSlaacRequestSuccessNumber,
       "qtechPFXv6MIBConformance": qtechPFXv6MIBConformance,
       "qtechPFXv6MIBCompliances": qtechPFXv6MIBCompliances,
       "qtechPFXv6MIBCompliance": qtechPFXv6MIBCompliance,
       "qtechPFXv6MIBGroups": qtechPFXv6MIBGroups,
       "qtechPFXv6MIBGroup": qtechPFXv6MIBGroup}
)
