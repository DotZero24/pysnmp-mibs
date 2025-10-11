# SNMP MIB module (MOXA-NP6000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/moxa/MOXA-NP6000-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:22:12 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

np6000 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Moxa_ObjectIdentity = ObjectIdentity
moxa = _Moxa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691)
)
_Nport_ObjectIdentity = ObjectIdentity
nport = _Nport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2)
)
_SwMgmt_ObjectIdentity = ObjectIdentity
swMgmt = _SwMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1)
)
_Overview_ObjectIdentity = ObjectIdentity
overview = _Overview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1)
)
_ModelName_Type = DisplayString
_ModelName_Object = MibScalar
modelName = _ModelName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1, 1),
    _ModelName_Type()
)
modelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelName.setStatus("current")
_SerialNumber_Type = Integer32
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1, 3),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_MacAddress_Type = MacAddress
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1, 4),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_ViewLanSpeed_Type = DisplayString
_ViewLanSpeed_Object = MibScalar
viewLanSpeed = _ViewLanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1, 5),
    _ViewLanSpeed_Type()
)
viewLanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewLanSpeed.setStatus("current")
_ViewLanModuleSpeed_Type = DisplayString
_ViewLanModuleSpeed_Object = MibScalar
viewLanModuleSpeed = _ViewLanModuleSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1, 6),
    _ViewLanModuleSpeed_Type()
)
viewLanModuleSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewLanModuleSpeed.setStatus("current")
_UpTime_Type = DisplayString
_UpTime_Object = MibScalar
upTime = _UpTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1, 7),
    _UpTime_Type()
)
upTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upTime.setStatus("current")
_ModuleType_Type = DisplayString
_ModuleType_Object = MibScalar
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1, 8),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("current")
_ModuleApVersion_Type = DisplayString
_ModuleApVersion_Object = MibScalar
moduleApVersion = _ModuleApVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1, 9),
    _ModuleApVersion_Type()
)
moduleApVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleApVersion.setStatus("current")
_ViewIpv4Address_Type = DisplayString
_ViewIpv4Address_Object = MibScalar
viewIpv4Address = _ViewIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1, 10),
    _ViewIpv4Address_Type()
)
viewIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewIpv4Address.setStatus("current")
_ViewIpv6LinkLocalAddress_Type = DisplayString
_ViewIpv6LinkLocalAddress_Object = MibScalar
viewIpv6LinkLocalAddress = _ViewIpv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1, 11),
    _ViewIpv6LinkLocalAddress_Type()
)
viewIpv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewIpv6LinkLocalAddress.setStatus("current")
_ViewIpv6GlobalAddress_Type = DisplayString
_ViewIpv6GlobalAddress_Object = MibScalar
viewIpv6GlobalAddress = _ViewIpv6GlobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 1, 12),
    _ViewIpv6GlobalAddress_Type()
)
viewIpv6GlobalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewIpv6GlobalAddress.setStatus("current")
_BasicSetting_ObjectIdentity = ObjectIdentity
basicSetting = _BasicSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 2)
)
_ServerSetting_ObjectIdentity = ObjectIdentity
serverSetting = _ServerSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 2, 1)
)
_ServerName_Type = DisplayString
_ServerName_Object = MibScalar
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 2, 1, 1),
    _ServerName_Type()
)
serverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverName.setStatus("current")
_ServerLocation_Type = DisplayString
_ServerLocation_Object = MibScalar
serverLocation = _ServerLocation_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 2, 1, 2),
    _ServerLocation_Type()
)
serverLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverLocation.setStatus("current")
_TimeSetting_ObjectIdentity = ObjectIdentity
timeSetting = _TimeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 2, 2)
)
_TimeZone_Type = Integer32
_TimeZone_Object = MibScalar
timeZone = _TimeZone_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 2, 2, 1),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")


class _LocalTime_Type(DisplayString):
    """Custom type localTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_LocalTime_Type.__name__ = "DisplayString"
_LocalTime_Object = MibScalar
localTime = _LocalTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 2, 2, 2),
    _LocalTime_Type()
)
localTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTime.setStatus("current")
_TimeServer_Type = DisplayString
_TimeServer_Object = MibScalar
timeServer = _TimeServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 2, 2, 3),
    _TimeServer_Type()
)
timeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer.setStatus("current")
_NetworkSetting_ObjectIdentity = ObjectIdentity
networkSetting = _NetworkSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3)
)


class _Ipv4Configuration_Type(Integer32):
    """Custom type ipv4Configuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dhcp", 1),
          ("dhcp-BOOTP", 2),
          ("bootp", 3),
          ("pppoe", 4))
    )


_Ipv4Configuration_Type.__name__ = "Integer32"
_Ipv4Configuration_Object = MibScalar
ipv4Configuration = _Ipv4Configuration_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 1),
    _Ipv4Configuration_Type()
)
ipv4Configuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4Configuration.setStatus("current")
_Ipv4Address_Type = IpAddress
_Ipv4Address_Object = MibScalar
ipv4Address = _Ipv4Address_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 2),
    _Ipv4Address_Type()
)
ipv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4Address.setStatus("current")
_Ipv4NetMask_Type = IpAddress
_Ipv4NetMask_Object = MibScalar
ipv4NetMask = _Ipv4NetMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 3),
    _Ipv4NetMask_Type()
)
ipv4NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4NetMask.setStatus("current")
_Ipv4DefaultGateway_Type = IpAddress
_Ipv4DefaultGateway_Object = MibScalar
ipv4DefaultGateway = _Ipv4DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 4),
    _Ipv4DefaultGateway_Type()
)
ipv4DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4DefaultGateway.setStatus("current")
_Ipv4DnsServer1IpAddr_Type = IpAddress
_Ipv4DnsServer1IpAddr_Object = MibScalar
ipv4DnsServer1IpAddr = _Ipv4DnsServer1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 5),
    _Ipv4DnsServer1IpAddr_Type()
)
ipv4DnsServer1IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4DnsServer1IpAddr.setStatus("current")
_Ipv4DnsServer2IpAddr_Type = IpAddress
_Ipv4DnsServer2IpAddr_Object = MibScalar
ipv4DnsServer2IpAddr = _Ipv4DnsServer2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 6),
    _Ipv4DnsServer2IpAddr_Type()
)
ipv4DnsServer2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4DnsServer2IpAddr.setStatus("current")
_Ipv4PppoeUserAccount_Type = DisplayString
_Ipv4PppoeUserAccount_Object = MibScalar
ipv4PppoeUserAccount = _Ipv4PppoeUserAccount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 7),
    _Ipv4PppoeUserAccount_Type()
)
ipv4PppoeUserAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4PppoeUserAccount.setStatus("current")
_Ipv4PppoePassword_Type = DisplayString
_Ipv4PppoePassword_Object = MibScalar
ipv4PppoePassword = _Ipv4PppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 8),
    _Ipv4PppoePassword_Type()
)
ipv4PppoePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4PppoePassword.setStatus("current")


class _Ipv4WinsFunction_Type(Integer32):
    """Custom type ipv4WinsFunction based on Integer32"""
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


_Ipv4WinsFunction_Type.__name__ = "Integer32"
_Ipv4WinsFunction_Object = MibScalar
ipv4WinsFunction = _Ipv4WinsFunction_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 9),
    _Ipv4WinsFunction_Type()
)
ipv4WinsFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4WinsFunction.setStatus("current")
_Ipv4WinsServer_Type = IpAddress
_Ipv4WinsServer_Object = MibScalar
ipv4WinsServer = _Ipv4WinsServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 10),
    _Ipv4WinsServer_Type()
)
ipv4WinsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4WinsServer.setStatus("current")


class _Lan1Speed_Type(Integer32):
    """Custom type lan1Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto-Negation", 0),
          ("tenMbps-Half", 1),
          ("tenMbps-Full", 2),
          ("hundredMbps-Half", 3),
          ("hundredMbps-Full", 4))
    )


_Lan1Speed_Type.__name__ = "Integer32"
_Lan1Speed_Object = MibScalar
lan1Speed = _Lan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 11),
    _Lan1Speed_Type()
)
lan1Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1Speed.setStatus("current")


class _RoutingProtocol_Type(Integer32):
    """Custom type routingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rip-1", 1),
          ("rip-2", 2))
    )


_RoutingProtocol_Type.__name__ = "Integer32"
_RoutingProtocol_Object = MibScalar
routingProtocol = _RoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 12),
    _RoutingProtocol_Type()
)
routingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingProtocol.setStatus("current")


class _GratuitousArp_Type(Integer32):
    """Custom type gratuitousArp based on Integer32"""
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


_GratuitousArp_Type.__name__ = "Integer32"
_GratuitousArp_Object = MibScalar
gratuitousArp = _GratuitousArp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 13),
    _GratuitousArp_Type()
)
gratuitousArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArp.setStatus("current")
_GratuitousArpSendPeriod_Type = Integer32
_GratuitousArpSendPeriod_Object = MibScalar
gratuitousArpSendPeriod = _GratuitousArpSendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 14),
    _GratuitousArpSendPeriod_Type()
)
gratuitousArpSendPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArpSendPeriod.setStatus("current")
_ModuleSetting_ObjectIdentity = ObjectIdentity
moduleSetting = _ModuleSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15)
)
_RedundancySetting_ObjectIdentity = ObjectIdentity
redundancySetting = _RedundancySetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1)
)


class _RedundancyProtocol_Type(Integer32):
    """Custom type redundancyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("spanningTree", 1),
          ("turboRing", 2),
          ("turboRingV2", 3))
    )


_RedundancyProtocol_Type.__name__ = "Integer32"
_RedundancyProtocol_Object = MibScalar
redundancyProtocol = _RedundancyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 1),
    _RedundancyProtocol_Type()
)
redundancyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyProtocol.setStatus("current")
_SpanningTree_ObjectIdentity = ObjectIdentity
spanningTree = _SpanningTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 2)
)


class _SpanningTreeBridgePriority_Type(Integer32):
    """Custom type spanningTreeBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4096,
              8192,
              12288,
              16384,
              20480,
              24576,
              28672,
              32768,
              36864,
              40960,
              45056,
              49152,
              53248,
              57344,
              61440)
        )
    )
    namedValues = NamedValues(
        *(("priority-0", 0),
          ("priority-4096", 4096),
          ("priority-8192", 8192),
          ("priority-12288", 12288),
          ("priority-16384", 16384),
          ("priority-20480", 20480),
          ("priority-24576", 24576),
          ("priority-28672", 28672),
          ("priority-32768", 32768),
          ("priority-36864", 36864),
          ("priority-40960", 40960),
          ("priority-45056", 45056),
          ("priority-49152", 49152),
          ("priority-53248", 53248),
          ("priority-57344", 57344),
          ("priority-61440", 61440))
    )


_SpanningTreeBridgePriority_Type.__name__ = "Integer32"
_SpanningTreeBridgePriority_Object = MibScalar
spanningTreeBridgePriority = _SpanningTreeBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 2, 1),
    _SpanningTreeBridgePriority_Type()
)
spanningTreeBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeBridgePriority.setStatus("current")
_SpanningTreeHelloTime_Type = Integer32
_SpanningTreeHelloTime_Object = MibScalar
spanningTreeHelloTime = _SpanningTreeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 2, 2),
    _SpanningTreeHelloTime_Type()
)
spanningTreeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeHelloTime.setStatus("current")
_SpanningTreeForwardingDelay_Type = Integer32
_SpanningTreeForwardingDelay_Object = MibScalar
spanningTreeForwardingDelay = _SpanningTreeForwardingDelay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 2, 3),
    _SpanningTreeForwardingDelay_Type()
)
spanningTreeForwardingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeForwardingDelay.setStatus("current")
_SpanningTreeMaxAge_Type = Integer32
_SpanningTreeMaxAge_Object = MibScalar
spanningTreeMaxAge = _SpanningTreeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 2, 4),
    _SpanningTreeMaxAge_Type()
)
spanningTreeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeMaxAge.setStatus("current")
_SpanningTreePortTable_Object = MibTable
spanningTreePortTable = _SpanningTreePortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 2, 5)
)
if mibBuilder.loadTexts:
    spanningTreePortTable.setStatus("current")
_SpanningTreePortEntry_Object = MibTableRow
spanningTreePortEntry = _SpanningTreePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 2, 5, 1)
)
spanningTreePortEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "spanningTreePortIndex"),
)
if mibBuilder.loadTexts:
    spanningTreePortEntry.setStatus("current")
_SpanningTreePortIndex_Type = Integer32
_SpanningTreePortIndex_Object = MibTableColumn
spanningTreePortIndex = _SpanningTreePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 2, 5, 1, 1),
    _SpanningTreePortIndex_Type()
)
spanningTreePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreePortIndex.setStatus("current")


class _SpanningTreePortEnable_Type(Integer32):
    """Custom type spanningTreePortEnable based on Integer32"""
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


_SpanningTreePortEnable_Type.__name__ = "Integer32"
_SpanningTreePortEnable_Object = MibTableColumn
spanningTreePortEnable = _SpanningTreePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 2, 5, 1, 2),
    _SpanningTreePortEnable_Type()
)
spanningTreePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreePortEnable.setStatus("current")


class _SpanningTreePortPriority_Type(Integer32):
    """Custom type spanningTreePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              32,
              48,
              64,
              80,
              96,
              112,
              128,
              144,
              160,
              176,
              192,
              208,
              224,
              240)
        )
    )
    namedValues = NamedValues(
        *(("priority-0", 0),
          ("priority-16", 16),
          ("priority-32", 32),
          ("priority-48", 48),
          ("priority-64", 64),
          ("priority-80", 80),
          ("priority-96", 96),
          ("priority-112", 112),
          ("priority-128", 128),
          ("priority-144", 144),
          ("priority-160", 160),
          ("priority-176", 176),
          ("priority-192", 192),
          ("priority-208", 208),
          ("priority-224", 224),
          ("priority-240", 240))
    )


_SpanningTreePortPriority_Type.__name__ = "Integer32"
_SpanningTreePortPriority_Object = MibTableColumn
spanningTreePortPriority = _SpanningTreePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 2, 5, 1, 3),
    _SpanningTreePortPriority_Type()
)
spanningTreePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreePortPriority.setStatus("current")
_SpanningTreePortCost_Type = Integer32
_SpanningTreePortCost_Object = MibTableColumn
spanningTreePortCost = _SpanningTreePortCost_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 2, 5, 1, 4),
    _SpanningTreePortCost_Type()
)
spanningTreePortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreePortCost.setStatus("current")
_TurboRing_ObjectIdentity = ObjectIdentity
turboRing = _TurboRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 3)
)


class _TurboRingMasterSetup_Type(Integer32):
    """Custom type turboRingMasterSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TurboRingMasterSetup_Type.__name__ = "Integer32"
_TurboRingMasterSetup_Object = MibScalar
turboRingMasterSetup = _TurboRingMasterSetup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 3, 1),
    _TurboRingMasterSetup_Type()
)
turboRingMasterSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingMasterSetup.setStatus("current")
_TurboRingRdntPort1_Type = Integer32
_TurboRingRdntPort1_Object = MibScalar
turboRingRdntPort1 = _TurboRingRdntPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 3, 2),
    _TurboRingRdntPort1_Type()
)
turboRingRdntPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingRdntPort1.setStatus("current")
_TurboRingRdntPort2_Type = Integer32
_TurboRingRdntPort2_Object = MibScalar
turboRingRdntPort2 = _TurboRingRdntPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 3, 3),
    _TurboRingRdntPort2_Type()
)
turboRingRdntPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingRdntPort2.setStatus("current")
_TurboRingV2_ObjectIdentity = ObjectIdentity
turboRingV2 = _TurboRingV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 4)
)


class _TurboRingV2MasterSetup_Type(Integer32):
    """Custom type turboRingV2MasterSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TurboRingV2MasterSetup_Type.__name__ = "Integer32"
_TurboRingV2MasterSetup_Object = MibScalar
turboRingV2MasterSetup = _TurboRingV2MasterSetup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 4, 1),
    _TurboRingV2MasterSetup_Type()
)
turboRingV2MasterSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingV2MasterSetup.setStatus("current")
_TurboRingV2RdntPort1_Type = Integer32
_TurboRingV2RdntPort1_Object = MibScalar
turboRingV2RdntPort1 = _TurboRingV2RdntPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 4, 2),
    _TurboRingV2RdntPort1_Type()
)
turboRingV2RdntPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingV2RdntPort1.setStatus("current")
_TurboRingV2RdntPort2_Type = Integer32
_TurboRingV2RdntPort2_Object = MibScalar
turboRingV2RdntPort2 = _TurboRingV2RdntPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 1, 4, 3),
    _TurboRingV2RdntPort2_Type()
)
turboRingV2RdntPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingV2RdntPort2.setStatus("current")
_GsmGprsSetting_ObjectIdentity = ObjectIdentity
gsmGprsSetting = _GsmGprsSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2)
)


class _GsmGprsType_Type(Integer32):
    """Custom type gsmGprsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gsm", 0),
          ("gprs", 1),
          ("sms", 2))
    )


_GsmGprsType_Type.__name__ = "Integer32"
_GsmGprsType_Object = MibScalar
gsmGprsType = _GsmGprsType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 1),
    _GsmGprsType_Type()
)
gsmGprsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmGprsType.setStatus("current")
_GsmGprsPIN_Type = DisplayString
_GsmGprsPIN_Object = MibScalar
gsmGprsPIN = _GsmGprsPIN_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 2),
    _GsmGprsPIN_Type()
)
gsmGprsPIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmGprsPIN.setStatus("current")


class _GsmGprsBand_Type(Integer32):
    """Custom type gsmGprsBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("band-850-Mhz", 0),
          ("band-900-Mhz", 1),
          ("band-1800-Mhz", 2),
          ("band-1900-Mhz", 3),
          ("band-850-1900-Mhz", 4),
          ("band-900-1800-Mhz", 5),
          ("band-900-1900-Mhz", 6))
    )


_GsmGprsBand_Type.__name__ = "Integer32"
_GsmGprsBand_Object = MibScalar
gsmGprsBand = _GsmGprsBand_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 3),
    _GsmGprsBand_Type()
)
gsmGprsBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmGprsBand.setStatus("current")
_GsmSetting_ObjectIdentity = ObjectIdentity
gsmSetting = _GsmSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4)
)


class _GsmMode_Type(Integer32):
    """Custom type gsmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 0),
          ("pppd", 1))
    )


_GsmMode_Type.__name__ = "Integer32"
_GsmMode_Object = MibScalar
gsmMode = _GsmMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 1),
    _GsmMode_Type()
)
gsmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmMode.setStatus("current")
_GsmDestinationIpAddress_Type = IpAddress
_GsmDestinationIpAddress_Object = MibScalar
gsmDestinationIpAddress = _GsmDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 2),
    _GsmDestinationIpAddress_Type()
)
gsmDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmDestinationIpAddress.setStatus("current")
_GsmSourceIpAddress_Type = IpAddress
_GsmSourceIpAddress_Object = MibScalar
gsmSourceIpAddress = _GsmSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 3),
    _GsmSourceIpAddress_Type()
)
gsmSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmSourceIpAddress.setStatus("current")
_GsmIpNetmask_Type = IpAddress
_GsmIpNetmask_Object = MibScalar
gsmIpNetmask = _GsmIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 4),
    _GsmIpNetmask_Type()
)
gsmIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmIpNetmask.setStatus("current")


class _GsmTcpIpCompression_Type(Integer32):
    """Custom type gsmTcpIpCompression based on Integer32"""
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


_GsmTcpIpCompression_Type.__name__ = "Integer32"
_GsmTcpIpCompression_Object = MibScalar
gsmTcpIpCompression = _GsmTcpIpCompression_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 5),
    _GsmTcpIpCompression_Type()
)
gsmTcpIpCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmTcpIpCompression.setStatus("current")
_GsmInactivityTime_Type = Integer32
_GsmInactivityTime_Object = MibScalar
gsmInactivityTime = _GsmInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 6),
    _GsmInactivityTime_Type()
)
gsmInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmInactivityTime.setStatus("current")


class _GsmLinkQualityReport_Type(Integer32):
    """Custom type gsmLinkQualityReport based on Integer32"""
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


_GsmLinkQualityReport_Type.__name__ = "Integer32"
_GsmLinkQualityReport_Object = MibScalar
gsmLinkQualityReport = _GsmLinkQualityReport_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 7),
    _GsmLinkQualityReport_Type()
)
gsmLinkQualityReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmLinkQualityReport.setStatus("current")


class _GsmUsername_Type(DisplayString):
    """Custom type gsmUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GsmUsername_Type.__name__ = "DisplayString"
_GsmUsername_Object = MibScalar
gsmUsername = _GsmUsername_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 8),
    _GsmUsername_Type()
)
gsmUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmUsername.setStatus("current")


class _GsmPassword_Type(DisplayString):
    """Custom type gsmPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GsmPassword_Type.__name__ = "DisplayString"
_GsmPassword_Object = MibScalar
gsmPassword = _GsmPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 9),
    _GsmPassword_Type()
)
gsmPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmPassword.setStatus("current")


class _GsmAuthenticationType_Type(Integer32):
    """Custom type gsmAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("local", 1),
          ("radius", 2),
          ("radius-local", 3),
          ("local-radius", 4),
          ("tacacsPlus", 5),
          ("tacacsPlus-local", 6),
          ("local-tacacsPlus", 7))
    )


_GsmAuthenticationType_Type.__name__ = "Integer32"
_GsmAuthenticationType_Object = MibScalar
gsmAuthenticationType = _GsmAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 10),
    _GsmAuthenticationType_Type()
)
gsmAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmAuthenticationType.setStatus("current")


class _GsmTryNextAuth_Type(Integer32):
    """Custom type gsmTryNextAuth based on Integer32"""
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


_GsmTryNextAuth_Type.__name__ = "Integer32"
_GsmTryNextAuth_Object = MibScalar
gsmTryNextAuth = _GsmTryNextAuth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 11),
    _GsmTryNextAuth_Type()
)
gsmTryNextAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmTryNextAuth.setStatus("current")


class _GsmOutPhoneNumber_Type(DisplayString):
    """Custom type gsmOutPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GsmOutPhoneNumber_Type.__name__ = "DisplayString"
_GsmOutPhoneNumber_Object = MibScalar
gsmOutPhoneNumber = _GsmOutPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 12),
    _GsmOutPhoneNumber_Type()
)
gsmOutPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmOutPhoneNumber.setStatus("current")


class _GsmInitialString_Type(DisplayString):
    """Custom type gsmInitialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_GsmInitialString_Type.__name__ = "DisplayString"
_GsmInitialString_Object = MibScalar
gsmInitialString = _GsmInitialString_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 13),
    _GsmInitialString_Type()
)
gsmInitialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmInitialString.setStatus("current")


class _GsmConnectionControl_Type(Integer32):
    """Custom type gsmConnectionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOn-None", 0),
          ("periodicallyConnect-InactivityTime", 1),
          ("remoteHostFail-remoteHostRecovered", 2))
    )


_GsmConnectionControl_Type.__name__ = "Integer32"
_GsmConnectionControl_Object = MibScalar
gsmConnectionControl = _GsmConnectionControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 14),
    _GsmConnectionControl_Type()
)
gsmConnectionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmConnectionControl.setStatus("current")
_GsmConnectionInterval_Type = Integer32
_GsmConnectionInterval_Object = MibScalar
gsmConnectionInterval = _GsmConnectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 15),
    _GsmConnectionInterval_Type()
)
gsmConnectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmConnectionInterval.setStatus("current")


class _GsmPingRemoteHost_Type(DisplayString):
    """Custom type gsmPingRemoteHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_GsmPingRemoteHost_Type.__name__ = "DisplayString"
_GsmPingRemoteHost_Object = MibScalar
gsmPingRemoteHost = _GsmPingRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 16),
    _GsmPingRemoteHost_Type()
)
gsmPingRemoteHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmPingRemoteHost.setStatus("current")


class _GsmInPhoneNumber_Type(DisplayString):
    """Custom type gsmInPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GsmInPhoneNumber_Type.__name__ = "DisplayString"
_GsmInPhoneNumber_Object = MibScalar
gsmInPhoneNumber = _GsmInPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 4, 17),
    _GsmInPhoneNumber_Type()
)
gsmInPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmInPhoneNumber.setStatus("current")
_GprsSetting_ObjectIdentity = ObjectIdentity
gprsSetting = _GprsSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 5)
)


class _GprsTcpIpCompression_Type(Integer32):
    """Custom type gprsTcpIpCompression based on Integer32"""
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


_GprsTcpIpCompression_Type.__name__ = "Integer32"
_GprsTcpIpCompression_Object = MibScalar
gprsTcpIpCompression = _GprsTcpIpCompression_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 5, 1),
    _GprsTcpIpCompression_Type()
)
gprsTcpIpCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gprsTcpIpCompression.setStatus("current")
_GprsInactivityTime_Type = Integer32
_GprsInactivityTime_Object = MibScalar
gprsInactivityTime = _GprsInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 5, 2),
    _GprsInactivityTime_Type()
)
gprsInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gprsInactivityTime.setStatus("current")


class _GprsLinkQualityReport_Type(Integer32):
    """Custom type gprsLinkQualityReport based on Integer32"""
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


_GprsLinkQualityReport_Type.__name__ = "Integer32"
_GprsLinkQualityReport_Object = MibScalar
gprsLinkQualityReport = _GprsLinkQualityReport_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 5, 3),
    _GprsLinkQualityReport_Type()
)
gprsLinkQualityReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gprsLinkQualityReport.setStatus("current")


class _GprsInitialString_Type(DisplayString):
    """Custom type gprsInitialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_GprsInitialString_Type.__name__ = "DisplayString"
_GprsInitialString_Object = MibScalar
gprsInitialString = _GprsInitialString_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 5, 4),
    _GprsInitialString_Type()
)
gprsInitialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gprsInitialString.setStatus("current")


class _GprsUsername_Type(DisplayString):
    """Custom type gprsUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GprsUsername_Type.__name__ = "DisplayString"
_GprsUsername_Object = MibScalar
gprsUsername = _GprsUsername_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 5, 5),
    _GprsUsername_Type()
)
gprsUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gprsUsername.setStatus("current")


class _GprsPassword_Type(DisplayString):
    """Custom type gprsPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GprsPassword_Type.__name__ = "DisplayString"
_GprsPassword_Object = MibScalar
gprsPassword = _GprsPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 5, 6),
    _GprsPassword_Type()
)
gprsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gprsPassword.setStatus("current")


class _GprsAPN_Type(DisplayString):
    """Custom type gprsAPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_GprsAPN_Type.__name__ = "DisplayString"
_GprsAPN_Object = MibScalar
gprsAPN = _GprsAPN_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 5, 7),
    _GprsAPN_Type()
)
gprsAPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gprsAPN.setStatus("current")


