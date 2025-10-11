# SNMP MIB module (RAD-SubRtr-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-SubRtr-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:19:09 2025
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

(bfdSessDstAddr,) = mibBuilder.importSymbols(
    "BFD-STD-MIB-R",
    "bfdSessDstAddr")

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(IANAtunnelType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAtunnelType")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifAlias,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifAlias",
    "ifIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

(ipIfStatsEntry,
 ipSystemStatsEntry) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipIfStatsEntry",
    "ipSystemStatsEntry")

(isdnSignalingEntry,) = mibBuilder.importSymbols(
    "ISDN-MIB",
    "isdnSignalingEntry")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason,
 bfdSessXDescription,
 radSysRtrEvents) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason",
    "bfdSessXDescription",
    "radSysRtrEvents")

(rad,
 rtrBridge) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "rad",
    "rtrBridge")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

radRouter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RtrIfConfigTYPE(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              9,
              15,
              20,
              21,
              22,
              23,
              28,
              32,
              33,
              37,
              40,
              45,
              62,
              69,
              500,
              1001,
              1002,
              1004,
              1010,
              1011,
              1020,
              1021,
              1022,
              1023,
              1024,
              1025,
              1026,
              1027,
              1060,
              1061,
              1062,
              1064,
              1080,
              1100)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ethernetLan", 6),
          ("iso88023Csmacd", 7),
          ("tokenRingLan", 9),
          ("fddi", 15),
          ("basicISDN", 20),
          ("primaryISDN", 21),
          ("propPointToPoint", 22),
          ("ppp", 23),
          ("slip", 28),
          ("frameRelay", 32),
          ("rs232", 33),
          ("atm", 37),
          ("x25ple", 40),
          ("v35", 45),
          ("fastEther", 62),
          ("fastEtherFX", 69),
          ("virtualNet", 500),
          ("cod", 1001),
          ("backUp", 1002),
          ("dialUp", 1004),
          ("b1isdn", 1010),
          ("b2isdn", 1011),
          ("ipBcst", 1020),
          ("ipPtp", 1021),
          ("ipxRaw", 1022),
          ("ipxEtType", 1023),
          ("ipxLlcSap", 1024),
          ("ipxLlcSnap", 1025),
          ("ipxPtp", 1026),
          ("brgUnder", 1027),
          ("wanDriver", 1060),
          ("ethernetDriver", 1061),
          ("tokenRingDriver", 1062),
          ("fddiDriver", 1064),
          ("virtualLan", 1080),
          ("unknown", 1100))
    )



class AdminDistance(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class RtrSafi(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              128)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("both", 3),
          ("mplsBgpVpn", 128))
    )



class InfoSourceDest(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              65536,
              131072,
              196608,
              262144,
              327680,
              393216,
              458752,
              524288,
              589824,
              655360,
              720896,
              786432,
              851968,
              917504,
              983040,
              1048576,
              1114112,
              1179648)
        )
    )
    namedValues = NamedValues(
        *(("infoSourceAll", 0),
          ("infoSourceAllInclConnected", 1),
          ("infoSourceOther", 65536),
          ("infoSourceConnected", 131072),
          ("infoSourceStatic", 196608),
          ("infoSourceIcmp", 262144),
          ("infoSourceEgp", 327680),
          ("infoSourceGgp", 393216),
          ("infoSourceHello", 458752),
          ("infoSourceRip", 524288),
          ("infoSourceIsis", 589824),
          ("infoSourceEsis", 655360),
          ("infoSourceIgrp", 720896),
          ("infoSourceBbnSpfIgp", 786432),
          ("infoSourceOspf", 851968),
          ("infoSourceBgp", 917504),
          ("infoSourceIdpr", 983040),
          ("infoSourceEigrp", 1048576),
          ("infoSourceDvmrp", 1114112),
          ("infoSourceDdrp", 1179648))
    )



# MIB Managed Objects in the order of their OIDs

_RtrEvents_ObjectIdentity = ObjectIdentity
rtrEvents = _RtrEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 0)
)
_RtrInterfaces_ObjectIdentity = ObjectIdentity
rtrInterfaces = _RtrInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 1)
)
_RtrConfigIfTable_Object = MibTable
rtrConfigIfTable = _RtrConfigIfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 1)
)
if mibBuilder.loadTexts:
    rtrConfigIfTable.setStatus("current")
_RtrConfigIfEntry_Object = MibTableRow
rtrConfigIfEntry = _RtrConfigIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 1, 1)
)
rtrConfigIfEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrConfigIfIndex"),
)
if mibBuilder.loadTexts:
    rtrConfigIfEntry.setStatus("current")
_RtrConfigIfIndex_Type = InterfaceIndex
_RtrConfigIfIndex_Object = MibTableColumn
rtrConfigIfIndex = _RtrConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 1, 1, 1),
    _RtrConfigIfIndex_Type()
)
rtrConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrConfigIfIndex.setStatus("current")
_RtrConfigIfType_Type = RtrIfConfigTYPE
_RtrConfigIfType_Object = MibTableColumn
rtrConfigIfType = _RtrConfigIfType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 1, 1, 2),
    _RtrConfigIfType_Type()
)
rtrConfigIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigIfType.setStatus("current")
_RtrConfigIfName_Type = DisplayString
_RtrConfigIfName_Object = MibTableColumn
rtrConfigIfName = _RtrConfigIfName_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 1, 1, 3),
    _RtrConfigIfName_Type()
)
rtrConfigIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigIfName.setStatus("current")
_RtrConfigIfStatus_Type = RowStatus
_RtrConfigIfStatus_Object = MibTableColumn
rtrConfigIfStatus = _RtrConfigIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 1, 1, 4),
    _RtrConfigIfStatus_Type()
)
rtrConfigIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigIfStatus.setStatus("current")
_RtrIfCfgTable_Object = MibTable
rtrIfCfgTable = _RtrIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2)
)
if mibBuilder.loadTexts:
    rtrIfCfgTable.setStatus("current")
_RtrIfCfgEntry_Object = MibTableRow
rtrIfCfgEntry = _RtrIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1)
)
rtrIfCfgEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrIfCfgIndex"),
    (0, "RAD-SubRtr-MIB", "rtrIfCfgIpAddress"),
)
if mibBuilder.loadTexts:
    rtrIfCfgEntry.setStatus("current")
_RtrIfCfgIndex_Type = Integer32
_RtrIfCfgIndex_Object = MibTableColumn
rtrIfCfgIndex = _RtrIfCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 1),
    _RtrIfCfgIndex_Type()
)
rtrIfCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrIfCfgIndex.setStatus("current")
_RtrIfCfgIpAddress_Type = IpAddress
_RtrIfCfgIpAddress_Object = MibTableColumn
rtrIfCfgIpAddress = _RtrIfCfgIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 2),
    _RtrIfCfgIpAddress_Type()
)
rtrIfCfgIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrIfCfgIpAddress.setStatus("current")
_RtrIfCfgRowStatus_Type = RowStatus
_RtrIfCfgRowStatus_Object = MibTableColumn
rtrIfCfgRowStatus = _RtrIfCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 3),
    _RtrIfCfgRowStatus_Type()
)
rtrIfCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgRowStatus.setStatus("current")
_RtrIfCfgIpMask_Type = IpAddress
_RtrIfCfgIpMask_Object = MibTableColumn
rtrIfCfgIpMask = _RtrIfCfgIpMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 4),
    _RtrIfCfgIpMask_Type()
)
rtrIfCfgIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgIpMask.setStatus("deprecated")
_RtrIfCfgIfIndex_Type = Integer32
_RtrIfCfgIfIndex_Object = MibTableColumn
rtrIfCfgIfIndex = _RtrIfCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 5),
    _RtrIfCfgIfIndex_Type()
)
rtrIfCfgIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgIfIndex.setStatus("current")


class _RtrIfCfgType_Type(Integer32):
    """Custom type rtrIfCfgType based on Integer32"""
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
        *(("notApplicable", 1),
          ("atm", 2),
          ("lis", 3),
          ("ethernet", 4),
          ("loopback", 5),
          ("unmunbered", 6))
    )


_RtrIfCfgType_Type.__name__ = "Integer32"
_RtrIfCfgType_Object = MibTableColumn
rtrIfCfgType = _RtrIfCfgType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 6),
    _RtrIfCfgType_Type()
)
rtrIfCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgType.setStatus("current")
_RtrIfCfgVlanId_Type = VlanIndex
_RtrIfCfgVlanId_Object = MibTableColumn
rtrIfCfgVlanId = _RtrIfCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 7),
    _RtrIfCfgVlanId_Type()
)
rtrIfCfgVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgVlanId.setStatus("current")
_RtrIfCfgMtu_Type = Integer32
_RtrIfCfgMtu_Object = MibTableColumn
rtrIfCfgMtu = _RtrIfCfgMtu_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 8),
    _RtrIfCfgMtu_Type()
)
rtrIfCfgMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgMtu.setStatus("current")
_RtrIfCfgName_Type = SnmpAdminString
_RtrIfCfgName_Object = MibTableColumn
rtrIfCfgName = _RtrIfCfgName_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 9),
    _RtrIfCfgName_Type()
)
rtrIfCfgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgName.setStatus("current")
_RtrIfCfgConnectionPointer_Type = RowPointer
_RtrIfCfgConnectionPointer_Object = MibTableColumn
rtrIfCfgConnectionPointer = _RtrIfCfgConnectionPointer_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 10),
    _RtrIfCfgConnectionPointer_Type()
)
rtrIfCfgConnectionPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgConnectionPointer.setStatus("current")


class _RtrIfCfgVlanTagging_Type(Integer32):
    """Custom type rtrIfCfgVlanTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("untag", 2),
          ("tag", 3))
    )


_RtrIfCfgVlanTagging_Type.__name__ = "Integer32"
_RtrIfCfgVlanTagging_Object = MibTableColumn
rtrIfCfgVlanTagging = _RtrIfCfgVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 11),
    _RtrIfCfgVlanTagging_Type()
)
rtrIfCfgVlanTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgVlanTagging.setStatus("current")
_RtrIfCfgVlanPriority_Type = Unsigned32
_RtrIfCfgVlanPriority_Object = MibTableColumn
rtrIfCfgVlanPriority = _RtrIfCfgVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 12),
    _RtrIfCfgVlanPriority_Type()
)
rtrIfCfgVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgVlanPriority.setStatus("current")
_RtrIfCfgParams_Type = Unsigned32
_RtrIfCfgParams_Object = MibTableColumn
rtrIfCfgParams = _RtrIfCfgParams_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 13),
    _RtrIfCfgParams_Type()
)
rtrIfCfgParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgParams.setStatus("current")


class _RtrIfCfgMngAccess_Type(Integer32):
    """Custom type rtrIfCfgMngAccess based on Integer32"""
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
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3),
          ("pingAllow", 4))
    )


_RtrIfCfgMngAccess_Type.__name__ = "Integer32"
_RtrIfCfgMngAccess_Object = MibTableColumn
rtrIfCfgMngAccess = _RtrIfCfgMngAccess_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 14),
    _RtrIfCfgMngAccess_Type()
)
rtrIfCfgMngAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgMngAccess.setStatus("current")


class _RtrIfCfgLlcSnapEncaps_Type(Integer32):
    """Custom type rtrIfCfgLlcSnapEncaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("bridgedPdu", 2),
          ("routedPdu", 3))
    )


_RtrIfCfgLlcSnapEncaps_Type.__name__ = "Integer32"
_RtrIfCfgLlcSnapEncaps_Object = MibTableColumn
rtrIfCfgLlcSnapEncaps = _RtrIfCfgLlcSnapEncaps_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 15),
    _RtrIfCfgLlcSnapEncaps_Type()
)
rtrIfCfgLlcSnapEncaps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgLlcSnapEncaps.setStatus("current")


class _RtrIfCfgDhcp_Type(Integer32):
    """Custom type rtrIfCfgDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_RtrIfCfgDhcp_Type.__name__ = "Integer32"
_RtrIfCfgDhcp_Object = MibTableColumn
rtrIfCfgDhcp = _RtrIfCfgDhcp_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 16),
    _RtrIfCfgDhcp_Type()
)
rtrIfCfgDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgDhcp.setStatus("current")
_RtrIfCfgIfIpAddressType_Type = InetAddressType
_RtrIfCfgIfIpAddressType_Object = MibTableColumn
rtrIfCfgIfIpAddressType = _RtrIfCfgIfIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 17),
    _RtrIfCfgIfIpAddressType_Type()
)
rtrIfCfgIfIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgIfIpAddressType.setStatus("deprecated")
_RtrIfCfgIfIpAddress_Type = InetAddress
_RtrIfCfgIfIpAddress_Object = MibTableColumn
rtrIfCfgIfIpAddress = _RtrIfCfgIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 18),
    _RtrIfCfgIfIpAddress_Type()
)
rtrIfCfgIfIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgIfIpAddress.setStatus("deprecated")


class _RtrIfCfgICMPUnreachable_Type(Integer32):
    """Custom type rtrIfCfgICMPUnreachable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_RtrIfCfgICMPUnreachable_Type.__name__ = "Integer32"
_RtrIfCfgICMPUnreachable_Object = MibTableColumn
rtrIfCfgICMPUnreachable = _RtrIfCfgICMPUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 19),
    _RtrIfCfgICMPUnreachable_Type()
)
rtrIfCfgICMPUnreachable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgICMPUnreachable.setStatus("current")


class _RtrIfCfgIpv6AutoConfig_Type(Integer32):
    """Custom type rtrIfCfgIpv6AutoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_RtrIfCfgIpv6AutoConfig_Type.__name__ = "Integer32"
_RtrIfCfgIpv6AutoConfig_Object = MibTableColumn
rtrIfCfgIpv6AutoConfig = _RtrIfCfgIpv6AutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 20),
    _RtrIfCfgIpv6AutoConfig_Type()
)
rtrIfCfgIpv6AutoConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgIpv6AutoConfig.setStatus("current")


class _RtrIfCfgDhcpRelay_Type(Integer32):
    """Custom type rtrIfCfgDhcpRelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_RtrIfCfgDhcpRelay_Type.__name__ = "Integer32"
_RtrIfCfgDhcpRelay_Object = MibTableColumn
rtrIfCfgDhcpRelay = _RtrIfCfgDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 26),
    _RtrIfCfgDhcpRelay_Type()
)
rtrIfCfgDhcpRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgDhcpRelay.setStatus("current")


class _RtrIfCfgDhcpv6ClientAdminStatus_Type(Integer32):
    """Custom type rtrIfCfgDhcpv6ClientAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_RtrIfCfgDhcpv6ClientAdminStatus_Type.__name__ = "Integer32"
_RtrIfCfgDhcpv6ClientAdminStatus_Object = MibTableColumn
rtrIfCfgDhcpv6ClientAdminStatus = _RtrIfCfgDhcpv6ClientAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 27),
    _RtrIfCfgDhcpv6ClientAdminStatus_Type()
)
rtrIfCfgDhcpv6ClientAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgDhcpv6ClientAdminStatus.setStatus("current")


class _RtrIfCfgIpForwarding_Type(Integer32):
    """Custom type rtrIfCfgIpForwarding based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_RtrIfCfgIpForwarding_Type.__name__ = "Integer32"
_RtrIfCfgIpForwarding_Object = MibTableColumn
rtrIfCfgIpForwarding = _RtrIfCfgIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 2, 1, 28),
    _RtrIfCfgIpForwarding_Type()
)
rtrIfCfgIpForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgIpForwarding.setStatus("current")
_RtrStaticRouteTable_Object = MibTable
rtrStaticRouteTable = _RtrStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3)
)
if mibBuilder.loadTexts:
    rtrStaticRouteTable.setStatus("current")
