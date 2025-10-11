# SNMP MIB module (AX-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/a10/AX-BGP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:57 2025
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

(a10Mgmt,) = mibBuilder.importSymbols(
    "A10-COMMON-MIB",
    "a10Mgmt")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber",
    "InetPortNumber")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

axBgpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxBgpNotification_ObjectIdentity = ObjectIdentity
axBgpNotification = _AxBgpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 0)
)


class _AxBgpVersion_Type(OctetString):
    """Custom type axBgpVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AxBgpVersion_Type.__name__ = "OctetString"
_AxBgpVersion_Object = MibScalar
axBgpVersion = _AxBgpVersion_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 1),
    _AxBgpVersion_Type()
)
axBgpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpVersion.setStatus("current")
_AxBgpLocalAs_Type = InetAutonomousSystemNumber
_AxBgpLocalAs_Object = MibScalar
axBgpLocalAs = _AxBgpLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 2),
    _AxBgpLocalAs_Type()
)
axBgpLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpLocalAs.setStatus("current")
_AxBgpIdentifier_Type = IpAddress
_AxBgpIdentifier_Object = MibScalar
axBgpIdentifier = _AxBgpIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 3),
    _AxBgpIdentifier_Type()
)
axBgpIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpIdentifier.setStatus("current")
_AxBgpPeerTable_Object = MibTable
axBgpPeerTable = _AxBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4)
)
if mibBuilder.loadTexts:
    axBgpPeerTable.setStatus("current")
_AxBgpPeerEntry_Object = MibTableRow
axBgpPeerEntry = _AxBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1)
)
axBgpPeerEntry.setIndexNames(
    (0, "AX-BGP-MIB", "axBgpPeerType"),
    (0, "AX-BGP-MIB", "axBgpPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    axBgpPeerEntry.setStatus("current")
_AxBgpPeerType_Type = InetAddressType
_AxBgpPeerType_Object = MibTableColumn
axBgpPeerType = _AxBgpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 1),
    _AxBgpPeerType_Type()
)
axBgpPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axBgpPeerType.setStatus("current")
_AxBgpPeerIdentifier_Type = IpAddress
_AxBgpPeerIdentifier_Object = MibTableColumn
axBgpPeerIdentifier = _AxBgpPeerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 2),
    _AxBgpPeerIdentifier_Type()
)
axBgpPeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerIdentifier.setStatus("current")


class _AxBgpPeerState_Type(Integer32):
    """Custom type axBgpPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )


_AxBgpPeerState_Type.__name__ = "Integer32"
_AxBgpPeerState_Object = MibTableColumn
axBgpPeerState = _AxBgpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 3),
    _AxBgpPeerState_Type()
)
axBgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerState.setStatus("current")


class _AxBgpPeerAdminStatus_Type(Integer32):
    """Custom type axBgpPeerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2))
    )


_AxBgpPeerAdminStatus_Type.__name__ = "Integer32"
_AxBgpPeerAdminStatus_Object = MibTableColumn
axBgpPeerAdminStatus = _AxBgpPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 4),
    _AxBgpPeerAdminStatus_Type()
)
axBgpPeerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerAdminStatus.setStatus("current")
_AxBgpPeerNegotiatedVersion_Type = Integer32
_AxBgpPeerNegotiatedVersion_Object = MibTableColumn
axBgpPeerNegotiatedVersion = _AxBgpPeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 5),
    _AxBgpPeerNegotiatedVersion_Type()
)
axBgpPeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerNegotiatedVersion.setStatus("current")
_AxBgpPeerLocalAddr_Type = InetAddress
_AxBgpPeerLocalAddr_Object = MibTableColumn
axBgpPeerLocalAddr = _AxBgpPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 6),
    _AxBgpPeerLocalAddr_Type()
)
axBgpPeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerLocalAddr.setStatus("current")


class _AxBgpPeerLocalPort_Type(Integer32):
    """Custom type axBgpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AxBgpPeerLocalPort_Type.__name__ = "Integer32"
_AxBgpPeerLocalPort_Object = MibTableColumn
axBgpPeerLocalPort = _AxBgpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 7),
    _AxBgpPeerLocalPort_Type()
)
axBgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerLocalPort.setStatus("current")
_AxBgpPeerRemoteAddr_Type = InetAddress
_AxBgpPeerRemoteAddr_Object = MibTableColumn
axBgpPeerRemoteAddr = _AxBgpPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 8),
    _AxBgpPeerRemoteAddr_Type()
)
axBgpPeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerRemoteAddr.setStatus("current")