class _GprsConnectionControl_Type(Integer32):
    """Custom type gprsConnectionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOn-None", 0),
          ("periodicallyConnect-InactivityTime", 1),
          ("remoteHostFail-remoteHostRecovered", 2))
    )


_GprsConnectionControl_Type.__name__ = "Integer32"
_GprsConnectionControl_Object = MibScalar
gprsConnectionControl = _GprsConnectionControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 5, 8),
    _GprsConnectionControl_Type()
)
gprsConnectionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gprsConnectionControl.setStatus("current")
_GprsConnectionInterval_Type = Integer32
_GprsConnectionInterval_Object = MibScalar
gprsConnectionInterval = _GprsConnectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 5, 9),
    _GprsConnectionInterval_Type()
)
gprsConnectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gprsConnectionInterval.setStatus("current")


class _GprsPingRemoteHost_Type(DisplayString):
    """Custom type gprsPingRemoteHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_GprsPingRemoteHost_Type.__name__ = "DisplayString"
_GprsPingRemoteHost_Object = MibScalar
gprsPingRemoteHost = _GprsPingRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 5, 10),
    _GprsPingRemoteHost_Type()
)
gprsPingRemoteHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gprsPingRemoteHost.setStatus("current")
_SmsSetting_ObjectIdentity = ObjectIdentity
smsSetting = _SmsSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 6)
)


class _SmsFormat_Type(Integer32):
    """Custom type smsFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("sms-Text-ASCII", 0)
    )


_SmsFormat_Type.__name__ = "Integer32"
_SmsFormat_Object = MibScalar
smsFormat = _SmsFormat_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 2, 6, 1),
    _SmsFormat_Type()
)
smsFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsFormat.setStatus("current")
_V92ModemSetting_ObjectIdentity = ObjectIdentity
v92ModemSetting = _V92ModemSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3)
)


class _V92ModemMode_Type(Integer32):
    """Custom type v92ModemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 0),
          ("pppd", 1))
    )


_V92ModemMode_Type.__name__ = "Integer32"
_V92ModemMode_Object = MibScalar
v92ModemMode = _V92ModemMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 1),
    _V92ModemMode_Type()
)
v92ModemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemMode.setStatus("current")
_V92ModemDestinationIpAddress_Type = IpAddress
_V92ModemDestinationIpAddress_Object = MibScalar
v92ModemDestinationIpAddress = _V92ModemDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 2),
    _V92ModemDestinationIpAddress_Type()
)
v92ModemDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemDestinationIpAddress.setStatus("current")
_V92ModemSourceIpAddress_Type = IpAddress
_V92ModemSourceIpAddress_Object = MibScalar
v92ModemSourceIpAddress = _V92ModemSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 3),
    _V92ModemSourceIpAddress_Type()
)
v92ModemSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemSourceIpAddress.setStatus("current")
_V92ModemIpNetmask_Type = IpAddress
_V92ModemIpNetmask_Object = MibScalar
v92ModemIpNetmask = _V92ModemIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 4),
    _V92ModemIpNetmask_Type()
)
v92ModemIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemIpNetmask.setStatus("current")


class _V92ModemTcpIpCompression_Type(Integer32):
    """Custom type v92ModemTcpIpCompression based on Integer32"""
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


_V92ModemTcpIpCompression_Type.__name__ = "Integer32"
_V92ModemTcpIpCompression_Object = MibScalar
v92ModemTcpIpCompression = _V92ModemTcpIpCompression_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 5),
    _V92ModemTcpIpCompression_Type()
)
v92ModemTcpIpCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemTcpIpCompression.setStatus("current")
_V92ModemInactivityTime_Type = Integer32
_V92ModemInactivityTime_Object = MibScalar
v92ModemInactivityTime = _V92ModemInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 6),
    _V92ModemInactivityTime_Type()
)
v92ModemInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemInactivityTime.setStatus("current")


class _V92ModemLinkQualityReport_Type(Integer32):
    """Custom type v92ModemLinkQualityReport based on Integer32"""
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


_V92ModemLinkQualityReport_Type.__name__ = "Integer32"
_V92ModemLinkQualityReport_Object = MibScalar
v92ModemLinkQualityReport = _V92ModemLinkQualityReport_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 7),
    _V92ModemLinkQualityReport_Type()
)
v92ModemLinkQualityReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemLinkQualityReport.setStatus("current")


class _V92ModemUsername_Type(DisplayString):
    """Custom type v92ModemUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_V92ModemUsername_Type.__name__ = "DisplayString"
_V92ModemUsername_Object = MibScalar
v92ModemUsername = _V92ModemUsername_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 8),
    _V92ModemUsername_Type()
)
v92ModemUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemUsername.setStatus("current")


class _V92ModemPassword_Type(DisplayString):
    """Custom type v92ModemPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_V92ModemPassword_Type.__name__ = "DisplayString"
_V92ModemPassword_Object = MibScalar
v92ModemPassword = _V92ModemPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 9),
    _V92ModemPassword_Type()
)
v92ModemPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemPassword.setStatus("current")


class _V92ModemIncomingPAPCheck_Type(Integer32):
    """Custom type v92ModemIncomingPAPCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("local", 1),
          ("radius", 2),
          ("radius-local", 3),
          ("local-radius", 4),
          ("tacacsPlus", 5),
          ("tacacsPlus-local", 6),
          ("local-tacacsPlus", 7))
    )


_V92ModemIncomingPAPCheck_Type.__name__ = "Integer32"
_V92ModemIncomingPAPCheck_Object = MibScalar
v92ModemIncomingPAPCheck = _V92ModemIncomingPAPCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 10),
    _V92ModemIncomingPAPCheck_Type()
)
v92ModemIncomingPAPCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemIncomingPAPCheck.setStatus("current")


class _V92ModemIncomingTryNextAuth_Type(Integer32):
    """Custom type v92ModemIncomingTryNextAuth based on Integer32"""
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


_V92ModemIncomingTryNextAuth_Type.__name__ = "Integer32"
_V92ModemIncomingTryNextAuth_Object = MibScalar
v92ModemIncomingTryNextAuth = _V92ModemIncomingTryNextAuth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 11),
    _V92ModemIncomingTryNextAuth_Type()
)
v92ModemIncomingTryNextAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemIncomingTryNextAuth.setStatus("current")


class _V92ModemPhoneNumber_Type(DisplayString):
    """Custom type v92ModemPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V92ModemPhoneNumber_Type.__name__ = "DisplayString"
_V92ModemPhoneNumber_Object = MibScalar
v92ModemPhoneNumber = _V92ModemPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 12),
    _V92ModemPhoneNumber_Type()
)
v92ModemPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemPhoneNumber.setStatus("current")


class _V92ModemInitialString_Type(DisplayString):
    """Custom type v92ModemInitialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_V92ModemInitialString_Type.__name__ = "DisplayString"
_V92ModemInitialString_Object = MibScalar
v92ModemInitialString = _V92ModemInitialString_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 13),
    _V92ModemInitialString_Type()
)
v92ModemInitialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemInitialString.setStatus("current")


class _V92ModemConnectionControl_Type(Integer32):
    """Custom type v92ModemConnectionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOn-None", 0),
          ("periodicallyConnect-InactivityTime", 1),
          ("remoteHostFail-remoteHostRecovered", 2))
    )


_V92ModemConnectionControl_Type.__name__ = "Integer32"
_V92ModemConnectionControl_Object = MibScalar
v92ModemConnectionControl = _V92ModemConnectionControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 14),
    _V92ModemConnectionControl_Type()
)
v92ModemConnectionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemConnectionControl.setStatus("current")
_V92ModemConnectionInterval_Type = Integer32
_V92ModemConnectionInterval_Object = MibScalar
v92ModemConnectionInterval = _V92ModemConnectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 15),
    _V92ModemConnectionInterval_Type()
)
v92ModemConnectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemConnectionInterval.setStatus("current")


class _V92ModemPingRemoteHost_Type(DisplayString):
    """Custom type v92ModemPingRemoteHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_V92ModemPingRemoteHost_Type.__name__ = "DisplayString"
_V92ModemPingRemoteHost_Object = MibScalar
v92ModemPingRemoteHost = _V92ModemPingRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 15, 3, 16),
    _V92ModemPingRemoteHost_Type()
)
v92ModemPingRemoteHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v92ModemPingRemoteHost.setStatus("current")


class _Ipv6Configuration_Type(Integer32):
    """Custom type ipv6Configuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("static", 1),
          ("disable", 2))
    )


_Ipv6Configuration_Type.__name__ = "Integer32"
_Ipv6Configuration_Object = MibScalar
ipv6Configuration = _Ipv6Configuration_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 16),
    _Ipv6Configuration_Type()
)
ipv6Configuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6Configuration.setStatus("current")


class _Ipv6Address_Type(DisplayString):
    """Custom type ipv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ipv6Address_Type.__name__ = "DisplayString"
_Ipv6Address_Object = MibScalar
ipv6Address = _Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 17),
    _Ipv6Address_Type()
)
ipv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6Address.setStatus("current")
_Ipv6Prefix_Type = Integer32
_Ipv6Prefix_Object = MibScalar
ipv6Prefix = _Ipv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 18),
    _Ipv6Prefix_Type()
)
ipv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6Prefix.setStatus("current")


class _Ipv6DefaultGateway_Type(DisplayString):
    """Custom type ipv6DefaultGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ipv6DefaultGateway_Type.__name__ = "DisplayString"
_Ipv6DefaultGateway_Object = MibScalar
ipv6DefaultGateway = _Ipv6DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 19),
    _Ipv6DefaultGateway_Type()
)
ipv6DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6DefaultGateway.setStatus("current")


class _Ipv6DnsServer1IpAddr_Type(DisplayString):
    """Custom type ipv6DnsServer1IpAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ipv6DnsServer1IpAddr_Type.__name__ = "DisplayString"
_Ipv6DnsServer1IpAddr_Object = MibScalar
ipv6DnsServer1IpAddr = _Ipv6DnsServer1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 20),
    _Ipv6DnsServer1IpAddr_Type()
)
ipv6DnsServer1IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6DnsServer1IpAddr.setStatus("current")


class _Ipv6DnsServer2IpAddr_Type(DisplayString):
    """Custom type ipv6DnsServer2IpAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ipv6DnsServer2IpAddr_Type.__name__ = "DisplayString"
_Ipv6DnsServer2IpAddr_Object = MibScalar
ipv6DnsServer2IpAddr = _Ipv6DnsServer2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 21),
    _Ipv6DnsServer2IpAddr_Type()
)
ipv6DnsServer2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6DnsServer2IpAddr.setStatus("current")


class _ConnectionPriority_Type(Integer32):
    """Custom type connectionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv6-first", 0),
          ("ipv4-first", 1))
    )


_ConnectionPriority_Type.__name__ = "Integer32"
_ConnectionPriority_Object = MibScalar
connectionPriority = _ConnectionPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 3, 22),
    _ConnectionPriority_Type()
)
connectionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionPriority.setStatus("current")
_PortSetting_ObjectIdentity = ObjectIdentity
portSetting = _PortSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4)
)
_OpModeSetting_ObjectIdentity = ObjectIdentity
opModeSetting = _OpModeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1)
)
_OpMode_ObjectIdentity = ObjectIdentity
opMode = _OpMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 1)
)
_OpModePortTable_Object = MibTable
opModePortTable = _OpModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    opModePortTable.setStatus("current")
_OpModePortEntry_Object = MibTableRow
opModePortEntry = _OpModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 1, 1, 1)
)
opModePortEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    opModePortEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 1, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortApplication_Type(Integer32):
    """Custom type portApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("dial-InOut", 1),
          ("terminal", 2),
          ("reverse-Terminal", 3),
          ("device-Control", 4),
          ("printer", 6),
          ("socket", 11),
          ("ethernet-Modem", 12),
          ("pair-Connection", 13))
    )


_PortApplication_Type.__name__ = "Integer32"
_PortApplication_Object = MibTableColumn
portApplication = _PortApplication_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 1, 1, 1, 2),
    _PortApplication_Type()
)
portApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portApplication.setStatus("current")


class _PortMode_Type(Integer32):
    """Custom type portMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("pair-Slave", 0),
          ("pair-Master", 1),
          ("real-Com", 2),
          ("raw-PRN", 3),
          ("slip", 4),
          ("slipd", 5),
          ("ppp", 6),
          ("disable", 7),
          ("reverse-Telnet", 8),
          ("dynamic", 9),
          ("tcp-Server", 10),
          ("lpd-PRN", 11),
          ("ethernet-Modem", 12),
          ("tcp-Client", 13),
          ("udp", 14),
          ("pppd", 15),
          ("term-ASC", 16),
          ("term-BIN", 17),
          ("reverse-SSH", 18),
          ("ssh", 19),
          ("rfc-2217", 20),
          ("reverse-Real-Com", 21))
    )


_PortMode_Type.__name__ = "Integer32"
_PortMode_Object = MibTableColumn
portMode = _PortMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 1, 1, 1, 3),
    _PortMode_Type()
)
portMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMode.setStatus("current")
_Application_ObjectIdentity = ObjectIdentity
application = _Application_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2)
)
_DeviceControl_ObjectIdentity = ObjectIdentity
deviceControl = _DeviceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1)
)
_DeviceControlTable_Object = MibTable
deviceControlTable = _DeviceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    deviceControlTable.setStatus("current")
_DeviceControlEntry_Object = MibTableRow
deviceControlEntry = _DeviceControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1)
)
deviceControlEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    deviceControlEntry.setStatus("current")
_DeviceControlTcpAliveCheck_Type = Integer32
_DeviceControlTcpAliveCheck_Object = MibTableColumn
deviceControlTcpAliveCheck = _DeviceControlTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 1),
    _DeviceControlTcpAliveCheck_Type()
)
deviceControlTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlTcpAliveCheck.setStatus("current")
_DeviceControlMaxConnection_Type = Integer32
_DeviceControlMaxConnection_Object = MibTableColumn
deviceControlMaxConnection = _DeviceControlMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 2),
    _DeviceControlMaxConnection_Type()
)
deviceControlMaxConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlMaxConnection.setStatus("current")


class _DeviceControlIgnoreJammedIp_Type(Integer32):
    """Custom type deviceControlIgnoreJammedIp based on Integer32"""
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


_DeviceControlIgnoreJammedIp_Type.__name__ = "Integer32"
_DeviceControlIgnoreJammedIp_Object = MibTableColumn
deviceControlIgnoreJammedIp = _DeviceControlIgnoreJammedIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 3),
    _DeviceControlIgnoreJammedIp_Type()
)
deviceControlIgnoreJammedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlIgnoreJammedIp.setStatus("current")


class _DeviceControlAllowDriverControl_Type(Integer32):
    """Custom type deviceControlAllowDriverControl based on Integer32"""
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


_DeviceControlAllowDriverControl_Type.__name__ = "Integer32"
_DeviceControlAllowDriverControl_Object = MibTableColumn
deviceControlAllowDriverControl = _DeviceControlAllowDriverControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 4),
    _DeviceControlAllowDriverControl_Type()
)
deviceControlAllowDriverControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlAllowDriverControl.setStatus("current")


class _DeviceControlCommandByCommandOperation_Type(Integer32):
    """Custom type deviceControlCommandByCommandOperation based on Integer32"""
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


_DeviceControlCommandByCommandOperation_Type.__name__ = "Integer32"
_DeviceControlCommandByCommandOperation_Object = MibTableColumn
deviceControlCommandByCommandOperation = _DeviceControlCommandByCommandOperation_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 5),
    _DeviceControlCommandByCommandOperation_Type()
)
deviceControlCommandByCommandOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlCommandByCommandOperation.setStatus("current")


class _DeviceControlSecure_Type(Integer32):
    """Custom type deviceControlSecure based on Integer32"""
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


_DeviceControlSecure_Type.__name__ = "Integer32"
_DeviceControlSecure_Object = MibTableColumn
deviceControlSecure = _DeviceControlSecure_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 6),
    _DeviceControlSecure_Type()
)
deviceControlSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlSecure.setStatus("current")


class _DeviceControlConnectionDownRTS_Type(Integer32):
    """Custom type deviceControlConnectionDownRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("always-high", 0),
          ("always-low", 1))
    )


_DeviceControlConnectionDownRTS_Type.__name__ = "Integer32"
_DeviceControlConnectionDownRTS_Object = MibTableColumn
deviceControlConnectionDownRTS = _DeviceControlConnectionDownRTS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 7),
    _DeviceControlConnectionDownRTS_Type()
)
deviceControlConnectionDownRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlConnectionDownRTS.setStatus("current")


class _DeviceControlConnectionDownDTR_Type(Integer32):
    """Custom type deviceControlConnectionDownDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("always-high", 0),
          ("always-low", 1))
    )


_DeviceControlConnectionDownDTR_Type.__name__ = "Integer32"
_DeviceControlConnectionDownDTR_Object = MibTableColumn
deviceControlConnectionDownDTR = _DeviceControlConnectionDownDTR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 8),
    _DeviceControlConnectionDownDTR_Type()
)
deviceControlConnectionDownDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlConnectionDownDTR.setStatus("current")
_DeviceControlResponseTimeout_Type = Integer32
_DeviceControlResponseTimeout_Object = MibTableColumn
deviceControlResponseTimeout = _DeviceControlResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 9),
    _DeviceControlResponseTimeout_Type()
)
deviceControlResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlResponseTimeout.setStatus("current")


class _DeviceControlNonRequestSerialData_Type(Integer32):
    """Custom type deviceControlNonRequestSerialData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("forward-to-last-requester", 1),
          ("forward-to-all-open-connections", 2))
    )


_DeviceControlNonRequestSerialData_Type.__name__ = "Integer32"
_DeviceControlNonRequestSerialData_Object = MibTableColumn
deviceControlNonRequestSerialData = _DeviceControlNonRequestSerialData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 10),
    _DeviceControlNonRequestSerialData_Type()
)
deviceControlNonRequestSerialData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlNonRequestSerialData.setStatus("current")
_DeviceControlTcpPort_Type = Integer32
_DeviceControlTcpPort_Object = MibTableColumn
deviceControlTcpPort = _DeviceControlTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 11),
    _DeviceControlTcpPort_Type()
)
deviceControlTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlTcpPort.setStatus("current")


class _DeviceControlDestinationAddress1_Type(DisplayString):
    """Custom type deviceControlDestinationAddress1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DeviceControlDestinationAddress1_Type.__name__ = "DisplayString"
_DeviceControlDestinationAddress1_Object = MibTableColumn
deviceControlDestinationAddress1 = _DeviceControlDestinationAddress1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 12),
    _DeviceControlDestinationAddress1_Type()
)
deviceControlDestinationAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlDestinationAddress1.setStatus("current")
_DeviceControlDestinationTcpPort1_Type = Integer32
_DeviceControlDestinationTcpPort1_Object = MibTableColumn
deviceControlDestinationTcpPort1 = _DeviceControlDestinationTcpPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 13),
    _DeviceControlDestinationTcpPort1_Type()
)
deviceControlDestinationTcpPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlDestinationTcpPort1.setStatus("current")
_DeviceControlDestinationCmdPort1_Type = Integer32
_DeviceControlDestinationCmdPort1_Object = MibTableColumn
deviceControlDestinationCmdPort1 = _DeviceControlDestinationCmdPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 14),
    _DeviceControlDestinationCmdPort1_Type()
)
deviceControlDestinationCmdPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlDestinationCmdPort1.setStatus("current")


class _DeviceControlDestinationAddress2_Type(DisplayString):
    """Custom type deviceControlDestinationAddress2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DeviceControlDestinationAddress2_Type.__name__ = "DisplayString"
_DeviceControlDestinationAddress2_Object = MibTableColumn
deviceControlDestinationAddress2 = _DeviceControlDestinationAddress2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 15),
    _DeviceControlDestinationAddress2_Type()
)
deviceControlDestinationAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlDestinationAddress2.setStatus("current")
_DeviceControlDestinationTcpPort2_Type = Integer32
_DeviceControlDestinationTcpPort2_Object = MibTableColumn
deviceControlDestinationTcpPort2 = _DeviceControlDestinationTcpPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 16),
    _DeviceControlDestinationTcpPort2_Type()
)
deviceControlDestinationTcpPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlDestinationTcpPort2.setStatus("current")
_DeviceControlDestinationCmdPort2_Type = Integer32
_DeviceControlDestinationCmdPort2_Object = MibTableColumn
deviceControlDestinationCmdPort2 = _DeviceControlDestinationCmdPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 17),
    _DeviceControlDestinationCmdPort2_Type()
)
deviceControlDestinationCmdPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlDestinationCmdPort2.setStatus("current")
_DeviceControlDesignatedLocalTcpPort1_Type = Integer32
_DeviceControlDesignatedLocalTcpPort1_Object = MibTableColumn
deviceControlDesignatedLocalTcpPort1 = _DeviceControlDesignatedLocalTcpPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 18),
    _DeviceControlDesignatedLocalTcpPort1_Type()
)
deviceControlDesignatedLocalTcpPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlDesignatedLocalTcpPort1.setStatus("current")
_DeviceControlDesignatedLocalCmdPort1_Type = Integer32
_DeviceControlDesignatedLocalCmdPort1_Object = MibTableColumn
deviceControlDesignatedLocalCmdPort1 = _DeviceControlDesignatedLocalCmdPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 19),
    _DeviceControlDesignatedLocalCmdPort1_Type()
)
deviceControlDesignatedLocalCmdPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlDesignatedLocalCmdPort1.setStatus("current")
_DeviceControlDesignatedLocalTcpPort2_Type = Integer32
_DeviceControlDesignatedLocalTcpPort2_Object = MibTableColumn
deviceControlDesignatedLocalTcpPort2 = _DeviceControlDesignatedLocalTcpPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 20),
    _DeviceControlDesignatedLocalTcpPort2_Type()
)
deviceControlDesignatedLocalTcpPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlDesignatedLocalTcpPort2.setStatus("current")
_DeviceControlDesignatedLocalCmdPort2_Type = Integer32
_DeviceControlDesignatedLocalCmdPort2_Object = MibTableColumn
deviceControlDesignatedLocalCmdPort2 = _DeviceControlDesignatedLocalCmdPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 1, 1, 1, 21),
    _DeviceControlDesignatedLocalCmdPort2_Type()
)
deviceControlDesignatedLocalCmdPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlDesignatedLocalCmdPort2.setStatus("current")
_Socket_ObjectIdentity = ObjectIdentity
socket = _Socket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2)
)
_SocketTable_Object = MibTable
socketTable = _SocketTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    socketTable.setStatus("current")
_SocketEntry_Object = MibTableRow
socketEntry = _SocketEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1)
)
socketEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    socketEntry.setStatus("current")
_SocketTcpAliveCheck_Type = Integer32
_SocketTcpAliveCheck_Object = MibTableColumn
socketTcpAliveCheck = _SocketTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 1),
    _SocketTcpAliveCheck_Type()
)
socketTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpAliveCheck.setStatus("current")
_SocketInactivityTime_Type = Integer32
_SocketInactivityTime_Object = MibTableColumn
socketInactivityTime = _SocketInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 2),
    _SocketInactivityTime_Type()
)
socketInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketInactivityTime.setStatus("current")
_SocketMaxConnection_Type = Integer32
_SocketMaxConnection_Object = MibTableColumn
socketMaxConnection = _SocketMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 3),
    _SocketMaxConnection_Type()
)
socketMaxConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketMaxConnection.setStatus("current")


class _SocketIgnoreJammedIp_Type(Integer32):
    """Custom type socketIgnoreJammedIp based on Integer32"""
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


_SocketIgnoreJammedIp_Type.__name__ = "Integer32"
_SocketIgnoreJammedIp_Object = MibTableColumn
socketIgnoreJammedIp = _SocketIgnoreJammedIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 4),
    _SocketIgnoreJammedIp_Type()
)
socketIgnoreJammedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketIgnoreJammedIp.setStatus("current")


class _SocketAllowDriverControl_Type(Integer32):
    """Custom type socketAllowDriverControl based on Integer32"""
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


_SocketAllowDriverControl_Type.__name__ = "Integer32"
_SocketAllowDriverControl_Object = MibTableColumn
socketAllowDriverControl = _SocketAllowDriverControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 5),
    _SocketAllowDriverControl_Type()
)
socketAllowDriverControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketAllowDriverControl.setStatus("current")


class _SocketCommandByCommandOperation_Type(Integer32):
    """Custom type socketCommandByCommandOperation based on Integer32"""
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


_SocketCommandByCommandOperation_Type.__name__ = "Integer32"
_SocketCommandByCommandOperation_Object = MibTableColumn
socketCommandByCommandOperation = _SocketCommandByCommandOperation_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 6),
    _SocketCommandByCommandOperation_Type()
)
socketCommandByCommandOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketCommandByCommandOperation.setStatus("current")


class _SocketSecure_Type(Integer32):
    """Custom type socketSecure based on Integer32"""
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


_SocketSecure_Type.__name__ = "Integer32"
_SocketSecure_Object = MibTableColumn
socketSecure = _SocketSecure_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 7),
    _SocketSecure_Type()
)
socketSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketSecure.setStatus("current")
_SocketTcpPort_Type = Integer32
_SocketTcpPort_Object = MibTableColumn
socketTcpPort = _SocketTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 8),
    _SocketTcpPort_Type()
)
socketTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpPort.setStatus("current")
_SocketCmdPort_Type = Integer32
_SocketCmdPort_Object = MibTableColumn
socketCmdPort = _SocketCmdPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 9),
    _SocketCmdPort_Type()
)
socketCmdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketCmdPort.setStatus("current")


class _SocketTcpServerConnectionDownRTS_Type(Integer32):
    """Custom type socketTcpServerConnectionDownRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("always-high", 0),
          ("always-low", 1))
    )


_SocketTcpServerConnectionDownRTS_Type.__name__ = "Integer32"
_SocketTcpServerConnectionDownRTS_Object = MibTableColumn
socketTcpServerConnectionDownRTS = _SocketTcpServerConnectionDownRTS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 10),
    _SocketTcpServerConnectionDownRTS_Type()
)
socketTcpServerConnectionDownRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpServerConnectionDownRTS.setStatus("current")


class _SocketTcpServerConnectionDownDTR_Type(Integer32):
    """Custom type socketTcpServerConnectionDownDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("always-high", 0),
          ("always-low", 1))
    )


_SocketTcpServerConnectionDownDTR_Type.__name__ = "Integer32"
_SocketTcpServerConnectionDownDTR_Object = MibTableColumn
socketTcpServerConnectionDownDTR = _SocketTcpServerConnectionDownDTR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 11),
    _SocketTcpServerConnectionDownDTR_Type()
)
socketTcpServerConnectionDownDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpServerConnectionDownDTR.setStatus("current")
_SocketResponseTimeout_Type = Integer32
_SocketResponseTimeout_Object = MibTableColumn
socketResponseTimeout = _SocketResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 12),
    _SocketResponseTimeout_Type()
)
socketResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketResponseTimeout.setStatus("current")


class _SocketNonRequestSerialData_Type(Integer32):
    """Custom type socketNonRequestSerialData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("forward-to-last-requester", 1),
          ("forward-to-all-open-connections", 2))
    )


_SocketNonRequestSerialData_Type.__name__ = "Integer32"
_SocketNonRequestSerialData_Object = MibTableColumn
socketNonRequestSerialData = _SocketNonRequestSerialData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 13),
    _SocketNonRequestSerialData_Type()
)
socketNonRequestSerialData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketNonRequestSerialData.setStatus("current")


class _SocketTcpClientDestinationAddress1_Type(DisplayString):
    """Custom type socketTcpClientDestinationAddress1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SocketTcpClientDestinationAddress1_Type.__name__ = "DisplayString"
