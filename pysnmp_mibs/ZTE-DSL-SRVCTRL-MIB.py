# SNMP MIB module (ZTE-DSL-SRVCTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-SRVCTRL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:21 2025
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

(adslLineAlarmConfProfileEntry,
 adslLineConfProfileEntry,
 adslLineConfProfileName) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "adslLineAlarmConfProfileEntry",
    "adslLineConfProfileEntry",
    "adslLineConfProfileName")

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

zxDslSrvctrlMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RateLimitProtocolType(TextualConvention, Integer32):
    status = "current"
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
              9,
              10,
              11,
              20)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 1),
          ("broadcast", 2),
          ("unknownMulticast", 3),
          ("dlf", 4),
          ("dhcp", 5),
          ("igmp", 6),
          ("icmp", 7),
          ("dhcpv6", 8),
          ("icmpv6", 9),
          ("mld", 10),
          ("arp", 11),
          ("all", 20))
    )



class RateLimitScale(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("nni", 2),
          ("uni", 3),
          ("globalVlan", 4),
          ("globalPvc", 5),
          ("vlan", 10),
          ("port", 11),
          ("pvc", 12))
    )



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxDsl_ObjectIdentity = ObjectIdentity
zxDsl = _ZxDsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004)
)
_ZxDslSrvctrlObjects_ObjectIdentity = ObjectIdentity
zxDslSrvctrlObjects = _ZxDslSrvctrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1)
)
_ZxDslMacLockTable_Object = MibTable
zxDslMacLockTable = _ZxDslMacLockTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 1)
)
if mibBuilder.loadTexts:
    zxDslMacLockTable.setStatus("current")
_ZxDslMacLockEntry_Object = MibTableRow
zxDslMacLockEntry = _ZxDslMacLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 1, 1)
)
zxDslMacLockEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslMacLockMacAddr"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslMacLockVid"),
)
if mibBuilder.loadTexts:
    zxDslMacLockEntry.setStatus("current")
_ZxDslMacLockMacAddr_Type = MacAddress
_ZxDslMacLockMacAddr_Object = MibTableColumn
zxDslMacLockMacAddr = _ZxDslMacLockMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 1, 1, 1),
    _ZxDslMacLockMacAddr_Type()
)
zxDslMacLockMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslMacLockMacAddr.setStatus("current")


class _ZxDslMacLockVid_Type(Integer32):
    """Custom type zxDslMacLockVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxDslMacLockVid_Type.__name__ = "Integer32"
_ZxDslMacLockVid_Object = MibTableColumn
zxDslMacLockVid = _ZxDslMacLockVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 1, 1, 2),
    _ZxDslMacLockVid_Type()
)
zxDslMacLockVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslMacLockVid.setStatus("current")


class _ZxDslMacLockRowStatus_Type(RowStatus):
    """Custom type zxDslMacLockRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
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
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_ZxDslMacLockRowStatus_Type.__name__ = "RowStatus"
_ZxDslMacLockRowStatus_Object = MibTableColumn
zxDslMacLockRowStatus = _ZxDslMacLockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 1, 1, 3),
    _ZxDslMacLockRowStatus_Type()
)
zxDslMacLockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslMacLockRowStatus.setStatus("current")
_ZxDslStaticMacTable_Object = MibTable
zxDslStaticMacTable = _ZxDslStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 2)
)
if mibBuilder.loadTexts:
    zxDslStaticMacTable.setStatus("current")
_ZxDslStaticMacEntry_Object = MibTableRow
zxDslStaticMacEntry = _ZxDslStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 2, 1)
)
zxDslStaticMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslStaticMacAddr"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslStaticMacVid"),
)
if mibBuilder.loadTexts:
    zxDslStaticMacEntry.setStatus("current")
_ZxDslStaticMacAddr_Type = MacAddress
_ZxDslStaticMacAddr_Object = MibTableColumn
zxDslStaticMacAddr = _ZxDslStaticMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 2, 1, 1),
    _ZxDslStaticMacAddr_Type()
)
zxDslStaticMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslStaticMacAddr.setStatus("current")
_ZxDslStaticMacVid_Type = Integer32
_ZxDslStaticMacVid_Object = MibTableColumn
zxDslStaticMacVid = _ZxDslStaticMacVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 2, 1, 2),
    _ZxDslStaticMacVid_Type()
)
zxDslStaticMacVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslStaticMacVid.setStatus("current")
_ZxDslStaticMacPvcId_Type = Integer32
_ZxDslStaticMacPvcId_Object = MibTableColumn
zxDslStaticMacPvcId = _ZxDslStaticMacPvcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 2, 1, 3),
    _ZxDslStaticMacPvcId_Type()
)
zxDslStaticMacPvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslStaticMacPvcId.setStatus("current")


class _ZxDslStaticMacTagflag_Type(Integer32):
    """Custom type zxDslStaticMacTagflag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("untag", 2),
          ("all", 3))
    )


_ZxDslStaticMacTagflag_Type.__name__ = "Integer32"
_ZxDslStaticMacTagflag_Object = MibTableColumn
zxDslStaticMacTagflag = _ZxDslStaticMacTagflag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 2, 1, 4),
    _ZxDslStaticMacTagflag_Type()
)
zxDslStaticMacTagflag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslStaticMacTagflag.setStatus("current")


class _ZxDslStaticMacRowStatus_Type(RowStatus):
    """Custom type zxDslStaticMacRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
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
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_ZxDslStaticMacRowStatus_Type.__name__ = "RowStatus"
_ZxDslStaticMacRowStatus_Object = MibTableColumn
zxDslStaticMacRowStatus = _ZxDslStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 2, 1, 5),
    _ZxDslStaticMacRowStatus_Type()
)
zxDslStaticMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslStaticMacRowStatus.setStatus("current")
_ZxDslIpLockTable_Object = MibTable
zxDslIpLockTable = _ZxDslIpLockTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 3)
)
if mibBuilder.loadTexts:
    zxDslIpLockTable.setStatus("current")
_ZxDslIpLockEntry_Object = MibTableRow
zxDslIpLockEntry = _ZxDslIpLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 3, 1)
)
zxDslIpLockEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslIpLockIpAddr"),
)
if mibBuilder.loadTexts:
    zxDslIpLockEntry.setStatus("current")
_ZxDslIpLockIpAddr_Type = IpAddress
_ZxDslIpLockIpAddr_Object = MibTableColumn
zxDslIpLockIpAddr = _ZxDslIpLockIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 3, 1, 1),
    _ZxDslIpLockIpAddr_Type()
)
zxDslIpLockIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslIpLockIpAddr.setStatus("current")


class _ZxDslIpLockRowStatus_Type(RowStatus):
    """Custom type zxDslIpLockRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
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
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_ZxDslIpLockRowStatus_Type.__name__ = "RowStatus"
_ZxDslIpLockRowStatus_Object = MibTableColumn
zxDslIpLockRowStatus = _ZxDslIpLockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 3, 1, 2),
    _ZxDslIpLockRowStatus_Type()
)
zxDslIpLockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslIpLockRowStatus.setStatus("current")
_ZxDslExtIfTable_Object = MibTable
zxDslExtIfTable = _ZxDslExtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4)
)
if mibBuilder.loadTexts:
    zxDslExtIfTable.setStatus("current")
_ZxDslExtIfEntry_Object = MibTableRow
zxDslExtIfEntry = _ZxDslExtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1)
)
zxDslExtIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxDslExtIfEntry.setStatus("current")


class _ZxDslExtIfFlowCtrlSet_Type(Integer32):
    """Custom type zxDslExtIfFlowCtrlSet based on Integer32"""
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
        *(("autoFlowControlEnable", 1),
          ("forceFlowControlEnable", 2),
          ("autoFlowControlDisable", 3),
          ("forceFlowControlDisable", 4))
    )


_ZxDslExtIfFlowCtrlSet_Type.__name__ = "Integer32"
_ZxDslExtIfFlowCtrlSet_Object = MibTableColumn
zxDslExtIfFlowCtrlSet = _ZxDslExtIfFlowCtrlSet_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 1),
    _ZxDslExtIfFlowCtrlSet_Type()
)
zxDslExtIfFlowCtrlSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfFlowCtrlSet.setStatus("current")


class _ZxDslExtIfFlowCtrlGet_Type(Integer32):
    """Custom type zxDslExtIfFlowCtrlGet based on Integer32"""
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
        *(("autoFlowControlEnable", 1),
          ("forceFlowControlEnable", 2),
          ("autoFlowControlDisable", 3),
          ("forceFlowControlDisable", 4))
    )


_ZxDslExtIfFlowCtrlGet_Type.__name__ = "Integer32"
_ZxDslExtIfFlowCtrlGet_Object = MibTableColumn
zxDslExtIfFlowCtrlGet = _ZxDslExtIfFlowCtrlGet_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 2),
    _ZxDslExtIfFlowCtrlGet_Type()
)
zxDslExtIfFlowCtrlGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslExtIfFlowCtrlGet.setStatus("current")


class _ZxDslExtIfSpeedSet_Type(Integer32):
    """Custom type zxDslExtIfSpeedSet based on Integer32"""
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
        *(("autoSpeed", 1),
          ("speed10M", 2),
          ("speed100M", 3),
          ("speed1000M", 4))
    )


_ZxDslExtIfSpeedSet_Type.__name__ = "Integer32"
_ZxDslExtIfSpeedSet_Object = MibTableColumn
zxDslExtIfSpeedSet = _ZxDslExtIfSpeedSet_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 3),
    _ZxDslExtIfSpeedSet_Type()
)
zxDslExtIfSpeedSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfSpeedSet.setStatus("current")


class _ZxDslExtIfSpeedGet_Type(Integer32):
    """Custom type zxDslExtIfSpeedGet based on Integer32"""
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
        *(("autoSpeed", 1),
          ("speed10M", 2),
          ("speed100M", 3),
          ("speed1000M", 4))
    )


_ZxDslExtIfSpeedGet_Type.__name__ = "Integer32"
_ZxDslExtIfSpeedGet_Object = MibTableColumn
zxDslExtIfSpeedGet = _ZxDslExtIfSpeedGet_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 4),
    _ZxDslExtIfSpeedGet_Type()
)
zxDslExtIfSpeedGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslExtIfSpeedGet.setStatus("current")


class _ZxDslExtIfDuplexSet_Type(Integer32):
    """Custom type zxDslExtIfDuplexSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDuplex", 1),
          ("half", 2),
          ("full", 3))
    )