class _AxBgpPeerRemotePort_Type(Integer32):
    """Custom type axBgpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AxBgpPeerRemotePort_Type.__name__ = "Integer32"
_AxBgpPeerRemotePort_Object = MibTableColumn
axBgpPeerRemotePort = _AxBgpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 9),
    _AxBgpPeerRemotePort_Type()
)
axBgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerRemotePort.setStatus("current")
_AxBgpPeerRemoteAs_Type = InetAutonomousSystemNumber
_AxBgpPeerRemoteAs_Object = MibTableColumn
axBgpPeerRemoteAs = _AxBgpPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 10),
    _AxBgpPeerRemoteAs_Type()
)
axBgpPeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerRemoteAs.setStatus("current")
_AxBgpPeerInUpdates_Type = Counter32
_AxBgpPeerInUpdates_Object = MibTableColumn
axBgpPeerInUpdates = _AxBgpPeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 11),
    _AxBgpPeerInUpdates_Type()
)
axBgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerInUpdates.setStatus("current")
_AxBgpPeerOutUpdates_Type = Counter32
_AxBgpPeerOutUpdates_Object = MibTableColumn
axBgpPeerOutUpdates = _AxBgpPeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 12),
    _AxBgpPeerOutUpdates_Type()
)
axBgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerOutUpdates.setStatus("current")
_AxBgpPeerInTotalMessages_Type = Counter32
_AxBgpPeerInTotalMessages_Object = MibTableColumn
axBgpPeerInTotalMessages = _AxBgpPeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 13),
    _AxBgpPeerInTotalMessages_Type()
)
axBgpPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerInTotalMessages.setStatus("current")
_AxBgpPeerOutTotalMessages_Type = Counter32
_AxBgpPeerOutTotalMessages_Object = MibTableColumn
axBgpPeerOutTotalMessages = _AxBgpPeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 14),
    _AxBgpPeerOutTotalMessages_Type()
)
axBgpPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerOutTotalMessages.setStatus("current")


class _AxBgpPeerLastError_Type(OctetString):
    """Custom type axBgpPeerLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AxBgpPeerLastError_Type.__name__ = "OctetString"
_AxBgpPeerLastError_Object = MibTableColumn
axBgpPeerLastError = _AxBgpPeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 15),
    _AxBgpPeerLastError_Type()
)
axBgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerLastError.setStatus("current")
_AxBgpPeerFsmEstablishedTransitions_Type = Counter32
_AxBgpPeerFsmEstablishedTransitions_Object = MibTableColumn
axBgpPeerFsmEstablishedTransitions = _AxBgpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 16),
    _AxBgpPeerFsmEstablishedTransitions_Type()
)
axBgpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerFsmEstablishedTransitions.setStatus("current")
_AxBgpPeerFsmEstablishedTime_Type = Gauge32
_AxBgpPeerFsmEstablishedTime_Object = MibTableColumn
axBgpPeerFsmEstablishedTime = _AxBgpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 17),
    _AxBgpPeerFsmEstablishedTime_Type()
)
axBgpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerFsmEstablishedTime.setStatus("current")
if mibBuilder.loadTexts:
    axBgpPeerFsmEstablishedTime.setUnits("seconds")


class _AxBgpPeerConnectRetryInterval_Type(Integer32):
    """Custom type axBgpPeerConnectRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AxBgpPeerConnectRetryInterval_Type.__name__ = "Integer32"
_AxBgpPeerConnectRetryInterval_Object = MibTableColumn
axBgpPeerConnectRetryInterval = _AxBgpPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 18),
    _AxBgpPeerConnectRetryInterval_Type()
)
axBgpPeerConnectRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    axBgpPeerConnectRetryInterval.setUnits("seconds")


class _AxBgpPeerHoldTime_Type(Integer32):
    """Custom type axBgpPeerHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_AxBgpPeerHoldTime_Type.__name__ = "Integer32"
_AxBgpPeerHoldTime_Object = MibTableColumn
axBgpPeerHoldTime = _AxBgpPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 19),
    _AxBgpPeerHoldTime_Type()
)
axBgpPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    axBgpPeerHoldTime.setUnits("seconds")


