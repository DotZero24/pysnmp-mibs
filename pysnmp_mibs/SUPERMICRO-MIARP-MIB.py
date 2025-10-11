# SNMP MIB module (SUPERMICRO-MIARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MIARP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:53 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(fsMIStdIpContextId,) = mibBuilder.importSymbols(
    "SUPERMICRO-MISTD-IPVX-MIB",
    "fsMIStdIpContextId")


# MODULE-IDENTITY

fsMiArp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 33)
)
if mibBuilder.loadTexts:
    fsMiArp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIArpTable_Object = MibTable
fsMIArpTable = _FsMIArpTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1)
)
if mibBuilder.loadTexts:
    fsMIArpTable.setStatus("current")
_FsMIArpEntry_Object = MibTableRow
fsMIArpEntry = _FsMIArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1, 1)
)
fsMIArpEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
)
if mibBuilder.loadTexts:
    fsMIArpEntry.setStatus("current")


class _FsMIArpCacheTimeout_Type(Integer32):
    """Custom type fsMIArpCacheTimeout based on Integer32"""
    defaultValue = 7200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_FsMIArpCacheTimeout_Type.__name__ = "Integer32"
_FsMIArpCacheTimeout_Object = MibTableColumn
fsMIArpCacheTimeout = _FsMIArpCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1, 1, 1),
    _FsMIArpCacheTimeout_Type()
)
fsMIArpCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIArpCacheTimeout.setStatus("current")


class _FsMIArpCachePendTime_Type(Integer32):
    """Custom type fsMIArpCachePendTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3000),
    )


_FsMIArpCachePendTime_Type.__name__ = "Integer32"
_FsMIArpCachePendTime_Object = MibTableColumn
fsMIArpCachePendTime = _FsMIArpCachePendTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1, 1, 2),
    _FsMIArpCachePendTime_Type()
)
fsMIArpCachePendTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIArpCachePendTime.setStatus("current")


class _FsMIArpMaxRetries_Type(Integer32):
    """Custom type fsMIArpMaxRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_FsMIArpMaxRetries_Type.__name__ = "Integer32"
_FsMIArpMaxRetries_Object = MibTableColumn
fsMIArpMaxRetries = _FsMIArpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1, 1, 3),
    _FsMIArpMaxRetries_Type()
)
fsMIArpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIArpMaxRetries.setStatus("current")
_FsMIArpPendingEntryCount_Type = Integer32
_FsMIArpPendingEntryCount_Object = MibTableColumn
fsMIArpPendingEntryCount = _FsMIArpPendingEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1, 1, 4),
    _FsMIArpPendingEntryCount_Type()
)
fsMIArpPendingEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIArpPendingEntryCount.setStatus("current")
_FsMIArpCacheEntryCount_Type = Integer32
_FsMIArpCacheEntryCount_Object = MibTableColumn
fsMIArpCacheEntryCount = _FsMIArpCacheEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1, 1, 5),
    _FsMIArpCacheEntryCount_Type()
)
fsMIArpCacheEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIArpCacheEntryCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MIARP-MIB",
    **{"fsMiArp": fsMiArp,
       "fsMIArpTable": fsMIArpTable,
       "fsMIArpEntry": fsMIArpEntry,
       "fsMIArpCacheTimeout": fsMIArpCacheTimeout,
       "fsMIArpCachePendTime": fsMIArpCachePendTime,
       "fsMIArpMaxRetries": fsMIArpMaxRetries,
       "fsMIArpPendingEntryCount": fsMIArpPendingEntryCount,
       "fsMIArpCacheEntryCount": fsMIArpCacheEntryCount}
)