_ZxDslExtIfDuplexSet_Type.__name__ = "Integer32"
_ZxDslExtIfDuplexSet_Object = MibTableColumn
zxDslExtIfDuplexSet = _ZxDslExtIfDuplexSet_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 5),
    _ZxDslExtIfDuplexSet_Type()
)
zxDslExtIfDuplexSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfDuplexSet.setStatus("current")


class _ZxDslExtIfDuplexGet_Type(Integer32):
    """Custom type zxDslExtIfDuplexGet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDuplex", 1),
          ("half", 2),
          ("full", 3))
    )


_ZxDslExtIfDuplexGet_Type.__name__ = "Integer32"
_ZxDslExtIfDuplexGet_Object = MibTableColumn
zxDslExtIfDuplexGet = _ZxDslExtIfDuplexGet_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 6),
    _ZxDslExtIfDuplexGet_Type()
)
zxDslExtIfDuplexGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslExtIfDuplexGet.setStatus("current")
_ZxDslExtIfMaxMacLearn_Type = Integer32
_ZxDslExtIfMaxMacLearn_Object = MibTableColumn
zxDslExtIfMaxMacLearn = _ZxDslExtIfMaxMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 7),
    _ZxDslExtIfMaxMacLearn_Type()
)
zxDslExtIfMaxMacLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfMaxMacLearn.setStatus("current")
_ZxDslExtIfBroadcastRatelimit_Type = Unsigned32
_ZxDslExtIfBroadcastRatelimit_Object = MibTableColumn
zxDslExtIfBroadcastRatelimit = _ZxDslExtIfBroadcastRatelimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 8),
    _ZxDslExtIfBroadcastRatelimit_Type()
)
zxDslExtIfBroadcastRatelimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfBroadcastRatelimit.setStatus("current")
_ZxDslExtIfMulticastRatelimit_Type = Unsigned32
_ZxDslExtIfMulticastRatelimit_Object = MibTableColumn
zxDslExtIfMulticastRatelimit = _ZxDslExtIfMulticastRatelimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 9),
    _ZxDslExtIfMulticastRatelimit_Type()
)
zxDslExtIfMulticastRatelimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfMulticastRatelimit.setStatus("current")
_ZxDslExtIfDlfRatelimit_Type = Unsigned32
_ZxDslExtIfDlfRatelimit_Object = MibTableColumn
zxDslExtIfDlfRatelimit = _ZxDslExtIfDlfRatelimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 10),
    _ZxDslExtIfDlfRatelimit_Type()
)
zxDslExtIfDlfRatelimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfDlfRatelimit.setStatus("current")
_ZxDslExtIfLinkErrors_Type = Unsigned32
_ZxDslExtIfLinkErrors_Object = MibTableColumn
zxDslExtIfLinkErrors = _ZxDslExtIfLinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 11),
    _ZxDslExtIfLinkErrors_Type()
)
zxDslExtIfLinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslExtIfLinkErrors.setStatus("current")


class _ZxDslExtIfInterTag_Type(Unsigned32):
    """Custom type zxDslExtIfInterTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ZxDslExtIfInterTag_Type.__name__ = "Unsigned32"
_ZxDslExtIfInterTag_Object = MibTableColumn
zxDslExtIfInterTag = _ZxDslExtIfInterTag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 12),
    _ZxDslExtIfInterTag_Type()
)
zxDslExtIfInterTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfInterTag.setStatus("current")


class _ZxDslExtIfBoardcastEnable_Type(Integer32):
    """Custom type zxDslExtIfBoardcastEnable based on Integer32"""
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


_ZxDslExtIfBoardcastEnable_Type.__name__ = "Integer32"
_ZxDslExtIfBoardcastEnable_Object = MibTableColumn
zxDslExtIfBoardcastEnable = _ZxDslExtIfBoardcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 13),
    _ZxDslExtIfBoardcastEnable_Type()
)
zxDslExtIfBoardcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfBoardcastEnable.setStatus("current")


class _ZxDslExtIfMulticastEnable_Type(Integer32):
    """Custom type zxDslExtIfMulticastEnable based on Integer32"""
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


_ZxDslExtIfMulticastEnable_Type.__name__ = "Integer32"
_ZxDslExtIfMulticastEnable_Object = MibTableColumn
zxDslExtIfMulticastEnable = _ZxDslExtIfMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 14),
    _ZxDslExtIfMulticastEnable_Type()
)
zxDslExtIfMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfMulticastEnable.setStatus("current")


class _ZxDslExtIfDlfEnable_Type(Integer32):
    """Custom type zxDslExtIfDlfEnable based on Integer32"""
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


_ZxDslExtIfDlfEnable_Type.__name__ = "Integer32"
_ZxDslExtIfDlfEnable_Object = MibTableColumn
zxDslExtIfDlfEnable = _ZxDslExtIfDlfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 15),
    _ZxDslExtIfDlfEnable_Type()
)
zxDslExtIfDlfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfDlfEnable.setStatus("current")
_ZxDslExtIfDhcpRatelimit_Type = Unsigned32
_ZxDslExtIfDhcpRatelimit_Object = MibTableColumn
zxDslExtIfDhcpRatelimit = _ZxDslExtIfDhcpRatelimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 16),
    _ZxDslExtIfDhcpRatelimit_Type()
)
zxDslExtIfDhcpRatelimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfDhcpRatelimit.setStatus("current")
if mibBuilder.loadTexts:
    zxDslExtIfDhcpRatelimit.setUnits("pps")


class _ZxDslExtIfUserInfoUserName_Type(DisplayString):
    """Custom type zxDslExtIfUserInfoUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxDslExtIfUserInfoUserName_Type.__name__ = "DisplayString"
_ZxDslExtIfUserInfoUserName_Object = MibTableColumn
zxDslExtIfUserInfoUserName = _ZxDslExtIfUserInfoUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 17),
    _ZxDslExtIfUserInfoUserName_Type()
)
zxDslExtIfUserInfoUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfUserInfoUserName.setStatus("current")


class _ZxDslExtIfUserInfoUserAddress_Type(DisplayString):
    """Custom type zxDslExtIfUserInfoUserAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxDslExtIfUserInfoUserAddress_Type.__name__ = "DisplayString"
_ZxDslExtIfUserInfoUserAddress_Object = MibTableColumn
zxDslExtIfUserInfoUserAddress = _ZxDslExtIfUserInfoUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 18),
    _ZxDslExtIfUserInfoUserAddress_Type()
)
zxDslExtIfUserInfoUserAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfUserInfoUserAddress.setStatus("current")


class _ZxDslExtIfUserInfoUserServiceConfigured_Type(DisplayString):
    """Custom type zxDslExtIfUserInfoUserServiceConfigured based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxDslExtIfUserInfoUserServiceConfigured_Type.__name__ = "DisplayString"
_ZxDslExtIfUserInfoUserServiceConfigured_Object = MibTableColumn
zxDslExtIfUserInfoUserServiceConfigured = _ZxDslExtIfUserInfoUserServiceConfigured_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 19),
    _ZxDslExtIfUserInfoUserServiceConfigured_Type()
)
zxDslExtIfUserInfoUserServiceConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfUserInfoUserServiceConfigured.setStatus("current")


class _ZxDslExtIfUserInfoUserOtherNode_Type(DisplayString):
    """Custom type zxDslExtIfUserInfoUserOtherNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZxDslExtIfUserInfoUserOtherNode_Type.__name__ = "DisplayString"
_ZxDslExtIfUserInfoUserOtherNode_Object = MibTableColumn
zxDslExtIfUserInfoUserOtherNode = _ZxDslExtIfUserInfoUserOtherNode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 20),
    _ZxDslExtIfUserInfoUserOtherNode_Type()
)
zxDslExtIfUserInfoUserOtherNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfUserInfoUserOtherNode.setStatus("current")