class _AxBgpPeerKeepAlive_Type(Integer32):
    """Custom type axBgpPeerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_AxBgpPeerKeepAlive_Type.__name__ = "Integer32"
_AxBgpPeerKeepAlive_Object = MibTableColumn
axBgpPeerKeepAlive = _AxBgpPeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 20),
    _AxBgpPeerKeepAlive_Type()
)
axBgpPeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    axBgpPeerKeepAlive.setUnits("seconds")


class _AxBgpPeerHoldTimeConfigured_Type(Integer32):
    """Custom type axBgpPeerHoldTimeConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_AxBgpPeerHoldTimeConfigured_Type.__name__ = "Integer32"
_AxBgpPeerHoldTimeConfigured_Object = MibTableColumn
axBgpPeerHoldTimeConfigured = _AxBgpPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 21),
    _AxBgpPeerHoldTimeConfigured_Type()
)
axBgpPeerHoldTimeConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerHoldTimeConfigured.setStatus("current")
if mibBuilder.loadTexts:
    axBgpPeerHoldTimeConfigured.setUnits("seconds")


class _AxBgpPeerKeepAliveConfigured_Type(Integer32):
    """Custom type axBgpPeerKeepAliveConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_AxBgpPeerKeepAliveConfigured_Type.__name__ = "Integer32"
_AxBgpPeerKeepAliveConfigured_Object = MibTableColumn
axBgpPeerKeepAliveConfigured = _AxBgpPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 22),
    _AxBgpPeerKeepAliveConfigured_Type()
)
axBgpPeerKeepAliveConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerKeepAliveConfigured.setStatus("current")
if mibBuilder.loadTexts:
    axBgpPeerKeepAliveConfigured.setUnits("seconds")


class _AxBgpPeerMinASOriginationInterval_Type(Integer32):
    """Custom type axBgpPeerMinASOriginationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AxBgpPeerMinASOriginationInterval_Type.__name__ = "Integer32"
_AxBgpPeerMinASOriginationInterval_Object = MibTableColumn
axBgpPeerMinASOriginationInterval = _AxBgpPeerMinASOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 23),
    _AxBgpPeerMinASOriginationInterval_Type()
)
axBgpPeerMinASOriginationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerMinASOriginationInterval.setStatus("current")
if mibBuilder.loadTexts:
    axBgpPeerMinASOriginationInterval.setUnits("seconds")


class _AxBgpPeerMinRouteAdvertisementInterval_Type(Integer32):
    """Custom type axBgpPeerMinRouteAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AxBgpPeerMinRouteAdvertisementInterval_Type.__name__ = "Integer32"
_AxBgpPeerMinRouteAdvertisementInterval_Object = MibTableColumn
axBgpPeerMinRouteAdvertisementInterval = _AxBgpPeerMinRouteAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 24),
    _AxBgpPeerMinRouteAdvertisementInterval_Type()
)
axBgpPeerMinRouteAdvertisementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerMinRouteAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    axBgpPeerMinRouteAdvertisementInterval.setUnits("seconds")
_AxBgpPeerInUpdateElapsedTime_Type = Gauge32
_AxBgpPeerInUpdateElapsedTime_Object = MibTableColumn
axBgpPeerInUpdateElapsedTime = _AxBgpPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 25),
    _AxBgpPeerInUpdateElapsedTime_Type()
)
axBgpPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerInUpdateElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    axBgpPeerInUpdateElapsedTime.setUnits("seconds")
_AxBgpPeerMaxPrefixLimit_Type = Gauge32
_AxBgpPeerMaxPrefixLimit_Object = MibTableColumn
axBgpPeerMaxPrefixLimit = _AxBgpPeerMaxPrefixLimit_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 26),
    _AxBgpPeerMaxPrefixLimit_Type()
)
axBgpPeerMaxPrefixLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerMaxPrefixLimit.setStatus("current")


class _AxBgpPeerThreshold_Type(Integer32):
    """Custom type axBgpPeerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AxBgpPeerThreshold_Type.__name__ = "Integer32"
