# SNMP MIB module (SUPERMICRO-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-PING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:59 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsPingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106)
)
if mibBuilder.loadTexts:
    fsPingMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPingMIBObjects_ObjectIdentity = ObjectIdentity
fsPingMIBObjects = _FsPingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1)
)
_FsPingTable_Object = MibTable
fsPingTable = _FsPingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1)
)
if mibBuilder.loadTexts:
    fsPingTable.setStatus("current")
_FsPingEntry_Object = MibTableRow
fsPingEntry = _FsPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1)
)
fsPingEntry.setIndexNames(
    (0, "SUPERMICRO-PING-MIB", "fsPingIndex"),
)
if mibBuilder.loadTexts:
    fsPingEntry.setStatus("current")


class _FsPingIndex_Type(Integer32):
    """Custom type fsPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPingIndex_Type.__name__ = "Integer32"
_FsPingIndex_Object = MibTableColumn
fsPingIndex = _FsPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1, 1),
    _FsPingIndex_Type()
)
fsPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPingIndex.setStatus("current")
_FsPingDest_Type = IpAddress
_FsPingDest_Object = MibTableColumn
fsPingDest = _FsPingDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1, 2),
    _FsPingDest_Type()
)
fsPingDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingDest.setStatus("current")


class _FsPingTimeout_Type(Integer32):
    """Custom type fsPingTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsPingTimeout_Type.__name__ = "Integer32"
_FsPingTimeout_Object = MibTableColumn
fsPingTimeout = _FsPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1, 3),
    _FsPingTimeout_Type()
)
fsPingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingTimeout.setStatus("current")


class _FsPingTries_Type(Integer32):
    """Custom type fsPingTries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsPingTries_Type.__name__ = "Integer32"
_FsPingTries_Object = MibTableColumn
fsPingTries = _FsPingTries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1, 4),
    _FsPingTries_Type()
)
fsPingTries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingTries.setStatus("current")


class _FsPingDataSize_Type(Integer32):
    """Custom type fsPingDataSize based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2080),
    )


_FsPingDataSize_Type.__name__ = "Integer32"
_FsPingDataSize_Object = MibTableColumn
fsPingDataSize = _FsPingDataSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1, 5),
    _FsPingDataSize_Type()
)
fsPingDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingDataSize.setStatus("current")


class _FsPingStatus_Type(Integer32):
    """Custom type fsPingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notinitiated", 1),
          ("progress", 2),
          ("completed", 3))
    )


_FsPingStatus_Type.__name__ = "Integer32"
_FsPingStatus_Object = MibTableColumn
fsPingStatus = _FsPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1, 6),
    _FsPingStatus_Type()
)
fsPingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPingStatus.setStatus("current")


class _FsPingSendCount_Type(Integer32):
    """Custom type fsPingSendCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPingSendCount_Type.__name__ = "Integer32"
_FsPingSendCount_Object = MibTableColumn
fsPingSendCount = _FsPingSendCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1, 7),
    _FsPingSendCount_Type()
)
fsPingSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPingSendCount.setStatus("current")


class _FsPingAverageTime_Type(Integer32):
    """Custom type fsPingAverageTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPingAverageTime_Type.__name__ = "Integer32"
_FsPingAverageTime_Object = MibTableColumn
fsPingAverageTime = _FsPingAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1, 8),
    _FsPingAverageTime_Type()
)
fsPingAverageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPingAverageTime.setStatus("current")


class _FsPingMaxTime_Type(Integer32):
    """Custom type fsPingMaxTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPingMaxTime_Type.__name__ = "Integer32"
_FsPingMaxTime_Object = MibTableColumn
fsPingMaxTime = _FsPingMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1, 9),
    _FsPingMaxTime_Type()
)
fsPingMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPingMaxTime.setStatus("current")


class _FsPingMinTime_Type(Integer32):
    """Custom type fsPingMinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPingMinTime_Type.__name__ = "Integer32"
_FsPingMinTime_Object = MibTableColumn
fsPingMinTime = _FsPingMinTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1, 10),
    _FsPingMinTime_Type()
)
fsPingMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPingMinTime.setStatus("current")
_FsPingSuccesses_Type = Counter32
_FsPingSuccesses_Object = MibTableColumn
fsPingSuccesses = _FsPingSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1, 11),
    _FsPingSuccesses_Type()
)
fsPingSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPingSuccesses.setStatus("current")
_FsPingEntryStatus_Type = RowStatus
_FsPingEntryStatus_Object = MibTableColumn
fsPingEntryStatus = _FsPingEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 106, 1, 1, 1, 12),
    _FsPingEntryStatus_Type()
)
fsPingEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingEntryStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-PING-MIB",
    **{"fsPingMIB": fsPingMIB,
       "fsPingMIBObjects": fsPingMIBObjects,
       "fsPingTable": fsPingTable,
       "fsPingEntry": fsPingEntry,
       "fsPingIndex": fsPingIndex,
       "fsPingDest": fsPingDest,
       "fsPingTimeout": fsPingTimeout,
       "fsPingTries": fsPingTries,
       "fsPingDataSize": fsPingDataSize,
       "fsPingStatus": fsPingStatus,
       "fsPingSendCount": fsPingSendCount,
       "fsPingAverageTime": fsPingAverageTime,
       "fsPingMaxTime": fsPingMaxTime,
       "fsPingMinTime": fsPingMinTime,
       "fsPingSuccesses": fsPingSuccesses,
       "fsPingEntryStatus": fsPingEntryStatus}
)