_RtrStaticRouteEntry_Object = MibTableRow
rtrStaticRouteEntry = _RtrStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1)
)
rtrStaticRouteEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrStaticRouteDestType"),
    (0, "RAD-SubRtr-MIB", "rtrStaticRouteDest"),
    (0, "RAD-SubRtr-MIB", "rtrStaticRoutePfxLen"),
    (0, "RAD-SubRtr-MIB", "rtrStaticRoutePolicy"),
    (0, "RAD-SubRtr-MIB", "rtrStaticRouteNextHopType"),
    (0, "RAD-SubRtr-MIB", "rtrStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    rtrStaticRouteEntry.setStatus("current")
_RtrStaticRouteDestType_Type = InetAddressType
_RtrStaticRouteDestType_Object = MibTableColumn
rtrStaticRouteDestType = _RtrStaticRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 1),
    _RtrStaticRouteDestType_Type()
)
rtrStaticRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrStaticRouteDestType.setStatus("current")
_RtrStaticRouteDest_Type = InetAddress
_RtrStaticRouteDest_Object = MibTableColumn
rtrStaticRouteDest = _RtrStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 2),
    _RtrStaticRouteDest_Type()
)
rtrStaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrStaticRouteDest.setStatus("current")
_RtrStaticRoutePfxLen_Type = InetAddressPrefixLength
_RtrStaticRoutePfxLen_Object = MibTableColumn
rtrStaticRoutePfxLen = _RtrStaticRoutePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 3),
    _RtrStaticRoutePfxLen_Type()
)
rtrStaticRoutePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrStaticRoutePfxLen.setStatus("current")
_RtrStaticRoutePolicy_Type = ObjectIdentifier
_RtrStaticRoutePolicy_Object = MibTableColumn
rtrStaticRoutePolicy = _RtrStaticRoutePolicy_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 4),
    _RtrStaticRoutePolicy_Type()
)
rtrStaticRoutePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrStaticRoutePolicy.setStatus("current")
_RtrStaticRouteNextHopType_Type = InetAddressType
_RtrStaticRouteNextHopType_Object = MibTableColumn
rtrStaticRouteNextHopType = _RtrStaticRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 5),
    _RtrStaticRouteNextHopType_Type()
)
rtrStaticRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrStaticRouteNextHopType.setStatus("current")
_RtrStaticRouteNextHop_Type = InetAddress
_RtrStaticRouteNextHop_Object = MibTableColumn
rtrStaticRouteNextHop = _RtrStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 6),
    _RtrStaticRouteNextHop_Type()
)
rtrStaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrStaticRouteNextHop.setStatus("current")
_RtrStaticRouteRtRIfIndex_Type = Integer32
_RtrStaticRouteRtRIfIndex_Object = MibTableColumn
rtrStaticRouteRtRIfIndex = _RtrStaticRouteRtRIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 7),
    _RtrStaticRouteRtRIfIndex_Type()
)
rtrStaticRouteRtRIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrStaticRouteRtRIfIndex.setStatus("current")


class _RtrStaticRouteType_Type(Integer32):
    """Custom type rtrStaticRouteType based on Integer32"""
    defaultValue = 4

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
        *(("other", 1),
          ("reject", 2),
          ("local", 3),
          ("remote", 4),
          ("blackhole", 5))
    )


_RtrStaticRouteType_Type.__name__ = "Integer32"
_RtrStaticRouteType_Object = MibTableColumn
rtrStaticRouteType = _RtrStaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 8),
    _RtrStaticRouteType_Type()
)
rtrStaticRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrStaticRouteType.setStatus("current")


class _RtrStaticRouteProto_Type(IANAipRouteProtocol):
    """Custom type rtrStaticRouteProto based on IANAipRouteProtocol"""
    defaultValue = 3


_RtrStaticRouteProto_Type.__name__ = "IANAipRouteProtocol"
_RtrStaticRouteProto_Object = MibTableColumn
rtrStaticRouteProto = _RtrStaticRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 9),
    _RtrStaticRouteProto_Type()
)
rtrStaticRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrStaticRouteProto.setStatus("current")
_RtrStaticRouteAge_Type = Gauge32
_RtrStaticRouteAge_Object = MibTableColumn
rtrStaticRouteAge = _RtrStaticRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 10),
    _RtrStaticRouteAge_Type()
)
rtrStaticRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrStaticRouteAge.setStatus("current")


class _RtrStaticRouteNextHopAS_Type(InetAutonomousSystemNumber):
    """Custom type rtrStaticRouteNextHopAS based on InetAutonomousSystemNumber"""
    defaultValue = 0


_RtrStaticRouteNextHopAS_Type.__name__ = "InetAutonomousSystemNumber"
_RtrStaticRouteNextHopAS_Object = MibTableColumn
rtrStaticRouteNextHopAS = _RtrStaticRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 11),
    _RtrStaticRouteNextHopAS_Type()
)
rtrStaticRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrStaticRouteNextHopAS.setStatus("current")


class _RtrStaticRouteMetric1_Type(Integer32):
    """Custom type rtrStaticRouteMetric1 based on Integer32"""
    defaultValue = -1


_RtrStaticRouteMetric1_Type.__name__ = "Integer32"
_RtrStaticRouteMetric1_Object = MibTableColumn
rtrStaticRouteMetric1 = _RtrStaticRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 12),
    _RtrStaticRouteMetric1_Type()
)
rtrStaticRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrStaticRouteMetric1.setStatus("current")


class _RtrStaticRouteMetric2_Type(Integer32):
    """Custom type rtrStaticRouteMetric2 based on Integer32"""
    defaultValue = -1


_RtrStaticRouteMetric2_Type.__name__ = "Integer32"
_RtrStaticRouteMetric2_Object = MibTableColumn
rtrStaticRouteMetric2 = _RtrStaticRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 13),
    _RtrStaticRouteMetric2_Type()
)
rtrStaticRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrStaticRouteMetric2.setStatus("current")


class _RtrStaticRouteMetric3_Type(Integer32):
    """Custom type rtrStaticRouteMetric3 based on Integer32"""
    defaultValue = -1


_RtrStaticRouteMetric3_Type.__name__ = "Integer32"
_RtrStaticRouteMetric3_Object = MibTableColumn
rtrStaticRouteMetric3 = _RtrStaticRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 14),
    _RtrStaticRouteMetric3_Type()
)
rtrStaticRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrStaticRouteMetric3.setStatus("current")


class _RtrStaticRouteMetric4_Type(Integer32):
    """Custom type rtrStaticRouteMetric4 based on Integer32"""
    defaultValue = -1


_RtrStaticRouteMetric4_Type.__name__ = "Integer32"
_RtrStaticRouteMetric4_Object = MibTableColumn
rtrStaticRouteMetric4 = _RtrStaticRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 15),
    _RtrStaticRouteMetric4_Type()
)
rtrStaticRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrStaticRouteMetric4.setStatus("current")


class _RtrStaticRouteMetric5_Type(Integer32):
    """Custom type rtrStaticRouteMetric5 based on Integer32"""
    defaultValue = -1


_RtrStaticRouteMetric5_Type.__name__ = "Integer32"
_RtrStaticRouteMetric5_Object = MibTableColumn
rtrStaticRouteMetric5 = _RtrStaticRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 16),
    _RtrStaticRouteMetric5_Type()
)
rtrStaticRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrStaticRouteMetric5.setStatus("current")
_RtrStaticRouteStatus_Type = RowStatus
_RtrStaticRouteStatus_Object = MibTableColumn
rtrStaticRouteStatus = _RtrStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 17),
    _RtrStaticRouteStatus_Type()
)
rtrStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrStaticRouteStatus.setStatus("current")


class _RtrStaticRouteNoInstall_Type(TruthValue):
    """Custom type rtrStaticRouteNoInstall based on TruthValue"""
    defaultValue = 2


_RtrStaticRouteNoInstall_Type.__name__ = "TruthValue"
_RtrStaticRouteNoInstall_Object = MibTableColumn
rtrStaticRouteNoInstall = _RtrStaticRouteNoInstall_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 3, 1, 18),
    _RtrStaticRouteNoInstall_Type()
)
rtrStaticRouteNoInstall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrStaticRouteNoInstall.setStatus("current")
_IpIfStatsXTable_Object = MibTable
ipIfStatsXTable = _IpIfStatsXTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 4)
)
if mibBuilder.loadTexts:
    ipIfStatsXTable.setStatus("current")
_IpIfStatsXEntry_Object = MibTableRow
ipIfStatsXEntry = _IpIfStatsXEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipIfStatsXEntry.setStatus("current")


class _IpIfStatsXClearStatisticsCmd_Type(TruthValue):
    """Custom type ipIfStatsXClearStatisticsCmd based on TruthValue"""
    defaultValue = 2


_IpIfStatsXClearStatisticsCmd_Type.__name__ = "TruthValue"
_IpIfStatsXClearStatisticsCmd_Object = MibTableColumn
ipIfStatsXClearStatisticsCmd = _IpIfStatsXClearStatisticsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 4, 1, 1),
    _IpIfStatsXClearStatisticsCmd_Type()
)
ipIfStatsXClearStatisticsCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfStatsXClearStatisticsCmd.setStatus("current")
_IpSystemStatsXTable_Object = MibTable
ipSystemStatsXTable = _IpSystemStatsXTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 5)
)
if mibBuilder.loadTexts:
    ipSystemStatsXTable.setStatus("current")
_IpSystemStatsXEntry_Object = MibTableRow
ipSystemStatsXEntry = _IpSystemStatsXEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ipSystemStatsXEntry.setStatus("current")


class _IpSystemStatsXClearStatisticsCmd_Type(TruthValue):
    """Custom type ipSystemStatsXClearStatisticsCmd based on TruthValue"""
    defaultValue = 2


_IpSystemStatsXClearStatisticsCmd_Type.__name__ = "TruthValue"
_IpSystemStatsXClearStatisticsCmd_Object = MibTableColumn
ipSystemStatsXClearStatisticsCmd = _IpSystemStatsXClearStatisticsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 5, 1, 1),
    _IpSystemStatsXClearStatisticsCmd_Type()
)
ipSystemStatsXClearStatisticsCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSystemStatsXClearStatisticsCmd.setStatus("current")


class _IpSystemStatsXClearAllStatisticsCmd_Type(Integer32):
    """Custom type ipSystemStatsXClearAllStatisticsCmd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("all", 3),
          ("ip-traffic", 4),
          ("access-list", 5))
    )


_IpSystemStatsXClearAllStatisticsCmd_Type.__name__ = "Integer32"
_IpSystemStatsXClearAllStatisticsCmd_Object = MibTableColumn
ipSystemStatsXClearAllStatisticsCmd = _IpSystemStatsXClearAllStatisticsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 5, 1, 2),
    _IpSystemStatsXClearAllStatisticsCmd_Type()
)
ipSystemStatsXClearAllStatisticsCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSystemStatsXClearAllStatisticsCmd.setStatus("current")
_IfIpAddressTable_Object = MibTable
ifIpAddressTable = _IfIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 7)
)
if mibBuilder.loadTexts:
    ifIpAddressTable.setStatus("current")
_IfIpAddressEntry_Object = MibTableRow
ifIpAddressEntry = _IfIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 7, 1)
)
ifIpAddressEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "ifIpAddressAddrType"),
    (0, "RAD-SubRtr-MIB", "ifIpAddressAddr"),
    (0, "RAD-SubRtr-MIB", "ifIpAddressPrefixLength"),
    (0, "RAD-SubRtr-MIB", "ifIpAddressIfIndex"),
)
if mibBuilder.loadTexts:
    ifIpAddressEntry.setStatus("current")
_IfIpAddressAddrType_Type = InetAddressType
_IfIpAddressAddrType_Object = MibTableColumn
ifIpAddressAddrType = _IfIpAddressAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 7, 1, 1),
    _IfIpAddressAddrType_Type()
)
ifIpAddressAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifIpAddressAddrType.setStatus("current")
_IfIpAddressAddr_Type = InetAddress
_IfIpAddressAddr_Object = MibTableColumn
ifIpAddressAddr = _IfIpAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 7, 1, 2),
    _IfIpAddressAddr_Type()
)
ifIpAddressAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifIpAddressAddr.setStatus("current")
_IfIpAddressPrefixLength_Type = InetAddressPrefixLength
_IfIpAddressPrefixLength_Object = MibTableColumn
ifIpAddressPrefixLength = _IfIpAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 7, 1, 3),
    _IfIpAddressPrefixLength_Type()
)
ifIpAddressPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifIpAddressPrefixLength.setStatus("current")
_IfIpAddressIfIndex_Type = InterfaceIndex
_IfIpAddressIfIndex_Object = MibTableColumn
ifIpAddressIfIndex = _IfIpAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 7, 1, 4),
    _IfIpAddressIfIndex_Type()
)
ifIpAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifIpAddressIfIndex.setStatus("current")
_IfIpAddressRowStatus_Type = RowStatus
_IfIpAddressRowStatus_Object = MibTableColumn
ifIpAddressRowStatus = _IfIpAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 7, 1, 5),
    _IfIpAddressRowStatus_Type()
)
ifIpAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifIpAddressRowStatus.setStatus("current")
_IfIpAddressPrefix_Type = InetAddress
_IfIpAddressPrefix_Object = MibTableColumn
ifIpAddressPrefix = _IfIpAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 7, 1, 6),
    _IfIpAddressPrefix_Type()
)
ifIpAddressPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIpAddressPrefix.setStatus("current")


class _IfIpAddressOrigin_Type(Integer32):
    """Custom type ifIpAddressOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("manual", 2),
          ("dhcp", 4),
          ("linklayer", 5),
          ("random", 6),
          ("nat", 7))
    )


_IfIpAddressOrigin_Type.__name__ = "Integer32"
_IfIpAddressOrigin_Object = MibTableColumn
ifIpAddressOrigin = _IfIpAddressOrigin_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 7, 1, 7),
    _IfIpAddressOrigin_Type()
)
ifIpAddressOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIpAddressOrigin.setStatus("current")
_RtrIfCfgBfdSessTable_Object = MibTable
rtrIfCfgBfdSessTable = _RtrIfCfgBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 8)
)
if mibBuilder.loadTexts:
    rtrIfCfgBfdSessTable.setStatus("current")
_RtrIfCfgBfdSessEntry_Object = MibTableRow
rtrIfCfgBfdSessEntry = _RtrIfCfgBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 8, 1)
)
rtrIfCfgBfdSessEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrIfCfgIndex"),
)
if mibBuilder.loadTexts:
    rtrIfCfgBfdSessEntry.setStatus("current")


class _RtrIfCfgBfdSessDesiredMinTxInterval_Type(Integer32):
    """Custom type rtrIfCfgBfdSessDesiredMinTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3300,
              10000,
              100000,
              1000000,
              10000000)
        )
    )
    namedValues = NamedValues(
        *(("interval3300microsec", 3300),
          ("interval10000microsec", 10000),
          ("interval100000microsec", 100000),
          ("interval1000000microsec", 1000000),
          ("interval10000000microsec", 10000000))
    )


_RtrIfCfgBfdSessDesiredMinTxInterval_Type.__name__ = "Integer32"
_RtrIfCfgBfdSessDesiredMinTxInterval_Object = MibTableColumn
rtrIfCfgBfdSessDesiredMinTxInterval = _RtrIfCfgBfdSessDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 8, 1, 1),
    _RtrIfCfgBfdSessDesiredMinTxInterval_Type()
)
rtrIfCfgBfdSessDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgBfdSessDesiredMinTxInterval.setStatus("current")


class _RtrIfCfgBfdSessReqMinRxInterval_Type(Integer32):
    """Custom type rtrIfCfgBfdSessReqMinRxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3300,
              10000,
              100000,
              1000000,
              10000000)
        )
    )
    namedValues = NamedValues(
        *(("interval3300microsec", 3300),
          ("interval10000microsec", 10000),
          ("interval100000microsec", 100000),
          ("interval1000000microsec", 1000000),
          ("interval10000000microsec", 10000000))
    )