_AxBgpPeerThreshold_Object = MibTableColumn
axBgpPeerThreshold = _AxBgpPeerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 4, 1, 27),
    _AxBgpPeerThreshold_Type()
)
axBgpPeerThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPeerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    axBgpPeerThreshold.setUnits("percent")
_AxBgpPathAttrTable_Object = MibTable
axBgpPathAttrTable = _AxBgpPathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5)
)
if mibBuilder.loadTexts:
    axBgpPathAttrTable.setStatus("current")
_AxBgpPathAttrEntry_Object = MibTableRow
axBgpPathAttrEntry = _AxBgpPathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1)
)
axBgpPathAttrEntry.setIndexNames(
    (0, "AX-BGP-MIB", "axBgpPathAttrIpAddrType"),
    (0, "AX-BGP-MIB", "axBgpPathAttrIpAddrPrefix"),
    (0, "AX-BGP-MIB", "axBgpPathAttrIpAddrPrefixLen"),
    (0, "AX-BGP-MIB", "axBgpPathAttrPeerType"),
    (0, "AX-BGP-MIB", "axBgpPathAttrPeer"),
)
if mibBuilder.loadTexts:
    axBgpPathAttrEntry.setStatus("current")
_AxBgpPathAttrIpAddrType_Type = InetAddressType
_AxBgpPathAttrIpAddrType_Object = MibTableColumn
axBgpPathAttrIpAddrType = _AxBgpPathAttrIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 1),
    _AxBgpPathAttrIpAddrType_Type()
)
axBgpPathAttrIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axBgpPathAttrIpAddrType.setStatus("current")
_AxBgpPathAttrPeerType_Type = InetAddress
_AxBgpPathAttrPeerType_Object = MibTableColumn
axBgpPathAttrPeerType = _AxBgpPathAttrPeerType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 2),
    _AxBgpPathAttrPeerType_Type()
)
axBgpPathAttrPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axBgpPathAttrPeerType.setStatus("current")
_AxBgpPathAttrPeer_Type = InetAddress
_AxBgpPathAttrPeer_Object = MibTableColumn
axBgpPathAttrPeer = _AxBgpPathAttrPeer_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 3),
    _AxBgpPathAttrPeer_Type()
)
axBgpPathAttrPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrPeer.setStatus("current")
_AxBgpPathAttrIpAddrPrefixLen_Type = InetAddressPrefixLength
_AxBgpPathAttrIpAddrPrefixLen_Object = MibTableColumn
axBgpPathAttrIpAddrPrefixLen = _AxBgpPathAttrIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 4),
    _AxBgpPathAttrIpAddrPrefixLen_Type()
)
axBgpPathAttrIpAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrIpAddrPrefixLen.setStatus("current")
_AxBgpPathAttrIpAddrPrefix_Type = InetAddress
_AxBgpPathAttrIpAddrPrefix_Object = MibTableColumn
axBgpPathAttrIpAddrPrefix = _AxBgpPathAttrIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 5),
    _AxBgpPathAttrIpAddrPrefix_Type()
)
axBgpPathAttrIpAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrIpAddrPrefix.setStatus("current")


class _AxBgpPathAttrOrigin_Type(Integer32):
    """Custom type axBgpPathAttrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igp", 1),
          ("egp", 2),
          ("incomplete", 3))
    )


_AxBgpPathAttrOrigin_Type.__name__ = "Integer32"
_AxBgpPathAttrOrigin_Object = MibTableColumn
axBgpPathAttrOrigin = _AxBgpPathAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 6),
    _AxBgpPathAttrOrigin_Type()
)
axBgpPathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrOrigin.setStatus("current")


class _AxBgpPathAttrASPathSegment_Type(OctetString):
    """Custom type axBgpPathAttrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_AxBgpPathAttrASPathSegment_Type.__name__ = "OctetString"
_AxBgpPathAttrASPathSegment_Object = MibTableColumn
axBgpPathAttrASPathSegment = _AxBgpPathAttrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 7),
    _AxBgpPathAttrASPathSegment_Type()
)
axBgpPathAttrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrASPathSegment.setStatus("current")
_AxBgpPathAttrNextHopType_Type = InetAddressType
_AxBgpPathAttrNextHopType_Object = MibTableColumn
axBgpPathAttrNextHopType = _AxBgpPathAttrNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 8),
    _AxBgpPathAttrNextHopType_Type()
)
axBgpPathAttrNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrNextHopType.setStatus("current")
_AxBgpPathAttrNextHop_Type = InetAddress
_AxBgpPathAttrNextHop_Object = MibTableColumn
axBgpPathAttrNextHop = _AxBgpPathAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 9),
    _AxBgpPathAttrNextHop_Type()
)
axBgpPathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrNextHop.setStatus("current")


