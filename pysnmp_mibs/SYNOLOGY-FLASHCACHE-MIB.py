# SNMP MIB module (SYNOLOGY-FLASHCACHE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-FLASHCACHE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:58:26 2025
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

flashCache = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 103)
)
if mibBuilder.loadTexts:
    flashCache.setRevisions(
        ("2014-07-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_FlashCacheTable_Object = MibTable
flashCacheTable = _FlashCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1)
)
if mibBuilder.loadTexts:
    flashCacheTable.setStatus("current")
_FlashCacheEntry_Object = MibTableRow
flashCacheEntry = _FlashCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1)
)
flashCacheEntry.setIndexNames(
    (0, "SYNOLOGY-FLASHCACHE-MIB", "flashCacheIndex"),
)
if mibBuilder.loadTexts:
    flashCacheEntry.setStatus("current")


class _FlashCacheIndex_Type(Integer32):
    """Custom type flashCacheIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FlashCacheIndex_Type.__name__ = "Integer32"
_FlashCacheIndex_Object = MibTableColumn
flashCacheIndex = _FlashCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 1),
    _FlashCacheIndex_Type()
)
flashCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flashCacheIndex.setStatus("current")
_FlashCacheSSDDev_Type = DisplayString
_FlashCacheSSDDev_Object = MibTableColumn
flashCacheSSDDev = _FlashCacheSSDDev_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 2),
    _FlashCacheSSDDev_Type()
)
flashCacheSSDDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheSSDDev.setStatus("current")
_FlashCacheSpaceDev_Type = DisplayString
_FlashCacheSpaceDev_Object = MibTableColumn
flashCacheSpaceDev = _FlashCacheSpaceDev_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 3),
    _FlashCacheSpaceDev_Type()
)
flashCacheSpaceDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheSpaceDev.setStatus("current")
_FlashCacheReadHits_Type = Counter64
_FlashCacheReadHits_Object = MibTableColumn
flashCacheReadHits = _FlashCacheReadHits_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 4),
    _FlashCacheReadHits_Type()
)
flashCacheReadHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheReadHits.setStatus("current")
_FlashCacheWriteHits_Type = Counter64
_FlashCacheWriteHits_Object = MibTableColumn
flashCacheWriteHits = _FlashCacheWriteHits_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 5),
    _FlashCacheWriteHits_Type()
)
flashCacheWriteHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheWriteHits.setStatus("current")
_FlashCacheDiskRead_Type = Counter64
_FlashCacheDiskRead_Object = MibTableColumn
flashCacheDiskRead = _FlashCacheDiskRead_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 6),
    _FlashCacheDiskRead_Type()
)
flashCacheDiskRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheDiskRead.setStatus("current")
_FlashCacheDiskWrite_Type = Counter64
_FlashCacheDiskWrite_Object = MibTableColumn
flashCacheDiskWrite = _FlashCacheDiskWrite_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 7),
    _FlashCacheDiskWrite_Type()
)
flashCacheDiskWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheDiskWrite.setStatus("current")
_FlashCacheTotalRead_Type = Counter64
_FlashCacheTotalRead_Object = MibTableColumn
flashCacheTotalRead = _FlashCacheTotalRead_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 8),
    _FlashCacheTotalRead_Type()
)
flashCacheTotalRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheTotalRead.setStatus("current")
_FlashCacheTotalWrite_Type = Counter64
_FlashCacheTotalWrite_Object = MibTableColumn
flashCacheTotalWrite = _FlashCacheTotalWrite_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 9),
    _FlashCacheTotalWrite_Type()
)
flashCacheTotalWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheTotalWrite.setStatus("current")


class _FlashCacheReadHitRate_Type(Integer32):
    """Custom type flashCacheReadHitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FlashCacheReadHitRate_Type.__name__ = "Integer32"
_FlashCacheReadHitRate_Object = MibTableColumn
flashCacheReadHitRate = _FlashCacheReadHitRate_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 10),
    _FlashCacheReadHitRate_Type()
)
flashCacheReadHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheReadHitRate.setStatus("current")


