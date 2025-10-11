# SNMP MIB module (MX-MGCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-MGCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:54 2025
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

(MxEnableState,
 MxIpConfigSource,
 MxIpDhcpSiteSpecificCode,
 MxIpHostName,
 MxIpPort,
 MxIpSelectConfigSource) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
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

mgcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1)
)
if mibBuilder.loadTexts:
    mgcpMIB.setRevisions(
        ("2008-07-29 00:00",
         "2004-09-21 00:00",
         "2004-07-20 00:00",
         "2002-12-31 00:00",
         "2002-11-18 00:00",
         "2002-07-10 00:00",
         "2002-07-05 00:00",
         "2002-06-26 00:00",
         "2002-05-01 00:00",
         "2002-03-13 00:00",
         "2001-11-23 00:00",
         "2001-08-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressStatusMgcpCallAgent_ObjectIdentity = ObjectIdentity
ipAddressStatusMgcpCallAgent = _IpAddressStatusMgcpCallAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 50)
)


class _MgcpCAConfigSource_Type(MxIpConfigSource):
    """Custom type mgcpCAConfigSource based on MxIpConfigSource"""
    defaultValue = 1


_MgcpCAConfigSource_Type.__name__ = "MxIpConfigSource"
_MgcpCAConfigSource_Object = MibScalar
mgcpCAConfigSource = _MgcpCAConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 50, 1),
    _MgcpCAConfigSource_Type()
)
mgcpCAConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcpCAConfigSource.setStatus("current")


class _MgcpCAHost_Type(MxIpHostName):
    """Custom type mgcpCAHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_MgcpCAHost_Type.__name__ = "MxIpHostName"
_MgcpCAHost_Object = MibScalar
mgcpCAHost = _MgcpCAHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 50, 2),
    _MgcpCAHost_Type()
)
mgcpCAHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcpCAHost.setStatus("current")


class _MgcpCAPort_Type(MxIpPort):
    """Custom type mgcpCAPort based on MxIpPort"""
    defaultValue = 2727


_MgcpCAPort_Type.__name__ = "MxIpPort"
_MgcpCAPort_Object = MibScalar
mgcpCAPort = _MgcpCAPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 50, 3),
    _MgcpCAPort_Type()
)
mgcpCAPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcpCAPort.setStatus("current")
_IpAddressConfigMgcpCallAgent_ObjectIdentity = ObjectIdentity
ipAddressConfigMgcpCallAgent = _IpAddressConfigMgcpCallAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 50)
)


class _MgcpCASelectConfigSource_Type(MxIpSelectConfigSource):
    """Custom type mgcpCASelectConfigSource based on MxIpSelectConfigSource"""
    defaultValue = 1


_MgcpCASelectConfigSource_Type.__name__ = "MxIpSelectConfigSource"
_MgcpCASelectConfigSource_Object = MibScalar
mgcpCASelectConfigSource = _MgcpCASelectConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 50, 1),
    _MgcpCASelectConfigSource_Type()
)
mgcpCASelectConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpCASelectConfigSource.setStatus("current")
_IpAddressConfigMgcpCAStatic_ObjectIdentity = ObjectIdentity
ipAddressConfigMgcpCAStatic = _IpAddressConfigMgcpCAStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 50, 6)
)


class _MgcpCAStaticHost_Type(MxIpHostName):
    """Custom type mgcpCAStaticHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_MgcpCAStaticHost_Type.__name__ = "MxIpHostName"
_MgcpCAStaticHost_Object = MibScalar
mgcpCAStaticHost = _MgcpCAStaticHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 50, 6, 1),
    _MgcpCAStaticHost_Type()
)
mgcpCAStaticHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpCAStaticHost.setStatus("current")


class _MgcpCAStaticPort_Type(MxIpPort):
    """Custom type mgcpCAStaticPort based on MxIpPort"""
    defaultValue = 2727


_MgcpCAStaticPort_Type.__name__ = "MxIpPort"
_MgcpCAStaticPort_Object = MibScalar
mgcpCAStaticPort = _MgcpCAStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 50, 6, 2),
    _MgcpCAStaticPort_Type()
)
mgcpCAStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpCAStaticPort.setStatus("current")
_IpAddressConfigMgcpCADhcp_ObjectIdentity = ObjectIdentity
ipAddressConfigMgcpCADhcp = _IpAddressConfigMgcpCADhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 50, 7)
)


class _MgcpCADhcpSiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):
    """Custom type mgcpCADhcpSiteSpecificCode based on MxIpDhcpSiteSpecificCode"""
    defaultValue = 0


_MgcpCADhcpSiteSpecificCode_Type.__name__ = "MxIpDhcpSiteSpecificCode"
_MgcpCADhcpSiteSpecificCode_Object = MibScalar
mgcpCADhcpSiteSpecificCode = _MgcpCADhcpSiteSpecificCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 50, 7, 1),
    _MgcpCADhcpSiteSpecificCode_Type()
)
mgcpCADhcpSiteSpecificCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpCADhcpSiteSpecificCode.setStatus("current")
_Mgcp_ObjectIdentity = ObjectIdentity
mgcp = _Mgcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1)
)
if mibBuilder.loadTexts:
    mgcp.setStatus("current")
_MgcpMIBObjects_ObjectIdentity = ObjectIdentity
mgcpMIBObjects = _MgcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1)
)


class _MgcpPort_Type(MxIpPort):
    """Custom type mgcpPort based on MxIpPort"""
    defaultValue = 2427


_MgcpPort_Type.__name__ = "MxIpPort"
_MgcpPort_Object = MibScalar
mgcpPort = _MgcpPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 1),
    _MgcpPort_Type()
)
mgcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpPort.setStatus("current")


class _MgcpDefaultDigitMap_Type(OctetString):
    """Custom type mgcpDefaultDigitMap based on OctetString"""
    defaultValue = OctetString("x.T")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MgcpDefaultDigitMap_Type.__name__ = "OctetString"
_MgcpDefaultDigitMap_Object = MibScalar
mgcpDefaultDigitMap = _MgcpDefaultDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 2),
    _MgcpDefaultDigitMap_Type()
)
mgcpDefaultDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpDefaultDigitMap.setStatus("current")


