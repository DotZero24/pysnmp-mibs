# SNMP MIB module (MX-NCS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-NCS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:44 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ipAddressConfig,
 ipAddressStatus,
 mediatrixIpTelephonySignaling) = mibBuilder.importSymbols(
    "MX-SMI",
    "ipAddressConfig",
    "ipAddressStatus",
    "mediatrixIpTelephonySignaling")

(MxIpConfigSource,
 MxIpDhcpSiteSpecificCode,
 MxIpHostName,
 MxIpPort,
 MxIpSelectConfigSource) = mibBuilder.importSymbols(
    "MX-TC",
    "MxIpConfigSource",
    "MxIpDhcpSiteSpecificCode",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSelectConfigSource")

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


# MODULE-IDENTITY

ncsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1)
)
if mibBuilder.loadTexts:
    ncsMIB.setRevisions(
        ("1902-11-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressStatusNcsCallAgent_ObjectIdentity = ObjectIdentity
ipAddressStatusNcsCallAgent = _IpAddressStatusNcsCallAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 60)
)


class _NcsCAConfigSource_Type(MxIpConfigSource):
    """Custom type ncsCAConfigSource based on MxIpConfigSource"""
    defaultValue = 1


_NcsCAConfigSource_Type.__name__ = "MxIpConfigSource"
_NcsCAConfigSource_Object = MibScalar
ncsCAConfigSource = _NcsCAConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 60, 1),
    _NcsCAConfigSource_Type()
)
ncsCAConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncsCAConfigSource.setStatus("current")


class _NcsCAHost_Type(MxIpHostName):
    """Custom type ncsCAHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_NcsCAHost_Type.__name__ = "MxIpHostName"
_NcsCAHost_Object = MibScalar
ncsCAHost = _NcsCAHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 60, 2),
    _NcsCAHost_Type()
)
ncsCAHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncsCAHost.setStatus("current")


class _NcsCAPort_Type(MxIpPort):
    """Custom type ncsCAPort based on MxIpPort"""
    defaultValue = 2727


_NcsCAPort_Type.__name__ = "MxIpPort"
_NcsCAPort_Object = MibScalar
ncsCAPort = _NcsCAPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 60, 3),
    _NcsCAPort_Type()
)
ncsCAPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncsCAPort.setStatus("current")
_IpAddressConfigNcsCallAgent_ObjectIdentity = ObjectIdentity
ipAddressConfigNcsCallAgent = _IpAddressConfigNcsCallAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 60)
)


class _NcsCASelectConfigSource_Type(MxIpSelectConfigSource):
    """Custom type ncsCASelectConfigSource based on MxIpSelectConfigSource"""
    defaultValue = 1


_NcsCASelectConfigSource_Type.__name__ = "MxIpSelectConfigSource"
_NcsCASelectConfigSource_Object = MibScalar
ncsCASelectConfigSource = _NcsCASelectConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 60, 1),
    _NcsCASelectConfigSource_Type()
)
ncsCASelectConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsCASelectConfigSource.setStatus("current")
_IpAddressConfigNcsCAStatic_ObjectIdentity = ObjectIdentity
ipAddressConfigNcsCAStatic = _IpAddressConfigNcsCAStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 60, 6)
)


class _NcsCAStaticHost_Type(MxIpHostName):
    """Custom type ncsCAStaticHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_NcsCAStaticHost_Type.__name__ = "MxIpHostName"
_NcsCAStaticHost_Object = MibScalar
ncsCAStaticHost = _NcsCAStaticHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 60, 6, 1),
    _NcsCAStaticHost_Type()
)
ncsCAStaticHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsCAStaticHost.setStatus("current")


class _NcsCAStaticPort_Type(MxIpPort):
    """Custom type ncsCAStaticPort based on MxIpPort"""
    defaultValue = 2727


_NcsCAStaticPort_Type.__name__ = "MxIpPort"
_NcsCAStaticPort_Object = MibScalar
ncsCAStaticPort = _NcsCAStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 60, 6, 2),
    _NcsCAStaticPort_Type()
)
ncsCAStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsCAStaticPort.setStatus("current")
_IpAddressConfigNcsCADhcp_ObjectIdentity = ObjectIdentity
ipAddressConfigNcsCADhcp = _IpAddressConfigNcsCADhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 60, 7)
)


class _NcsCADhcpSiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):
    """Custom type ncsCADhcpSiteSpecificCode based on MxIpDhcpSiteSpecificCode"""
    defaultValue = 0


_NcsCADhcpSiteSpecificCode_Type.__name__ = "MxIpDhcpSiteSpecificCode"
_NcsCADhcpSiteSpecificCode_Object = MibScalar
ncsCADhcpSiteSpecificCode = _NcsCADhcpSiteSpecificCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 60, 7, 1),
    _NcsCADhcpSiteSpecificCode_Type()
)
ncsCADhcpSiteSpecificCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsCADhcpSiteSpecificCode.setStatus("current")
_Ncs_ObjectIdentity = ObjectIdentity
ncs = _Ncs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10)
)
if mibBuilder.loadTexts:
    ncs.setStatus("current")