class _ZxDslExtIfPoeStatus_Type(Integer32):
    """Custom type zxDslExtIfPoeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ZxDslExtIfPoeStatus_Type.__name__ = "Integer32"
_ZxDslExtIfPoeStatus_Object = MibTableColumn
zxDslExtIfPoeStatus = _ZxDslExtIfPoeStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 21),
    _ZxDslExtIfPoeStatus_Type()
)
zxDslExtIfPoeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslExtIfPoeStatus.setStatus("current")


class _ZxDslExtIfPoeEnable_Type(Integer32):
    """Custom type zxDslExtIfPoeEnable based on Integer32"""
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


_ZxDslExtIfPoeEnable_Type.__name__ = "Integer32"
_ZxDslExtIfPoeEnable_Object = MibTableColumn
zxDslExtIfPoeEnable = _ZxDslExtIfPoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 22),
    _ZxDslExtIfPoeEnable_Type()
)
zxDslExtIfPoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfPoeEnable.setStatus("current")


class _ZxDslExtIfDhcpv6RateLimit_Type(Unsigned32):
    """Custom type zxDslExtIfDhcpv6RateLimit based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ZxDslExtIfDhcpv6RateLimit_Type.__name__ = "Unsigned32"
_ZxDslExtIfDhcpv6RateLimit_Object = MibTableColumn
zxDslExtIfDhcpv6RateLimit = _ZxDslExtIfDhcpv6RateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 23),
    _ZxDslExtIfDhcpv6RateLimit_Type()
)
zxDslExtIfDhcpv6RateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfDhcpv6RateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxDslExtIfDhcpv6RateLimit.setUnits("pps")


class _ZxDslExtIfIcmpv6RateLimit_Type(Unsigned32):
    """Custom type zxDslExtIfIcmpv6RateLimit based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ZxDslExtIfIcmpv6RateLimit_Type.__name__ = "Unsigned32"
_ZxDslExtIfIcmpv6RateLimit_Object = MibScalar
zxDslExtIfIcmpv6RateLimit = _ZxDslExtIfIcmpv6RateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 4, 1, 24),
    _ZxDslExtIfIcmpv6RateLimit_Type()
)
zxDslExtIfIcmpv6RateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslExtIfIcmpv6RateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxDslExtIfIcmpv6RateLimit.setUnits("pps")
_ZxDslMacFilterTable_Object = MibTable
zxDslMacFilterTable = _ZxDslMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 5)
)
if mibBuilder.loadTexts:
    zxDslMacFilterTable.setStatus("current")
_ZxDslMacFilterEntry_Object = MibTableRow
zxDslMacFilterEntry = _ZxDslMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 5, 1)
)
zxDslMacFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslMacFilterMacAddr"),
)
if mibBuilder.loadTexts:
    zxDslMacFilterEntry.setStatus("current")
_ZxDslMacFilterMacAddr_Type = MacAddress
_ZxDslMacFilterMacAddr_Object = MibTableColumn
zxDslMacFilterMacAddr = _ZxDslMacFilterMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 5, 1, 1),
    _ZxDslMacFilterMacAddr_Type()
)
zxDslMacFilterMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslMacFilterMacAddr.setStatus("current")


class _ZxDslMacFilterRowStatus_Type(RowStatus):
    """Custom type zxDslMacFilterRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
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
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_ZxDslMacFilterRowStatus_Type.__name__ = "RowStatus"
_ZxDslMacFilterRowStatus_Object = MibTableColumn
zxDslMacFilterRowStatus = _ZxDslMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 5, 1, 2),
    _ZxDslMacFilterRowStatus_Type()
)
zxDslMacFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslMacFilterRowStatus.setStatus("current")
_ZxDslMacCtrlObjects_ObjectIdentity = ObjectIdentity
zxDslMacCtrlObjects = _ZxDslMacCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9)
)
_ZxDslMacCtrlGlobalObjects_ObjectIdentity = ObjectIdentity
zxDslMacCtrlGlobalObjects = _ZxDslMacCtrlGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 1)
)


class _ZxDslMacLearnType_Type(Integer32):
    """Custom type zxDslMacLearnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chip", 1),
          ("dslamSoftware", 2))
    )


_ZxDslMacLearnType_Type.__name__ = "Integer32"
_ZxDslMacLearnType_Object = MibScalar
zxDslMacLearnType = _ZxDslMacLearnType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 1, 1),
    _ZxDslMacLearnType_Type()
)
zxDslMacLearnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslMacLearnType.setStatus("current")


class _ZxDslPredefMacForwardEnable_Type(Integer32):
    """Custom type zxDslPredefMacForwardEnable based on Integer32"""
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


_ZxDslPredefMacForwardEnable_Type.__name__ = "Integer32"
_ZxDslPredefMacForwardEnable_Object = MibScalar
zxDslPredefMacForwardEnable = _ZxDslPredefMacForwardEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 1, 2),
    _ZxDslPredefMacForwardEnable_Type()
)
zxDslPredefMacForwardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslPredefMacForwardEnable.setStatus("current")
_ZxDslMacClear_ObjectIdentity = ObjectIdentity
zxDslMacClear = _ZxDslMacClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 2)
)


class _ZxDslMacClearType_Type(Integer32):
    """Custom type zxDslMacClearType based on Integer32"""
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
        *(("all", 1),
          ("mac", 2),
          ("port", 3),
          ("vlan", 4),
          ("vlanOfMac", 5))
    )


_ZxDslMacClearType_Type.__name__ = "Integer32"
_ZxDslMacClearType_Object = MibScalar
zxDslMacClearType = _ZxDslMacClearType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 2, 1),
    _ZxDslMacClearType_Type()
)
zxDslMacClearType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslMacClearType.setStatus("current")


class _ZxDslMacClearValue_Type(DisplayString):
    """Custom type zxDslMacClearValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxDslMacClearValue_Type.__name__ = "DisplayString"
_ZxDslMacClearValue_Object = MibScalar
zxDslMacClearValue = _ZxDslMacClearValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 2, 2),
    _ZxDslMacClearValue_Type()
)
zxDslMacClearValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslMacClearValue.setStatus("current")
_ZxDslMacAddressObject_ObjectIdentity = ObjectIdentity
zxDslMacAddressObject = _ZxDslMacAddressObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 3)
)
_ZxDslMacAddressTable_Object = MibTable
zxDslMacAddressTable = _ZxDslMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    zxDslMacAddressTable.setStatus("current")
_ZxDslMacAddressEntry_Object = MibTableRow
zxDslMacAddressEntry = _ZxDslMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 3, 1, 1)
)
zxDslMacAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxDslMacAddressEntry.setStatus("current")


class _ZxDslMacAddressList_Type(OctetString):
    """Custom type zxDslMacAddressList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ZxDslMacAddressList_Type.__name__ = "OctetString"
_ZxDslMacAddressList_Object = MibTableColumn
zxDslMacAddressList = _ZxDslMacAddressList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 3, 1, 1, 1),
    _ZxDslMacAddressList_Type()
)
zxDslMacAddressList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslMacAddressList.setStatus("current")
_ZxDslMacAddressExtTable_Object = MibTable
zxDslMacAddressExtTable = _ZxDslMacAddressExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    zxDslMacAddressExtTable.setStatus("current")
_ZxDslMacAddressExtEntry_Object = MibTableRow
zxDslMacAddressExtEntry = _ZxDslMacAddressExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 3, 2, 1)
)
zxDslMacAddressExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslMacAddressExtSeqId"),
)
if mibBuilder.loadTexts:
    zxDslMacAddressExtEntry.setStatus("current")
_ZxDslMacAddressExtSeqId_Type = Unsigned32
_ZxDslMacAddressExtSeqId_Object = MibTableColumn
zxDslMacAddressExtSeqId = _ZxDslMacAddressExtSeqId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 3, 2, 1, 1),
    _ZxDslMacAddressExtSeqId_Type()
)
zxDslMacAddressExtSeqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslMacAddressExtSeqId.setStatus("current")


class _ZxDslMacAddressExtList_Type(OctetString):
    """Custom type zxDslMacAddressExtList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ZxDslMacAddressExtList_Type.__name__ = "OctetString"
_ZxDslMacAddressExtList_Object = MibTableColumn
zxDslMacAddressExtList = _ZxDslMacAddressExtList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 3, 2, 1, 2),
    _ZxDslMacAddressExtList_Type()
)
zxDslMacAddressExtList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslMacAddressExtList.setStatus("current")
_ZxDslVmacObjects_ObjectIdentity = ObjectIdentity
zxDslVmacObjects = _ZxDslVmacObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4)
)
_ZxDslVmacGlobalObjects_ObjectIdentity = ObjectIdentity
zxDslVmacGlobalObjects = _ZxDslVmacGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 1)
)


