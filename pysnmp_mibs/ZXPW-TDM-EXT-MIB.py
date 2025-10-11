# SNMP MIB module (ZXPW-TDM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXPW-TDM-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:42 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(zxPwCTDM,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxPwCTDM")

(IANAPwTypeTC,) = mibBuilder.importSymbols(
    "ZX-PWE3-MIB",
    "IANAPwTypeTC")

(zxPwIndex,) = mibBuilder.importSymbols(
    "ZXPW-STD-MIB",
    "zxPwIndex")


# MODULE-IDENTITY

zxPwTDMExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PwTDMCfgIndex(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_ZxPwTDMExtObjects_ObjectIdentity = ObjectIdentity
zxPwTDMExtObjects = _ZxPwTDMExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1)
)
_ZxPwTDMExtCardTable_Object = MibTable
zxPwTDMExtCardTable = _ZxPwTDMExtCardTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    zxPwTDMExtCardTable.setStatus("current")
_ZxPwTDMExtCardEntry_Object = MibTableRow
zxPwTDMExtCardEntry = _ZxPwTDMExtCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1, 1)
)
zxPwTDMExtCardEntry.setIndexNames(
    (0, "ZXPW-TDM-EXT-MIB", "zxPwTDMExtRack"),
    (0, "ZXPW-TDM-EXT-MIB", "zxPwTDMExtShelf"),
    (0, "ZXPW-TDM-EXT-MIB", "zxPwTDMExtSlot"),
)
if mibBuilder.loadTexts:
    zxPwTDMExtCardEntry.setStatus("current")
_ZxPwTDMExtRack_Type = Integer32
_ZxPwTDMExtRack_Object = MibTableColumn
zxPwTDMExtRack = _ZxPwTDMExtRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1, 1, 1),
    _ZxPwTDMExtRack_Type()
)
zxPwTDMExtRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxPwTDMExtRack.setStatus("current")
_ZxPwTDMExtShelf_Type = Integer32
_ZxPwTDMExtShelf_Object = MibTableColumn
zxPwTDMExtShelf = _ZxPwTDMExtShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1, 1, 2),
    _ZxPwTDMExtShelf_Type()
)
zxPwTDMExtShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxPwTDMExtShelf.setStatus("current")
_ZxPwTDMExtSlot_Type = Integer32
_ZxPwTDMExtSlot_Object = MibTableColumn
zxPwTDMExtSlot = _ZxPwTDMExtSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1, 1, 3),
    _ZxPwTDMExtSlot_Type()
)
zxPwTDMExtSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxPwTDMExtSlot.setStatus("current")


class _ZxPwTDMExtTDMType_Type(Integer32):
    """Custom type zxPwTDMExtTDMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("udt", 1),
          ("sdtMaster", 2),
          ("sdtSlave", 3),
          ("unconfigured", 9))
    )


_ZxPwTDMExtTDMType_Type.__name__ = "Integer32"
_ZxPwTDMExtTDMType_Object = MibTableColumn
zxPwTDMExtTDMType = _ZxPwTDMExtTDMType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1, 1, 4),
    _ZxPwTDMExtTDMType_Type()
)
zxPwTDMExtTDMType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwTDMExtTDMType.setStatus("current")


class _ZxPwTDMExtTransmitClockSource_Type(Integer32):
    """Custom type zxPwTDMExtTransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3),
          ("adaptive", 4),
          ("enhancedAdaptive", 5),
          ("differential", 6),
          ("lineTiming", 7),
          ("wanderOptimalAdaptive", 8))
    )


_ZxPwTDMExtTransmitClockSource_Type.__name__ = "Integer32"
_ZxPwTDMExtTransmitClockSource_Object = MibTableColumn
zxPwTDMExtTransmitClockSource = _ZxPwTDMExtTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1, 1, 5),
    _ZxPwTDMExtTransmitClockSource_Type()
)
zxPwTDMExtTransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwTDMExtTransmitClockSource.setStatus("current")


class _ZxPwTDMExtPrimaryClock_Type(Integer32):
    """Custom type zxPwTDMExtPrimaryClock based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxPwTDMExtPrimaryClock_Type.__name__ = "Integer32"
_ZxPwTDMExtPrimaryClock_Object = MibTableColumn
zxPwTDMExtPrimaryClock = _ZxPwTDMExtPrimaryClock_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1, 1, 6),
    _ZxPwTDMExtPrimaryClock_Type()
)
zxPwTDMExtPrimaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwTDMExtPrimaryClock.setStatus("current")


class _ZxPwTDMExtSecondaryClock_Type(Integer32):
    """Custom type zxPwTDMExtSecondaryClock based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxPwTDMExtSecondaryClock_Type.__name__ = "Integer32"
_ZxPwTDMExtSecondaryClock_Object = MibTableColumn
zxPwTDMExtSecondaryClock = _ZxPwTDMExtSecondaryClock_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1, 1, 7),
    _ZxPwTDMExtSecondaryClock_Type()
)
zxPwTDMExtSecondaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwTDMExtSecondaryClock.setStatus("current")
_ZxPwTDMExtPwType_Type = IANAPwTypeTC
_ZxPwTDMExtPwType_Object = MibTableColumn
zxPwTDMExtPwType = _ZxPwTDMExtPwType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1, 1, 8),
    _ZxPwTDMExtPwType_Type()
)
zxPwTDMExtPwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwTDMExtPwType.setStatus("current")