_SocketTcpClientDestinationAddress1_Object = MibTableColumn
socketTcpClientDestinationAddress1 = _SocketTcpClientDestinationAddress1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 14),
    _SocketTcpClientDestinationAddress1_Type()
)
socketTcpClientDestinationAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationAddress1.setStatus("current")
_SocketTcpClientDestinationPort1_Type = Integer32
_SocketTcpClientDestinationPort1_Object = MibTableColumn
socketTcpClientDestinationPort1 = _SocketTcpClientDestinationPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 15),
    _SocketTcpClientDestinationPort1_Type()
)
socketTcpClientDestinationPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationPort1.setStatus("current")


class _SocketTcpClientDestinationAddress2_Type(DisplayString):
    """Custom type socketTcpClientDestinationAddress2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SocketTcpClientDestinationAddress2_Type.__name__ = "DisplayString"
_SocketTcpClientDestinationAddress2_Object = MibTableColumn
socketTcpClientDestinationAddress2 = _SocketTcpClientDestinationAddress2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 16),
    _SocketTcpClientDestinationAddress2_Type()
)
socketTcpClientDestinationAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationAddress2.setStatus("current")
_SocketTcpClientDestinationPort2_Type = Integer32
_SocketTcpClientDestinationPort2_Object = MibTableColumn
socketTcpClientDestinationPort2 = _SocketTcpClientDestinationPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 17),
    _SocketTcpClientDestinationPort2_Type()
)
socketTcpClientDestinationPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationPort2.setStatus("current")


class _SocketTcpClientDestinationAddress3_Type(DisplayString):
    """Custom type socketTcpClientDestinationAddress3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SocketTcpClientDestinationAddress3_Type.__name__ = "DisplayString"
_SocketTcpClientDestinationAddress3_Object = MibTableColumn
socketTcpClientDestinationAddress3 = _SocketTcpClientDestinationAddress3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 18),
    _SocketTcpClientDestinationAddress3_Type()
)
socketTcpClientDestinationAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationAddress3.setStatus("current")
_SocketTcpClientDestinationPort3_Type = Integer32
_SocketTcpClientDestinationPort3_Object = MibTableColumn
socketTcpClientDestinationPort3 = _SocketTcpClientDestinationPort3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 19),
    _SocketTcpClientDestinationPort3_Type()
)
socketTcpClientDestinationPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationPort3.setStatus("current")


class _SocketTcpClientDestinationAddress4_Type(DisplayString):
    """Custom type socketTcpClientDestinationAddress4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SocketTcpClientDestinationAddress4_Type.__name__ = "DisplayString"
_SocketTcpClientDestinationAddress4_Object = MibTableColumn
socketTcpClientDestinationAddress4 = _SocketTcpClientDestinationAddress4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 20),
    _SocketTcpClientDestinationAddress4_Type()
)
socketTcpClientDestinationAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationAddress4.setStatus("current")
_SocketTcpClientDestinationPort4_Type = Integer32
_SocketTcpClientDestinationPort4_Object = MibTableColumn
socketTcpClientDestinationPort4 = _SocketTcpClientDestinationPort4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 21),
    _SocketTcpClientDestinationPort4_Type()
)
socketTcpClientDestinationPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationPort4.setStatus("current")
_SocketTcpClientDesignatedLocalPort1_Type = Integer32
_SocketTcpClientDesignatedLocalPort1_Object = MibTableColumn
socketTcpClientDesignatedLocalPort1 = _SocketTcpClientDesignatedLocalPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 22),
    _SocketTcpClientDesignatedLocalPort1_Type()
)
socketTcpClientDesignatedLocalPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDesignatedLocalPort1.setStatus("current")
_SocketTcpClientDesignatedLocalPort2_Type = Integer32
_SocketTcpClientDesignatedLocalPort2_Object = MibTableColumn
socketTcpClientDesignatedLocalPort2 = _SocketTcpClientDesignatedLocalPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 23),
    _SocketTcpClientDesignatedLocalPort2_Type()
)
socketTcpClientDesignatedLocalPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDesignatedLocalPort2.setStatus("current")
_SocketTcpClientDesignatedLocalPort3_Type = Integer32
_SocketTcpClientDesignatedLocalPort3_Object = MibTableColumn
socketTcpClientDesignatedLocalPort3 = _SocketTcpClientDesignatedLocalPort3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 24),
    _SocketTcpClientDesignatedLocalPort3_Type()
)
socketTcpClientDesignatedLocalPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDesignatedLocalPort3.setStatus("current")
_SocketTcpClientDesignatedLocalPort4_Type = Integer32
_SocketTcpClientDesignatedLocalPort4_Object = MibTableColumn
socketTcpClientDesignatedLocalPort4 = _SocketTcpClientDesignatedLocalPort4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 25),
    _SocketTcpClientDesignatedLocalPort4_Type()
)
socketTcpClientDesignatedLocalPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDesignatedLocalPort4.setStatus("current")


class _SocketTcpClientConnectionControl_Type(Integer32):
    """Custom type socketTcpClientConnectionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(257,
              258,
              260,
              264,
              514,
              1028,
              2056)
        )
    )
    namedValues = NamedValues(
        *(("startup-None", 257),
          ("anyCharacter-None", 258),
          ("dsrOn-None", 260),
          ("dcdOn-None", 264),
          ("anyCharacter-InactivityTime", 514),
          ("dsrOn-DSR-Off", 1028),
          ("dcdOn-DCD-Off", 2056))
    )


_SocketTcpClientConnectionControl_Type.__name__ = "Integer32"
_SocketTcpClientConnectionControl_Object = MibTableColumn
socketTcpClientConnectionControl = _SocketTcpClientConnectionControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 26),
    _SocketTcpClientConnectionControl_Type()
)
socketTcpClientConnectionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientConnectionControl.setStatus("current")


class _SocketUdpDestinationAddress1Begin_Type(DisplayString):
    """Custom type socketUdpDestinationAddress1Begin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SocketUdpDestinationAddress1Begin_Type.__name__ = "DisplayString"
_SocketUdpDestinationAddress1Begin_Object = MibTableColumn
socketUdpDestinationAddress1Begin = _SocketUdpDestinationAddress1Begin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 27),
    _SocketUdpDestinationAddress1Begin_Type()
)
socketUdpDestinationAddress1Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress1Begin.setStatus("current")


class _SocketUdpDestinationAddress1End_Type(DisplayString):
    """Custom type socketUdpDestinationAddress1End based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SocketUdpDestinationAddress1End_Type.__name__ = "DisplayString"
_SocketUdpDestinationAddress1End_Object = MibTableColumn
socketUdpDestinationAddress1End = _SocketUdpDestinationAddress1End_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 28),
    _SocketUdpDestinationAddress1End_Type()
)
socketUdpDestinationAddress1End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress1End.setStatus("current")
_SocketUdpDestinationPort1_Type = Integer32
_SocketUdpDestinationPort1_Object = MibTableColumn
socketUdpDestinationPort1 = _SocketUdpDestinationPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 29),
    _SocketUdpDestinationPort1_Type()
)
socketUdpDestinationPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationPort1.setStatus("current")


class _SocketUdpDestinationAddress2Begin_Type(DisplayString):
    """Custom type socketUdpDestinationAddress2Begin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SocketUdpDestinationAddress2Begin_Type.__name__ = "DisplayString"
_SocketUdpDestinationAddress2Begin_Object = MibTableColumn
socketUdpDestinationAddress2Begin = _SocketUdpDestinationAddress2Begin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 30),
    _SocketUdpDestinationAddress2Begin_Type()
)
socketUdpDestinationAddress2Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress2Begin.setStatus("current")


class _SocketUdpDestinationAddress2End_Type(DisplayString):
    """Custom type socketUdpDestinationAddress2End based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SocketUdpDestinationAddress2End_Type.__name__ = "DisplayString"
_SocketUdpDestinationAddress2End_Object = MibTableColumn
socketUdpDestinationAddress2End = _SocketUdpDestinationAddress2End_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 31),
    _SocketUdpDestinationAddress2End_Type()
)
socketUdpDestinationAddress2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress2End.setStatus("current")
_SocketUdpDestinationPort2_Type = Integer32
_SocketUdpDestinationPort2_Object = MibTableColumn
socketUdpDestinationPort2 = _SocketUdpDestinationPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 32),
    _SocketUdpDestinationPort2_Type()
)
socketUdpDestinationPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationPort2.setStatus("current")


class _SocketUdpDestinationAddress3Begin_Type(DisplayString):
    """Custom type socketUdpDestinationAddress3Begin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SocketUdpDestinationAddress3Begin_Type.__name__ = "DisplayString"
_SocketUdpDestinationAddress3Begin_Object = MibTableColumn
socketUdpDestinationAddress3Begin = _SocketUdpDestinationAddress3Begin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 33),
    _SocketUdpDestinationAddress3Begin_Type()
)
socketUdpDestinationAddress3Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress3Begin.setStatus("current")


class _SocketUdpDestinationAddress3End_Type(DisplayString):
    """Custom type socketUdpDestinationAddress3End based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SocketUdpDestinationAddress3End_Type.__name__ = "DisplayString"
_SocketUdpDestinationAddress3End_Object = MibTableColumn
socketUdpDestinationAddress3End = _SocketUdpDestinationAddress3End_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 34),
    _SocketUdpDestinationAddress3End_Type()
)
socketUdpDestinationAddress3End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress3End.setStatus("current")
_SocketUdpDestinationPort3_Type = Integer32
_SocketUdpDestinationPort3_Object = MibTableColumn
socketUdpDestinationPort3 = _SocketUdpDestinationPort3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 35),
    _SocketUdpDestinationPort3_Type()
)
socketUdpDestinationPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationPort3.setStatus("current")


class _SocketUdpDestinationAddress4Begin_Type(DisplayString):
    """Custom type socketUdpDestinationAddress4Begin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SocketUdpDestinationAddress4Begin_Type.__name__ = "DisplayString"
_SocketUdpDestinationAddress4Begin_Object = MibTableColumn
socketUdpDestinationAddress4Begin = _SocketUdpDestinationAddress4Begin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 36),
    _SocketUdpDestinationAddress4Begin_Type()
)
socketUdpDestinationAddress4Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress4Begin.setStatus("current")


class _SocketUdpDestinationAddress4End_Type(DisplayString):
    """Custom type socketUdpDestinationAddress4End based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SocketUdpDestinationAddress4End_Type.__name__ = "DisplayString"
_SocketUdpDestinationAddress4End_Object = MibTableColumn
socketUdpDestinationAddress4End = _SocketUdpDestinationAddress4End_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 37),
    _SocketUdpDestinationAddress4End_Type()
)
socketUdpDestinationAddress4End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress4End.setStatus("current")
_SocketUdpDestinationPort4_Type = Integer32
_SocketUdpDestinationPort4_Object = MibTableColumn
socketUdpDestinationPort4 = _SocketUdpDestinationPort4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 38),
    _SocketUdpDestinationPort4_Type()
)
socketUdpDestinationPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationPort4.setStatus("current")
_SocketUdpLocalListenPort_Type = Integer32
_SocketUdpLocalListenPort_Object = MibTableColumn
socketUdpLocalListenPort = _SocketUdpLocalListenPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 39),
    _SocketUdpLocalListenPort_Type()
)
socketUdpLocalListenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpLocalListenPort.setStatus("current")


class _SocketUDPDynamicDst_Type(Integer32):
    """Custom type socketUDPDynamicDst based on Integer32"""
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


_SocketUDPDynamicDst_Type.__name__ = "Integer32"
_SocketUDPDynamicDst_Object = MibTableColumn
socketUDPDynamicDst = _SocketUDPDynamicDst_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 40),
    _SocketUDPDynamicDst_Type()
)
socketUDPDynamicDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUDPDynamicDst.setStatus("current")
_SocketUDPDynamicDstTimeout_Type = Integer32
_SocketUDPDynamicDstTimeout_Object = MibTableColumn
socketUDPDynamicDstTimeout = _SocketUDPDynamicDstTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 2, 1, 1, 41),
    _SocketUDPDynamicDstTimeout_Type()
)
socketUDPDynamicDstTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUDPDynamicDstTimeout.setStatus("current")
_PairConnection_ObjectIdentity = ObjectIdentity
pairConnection = _PairConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 3)
)
_PairConnectionTable_Object = MibTable
pairConnectionTable = _PairConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pairConnectionTable.setStatus("current")
_PairConnectionEntry_Object = MibTableRow
pairConnectionEntry = _PairConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 3, 1, 1)
)
pairConnectionEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    pairConnectionEntry.setStatus("current")
_PairConnectionTcpAliveCheck_Type = Integer32
_PairConnectionTcpAliveCheck_Object = MibTableColumn
pairConnectionTcpAliveCheck = _PairConnectionTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 3, 1, 1, 1),
    _PairConnectionTcpAliveCheck_Type()
)
pairConnectionTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pairConnectionTcpAliveCheck.setStatus("current")


class _PairConnectionSecure_Type(Integer32):
    """Custom type pairConnectionSecure based on Integer32"""
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


_PairConnectionSecure_Type.__name__ = "Integer32"
_PairConnectionSecure_Object = MibTableColumn
pairConnectionSecure = _PairConnectionSecure_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 3, 1, 1, 2),
    _PairConnectionSecure_Type()
)
pairConnectionSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pairConnectionSecure.setStatus("current")


class _PairConnectionDestinationAddress_Type(DisplayString):
    """Custom type pairConnectionDestinationAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_PairConnectionDestinationAddress_Type.__name__ = "DisplayString"
_PairConnectionDestinationAddress_Object = MibTableColumn
pairConnectionDestinationAddress = _PairConnectionDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 3, 1, 1, 3),
    _PairConnectionDestinationAddress_Type()
)
pairConnectionDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pairConnectionDestinationAddress.setStatus("current")
_PairConnectionDestinationPort_Type = Integer32
_PairConnectionDestinationPort_Object = MibTableColumn
pairConnectionDestinationPort = _PairConnectionDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 3, 1, 1, 4),
    _PairConnectionDestinationPort_Type()
)
pairConnectionDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pairConnectionDestinationPort.setStatus("current")
_PairConnectionTcpPort_Type = Integer32
_PairConnectionTcpPort_Object = MibTableColumn
pairConnectionTcpPort = _PairConnectionTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 3, 1, 1, 5),
    _PairConnectionTcpPort_Type()
)
pairConnectionTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pairConnectionTcpPort.setStatus("current")
_EthernetModem_ObjectIdentity = ObjectIdentity
ethernetModem = _EthernetModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 4)
)
_EthernetModemTable_Object = MibTable
ethernetModemTable = _EthernetModemTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ethernetModemTable.setStatus("current")
_EthernetModemEntry_Object = MibTableRow
ethernetModemEntry = _EthernetModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 4, 1, 1)
)
ethernetModemEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    ethernetModemEntry.setStatus("current")
_EthernetModemTcpAliveCheck_Type = Integer32
_EthernetModemTcpAliveCheck_Object = MibTableColumn
ethernetModemTcpAliveCheck = _EthernetModemTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 4, 1, 1, 1),
    _EthernetModemTcpAliveCheck_Type()
)
ethernetModemTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetModemTcpAliveCheck.setStatus("current")
_EthernetModemTcpPort_Type = Integer32
_EthernetModemTcpPort_Object = MibTableColumn
ethernetModemTcpPort = _EthernetModemTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 4, 1, 1, 2),
    _EthernetModemTcpPort_Type()
)
ethernetModemTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetModemTcpPort.setStatus("current")
_Terminal_ObjectIdentity = ObjectIdentity
terminal = _Terminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5)
)
_TerminalTable_Object = MibTable
terminalTable = _TerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    terminalTable.setStatus("current")
_TerminalEntry_Object = MibTableRow
terminalEntry = _TerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1)
)
terminalEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    terminalEntry.setStatus("current")
_TerminalTcpAliveCheck_Type = Integer32
_TerminalTcpAliveCheck_Object = MibTableColumn
terminalTcpAliveCheck = _TerminalTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 1),
    _TerminalTcpAliveCheck_Type()
)
terminalTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalTcpAliveCheck.setStatus("current")
_TerminalInactivityTime_Type = Integer32
_TerminalInactivityTime_Object = MibTableColumn
terminalInactivityTime = _TerminalInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 2),
    _TerminalInactivityTime_Type()
)
terminalInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalInactivityTime.setStatus("current")


class _TerminalAutoLinkProtocol_Type(Integer32):
    """Custom type terminalAutoLinkProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("telnet", 1),
          ("rlogin", 2))
    )


_TerminalAutoLinkProtocol_Type.__name__ = "Integer32"
_TerminalAutoLinkProtocol_Object = MibTableColumn
terminalAutoLinkProtocol = _TerminalAutoLinkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 3),
    _TerminalAutoLinkProtocol_Type()
)
terminalAutoLinkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalAutoLinkProtocol.setStatus("current")


class _TerminalPrimaryHostAddress_Type(DisplayString):
    """Custom type terminalPrimaryHostAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TerminalPrimaryHostAddress_Type.__name__ = "DisplayString"
_TerminalPrimaryHostAddress_Object = MibTableColumn
terminalPrimaryHostAddress = _TerminalPrimaryHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 4),
    _TerminalPrimaryHostAddress_Type()
)
terminalPrimaryHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalPrimaryHostAddress.setStatus("current")


class _TerminalSecondHostAddress_Type(DisplayString):
    """Custom type terminalSecondHostAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TerminalSecondHostAddress_Type.__name__ = "DisplayString"
_TerminalSecondHostAddress_Object = MibTableColumn
terminalSecondHostAddress = _TerminalSecondHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 5),
    _TerminalSecondHostAddress_Type()
)
terminalSecondHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalSecondHostAddress.setStatus("current")
_TerminalTelnetTcpPort_Type = Integer32
_TerminalTelnetTcpPort_Object = MibTableColumn
terminalTelnetTcpPort = _TerminalTelnetTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 6),
    _TerminalTelnetTcpPort_Type()
)
terminalTelnetTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalTelnetTcpPort.setStatus("current")
_TerminalSshTcpPort_Type = Integer32
_TerminalSshTcpPort_Object = MibTableColumn
terminalSshTcpPort = _TerminalSshTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 7),
    _TerminalSshTcpPort_Type()
)
terminalSshTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalSshTcpPort.setStatus("current")


class _TerminalType_Type(DisplayString):
    """Custom type terminalType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TerminalType_Type.__name__ = "DisplayString"
_TerminalType_Object = MibTableColumn
terminalType = _TerminalType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 8),
    _TerminalType_Type()
)
terminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalType.setStatus("current")


class _TerminalMaxSessions_Type(Integer32):
    """Custom type terminalMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TerminalMaxSessions_Type.__name__ = "Integer32"
_TerminalMaxSessions_Object = MibTableColumn
terminalMaxSessions = _TerminalMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 9),
    _TerminalMaxSessions_Type()
)
terminalMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalMaxSessions.setStatus("current")


class _TerminalChangeSession_Type(DisplayString):
    """Custom type terminalChangeSession based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TerminalChangeSession_Type.__name__ = "DisplayString"
_TerminalChangeSession_Object = MibTableColumn
terminalChangeSession = _TerminalChangeSession_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 10),
    _TerminalChangeSession_Type()
)
terminalChangeSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalChangeSession.setStatus("current")


class _TerminalQuit_Type(DisplayString):
    """Custom type terminalQuit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TerminalQuit_Type.__name__ = "DisplayString"
_TerminalQuit_Object = MibTableColumn
terminalQuit = _TerminalQuit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 11),
    _TerminalQuit_Type()
)
terminalQuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalQuit.setStatus("current")


class _TerminalBreak_Type(DisplayString):
    """Custom type terminalBreak based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TerminalBreak_Type.__name__ = "DisplayString"
_TerminalBreak_Object = MibTableColumn
terminalBreak = _TerminalBreak_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 12),
    _TerminalBreak_Type()
)
terminalBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalBreak.setStatus("current")


class _TerminalInterrupt_Type(DisplayString):
    """Custom type terminalInterrupt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TerminalInterrupt_Type.__name__ = "DisplayString"
_TerminalInterrupt_Object = MibTableColumn
terminalInterrupt = _TerminalInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 13),
    _TerminalInterrupt_Type()
)
terminalInterrupt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalInterrupt.setStatus("current")


class _TerminalAuthenticationType_Type(Integer32):
    """Custom type terminalAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("local", 1),
          ("radius", 2),
          ("radius-local", 3),
          ("local-radius", 4),
          ("tacacsPlus", 5),
          ("tacacsPlus-local", 6),
          ("local-tacacsPlus", 7))
    )


_TerminalAuthenticationType_Type.__name__ = "Integer32"
_TerminalAuthenticationType_Object = MibTableColumn
terminalAuthenticationType = _TerminalAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 14),
    _TerminalAuthenticationType_Type()
)
terminalAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalAuthenticationType.setStatus("current")


class _TerminalTryNextAuth_Type(Integer32):
    """Custom type terminalTryNextAuth based on Integer32"""
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


_TerminalTryNextAuth_Type.__name__ = "Integer32"
_TerminalTryNextAuth_Object = MibTableColumn
terminalTryNextAuth = _TerminalTryNextAuth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 15),
    _TerminalTryNextAuth_Type()
)
terminalTryNextAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalTryNextAuth.setStatus("current")


class _TerminalAutoLoginPrompt_Type(DisplayString):
    """Custom type terminalAutoLoginPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TerminalAutoLoginPrompt_Type.__name__ = "DisplayString"
_TerminalAutoLoginPrompt_Object = MibTableColumn
terminalAutoLoginPrompt = _TerminalAutoLoginPrompt_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 16),
    _TerminalAutoLoginPrompt_Type()
)
terminalAutoLoginPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalAutoLoginPrompt.setStatus("current")


class _TerminalPasswordPrompt_Type(DisplayString):
    """Custom type terminalPasswordPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TerminalPasswordPrompt_Type.__name__ = "DisplayString"
_TerminalPasswordPrompt_Object = MibTableColumn
terminalPasswordPrompt = _TerminalPasswordPrompt_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 17),
    _TerminalPasswordPrompt_Type()
)
terminalPasswordPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalPasswordPrompt.setStatus("current")


class _TerminalLoginUserName_Type(DisplayString):
    """Custom type terminalLoginUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TerminalLoginUserName_Type.__name__ = "DisplayString"
_TerminalLoginUserName_Object = MibTableColumn
terminalLoginUserName = _TerminalLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 18),
    _TerminalLoginUserName_Type()
)
terminalLoginUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalLoginUserName.setStatus("current")


class _TerminalLoginPassword_Type(DisplayString):
    """Custom type terminalLoginPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TerminalLoginPassword_Type.__name__ = "DisplayString"
_TerminalLoginPassword_Object = MibTableColumn
terminalLoginPassword = _TerminalLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 5, 1, 1, 19),
    _TerminalLoginPassword_Type()
)
terminalLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalLoginPassword.setStatus("current")
_ReverseTerminal_ObjectIdentity = ObjectIdentity
reverseTerminal = _ReverseTerminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 6)
)
_ReverseTerminalTable_Object = MibTable
reverseTerminalTable = _ReverseTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    reverseTerminalTable.setStatus("current")
_ReverseTerminalEntry_Object = MibTableRow
reverseTerminalEntry = _ReverseTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 6, 1, 1)
)
reverseTerminalEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    reverseTerminalEntry.setStatus("current")
_ReverseTerminalTcpAliveCheck_Type = Integer32
_ReverseTerminalTcpAliveCheck_Object = MibTableColumn
reverseTerminalTcpAliveCheck = _ReverseTerminalTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 6, 1, 1, 1),
    _ReverseTerminalTcpAliveCheck_Type()
)
reverseTerminalTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalTcpAliveCheck.setStatus("current")
_ReverseTerminalInactivityTime_Type = Integer32
_ReverseTerminalInactivityTime_Object = MibTableColumn
reverseTerminalInactivityTime = _ReverseTerminalInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 6, 1, 1, 2),
    _ReverseTerminalInactivityTime_Type()
)
reverseTerminalInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalInactivityTime.setStatus("current")
_ReverseTerminalTcpPort_Type = Integer32
_ReverseTerminalTcpPort_Object = MibTableColumn
reverseTerminalTcpPort = _ReverseTerminalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 6, 1, 1, 3),
    _ReverseTerminalTcpPort_Type()
)
reverseTerminalTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalTcpPort.setStatus("current")


class _ReverseTerminalAuthenticationType_Type(Integer32):
    """Custom type reverseTerminalAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("local", 1),
          ("radius", 2),
          ("radius-local", 3),
          ("local-radius", 4),
          ("tacacsPlus", 5),
          ("tacacsPlus-local", 6),
          ("local-tacacsPlus", 7))
    )


_ReverseTerminalAuthenticationType_Type.__name__ = "Integer32"
_ReverseTerminalAuthenticationType_Object = MibTableColumn
reverseTerminalAuthenticationType = _ReverseTerminalAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 6, 1, 1, 4),
    _ReverseTerminalAuthenticationType_Type()
)
reverseTerminalAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalAuthenticationType.setStatus("current")


class _ReverseTerminalTryNextAuth_Type(Integer32):
    """Custom type reverseTerminalTryNextAuth based on Integer32"""
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


_ReverseTerminalTryNextAuth_Type.__name__ = "Integer32"
_ReverseTerminalTryNextAuth_Object = MibTableColumn
reverseTerminalTryNextAuth = _ReverseTerminalTryNextAuth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 6, 1, 1, 5),
    _ReverseTerminalTryNextAuth_Type()
)
reverseTerminalTryNextAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalTryNextAuth.setStatus("current")


class _ReverseTerminalMapKeys_Type(Integer32):
    """Custom type reverseTerminalMapKeys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cr-lf", 0),
          ("cr", 1),
          ("lf", 2))
    )


_ReverseTerminalMapKeys_Type.__name__ = "Integer32"
_ReverseTerminalMapKeys_Object = MibTableColumn
reverseTerminalMapKeys = _ReverseTerminalMapKeys_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 6, 1, 1, 6),
    _ReverseTerminalMapKeys_Type()
)
reverseTerminalMapKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalMapKeys.setStatus("current")
_Printer_ObjectIdentity = ObjectIdentity
printer = _Printer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 7)
)
_PrinterTable_Object = MibTable
printerTable = _PrinterTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    printerTable.setStatus("current")
_PrinterEntry_Object = MibTableRow
printerEntry = _PrinterEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 7, 1, 1)
)
printerEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    printerEntry.setStatus("current")
_PrinterTcpAliveCheck_Type = Integer32
_PrinterTcpAliveCheck_Object = MibTableColumn
printerTcpAliveCheck = _PrinterTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 7, 1, 1, 1),
    _PrinterTcpAliveCheck_Type()
)
printerTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    printerTcpAliveCheck.setStatus("current")
_PrinterTcpPort_Type = Integer32
_PrinterTcpPort_Object = MibTableColumn
printerTcpPort = _PrinterTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 7, 1, 1, 2),
    _PrinterTcpPort_Type()
)
printerTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printerTcpPort.setStatus("current")


class _PrinterGroup_Type(Integer32):
    """Custom type printerGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("group1", 0),
          ("group2", 1),
          ("group3", 2),
          ("group4", 3),
          ("group5", 4),
          ("group6", 5),
          ("group7", 6),
          ("group8", 7),
          ("group9", 8),
          ("group10", 9),
          ("group11", 10),
          ("group12", 11),
          ("group13", 12),
          ("group14", 13),
          ("group15", 14),
          ("group16", 15),
          ("group17", 16),
          ("group18", 17),
          ("group19", 18),
          ("group20", 19),
          ("group21", 20),
          ("group22", 21),
          ("group23", 22),
          ("group24", 23),
          ("group25", 24),
          ("group26", 25),
          ("group27", 26),
          ("group28", 27),
          ("group29", 28),
          ("group30", 29),
          ("group31", 30),
          ("group32", 31))
    )