_RtrIfCfgBfdSessReqMinRxInterval_Type.__name__ = "Integer32"
_RtrIfCfgBfdSessReqMinRxInterval_Object = MibTableColumn
rtrIfCfgBfdSessReqMinRxInterval = _RtrIfCfgBfdSessReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 8, 1, 2),
    _RtrIfCfgBfdSessReqMinRxInterval_Type()
)
rtrIfCfgBfdSessReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgBfdSessReqMinRxInterval.setStatus("current")
_RtrIfCfgBfdSessDetectMult_Type = Integer32
_RtrIfCfgBfdSessDetectMult_Object = MibTableColumn
rtrIfCfgBfdSessDetectMult = _RtrIfCfgBfdSessDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 1, 8, 1, 3),
    _RtrIfCfgBfdSessDetectMult_Type()
)
rtrIfCfgBfdSessDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIfCfgBfdSessDetectMult.setStatus("current")
_IpSpec_ObjectIdentity = ObjectIdentity
ipSpec = _IpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 2)
)
_RtrIpAddrTable_Object = MibTable
rtrIpAddrTable = _RtrIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 1)
)
if mibBuilder.loadTexts:
    rtrIpAddrTable.setStatus("current")
_RtrIpAddrEntry_Object = MibTableRow
rtrIpAddrEntry = _RtrIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 1, 1)
)
rtrIpAddrEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    rtrIpAddrEntry.setStatus("current")
_RtrIpAdEntAddr_Type = IpAddress
_RtrIpAdEntAddr_Object = MibTableColumn
rtrIpAdEntAddr = _RtrIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 1, 1, 1),
    _RtrIpAdEntAddr_Type()
)
rtrIpAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrIpAdEntAddr.setStatus("current")
_RtrIpAdEntIfIndex_Type = Integer32
_RtrIpAdEntIfIndex_Object = MibTableColumn
rtrIpAdEntIfIndex = _RtrIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 1, 1, 2),
    _RtrIpAdEntIfIndex_Type()
)
rtrIpAdEntIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIpAdEntIfIndex.setStatus("current")
_RtrIpAdEntNetMask_Type = IpAddress
_RtrIpAdEntNetMask_Object = MibTableColumn
rtrIpAdEntNetMask = _RtrIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 1, 1, 3),
    _RtrIpAdEntNetMask_Type()
)
rtrIpAdEntNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIpAdEntNetMask.setStatus("current")


class _RtrIpAdEntForwardIpBroadcast_Type(Integer32):
    """Custom type rtrIpAdEntForwardIpBroadcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RtrIpAdEntForwardIpBroadcast_Type.__name__ = "Integer32"
_RtrIpAdEntForwardIpBroadcast_Object = MibTableColumn
rtrIpAdEntForwardIpBroadcast = _RtrIpAdEntForwardIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 1, 1, 4),
    _RtrIpAdEntForwardIpBroadcast_Type()
)
rtrIpAdEntForwardIpBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIpAdEntForwardIpBroadcast.setStatus("current")
_RtrIpAdEntBackupAddr_Type = IpAddress
_RtrIpAdEntBackupAddr_Object = MibTableColumn
rtrIpAdEntBackupAddr = _RtrIpAdEntBackupAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 1, 1, 5),
    _RtrIpAdEntBackupAddr_Type()
)
rtrIpAdEntBackupAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIpAdEntBackupAddr.setStatus("current")
_RtrIpAdEntStatus_Type = RowStatus
_RtrIpAdEntStatus_Object = MibTableColumn
rtrIpAdEntStatus = _RtrIpAdEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 1, 1, 6),
    _RtrIpAdEntStatus_Type()
)
rtrIpAdEntStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrIpAdEntStatus.setStatus("current")
_IcmpSpec_ObjectIdentity = ObjectIdentity
icmpSpec = _IcmpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 2)
)


class _RtrIcmpGenErrMsgEnable_Type(Integer32):
    """Custom type rtrIcmpGenErrMsgEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RtrIcmpGenErrMsgEnable_Type.__name__ = "Integer32"
_RtrIcmpGenErrMsgEnable_Object = MibScalar
rtrIcmpGenErrMsgEnable = _RtrIcmpGenErrMsgEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 2, 1),
    _RtrIcmpGenErrMsgEnable_Type()
)
rtrIcmpGenErrMsgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpGenErrMsgEnable.setStatus("current")
_RtrIcmpRdTable_Object = MibTable
rtrIcmpRdTable = _RtrIcmpRdTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rtrIcmpRdTable.setStatus("current")
_RtrIcmpRdEntry_Object = MibTableRow
rtrIcmpRdEntry = _RtrIcmpRdEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 2, 2, 1)
)
rtrIcmpRdEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrIcmpRdIpAddr"),
)
if mibBuilder.loadTexts:
    rtrIcmpRdEntry.setStatus("current")
_RtrIcmpRdIpAddr_Type = IpAddress
_RtrIcmpRdIpAddr_Object = MibTableColumn
rtrIcmpRdIpAddr = _RtrIcmpRdIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 2, 2, 1, 1),
    _RtrIcmpRdIpAddr_Type()
)
rtrIcmpRdIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrIcmpRdIpAddr.setStatus("current")
_RtrIcmpRdIpAdvertAddr_Type = IpAddress
_RtrIcmpRdIpAdvertAddr_Object = MibTableColumn
rtrIcmpRdIpAdvertAddr = _RtrIcmpRdIpAdvertAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 2, 2, 1, 2),
    _RtrIcmpRdIpAdvertAddr_Type()
)
rtrIcmpRdIpAdvertAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpRdIpAdvertAddr.setStatus("current")


class _RtrIcmpRdMaxAdvertInterval_Type(Integer32):
    """Custom type rtrIcmpRdMaxAdvertInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_RtrIcmpRdMaxAdvertInterval_Type.__name__ = "Integer32"
_RtrIcmpRdMaxAdvertInterval_Object = MibTableColumn
rtrIcmpRdMaxAdvertInterval = _RtrIcmpRdMaxAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 2, 2, 1, 3),
    _RtrIcmpRdMaxAdvertInterval_Type()
)
rtrIcmpRdMaxAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpRdMaxAdvertInterval.setStatus("current")


class _RtrIcmpRdMinAdvertInterval_Type(Integer32):
    """Custom type rtrIcmpRdMinAdvertInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_RtrIcmpRdMinAdvertInterval_Type.__name__ = "Integer32"
_RtrIcmpRdMinAdvertInterval_Object = MibTableColumn
rtrIcmpRdMinAdvertInterval = _RtrIcmpRdMinAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 2, 2, 1, 4),
    _RtrIcmpRdMinAdvertInterval_Type()
)
rtrIcmpRdMinAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpRdMinAdvertInterval.setStatus("current")


class _RtrIcmpRdAdvertLifetime_Type(Integer32):
    """Custom type rtrIcmpRdAdvertLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9000),
    )


_RtrIcmpRdAdvertLifetime_Type.__name__ = "Integer32"
_RtrIcmpRdAdvertLifetime_Object = MibTableColumn
rtrIcmpRdAdvertLifetime = _RtrIcmpRdAdvertLifetime_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 2, 2, 1, 5),
    _RtrIcmpRdAdvertLifetime_Type()
)
rtrIcmpRdAdvertLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpRdAdvertLifetime.setStatus("current")


class _RtrIcmpRdAdvertise_Type(Integer32):
    """Custom type rtrIcmpRdAdvertise based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RtrIcmpRdAdvertise_Type.__name__ = "Integer32"
_RtrIcmpRdAdvertise_Object = MibTableColumn
rtrIcmpRdAdvertise = _RtrIcmpRdAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 2, 2, 1, 6),
    _RtrIcmpRdAdvertise_Type()
)
rtrIcmpRdAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpRdAdvertise.setStatus("current")


class _RtrIcmpRdPreferenceLevel_Type(Integer32):
    """Custom type rtrIcmpRdPreferenceLevel based on Integer32"""
    defaultValue = 0


_RtrIcmpRdPreferenceLevel_Type.__name__ = "Integer32"
_RtrIcmpRdPreferenceLevel_Object = MibTableColumn
rtrIcmpRdPreferenceLevel = _RtrIcmpRdPreferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 2, 2, 1, 7),
    _RtrIcmpRdPreferenceLevel_Type()
)
rtrIcmpRdPreferenceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpRdPreferenceLevel.setStatus("current")
_RtrIcmpRdEntStatus_Type = Integer32
_RtrIcmpRdEntStatus_Object = MibTableColumn
rtrIcmpRdEntStatus = _RtrIcmpRdEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 2, 2, 1, 8),
    _RtrIcmpRdEntStatus_Type()
)
rtrIcmpRdEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpRdEntStatus.setStatus("current")
_Rip2Spec_ObjectIdentity = ObjectIdentity
rip2Spec = _Rip2Spec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 3)
)
_RtrRip2IfConfTable_Object = MibTable
rtrRip2IfConfTable = _RtrRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rtrRip2IfConfTable.setStatus("current")
_RtrRip2IfConfEntry_Object = MibTableRow
rtrRip2IfConfEntry = _RtrRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 3, 1, 1)
)
rtrRip2IfConfEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrRip2IfConfAddress"),
)
if mibBuilder.loadTexts:
    rtrRip2IfConfEntry.setStatus("current")
_RtrRip2IfConfAddress_Type = IpAddress
_RtrRip2IfConfAddress_Object = MibTableColumn
rtrRip2IfConfAddress = _RtrRip2IfConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 3, 1, 1, 1),
    _RtrRip2IfConfAddress_Type()
)
rtrRip2IfConfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrRip2IfConfAddress.setStatus("current")


class _RtrRip2IfConfVirtualDis_Type(Integer32):
    """Custom type rtrRip2IfConfVirtualDis based on Integer32"""
    defaultValue = 1


_RtrRip2IfConfVirtualDis_Type.__name__ = "Integer32"
_RtrRip2IfConfVirtualDis_Object = MibTableColumn
rtrRip2IfConfVirtualDis = _RtrRip2IfConfVirtualDis_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 3, 1, 1, 2),
    _RtrRip2IfConfVirtualDis_Type()
)
rtrRip2IfConfVirtualDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrRip2IfConfVirtualDis.setStatus("deprecated")


class _RtrRip2IfConfAutoSend_Type(Integer32):
    """Custom type rtrRip2IfConfAutoSend based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RtrRip2IfConfAutoSend_Type.__name__ = "Integer32"
_RtrRip2IfConfAutoSend_Object = MibTableColumn
rtrRip2IfConfAutoSend = _RtrRip2IfConfAutoSend_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 3, 1, 1, 3),
    _RtrRip2IfConfAutoSend_Type()
)
rtrRip2IfConfAutoSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrRip2IfConfAutoSend.setStatus("deprecated")


class _RtrRip2IfConfRipEnable_Type(Integer32):
    """Custom type rtrRip2IfConfRipEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_RtrRip2IfConfRipEnable_Type.__name__ = "Integer32"
_RtrRip2IfConfRipEnable_Object = MibTableColumn
rtrRip2IfConfRipEnable = _RtrRip2IfConfRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 3, 1, 1, 4),
    _RtrRip2IfConfRipEnable_Type()
)
rtrRip2IfConfRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrRip2IfConfRipEnable.setStatus("current")
_ArpSpec_ObjectIdentity = ObjectIdentity
arpSpec = _ArpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 4)
)
_RtrArpDeleteTable_Type = Integer32
_RtrArpDeleteTable_Object = MibScalar
rtrArpDeleteTable = _RtrArpDeleteTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 4, 1),
    _RtrArpDeleteTable_Type()
)
rtrArpDeleteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrArpDeleteTable.setStatus("current")


class _RtrArpInactiveTimeOut_Type(Integer32):
    """Custom type rtrArpInactiveTimeOut based on Integer32"""
    defaultValue = 60000


_RtrArpInactiveTimeOut_Type.__name__ = "Integer32"
_RtrArpInactiveTimeOut_Object = MibScalar
rtrArpInactiveTimeOut = _RtrArpInactiveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 4, 2),
    _RtrArpInactiveTimeOut_Type()
)
rtrArpInactiveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrArpInactiveTimeOut.setStatus("current")


class _RtrArpProxy_Type(Integer32):
    """Custom type rtrArpProxy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RtrArpProxy_Type.__name__ = "Integer32"
_RtrArpProxy_Object = MibScalar
rtrArpProxy = _RtrArpProxy_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 4, 3),
    _RtrArpProxy_Type()
)
rtrArpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrArpProxy.setStatus("current")
_RtrNat_ObjectIdentity = ObjectIdentity
rtrNat = _RtrNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5)
)
_RtrNatIfConfTable_Object = MibTable
rtrNatIfConfTable = _RtrNatIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 1)
)
if mibBuilder.loadTexts:
    rtrNatIfConfTable.setStatus("current")
_RtrNatIfConfEntry_Object = MibTableRow
rtrNatIfConfEntry = _RtrNatIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 1, 1)
)
rtrNatIfConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAD-SubRtr-MIB", "rtrNatIfVirtualAddress"),
    (0, "RAD-SubRtr-MIB", "rtrNatIfVirtualMask"),
)
if mibBuilder.loadTexts:
    rtrNatIfConfEntry.setStatus("current")
_RtrNatIfVirtualAddress_Type = IpAddress
_RtrNatIfVirtualAddress_Object = MibTableColumn
rtrNatIfVirtualAddress = _RtrNatIfVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 1, 1, 1),
    _RtrNatIfVirtualAddress_Type()
)
rtrNatIfVirtualAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrNatIfVirtualAddress.setStatus("current")
_RtrNatIfVirtualMask_Type = IpAddress
_RtrNatIfVirtualMask_Object = MibTableColumn
rtrNatIfVirtualMask = _RtrNatIfVirtualMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 1, 1, 2),
    _RtrNatIfVirtualMask_Type()
)
rtrNatIfVirtualMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrNatIfVirtualMask.setStatus("current")
_RtrNatIfConfStatus_Type = RowStatus
_RtrNatIfConfStatus_Object = MibTableColumn
rtrNatIfConfStatus = _RtrNatIfConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 1, 1, 3),
    _RtrNatIfConfStatus_Type()
)
rtrNatIfConfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrNatIfConfStatus.setStatus("current")
_RtrNatIfRealAddress_Type = IpAddress
_RtrNatIfRealAddress_Object = MibTableColumn
rtrNatIfRealAddress = _RtrNatIfRealAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 1, 1, 4),
    _RtrNatIfRealAddress_Type()
)
rtrNatIfRealAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrNatIfRealAddress.setStatus("current")
_RtrNatIfRealMask_Type = IpAddress
_RtrNatIfRealMask_Object = MibTableColumn
rtrNatIfRealMask = _RtrNatIfRealMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 1, 1, 5),
    _RtrNatIfRealMask_Type()
)
rtrNatIfRealMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrNatIfRealMask.setStatus("current")


class _RtrNatIfType_Type(Integer32):
    """Custom type rtrNatIfType based on Integer32"""
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
        *(("static", 1),
          ("dynamic", 2),
          ("pat", 3),
          ("transparent", 4))
    )


_RtrNatIfType_Type.__name__ = "Integer32"
_RtrNatIfType_Object = MibTableColumn
rtrNatIfType = _RtrNatIfType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 1, 1, 6),
    _RtrNatIfType_Type()
)
rtrNatIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrNatIfType.setStatus("current")
_RtrPatTable_Object = MibTable
rtrPatTable = _RtrPatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 2)
)
if mibBuilder.loadTexts:
    rtrPatTable.setStatus("current")
_RtrPatEntry_Object = MibTableRow
rtrPatEntry = _RtrPatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 2, 1)
)
rtrPatEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrPatIdx"),
)
if mibBuilder.loadTexts:
    rtrPatEntry.setStatus("current")


class _RtrPatIdx_Type(Integer32):
    """Custom type rtrPatIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RtrPatIdx_Type.__name__ = "Integer32"
_RtrPatIdx_Object = MibTableColumn
rtrPatIdx = _RtrPatIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 2, 1, 1),
    _RtrPatIdx_Type()
)
rtrPatIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrPatIdx.setStatus("current")
_RtrPatRealAddress_Type = IpAddress
_RtrPatRealAddress_Object = MibTableColumn
rtrPatRealAddress = _RtrPatRealAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 2, 1, 2),
    _RtrPatRealAddress_Type()
)
rtrPatRealAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPatRealAddress.setStatus("current")
_RtrPatVirtualAddress_Type = IpAddress
_RtrPatVirtualAddress_Object = MibTableColumn
rtrPatVirtualAddress = _RtrPatVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 2, 1, 3),
    _RtrPatVirtualAddress_Type()
)
rtrPatVirtualAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPatVirtualAddress.setStatus("current")