_NcsMIBObjects_ObjectIdentity = ObjectIdentity
ncsMIBObjects = _NcsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1)
)


class _NcsPort_Type(MxIpPort):
    """Custom type ncsPort based on MxIpPort"""
    defaultValue = 2427


_NcsPort_Type.__name__ = "MxIpPort"
_NcsPort_Object = MibScalar
ncsPort = _NcsPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 1),
    _NcsPort_Type()
)
ncsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsPort.setStatus("current")


class _NcsDefaultDigitMap_Type(OctetString):
    """Custom type ncsDefaultDigitMap based on OctetString"""
    defaultValue = OctetString("x.T")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NcsDefaultDigitMap_Type.__name__ = "OctetString"
_NcsDefaultDigitMap_Object = MibScalar
ncsDefaultDigitMap = _NcsDefaultDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 2),
    _NcsDefaultDigitMap_Type()
)
ncsDefaultDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsDefaultDigitMap.setStatus("current")


class _NcsRestartLevel_Type(Integer32):
    """Custom type ncsRestartLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gateway", 0),
          ("group", 1),
          ("endpoint", 2))
    )


_NcsRestartLevel_Type.__name__ = "Integer32"
_NcsRestartLevel_Object = MibScalar
ncsRestartLevel = _NcsRestartLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 4),
    _NcsRestartLevel_Type()
)
ncsRestartLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRestartLevel.setStatus("current")


class _NcsEndpointIdListIncludeNotStarted_Type(Integer32):
    """Custom type ncsEndpointIdListIncludeNotStarted based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("excludeNotStarted", 0),
          ("includeNotStarted", 1))
    )


_NcsEndpointIdListIncludeNotStarted_Type.__name__ = "Integer32"
_NcsEndpointIdListIncludeNotStarted_Object = MibScalar
ncsEndpointIdListIncludeNotStarted = _NcsEndpointIdListIncludeNotStarted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 5),
    _NcsEndpointIdListIncludeNotStarted_Type()
)
ncsEndpointIdListIncludeNotStarted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsEndpointIdListIncludeNotStarted.setStatus("current")


class _NcsPiggyBackingEnable_Type(Integer32):
    """Custom type ncsPiggyBackingEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NcsPiggyBackingEnable_Type.__name__ = "Integer32"
_NcsPiggyBackingEnable_Object = MibScalar
ncsPiggyBackingEnable = _NcsPiggyBackingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 6),
    _NcsPiggyBackingEnable_Type()
)
ncsPiggyBackingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsPiggyBackingEnable.setStatus("current")
_NcsEndpointId_ObjectIdentity = ObjectIdentity
ncsEndpointId = _NcsEndpointId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 20)
)
_NcsEndpointIfTable_Object = MibTable
ncsEndpointIfTable = _NcsEndpointIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 20, 10)
)
if mibBuilder.loadTexts:
    ncsEndpointIfTable.setStatus("current")
_NcsEndpointIfEntry_Object = MibTableRow
ncsEndpointIfEntry = _NcsEndpointIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 20, 10, 1)
)
ncsEndpointIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ncsEndpointIfEntry.setStatus("current")


class _NcsEndpointIdTerm1_Type(OctetString):
    """Custom type ncsEndpointIdTerm1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NcsEndpointIdTerm1_Type.__name__ = "OctetString"
_NcsEndpointIdTerm1_Object = MibTableColumn
ncsEndpointIdTerm1 = _NcsEndpointIdTerm1_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 20, 10, 1, 1),
    _NcsEndpointIdTerm1_Type()
)
ncsEndpointIdTerm1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsEndpointIdTerm1.setStatus("current")


class _NcsEndpointIdTerm2_Type(OctetString):
    """Custom type ncsEndpointIdTerm2 based on OctetString"""
    defaultValue = OctetString("aaln")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NcsEndpointIdTerm2_Type.__name__ = "OctetString"
_NcsEndpointIdTerm2_Object = MibTableColumn
ncsEndpointIdTerm2 = _NcsEndpointIdTerm2_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 20, 10, 1, 2),
    _NcsEndpointIdTerm2_Type()
)
ncsEndpointIdTerm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsEndpointIdTerm2.setStatus("current")
_NcsRetransmission_ObjectIdentity = ObjectIdentity
ncsRetransmission = _NcsRetransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23)
)