class _MgcpDefaultPackage_Type(Integer32):
    """Custom type mgcpDefaultPackage based on Integer32"""
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
        *(("linePackage", 0),
          ("dtmfPackage", 1),
          ("genericPackage", 2))
    )


_MgcpDefaultPackage_Type.__name__ = "Integer32"
_MgcpDefaultPackage_Object = MibScalar
mgcpDefaultPackage = _MgcpDefaultPackage_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 3),
    _MgcpDefaultPackage_Type()
)
mgcpDefaultPackage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpDefaultPackage.setStatus("current")


class _MgcpRestartLevel_Type(Integer32):
    """Custom type mgcpRestartLevel based on Integer32"""
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


_MgcpRestartLevel_Type.__name__ = "Integer32"
_MgcpRestartLevel_Object = MibScalar
mgcpRestartLevel = _MgcpRestartLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 4),
    _MgcpRestartLevel_Type()
)
mgcpRestartLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRestartLevel.setStatus("current")


class _MgcpEndpointIdListIncludeNotStarted_Type(Integer32):
    """Custom type mgcpEndpointIdListIncludeNotStarted based on Integer32"""
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


_MgcpEndpointIdListIncludeNotStarted_Type.__name__ = "Integer32"
_MgcpEndpointIdListIncludeNotStarted_Object = MibScalar
mgcpEndpointIdListIncludeNotStarted = _MgcpEndpointIdListIncludeNotStarted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 5),
    _MgcpEndpointIdListIncludeNotStarted_Type()
)
mgcpEndpointIdListIncludeNotStarted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpEndpointIdListIncludeNotStarted.setStatus("current")


class _MgcpPiggyBackingEnable_Type(Integer32):
    """Custom type mgcpPiggyBackingEnable based on Integer32"""
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


_MgcpPiggyBackingEnable_Type.__name__ = "Integer32"
_MgcpPiggyBackingEnable_Object = MibScalar
mgcpPiggyBackingEnable = _MgcpPiggyBackingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 6),
    _MgcpPiggyBackingEnable_Type()
)
mgcpPiggyBackingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpPiggyBackingEnable.setStatus("current")


class _MgcpAddPtimeIfPresentInLCO_Type(Integer32):
    """Custom type mgcpAddPtimeIfPresentInLCO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("excludePtime", 0),
          ("includePtime", 1))
    )


_MgcpAddPtimeIfPresentInLCO_Type.__name__ = "Integer32"
_MgcpAddPtimeIfPresentInLCO_Object = MibScalar
mgcpAddPtimeIfPresentInLCO = _MgcpAddPtimeIfPresentInLCO_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 10),
    _MgcpAddPtimeIfPresentInLCO_Type()
)
mgcpAddPtimeIfPresentInLCO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpAddPtimeIfPresentInLCO.setStatus("current")
_MgcpEndpointId_ObjectIdentity = ObjectIdentity
mgcpEndpointId = _MgcpEndpointId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 17)
)
_MgcpEndpointIfTable_Object = MibTable
mgcpEndpointIfTable = _MgcpEndpointIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 17, 10)
)
if mibBuilder.loadTexts:
    mgcpEndpointIfTable.setStatus("current")
_MgcpEndpointIfEntry_Object = MibTableRow
mgcpEndpointIfEntry = _MgcpEndpointIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 17, 10, 1)
)
mgcpEndpointIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mgcpEndpointIfEntry.setStatus("current")


class _MgcpEndpointIdTerm1_Type(OctetString):
    """Custom type mgcpEndpointIdTerm1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MgcpEndpointIdTerm1_Type.__name__ = "OctetString"
_MgcpEndpointIdTerm1_Object = MibTableColumn
mgcpEndpointIdTerm1 = _MgcpEndpointIdTerm1_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 17, 10, 1, 1),
    _MgcpEndpointIdTerm1_Type()
)
mgcpEndpointIdTerm1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpEndpointIdTerm1.setStatus("current")


class _MgcpEndpointIdTerm2_Type(OctetString):
    """Custom type mgcpEndpointIdTerm2 based on OctetString"""
    defaultValue = OctetString("aaln")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MgcpEndpointIdTerm2_Type.__name__ = "OctetString"
_MgcpEndpointIdTerm2_Object = MibTableColumn
mgcpEndpointIdTerm2 = _MgcpEndpointIdTerm2_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 17, 10, 1, 2),
    _MgcpEndpointIdTerm2_Type()
)
mgcpEndpointIdTerm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpEndpointIdTerm2.setStatus("current")
_MgcpRetransmission_ObjectIdentity = ObjectIdentity
mgcpRetransmission = _MgcpRetransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18)
)


class _MgcpRetransmissionAlgorithm_Type(Integer32):
    """Custom type mgcpRetransmissionAlgorithm based on Integer32"""
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


_MgcpRetransmissionAlgorithm_Type.__name__ = "Integer32"
_MgcpRetransmissionAlgorithm_Object = MibScalar
mgcpRetransmissionAlgorithm = _MgcpRetransmissionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 1),
    _MgcpRetransmissionAlgorithm_Type()
)
mgcpRetransmissionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionAlgorithm.setStatus("current")


class _MgcpRetransmissionInitialPeriod_Type(Unsigned32):
    """Custom type mgcpRetransmissionInitialPeriod based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4294967295),
    )


_MgcpRetransmissionInitialPeriod_Type.__name__ = "Unsigned32"
_MgcpRetransmissionInitialPeriod_Object = MibScalar
mgcpRetransmissionInitialPeriod = _MgcpRetransmissionInitialPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 2),
    _MgcpRetransmissionInitialPeriod_Type()
)
mgcpRetransmissionInitialPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionInitialPeriod.setStatus("current")


class _MgcpRetransmissionMaxPeriod_Type(Unsigned32):
    """Custom type mgcpRetransmissionMaxPeriod based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4294967295),
    )