class _RtrPatLowestPort_Type(Integer32):
    """Custom type rtrPatLowestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RtrPatLowestPort_Type.__name__ = "Integer32"
_RtrPatLowestPort_Object = MibTableColumn
rtrPatLowestPort = _RtrPatLowestPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 2, 1, 4),
    _RtrPatLowestPort_Type()
)
rtrPatLowestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPatLowestPort.setStatus("current")


class _RtrPatHighestPort_Type(Integer32):
    """Custom type rtrPatHighestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RtrPatHighestPort_Type.__name__ = "Integer32"
_RtrPatHighestPort_Object = MibTableColumn
rtrPatHighestPort = _RtrPatHighestPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 2, 1, 5),
    _RtrPatHighestPort_Type()
)
rtrPatHighestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPatHighestPort.setStatus("current")
_RtrPatProtocol_Type = Integer32
_RtrPatProtocol_Object = MibTableColumn
rtrPatProtocol = _RtrPatProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 2, 1, 6),
    _RtrPatProtocol_Type()
)
rtrPatProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPatProtocol.setStatus("current")
_RtrPatStatus_Type = RowStatus
_RtrPatStatus_Object = MibTableColumn
rtrPatStatus = _RtrPatStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 2, 5, 2, 1, 7),
    _RtrPatStatus_Type()
)
rtrPatStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPatStatus.setStatus("current")
_RtrInformationTable_Object = MibTable
rtrInformationTable = _RtrInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 3)
)
if mibBuilder.loadTexts:
    rtrInformationTable.setStatus("current")
_RtrInformationEntry_Object = MibTableRow
rtrInformationEntry = _RtrInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 3, 1)
)
rtrInformationEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrInformationId"),
)
if mibBuilder.loadTexts:
    rtrInformationEntry.setStatus("current")
_RtrInformationId_Type = Unsigned32
_RtrInformationId_Object = MibTableColumn
rtrInformationId = _RtrInformationId_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 3, 1, 1),
    _RtrInformationId_Type()
)
rtrInformationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrInformationId.setStatus("current")


class _RtrInformationProtMemAllocStatus_Type(Integer32):
    """Custom type rtrInformationProtMemAllocStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("clearError", 2),
          ("fatalError", 3))
    )


_RtrInformationProtMemAllocStatus_Type.__name__ = "Integer32"
_RtrInformationProtMemAllocStatus_Object = MibTableColumn
rtrInformationProtMemAllocStatus = _RtrInformationProtMemAllocStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 3, 1, 2),
    _RtrInformationProtMemAllocStatus_Type()
)
rtrInformationProtMemAllocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrInformationProtMemAllocStatus.setStatus("current")
_RtrInformationProtMemAllocInfo_Type = SnmpAdminString
_RtrInformationProtMemAllocInfo_Object = MibTableColumn
rtrInformationProtMemAllocInfo = _RtrInformationProtMemAllocInfo_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 3, 1, 3),
    _RtrInformationProtMemAllocInfo_Type()
)
rtrInformationProtMemAllocInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrInformationProtMemAllocInfo.setStatus("current")
_RtrFACS_ObjectIdentity = ObjectIdentity
rtrFACS = _RtrFACS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 5)
)


class _RtrFACSDefaultAction_Type(Integer32):
    """Custom type rtrFACSDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              129)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("forward", 2),
          ("blockAndReport", 129))
    )


_RtrFACSDefaultAction_Type.__name__ = "Integer32"
_RtrFACSDefaultAction_Object = MibScalar
rtrFACSDefaultAction = _RtrFACSDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 1),
    _RtrFACSDefaultAction_Type()
)
rtrFACSDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSDefaultAction.setStatus("current")
_RtrFACSActTable_Object = MibTable
rtrFACSActTable = _RtrFACSActTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 2)
)
if mibBuilder.loadTexts:
    rtrFACSActTable.setStatus("current")
_RtrFACSActEntry_Object = MibTableRow
rtrFACSActEntry = _RtrFACSActEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 2, 1)
)
rtrFACSActEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrFACSActType"),
    (0, "RAD-SubRtr-MIB", "rtrFACSActIfIndex"),
)
if mibBuilder.loadTexts:
    rtrFACSActEntry.setStatus("current")


class _RtrFACSActType_Type(Integer32):
    """Custom type rtrFACSActType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tx", 1),
          ("rx", 2))
    )


_RtrFACSActType_Type.__name__ = "Integer32"
_RtrFACSActType_Object = MibTableColumn
rtrFACSActType = _RtrFACSActType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 2, 1, 1),
    _RtrFACSActType_Type()
)
rtrFACSActType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFACSActType.setStatus("current")
_RtrFACSActIfIndex_Type = Integer32
_RtrFACSActIfIndex_Object = MibTableColumn
rtrFACSActIfIndex = _RtrFACSActIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 2, 1, 2),
    _RtrFACSActIfIndex_Type()
)
rtrFACSActIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFACSActIfIndex.setStatus("current")


class _RtrFACSAction_Type(Integer32):
    """Custom type rtrFACSAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("eraseIP", 2),
          ("eraseDECnet", 3),
          ("eraseIPX", 4),
          ("eraseBrg", 5),
          ("replaceIP", 6),
          ("replaceIPX", 8),
          ("replaceBrg", 9),
          ("backupIP", 10),
          ("backupIPX", 12),
          ("backupBrg", 13))
    )


_RtrFACSAction_Type.__name__ = "Integer32"
_RtrFACSAction_Object = MibTableColumn
rtrFACSAction = _RtrFACSAction_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 2, 1, 3),
    _RtrFACSAction_Type()
)
rtrFACSAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSAction.setStatus("current")


class _RtrFACSActiveDB_Type(Integer32):
    """Custom type rtrFACSActiveDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("temporary", 2))
    )


_RtrFACSActiveDB_Type.__name__ = "Integer32"
_RtrFACSActiveDB_Object = MibTableColumn
rtrFACSActiveDB = _RtrFACSActiveDB_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 2, 1, 4),
    _RtrFACSActiveDB_Type()
)
rtrFACSActiveDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSActiveDB.setStatus("current")
_RtrFACSTable_Object = MibTable
rtrFACSTable = _RtrFACSTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3)
)
if mibBuilder.loadTexts:
    rtrFACSTable.setStatus("current")
_RtrFACSEntry_Object = MibTableRow
rtrFACSEntry = _RtrFACSEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1)
)
rtrFACSEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrFACSIfIndex"),
    (0, "RAD-SubRtr-MIB", "rtrFACSProtocolType"),
    (0, "RAD-SubRtr-MIB", "rtrFACSType"),
    (0, "RAD-SubRtr-MIB", "rtrFACSIndex"),
)
if mibBuilder.loadTexts:
    rtrFACSEntry.setStatus("current")
_RtrFACSIfIndex_Type = Integer32
_RtrFACSIfIndex_Object = MibTableColumn
rtrFACSIfIndex = _RtrFACSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 1),
    _RtrFACSIfIndex_Type()
)
rtrFACSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFACSIfIndex.setStatus("current")


class _RtrFACSProtocolType_Type(Integer32):
    """Custom type rtrFACSProtocolType based on Integer32"""
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
        *(("ip", 1),
          ("ipx", 2),
          ("dec", 3),
          ("bridge", 4))
    )


_RtrFACSProtocolType_Type.__name__ = "Integer32"
_RtrFACSProtocolType_Object = MibTableColumn
rtrFACSProtocolType = _RtrFACSProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 2),
    _RtrFACSProtocolType_Type()
)
rtrFACSProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFACSProtocolType.setStatus("current")


class _RtrFACSType_Type(Integer32):
    """Custom type rtrFACSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tx", 1),
          ("rx", 2),
          ("cod", 3))
    )


_RtrFACSType_Type.__name__ = "Integer32"
_RtrFACSType_Object = MibTableColumn
rtrFACSType = _RtrFACSType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 3),
    _RtrFACSType_Type()
)
rtrFACSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFACSType.setStatus("current")
_RtrFACSIndex_Type = Integer32
_RtrFACSIndex_Object = MibTableColumn
rtrFACSIndex = _RtrFACSIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 4),
    _RtrFACSIndex_Type()
)
rtrFACSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFACSIndex.setStatus("current")
_RtrFACSSrcAdd_Type = OctetString
_RtrFACSSrcAdd_Object = MibTableColumn
rtrFACSSrcAdd = _RtrFACSSrcAdd_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 5),
    _RtrFACSSrcAdd_Type()
)
rtrFACSSrcAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSSrcAdd.setStatus("current")
_RtrFACSSrcAddMask_Type = OctetString
_RtrFACSSrcAddMask_Object = MibTableColumn
rtrFACSSrcAddMask = _RtrFACSSrcAddMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 6),
    _RtrFACSSrcAddMask_Type()
)
rtrFACSSrcAddMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSSrcAddMask.setStatus("current")
_RtrFACSDesAdd_Type = OctetString
_RtrFACSDesAdd_Object = MibTableColumn
rtrFACSDesAdd = _RtrFACSDesAdd_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 7),
    _RtrFACSDesAdd_Type()
)
rtrFACSDesAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSDesAdd.setStatus("current")
_RtrFACSDesAddMask_Type = OctetString
_RtrFACSDesAddMask_Object = MibTableColumn
rtrFACSDesAddMask = _RtrFACSDesAddMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 8),
    _RtrFACSDesAddMask_Type()
)
rtrFACSDesAddMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSDesAddMask.setStatus("current")


class _RtrFACSOperation_Type(Integer32):
    """Custom type rtrFACSOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              129)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("forward", 2),
          ("permit", 3),
          ("deny", 4),
          ("blockAndReport", 129))
    )


_RtrFACSOperation_Type.__name__ = "Integer32"
_RtrFACSOperation_Object = MibTableColumn
rtrFACSOperation = _RtrFACSOperation_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 9),
    _RtrFACSOperation_Type()
)
rtrFACSOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSOperation.setStatus("current")


class _RtrFACSNetFiltering_Type(Integer32):
    """Custom type rtrFACSNetFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("l2multicast", 2),
          ("arp", 3),
          ("icmp", 4),
          ("ip", 5),
          ("udp", 6),
          ("tcp", 7),
          ("decnet", 8),
          ("ipx", 9))
    )


_RtrFACSNetFiltering_Type.__name__ = "Integer32"
_RtrFACSNetFiltering_Object = MibTableColumn
rtrFACSNetFiltering = _RtrFACSNetFiltering_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 10),
    _RtrFACSNetFiltering_Type()
)
rtrFACSNetFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSNetFiltering.setStatus("current")
_RtrFACSSocketNum_Type = Integer32
_RtrFACSSocketNum_Object = MibTableColumn
rtrFACSSocketNum = _RtrFACSSocketNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 11),
    _RtrFACSSocketNum_Type()
)
rtrFACSSocketNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSSocketNum.setStatus("current")
_RtrFACSMask1Id_Type = Integer32
_RtrFACSMask1Id_Object = MibTableColumn
rtrFACSMask1Id = _RtrFACSMask1Id_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 12),
    _RtrFACSMask1Id_Type()
)
rtrFACSMask1Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSMask1Id.setStatus("current")
_RtrFACSMask2Id_Type = Integer32
_RtrFACSMask2Id_Object = MibTableColumn
rtrFACSMask2Id = _RtrFACSMask2Id_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 13),
    _RtrFACSMask2Id_Type()
)
rtrFACSMask2Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSMask2Id.setStatus("current")


class _RtrFACSStatus_Type(Integer32):
    """Custom type rtrFACSStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_RtrFACSStatus_Type.__name__ = "Integer32"
_RtrFACSStatus_Object = MibTableColumn
rtrFACSStatus = _RtrFACSStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 3, 1, 14),
    _RtrFACSStatus_Type()
)
rtrFACSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFACSStatus.setStatus("current")


class _RtrFACSFrameData_Type(OctetString):
    """Custom type rtrFACSFrameData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RtrFACSFrameData_Type.__name__ = "OctetString"
_RtrFACSFrameData_Object = MibScalar
rtrFACSFrameData = _RtrFACSFrameData_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 5, 4),
    _RtrFACSFrameData_Type()
)
rtrFACSFrameData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFACSFrameData.setStatus("current")
_RtrRtmEntityTable_Object = MibTable
rtrRtmEntityTable = _RtrRtmEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 6)
)
if mibBuilder.loadTexts:
    rtrRtmEntityTable.setStatus("current")
_RtrRtmEntityEntry_Object = MibTableRow
rtrRtmEntityEntry = _RtrRtmEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 6, 1)
)
rtrRtmEntityEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrRtmEntityAfiType"),
    (0, "RAD-SubRtr-MIB", "rtrRtmEntitySafi"),
)
if mibBuilder.loadTexts:
    rtrRtmEntityEntry.setStatus("current")
_RtrRtmEntityAfiType_Type = InetAddressType
_RtrRtmEntityAfiType_Object = MibTableColumn
rtrRtmEntityAfiType = _RtrRtmEntityAfiType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 6, 1, 1),
    _RtrRtmEntityAfiType_Type()
)
rtrRtmEntityAfiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRtmEntityAfiType.setStatus("current")
_RtrRtmEntitySafi_Type = RtrSafi
_RtrRtmEntitySafi_Object = MibTableColumn
rtrRtmEntitySafi = _RtrRtmEntitySafi_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 6, 1, 2),
    _RtrRtmEntitySafi_Type()
)
rtrRtmEntitySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRtmEntitySafi.setStatus("current")


class _RtrRtmEntityDsStatDf_Type(AdminDistance):
    """Custom type rtrRtmEntityDsStatDf based on AdminDistance"""
    defaultValue = 1


_RtrRtmEntityDsStatDf_Type.__name__ = "AdminDistance"
_RtrRtmEntityDsStatDf_Object = MibTableColumn
rtrRtmEntityDsStatDf = _RtrRtmEntityDsStatDf_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 6, 1, 3),
    _RtrRtmEntityDsStatDf_Type()
)
rtrRtmEntityDsStatDf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrRtmEntityDsStatDf.setStatus("current")


class _RtrRtmEntityDsOspfInt_Type(AdminDistance):
    """Custom type rtrRtmEntityDsOspfInt based on AdminDistance"""
    defaultValue = 30


_RtrRtmEntityDsOspfInt_Type.__name__ = "AdminDistance"
_RtrRtmEntityDsOspfInt_Object = MibTableColumn
rtrRtmEntityDsOspfInt = _RtrRtmEntityDsOspfInt_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 6, 1, 4),
    _RtrRtmEntityDsOspfInt_Type()
)
rtrRtmEntityDsOspfInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrRtmEntityDsOspfInt.setStatus("current")


class _RtrRtmEntityDsOspfExt_Type(AdminDistance):
    """Custom type rtrRtmEntityDsOspfExt based on AdminDistance"""
    defaultValue = 110


_RtrRtmEntityDsOspfExt_Type.__name__ = "AdminDistance"
_RtrRtmEntityDsOspfExt_Object = MibTableColumn
rtrRtmEntityDsOspfExt = _RtrRtmEntityDsOspfExt_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 6, 1, 5),
    _RtrRtmEntityDsOspfExt_Type()
)
rtrRtmEntityDsOspfExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrRtmEntityDsOspfExt.setStatus("current")


class _RtrRtmEntityDsIntBgp_Type(AdminDistance):
    """Custom type rtrRtmEntityDsIntBgp based on AdminDistance"""
    defaultValue = 200


_RtrRtmEntityDsIntBgp_Type.__name__ = "AdminDistance"
_RtrRtmEntityDsIntBgp_Object = MibTableColumn
rtrRtmEntityDsIntBgp = _RtrRtmEntityDsIntBgp_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 6, 1, 6),
    _RtrRtmEntityDsIntBgp_Type()
)
rtrRtmEntityDsIntBgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrRtmEntityDsIntBgp.setStatus("current")


