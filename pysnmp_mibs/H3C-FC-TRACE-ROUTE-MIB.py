# SNMP MIB module (H3C-FC-TRACE-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-FC-TRACE-ROUTE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:45 2025
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
 H3cFcNameId,
 H3cFcStartOper,
 H3cFcVsanIndex) = mibBuilder.importSymbols(
    "H3C-FC-TC-MIB",
    "H3cFcAddress",
    "H3cFcAddressType",
    "H3cFcNameId",
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

h3cFcTraceRoute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4)
)
if mibBuilder.loadTexts:
    h3cFcTraceRoute.setRevisions(
        ("2013-02-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cFcTraceRouteObjects_ObjectIdentity = ObjectIdentity
h3cFcTraceRouteObjects = _H3cFcTraceRouteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1)
)
_H3cFcTraceRouteConfigurations_ObjectIdentity = ObjectIdentity
h3cFcTraceRouteConfigurations = _H3cFcTraceRouteConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1)
)
_H3cFcTraceRouteTable_Object = MibTable
h3cFcTraceRouteTable = _H3cFcTraceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cFcTraceRouteTable.setStatus("current")
_H3cFcTraceRouteEntry_Object = MibTableRow
h3cFcTraceRouteEntry = _H3cFcTraceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1, 1, 1)
)
h3cFcTraceRouteEntry.setIndexNames(
    (0, "H3C-FC-TRACE-ROUTE-MIB", "h3cFcTraceRouteIndex"),
)
if mibBuilder.loadTexts:
    h3cFcTraceRouteEntry.setStatus("current")


class _H3cFcTraceRouteIndex_Type(Unsigned32):
    """Custom type h3cFcTraceRouteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cFcTraceRouteIndex_Type.__name__ = "Unsigned32"
_H3cFcTraceRouteIndex_Object = MibTableColumn
h3cFcTraceRouteIndex = _H3cFcTraceRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1, 1, 1, 1),
    _H3cFcTraceRouteIndex_Type()
)
h3cFcTraceRouteIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cFcTraceRouteIndex.setStatus("current")
_H3cFcTraceRouteVsan_Type = H3cFcVsanIndex
_H3cFcTraceRouteVsan_Object = MibTableColumn
h3cFcTraceRouteVsan = _H3cFcTraceRouteVsan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1, 1, 1, 2),
    _H3cFcTraceRouteVsan_Type()
)
h3cFcTraceRouteVsan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcTraceRouteVsan.setStatus("current")


class _H3cFcTraceRouteAddressType_Type(H3cFcAddressType):
    """Custom type h3cFcTraceRouteAddressType based on H3cFcAddressType"""
    defaultValue = 2


_H3cFcTraceRouteAddressType_Type.__name__ = "H3cFcAddressType"
_H3cFcTraceRouteAddressType_Object = MibTableColumn
h3cFcTraceRouteAddressType = _H3cFcTraceRouteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1, 1, 1, 3),
    _H3cFcTraceRouteAddressType_Type()
)
h3cFcTraceRouteAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcTraceRouteAddressType.setStatus("current")
_H3cFcTraceRouteAddress_Type = H3cFcAddress
_H3cFcTraceRouteAddress_Object = MibTableColumn
h3cFcTraceRouteAddress = _H3cFcTraceRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1, 1, 1, 4),
    _H3cFcTraceRouteAddress_Type()
)
h3cFcTraceRouteAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcTraceRouteAddress.setStatus("current")


class _H3cFcTraceRouteTimeout_Type(Unsigned32):
    """Custom type h3cFcTraceRouteTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_H3cFcTraceRouteTimeout_Type.__name__ = "Unsigned32"
_H3cFcTraceRouteTimeout_Object = MibTableColumn
h3cFcTraceRouteTimeout = _H3cFcTraceRouteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1, 1, 1, 5),
    _H3cFcTraceRouteTimeout_Type()
)
h3cFcTraceRouteTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcTraceRouteTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cFcTraceRouteTimeout.setUnits("seconds")