class _ZxPwTDMExtReferenceClockSource_Type(Integer32):
    """Custom type zxPwTDMExtReferenceClockSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("line", 2))
    )


_ZxPwTDMExtReferenceClockSource_Type.__name__ = "Integer32"
_ZxPwTDMExtReferenceClockSource_Object = MibTableColumn
zxPwTDMExtReferenceClockSource = _ZxPwTDMExtReferenceClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1, 1, 9),
    _ZxPwTDMExtReferenceClockSource_Type()
)
zxPwTDMExtReferenceClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwTDMExtReferenceClockSource.setStatus("current")


class _ZxPwTDMExtServiceClockSource_Type(Integer32):
    """Custom type zxPwTDMExtServiceClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalClock", 1),
          ("e1Clock", 2))
    )


_ZxPwTDMExtServiceClockSource_Type.__name__ = "Integer32"
_ZxPwTDMExtServiceClockSource_Object = MibTableColumn
zxPwTDMExtServiceClockSource = _ZxPwTDMExtServiceClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1, 1, 10),
    _ZxPwTDMExtServiceClockSource_Type()
)
zxPwTDMExtServiceClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwTDMExtServiceClockSource.setStatus("current")
_ZxPwTDMExtServiceClockE1No_Type = Integer32
_ZxPwTDMExtServiceClockE1No_Object = MibTableColumn
zxPwTDMExtServiceClockE1No = _ZxPwTDMExtServiceClockE1No_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 1, 1, 11),
    _ZxPwTDMExtServiceClockE1No_Type()
)
zxPwTDMExtServiceClockE1No.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwTDMExtServiceClockE1No.setStatus("current")
_ZxPwTDMExtTable_Object = MibTable
zxPwTDMExtTable = _ZxPwTDMExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    zxPwTDMExtTable.setStatus("current")
_ZxPwTDMExtEntry_Object = MibTableRow
zxPwTDMExtEntry = _ZxPwTDMExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 2, 1)
)
zxPwTDMExtEntry.setIndexNames(
    (0, "ZXPW-STD-MIB", "zxPwIndex"),
)
if mibBuilder.loadTexts:
    zxPwTDMExtEntry.setStatus("current")
_ZxPwTDMExtHWNo_Type = Integer32
_ZxPwTDMExtHWNo_Object = MibTableColumn
zxPwTDMExtHWNo = _ZxPwTDMExtHWNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 2, 1, 1),
    _ZxPwTDMExtHWNo_Type()
)
zxPwTDMExtHWNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwTDMExtHWNo.setStatus("current")
_ZxPwTDMExtTSList_Type = DisplayString
_ZxPwTDMExtTSList_Object = MibTableColumn
zxPwTDMExtTSList = _ZxPwTDMExtTSList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 2, 1, 2),
    _ZxPwTDMExtTSList_Type()
)
zxPwTDMExtTSList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwTDMExtTSList.setStatus("current")
_ZxPwExtGenTDMCfgIndex_Type = PwTDMCfgIndex
_ZxPwExtGenTDMCfgIndex_Object = MibTableColumn
zxPwExtGenTDMCfgIndex = _ZxPwExtGenTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 2, 1, 3),
    _ZxPwExtGenTDMCfgIndex_Type()
)
zxPwExtGenTDMCfgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwExtGenTDMCfgIndex.setStatus("current")


class _ZxPwTDMExtFramesPerPacket_Type(Integer32):
    """Custom type zxPwTDMExtFramesPerPacket based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ZxPwTDMExtFramesPerPacket_Type.__name__ = "Integer32"
_ZxPwTDMExtFramesPerPacket_Object = MibTableColumn
zxPwTDMExtFramesPerPacket = _ZxPwTDMExtFramesPerPacket_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 11, 1, 2, 1, 4),
    _ZxPwTDMExtFramesPerPacket_Type()
)
zxPwTDMExtFramesPerPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwTDMExtFramesPerPacket.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXPW-TDM-EXT-MIB",
    **{"PwTDMCfgIndex": PwTDMCfgIndex,
       "zxPwTDMExtMIB": zxPwTDMExtMIB,
       "zxPwTDMExtObjects": zxPwTDMExtObjects,
       "zxPwTDMExtCardTable": zxPwTDMExtCardTable,
       "zxPwTDMExtCardEntry": zxPwTDMExtCardEntry,
       "zxPwTDMExtRack": zxPwTDMExtRack,
       "zxPwTDMExtShelf": zxPwTDMExtShelf,
       "zxPwTDMExtSlot": zxPwTDMExtSlot,
       "zxPwTDMExtTDMType": zxPwTDMExtTDMType,
       "zxPwTDMExtTransmitClockSource": zxPwTDMExtTransmitClockSource,
       "zxPwTDMExtPrimaryClock": zxPwTDMExtPrimaryClock,
       "zxPwTDMExtSecondaryClock": zxPwTDMExtSecondaryClock,
       "zxPwTDMExtPwType": zxPwTDMExtPwType,
       "zxPwTDMExtReferenceClockSource": zxPwTDMExtReferenceClockSource,
       "zxPwTDMExtServiceClockSource": zxPwTDMExtServiceClockSource,
       "zxPwTDMExtServiceClockE1No": zxPwTDMExtServiceClockE1No,
       "zxPwTDMExtTable": zxPwTDMExtTable,
       "zxPwTDMExtEntry": zxPwTDMExtEntry,
       "zxPwTDMExtHWNo": zxPwTDMExtHWNo,
       "zxPwTDMExtTSList": zxPwTDMExtTSList,
       "zxPwExtGenTDMCfgIndex": zxPwExtGenTDMCfgIndex,
       "zxPwTDMExtFramesPerPacket": zxPwTDMExtFramesPerPacket}
)