class _ZxDslVmacDeviceId_Type(Integer32):
    """Custom type zxDslVmacDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_ZxDslVmacDeviceId_Type.__name__ = "Integer32"
_ZxDslVmacDeviceId_Object = MibScalar
zxDslVmacDeviceId = _ZxDslVmacDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 1, 1),
    _ZxDslVmacDeviceId_Type()
)
zxDslVmacDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslVmacDeviceId.setStatus("current")
_ZxDslVmacSysMac_Type = MacAddress
_ZxDslVmacSysMac_Object = MibScalar
zxDslVmacSysMac = _ZxDslVmacSysMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 1, 2),
    _ZxDslVmacSysMac_Type()
)
zxDslVmacSysMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslVmacSysMac.setStatus("current")
_ZxDslVmacPortObject_ObjectIdentity = ObjectIdentity
zxDslVmacPortObject = _ZxDslVmacPortObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 2)
)
_ZxDslVmacBrgPortTable_Object = MibTable
zxDslVmacBrgPortTable = _ZxDslVmacBrgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 2, 1)
)
if mibBuilder.loadTexts:
    zxDslVmacBrgPortTable.setStatus("current")
_ZxDslVmacBrgPortEntry_Object = MibTableRow
zxDslVmacBrgPortEntry = _ZxDslVmacBrgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 2, 1, 1)
)
zxDslVmacBrgPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslVmacBrgPortId"),
)
if mibBuilder.loadTexts:
    zxDslVmacBrgPortEntry.setStatus("current")
_ZxDslVmacBrgPortId_Type = Integer32
_ZxDslVmacBrgPortId_Object = MibTableColumn
zxDslVmacBrgPortId = _ZxDslVmacBrgPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 2, 1, 1, 1),
    _ZxDslVmacBrgPortId_Type()
)
zxDslVmacBrgPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslVmacBrgPortId.setStatus("current")


class _ZxDslVmacTranslateMode_Type(Integer32):
    """Custom type zxDslVmacTranslateMode based on Integer32"""
    defaultValue = 1

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
        *(("disable", 1),
          ("nToOne", 2),
          ("oneToOneFromMacPool", 3),
          ("oneToOneFromMappingRule", 4))
    )


_ZxDslVmacTranslateMode_Type.__name__ = "Integer32"
_ZxDslVmacTranslateMode_Object = MibTableColumn
zxDslVmacTranslateMode = _ZxDslVmacTranslateMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 2, 1, 1, 2),
    _ZxDslVmacTranslateMode_Type()
)
zxDslVmacTranslateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslVmacTranslateMode.setStatus("current")


class _ZxDslVmacTranslateLimit_Type(Integer32):
    """Custom type zxDslVmacTranslateLimit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ZxDslVmacTranslateLimit_Type.__name__ = "Integer32"
_ZxDslVmacTranslateLimit_Object = MibTableColumn
zxDslVmacTranslateLimit = _ZxDslVmacTranslateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 2, 1, 1, 3),
    _ZxDslVmacTranslateLimit_Type()
)
zxDslVmacTranslateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslVmacTranslateLimit.setStatus("current")
_ZxDslVmacTranslateTable_Object = MibTable
zxDslVmacTranslateTable = _ZxDslVmacTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 2, 2)
)
if mibBuilder.loadTexts:
    zxDslVmacTranslateTable.setStatus("current")
_ZxDslVmacTranslateEntry_Object = MibTableRow
zxDslVmacTranslateEntry = _ZxDslVmacTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 2, 2, 1)
)
zxDslVmacTranslateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslVmacTranslateBrgPortId"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslVmacTranslateUserMac"),
)
if mibBuilder.loadTexts:
    zxDslVmacTranslateEntry.setStatus("current")
_ZxDslVmacTranslateBrgPortId_Type = Integer32
_ZxDslVmacTranslateBrgPortId_Object = MibTableColumn
zxDslVmacTranslateBrgPortId = _ZxDslVmacTranslateBrgPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 2, 2, 1, 1),
    _ZxDslVmacTranslateBrgPortId_Type()
)
zxDslVmacTranslateBrgPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslVmacTranslateBrgPortId.setStatus("current")
_ZxDslVmacTranslateUserMac_Type = MacAddress
_ZxDslVmacTranslateUserMac_Object = MibTableColumn
zxDslVmacTranslateUserMac = _ZxDslVmacTranslateUserMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 2, 2, 1, 2),
    _ZxDslVmacTranslateUserMac_Type()
)
zxDslVmacTranslateUserMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslVmacTranslateUserMac.setStatus("current")
_ZxDslVmacTranslateSysMac_Type = MacAddress
_ZxDslVmacTranslateSysMac_Object = MibTableColumn
zxDslVmacTranslateSysMac = _ZxDslVmacTranslateSysMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 9, 4, 2, 2, 1, 3),
    _ZxDslVmacTranslateSysMac_Type()
)
zxDslVmacTranslateSysMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslVmacTranslateSysMac.setStatus("current")
_ZxDslPvlan_ObjectIdentity = ObjectIdentity
zxDslPvlan = _ZxDslPvlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 10)
)
_ZxDslUpLinkPortList_Type = PortList
_ZxDslUpLinkPortList_Object = MibScalar
zxDslUpLinkPortList = _ZxDslUpLinkPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 10, 1),
    _ZxDslUpLinkPortList_Type()
)
zxDslUpLinkPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslUpLinkPortList.setStatus("current")


class _ZxDslpvlanStatus_Type(Integer32):
    """Custom type zxDslpvlanStatus based on Integer32"""
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


_ZxDslpvlanStatus_Type.__name__ = "Integer32"
_ZxDslpvlanStatus_Object = MibScalar
zxDslpvlanStatus = _ZxDslpvlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 10, 2),
    _ZxDslpvlanStatus_Type()
)
zxDslpvlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslpvlanStatus.setStatus("current")
_ZxDslPvlanPortTable_Object = MibTable
zxDslPvlanPortTable = _ZxDslPvlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 10, 3)
)
if mibBuilder.loadTexts:
    zxDslPvlanPortTable.setStatus("current")
_ZxDslPvlanPortEntry_Object = MibTableRow
zxDslPvlanPortEntry = _ZxDslPvlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 10, 3, 1)
)
zxDslPvlanPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxDslPvlanPortEntry.setStatus("current")
_ZxDslPvlanPortInterList_Type = PortList
_ZxDslPvlanPortInterList_Object = MibTableColumn
zxDslPvlanPortInterList = _ZxDslPvlanPortInterList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 10, 3, 1, 2),
    _ZxDslPvlanPortInterList_Type()
)
zxDslPvlanPortInterList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslPvlanPortInterList.setStatus("current")


class _ZxDslPvlanPortAction_Type(Integer32):
    """Custom type zxDslPvlanPortAction based on Integer32"""
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


_ZxDslPvlanPortAction_Type.__name__ = "Integer32"
_ZxDslPvlanPortAction_Object = MibTableColumn
zxDslPvlanPortAction = _ZxDslPvlanPortAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 10, 3, 1, 3),
    _ZxDslPvlanPortAction_Type()
)
zxDslPvlanPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslPvlanPortAction.setStatus("current")
_ZxDslCPvlanTable_Object = MibTable
zxDslCPvlanTable = _ZxDslCPvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 10, 4)
)
if mibBuilder.loadTexts:
    zxDslCPvlanTable.setStatus("current")
_ZxDslCPvlanEntry_Object = MibTableRow
zxDslCPvlanEntry = _ZxDslCPvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 10, 4, 1)
)
zxDslCPvlanEntry.setIndexNames(
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslCPvlanVid"),
)
if mibBuilder.loadTexts:
    zxDslCPvlanEntry.setStatus("current")
_ZxDslCPvlanVid_Type = Integer32
_ZxDslCPvlanVid_Object = MibTableColumn
zxDslCPvlanVid = _ZxDslCPvlanVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 10, 4, 1, 1),
    _ZxDslCPvlanVid_Type()
)
zxDslCPvlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslCPvlanVid.setStatus("current")


class _ZxDslCPvlanStatus_Type(Integer32):
    """Custom type zxDslCPvlanStatus based on Integer32"""
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


_ZxDslCPvlanStatus_Type.__name__ = "Integer32"
_ZxDslCPvlanStatus_Object = MibTableColumn
zxDslCPvlanStatus = _ZxDslCPvlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 10, 4, 1, 2),
    _ZxDslCPvlanStatus_Type()
)
zxDslCPvlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslCPvlanStatus.setStatus("current")
_ZxDslSrvctrlGlobal_ObjectIdentity = ObjectIdentity
zxDslSrvctrlGlobal = _ZxDslSrvctrlGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 11)
)
_ZxDslBoardcastRateLimit_Type = Integer32
_ZxDslBoardcastRateLimit_Object = MibScalar
zxDslBoardcastRateLimit = _ZxDslBoardcastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 11, 1),
    _ZxDslBoardcastRateLimit_Type()
)
zxDslBoardcastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslBoardcastRateLimit.setStatus("current")
_ZxDslMulticastRateLimit_Type = Integer32
_ZxDslMulticastRateLimit_Object = MibScalar
zxDslMulticastRateLimit = _ZxDslMulticastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 11, 2),
    _ZxDslMulticastRateLimit_Type()
)
zxDslMulticastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslMulticastRateLimit.setStatus("current")
_ZxDslDlfRateLimit_Type = Integer32
_ZxDslDlfRateLimit_Object = MibScalar
zxDslDlfRateLimit = _ZxDslDlfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 11, 3),
    _ZxDslDlfRateLimit_Type()
)
zxDslDlfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslDlfRateLimit.setStatus("current")