_PrinterGroup_Type.__name__ = "Integer32"
_PrinterGroup_Object = MibTableColumn
printerGroup = _PrinterGroup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 7, 1, 1, 3),
    _PrinterGroup_Type()
)
printerGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    printerGroup.setStatus("current")


class _PrinterQueueNameRaw_Type(DisplayString):
    """Custom type printerQueueNameRaw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PrinterQueueNameRaw_Type.__name__ = "DisplayString"
_PrinterQueueNameRaw_Object = MibTableColumn
printerQueueNameRaw = _PrinterQueueNameRaw_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 7, 1, 1, 4),
    _PrinterQueueNameRaw_Type()
)
printerQueueNameRaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    printerQueueNameRaw.setStatus("current")


class _PrinterQueueNameASCII_Type(DisplayString):
    """Custom type printerQueueNameASCII based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PrinterQueueNameASCII_Type.__name__ = "DisplayString"
_PrinterQueueNameASCII_Object = MibTableColumn
printerQueueNameASCII = _PrinterQueueNameASCII_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 7, 1, 1, 5),
    _PrinterQueueNameASCII_Type()
)
printerQueueNameASCII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    printerQueueNameASCII.setStatus("current")


class _PrinterAppendFormFeed_Type(Integer32):
    """Custom type printerAppendFormFeed based on Integer32"""
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


_PrinterAppendFormFeed_Type.__name__ = "Integer32"
_PrinterAppendFormFeed_Object = MibTableColumn
printerAppendFormFeed = _PrinterAppendFormFeed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 7, 1, 1, 6),
    _PrinterAppendFormFeed_Type()
)
printerAppendFormFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    printerAppendFormFeed.setStatus("current")
_Dial_ObjectIdentity = ObjectIdentity
dial = _Dial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8)
)
_DialTable_Object = MibTable
dialTable = _DialTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    dialTable.setStatus("current")
_DialEntry_Object = MibTableRow
dialEntry = _DialEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1)
)
dialEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    dialEntry.setStatus("current")


class _DialTERMBINMode_Type(Integer32):
    """Custom type dialTERMBINMode based on Integer32"""
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


_DialTERMBINMode_Type.__name__ = "Integer32"
_DialTERMBINMode_Object = MibTableColumn
dialTERMBINMode = _DialTERMBINMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 1),
    _DialTERMBINMode_Type()
)
dialTERMBINMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialTERMBINMode.setStatus("current")


class _DialPPPDMode_Type(Integer32):
    """Custom type dialPPPDMode based on Integer32"""
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


_DialPPPDMode_Type.__name__ = "Integer32"
_DialPPPDMode_Object = MibTableColumn
dialPPPDMode = _DialPPPDMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 2),
    _DialPPPDMode_Type()
)
dialPPPDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPPPDMode.setStatus("current")


class _DialSLIPDMode_Type(Integer32):
    """Custom type dialSLIPDMode based on Integer32"""
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


_DialSLIPDMode_Type.__name__ = "Integer32"
_DialSLIPDMode_Object = MibTableColumn
dialSLIPDMode = _DialSLIPDMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 3),
    _DialSLIPDMode_Type()
)
dialSLIPDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialSLIPDMode.setStatus("current")


class _DialAuthType_Type(Integer32):
    """Custom type dialAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("local", 1),
          ("radius", 2),
          ("radius-local", 3),
          ("local-radius", 4),
          ("tacacsPlus", 5),
          ("tacacsPlus-local", 6),
          ("local-tacacsPlus", 7))
    )


_DialAuthType_Type.__name__ = "Integer32"
_DialAuthType_Object = MibTableColumn
dialAuthType = _DialAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 4),
    _DialAuthType_Type()
)
dialAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialAuthType.setStatus("current")


class _DialTryNextAuth_Type(Integer32):
    """Custom type dialTryNextAuth based on Integer32"""
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


_DialTryNextAuth_Type.__name__ = "Integer32"
_DialTryNextAuth_Object = MibTableColumn
dialTryNextAuth = _DialTryNextAuth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 5),
    _DialTryNextAuth_Type()
)
dialTryNextAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialTryNextAuth.setStatus("current")


class _DialDisconnectBy_Type(Integer32):
    """Custom type dialDisconnectBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dcd-off", 2),
          ("dsr-off", 4))
    )


_DialDisconnectBy_Type.__name__ = "Integer32"
_DialDisconnectBy_Object = MibTableColumn
dialDisconnectBy = _DialDisconnectBy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 6),
    _DialDisconnectBy_Type()
)
dialDisconnectBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialDisconnectBy.setStatus("current")
_DialDestinationIpAddress_Type = IpAddress
_DialDestinationIpAddress_Object = MibTableColumn
dialDestinationIpAddress = _DialDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 7),
    _DialDestinationIpAddress_Type()
)
dialDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialDestinationIpAddress.setStatus("current")
_DialSourceIpAddress_Type = IpAddress
_DialSourceIpAddress_Object = MibTableColumn
dialSourceIpAddress = _DialSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 8),
    _DialSourceIpAddress_Type()
)
dialSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialSourceIpAddress.setStatus("current")
_DialIpNetmask_Type = IpAddress
_DialIpNetmask_Object = MibTableColumn
dialIpNetmask = _DialIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 9),
    _DialIpNetmask_Type()
)
dialIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialIpNetmask.setStatus("current")


class _DialTcpIpCompression_Type(Integer32):
    """Custom type dialTcpIpCompression based on Integer32"""
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


_DialTcpIpCompression_Type.__name__ = "Integer32"
_DialTcpIpCompression_Object = MibTableColumn
dialTcpIpCompression = _DialTcpIpCompression_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 10),
    _DialTcpIpCompression_Type()
)
dialTcpIpCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialTcpIpCompression.setStatus("current")
_DialInactivityTime_Type = Integer32
_DialInactivityTime_Object = MibTableColumn
dialInactivityTime = _DialInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 11),
    _DialInactivityTime_Type()
)
dialInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialInactivityTime.setStatus("current")


class _DialLinkQualityReport_Type(Integer32):
    """Custom type dialLinkQualityReport based on Integer32"""
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


_DialLinkQualityReport_Type.__name__ = "Integer32"
_DialLinkQualityReport_Object = MibTableColumn
dialLinkQualityReport = _DialLinkQualityReport_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 12),
    _DialLinkQualityReport_Type()
)
dialLinkQualityReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialLinkQualityReport.setStatus("current")


class _DialUsername_Type(DisplayString):
    """Custom type dialUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DialUsername_Type.__name__ = "DisplayString"
_DialUsername_Object = MibTableColumn
dialUsername = _DialUsername_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 13),
    _DialUsername_Type()
)
dialUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialUsername.setStatus("current")


class _DialPassword_Type(DisplayString):
    """Custom type dialPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DialPassword_Type.__name__ = "DisplayString"
_DialPassword_Object = MibTableColumn
dialPassword = _DialPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 14),
    _DialPassword_Type()
)
dialPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPassword.setStatus("current")


class _DialIncomingPAPCheck_Type(Integer32):
    """Custom type dialIncomingPAPCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("local", 1),
          ("radius", 2),
          ("radius-local", 3),
          ("local-radius", 4),
          ("tacacsPlus", 5),
          ("tacacsPlus-local", 6),
          ("local-tacacsPlus", 7))
    )


_DialIncomingPAPCheck_Type.__name__ = "Integer32"
_DialIncomingPAPCheck_Object = MibTableColumn
dialIncomingPAPCheck = _DialIncomingPAPCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 15),
    _DialIncomingPAPCheck_Type()
)
dialIncomingPAPCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialIncomingPAPCheck.setStatus("current")


class _DialIncomingTryNextAuth_Type(Integer32):
    """Custom type dialIncomingTryNextAuth based on Integer32"""
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


_DialIncomingTryNextAuth_Type.__name__ = "Integer32"
_DialIncomingTryNextAuth_Object = MibTableColumn
dialIncomingTryNextAuth = _DialIncomingTryNextAuth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 2, 8, 1, 1, 16),
    _DialIncomingTryNextAuth_Type()
)
dialIncomingTryNextAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialIncomingTryNextAuth.setStatus("current")
_DataPacking_ObjectIdentity = ObjectIdentity
dataPacking = _DataPacking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 3)
)
_DataPackingPortTable_Object = MibTable
dataPackingPortTable = _DataPackingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dataPackingPortTable.setStatus("current")
_DataPackingPortEntry_Object = MibTableRow
dataPackingPortEntry = _DataPackingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 3, 1, 1)
)
dataPackingPortEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    dataPackingPortEntry.setStatus("current")
_PortPacketLength_Type = Integer32
_PortPacketLength_Object = MibTableColumn
portPacketLength = _PortPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 3, 1, 1, 1),
    _PortPacketLength_Type()
)
portPacketLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPacketLength.setStatus("current")


class _PortDelimiter1Enable_Type(Integer32):
    """Custom type portDelimiter1Enable based on Integer32"""
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


_PortDelimiter1Enable_Type.__name__ = "Integer32"
_PortDelimiter1Enable_Object = MibTableColumn
portDelimiter1Enable = _PortDelimiter1Enable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 3, 1, 1, 2),
    _PortDelimiter1Enable_Type()
)
portDelimiter1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDelimiter1Enable.setStatus("current")


class _PortDelimiter1_Type(DisplayString):
    """Custom type portDelimiter1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_PortDelimiter1_Type.__name__ = "DisplayString"
_PortDelimiter1_Object = MibTableColumn
portDelimiter1 = _PortDelimiter1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 3, 1, 1, 3),
    _PortDelimiter1_Type()
)
portDelimiter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDelimiter1.setStatus("current")


class _PortDelimiter2Enable_Type(Integer32):
    """Custom type portDelimiter2Enable based on Integer32"""
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


_PortDelimiter2Enable_Type.__name__ = "Integer32"
_PortDelimiter2Enable_Object = MibTableColumn
portDelimiter2Enable = _PortDelimiter2Enable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 3, 1, 1, 4),
    _PortDelimiter2Enable_Type()
)
portDelimiter2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDelimiter2Enable.setStatus("current")


class _PortDelimiter2_Type(DisplayString):
    """Custom type portDelimiter2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_PortDelimiter2_Type.__name__ = "DisplayString"
_PortDelimiter2_Object = MibTableColumn
portDelimiter2 = _PortDelimiter2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 3, 1, 1, 5),
    _PortDelimiter2_Type()
)
portDelimiter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDelimiter2.setStatus("current")


class _PortDelimiterProcess_Type(Integer32):
    """Custom type portDelimiterProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("delimiterAddOne", 2),
          ("delimiterAddTwo", 4),
          ("stripDelimiter", 8))
    )


_PortDelimiterProcess_Type.__name__ = "Integer32"
_PortDelimiterProcess_Object = MibTableColumn
portDelimiterProcess = _PortDelimiterProcess_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 3, 1, 1, 6),
    _PortDelimiterProcess_Type()
)
portDelimiterProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDelimiterProcess.setStatus("current")
_PortForceTransmit_Type = Integer32
_PortForceTransmit_Object = MibTableColumn
portForceTransmit = _PortForceTransmit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 1, 3, 1, 1, 7),
    _PortForceTransmit_Type()
)
portForceTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForceTransmit.setStatus("current")
_ComParamSetting_ObjectIdentity = ObjectIdentity
comParamSetting = _ComParamSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2)
)
_ComParamPortTable_Object = MibTable
comParamPortTable = _ComParamPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    comParamPortTable.setStatus("current")
_ComParamPortEntry_Object = MibTableRow
comParamPortEntry = _ComParamPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1, 1)
)
comParamPortEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    comParamPortEntry.setStatus("current")


class _PortAlias_Type(DisplayString):
    """Custom type portAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortAlias_Type.__name__ = "DisplayString"
_PortAlias_Object = MibTableColumn
portAlias = _PortAlias_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1, 1, 1),
    _PortAlias_Type()
)
portAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAlias.setStatus("current")


class _PortInterface_Type(Integer32):
    """Custom type portInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs-232", 0),
          ("rs-422", 1),
          ("rs-485-2-wire", 2),
          ("rs-485-4-wire", 3))
    )


_PortInterface_Type.__name__ = "Integer32"
_PortInterface_Object = MibTableColumn
portInterface = _PortInterface_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1, 1, 2),
    _PortInterface_Type()
)
portInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInterface.setStatus("current")


class _PortBaudRate_Type(Integer32):
    """Custom type portBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("b50", 0),
          ("b75", 1),
          ("b110", 2),
          ("b134", 3),
          ("b150", 4),
          ("b300", 5),
          ("b600", 6),
          ("b1200", 7),
          ("b1800", 8),
          ("b2400", 9),
          ("b4800", 10),
          ("b7200", 11),
          ("b9600", 12),
          ("b19200", 13),
          ("b38400", 14),
          ("b57600", 15),
          ("b115200", 16),
          ("b230400", 17),
          ("b460800", 18),
          ("b921600", 19))
    )


_PortBaudRate_Type.__name__ = "Integer32"
_PortBaudRate_Object = MibTableColumn
portBaudRate = _PortBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1, 1, 3),
    _PortBaudRate_Type()
)
portBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaudRate.setStatus("current")


class _PortBaudRateManual_Type(Integer32):
    """Custom type portBaudRateManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 921600),
    )


_PortBaudRateManual_Type.__name__ = "Integer32"
_PortBaudRateManual_Object = MibTableColumn
portBaudRateManual = _PortBaudRateManual_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1, 1, 4),
    _PortBaudRateManual_Type()
)
portBaudRateManual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaudRateManual.setStatus("current")


class _PortDataBits_Type(Integer32):
    """Custom type portDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bits-5", 0),
          ("bits-6", 1),
          ("bits-7", 2),
          ("bits-8", 3))
    )


_PortDataBits_Type.__name__ = "Integer32"
_PortDataBits_Object = MibTableColumn
portDataBits = _PortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1, 1, 5),
    _PortDataBits_Type()
)
portDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDataBits.setStatus("current")


class _PortStopBits_Type(Integer32):
    """Custom type portStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bits-1", 0),
          ("bits-1dot5", 1),
          ("bits-2", 2))
    )


_PortStopBits_Type.__name__ = "Integer32"
_PortStopBits_Object = MibTableColumn
portStopBits = _PortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1, 1, 6),
    _PortStopBits_Type()
)
portStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portStopBits.setStatus("current")


class _PortParity_Type(Integer32):
    """Custom type portParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("odd", 1),
          ("even", 2),
          ("mark", 3),
          ("space", 4))
    )


_PortParity_Type.__name__ = "Integer32"
_PortParity_Object = MibTableColumn
portParity = _PortParity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1, 1, 7),
    _PortParity_Type()
)
portParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portParity.setStatus("current")


class _PortFlowControl_Type(Integer32):
    """Custom type portFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rts-cts", 1),
          ("xon-xoff", 2),
          ("dtr-dsr", 3),
          ("rts-toggle", 4))
    )


_PortFlowControl_Type.__name__ = "Integer32"
_PortFlowControl_Object = MibTableColumn
portFlowControl = _PortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1, 1, 8),
    _PortFlowControl_Type()
)
portFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlowControl.setStatus("current")


class _PortFIFO_Type(Integer32):
    """Custom type portFIFO based on Integer32"""
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


_PortFIFO_Type.__name__ = "Integer32"
_PortFIFO_Object = MibTableColumn
portFIFO = _PortFIFO_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1, 1, 9),
    _PortFIFO_Type()
)
portFIFO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFIFO.setStatus("current")
_PortOnDelay_Type = Integer32
_PortOnDelay_Object = MibTableColumn
portOnDelay = _PortOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1, 1, 10),
    _PortOnDelay_Type()
)
portOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOnDelay.setStatus("current")
_PortOffDelay_Type = Integer32
_PortOffDelay_Object = MibTableColumn
portOffDelay = _PortOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 2, 1, 1, 11),
    _PortOffDelay_Type()
)
portOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOffDelay.setStatus("current")
_DataBuffering_ObjectIdentity = ObjectIdentity
dataBuffering = _DataBuffering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 3)
)
_DataBufferingPortTable_Object = MibTable
dataBufferingPortTable = _DataBufferingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    dataBufferingPortTable.setStatus("current")
_DataBufferingPortEntry_Object = MibTableRow
dataBufferingPortEntry = _DataBufferingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 3, 1, 1)
)
dataBufferingPortEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    dataBufferingPortEntry.setStatus("current")


class _PortBufferingEnable_Type(Integer32):
    """Custom type portBufferingEnable based on Integer32"""
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


_PortBufferingEnable_Type.__name__ = "Integer32"
_PortBufferingEnable_Object = MibTableColumn
portBufferingEnable = _PortBufferingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 3, 1, 1, 1),
    _PortBufferingEnable_Type()
)
portBufferingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBufferingEnable.setStatus("current")


class _PortBufferingLocation_Type(Integer32):
    """Custom type portBufferingLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("memory", 0),
          ("sdCard", 1))
    )


_PortBufferingLocation_Type.__name__ = "Integer32"
_PortBufferingLocation_Object = MibTableColumn
portBufferingLocation = _PortBufferingLocation_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 3, 1, 1, 2),
    _PortBufferingLocation_Type()
)
portBufferingLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBufferingLocation.setStatus("current")
_PortBufferingSDFileSize_Type = Integer32
_PortBufferingSDFileSize_Object = MibTableColumn
portBufferingSDFileSize = _PortBufferingSDFileSize_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 3, 1, 1, 3),
    _PortBufferingSDFileSize_Type()
)
portBufferingSDFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBufferingSDFileSize.setStatus("current")


class _PortSerialDataLoggingEnable_Type(Integer32):
    """Custom type portSerialDataLoggingEnable based on Integer32"""
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


_PortSerialDataLoggingEnable_Type.__name__ = "Integer32"
_PortSerialDataLoggingEnable_Object = MibTableColumn
portSerialDataLoggingEnable = _PortSerialDataLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 3, 1, 1, 4),
    _PortSerialDataLoggingEnable_Type()
)
portSerialDataLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSerialDataLoggingEnable.setStatus("current")
_ModemSettings_ObjectIdentity = ObjectIdentity
modemSettings = _ModemSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 4)
)
_ModemSettingsPortTable_Object = MibTable
modemSettingsPortTable = _ModemSettingsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    modemSettingsPortTable.setStatus("current")
_ModemSettingsPortEntry_Object = MibTableRow
modemSettingsPortEntry = _ModemSettingsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 4, 1, 1)
)
modemSettingsPortEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    modemSettingsPortEntry.setStatus("current")


class _PortEnableModem_Type(Integer32):
    """Custom type portEnableModem based on Integer32"""
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


_PortEnableModem_Type.__name__ = "Integer32"
_PortEnableModem_Object = MibTableColumn
portEnableModem = _PortEnableModem_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 4, 1, 1, 1),
    _PortEnableModem_Type()
)
portEnableModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnableModem.setStatus("current")


class _PortInitialString_Type(DisplayString):
    """Custom type portInitialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_PortInitialString_Type.__name__ = "DisplayString"
_PortInitialString_Object = MibTableColumn
portInitialString = _PortInitialString_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 4, 1, 1, 2),
    _PortInitialString_Type()
)
portInitialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInitialString.setStatus("current")


class _PortDialUp_Type(DisplayString):
    """Custom type portDialUp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PortDialUp_Type.__name__ = "DisplayString"
_PortDialUp_Object = MibTableColumn
portDialUp = _PortDialUp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 4, 1, 1, 3),
    _PortDialUp_Type()
)
portDialUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDialUp.setStatus("current")


class _PortPhoneNumber_Type(DisplayString):
    """Custom type portPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortPhoneNumber_Type.__name__ = "DisplayString"
_PortPhoneNumber_Object = MibTableColumn
portPhoneNumber = _PortPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 4, 1, 1, 4),
    _PortPhoneNumber_Type()
)
portPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhoneNumber.setStatus("current")
_CipherSettings_ObjectIdentity = ObjectIdentity
cipherSettings = _CipherSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 5)
)
_CipherSettingsPortTable_Object = MibTable
cipherSettingsPortTable = _CipherSettingsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    cipherSettingsPortTable.setStatus("current")
_CipherSettingsPortEntry_Object = MibTableRow
cipherSettingsPortEntry = _CipherSettingsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 5, 1, 1)
)
cipherSettingsPortEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    cipherSettingsPortEntry.setStatus("current")


class _SslCipherSort_Type(DisplayString):
    """Custom type sslCipherSort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(53, 53),
    )
    fixed_length = 53


_SslCipherSort_Type.__name__ = "DisplayString"
_SslCipherSort_Object = MibTableColumn
sslCipherSort = _SslCipherSort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 5, 1, 1, 1),
    _SslCipherSort_Type()
)
sslCipherSort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCipherSort.setStatus("current")


class _SshCipherSort_Type(DisplayString):
    """Custom type sshCipherSort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_SshCipherSort_Type.__name__ = "DisplayString"
_SshCipherSort_Object = MibTableColumn
sshCipherSort = _SshCipherSort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 5, 1, 1, 2),
    _SshCipherSort_Type()
)
sshCipherSort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshCipherSort.setStatus("current")
_WelcomeMessage_ObjectIdentity = ObjectIdentity
welcomeMessage = _WelcomeMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 6)
)


class _PortEnableWelcomeMessage_Type(Integer32):
    """Custom type portEnableWelcomeMessage based on Integer32"""
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


_PortEnableWelcomeMessage_Type.__name__ = "Integer32"
_PortEnableWelcomeMessage_Object = MibScalar
portEnableWelcomeMessage = _PortEnableWelcomeMessage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 6, 1),
    _PortEnableWelcomeMessage_Type()
)
portEnableWelcomeMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnableWelcomeMessage.setStatus("current")


class _PortMessage_Type(DisplayString):
    """Custom type portMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1280),
    )


_PortMessage_Type.__name__ = "DisplayString"
_PortMessage_Object = MibScalar
portMessage = _PortMessage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 4, 6, 2),
    _PortMessage_Type()
)
portMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMessage.setStatus("current")
_SysManagement_ObjectIdentity = ObjectIdentity
sysManagement = _SysManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5)
)
_MiscNetworkSettings_ObjectIdentity = ObjectIdentity
miscNetworkSettings = _MiscNetworkSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1)
)
_AccessibleIp_ObjectIdentity = ObjectIdentity
accessibleIp = _AccessibleIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 1)
)


class _EnableAccessibleIpList_Type(Integer32):
    """Custom type enableAccessibleIpList based on Integer32"""
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


_EnableAccessibleIpList_Type.__name__ = "Integer32"
_EnableAccessibleIpList_Object = MibScalar
enableAccessibleIpList = _EnableAccessibleIpList_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 1, 1),
    _EnableAccessibleIpList_Type()
)
enableAccessibleIpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAccessibleIpList.setStatus("current")
_AccessibleIpListTable_Object = MibTable
accessibleIpListTable = _AccessibleIpListTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    accessibleIpListTable.setStatus("current")
_AccessibleIpListEntry_Object = MibTableRow
accessibleIpListEntry = _AccessibleIpListEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 1, 2, 1)
)
accessibleIpListEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "accessibleIpListIndex"),
)
if mibBuilder.loadTexts:
    accessibleIpListEntry.setStatus("current")
_AccessibleIpListIndex_Type = Integer32
_AccessibleIpListIndex_Object = MibTableColumn
accessibleIpListIndex = _AccessibleIpListIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 1, 2, 1, 1),
    _AccessibleIpListIndex_Type()
)
accessibleIpListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessibleIpListIndex.setStatus("current")


class _ActiveAccessibleIpList_Type(Integer32):
    """Custom type activeAccessibleIpList based on Integer32"""
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


_ActiveAccessibleIpList_Type.__name__ = "Integer32"
_ActiveAccessibleIpList_Object = MibTableColumn
activeAccessibleIpList = _ActiveAccessibleIpList_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 1, 2, 1, 2),
    _ActiveAccessibleIpList_Type()
)
activeAccessibleIpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeAccessibleIpList.setStatus("current")


class _AccessibleIpListAddress_Type(DisplayString):
    """Custom type accessibleIpListAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AccessibleIpListAddress_Type.__name__ = "DisplayString"
_AccessibleIpListAddress_Object = MibTableColumn
accessibleIpListAddress = _AccessibleIpListAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 1, 2, 1, 3),
    _AccessibleIpListAddress_Type()
)
accessibleIpListAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessibleIpListAddress.setStatus("current")


class _AccessibleIpListNetmask_Type(DisplayString):
    """Custom type accessibleIpListNetmask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AccessibleIpListNetmask_Type.__name__ = "DisplayString"
_AccessibleIpListNetmask_Object = MibTableColumn
accessibleIpListNetmask = _AccessibleIpListNetmask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 1, 2, 1, 4),
    _AccessibleIpListNetmask_Type()
)
accessibleIpListNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessibleIpListNetmask.setStatus("current")
_SnmpAgentSettings_ObjectIdentity = ObjectIdentity
snmpAgentSettings = _SnmpAgentSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 2)
)


class _SnmpEnable_Type(Integer32):
    """Custom type snmpEnable based on Integer32"""
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


_SnmpEnable_Type.__name__ = "Integer32"
_SnmpEnable_Object = MibScalar
snmpEnable = _SnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 2, 1),
    _SnmpEnable_Type()
)
snmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEnable.setStatus("current")


class _SnmpContactName_Type(DisplayString):
    """Custom type snmpContactName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SnmpContactName_Type.__name__ = "DisplayString"
_SnmpContactName_Object = MibScalar
snmpContactName = _SnmpContactName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 2, 2),
    _SnmpContactName_Type()
)
snmpContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpContactName.setStatus("current")


class _SnmpLocation_Type(DisplayString):
    """Custom type snmpLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SnmpLocation_Type.__name__ = "DisplayString"
_SnmpLocation_Object = MibScalar
snmpLocation = _SnmpLocation_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 2, 3),
    _SnmpLocation_Type()
)
snmpLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLocation.setStatus("current")
_DDNS_ObjectIdentity = ObjectIdentity
dDNS = _DDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 3)
)


class _DDNSEnable_Type(Integer32):
    """Custom type dDNSEnable based on Integer32"""
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


_DDNSEnable_Type.__name__ = "Integer32"
_DDNSEnable_Object = MibScalar
dDNSEnable = _DDNSEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 3, 1),
    _DDNSEnable_Type()
)
dDNSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDNSEnable.setStatus("current")


class _DDNSServerAddress_Type(Integer32):
    """Custom type dDNSServerAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("dynDns-org", 0)
    )