class _AxBgpPathAttrMultiExitDisc_Type(Integer32):
    """Custom type axBgpPathAttrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AxBgpPathAttrMultiExitDisc_Type.__name__ = "Integer32"
_AxBgpPathAttrMultiExitDisc_Object = MibTableColumn
axBgpPathAttrMultiExitDisc = _AxBgpPathAttrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 10),
    _AxBgpPathAttrMultiExitDisc_Type()
)
axBgpPathAttrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrMultiExitDisc.setStatus("current")


class _AxBgpPathAttrLocalPref_Type(Integer32):
    """Custom type axBgpPathAttrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AxBgpPathAttrLocalPref_Type.__name__ = "Integer32"
_AxBgpPathAttrLocalPref_Object = MibTableColumn
axBgpPathAttrLocalPref = _AxBgpPathAttrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 11),
    _AxBgpPathAttrLocalPref_Type()
)
axBgpPathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrLocalPref.setStatus("current")


class _AxBgpPathAttrAtomicAggregate_Type(Integer32):
    """Custom type axBgpPathAttrAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRouteNotSelected", 1),
          ("lessSpecificRouteSelected", 2))
    )


_AxBgpPathAttrAtomicAggregate_Type.__name__ = "Integer32"
_AxBgpPathAttrAtomicAggregate_Object = MibTableColumn
axBgpPathAttrAtomicAggregate = _AxBgpPathAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 12),
    _AxBgpPathAttrAtomicAggregate_Type()
)
axBgpPathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrAtomicAggregate.setStatus("current")


class _AxBgpPathAttrAggregatorAS_Type(Integer32):
    """Custom type axBgpPathAttrAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AxBgpPathAttrAggregatorAS_Type.__name__ = "Integer32"
_AxBgpPathAttrAggregatorAS_Object = MibTableColumn
axBgpPathAttrAggregatorAS = _AxBgpPathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 13),
    _AxBgpPathAttrAggregatorAS_Type()
)
axBgpPathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrAggregatorAS.setStatus("current")
_AxBgpPathAttrAggregatorAddr_Type = IpAddress
_AxBgpPathAttrAggregatorAddr_Object = MibTableColumn
axBgpPathAttrAggregatorAddr = _AxBgpPathAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 14),
    _AxBgpPathAttrAggregatorAddr_Type()
)
axBgpPathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrAggregatorAddr.setStatus("current")


class _AxBgpPathAttrCalcLocalPref_Type(Integer32):
    """Custom type axBgpPathAttrCalcLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AxBgpPathAttrCalcLocalPref_Type.__name__ = "Integer32"
_AxBgpPathAttrCalcLocalPref_Object = MibTableColumn
axBgpPathAttrCalcLocalPref = _AxBgpPathAttrCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 15),
    _AxBgpPathAttrCalcLocalPref_Type()
)
axBgpPathAttrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrCalcLocalPref.setStatus("current")


class _AxBgpPathAttrBest_Type(Integer32):
    """Custom type axBgpPathAttrBest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AxBgpPathAttrBest_Type.__name__ = "Integer32"
_AxBgpPathAttrBest_Object = MibTableColumn
axBgpPathAttrBest = _AxBgpPathAttrBest_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 16),
    _AxBgpPathAttrBest_Type()
)
axBgpPathAttrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrBest.setStatus("current")