class _RtrRtmEntityDsExtBgp_Type(AdminDistance):
    """Custom type rtrRtmEntityDsExtBgp based on AdminDistance"""
    defaultValue = 20


_RtrRtmEntityDsExtBgp_Type.__name__ = "AdminDistance"
_RtrRtmEntityDsExtBgp_Object = MibTableColumn
rtrRtmEntityDsExtBgp = _RtrRtmEntityDsExtBgp_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 6, 1, 7),
    _RtrRtmEntityDsExtBgp_Type()
)
rtrRtmEntityDsExtBgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrRtmEntityDsExtBgp.setStatus("current")
_RtrBridgePortConfigTable_Object = MibTable
rtrBridgePortConfigTable = _RtrBridgePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 1)
)
if mibBuilder.loadTexts:
    rtrBridgePortConfigTable.setStatus("current")
_RtrBridgePortConfigEntry_Object = MibTableRow
rtrBridgePortConfigEntry = _RtrBridgePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 1, 1)
)
rtrBridgePortConfigEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrBridgePortCIndex"),
)
if mibBuilder.loadTexts:
    rtrBridgePortConfigEntry.setStatus("current")
_RtrBridgePortCIndex_Type = Integer32
_RtrBridgePortCIndex_Object = MibTableColumn
rtrBridgePortCIndex = _RtrBridgePortCIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 1, 1, 1),
    _RtrBridgePortCIndex_Type()
)
rtrBridgePortCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrBridgePortCIndex.setStatus("current")
_RtrBridgePortCIf_Type = Integer32
_RtrBridgePortCIf_Object = MibTableColumn
rtrBridgePortCIf = _RtrBridgePortCIf_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 1, 1, 2),
    _RtrBridgePortCIf_Type()
)
rtrBridgePortCIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrBridgePortCIf.setStatus("current")
_RtrBridgePortCStatus_Type = RowStatus
_RtrBridgePortCStatus_Object = MibTableColumn
rtrBridgePortCStatus = _RtrBridgePortCStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 7, 1, 1, 3),
    _RtrBridgePortCStatus_Type()
)
rtrBridgePortCStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrBridgePortCStatus.setStatus("current")
_RadRouterConfig_ObjectIdentity = ObjectIdentity
radRouterConfig = _RadRouterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 9)
)
_RtrConfigTable_Object = MibTable
rtrConfigTable = _RtrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1)
)
if mibBuilder.loadTexts:
    rtrConfigTable.setStatus("current")
_RtrConfigEntry_Object = MibTableRow
rtrConfigEntry = _RtrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1)
)
rtrConfigEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrConfigIndex"),
)
if mibBuilder.loadTexts:
    rtrConfigEntry.setStatus("current")
_RtrConfigIndex_Type = Integer32
_RtrConfigIndex_Object = MibTableColumn
rtrConfigIndex = _RtrConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 1),
    _RtrConfigIndex_Type()
)
rtrConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrConfigIndex.setStatus("current")
_RtrConfigDefaultGateway_Type = IpAddress
_RtrConfigDefaultGateway_Object = MibTableColumn
rtrConfigDefaultGateway = _RtrConfigDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 2),
    _RtrConfigDefaultGateway_Type()
)
rtrConfigDefaultGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigDefaultGateway.setStatus("current")
_RtrConfigArpAgingTime_Type = Integer32
_RtrConfigArpAgingTime_Object = MibTableColumn
rtrConfigArpAgingTime = _RtrConfigArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 3),
    _RtrConfigArpAgingTime_Type()
)
rtrConfigArpAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigArpAgingTime.setStatus("current")
_RtrConfigClassifierTosMask_Type = Integer32
_RtrConfigClassifierTosMask_Object = MibTableColumn
rtrConfigClassifierTosMask = _RtrConfigClassifierTosMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 5),
    _RtrConfigClassifierTosMask_Type()
)
rtrConfigClassifierTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigClassifierTosMask.setStatus("current")


class _RtrConfigRIPMode_Type(Integer32):
    """Custom type rtrConfigRIPMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("rip1", 2),
          ("rip2", 3),
          ("rip1And2", 4))
    )


_RtrConfigRIPMode_Type.__name__ = "Integer32"
_RtrConfigRIPMode_Object = MibTableColumn
rtrConfigRIPMode = _RtrConfigRIPMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 6),
    _RtrConfigRIPMode_Type()
)
rtrConfigRIPMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigRIPMode.setStatus("current")


class _RtrConfigRoutingName_Type(SnmpAdminString):
    """Custom type rtrConfigRoutingName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RtrConfigRoutingName_Type.__name__ = "SnmpAdminString"
_RtrConfigRoutingName_Object = MibTableColumn
rtrConfigRoutingName = _RtrConfigRoutingName_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 7),
    _RtrConfigRoutingName_Type()
)
rtrConfigRoutingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigRoutingName.setStatus("current")
_RtrConfigRowStatus_Type = RowStatus
_RtrConfigRowStatus_Object = MibTableColumn
rtrConfigRowStatus = _RtrConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 8),
    _RtrConfigRowStatus_Type()
)
rtrConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigRowStatus.setStatus("current")


class _RtrConfigDhcpClientOpHostNameType_Type(Integer32):
    """Custom type rtrConfigDhcpClientOpHostNameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("userId", 0),
          ("sysName", 1))
    )


_RtrConfigDhcpClientOpHostNameType_Type.__name__ = "Integer32"
_RtrConfigDhcpClientOpHostNameType_Object = MibTableColumn
rtrConfigDhcpClientOpHostNameType = _RtrConfigDhcpClientOpHostNameType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 9),
    _RtrConfigDhcpClientOpHostNameType_Type()
)
rtrConfigDhcpClientOpHostNameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigDhcpClientOpHostNameType.setStatus("current")
_RtrConfigDhcpClientOpHostName_Type = SnmpAdminString
_RtrConfigDhcpClientOpHostName_Object = MibTableColumn
rtrConfigDhcpClientOpHostName = _RtrConfigDhcpClientOpHostName_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 10),
    _RtrConfigDhcpClientOpHostName_Type()
)
rtrConfigDhcpClientOpHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigDhcpClientOpHostName.setStatus("current")


class _RtrConfigDhcpClientOpVendorClassIdType_Type(Integer32):
    """Custom type rtrConfigDhcpClientOpVendorClassIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("userId", 0),
          ("entPhysicalName", 1))
    )


_RtrConfigDhcpClientOpVendorClassIdType_Type.__name__ = "Integer32"
_RtrConfigDhcpClientOpVendorClassIdType_Object = MibTableColumn
rtrConfigDhcpClientOpVendorClassIdType = _RtrConfigDhcpClientOpVendorClassIdType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 11),
    _RtrConfigDhcpClientOpVendorClassIdType_Type()
)
rtrConfigDhcpClientOpVendorClassIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigDhcpClientOpVendorClassIdType.setStatus("current")
_RtrConfigDhcpClientOpVendorClassId_Type = SnmpAdminString
_RtrConfigDhcpClientOpVendorClassId_Object = MibTableColumn
rtrConfigDhcpClientOpVendorClassId = _RtrConfigDhcpClientOpVendorClassId_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 12),
    _RtrConfigDhcpClientOpVendorClassId_Type()
)
rtrConfigDhcpClientOpVendorClassId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigDhcpClientOpVendorClassId.setStatus("current")


class _RtrConfigDhcpClientOpControl_Type(Bits):
    """Custom type rtrConfigDhcpClientOpControl based on Bits"""
    namedValues = NamedValues(
        *(("vendorClassId", 0),
          ("hostName", 1))
    )

_RtrConfigDhcpClientOpControl_Type.__name__ = "Bits"
_RtrConfigDhcpClientOpControl_Object = MibTableColumn
rtrConfigDhcpClientOpControl = _RtrConfigDhcpClientOpControl_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 13),
    _RtrConfigDhcpClientOpControl_Type()
)
rtrConfigDhcpClientOpControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigDhcpClientOpControl.setStatus("current")


class _RtrConfigClearIpv4ArpCmd_Type(Integer32):
    """Custom type rtrConfigClearIpv4ArpCmd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_RtrConfigClearIpv4ArpCmd_Type.__name__ = "Integer32"
_RtrConfigClearIpv4ArpCmd_Object = MibTableColumn
rtrConfigClearIpv4ArpCmd = _RtrConfigClearIpv4ArpCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 14),
    _RtrConfigClearIpv4ArpCmd_Type()
)
rtrConfigClearIpv4ArpCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigClearIpv4ArpCmd.setStatus("current")


class _RtrConfigClearIpv6NeighborCmd_Type(Integer32):
    """Custom type rtrConfigClearIpv6NeighborCmd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_RtrConfigClearIpv6NeighborCmd_Type.__name__ = "Integer32"
_RtrConfigClearIpv6NeighborCmd_Object = MibTableColumn
rtrConfigClearIpv6NeighborCmd = _RtrConfigClearIpv6NeighborCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 15),
    _RtrConfigClearIpv6NeighborCmd_Type()
)
rtrConfigClearIpv6NeighborCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigClearIpv6NeighborCmd.setStatus("current")


class _RtrConfigRouterDscp_Type(Unsigned32):
    """Custom type rtrConfigRouterDscp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RtrConfigRouterDscp_Type.__name__ = "Unsigned32"
_RtrConfigRouterDscp_Object = MibTableColumn
rtrConfigRouterDscp = _RtrConfigRouterDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 1, 1, 16),
    _RtrConfigRouterDscp_Type()
)
rtrConfigRouterDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrConfigRouterDscp.setStatus("current")
_RtrSystemAddress_Type = IpAddress
_RtrSystemAddress_Object = MibScalar
rtrSystemAddress = _RtrSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 2),
    _RtrSystemAddress_Type()
)
rtrSystemAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrSystemAddress.setStatus("current")
_RtrFwdTable_Object = MibTable
rtrFwdTable = _RtrFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3)
)
if mibBuilder.loadTexts:
    rtrFwdTable.setStatus("current")
_RtrFwdEntry_Object = MibTableRow
rtrFwdEntry = _RtrFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3, 1)
)
rtrFwdEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrFwdIdx"),
    (0, "RAD-SubRtr-MIB", "rtrFwdIpAddress"),
    (0, "RAD-SubRtr-MIB", "rtrFwdIpMask"),
    (0, "RAD-SubRtr-MIB", "rtrFwdRuleIdx"),
)
if mibBuilder.loadTexts:
    rtrFwdEntry.setStatus("current")
_RtrFwdIdx_Type = Integer32
_RtrFwdIdx_Object = MibTableColumn
rtrFwdIdx = _RtrFwdIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3, 1, 1),
    _RtrFwdIdx_Type()
)
rtrFwdIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFwdIdx.setStatus("current")
_RtrFwdIpAddress_Type = IpAddress
_RtrFwdIpAddress_Object = MibTableColumn
rtrFwdIpAddress = _RtrFwdIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3, 1, 2),
    _RtrFwdIpAddress_Type()
)
rtrFwdIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFwdIpAddress.setStatus("current")
_RtrFwdIpMask_Type = IpAddress
_RtrFwdIpMask_Object = MibTableColumn
rtrFwdIpMask = _RtrFwdIpMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3, 1, 3),
    _RtrFwdIpMask_Type()
)
rtrFwdIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFwdIpMask.setStatus("current")
_RtrFwdRuleIdx_Type = Integer32
_RtrFwdRuleIdx_Object = MibTableColumn
rtrFwdRuleIdx = _RtrFwdRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3, 1, 4),
    _RtrFwdRuleIdx_Type()
)
rtrFwdRuleIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFwdRuleIdx.setStatus("current")
_RtrFwdRowStatus_Type = RowStatus
_RtrFwdRowStatus_Object = MibTableColumn
rtrFwdRowStatus = _RtrFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3, 1, 5),
    _RtrFwdRowStatus_Type()
)
rtrFwdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrFwdRowStatus.setStatus("current")
_RtrFwdNextHop_Type = IpAddress
_RtrFwdNextHop_Object = MibTableColumn
rtrFwdNextHop = _RtrFwdNextHop_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3, 1, 6),
    _RtrFwdNextHop_Type()
)
rtrFwdNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrFwdNextHop.setStatus("current")
_RtrFwdIfIndex_Type = Integer32
_RtrFwdIfIndex_Object = MibTableColumn
rtrFwdIfIndex = _RtrFwdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3, 1, 7),
    _RtrFwdIfIndex_Type()
)
rtrFwdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFwdIfIndex.setStatus("current")


class _RtrFwdType_Type(Integer32):
    """Custom type rtrFwdType based on Integer32"""
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
        *(("other", 1),
          ("reject", 2),
          ("local", 3),
          ("remote", 4))
    )


_RtrFwdType_Type.__name__ = "Integer32"
_RtrFwdType_Object = MibTableColumn
rtrFwdType = _RtrFwdType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3, 1, 8),
    _RtrFwdType_Type()
)
rtrFwdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrFwdType.setStatus("current")


class _RtrFwdProto_Type(Integer32):
    """Custom type rtrFwdProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              41)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("rip", 8),
          ("lis", 41))
    )


_RtrFwdProto_Type.__name__ = "Integer32"
_RtrFwdProto_Object = MibTableColumn
rtrFwdProto = _RtrFwdProto_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3, 1, 9),
    _RtrFwdProto_Type()
)
rtrFwdProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFwdProto.setStatus("current")
_RtrFwdEthQueue_Type = Integer32
_RtrFwdEthQueue_Object = MibTableColumn
rtrFwdEthQueue = _RtrFwdEthQueue_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3, 1, 10),
    _RtrFwdEthQueue_Type()
)
rtrFwdEthQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrFwdEthQueue.setStatus("current")


class _RtrFwdMetric1_Type(Integer32):
    """Custom type rtrFwdMetric1 based on Integer32"""
    defaultValue = -1


_RtrFwdMetric1_Type.__name__ = "Integer32"
_RtrFwdMetric1_Object = MibTableColumn
rtrFwdMetric1 = _RtrFwdMetric1_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 3, 1, 11),
    _RtrFwdMetric1_Type()
)
rtrFwdMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrFwdMetric1.setStatus("current")
_RtrPbrTable_Object = MibTable
rtrPbrTable = _RtrPbrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4)
)
if mibBuilder.loadTexts:
    rtrPbrTable.setStatus("current")
_RtrPbrEntry_Object = MibTableRow
rtrPbrEntry = _RtrPbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1)
)
rtrPbrEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrPbrIdx"),
    (0, "RAD-SubRtr-MIB", "rtrPbrInterface"),
    (0, "RAD-SubRtr-MIB", "rtrPbrRuleIdx"),
)
if mibBuilder.loadTexts:
    rtrPbrEntry.setStatus("current")
_RtrPbrIdx_Type = Unsigned32
_RtrPbrIdx_Object = MibTableColumn
rtrPbrIdx = _RtrPbrIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 1),
    _RtrPbrIdx_Type()
)
rtrPbrIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrPbrIdx.setStatus("current")
_RtrPbrInterface_Type = InterfaceIndex
_RtrPbrInterface_Object = MibTableColumn
rtrPbrInterface = _RtrPbrInterface_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 2),
    _RtrPbrInterface_Type()
)
rtrPbrInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrPbrInterface.setStatus("current")
_RtrPbrRuleIdx_Type = Unsigned32
_RtrPbrRuleIdx_Object = MibTableColumn
rtrPbrRuleIdx = _RtrPbrRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 3),
    _RtrPbrRuleIdx_Type()
)
rtrPbrRuleIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrPbrRuleIdx.setStatus("current")
_RtrPbrRowStatus_Type = RowStatus
_RtrPbrRowStatus_Object = MibTableColumn
rtrPbrRowStatus = _RtrPbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 4),
    _RtrPbrRowStatus_Type()
)
rtrPbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPbrRowStatus.setStatus("current")


