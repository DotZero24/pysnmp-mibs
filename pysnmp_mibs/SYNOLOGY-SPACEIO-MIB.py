# SNMP MIB module (SYNOLOGY-SPACEIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-SPACEIO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:58:21 2025
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

spaceIO = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 102)
)
if mibBuilder.loadTexts:
    spaceIO.setRevisions(
        ("2013-09-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_SpaceIOTable_Object = MibTable
spaceIOTable = _SpaceIOTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1)
)
if mibBuilder.loadTexts:
    spaceIOTable.setStatus("current")
_SpaceIOEntry_Object = MibTableRow
spaceIOEntry = _SpaceIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1)
)
spaceIOEntry.setIndexNames(
    (0, "SYNOLOGY-SPACEIO-MIB", "spaceIOIndex"),
)
if mibBuilder.loadTexts:
    spaceIOEntry.setStatus("current")


class _SpaceIOIndex_Type(Integer32):
    """Custom type spaceIOIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpaceIOIndex_Type.__name__ = "Integer32"
_SpaceIOIndex_Object = MibTableColumn
spaceIOIndex = _SpaceIOIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 1),
    _SpaceIOIndex_Type()
)
spaceIOIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spaceIOIndex.setStatus("current")
_SpaceIODevice_Type = DisplayString
_SpaceIODevice_Object = MibTableColumn
spaceIODevice = _SpaceIODevice_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 2),
    _SpaceIODevice_Type()
)
spaceIODevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spaceIODevice.setStatus("current")
_SpaceIONRead_Type = Counter32
_SpaceIONRead_Object = MibTableColumn
spaceIONRead = _SpaceIONRead_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 3),
    _SpaceIONRead_Type()
)
spaceIONRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spaceIONRead.setStatus("current")
_SpaceIONWritten_Type = Counter32
_SpaceIONWritten_Object = MibTableColumn
spaceIONWritten = _SpaceIONWritten_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 4),
    _SpaceIONWritten_Type()
)
spaceIONWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spaceIONWritten.setStatus("current")
_SpaceIOReads_Type = Counter32
_SpaceIOReads_Object = MibTableColumn
spaceIOReads = _SpaceIOReads_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 5),
    _SpaceIOReads_Type()
)
spaceIOReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spaceIOReads.setStatus("current")
_SpaceIOWrites_Type = Counter32
_SpaceIOWrites_Object = MibTableColumn
spaceIOWrites = _SpaceIOWrites_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 6),
    _SpaceIOWrites_Type()
)
spaceIOWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spaceIOWrites.setStatus("current")


class _SpaceIOLA_Type(Integer32):
    """Custom type spaceIOLA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SpaceIOLA_Type.__name__ = "Integer32"
_SpaceIOLA_Object = MibTableColumn
spaceIOLA = _SpaceIOLA_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 8),
    _SpaceIOLA_Type()
)
spaceIOLA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spaceIOLA.setStatus("current")


class _SpaceIOLA1_Type(Integer32):
    """Custom type spaceIOLA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SpaceIOLA1_Type.__name__ = "Integer32"
_SpaceIOLA1_Object = MibTableColumn
spaceIOLA1 = _SpaceIOLA1_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 9),
    _SpaceIOLA1_Type()
)
spaceIOLA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spaceIOLA1.setStatus("current")


class _SpaceIOLA5_Type(Integer32):
    """Custom type spaceIOLA5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SpaceIOLA5_Type.__name__ = "Integer32"
_SpaceIOLA5_Object = MibTableColumn
spaceIOLA5 = _SpaceIOLA5_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 10),
    _SpaceIOLA5_Type()
)
spaceIOLA5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spaceIOLA5.setStatus("current")