_DDNSServerAddress_Type.__name__ = "Integer32"
_DDNSServerAddress_Object = MibScalar
dDNSServerAddress = _DDNSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 3, 2),
    _DDNSServerAddress_Type()
)
dDNSServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDNSServerAddress.setStatus("current")


class _DDNSHostName_Type(DisplayString):
    """Custom type dDNSHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_DDNSHostName_Type.__name__ = "DisplayString"
_DDNSHostName_Object = MibScalar
dDNSHostName = _DDNSHostName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 3, 3),
    _DDNSHostName_Type()
)
dDNSHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDNSHostName.setStatus("current")


class _DDNSUserName_Type(DisplayString):
    """Custom type dDNSUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_DDNSUserName_Type.__name__ = "DisplayString"
_DDNSUserName_Object = MibScalar
dDNSUserName = _DDNSUserName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 3, 4),
    _DDNSUserName_Type()
)
dDNSUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDNSUserName.setStatus("current")


class _DDNSPassword_Type(DisplayString):
    """Custom type dDNSPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_DDNSPassword_Type.__name__ = "DisplayString"
_DDNSPassword_Object = MibScalar
dDNSPassword = _DDNSPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 3, 5),
    _DDNSPassword_Type()
)
dDNSPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDNSPassword.setStatus("current")
_HostTable_ObjectIdentity = ObjectIdentity
hostTable = _HostTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 4)
)
_HostTableTable_Object = MibTable
hostTableTable = _HostTableTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hostTableTable.setStatus("current")
_HostTableEntry_Object = MibTableRow
hostTableEntry = _HostTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 4, 1, 1)
)
hostTableEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "hostTableIndex"),
)
if mibBuilder.loadTexts:
    hostTableEntry.setStatus("current")
_HostTableIndex_Type = Integer32
_HostTableIndex_Object = MibTableColumn
hostTableIndex = _HostTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 4, 1, 1, 1),
    _HostTableIndex_Type()
)
hostTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTableIndex.setStatus("current")


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 4, 1, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostName.setStatus("current")


class _HostIpAddress_Type(DisplayString):
    """Custom type hostIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HostIpAddress_Type.__name__ = "DisplayString"
_HostIpAddress_Object = MibTableColumn
hostIpAddress = _HostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 4, 1, 1, 3),
    _HostIpAddress_Type()
)
hostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIpAddress.setStatus("current")
_RouteTable_ObjectIdentity = ObjectIdentity
routeTable = _RouteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 5)
)
_RouteTableTable_Object = MibTable
routeTableTable = _RouteTableTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 5, 1)
)
if mibBuilder.loadTexts:
    routeTableTable.setStatus("current")
_RouteTableEntry_Object = MibTableRow
routeTableEntry = _RouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 5, 1, 1)
)
routeTableEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "routeTableIndex"),
)
if mibBuilder.loadTexts:
    routeTableEntry.setStatus("current")
_RouteTableIndex_Type = Integer32
_RouteTableIndex_Object = MibTableColumn
routeTableIndex = _RouteTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 5, 1, 1, 1),
    _RouteTableIndex_Type()
)
routeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeTableIndex.setStatus("current")
_GatewayRouteTable_Type = IpAddress
_GatewayRouteTable_Object = MibTableColumn
gatewayRouteTable = _GatewayRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 5, 1, 1, 2),
    _GatewayRouteTable_Type()
)
gatewayRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayRouteTable.setStatus("current")
_DestinationRouteTable_Type = IpAddress
_DestinationRouteTable_Object = MibTableColumn
destinationRouteTable = _DestinationRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 5, 1, 1, 3),
    _DestinationRouteTable_Type()
)
destinationRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationRouteTable.setStatus("current")
_NetmaskRouteTable_Type = IpAddress
_NetmaskRouteTable_Object = MibTableColumn
netmaskRouteTable = _NetmaskRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 5, 1, 1, 4),
    _NetmaskRouteTable_Type()
)
netmaskRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netmaskRouteTable.setStatus("current")
_MetricRouteTable_Type = Integer32
_MetricRouteTable_Object = MibTableColumn
metricRouteTable = _MetricRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 5, 1, 1, 5),
    _MetricRouteTable_Type()
)
metricRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metricRouteTable.setStatus("current")


class _InterfaceRouteTable_Type(Integer32):
    """Custom type interfaceRouteTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              256)
        )
    )
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31),
          ("lan", 256))
    )


_InterfaceRouteTable_Type.__name__ = "Integer32"
_InterfaceRouteTable_Object = MibTableColumn
interfaceRouteTable = _InterfaceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 5, 1, 1, 6),
    _InterfaceRouteTable_Type()
)
interfaceRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceRouteTable.setStatus("current")
_UserTable_ObjectIdentity = ObjectIdentity
userTable = _UserTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 6)
)
_UserTableTable_Object = MibTable
userTableTable = _UserTableTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 6, 1)
)
if mibBuilder.loadTexts:
    userTableTable.setStatus("current")
_UserTableEntry_Object = MibTableRow
userTableEntry = _UserTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 6, 1, 1)
)
userTableEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "userTableIndex"),
)
if mibBuilder.loadTexts:
    userTableEntry.setStatus("current")
_UserTableIndex_Type = Integer32
_UserTableIndex_Object = MibTableColumn
userTableIndex = _UserTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 6, 1, 1, 1),
    _UserTableIndex_Type()
)
userTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userTableIndex.setStatus("current")


class _UserNameUserTable_Type(DisplayString):
    """Custom type userNameUserTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UserNameUserTable_Type.__name__ = "DisplayString"
_UserNameUserTable_Object = MibTableColumn
userNameUserTable = _UserNameUserTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 6, 1, 1, 2),
    _UserNameUserTable_Type()
)
userNameUserTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userNameUserTable.setStatus("current")


class _PasswordUserTable_Type(DisplayString):
    """Custom type passwordUserTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PasswordUserTable_Type.__name__ = "DisplayString"
_PasswordUserTable_Object = MibTableColumn
passwordUserTable = _PasswordUserTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 6, 1, 1, 3),
    _PasswordUserTable_Type()
)
passwordUserTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passwordUserTable.setStatus("current")


class _PhoneNumberUserTable_Type(DisplayString):
    """Custom type phoneNumberUserTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PhoneNumberUserTable_Type.__name__ = "DisplayString"
_PhoneNumberUserTable_Object = MibTableColumn
phoneNumberUserTable = _PhoneNumberUserTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 6, 1, 1, 4),
    _PhoneNumberUserTable_Type()
)
phoneNumberUserTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phoneNumberUserTable.setStatus("current")
_AuthenticationServer_ObjectIdentity = ObjectIdentity
authenticationServer = _AuthenticationServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 7)
)


class _RadiusServerIp_Type(DisplayString):
    """Custom type radiusServerIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RadiusServerIp_Type.__name__ = "DisplayString"
_RadiusServerIp_Object = MibScalar
radiusServerIp = _RadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 7, 1),
    _RadiusServerIp_Type()
)
radiusServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerIp.setStatus("current")


class _RadiusKey_Type(DisplayString):
    """Custom type radiusKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RadiusKey_Type.__name__ = "DisplayString"
_RadiusKey_Object = MibScalar
radiusKey = _RadiusKey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 7, 2),
    _RadiusKey_Type()
)
radiusKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusKey.setStatus("current")


class _UdpPortAuthenticationServer_Type(Integer32):
    """Custom type udpPortAuthenticationServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1645,
              1812)
        )
    )
    namedValues = NamedValues(
        *(("port1645", 1645),
          ("port1812", 1812))
    )


_UdpPortAuthenticationServer_Type.__name__ = "Integer32"
_UdpPortAuthenticationServer_Object = MibScalar
udpPortAuthenticationServer = _UdpPortAuthenticationServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 7, 3),
    _UdpPortAuthenticationServer_Type()
)
udpPortAuthenticationServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpPortAuthenticationServer.setStatus("current")


class _RadiusAccounting_Type(Integer32):
    """Custom type radiusAccounting based on Integer32"""
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


_RadiusAccounting_Type.__name__ = "Integer32"
_RadiusAccounting_Object = MibScalar
radiusAccounting = _RadiusAccounting_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 7, 4),
    _RadiusAccounting_Type()
)
radiusAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccounting.setStatus("current")


class _TacacsPlusServerIp_Type(DisplayString):
    """Custom type tacacsPlusServerIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TacacsPlusServerIp_Type.__name__ = "DisplayString"
_TacacsPlusServerIp_Object = MibScalar
tacacsPlusServerIp = _TacacsPlusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 7, 5),
    _TacacsPlusServerIp_Type()
)
tacacsPlusServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusServerIp.setStatus("current")


class _TacacsPlusSecret_Type(DisplayString):
    """Custom type tacacsPlusSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TacacsPlusSecret_Type.__name__ = "DisplayString"
_TacacsPlusSecret_Object = MibScalar
tacacsPlusSecret = _TacacsPlusSecret_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 7, 6),
    _TacacsPlusSecret_Type()
)
tacacsPlusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusSecret.setStatus("current")


class _TacacsPlusAccounting_Type(Integer32):
    """Custom type tacacsPlusAccounting based on Integer32"""
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


_TacacsPlusAccounting_Type.__name__ = "Integer32"
_TacacsPlusAccounting_Object = MibScalar
tacacsPlusAccounting = _TacacsPlusAccounting_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 7, 7),
    _TacacsPlusAccounting_Type()
)
tacacsPlusAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusAccounting.setStatus("current")
_SysLogSettings_ObjectIdentity = ObjectIdentity
sysLogSettings = _SysLogSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 8)
)


class _SysLocalLog_Type(Integer32):
    """Custom type sysLocalLog based on Integer32"""
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


_SysLocalLog_Type.__name__ = "Integer32"
_SysLocalLog_Object = MibScalar
sysLocalLog = _SysLocalLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 8, 1),
    _SysLocalLog_Type()
)
sysLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocalLog.setStatus("current")


class _NetworkLocalLog_Type(Integer32):
    """Custom type networkLocalLog based on Integer32"""
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


_NetworkLocalLog_Type.__name__ = "Integer32"
_NetworkLocalLog_Object = MibScalar
networkLocalLog = _NetworkLocalLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 8, 2),
    _NetworkLocalLog_Type()
)
networkLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLocalLog.setStatus("current")


class _ConfigLocalLog_Type(Integer32):
    """Custom type configLocalLog based on Integer32"""
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


_ConfigLocalLog_Type.__name__ = "Integer32"
_ConfigLocalLog_Object = MibScalar
configLocalLog = _ConfigLocalLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 8, 3),
    _ConfigLocalLog_Type()
)
configLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLocalLog.setStatus("current")


class _OpModeLocalLog_Type(Integer32):
    """Custom type opModeLocalLog based on Integer32"""
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


_OpModeLocalLog_Type.__name__ = "Integer32"
_OpModeLocalLog_Object = MibScalar
opModeLocalLog = _OpModeLocalLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 8, 4),
    _OpModeLocalLog_Type()
)
opModeLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opModeLocalLog.setStatus("current")


class _SysRemoteLog_Type(Integer32):
    """Custom type sysRemoteLog based on Integer32"""
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


_SysRemoteLog_Type.__name__ = "Integer32"
_SysRemoteLog_Object = MibScalar
sysRemoteLog = _SysRemoteLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 8, 5),
    _SysRemoteLog_Type()
)
sysRemoteLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRemoteLog.setStatus("current")


class _NetworkRemoteLog_Type(Integer32):
    """Custom type networkRemoteLog based on Integer32"""
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


_NetworkRemoteLog_Type.__name__ = "Integer32"
_NetworkRemoteLog_Object = MibScalar
networkRemoteLog = _NetworkRemoteLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 8, 6),
    _NetworkRemoteLog_Type()
)
networkRemoteLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRemoteLog.setStatus("current")


class _ConfigRemoteLog_Type(Integer32):
    """Custom type configRemoteLog based on Integer32"""
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


_ConfigRemoteLog_Type.__name__ = "Integer32"
_ConfigRemoteLog_Object = MibScalar
configRemoteLog = _ConfigRemoteLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 8, 7),
    _ConfigRemoteLog_Type()
)
configRemoteLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRemoteLog.setStatus("current")


class _OpModeRemoteLog_Type(Integer32):
    """Custom type opModeRemoteLog based on Integer32"""
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


_OpModeRemoteLog_Type.__name__ = "Integer32"
_OpModeRemoteLog_Object = MibScalar
opModeRemoteLog = _OpModeRemoteLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 8, 8),
    _OpModeRemoteLog_Type()
)
opModeRemoteLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opModeRemoteLog.setStatus("current")
_RemoteLogServer_ObjectIdentity = ObjectIdentity
remoteLogServer = _RemoteLogServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 9)
)


class _SyslogServerIp_Type(DisplayString):
    """Custom type syslogServerIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SyslogServerIp_Type.__name__ = "DisplayString"
_SyslogServerIp_Object = MibScalar
syslogServerIp = _SyslogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 9, 1),
    _SyslogServerIp_Type()
)
syslogServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIp.setStatus("current")


class _SyslogFacility_Type(Integer32):
    """Custom type syslogFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("local-use-0", 0),
          ("local-use-1", 1),
          ("local-use-2", 2),
          ("local-use-3", 3),
          ("local-use-4", 4),
          ("local-use-5", 5),
          ("local-use-6", 6),
          ("local-use-7", 7))
    )


_SyslogFacility_Type.__name__ = "Integer32"
_SyslogFacility_Object = MibScalar
syslogFacility = _SyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 9, 2),
    _SyslogFacility_Type()
)
syslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogFacility.setStatus("current")


class _SyslogSeverity_Type(Integer32):
    """Custom type syslogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("informational", 6),
          ("debug", 7))
    )


_SyslogSeverity_Type.__name__ = "Integer32"
_SyslogSeverity_Object = MibScalar
syslogSeverity = _SyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 1, 9, 3),
    _SyslogSeverity_Type()
)
syslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSeverity.setStatus("current")
_AutoWarningSettings_ObjectIdentity = ObjectIdentity
autoWarningSettings = _AutoWarningSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2)
)
_EventSettings_ObjectIdentity = ObjectIdentity
eventSettings = _EventSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1)
)


class _MailWarningColdStart_Type(Integer32):
    """Custom type mailWarningColdStart based on Integer32"""
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


_MailWarningColdStart_Type.__name__ = "Integer32"
_MailWarningColdStart_Object = MibScalar
mailWarningColdStart = _MailWarningColdStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 1),
    _MailWarningColdStart_Type()
)
mailWarningColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningColdStart.setStatus("current")


class _MailWarningWarmStart_Type(Integer32):
    """Custom type mailWarningWarmStart based on Integer32"""
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


_MailWarningWarmStart_Type.__name__ = "Integer32"
_MailWarningWarmStart_Object = MibScalar
mailWarningWarmStart = _MailWarningWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 2),
    _MailWarningWarmStart_Type()
)
mailWarningWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningWarmStart.setStatus("current")


class _MailWarningAuthFailure_Type(Integer32):
    """Custom type mailWarningAuthFailure based on Integer32"""
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


_MailWarningAuthFailure_Type.__name__ = "Integer32"
_MailWarningAuthFailure_Object = MibScalar
mailWarningAuthFailure = _MailWarningAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 3),
    _MailWarningAuthFailure_Type()
)
mailWarningAuthFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningAuthFailure.setStatus("current")


class _MailWarningIpChanged_Type(Integer32):
    """Custom type mailWarningIpChanged based on Integer32"""
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


_MailWarningIpChanged_Type.__name__ = "Integer32"
_MailWarningIpChanged_Object = MibScalar
mailWarningIpChanged = _MailWarningIpChanged_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 4),
    _MailWarningIpChanged_Type()
)
mailWarningIpChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningIpChanged.setStatus("current")


class _MailWarningPasswordChanged_Type(Integer32):
    """Custom type mailWarningPasswordChanged based on Integer32"""
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


_MailWarningPasswordChanged_Type.__name__ = "Integer32"
_MailWarningPasswordChanged_Object = MibScalar
mailWarningPasswordChanged = _MailWarningPasswordChanged_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 5),
    _MailWarningPasswordChanged_Type()
)
mailWarningPasswordChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningPasswordChanged.setStatus("current")


class _TrapServerColdStart_Type(Integer32):
    """Custom type trapServerColdStart based on Integer32"""
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


_TrapServerColdStart_Type.__name__ = "Integer32"
_TrapServerColdStart_Object = MibScalar
trapServerColdStart = _TrapServerColdStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 6),
    _TrapServerColdStart_Type()
)
trapServerColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerColdStart.setStatus("current")


class _TrapServerWarmStart_Type(Integer32):
    """Custom type trapServerWarmStart based on Integer32"""
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


_TrapServerWarmStart_Type.__name__ = "Integer32"
_TrapServerWarmStart_Object = MibScalar
trapServerWarmStart = _TrapServerWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 7),
    _TrapServerWarmStart_Type()
)
trapServerWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerWarmStart.setStatus("current")


class _TrapServerAuthFailure_Type(Integer32):
    """Custom type trapServerAuthFailure based on Integer32"""
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


_TrapServerAuthFailure_Type.__name__ = "Integer32"
_TrapServerAuthFailure_Object = MibScalar
trapServerAuthFailure = _TrapServerAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 8),
    _TrapServerAuthFailure_Type()
)
trapServerAuthFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerAuthFailure.setStatus("current")


class _AlarmServerEthernet1LinkDown_Type(Integer32):
    """Custom type alarmServerEthernet1LinkDown based on Integer32"""
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


_AlarmServerEthernet1LinkDown_Type.__name__ = "Integer32"
_AlarmServerEthernet1LinkDown_Object = MibScalar
alarmServerEthernet1LinkDown = _AlarmServerEthernet1LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 9),
    _AlarmServerEthernet1LinkDown_Type()
)
alarmServerEthernet1LinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmServerEthernet1LinkDown.setStatus("current")


class _AlarmServerEthernet2LinkDown_Type(Integer32):
    """Custom type alarmServerEthernet2LinkDown based on Integer32"""
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


_AlarmServerEthernet2LinkDown_Type.__name__ = "Integer32"
_AlarmServerEthernet2LinkDown_Object = MibScalar
alarmServerEthernet2LinkDown = _AlarmServerEthernet2LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 10),
    _AlarmServerEthernet2LinkDown_Type()
)
alarmServerEthernet2LinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmServerEthernet2LinkDown.setStatus("current")


class _AlarmServerEthernet3LinkDown_Type(Integer32):
    """Custom type alarmServerEthernet3LinkDown based on Integer32"""
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


_AlarmServerEthernet3LinkDown_Type.__name__ = "Integer32"
_AlarmServerEthernet3LinkDown_Object = MibScalar
alarmServerEthernet3LinkDown = _AlarmServerEthernet3LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 11),
    _AlarmServerEthernet3LinkDown_Type()
)
alarmServerEthernet3LinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmServerEthernet3LinkDown.setStatus("current")


class _SmsServerColdStart_Type(Integer32):
    """Custom type smsServerColdStart based on Integer32"""
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


_SmsServerColdStart_Type.__name__ = "Integer32"
_SmsServerColdStart_Object = MibScalar
smsServerColdStart = _SmsServerColdStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 12),
    _SmsServerColdStart_Type()
)
smsServerColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsServerColdStart.setStatus("current")


class _SmsServerWarmStart_Type(Integer32):
    """Custom type smsServerWarmStart based on Integer32"""
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


_SmsServerWarmStart_Type.__name__ = "Integer32"
_SmsServerWarmStart_Object = MibScalar
smsServerWarmStart = _SmsServerWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 13),
    _SmsServerWarmStart_Type()
)
smsServerWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsServerWarmStart.setStatus("current")


class _SmsServerEthernet1LinkDown_Type(Integer32):
    """Custom type smsServerEthernet1LinkDown based on Integer32"""
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


_SmsServerEthernet1LinkDown_Type.__name__ = "Integer32"
_SmsServerEthernet1LinkDown_Object = MibScalar
smsServerEthernet1LinkDown = _SmsServerEthernet1LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 14),
    _SmsServerEthernet1LinkDown_Type()
)
smsServerEthernet1LinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsServerEthernet1LinkDown.setStatus("current")


class _SmsServerEthernet2LinkDown_Type(Integer32):
    """Custom type smsServerEthernet2LinkDown based on Integer32"""
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


_SmsServerEthernet2LinkDown_Type.__name__ = "Integer32"
_SmsServerEthernet2LinkDown_Object = MibScalar
smsServerEthernet2LinkDown = _SmsServerEthernet2LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 15),
    _SmsServerEthernet2LinkDown_Type()
)
smsServerEthernet2LinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsServerEthernet2LinkDown.setStatus("current")


class _SmsServerEthernet3LinkDown_Type(Integer32):
    """Custom type smsServerEthernet3LinkDown based on Integer32"""
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


_SmsServerEthernet3LinkDown_Type.__name__ = "Integer32"
_SmsServerEthernet3LinkDown_Object = MibScalar
smsServerEthernet3LinkDown = _SmsServerEthernet3LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 16),
    _SmsServerEthernet3LinkDown_Type()
)
smsServerEthernet3LinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsServerEthernet3LinkDown.setStatus("current")


class _SmsServerAuthFailure_Type(Integer32):
    """Custom type smsServerAuthFailure based on Integer32"""
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


_SmsServerAuthFailure_Type.__name__ = "Integer32"
_SmsServerAuthFailure_Object = MibScalar
smsServerAuthFailure = _SmsServerAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 17),
    _SmsServerAuthFailure_Type()
)
smsServerAuthFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsServerAuthFailure.setStatus("current")


class _SmsServerIpChanged_Type(Integer32):
    """Custom type smsServerIpChanged based on Integer32"""
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


_SmsServerIpChanged_Type.__name__ = "Integer32"
_SmsServerIpChanged_Object = MibScalar
smsServerIpChanged = _SmsServerIpChanged_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 18),
    _SmsServerIpChanged_Type()
)
smsServerIpChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsServerIpChanged.setStatus("current")


class _SmsServerPasswordChanged_Type(Integer32):
    """Custom type smsServerPasswordChanged based on Integer32"""
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


_SmsServerPasswordChanged_Type.__name__ = "Integer32"
_SmsServerPasswordChanged_Object = MibScalar
smsServerPasswordChanged = _SmsServerPasswordChanged_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 1, 19),
    _SmsServerPasswordChanged_Type()
)
smsServerPasswordChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsServerPasswordChanged.setStatus("current")
_SerialEventSettings_ObjectIdentity = ObjectIdentity
serialEventSettings = _SerialEventSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 2)
)
_PortEventSettingsTable_Object = MibTable
portEventSettingsTable = _PortEventSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    portEventSettingsTable.setStatus("current")
_PortEventSettingsEntry_Object = MibTableRow
portEventSettingsEntry = _PortEventSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 2, 1, 1)
)
portEventSettingsEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEventSettingsEntry.setStatus("current")


class _MailDCDchange_Type(Integer32):
    """Custom type mailDCDchange based on Integer32"""
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


_MailDCDchange_Type.__name__ = "Integer32"
_MailDCDchange_Object = MibTableColumn
mailDCDchange = _MailDCDchange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 2, 1, 1, 1),
    _MailDCDchange_Type()
)
mailDCDchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailDCDchange.setStatus("current")


class _TrapDCDchange_Type(Integer32):
    """Custom type trapDCDchange based on Integer32"""
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


_TrapDCDchange_Type.__name__ = "Integer32"
_TrapDCDchange_Object = MibTableColumn
trapDCDchange = _TrapDCDchange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 2, 1, 1, 2),
    _TrapDCDchange_Type()
)
trapDCDchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDCDchange.setStatus("current")


class _AlarmDCDchange_Type(Integer32):
    """Custom type alarmDCDchange based on Integer32"""
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


_AlarmDCDchange_Type.__name__ = "Integer32"
_AlarmDCDchange_Object = MibTableColumn
alarmDCDchange = _AlarmDCDchange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 2, 1, 1, 3),
    _AlarmDCDchange_Type()
)
alarmDCDchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmDCDchange.setStatus("current")


class _SmsDCDchange_Type(Integer32):
    """Custom type smsDCDchange based on Integer32"""
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


_SmsDCDchange_Type.__name__ = "Integer32"
_SmsDCDchange_Object = MibTableColumn
smsDCDchange = _SmsDCDchange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 2, 1, 1, 4),
    _SmsDCDchange_Type()
)
smsDCDchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsDCDchange.setStatus("current")


class _MailDSRchange_Type(Integer32):
    """Custom type mailDSRchange based on Integer32"""
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


_MailDSRchange_Type.__name__ = "Integer32"
_MailDSRchange_Object = MibTableColumn
mailDSRchange = _MailDSRchange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 2, 1, 1, 5),
    _MailDSRchange_Type()
)
mailDSRchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailDSRchange.setStatus("current")


class _TrapDSRchange_Type(Integer32):
    """Custom type trapDSRchange based on Integer32"""
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


_TrapDSRchange_Type.__name__ = "Integer32"
_TrapDSRchange_Object = MibTableColumn
trapDSRchange = _TrapDSRchange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 2, 1, 1, 6),
    _TrapDSRchange_Type()
)
trapDSRchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDSRchange.setStatus("current")


class _AlarmDSRchange_Type(Integer32):
    """Custom type alarmDSRchange based on Integer32"""
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


_AlarmDSRchange_Type.__name__ = "Integer32"
_AlarmDSRchange_Object = MibTableColumn
alarmDSRchange = _AlarmDSRchange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 2, 1, 1, 7),
    _AlarmDSRchange_Type()
)
alarmDSRchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmDSRchange.setStatus("current")


class _SmsDSRchange_Type(Integer32):
    """Custom type smsDSRchange based on Integer32"""
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


_SmsDSRchange_Type.__name__ = "Integer32"
_SmsDSRchange_Object = MibTableColumn
smsDSRchange = _SmsDSRchange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 2, 1, 1, 8),
    _SmsDSRchange_Type()
)
smsDSRchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsDSRchange.setStatus("current")
_EmailAlert_ObjectIdentity = ObjectIdentity
emailAlert = _EmailAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 3)
)
_EmailWarningMailServer_Type = DisplayString
_EmailWarningMailServer_Object = MibScalar
emailWarningMailServer = _EmailWarningMailServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 3, 1),
    _EmailWarningMailServer_Type()
)
emailWarningMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningMailServer.setStatus("current")


class _EmailRequiresAuthentication_Type(Integer32):
    """Custom type emailRequiresAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-require", 0),
          ("require", 1))
    )


_EmailRequiresAuthentication_Type.__name__ = "Integer32"
_EmailRequiresAuthentication_Object = MibScalar
emailRequiresAuthentication = _EmailRequiresAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 3, 2),
    _EmailRequiresAuthentication_Type()
)
emailRequiresAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailRequiresAuthentication.setStatus("current")


class _EmailWarningUserName_Type(DisplayString):
    """Custom type emailWarningUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EmailWarningUserName_Type.__name__ = "DisplayString"
_EmailWarningUserName_Object = MibScalar
emailWarningUserName = _EmailWarningUserName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 3, 3),
    _EmailWarningUserName_Type()
)
emailWarningUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningUserName.setStatus("current")