class _ZxDslBoardcastEnalbed_Type(Integer32):
    """Custom type zxDslBoardcastEnalbed based on Integer32"""
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


_ZxDslBoardcastEnalbed_Type.__name__ = "Integer32"
_ZxDslBoardcastEnalbed_Object = MibScalar
zxDslBoardcastEnalbed = _ZxDslBoardcastEnalbed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 11, 4),
    _ZxDslBoardcastEnalbed_Type()
)
zxDslBoardcastEnalbed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslBoardcastEnalbed.setStatus("current")


class _ZxDslMulticastEnalbed_Type(Integer32):
    """Custom type zxDslMulticastEnalbed based on Integer32"""
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


_ZxDslMulticastEnalbed_Type.__name__ = "Integer32"
_ZxDslMulticastEnalbed_Object = MibScalar
zxDslMulticastEnalbed = _ZxDslMulticastEnalbed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 11, 5),
    _ZxDslMulticastEnalbed_Type()
)
zxDslMulticastEnalbed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslMulticastEnalbed.setStatus("current")


class _ZxDslDlfEnalbed_Type(Integer32):
    """Custom type zxDslDlfEnalbed based on Integer32"""
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


_ZxDslDlfEnalbed_Type.__name__ = "Integer32"
_ZxDslDlfEnalbed_Object = MibScalar
zxDslDlfEnalbed = _ZxDslDlfEnalbed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 11, 6),
    _ZxDslDlfEnalbed_Type()
)
zxDslDlfEnalbed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslDlfEnalbed.setStatus("current")


class _ZxDslAntiMacSpoofEnable_Type(Integer32):
    """Custom type zxDslAntiMacSpoofEnable based on Integer32"""
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


_ZxDslAntiMacSpoofEnable_Type.__name__ = "Integer32"
_ZxDslAntiMacSpoofEnable_Object = MibScalar
zxDslAntiMacSpoofEnable = _ZxDslAntiMacSpoofEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 11, 7),
    _ZxDslAntiMacSpoofEnable_Type()
)
zxDslAntiMacSpoofEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslAntiMacSpoofEnable.setStatus("current")


class _ZxDslEthMgmtIfForwardToNetIf_Type(Integer32):
    """Custom type zxDslEthMgmtIfForwardToNetIf based on Integer32"""
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


_ZxDslEthMgmtIfForwardToNetIf_Type.__name__ = "Integer32"
_ZxDslEthMgmtIfForwardToNetIf_Object = MibScalar
zxDslEthMgmtIfForwardToNetIf = _ZxDslEthMgmtIfForwardToNetIf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 11, 8),
    _ZxDslEthMgmtIfForwardToNetIf_Type()
)
zxDslEthMgmtIfForwardToNetIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslEthMgmtIfForwardToNetIf.setStatus("current")
_ZxDslEthMgmtIfForwardVlan_Type = Integer32
_ZxDslEthMgmtIfForwardVlan_Object = MibScalar
zxDslEthMgmtIfForwardVlan = _ZxDslEthMgmtIfForwardVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 11, 9),
    _ZxDslEthMgmtIfForwardVlan_Type()
)
zxDslEthMgmtIfForwardVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslEthMgmtIfForwardVlan.setStatus("current")


class _ZxDslVlanMode_Type(Integer32):
    """Custom type zxDslVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("traditionalVlan", 1),
          ("translatingVlan", 2),
          ("nToOneVlan", 3))
    )


_ZxDslVlanMode_Type.__name__ = "Integer32"
_ZxDslVlanMode_Object = MibScalar
zxDslVlanMode = _ZxDslVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 11, 10),
    _ZxDslVlanMode_Type()
)
zxDslVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslVlanMode.setStatus("current")
_ZxDslSrvMulticast_ObjectIdentity = ObjectIdentity
zxDslSrvMulticast = _ZxDslSrvMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 12)
)
_ZxDslMvidTable_Object = MibTable
zxDslMvidTable = _ZxDslMvidTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 12, 1)
)
if mibBuilder.loadTexts:
    zxDslMvidTable.setStatus("current")
_ZxDslMvidEntry_Object = MibTableRow
zxDslMvidEntry = _ZxDslMvidEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 12, 1, 1)
)
zxDslMvidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslMvidBrgPortId"),
)
if mibBuilder.loadTexts:
    zxDslMvidEntry.setStatus("current")
_ZxDslMvidBrgPortId_Type = Integer32
_ZxDslMvidBrgPortId_Object = MibTableColumn
zxDslMvidBrgPortId = _ZxDslMvidBrgPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 12, 1, 1, 1),
    _ZxDslMvidBrgPortId_Type()
)
zxDslMvidBrgPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslMvidBrgPortId.setStatus("current")
_ZxDslMvid_Type = Integer32
_ZxDslMvid_Object = MibTableColumn
zxDslMvid = _ZxDslMvid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 12, 1, 1, 2),
    _ZxDslMvid_Type()
)
zxDslMvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslMvid.setStatus("current")
_ZxDslMvidRowStatus_Type = RowStatus
_ZxDslMvidRowStatus_Object = MibTableColumn
zxDslMvidRowStatus = _ZxDslMvidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 12, 1, 1, 10),
    _ZxDslMvidRowStatus_Type()
)
zxDslMvidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslMvidRowStatus.setStatus("current")
_ZxDslServicePort_ObjectIdentity = ObjectIdentity
zxDslServicePort = _ZxDslServicePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 13)
)
_ZxDslServicePortTable_Object = MibTable
zxDslServicePortTable = _ZxDslServicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 13, 1)
)
if mibBuilder.loadTexts:
    zxDslServicePortTable.setStatus("current")
_ZxDslServicePortEntry_Object = MibTableRow
zxDslServicePortEntry = _ZxDslServicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 13, 1, 1)
)
zxDslServicePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslServicePortId"),
)
if mibBuilder.loadTexts:
    zxDslServicePortEntry.setStatus("current")
_ZxDslServicePortId_Type = Integer32
_ZxDslServicePortId_Object = MibTableColumn
zxDslServicePortId = _ZxDslServicePortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 13, 1, 1, 1),
    _ZxDslServicePortId_Type()
)
zxDslServicePortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslServicePortId.setStatus("current")


class _ZxDslServicePortDesc_Type(DisplayString):
    """Custom type zxDslServicePortDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxDslServicePortDesc_Type.__name__ = "DisplayString"
_ZxDslServicePortDesc_Object = MibTableColumn
zxDslServicePortDesc = _ZxDslServicePortDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 13, 1, 1, 2),
    _ZxDslServicePortDesc_Type()
)
zxDslServicePortDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslServicePortDesc.setStatus("current")


class _ZxDslServicePortServiceMode_Type(Bits):
    """Custom type zxDslServicePortServiceMode based on Bits"""
    namedValues = NamedValues(
        *(("pvc", 0),
          ("vlan", 1),
          ("priority", 2),
          ("encapType", 3))
    )

_ZxDslServicePortServiceMode_Type.__name__ = "Bits"
_ZxDslServicePortServiceMode_Object = MibTableColumn
zxDslServicePortServiceMode = _ZxDslServicePortServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 13, 1, 1, 3),
    _ZxDslServicePortServiceMode_Type()
)
zxDslServicePortServiceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslServicePortServiceMode.setStatus("current")


class _ZxDslServicePortPvc_Type(Integer32):
    """Custom type zxDslServicePortPvc based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxDslServicePortPvc_Type.__name__ = "Integer32"
_ZxDslServicePortPvc_Object = MibTableColumn
zxDslServicePortPvc = _ZxDslServicePortPvc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 13, 1, 1, 4),
    _ZxDslServicePortPvc_Type()
)
zxDslServicePortPvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslServicePortPvc.setStatus("current")


class _ZxDslServicePortVlan_Type(Integer32):
    """Custom type zxDslServicePortVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxDslServicePortVlan_Type.__name__ = "Integer32"
_ZxDslServicePortVlan_Object = MibTableColumn
zxDslServicePortVlan = _ZxDslServicePortVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 13, 1, 1, 5),
    _ZxDslServicePortVlan_Type()
)
zxDslServicePortVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslServicePortVlan.setStatus("current")


