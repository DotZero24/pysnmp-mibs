# SNMP MIB module (SUPERMICRO-MIPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MIPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:11 2025
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

fsMIPingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36)
)
if mibBuilder.loadTexts:
    fsMIPingMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIPingMIBObjects_ObjectIdentity = ObjectIdentity
fsMIPingMIBObjects = _FsMIPingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1)
)
_FsMIPingTable_Object = MibTable
fsMIPingTable = _FsMIPingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIPingTable.setStatus("current")
_FsMIPingEntry_Object = MibTableRow
fsMIPingEntry = _FsMIPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1)
)
fsMIPingEntry.setIndexNames(
    (0, "SUPERMICRO-MIPING-MIB", "fsMIPingIndex"),
)
if mibBuilder.loadTexts:
    fsMIPingEntry.setStatus("current")


class _FsMIPingIndex_Type(Integer32):
    """Custom type fsMIPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIPingIndex_Type.__name__ = "Integer32"
_FsMIPingIndex_Object = MibTableColumn
fsMIPingIndex = _FsMIPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 1),
    _FsMIPingIndex_Type()
)
fsMIPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPingIndex.setStatus("current")
_FsMIPingDest_Type = IpAddress
_FsMIPingDest_Object = MibTableColumn
fsMIPingDest = _FsMIPingDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 2),
    _FsMIPingDest_Type()
)
fsMIPingDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPingDest.setStatus("current")


class _FsMIPingContextId_Type(Integer32):
    """Custom type fsMIPingContextId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIPingContextId_Type.__name__ = "Integer32"
_FsMIPingContextId_Object = MibTableColumn
fsMIPingContextId = _FsMIPingContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 3),
    _FsMIPingContextId_Type()
)
fsMIPingContextId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPingContextId.setStatus("current")


class _FsMIPingTimeout_Type(Integer32):
    """Custom type fsMIPingTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsMIPingTimeout_Type.__name__ = "Integer32"
_FsMIPingTimeout_Object = MibTableColumn
fsMIPingTimeout = _FsMIPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 4),
    _FsMIPingTimeout_Type()
)
fsMIPingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPingTimeout.setStatus("current")


class _FsMIPingTries_Type(Integer32):
    """Custom type fsMIPingTries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsMIPingTries_Type.__name__ = "Integer32"
_FsMIPingTries_Object = MibTableColumn
fsMIPingTries = _FsMIPingTries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 5),
    _FsMIPingTries_Type()
)
fsMIPingTries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPingTries.setStatus("current")


class _FsMIPingDataSize_Type(Integer32):
    """Custom type fsMIPingDataSize based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2080),
    )


_FsMIPingDataSize_Type.__name__ = "Integer32"
_FsMIPingDataSize_Object = MibTableColumn
fsMIPingDataSize = _FsMIPingDataSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 6),
    _FsMIPingDataSize_Type()
)
fsMIPingDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPingDataSize.setStatus("current")


class _FsMIPingStatus_Type(Integer32):
    """Custom type fsMIPingStatus based on Integer32"""
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


_FsMIPingStatus_Type.__name__ = "Integer32"
_FsMIPingStatus_Object = MibTableColumn
fsMIPingStatus = _FsMIPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 7),
    _FsMIPingStatus_Type()
)
fsMIPingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPingStatus.setStatus("current")


class _FsMIPingSendCount_Type(Integer32):
    """Custom type fsMIPingSendCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIPingSendCount_Type.__name__ = "Integer32"
_FsMIPingSendCount_Object = MibTableColumn
fsMIPingSendCount = _FsMIPingSendCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 8),
    _FsMIPingSendCount_Type()
)
fsMIPingSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPingSendCount.setStatus("current")


class _FsMIPingAverageTime_Type(Integer32):
    """Custom type fsMIPingAverageTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIPingAverageTime_Type.__name__ = "Integer32"
_FsMIPingAverageTime_Object = MibTableColumn
fsMIPingAverageTime = _FsMIPingAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 9),
    _FsMIPingAverageTime_Type()
)
fsMIPingAverageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPingAverageTime.setStatus("current")


class _FsMIPingMaxTime_Type(Integer32):
    """Custom type fsMIPingMaxTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIPingMaxTime_Type.__name__ = "Integer32"
_FsMIPingMaxTime_Object = MibTableColumn
fsMIPingMaxTime = _FsMIPingMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 10),
    _FsMIPingMaxTime_Type()
)
fsMIPingMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPingMaxTime.setStatus("current")


class _FsMIPingMinTime_Type(Integer32):
    """Custom type fsMIPingMinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIPingMinTime_Type.__name__ = "Integer32"
_FsMIPingMinTime_Object = MibTableColumn
fsMIPingMinTime = _FsMIPingMinTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 11),
    _FsMIPingMinTime_Type()
)
fsMIPingMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPingMinTime.setStatus("current")
_FsMIPingSuccesses_Type = Counter32
_FsMIPingSuccesses_Object = MibTableColumn
fsMIPingSuccesses = _FsMIPingSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 12),
    _FsMIPingSuccesses_Type()
)
fsMIPingSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPingSuccesses.setStatus("current")
_FsMIPingEntryStatus_Type = RowStatus
_FsMIPingEntryStatus_Object = MibTableColumn
fsMIPingEntryStatus = _FsMIPingEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 36, 1, 1, 1, 13),
    _FsMIPingEntryStatus_Type()
)
fsMIPingEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPingEntryStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MIPING-MIB",
    **{"fsMIPingMIB": fsMIPingMIB,
       "fsMIPingMIBObjects": fsMIPingMIBObjects,
       "fsMIPingTable": fsMIPingTable,
       "fsMIPingEntry": fsMIPingEntry,
       "fsMIPingIndex": fsMIPingIndex,
       "fsMIPingDest": fsMIPingDest,
       "fsMIPingContextId": fsMIPingContextId,
       "fsMIPingTimeout": fsMIPingTimeout,
       "fsMIPingTries": fsMIPingTries,
       "fsMIPingDataSize": fsMIPingDataSize,
       "fsMIPingStatus": fsMIPingStatus,
       "fsMIPingSendCount": fsMIPingSendCount,
       "fsMIPingAverageTime": fsMIPingAverageTime,
       "fsMIPingMaxTime": fsMIPingMaxTime,
       "fsMIPingMinTime": fsMIPingMinTime,
       "fsMIPingSuccesses": fsMIPingSuccesses,
       "fsMIPingEntryStatus": fsMIPingEntryStatus}
)