_MgcpRetransmissionMaxPeriod_Type.__name__ = "Unsigned32"
_MgcpRetransmissionMaxPeriod_Object = MibScalar
mgcpRetransmissionMaxPeriod = _MgcpRetransmissionMaxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 3),
    _MgcpRetransmissionMaxPeriod_Type()
)
mgcpRetransmissionMaxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionMaxPeriod.setStatus("current")


class _MgcpRetransmissionDisconnectTimeout_Type(Unsigned32):
    """Custom type mgcpRetransmissionDisconnectTimeout based on Unsigned32"""
    defaultValue = 20000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_MgcpRetransmissionDisconnectTimeout_Type.__name__ = "Unsigned32"
_MgcpRetransmissionDisconnectTimeout_Object = MibScalar
mgcpRetransmissionDisconnectTimeout = _MgcpRetransmissionDisconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 4),
    _MgcpRetransmissionDisconnectTimeout_Type()
)
mgcpRetransmissionDisconnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionDisconnectTimeout.setStatus("current")


class _MgcpRetransmissionSuspicionThreshold_Type(Unsigned32):
    """Custom type mgcpRetransmissionSuspicionThreshold based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MgcpRetransmissionSuspicionThreshold_Type.__name__ = "Unsigned32"
_MgcpRetransmissionSuspicionThreshold_Object = MibScalar
mgcpRetransmissionSuspicionThreshold = _MgcpRetransmissionSuspicionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 5),
    _MgcpRetransmissionSuspicionThreshold_Type()
)
mgcpRetransmissionSuspicionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionSuspicionThreshold.setStatus("current")


class _MgcpRetransmissionSuspicionThresholdDnsQuery_Type(Integer32):
    """Custom type mgcpRetransmissionSuspicionThresholdDnsQuery based on Integer32"""
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


_MgcpRetransmissionSuspicionThresholdDnsQuery_Type.__name__ = "Integer32"
_MgcpRetransmissionSuspicionThresholdDnsQuery_Object = MibScalar
mgcpRetransmissionSuspicionThresholdDnsQuery = _MgcpRetransmissionSuspicionThresholdDnsQuery_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 6),
    _MgcpRetransmissionSuspicionThresholdDnsQuery_Type()
)
mgcpRetransmissionSuspicionThresholdDnsQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionSuspicionThresholdDnsQuery.setStatus("current")


class _MgcpRetransmissionDisconnectThreshold_Type(Unsigned32):
    """Custom type mgcpRetransmissionDisconnectThreshold based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MgcpRetransmissionDisconnectThreshold_Type.__name__ = "Unsigned32"
_MgcpRetransmissionDisconnectThreshold_Object = MibScalar
mgcpRetransmissionDisconnectThreshold = _MgcpRetransmissionDisconnectThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 7),
    _MgcpRetransmissionDisconnectThreshold_Type()
)
mgcpRetransmissionDisconnectThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionDisconnectThreshold.setStatus("current")


class _MgcpRetransmissionDisconnectThresholdDnsQuery_Type(Integer32):
    """Custom type mgcpRetransmissionDisconnectThresholdDnsQuery based on Integer32"""
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


_MgcpRetransmissionDisconnectThresholdDnsQuery_Type.__name__ = "Integer32"
_MgcpRetransmissionDisconnectThresholdDnsQuery_Object = MibScalar
mgcpRetransmissionDisconnectThresholdDnsQuery = _MgcpRetransmissionDisconnectThresholdDnsQuery_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 8),
    _MgcpRetransmissionDisconnectThresholdDnsQuery_Type()
)
mgcpRetransmissionDisconnectThresholdDnsQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionDisconnectThresholdDnsQuery.setStatus("current")


class _MgcpRetransmissionHistoryTimeout_Type(Unsigned32):
    """Custom type mgcpRetransmissionHistoryTimeout based on Unsigned32"""
    defaultValue = 20000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_MgcpRetransmissionHistoryTimeout_Type.__name__ = "Unsigned32"
_MgcpRetransmissionHistoryTimeout_Object = MibScalar
mgcpRetransmissionHistoryTimeout = _MgcpRetransmissionHistoryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 9),
    _MgcpRetransmissionHistoryTimeout_Type()
)
mgcpRetransmissionHistoryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionHistoryTimeout.setStatus("current")


class _MgcpRetransmissionMaxWaitingDelay_Type(Unsigned32):
    """Custom type mgcpRetransmissionMaxWaitingDelay based on Unsigned32"""
    defaultValue = 600000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_MgcpRetransmissionMaxWaitingDelay_Type.__name__ = "Unsigned32"
_MgcpRetransmissionMaxWaitingDelay_Object = MibScalar
mgcpRetransmissionMaxWaitingDelay = _MgcpRetransmissionMaxWaitingDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 10),
    _MgcpRetransmissionMaxWaitingDelay_Type()
)
mgcpRetransmissionMaxWaitingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionMaxWaitingDelay.setStatus("current")


class _MgcpRetransmissionDisconnectInitialWaitingPeriod_Type(Unsigned32):
    """Custom type mgcpRetransmissionDisconnectInitialWaitingPeriod based on Unsigned32"""
    defaultValue = 15000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_MgcpRetransmissionDisconnectInitialWaitingPeriod_Type.__name__ = "Unsigned32"
_MgcpRetransmissionDisconnectInitialWaitingPeriod_Object = MibScalar
mgcpRetransmissionDisconnectInitialWaitingPeriod = _MgcpRetransmissionDisconnectInitialWaitingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 11),
    _MgcpRetransmissionDisconnectInitialWaitingPeriod_Type()
)
mgcpRetransmissionDisconnectInitialWaitingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionDisconnectInitialWaitingPeriod.setStatus("current")


class _MgcpRetransmissionDisconnectMinWaitingPeriod_Type(Unsigned32):
    """Custom type mgcpRetransmissionDisconnectMinWaitingPeriod based on Unsigned32"""
    defaultValue = 15000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_MgcpRetransmissionDisconnectMinWaitingPeriod_Type.__name__ = "Unsigned32"