class _RtrPbrMatchAllFrames_Type(Integer32):
    """Custom type rtrPbrMatchAllFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_RtrPbrMatchAllFrames_Type.__name__ = "Integer32"
_RtrPbrMatchAllFrames_Object = MibTableColumn
rtrPbrMatchAllFrames = _RtrPbrMatchAllFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 5),
    _RtrPbrMatchAllFrames_Type()
)
rtrPbrMatchAllFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPbrMatchAllFrames.setStatus("current")
_RtrPbrSourceIpAddress_Type = IpAddress
_RtrPbrSourceIpAddress_Object = MibTableColumn
rtrPbrSourceIpAddress = _RtrPbrSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 6),
    _RtrPbrSourceIpAddress_Type()
)
rtrPbrSourceIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPbrSourceIpAddress.setStatus("current")
_RtrPbrSourceIpMask_Type = IpAddress
_RtrPbrSourceIpMask_Object = MibTableColumn
rtrPbrSourceIpMask = _RtrPbrSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 7),
    _RtrPbrSourceIpMask_Type()
)
rtrPbrSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPbrSourceIpMask.setStatus("current")
_RtrPbrDestIpAddress_Type = IpAddress
_RtrPbrDestIpAddress_Object = MibTableColumn
rtrPbrDestIpAddress = _RtrPbrDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 8),
    _RtrPbrDestIpAddress_Type()
)
rtrPbrDestIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPbrDestIpAddress.setStatus("current")
_RtrPbrDestIpMask_Type = IpAddress
_RtrPbrDestIpMask_Object = MibTableColumn
rtrPbrDestIpMask = _RtrPbrDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 9),
    _RtrPbrDestIpMask_Type()
)
rtrPbrDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPbrDestIpMask.setStatus("current")
_RtrPbrIpProtocol_Type = Unsigned32
_RtrPbrIpProtocol_Object = MibTableColumn
rtrPbrIpProtocol = _RtrPbrIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 10),
    _RtrPbrIpProtocol_Type()
)
rtrPbrIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPbrIpProtocol.setStatus("current")
_RtrPbrMinFrameLength_Type = Unsigned32
_RtrPbrMinFrameLength_Object = MibTableColumn
rtrPbrMinFrameLength = _RtrPbrMinFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 11),
    _RtrPbrMinFrameLength_Type()
)
rtrPbrMinFrameLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPbrMinFrameLength.setStatus("current")
_RtrPbrMaxFrameLength_Type = Unsigned32
_RtrPbrMaxFrameLength_Object = MibTableColumn
rtrPbrMaxFrameLength = _RtrPbrMaxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 12),
    _RtrPbrMaxFrameLength_Type()
)
rtrPbrMaxFrameLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPbrMaxFrameLength.setStatus("current")


class _RtrPbrDiscardFrame_Type(Integer32):
    """Custom type rtrPbrDiscardFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_RtrPbrDiscardFrame_Type.__name__ = "Integer32"
_RtrPbrDiscardFrame_Object = MibTableColumn
rtrPbrDiscardFrame = _RtrPbrDiscardFrame_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 13),
    _RtrPbrDiscardFrame_Type()
)
rtrPbrDiscardFrame.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPbrDiscardFrame.setStatus("current")
_RtrPbrForwardingInterface_Type = InterfaceIndexOrZero
_RtrPbrForwardingInterface_Object = MibTableColumn
rtrPbrForwardingInterface = _RtrPbrForwardingInterface_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 14),
    _RtrPbrForwardingInterface_Type()
)
rtrPbrForwardingInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPbrForwardingInterface.setStatus("current")
_RtrPbrNextHop_Type = IpAddress
_RtrPbrNextHop_Object = MibTableColumn
rtrPbrNextHop = _RtrPbrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 4, 1, 15),
    _RtrPbrNextHop_Type()
)
rtrPbrNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPbrNextHop.setStatus("current")
_RtrSourceAddressTable_Object = MibTable
rtrSourceAddressTable = _RtrSourceAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 6)
)
if mibBuilder.loadTexts:
    rtrSourceAddressTable.setStatus("current")
_RtrSourceAddressEntry_Object = MibTableRow
rtrSourceAddressEntry = _RtrSourceAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 6, 1)
)
rtrSourceAddressEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrSourceAddressApp"),
    (0, "RAD-SubRtr-MIB", "rtrSourceAddressType"),
    (0, "RAD-SubRtr-MIB", "rtrSourceAddress"),
    (0, "RAD-SubRtr-MIB", "rtrSourceAddressIfIndex"),
)
if mibBuilder.loadTexts:
    rtrSourceAddressEntry.setStatus("current")


class _RtrSourceAddressApp_Type(Integer32):
    """Custom type rtrSourceAddressApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("trap", 2),
          ("loopback", 3),
          ("clock", 4),
          ("managementAll", 255))
    )


_RtrSourceAddressApp_Type.__name__ = "Integer32"
_RtrSourceAddressApp_Object = MibTableColumn
rtrSourceAddressApp = _RtrSourceAddressApp_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 6, 1, 1),
    _RtrSourceAddressApp_Type()
)
rtrSourceAddressApp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrSourceAddressApp.setStatus("current")
_RtrSourceAddressType_Type = InetAddressType
_RtrSourceAddressType_Object = MibTableColumn
rtrSourceAddressType = _RtrSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 6, 1, 2),
    _RtrSourceAddressType_Type()
)
rtrSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrSourceAddressType.setStatus("current")
_RtrSourceAddress_Type = InetAddress
_RtrSourceAddress_Object = MibTableColumn
rtrSourceAddress = _RtrSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 6, 1, 3),
    _RtrSourceAddress_Type()
)
rtrSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrSourceAddress.setStatus("current")
_RtrSourceAddressIfIndex_Type = Unsigned32
_RtrSourceAddressIfIndex_Object = MibTableColumn
rtrSourceAddressIfIndex = _RtrSourceAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 6, 1, 4),
    _RtrSourceAddressIfIndex_Type()
)
rtrSourceAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrSourceAddressIfIndex.setStatus("current")
_RtrSourceAddressRowStatus_Type = RowStatus
_RtrSourceAddressRowStatus_Object = MibTableColumn
rtrSourceAddressRowStatus = _RtrSourceAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 6, 1, 5),
    _RtrSourceAddressRowStatus_Type()
)
rtrSourceAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrSourceAddressRowStatus.setStatus("current")
_RtrRedistTable_Object = MibTable
rtrRedistTable = _RtrRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 7)
)
if mibBuilder.loadTexts:
    rtrRedistTable.setStatus("current")
_RtrRedistEntry_Object = MibTableRow
rtrRedistEntry = _RtrRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 7, 1)
)
rtrRedistEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrRedistAfiType"),
    (0, "RAD-SubRtr-MIB", "rtrRedistSafi"),
    (0, "RAD-SubRtr-MIB", "rtrRedistInfoSrc"),
    (0, "RAD-SubRtr-MIB", "rtrRedistInfoDest"),
)
if mibBuilder.loadTexts:
    rtrRedistEntry.setStatus("current")
_RtrRedistAfiType_Type = InetAddressType
_RtrRedistAfiType_Object = MibTableColumn
rtrRedistAfiType = _RtrRedistAfiType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 7, 1, 1),
    _RtrRedistAfiType_Type()
)
rtrRedistAfiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRedistAfiType.setStatus("current")
_RtrRedistSafi_Type = RtrSafi
_RtrRedistSafi_Object = MibTableColumn
rtrRedistSafi = _RtrRedistSafi_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 7, 1, 2),
    _RtrRedistSafi_Type()
)
rtrRedistSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRedistSafi.setStatus("current")


class _RtrRedistInfoSrc_Type(InfoSourceDest):
    """Custom type rtrRedistInfoSrc based on InfoSourceDest"""
    defaultValue = 0


_RtrRedistInfoSrc_Type.__name__ = "InfoSourceDest"
_RtrRedistInfoSrc_Object = MibTableColumn
rtrRedistInfoSrc = _RtrRedistInfoSrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 7, 1, 3),
    _RtrRedistInfoSrc_Type()
)
rtrRedistInfoSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRedistInfoSrc.setStatus("current")


class _RtrRedistInfoDest_Type(InfoSourceDest):
    """Custom type rtrRedistInfoDest based on InfoSourceDest"""
    defaultValue = 0


_RtrRedistInfoDest_Type.__name__ = "InfoSourceDest"
_RtrRedistInfoDest_Object = MibTableColumn
rtrRedistInfoDest = _RtrRedistInfoDest_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 7, 1, 4),
    _RtrRedistInfoDest_Type()
)
rtrRedistInfoDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRedistInfoDest.setStatus("current")
_RtrRedistRowStatus_Type = RowStatus
_RtrRedistRowStatus_Object = MibTableColumn
rtrRedistRowStatus = _RtrRedistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 9, 7, 1, 5),
    _RtrRedistRowStatus_Type()
)
rtrRedistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrRedistRowStatus.setStatus("current")
_RtrPolicy_ObjectIdentity = ObjectIdentity
rtrPolicy = _RtrPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 13)
)
_RtrPolicyMainTable_Object = MibTable
rtrPolicyMainTable = _RtrPolicyMainTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 1)
)
if mibBuilder.loadTexts:
    rtrPolicyMainTable.setStatus("current")
_RtrPolicyMainEntry_Object = MibTableRow
rtrPolicyMainEntry = _RtrPolicyMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 1, 1)
)
rtrPolicyMainEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrPolicyName"),
)
if mibBuilder.loadTexts:
    rtrPolicyMainEntry.setStatus("current")


class _RtrPolicyName_Type(SnmpAdminString):
    """Custom type rtrPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RtrPolicyName_Type.__name__ = "SnmpAdminString"
_RtrPolicyName_Object = MibTableColumn
rtrPolicyName = _RtrPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 1, 1, 1),
    _RtrPolicyName_Type()
)
rtrPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrPolicyName.setStatus("current")
_RtrPolicyNumberOfRules_Type = Unsigned32
_RtrPolicyNumberOfRules_Object = MibTableColumn
rtrPolicyNumberOfRules = _RtrPolicyNumberOfRules_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 1, 1, 2),
    _RtrPolicyNumberOfRules_Type()
)
rtrPolicyNumberOfRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrPolicyNumberOfRules.setStatus("current")
_RtrPolicyLastSeqeunceNumber_Type = Unsigned32
_RtrPolicyLastSeqeunceNumber_Object = MibTableColumn
rtrPolicyLastSeqeunceNumber = _RtrPolicyLastSeqeunceNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 1, 1, 3),
    _RtrPolicyLastSeqeunceNumber_Type()
)
rtrPolicyLastSeqeunceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrPolicyLastSeqeunceNumber.setStatus("current")
_RtrPolicyResequenceCmd_Type = Unsigned32
_RtrPolicyResequenceCmd_Object = MibTableColumn
rtrPolicyResequenceCmd = _RtrPolicyResequenceCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 1, 1, 4),
    _RtrPolicyResequenceCmd_Type()
)
rtrPolicyResequenceCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPolicyResequenceCmd.setStatus("current")


class _RtrPolicyType_Type(Integer32):
    """Custom type rtrPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bgpPrefixListIpv4", 2),
          ("bgpPrefixListIpv6", 3),
          ("bgpRouteMap", 4))
    )


_RtrPolicyType_Type.__name__ = "Integer32"
_RtrPolicyType_Object = MibTableColumn
rtrPolicyType = _RtrPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 1, 1, 5),
    _RtrPolicyType_Type()
)
rtrPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPolicyType.setStatus("current")
_RtrPolicyRowStatus_Type = RowStatus
_RtrPolicyRowStatus_Object = MibTableColumn
rtrPolicyRowStatus = _RtrPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 1, 1, 6),
    _RtrPolicyRowStatus_Type()
)
rtrPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPolicyRowStatus.setStatus("current")
_RtrPolicyRuleTable_Object = MibTable
rtrPolicyRuleTable = _RtrPolicyRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 2)
)
if mibBuilder.loadTexts:
    rtrPolicyRuleTable.setStatus("current")
_RtrPolicyRuleEntry_Object = MibTableRow
rtrPolicyRuleEntry = _RtrPolicyRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 2, 1)
)
rtrPolicyRuleEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrPolicyRuleIdx"),
)
if mibBuilder.loadTexts:
    rtrPolicyRuleEntry.setStatus("current")
_RtrPolicyRuleIdx_Type = Unsigned32
_RtrPolicyRuleIdx_Object = MibTableColumn
rtrPolicyRuleIdx = _RtrPolicyRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 2, 1, 1),
    _RtrPolicyRuleIdx_Type()
)
rtrPolicyRuleIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrPolicyRuleIdx.setStatus("current")


class _RtrPolicyRuleName_Type(SnmpAdminString):
    """Custom type rtrPolicyRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_RtrPolicyRuleName_Type.__name__ = "SnmpAdminString"
_RtrPolicyRuleName_Object = MibTableColumn
rtrPolicyRuleName = _RtrPolicyRuleName_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 2, 1, 2),
    _RtrPolicyRuleName_Type()
)
rtrPolicyRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPolicyRuleName.setStatus("current")
_RtrPolicyRuleSequenceNumber_Type = Unsigned32
_RtrPolicyRuleSequenceNumber_Object = MibTableColumn
rtrPolicyRuleSequenceNumber = _RtrPolicyRuleSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 2, 1, 3),
    _RtrPolicyRuleSequenceNumber_Type()
)
rtrPolicyRuleSequenceNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPolicyRuleSequenceNumber.setStatus("current")


class _RtrPolicyRuleType_Type(Integer32):
    """Custom type rtrPolicyRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("remark", 1),
          ("deny", 2),
          ("permit", 3))
    )


_RtrPolicyRuleType_Type.__name__ = "Integer32"
_RtrPolicyRuleType_Object = MibTableColumn
rtrPolicyRuleType = _RtrPolicyRuleType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 2, 1, 4),
    _RtrPolicyRuleType_Type()
)
rtrPolicyRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPolicyRuleType.setStatus("current")
_RtrPolicyRulePointer_Type = RowPointer
_RtrPolicyRulePointer_Object = MibTableColumn
rtrPolicyRulePointer = _RtrPolicyRulePointer_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 2, 1, 5),
    _RtrPolicyRulePointer_Type()
)
rtrPolicyRulePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPolicyRulePointer.setStatus("current")
_RtrPolicyRuleRowStatus_Type = RowStatus
_RtrPolicyRuleRowStatus_Object = MibTableColumn
rtrPolicyRuleRowStatus = _RtrPolicyRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 2, 1, 6),
    _RtrPolicyRuleRowStatus_Type()
)
rtrPolicyRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPolicyRuleRowStatus.setStatus("current")
_RtrPolicyInvRuleTable_Object = MibTable
rtrPolicyInvRuleTable = _RtrPolicyInvRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 3)
)
if mibBuilder.loadTexts:
    rtrPolicyInvRuleTable.setStatus("current")
_RtrPolicyInvRuleEntry_Object = MibTableRow
rtrPolicyInvRuleEntry = _RtrPolicyInvRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 3, 1)
)
rtrPolicyInvRuleEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrPolicyName"),
    (0, "RAD-SubRtr-MIB", "rtrPolicyRuleSequenceNumber"),
)
if mibBuilder.loadTexts:
    rtrPolicyInvRuleEntry.setStatus("current")
_RtrPolicyInvRuleIdx_Type = Unsigned32
_RtrPolicyInvRuleIdx_Object = MibTableColumn
rtrPolicyInvRuleIdx = _RtrPolicyInvRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 3, 1, 1),
    _RtrPolicyInvRuleIdx_Type()
)
rtrPolicyInvRuleIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrPolicyInvRuleIdx.setStatus("current")


class _RtrPolicyInvRuleType_Type(Integer32):
    """Custom type rtrPolicyInvRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("remark", 1),
          ("deny", 2),
          ("permit", 3))
    )