class _EmailWarningPassword_Type(DisplayString):
    """Custom type emailWarningPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EmailWarningPassword_Type.__name__ = "DisplayString"
_EmailWarningPassword_Object = MibScalar
emailWarningPassword = _EmailWarningPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 3, 4),
    _EmailWarningPassword_Type()
)
emailWarningPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningPassword.setStatus("current")
_EmailWarningFromEmail_Type = DisplayString
_EmailWarningFromEmail_Object = MibScalar
emailWarningFromEmail = _EmailWarningFromEmail_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 3, 5),
    _EmailWarningFromEmail_Type()
)
emailWarningFromEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFromEmail.setStatus("current")
_EmailWarningFirstEmailAddr_Type = DisplayString
_EmailWarningFirstEmailAddr_Object = MibScalar
emailWarningFirstEmailAddr = _EmailWarningFirstEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 3, 6),
    _EmailWarningFirstEmailAddr_Type()
)
emailWarningFirstEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFirstEmailAddr.setStatus("current")
_EmailWarningSecondEmailAddr_Type = DisplayString
_EmailWarningSecondEmailAddr_Object = MibScalar
emailWarningSecondEmailAddr = _EmailWarningSecondEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 3, 7),
    _EmailWarningSecondEmailAddr_Type()
)
emailWarningSecondEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSecondEmailAddr.setStatus("current")
_EmailWarningThirdEmailAddr_Type = DisplayString
_EmailWarningThirdEmailAddr_Object = MibScalar
emailWarningThirdEmailAddr = _EmailWarningThirdEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 3, 8),
    _EmailWarningThirdEmailAddr_Type()
)
emailWarningThirdEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningThirdEmailAddr.setStatus("current")
_EmailWarningFourthEmailAddr_Type = DisplayString
_EmailWarningFourthEmailAddr_Object = MibScalar
emailWarningFourthEmailAddr = _EmailWarningFourthEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 3, 9),
    _EmailWarningFourthEmailAddr_Type()
)
emailWarningFourthEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFourthEmailAddr.setStatus("current")
_SnmpTrap_ObjectIdentity = ObjectIdentity
snmpTrap = _SnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 4)
)
_SnmpTrapReceiverIp_Type = DisplayString
_SnmpTrapReceiverIp_Object = MibScalar
snmpTrapReceiverIp = _SnmpTrapReceiverIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 4, 1),
    _SnmpTrapReceiverIp_Type()
)
snmpTrapReceiverIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapReceiverIp.setStatus("current")


class _TrapVersion_Type(Integer32):
    """Custom type trapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1))
    )


_TrapVersion_Type.__name__ = "Integer32"
_TrapVersion_Object = MibScalar
trapVersion = _TrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 4, 2),
    _TrapVersion_Type()
)
trapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapVersion.setStatus("current")
_SmsAlert_ObjectIdentity = ObjectIdentity
smsAlert = _SmsAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 5)
)


class _SmsAlertFirstPhoneNumber_Type(DisplayString):
    """Custom type smsAlertFirstPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SmsAlertFirstPhoneNumber_Type.__name__ = "DisplayString"
_SmsAlertFirstPhoneNumber_Object = MibScalar
smsAlertFirstPhoneNumber = _SmsAlertFirstPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 5, 1),
    _SmsAlertFirstPhoneNumber_Type()
)
smsAlertFirstPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsAlertFirstPhoneNumber.setStatus("current")


class _SmsAlertSecondPhoneNumber_Type(DisplayString):
    """Custom type smsAlertSecondPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SmsAlertSecondPhoneNumber_Type.__name__ = "DisplayString"
_SmsAlertSecondPhoneNumber_Object = MibScalar
smsAlertSecondPhoneNumber = _SmsAlertSecondPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 5, 2),
    _SmsAlertSecondPhoneNumber_Type()
)
smsAlertSecondPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsAlertSecondPhoneNumber.setStatus("current")


class _SmsAlertThirdPhoneNumber_Type(DisplayString):
    """Custom type smsAlertThirdPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SmsAlertThirdPhoneNumber_Type.__name__ = "DisplayString"
_SmsAlertThirdPhoneNumber_Object = MibScalar
smsAlertThirdPhoneNumber = _SmsAlertThirdPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 5, 3),
    _SmsAlertThirdPhoneNumber_Type()
)
smsAlertThirdPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsAlertThirdPhoneNumber.setStatus("current")


class _SmsAlertFourthPhoneNumber_Type(DisplayString):
    """Custom type smsAlertFourthPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SmsAlertFourthPhoneNumber_Type.__name__ = "DisplayString"
_SmsAlertFourthPhoneNumber_Object = MibScalar
smsAlertFourthPhoneNumber = _SmsAlertFourthPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 5, 4),
    _SmsAlertFourthPhoneNumber_Type()
)
smsAlertFourthPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsAlertFourthPhoneNumber.setStatus("current")
_EventLogSettings_ObjectIdentity = ObjectIdentity
eventLogSettings = _EventLogSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 6)
)
_CurrentLogCapacityRatio_Type = DisplayString
_CurrentLogCapacityRatio_Object = MibScalar
currentLogCapacityRatio = _CurrentLogCapacityRatio_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 6, 1),
    _CurrentLogCapacityRatio_Type()
)
currentLogCapacityRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentLogCapacityRatio.setStatus("current")


class _LogCapacityWarningEnable_Type(Integer32):
    """Custom type logCapacityWarningEnable based on Integer32"""
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


_LogCapacityWarningEnable_Type.__name__ = "Integer32"
_LogCapacityWarningEnable_Object = MibScalar
logCapacityWarningEnable = _LogCapacityWarningEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 6, 2),
    _LogCapacityWarningEnable_Type()
)
logCapacityWarningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logCapacityWarningEnable.setStatus("current")


class _LogCapacityWarningThreshold_Type(Integer32):
    """Custom type logCapacityWarningThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LogCapacityWarningThreshold_Type.__name__ = "Integer32"
_LogCapacityWarningThreshold_Object = MibScalar
logCapacityWarningThreshold = _LogCapacityWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 6, 3),
    _LogCapacityWarningThreshold_Type()
)
logCapacityWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logCapacityWarningThreshold.setStatus("current")


class _MailLogCapacity_Type(Integer32):
    """Custom type mailLogCapacity based on Integer32"""
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


_MailLogCapacity_Type.__name__ = "Integer32"
_MailLogCapacity_Object = MibScalar
mailLogCapacity = _MailLogCapacity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 6, 4),
    _MailLogCapacity_Type()
)
mailLogCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailLogCapacity.setStatus("current")


class _TrapLogCapacity_Type(Integer32):
    """Custom type trapLogCapacity based on Integer32"""
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


_TrapLogCapacity_Type.__name__ = "Integer32"
_TrapLogCapacity_Object = MibScalar
trapLogCapacity = _TrapLogCapacity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 6, 5),
    _TrapLogCapacity_Type()
)
trapLogCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLogCapacity.setStatus("current")


class _LogOversizeAction_Type(Integer32):
    """Custom type logOversizeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("overwriteTheOldestEventLog", 0),
          ("stopRecordingEventLog", 1))
    )


_LogOversizeAction_Type.__name__ = "Integer32"
_LogOversizeAction_Object = MibScalar
logOversizeAction = _LogOversizeAction_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 2, 6, 6),
    _LogOversizeAction_Type()
)
logOversizeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logOversizeAction.setStatus("current")
_Maintenance_ObjectIdentity = ObjectIdentity
maintenance = _Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3)
)
_ConsoleSettings_ObjectIdentity = ObjectIdentity
consoleSettings = _ConsoleSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 1)
)


class _HttpConsole_Type(Integer32):
    """Custom type httpConsole based on Integer32"""
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


_HttpConsole_Type.__name__ = "Integer32"
_HttpConsole_Object = MibScalar
httpConsole = _HttpConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 1, 1),
    _HttpConsole_Type()
)
httpConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpConsole.setStatus("current")


class _HttpsConsole_Type(Integer32):
    """Custom type httpsConsole based on Integer32"""
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


_HttpsConsole_Type.__name__ = "Integer32"
_HttpsConsole_Object = MibScalar
httpsConsole = _HttpsConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 1, 2),
    _HttpsConsole_Type()
)
httpsConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsConsole.setStatus("current")


class _TelnetConsole_Type(Integer32):
    """Custom type telnetConsole based on Integer32"""
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


_TelnetConsole_Type.__name__ = "Integer32"
_TelnetConsole_Object = MibScalar
telnetConsole = _TelnetConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 1, 3),
    _TelnetConsole_Type()
)
telnetConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetConsole.setStatus("current")


class _SshConsole_Type(Integer32):
    """Custom type sshConsole based on Integer32"""
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


_SshConsole_Type.__name__ = "Integer32"
_SshConsole_Object = MibScalar
sshConsole = _SshConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 1, 4),
    _SshConsole_Type()
)
sshConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshConsole.setStatus("current")


class _ConsoleAuthenticationType_Type(Integer32):
    """Custom type consoleAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("radius", 1),
          ("radius-local", 2),
          ("local-radius", 3),
          ("tacacsPlus", 4),
          ("tacacsPlus-local", 5),
          ("local-tacacsPlus", 6))
    )


_ConsoleAuthenticationType_Type.__name__ = "Integer32"
_ConsoleAuthenticationType_Object = MibScalar
consoleAuthenticationType = _ConsoleAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 1, 5),
    _ConsoleAuthenticationType_Type()
)
consoleAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleAuthenticationType.setStatus("current")


class _TryNextTypeOnAuthDenied_Type(Integer32):
    """Custom type tryNextTypeOnAuthDenied based on Integer32"""
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


_TryNextTypeOnAuthDenied_Type.__name__ = "Integer32"
_TryNextTypeOnAuthDenied_Object = MibScalar
tryNextTypeOnAuthDenied = _TryNextTypeOnAuthDenied_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 1, 6),
    _TryNextTypeOnAuthDenied_Type()
)
tryNextTypeOnAuthDenied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tryNextTypeOnAuthDenied.setStatus("current")


class _ResetButtonFunction_Type(Integer32):
    """Custom type resetButtonFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable-after-60-sec", 0),
          ("always-enable", 1))
    )


_ResetButtonFunction_Type.__name__ = "Integer32"
_ResetButtonFunction_Object = MibScalar
resetButtonFunction = _ResetButtonFunction_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 1, 7),
    _ResetButtonFunction_Type()
)
resetButtonFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetButtonFunction.setStatus("current")


class _LcmReadOnlyProtect_Type(Integer32):
    """Custom type lcmReadOnlyProtect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 0),
          ("writable", 1))
    )


_LcmReadOnlyProtect_Type.__name__ = "Integer32"
_LcmReadOnlyProtect_Object = MibScalar
lcmReadOnlyProtect = _LcmReadOnlyProtect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 1, 8),
    _LcmReadOnlyProtect_Type()
)
lcmReadOnlyProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcmReadOnlyProtect.setStatus("current")


class _MaxHttpLoginUsers_Type(Integer32):
    """Custom type maxHttpLoginUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MaxHttpLoginUsers_Type.__name__ = "Integer32"
_MaxHttpLoginUsers_Object = MibScalar
maxHttpLoginUsers = _MaxHttpLoginUsers_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 1, 9),
    _MaxHttpLoginUsers_Type()
)
maxHttpLoginUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxHttpLoginUsers.setStatus("current")


class _AutoLogoutSetting_Type(Integer32):
    """Custom type autoLogoutSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_AutoLogoutSetting_Type.__name__ = "Integer32"
_AutoLogoutSetting_Object = MibScalar
autoLogoutSetting = _AutoLogoutSetting_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 1, 10),
    _AutoLogoutSetting_Type()
)
autoLogoutSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoLogoutSetting.setStatus("current")
_LoadFactoryDefault_ObjectIdentity = ObjectIdentity
loadFactoryDefault = _LoadFactoryDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 2)
)


class _LoadFactoryDefaultSetting_Type(Integer32):
    """Custom type loadFactoryDefaultSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("resetToFactoryDefault-ExcludingIpConfiguration", 0),
          ("resetToFactoryDefault", 1))
    )


_LoadFactoryDefaultSetting_Type.__name__ = "Integer32"
_LoadFactoryDefaultSetting_Object = MibScalar
loadFactoryDefaultSetting = _LoadFactoryDefaultSetting_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 3, 2, 1),
    _LoadFactoryDefaultSetting_Type()
)
loadFactoryDefaultSetting.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    loadFactoryDefaultSetting.setStatus("current")
_AccountManagement_ObjectIdentity = ObjectIdentity
accountManagement = _AccountManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4)
)
_NotificationMessage_ObjectIdentity = ObjectIdentity
notificationMessage = _NotificationMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 1)
)


class _LoginNotificationMessage_Type(DisplayString):
    """Custom type loginNotificationMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_LoginNotificationMessage_Type.__name__ = "DisplayString"
_LoginNotificationMessage_Object = MibScalar
loginNotificationMessage = _LoginNotificationMessage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 1, 1),
    _LoginNotificationMessage_Type()
)
loginNotificationMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginNotificationMessage.setStatus("current")


class _LoginFailureMessage_Type(DisplayString):
    """Custom type loginFailureMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_LoginFailureMessage_Type.__name__ = "DisplayString"
_LoginFailureMessage_Object = MibScalar
loginFailureMessage = _LoginFailureMessage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 1, 2),
    _LoginFailureMessage_Type()
)
loginFailureMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginFailureMessage.setStatus("current")
_UserAccount_ObjectIdentity = ObjectIdentity
userAccount = _UserAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 2)
)
_UserAccountTable_Object = MibTable
userAccountTable = _UserAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    userAccountTable.setStatus("current")
_UserAccountEntry_Object = MibTableRow
userAccountEntry = _UserAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 2, 1, 1)
)
userAccountEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "userAccountIndex"),
)
if mibBuilder.loadTexts:
    userAccountEntry.setStatus("current")
_UserAccountIndex_Type = Integer32
_UserAccountIndex_Object = MibTableColumn
userAccountIndex = _UserAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 2, 1, 1, 1),
    _UserAccountIndex_Type()
)
userAccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAccountIndex.setStatus("current")


class _ActiveUserAccount_Type(Integer32):
    """Custom type activeUserAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non_active", 0),
          ("avtive", 1))
    )


_ActiveUserAccount_Type.__name__ = "Integer32"
_ActiveUserAccount_Object = MibTableColumn
activeUserAccount = _ActiveUserAccount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 2, 1, 1, 2),
    _ActiveUserAccount_Type()
)
activeUserAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeUserAccount.setStatus("current")


class _AccountName_Type(DisplayString):
    """Custom type accountName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AccountName_Type.__name__ = "DisplayString"
_AccountName_Object = MibTableColumn
accountName = _AccountName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 2, 1, 1, 3),
    _AccountName_Type()
)
accountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountName.setStatus("current")


class _AccountGroupName_Type(DisplayString):
    """Custom type accountGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AccountGroupName_Type.__name__ = "DisplayString"
_AccountGroupName_Object = MibTableColumn
accountGroupName = _AccountGroupName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 2, 1, 1, 4),
    _AccountGroupName_Type()
)
accountGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountGroupName.setStatus("current")
_AccessPermission_ObjectIdentity = ObjectIdentity
accessPermission = _AccessPermission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 3)
)
_AccessPermissionTable_Object = MibTable
accessPermissionTable = _AccessPermissionTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 3, 1)
)
if mibBuilder.loadTexts:
    accessPermissionTable.setStatus("current")
_AccessPermissionEntry_Object = MibTableRow
accessPermissionEntry = _AccessPermissionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 3, 1, 1)
)
accessPermissionEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "groupName"),
)
if mibBuilder.loadTexts:
    accessPermissionEntry.setStatus("current")


class _GroupName_Type(DisplayString):
    """Custom type groupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GroupName_Type.__name__ = "DisplayString"
_GroupName_Object = MibTableColumn
groupName = _GroupName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 3, 1, 1, 1),
    _GroupName_Type()
)
groupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupName.setStatus("current")


class _NetworkConfig_Type(Integer32):
    """Custom type networkConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-display", 0),
          ("read-only", 1),
          ("read-write", 2))
    )


_NetworkConfig_Type.__name__ = "Integer32"
_NetworkConfig_Object = MibTableColumn
networkConfig = _NetworkConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 3, 1, 1, 2),
    _NetworkConfig_Type()
)
networkConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkConfig.setStatus("current")


class _SerialConfig_Type(Integer32):
    """Custom type serialConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-display", 0),
          ("read-only", 1),
          ("read-write", 2))
    )


_SerialConfig_Type.__name__ = "Integer32"
_SerialConfig_Object = MibTableColumn
serialConfig = _SerialConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 3, 1, 1, 3),
    _SerialConfig_Type()
)
serialConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialConfig.setStatus("current")


class _SystemConfig_Type(Integer32):
    """Custom type systemConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-display", 0),
          ("read-only", 1),
          ("read-write", 2))
    )


_SystemConfig_Type.__name__ = "Integer32"
_SystemConfig_Object = MibTableColumn
systemConfig = _SystemConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 3, 1, 1, 4),
    _SystemConfig_Type()
)
systemConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfig.setStatus("current")


class _AdminConfig_Type(Integer32):
    """Custom type adminConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-display", 0),
          ("read-only", 1),
          ("read-write", 2))
    )


_AdminConfig_Type.__name__ = "Integer32"
_AdminConfig_Object = MibTableColumn
adminConfig = _AdminConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 3, 1, 1, 5),
    _AdminConfig_Type()
)
adminConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminConfig.setStatus("current")


class _MonitorLogWarning_Type(Integer32):
    """Custom type monitorLogWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-display", 0),
          ("read-only", 1),
          ("read-write", 2))
    )


_MonitorLogWarning_Type.__name__ = "Integer32"
_MonitorLogWarning_Object = MibTableColumn
monitorLogWarning = _MonitorLogWarning_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 3, 1, 1, 6),
    _MonitorLogWarning_Type()
)
monitorLogWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorLogWarning.setStatus("current")


class _CommonSetting_Type(Integer32):
    """Custom type commonSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-display", 0),
          ("read-only", 1),
          ("read-write", 2))
    )


_CommonSetting_Type.__name__ = "Integer32"
_CommonSetting_Object = MibTableColumn
commonSetting = _CommonSetting_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 3, 1, 1, 7),
    _CommonSetting_Type()
)
commonSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonSetting.setStatus("current")
_AccountPasswordAndLoginMgmt_ObjectIdentity = ObjectIdentity
accountPasswordAndLoginMgmt = _AccountPasswordAndLoginMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 4)
)
_AccountPasswordPolicy_ObjectIdentity = ObjectIdentity
accountPasswordPolicy = _AccountPasswordPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 4, 1)
)


class _PwdMinLength_Type(Integer32):
    """Custom type pwdMinLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 16),
    )


_PwdMinLength_Type.__name__ = "Integer32"
_PwdMinLength_Object = MibScalar
pwdMinLength = _PwdMinLength_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 4, 1, 1),
    _PwdMinLength_Type()
)
pwdMinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwdMinLength.setStatus("current")


class _PwdComplexityCheckEnable_Type(Integer32):
    """Custom type pwdComplexityCheckEnable based on Integer32"""
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


_PwdComplexityCheckEnable_Type.__name__ = "Integer32"
_PwdComplexityCheckEnable_Object = MibScalar
pwdComplexityCheckEnable = _PwdComplexityCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 4, 1, 2),
    _PwdComplexityCheckEnable_Type()
)
pwdComplexityCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwdComplexityCheckEnable.setStatus("current")


class _PwdComplexityCheckDigitEnable_Type(Integer32):
    """Custom type pwdComplexityCheckDigitEnable based on Integer32"""
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


_PwdComplexityCheckDigitEnable_Type.__name__ = "Integer32"
_PwdComplexityCheckDigitEnable_Object = MibScalar
pwdComplexityCheckDigitEnable = _PwdComplexityCheckDigitEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 4, 1, 3),
    _PwdComplexityCheckDigitEnable_Type()
)
pwdComplexityCheckDigitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwdComplexityCheckDigitEnable.setStatus("current")


class _PwdComplexityCheckAlphabetEnable_Type(Integer32):
    """Custom type pwdComplexityCheckAlphabetEnable based on Integer32"""
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


_PwdComplexityCheckAlphabetEnable_Type.__name__ = "Integer32"
_PwdComplexityCheckAlphabetEnable_Object = MibScalar
pwdComplexityCheckAlphabetEnable = _PwdComplexityCheckAlphabetEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 4, 1, 4),
    _PwdComplexityCheckAlphabetEnable_Type()
)
pwdComplexityCheckAlphabetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwdComplexityCheckAlphabetEnable.setStatus("current")


class _PwdComplexityCheckSpecialCharEnable_Type(Integer32):
    """Custom type pwdComplexityCheckSpecialCharEnable based on Integer32"""
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


_PwdComplexityCheckSpecialCharEnable_Type.__name__ = "Integer32"
_PwdComplexityCheckSpecialCharEnable_Object = MibScalar
pwdComplexityCheckSpecialCharEnable = _PwdComplexityCheckSpecialCharEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 4, 1, 5),
    _PwdComplexityCheckSpecialCharEnable_Type()
)
pwdComplexityCheckSpecialCharEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwdComplexityCheckSpecialCharEnable.setStatus("current")


class _PwdLifetime_Type(Integer32):
    """Custom type pwdLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 180),
    )


_PwdLifetime_Type.__name__ = "Integer32"
_PwdLifetime_Object = MibScalar
pwdLifetime = _PwdLifetime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 4, 1, 6),
    _PwdLifetime_Type()
)
pwdLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwdLifetime.setStatus("current")
_AccountLoginFailureLockout_ObjectIdentity = ObjectIdentity
accountLoginFailureLockout = _AccountLoginFailureLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 4, 2)
)


class _LoginFailureLockoutEnable_Type(Integer32):
    """Custom type loginFailureLockoutEnable based on Integer32"""
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


_LoginFailureLockoutEnable_Type.__name__ = "Integer32"
_LoginFailureLockoutEnable_Object = MibScalar
loginFailureLockoutEnable = _LoginFailureLockoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 4, 2, 1),
    _LoginFailureLockoutEnable_Type()
)
loginFailureLockoutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginFailureLockoutEnable.setStatus("current")


class _LoginFailureLockoutRetrys_Type(Integer32):
    """Custom type loginFailureLockoutRetrys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LoginFailureLockoutRetrys_Type.__name__ = "Integer32"
_LoginFailureLockoutRetrys_Object = MibScalar
loginFailureLockoutRetrys = _LoginFailureLockoutRetrys_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 4, 2, 2),
    _LoginFailureLockoutRetrys_Type()
)
loginFailureLockoutRetrys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginFailureLockoutRetrys.setStatus("current")


class _LoginFailureLockoutTime_Type(Integer32):
    """Custom type loginFailureLockoutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_LoginFailureLockoutTime_Type.__name__ = "Integer32"
_LoginFailureLockoutTime_Object = MibScalar
loginFailureLockoutTime = _LoginFailureLockoutTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 5, 4, 4, 2, 3),
    _LoginFailureLockoutTime_Type()
)
loginFailureLockoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginFailureLockoutTime.setStatus("current")
_SysStatus_ObjectIdentity = ObjectIdentity
sysStatus = _SysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6)
)
_S2eConnections_ObjectIdentity = ObjectIdentity
s2eConnections = _S2eConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 1)
)
_MonitorRemoteIpTable_Object = MibTable
monitorRemoteIpTable = _MonitorRemoteIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    monitorRemoteIpTable.setStatus("current")
_MonitorRemoteIpEntry_Object = MibTableRow
monitorRemoteIpEntry = _MonitorRemoteIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 1, 1, 1)
)
monitorRemoteIpEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
    (0, "MOXA-NP6000-MIB", "remoteIpIndex"),
)
if mibBuilder.loadTexts:
    monitorRemoteIpEntry.setStatus("current")
_RemoteIpIndex_Type = Integer32
_RemoteIpIndex_Object = MibTableColumn
remoteIpIndex = _RemoteIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 1, 1, 1, 1),
    _RemoteIpIndex_Type()
)
remoteIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIpIndex.setStatus("current")
_MonitorRemoteIp_Type = DisplayString
_MonitorRemoteIp_Object = MibTableColumn
monitorRemoteIp = _MonitorRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 1, 1, 1, 2),
    _MonitorRemoteIp_Type()
)
monitorRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRemoteIp.setStatus("current")
_MonitorCipher_Type = DisplayString
_MonitorCipher_Object = MibTableColumn
monitorCipher = _MonitorCipher_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 1, 1, 1, 3),
    _MonitorCipher_Type()
)
monitorCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorCipher.setStatus("current")
_SerialPortStatus_ObjectIdentity = ObjectIdentity
serialPortStatus = _SerialPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 2)
)
_MonitorSerialPortStatusTable_Object = MibTable
monitorSerialPortStatusTable = _MonitorSerialPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    monitorSerialPortStatusTable.setStatus("current")
_MonitorSerialPortStatusEntry_Object = MibTableRow
monitorSerialPortStatusEntry = _MonitorSerialPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 2, 1, 1)
)
monitorSerialPortStatusEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSerialPortStatusEntry.setStatus("current")
_MonitorTxCount_Type = Integer32
_MonitorTxCount_Object = MibTableColumn
monitorTxCount = _MonitorTxCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 2, 1, 1, 1),
    _MonitorTxCount_Type()
)
monitorTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorTxCount.setStatus("current")
_MonitorRxCount_Type = Integer32
_MonitorRxCount_Object = MibTableColumn
monitorRxCount = _MonitorRxCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 2, 1, 1, 2),
    _MonitorRxCount_Type()
)
monitorRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRxCount.setStatus("current")
_MonitorTxTotalCount_Type = Integer32
_MonitorTxTotalCount_Object = MibTableColumn
monitorTxTotalCount = _MonitorTxTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 2, 1, 1, 3),
    _MonitorTxTotalCount_Type()
)
monitorTxTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorTxTotalCount.setStatus("current")
_MonitorRxTotalCount_Type = Integer32
_MonitorRxTotalCount_Object = MibTableColumn
monitorRxTotalCount = _MonitorRxTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 2, 1, 1, 4),
    _MonitorRxTotalCount_Type()
)
monitorRxTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRxTotalCount.setStatus("current")


class _MonitorDSR_Type(Integer32):
    """Custom type monitorDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorDSR_Type.__name__ = "Integer32"
_MonitorDSR_Object = MibTableColumn
monitorDSR = _MonitorDSR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 2, 1, 1, 5),
    _MonitorDSR_Type()
)
monitorDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDSR.setStatus("current")


class _MonitorDTR_Type(Integer32):
    """Custom type monitorDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorDTR_Type.__name__ = "Integer32"
_MonitorDTR_Object = MibTableColumn
monitorDTR = _MonitorDTR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 2, 1, 1, 6),
    _MonitorDTR_Type()
)
monitorDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDTR.setStatus("current")


class _MonitorRTS_Type(Integer32):
    """Custom type monitorRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorRTS_Type.__name__ = "Integer32"
_MonitorRTS_Object = MibTableColumn
monitorRTS = _MonitorRTS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 2, 1, 1, 7),
    _MonitorRTS_Type()
)
monitorRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRTS.setStatus("current")


class _MonitorCTS_Type(Integer32):
    """Custom type monitorCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorCTS_Type.__name__ = "Integer32"