_MgcpRetransmissionDisconnectMinWaitingPeriod_Object = MibScalar
mgcpRetransmissionDisconnectMinWaitingPeriod = _MgcpRetransmissionDisconnectMinWaitingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 12),
    _MgcpRetransmissionDisconnectMinWaitingPeriod_Type()
)
mgcpRetransmissionDisconnectMinWaitingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionDisconnectMinWaitingPeriod.setStatus("current")


class _MgcpRetransmissionDisconnectMaxWaitingPeriod_Type(Unsigned32):
    """Custom type mgcpRetransmissionDisconnectMaxWaitingPeriod based on Unsigned32"""
    defaultValue = 600000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_MgcpRetransmissionDisconnectMaxWaitingPeriod_Type.__name__ = "Unsigned32"
_MgcpRetransmissionDisconnectMaxWaitingPeriod_Object = MibScalar
mgcpRetransmissionDisconnectMaxWaitingPeriod = _MgcpRetransmissionDisconnectMaxWaitingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 18, 13),
    _MgcpRetransmissionDisconnectMaxWaitingPeriod_Type()
)
mgcpRetransmissionDisconnectMaxWaitingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpRetransmissionDisconnectMaxWaitingPeriod.setStatus("current")
_MgcpDtmfPackage_ObjectIdentity = ObjectIdentity
mgcpDtmfPackage = _MgcpDtmfPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 30)
)


class _MgcpDtmfPackageLDuration_Type(Unsigned32):
    """Custom type mgcpDtmfPackageLDuration based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpDtmfPackageLDuration_Type.__name__ = "Unsigned32"
_MgcpDtmfPackageLDuration_Object = MibScalar
mgcpDtmfPackageLDuration = _MgcpDtmfPackageLDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 30, 4),
    _MgcpDtmfPackageLDuration_Type()
)
mgcpDtmfPackageLDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpDtmfPackageLDuration.setStatus("current")


class _MgcpDtmfPackageTCriticalDuration_Type(Unsigned32):
    """Custom type mgcpDtmfPackageTCriticalDuration based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpDtmfPackageTCriticalDuration_Type.__name__ = "Unsigned32"
_MgcpDtmfPackageTCriticalDuration_Object = MibScalar
mgcpDtmfPackageTCriticalDuration = _MgcpDtmfPackageTCriticalDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 30, 8),
    _MgcpDtmfPackageTCriticalDuration_Type()
)
mgcpDtmfPackageTCriticalDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpDtmfPackageTCriticalDuration.setStatus("current")


class _MgcpDtmfPackageTPartialDuration_Type(Unsigned32):
    """Custom type mgcpDtmfPackageTPartialDuration based on Unsigned32"""
    defaultValue = 16000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpDtmfPackageTPartialDuration_Type.__name__ = "Unsigned32"
_MgcpDtmfPackageTPartialDuration_Object = MibScalar
mgcpDtmfPackageTPartialDuration = _MgcpDtmfPackageTPartialDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 30, 12),
    _MgcpDtmfPackageTPartialDuration_Type()
)
mgcpDtmfPackageTPartialDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpDtmfPackageTPartialDuration.setStatus("current")
_MgcpGenericMediaPackage_ObjectIdentity = ObjectIdentity
mgcpGenericMediaPackage = _MgcpGenericMediaPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 35)
)


class _MgcpGenericMediaPackageRbkDuration_Type(Unsigned32):
    """Custom type mgcpGenericMediaPackageRbkDuration based on Unsigned32"""
    defaultValue = 180000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpGenericMediaPackageRbkDuration_Type.__name__ = "Unsigned32"
_MgcpGenericMediaPackageRbkDuration_Object = MibScalar
mgcpGenericMediaPackageRbkDuration = _MgcpGenericMediaPackageRbkDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 35, 10),
    _MgcpGenericMediaPackageRbkDuration_Type()
)
mgcpGenericMediaPackageRbkDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpGenericMediaPackageRbkDuration.setStatus("current")


class _MgcpGenericMediaPackageRtDuration_Type(Unsigned32):
    """Custom type mgcpGenericMediaPackageRtDuration based on Unsigned32"""
    defaultValue = 180000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpGenericMediaPackageRtDuration_Type.__name__ = "Unsigned32"
_MgcpGenericMediaPackageRtDuration_Object = MibScalar
mgcpGenericMediaPackageRtDuration = _MgcpGenericMediaPackageRtDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 35, 14),
    _MgcpGenericMediaPackageRtDuration_Type()
)
mgcpGenericMediaPackageRtDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpGenericMediaPackageRtDuration.setStatus("current")
_MgcpLinePackage_ObjectIdentity = ObjectIdentity
mgcpLinePackage = _MgcpLinePackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40)
)


class _MgcpLinePackageBzDuration_Type(Unsigned32):
    """Custom type mgcpLinePackageBzDuration based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpLinePackageBzDuration_Type.__name__ = "Unsigned32"
_MgcpLinePackageBzDuration_Object = MibScalar
mgcpLinePackageBzDuration = _MgcpLinePackageBzDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40, 4),
    _MgcpLinePackageBzDuration_Type()
)
mgcpLinePackageBzDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpLinePackageBzDuration.setStatus("current")


class _MgcpLinePackageDlDuration_Type(Unsigned32):
    """Custom type mgcpLinePackageDlDuration based on Unsigned32"""
    defaultValue = 16000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpLinePackageDlDuration_Type.__name__ = "Unsigned32"
_MgcpLinePackageDlDuration_Object = MibScalar
mgcpLinePackageDlDuration = _MgcpLinePackageDlDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40, 8),
    _MgcpLinePackageDlDuration_Type()
)
mgcpLinePackageDlDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpLinePackageDlDuration.setStatus("current")


class _MgcpLinePackageMwiDuration_Type(Unsigned32):
    """Custom type mgcpLinePackageMwiDuration based on Unsigned32"""
    defaultValue = 16000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpLinePackageMwiDuration_Type.__name__ = "Unsigned32"
_MgcpLinePackageMwiDuration_Object = MibScalar
mgcpLinePackageMwiDuration = _MgcpLinePackageMwiDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40, 12),
    _MgcpLinePackageMwiDuration_Type()
)
mgcpLinePackageMwiDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpLinePackageMwiDuration.setStatus("current")


class _MgcpLinePackageOtDuration_Type(Unsigned32):
    """Custom type mgcpLinePackageOtDuration based on Unsigned32"""
    defaultValue = 65535000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpLinePackageOtDuration_Type.__name__ = "Unsigned32"
_MgcpLinePackageOtDuration_Object = MibScalar
mgcpLinePackageOtDuration = _MgcpLinePackageOtDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40, 16),
    _MgcpLinePackageOtDuration_Type()
)
mgcpLinePackageOtDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpLinePackageOtDuration.setStatus("current")


class _MgcpLinePackageRgDuration_Type(Unsigned32):
    """Custom type mgcpLinePackageRgDuration based on Unsigned32"""
    defaultValue = 180000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpLinePackageRgDuration_Type.__name__ = "Unsigned32"
_MgcpLinePackageRgDuration_Object = MibScalar
mgcpLinePackageRgDuration = _MgcpLinePackageRgDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40, 20),
    _MgcpLinePackageRgDuration_Type()
)
mgcpLinePackageRgDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpLinePackageRgDuration.setStatus("current")


class _MgcpLinePackageRoDuration_Type(Unsigned32):
    """Custom type mgcpLinePackageRoDuration based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpLinePackageRoDuration_Type.__name__ = "Unsigned32"