class _NcsRetransmissionAlgorithm_Type(Integer32):
    """Custom type ncsRetransmissionAlgorithm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("exponential", 1),
          ("exponentialWithJitter", 2))
    )


_NcsRetransmissionAlgorithm_Type.__name__ = "Integer32"
_NcsRetransmissionAlgorithm_Object = MibScalar
ncsRetransmissionAlgorithm = _NcsRetransmissionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 1),
    _NcsRetransmissionAlgorithm_Type()
)
ncsRetransmissionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionAlgorithm.setStatus("current")


class _NcsRetransmissionInitialPeriod_Type(Unsigned32):
    """Custom type ncsRetransmissionInitialPeriod based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4294967295),
    )


_NcsRetransmissionInitialPeriod_Type.__name__ = "Unsigned32"
_NcsRetransmissionInitialPeriod_Object = MibScalar
ncsRetransmissionInitialPeriod = _NcsRetransmissionInitialPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 2),
    _NcsRetransmissionInitialPeriod_Type()
)
ncsRetransmissionInitialPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionInitialPeriod.setStatus("current")


class _NcsRetransmissionMaxPeriod_Type(Unsigned32):
    """Custom type ncsRetransmissionMaxPeriod based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4294967295),
    )


_NcsRetransmissionMaxPeriod_Type.__name__ = "Unsigned32"
_NcsRetransmissionMaxPeriod_Object = MibScalar
ncsRetransmissionMaxPeriod = _NcsRetransmissionMaxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 3),
    _NcsRetransmissionMaxPeriod_Type()
)
ncsRetransmissionMaxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionMaxPeriod.setStatus("current")


class _NcsRetransmissionDisconnectTimeout_Type(Unsigned32):
    """Custom type ncsRetransmissionDisconnectTimeout based on Unsigned32"""
    defaultValue = 20000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_NcsRetransmissionDisconnectTimeout_Type.__name__ = "Unsigned32"
_NcsRetransmissionDisconnectTimeout_Object = MibScalar
ncsRetransmissionDisconnectTimeout = _NcsRetransmissionDisconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 4),
    _NcsRetransmissionDisconnectTimeout_Type()
)
ncsRetransmissionDisconnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionDisconnectTimeout.setStatus("current")


class _NcsRetransmissionSuspicionThreshold_Type(Unsigned32):
    """Custom type ncsRetransmissionSuspicionThreshold based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NcsRetransmissionSuspicionThreshold_Type.__name__ = "Unsigned32"
_NcsRetransmissionSuspicionThreshold_Object = MibScalar
ncsRetransmissionSuspicionThreshold = _NcsRetransmissionSuspicionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 5),
    _NcsRetransmissionSuspicionThreshold_Type()
)
ncsRetransmissionSuspicionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionSuspicionThreshold.setStatus("current")


class _NcsRetransmissionSuspicionThresholdDnsQuery_Type(Integer32):
    """Custom type ncsRetransmissionSuspicionThresholdDnsQuery based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noDnsQuery", 0),
          ("performDnsQuery", 1))
    )


_NcsRetransmissionSuspicionThresholdDnsQuery_Type.__name__ = "Integer32"
_NcsRetransmissionSuspicionThresholdDnsQuery_Object = MibScalar
ncsRetransmissionSuspicionThresholdDnsQuery = _NcsRetransmissionSuspicionThresholdDnsQuery_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 6),
    _NcsRetransmissionSuspicionThresholdDnsQuery_Type()
)
ncsRetransmissionSuspicionThresholdDnsQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionSuspicionThresholdDnsQuery.setStatus("current")


class _NcsRetransmissionDisconnectThreshold_Type(Unsigned32):
    """Custom type ncsRetransmissionDisconnectThreshold based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NcsRetransmissionDisconnectThreshold_Type.__name__ = "Unsigned32"
_NcsRetransmissionDisconnectThreshold_Object = MibScalar
ncsRetransmissionDisconnectThreshold = _NcsRetransmissionDisconnectThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 7),
    _NcsRetransmissionDisconnectThreshold_Type()
)
ncsRetransmissionDisconnectThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionDisconnectThreshold.setStatus("current")