_MonitorCTS_Object = MibTableColumn
monitorCTS = _MonitorCTS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 2, 1, 1, 8),
    _MonitorCTS_Type()
)
monitorCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorCTS.setStatus("current")


class _MonitorDCD_Type(Integer32):
    """Custom type monitorDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorDCD_Type.__name__ = "Integer32"
_MonitorDCD_Object = MibTableColumn
monitorDCD = _MonitorDCD_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 2, 1, 1, 9),
    _MonitorDCD_Type()
)
monitorDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDCD.setStatus("current")
_SerialPortErrorCount_ObjectIdentity = ObjectIdentity
serialPortErrorCount = _SerialPortErrorCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 3)
)
_MonitorSerialPortErrorCountTable_Object = MibTable
monitorSerialPortErrorCountTable = _MonitorSerialPortErrorCountTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    monitorSerialPortErrorCountTable.setStatus("current")
_MonitorSerialPortErrorCountEntry_Object = MibTableRow
monitorSerialPortErrorCountEntry = _MonitorSerialPortErrorCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 3, 1, 1)
)
monitorSerialPortErrorCountEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSerialPortErrorCountEntry.setStatus("current")
_MonitorErrorCountFrame_Type = Integer32
_MonitorErrorCountFrame_Object = MibTableColumn
monitorErrorCountFrame = _MonitorErrorCountFrame_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 3, 1, 1, 1),
    _MonitorErrorCountFrame_Type()
)
monitorErrorCountFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorErrorCountFrame.setStatus("current")
_MonitorErrorCountParity_Type = Integer32
_MonitorErrorCountParity_Object = MibTableColumn
monitorErrorCountParity = _MonitorErrorCountParity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 3, 1, 1, 2),
    _MonitorErrorCountParity_Type()
)
monitorErrorCountParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorErrorCountParity.setStatus("current")
_MonitorErrorCountOverrun_Type = Integer32
_MonitorErrorCountOverrun_Object = MibTableColumn
monitorErrorCountOverrun = _MonitorErrorCountOverrun_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 3, 1, 1, 3),
    _MonitorErrorCountOverrun_Type()
)
monitorErrorCountOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorErrorCountOverrun.setStatus("current")
_MonitorErrorCountBreak_Type = Integer32
_MonitorErrorCountBreak_Object = MibTableColumn
monitorErrorCountBreak = _MonitorErrorCountBreak_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 3, 1, 1, 4),
    _MonitorErrorCountBreak_Type()
)
monitorErrorCountBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorErrorCountBreak.setStatus("current")
_SerialPortSettings_ObjectIdentity = ObjectIdentity
serialPortSettings = _SerialPortSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4)
)
_MonitorSerialPortSettingsTable_Object = MibTable
monitorSerialPortSettingsTable = _MonitorSerialPortSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    monitorSerialPortSettingsTable.setStatus("current")
_MonitorSerialPortSettingsEntry_Object = MibTableRow
monitorSerialPortSettingsEntry = _MonitorSerialPortSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4, 1, 1)
)
monitorSerialPortSettingsEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSerialPortSettingsEntry.setStatus("current")
_MonitorBaudRate_Type = Integer32
_MonitorBaudRate_Object = MibTableColumn
monitorBaudRate = _MonitorBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4, 1, 1, 1),
    _MonitorBaudRate_Type()
)
monitorBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorBaudRate.setStatus("current")


class _MonitorDataBits_Type(Integer32):
    """Custom type monitorDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bits-5", 0),
          ("bits-6", 1),
          ("bits-7", 2),
          ("bits-8", 3))
    )


_MonitorDataBits_Type.__name__ = "Integer32"
_MonitorDataBits_Object = MibTableColumn
monitorDataBits = _MonitorDataBits_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4, 1, 1, 2),
    _MonitorDataBits_Type()
)
monitorDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDataBits.setStatus("current")
_MonitorStopBits_Type = DisplayString
_MonitorStopBits_Object = MibTableColumn
monitorStopBits = _MonitorStopBits_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4, 1, 1, 3),
    _MonitorStopBits_Type()
)
monitorStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorStopBits.setStatus("current")


class _MonitorParity_Type(Integer32):
    """Custom type monitorParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              24,
              40,
              56)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("odd", 8),
          ("even", 24),
          ("mark", 40),
          ("space", 56))
    )


_MonitorParity_Type.__name__ = "Integer32"
_MonitorParity_Object = MibTableColumn
monitorParity = _MonitorParity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4, 1, 1, 4),
    _MonitorParity_Type()
)
monitorParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorParity.setStatus("current")


class _MonitorRTSCTSFlowControl_Type(Integer32):
    """Custom type monitorRTSCTSFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorRTSCTSFlowControl_Type.__name__ = "Integer32"
_MonitorRTSCTSFlowControl_Object = MibTableColumn
monitorRTSCTSFlowControl = _MonitorRTSCTSFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4, 1, 1, 5),
    _MonitorRTSCTSFlowControl_Type()
)
monitorRTSCTSFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRTSCTSFlowControl.setStatus("current")


class _MonitorXONXOFFFlowControl_Type(Integer32):
    """Custom type monitorXONXOFFFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorXONXOFFFlowControl_Type.__name__ = "Integer32"
_MonitorXONXOFFFlowControl_Object = MibTableColumn
monitorXONXOFFFlowControl = _MonitorXONXOFFFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4, 1, 1, 6),
    _MonitorXONXOFFFlowControl_Type()
)
monitorXONXOFFFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorXONXOFFFlowControl.setStatus("current")


class _MonitorDTRDSRFlowControl_Type(Integer32):
    """Custom type monitorDTRDSRFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorDTRDSRFlowControl_Type.__name__ = "Integer32"
_MonitorDTRDSRFlowControl_Object = MibTableColumn
monitorDTRDSRFlowControl = _MonitorDTRDSRFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4, 1, 1, 7),
    _MonitorDTRDSRFlowControl_Type()
)
monitorDTRDSRFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDTRDSRFlowControl.setStatus("current")


class _MonitorRTSToggleFlowControl_Type(Integer32):
    """Custom type monitorRTSToggleFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorRTSToggleFlowControl_Type.__name__ = "Integer32"
_MonitorRTSToggleFlowControl_Object = MibTableColumn
monitorRTSToggleFlowControl = _MonitorRTSToggleFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4, 1, 1, 8),
    _MonitorRTSToggleFlowControl_Type()
)
monitorRTSToggleFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRTSToggleFlowControl.setStatus("current")


class _MonitorFIFO_Type(Integer32):
    """Custom type monitorFIFO based on Integer32"""
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


_MonitorFIFO_Type.__name__ = "Integer32"
_MonitorFIFO_Object = MibTableColumn
monitorFIFO = _MonitorFIFO_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4, 1, 1, 9),
    _MonitorFIFO_Type()
)
monitorFIFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFIFO.setStatus("current")


class _MonitorInterface_Type(Integer32):
    """Custom type monitorInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs-232", 0),
          ("rs-422", 1),
          ("rs-485-2-wire", 2),
          ("rs-485-4-wire", 3))
    )


_MonitorInterface_Type.__name__ = "Integer32"
_MonitorInterface_Object = MibTableColumn
monitorInterface = _MonitorInterface_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 4, 1, 1, 10),
    _MonitorInterface_Type()
)
monitorInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorInterface.setStatus("current")
_SerialPortBuffering_ObjectIdentity = ObjectIdentity
serialPortBuffering = _SerialPortBuffering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 5)
)
_MonitorSerialPortBufferingTable_Object = MibTable
monitorSerialPortBufferingTable = _MonitorSerialPortBufferingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    monitorSerialPortBufferingTable.setStatus("current")
_MonitorSerialPortBufferingEntry_Object = MibTableRow
monitorSerialPortBufferingEntry = _MonitorSerialPortBufferingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 5, 1, 1)
)
monitorSerialPortBufferingEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSerialPortBufferingEntry.setStatus("current")
_MonitorBuffering_Type = Integer32
_MonitorBuffering_Object = MibTableColumn
monitorBuffering = _MonitorBuffering_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 5, 1, 1, 1),
    _MonitorBuffering_Type()
)
monitorBuffering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorBuffering.setStatus("current")
_RelayOutputStatus_ObjectIdentity = ObjectIdentity
relayOutputStatus = _RelayOutputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6)
)


class _RelayOutputEthernet1LinkDown_Type(Integer32):
    """Custom type relayOutputEthernet1LinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("alarm", 1),
          ("alarm-Acked", 2))
    )


_RelayOutputEthernet1LinkDown_Type.__name__ = "Integer32"
_RelayOutputEthernet1LinkDown_Object = MibScalar
relayOutputEthernet1LinkDown = _RelayOutputEthernet1LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 1),
    _RelayOutputEthernet1LinkDown_Type()
)
relayOutputEthernet1LinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayOutputEthernet1LinkDown.setStatus("current")


class _Ethernet1LinkDownAcknowledge_Type(Integer32):
    """Custom type ethernet1LinkDownAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("acked", 0)
    )


_Ethernet1LinkDownAcknowledge_Type.__name__ = "Integer32"
_Ethernet1LinkDownAcknowledge_Object = MibScalar
ethernet1LinkDownAcknowledge = _Ethernet1LinkDownAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 2),
    _Ethernet1LinkDownAcknowledge_Type()
)
ethernet1LinkDownAcknowledge.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ethernet1LinkDownAcknowledge.setStatus("current")


class _RelayOutputEthernet2LinkDown_Type(Integer32):
    """Custom type relayOutputEthernet2LinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("alarm", 1),
          ("alarm-Acked", 2))
    )


_RelayOutputEthernet2LinkDown_Type.__name__ = "Integer32"
_RelayOutputEthernet2LinkDown_Object = MibScalar
relayOutputEthernet2LinkDown = _RelayOutputEthernet2LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 3),
    _RelayOutputEthernet2LinkDown_Type()
)
relayOutputEthernet2LinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayOutputEthernet2LinkDown.setStatus("current")


class _Ethernet2LinkDownAcknowledge_Type(Integer32):
    """Custom type ethernet2LinkDownAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("acked", 0)
    )


_Ethernet2LinkDownAcknowledge_Type.__name__ = "Integer32"
_Ethernet2LinkDownAcknowledge_Object = MibScalar
ethernet2LinkDownAcknowledge = _Ethernet2LinkDownAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 4),
    _Ethernet2LinkDownAcknowledge_Type()
)
ethernet2LinkDownAcknowledge.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ethernet2LinkDownAcknowledge.setStatus("current")


class _RelayOutputEthernet3LinkDown_Type(Integer32):
    """Custom type relayOutputEthernet3LinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("alarm", 1),
          ("alarm-Acked", 2))
    )


_RelayOutputEthernet3LinkDown_Type.__name__ = "Integer32"
_RelayOutputEthernet3LinkDown_Object = MibScalar
relayOutputEthernet3LinkDown = _RelayOutputEthernet3LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 5),
    _RelayOutputEthernet3LinkDown_Type()
)
relayOutputEthernet3LinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayOutputEthernet3LinkDown.setStatus("current")


class _Ethernet3LinkDownAcknowledge_Type(Integer32):
    """Custom type ethernet3LinkDownAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("acked", 0)
    )


_Ethernet3LinkDownAcknowledge_Type.__name__ = "Integer32"
_Ethernet3LinkDownAcknowledge_Object = MibScalar
ethernet3LinkDownAcknowledge = _Ethernet3LinkDownAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 6),
    _Ethernet3LinkDownAcknowledge_Type()
)
ethernet3LinkDownAcknowledge.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ethernet3LinkDownAcknowledge.setStatus("current")
_PortDCDChangedStatusTable_Object = MibTable
portDCDChangedStatusTable = _PortDCDChangedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 7)
)
if mibBuilder.loadTexts:
    portDCDChangedStatusTable.setStatus("current")
_PortDCDChangedStatusEntry_Object = MibTableRow
portDCDChangedStatusEntry = _PortDCDChangedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 7, 1)
)
portDCDChangedStatusEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portDCDChangedStatusEntry.setStatus("current")


class _PortDCDChangedStatus_Type(Integer32):
    """Custom type portDCDChangedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("alarm", 1),
          ("alarm-Acked", 2))
    )


_PortDCDChangedStatus_Type.__name__ = "Integer32"
_PortDCDChangedStatus_Object = MibTableColumn
portDCDChangedStatus = _PortDCDChangedStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 7, 1, 1),
    _PortDCDChangedStatus_Type()
)
portDCDChangedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDCDChangedStatus.setStatus("current")


class _PortDCDChangedAcknowledge_Type(Integer32):
    """Custom type portDCDChangedAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("acked", 0)
    )


_PortDCDChangedAcknowledge_Type.__name__ = "Integer32"
_PortDCDChangedAcknowledge_Object = MibTableColumn
portDCDChangedAcknowledge = _PortDCDChangedAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 7, 1, 2),
    _PortDCDChangedAcknowledge_Type()
)
portDCDChangedAcknowledge.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    portDCDChangedAcknowledge.setStatus("current")
_PortDSRChangedStatusTable_Object = MibTable
portDSRChangedStatusTable = _PortDSRChangedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 8)
)
if mibBuilder.loadTexts:
    portDSRChangedStatusTable.setStatus("current")
_PortDSRChangedStatusEntry_Object = MibTableRow
portDSRChangedStatusEntry = _PortDSRChangedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 8, 1)
)
portDSRChangedStatusEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portDSRChangedStatusEntry.setStatus("current")


class _PortDSRChangedStatus_Type(Integer32):
    """Custom type portDSRChangedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("alarm", 1),
          ("alarm-Acked", 2))
    )


_PortDSRChangedStatus_Type.__name__ = "Integer32"
_PortDSRChangedStatus_Object = MibTableColumn
portDSRChangedStatus = _PortDSRChangedStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 8, 1, 1),
    _PortDSRChangedStatus_Type()
)
portDSRChangedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDSRChangedStatus.setStatus("current")


class _PortDSRChangedAcknowledge_Type(Integer32):
    """Custom type portDSRChangedAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("acked", 0)
    )


_PortDSRChangedAcknowledge_Type.__name__ = "Integer32"
_PortDSRChangedAcknowledge_Object = MibTableColumn
portDSRChangedAcknowledge = _PortDSRChangedAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 6, 8, 1, 2),
    _PortDSRChangedAcknowledge_Type()
)
portDSRChangedAcknowledge.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    portDSRChangedAcknowledge.setStatus("current")
_ModuleStatus_ObjectIdentity = ObjectIdentity
moduleStatus = _ModuleStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7)
)
_RedundancyStatus_ObjectIdentity = ObjectIdentity
redundancyStatus = _RedundancyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1)
)


class _ActiveRedundancyProtocol_Type(Integer32):
    """Custom type activeRedundancyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("spanningTree", 1),
          ("turboRing", 2),
          ("turboRingV2", 3))
    )


_ActiveRedundancyProtocol_Type.__name__ = "Integer32"
_ActiveRedundancyProtocol_Object = MibScalar
activeRedundancyProtocol = _ActiveRedundancyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 1),
    _ActiveRedundancyProtocol_Type()
)
activeRedundancyProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeRedundancyProtocol.setStatus("current")
_SpanningTreeStatus_ObjectIdentity = ObjectIdentity
spanningTreeStatus = _SpanningTreeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 2)
)
_SpanningTreeBridgeRole_Type = DisplayString
_SpanningTreeBridgeRole_Object = MibScalar
spanningTreeBridgeRole = _SpanningTreeBridgeRole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 2, 1),
    _SpanningTreeBridgeRole_Type()
)
spanningTreeBridgeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreeBridgeRole.setStatus("current")
_SpanningTreeRootBridge_Type = DisplayString
_SpanningTreeRootBridge_Object = MibScalar
spanningTreeRootBridge = _SpanningTreeRootBridge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 2, 2),
    _SpanningTreeRootBridge_Type()
)
spanningTreeRootBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreeRootBridge.setStatus("current")
_SpanningTreeRootPathCost_Type = DisplayString
_SpanningTreeRootPathCost_Object = MibScalar
spanningTreeRootPathCost = _SpanningTreeRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 2, 3),
    _SpanningTreeRootPathCost_Type()
)
spanningTreeRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreeRootPathCost.setStatus("current")
_SpanningTreePortStatusTable_Object = MibTable
spanningTreePortStatusTable = _SpanningTreePortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 2, 4)
)
if mibBuilder.loadTexts:
    spanningTreePortStatusTable.setStatus("current")
_SpanningTreePortStatusEntry_Object = MibTableRow
spanningTreePortStatusEntry = _SpanningTreePortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 2, 4, 1)
)
spanningTreePortStatusEntry.setIndexNames(
    (0, "MOXA-NP6000-MIB", "spanningTreePortStatusIndex"),
)
if mibBuilder.loadTexts:
    spanningTreePortStatusEntry.setStatus("current")
_SpanningTreePortStatusIndex_Type = Integer32
_SpanningTreePortStatusIndex_Object = MibTableColumn
spanningTreePortStatusIndex = _SpanningTreePortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 2, 4, 1, 1),
    _SpanningTreePortStatusIndex_Type()
)
spanningTreePortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreePortStatusIndex.setStatus("current")


class _SpanningTreePortEnableStatus_Type(Integer32):
    """Custom type spanningTreePortEnableStatus based on Integer32"""
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


_SpanningTreePortEnableStatus_Type.__name__ = "Integer32"
_SpanningTreePortEnableStatus_Object = MibTableColumn
spanningTreePortEnableStatus = _SpanningTreePortEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 2, 4, 1, 2),
    _SpanningTreePortEnableStatus_Type()
)
spanningTreePortEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreePortEnableStatus.setStatus("current")
_SpanningTreePortRole_Type = DisplayString
_SpanningTreePortRole_Object = MibTableColumn
spanningTreePortRole = _SpanningTreePortRole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 2, 4, 1, 3),
    _SpanningTreePortRole_Type()
)
spanningTreePortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreePortRole.setStatus("current")
_SpanningTreePortDesignatedBridge_Type = DisplayString
_SpanningTreePortDesignatedBridge_Object = MibTableColumn
spanningTreePortDesignatedBridge = _SpanningTreePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 2, 4, 1, 4),
    _SpanningTreePortDesignatedBridge_Type()
)
spanningTreePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreePortDesignatedBridge.setStatus("current")
_SpanningTreePortStatus_Type = DisplayString
_SpanningTreePortStatus_Object = MibTableColumn
spanningTreePortStatus = _SpanningTreePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 2, 4, 1, 5),
    _SpanningTreePortStatus_Type()
)
spanningTreePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreePortStatus.setStatus("current")
_TurboRingStatus_ObjectIdentity = ObjectIdentity
turboRingStatus = _TurboRingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 3)
)


class _TurboRingBrokenStatus_Type(Integer32):
    """Custom type turboRingBrokenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notTurboRingV2", 0),
          ("healthy", 1),
          ("break", 2))
    )


_TurboRingBrokenStatus_Type.__name__ = "Integer32"
_TurboRingBrokenStatus_Object = MibScalar
turboRingBrokenStatus = _TurboRingBrokenStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 3, 1),
    _TurboRingBrokenStatus_Type()
)
turboRingBrokenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingBrokenStatus.setStatus("current")


class _TurboRingMaster_Type(Integer32):
    """Custom type turboRingMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TurboRingMaster_Type.__name__ = "Integer32"
_TurboRingMaster_Object = MibScalar
turboRingMaster = _TurboRingMaster_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 3, 2),
    _TurboRingMaster_Type()
)
turboRingMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingMaster.setStatus("current")
_TurboRingPort1_Type = Integer32
_TurboRingPort1_Object = MibScalar
turboRingPort1 = _TurboRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 3, 3),
    _TurboRingPort1_Type()
)
turboRingPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPort1.setStatus("current")
_TurboRingPort2_Type = Integer32
_TurboRingPort2_Object = MibScalar
turboRingPort2 = _TurboRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 3, 4),
    _TurboRingPort2_Type()
)
turboRingPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPort2.setStatus("current")
_TurboRingPort1Status_Type = DisplayString
_TurboRingPort1Status_Object = MibScalar
turboRingPort1Status = _TurboRingPort1Status_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 3, 5),
    _TurboRingPort1Status_Type()
)
turboRingPort1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPort1Status.setStatus("current")
_TurboRingPort2Status_Type = DisplayString
_TurboRingPort2Status_Object = MibScalar
turboRingPort2Status = _TurboRingPort2Status_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 6, 7, 1, 3, 6),
    _TurboRingPort2Status_Type()
)
turboRingPort2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPort2Status.setStatus("current")
_SaveConfiguration_ObjectIdentity = ObjectIdentity
saveConfiguration = _SaveConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 7)
)


class _SaveConfig_Type(Integer32):
    """Custom type saveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_SaveConfig_Type.__name__ = "Integer32"
_SaveConfig_Object = MibScalar
saveConfig = _SaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 7, 1),
    _SaveConfig_Type()
)
saveConfig.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    saveConfig.setStatus("current")
_Restart_ObjectIdentity = ObjectIdentity
restart = _Restart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 8)
)


class _RestartPorts_Type(Integer32):
    """Custom type restartPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port17", 16),
          ("port18", 17),
          ("port19", 18),
          ("port20", 19),
          ("port21", 20),
          ("port22", 21),
          ("port23", 22),
          ("port24", 23),
          ("port25", 24),
          ("port26", 25),
          ("port27", 26),
          ("port28", 27),
          ("port29", 28),
          ("port30", 29),
          ("port31", 30),
          ("port32", 31))
    )


_RestartPorts_Type.__name__ = "Integer32"
_RestartPorts_Object = MibScalar
restartPorts = _RestartPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 8, 1),
    _RestartPorts_Type()
)
restartPorts.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    restartPorts.setStatus("current")


class _RestartSystem_Type(Integer32):
    """Custom type restartSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_RestartSystem_Type.__name__ = "Integer32"
