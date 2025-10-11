# SNMP MIB module (ARICENT-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-ARP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:34 2025
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsarp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 109)
)
if mibBuilder.loadTexts:
    fsarp.setRevisions(
        ("2012-09-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Arp_ObjectIdentity = ObjectIdentity
arp = _Arp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 109, 1)
)


class _FsArpCacheTimeout_Type(Integer32):
    """Custom type fsArpCacheTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_FsArpCacheTimeout_Type.__name__ = "Integer32"
_FsArpCacheTimeout_Object = MibScalar
fsArpCacheTimeout = _FsArpCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2076, 109, 1, 1),
    _FsArpCacheTimeout_Type()
)
fsArpCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsArpCacheTimeout.setStatus("current")


class _FsArpCachePendTime_Type(Integer32):
    """Custom type fsArpCachePendTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3000),
    )


_FsArpCachePendTime_Type.__name__ = "Integer32"
_FsArpCachePendTime_Object = MibScalar
fsArpCachePendTime = _FsArpCachePendTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 109, 1, 2),
    _FsArpCachePendTime_Type()
)
fsArpCachePendTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsArpCachePendTime.setStatus("current")


class _FsArpMaxRetries_Type(Integer32):
    """Custom type fsArpMaxRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_FsArpMaxRetries_Type.__name__ = "Integer32"
_FsArpMaxRetries_Object = MibScalar
fsArpMaxRetries = _FsArpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 109, 1, 3),
    _FsArpMaxRetries_Type()
)
fsArpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsArpMaxRetries.setStatus("current")
_Arptest_ObjectIdentity = ObjectIdentity
arptest = _Arptest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 109, 2)
)
_FsArpPendingEntryCount_Type = Integer32
_FsArpPendingEntryCount_Object = MibScalar
fsArpPendingEntryCount = _FsArpPendingEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 109, 2, 1),
    _FsArpPendingEntryCount_Type()
)
fsArpPendingEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsArpPendingEntryCount.setStatus("current")
_FsArpCacheEntryCount_Type = Integer32
_FsArpCacheEntryCount_Object = MibScalar
fsArpCacheEntryCount = _FsArpCacheEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 109, 2, 2),
    _FsArpCacheEntryCount_Type()
)
fsArpCacheEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsArpCacheEntryCount.setStatus("current")
_FsArpRedEntryTime_Type = Integer32
_FsArpRedEntryTime_Object = MibScalar
fsArpRedEntryTime = _FsArpRedEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 109, 2, 3),
    _FsArpRedEntryTime_Type()
)
fsArpRedEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsArpRedEntryTime.setStatus("current")
_FsArpRedExitTime_Type = Integer32
_FsArpRedExitTime_Object = MibScalar
fsArpRedExitTime = _FsArpRedExitTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 109, 2, 4),
    _FsArpRedExitTime_Type()
)
fsArpRedExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsArpRedExitTime.setStatus("current")
_FsArpCacheFlushStatus_Type = TruthValue
_FsArpCacheFlushStatus_Object = MibScalar
fsArpCacheFlushStatus = _FsArpCacheFlushStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 109, 2, 5),
    _FsArpCacheFlushStatus_Type()
)
fsArpCacheFlushStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsArpCacheFlushStatus.setStatus("current")


class _FsArpGlobalDebug_Type(Integer32):
    """Custom type fsArpGlobalDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsArpGlobalDebug_Type.__name__ = "Integer32"
_FsArpGlobalDebug_Object = MibScalar
fsArpGlobalDebug = _FsArpGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 109, 2, 6),
    _FsArpGlobalDebug_Type()
)
fsArpGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsArpGlobalDebug.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-ARP-MIB",
    **{"fsarp": fsarp,
       "arp": arp,
       "fsArpCacheTimeout": fsArpCacheTimeout,
       "fsArpCachePendTime": fsArpCachePendTime,
       "fsArpMaxRetries": fsArpMaxRetries,
       "arptest": arptest,
       "fsArpPendingEntryCount": fsArpPendingEntryCount,
       "fsArpCacheEntryCount": fsArpCacheEntryCount,
       "fsArpRedEntryTime": fsArpRedEntryTime,
       "fsArpRedExitTime": fsArpRedExitTime,
       "fsArpCacheFlushStatus": fsArpCacheFlushStatus,
       "fsArpGlobalDebug": fsArpGlobalDebug}
)
