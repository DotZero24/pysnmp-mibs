# SNMP MIB module (H3C-FC-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-FC-PING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:26 2025
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

(H3cFcAddress,
 H3cFcAddressType,
 H3cFcStartOper,
 H3cFcVsanIndex) = mibBuilder.importSymbols(
    "H3C-FC-TC-MIB",
    "H3cFcAddress",
    "H3cFcAddressType",
    "H3cFcStartOper",
    "H3cFcVsanIndex")

(h3cSan,) = mibBuilder.importSymbols(
    "H3C-VSAN-MIB",
    "h3cSan")

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

h3cFcPing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5)
)
if mibBuilder.loadTexts:
    h3cFcPing.setRevisions(
        ("2013-03-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cFcPingObjects_ObjectIdentity = ObjectIdentity
h3cFcPingObjects = _H3cFcPingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1)
)
_H3cFcPingConfigurations_ObjectIdentity = ObjectIdentity
h3cFcPingConfigurations = _H3cFcPingConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1)
)
_H3cFcPingTable_Object = MibTable
h3cFcPingTable = _H3cFcPingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cFcPingTable.setStatus("current")
_H3cFcPingEntry_Object = MibTableRow
h3cFcPingEntry = _H3cFcPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1)
)
h3cFcPingEntry.setIndexNames(
    (0, "H3C-FC-PING-MIB", "h3cFcPingIndex"),
)
if mibBuilder.loadTexts:
    h3cFcPingEntry.setStatus("current")


class _H3cFcPingIndex_Type(Unsigned32):
    """Custom type h3cFcPingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cFcPingIndex_Type.__name__ = "Unsigned32"
_H3cFcPingIndex_Object = MibTableColumn
h3cFcPingIndex = _H3cFcPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 1),
    _H3cFcPingIndex_Type()
)
h3cFcPingIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cFcPingIndex.setStatus("current")
_H3cFcPingVsan_Type = H3cFcVsanIndex
_H3cFcPingVsan_Object = MibTableColumn
h3cFcPingVsan = _H3cFcPingVsan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 2),
    _H3cFcPingVsan_Type()
)
h3cFcPingVsan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPingVsan.setStatus("current")


class _H3cFcPingAddressType_Type(H3cFcAddressType):
    """Custom type h3cFcPingAddressType based on H3cFcAddressType"""
    defaultValue = 2


_H3cFcPingAddressType_Type.__name__ = "H3cFcAddressType"
_H3cFcPingAddressType_Object = MibTableColumn
h3cFcPingAddressType = _H3cFcPingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 3),
    _H3cFcPingAddressType_Type()
)
h3cFcPingAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPingAddressType.setStatus("current")
_H3cFcPingAddress_Type = H3cFcAddress
_H3cFcPingAddress_Object = MibTableColumn
h3cFcPingAddress = _H3cFcPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 4),
    _H3cFcPingAddress_Type()
)
h3cFcPingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPingAddress.setStatus("current")


class _H3cFcPingPacketCount_Type(Unsigned32):
    """Custom type h3cFcPingPacketCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cFcPingPacketCount_Type.__name__ = "Unsigned32"
_H3cFcPingPacketCount_Object = MibTableColumn
h3cFcPingPacketCount = _H3cFcPingPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 5),
    _H3cFcPingPacketCount_Type()
)
h3cFcPingPacketCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPingPacketCount.setStatus("current")
_H3cFcPingPayloadSize_Type = Unsigned32
_H3cFcPingPayloadSize_Object = MibTableColumn
h3cFcPingPayloadSize = _H3cFcPingPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 6),
    _H3cFcPingPayloadSize_Type()
)
h3cFcPingPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPingPayloadSize.setStatus("current")


class _H3cFcPingTimeout_Type(Unsigned32):
    """Custom type h3cFcPingTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_H3cFcPingTimeout_Type.__name__ = "Unsigned32"
_H3cFcPingTimeout_Object = MibTableColumn
h3cFcPingTimeout = _H3cFcPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 7),
    _H3cFcPingTimeout_Type()
)
h3cFcPingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cFcPingTimeout.setUnits("seconds")
_H3cFcPingDelay_Type = Unsigned32
_H3cFcPingDelay_Object = MibTableColumn
h3cFcPingDelay = _H3cFcPingDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 8),
    _H3cFcPingDelay_Type()
)
h3cFcPingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPingDelay.setStatus("current")
if mibBuilder.loadTexts:
    h3cFcPingDelay.setUnits("seconds")


class _H3cFcPingAgeInterval_Type(Unsigned32):
    """Custom type h3cFcPingAgeInterval based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 900),
    )