class _NcsRetransmissionDisconnectThresholdDnsQuery_Type(Integer32):
    """Custom type ncsRetransmissionDisconnectThresholdDnsQuery based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noDnsQuery", 0),
          ("performDnsQuery", 1))
    )


_NcsRetransmissionDisconnectThresholdDnsQuery_Type.__name__ = "Integer32"
_NcsRetransmissionDisconnectThresholdDnsQuery_Object = MibScalar
ncsRetransmissionDisconnectThresholdDnsQuery = _NcsRetransmissionDisconnectThresholdDnsQuery_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 8),
    _NcsRetransmissionDisconnectThresholdDnsQuery_Type()
)
ncsRetransmissionDisconnectThresholdDnsQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionDisconnectThresholdDnsQuery.setStatus("current")


class _NcsRetransmissionHistoryTimeout_Type(Unsigned32):
    """Custom type ncsRetransmissionHistoryTimeout based on Unsigned32"""
    defaultValue = 20000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_NcsRetransmissionHistoryTimeout_Type.__name__ = "Unsigned32"
_NcsRetransmissionHistoryTimeout_Object = MibScalar
ncsRetransmissionHistoryTimeout = _NcsRetransmissionHistoryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 9),
    _NcsRetransmissionHistoryTimeout_Type()
)
ncsRetransmissionHistoryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionHistoryTimeout.setStatus("current")


class _NcsRetransmissionMaxWaitingDelay_Type(Unsigned32):
    """Custom type ncsRetransmissionMaxWaitingDelay based on Unsigned32"""
    defaultValue = 600000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_NcsRetransmissionMaxWaitingDelay_Type.__name__ = "Unsigned32"
_NcsRetransmissionMaxWaitingDelay_Object = MibScalar
ncsRetransmissionMaxWaitingDelay = _NcsRetransmissionMaxWaitingDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 10),
    _NcsRetransmissionMaxWaitingDelay_Type()
)
ncsRetransmissionMaxWaitingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionMaxWaitingDelay.setStatus("current")


class _NcsRetransmissionDisconnectInitialWaitingPeriod_Type(Unsigned32):
    """Custom type ncsRetransmissionDisconnectInitialWaitingPeriod based on Unsigned32"""
    defaultValue = 15000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_NcsRetransmissionDisconnectInitialWaitingPeriod_Type.__name__ = "Unsigned32"
_NcsRetransmissionDisconnectInitialWaitingPeriod_Object = MibScalar
ncsRetransmissionDisconnectInitialWaitingPeriod = _NcsRetransmissionDisconnectInitialWaitingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 11),
    _NcsRetransmissionDisconnectInitialWaitingPeriod_Type()
)
ncsRetransmissionDisconnectInitialWaitingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionDisconnectInitialWaitingPeriod.setStatus("current")


class _NcsRetransmissionDisconnectMinWaitingPeriod_Type(Unsigned32):
    """Custom type ncsRetransmissionDisconnectMinWaitingPeriod based on Unsigned32"""
    defaultValue = 15000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_NcsRetransmissionDisconnectMinWaitingPeriod_Type.__name__ = "Unsigned32"
_NcsRetransmissionDisconnectMinWaitingPeriod_Object = MibScalar
ncsRetransmissionDisconnectMinWaitingPeriod = _NcsRetransmissionDisconnectMinWaitingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 12),
    _NcsRetransmissionDisconnectMinWaitingPeriod_Type()
)
ncsRetransmissionDisconnectMinWaitingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionDisconnectMinWaitingPeriod.setStatus("current")


class _NcsRetransmissionDisconnectMaxWaitingPeriod_Type(Unsigned32):
    """Custom type ncsRetransmissionDisconnectMaxWaitingPeriod based on Unsigned32"""
    defaultValue = 600000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_NcsRetransmissionDisconnectMaxWaitingPeriod_Type.__name__ = "Unsigned32"
_NcsRetransmissionDisconnectMaxWaitingPeriod_Object = MibScalar
ncsRetransmissionDisconnectMaxWaitingPeriod = _NcsRetransmissionDisconnectMaxWaitingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 23, 13),
    _NcsRetransmissionDisconnectMaxWaitingPeriod_Type()
)
ncsRetransmissionDisconnectMaxWaitingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsRetransmissionDisconnectMaxWaitingPeriod.setStatus("current")
_NcsLinePackage_ObjectIdentity = ObjectIdentity
ncsLinePackage = _NcsLinePackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30)
)


class _NcsLinePackageBzDuration_Type(Unsigned32):
    """Custom type ncsLinePackageBzDuration based on Unsigned32"""
    defaultValue = 30000


_NcsLinePackageBzDuration_Type.__name__ = "Unsigned32"
_NcsLinePackageBzDuration_Object = MibScalar
ncsLinePackageBzDuration = _NcsLinePackageBzDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30, 4),
    _NcsLinePackageBzDuration_Type()
)
ncsLinePackageBzDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsLinePackageBzDuration.setStatus("current")


class _NcsLinePackageDlDuration_Type(Unsigned32):
    """Custom type ncsLinePackageDlDuration based on Unsigned32"""
    defaultValue = 16000


_NcsLinePackageDlDuration_Type.__name__ = "Unsigned32"
_NcsLinePackageDlDuration_Object = MibScalar
ncsLinePackageDlDuration = _NcsLinePackageDlDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30, 8),
    _NcsLinePackageDlDuration_Type()
)
ncsLinePackageDlDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsLinePackageDlDuration.setStatus("current")


class _NcsLinePackageLDuration_Type(Unsigned32):
    """Custom type ncsLinePackageLDuration based on Unsigned32"""
    defaultValue = 2000


_NcsLinePackageLDuration_Type.__name__ = "Unsigned32"
_NcsLinePackageLDuration_Object = MibScalar
ncsLinePackageLDuration = _NcsLinePackageLDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30, 12),
    _NcsLinePackageLDuration_Type()
)
ncsLinePackageLDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsLinePackageLDuration.setStatus("current")


class _NcsLinePackageMwiDuration_Type(Unsigned32):
    """Custom type ncsLinePackageMwiDuration based on Unsigned32"""
    defaultValue = 16000


_NcsLinePackageMwiDuration_Type.__name__ = "Unsigned32"
_NcsLinePackageMwiDuration_Object = MibScalar
ncsLinePackageMwiDuration = _NcsLinePackageMwiDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30, 16),
    _NcsLinePackageMwiDuration_Type()
)
ncsLinePackageMwiDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsLinePackageMwiDuration.setStatus("current")


class _NcsLinePackageOtDuration_Type(Unsigned32):
    """Custom type ncsLinePackageOtDuration based on Unsigned32"""
    defaultValue = 65535000


_NcsLinePackageOtDuration_Type.__name__ = "Unsigned32"
_NcsLinePackageOtDuration_Object = MibScalar
ncsLinePackageOtDuration = _NcsLinePackageOtDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30, 20),
    _NcsLinePackageOtDuration_Type()
)
ncsLinePackageOtDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsLinePackageOtDuration.setStatus("current")


class _NcsLinePackageRbkDuration_Type(Unsigned32):
    """Custom type ncsLinePackageRbkDuration based on Unsigned32"""
    defaultValue = 180000


_NcsLinePackageRbkDuration_Type.__name__ = "Unsigned32"
_NcsLinePackageRbkDuration_Object = MibScalar
ncsLinePackageRbkDuration = _NcsLinePackageRbkDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30, 24),
    _NcsLinePackageRbkDuration_Type()
)
ncsLinePackageRbkDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsLinePackageRbkDuration.setStatus("current")


class _NcsLinePackageRgDuration_Type(Unsigned32):
    """Custom type ncsLinePackageRgDuration based on Unsigned32"""
    defaultValue = 180000


_NcsLinePackageRgDuration_Type.__name__ = "Unsigned32"
_NcsLinePackageRgDuration_Object = MibScalar
ncsLinePackageRgDuration = _NcsLinePackageRgDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30, 28),
    _NcsLinePackageRgDuration_Type()
)
ncsLinePackageRgDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsLinePackageRgDuration.setStatus("current")


class _NcsLinePackageRoDuration_Type(Unsigned32):
    """Custom type ncsLinePackageRoDuration based on Unsigned32"""
    defaultValue = 30000


_NcsLinePackageRoDuration_Type.__name__ = "Unsigned32"
_NcsLinePackageRoDuration_Object = MibScalar
ncsLinePackageRoDuration = _NcsLinePackageRoDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30, 32),
    _NcsLinePackageRoDuration_Type()
)
ncsLinePackageRoDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsLinePackageRoDuration.setStatus("current")


class _NcsLinePackageRtDuration_Type(Unsigned32):
    """Custom type ncsLinePackageRtDuration based on Unsigned32"""
    defaultValue = 180000


_NcsLinePackageRtDuration_Type.__name__ = "Unsigned32"
_NcsLinePackageRtDuration_Object = MibScalar
ncsLinePackageRtDuration = _NcsLinePackageRtDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30, 36),
    _NcsLinePackageRtDuration_Type()
)
ncsLinePackageRtDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsLinePackageRtDuration.setStatus("current")


class _NcsLinePackageSlDuration_Type(Unsigned32):
    """Custom type ncsLinePackageSlDuration based on Unsigned32"""
    defaultValue = 16000


_NcsLinePackageSlDuration_Type.__name__ = "Unsigned32"
_NcsLinePackageSlDuration_Object = MibScalar
ncsLinePackageSlDuration = _NcsLinePackageSlDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30, 40),
    _NcsLinePackageSlDuration_Type()
)
ncsLinePackageSlDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsLinePackageSlDuration.setStatus("current")


class _NcsLinePackageTCriticalDuration_Type(Unsigned32):
    """Custom type ncsLinePackageTCriticalDuration based on Unsigned32"""
    defaultValue = 4000


_NcsLinePackageTCriticalDuration_Type.__name__ = "Unsigned32"
_NcsLinePackageTCriticalDuration_Object = MibScalar
ncsLinePackageTCriticalDuration = _NcsLinePackageTCriticalDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30, 44),
    _NcsLinePackageTCriticalDuration_Type()
)
ncsLinePackageTCriticalDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsLinePackageTCriticalDuration.setStatus("current")


class _NcsLinePackageTPartialDuration_Type(Unsigned32):
    """Custom type ncsLinePackageTPartialDuration based on Unsigned32"""
    defaultValue = 16000


_NcsLinePackageTPartialDuration_Type.__name__ = "Unsigned32"
_NcsLinePackageTPartialDuration_Object = MibScalar
ncsLinePackageTPartialDuration = _NcsLinePackageTPartialDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 30, 48),
    _NcsLinePackageTPartialDuration_Type()
)
ncsLinePackageTPartialDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncsLinePackageTPartialDuration.setStatus("current")
_NcsStats_ObjectIdentity = ObjectIdentity
ncsStats = _NcsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 50)
)
_NcsStatsCurrentNumberOfActiveConnections_Type = Unsigned32
_NcsStatsCurrentNumberOfActiveConnections_Object = MibScalar
ncsStatsCurrentNumberOfActiveConnections = _NcsStatsCurrentNumberOfActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 50, 1),
    _NcsStatsCurrentNumberOfActiveConnections_Type()
)
ncsStatsCurrentNumberOfActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncsStatsCurrentNumberOfActiveConnections.setStatus("current")
_NcsStatsCurrentStatistics_ObjectIdentity = ObjectIdentity
ncsStatsCurrentStatistics = _NcsStatsCurrentStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 50, 5)
)
_NcsStatsCurrentTotalNumberOfConnections_Type = Unsigned32
_NcsStatsCurrentTotalNumberOfConnections_Object = MibScalar
ncsStatsCurrentTotalNumberOfConnections = _NcsStatsCurrentTotalNumberOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 50, 5, 1),
    _NcsStatsCurrentTotalNumberOfConnections_Type()
)
ncsStatsCurrentTotalNumberOfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncsStatsCurrentTotalNumberOfConnections.setStatus("current")
_NcsStatsCurrentAvgConnectionTime_Type = Unsigned32
_NcsStatsCurrentAvgConnectionTime_Object = MibScalar
ncsStatsCurrentAvgConnectionTime = _NcsStatsCurrentAvgConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 50, 5, 2),
    _NcsStatsCurrentAvgConnectionTime_Type()
)
ncsStatsCurrentAvgConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncsStatsCurrentAvgConnectionTime.setStatus("current")
_NcsStatsCumulatedStatistics_ObjectIdentity = ObjectIdentity
ncsStatsCumulatedStatistics = _NcsStatsCumulatedStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 50, 6)
)
_NcsStatsCumulatedTotalNumberOfConnections_Type = Unsigned32
_NcsStatsCumulatedTotalNumberOfConnections_Object = MibScalar
ncsStatsCumulatedTotalNumberOfConnections = _NcsStatsCumulatedTotalNumberOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 50, 6, 1),
    _NcsStatsCumulatedTotalNumberOfConnections_Type()
)
ncsStatsCumulatedTotalNumberOfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncsStatsCumulatedTotalNumberOfConnections.setStatus("current")
_NcsStatsCumulatedAvgConnectionTime_Type = Unsigned32
_NcsStatsCumulatedAvgConnectionTime_Object = MibScalar
ncsStatsCumulatedAvgConnectionTime = _NcsStatsCumulatedAvgConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 1, 50, 6, 2),
    _NcsStatsCumulatedAvgConnectionTime_Type()
)
ncsStatsCumulatedAvgConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncsStatsCumulatedAvgConnectionTime.setStatus("current")
_NcsConformance_ObjectIdentity = ObjectIdentity
ncsConformance = _NcsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 2)
)
_NcsCompliances_ObjectIdentity = ObjectIdentity
ncsCompliances = _NcsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 2, 1)
)
_NcsGroups_ObjectIdentity = ObjectIdentity
ncsGroups = _NcsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 2, 2)
)

# Managed Objects groups

ncsBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 2, 2, 1)
)
ncsBasicGroupVer1.setObjects(
      *(("MX-NCS-MIB", "ncsPort"),
        ("MX-NCS-MIB", "ncsDefaultDigitMap"),
        ("MX-NCS-MIB", "ncsRestartLevel"),
        ("MX-NCS-MIB", "ncsEndpointIdListIncludeNotStarted"),
        ("MX-NCS-MIB", "ncsPiggyBackingEnable"),
        ("MX-NCS-MIB", "ncsEndpointIdTerm1"),
        ("MX-NCS-MIB", "ncsEndpointIdTerm2"),
        ("MX-NCS-MIB", "ncsRetransmissionAlgorithm"),
        ("MX-NCS-MIB", "ncsRetransmissionInitialPeriod"),
        ("MX-NCS-MIB", "ncsRetransmissionMaxPeriod"),
        ("MX-NCS-MIB", "ncsRetransmissionDisconnectTimeout"),
        ("MX-NCS-MIB", "ncsRetransmissionSuspicionThreshold"),
        ("MX-NCS-MIB", "ncsRetransmissionSuspicionThresholdDnsQuery"),
        ("MX-NCS-MIB", "ncsRetransmissionDisconnectThreshold"),
        ("MX-NCS-MIB", "ncsRetransmissionDisconnectThresholdDnsQuery"),
        ("MX-NCS-MIB", "ncsRetransmissionHistoryTimeout"),
        ("MX-NCS-MIB", "ncsRetransmissionMaxWaitingDelay"),
        ("MX-NCS-MIB", "ncsRetransmissionDisconnectInitialWaitingPeriod"),
        ("MX-NCS-MIB", "ncsRetransmissionDisconnectMinWaitingPeriod"),
        ("MX-NCS-MIB", "ncsRetransmissionDisconnectMaxWaitingPeriod"))
)
if mibBuilder.loadTexts:
    ncsBasicGroupVer1.setStatus("current")

ncsLinePkgGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 2, 2, 4)
)
ncsLinePkgGroupVer1.setObjects(
      *(("MX-NCS-MIB", "ncsLinePackageBzDuration"),
        ("MX-NCS-MIB", "ncsLinePackageDlDuration"),
        ("MX-NCS-MIB", "ncsLinePackageLDuration"),
        ("MX-NCS-MIB", "ncsLinePackageMwiDuration"),
        ("MX-NCS-MIB", "ncsLinePackageOtDuration"),
        ("MX-NCS-MIB", "ncsLinePackageRbkDuration"),
        ("MX-NCS-MIB", "ncsLinePackageRgDuration"),
        ("MX-NCS-MIB", "ncsLinePackageRoDuration"),
        ("MX-NCS-MIB", "ncsLinePackageRtDuration"),
        ("MX-NCS-MIB", "ncsLinePackageSlDuration"),
        ("MX-NCS-MIB", "ncsLinePackageTCriticalDuration"),
        ("MX-NCS-MIB", "ncsLinePackageTPartialDuration"))
)
if mibBuilder.loadTexts:
    ncsLinePkgGroupVer1.setStatus("current")

ncsStatsBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 2, 2, 5)
)
ncsStatsBasicGroupVer1.setObjects(
      *(("MX-NCS-MIB", "ncsStatsCurrentNumberOfActiveConnections"),
        ("MX-NCS-MIB", "ncsStatsCurrentTotalNumberOfConnections"),
        ("MX-NCS-MIB", "ncsStatsCurrentAvgConnectionTime"),
        ("MX-NCS-MIB", "ncsStatsCumulatedTotalNumberOfConnections"),
        ("MX-NCS-MIB", "ncsStatsCumulatedAvgConnectionTime"))
)
if mibBuilder.loadTexts:
    ncsStatsBasicGroupVer1.setStatus("current")

ncsCallAgentGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 2, 2, 6)
)
ncsCallAgentGroupVer1.setObjects(
      *(("MX-NCS-MIB", "ncsCAConfigSource"),
        ("MX-NCS-MIB", "ncsCAHost"),
        ("MX-NCS-MIB", "ncsCAPort"),
        ("MX-NCS-MIB", "ncsCASelectConfigSource"),
        ("MX-NCS-MIB", "ncsCAStaticHost"),
        ("MX-NCS-MIB", "ncsCAStaticPort"),
        ("MX-NCS-MIB", "ncsCADhcpSiteSpecificCode"))
)
if mibBuilder.loadTexts:
    ncsCallAgentGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ncsResidentialGatewayBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 20, 10, 1, 2, 1, 1)
)
ncsResidentialGatewayBasicComplVer1.setObjects(
      *(("MX-NCS-MIB", "ncsBasicGroupVer1"),
        ("MX-NCS-MIB", "ncsLinePkgGroupVer1"),
        ("MX-NCS-MIB", "ncsStatsBasicGroupVer1"),
        ("MX-NCS-MIB", "ncsCallAgentGroupVer1"))
)
if mibBuilder.loadTexts:
    ncsResidentialGatewayBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-NCS-MIB",
    **{"ipAddressStatusNcsCallAgent": ipAddressStatusNcsCallAgent,
       "ncsCAConfigSource": ncsCAConfigSource,
       "ncsCAHost": ncsCAHost,
       "ncsCAPort": ncsCAPort,
       "ipAddressConfigNcsCallAgent": ipAddressConfigNcsCallAgent,
       "ncsCASelectConfigSource": ncsCASelectConfigSource,
       "ipAddressConfigNcsCAStatic": ipAddressConfigNcsCAStatic,
       "ncsCAStaticHost": ncsCAStaticHost,
       "ncsCAStaticPort": ncsCAStaticPort,
       "ipAddressConfigNcsCADhcp": ipAddressConfigNcsCADhcp,
       "ncsCADhcpSiteSpecificCode": ncsCADhcpSiteSpecificCode,
       "ncs": ncs,
       "ncsMIB": ncsMIB,
       "ncsMIBObjects": ncsMIBObjects,
       "ncsPort": ncsPort,
       "ncsDefaultDigitMap": ncsDefaultDigitMap,
       "ncsRestartLevel": ncsRestartLevel,
       "ncsEndpointIdListIncludeNotStarted": ncsEndpointIdListIncludeNotStarted,
       "ncsPiggyBackingEnable": ncsPiggyBackingEnable,
       "ncsEndpointId": ncsEndpointId,
       "ncsEndpointIfTable": ncsEndpointIfTable,
       "ncsEndpointIfEntry": ncsEndpointIfEntry,
       "ncsEndpointIdTerm1": ncsEndpointIdTerm1,
       "ncsEndpointIdTerm2": ncsEndpointIdTerm2,
       "ncsRetransmission": ncsRetransmission,
       "ncsRetransmissionAlgorithm": ncsRetransmissionAlgorithm,
       "ncsRetransmissionInitialPeriod": ncsRetransmissionInitialPeriod,
       "ncsRetransmissionMaxPeriod": ncsRetransmissionMaxPeriod,
       "ncsRetransmissionDisconnectTimeout": ncsRetransmissionDisconnectTimeout,
       "ncsRetransmissionSuspicionThreshold": ncsRetransmissionSuspicionThreshold,
       "ncsRetransmissionSuspicionThresholdDnsQuery": ncsRetransmissionSuspicionThresholdDnsQuery,
       "ncsRetransmissionDisconnectThreshold": ncsRetransmissionDisconnectThreshold,
       "ncsRetransmissionDisconnectThresholdDnsQuery": ncsRetransmissionDisconnectThresholdDnsQuery,
       "ncsRetransmissionHistoryTimeout": ncsRetransmissionHistoryTimeout,
       "ncsRetransmissionMaxWaitingDelay": ncsRetransmissionMaxWaitingDelay,
       "ncsRetransmissionDisconnectInitialWaitingPeriod": ncsRetransmissionDisconnectInitialWaitingPeriod,
       "ncsRetransmissionDisconnectMinWaitingPeriod": ncsRetransmissionDisconnectMinWaitingPeriod,
       "ncsRetransmissionDisconnectMaxWaitingPeriod": ncsRetransmissionDisconnectMaxWaitingPeriod,
       "ncsLinePackage": ncsLinePackage,
       "ncsLinePackageBzDuration": ncsLinePackageBzDuration,
       "ncsLinePackageDlDuration": ncsLinePackageDlDuration,
       "ncsLinePackageLDuration": ncsLinePackageLDuration,
       "ncsLinePackageMwiDuration": ncsLinePackageMwiDuration,
       "ncsLinePackageOtDuration": ncsLinePackageOtDuration,
       "ncsLinePackageRbkDuration": ncsLinePackageRbkDuration,
       "ncsLinePackageRgDuration": ncsLinePackageRgDuration,
       "ncsLinePackageRoDuration": ncsLinePackageRoDuration,
       "ncsLinePackageRtDuration": ncsLinePackageRtDuration,
       "ncsLinePackageSlDuration": ncsLinePackageSlDuration,
       "ncsLinePackageTCriticalDuration": ncsLinePackageTCriticalDuration,
       "ncsLinePackageTPartialDuration": ncsLinePackageTPartialDuration,
       "ncsStats": ncsStats,
       "ncsStatsCurrentNumberOfActiveConnections": ncsStatsCurrentNumberOfActiveConnections,
       "ncsStatsCurrentStatistics": ncsStatsCurrentStatistics,
       "ncsStatsCurrentTotalNumberOfConnections": ncsStatsCurrentTotalNumberOfConnections,
       "ncsStatsCurrentAvgConnectionTime": ncsStatsCurrentAvgConnectionTime,
       "ncsStatsCumulatedStatistics": ncsStatsCumulatedStatistics,
       "ncsStatsCumulatedTotalNumberOfConnections": ncsStatsCumulatedTotalNumberOfConnections,
       "ncsStatsCumulatedAvgConnectionTime": ncsStatsCumulatedAvgConnectionTime,
       "ncsConformance": ncsConformance,
       "ncsCompliances": ncsCompliances,
       "ncsResidentialGatewayBasicComplVer1": ncsResidentialGatewayBasicComplVer1,
       "ncsGroups": ncsGroups,
       "ncsBasicGroupVer1": ncsBasicGroupVer1,
       "ncsLinePkgGroupVer1": ncsLinePkgGroupVer1,
       "ncsStatsBasicGroupVer1": ncsStatsBasicGroupVer1,
       "ncsCallAgentGroupVer1": ncsCallAgentGroupVer1}
)