_RestartSystem_Object = MibScalar
restartSystem = _RestartSystem_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 8, 1, 8, 2),
    _RestartSystem_Type()
)
restartSystem.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    restartSystem.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-NP6000-MIB",
    **{"PortList": PortList,
       "moxa": moxa,
       "nport": nport,
       "np6000": np6000,
       "swMgmt": swMgmt,
       "overview": overview,
       "modelName": modelName,
       "serialNumber": serialNumber,
       "firmwareVersion": firmwareVersion,
       "macAddress": macAddress,
       "viewLanSpeed": viewLanSpeed,
       "viewLanModuleSpeed": viewLanModuleSpeed,
       "upTime": upTime,
       "moduleType": moduleType,
       "moduleApVersion": moduleApVersion,
       "viewIpv4Address": viewIpv4Address,
       "viewIpv6LinkLocalAddress": viewIpv6LinkLocalAddress,
       "viewIpv6GlobalAddress": viewIpv6GlobalAddress,
       "basicSetting": basicSetting,
       "serverSetting": serverSetting,
       "serverName": serverName,
       "serverLocation": serverLocation,
       "timeSetting": timeSetting,
       "timeZone": timeZone,
       "localTime": localTime,
       "timeServer": timeServer,
       "networkSetting": networkSetting,
       "ipv4Configuration": ipv4Configuration,
       "ipv4Address": ipv4Address,
       "ipv4NetMask": ipv4NetMask,
       "ipv4DefaultGateway": ipv4DefaultGateway,
       "ipv4DnsServer1IpAddr": ipv4DnsServer1IpAddr,
       "ipv4DnsServer2IpAddr": ipv4DnsServer2IpAddr,
       "ipv4PppoeUserAccount": ipv4PppoeUserAccount,
       "ipv4PppoePassword": ipv4PppoePassword,
       "ipv4WinsFunction": ipv4WinsFunction,
       "ipv4WinsServer": ipv4WinsServer,
       "lan1Speed": lan1Speed,
       "routingProtocol": routingProtocol,
       "gratuitousArp": gratuitousArp,
       "gratuitousArpSendPeriod": gratuitousArpSendPeriod,
       "moduleSetting": moduleSetting,
       "redundancySetting": redundancySetting,
       "redundancyProtocol": redundancyProtocol,
       "spanningTree": spanningTree,
       "spanningTreeBridgePriority": spanningTreeBridgePriority,
       "spanningTreeHelloTime": spanningTreeHelloTime,
       "spanningTreeForwardingDelay": spanningTreeForwardingDelay,
       "spanningTreeMaxAge": spanningTreeMaxAge,
       "spanningTreePortTable": spanningTreePortTable,
       "spanningTreePortEntry": spanningTreePortEntry,
       "spanningTreePortIndex": spanningTreePortIndex,
       "spanningTreePortEnable": spanningTreePortEnable,
       "spanningTreePortPriority": spanningTreePortPriority,
       "spanningTreePortCost": spanningTreePortCost,
       "turboRing": turboRing,
       "turboRingMasterSetup": turboRingMasterSetup,
       "turboRingRdntPort1": turboRingRdntPort1,
       "turboRingRdntPort2": turboRingRdntPort2,
       "turboRingV2": turboRingV2,
       "turboRingV2MasterSetup": turboRingV2MasterSetup,
       "turboRingV2RdntPort1": turboRingV2RdntPort1,
       "turboRingV2RdntPort2": turboRingV2RdntPort2,
       "gsmGprsSetting": gsmGprsSetting,
       "gsmGprsType": gsmGprsType,
       "gsmGprsPIN": gsmGprsPIN,
       "gsmGprsBand": gsmGprsBand,
       "gsmSetting": gsmSetting,
       "gsmMode": gsmMode,
       "gsmDestinationIpAddress": gsmDestinationIpAddress,
       "gsmSourceIpAddress": gsmSourceIpAddress,
       "gsmIpNetmask": gsmIpNetmask,
       "gsmTcpIpCompression": gsmTcpIpCompression,
       "gsmInactivityTime": gsmInactivityTime,
       "gsmLinkQualityReport": gsmLinkQualityReport,
       "gsmUsername": gsmUsername,
       "gsmPassword": gsmPassword,
       "gsmAuthenticationType": gsmAuthenticationType,
       "gsmTryNextAuth": gsmTryNextAuth,
       "gsmOutPhoneNumber": gsmOutPhoneNumber,
       "gsmInitialString": gsmInitialString,
       "gsmConnectionControl": gsmConnectionControl,
       "gsmConnectionInterval": gsmConnectionInterval,
       "gsmPingRemoteHost": gsmPingRemoteHost,
       "gsmInPhoneNumber": gsmInPhoneNumber,
       "gprsSetting": gprsSetting,
       "gprsTcpIpCompression": gprsTcpIpCompression,
       "gprsInactivityTime": gprsInactivityTime,
       "gprsLinkQualityReport": gprsLinkQualityReport,
       "gprsInitialString": gprsInitialString,
       "gprsUsername": gprsUsername,
       "gprsPassword": gprsPassword,
       "gprsAPN": gprsAPN,
       "gprsConnectionControl": gprsConnectionControl,
       "gprsConnectionInterval": gprsConnectionInterval,
       "gprsPingRemoteHost": gprsPingRemoteHost,
       "smsSetting": smsSetting,
       "smsFormat": smsFormat,
       "v92ModemSetting": v92ModemSetting,
       "v92ModemMode": v92ModemMode,
       "v92ModemDestinationIpAddress": v92ModemDestinationIpAddress,
       "v92ModemSourceIpAddress": v92ModemSourceIpAddress,
       "v92ModemIpNetmask": v92ModemIpNetmask,
       "v92ModemTcpIpCompression": v92ModemTcpIpCompression,
       "v92ModemInactivityTime": v92ModemInactivityTime,
       "v92ModemLinkQualityReport": v92ModemLinkQualityReport,
       "v92ModemUsername": v92ModemUsername,
       "v92ModemPassword": v92ModemPassword,
       "v92ModemIncomingPAPCheck": v92ModemIncomingPAPCheck,
       "v92ModemIncomingTryNextAuth": v92ModemIncomingTryNextAuth,
       "v92ModemPhoneNumber": v92ModemPhoneNumber,
       "v92ModemInitialString": v92ModemInitialString,
       "v92ModemConnectionControl": v92ModemConnectionControl,
       "v92ModemConnectionInterval": v92ModemConnectionInterval,
       "v92ModemPingRemoteHost": v92ModemPingRemoteHost,
       "ipv6Configuration": ipv6Configuration,
       "ipv6Address": ipv6Address,
       "ipv6Prefix": ipv6Prefix,
       "ipv6DefaultGateway": ipv6DefaultGateway,
       "ipv6DnsServer1IpAddr": ipv6DnsServer1IpAddr,
       "ipv6DnsServer2IpAddr": ipv6DnsServer2IpAddr,
       "connectionPriority": connectionPriority,
       "portSetting": portSetting,
       "opModeSetting": opModeSetting,
       "opMode": opMode,
       "opModePortTable": opModePortTable,
       "opModePortEntry": opModePortEntry,
       "portIndex": portIndex,
       "portApplication": portApplication,
       "portMode": portMode,
       "application": application,
       "deviceControl": deviceControl,
       "deviceControlTable": deviceControlTable,
       "deviceControlEntry": deviceControlEntry,
       "deviceControlTcpAliveCheck": deviceControlTcpAliveCheck,
       "deviceControlMaxConnection": deviceControlMaxConnection,
       "deviceControlIgnoreJammedIp": deviceControlIgnoreJammedIp,
       "deviceControlAllowDriverControl": deviceControlAllowDriverControl,
       "deviceControlCommandByCommandOperation": deviceControlCommandByCommandOperation,
       "deviceControlSecure": deviceControlSecure,
       "deviceControlConnectionDownRTS": deviceControlConnectionDownRTS,
       "deviceControlConnectionDownDTR": deviceControlConnectionDownDTR,
       "deviceControlResponseTimeout": deviceControlResponseTimeout,
       "deviceControlNonRequestSerialData": deviceControlNonRequestSerialData,
       "deviceControlTcpPort": deviceControlTcpPort,
       "deviceControlDestinationAddress1": deviceControlDestinationAddress1,
       "deviceControlDestinationTcpPort1": deviceControlDestinationTcpPort1,
       "deviceControlDestinationCmdPort1": deviceControlDestinationCmdPort1,
       "deviceControlDestinationAddress2": deviceControlDestinationAddress2,
       "deviceControlDestinationTcpPort2": deviceControlDestinationTcpPort2,
       "deviceControlDestinationCmdPort2": deviceControlDestinationCmdPort2,
       "deviceControlDesignatedLocalTcpPort1": deviceControlDesignatedLocalTcpPort1,
       "deviceControlDesignatedLocalCmdPort1": deviceControlDesignatedLocalCmdPort1,
       "deviceControlDesignatedLocalTcpPort2": deviceControlDesignatedLocalTcpPort2,
       "deviceControlDesignatedLocalCmdPort2": deviceControlDesignatedLocalCmdPort2,
       "socket": socket,
       "socketTable": socketTable,
       "socketEntry": socketEntry,
       "socketTcpAliveCheck": socketTcpAliveCheck,
       "socketInactivityTime": socketInactivityTime,
       "socketMaxConnection": socketMaxConnection,
       "socketIgnoreJammedIp": socketIgnoreJammedIp,
       "socketAllowDriverControl": socketAllowDriverControl,
       "socketCommandByCommandOperation": socketCommandByCommandOperation,
       "socketSecure": socketSecure,
       "socketTcpPort": socketTcpPort,
       "socketCmdPort": socketCmdPort,
       "socketTcpServerConnectionDownRTS": socketTcpServerConnectionDownRTS,
       "socketTcpServerConnectionDownDTR": socketTcpServerConnectionDownDTR,
       "socketResponseTimeout": socketResponseTimeout,
       "socketNonRequestSerialData": socketNonRequestSerialData,
       "socketTcpClientDestinationAddress1": socketTcpClientDestinationAddress1,
       "socketTcpClientDestinationPort1": socketTcpClientDestinationPort1,
       "socketTcpClientDestinationAddress2": socketTcpClientDestinationAddress2,
       "socketTcpClientDestinationPort2": socketTcpClientDestinationPort2,
       "socketTcpClientDestinationAddress3": socketTcpClientDestinationAddress3,
       "socketTcpClientDestinationPort3": socketTcpClientDestinationPort3,
       "socketTcpClientDestinationAddress4": socketTcpClientDestinationAddress4,
       "socketTcpClientDestinationPort4": socketTcpClientDestinationPort4,
       "socketTcpClientDesignatedLocalPort1": socketTcpClientDesignatedLocalPort1,
       "socketTcpClientDesignatedLocalPort2": socketTcpClientDesignatedLocalPort2,
       "socketTcpClientDesignatedLocalPort3": socketTcpClientDesignatedLocalPort3,
       "socketTcpClientDesignatedLocalPort4": socketTcpClientDesignatedLocalPort4,
       "socketTcpClientConnectionControl": socketTcpClientConnectionControl,
       "socketUdpDestinationAddress1Begin": socketUdpDestinationAddress1Begin,
       "socketUdpDestinationAddress1End": socketUdpDestinationAddress1End,
       "socketUdpDestinationPort1": socketUdpDestinationPort1,
       "socketUdpDestinationAddress2Begin": socketUdpDestinationAddress2Begin,
       "socketUdpDestinationAddress2End": socketUdpDestinationAddress2End,
       "socketUdpDestinationPort2": socketUdpDestinationPort2,
       "socketUdpDestinationAddress3Begin": socketUdpDestinationAddress3Begin,
       "socketUdpDestinationAddress3End": socketUdpDestinationAddress3End,
       "socketUdpDestinationPort3": socketUdpDestinationPort3,
       "socketUdpDestinationAddress4Begin": socketUdpDestinationAddress4Begin,
       "socketUdpDestinationAddress4End": socketUdpDestinationAddress4End,
       "socketUdpDestinationPort4": socketUdpDestinationPort4,
       "socketUdpLocalListenPort": socketUdpLocalListenPort,
       "socketUDPDynamicDst": socketUDPDynamicDst,
       "socketUDPDynamicDstTimeout": socketUDPDynamicDstTimeout,
       "pairConnection": pairConnection,
       "pairConnectionTable": pairConnectionTable,
       "pairConnectionEntry": pairConnectionEntry,
       "pairConnectionTcpAliveCheck": pairConnectionTcpAliveCheck,
       "pairConnectionSecure": pairConnectionSecure,
       "pairConnectionDestinationAddress": pairConnectionDestinationAddress,
       "pairConnectionDestinationPort": pairConnectionDestinationPort,
       "pairConnectionTcpPort": pairConnectionTcpPort,
       "ethernetModem": ethernetModem,
       "ethernetModemTable": ethernetModemTable,
       "ethernetModemEntry": ethernetModemEntry,
       "ethernetModemTcpAliveCheck": ethernetModemTcpAliveCheck,
       "ethernetModemTcpPort": ethernetModemTcpPort,
       "terminal": terminal,
       "terminalTable": terminalTable,
       "terminalEntry": terminalEntry,
       "terminalTcpAliveCheck": terminalTcpAliveCheck,
       "terminalInactivityTime": terminalInactivityTime,
       "terminalAutoLinkProtocol": terminalAutoLinkProtocol,
       "terminalPrimaryHostAddress": terminalPrimaryHostAddress,
       "terminalSecondHostAddress": terminalSecondHostAddress,
       "terminalTelnetTcpPort": terminalTelnetTcpPort,
       "terminalSshTcpPort": terminalSshTcpPort,
       "terminalType": terminalType,
       "terminalMaxSessions": terminalMaxSessions,
       "terminalChangeSession": terminalChangeSession,
       "terminalQuit": terminalQuit,
       "terminalBreak": terminalBreak,
       "terminalInterrupt": terminalInterrupt,
       "terminalAuthenticationType": terminalAuthenticationType,
       "terminalTryNextAuth": terminalTryNextAuth,
       "terminalAutoLoginPrompt": terminalAutoLoginPrompt,
       "terminalPasswordPrompt": terminalPasswordPrompt,
       "terminalLoginUserName": terminalLoginUserName,
       "terminalLoginPassword": terminalLoginPassword,
       "reverseTerminal": reverseTerminal,
       "reverseTerminalTable": reverseTerminalTable,
       "reverseTerminalEntry": reverseTerminalEntry,
       "reverseTerminalTcpAliveCheck": reverseTerminalTcpAliveCheck,
       "reverseTerminalInactivityTime": reverseTerminalInactivityTime,
       "reverseTerminalTcpPort": reverseTerminalTcpPort,
       "reverseTerminalAuthenticationType": reverseTerminalAuthenticationType,
       "reverseTerminalTryNextAuth": reverseTerminalTryNextAuth,
       "reverseTerminalMapKeys": reverseTerminalMapKeys,
       "printer": printer,
       "printerTable": printerTable,
       "printerEntry": printerEntry,
       "printerTcpAliveCheck": printerTcpAliveCheck,
       "printerTcpPort": printerTcpPort,
       "printerGroup": printerGroup,
       "printerQueueNameRaw": printerQueueNameRaw,
       "printerQueueNameASCII": printerQueueNameASCII,
       "printerAppendFormFeed": printerAppendFormFeed,
       "dial": dial,
       "dialTable": dialTable,
       "dialEntry": dialEntry,
       "dialTERMBINMode": dialTERMBINMode,
       "dialPPPDMode": dialPPPDMode,
       "dialSLIPDMode": dialSLIPDMode,
       "dialAuthType": dialAuthType,
       "dialTryNextAuth": dialTryNextAuth,
       "dialDisconnectBy": dialDisconnectBy,
       "dialDestinationIpAddress": dialDestinationIpAddress,
       "dialSourceIpAddress": dialSourceIpAddress,
       "dialIpNetmask": dialIpNetmask,
       "dialTcpIpCompression": dialTcpIpCompression,
       "dialInactivityTime": dialInactivityTime,
       "dialLinkQualityReport": dialLinkQualityReport,
       "dialUsername": dialUsername,
       "dialPassword": dialPassword,
       "dialIncomingPAPCheck": dialIncomingPAPCheck,
       "dialIncomingTryNextAuth": dialIncomingTryNextAuth,
       "dataPacking": dataPacking,
       "dataPackingPortTable": dataPackingPortTable,
       "dataPackingPortEntry": dataPackingPortEntry,
       "portPacketLength": portPacketLength,
       "portDelimiter1Enable": portDelimiter1Enable,
       "portDelimiter1": portDelimiter1,
       "portDelimiter2Enable": portDelimiter2Enable,
       "portDelimiter2": portDelimiter2,
       "portDelimiterProcess": portDelimiterProcess,
       "portForceTransmit": portForceTransmit,
       "comParamSetting": comParamSetting,
       "comParamPortTable": comParamPortTable,
       "comParamPortEntry": comParamPortEntry,
       "portAlias": portAlias,
       "portInterface": portInterface,
       "portBaudRate": portBaudRate,
       "portBaudRateManual": portBaudRateManual,
       "portDataBits": portDataBits,
       "portStopBits": portStopBits,
       "portParity": portParity,
       "portFlowControl": portFlowControl,
       "portFIFO": portFIFO,
       "portOnDelay": portOnDelay,
       "portOffDelay": portOffDelay,
       "dataBuffering": dataBuffering,
       "dataBufferingPortTable": dataBufferingPortTable,
       "dataBufferingPortEntry": dataBufferingPortEntry,
       "portBufferingEnable": portBufferingEnable,
       "portBufferingLocation": portBufferingLocation,
       "portBufferingSDFileSize": portBufferingSDFileSize,
       "portSerialDataLoggingEnable": portSerialDataLoggingEnable,
       "modemSettings": modemSettings,
       "modemSettingsPortTable": modemSettingsPortTable,
       "modemSettingsPortEntry": modemSettingsPortEntry,
       "portEnableModem": portEnableModem,
       "portInitialString": portInitialString,
       "portDialUp": portDialUp,
       "portPhoneNumber": portPhoneNumber,
       "cipherSettings": cipherSettings,
       "cipherSettingsPortTable": cipherSettingsPortTable,
       "cipherSettingsPortEntry": cipherSettingsPortEntry,
       "sslCipherSort": sslCipherSort,
       "sshCipherSort": sshCipherSort,
       "welcomeMessage": welcomeMessage,
       "portEnableWelcomeMessage": portEnableWelcomeMessage,
       "portMessage": portMessage,
       "sysManagement": sysManagement,
       "miscNetworkSettings": miscNetworkSettings,
       "accessibleIp": accessibleIp,
       "enableAccessibleIpList": enableAccessibleIpList,
       "accessibleIpListTable": accessibleIpListTable,
       "accessibleIpListEntry": accessibleIpListEntry,
       "accessibleIpListIndex": accessibleIpListIndex,
       "activeAccessibleIpList": activeAccessibleIpList,
       "accessibleIpListAddress": accessibleIpListAddress,
       "accessibleIpListNetmask": accessibleIpListNetmask,
       "snmpAgentSettings": snmpAgentSettings,
       "snmpEnable": snmpEnable,
       "snmpContactName": snmpContactName,
       "snmpLocation": snmpLocation,
       "dDNS": dDNS,
       "dDNSEnable": dDNSEnable,
       "dDNSServerAddress": dDNSServerAddress,
       "dDNSHostName": dDNSHostName,
       "dDNSUserName": dDNSUserName,
       "dDNSPassword": dDNSPassword,
       "hostTable": hostTable,
       "hostTableTable": hostTableTable,
       "hostTableEntry": hostTableEntry,
       "hostTableIndex": hostTableIndex,
       "hostName": hostName,
       "hostIpAddress": hostIpAddress,
       "routeTable": routeTable,
       "routeTableTable": routeTableTable,
       "routeTableEntry": routeTableEntry,
       "routeTableIndex": routeTableIndex,
       "gatewayRouteTable": gatewayRouteTable,
       "destinationRouteTable": destinationRouteTable,
       "netmaskRouteTable": netmaskRouteTable,
       "metricRouteTable": metricRouteTable,
       "interfaceRouteTable": interfaceRouteTable,
       "userTable": userTable,
       "userTableTable": userTableTable,
       "userTableEntry": userTableEntry,
       "userTableIndex": userTableIndex,
       "userNameUserTable": userNameUserTable,
       "passwordUserTable": passwordUserTable,
       "phoneNumberUserTable": phoneNumberUserTable,
       "authenticationServer": authenticationServer,
       "radiusServerIp": radiusServerIp,
       "radiusKey": radiusKey,
       "udpPortAuthenticationServer": udpPortAuthenticationServer,
       "radiusAccounting": radiusAccounting,
       "tacacsPlusServerIp": tacacsPlusServerIp,
       "tacacsPlusSecret": tacacsPlusSecret,
       "tacacsPlusAccounting": tacacsPlusAccounting,
       "sysLogSettings": sysLogSettings,
       "sysLocalLog": sysLocalLog,
       "networkLocalLog": networkLocalLog,
       "configLocalLog": configLocalLog,
       "opModeLocalLog": opModeLocalLog,
       "sysRemoteLog": sysRemoteLog,
       "networkRemoteLog": networkRemoteLog,
       "configRemoteLog": configRemoteLog,
       "opModeRemoteLog": opModeRemoteLog,
       "remoteLogServer": remoteLogServer,
       "syslogServerIp": syslogServerIp,
       "syslogFacility": syslogFacility,
       "syslogSeverity": syslogSeverity,
       "autoWarningSettings": autoWarningSettings,
       "eventSettings": eventSettings,
       "mailWarningColdStart": mailWarningColdStart,
       "mailWarningWarmStart": mailWarningWarmStart,
       "mailWarningAuthFailure": mailWarningAuthFailure,
       "mailWarningIpChanged": mailWarningIpChanged,
       "mailWarningPasswordChanged": mailWarningPasswordChanged,
       "trapServerColdStart": trapServerColdStart,
       "trapServerWarmStart": trapServerWarmStart,
       "trapServerAuthFailure": trapServerAuthFailure,
       "alarmServerEthernet1LinkDown": alarmServerEthernet1LinkDown,
       "alarmServerEthernet2LinkDown": alarmServerEthernet2LinkDown,
       "alarmServerEthernet3LinkDown": alarmServerEthernet3LinkDown,
       "smsServerColdStart": smsServerColdStart,
       "smsServerWarmStart": smsServerWarmStart,
       "smsServerEthernet1LinkDown": smsServerEthernet1LinkDown,
       "smsServerEthernet2LinkDown": smsServerEthernet2LinkDown,
       "smsServerEthernet3LinkDown": smsServerEthernet3LinkDown,
       "smsServerAuthFailure": smsServerAuthFailure,
       "smsServerIpChanged": smsServerIpChanged,
       "smsServerPasswordChanged": smsServerPasswordChanged,
       "serialEventSettings": serialEventSettings,
       "portEventSettingsTable": portEventSettingsTable,
       "portEventSettingsEntry": portEventSettingsEntry,
       "mailDCDchange": mailDCDchange,
       "trapDCDchange": trapDCDchange,
       "alarmDCDchange": alarmDCDchange,
       "smsDCDchange": smsDCDchange,
       "mailDSRchange": mailDSRchange,
       "trapDSRchange": trapDSRchange,
       "alarmDSRchange": alarmDSRchange,
       "smsDSRchange": smsDSRchange,
       "emailAlert": emailAlert,
       "emailWarningMailServer": emailWarningMailServer,
       "emailRequiresAuthentication": emailRequiresAuthentication,
       "emailWarningUserName": emailWarningUserName,
       "emailWarningPassword": emailWarningPassword,
       "emailWarningFromEmail": emailWarningFromEmail,
       "emailWarningFirstEmailAddr": emailWarningFirstEmailAddr,
       "emailWarningSecondEmailAddr": emailWarningSecondEmailAddr,
       "emailWarningThirdEmailAddr": emailWarningThirdEmailAddr,
       "emailWarningFourthEmailAddr": emailWarningFourthEmailAddr,
       "snmpTrap": snmpTrap,
       "snmpTrapReceiverIp": snmpTrapReceiverIp,
       "trapVersion": trapVersion,
       "smsAlert": smsAlert,
       "smsAlertFirstPhoneNumber": smsAlertFirstPhoneNumber,
       "smsAlertSecondPhoneNumber": smsAlertSecondPhoneNumber,
       "smsAlertThirdPhoneNumber": smsAlertThirdPhoneNumber,
       "smsAlertFourthPhoneNumber": smsAlertFourthPhoneNumber,
       "eventLogSettings": eventLogSettings,
       "currentLogCapacityRatio": currentLogCapacityRatio,
       "logCapacityWarningEnable": logCapacityWarningEnable,
       "logCapacityWarningThreshold": logCapacityWarningThreshold,
       "mailLogCapacity": mailLogCapacity,
       "trapLogCapacity": trapLogCapacity,
       "logOversizeAction": logOversizeAction,
       "maintenance": maintenance,
       "consoleSettings": consoleSettings,
       "httpConsole": httpConsole,
       "httpsConsole": httpsConsole,
       "telnetConsole": telnetConsole,
       "sshConsole": sshConsole,
       "consoleAuthenticationType": consoleAuthenticationType,
       "tryNextTypeOnAuthDenied": tryNextTypeOnAuthDenied,
       "resetButtonFunction": resetButtonFunction,
       "lcmReadOnlyProtect": lcmReadOnlyProtect,
       "maxHttpLoginUsers": maxHttpLoginUsers,
       "autoLogoutSetting": autoLogoutSetting,
       "loadFactoryDefault": loadFactoryDefault,
       "loadFactoryDefaultSetting": loadFactoryDefaultSetting,
       "accountManagement": accountManagement,
       "notificationMessage": notificationMessage,
       "loginNotificationMessage": loginNotificationMessage,
       "loginFailureMessage": loginFailureMessage,
       "userAccount": userAccount,
       "userAccountTable": userAccountTable,
       "userAccountEntry": userAccountEntry,
       "userAccountIndex": userAccountIndex,
       "activeUserAccount": activeUserAccount,
       "accountName": accountName,
       "accountGroupName": accountGroupName,
       "accessPermission": accessPermission,
       "accessPermissionTable": accessPermissionTable,
       "accessPermissionEntry": accessPermissionEntry,
       "groupName": groupName,
       "networkConfig": networkConfig,
       "serialConfig": serialConfig,
       "systemConfig": systemConfig,
       "adminConfig": adminConfig,
       "monitorLogWarning": monitorLogWarning,
       "commonSetting": commonSetting,
       "accountPasswordAndLoginMgmt": accountPasswordAndLoginMgmt,
       "accountPasswordPolicy": accountPasswordPolicy,
       "pwdMinLength": pwdMinLength,
       "pwdComplexityCheckEnable": pwdComplexityCheckEnable,
       "pwdComplexityCheckDigitEnable": pwdComplexityCheckDigitEnable,
       "pwdComplexityCheckAlphabetEnable": pwdComplexityCheckAlphabetEnable,
       "pwdComplexityCheckSpecialCharEnable": pwdComplexityCheckSpecialCharEnable,
       "pwdLifetime": pwdLifetime,
       "accountLoginFailureLockout": accountLoginFailureLockout,
       "loginFailureLockoutEnable": loginFailureLockoutEnable,
       "loginFailureLockoutRetrys": loginFailureLockoutRetrys,
       "loginFailureLockoutTime": loginFailureLockoutTime,
       "sysStatus": sysStatus,
       "s2eConnections": s2eConnections,
       "monitorRemoteIpTable": monitorRemoteIpTable,
       "monitorRemoteIpEntry": monitorRemoteIpEntry,
       "remoteIpIndex": remoteIpIndex,
       "monitorRemoteIp": monitorRemoteIp,
       "monitorCipher": monitorCipher,
       "serialPortStatus": serialPortStatus,
       "monitorSerialPortStatusTable": monitorSerialPortStatusTable,
       "monitorSerialPortStatusEntry": monitorSerialPortStatusEntry,
       "monitorTxCount": monitorTxCount,
       "monitorRxCount": monitorRxCount,
       "monitorTxTotalCount": monitorTxTotalCount,
       "monitorRxTotalCount": monitorRxTotalCount,
       "monitorDSR": monitorDSR,
       "monitorDTR": monitorDTR,
       "monitorRTS": monitorRTS,
       "monitorCTS": monitorCTS,
       "monitorDCD": monitorDCD,
       "serialPortErrorCount": serialPortErrorCount,
       "monitorSerialPortErrorCountTable": monitorSerialPortErrorCountTable,
       "monitorSerialPortErrorCountEntry": monitorSerialPortErrorCountEntry,
       "monitorErrorCountFrame": monitorErrorCountFrame,
       "monitorErrorCountParity": monitorErrorCountParity,
       "monitorErrorCountOverrun": monitorErrorCountOverrun,
       "monitorErrorCountBreak": monitorErrorCountBreak,
       "serialPortSettings": serialPortSettings,
       "monitorSerialPortSettingsTable": monitorSerialPortSettingsTable,
       "monitorSerialPortSettingsEntry": monitorSerialPortSettingsEntry,
       "monitorBaudRate": monitorBaudRate,
       "monitorDataBits": monitorDataBits,
       "monitorStopBits": monitorStopBits,
       "monitorParity": monitorParity,
       "monitorRTSCTSFlowControl": monitorRTSCTSFlowControl,
       "monitorXONXOFFFlowControl": monitorXONXOFFFlowControl,
       "monitorDTRDSRFlowControl": monitorDTRDSRFlowControl,
       "monitorRTSToggleFlowControl": monitorRTSToggleFlowControl,
       "monitorFIFO": monitorFIFO,
       "monitorInterface": monitorInterface,
       "serialPortBuffering": serialPortBuffering,
       "monitorSerialPortBufferingTable": monitorSerialPortBufferingTable,
       "monitorSerialPortBufferingEntry": monitorSerialPortBufferingEntry,
       "monitorBuffering": monitorBuffering,
       "relayOutputStatus": relayOutputStatus,
       "relayOutputEthernet1LinkDown": relayOutputEthernet1LinkDown,
       "ethernet1LinkDownAcknowledge": ethernet1LinkDownAcknowledge,
       "relayOutputEthernet2LinkDown": relayOutputEthernet2LinkDown,
       "ethernet2LinkDownAcknowledge": ethernet2LinkDownAcknowledge,
       "relayOutputEthernet3LinkDown": relayOutputEthernet3LinkDown,
       "ethernet3LinkDownAcknowledge": ethernet3LinkDownAcknowledge,
       "portDCDChangedStatusTable": portDCDChangedStatusTable,
       "portDCDChangedStatusEntry": portDCDChangedStatusEntry,
       "portDCDChangedStatus": portDCDChangedStatus,
       "portDCDChangedAcknowledge": portDCDChangedAcknowledge,
       "portDSRChangedStatusTable": portDSRChangedStatusTable,
       "portDSRChangedStatusEntry": portDSRChangedStatusEntry,
       "portDSRChangedStatus": portDSRChangedStatus,
       "portDSRChangedAcknowledge": portDSRChangedAcknowledge,
       "moduleStatus": moduleStatus,
       "redundancyStatus": redundancyStatus,
       "activeRedundancyProtocol": activeRedundancyProtocol,
       "spanningTreeStatus": spanningTreeStatus,
       "spanningTreeBridgeRole": spanningTreeBridgeRole,
       "spanningTreeRootBridge": spanningTreeRootBridge,
       "spanningTreeRootPathCost": spanningTreeRootPathCost,
       "spanningTreePortStatusTable": spanningTreePortStatusTable,
       "spanningTreePortStatusEntry": spanningTreePortStatusEntry,
       "spanningTreePortStatusIndex": spanningTreePortStatusIndex,
       "spanningTreePortEnableStatus": spanningTreePortEnableStatus,
       "spanningTreePortRole": spanningTreePortRole,
       "spanningTreePortDesignatedBridge": spanningTreePortDesignatedBridge,
       "spanningTreePortStatus": spanningTreePortStatus,
       "turboRingStatus": turboRingStatus,
       "turboRingBrokenStatus": turboRingBrokenStatus,
       "turboRingMaster": turboRingMaster,
       "turboRingPort1": turboRingPort1,
       "turboRingPort2": turboRingPort2,
       "turboRingPort1Status": turboRingPort1Status,
       "turboRingPort2Status": turboRingPort2Status,
       "saveConfiguration": saveConfiguration,
       "saveConfig": saveConfig,
       "restart": restart,
       "restartPorts": restartPorts,
       "restartSystem": restartSystem}
)
