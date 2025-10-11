# SNMP MIB module (SYNOLOGY-STORAGEIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-STORAGEIO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:58:22 2025
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

storageIO = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 101)
)
if mibBuilder.loadTexts:
    storageIO.setRevisions(
        ("2013-09-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_StorageIOTable_Object = MibTable
storageIOTable = _StorageIOTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1)
)
if mibBuilder.loadTexts:
    storageIOTable.setStatus("current")
_StorageIOEntry_Object = MibTableRow
storageIOEntry = _StorageIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1)
)
storageIOEntry.setIndexNames(
    (0, "SYNOLOGY-STORAGEIO-MIB", "storageIOIndex"),
)
if mibBuilder.loadTexts:
    storageIOEntry.setStatus("current")


class _StorageIOIndex_Type(Integer32):
    """Custom type storageIOIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StorageIOIndex_Type.__name__ = "Integer32"
_StorageIOIndex_Object = MibTableColumn
storageIOIndex = _StorageIOIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 1),
    _StorageIOIndex_Type()
)
storageIOIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    storageIOIndex.setStatus("current")
_StorageIODevice_Type = DisplayString
_StorageIODevice_Object = MibTableColumn
storageIODevice = _StorageIODevice_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 2),
    _StorageIODevice_Type()
)
storageIODevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageIODevice.setStatus("current")
_StorageIONRead_Type = Counter32
_StorageIONRead_Object = MibTableColumn
storageIONRead = _StorageIONRead_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 3),
    _StorageIONRead_Type()
)
storageIONRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageIONRead.setStatus("current")
_StorageIONWritten_Type = Counter32
_StorageIONWritten_Object = MibTableColumn
storageIONWritten = _StorageIONWritten_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 4),
    _StorageIONWritten_Type()
)
storageIONWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageIONWritten.setStatus("current")
_StorageIOReads_Type = Counter32
_StorageIOReads_Object = MibTableColumn
storageIOReads = _StorageIOReads_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 5),
    _StorageIOReads_Type()
)
storageIOReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageIOReads.setStatus("current")
_StorageIOWrites_Type = Counter32
_StorageIOWrites_Object = MibTableColumn
storageIOWrites = _StorageIOWrites_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 6),
    _StorageIOWrites_Type()
)
storageIOWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageIOWrites.setStatus("current")


class _StorageIOLA_Type(Integer32):
    """Custom type storageIOLA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StorageIOLA_Type.__name__ = "Integer32"
_StorageIOLA_Object = MibTableColumn
storageIOLA = _StorageIOLA_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 8),
    _StorageIOLA_Type()
)
storageIOLA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageIOLA.setStatus("current")


class _StorageIOLA1_Type(Integer32):
    """Custom type storageIOLA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StorageIOLA1_Type.__name__ = "Integer32"
_StorageIOLA1_Object = MibTableColumn
storageIOLA1 = _StorageIOLA1_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 9),
    _StorageIOLA1_Type()
)
storageIOLA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageIOLA1.setStatus("current")


class _StorageIOLA5_Type(Integer32):
    """Custom type storageIOLA5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StorageIOLA5_Type.__name__ = "Integer32"
_StorageIOLA5_Object = MibTableColumn
storageIOLA5 = _StorageIOLA5_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 10),
    _StorageIOLA5_Type()
)
storageIOLA5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageIOLA5.setStatus("current")


class _StorageIOLA15_Type(Integer32):
    """Custom type storageIOLA15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StorageIOLA15_Type.__name__ = "Integer32"
_StorageIOLA15_Object = MibTableColumn
storageIOLA15 = _StorageIOLA15_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 11),
    _StorageIOLA15_Type()
)
storageIOLA15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageIOLA15.setStatus("current")
_StorageIONReadX_Type = Counter64
_StorageIONReadX_Object = MibTableColumn
storageIONReadX = _StorageIONReadX_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 12),
    _StorageIONReadX_Type()
)
storageIONReadX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageIONReadX.setStatus("current")
_StorageIONWrittenX_Type = Counter64
_StorageIONWrittenX_Object = MibTableColumn
storageIONWrittenX = _StorageIONWrittenX_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 13),
    _StorageIONWrittenX_Type()
)
storageIONWrittenX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageIONWrittenX.setStatus("current")
_StorageIODeviceSerial_Type = DisplayString
_StorageIODeviceSerial_Object = MibTableColumn
storageIODeviceSerial = _StorageIODeviceSerial_Object(
    (1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 14),
    _StorageIODeviceSerial_Type()
)
storageIODeviceSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageIODeviceSerial.setStatus("current")
_StorageIOConformance_ObjectIdentity = ObjectIdentity
storageIOConformance = _StorageIOConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 101, 2)
)
_StorageIOCompliances_ObjectIdentity = ObjectIdentity
storageIOCompliances = _StorageIOCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 101, 2, 1)
)
_StorageIOGroups_ObjectIdentity = ObjectIdentity
storageIOGroups = _StorageIOGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 101, 2, 2)
)

# Managed Objects groups

storageIOGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 101, 2, 2, 1)
)
storageIOGroup.setObjects(
      *(("SYNOLOGY-STORAGEIO-MIB", "storageIODevice"),
        ("SYNOLOGY-STORAGEIO-MIB", "storageIONRead"),
        ("SYNOLOGY-STORAGEIO-MIB", "storageIONWritten"),
        ("SYNOLOGY-STORAGEIO-MIB", "storageIOReads"),
        ("SYNOLOGY-STORAGEIO-MIB", "storageIOWrites"),
        ("SYNOLOGY-STORAGEIO-MIB", "storageIOLA"),
        ("SYNOLOGY-STORAGEIO-MIB", "storageIOLA1"),
        ("SYNOLOGY-STORAGEIO-MIB", "storageIOLA5"),
        ("SYNOLOGY-STORAGEIO-MIB", "storageIOLA15"),
        ("SYNOLOGY-STORAGEIO-MIB", "storageIONReadX"),
        ("SYNOLOGY-STORAGEIO-MIB", "storageIONWrittenX"),
        ("SYNOLOGY-STORAGEIO-MIB", "storageIODeviceSerial"))
)
if mibBuilder.loadTexts:
    storageIOGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

storageIOCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 101, 2, 1, 1)
)
storageIOCompliance.setObjects(
    ("SYNOLOGY-STORAGEIO-MIB", "storageIOGroup")
)
if mibBuilder.loadTexts:
    storageIOCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-STORAGEIO-MIB",
    **{"synology": synology,
       "storageIO": storageIO,
       "storageIOTable": storageIOTable,
       "storageIOEntry": storageIOEntry,
       "storageIOIndex": storageIOIndex,
       "storageIODevice": storageIODevice,
       "storageIONRead": storageIONRead,
       "storageIONWritten": storageIONWritten,
       "storageIOReads": storageIOReads,
       "storageIOWrites": storageIOWrites,
       "storageIOLA": storageIOLA,
       "storageIOLA1": storageIOLA1,
       "storageIOLA5": storageIOLA5,
       "storageIOLA15": storageIOLA15,
       "storageIONReadX": storageIONReadX,
       "storageIONWrittenX": storageIONWrittenX,
       "storageIODeviceSerial": storageIODeviceSerial,
       "storageIOConformance": storageIOConformance,
       "storageIOCompliances": storageIOCompliances,
       "storageIOCompliance": storageIOCompliance,
       "storageIOGroups": storageIOGroups,
       "storageIOGroup": storageIOGroup}
)