_H3cFcPingAgeInterval_Type.__name__ = "Unsigned32"
_H3cFcPingAgeInterval_Object = MibTableColumn
h3cFcPingAgeInterval = _H3cFcPingAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 9),
    _H3cFcPingAgeInterval_Type()
)
h3cFcPingAgeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPingAgeInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cFcPingAgeInterval.setUnits("seconds")


class _H3cFcPingAdminStatus_Type(H3cFcStartOper):
    """Custom type h3cFcPingAdminStatus based on H3cFcStartOper"""
    defaultValue = 2


_H3cFcPingAdminStatus_Type.__name__ = "H3cFcStartOper"
_H3cFcPingAdminStatus_Object = MibTableColumn
h3cFcPingAdminStatus = _H3cFcPingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 10),
    _H3cFcPingAdminStatus_Type()
)
h3cFcPingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPingAdminStatus.setStatus("current")


class _H3cFcPingOperStatus_Type(Integer32):
    """Custom type h3cFcPingOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("complete", 2),
          ("disabled", 3),
          ("failed", 4))
    )


_H3cFcPingOperStatus_Type.__name__ = "Integer32"
_H3cFcPingOperStatus_Object = MibTableColumn
h3cFcPingOperStatus = _H3cFcPingOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 11),
    _H3cFcPingOperStatus_Type()
)
h3cFcPingOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPingOperStatus.setStatus("current")


class _H3cFcPingTrapOnCompletion_Type(TruthValue):
    """Custom type h3cFcPingTrapOnCompletion based on TruthValue"""
    defaultValue = 2


_H3cFcPingTrapOnCompletion_Type.__name__ = "TruthValue"
_H3cFcPingTrapOnCompletion_Object = MibTableColumn
h3cFcPingTrapOnCompletion = _H3cFcPingTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 12),
    _H3cFcPingTrapOnCompletion_Type()
)
h3cFcPingTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPingTrapOnCompletion.setStatus("current")
_H3cFcPingRowStatus_Type = RowStatus
_H3cFcPingRowStatus_Object = MibTableColumn
h3cFcPingRowStatus = _H3cFcPingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 1, 1, 1, 13),
    _H3cFcPingRowStatus_Type()
)
h3cFcPingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcPingRowStatus.setStatus("current")
_H3cFcPingStatistics_ObjectIdentity = ObjectIdentity
h3cFcPingStatistics = _H3cFcPingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 2)
)
_H3cFcPingStatTable_Object = MibTable
h3cFcPingStatTable = _H3cFcPingStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cFcPingStatTable.setStatus("current")
_H3cFcPingStatEntry_Object = MibTableRow
h3cFcPingStatEntry = _H3cFcPingStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 2, 1, 1)
)
h3cFcPingStatEntry.setIndexNames(
    (0, "H3C-FC-PING-MIB", "h3cFcPingIndex"),
)
if mibBuilder.loadTexts:
    h3cFcPingStatEntry.setStatus("current")
_H3cFcPingReqPackets_Type = Unsigned32
_H3cFcPingReqPackets_Object = MibTableColumn
h3cFcPingReqPackets = _H3cFcPingReqPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 2, 1, 1, 1),
    _H3cFcPingReqPackets_Type()
)
h3cFcPingReqPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPingReqPackets.setStatus("current")
_H3cFcPingResPackets_Type = Unsigned32
_H3cFcPingResPackets_Object = MibTableColumn
h3cFcPingResPackets = _H3cFcPingResPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 2, 1, 1, 2),
    _H3cFcPingResPackets_Type()
)
h3cFcPingResPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPingResPackets.setStatus("current")
_H3cFcPingMinTime_Type = Integer32
_H3cFcPingMinTime_Object = MibTableColumn
h3cFcPingMinTime = _H3cFcPingMinTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 2, 1, 1, 3),
    _H3cFcPingMinTime_Type()
)
h3cFcPingMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPingMinTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cFcPingMinTime.setUnits("microseconds")
_H3cFcPingAverageTime_Type = Integer32
_H3cFcPingAverageTime_Object = MibTableColumn
h3cFcPingAverageTime = _H3cFcPingAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 2, 1, 1, 4),
    _H3cFcPingAverageTime_Type()
)
h3cFcPingAverageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPingAverageTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cFcPingAverageTime.setUnits("microseconds")
_H3cFcPingMaxTime_Type = Integer32
_H3cFcPingMaxTime_Object = MibTableColumn
h3cFcPingMaxTime = _H3cFcPingMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 2, 1, 1, 5),
    _H3cFcPingMaxTime_Type()
)
h3cFcPingMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPingMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cFcPingMaxTime.setUnits("microseconds")
_H3cFcPingTimeoutNum_Type = Unsigned32
_H3cFcPingTimeoutNum_Object = MibTableColumn
h3cFcPingTimeoutNum = _H3cFcPingTimeoutNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 2, 1, 1, 6),
    _H3cFcPingTimeoutNum_Type()
)
h3cFcPingTimeoutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcPingTimeoutNum.setStatus("current")
_H3cFcPingNotifications_ObjectIdentity = ObjectIdentity
h3cFcPingNotifications = _H3cFcPingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 3)
)
_H3cFcPingNotifyPrefix_ObjectIdentity = ObjectIdentity
h3cFcPingNotifyPrefix = _H3cFcPingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

h3cFcPingCompletionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 5, 1, 3, 0, 1)
)
h3cFcPingCompletionNotify.setObjects(
      *(("H3C-FC-PING-MIB", "h3cFcPingIndex"),
        ("H3C-FC-PING-MIB", "h3cFcPingVsan"),
        ("H3C-FC-PING-MIB", "h3cFcPingAddressType"),
        ("H3C-FC-PING-MIB", "h3cFcPingAddress"),
        ("H3C-FC-PING-MIB", "h3cFcPingReqPackets"),
        ("H3C-FC-PING-MIB", "h3cFcPingResPackets"))
)
if mibBuilder.loadTexts:
    h3cFcPingCompletionNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FC-PING-MIB",
    **{"h3cFcPing": h3cFcPing,
       "h3cFcPingObjects": h3cFcPingObjects,
       "h3cFcPingConfigurations": h3cFcPingConfigurations,
       "h3cFcPingTable": h3cFcPingTable,
       "h3cFcPingEntry": h3cFcPingEntry,
       "h3cFcPingIndex": h3cFcPingIndex,
       "h3cFcPingVsan": h3cFcPingVsan,
       "h3cFcPingAddressType": h3cFcPingAddressType,
       "h3cFcPingAddress": h3cFcPingAddress,
       "h3cFcPingPacketCount": h3cFcPingPacketCount,
       "h3cFcPingPayloadSize": h3cFcPingPayloadSize,
       "h3cFcPingTimeout": h3cFcPingTimeout,
       "h3cFcPingDelay": h3cFcPingDelay,
       "h3cFcPingAgeInterval": h3cFcPingAgeInterval,
       "h3cFcPingAdminStatus": h3cFcPingAdminStatus,
       "h3cFcPingOperStatus": h3cFcPingOperStatus,
       "h3cFcPingTrapOnCompletion": h3cFcPingTrapOnCompletion,
       "h3cFcPingRowStatus": h3cFcPingRowStatus,
       "h3cFcPingStatistics": h3cFcPingStatistics,
       "h3cFcPingStatTable": h3cFcPingStatTable,
       "h3cFcPingStatEntry": h3cFcPingStatEntry,
       "h3cFcPingReqPackets": h3cFcPingReqPackets,
       "h3cFcPingResPackets": h3cFcPingResPackets,
       "h3cFcPingMinTime": h3cFcPingMinTime,
       "h3cFcPingAverageTime": h3cFcPingAverageTime,
       "h3cFcPingMaxTime": h3cFcPingMaxTime,
       "h3cFcPingTimeoutNum": h3cFcPingTimeoutNum,
       "h3cFcPingNotifications": h3cFcPingNotifications,
       "h3cFcPingNotifyPrefix": h3cFcPingNotifyPrefix,
       "h3cFcPingCompletionNotify": h3cFcPingCompletionNotify}
)