class _ZxDslServicePortPriority_Type(Integer32):
    """Custom type zxDslServicePortPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxDslServicePortPriority_Type.__name__ = "Integer32"
_ZxDslServicePortPriority_Object = MibTableColumn
zxDslServicePortPriority = _ZxDslServicePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 13, 1, 1, 6),
    _ZxDslServicePortPriority_Type()
)
zxDslServicePortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslServicePortPriority.setStatus("current")


class _ZxDslServicePortEthType_Type(Integer32):
    """Custom type zxDslServicePortEthType based on Integer32"""
    defaultValue = 1

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
        *(("pppoe", 1),
          ("arp", 2),
          ("ipoe", 3),
          ("ipoev6", 4),
          ("customized", 5))
    )


_ZxDslServicePortEthType_Type.__name__ = "Integer32"
_ZxDslServicePortEthType_Object = MibTableColumn
zxDslServicePortEthType = _ZxDslServicePortEthType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 13, 1, 1, 7),
    _ZxDslServicePortEthType_Type()
)
zxDslServicePortEthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslServicePortEthType.setStatus("current")
_ZxDslServicePortCustomizedEthType_Type = Integer32
_ZxDslServicePortCustomizedEthType_Object = MibTableColumn
zxDslServicePortCustomizedEthType = _ZxDslServicePortCustomizedEthType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 13, 1, 1, 8),
    _ZxDslServicePortCustomizedEthType_Type()
)
zxDslServicePortCustomizedEthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslServicePortCustomizedEthType.setStatus("current")
_ZxDslServicePortRowStatus_Type = RowStatus
_ZxDslServicePortRowStatus_Object = MibTableColumn
zxDslServicePortRowStatus = _ZxDslServicePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 13, 1, 1, 50),
    _ZxDslServicePortRowStatus_Type()
)
zxDslServicePortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslServicePortRowStatus.setStatus("current")
_ZxDslNni_ObjectIdentity = ObjectIdentity
zxDslNni = _ZxDslNni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 14)
)
_ZxDslNniTable_Object = MibTable
zxDslNniTable = _ZxDslNniTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 14, 1)
)
if mibBuilder.loadTexts:
    zxDslNniTable.setStatus("current")
_ZxDslNniEntry_Object = MibTableRow
zxDslNniEntry = _ZxDslNniEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 14, 1, 1)
)
zxDslNniEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxDslNniEntry.setStatus("current")
_ZxDslNniTxOpticalPower_Type = Integer32
_ZxDslNniTxOpticalPower_Object = MibTableColumn
zxDslNniTxOpticalPower = _ZxDslNniTxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 14, 1, 1, 1),
    _ZxDslNniTxOpticalPower_Type()
)
zxDslNniTxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslNniTxOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    zxDslNniTxOpticalPower.setUnits("0.001dbm")
_ZxDslNniRxOpticalPower_Type = Integer32
_ZxDslNniRxOpticalPower_Object = MibTableColumn
zxDslNniRxOpticalPower = _ZxDslNniRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 14, 1, 1, 2),
    _ZxDslNniRxOpticalPower_Type()
)
zxDslNniRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslNniRxOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    zxDslNniRxOpticalPower.setUnits("0.001dbm")
_ZxDslNniOpticalTxBiasCurrent_Type = Integer32
_ZxDslNniOpticalTxBiasCurrent_Object = MibTableColumn
zxDslNniOpticalTxBiasCurrent = _ZxDslNniOpticalTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 14, 1, 1, 3),
    _ZxDslNniOpticalTxBiasCurrent_Type()
)
zxDslNniOpticalTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslNniOpticalTxBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxDslNniOpticalTxBiasCurrent.setUnits("0.001uA")
_ZxDslNniOpticalVoltage_Type = Integer32
_ZxDslNniOpticalVoltage_Object = MibTableColumn
zxDslNniOpticalVoltage = _ZxDslNniOpticalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 14, 1, 1, 4),
    _ZxDslNniOpticalVoltage_Type()
)
zxDslNniOpticalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslNniOpticalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    zxDslNniOpticalVoltage.setUnits("0.001V")
_ZxDslNniOpticalTemperature_Type = Integer32
_ZxDslNniOpticalTemperature_Object = MibTableColumn
zxDslNniOpticalTemperature = _ZxDslNniOpticalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 14, 1, 1, 5),
    _ZxDslNniOpticalTemperature_Type()
)
zxDslNniOpticalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslNniOpticalTemperature.setStatus("current")
if mibBuilder.loadTexts:
    zxDslNniOpticalTemperature.setUnits("0.001centigrade")
_ZxDslIpv6Objects_ObjectIdentity = ObjectIdentity
zxDslIpv6Objects = _ZxDslIpv6Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 15)
)
_ZxDslIpv6IpLockTable_Object = MibTable
zxDslIpv6IpLockTable = _ZxDslIpv6IpLockTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 15, 1)
)
if mibBuilder.loadTexts:
    zxDslIpv6IpLockTable.setStatus("current")
_ZxDslIpv6IpLockEntry_Object = MibTableRow
zxDslIpv6IpLockEntry = _ZxDslIpv6IpLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 15, 1, 1)
)
zxDslIpv6IpLockEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslIpv6IpLockIpAddr"),
)
if mibBuilder.loadTexts:
    zxDslIpv6IpLockEntry.setStatus("current")
_ZxDslIpv6IpLockIpAddr_Type = InetAddress
_ZxDslIpv6IpLockIpAddr_Object = MibTableColumn
zxDslIpv6IpLockIpAddr = _ZxDslIpv6IpLockIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 15, 1, 1, 1),
    _ZxDslIpv6IpLockIpAddr_Type()
)
zxDslIpv6IpLockIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslIpv6IpLockIpAddr.setStatus("current")
_ZxDslIpv6IpLockIpAddrPfxLen_Type = InetAddressPrefixLength
_ZxDslIpv6IpLockIpAddrPfxLen_Object = MibTableColumn
zxDslIpv6IpLockIpAddrPfxLen = _ZxDslIpv6IpLockIpAddrPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 15, 1, 1, 2),
    _ZxDslIpv6IpLockIpAddrPfxLen_Type()
)
zxDslIpv6IpLockIpAddrPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslIpv6IpLockIpAddrPfxLen.setStatus("current")
_ZxDslIpv6IpLockRowStatus_Type = RowStatus
_ZxDslIpv6IpLockRowStatus_Object = MibTableColumn
zxDslIpv6IpLockRowStatus = _ZxDslIpv6IpLockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 15, 1, 1, 10),
    _ZxDslIpv6IpLockRowStatus_Type()
)
zxDslIpv6IpLockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslIpv6IpLockRowStatus.setStatus("current")
_ZxDslPonLinkObjects_ObjectIdentity = ObjectIdentity
zxDslPonLinkObjects = _ZxDslPonLinkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 16)
)
_ZxDslPonLinkGlobalObjects_ObjectIdentity = ObjectIdentity
zxDslPonLinkGlobalObjects = _ZxDslPonLinkGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 16, 1)
)
_ZxDslPonLinkForceSwap_Type = Integer32
_ZxDslPonLinkForceSwap_Object = MibScalar
zxDslPonLinkForceSwap = _ZxDslPonLinkForceSwap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 16, 1, 1),
    _ZxDslPonLinkForceSwap_Type()
)
zxDslPonLinkForceSwap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslPonLinkForceSwap.setStatus("current")
_ZxDslProtocolRateLimitObjects_ObjectIdentity = ObjectIdentity
zxDslProtocolRateLimitObjects = _ZxDslProtocolRateLimitObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17)
)
_ZxDslProtocolRateLimitTable_Object = MibTable
zxDslProtocolRateLimitTable = _ZxDslProtocolRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17, 1)
)
if mibBuilder.loadTexts:
    zxDslProtocolRateLimitTable.setStatus("current")
_ZxDslProtocolRateLimitEntry_Object = MibTableRow
zxDslProtocolRateLimitEntry = _ZxDslProtocolRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17, 1, 1)
)
zxDslProtocolRateLimitEntry.setIndexNames(
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslProtocolType"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslProtocolRateLimitScale"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslProtocolRateLimitIndex"),
)
if mibBuilder.loadTexts:
    zxDslProtocolRateLimitEntry.setStatus("current")
_ZxDslProtocolType_Type = RateLimitProtocolType
_ZxDslProtocolType_Object = MibTableColumn
zxDslProtocolType = _ZxDslProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17, 1, 1, 1),
    _ZxDslProtocolType_Type()
)
zxDslProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslProtocolType.setStatus("current")
_ZxDslProtocolRateLimitScale_Type = RateLimitScale
_ZxDslProtocolRateLimitScale_Object = MibTableColumn
zxDslProtocolRateLimitScale = _ZxDslProtocolRateLimitScale_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17, 1, 1, 2),
    _ZxDslProtocolRateLimitScale_Type()
)
zxDslProtocolRateLimitScale.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslProtocolRateLimitScale.setStatus("current")
_ZxDslProtocolRateLimitIndex_Type = Integer32
_ZxDslProtocolRateLimitIndex_Object = MibTableColumn
zxDslProtocolRateLimitIndex = _ZxDslProtocolRateLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17, 1, 1, 3),
    _ZxDslProtocolRateLimitIndex_Type()
)
zxDslProtocolRateLimitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslProtocolRateLimitIndex.setStatus("current")


class _ZxDslProtocolRateLimitAction_Type(Integer32):
    """Custom type zxDslProtocolRateLimitAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("rateLimit", 2),
          ("rateUnlimit", 3))
    )