_RtrPolicyInvRuleType_Type.__name__ = "Integer32"
_RtrPolicyInvRuleType_Object = MibTableColumn
rtrPolicyInvRuleType = _RtrPolicyInvRuleType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 3, 1, 2),
    _RtrPolicyInvRuleType_Type()
)
rtrPolicyInvRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrPolicyInvRuleType.setStatus("current")
_RtrPolicyInvRulePointer_Type = RowPointer
_RtrPolicyInvRulePointer_Object = MibTableColumn
rtrPolicyInvRulePointer = _RtrPolicyInvRulePointer_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 3, 1, 3),
    _RtrPolicyInvRulePointer_Type()
)
rtrPolicyInvRulePointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrPolicyInvRulePointer.setStatus("current")
_RtrPolicyRuleRemarkTable_Object = MibTable
rtrPolicyRuleRemarkTable = _RtrPolicyRuleRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 4)
)
if mibBuilder.loadTexts:
    rtrPolicyRuleRemarkTable.setStatus("current")
_RtrPolicyRuleRemarkEntry_Object = MibTableRow
rtrPolicyRuleRemarkEntry = _RtrPolicyRuleRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 4, 1)
)
rtrPolicyRuleRemarkEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrPolicyRuleIdx"),
)
if mibBuilder.loadTexts:
    rtrPolicyRuleRemarkEntry.setStatus("current")


class _RtrPolicyRuleRemark_Type(SnmpAdminString):
    """Custom type rtrPolicyRuleRemark based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_RtrPolicyRuleRemark_Type.__name__ = "SnmpAdminString"
_RtrPolicyRuleRemark_Object = MibTableColumn
rtrPolicyRuleRemark = _RtrPolicyRuleRemark_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 13, 4, 1, 1),
    _RtrPolicyRuleRemark_Type()
)
rtrPolicyRuleRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtrPolicyRuleRemark.setStatus("current")
_RtrDhcp_ObjectIdentity = ObjectIdentity
rtrDhcp = _RtrDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 15)
)
_RtrDhcpRelay_ObjectIdentity = ObjectIdentity
rtrDhcpRelay = _RtrDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 15, 1)
)
_DhcpRelayServerTable_Object = MibTable
dhcpRelayServerTable = _DhcpRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 15, 1, 2)
)
if mibBuilder.loadTexts:
    dhcpRelayServerTable.setStatus("current")
_DhcpRelayServerEntry_Object = MibTableRow
dhcpRelayServerEntry = _DhcpRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 15, 1, 2, 1)
)
dhcpRelayServerEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "dhcpRelayServerRtrIfIndex"),
    (0, "RAD-SubRtr-MIB", "dhcpRelayServerAddrType"),
    (0, "RAD-SubRtr-MIB", "dhcpRelayServerAddr"),
)
if mibBuilder.loadTexts:
    dhcpRelayServerEntry.setStatus("current")
_DhcpRelayServerRtrIfIndex_Type = InterfaceIndex
_DhcpRelayServerRtrIfIndex_Object = MibTableColumn
dhcpRelayServerRtrIfIndex = _DhcpRelayServerRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 15, 1, 2, 1, 1),
    _DhcpRelayServerRtrIfIndex_Type()
)
dhcpRelayServerRtrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpRelayServerRtrIfIndex.setStatus("current")
_DhcpRelayServerAddrType_Type = InetAddressType
_DhcpRelayServerAddrType_Object = MibTableColumn
dhcpRelayServerAddrType = _DhcpRelayServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 15, 1, 2, 1, 2),
    _DhcpRelayServerAddrType_Type()
)
dhcpRelayServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpRelayServerAddrType.setStatus("current")
_DhcpRelayServerAddr_Type = InetAddress
_DhcpRelayServerAddr_Object = MibTableColumn
dhcpRelayServerAddr = _DhcpRelayServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 15, 1, 2, 1, 3),
    _DhcpRelayServerAddr_Type()
)
dhcpRelayServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpRelayServerAddr.setStatus("current")
_DhcpRelayServerRowStatus_Type = RowStatus
_DhcpRelayServerRowStatus_Object = MibTableColumn
dhcpRelayServerRowStatus = _DhcpRelayServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 15, 1, 2, 1, 4),
    _DhcpRelayServerRowStatus_Type()
)
dhcpRelayServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayServerRowStatus.setStatus("current")
_RtrRouterEntity_ObjectIdentity = ObjectIdentity
rtrRouterEntity = _RtrRouterEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 16)
)
_RtrRibTable_Object = MibTable
rtrRibTable = _RtrRibTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1)
)
if mibBuilder.loadTexts:
    rtrRibTable.setStatus("current")
_RtrRibEntry_Object = MibTableRow
rtrRibEntry = _RtrRibEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1, 1)
)
rtrRibEntry.setIndexNames(
    (0, "RAD-SubRtr-MIB", "rtrRibDestType"),
    (0, "RAD-SubRtr-MIB", "rtrRibDest"),
    (0, "RAD-SubRtr-MIB", "rtrRibDestLen"),
    (0, "RAD-SubRtr-MIB", "rtrRibTos"),
    (0, "RAD-SubRtr-MIB", "rtrRibNextHopType"),
    (0, "RAD-SubRtr-MIB", "rtrRibNextHop"),
    (0, "RAD-SubRtr-MIB", "rtrRibIfIndex"),
    (0, "RAD-SubRtr-MIB", "rtrRibProto"),
    (0, "RAD-SubRtr-MIB", "rtrRibRpmIndex"),
)
if mibBuilder.loadTexts:
    rtrRibEntry.setStatus("current")
_RtrRibDestType_Type = InetAddressType
_RtrRibDestType_Object = MibTableColumn
rtrRibDestType = _RtrRibDestType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1, 1, 1),
    _RtrRibDestType_Type()
)
rtrRibDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRibDestType.setStatus("current")


class _RtrRibDest_Type(InetAddress):
    """Custom type rtrRibDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtrRibDest_Type.__name__ = "InetAddress"
_RtrRibDest_Object = MibTableColumn
rtrRibDest = _RtrRibDest_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1, 1, 2),
    _RtrRibDest_Type()
)
rtrRibDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRibDest.setStatus("current")


class _RtrRibDestLen_Type(Integer32):
    """Custom type rtrRibDestLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RtrRibDestLen_Type.__name__ = "Integer32"
_RtrRibDestLen_Object = MibTableColumn
rtrRibDestLen = _RtrRibDestLen_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1, 1, 3),
    _RtrRibDestLen_Type()
)
rtrRibDestLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRibDestLen.setStatus("current")


class _RtrRibTos_Type(Integer32):
    """Custom type rtrRibTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RtrRibTos_Type.__name__ = "Integer32"
_RtrRibTos_Object = MibTableColumn
rtrRibTos = _RtrRibTos_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1, 1, 4),
    _RtrRibTos_Type()
)
rtrRibTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRibTos.setStatus("current")
_RtrRibNextHopType_Type = InetAddressType
_RtrRibNextHopType_Object = MibTableColumn
rtrRibNextHopType = _RtrRibNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1, 1, 5),
    _RtrRibNextHopType_Type()
)
rtrRibNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRibNextHopType.setStatus("current")


class _RtrRibNextHop_Type(InetAddress):
    """Custom type rtrRibNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtrRibNextHop_Type.__name__ = "InetAddress"
_RtrRibNextHop_Object = MibTableColumn
rtrRibNextHop = _RtrRibNextHop_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1, 1, 6),
    _RtrRibNextHop_Type()
)
rtrRibNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRibNextHop.setStatus("current")


class _RtrRibIfIndex_Type(Integer32):
    """Custom type rtrRibIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtrRibIfIndex_Type.__name__ = "Integer32"
_RtrRibIfIndex_Object = MibTableColumn
rtrRibIfIndex = _RtrRibIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1, 1, 7),
    _RtrRibIfIndex_Type()
)
rtrRibIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRibIfIndex.setStatus("current")
_RtrRibProto_Type = IANAipRouteProtocol
_RtrRibProto_Object = MibTableColumn
rtrRibProto = _RtrRibProto_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1, 1, 8),
    _RtrRibProto_Type()
)
rtrRibProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRibProto.setStatus("current")