class _FlashCacheWriteHitRate_Type(Integer32):
    """Custom type flashCacheWriteHitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FlashCacheWriteHitRate_Type.__name__ = "Integer32"
_FlashCacheWriteHitRate_Object = MibTableColumn
flashCacheWriteHitRate = _FlashCacheWriteHitRate_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 11),
    _FlashCacheWriteHitRate_Type()
)
flashCacheWriteHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheWriteHitRate.setStatus("current")
_FlashCacheReadSeqSkip_Type = Counter64
_FlashCacheReadSeqSkip_Object = MibTableColumn
flashCacheReadSeqSkip = _FlashCacheReadSeqSkip_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 12),
    _FlashCacheReadSeqSkip_Type()
)
flashCacheReadSeqSkip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheReadSeqSkip.setStatus("current")
_FlashCacheWriteSeqSkip_Type = Counter64
_FlashCacheWriteSeqSkip_Object = MibTableColumn
flashCacheWriteSeqSkip = _FlashCacheWriteSeqSkip_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 13),
    _FlashCacheWriteSeqSkip_Type()
)
flashCacheWriteSeqSkip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheWriteSeqSkip.setStatus("current")
_FlashCacheWriteMissSsd_Type = Counter64
_FlashCacheWriteMissSsd_Object = MibTableColumn
flashCacheWriteMissSsd = _FlashCacheWriteMissSsd_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 14),
    _FlashCacheWriteMissSsd_Type()
)
flashCacheWriteMissSsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheWriteMissSsd.setStatus("current")
_FlashCacheSsdUuid_Type = DisplayString
_FlashCacheSsdUuid_Object = MibTableColumn
flashCacheSsdUuid = _FlashCacheSsdUuid_Object(
    (1, 3, 6, 1, 4, 1, 6574, 103, 1, 1, 15),
    _FlashCacheSsdUuid_Type()
)
flashCacheSsdUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCacheSsdUuid.setStatus("current")
_FlashCacheConformance_ObjectIdentity = ObjectIdentity
flashCacheConformance = _FlashCacheConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 103, 2)
)
_FlashCacheCompliances_ObjectIdentity = ObjectIdentity
flashCacheCompliances = _FlashCacheCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 103, 2, 1)
)
_FlashCacheGroups_ObjectIdentity = ObjectIdentity
flashCacheGroups = _FlashCacheGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 103, 2, 2)
)

# Managed Objects groups

flashCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 103, 2, 2, 1)
)
flashCacheGroup.setObjects(
      *(("SYNOLOGY-FLASHCACHE-MIB", "flashCacheSSDDev"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheSpaceDev"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheReadHits"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheWriteHits"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheDiskRead"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheDiskWrite"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheTotalRead"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheTotalWrite"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheReadHitRate"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheWriteHitRate"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheReadSeqSkip"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheWriteSeqSkip"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheWriteMissSsd"),
        ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheSsdUuid"))
)
if mibBuilder.loadTexts:
    flashCacheGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flashCacheCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 103, 2, 1, 1)
)
flashCacheCompliance.setObjects(
    ("SYNOLOGY-FLASHCACHE-MIB", "flashCacheGroup")
)
if mibBuilder.loadTexts:
    flashCacheCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-FLASHCACHE-MIB",
    **{"synology": synology,
       "flashCache": flashCache,
       "flashCacheTable": flashCacheTable,
       "flashCacheEntry": flashCacheEntry,
       "flashCacheIndex": flashCacheIndex,
       "flashCacheSSDDev": flashCacheSSDDev,
       "flashCacheSpaceDev": flashCacheSpaceDev,
       "flashCacheReadHits": flashCacheReadHits,
       "flashCacheWriteHits": flashCacheWriteHits,
       "flashCacheDiskRead": flashCacheDiskRead,
       "flashCacheDiskWrite": flashCacheDiskWrite,
       "flashCacheTotalRead": flashCacheTotalRead,
       "flashCacheTotalWrite": flashCacheTotalWrite,
       "flashCacheReadHitRate": flashCacheReadHitRate,
       "flashCacheWriteHitRate": flashCacheWriteHitRate,
       "flashCacheReadSeqSkip": flashCacheReadSeqSkip,
       "flashCacheWriteSeqSkip": flashCacheWriteSeqSkip,
       "flashCacheWriteMissSsd": flashCacheWriteMissSsd,
       "flashCacheSsdUuid": flashCacheSsdUuid,
       "flashCacheConformance": flashCacheConformance,
       "flashCacheCompliances": flashCacheCompliances,
       "flashCacheCompliance": flashCacheCompliance,
       "flashCacheGroups": flashCacheGroups,
       "flashCacheGroup": flashCacheGroup}
)