class _H3cFcTraceRouteAdminStatus_Type(H3cFcStartOper):
    """Custom type h3cFcTraceRouteAdminStatus based on H3cFcStartOper"""
    defaultValue = 2


_H3cFcTraceRouteAdminStatus_Type.__name__ = "H3cFcStartOper"
_H3cFcTraceRouteAdminStatus_Object = MibTableColumn
h3cFcTraceRouteAdminStatus = _H3cFcTraceRouteAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1, 1, 1, 6),
    _H3cFcTraceRouteAdminStatus_Type()
)
h3cFcTraceRouteAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcTraceRouteAdminStatus.setStatus("current")


class _H3cFcTraceRouteOperStatus_Type(Integer32):
    """Custom type h3cFcTraceRouteOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("success", 2),
          ("partialSuccess", 3),
          ("failure", 4),
          ("disabled", 5))
    )


_H3cFcTraceRouteOperStatus_Type.__name__ = "Integer32"
_H3cFcTraceRouteOperStatus_Object = MibTableColumn
h3cFcTraceRouteOperStatus = _H3cFcTraceRouteOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1, 1, 1, 7),
    _H3cFcTraceRouteOperStatus_Type()
)
h3cFcTraceRouteOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcTraceRouteOperStatus.setStatus("current")


class _H3cFcTraceRouteAgeInterval_Type(Unsigned32):
    """Custom type h3cFcTraceRouteAgeInterval based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 900),
    )


_H3cFcTraceRouteAgeInterval_Type.__name__ = "Unsigned32"
_H3cFcTraceRouteAgeInterval_Object = MibTableColumn
h3cFcTraceRouteAgeInterval = _H3cFcTraceRouteAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1, 1, 1, 8),
    _H3cFcTraceRouteAgeInterval_Type()
)
h3cFcTraceRouteAgeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcTraceRouteAgeInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cFcTraceRouteAgeInterval.setUnits("seconds")


class _H3cFcTraceRouteTrapOnCompletion_Type(TruthValue):
    """Custom type h3cFcTraceRouteTrapOnCompletion based on TruthValue"""
    defaultValue = 2


_H3cFcTraceRouteTrapOnCompletion_Type.__name__ = "TruthValue"
_H3cFcTraceRouteTrapOnCompletion_Object = MibTableColumn
h3cFcTraceRouteTrapOnCompletion = _H3cFcTraceRouteTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1, 1, 1, 9),
    _H3cFcTraceRouteTrapOnCompletion_Type()
)
h3cFcTraceRouteTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcTraceRouteTrapOnCompletion.setStatus("current")
_H3cFcTraceRouteRowStatus_Type = RowStatus
_H3cFcTraceRouteRowStatus_Object = MibTableColumn
h3cFcTraceRouteRowStatus = _H3cFcTraceRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 1, 1, 1, 10),
    _H3cFcTraceRouteRowStatus_Type()
)
h3cFcTraceRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcTraceRouteRowStatus.setStatus("current")
_H3cFcTraceRouteResults_ObjectIdentity = ObjectIdentity
h3cFcTraceRouteResults = _H3cFcTraceRouteResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 2)
)
_H3cFcTraceRouteHopsTable_Object = MibTable
h3cFcTraceRouteHopsTable = _H3cFcTraceRouteHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cFcTraceRouteHopsTable.setStatus("current")
_H3cFcTraceRouteHopsEntry_Object = MibTableRow
h3cFcTraceRouteHopsEntry = _H3cFcTraceRouteHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 2, 1, 1)
)
h3cFcTraceRouteHopsEntry.setIndexNames(
    (0, "H3C-FC-TRACE-ROUTE-MIB", "h3cFcTraceRouteIndex"),
    (0, "H3C-FC-TRACE-ROUTE-MIB", "h3cFcTraceRouteHopsIndex"),
)
if mibBuilder.loadTexts:
    h3cFcTraceRouteHopsEntry.setStatus("current")