_MgcpLinePackageRoDuration_Object = MibScalar
mgcpLinePackageRoDuration = _MgcpLinePackageRoDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40, 24),
    _MgcpLinePackageRoDuration_Type()
)
mgcpLinePackageRoDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpLinePackageRoDuration.setStatus("current")


class _MgcpLinePackageSlDuration_Type(Unsigned32):
    """Custom type mgcpLinePackageSlDuration based on Unsigned32"""
    defaultValue = 16000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpLinePackageSlDuration_Type.__name__ = "Unsigned32"
_MgcpLinePackageSlDuration_Object = MibScalar
mgcpLinePackageSlDuration = _MgcpLinePackageSlDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40, 28),
    _MgcpLinePackageSlDuration_Type()
)
mgcpLinePackageSlDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpLinePackageSlDuration.setStatus("current")


class _MgcpLinePackageWtDuration_Type(Unsigned32):
    """Custom type mgcpLinePackageWtDuration based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpLinePackageWtDuration_Type.__name__ = "Unsigned32"
_MgcpLinePackageWtDuration_Object = MibScalar
mgcpLinePackageWtDuration = _MgcpLinePackageWtDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40, 32),
    _MgcpLinePackageWtDuration_Type()
)
mgcpLinePackageWtDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpLinePackageWtDuration.setStatus("current")


class _MgcpLinePackageOsiDuration_Type(Unsigned32):
    """Custom type mgcpLinePackageOsiDuration based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpLinePackageOsiDuration_Type.__name__ = "Unsigned32"
_MgcpLinePackageOsiDuration_Object = MibScalar
mgcpLinePackageOsiDuration = _MgcpLinePackageOsiDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40, 36),
    _MgcpLinePackageOsiDuration_Type()
)
mgcpLinePackageOsiDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpLinePackageOsiDuration.setStatus("current")


class _MgcpLinePackageHdPersistent_Type(Integer32):
    """Custom type mgcpLinePackageHdPersistent based on Integer32"""
    defaultValue = 0

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


_MgcpLinePackageHdPersistent_Type.__name__ = "Integer32"
_MgcpLinePackageHdPersistent_Object = MibScalar
mgcpLinePackageHdPersistent = _MgcpLinePackageHdPersistent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40, 100),
    _MgcpLinePackageHdPersistent_Type()
)
mgcpLinePackageHdPersistent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpLinePackageHdPersistent.setStatus("current")


class _MgcpLinePackageHfPersistent_Type(Integer32):
    """Custom type mgcpLinePackageHfPersistent based on Integer32"""
    defaultValue = 0

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


_MgcpLinePackageHfPersistent_Type.__name__ = "Integer32"
_MgcpLinePackageHfPersistent_Object = MibScalar
mgcpLinePackageHfPersistent = _MgcpLinePackageHfPersistent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40, 101),
    _MgcpLinePackageHfPersistent_Type()
)
mgcpLinePackageHfPersistent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpLinePackageHfPersistent.setStatus("current")


class _MgcpLinePackageHuPersistent_Type(Integer32):
    """Custom type mgcpLinePackageHuPersistent based on Integer32"""
    defaultValue = 0

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


_MgcpLinePackageHuPersistent_Type.__name__ = "Integer32"
_MgcpLinePackageHuPersistent_Object = MibScalar
mgcpLinePackageHuPersistent = _MgcpLinePackageHuPersistent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 40, 102),
    _MgcpLinePackageHuPersistent_Type()
)
mgcpLinePackageHuPersistent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpLinePackageHuPersistent.setStatus("current")
_MgcpXPPackage_ObjectIdentity = ObjectIdentity
mgcpXPPackage = _MgcpXPPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 43)
)


class _MgcpXPPackageIrDuration_Type(Unsigned32):
    """Custom type mgcpXPPackageIrDuration based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MgcpXPPackageIrDuration_Type.__name__ = "Unsigned32"
_MgcpXPPackageIrDuration_Object = MibScalar
mgcpXPPackageIrDuration = _MgcpXPPackageIrDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 43, 4),
    _MgcpXPPackageIrDuration_Type()
)
mgcpXPPackageIrDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpXPPackageIrDuration.setStatus("current")
_MgcpFirewall_ObjectIdentity = ObjectIdentity
mgcpFirewall = _MgcpFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 46)
)


class _MgcpFwKeepAliveEnable_Type(MxEnableState):
    """Custom type mgcpFwKeepAliveEnable based on MxEnableState"""
    defaultValue = 0


_MgcpFwKeepAliveEnable_Type.__name__ = "MxEnableState"
_MgcpFwKeepAliveEnable_Object = MibScalar
mgcpFwKeepAliveEnable = _MgcpFwKeepAliveEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 46, 5),
    _MgcpFwKeepAliveEnable_Type()
)
mgcpFwKeepAliveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpFwKeepAliveEnable.setStatus("current")


class _MgcpFwKeepAliveTimeout_Type(Unsigned32):
    """Custom type mgcpFwKeepAliveTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_MgcpFwKeepAliveTimeout_Type.__name__ = "Unsigned32"