_ZxDslProtocolRateLimitAction_Type.__name__ = "Integer32"
_ZxDslProtocolRateLimitAction_Object = MibTableColumn
zxDslProtocolRateLimitAction = _ZxDslProtocolRateLimitAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17, 1, 1, 4),
    _ZxDslProtocolRateLimitAction_Type()
)
zxDslProtocolRateLimitAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslProtocolRateLimitAction.setStatus("current")
_ZxDslProtocolRateLimitValue_Type = Integer32
_ZxDslProtocolRateLimitValue_Object = MibTableColumn
zxDslProtocolRateLimitValue = _ZxDslProtocolRateLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17, 1, 1, 5),
    _ZxDslProtocolRateLimitValue_Type()
)
zxDslProtocolRateLimitValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslProtocolRateLimitValue.setStatus("current")
_ZxDslSupportedRateLimitTable_Object = MibTable
zxDslSupportedRateLimitTable = _ZxDslSupportedRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17, 2)
)
if mibBuilder.loadTexts:
    zxDslSupportedRateLimitTable.setStatus("current")
_ZxDslSupportedRateLimitEntry_Object = MibTableRow
zxDslSupportedRateLimitEntry = _ZxDslSupportedRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17, 2, 1)
)
zxDslSupportedRateLimitEntry.setIndexNames(
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslSupportedProtocolType"),
    (0, "ZTE-DSL-SRVCTRL-MIB", "zxDslSupportedRateLimitScale"),
)
if mibBuilder.loadTexts:
    zxDslSupportedRateLimitEntry.setStatus("current")
_ZxDslSupportedProtocolType_Type = RateLimitProtocolType
_ZxDslSupportedProtocolType_Object = MibTableColumn
zxDslSupportedProtocolType = _ZxDslSupportedProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17, 2, 1, 1),
    _ZxDslSupportedProtocolType_Type()
)
zxDslSupportedProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslSupportedProtocolType.setStatus("current")
_ZxDslSupportedRateLimitScale_Type = RateLimitScale
_ZxDslSupportedRateLimitScale_Object = MibTableColumn
zxDslSupportedRateLimitScale = _ZxDslSupportedRateLimitScale_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17, 2, 1, 2),
    _ZxDslSupportedRateLimitScale_Type()
)
zxDslSupportedRateLimitScale.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslSupportedRateLimitScale.setStatus("current")