class _H3cFcTraceRouteHopsIndex_Type(Unsigned32):
    """Custom type h3cFcTraceRouteHopsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cFcTraceRouteHopsIndex_Type.__name__ = "Unsigned32"
_H3cFcTraceRouteHopsIndex_Object = MibTableColumn
h3cFcTraceRouteHopsIndex = _H3cFcTraceRouteHopsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 2, 1, 1, 1),
    _H3cFcTraceRouteHopsIndex_Type()
)
h3cFcTraceRouteHopsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFcTraceRouteHopsIndex.setStatus("current")
_H3cFcTraceRouteHopsAddr_Type = H3cFcNameId
_H3cFcTraceRouteHopsAddr_Object = MibTableColumn
h3cFcTraceRouteHopsAddr = _H3cFcTraceRouteHopsAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 2, 1, 1, 2),
    _H3cFcTraceRouteHopsAddr_Type()
)
h3cFcTraceRouteHopsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcTraceRouteHopsAddr.setStatus("current")
_H3cFcTraceRouteNotifications_ObjectIdentity = ObjectIdentity
h3cFcTraceRouteNotifications = _H3cFcTraceRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 3)
)
_H3cFcTraceRouteNotifyPrefix_ObjectIdentity = ObjectIdentity
h3cFcTraceRouteNotifyPrefix = _H3cFcTraceRouteNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

h3cFcTraceRouteCompletionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 4, 1, 3, 0, 1)
)
h3cFcTraceRouteCompletionNotify.setObjects(
      *(("H3C-FC-TRACE-ROUTE-MIB", "h3cFcTraceRouteIndex"),
        ("H3C-FC-TRACE-ROUTE-MIB", "h3cFcTraceRouteVsan"),
        ("H3C-FC-TRACE-ROUTE-MIB", "h3cFcTraceRouteAddressType"),
        ("H3C-FC-TRACE-ROUTE-MIB", "h3cFcTraceRouteAddress"),
        ("H3C-FC-TRACE-ROUTE-MIB", "h3cFcTraceRouteOperStatus"))
)
if mibBuilder.loadTexts:
    h3cFcTraceRouteCompletionNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FC-TRACE-ROUTE-MIB",
    **{"h3cFcTraceRoute": h3cFcTraceRoute,
       "h3cFcTraceRouteObjects": h3cFcTraceRouteObjects,
       "h3cFcTraceRouteConfigurations": h3cFcTraceRouteConfigurations,
       "h3cFcTraceRouteTable": h3cFcTraceRouteTable,
       "h3cFcTraceRouteEntry": h3cFcTraceRouteEntry,
       "h3cFcTraceRouteIndex": h3cFcTraceRouteIndex,
       "h3cFcTraceRouteVsan": h3cFcTraceRouteVsan,
       "h3cFcTraceRouteAddressType": h3cFcTraceRouteAddressType,
       "h3cFcTraceRouteAddress": h3cFcTraceRouteAddress,
       "h3cFcTraceRouteTimeout": h3cFcTraceRouteTimeout,
       "h3cFcTraceRouteAdminStatus": h3cFcTraceRouteAdminStatus,
       "h3cFcTraceRouteOperStatus": h3cFcTraceRouteOperStatus,
       "h3cFcTraceRouteAgeInterval": h3cFcTraceRouteAgeInterval,
       "h3cFcTraceRouteTrapOnCompletion": h3cFcTraceRouteTrapOnCompletion,
       "h3cFcTraceRouteRowStatus": h3cFcTraceRouteRowStatus,
       "h3cFcTraceRouteResults": h3cFcTraceRouteResults,
       "h3cFcTraceRouteHopsTable": h3cFcTraceRouteHopsTable,
       "h3cFcTraceRouteHopsEntry": h3cFcTraceRouteHopsEntry,
       "h3cFcTraceRouteHopsIndex": h3cFcTraceRouteHopsIndex,
       "h3cFcTraceRouteHopsAddr": h3cFcTraceRouteHopsAddr,
       "h3cFcTraceRouteNotifications": h3cFcTraceRouteNotifications,
       "h3cFcTraceRouteNotifyPrefix": h3cFcTraceRouteNotifyPrefix,
       "h3cFcTraceRouteCompletionNotify": h3cFcTraceRouteCompletionNotify}
)