_MgcpFwKeepAliveTimeout_Object = MibScalar
mgcpFwKeepAliveTimeout = _MgcpFwKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 46, 10),
    _MgcpFwKeepAliveTimeout_Type()
)
mgcpFwKeepAliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpFwKeepAliveTimeout.setStatus("current")
_MgcpStats_ObjectIdentity = ObjectIdentity
mgcpStats = _MgcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 50)
)
_MgcpStatsCurrentNumberOfActiveConnections_Type = Unsigned32
_MgcpStatsCurrentNumberOfActiveConnections_Object = MibScalar
mgcpStatsCurrentNumberOfActiveConnections = _MgcpStatsCurrentNumberOfActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 50, 1),
    _MgcpStatsCurrentNumberOfActiveConnections_Type()
)
mgcpStatsCurrentNumberOfActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcpStatsCurrentNumberOfActiveConnections.setStatus("current")
_MgcpStatsCurrentStatistics_ObjectIdentity = ObjectIdentity
mgcpStatsCurrentStatistics = _MgcpStatsCurrentStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 50, 5)
)
_MgcpStatsCurrentTotalNumberOfConnections_Type = Unsigned32
_MgcpStatsCurrentTotalNumberOfConnections_Object = MibScalar
mgcpStatsCurrentTotalNumberOfConnections = _MgcpStatsCurrentTotalNumberOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 50, 5, 1),
    _MgcpStatsCurrentTotalNumberOfConnections_Type()
)
mgcpStatsCurrentTotalNumberOfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcpStatsCurrentTotalNumberOfConnections.setStatus("current")
_MgcpStatsCurrentAvgConnectionTime_Type = Unsigned32
_MgcpStatsCurrentAvgConnectionTime_Object = MibScalar
mgcpStatsCurrentAvgConnectionTime = _MgcpStatsCurrentAvgConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 50, 5, 2),
    _MgcpStatsCurrentAvgConnectionTime_Type()
)
mgcpStatsCurrentAvgConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcpStatsCurrentAvgConnectionTime.setStatus("current")
_MgcpStatsCumulatedStatistics_ObjectIdentity = ObjectIdentity
mgcpStatsCumulatedStatistics = _MgcpStatsCumulatedStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 50, 6)
)
_MgcpStatsCumulatedTotalNumberOfConnections_Type = Unsigned32
_MgcpStatsCumulatedTotalNumberOfConnections_Object = MibScalar
mgcpStatsCumulatedTotalNumberOfConnections = _MgcpStatsCumulatedTotalNumberOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 50, 6, 1),
    _MgcpStatsCumulatedTotalNumberOfConnections_Type()
)
mgcpStatsCumulatedTotalNumberOfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcpStatsCumulatedTotalNumberOfConnections.setStatus("current")
_MgcpStatsCumulatedAvgConnectionTime_Type = Unsigned32
_MgcpStatsCumulatedAvgConnectionTime_Object = MibScalar
mgcpStatsCumulatedAvgConnectionTime = _MgcpStatsCumulatedAvgConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 1, 50, 6, 2),
    _MgcpStatsCumulatedAvgConnectionTime_Type()
)
mgcpStatsCumulatedAvgConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcpStatsCumulatedAvgConnectionTime.setStatus("current")
_MgcpConformance_ObjectIdentity = ObjectIdentity
mgcpConformance = _MgcpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 2)
)
_MgcpCompliances_ObjectIdentity = ObjectIdentity
mgcpCompliances = _MgcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 2, 1)
)
_MgcpGroups_ObjectIdentity = ObjectIdentity
mgcpGroups = _MgcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 2, 2)
)

# Managed Objects groups

mgcpBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 2, 2, 1)
)
mgcpBasicGroupVer1.setObjects(
      *(("MX-MGCP-MIB", "mgcpPort"),
        ("MX-MGCP-MIB", "mgcpDefaultDigitMap"),
        ("MX-MGCP-MIB", "mgcpDefaultPackage"),
        ("MX-MGCP-MIB", "mgcpRestartLevel"),
        ("MX-MGCP-MIB", "mgcpEndpointIdListIncludeNotStarted"),
        ("MX-MGCP-MIB", "mgcpPiggyBackingEnable"),
        ("MX-MGCP-MIB", "mgcpAddPtimeIfPresentInLCO"),
        ("MX-MGCP-MIB", "mgcpEndpointIdTerm1"),
        ("MX-MGCP-MIB", "mgcpEndpointIdTerm2"),
        ("MX-MGCP-MIB", "mgcpRetransmissionAlgorithm"),
        ("MX-MGCP-MIB", "mgcpRetransmissionInitialPeriod"),
        ("MX-MGCP-MIB", "mgcpRetransmissionMaxPeriod"),
        ("MX-MGCP-MIB", "mgcpRetransmissionDisconnectTimeout"),
        ("MX-MGCP-MIB", "mgcpRetransmissionSuspicionThreshold"),
        ("MX-MGCP-MIB", "mgcpRetransmissionSuspicionThresholdDnsQuery"),
        ("MX-MGCP-MIB", "mgcpRetransmissionDisconnectThreshold"),
        ("MX-MGCP-MIB", "mgcpRetransmissionDisconnectThresholdDnsQuery"),
        ("MX-MGCP-MIB", "mgcpRetransmissionHistoryTimeout"),
        ("MX-MGCP-MIB", "mgcpRetransmissionMaxWaitingDelay"),
        ("MX-MGCP-MIB", "mgcpRetransmissionDisconnectInitialWaitingPeriod"),
        ("MX-MGCP-MIB", "mgcpRetransmissionDisconnectMinWaitingPeriod"),
        ("MX-MGCP-MIB", "mgcpRetransmissionDisconnectMaxWaitingPeriod"))
)
if mibBuilder.loadTexts:
    mgcpBasicGroupVer1.setStatus("current")

mgcpGenericPkgGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 2, 2, 2)
)
mgcpGenericPkgGroupVer1.setObjects(
      *(("MX-MGCP-MIB", "mgcpGenericMediaPackageRbkDuration"),
        ("MX-MGCP-MIB", "mgcpGenericMediaPackageRtDuration"))
)
if mibBuilder.loadTexts:
    mgcpGenericPkgGroupVer1.setStatus("current")

mgcpDtmfPkgGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 2, 2, 3)
)
mgcpDtmfPkgGroupVer1.setObjects(
      *(("MX-MGCP-MIB", "mgcpDtmfPackageLDuration"),
        ("MX-MGCP-MIB", "mgcpDtmfPackageTCriticalDuration"),
        ("MX-MGCP-MIB", "mgcpDtmfPackageTPartialDuration"))
)
if mibBuilder.loadTexts:
    mgcpDtmfPkgGroupVer1.setStatus("current")

mgcpLinePkgGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 2, 2, 4)
)
mgcpLinePkgGroupVer1.setObjects(
      *(("MX-MGCP-MIB", "mgcpLinePackageBzDuration"),
        ("MX-MGCP-MIB", "mgcpLinePackageDlDuration"),
        ("MX-MGCP-MIB", "mgcpLinePackageMwiDuration"),
        ("MX-MGCP-MIB", "mgcpLinePackageOtDuration"),
        ("MX-MGCP-MIB", "mgcpLinePackageRoDuration"),
        ("MX-MGCP-MIB", "mgcpLinePackageRgDuration"),
        ("MX-MGCP-MIB", "mgcpLinePackageSlDuration"),
        ("MX-MGCP-MIB", "mgcpLinePackageWtDuration"))
)
if mibBuilder.loadTexts:
    mgcpLinePkgGroupVer1.setStatus("current")

mgcpStatsBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 2, 2, 5)
)
mgcpStatsBasicGroupVer1.setObjects(
      *(("MX-MGCP-MIB", "mgcpStatsCurrentNumberOfActiveConnections"),
        ("MX-MGCP-MIB", "mgcpStatsCurrentTotalNumberOfConnections"),
        ("MX-MGCP-MIB", "mgcpStatsCurrentAvgConnectionTime"),
        ("MX-MGCP-MIB", "mgcpStatsCumulatedTotalNumberOfConnections"),
        ("MX-MGCP-MIB", "mgcpStatsCumulatedAvgConnectionTime"))
)
if mibBuilder.loadTexts:
    mgcpStatsBasicGroupVer1.setStatus("current")

mgcpCallAgentGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 2, 2, 6)
)
mgcpCallAgentGroupVer1.setObjects(
      *(("MX-MGCP-MIB", "mgcpCAConfigSource"),
        ("MX-MGCP-MIB", "mgcpCAHost"),
        ("MX-MGCP-MIB", "mgcpCAPort"),
        ("MX-MGCP-MIB", "mgcpCASelectConfigSource"),
        ("MX-MGCP-MIB", "mgcpCAStaticHost"),
        ("MX-MGCP-MIB", "mgcpCAStaticPort"),
        ("MX-MGCP-MIB", "mgcpCADhcpSiteSpecificCode"))
)
if mibBuilder.loadTexts:
    mgcpCallAgentGroupVer1.setStatus("current")

mgcpXPPackageGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 2, 2, 15)
)
mgcpXPPackageGroupVer1.setObjects(
    ("MX-MGCP-MIB", "mgcpXPPackageIrDuration")
)
if mibBuilder.loadTexts:
    mgcpXPPackageGroupVer1.setStatus("current")

mgcpFirewallGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 2, 2, 20)
)
mgcpFirewallGroupVer1.setObjects(
      *(("MX-MGCP-MIB", "mgcpFwKeepAliveEnable"),
        ("MX-MGCP-MIB", "mgcpFwKeepAliveTimeout"))
)
if mibBuilder.loadTexts:
    mgcpFirewallGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mgcpResidentialGatewayBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 20, 1, 1, 2, 1, 1)
)
mgcpResidentialGatewayBasicComplVer1.setObjects(
      *(("MX-MGCP-MIB", "mgcpBasicGroupVer1"),
        ("MX-MGCP-MIB", "mgcpGenericPkgGroupVer1"),
        ("MX-MGCP-MIB", "mgcpDtmfPkgGroupVer1"),
        ("MX-MGCP-MIB", "mgcpLinePkgGroupVer1"),
        ("MX-MGCP-MIB", "mgcpStatsBasicGroupVer1"),
        ("MX-MGCP-MIB", "mgcpCallAgentGroupVer1"),
        ("MX-MGCP-MIB", "mgcpXPPackageGroupVer1"),
        ("MX-MGCP-MIB", "mgcpFirewallGroupVer1"))
)
if mibBuilder.loadTexts:
    mgcpResidentialGatewayBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-MGCP-MIB",
    **{"ipAddressStatusMgcpCallAgent": ipAddressStatusMgcpCallAgent,
       "mgcpCAConfigSource": mgcpCAConfigSource,
       "mgcpCAHost": mgcpCAHost,
       "mgcpCAPort": mgcpCAPort,
       "ipAddressConfigMgcpCallAgent": ipAddressConfigMgcpCallAgent,
       "mgcpCASelectConfigSource": mgcpCASelectConfigSource,
       "ipAddressConfigMgcpCAStatic": ipAddressConfigMgcpCAStatic,
       "mgcpCAStaticHost": mgcpCAStaticHost,
       "mgcpCAStaticPort": mgcpCAStaticPort,
       "ipAddressConfigMgcpCADhcp": ipAddressConfigMgcpCADhcp,
       "mgcpCADhcpSiteSpecificCode": mgcpCADhcpSiteSpecificCode,
       "mgcp": mgcp,
       "mgcpMIB": mgcpMIB,
       "mgcpMIBObjects": mgcpMIBObjects,
       "mgcpPort": mgcpPort,
       "mgcpDefaultDigitMap": mgcpDefaultDigitMap,
       "mgcpDefaultPackage": mgcpDefaultPackage,
       "mgcpRestartLevel": mgcpRestartLevel,
       "mgcpEndpointIdListIncludeNotStarted": mgcpEndpointIdListIncludeNotStarted,
       "mgcpPiggyBackingEnable": mgcpPiggyBackingEnable,
       "mgcpAddPtimeIfPresentInLCO": mgcpAddPtimeIfPresentInLCO,
       "mgcpEndpointId": mgcpEndpointId,
       "mgcpEndpointIfTable": mgcpEndpointIfTable,
       "mgcpEndpointIfEntry": mgcpEndpointIfEntry,
       "mgcpEndpointIdTerm1": mgcpEndpointIdTerm1,
       "mgcpEndpointIdTerm2": mgcpEndpointIdTerm2,
       "mgcpRetransmission": mgcpRetransmission,
       "mgcpRetransmissionAlgorithm": mgcpRetransmissionAlgorithm,
       "mgcpRetransmissionInitialPeriod": mgcpRetransmissionInitialPeriod,
       "mgcpRetransmissionMaxPeriod": mgcpRetransmissionMaxPeriod,
       "mgcpRetransmissionDisconnectTimeout": mgcpRetransmissionDisconnectTimeout,
       "mgcpRetransmissionSuspicionThreshold": mgcpRetransmissionSuspicionThreshold,
       "mgcpRetransmissionSuspicionThresholdDnsQuery": mgcpRetransmissionSuspicionThresholdDnsQuery,
       "mgcpRetransmissionDisconnectThreshold": mgcpRetransmissionDisconnectThreshold,
       "mgcpRetransmissionDisconnectThresholdDnsQuery": mgcpRetransmissionDisconnectThresholdDnsQuery,
       "mgcpRetransmissionHistoryTimeout": mgcpRetransmissionHistoryTimeout,
       "mgcpRetransmissionMaxWaitingDelay": mgcpRetransmissionMaxWaitingDelay,
       "mgcpRetransmissionDisconnectInitialWaitingPeriod": mgcpRetransmissionDisconnectInitialWaitingPeriod,
       "mgcpRetransmissionDisconnectMinWaitingPeriod": mgcpRetransmissionDisconnectMinWaitingPeriod,
       "mgcpRetransmissionDisconnectMaxWaitingPeriod": mgcpRetransmissionDisconnectMaxWaitingPeriod,
       "mgcpDtmfPackage": mgcpDtmfPackage,
       "mgcpDtmfPackageLDuration": mgcpDtmfPackageLDuration,
       "mgcpDtmfPackageTCriticalDuration": mgcpDtmfPackageTCriticalDuration,
       "mgcpDtmfPackageTPartialDuration": mgcpDtmfPackageTPartialDuration,
       "mgcpGenericMediaPackage": mgcpGenericMediaPackage,
       "mgcpGenericMediaPackageRbkDuration": mgcpGenericMediaPackageRbkDuration,
       "mgcpGenericMediaPackageRtDuration": mgcpGenericMediaPackageRtDuration,
       "mgcpLinePackage": mgcpLinePackage,
       "mgcpLinePackageBzDuration": mgcpLinePackageBzDuration,
       "mgcpLinePackageDlDuration": mgcpLinePackageDlDuration,
       "mgcpLinePackageMwiDuration": mgcpLinePackageMwiDuration,
       "mgcpLinePackageOtDuration": mgcpLinePackageOtDuration,
       "mgcpLinePackageRgDuration": mgcpLinePackageRgDuration,
       "mgcpLinePackageRoDuration": mgcpLinePackageRoDuration,
       "mgcpLinePackageSlDuration": mgcpLinePackageSlDuration,
       "mgcpLinePackageWtDuration": mgcpLinePackageWtDuration,
       "mgcpLinePackageOsiDuration": mgcpLinePackageOsiDuration,
       "mgcpLinePackageHdPersistent": mgcpLinePackageHdPersistent,
       "mgcpLinePackageHfPersistent": mgcpLinePackageHfPersistent,
       "mgcpLinePackageHuPersistent": mgcpLinePackageHuPersistent,
       "mgcpXPPackage": mgcpXPPackage,
       "mgcpXPPackageIrDuration": mgcpXPPackageIrDuration,
       "mgcpFirewall": mgcpFirewall,
       "mgcpFwKeepAliveEnable": mgcpFwKeepAliveEnable,
       "mgcpFwKeepAliveTimeout": mgcpFwKeepAliveTimeout,
       "mgcpStats": mgcpStats,
       "mgcpStatsCurrentNumberOfActiveConnections": mgcpStatsCurrentNumberOfActiveConnections,
       "mgcpStatsCurrentStatistics": mgcpStatsCurrentStatistics,
       "mgcpStatsCurrentTotalNumberOfConnections": mgcpStatsCurrentTotalNumberOfConnections,
       "mgcpStatsCurrentAvgConnectionTime": mgcpStatsCurrentAvgConnectionTime,
       "mgcpStatsCumulatedStatistics": mgcpStatsCumulatedStatistics,
       "mgcpStatsCumulatedTotalNumberOfConnections": mgcpStatsCumulatedTotalNumberOfConnections,
       "mgcpStatsCumulatedAvgConnectionTime": mgcpStatsCumulatedAvgConnectionTime,
       "mgcpConformance": mgcpConformance,
       "mgcpCompliances": mgcpCompliances,
       "mgcpResidentialGatewayBasicComplVer1": mgcpResidentialGatewayBasicComplVer1,
       "mgcpGroups": mgcpGroups,
       "mgcpBasicGroupVer1": mgcpBasicGroupVer1,
       "mgcpGenericPkgGroupVer1": mgcpGenericPkgGroupVer1,
       "mgcpDtmfPkgGroupVer1": mgcpDtmfPkgGroupVer1,
       "mgcpLinePkgGroupVer1": mgcpLinePkgGroupVer1,
       "mgcpStatsBasicGroupVer1": mgcpStatsBasicGroupVer1,
       "mgcpCallAgentGroupVer1": mgcpCallAgentGroupVer1,
       "mgcpXPPackageGroupVer1": mgcpXPPackageGroupVer1,
       "mgcpFirewallGroupVer1": mgcpFirewallGroupVer1}
)