class _ZxDslSupportedRateLimitUnits_Type(Integer32):
    """Custom type zxDslSupportedRateLimitUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("pps", 2))
    )


_ZxDslSupportedRateLimitUnits_Type.__name__ = "Integer32"
_ZxDslSupportedRateLimitUnits_Object = MibTableColumn
zxDslSupportedRateLimitUnits = _ZxDslSupportedRateLimitUnits_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 1, 17, 2, 1, 3),
    _ZxDslSupportedRateLimitUnits_Type()
)
zxDslSupportedRateLimitUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslSupportedRateLimitUnits.setStatus("current")
_ZxDslSrvctrlTrapObjects_ObjectIdentity = ObjectIdentity
zxDslSrvctrlTrapObjects = _ZxDslSrvctrlTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 2)
)
_ZxDslSrvctrlTrapBindVar_ObjectIdentity = ObjectIdentity
zxDslSrvctrlTrapBindVar = _ZxDslSrvctrlTrapBindVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 3)
)
_ZxDslExtIfAntiDosSourceMacAddr_Type = MacAddress
_ZxDslExtIfAntiDosSourceMacAddr_Object = MibScalar
zxDslExtIfAntiDosSourceMacAddr = _ZxDslExtIfAntiDosSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 3, 1),
    _ZxDslExtIfAntiDosSourceMacAddr_Type()
)
zxDslExtIfAntiDosSourceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslExtIfAntiDosSourceMacAddr.setStatus("current")

# Managed Objects groups


# Notification objects

zxDslExtIfMacLearnExceedLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 2, 1)
)
zxDslExtIfMacLearnExceedLimit.setObjects(
    ("ZTE-DSL-SRVCTRL-MIB", "zxDslExtIfMaxMacLearn")
)
if mibBuilder.loadTexts:
    zxDslExtIfMacLearnExceedLimit.setStatus(
        "current"
    )

zxDslExtIfAntiDosFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 2, 2)
)
zxDslExtIfAntiDosFault.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZTE-DSL-SRVCTRL-MIB", "zxDslExtIfAntiDosSourceMacAddr"))
)
if mibBuilder.loadTexts:
    zxDslExtIfAntiDosFault.setStatus(
        "current"
    )

zxDslExtIfAntiDosFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 2, 3)
)
zxDslExtIfAntiDosFaultCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZTE-DSL-SRVCTRL-MIB", "zxDslExtIfAttackedMacAddr"))
)
if mibBuilder.loadTexts:
    zxDslExtIfAntiDosFaultCleared.setStatus(
        "current"
    )

zxDslRateOverThreshFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 2, 4)
)
zxDslRateOverThreshFault.setObjects(
    ("ZTE-DSL-SRVCTRL-MIB", "zxDslProtocolRateLimitValue")
)
if mibBuilder.loadTexts:
    zxDslRateOverThreshFault.setStatus(
        "current"
    )

zxDslRateOverThreshFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 7, 2, 5)
)
zxDslRateOverThreshFaultCleared.setObjects(
    ("ZTE-DSL-SRVCTRL-MIB", "zxDslProtocolRateLimitValue")
)
if mibBuilder.loadTexts:
    zxDslRateOverThreshFaultCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-SRVCTRL-MIB",
    **{"RateLimitProtocolType": RateLimitProtocolType,
       "RateLimitScale": RateLimitScale,
       "zte": zte,
       "zxDsl": zxDsl,
       "zxDslSrvctrlMib": zxDslSrvctrlMib,
       "zxDslSrvctrlObjects": zxDslSrvctrlObjects,
       "zxDslMacLockTable": zxDslMacLockTable,
       "zxDslMacLockEntry": zxDslMacLockEntry,
       "zxDslMacLockMacAddr": zxDslMacLockMacAddr,
       "zxDslMacLockVid": zxDslMacLockVid,
       "zxDslMacLockRowStatus": zxDslMacLockRowStatus,
       "zxDslStaticMacTable": zxDslStaticMacTable,
       "zxDslStaticMacEntry": zxDslStaticMacEntry,
       "zxDslStaticMacAddr": zxDslStaticMacAddr,
       "zxDslStaticMacVid": zxDslStaticMacVid,
       "zxDslStaticMacPvcId": zxDslStaticMacPvcId,
       "zxDslStaticMacTagflag": zxDslStaticMacTagflag,
       "zxDslStaticMacRowStatus": zxDslStaticMacRowStatus,
       "zxDslIpLockTable": zxDslIpLockTable,
       "zxDslIpLockEntry": zxDslIpLockEntry,
       "zxDslIpLockIpAddr": zxDslIpLockIpAddr,
       "zxDslIpLockRowStatus": zxDslIpLockRowStatus,
       "zxDslExtIfTable": zxDslExtIfTable,
       "zxDslExtIfEntry": zxDslExtIfEntry,
       "zxDslExtIfFlowCtrlSet": zxDslExtIfFlowCtrlSet,
       "zxDslExtIfFlowCtrlGet": zxDslExtIfFlowCtrlGet,
       "zxDslExtIfSpeedSet": zxDslExtIfSpeedSet,
       "zxDslExtIfSpeedGet": zxDslExtIfSpeedGet,
       "zxDslExtIfDuplexSet": zxDslExtIfDuplexSet,
       "zxDslExtIfDuplexGet": zxDslExtIfDuplexGet,
       "zxDslExtIfMaxMacLearn": zxDslExtIfMaxMacLearn,
       "zxDslExtIfBroadcastRatelimit": zxDslExtIfBroadcastRatelimit,
       "zxDslExtIfMulticastRatelimit": zxDslExtIfMulticastRatelimit,
       "zxDslExtIfDlfRatelimit": zxDslExtIfDlfRatelimit,
       "zxDslExtIfLinkErrors": zxDslExtIfLinkErrors,
       "zxDslExtIfInterTag": zxDslExtIfInterTag,
       "zxDslExtIfBoardcastEnable": zxDslExtIfBoardcastEnable,
       "zxDslExtIfMulticastEnable": zxDslExtIfMulticastEnable,
       "zxDslExtIfDlfEnable": zxDslExtIfDlfEnable,
       "zxDslExtIfDhcpRatelimit": zxDslExtIfDhcpRatelimit,
       "zxDslExtIfUserInfoUserName": zxDslExtIfUserInfoUserName,
       "zxDslExtIfUserInfoUserAddress": zxDslExtIfUserInfoUserAddress,
       "zxDslExtIfUserInfoUserServiceConfigured": zxDslExtIfUserInfoUserServiceConfigured,
       "zxDslExtIfUserInfoUserOtherNode": zxDslExtIfUserInfoUserOtherNode,
       "zxDslExtIfPoeStatus": zxDslExtIfPoeStatus,
       "zxDslExtIfPoeEnable": zxDslExtIfPoeEnable,
       "zxDslExtIfDhcpv6RateLimit": zxDslExtIfDhcpv6RateLimit,
       "zxDslExtIfIcmpv6RateLimit": zxDslExtIfIcmpv6RateLimit,
       "zxDslMacFilterTable": zxDslMacFilterTable,
       "zxDslMacFilterEntry": zxDslMacFilterEntry,
       "zxDslMacFilterMacAddr": zxDslMacFilterMacAddr,
       "zxDslMacFilterRowStatus": zxDslMacFilterRowStatus,
       "zxDslMacCtrlObjects": zxDslMacCtrlObjects,
       "zxDslMacCtrlGlobalObjects": zxDslMacCtrlGlobalObjects,
       "zxDslMacLearnType": zxDslMacLearnType,
       "zxDslPredefMacForwardEnable": zxDslPredefMacForwardEnable,
       "zxDslMacClear": zxDslMacClear,
       "zxDslMacClearType": zxDslMacClearType,
       "zxDslMacClearValue": zxDslMacClearValue,
       "zxDslMacAddressObject": zxDslMacAddressObject,
       "zxDslMacAddressTable": zxDslMacAddressTable,
       "zxDslMacAddressEntry": zxDslMacAddressEntry,
       "zxDslMacAddressList": zxDslMacAddressList,
       "zxDslMacAddressExtTable": zxDslMacAddressExtTable,
       "zxDslMacAddressExtEntry": zxDslMacAddressExtEntry,
       "zxDslMacAddressExtSeqId": zxDslMacAddressExtSeqId,
       "zxDslMacAddressExtList": zxDslMacAddressExtList,
       "zxDslVmacObjects": zxDslVmacObjects,
       "zxDslVmacGlobalObjects": zxDslVmacGlobalObjects,
       "zxDslVmacDeviceId": zxDslVmacDeviceId,
       "zxDslVmacSysMac": zxDslVmacSysMac,
       "zxDslVmacPortObject": zxDslVmacPortObject,
       "zxDslVmacBrgPortTable": zxDslVmacBrgPortTable,
       "zxDslVmacBrgPortEntry": zxDslVmacBrgPortEntry,
       "zxDslVmacBrgPortId": zxDslVmacBrgPortId,
       "zxDslVmacTranslateMode": zxDslVmacTranslateMode,
       "zxDslVmacTranslateLimit": zxDslVmacTranslateLimit,
       "zxDslVmacTranslateTable": zxDslVmacTranslateTable,
       "zxDslVmacTranslateEntry": zxDslVmacTranslateEntry,
       "zxDslVmacTranslateBrgPortId": zxDslVmacTranslateBrgPortId,
       "zxDslVmacTranslateUserMac": zxDslVmacTranslateUserMac,
       "zxDslVmacTranslateSysMac": zxDslVmacTranslateSysMac,
       "zxDslPvlan": zxDslPvlan,
       "zxDslUpLinkPortList": zxDslUpLinkPortList,
       "zxDslpvlanStatus": zxDslpvlanStatus,
       "zxDslPvlanPortTable": zxDslPvlanPortTable,
       "zxDslPvlanPortEntry": zxDslPvlanPortEntry,
       "zxDslPvlanPortInterList": zxDslPvlanPortInterList,
       "zxDslPvlanPortAction": zxDslPvlanPortAction,
       "zxDslCPvlanTable": zxDslCPvlanTable,
       "zxDslCPvlanEntry": zxDslCPvlanEntry,
       "zxDslCPvlanVid": zxDslCPvlanVid,
       "zxDslCPvlanStatus": zxDslCPvlanStatus,
       "zxDslSrvctrlGlobal": zxDslSrvctrlGlobal,
       "zxDslBoardcastRateLimit": zxDslBoardcastRateLimit,
       "zxDslMulticastRateLimit": zxDslMulticastRateLimit,
       "zxDslDlfRateLimit": zxDslDlfRateLimit,
       "zxDslBoardcastEnalbed": zxDslBoardcastEnalbed,
       "zxDslMulticastEnalbed": zxDslMulticastEnalbed,
       "zxDslDlfEnalbed": zxDslDlfEnalbed,
       "zxDslAntiMacSpoofEnable": zxDslAntiMacSpoofEnable,
       "zxDslEthMgmtIfForwardToNetIf": zxDslEthMgmtIfForwardToNetIf,
       "zxDslEthMgmtIfForwardVlan": zxDslEthMgmtIfForwardVlan,
       "zxDslVlanMode": zxDslVlanMode,
       "zxDslSrvMulticast": zxDslSrvMulticast,
       "zxDslMvidTable": zxDslMvidTable,
       "zxDslMvidEntry": zxDslMvidEntry,
       "zxDslMvidBrgPortId": zxDslMvidBrgPortId,
       "zxDslMvid": zxDslMvid,
       "zxDslMvidRowStatus": zxDslMvidRowStatus,
       "zxDslServicePort": zxDslServicePort,
       "zxDslServicePortTable": zxDslServicePortTable,
       "zxDslServicePortEntry": zxDslServicePortEntry,
       "zxDslServicePortId": zxDslServicePortId,
       "zxDslServicePortDesc": zxDslServicePortDesc,
       "zxDslServicePortServiceMode": zxDslServicePortServiceMode,
       "zxDslServicePortPvc": zxDslServicePortPvc,
       "zxDslServicePortVlan": zxDslServicePortVlan,
       "zxDslServicePortPriority": zxDslServicePortPriority,
       "zxDslServicePortEthType": zxDslServicePortEthType,
       "zxDslServicePortCustomizedEthType": zxDslServicePortCustomizedEthType,
       "zxDslServicePortRowStatus": zxDslServicePortRowStatus,
       "zxDslNni": zxDslNni,
       "zxDslNniTable": zxDslNniTable,
       "zxDslNniEntry": zxDslNniEntry,
       "zxDslNniTxOpticalPower": zxDslNniTxOpticalPower,
       "zxDslNniRxOpticalPower": zxDslNniRxOpticalPower,
       "zxDslNniOpticalTxBiasCurrent": zxDslNniOpticalTxBiasCurrent,
       "zxDslNniOpticalVoltage": zxDslNniOpticalVoltage,
       "zxDslNniOpticalTemperature": zxDslNniOpticalTemperature,
       "zxDslIpv6Objects": zxDslIpv6Objects,
       "zxDslIpv6IpLockTable": zxDslIpv6IpLockTable,
       "zxDslIpv6IpLockEntry": zxDslIpv6IpLockEntry,
       "zxDslIpv6IpLockIpAddr": zxDslIpv6IpLockIpAddr,
       "zxDslIpv6IpLockIpAddrPfxLen": zxDslIpv6IpLockIpAddrPfxLen,
       "zxDslIpv6IpLockRowStatus": zxDslIpv6IpLockRowStatus,
       "zxDslPonLinkObjects": zxDslPonLinkObjects,
       "zxDslPonLinkGlobalObjects": zxDslPonLinkGlobalObjects,
       "zxDslPonLinkForceSwap": zxDslPonLinkForceSwap,
       "zxDslProtocolRateLimitObjects": zxDslProtocolRateLimitObjects,
       "zxDslProtocolRateLimitTable": zxDslProtocolRateLimitTable,
       "zxDslProtocolRateLimitEntry": zxDslProtocolRateLimitEntry,
       "zxDslProtocolType": zxDslProtocolType,
       "zxDslProtocolRateLimitScale": zxDslProtocolRateLimitScale,
       "zxDslProtocolRateLimitIndex": zxDslProtocolRateLimitIndex,
       "zxDslProtocolRateLimitAction": zxDslProtocolRateLimitAction,
       "zxDslProtocolRateLimitValue": zxDslProtocolRateLimitValue,
       "zxDslSupportedRateLimitTable": zxDslSupportedRateLimitTable,
       "zxDslSupportedRateLimitEntry": zxDslSupportedRateLimitEntry,
       "zxDslSupportedProtocolType": zxDslSupportedProtocolType,
       "zxDslSupportedRateLimitScale": zxDslSupportedRateLimitScale,
       "zxDslSupportedRateLimitUnits": zxDslSupportedRateLimitUnits,
       "zxDslSrvctrlTrapObjects": zxDslSrvctrlTrapObjects,
       "zxDslExtIfMacLearnExceedLimit": zxDslExtIfMacLearnExceedLimit,
       "zxDslExtIfAntiDosFault": zxDslExtIfAntiDosFault,
       "zxDslExtIfAntiDosFaultCleared": zxDslExtIfAntiDosFaultCleared,
       "zxDslRateOverThreshFault": zxDslRateOverThreshFault,
       "zxDslRateOverThreshFaultCleared": zxDslRateOverThreshFaultCleared,
       "zxDslSrvctrlTrapBindVar": zxDslSrvctrlTrapBindVar,
       "zxDslExtIfAntiDosSourceMacAddr": zxDslExtIfAntiDosSourceMacAddr}
)