class _RtrRibRpmIndex_Type(Integer32):
    """Custom type rtrRibRpmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtrRibRpmIndex_Type.__name__ = "Integer32"
_RtrRibRpmIndex_Object = MibTableColumn
rtrRibRpmIndex = _RtrRibRpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1, 1, 9),
    _RtrRibRpmIndex_Type()
)
rtrRibRpmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtrRibRpmIndex.setStatus("current")


class _RtrRibMetric1_Type(Integer32):
    """Custom type rtrRibMetric1 based on Integer32"""
    defaultValue = -1


_RtrRibMetric1_Type.__name__ = "Integer32"
_RtrRibMetric1_Object = MibTableColumn
rtrRibMetric1 = _RtrRibMetric1_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1, 1, 10),
    _RtrRibMetric1_Type()
)
rtrRibMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrRibMetric1.setStatus("current")
_RtrRibFibRoute_Type = TruthValue
_RtrRibFibRoute_Object = MibTableColumn
rtrRibFibRoute = _RtrRibFibRoute_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 16, 1, 1, 11),
    _RtrRibFibRoute_Type()
)
rtrRibFibRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrRibFibRoute.setStatus("current")
ipIfStatsEntry.registerAugmentions(
    ("RAD-SubRtr-MIB",
     "ipIfStatsXEntry")
)
ipIfStatsXEntry.setIndexNames(*ipIfStatsEntry.getIndexNames())
ipSystemStatsEntry.registerAugmentions(
    ("RAD-SubRtr-MIB",
     "ipSystemStatsXEntry")
)
ipSystemStatsXEntry.setIndexNames(*ipSystemStatsEntry.getIndexNames())

# Managed Objects groups


# Notification objects

rtrFACSViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 0, 1)
)
rtrFACSViolation.setObjects(
      *(("RAD-SubRtr-MIB", "rtrFACSFrameData"),
        ("RAD-SubRtr-MIB", "rtrFACSProtocolType"))
)
if mibBuilder.loadTexts:
    rtrFACSViolation.setStatus(
        "current"
    )

rtrSwDwnLoadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 0, 2)
)
rtrSwDwnLoadTrap.setObjects(
    ("RAD-SubRtr-MIB", "fileName")
)
if mibBuilder.loadTexts:
    rtrSwDwnLoadTrap.setStatus(
        "current"
    )

ipBfdDetectionTimeExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 0, 6)
)
ipBfdDetectionTimeExpired.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-GEN-MIB", "bfdSessXDescription"),
        ("BFD-STD-MIB-R", "bfdSessDstAddr"))
)
if mibBuilder.loadTexts:
    ipBfdDetectionTimeExpired.setStatus(
        "current"
    )

ipBfdNeighborShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 0, 7)
)
ipBfdNeighborShutdown.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-GEN-MIB", "bfdSessXDescription"),
        ("BFD-STD-MIB-R", "bfdSessDstAddr"))
)
if mibBuilder.loadTexts:
    ipBfdNeighborShutdown.setStatus(
        "current"
    )

ipBfdNeighborAddressChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 0, 8)
)
ipBfdNeighborAddressChange.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-GEN-MIB", "bfdSessXDescription"),
        ("BFD-STD-MIB-R", "bfdSessDstAddr"))
)
if mibBuilder.loadTexts:
    ipBfdNeighborAddressChange.setStatus(
        "current"
    )

systemTraceMsgProtoMemAllocErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 11, 0, 1)
)
systemTraceMsgProtoMemAllocErr.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-SubRtr-MIB", "rtrInformationProtMemAllocStatus"),
        ("RAD-SubRtr-MIB", "rtrInformationProtMemAllocInfo"))
)
if mibBuilder.loadTexts:
    systemTraceMsgProtoMemAllocErr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-SubRtr-MIB",
    **{"RtrIfConfigTYPE": RtrIfConfigTYPE,
       "AdminDistance": AdminDistance,
       "RtrSafi": RtrSafi,
       "InfoSourceDest": InfoSourceDest,
       "rtrFACSViolation": rtrFACSViolation,
       "rtrSwDwnLoadTrap": rtrSwDwnLoadTrap,
       "ipBfdDetectionTimeExpired": ipBfdDetectionTimeExpired,
       "ipBfdNeighborShutdown": ipBfdNeighborShutdown,
       "ipBfdNeighborAddressChange": ipBfdNeighborAddressChange,
       "radRouter": radRouter,
       "rtrEvents": rtrEvents,
       "systemTraceMsgProtoMemAllocErr": systemTraceMsgProtoMemAllocErr,
       "rtrInterfaces": rtrInterfaces,
       "rtrConfigIfTable": rtrConfigIfTable,
       "rtrConfigIfEntry": rtrConfigIfEntry,
       "rtrConfigIfIndex": rtrConfigIfIndex,
       "rtrConfigIfType": rtrConfigIfType,
       "rtrConfigIfName": rtrConfigIfName,
       "rtrConfigIfStatus": rtrConfigIfStatus,
       "rtrIfCfgTable": rtrIfCfgTable,
       "rtrIfCfgEntry": rtrIfCfgEntry,
       "rtrIfCfgIndex": rtrIfCfgIndex,
       "rtrIfCfgIpAddress": rtrIfCfgIpAddress,
       "rtrIfCfgRowStatus": rtrIfCfgRowStatus,
       "rtrIfCfgIpMask": rtrIfCfgIpMask,
       "rtrIfCfgIfIndex": rtrIfCfgIfIndex,
       "rtrIfCfgType": rtrIfCfgType,
       "rtrIfCfgVlanId": rtrIfCfgVlanId,
       "rtrIfCfgMtu": rtrIfCfgMtu,
       "rtrIfCfgName": rtrIfCfgName,
       "rtrIfCfgConnectionPointer": rtrIfCfgConnectionPointer,
       "rtrIfCfgVlanTagging": rtrIfCfgVlanTagging,
       "rtrIfCfgVlanPriority": rtrIfCfgVlanPriority,
       "rtrIfCfgParams": rtrIfCfgParams,
       "rtrIfCfgMngAccess": rtrIfCfgMngAccess,
       "rtrIfCfgLlcSnapEncaps": rtrIfCfgLlcSnapEncaps,
       "rtrIfCfgDhcp": rtrIfCfgDhcp,
       "rtrIfCfgIfIpAddressType": rtrIfCfgIfIpAddressType,
       "rtrIfCfgIfIpAddress": rtrIfCfgIfIpAddress,
       "rtrIfCfgICMPUnreachable": rtrIfCfgICMPUnreachable,
       "rtrIfCfgIpv6AutoConfig": rtrIfCfgIpv6AutoConfig,
       "rtrIfCfgDhcpRelay": rtrIfCfgDhcpRelay,
       "rtrIfCfgDhcpv6ClientAdminStatus": rtrIfCfgDhcpv6ClientAdminStatus,
       "rtrIfCfgIpForwarding": rtrIfCfgIpForwarding,
       "rtrStaticRouteTable": rtrStaticRouteTable,
       "rtrStaticRouteEntry": rtrStaticRouteEntry,
       "rtrStaticRouteDestType": rtrStaticRouteDestType,
       "rtrStaticRouteDest": rtrStaticRouteDest,
       "rtrStaticRoutePfxLen": rtrStaticRoutePfxLen,
       "rtrStaticRoutePolicy": rtrStaticRoutePolicy,
       "rtrStaticRouteNextHopType": rtrStaticRouteNextHopType,
       "rtrStaticRouteNextHop": rtrStaticRouteNextHop,
       "rtrStaticRouteRtRIfIndex": rtrStaticRouteRtRIfIndex,
       "rtrStaticRouteType": rtrStaticRouteType,
       "rtrStaticRouteProto": rtrStaticRouteProto,
       "rtrStaticRouteAge": rtrStaticRouteAge,
       "rtrStaticRouteNextHopAS": rtrStaticRouteNextHopAS,
       "rtrStaticRouteMetric1": rtrStaticRouteMetric1,
       "rtrStaticRouteMetric2": rtrStaticRouteMetric2,
       "rtrStaticRouteMetric3": rtrStaticRouteMetric3,
       "rtrStaticRouteMetric4": rtrStaticRouteMetric4,
       "rtrStaticRouteMetric5": rtrStaticRouteMetric5,
       "rtrStaticRouteStatus": rtrStaticRouteStatus,
       "rtrStaticRouteNoInstall": rtrStaticRouteNoInstall,
       "ipIfStatsXTable": ipIfStatsXTable,
       "ipIfStatsXEntry": ipIfStatsXEntry,
       "ipIfStatsXClearStatisticsCmd": ipIfStatsXClearStatisticsCmd,
       "ipSystemStatsXTable": ipSystemStatsXTable,
       "ipSystemStatsXEntry": ipSystemStatsXEntry,
       "ipSystemStatsXClearStatisticsCmd": ipSystemStatsXClearStatisticsCmd,
       "ipSystemStatsXClearAllStatisticsCmd": ipSystemStatsXClearAllStatisticsCmd,
       "ifIpAddressTable": ifIpAddressTable,
       "ifIpAddressEntry": ifIpAddressEntry,
       "ifIpAddressAddrType": ifIpAddressAddrType,
       "ifIpAddressAddr": ifIpAddressAddr,
       "ifIpAddressPrefixLength": ifIpAddressPrefixLength,
       "ifIpAddressIfIndex": ifIpAddressIfIndex,
       "ifIpAddressRowStatus": ifIpAddressRowStatus,
       "ifIpAddressPrefix": ifIpAddressPrefix,
       "ifIpAddressOrigin": ifIpAddressOrigin,
       "rtrIfCfgBfdSessTable": rtrIfCfgBfdSessTable,
       "rtrIfCfgBfdSessEntry": rtrIfCfgBfdSessEntry,
       "rtrIfCfgBfdSessDesiredMinTxInterval": rtrIfCfgBfdSessDesiredMinTxInterval,
       "rtrIfCfgBfdSessReqMinRxInterval": rtrIfCfgBfdSessReqMinRxInterval,
       "rtrIfCfgBfdSessDetectMult": rtrIfCfgBfdSessDetectMult,
       "ipSpec": ipSpec,
       "rtrIpAddrTable": rtrIpAddrTable,
       "rtrIpAddrEntry": rtrIpAddrEntry,
       "rtrIpAdEntAddr": rtrIpAdEntAddr,
       "rtrIpAdEntIfIndex": rtrIpAdEntIfIndex,
       "rtrIpAdEntNetMask": rtrIpAdEntNetMask,
       "rtrIpAdEntForwardIpBroadcast": rtrIpAdEntForwardIpBroadcast,
       "rtrIpAdEntBackupAddr": rtrIpAdEntBackupAddr,
       "rtrIpAdEntStatus": rtrIpAdEntStatus,
       "icmpSpec": icmpSpec,
       "rtrIcmpGenErrMsgEnable": rtrIcmpGenErrMsgEnable,
       "rtrIcmpRdTable": rtrIcmpRdTable,
       "rtrIcmpRdEntry": rtrIcmpRdEntry,
       "rtrIcmpRdIpAddr": rtrIcmpRdIpAddr,
       "rtrIcmpRdIpAdvertAddr": rtrIcmpRdIpAdvertAddr,
       "rtrIcmpRdMaxAdvertInterval": rtrIcmpRdMaxAdvertInterval,
       "rtrIcmpRdMinAdvertInterval": rtrIcmpRdMinAdvertInterval,
       "rtrIcmpRdAdvertLifetime": rtrIcmpRdAdvertLifetime,
       "rtrIcmpRdAdvertise": rtrIcmpRdAdvertise,
       "rtrIcmpRdPreferenceLevel": rtrIcmpRdPreferenceLevel,
       "rtrIcmpRdEntStatus": rtrIcmpRdEntStatus,
       "rip2Spec": rip2Spec,
       "rtrRip2IfConfTable": rtrRip2IfConfTable,
       "rtrRip2IfConfEntry": rtrRip2IfConfEntry,
       "rtrRip2IfConfAddress": rtrRip2IfConfAddress,
       "rtrRip2IfConfVirtualDis": rtrRip2IfConfVirtualDis,
       "rtrRip2IfConfAutoSend": rtrRip2IfConfAutoSend,
       "rtrRip2IfConfRipEnable": rtrRip2IfConfRipEnable,
       "arpSpec": arpSpec,
       "rtrArpDeleteTable": rtrArpDeleteTable,
       "rtrArpInactiveTimeOut": rtrArpInactiveTimeOut,
       "rtrArpProxy": rtrArpProxy,
       "rtrNat": rtrNat,
       "rtrNatIfConfTable": rtrNatIfConfTable,
       "rtrNatIfConfEntry": rtrNatIfConfEntry,
       "rtrNatIfVirtualAddress": rtrNatIfVirtualAddress,
       "rtrNatIfVirtualMask": rtrNatIfVirtualMask,
       "rtrNatIfConfStatus": rtrNatIfConfStatus,
       "rtrNatIfRealAddress": rtrNatIfRealAddress,
       "rtrNatIfRealMask": rtrNatIfRealMask,
       "rtrNatIfType": rtrNatIfType,
       "rtrPatTable": rtrPatTable,
       "rtrPatEntry": rtrPatEntry,
       "rtrPatIdx": rtrPatIdx,
       "rtrPatRealAddress": rtrPatRealAddress,
       "rtrPatVirtualAddress": rtrPatVirtualAddress,
       "rtrPatLowestPort": rtrPatLowestPort,
       "rtrPatHighestPort": rtrPatHighestPort,
       "rtrPatProtocol": rtrPatProtocol,
       "rtrPatStatus": rtrPatStatus,
       "rtrInformationTable": rtrInformationTable,
       "rtrInformationEntry": rtrInformationEntry,
       "rtrInformationId": rtrInformationId,
       "rtrInformationProtMemAllocStatus": rtrInformationProtMemAllocStatus,
       "rtrInformationProtMemAllocInfo": rtrInformationProtMemAllocInfo,
       "rtrFACS": rtrFACS,
       "rtrFACSDefaultAction": rtrFACSDefaultAction,
       "rtrFACSActTable": rtrFACSActTable,
       "rtrFACSActEntry": rtrFACSActEntry,
       "rtrFACSActType": rtrFACSActType,
       "rtrFACSActIfIndex": rtrFACSActIfIndex,
       "rtrFACSAction": rtrFACSAction,
       "rtrFACSActiveDB": rtrFACSActiveDB,
       "rtrFACSTable": rtrFACSTable,
       "rtrFACSEntry": rtrFACSEntry,
       "rtrFACSIfIndex": rtrFACSIfIndex,
       "rtrFACSProtocolType": rtrFACSProtocolType,
       "rtrFACSType": rtrFACSType,
       "rtrFACSIndex": rtrFACSIndex,
       "rtrFACSSrcAdd": rtrFACSSrcAdd,
       "rtrFACSSrcAddMask": rtrFACSSrcAddMask,
       "rtrFACSDesAdd": rtrFACSDesAdd,
       "rtrFACSDesAddMask": rtrFACSDesAddMask,
       "rtrFACSOperation": rtrFACSOperation,
       "rtrFACSNetFiltering": rtrFACSNetFiltering,
       "rtrFACSSocketNum": rtrFACSSocketNum,
       "rtrFACSMask1Id": rtrFACSMask1Id,
       "rtrFACSMask2Id": rtrFACSMask2Id,
       "rtrFACSStatus": rtrFACSStatus,
       "rtrFACSFrameData": rtrFACSFrameData,
       "rtrRtmEntityTable": rtrRtmEntityTable,
       "rtrRtmEntityEntry": rtrRtmEntityEntry,
       "rtrRtmEntityAfiType": rtrRtmEntityAfiType,
       "rtrRtmEntitySafi": rtrRtmEntitySafi,
       "rtrRtmEntityDsStatDf": rtrRtmEntityDsStatDf,
       "rtrRtmEntityDsOspfInt": rtrRtmEntityDsOspfInt,
       "rtrRtmEntityDsOspfExt": rtrRtmEntityDsOspfExt,
       "rtrRtmEntityDsIntBgp": rtrRtmEntityDsIntBgp,
       "rtrRtmEntityDsExtBgp": rtrRtmEntityDsExtBgp,
       "rtrBridgePortConfigTable": rtrBridgePortConfigTable,
       "rtrBridgePortConfigEntry": rtrBridgePortConfigEntry,
       "rtrBridgePortCIndex": rtrBridgePortCIndex,
       "rtrBridgePortCIf": rtrBridgePortCIf,
       "rtrBridgePortCStatus": rtrBridgePortCStatus,
       "radRouterConfig": radRouterConfig,
       "rtrConfigTable": rtrConfigTable,
       "rtrConfigEntry": rtrConfigEntry,
       "rtrConfigIndex": rtrConfigIndex,
       "rtrConfigDefaultGateway": rtrConfigDefaultGateway,
       "rtrConfigArpAgingTime": rtrConfigArpAgingTime,
       "rtrConfigClassifierTosMask": rtrConfigClassifierTosMask,
       "rtrConfigRIPMode": rtrConfigRIPMode,
       "rtrConfigRoutingName": rtrConfigRoutingName,
       "rtrConfigRowStatus": rtrConfigRowStatus,
       "rtrConfigDhcpClientOpHostNameType": rtrConfigDhcpClientOpHostNameType,
       "rtrConfigDhcpClientOpHostName": rtrConfigDhcpClientOpHostName,
       "rtrConfigDhcpClientOpVendorClassIdType": rtrConfigDhcpClientOpVendorClassIdType,
       "rtrConfigDhcpClientOpVendorClassId": rtrConfigDhcpClientOpVendorClassId,
       "rtrConfigDhcpClientOpControl": rtrConfigDhcpClientOpControl,
       "rtrConfigClearIpv4ArpCmd": rtrConfigClearIpv4ArpCmd,
       "rtrConfigClearIpv6NeighborCmd": rtrConfigClearIpv6NeighborCmd,
       "rtrConfigRouterDscp": rtrConfigRouterDscp,
       "rtrSystemAddress": rtrSystemAddress,
       "rtrFwdTable": rtrFwdTable,
       "rtrFwdEntry": rtrFwdEntry,
       "rtrFwdIdx": rtrFwdIdx,
       "rtrFwdIpAddress": rtrFwdIpAddress,
       "rtrFwdIpMask": rtrFwdIpMask,
       "rtrFwdRuleIdx": rtrFwdRuleIdx,
       "rtrFwdRowStatus": rtrFwdRowStatus,
       "rtrFwdNextHop": rtrFwdNextHop,
       "rtrFwdIfIndex": rtrFwdIfIndex,
       "rtrFwdType": rtrFwdType,
       "rtrFwdProto": rtrFwdProto,
       "rtrFwdEthQueue": rtrFwdEthQueue,
       "rtrFwdMetric1": rtrFwdMetric1,
       "rtrPbrTable": rtrPbrTable,
       "rtrPbrEntry": rtrPbrEntry,
       "rtrPbrIdx": rtrPbrIdx,
       "rtrPbrInterface": rtrPbrInterface,
       "rtrPbrRuleIdx": rtrPbrRuleIdx,
       "rtrPbrRowStatus": rtrPbrRowStatus,
       "rtrPbrMatchAllFrames": rtrPbrMatchAllFrames,
       "rtrPbrSourceIpAddress": rtrPbrSourceIpAddress,
       "rtrPbrSourceIpMask": rtrPbrSourceIpMask,
       "rtrPbrDestIpAddress": rtrPbrDestIpAddress,
       "rtrPbrDestIpMask": rtrPbrDestIpMask,
       "rtrPbrIpProtocol": rtrPbrIpProtocol,
       "rtrPbrMinFrameLength": rtrPbrMinFrameLength,
       "rtrPbrMaxFrameLength": rtrPbrMaxFrameLength,
       "rtrPbrDiscardFrame": rtrPbrDiscardFrame,
       "rtrPbrForwardingInterface": rtrPbrForwardingInterface,
       "rtrPbrNextHop": rtrPbrNextHop,
       "rtrSourceAddressTable": rtrSourceAddressTable,
       "rtrSourceAddressEntry": rtrSourceAddressEntry,
       "rtrSourceAddressApp": rtrSourceAddressApp,
       "rtrSourceAddressType": rtrSourceAddressType,
       "rtrSourceAddress": rtrSourceAddress,
       "rtrSourceAddressIfIndex": rtrSourceAddressIfIndex,
       "rtrSourceAddressRowStatus": rtrSourceAddressRowStatus,
       "rtrRedistTable": rtrRedistTable,
       "rtrRedistEntry": rtrRedistEntry,
       "rtrRedistAfiType": rtrRedistAfiType,
       "rtrRedistSafi": rtrRedistSafi,
       "rtrRedistInfoSrc": rtrRedistInfoSrc,
       "rtrRedistInfoDest": rtrRedistInfoDest,
       "rtrRedistRowStatus": rtrRedistRowStatus,
       "rtrPolicy": rtrPolicy,
       "rtrPolicyMainTable": rtrPolicyMainTable,
       "rtrPolicyMainEntry": rtrPolicyMainEntry,
       "rtrPolicyName": rtrPolicyName,
       "rtrPolicyNumberOfRules": rtrPolicyNumberOfRules,
       "rtrPolicyLastSeqeunceNumber": rtrPolicyLastSeqeunceNumber,
       "rtrPolicyResequenceCmd": rtrPolicyResequenceCmd,
       "rtrPolicyType": rtrPolicyType,
       "rtrPolicyRowStatus": rtrPolicyRowStatus,
       "rtrPolicyRuleTable": rtrPolicyRuleTable,
       "rtrPolicyRuleEntry": rtrPolicyRuleEntry,
       "rtrPolicyRuleIdx": rtrPolicyRuleIdx,
       "rtrPolicyRuleName": rtrPolicyRuleName,
       "rtrPolicyRuleSequenceNumber": rtrPolicyRuleSequenceNumber,
       "rtrPolicyRuleType": rtrPolicyRuleType,
       "rtrPolicyRulePointer": rtrPolicyRulePointer,
       "rtrPolicyRuleRowStatus": rtrPolicyRuleRowStatus,
       "rtrPolicyInvRuleTable": rtrPolicyInvRuleTable,
       "rtrPolicyInvRuleEntry": rtrPolicyInvRuleEntry,
       "rtrPolicyInvRuleIdx": rtrPolicyInvRuleIdx,
       "rtrPolicyInvRuleType": rtrPolicyInvRuleType,
       "rtrPolicyInvRulePointer": rtrPolicyInvRulePointer,
       "rtrPolicyRuleRemarkTable": rtrPolicyRuleRemarkTable,
       "rtrPolicyRuleRemarkEntry": rtrPolicyRuleRemarkEntry,
       "rtrPolicyRuleRemark": rtrPolicyRuleRemark,
       "rtrDhcp": rtrDhcp,
       "rtrDhcpRelay": rtrDhcpRelay,
       "dhcpRelayServerTable": dhcpRelayServerTable,
       "dhcpRelayServerEntry": dhcpRelayServerEntry,
       "dhcpRelayServerRtrIfIndex": dhcpRelayServerRtrIfIndex,
       "dhcpRelayServerAddrType": dhcpRelayServerAddrType,
       "dhcpRelayServerAddr": dhcpRelayServerAddr,
       "dhcpRelayServerRowStatus": dhcpRelayServerRowStatus,
       "rtrRouterEntity": rtrRouterEntity,
       "rtrRibTable": rtrRibTable,
       "rtrRibEntry": rtrRibEntry,
       "rtrRibDestType": rtrRibDestType,
       "rtrRibDest": rtrRibDest,
       "rtrRibDestLen": rtrRibDestLen,
       "rtrRibTos": rtrRibTos,
       "rtrRibNextHopType": rtrRibNextHopType,
       "rtrRibNextHop": rtrRibNextHop,
       "rtrRibIfIndex": rtrRibIfIndex,
       "rtrRibProto": rtrRibProto,
       "rtrRibRpmIndex": rtrRibRpmIndex,
       "rtrRibMetric1": rtrRibMetric1,
       "rtrRibFibRoute": rtrRibFibRoute}
)