class _AxBgpPathAttrUnknown_Type(OctetString):
    """Custom type axBgpPathAttrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AxBgpPathAttrUnknown_Type.__name__ = "OctetString"
_AxBgpPathAttrUnknown_Object = MibTableColumn
axBgpPathAttrUnknown = _AxBgpPathAttrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 5, 1, 17),
    _AxBgpPathAttrUnknown_Type()
)
axBgpPathAttrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBgpPathAttrUnknown.setStatus("current")
_AxBgpMIBConformance_ObjectIdentity = ObjectIdentity
axBgpMIBConformance = _AxBgpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 8)
)
_AxBgpMIBCompliances_ObjectIdentity = ObjectIdentity
axBgpMIBCompliances = _AxBgpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 8, 1)
)
_AxBgpMIBGroups_ObjectIdentity = ObjectIdentity
axBgpMIBGroups = _AxBgpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 8, 2)
)

# Managed Objects groups

axBgpMIBGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 8, 2, 1)
)
axBgpMIBGlobalsGroup.setObjects(
      *(("AX-BGP-MIB", "axBgpVersion"),
        ("AX-BGP-MIB", "axBgpLocalAs"),
        ("AX-BGP-MIB", "axBgpIdentifier"))
)
if mibBuilder.loadTexts:
    axBgpMIBGlobalsGroup.setStatus("current")

axBgpMIBPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 8, 2, 2)
)
axBgpMIBPeerGroup.setObjects(
      *(("AX-BGP-MIB", "axBgpPeerType"),
        ("AX-BGP-MIB", "axBgpPeerIdentifier"),
        ("AX-BGP-MIB", "axBgpPeerState"),
        ("AX-BGP-MIB", "axBgpPeerAdminStatus"),
        ("AX-BGP-MIB", "axBgpPeerNegotiatedVersion"),
        ("AX-BGP-MIB", "axBgpPeerLocalAddr"),
        ("AX-BGP-MIB", "axBgpPeerLocalPort"),
        ("AX-BGP-MIB", "axBgpPeerRemoteAddr"),
        ("AX-BGP-MIB", "axBgpPeerRemotePort"),
        ("AX-BGP-MIB", "axBgpPeerRemoteAs"),
        ("AX-BGP-MIB", "axBgpPeerInUpdates"),
        ("AX-BGP-MIB", "axBgpPeerOutUpdates"),
        ("AX-BGP-MIB", "axBgpPeerInTotalMessages"),
        ("AX-BGP-MIB", "axBgpPeerOutTotalMessages"),
        ("AX-BGP-MIB", "axBgpPeerLastError"),
        ("AX-BGP-MIB", "axBgpPeerFsmEstablishedTransitions"),
        ("AX-BGP-MIB", "axBgpPeerFsmEstablishedTime"),
        ("AX-BGP-MIB", "axBgpPeerConnectRetryInterval"),
        ("AX-BGP-MIB", "axBgpPeerHoldTime"),
        ("AX-BGP-MIB", "axBgpPeerKeepAlive"),
        ("AX-BGP-MIB", "axBgpPeerHoldTimeConfigured"),
        ("AX-BGP-MIB", "axBgpPeerKeepAliveConfigured"),
        ("AX-BGP-MIB", "axBgpPeerMinASOriginationInterval"),
        ("AX-BGP-MIB", "axBgpPeerMinRouteAdvertisementInterval"),
        ("AX-BGP-MIB", "axBgpPeerInUpdateElapsedTime"),
        ("AX-BGP-MIB", "axBgpPeerMaxPrefixLimit"),
        ("AX-BGP-MIB", "axBgpPeerThreshold"))
)
if mibBuilder.loadTexts:
    axBgpMIBPeerGroup.setStatus("current")

axBgpMIBPathAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 8, 2, 3)
)
axBgpMIBPathAttrGroup.setObjects(
      *(("AX-BGP-MIB", "axBgpPathAttrIpAddrType"),
        ("AX-BGP-MIB", "axBgpPathAttrPeerType"),
        ("AX-BGP-MIB", "axBgpPathAttrPeer"),
        ("AX-BGP-MIB", "axBgpPathAttrIpAddrPrefixLen"),
        ("AX-BGP-MIB", "axBgpPathAttrIpAddrPrefix"),
        ("AX-BGP-MIB", "axBgpPathAttrOrigin"),
        ("AX-BGP-MIB", "axBgpPathAttrASPathSegment"),
        ("AX-BGP-MIB", "axBgpPathAttrNextHopType"),
        ("AX-BGP-MIB", "axBgpPathAttrNextHop"),
        ("AX-BGP-MIB", "axBgpPathAttrMultiExitDisc"),
        ("AX-BGP-MIB", "axBgpPathAttrLocalPref"),
        ("AX-BGP-MIB", "axBgpPathAttrAtomicAggregate"),
        ("AX-BGP-MIB", "axBgpPathAttrAggregatorAS"),
        ("AX-BGP-MIB", "axBgpPathAttrAggregatorAddr"),
        ("AX-BGP-MIB", "axBgpPathAttrCalcLocalPref"),
        ("AX-BGP-MIB", "axBgpPathAttrBest"),
        ("AX-BGP-MIB", "axBgpPathAttrUnknown"))
)
if mibBuilder.loadTexts:
    axBgpMIBPathAttrGroup.setStatus("current")


# Notification objects

axBgpEstablishedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 0, 1)
)
axBgpEstablishedNotification.setObjects(
      *(("AX-BGP-MIB", "axBgpPeerRemoteAddr"),
        ("AX-BGP-MIB", "axBgpPeerLastError"),
        ("AX-BGP-MIB", "axBgpPeerState"))
)
if mibBuilder.loadTexts:
    axBgpEstablishedNotification.setStatus(
        "current"
    )

axBgpBackwardTransNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 0, 2)
)
axBgpBackwardTransNotification.setObjects(
      *(("AX-BGP-MIB", "axBgpPeerRemoteAddr"),
        ("AX-BGP-MIB", "axBgpPeerLastError"),
        ("AX-BGP-MIB", "axBgpPeerState"))
)
if mibBuilder.loadTexts:
    axBgpBackwardTransNotification.setStatus(
        "current"
    )

axBgpPrefixThresholdExceededNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 0, 3)
)
axBgpPrefixThresholdExceededNotification.setObjects(
      *(("AX-BGP-MIB", "axBgpPeerRemoteAddr"),
        ("AX-BGP-MIB", "axBgpPeerMaxPrefixLimit"),
        ("AX-BGP-MIB", "axBgpPeerThreshold"))
)
if mibBuilder.loadTexts:
    axBgpPrefixThresholdExceededNotification.setStatus(
        "current"
    )

axBgpPrefixThresholdClearNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 0, 4)
)
axBgpPrefixThresholdClearNotification.setObjects(
      *(("AX-BGP-MIB", "axBgpPeerRemoteAddr"),
        ("AX-BGP-MIB", "axBgpPeerMaxPrefixLimit"),
        ("AX-BGP-MIB", "axBgpPeerThreshold"))
)
if mibBuilder.loadTexts:
    axBgpPrefixThresholdClearNotification.setStatus(
        "current"
    )


# Notifications groups

axBgpMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 8, 2, 4)
)
axBgpMIBNotificationGroup.setObjects(
      *(("AX-BGP-MIB", "axBgpEstablishedNotification"),
        ("AX-BGP-MIB", "axBgpBackwardTransNotification"),
        ("AX-BGP-MIB", "axBgpPrefixThresholdExceededNotification"),
        ("AX-BGP-MIB", "axBgpPrefixThresholdClearNotification"))
)
if mibBuilder.loadTexts:
    axBgpMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axBgpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22610, 2, 5, 8, 1, 1)
)
axBgpMIBCompliance.setObjects(
      *(("AX-BGP-MIB", "axBgpMIBGlobalsGroup"),
        ("AX-BGP-MIB", "axBgpMIBPeerGroup"),
        ("AX-BGP-MIB", "axBgpMIBPathAttrGroup"),
        ("AX-BGP-MIB", "axBgpMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    axBgpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-BGP-MIB",
    **{"axBgpMIB": axBgpMIB,
       "axBgpNotification": axBgpNotification,
       "axBgpEstablishedNotification": axBgpEstablishedNotification,
       "axBgpBackwardTransNotification": axBgpBackwardTransNotification,
       "axBgpPrefixThresholdExceededNotification": axBgpPrefixThresholdExceededNotification,
       "axBgpPrefixThresholdClearNotification": axBgpPrefixThresholdClearNotification,
       "axBgpVersion": axBgpVersion,
       "axBgpLocalAs": axBgpLocalAs,
       "axBgpIdentifier": axBgpIdentifier,
       "axBgpPeerTable": axBgpPeerTable,
       "axBgpPeerEntry": axBgpPeerEntry,
       "axBgpPeerType": axBgpPeerType,
       "axBgpPeerIdentifier": axBgpPeerIdentifier,
       "axBgpPeerState": axBgpPeerState,
       "axBgpPeerAdminStatus": axBgpPeerAdminStatus,
       "axBgpPeerNegotiatedVersion": axBgpPeerNegotiatedVersion,
       "axBgpPeerLocalAddr": axBgpPeerLocalAddr,
       "axBgpPeerLocalPort": axBgpPeerLocalPort,
       "axBgpPeerRemoteAddr": axBgpPeerRemoteAddr,
       "axBgpPeerRemotePort": axBgpPeerRemotePort,
       "axBgpPeerRemoteAs": axBgpPeerRemoteAs,
       "axBgpPeerInUpdates": axBgpPeerInUpdates,
       "axBgpPeerOutUpdates": axBgpPeerOutUpdates,
       "axBgpPeerInTotalMessages": axBgpPeerInTotalMessages,
       "axBgpPeerOutTotalMessages": axBgpPeerOutTotalMessages,
       "axBgpPeerLastError": axBgpPeerLastError,
       "axBgpPeerFsmEstablishedTransitions": axBgpPeerFsmEstablishedTransitions,
       "axBgpPeerFsmEstablishedTime": axBgpPeerFsmEstablishedTime,
       "axBgpPeerConnectRetryInterval": axBgpPeerConnectRetryInterval,
       "axBgpPeerHoldTime": axBgpPeerHoldTime,
       "axBgpPeerKeepAlive": axBgpPeerKeepAlive,
       "axBgpPeerHoldTimeConfigured": axBgpPeerHoldTimeConfigured,
       "axBgpPeerKeepAliveConfigured": axBgpPeerKeepAliveConfigured,
       "axBgpPeerMinASOriginationInterval": axBgpPeerMinASOriginationInterval,
       "axBgpPeerMinRouteAdvertisementInterval": axBgpPeerMinRouteAdvertisementInterval,
       "axBgpPeerInUpdateElapsedTime": axBgpPeerInUpdateElapsedTime,
       "axBgpPeerMaxPrefixLimit": axBgpPeerMaxPrefixLimit,
       "axBgpPeerThreshold": axBgpPeerThreshold,
       "axBgpPathAttrTable": axBgpPathAttrTable,
       "axBgpPathAttrEntry": axBgpPathAttrEntry,
       "axBgpPathAttrIpAddrType": axBgpPathAttrIpAddrType,
       "axBgpPathAttrPeerType": axBgpPathAttrPeerType,
       "axBgpPathAttrPeer": axBgpPathAttrPeer,
       "axBgpPathAttrIpAddrPrefixLen": axBgpPathAttrIpAddrPrefixLen,
       "axBgpPathAttrIpAddrPrefix": axBgpPathAttrIpAddrPrefix,
       "axBgpPathAttrOrigin": axBgpPathAttrOrigin,
       "axBgpPathAttrASPathSegment": axBgpPathAttrASPathSegment,
       "axBgpPathAttrNextHopType": axBgpPathAttrNextHopType,
       "axBgpPathAttrNextHop": axBgpPathAttrNextHop,
       "axBgpPathAttrMultiExitDisc": axBgpPathAttrMultiExitDisc,
       "axBgpPathAttrLocalPref": axBgpPathAttrLocalPref,
       "axBgpPathAttrAtomicAggregate": axBgpPathAttrAtomicAggregate,
       "axBgpPathAttrAggregatorAS": axBgpPathAttrAggregatorAS,
       "axBgpPathAttrAggregatorAddr": axBgpPathAttrAggregatorAddr,
       "axBgpPathAttrCalcLocalPref": axBgpPathAttrCalcLocalPref,
       "axBgpPathAttrBest": axBgpPathAttrBest,
       "axBgpPathAttrUnknown": axBgpPathAttrUnknown,
       "axBgpMIBConformance": axBgpMIBConformance,
       "axBgpMIBCompliances": axBgpMIBCompliances,
       "axBgpMIBCompliance": axBgpMIBCompliance,
       "axBgpMIBGroups": axBgpMIBGroups,
       "axBgpMIBGlobalsGroup": axBgpMIBGlobalsGroup,
       "axBgpMIBPeerGroup": axBgpMIBPeerGroup,
       "axBgpMIBPathAttrGroup": axBgpMIBPathAttrGroup,
       "axBgpMIBNotificationGroup": axBgpMIBNotificationGroup}
)