class _SpaceIOLA15_Type(Integer32):
    """Custom type spaceIOLA15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SpaceIOLA15_Type.__name__ = "Integer32"
_SpaceIOLA15_Object = MibTableColumn
spaceIOLA15 = _SpaceIOLA15_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 11),
    _SpaceIOLA15_Type()
)
spaceIOLA15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spaceIOLA15.setStatus("current")
_SpaceIONReadX_Type = Counter64
_SpaceIONReadX_Object = MibTableColumn
spaceIONReadX = _SpaceIONReadX_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 12),
    _SpaceIONReadX_Type()
)
spaceIONReadX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spaceIONReadX.setStatus("current")
_SpaceIONWrittenX_Type = Counter64
_SpaceIONWrittenX_Object = MibTableColumn
spaceIONWrittenX = _SpaceIONWrittenX_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 13),
    _SpaceIONWrittenX_Type()
)
spaceIONWrittenX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spaceIONWrittenX.setStatus("current")
_SpaceUUID_Type = DisplayString
_SpaceUUID_Object = MibTableColumn
spaceUUID = _SpaceUUID_Object(
    (1, 3, 6, 1, 4, 1, 6574, 102, 1, 1, 14),
    _SpaceUUID_Type()
)
spaceUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spaceUUID.setStatus("current")
_SpaceIOConformance_ObjectIdentity = ObjectIdentity
spaceIOConformance = _SpaceIOConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 102, 2)
)
_SpaceIOCompliances_ObjectIdentity = ObjectIdentity
spaceIOCompliances = _SpaceIOCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 102, 2, 1)
)
_SpaceIOGroups_ObjectIdentity = ObjectIdentity
spaceIOGroups = _SpaceIOGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 102, 2, 2)
)

# Managed Objects groups

spaceIOGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 102, 2, 2, 1)
)
spaceIOGroup.setObjects(
      *(("SYNOLOGY-SPACEIO-MIB", "spaceIODevice"),
        ("SYNOLOGY-SPACEIO-MIB", "spaceIONRead"),
        ("SYNOLOGY-SPACEIO-MIB", "spaceIONWritten"),
        ("SYNOLOGY-SPACEIO-MIB", "spaceIOReads"),
        ("SYNOLOGY-SPACEIO-MIB", "spaceIOWrites"),
        ("SYNOLOGY-SPACEIO-MIB", "spaceIOLA"),
        ("SYNOLOGY-SPACEIO-MIB", "spaceIOLA1"),
        ("SYNOLOGY-SPACEIO-MIB", "spaceIOLA5"),
        ("SYNOLOGY-SPACEIO-MIB", "spaceIOLA15"),
        ("SYNOLOGY-SPACEIO-MIB", "spaceIONReadX"),
        ("SYNOLOGY-SPACEIO-MIB", "spaceIONWrittenX"),
        ("SYNOLOGY-SPACEIO-MIB", "spaceUUID"))
)
if mibBuilder.loadTexts:
    spaceIOGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

spaceIOCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 102, 2, 1, 1)
)
spaceIOCompliance.setObjects(
    ("SYNOLOGY-SPACEIO-MIB", "spaceIOGroup")
)
if mibBuilder.loadTexts:
    spaceIOCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-SPACEIO-MIB",
    **{"synology": synology,
       "spaceIO": spaceIO,
       "spaceIOTable": spaceIOTable,
       "spaceIOEntry": spaceIOEntry,
       "spaceIOIndex": spaceIOIndex,
       "spaceIODevice": spaceIODevice,
       "spaceIONRead": spaceIONRead,
       "spaceIONWritten": spaceIONWritten,
       "spaceIOReads": spaceIOReads,
       "spaceIOWrites": spaceIOWrites,
       "spaceIOLA": spaceIOLA,
       "spaceIOLA1": spaceIOLA1,
       "spaceIOLA5": spaceIOLA5,
       "spaceIOLA15": spaceIOLA15,
       "spaceIONReadX": spaceIONReadX,
       "spaceIONWrittenX": spaceIONWrittenX,
       "spaceUUID": spaceUUID,
       "spaceIOConformance": spaceIOConformance,
       "spaceIOCompliances": spaceIOCompliances,
       "spaceIOCompliance": spaceIOCompliance,
       "spaceIOGroups": spaceIOGroups,
       "spaceIOGroup": spaceIOGroup}
)
