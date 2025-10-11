# SNMP MIB module (TN-VRTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-VRTR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:59:21 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")

(TCpmProtPolicyID,
 TIPFilterID,
 TItemDescription,
 TItemLongDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TNetworkPolicyID,
 TmnxAdminState,
 TmnxBgpAutonomousSystem,
 TmnxCustId,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxMplsTpGlobalID,
 TmnxMplsTpNodeID,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxStatus,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrID,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TCpmProtPolicyID",
    "TIPFilterID",
    "TItemDescription",
    "TItemLongDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TNetworkPolicyID",
    "TmnxAdminState",
    "TmnxBgpAutonomousSystem",
    "TmnxCustId",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxMplsTpGlobalID",
    "TmnxMplsTpNodeID",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxStatus",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnVRtrMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tnVRtrMIBModule.setRevisions(
        ("2015-09-14 00:00",
         "2015-04-21 00:00",
         "2015-04-06 00:00",
         "2015-03-24 00:00",
         "2015-03-02 00:00",
         "2015-01-30 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-02-28 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2000-08-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxVPNId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )



class TmnxInetAddrState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("tentative", 1),
          ("duplicated", 2),
          ("inaccessible", 3),
          ("deprecated", 4),
          ("preferred", 5))
    )



class TDSCPAppId(TextualConvention, Integer32):
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
        *(("bgp", 1),
          ("cflowd", 2),
          ("dhcp", 3),
          ("dns", 4),
          ("ftp", 5),
          ("icmp", 6),
          ("igmp", 7),
          ("l2tp", 8),
          ("ldp", 9),
          ("mld", 10),
          ("msdp", 11),
          ("ndis", 12),
          ("ntp", 13),
          ("ospf", 14),
          ("pim", 15),
          ("radius", 16),
          ("rip", 17),
          ("rsvp", 18),
          ("snmp", 19),
          ("snmp-notification", 20),
          ("srrp", 21),
          ("ssh", 22),
          ("syslog", 23),
          ("tacplus", 24),
          ("telnet", 25),
          ("tftp", 26),
          ("traceroute", 27),
          ("vrrp", 28),
          ("ptp", 29),
          ("igmp-reporter", 30),
          ("gtp", 31))
    )



class TDot1pAppId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("isis", 2),
          ("pppoe", 3))
    )



class TmnxVrtrSingleSfmOverloadState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("normal", 1),
          ("overload", 2))
    )



class TmnxInetCidrNextHopType(TextualConvention, Integer32):
    status = "current"
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
        *(("regular", 1),
          ("tunneled", 2),
          ("sixOverMPLS", 3),
          ("sixOverFour", 4))
    )



class TmnxInetCidrNextHopOwner(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("rsvp", 1),
          ("ldp", 2),
          ("ldpOverRsvp", 3))
    )



class TmnxL3RouteOwner(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("local", 1),
          ("host", 2),
          ("static", 5),
          ("bgp", 16))
    )



# MIB Managed Objects in the order of their OIDs

_TnVRtrObjs_ObjectIdentity = ObjectIdentity
tnVRtrObjs = _TnVRtrObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3)
)
_VRtrConfTable_Object = MibTable
vRtrConfTable = _VRtrConfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vRtrConfTable.setStatus("current")
_VRtrConfEntry_Object = MibTableRow
vRtrConfEntry = _VRtrConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1)
)
vRtrConfEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrConfEntry.setStatus("current")
_VRtrID_Type = TmnxVRtrID
_VRtrID_Object = MibTableColumn
vRtrID = _VRtrID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 1),
    _VRtrID_Type()
)
vRtrID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrID.setStatus("current")
_VRtrRowStatus_Type = RowStatus
_VRtrRowStatus_Object = MibTableColumn
vRtrRowStatus = _VRtrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 2),
    _VRtrRowStatus_Type()
)
vRtrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRowStatus.setStatus("current")


class _VRtrAdminState_Type(TmnxAdminState):
    """Custom type vRtrAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrAdminState_Type.__name__ = "TmnxAdminState"
_VRtrAdminState_Object = MibTableColumn
vRtrAdminState = _VRtrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 3),
    _VRtrAdminState_Type()
)
vRtrAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAdminState.setStatus("current")
_VRtrName_Type = TNamedItemOrEmpty
_VRtrName_Object = MibTableColumn
vRtrName = _VRtrName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 4),
    _VRtrName_Type()
)
vRtrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrName.setStatus("current")


class _VRtrMaxNumRoutes_Type(Integer32):
    """Custom type vRtrMaxNumRoutes based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_VRtrMaxNumRoutes_Type.__name__ = "Integer32"
_VRtrMaxNumRoutes_Object = MibTableColumn
vRtrMaxNumRoutes = _VRtrMaxNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 5),
    _VRtrMaxNumRoutes_Type()
)
vRtrMaxNumRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMaxNumRoutes.setStatus("current")


class _VRtrBgpStatus_Type(TmnxStatus):
    """Custom type vRtrBgpStatus based on TmnxStatus"""
    defaultValue = 2


_VRtrBgpStatus_Type.__name__ = "TmnxStatus"
_VRtrBgpStatus_Object = MibTableColumn
vRtrBgpStatus = _VRtrBgpStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 6),
    _VRtrBgpStatus_Type()
)
vRtrBgpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrBgpStatus.setStatus("current")


class _VRtrMplsStatus_Type(TmnxStatus):
    """Custom type vRtrMplsStatus based on TmnxStatus"""
    defaultValue = 2


_VRtrMplsStatus_Type.__name__ = "TmnxStatus"
_VRtrMplsStatus_Object = MibTableColumn
vRtrMplsStatus = _VRtrMplsStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 7),
    _VRtrMplsStatus_Type()
)
vRtrMplsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsStatus.setStatus("current")


class _VRtrOspfStatus_Type(TmnxStatus):
    """Custom type vRtrOspfStatus based on TmnxStatus"""
    defaultValue = 2


_VRtrOspfStatus_Type.__name__ = "TmnxStatus"
_VRtrOspfStatus_Object = MibTableColumn
vRtrOspfStatus = _VRtrOspfStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 8),
    _VRtrOspfStatus_Type()
)
vRtrOspfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfStatus.setStatus("obsolete")


class _VRtrRipStatus_Type(TmnxStatus):
    """Custom type vRtrRipStatus based on TmnxStatus"""
    defaultValue = 2


_VRtrRipStatus_Type.__name__ = "TmnxStatus"
_VRtrRipStatus_Object = MibTableColumn
vRtrRipStatus = _VRtrRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 9),
    _VRtrRipStatus_Type()
)
vRtrRipStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipStatus.setStatus("current")


class _VRtrRsvpStatus_Type(TmnxStatus):
    """Custom type vRtrRsvpStatus based on TmnxStatus"""
    defaultValue = 2


_VRtrRsvpStatus_Type.__name__ = "TmnxStatus"
_VRtrRsvpStatus_Object = MibTableColumn
vRtrRsvpStatus = _VRtrRsvpStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 10),
    _VRtrRsvpStatus_Type()
)
vRtrRsvpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpStatus.setStatus("current")


class _VRtrEcmpMaxRoutes_Type(Unsigned32):
    """Custom type vRtrEcmpMaxRoutes based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VRtrEcmpMaxRoutes_Type.__name__ = "Unsigned32"
_VRtrEcmpMaxRoutes_Object = MibTableColumn
vRtrEcmpMaxRoutes = _VRtrEcmpMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 11),
    _VRtrEcmpMaxRoutes_Type()
)
vRtrEcmpMaxRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrEcmpMaxRoutes.setStatus("current")


class _VRtrAS_Type(TmnxBgpAutonomousSystem):
    """Custom type vRtrAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_VRtrAS_Type.__name__ = "TmnxBgpAutonomousSystem"
_VRtrAS_Object = MibTableColumn
vRtrAS = _VRtrAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 12),
    _VRtrAS_Type()
)
vRtrAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAS.setStatus("obsolete")
_VRtrNewIfIndex_Type = TestAndIncr
_VRtrNewIfIndex_Object = MibTableColumn
vRtrNewIfIndex = _VRtrNewIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 13),
    _VRtrNewIfIndex_Type()
)
vRtrNewIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrNewIfIndex.setStatus("current")


class _VRtrLdpStatus_Type(TmnxStatus):
    """Custom type vRtrLdpStatus based on TmnxStatus"""
    defaultValue = 2


_VRtrLdpStatus_Type.__name__ = "TmnxStatus"
_VRtrLdpStatus_Object = MibTableColumn
vRtrLdpStatus = _VRtrLdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 14),
    _VRtrLdpStatus_Type()
)
vRtrLdpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStatus.setStatus("current")


class _VRtrIsIsStatus_Type(TmnxStatus):
    """Custom type vRtrIsIsStatus based on TmnxStatus"""
    defaultValue = 2


_VRtrIsIsStatus_Type.__name__ = "TmnxStatus"
_VRtrIsIsStatus_Object = MibTableColumn
vRtrIsIsStatus = _VRtrIsIsStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 15),
    _VRtrIsIsStatus_Type()
)
vRtrIsIsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsIsStatus.setStatus("obsolete")
_VRtrRouterId_Type = IpAddress
_VRtrRouterId_Object = MibTableColumn
vRtrRouterId = _VRtrRouterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 16),
    _VRtrRouterId_Type()
)
vRtrRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRouterId.setStatus("current")


class _VRtrTriggeredPolicy_Type(TruthValue):
    """Custom type vRtrTriggeredPolicy based on TruthValue"""
    defaultValue = 2


_VRtrTriggeredPolicy_Type.__name__ = "TruthValue"
_VRtrTriggeredPolicy_Object = MibTableColumn
vRtrTriggeredPolicy = _VRtrTriggeredPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 17),
    _VRtrTriggeredPolicy_Type()
)
vRtrTriggeredPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTriggeredPolicy.setStatus("current")


class _VRtrConfederationAS_Type(TmnxBgpAutonomousSystem):
    """Custom type vRtrConfederationAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_VRtrConfederationAS_Type.__name__ = "TmnxBgpAutonomousSystem"
_VRtrConfederationAS_Object = MibTableColumn
vRtrConfederationAS = _VRtrConfederationAS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 18),
    _VRtrConfederationAS_Type()
)
vRtrConfederationAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrConfederationAS.setStatus("obsolete")


class _VRtrRouteDistinguisher_Type(TmnxVPNRouteDistinguisher):
    """Custom type vRtrRouteDistinguisher based on TmnxVPNRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_VRtrRouteDistinguisher_Type.__name__ = "TmnxVPNRouteDistinguisher"
_VRtrRouteDistinguisher_Object = MibTableColumn
vRtrRouteDistinguisher = _VRtrRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 19),
    _VRtrRouteDistinguisher_Type()
)
vRtrRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRouteDistinguisher.setStatus("current")


class _VRtrMidRouteThreshold_Type(Unsigned32):
    """Custom type vRtrMidRouteThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMidRouteThreshold_Type.__name__ = "Unsigned32"
_VRtrMidRouteThreshold_Object = MibTableColumn
vRtrMidRouteThreshold = _VRtrMidRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 20),
    _VRtrMidRouteThreshold_Type()
)
vRtrMidRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMidRouteThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMidRouteThreshold.setUnits("percent")


class _VRtrHighRouteThreshold_Type(Unsigned32):
    """Custom type vRtrHighRouteThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrHighRouteThreshold_Type.__name__ = "Unsigned32"
_VRtrHighRouteThreshold_Object = MibTableColumn
vRtrHighRouteThreshold = _VRtrHighRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 21),
    _VRtrHighRouteThreshold_Type()
)
vRtrHighRouteThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrHighRouteThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrHighRouteThreshold.setUnits("percent")


class _VRtrIllegalLabelThreshold_Type(Unsigned32):
    """Custom type vRtrIllegalLabelThreshold based on Unsigned32"""
    defaultValue = 0


_VRtrIllegalLabelThreshold_Type.__name__ = "Unsigned32"
_VRtrIllegalLabelThreshold_Object = MibTableColumn
vRtrIllegalLabelThreshold = _VRtrIllegalLabelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 22),
    _VRtrIllegalLabelThreshold_Type()
)
vRtrIllegalLabelThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIllegalLabelThreshold.setStatus("current")


class _VRtrVpnId_Type(TmnxVPNId):
    """Custom type vRtrVpnId based on TmnxVPNId"""
    defaultHexValue = ""


_VRtrVpnId_Type.__name__ = "TmnxVPNId"
_VRtrVpnId_Object = MibTableColumn
vRtrVpnId = _VRtrVpnId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 23),
    _VRtrVpnId_Type()
)
vRtrVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrVpnId.setStatus("current")


class _VRtrDescription_Type(TItemDescription):
    """Custom type vRtrDescription based on TItemDescription"""
    defaultHexValue = ""


_VRtrDescription_Type.__name__ = "TItemDescription"
_VRtrDescription_Object = MibTableColumn
vRtrDescription = _VRtrDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 25),
    _VRtrDescription_Type()
)
vRtrDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrDescription.setStatus("current")


class _VRtrGracefulRestart_Type(TruthValue):
    """Custom type vRtrGracefulRestart based on TruthValue"""
    defaultValue = 2


_VRtrGracefulRestart_Type.__name__ = "TruthValue"
_VRtrGracefulRestart_Object = MibTableColumn
vRtrGracefulRestart = _VRtrGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 26),
    _VRtrGracefulRestart_Type()
)
vRtrGracefulRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGracefulRestart.setStatus("current")


class _VRtrGracefulRestartType_Type(Integer32):
    """Custom type vRtrGracefulRestartType based on Integer32"""
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
        *(("never", 0),
          ("manual", 1),
          ("automatic", 2))
    )


_VRtrGracefulRestartType_Type.__name__ = "Integer32"
_VRtrGracefulRestartType_Object = MibTableColumn
vRtrGracefulRestartType = _VRtrGracefulRestartType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 27),
    _VRtrGracefulRestartType_Type()
)
vRtrGracefulRestartType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGracefulRestartType.setStatus("current")


class _VRtrType_Type(Integer32):
    """Custom type vRtrType based on Integer32"""
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
        *(("unknown", 0),
          ("baseRouter", 1),
          ("vprn", 2),
          ("vr", 3))
    )


_VRtrType_Type.__name__ = "Integer32"
_VRtrType_Object = MibTableColumn
vRtrType = _VRtrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 28),
    _VRtrType_Type()
)
vRtrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrType.setStatus("current")
_VRtrServiceId_Type = TmnxServId
_VRtrServiceId_Object = MibTableColumn
vRtrServiceId = _VRtrServiceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 29),
    _VRtrServiceId_Type()
)
vRtrServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrServiceId.setStatus("current")
_VRtrCustId_Type = TmnxCustId
_VRtrCustId_Object = MibTableColumn
vRtrCustId = _VRtrCustId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 30),
    _VRtrCustId_Type()
)
vRtrCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrCustId.setStatus("current")


class _VRtrIgmpStatus_Type(TmnxStatus):
    """Custom type vRtrIgmpStatus based on TmnxStatus"""
    defaultValue = 2


_VRtrIgmpStatus_Type.__name__ = "TmnxStatus"
_VRtrIgmpStatus_Object = MibTableColumn
vRtrIgmpStatus = _VRtrIgmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 31),
    _VRtrIgmpStatus_Type()
)
vRtrIgmpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpStatus.setStatus("current")


class _VRtrMaxNumRoutesLogOnly_Type(TruthValue):
    """Custom type vRtrMaxNumRoutesLogOnly based on TruthValue"""
    defaultValue = 2


_VRtrMaxNumRoutesLogOnly_Type.__name__ = "TruthValue"
_VRtrMaxNumRoutesLogOnly_Object = MibTableColumn
vRtrMaxNumRoutesLogOnly = _VRtrMaxNumRoutesLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 32),
    _VRtrMaxNumRoutesLogOnly_Type()
)
vRtrMaxNumRoutesLogOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMaxNumRoutesLogOnly.setStatus("current")
_VRtrVrfTarget_Type = TNamedItemOrEmpty
_VRtrVrfTarget_Object = MibTableColumn
vRtrVrfTarget = _VRtrVrfTarget_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 33),
    _VRtrVrfTarget_Type()
)
vRtrVrfTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrVrfTarget.setStatus("current")
_VRtrVrfExportTarget_Type = TNamedItemOrEmpty
_VRtrVrfExportTarget_Object = MibTableColumn
vRtrVrfExportTarget = _VRtrVrfExportTarget_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 34),
    _VRtrVrfExportTarget_Type()
)
vRtrVrfExportTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrVrfExportTarget.setStatus("current")
_VRtrVrfImportTarget_Type = TNamedItemOrEmpty
_VRtrVrfImportTarget_Object = MibTableColumn
vRtrVrfImportTarget = _VRtrVrfImportTarget_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 35),
    _VRtrVrfImportTarget_Type()
)
vRtrVrfImportTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrVrfImportTarget.setStatus("current")


class _VRtrPimStatus_Type(TmnxStatus):
    """Custom type vRtrPimStatus based on TmnxStatus"""
    defaultValue = 2


_VRtrPimStatus_Type.__name__ = "TmnxStatus"
_VRtrPimStatus_Object = MibTableColumn
vRtrPimStatus = _VRtrPimStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 36),
    _VRtrPimStatus_Type()
)
vRtrPimStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimStatus.setStatus("current")


class _VRtrMaxMcastNumRoutes_Type(Integer32):
    """Custom type vRtrMaxMcastNumRoutes based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_VRtrMaxMcastNumRoutes_Type.__name__ = "Integer32"
_VRtrMaxMcastNumRoutes_Object = MibTableColumn
vRtrMaxMcastNumRoutes = _VRtrMaxMcastNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 37),
    _VRtrMaxMcastNumRoutes_Type()
)
vRtrMaxMcastNumRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMaxMcastNumRoutes.setStatus("current")


class _VRtrMaxMcastNumRoutesLogOnly_Type(TruthValue):
    """Custom type vRtrMaxMcastNumRoutesLogOnly based on TruthValue"""
    defaultValue = 2


_VRtrMaxMcastNumRoutesLogOnly_Type.__name__ = "TruthValue"
_VRtrMaxMcastNumRoutesLogOnly_Object = MibTableColumn
vRtrMaxMcastNumRoutesLogOnly = _VRtrMaxMcastNumRoutesLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 38),
    _VRtrMaxMcastNumRoutesLogOnly_Type()
)
vRtrMaxMcastNumRoutesLogOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMaxMcastNumRoutesLogOnly.setStatus("current")


class _VRtrMcastMidRouteThreshold_Type(Unsigned32):
    """Custom type vRtrMcastMidRouteThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMcastMidRouteThreshold_Type.__name__ = "Unsigned32"
_VRtrMcastMidRouteThreshold_Object = MibTableColumn
vRtrMcastMidRouteThreshold = _VRtrMcastMidRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 39),
    _VRtrMcastMidRouteThreshold_Type()
)
vRtrMcastMidRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMcastMidRouteThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMcastMidRouteThreshold.setUnits("percent")


class _VRtrIgnoreIcmpRedirect_Type(TruthValue):
    """Custom type vRtrIgnoreIcmpRedirect based on TruthValue"""
    defaultValue = 1


_VRtrIgnoreIcmpRedirect_Type.__name__ = "TruthValue"
_VRtrIgnoreIcmpRedirect_Object = MibTableColumn
vRtrIgnoreIcmpRedirect = _VRtrIgnoreIcmpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 40),
    _VRtrIgnoreIcmpRedirect_Type()
)
vRtrIgnoreIcmpRedirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgnoreIcmpRedirect.setStatus("current")


class _VRtrOspfv3Status_Type(TmnxStatus):
    """Custom type vRtrOspfv3Status based on TmnxStatus"""
    defaultValue = 2


_VRtrOspfv3Status_Type.__name__ = "TmnxStatus"
_VRtrOspfv3Status_Object = MibTableColumn
vRtrOspfv3Status = _VRtrOspfv3Status_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 41),
    _VRtrOspfv3Status_Type()
)
vRtrOspfv3Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfv3Status.setStatus("obsolete")


class _VRtrMsdpStatus_Type(TmnxStatus):
    """Custom type vRtrMsdpStatus based on TmnxStatus"""
    defaultValue = 2


_VRtrMsdpStatus_Type.__name__ = "TmnxStatus"
_VRtrMsdpStatus_Object = MibTableColumn
vRtrMsdpStatus = _VRtrMsdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 42),
    _VRtrMsdpStatus_Type()
)
vRtrMsdpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMsdpStatus.setStatus("current")


class _VRtrVprnType_Type(Integer32):
    """Custom type vRtrVprnType based on Integer32"""
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
        *(("regular", 1),
          ("hub", 2),
          ("spoke", 3),
          ("subscriberSplitHorizon", 4))
    )


_VRtrVprnType_Type.__name__ = "Integer32"
_VRtrVprnType_Object = MibTableColumn
vRtrVprnType = _VRtrVprnType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 43),
    _VRtrVprnType_Type()
)
vRtrVprnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrVprnType.setStatus("current")
_VRtrSecondaryVrfId_Type = TmnxVRtrIDOrZero
_VRtrSecondaryVrfId_Object = MibTableColumn
vRtrSecondaryVrfId = _VRtrSecondaryVrfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 44),
    _VRtrSecondaryVrfId_Type()
)
vRtrSecondaryVrfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSecondaryVrfId.setStatus("current")


class _VRtrMldStatus_Type(TmnxStatus):
    """Custom type vRtrMldStatus based on TmnxStatus"""
    defaultValue = 2


_VRtrMldStatus_Type.__name__ = "TmnxStatus"
_VRtrMldStatus_Object = MibTableColumn
vRtrMldStatus = _VRtrMldStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 45),
    _VRtrMldStatus_Type()
)
vRtrMldStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldStatus.setStatus("current")


class _VRtrIPv6MaxNumRoutes_Type(Integer32):
    """Custom type vRtrIPv6MaxNumRoutes based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_VRtrIPv6MaxNumRoutes_Type.__name__ = "Integer32"
_VRtrIPv6MaxNumRoutes_Object = MibTableColumn
vRtrIPv6MaxNumRoutes = _VRtrIPv6MaxNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 46),
    _VRtrIPv6MaxNumRoutes_Type()
)
vRtrIPv6MaxNumRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIPv6MaxNumRoutes.setStatus("current")


class _VRtrIPv6MidRouteThreshold_Type(Unsigned32):
    """Custom type vRtrIPv6MidRouteThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrIPv6MidRouteThreshold_Type.__name__ = "Unsigned32"
_VRtrIPv6MidRouteThreshold_Object = MibTableColumn
vRtrIPv6MidRouteThreshold = _VRtrIPv6MidRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 47),
    _VRtrIPv6MidRouteThreshold_Type()
)
vRtrIPv6MidRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIPv6MidRouteThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIPv6MidRouteThreshold.setUnits("percent")


class _VRtrIPv6HighRouteThreshold_Type(Unsigned32):
    """Custom type vRtrIPv6HighRouteThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrIPv6HighRouteThreshold_Type.__name__ = "Unsigned32"
_VRtrIPv6HighRouteThreshold_Object = MibTableColumn
vRtrIPv6HighRouteThreshold = _VRtrIPv6HighRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 48),
    _VRtrIPv6HighRouteThreshold_Type()
)
vRtrIPv6HighRouteThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIPv6HighRouteThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIPv6HighRouteThreshold.setUnits("percent")


class _VRtrIPv6MaxNumRoutesLogOnly_Type(TruthValue):
    """Custom type vRtrIPv6MaxNumRoutesLogOnly based on TruthValue"""
    defaultValue = 2


_VRtrIPv6MaxNumRoutesLogOnly_Type.__name__ = "TruthValue"
_VRtrIPv6MaxNumRoutesLogOnly_Object = MibTableColumn
vRtrIPv6MaxNumRoutesLogOnly = _VRtrIPv6MaxNumRoutesLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 49),
    _VRtrIPv6MaxNumRoutesLogOnly_Type()
)
vRtrIPv6MaxNumRoutesLogOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIPv6MaxNumRoutesLogOnly.setStatus("current")


class _VRtrIPv6IgnoreIcmpRedirect_Type(TruthValue):
    """Custom type vRtrIPv6IgnoreIcmpRedirect based on TruthValue"""
    defaultValue = 1


_VRtrIPv6IgnoreIcmpRedirect_Type.__name__ = "TruthValue"
_VRtrIPv6IgnoreIcmpRedirect_Object = MibTableColumn
vRtrIPv6IgnoreIcmpRedirect = _VRtrIPv6IgnoreIcmpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 50),
    _VRtrIPv6IgnoreIcmpRedirect_Type()
)
vRtrIPv6IgnoreIcmpRedirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIPv6IgnoreIcmpRedirect.setStatus("current")


class _VRtrMcPathMgmtPlcyName_Type(TNamedItem):
    """Custom type vRtrMcPathMgmtPlcyName based on TNamedItem"""
    defaultValue = OctetString("default")


_VRtrMcPathMgmtPlcyName_Type.__name__ = "TNamedItem"
_VRtrMcPathMgmtPlcyName_Object = MibTableColumn
vRtrMcPathMgmtPlcyName = _VRtrMcPathMgmtPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 51),
    _VRtrMcPathMgmtPlcyName_Type()
)
vRtrMcPathMgmtPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMcPathMgmtPlcyName.setStatus("current")


class _VRtrIgnoreNextHopMetric_Type(TruthValue):
    """Custom type vRtrIgnoreNextHopMetric based on TruthValue"""
    defaultValue = 2


_VRtrIgnoreNextHopMetric_Type.__name__ = "TruthValue"
_VRtrIgnoreNextHopMetric_Object = MibTableColumn
vRtrIgnoreNextHopMetric = _VRtrIgnoreNextHopMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 52),
    _VRtrIgnoreNextHopMetric_Type()
)
vRtrIgnoreNextHopMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgnoreNextHopMetric.setStatus("current")


class _VRtrMvpnVrfTarget_Type(TNamedItemOrEmpty):
    """Custom type vRtrMvpnVrfTarget based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrMvpnVrfTarget_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMvpnVrfTarget_Object = MibTableColumn
vRtrMvpnVrfTarget = _VRtrMvpnVrfTarget_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 53),
    _VRtrMvpnVrfTarget_Type()
)
vRtrMvpnVrfTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMvpnVrfTarget.setStatus("current")


class _VRtrMvpnVrfExportTarget_Type(TNamedItemOrEmpty):
    """Custom type vRtrMvpnVrfExportTarget based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrMvpnVrfExportTarget_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMvpnVrfExportTarget_Object = MibTableColumn
vRtrMvpnVrfExportTarget = _VRtrMvpnVrfExportTarget_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 54),
    _VRtrMvpnVrfExportTarget_Type()
)
vRtrMvpnVrfExportTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMvpnVrfExportTarget.setStatus("current")


class _VRtrMvpnVrfImportTarget_Type(TNamedItemOrEmpty):
    """Custom type vRtrMvpnVrfImportTarget based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrMvpnVrfImportTarget_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMvpnVrfImportTarget_Object = MibTableColumn
vRtrMvpnVrfImportTarget = _VRtrMvpnVrfImportTarget_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 55),
    _VRtrMvpnVrfImportTarget_Type()
)
vRtrMvpnVrfImportTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMvpnVrfImportTarget.setStatus("current")


class _VRtrMvpnVrfTargetUnicast_Type(TruthValue):
    """Custom type vRtrMvpnVrfTargetUnicast based on TruthValue"""
    defaultValue = 2


_VRtrMvpnVrfTargetUnicast_Type.__name__ = "TruthValue"
_VRtrMvpnVrfTargetUnicast_Object = MibTableColumn
vRtrMvpnVrfTargetUnicast = _VRtrMvpnVrfTargetUnicast_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 56),
    _VRtrMvpnVrfTargetUnicast_Type()
)
vRtrMvpnVrfTargetUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMvpnVrfTargetUnicast.setStatus("current")


class _VRtrMvpnVrfExportTargetUnicast_Type(TruthValue):
    """Custom type vRtrMvpnVrfExportTargetUnicast based on TruthValue"""
    defaultValue = 2


_VRtrMvpnVrfExportTargetUnicast_Type.__name__ = "TruthValue"
_VRtrMvpnVrfExportTargetUnicast_Object = MibTableColumn
vRtrMvpnVrfExportTargetUnicast = _VRtrMvpnVrfExportTargetUnicast_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 57),
    _VRtrMvpnVrfExportTargetUnicast_Type()
)
vRtrMvpnVrfExportTargetUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMvpnVrfExportTargetUnicast.setStatus("current")


class _VRtrMvpnVrfImportTargetUnicast_Type(TruthValue):
    """Custom type vRtrMvpnVrfImportTargetUnicast based on TruthValue"""
    defaultValue = 2


_VRtrMvpnVrfImportTargetUnicast_Type.__name__ = "TruthValue"
_VRtrMvpnVrfImportTargetUnicast_Object = MibTableColumn
vRtrMvpnVrfImportTargetUnicast = _VRtrMvpnVrfImportTargetUnicast_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 58),
    _VRtrMvpnVrfImportTargetUnicast_Type()
)
vRtrMvpnVrfImportTargetUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMvpnVrfImportTargetUnicast.setStatus("current")


class _VRtrAS4Byte_Type(InetAutonomousSystemNumber):
    """Custom type vRtrAS4Byte based on InetAutonomousSystemNumber"""
    defaultValue = 0


_VRtrAS4Byte_Type.__name__ = "InetAutonomousSystemNumber"
_VRtrAS4Byte_Object = MibTableColumn
vRtrAS4Byte = _VRtrAS4Byte_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 59),
    _VRtrAS4Byte_Type()
)
vRtrAS4Byte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAS4Byte.setStatus("current")


class _VRtrConfederationAS4Byte_Type(InetAutonomousSystemNumber):
    """Custom type vRtrConfederationAS4Byte based on InetAutonomousSystemNumber"""
    defaultValue = 0


_VRtrConfederationAS4Byte_Type.__name__ = "InetAutonomousSystemNumber"
_VRtrConfederationAS4Byte_Object = MibTableColumn
vRtrConfederationAS4Byte = _VRtrConfederationAS4Byte_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 60),
    _VRtrConfederationAS4Byte_Type()
)
vRtrConfederationAS4Byte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrConfederationAS4Byte.setStatus("current")


class _VRtrMvpnCMcastImportRT_Type(TNamedItemOrEmpty):
    """Custom type vRtrMvpnCMcastImportRT based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrMvpnCMcastImportRT_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMvpnCMcastImportRT_Object = MibTableColumn
vRtrMvpnCMcastImportRT = _VRtrMvpnCMcastImportRT_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 61),
    _VRtrMvpnCMcastImportRT_Type()
)
vRtrMvpnCMcastImportRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMvpnCMcastImportRT.setStatus("current")
_VRtrInterASMvpn_Type = TruthValue
_VRtrInterASMvpn_Object = MibTableColumn
vRtrInterASMvpn = _VRtrInterASMvpn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 1, 1, 64),
    _VRtrInterASMvpn_Type()
)
vRtrInterASMvpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInterASMvpn.setStatus("current")
_VRtrStatTable_Object = MibTable
vRtrStatTable = _VRtrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    vRtrStatTable.setStatus("current")
_VRtrStatEntry_Object = MibTableRow
vRtrStatEntry = _VRtrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrStatEntry.setStatus("current")
_VRtrOperState_Type = TmnxOperState
_VRtrOperState_Object = MibTableColumn
vRtrOperState = _VRtrOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 1),
    _VRtrOperState_Type()
)
vRtrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOperState.setStatus("current")
_VRtrDirectRoutes_Type = Gauge32
_VRtrDirectRoutes_Object = MibTableColumn
vRtrDirectRoutes = _VRtrDirectRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 2),
    _VRtrDirectRoutes_Type()
)
vRtrDirectRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrDirectRoutes.setStatus("current")
_VRtrDirectActiveRoutes_Type = Gauge32
_VRtrDirectActiveRoutes_Object = MibTableColumn
vRtrDirectActiveRoutes = _VRtrDirectActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 3),
    _VRtrDirectActiveRoutes_Type()
)
vRtrDirectActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrDirectActiveRoutes.setStatus("current")
_VRtrStaticRoutes_Type = Gauge32
_VRtrStaticRoutes_Object = MibTableColumn
vRtrStaticRoutes = _VRtrStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 4),
    _VRtrStaticRoutes_Type()
)
vRtrStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticRoutes.setStatus("current")
_VRtrStaticActiveRoutes_Type = Gauge32
_VRtrStaticActiveRoutes_Object = MibTableColumn
vRtrStaticActiveRoutes = _VRtrStaticActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 5),
    _VRtrStaticActiveRoutes_Type()
)
vRtrStaticActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticActiveRoutes.setStatus("current")
_VRtrOSPFRoutes_Type = Gauge32
_VRtrOSPFRoutes_Object = MibTableColumn
vRtrOSPFRoutes = _VRtrOSPFRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 6),
    _VRtrOSPFRoutes_Type()
)
vRtrOSPFRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOSPFRoutes.setStatus("current")
_VRtrOSPFActiveRoutes_Type = Gauge32
_VRtrOSPFActiveRoutes_Object = MibTableColumn
vRtrOSPFActiveRoutes = _VRtrOSPFActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 7),
    _VRtrOSPFActiveRoutes_Type()
)
vRtrOSPFActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOSPFActiveRoutes.setStatus("current")
_VRtrBGPRoutes_Type = Gauge32
_VRtrBGPRoutes_Object = MibTableColumn
vRtrBGPRoutes = _VRtrBGPRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 8),
    _VRtrBGPRoutes_Type()
)
vRtrBGPRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBGPRoutes.setStatus("current")
_VRtrBGPActiveRoutes_Type = Gauge32
_VRtrBGPActiveRoutes_Object = MibTableColumn
vRtrBGPActiveRoutes = _VRtrBGPActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 9),
    _VRtrBGPActiveRoutes_Type()
)
vRtrBGPActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBGPActiveRoutes.setStatus("current")
_VRtrISISRoutes_Type = Gauge32
_VRtrISISRoutes_Object = MibTableColumn
vRtrISISRoutes = _VRtrISISRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 10),
    _VRtrISISRoutes_Type()
)
vRtrISISRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrISISRoutes.setStatus("current")
_VRtrISISActiveRoutes_Type = Gauge32
_VRtrISISActiveRoutes_Object = MibTableColumn
vRtrISISActiveRoutes = _VRtrISISActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 11),
    _VRtrISISActiveRoutes_Type()
)
vRtrISISActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrISISActiveRoutes.setStatus("current")
_VRtrRIPRoutes_Type = Gauge32
_VRtrRIPRoutes_Object = MibTableColumn
vRtrRIPRoutes = _VRtrRIPRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 12),
    _VRtrRIPRoutes_Type()
)
vRtrRIPRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRIPRoutes.setStatus("current")
_VRtrRIPActiveRoutes_Type = Gauge32
_VRtrRIPActiveRoutes_Object = MibTableColumn
vRtrRIPActiveRoutes = _VRtrRIPActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 13),
    _VRtrRIPActiveRoutes_Type()
)
vRtrRIPActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRIPActiveRoutes.setStatus("current")
_VRtrAggregateRoutes_Type = Gauge32
_VRtrAggregateRoutes_Object = MibTableColumn
vRtrAggregateRoutes = _VRtrAggregateRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 14),
    _VRtrAggregateRoutes_Type()
)
vRtrAggregateRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrAggregateRoutes.setStatus("current")
_VRtrAggregateActiveRoutes_Type = Gauge32
_VRtrAggregateActiveRoutes_Object = MibTableColumn
vRtrAggregateActiveRoutes = _VRtrAggregateActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 15),
    _VRtrAggregateActiveRoutes_Type()
)
vRtrAggregateActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrAggregateActiveRoutes.setStatus("current")
_VRtrStatConfiguredIfs_Type = Gauge32
_VRtrStatConfiguredIfs_Object = MibTableColumn
vRtrStatConfiguredIfs = _VRtrStatConfiguredIfs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 16),
    _VRtrStatConfiguredIfs_Type()
)
vRtrStatConfiguredIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatConfiguredIfs.setStatus("current")
_VRtrStatActiveIfs_Type = Gauge32
_VRtrStatActiveIfs_Object = MibTableColumn
vRtrStatActiveIfs = _VRtrStatActiveIfs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 17),
    _VRtrStatActiveIfs_Type()
)
vRtrStatActiveIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatActiveIfs.setStatus("current")
_VRtrStatIllegalLabels_Type = Counter32
_VRtrStatIllegalLabels_Object = MibTableColumn
vRtrStatIllegalLabels = _VRtrStatIllegalLabels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 18),
    _VRtrStatIllegalLabels_Type()
)
vRtrStatIllegalLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatIllegalLabels.setStatus("current")
_VRtrStatCurrNumRoutes_Type = Gauge32
_VRtrStatCurrNumRoutes_Object = MibTableColumn
vRtrStatCurrNumRoutes = _VRtrStatCurrNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 19),
    _VRtrStatCurrNumRoutes_Type()
)
vRtrStatCurrNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatCurrNumRoutes.setStatus("current")
_VRtrStatBGPVpnRoutes_Type = Gauge32
_VRtrStatBGPVpnRoutes_Object = MibTableColumn
vRtrStatBGPVpnRoutes = _VRtrStatBGPVpnRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 20),
    _VRtrStatBGPVpnRoutes_Type()
)
vRtrStatBGPVpnRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatBGPVpnRoutes.setStatus("current")
_VRtrStatBGPVpnActiveRoutes_Type = Gauge32
_VRtrStatBGPVpnActiveRoutes_Object = MibTableColumn
vRtrStatBGPVpnActiveRoutes = _VRtrStatBGPVpnActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 21),
    _VRtrStatBGPVpnActiveRoutes_Type()
)
vRtrStatBGPVpnActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatBGPVpnActiveRoutes.setStatus("current")
_VRtrStatTotalLdpTunnels_Type = Gauge32
_VRtrStatTotalLdpTunnels_Object = MibTableColumn
vRtrStatTotalLdpTunnels = _VRtrStatTotalLdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 22),
    _VRtrStatTotalLdpTunnels_Type()
)
vRtrStatTotalLdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatTotalLdpTunnels.setStatus("current")
_VRtrStatTotalSdpTunnels_Type = Gauge32
_VRtrStatTotalSdpTunnels_Object = MibTableColumn
vRtrStatTotalSdpTunnels = _VRtrStatTotalSdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 23),
    _VRtrStatTotalSdpTunnels_Type()
)
vRtrStatTotalSdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatTotalSdpTunnels.setStatus("current")
_VRtrStatActiveLdpTunnels_Type = Gauge32
_VRtrStatActiveLdpTunnels_Object = MibTableColumn
vRtrStatActiveLdpTunnels = _VRtrStatActiveLdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 24),
    _VRtrStatActiveLdpTunnels_Type()
)
vRtrStatActiveLdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatActiveLdpTunnels.setStatus("current")
_VRtrStatActiveSdpTunnels_Type = Gauge32
_VRtrStatActiveSdpTunnels_Object = MibTableColumn
vRtrStatActiveSdpTunnels = _VRtrStatActiveSdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 25),
    _VRtrStatActiveSdpTunnels_Type()
)
vRtrStatActiveSdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatActiveSdpTunnels.setStatus("current")
_VRtrMulticastRoutes_Type = Gauge32
_VRtrMulticastRoutes_Object = MibTableColumn
vRtrMulticastRoutes = _VRtrMulticastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 26),
    _VRtrMulticastRoutes_Type()
)
vRtrMulticastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMulticastRoutes.setStatus("current")
_VRtrStatActiveARPEntries_Type = Gauge32
_VRtrStatActiveARPEntries_Object = MibTableColumn
vRtrStatActiveARPEntries = _VRtrStatActiveARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 27),
    _VRtrStatActiveARPEntries_Type()
)
vRtrStatActiveARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatActiveARPEntries.setStatus("current")
_VRtrStatTotalARPEntries_Type = Gauge32
_VRtrStatTotalARPEntries_Object = MibTableColumn
vRtrStatTotalARPEntries = _VRtrStatTotalARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 28),
    _VRtrStatTotalARPEntries_Type()
)
vRtrStatTotalARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatTotalARPEntries.setStatus("current")
_VRtrV6DirectRoutes_Type = Gauge32
_VRtrV6DirectRoutes_Object = MibTableColumn
vRtrV6DirectRoutes = _VRtrV6DirectRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 29),
    _VRtrV6DirectRoutes_Type()
)
vRtrV6DirectRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6DirectRoutes.setStatus("current")
_VRtrV6DirectActiveRoutes_Type = Gauge32
_VRtrV6DirectActiveRoutes_Object = MibTableColumn
vRtrV6DirectActiveRoutes = _VRtrV6DirectActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 30),
    _VRtrV6DirectActiveRoutes_Type()
)
vRtrV6DirectActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6DirectActiveRoutes.setStatus("current")
_VRtrV6StaticRoutes_Type = Gauge32
_VRtrV6StaticRoutes_Object = MibTableColumn
vRtrV6StaticRoutes = _VRtrV6StaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 31),
    _VRtrV6StaticRoutes_Type()
)
vRtrV6StaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StaticRoutes.setStatus("current")
_VRtrV6StaticActiveRoutes_Type = Gauge32
_VRtrV6StaticActiveRoutes_Object = MibTableColumn
vRtrV6StaticActiveRoutes = _VRtrV6StaticActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 32),
    _VRtrV6StaticActiveRoutes_Type()
)
vRtrV6StaticActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StaticActiveRoutes.setStatus("current")
_VRtrV6OSPFRoutes_Type = Gauge32
_VRtrV6OSPFRoutes_Object = MibTableColumn
vRtrV6OSPFRoutes = _VRtrV6OSPFRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 33),
    _VRtrV6OSPFRoutes_Type()
)
vRtrV6OSPFRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6OSPFRoutes.setStatus("current")
_VRtrV6OSPFActiveRoutes_Type = Gauge32
_VRtrV6OSPFActiveRoutes_Object = MibTableColumn
vRtrV6OSPFActiveRoutes = _VRtrV6OSPFActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 34),
    _VRtrV6OSPFActiveRoutes_Type()
)
vRtrV6OSPFActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6OSPFActiveRoutes.setStatus("current")
_VRtrV6BGPRoutes_Type = Gauge32
_VRtrV6BGPRoutes_Object = MibTableColumn
vRtrV6BGPRoutes = _VRtrV6BGPRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 35),
    _VRtrV6BGPRoutes_Type()
)
vRtrV6BGPRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6BGPRoutes.setStatus("current")
_VRtrV6BGPActiveRoutes_Type = Gauge32
_VRtrV6BGPActiveRoutes_Object = MibTableColumn
vRtrV6BGPActiveRoutes = _VRtrV6BGPActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 36),
    _VRtrV6BGPActiveRoutes_Type()
)
vRtrV6BGPActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6BGPActiveRoutes.setStatus("current")
_VRtrV6ISISRoutes_Type = Gauge32
_VRtrV6ISISRoutes_Object = MibTableColumn
vRtrV6ISISRoutes = _VRtrV6ISISRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 37),
    _VRtrV6ISISRoutes_Type()
)
vRtrV6ISISRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6ISISRoutes.setStatus("current")
_VRtrV6ISISActiveRoutes_Type = Gauge32
_VRtrV6ISISActiveRoutes_Object = MibTableColumn
vRtrV6ISISActiveRoutes = _VRtrV6ISISActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 38),
    _VRtrV6ISISActiveRoutes_Type()
)
vRtrV6ISISActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6ISISActiveRoutes.setStatus("current")
_VRtrV6RIPRoutes_Type = Gauge32
_VRtrV6RIPRoutes_Object = MibTableColumn
vRtrV6RIPRoutes = _VRtrV6RIPRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 39),
    _VRtrV6RIPRoutes_Type()
)
vRtrV6RIPRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6RIPRoutes.setStatus("current")
_VRtrV6RIPActiveRoutes_Type = Gauge32
_VRtrV6RIPActiveRoutes_Object = MibTableColumn
vRtrV6RIPActiveRoutes = _VRtrV6RIPActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 40),
    _VRtrV6RIPActiveRoutes_Type()
)
vRtrV6RIPActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6RIPActiveRoutes.setStatus("current")
_VRtrV6AggregateRoutes_Type = Gauge32
_VRtrV6AggregateRoutes_Object = MibTableColumn
vRtrV6AggregateRoutes = _VRtrV6AggregateRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 41),
    _VRtrV6AggregateRoutes_Type()
)
vRtrV6AggregateRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6AggregateRoutes.setStatus("current")
_VRtrV6AggregateActiveRoutes_Type = Gauge32
_VRtrV6AggregateActiveRoutes_Object = MibTableColumn
vRtrV6AggregateActiveRoutes = _VRtrV6AggregateActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 42),
    _VRtrV6AggregateActiveRoutes_Type()
)
vRtrV6AggregateActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6AggregateActiveRoutes.setStatus("current")
_VRtrV6StatConfiguredIfs_Type = Gauge32
_VRtrV6StatConfiguredIfs_Object = MibTableColumn
vRtrV6StatConfiguredIfs = _VRtrV6StatConfiguredIfs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 43),
    _VRtrV6StatConfiguredIfs_Type()
)
vRtrV6StatConfiguredIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatConfiguredIfs.setStatus("current")
_VRtrV6StatActiveIfs_Type = Gauge32
_VRtrV6StatActiveIfs_Object = MibTableColumn
vRtrV6StatActiveIfs = _VRtrV6StatActiveIfs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 44),
    _VRtrV6StatActiveIfs_Type()
)
vRtrV6StatActiveIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatActiveIfs.setStatus("current")
_VRtrV6StatIllegalLabels_Type = Counter32
_VRtrV6StatIllegalLabels_Object = MibTableColumn
vRtrV6StatIllegalLabels = _VRtrV6StatIllegalLabels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 45),
    _VRtrV6StatIllegalLabels_Type()
)
vRtrV6StatIllegalLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatIllegalLabels.setStatus("current")
_VRtrV6StatCurrNumRoutes_Type = Gauge32
_VRtrV6StatCurrNumRoutes_Object = MibTableColumn
vRtrV6StatCurrNumRoutes = _VRtrV6StatCurrNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 46),
    _VRtrV6StatCurrNumRoutes_Type()
)
vRtrV6StatCurrNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatCurrNumRoutes.setStatus("current")
_VRtrV6StatBGPVpnRoutes_Type = Gauge32
_VRtrV6StatBGPVpnRoutes_Object = MibTableColumn
vRtrV6StatBGPVpnRoutes = _VRtrV6StatBGPVpnRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 47),
    _VRtrV6StatBGPVpnRoutes_Type()
)
vRtrV6StatBGPVpnRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatBGPVpnRoutes.setStatus("current")
_VRtrV6StatBGPVpnActiveRoutes_Type = Gauge32
_VRtrV6StatBGPVpnActiveRoutes_Object = MibTableColumn
vRtrV6StatBGPVpnActiveRoutes = _VRtrV6StatBGPVpnActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 48),
    _VRtrV6StatBGPVpnActiveRoutes_Type()
)
vRtrV6StatBGPVpnActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatBGPVpnActiveRoutes.setStatus("current")
_VRtrV6StatTotalLdpTunnels_Type = Gauge32
_VRtrV6StatTotalLdpTunnels_Object = MibTableColumn
vRtrV6StatTotalLdpTunnels = _VRtrV6StatTotalLdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 49),
    _VRtrV6StatTotalLdpTunnels_Type()
)
vRtrV6StatTotalLdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatTotalLdpTunnels.setStatus("current")
_VRtrV6StatTotalSdpTunnels_Type = Gauge32
_VRtrV6StatTotalSdpTunnels_Object = MibTableColumn
vRtrV6StatTotalSdpTunnels = _VRtrV6StatTotalSdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 50),
    _VRtrV6StatTotalSdpTunnels_Type()
)
vRtrV6StatTotalSdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatTotalSdpTunnels.setStatus("current")
_VRtrV6StatActiveLdpTunnels_Type = Gauge32
_VRtrV6StatActiveLdpTunnels_Object = MibTableColumn
vRtrV6StatActiveLdpTunnels = _VRtrV6StatActiveLdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 51),
    _VRtrV6StatActiveLdpTunnels_Type()
)
vRtrV6StatActiveLdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatActiveLdpTunnels.setStatus("current")
_VRtrV6StatActiveSdpTunnels_Type = Gauge32
_VRtrV6StatActiveSdpTunnels_Object = MibTableColumn
vRtrV6StatActiveSdpTunnels = _VRtrV6StatActiveSdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 52),
    _VRtrV6StatActiveSdpTunnels_Type()
)
vRtrV6StatActiveSdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatActiveSdpTunnels.setStatus("current")
_VRtrV6MulticastRoutes_Type = Gauge32
_VRtrV6MulticastRoutes_Object = MibTableColumn
vRtrV6MulticastRoutes = _VRtrV6MulticastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 53),
    _VRtrV6MulticastRoutes_Type()
)
vRtrV6MulticastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6MulticastRoutes.setStatus("current")
_VRtrV6StatActiveNbrEntries_Type = Gauge32
_VRtrV6StatActiveNbrEntries_Object = MibTableColumn
vRtrV6StatActiveNbrEntries = _VRtrV6StatActiveNbrEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 54),
    _VRtrV6StatActiveNbrEntries_Type()
)
vRtrV6StatActiveNbrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatActiveNbrEntries.setStatus("current")
_VRtrV6StatTotalNbrEntries_Type = Gauge32
_VRtrV6StatTotalNbrEntries_Object = MibTableColumn
vRtrV6StatTotalNbrEntries = _VRtrV6StatTotalNbrEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 55),
    _VRtrV6StatTotalNbrEntries_Type()
)
vRtrV6StatTotalNbrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatTotalNbrEntries.setStatus("current")
_VRtrSubMgmtRoutes_Type = Gauge32
_VRtrSubMgmtRoutes_Object = MibTableColumn
vRtrSubMgmtRoutes = _VRtrSubMgmtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 56),
    _VRtrSubMgmtRoutes_Type()
)
vRtrSubMgmtRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSubMgmtRoutes.setStatus("current")
_VRtrSubMgmtActiveRoutes_Type = Gauge32
_VRtrSubMgmtActiveRoutes_Object = MibTableColumn
vRtrSubMgmtActiveRoutes = _VRtrSubMgmtActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 57),
    _VRtrSubMgmtActiveRoutes_Type()
)
vRtrSubMgmtActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSubMgmtActiveRoutes.setStatus("current")
_VRtrStatTotalRsvpTunnels_Type = Gauge32
_VRtrStatTotalRsvpTunnels_Object = MibTableColumn
vRtrStatTotalRsvpTunnels = _VRtrStatTotalRsvpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 58),
    _VRtrStatTotalRsvpTunnels_Type()
)
vRtrStatTotalRsvpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatTotalRsvpTunnels.setStatus("current")
_VRtrStatActiveRsvpTunnels_Type = Gauge32
_VRtrStatActiveRsvpTunnels_Object = MibTableColumn
vRtrStatActiveRsvpTunnels = _VRtrStatActiveRsvpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 59),
    _VRtrStatActiveRsvpTunnels_Type()
)
vRtrStatActiveRsvpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatActiveRsvpTunnels.setStatus("current")
_VRtrV6StatTotalRsvpTunnels_Type = Gauge32
_VRtrV6StatTotalRsvpTunnels_Object = MibTableColumn
vRtrV6StatTotalRsvpTunnels = _VRtrV6StatTotalRsvpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 60),
    _VRtrV6StatTotalRsvpTunnels_Type()
)
vRtrV6StatTotalRsvpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatTotalRsvpTunnels.setStatus("current")
_VRtrV6StatActiveRsvpTunnels_Type = Gauge32
_VRtrV6StatActiveRsvpTunnels_Object = MibTableColumn
vRtrV6StatActiveRsvpTunnels = _VRtrV6StatActiveRsvpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 61),
    _VRtrV6StatActiveRsvpTunnels_Type()
)
vRtrV6StatActiveRsvpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatActiveRsvpTunnels.setStatus("current")
_VRtrHostRoutes_Type = Gauge32
_VRtrHostRoutes_Object = MibTableColumn
vRtrHostRoutes = _VRtrHostRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 62),
    _VRtrHostRoutes_Type()
)
vRtrHostRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrHostRoutes.setStatus("current")
_VRtrHostActiveRoutes_Type = Gauge32
_VRtrHostActiveRoutes_Object = MibTableColumn
vRtrHostActiveRoutes = _VRtrHostActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 63),
    _VRtrHostActiveRoutes_Type()
)
vRtrHostActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrHostActiveRoutes.setStatus("current")
_VRtrV6HostRoutes_Type = Gauge32
_VRtrV6HostRoutes_Object = MibTableColumn
vRtrV6HostRoutes = _VRtrV6HostRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 64),
    _VRtrV6HostRoutes_Type()
)
vRtrV6HostRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6HostRoutes.setStatus("current")
_VRtrV6HostActiveRoutes_Type = Gauge32
_VRtrV6HostActiveRoutes_Object = MibTableColumn
vRtrV6HostActiveRoutes = _VRtrV6HostActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 65),
    _VRtrV6HostActiveRoutes_Type()
)
vRtrV6HostActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6HostActiveRoutes.setStatus("current")
_VRtrStatLocalARPEntries_Type = Gauge32
_VRtrStatLocalARPEntries_Object = MibTableColumn
vRtrStatLocalARPEntries = _VRtrStatLocalARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 66),
    _VRtrStatLocalARPEntries_Type()
)
vRtrStatLocalARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatLocalARPEntries.setStatus("current")
_VRtrStatStaticARPEntries_Type = Gauge32
_VRtrStatStaticARPEntries_Object = MibTableColumn
vRtrStatStaticARPEntries = _VRtrStatStaticARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 67),
    _VRtrStatStaticARPEntries_Type()
)
vRtrStatStaticARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatStaticARPEntries.setStatus("current")
_VRtrStatDynamicARPEntries_Type = Gauge32
_VRtrStatDynamicARPEntries_Object = MibTableColumn
vRtrStatDynamicARPEntries = _VRtrStatDynamicARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 68),
    _VRtrStatDynamicARPEntries_Type()
)
vRtrStatDynamicARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatDynamicARPEntries.setStatus("current")
_VRtrStatManagedARPEntries_Type = Gauge32
_VRtrStatManagedARPEntries_Object = MibTableColumn
vRtrStatManagedARPEntries = _VRtrStatManagedARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 69),
    _VRtrStatManagedARPEntries_Type()
)
vRtrStatManagedARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatManagedARPEntries.setStatus("current")
_VRtrStatInternalARPEntries_Type = Gauge32
_VRtrStatInternalARPEntries_Object = MibTableColumn
vRtrStatInternalARPEntries = _VRtrStatInternalARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 70),
    _VRtrStatInternalARPEntries_Type()
)
vRtrStatInternalARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatInternalARPEntries.setStatus("current")
_VRtrManagedRoutes_Type = Gauge32
_VRtrManagedRoutes_Object = MibTableColumn
vRtrManagedRoutes = _VRtrManagedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 71),
    _VRtrManagedRoutes_Type()
)
vRtrManagedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrManagedRoutes.setStatus("current")
_VRtrManagedActiveRoutes_Type = Gauge32
_VRtrManagedActiveRoutes_Object = MibTableColumn
vRtrManagedActiveRoutes = _VRtrManagedActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 72),
    _VRtrManagedActiveRoutes_Type()
)
vRtrManagedActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrManagedActiveRoutes.setStatus("current")
_VRtrLDPRoutes_Type = Gauge32
_VRtrLDPRoutes_Object = MibTableColumn
vRtrLDPRoutes = _VRtrLDPRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 73),
    _VRtrLDPRoutes_Type()
)
vRtrLDPRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLDPRoutes.setStatus("current")
_VRtrLDPActiveRoutes_Type = Gauge32
_VRtrLDPActiveRoutes_Object = MibTableColumn
vRtrLDPActiveRoutes = _VRtrLDPActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 74),
    _VRtrLDPActiveRoutes_Type()
)
vRtrLDPActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLDPActiveRoutes.setStatus("current")
_VRtrVPNLeakRoutes_Type = Gauge32
_VRtrVPNLeakRoutes_Object = MibTableColumn
vRtrVPNLeakRoutes = _VRtrVPNLeakRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 75),
    _VRtrVPNLeakRoutes_Type()
)
vRtrVPNLeakRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrVPNLeakRoutes.setStatus("current")
_VRtrVPNLeakActiveRoutes_Type = Gauge32
_VRtrVPNLeakActiveRoutes_Object = MibTableColumn
vRtrVPNLeakActiveRoutes = _VRtrVPNLeakActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 76),
    _VRtrVPNLeakActiveRoutes_Type()
)
vRtrVPNLeakActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrVPNLeakActiveRoutes.setStatus("current")
_VRtrV6VPNLeakRoutes_Type = Gauge32
_VRtrV6VPNLeakRoutes_Object = MibTableColumn
vRtrV6VPNLeakRoutes = _VRtrV6VPNLeakRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 77),
    _VRtrV6VPNLeakRoutes_Type()
)
vRtrV6VPNLeakRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6VPNLeakRoutes.setStatus("current")
_VRtrV6VPNLeakActiveRoutes_Type = Gauge32
_VRtrV6VPNLeakActiveRoutes_Object = MibTableColumn
vRtrV6VPNLeakActiveRoutes = _VRtrV6VPNLeakActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 78),
    _VRtrV6VPNLeakActiveRoutes_Type()
)
vRtrV6VPNLeakActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6VPNLeakActiveRoutes.setStatus("current")
_VRtrV6SubMgmtRoutes_Type = Gauge32
_VRtrV6SubMgmtRoutes_Object = MibTableColumn
vRtrV6SubMgmtRoutes = _VRtrV6SubMgmtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 79),
    _VRtrV6SubMgmtRoutes_Type()
)
vRtrV6SubMgmtRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6SubMgmtRoutes.setStatus("current")
_VRtrV6SubMgmtActiveRoutes_Type = Gauge32
_VRtrV6SubMgmtActiveRoutes_Object = MibTableColumn
vRtrV6SubMgmtActiveRoutes = _VRtrV6SubMgmtActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 80),
    _VRtrV6SubMgmtActiveRoutes_Type()
)
vRtrV6SubMgmtActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6SubMgmtActiveRoutes.setStatus("current")
_VRtrMobileHostRoutes_Type = Gauge32
_VRtrMobileHostRoutes_Object = MibTableColumn
vRtrMobileHostRoutes = _VRtrMobileHostRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 81),
    _VRtrMobileHostRoutes_Type()
)
vRtrMobileHostRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMobileHostRoutes.setStatus("current")
_VRtrMobileHostActiveRoutes_Type = Gauge32
_VRtrMobileHostActiveRoutes_Object = MibTableColumn
vRtrMobileHostActiveRoutes = _VRtrMobileHostActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 82),
    _VRtrMobileHostActiveRoutes_Type()
)
vRtrMobileHostActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMobileHostActiveRoutes.setStatus("current")
_VRtrV6MobileHostRoutes_Type = Gauge32
_VRtrV6MobileHostRoutes_Object = MibTableColumn
vRtrV6MobileHostRoutes = _VRtrV6MobileHostRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 83),
    _VRtrV6MobileHostRoutes_Type()
)
vRtrV6MobileHostRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6MobileHostRoutes.setStatus("current")
_VRtrV6MobileHostActiveRoutes_Type = Gauge32
_VRtrV6MobileHostActiveRoutes_Object = MibTableColumn
vRtrV6MobileHostActiveRoutes = _VRtrV6MobileHostActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 84),
    _VRtrV6MobileHostActiveRoutes_Type()
)
vRtrV6MobileHostActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6MobileHostActiveRoutes.setStatus("current")
_VRtrStatTotalBgpTunnels_Type = Gauge32
_VRtrStatTotalBgpTunnels_Object = MibTableColumn
vRtrStatTotalBgpTunnels = _VRtrStatTotalBgpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 85),
    _VRtrStatTotalBgpTunnels_Type()
)
vRtrStatTotalBgpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatTotalBgpTunnels.setStatus("current")
_VRtrStatActiveBgpTunnels_Type = Gauge32
_VRtrStatActiveBgpTunnels_Object = MibTableColumn
vRtrStatActiveBgpTunnels = _VRtrStatActiveBgpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 86),
    _VRtrStatActiveBgpTunnels_Type()
)
vRtrStatActiveBgpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatActiveBgpTunnels.setStatus("current")
_VRtrNatRoutes_Type = Gauge32
_VRtrNatRoutes_Object = MibTableColumn
vRtrNatRoutes = _VRtrNatRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 87),
    _VRtrNatRoutes_Type()
)
vRtrNatRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrNatRoutes.setStatus("current")
_VRtrNatActiveRoutes_Type = Gauge32
_VRtrNatActiveRoutes_Object = MibTableColumn
vRtrNatActiveRoutes = _VRtrNatActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 88),
    _VRtrNatActiveRoutes_Type()
)
vRtrNatActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrNatActiveRoutes.setStatus("current")
_VRtrV6NatRoutes_Type = Gauge32
_VRtrV6NatRoutes_Object = MibTableColumn
vRtrV6NatRoutes = _VRtrV6NatRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 89),
    _VRtrV6NatRoutes_Type()
)
vRtrV6NatRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6NatRoutes.setStatus("current")
_VRtrV6NatActiveRoutes_Type = Gauge32
_VRtrV6NatActiveRoutes_Object = MibTableColumn
vRtrV6NatActiveRoutes = _VRtrV6NatActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 90),
    _VRtrV6NatActiveRoutes_Type()
)
vRtrV6NatActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6NatActiveRoutes.setStatus("current")
_VRtrPeriodicRoutes_Type = Gauge32
_VRtrPeriodicRoutes_Object = MibTableColumn
vRtrPeriodicRoutes = _VRtrPeriodicRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 91),
    _VRtrPeriodicRoutes_Type()
)
vRtrPeriodicRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPeriodicRoutes.setStatus("current")
_VRtrPeriodicActiveRoutes_Type = Gauge32
_VRtrPeriodicActiveRoutes_Object = MibTableColumn
vRtrPeriodicActiveRoutes = _VRtrPeriodicActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 92),
    _VRtrPeriodicActiveRoutes_Type()
)
vRtrPeriodicActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPeriodicActiveRoutes.setStatus("current")
_VRtrV6PeriodicRoutes_Type = Gauge32
_VRtrV6PeriodicRoutes_Object = MibTableColumn
vRtrV6PeriodicRoutes = _VRtrV6PeriodicRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 93),
    _VRtrV6PeriodicRoutes_Type()
)
vRtrV6PeriodicRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6PeriodicRoutes.setStatus("current")
_VRtrV6PeriodicActiveRoutes_Type = Gauge32
_VRtrV6PeriodicActiveRoutes_Object = MibTableColumn
vRtrV6PeriodicActiveRoutes = _VRtrV6PeriodicActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 94),
    _VRtrV6PeriodicActiveRoutes_Type()
)
vRtrV6PeriodicActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6PeriodicActiveRoutes.setStatus("current")
_VRtrStatTotalMplsTpTunnels_Type = Gauge32
_VRtrStatTotalMplsTpTunnels_Object = MibTableColumn
vRtrStatTotalMplsTpTunnels = _VRtrStatTotalMplsTpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 97),
    _VRtrStatTotalMplsTpTunnels_Type()
)
vRtrStatTotalMplsTpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatTotalMplsTpTunnels.setStatus("current")
_VRtrStatActiveMplsTpTunnels_Type = Gauge32
_VRtrStatActiveMplsTpTunnels_Object = MibTableColumn
vRtrStatActiveMplsTpTunnels = _VRtrStatActiveMplsTpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 2, 1, 98),
    _VRtrStatActiveMplsTpTunnels_Type()
)
vRtrStatActiveMplsTpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatActiveMplsTpTunnels.setStatus("current")


class _VRtrIfTotalNumber_Type(Integer32):
    """Custom type vRtrIfTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIfTotalNumber_Type.__name__ = "Integer32"
_VRtrIfTotalNumber_Object = MibScalar
vRtrIfTotalNumber = _VRtrIfTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 3),
    _VRtrIfTotalNumber_Type()
)
vRtrIfTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTotalNumber.setStatus("current")
_VRtrIfTable_Object = MibTable
vRtrIfTable = _VRtrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    vRtrIfTable.setStatus("current")
_VRtrIfEntry_Object = MibTableRow
vRtrIfEntry = _VRtrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1)
)
vRtrIfEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (0, "TN-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrIfEntry.setStatus("current")
_VRtrIfIndex_Type = InterfaceIndex
_VRtrIfIndex_Object = MibTableColumn
vRtrIfIndex = _VRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 1),
    _VRtrIfIndex_Type()
)
vRtrIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIfIndex.setStatus("current")
_VRtrIfRowStatus_Type = RowStatus
_VRtrIfRowStatus_Object = MibTableColumn
vRtrIfRowStatus = _VRtrIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 2),
    _VRtrIfRowStatus_Type()
)
vRtrIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfRowStatus.setStatus("current")


class _VRtrIfType_Type(Integer32):
    """Custom type vRtrIfType based on Integer32"""
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("service", 2),
          ("serviceIes", 3),
          ("serviceRtdVpls", 4),
          ("serviceVprn", 5),
          ("serviceIesSubscriber", 6),
          ("serviceIesGroup", 7),
          ("serviceVprnSubscriber", 8),
          ("serviceVprnGroup", 9),
          ("serviceIesRedundant", 10),
          ("serviceVprnRedundant", 11),
          ("serviceVpls", 12),
          ("serviceIesCem", 13),
          ("serviceVprnCem", 14),
          ("serviceVprnIPsec", 15),
          ("serviceVprnIPMirror", 16),
          ("serviceVideo", 17),
          ("serviceVplsVideo", 18),
          ("multiHomingPrimary", 19),
          ("multiHomingSecondary", 20),
          ("serviceIesTunnel", 21),
          ("serviceIpReas", 22),
          ("networkIpReas", 23),
          ("networkVprn", 24),
          ("tmsService", 25),
          ("serviceIesAarp", 26),
          ("serviceVprnAarp", 27),
          ("serviceIesAa", 28),
          ("serviceVprnAa", 29),
          ("unnumMplsTp", 30))
    )


_VRtrIfType_Type.__name__ = "Integer32"
_VRtrIfType_Object = MibTableColumn
vRtrIfType = _VRtrIfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 3),
    _VRtrIfType_Type()
)
vRtrIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfType.setStatus("current")
_VRtrIfName_Type = TNamedItem
_VRtrIfName_Object = MibTableColumn
vRtrIfName = _VRtrIfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 4),
    _VRtrIfName_Type()
)
vRtrIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfName.setStatus("current")


class _VRtrIfPortID_Type(InterfaceIndexOrZero):
    """Custom type vRtrIfPortID based on InterfaceIndexOrZero"""
    defaultValue = 0


_VRtrIfPortID_Type.__name__ = "InterfaceIndexOrZero"
_VRtrIfPortID_Object = MibTableColumn
vRtrIfPortID = _VRtrIfPortID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 5),
    _VRtrIfPortID_Type()
)
vRtrIfPortID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfPortID.setStatus("current")


class _VRtrIfChannelID_Type(Unsigned32):
    """Custom type vRtrIfChannelID based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_VRtrIfChannelID_Type.__name__ = "Unsigned32"
_VRtrIfChannelID_Object = MibTableColumn
vRtrIfChannelID = _VRtrIfChannelID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 6),
    _VRtrIfChannelID_Type()
)
vRtrIfChannelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfChannelID.setStatus("obsolete")
_VRtrIfEncapValue_Type = TmnxEncapVal
_VRtrIfEncapValue_Object = MibTableColumn
vRtrIfEncapValue = _VRtrIfEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 7),
    _VRtrIfEncapValue_Type()
)
vRtrIfEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfEncapValue.setStatus("current")


class _VRtrIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrIfAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrIfAdminState_Object = MibTableColumn
vRtrIfAdminState = _VRtrIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 8),
    _VRtrIfAdminState_Type()
)
vRtrIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfAdminState.setStatus("current")
_VRtrIfOperState_Type = TmnxOperState
_VRtrIfOperState_Object = MibTableColumn
vRtrIfOperState = _VRtrIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 9),
    _VRtrIfOperState_Type()
)
vRtrIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfOperState.setStatus("current")


class _VRtrIfAlias_Type(DisplayString):
    """Custom type vRtrIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRtrIfAlias_Type.__name__ = "DisplayString"
_VRtrIfAlias_Object = MibTableColumn
vRtrIfAlias = _VRtrIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 10),
    _VRtrIfAlias_Type()
)
vRtrIfAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfAlias.setStatus("current")
_VRtrIfPhysicalAddress_Type = MacAddress
_VRtrIfPhysicalAddress_Object = MibTableColumn
vRtrIfPhysicalAddress = _VRtrIfPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 11),
    _VRtrIfPhysicalAddress_Type()
)
vRtrIfPhysicalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfPhysicalAddress.setStatus("current")


class _VRtrIfArpTimeout_Type(Unsigned32):
    """Custom type vRtrIfArpTimeout based on Unsigned32"""
    defaultValue = 14400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIfArpTimeout_Type.__name__ = "Unsigned32"
_VRtrIfArpTimeout_Object = MibTableColumn
vRtrIfArpTimeout = _VRtrIfArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 12),
    _VRtrIfArpTimeout_Type()
)
vRtrIfArpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfArpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfArpTimeout.setUnits("seconds")


class _VRtrIfIcmpMaskReply_Type(TruthValue):
    """Custom type vRtrIfIcmpMaskReply based on TruthValue"""
    defaultValue = 1


_VRtrIfIcmpMaskReply_Type.__name__ = "TruthValue"
_VRtrIfIcmpMaskReply_Object = MibTableColumn
vRtrIfIcmpMaskReply = _VRtrIfIcmpMaskReply_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 13),
    _VRtrIfIcmpMaskReply_Type()
)
vRtrIfIcmpMaskReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpMaskReply.setStatus("current")


class _VRtrIfIcmpRedirects_Type(TruthValue):
    """Custom type vRtrIfIcmpRedirects based on TruthValue"""
    defaultValue = 1


_VRtrIfIcmpRedirects_Type.__name__ = "TruthValue"
_VRtrIfIcmpRedirects_Object = MibTableColumn
vRtrIfIcmpRedirects = _VRtrIfIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 14),
    _VRtrIfIcmpRedirects_Type()
)
vRtrIfIcmpRedirects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpRedirects.setStatus("current")


class _VRtrIfIcmpNumRedirects_Type(Unsigned32):
    """Custom type vRtrIfIcmpNumRedirects based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpNumRedirects_Type.__name__ = "Unsigned32"
_VRtrIfIcmpNumRedirects_Object = MibTableColumn
vRtrIfIcmpNumRedirects = _VRtrIfIcmpNumRedirects_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 15),
    _VRtrIfIcmpNumRedirects_Type()
)
vRtrIfIcmpNumRedirects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpNumRedirects.setStatus("current")


class _VRtrIfIcmpRedirectsTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpRedirectsTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpRedirectsTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpRedirectsTime_Object = MibTableColumn
vRtrIfIcmpRedirectsTime = _VRtrIfIcmpRedirectsTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 16),
    _VRtrIfIcmpRedirectsTime_Type()
)
vRtrIfIcmpRedirectsTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpRedirectsTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpRedirectsTime.setUnits("seconds")


class _VRtrIfIcmpUnreachables_Type(TruthValue):
    """Custom type vRtrIfIcmpUnreachables based on TruthValue"""
    defaultValue = 1


_VRtrIfIcmpUnreachables_Type.__name__ = "TruthValue"
_VRtrIfIcmpUnreachables_Object = MibTableColumn
vRtrIfIcmpUnreachables = _VRtrIfIcmpUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 17),
    _VRtrIfIcmpUnreachables_Type()
)
vRtrIfIcmpUnreachables.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpUnreachables.setStatus("current")


class _VRtrIfIcmpNumUnreachables_Type(Unsigned32):
    """Custom type vRtrIfIcmpNumUnreachables based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpNumUnreachables_Type.__name__ = "Unsigned32"
_VRtrIfIcmpNumUnreachables_Object = MibTableColumn
vRtrIfIcmpNumUnreachables = _VRtrIfIcmpNumUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 18),
    _VRtrIfIcmpNumUnreachables_Type()
)
vRtrIfIcmpNumUnreachables.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpNumUnreachables.setStatus("current")


class _VRtrIfIcmpUnreachablesTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpUnreachablesTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpUnreachablesTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpUnreachablesTime_Object = MibTableColumn
vRtrIfIcmpUnreachablesTime = _VRtrIfIcmpUnreachablesTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 19),
    _VRtrIfIcmpUnreachablesTime_Type()
)
vRtrIfIcmpUnreachablesTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpUnreachablesTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpUnreachablesTime.setUnits("seconds")


class _VRtrIfIcmpTtlExpired_Type(TruthValue):
    """Custom type vRtrIfIcmpTtlExpired based on TruthValue"""
    defaultValue = 1


_VRtrIfIcmpTtlExpired_Type.__name__ = "TruthValue"
_VRtrIfIcmpTtlExpired_Object = MibTableColumn
vRtrIfIcmpTtlExpired = _VRtrIfIcmpTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 20),
    _VRtrIfIcmpTtlExpired_Type()
)
vRtrIfIcmpTtlExpired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpTtlExpired.setStatus("current")


class _VRtrIfIcmpNumTtlExpired_Type(Unsigned32):
    """Custom type vRtrIfIcmpNumTtlExpired based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpNumTtlExpired_Type.__name__ = "Unsigned32"
_VRtrIfIcmpNumTtlExpired_Object = MibTableColumn
vRtrIfIcmpNumTtlExpired = _VRtrIfIcmpNumTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 21),
    _VRtrIfIcmpNumTtlExpired_Type()
)
vRtrIfIcmpNumTtlExpired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpNumTtlExpired.setStatus("current")


class _VRtrIfIcmpTtlExpiredTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpTtlExpiredTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpTtlExpiredTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpTtlExpiredTime_Object = MibTableColumn
vRtrIfIcmpTtlExpiredTime = _VRtrIfIcmpTtlExpiredTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 22),
    _VRtrIfIcmpTtlExpiredTime_Type()
)
vRtrIfIcmpTtlExpiredTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpTtlExpiredTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpTtlExpiredTime.setUnits("seconds")


class _VRtrIfNtpBroadcast_Type(TruthValue):
    """Custom type vRtrIfNtpBroadcast based on TruthValue"""
    defaultValue = 2


_VRtrIfNtpBroadcast_Type.__name__ = "TruthValue"
_VRtrIfNtpBroadcast_Object = MibTableColumn
vRtrIfNtpBroadcast = _VRtrIfNtpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 23),
    _VRtrIfNtpBroadcast_Type()
)
vRtrIfNtpBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfNtpBroadcast.setStatus("current")


class _VRtrIfUnnumbered_Type(IpAddress):
    """Custom type vRtrIfUnnumbered based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrIfUnnumbered_Type.__name__ = "IpAddress"
_VRtrIfUnnumbered_Object = MibTableColumn
vRtrIfUnnumbered = _VRtrIfUnnumbered_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 24),
    _VRtrIfUnnumbered_Type()
)
vRtrIfUnnumbered.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfUnnumbered.setStatus("current")


class _VRtrIfMtu_Type(Unsigned32):
    """Custom type vRtrIfMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_VRtrIfMtu_Type.__name__ = "Unsigned32"
_VRtrIfMtu_Object = MibTableColumn
vRtrIfMtu = _VRtrIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 25),
    _VRtrIfMtu_Type()
)
vRtrIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfMtu.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfMtu.setUnits("bytes")


class _VRtrIfQosPolicyId_Type(TNetworkPolicyID):
    """Custom type vRtrIfQosPolicyId based on TNetworkPolicyID"""
    defaultValue = 1


_VRtrIfQosPolicyId_Type.__name__ = "TNetworkPolicyID"
_VRtrIfQosPolicyId_Object = MibTableColumn
vRtrIfQosPolicyId = _VRtrIfQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 26),
    _VRtrIfQosPolicyId_Type()
)
vRtrIfQosPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfQosPolicyId.setStatus("obsolete")


class _VRtrIfIngressFilterId_Type(TIPFilterID):
    """Custom type vRtrIfIngressFilterId based on TIPFilterID"""
    defaultValue = 0


_VRtrIfIngressFilterId_Type.__name__ = "TIPFilterID"
_VRtrIfIngressFilterId_Object = MibTableColumn
vRtrIfIngressFilterId = _VRtrIfIngressFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 27),
    _VRtrIfIngressFilterId_Type()
)
vRtrIfIngressFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIngressFilterId.setStatus("current")


class _VRtrIfEgressFilterId_Type(TIPFilterID):
    """Custom type vRtrIfEgressFilterId based on TIPFilterID"""
    defaultValue = 0


_VRtrIfEgressFilterId_Type.__name__ = "TIPFilterID"
_VRtrIfEgressFilterId_Object = MibTableColumn
vRtrIfEgressFilterId = _VRtrIfEgressFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 28),
    _VRtrIfEgressFilterId_Type()
)
vRtrIfEgressFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfEgressFilterId.setStatus("current")


class _VRtrIfDirectedBroadcast_Type(TruthValue):
    """Custom type vRtrIfDirectedBroadcast based on TruthValue"""
    defaultValue = 2


_VRtrIfDirectedBroadcast_Type.__name__ = "TruthValue"
_VRtrIfDirectedBroadcast_Object = MibTableColumn
vRtrIfDirectedBroadcast = _VRtrIfDirectedBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 29),
    _VRtrIfDirectedBroadcast_Type()
)
vRtrIfDirectedBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDirectedBroadcast.setStatus("current")


class _VRtrIfMplsStatus_Type(TmnxStatus):
    """Custom type vRtrIfMplsStatus based on TmnxStatus"""
    defaultValue = 2


_VRtrIfMplsStatus_Type.__name__ = "TmnxStatus"
_VRtrIfMplsStatus_Object = MibTableColumn
vRtrIfMplsStatus = _VRtrIfMplsStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 30),
    _VRtrIfMplsStatus_Type()
)
vRtrIfMplsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfMplsStatus.setStatus("current")


class _VRtrIfUnnumberedIf_Type(DisplayString):
    """Custom type vRtrIfUnnumberedIf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRtrIfUnnumberedIf_Type.__name__ = "DisplayString"
_VRtrIfUnnumberedIf_Object = MibTableColumn
vRtrIfUnnumberedIf = _VRtrIfUnnumberedIf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 31),
    _VRtrIfUnnumberedIf_Type()
)
vRtrIfUnnumberedIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfUnnumberedIf.setStatus("current")


class _VRtrIfCflowd_Type(Integer32):
    """Custom type vRtrIfCflowd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("aclIngressOnly", 2),
          ("interfaceIngressOnly", 3),
          ("aclEgressOnly", 4),
          ("interfaceEgressOnly", 5),
          ("aclIngressEgress", 6),
          ("interfaceIngressEgress", 7))
    )


_VRtrIfCflowd_Type.__name__ = "Integer32"
_VRtrIfCflowd_Object = MibTableColumn
vRtrIfCflowd = _VRtrIfCflowd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 32),
    _VRtrIfCflowd_Type()
)
vRtrIfCflowd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfCflowd.setStatus("current")


class _VRtrIfVPNClass_Type(Integer32):
    """Custom type vRtrIfVPNClass based on Integer32"""
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
        *(("unknown", 0),
          ("carrierOfCarrier", 1),
          ("enterprise", 2),
          ("interProvider", 3))
    )


_VRtrIfVPNClass_Type.__name__ = "Integer32"
_VRtrIfVPNClass_Object = MibTableColumn
vRtrIfVPNClass = _VRtrIfVPNClass_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 33),
    _VRtrIfVPNClass_Type()
)
vRtrIfVPNClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfVPNClass.setStatus("current")


class _VRtrIfDescription_Type(TItemLongDescription):
    """Custom type vRtrIfDescription based on TItemLongDescription"""
    defaultHexValue = ""


_VRtrIfDescription_Type.__name__ = "TItemLongDescription"
_VRtrIfDescription_Object = MibTableColumn
vRtrIfDescription = _VRtrIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 34),
    _VRtrIfDescription_Type()
)
vRtrIfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDescription.setStatus("current")


class _VRtrIfProtocol_Type(Bits):
    """Custom type vRtrIfProtocol based on Bits"""
    namedValues = NamedValues(
        *(("ospfv2", 0),
          ("rip", 1),
          ("isis", 2),
          ("bgp", 3),
          ("mpls", 4),
          ("rsvp", 5),
          ("ldp", 6),
          ("igmp", 7),
          ("pim", 8),
          ("ospf3", 9),
          ("mld", 10))
    )

_VRtrIfProtocol_Type.__name__ = "Bits"
_VRtrIfProtocol_Object = MibTableColumn
vRtrIfProtocol = _VRtrIfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 35),
    _VRtrIfProtocol_Type()
)
vRtrIfProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfProtocol.setStatus("current")


class _VRtrIfTosMarkingTrusted_Type(TruthValue):
    """Custom type vRtrIfTosMarkingTrusted based on TruthValue"""
    defaultValue = 1


_VRtrIfTosMarkingTrusted_Type.__name__ = "TruthValue"
_VRtrIfTosMarkingTrusted_Object = MibTableColumn
vRtrIfTosMarkingTrusted = _VRtrIfTosMarkingTrusted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 36),
    _VRtrIfTosMarkingTrusted_Type()
)
vRtrIfTosMarkingTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfTosMarkingTrusted.setStatus("current")


class _VRtrIfServiceId_Type(TmnxServId):
    """Custom type vRtrIfServiceId based on TmnxServId"""
    defaultValue = 0


_VRtrIfServiceId_Type.__name__ = "TmnxServId"
_VRtrIfServiceId_Object = MibTableColumn
vRtrIfServiceId = _VRtrIfServiceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 37),
    _VRtrIfServiceId_Type()
)
vRtrIfServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfServiceId.setStatus("current")


class _VRtrIfArpPopulate_Type(Integer32):
    """Custom type vRtrIfArpPopulate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_VRtrIfArpPopulate_Type.__name__ = "Integer32"
_VRtrIfArpPopulate_Object = MibTableColumn
vRtrIfArpPopulate = _VRtrIfArpPopulate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 38),
    _VRtrIfArpPopulate_Type()
)
vRtrIfArpPopulate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfArpPopulate.setStatus("current")


class _VRtrIfIPv6ConfigAllowed_Type(TruthValue):
    """Custom type vRtrIfIPv6ConfigAllowed based on TruthValue"""
    defaultValue = 2


_VRtrIfIPv6ConfigAllowed_Type.__name__ = "TruthValue"
_VRtrIfIPv6ConfigAllowed_Object = MibTableColumn
vRtrIfIPv6ConfigAllowed = _VRtrIfIPv6ConfigAllowed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 39),
    _VRtrIfIPv6ConfigAllowed_Type()
)
vRtrIfIPv6ConfigAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIPv6ConfigAllowed.setStatus("current")
_VRtrIfIPv6OperState_Type = TmnxOperState
_VRtrIfIPv6OperState_Object = MibTableColumn
vRtrIfIPv6OperState = _VRtrIfIPv6OperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 40),
    _VRtrIfIPv6OperState_Type()
)
vRtrIfIPv6OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIPv6OperState.setStatus("current")


class _VRtrIfIPv6IngressFilterId_Type(TIPFilterID):
    """Custom type vRtrIfIPv6IngressFilterId based on TIPFilterID"""
    defaultValue = 0


_VRtrIfIPv6IngressFilterId_Type.__name__ = "TIPFilterID"
_VRtrIfIPv6IngressFilterId_Object = MibTableColumn
vRtrIfIPv6IngressFilterId = _VRtrIfIPv6IngressFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 41),
    _VRtrIfIPv6IngressFilterId_Type()
)
vRtrIfIPv6IngressFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIPv6IngressFilterId.setStatus("current")


class _VRtrIfIPv6EgressFilterId_Type(TIPFilterID):
    """Custom type vRtrIfIPv6EgressFilterId based on TIPFilterID"""
    defaultValue = 0


_VRtrIfIPv6EgressFilterId_Type.__name__ = "TIPFilterID"
_VRtrIfIPv6EgressFilterId_Object = MibTableColumn
vRtrIfIPv6EgressFilterId = _VRtrIfIPv6EgressFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 42),
    _VRtrIfIPv6EgressFilterId_Type()
)
vRtrIfIPv6EgressFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIPv6EgressFilterId.setStatus("current")


class _VRtrIfIcmpV6Redirects_Type(TruthValue):
    """Custom type vRtrIfIcmpV6Redirects based on TruthValue"""
    defaultValue = 1


_VRtrIfIcmpV6Redirects_Type.__name__ = "TruthValue"
_VRtrIfIcmpV6Redirects_Object = MibTableColumn
vRtrIfIcmpV6Redirects = _VRtrIfIcmpV6Redirects_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 43),
    _VRtrIfIcmpV6Redirects_Type()
)
vRtrIfIcmpV6Redirects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6Redirects.setStatus("current")


class _VRtrIfIcmpV6NumRedirects_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6NumRedirects based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpV6NumRedirects_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6NumRedirects_Object = MibTableColumn
vRtrIfIcmpV6NumRedirects = _VRtrIfIcmpV6NumRedirects_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 44),
    _VRtrIfIcmpV6NumRedirects_Type()
)
vRtrIfIcmpV6NumRedirects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6NumRedirects.setStatus("current")


class _VRtrIfIcmpV6RedirectsTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6RedirectsTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpV6RedirectsTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6RedirectsTime_Object = MibTableColumn
vRtrIfIcmpV6RedirectsTime = _VRtrIfIcmpV6RedirectsTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 45),
    _VRtrIfIcmpV6RedirectsTime_Type()
)
vRtrIfIcmpV6RedirectsTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6RedirectsTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6RedirectsTime.setUnits("seconds")


class _VRtrIfIcmpV6Unreachables_Type(TruthValue):
    """Custom type vRtrIfIcmpV6Unreachables based on TruthValue"""
    defaultValue = 1


_VRtrIfIcmpV6Unreachables_Type.__name__ = "TruthValue"
_VRtrIfIcmpV6Unreachables_Object = MibTableColumn
vRtrIfIcmpV6Unreachables = _VRtrIfIcmpV6Unreachables_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 46),
    _VRtrIfIcmpV6Unreachables_Type()
)
vRtrIfIcmpV6Unreachables.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6Unreachables.setStatus("current")


class _VRtrIfIcmpV6NumUnreachables_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6NumUnreachables based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpV6NumUnreachables_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6NumUnreachables_Object = MibTableColumn
vRtrIfIcmpV6NumUnreachables = _VRtrIfIcmpV6NumUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 47),
    _VRtrIfIcmpV6NumUnreachables_Type()
)
vRtrIfIcmpV6NumUnreachables.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6NumUnreachables.setStatus("current")


class _VRtrIfIcmpV6UnreachablesTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6UnreachablesTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpV6UnreachablesTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6UnreachablesTime_Object = MibTableColumn
vRtrIfIcmpV6UnreachablesTime = _VRtrIfIcmpV6UnreachablesTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 48),
    _VRtrIfIcmpV6UnreachablesTime_Type()
)
vRtrIfIcmpV6UnreachablesTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6UnreachablesTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6UnreachablesTime.setUnits("seconds")


class _VRtrIfIcmpV6TimeExceeded_Type(TruthValue):
    """Custom type vRtrIfIcmpV6TimeExceeded based on TruthValue"""
    defaultValue = 1


_VRtrIfIcmpV6TimeExceeded_Type.__name__ = "TruthValue"
_VRtrIfIcmpV6TimeExceeded_Object = MibTableColumn
vRtrIfIcmpV6TimeExceeded = _VRtrIfIcmpV6TimeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 49),
    _VRtrIfIcmpV6TimeExceeded_Type()
)
vRtrIfIcmpV6TimeExceeded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6TimeExceeded.setStatus("current")


class _VRtrIfIcmpV6NumTimeExceeded_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6NumTimeExceeded based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpV6NumTimeExceeded_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6NumTimeExceeded_Object = MibTableColumn
vRtrIfIcmpV6NumTimeExceeded = _VRtrIfIcmpV6NumTimeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 50),
    _VRtrIfIcmpV6NumTimeExceeded_Type()
)
vRtrIfIcmpV6NumTimeExceeded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6NumTimeExceeded.setStatus("current")


class _VRtrIfIcmpV6TimeExceededTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6TimeExceededTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpV6TimeExceededTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6TimeExceededTime_Object = MibTableColumn
vRtrIfIcmpV6TimeExceededTime = _VRtrIfIcmpV6TimeExceededTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 51),
    _VRtrIfIcmpV6TimeExceededTime_Type()
)
vRtrIfIcmpV6TimeExceededTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6TimeExceededTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6TimeExceededTime.setUnits("seconds")


class _VRtrIfIcmpV6PktTooBig_Type(TruthValue):
    """Custom type vRtrIfIcmpV6PktTooBig based on TruthValue"""
    defaultValue = 1


_VRtrIfIcmpV6PktTooBig_Type.__name__ = "TruthValue"
_VRtrIfIcmpV6PktTooBig_Object = MibTableColumn
vRtrIfIcmpV6PktTooBig = _VRtrIfIcmpV6PktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 52),
    _VRtrIfIcmpV6PktTooBig_Type()
)
vRtrIfIcmpV6PktTooBig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6PktTooBig.setStatus("current")


class _VRtrIfIcmpV6NumPktTooBig_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6NumPktTooBig based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpV6NumPktTooBig_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6NumPktTooBig_Object = MibTableColumn
vRtrIfIcmpV6NumPktTooBig = _VRtrIfIcmpV6NumPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 53),
    _VRtrIfIcmpV6NumPktTooBig_Type()
)
vRtrIfIcmpV6NumPktTooBig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6NumPktTooBig.setStatus("current")


class _VRtrIfIcmpV6PktTooBigTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6PktTooBigTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpV6PktTooBigTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6PktTooBigTime_Object = MibTableColumn
vRtrIfIcmpV6PktTooBigTime = _VRtrIfIcmpV6PktTooBigTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 54),
    _VRtrIfIcmpV6PktTooBigTime_Type()
)
vRtrIfIcmpV6PktTooBigTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6PktTooBigTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6PktTooBigTime.setUnits("seconds")


class _VRtrIfIcmpV6ParamProblem_Type(TruthValue):
    """Custom type vRtrIfIcmpV6ParamProblem based on TruthValue"""
    defaultValue = 1


_VRtrIfIcmpV6ParamProblem_Type.__name__ = "TruthValue"
_VRtrIfIcmpV6ParamProblem_Object = MibTableColumn
vRtrIfIcmpV6ParamProblem = _VRtrIfIcmpV6ParamProblem_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 55),
    _VRtrIfIcmpV6ParamProblem_Type()
)
vRtrIfIcmpV6ParamProblem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6ParamProblem.setStatus("current")


class _VRtrIfIcmpV6NumParamProblem_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6NumParamProblem based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpV6NumParamProblem_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6NumParamProblem_Object = MibTableColumn
vRtrIfIcmpV6NumParamProblem = _VRtrIfIcmpV6NumParamProblem_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 56),
    _VRtrIfIcmpV6NumParamProblem_Type()
)
vRtrIfIcmpV6NumParamProblem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6NumParamProblem.setStatus("current")


class _VRtrIfIcmpV6ParamProblemTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6ParamProblemTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpV6ParamProblemTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6ParamProblemTime_Object = MibTableColumn
vRtrIfIcmpV6ParamProblemTime = _VRtrIfIcmpV6ParamProblemTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 57),
    _VRtrIfIcmpV6ParamProblemTime_Type()
)
vRtrIfIcmpV6ParamProblemTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6ParamProblemTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6ParamProblemTime.setUnits("seconds")
_VRtrIfLinkLocalAddressType_Type = InetAddressType
_VRtrIfLinkLocalAddressType_Object = MibTableColumn
vRtrIfLinkLocalAddressType = _VRtrIfLinkLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 58),
    _VRtrIfLinkLocalAddressType_Type()
)
vRtrIfLinkLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfLinkLocalAddressType.setStatus("current")


class _VRtrIfLinkLocalAddress_Type(InetAddress):
    """Custom type vRtrIfLinkLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )


_VRtrIfLinkLocalAddress_Type.__name__ = "InetAddress"
_VRtrIfLinkLocalAddress_Object = MibTableColumn
vRtrIfLinkLocalAddress = _VRtrIfLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 59),
    _VRtrIfLinkLocalAddress_Type()
)
vRtrIfLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfLinkLocalAddress.setStatus("current")
_VRtrIfLinkLocalAddressState_Type = TmnxInetAddrState
_VRtrIfLinkLocalAddressState_Object = MibTableColumn
vRtrIfLinkLocalAddressState = _VRtrIfLinkLocalAddressState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 60),
    _VRtrIfLinkLocalAddressState_Type()
)
vRtrIfLinkLocalAddressState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfLinkLocalAddressState.setStatus("current")
_VRtrIfLastOperStateChange_Type = TimeStamp
_VRtrIfLastOperStateChange_Object = MibTableColumn
vRtrIfLastOperStateChange = _VRtrIfLastOperStateChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 61),
    _VRtrIfLastOperStateChange_Type()
)
vRtrIfLastOperStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfLastOperStateChange.setStatus("current")
_VRtrIfOperMtu_Type = Unsigned32
_VRtrIfOperMtu_Object = MibTableColumn
vRtrIfOperMtu = _VRtrIfOperMtu_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 62),
    _VRtrIfOperMtu_Type()
)
vRtrIfOperMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfOperMtu.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfOperMtu.setUnits("bytes")


class _VRtrIfGlobalIndex_Type(Unsigned32):
    """Custom type vRtrIfGlobalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262144),
    )


_VRtrIfGlobalIndex_Type.__name__ = "Unsigned32"
_VRtrIfGlobalIndex_Object = MibTableColumn
vRtrIfGlobalIndex = _VRtrIfGlobalIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 63),
    _VRtrIfGlobalIndex_Type()
)
vRtrIfGlobalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfGlobalIndex.setStatus("current")


class _VRtrIfDelaySeconds_Type(Unsigned32):
    """Custom type vRtrIfDelaySeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIfDelaySeconds_Type.__name__ = "Unsigned32"
_VRtrIfDelaySeconds_Object = MibTableColumn
vRtrIfDelaySeconds = _VRtrIfDelaySeconds_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 64),
    _VRtrIfDelaySeconds_Type()
)
vRtrIfDelaySeconds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDelaySeconds.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfDelaySeconds.setUnits("seconds")
_VRtrIfDelayUpTimer_Type = Integer32
_VRtrIfDelayUpTimer_Object = MibTableColumn
vRtrIfDelayUpTimer = _VRtrIfDelayUpTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 65),
    _VRtrIfDelayUpTimer_Type()
)
vRtrIfDelayUpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDelayUpTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfDelayUpTimer.setUnits("seconds")


class _VRtrIfLocalDhcpServerName_Type(TNamedItemOrEmpty):
    """Custom type vRtrIfLocalDhcpServerName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrIfLocalDhcpServerName_Type.__name__ = "TNamedItemOrEmpty"
_VRtrIfLocalDhcpServerName_Object = MibTableColumn
vRtrIfLocalDhcpServerName = _VRtrIfLocalDhcpServerName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 66),
    _VRtrIfLocalDhcpServerName_Type()
)
vRtrIfLocalDhcpServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfLocalDhcpServerName.setStatus("current")


class _VRtrIfInitDelayEnable_Type(TruthValue):
    """Custom type vRtrIfInitDelayEnable based on TruthValue"""
    defaultValue = 2


_VRtrIfInitDelayEnable_Type.__name__ = "TruthValue"
_VRtrIfInitDelayEnable_Object = MibTableColumn
vRtrIfInitDelayEnable = _VRtrIfInitDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 67),
    _VRtrIfInitDelayEnable_Type()
)
vRtrIfInitDelayEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfInitDelayEnable.setStatus("current")
_VRtrIfCpmProtPolicyId_Type = TCpmProtPolicyID
_VRtrIfCpmProtPolicyId_Object = MibTableColumn
vRtrIfCpmProtPolicyId = _VRtrIfCpmProtPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 68),
    _VRtrIfCpmProtPolicyId_Type()
)
vRtrIfCpmProtPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfCpmProtPolicyId.setStatus("current")
_VRtrIfCpmProtUncfgdProtoDropCnt_Type = Gauge32
_VRtrIfCpmProtUncfgdProtoDropCnt_Object = MibTableColumn
vRtrIfCpmProtUncfgdProtoDropCnt = _VRtrIfCpmProtUncfgdProtoDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 69),
    _VRtrIfCpmProtUncfgdProtoDropCnt_Type()
)
vRtrIfCpmProtUncfgdProtoDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfCpmProtUncfgdProtoDropCnt.setStatus("current")


class _VRtrIfLdpSyncTimer_Type(Unsigned32):
    """Custom type vRtrIfLdpSyncTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1800),
    )


_VRtrIfLdpSyncTimer_Type.__name__ = "Unsigned32"
_VRtrIfLdpSyncTimer_Object = MibTableColumn
vRtrIfLdpSyncTimer = _VRtrIfLdpSyncTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 70),
    _VRtrIfLdpSyncTimer_Type()
)
vRtrIfLdpSyncTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfLdpSyncTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfLdpSyncTimer.setUnits("seconds")


class _VRtrIfStripLabel_Type(TruthValue):
    """Custom type vRtrIfStripLabel based on TruthValue"""
    defaultValue = 2


_VRtrIfStripLabel_Type.__name__ = "TruthValue"
_VRtrIfStripLabel_Object = MibTableColumn
vRtrIfStripLabel = _VRtrIfStripLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 71),
    _VRtrIfStripLabel_Type()
)
vRtrIfStripLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfStripLabel.setStatus("current")


class _VRtrIfuRPFCheckState_Type(TmnxEnabledDisabled):
    """Custom type vRtrIfuRPFCheckState based on TmnxEnabledDisabled"""
    defaultValue = 2


_VRtrIfuRPFCheckState_Type.__name__ = "TmnxEnabledDisabled"
_VRtrIfuRPFCheckState_Object = MibTableColumn
vRtrIfuRPFCheckState = _VRtrIfuRPFCheckState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 72),
    _VRtrIfuRPFCheckState_Type()
)
vRtrIfuRPFCheckState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfuRPFCheckState.setStatus("current")


class _VRtrIfuRPFCheckMode_Type(Integer32):
    """Custom type vRtrIfuRPFCheckMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("loose", 2))
    )


_VRtrIfuRPFCheckMode_Type.__name__ = "Integer32"
_VRtrIfuRPFCheckMode_Object = MibTableColumn
vRtrIfuRPFCheckMode = _VRtrIfuRPFCheckMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 73),
    _VRtrIfuRPFCheckMode_Type()
)
vRtrIfuRPFCheckMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfuRPFCheckMode.setStatus("current")


class _VRtrIfQosQGrp_Type(TNamedItemOrEmpty):
    """Custom type vRtrIfQosQGrp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrIfQosQGrp_Type.__name__ = "TNamedItemOrEmpty"
_VRtrIfQosQGrp_Object = MibTableColumn
vRtrIfQosQGrp = _VRtrIfQosQGrp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 74),
    _VRtrIfQosQGrp_Type()
)
vRtrIfQosQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfQosQGrp.setStatus("obsolete")


class _VRtrIfAdminLinkLocalAddrType_Type(InetAddressType):
    """Custom type vRtrIfAdminLinkLocalAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrIfAdminLinkLocalAddrType_Type.__name__ = "InetAddressType"
_VRtrIfAdminLinkLocalAddrType_Object = MibTableColumn
vRtrIfAdminLinkLocalAddrType = _VRtrIfAdminLinkLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 75),
    _VRtrIfAdminLinkLocalAddrType_Type()
)
vRtrIfAdminLinkLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfAdminLinkLocalAddrType.setStatus("current")


class _VRtrIfAdminLinkLocalAddr_Type(InetAddress):
    """Custom type vRtrIfAdminLinkLocalAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )


_VRtrIfAdminLinkLocalAddr_Type.__name__ = "InetAddress"
_VRtrIfAdminLinkLocalAddr_Object = MibTableColumn
vRtrIfAdminLinkLocalAddr = _VRtrIfAdminLinkLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 76),
    _VRtrIfAdminLinkLocalAddr_Type()
)
vRtrIfAdminLinkLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfAdminLinkLocalAddr.setStatus("current")


class _VRtrIfAdmLnkLclAddrPreferred_Type(TruthValue):
    """Custom type vRtrIfAdmLnkLclAddrPreferred based on TruthValue"""
    defaultValue = 2


_VRtrIfAdmLnkLclAddrPreferred_Type.__name__ = "TruthValue"
_VRtrIfAdmLnkLclAddrPreferred_Object = MibTableColumn
vRtrIfAdmLnkLclAddrPreferred = _VRtrIfAdmLnkLclAddrPreferred_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 77),
    _VRtrIfAdmLnkLclAddrPreferred_Type()
)
vRtrIfAdmLnkLclAddrPreferred.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfAdmLnkLclAddrPreferred.setStatus("current")


class _VRtrIfOperDownReason_Type(Bits):
    """Custom type vRtrIfOperDownReason based on Bits"""
    namedValues = NamedValues(
        *(("ifAdminDown", 0),
          ("svcAdminDown", 1),
          ("portOperDown", 2),
          ("addrOrIfNotReady", 3),
          ("assocObjNotReady", 4),
          ("rvplsDown", 5),
          ("operGrpDown", 6),
          ("ifAdminDestroy", 7),
          ("noIfAddress", 8),
          ("noIfInfo", 9),
          ("delayedStartEnabled", 10),
          ("ifProtoOperDown", 11),
          ("invalidPortCfg", 12),
          ("unknown", 13),
          ("ipv6Misconfig", 14))
    )

_VRtrIfOperDownReason_Type.__name__ = "Bits"
_VRtrIfOperDownReason_Object = MibTableColumn
vRtrIfOperDownReason = _VRtrIfOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 4, 1, 78),
    _VRtrIfOperDownReason_Type()
)
vRtrIfOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfOperDownReason.setStatus("current")
_VRtrIfNameTable_Object = MibTable
vRtrIfNameTable = _VRtrIfNameTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    vRtrIfNameTable.setStatus("current")
_VRtrIfNameEntry_Object = MibTableRow
vRtrIfNameEntry = _VRtrIfNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 5, 1)
)
vRtrIfNameEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (1, "TN-VRTR-MIB", "vRtrIfName"),
)
if mibBuilder.loadTexts:
    vRtrIfNameEntry.setStatus("current")
_VRtrIfNameIndex_Type = InterfaceIndex
_VRtrIfNameIndex_Object = MibTableColumn
vRtrIfNameIndex = _VRtrIfNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 5, 1, 1),
    _VRtrIfNameIndex_Type()
)
vRtrIfNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfNameIndex.setStatus("current")
_VRtrIpAddrTable_Object = MibTable
vRtrIpAddrTable = _VRtrIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    vRtrIpAddrTable.setStatus("current")
_VRtrIpAddrEntry_Object = MibTableRow
vRtrIpAddrEntry = _VRtrIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1)
)
vRtrIpAddrEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (0, "TN-VRTR-MIB", "vRtrIfIndex"),
    (0, "TN-VRTR-MIB", "vRiaIndex"),
)
if mibBuilder.loadTexts:
    vRtrIpAddrEntry.setStatus("current")


class _VRiaIndex_Type(Integer32):
    """Custom type vRiaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_VRiaIndex_Type.__name__ = "Integer32"
_VRiaIndex_Object = MibTableColumn
vRiaIndex = _VRiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 1),
    _VRiaIndex_Type()
)
vRiaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRiaIndex.setStatus("current")
_VRiaRowStatus_Type = RowStatus
_VRiaRowStatus_Object = MibTableColumn
vRiaRowStatus = _VRiaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 2),
    _VRiaRowStatus_Type()
)
vRiaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaRowStatus.setStatus("current")
_VRiaIpAddress_Type = IpAddress
_VRiaIpAddress_Object = MibTableColumn
vRiaIpAddress = _VRiaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 3),
    _VRiaIpAddress_Type()
)
vRiaIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaIpAddress.setStatus("current")


class _VRiaNetMask_Type(IpAddress):
    """Custom type vRiaNetMask based on IpAddress"""
    defaultHexValue = "FFFFFF00"


_VRiaNetMask_Type.__name__ = "IpAddress"
_VRiaNetMask_Object = MibTableColumn
vRiaNetMask = _VRiaNetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 4),
    _VRiaNetMask_Type()
)
vRiaNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaNetMask.setStatus("current")


class _VRiaBcastAddrFormat_Type(Integer32):
    """Custom type vRiaBcastAddrFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 1),
          ("hostOnes", 2))
    )


_VRiaBcastAddrFormat_Type.__name__ = "Integer32"
_VRiaBcastAddrFormat_Object = MibTableColumn
vRiaBcastAddrFormat = _VRiaBcastAddrFormat_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 5),
    _VRiaBcastAddrFormat_Type()
)
vRiaBcastAddrFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaBcastAddrFormat.setStatus("current")


class _VRiaReasmMaxSize_Type(Integer32):
    """Custom type vRiaReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRiaReasmMaxSize_Type.__name__ = "Integer32"
_VRiaReasmMaxSize_Object = MibTableColumn
vRiaReasmMaxSize = _VRiaReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 6),
    _VRiaReasmMaxSize_Type()
)
vRiaReasmMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaReasmMaxSize.setStatus("current")
_VRiaIgpInhibit_Type = TruthValue
_VRiaIgpInhibit_Object = MibTableColumn
vRiaIgpInhibit = _VRiaIgpInhibit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 7),
    _VRiaIgpInhibit_Type()
)
vRiaIgpInhibit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaIgpInhibit.setStatus("current")
_VRiaInetAddressType_Type = InetAddressType
_VRiaInetAddressType_Object = MibTableColumn
vRiaInetAddressType = _VRiaInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 8),
    _VRiaInetAddressType_Type()
)
vRiaInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetAddressType.setStatus("current")


class _VRiaInetAddress_Type(InetAddress):
    """Custom type vRiaInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRiaInetAddress_Type.__name__ = "InetAddress"
_VRiaInetAddress_Object = MibTableColumn
vRiaInetAddress = _VRiaInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 9),
    _VRiaInetAddress_Type()
)
vRiaInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetAddress.setStatus("current")
_VRiaInetPrefixLen_Type = InetAddressPrefixLength
_VRiaInetPrefixLen_Object = MibTableColumn
vRiaInetPrefixLen = _VRiaInetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 10),
    _VRiaInetPrefixLen_Type()
)
vRiaInetPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetPrefixLen.setStatus("current")
_VRiaInetAddrState_Type = TmnxInetAddrState
_VRiaInetAddrState_Object = MibTableColumn
vRiaInetAddrState = _VRiaInetAddrState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 11),
    _VRiaInetAddrState_Type()
)
vRiaInetAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRiaInetAddrState.setStatus("current")


class _VRiaInetEui64_Type(TruthValue):
    """Custom type vRiaInetEui64 based on TruthValue"""
    defaultValue = 2


_VRiaInetEui64_Type.__name__ = "TruthValue"
_VRiaInetEui64_Object = MibTableColumn
vRiaInetEui64 = _VRiaInetEui64_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 12),
    _VRiaInetEui64_Type()
)
vRiaInetEui64.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetEui64.setStatus("current")
_VRiaInetOperAddress_Type = InetAddress
_VRiaInetOperAddress_Object = MibTableColumn
vRiaInetOperAddress = _VRiaInetOperAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 13),
    _VRiaInetOperAddress_Type()
)
vRiaInetOperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRiaInetOperAddress.setStatus("current")


class _VRiaInetGwAddressType_Type(InetAddressType):
    """Custom type vRiaInetGwAddressType based on InetAddressType"""
    defaultValue = 0


_VRiaInetGwAddressType_Type.__name__ = "InetAddressType"
_VRiaInetGwAddressType_Object = MibTableColumn
vRiaInetGwAddressType = _VRiaInetGwAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 14),
    _VRiaInetGwAddressType_Type()
)
vRiaInetGwAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetGwAddressType.setStatus("current")


class _VRiaInetGwAddress_Type(InetAddress):
    """Custom type vRiaInetGwAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRiaInetGwAddress_Type.__name__ = "InetAddress"
_VRiaInetGwAddress_Object = MibTableColumn
vRiaInetGwAddress = _VRiaInetGwAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 15),
    _VRiaInetGwAddress_Type()
)
vRiaInetGwAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetGwAddress.setStatus("current")


class _VRiaInetRemoteIpType_Type(InetAddressType):
    """Custom type vRiaInetRemoteIpType based on InetAddressType"""
    defaultValue = 0


_VRiaInetRemoteIpType_Type.__name__ = "InetAddressType"
_VRiaInetRemoteIpType_Object = MibTableColumn
vRiaInetRemoteIpType = _VRiaInetRemoteIpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 16),
    _VRiaInetRemoteIpType_Type()
)
vRiaInetRemoteIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetRemoteIpType.setStatus("current")


class _VRiaInetRemoteIp_Type(InetAddress):
    """Custom type vRiaInetRemoteIp based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRiaInetRemoteIp_Type.__name__ = "InetAddress"
_VRiaInetRemoteIp_Object = MibTableColumn
vRiaInetRemoteIp = _VRiaInetRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 17),
    _VRiaInetRemoteIp_Type()
)
vRiaInetRemoteIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetRemoteIp.setStatus("current")


class _VRiaInetAddrPreferred_Type(TruthValue):
    """Custom type vRiaInetAddrPreferred based on TruthValue"""
    defaultValue = 2


_VRiaInetAddrPreferred_Type.__name__ = "TruthValue"
_VRiaInetAddrPreferred_Object = MibTableColumn
vRiaInetAddrPreferred = _VRiaInetAddrPreferred_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 18),
    _VRiaInetAddrPreferred_Type()
)
vRiaInetAddrPreferred.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetAddrPreferred.setStatus("current")


class _VRiaSubscrPrefix_Type(TruthValue):
    """Custom type vRiaSubscrPrefix based on TruthValue"""
    defaultValue = 2


_VRiaSubscrPrefix_Type.__name__ = "TruthValue"
_VRiaSubscrPrefix_Object = MibTableColumn
vRiaSubscrPrefix = _VRiaSubscrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 19),
    _VRiaSubscrPrefix_Type()
)
vRiaSubscrPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaSubscrPrefix.setStatus("current")


class _VRiaSubscrPrefixType_Type(Bits):
    """Custom type vRiaSubscrPrefixType based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("pd", 0),
          ("wan-host", 1))
    )

_VRiaSubscrPrefixType_Type.__name__ = "Bits"
_VRiaSubscrPrefixType_Object = MibTableColumn
vRiaSubscrPrefixType = _VRiaSubscrPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 20),
    _VRiaSubscrPrefixType_Type()
)
vRiaSubscrPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaSubscrPrefixType.setStatus("current")


class _VRiaSubscrHostRoutePopulate_Type(TruthValue):
    """Custom type vRiaSubscrHostRoutePopulate based on TruthValue"""
    defaultValue = 2


_VRiaSubscrHostRoutePopulate_Type.__name__ = "TruthValue"
_VRiaSubscrHostRoutePopulate_Object = MibTableColumn
vRiaSubscrHostRoutePopulate = _VRiaSubscrHostRoutePopulate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 21),
    _VRiaSubscrHostRoutePopulate_Type()
)
vRiaSubscrHostRoutePopulate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaSubscrHostRoutePopulate.setStatus("current")


class _VRiaTrackSrrpInstance_Type(Unsigned32):
    """Custom type vRiaTrackSrrpInstance based on Unsigned32"""
    defaultValue = 0


_VRiaTrackSrrpInstance_Type.__name__ = "Unsigned32"
_VRiaTrackSrrpInstance_Object = MibTableColumn
vRiaTrackSrrpInstance = _VRiaTrackSrrpInstance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 22),
    _VRiaTrackSrrpInstance_Type()
)
vRiaTrackSrrpInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaTrackSrrpInstance.setStatus("current")


class _VRiaHoldUpTime_Type(Unsigned32):
    """Custom type vRiaHoldUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 5000),
    )


_VRiaHoldUpTime_Type.__name__ = "Unsigned32"
_VRiaHoldUpTime_Object = MibTableColumn
vRiaHoldUpTime = _VRiaHoldUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 6, 1, 23),
    _VRiaHoldUpTime_Type()
)
vRiaHoldUpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaHoldUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRiaHoldUpTime.setUnits("milli-seconds")
_TnVRtrGlobalObjs_ObjectIdentity = ObjectIdentity
tnVRtrGlobalObjs = _TnVRtrGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 15)
)
_VRtrNextVRtrID_Type = TestAndIncr
_VRtrNextVRtrID_Object = MibScalar
vRtrNextVRtrID = _VRtrNextVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 15, 1),
    _VRtrNextVRtrID_Type()
)
vRtrNextVRtrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrNextVRtrID.setStatus("current")
_VRtrConfiguredVRtrs_Type = Gauge32
_VRtrConfiguredVRtrs_Object = MibScalar
vRtrConfiguredVRtrs = _VRtrConfiguredVRtrs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 15, 2),
    _VRtrConfiguredVRtrs_Type()
)
vRtrConfiguredVRtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrConfiguredVRtrs.setStatus("current")
_VRtrActiveVRtrs_Type = Gauge32
_VRtrActiveVRtrs_Object = MibScalar
vRtrActiveVRtrs = _VRtrActiveVRtrs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 15, 3),
    _VRtrActiveVRtrs_Type()
)
vRtrActiveVRtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrActiveVRtrs.setStatus("current")


class _VRtrRouteThresholdSoakTime_Type(Unsigned32):
    """Custom type vRtrRouteThresholdSoakTime based on Unsigned32"""
    defaultValue = 600


_VRtrRouteThresholdSoakTime_Type.__name__ = "Unsigned32"
_VRtrRouteThresholdSoakTime_Object = MibScalar
vRtrRouteThresholdSoakTime = _VRtrRouteThresholdSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 15, 4),
    _VRtrRouteThresholdSoakTime_Type()
)
vRtrRouteThresholdSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrRouteThresholdSoakTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRouteThresholdSoakTime.setUnits("seconds")
_VRtrMaxARPEntries_Type = Unsigned32
_VRtrMaxARPEntries_Object = MibScalar
vRtrMaxARPEntries = _VRtrMaxARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 15, 5),
    _VRtrMaxARPEntries_Type()
)
vRtrMaxARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMaxARPEntries.setStatus("current")


class _VRtrIPv6RouteThresholdSoakTime_Type(Unsigned32):
    """Custom type vRtrIPv6RouteThresholdSoakTime based on Unsigned32"""
    defaultValue = 600


_VRtrIPv6RouteThresholdSoakTime_Type.__name__ = "Unsigned32"
_VRtrIPv6RouteThresholdSoakTime_Object = MibScalar
vRtrIPv6RouteThresholdSoakTime = _VRtrIPv6RouteThresholdSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 15, 6),
    _VRtrIPv6RouteThresholdSoakTime_Type()
)
vRtrIPv6RouteThresholdSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIPv6RouteThresholdSoakTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIPv6RouteThresholdSoakTime.setUnits("seconds")
_VRtrIfGlobalIndexTable_Object = MibTable
vRtrIfGlobalIndexTable = _VRtrIfGlobalIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 37)
)
if mibBuilder.loadTexts:
    vRtrIfGlobalIndexTable.setStatus("current")
_VRtrIfGlobalIndexEntry_Object = MibTableRow
vRtrIfGlobalIndexEntry = _VRtrIfGlobalIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 37, 1)
)
vRtrIfGlobalIndexEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrIfGlobalIndex"),
)
if mibBuilder.loadTexts:
    vRtrIfGlobalIndexEntry.setStatus("current")
_VRtrIfGlobalIndexvRtrID_Type = TmnxVRtrID
_VRtrIfGlobalIndexvRtrID_Object = MibTableColumn
vRtrIfGlobalIndexvRtrID = _VRtrIfGlobalIndexvRtrID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 37, 1, 1),
    _VRtrIfGlobalIndexvRtrID_Type()
)
vRtrIfGlobalIndexvRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfGlobalIndexvRtrID.setStatus("current")
_VRtrIfGlobalIndexvRtrIfIndex_Type = InterfaceIndex
_VRtrIfGlobalIndexvRtrIfIndex_Object = MibTableColumn
vRtrIfGlobalIndexvRtrIfIndex = _VRtrIfGlobalIndexvRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 37, 1, 2),
    _VRtrIfGlobalIndexvRtrIfIndex_Type()
)
vRtrIfGlobalIndexvRtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfGlobalIndexvRtrIfIndex.setStatus("current")
_VRtrIfStatsTable_Object = MibTable
vRtrIfStatsTable = _VRtrIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54)
)
if mibBuilder.loadTexts:
    vRtrIfStatsTable.setStatus("current")
_VRtrIfStatsEntry_Object = MibTableRow
vRtrIfStatsEntry = _VRtrIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1)
)
vRtrIfStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (0, "TN-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrIfStatsEntry.setStatus("current")
_VRtrIfuRPFCheckFailPkts_Type = Counter64
_VRtrIfuRPFCheckFailPkts_Object = MibTableColumn
vRtrIfuRPFCheckFailPkts = _VRtrIfuRPFCheckFailPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 1),
    _VRtrIfuRPFCheckFailPkts_Type()
)
vRtrIfuRPFCheckFailPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfuRPFCheckFailPkts.setStatus("current")
_VRtrIfuRPFCheckFailPktsLow32_Type = Counter32
_VRtrIfuRPFCheckFailPktsLow32_Object = MibTableColumn
vRtrIfuRPFCheckFailPktsLow32 = _VRtrIfuRPFCheckFailPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 2),
    _VRtrIfuRPFCheckFailPktsLow32_Type()
)
vRtrIfuRPFCheckFailPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfuRPFCheckFailPktsLow32.setStatus("current")
_VRtrIfuRPFCheckFailPktsHigh32_Type = Counter32
_VRtrIfuRPFCheckFailPktsHigh32_Object = MibTableColumn
vRtrIfuRPFCheckFailPktsHigh32 = _VRtrIfuRPFCheckFailPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 3),
    _VRtrIfuRPFCheckFailPktsHigh32_Type()
)
vRtrIfuRPFCheckFailPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfuRPFCheckFailPktsHigh32.setStatus("current")
_VRtrIfuRPFCheckFailBytes_Type = Counter64
_VRtrIfuRPFCheckFailBytes_Object = MibTableColumn
vRtrIfuRPFCheckFailBytes = _VRtrIfuRPFCheckFailBytes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 4),
    _VRtrIfuRPFCheckFailBytes_Type()
)
vRtrIfuRPFCheckFailBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfuRPFCheckFailBytes.setStatus("current")
_VRtrIfuRPFCheckFailBytesLow32_Type = Counter32
_VRtrIfuRPFCheckFailBytesLow32_Object = MibTableColumn
vRtrIfuRPFCheckFailBytesLow32 = _VRtrIfuRPFCheckFailBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 5),
    _VRtrIfuRPFCheckFailBytesLow32_Type()
)
vRtrIfuRPFCheckFailBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfuRPFCheckFailBytesLow32.setStatus("current")
_VRtrIfuRPFCheckFailBytesHigh32_Type = Counter32
_VRtrIfuRPFCheckFailBytesHigh32_Object = MibTableColumn
vRtrIfuRPFCheckFailBytesHigh32 = _VRtrIfuRPFCheckFailBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 6),
    _VRtrIfuRPFCheckFailBytesHigh32_Type()
)
vRtrIfuRPFCheckFailBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfuRPFCheckFailBytesHigh32.setStatus("current")
_VRtrIfIpReasFragPktsRcvd_Type = Counter64
_VRtrIfIpReasFragPktsRcvd_Object = MibTableColumn
vRtrIfIpReasFragPktsRcvd = _VRtrIfIpReasFragPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 7),
    _VRtrIfIpReasFragPktsRcvd_Type()
)
vRtrIfIpReasFragPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragPktsRcvd.setStatus("current")
_VRtrIfIpReasFragPktsRcvdLow32_Type = Counter32
_VRtrIfIpReasFragPktsRcvdLow32_Object = MibTableColumn
vRtrIfIpReasFragPktsRcvdLow32 = _VRtrIfIpReasFragPktsRcvdLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 8),
    _VRtrIfIpReasFragPktsRcvdLow32_Type()
)
vRtrIfIpReasFragPktsRcvdLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragPktsRcvdLow32.setStatus("current")
_VRtrIfIpReasFragPktsRcvdHigh32_Type = Counter32
_VRtrIfIpReasFragPktsRcvdHigh32_Object = MibTableColumn
vRtrIfIpReasFragPktsRcvdHigh32 = _VRtrIfIpReasFragPktsRcvdHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 9),
    _VRtrIfIpReasFragPktsRcvdHigh32_Type()
)
vRtrIfIpReasFragPktsRcvdHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragPktsRcvdHigh32.setStatus("current")
_VRtrIfIpReasFragBytesRcvd_Type = Counter64
_VRtrIfIpReasFragBytesRcvd_Object = MibTableColumn
vRtrIfIpReasFragBytesRcvd = _VRtrIfIpReasFragBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 10),
    _VRtrIfIpReasFragBytesRcvd_Type()
)
vRtrIfIpReasFragBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragBytesRcvd.setStatus("current")
_VRtrIfIpReasFragBytesRcvdLow32_Type = Counter32
_VRtrIfIpReasFragBytesRcvdLow32_Object = MibTableColumn
vRtrIfIpReasFragBytesRcvdLow32 = _VRtrIfIpReasFragBytesRcvdLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 11),
    _VRtrIfIpReasFragBytesRcvdLow32_Type()
)
vRtrIfIpReasFragBytesRcvdLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragBytesRcvdLow32.setStatus("current")
_VRtrIfIpReasFragBytesRcvdHigh32_Type = Counter32
_VRtrIfIpReasFragBytesRcvdHigh32_Object = MibTableColumn
vRtrIfIpReasFragBytesRcvdHigh32 = _VRtrIfIpReasFragBytesRcvdHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 12),
    _VRtrIfIpReasFragBytesRcvdHigh32_Type()
)
vRtrIfIpReasFragBytesRcvdHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragBytesRcvdHigh32.setStatus("current")
_VRtrIfIpReasFragPktsReas_Type = Counter64
_VRtrIfIpReasFragPktsReas_Object = MibTableColumn
vRtrIfIpReasFragPktsReas = _VRtrIfIpReasFragPktsReas_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 13),
    _VRtrIfIpReasFragPktsReas_Type()
)
vRtrIfIpReasFragPktsReas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragPktsReas.setStatus("current")
_VRtrIfIpReasFragPktsReasLow32_Type = Counter32
_VRtrIfIpReasFragPktsReasLow32_Object = MibTableColumn
vRtrIfIpReasFragPktsReasLow32 = _VRtrIfIpReasFragPktsReasLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 14),
    _VRtrIfIpReasFragPktsReasLow32_Type()
)
vRtrIfIpReasFragPktsReasLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragPktsReasLow32.setStatus("current")
_VRtrIfIpReasFragPktsReasHigh32_Type = Counter32
_VRtrIfIpReasFragPktsReasHigh32_Object = MibTableColumn
vRtrIfIpReasFragPktsReasHigh32 = _VRtrIfIpReasFragPktsReasHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 15),
    _VRtrIfIpReasFragPktsReasHigh32_Type()
)
vRtrIfIpReasFragPktsReasHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragPktsReasHigh32.setStatus("current")
_VRtrIfIpReasFragBytesReas_Type = Counter64
_VRtrIfIpReasFragBytesReas_Object = MibTableColumn
vRtrIfIpReasFragBytesReas = _VRtrIfIpReasFragBytesReas_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 16),
    _VRtrIfIpReasFragBytesReas_Type()
)
vRtrIfIpReasFragBytesReas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragBytesReas.setStatus("current")
_VRtrIfIpReasFragBytesReasLow32_Type = Counter32
_VRtrIfIpReasFragBytesReasLow32_Object = MibTableColumn
vRtrIfIpReasFragBytesReasLow32 = _VRtrIfIpReasFragBytesReasLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 17),
    _VRtrIfIpReasFragBytesReasLow32_Type()
)
vRtrIfIpReasFragBytesReasLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragBytesReasLow32.setStatus("current")
_VRtrIfIpReasFragBytesReasHigh32_Type = Counter32
_VRtrIfIpReasFragBytesReasHigh32_Object = MibTableColumn
vRtrIfIpReasFragBytesReasHigh32 = _VRtrIfIpReasFragBytesReasHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 18),
    _VRtrIfIpReasFragBytesReasHigh32_Type()
)
vRtrIfIpReasFragBytesReasHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragBytesReasHigh32.setStatus("current")
_VRtrIfIpReasFragReasErrors_Type = Counter64
_VRtrIfIpReasFragReasErrors_Object = MibTableColumn
vRtrIfIpReasFragReasErrors = _VRtrIfIpReasFragReasErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 19),
    _VRtrIfIpReasFragReasErrors_Type()
)
vRtrIfIpReasFragReasErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragReasErrors.setStatus("current")
_VRtrIfIpReasFragReasErrorsLow32_Type = Counter32
_VRtrIfIpReasFragReasErrorsLow32_Object = MibTableColumn
vRtrIfIpReasFragReasErrorsLow32 = _VRtrIfIpReasFragReasErrorsLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 20),
    _VRtrIfIpReasFragReasErrorsLow32_Type()
)
vRtrIfIpReasFragReasErrorsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragReasErrorsLow32.setStatus("current")
_VRtrIfIpReasFragReasErrorsHigh32_Type = Counter32
_VRtrIfIpReasFragReasErrorsHigh32_Object = MibTableColumn
vRtrIfIpReasFragReasErrorsHigh32 = _VRtrIfIpReasFragReasErrorsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 21),
    _VRtrIfIpReasFragReasErrorsHigh32_Type()
)
vRtrIfIpReasFragReasErrorsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragReasErrorsHigh32.setStatus("current")
_VRtrIfIpReasFragDisc_Type = Counter64
_VRtrIfIpReasFragDisc_Object = MibTableColumn
vRtrIfIpReasFragDisc = _VRtrIfIpReasFragDisc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 22),
    _VRtrIfIpReasFragDisc_Type()
)
vRtrIfIpReasFragDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragDisc.setStatus("current")
_VRtrIfIpReasFragDiscLow32_Type = Counter32
_VRtrIfIpReasFragDiscLow32_Object = MibTableColumn
vRtrIfIpReasFragDiscLow32 = _VRtrIfIpReasFragDiscLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 23),
    _VRtrIfIpReasFragDiscLow32_Type()
)
vRtrIfIpReasFragDiscLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragDiscLow32.setStatus("current")
_VRtrIfIpReasFragDiscHigh32_Type = Counter32
_VRtrIfIpReasFragDiscHigh32_Object = MibTableColumn
vRtrIfIpReasFragDiscHigh32 = _VRtrIfIpReasFragDiscHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 24),
    _VRtrIfIpReasFragDiscHigh32_Type()
)
vRtrIfIpReasFragDiscHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasFragDiscHigh32.setStatus("current")
_VRtrIfIpReasOutBufRes_Type = Counter64
_VRtrIfIpReasOutBufRes_Object = MibTableColumn
vRtrIfIpReasOutBufRes = _VRtrIfIpReasOutBufRes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 25),
    _VRtrIfIpReasOutBufRes_Type()
)
vRtrIfIpReasOutBufRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasOutBufRes.setStatus("current")
_VRtrIfIpReasOutBufResLow32_Type = Counter32
_VRtrIfIpReasOutBufResLow32_Object = MibTableColumn
vRtrIfIpReasOutBufResLow32 = _VRtrIfIpReasOutBufResLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 26),
    _VRtrIfIpReasOutBufResLow32_Type()
)
vRtrIfIpReasOutBufResLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasOutBufResLow32.setStatus("current")
_VRtrIfIpReasOutBufResHigh32_Type = Counter32
_VRtrIfIpReasOutBufResHigh32_Object = MibTableColumn
vRtrIfIpReasOutBufResHigh32 = _VRtrIfIpReasOutBufResHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 27),
    _VRtrIfIpReasOutBufResHigh32_Type()
)
vRtrIfIpReasOutBufResHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasOutBufResHigh32.setStatus("current")
_VRtrIfIpReasPktsRx_Type = Counter64
_VRtrIfIpReasPktsRx_Object = MibTableColumn
vRtrIfIpReasPktsRx = _VRtrIfIpReasPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 28),
    _VRtrIfIpReasPktsRx_Type()
)
vRtrIfIpReasPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasPktsRx.setStatus("current")
_VRtrIfIpReasPktsRxLow32_Type = Counter32
_VRtrIfIpReasPktsRxLow32_Object = MibTableColumn
vRtrIfIpReasPktsRxLow32 = _VRtrIfIpReasPktsRxLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 29),
    _VRtrIfIpReasPktsRxLow32_Type()
)
vRtrIfIpReasPktsRxLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasPktsRxLow32.setStatus("current")
_VRtrIfIpReasPktsRxHigh32_Type = Counter32
_VRtrIfIpReasPktsRxHigh32_Object = MibTableColumn
vRtrIfIpReasPktsRxHigh32 = _VRtrIfIpReasPktsRxHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 30),
    _VRtrIfIpReasPktsRxHigh32_Type()
)
vRtrIfIpReasPktsRxHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasPktsRxHigh32.setStatus("current")
_VRtrIfIpReasBytesRx_Type = Counter64
_VRtrIfIpReasBytesRx_Object = MibTableColumn
vRtrIfIpReasBytesRx = _VRtrIfIpReasBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 31),
    _VRtrIfIpReasBytesRx_Type()
)
vRtrIfIpReasBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasBytesRx.setStatus("current")
_VRtrIfIpReasBytesRxLow32_Type = Counter32
_VRtrIfIpReasBytesRxLow32_Object = MibTableColumn
vRtrIfIpReasBytesRxLow32 = _VRtrIfIpReasBytesRxLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 32),
    _VRtrIfIpReasBytesRxLow32_Type()
)
vRtrIfIpReasBytesRxLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasBytesRxLow32.setStatus("current")
_VRtrIfIpReasBytesRxHigh32_Type = Counter32
_VRtrIfIpReasBytesRxHigh32_Object = MibTableColumn
vRtrIfIpReasBytesRxHigh32 = _VRtrIfIpReasBytesRxHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 33),
    _VRtrIfIpReasBytesRxHigh32_Type()
)
vRtrIfIpReasBytesRxHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasBytesRxHigh32.setStatus("current")
_VRtrIfIpReasPktsTx_Type = Counter64
_VRtrIfIpReasPktsTx_Object = MibTableColumn
vRtrIfIpReasPktsTx = _VRtrIfIpReasPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 34),
    _VRtrIfIpReasPktsTx_Type()
)
vRtrIfIpReasPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasPktsTx.setStatus("current")
_VRtrIfIpReasPktsTxLow32_Type = Counter32
_VRtrIfIpReasPktsTxLow32_Object = MibTableColumn
vRtrIfIpReasPktsTxLow32 = _VRtrIfIpReasPktsTxLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 35),
    _VRtrIfIpReasPktsTxLow32_Type()
)
vRtrIfIpReasPktsTxLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasPktsTxLow32.setStatus("current")
_VRtrIfIpReasPktsTxHigh32_Type = Counter32
_VRtrIfIpReasPktsTxHigh32_Object = MibTableColumn
vRtrIfIpReasPktsTxHigh32 = _VRtrIfIpReasPktsTxHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 36),
    _VRtrIfIpReasPktsTxHigh32_Type()
)
vRtrIfIpReasPktsTxHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasPktsTxHigh32.setStatus("current")
_VRtrIfIpReasBytesTx_Type = Counter64
_VRtrIfIpReasBytesTx_Object = MibTableColumn
vRtrIfIpReasBytesTx = _VRtrIfIpReasBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 37),
    _VRtrIfIpReasBytesTx_Type()
)
vRtrIfIpReasBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasBytesTx.setStatus("current")
_VRtrIfIpReasBytesTxLow32_Type = Counter32
_VRtrIfIpReasBytesTxLow32_Object = MibTableColumn
vRtrIfIpReasBytesTxLow32 = _VRtrIfIpReasBytesTxLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 38),
    _VRtrIfIpReasBytesTxLow32_Type()
)
vRtrIfIpReasBytesTxLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasBytesTxLow32.setStatus("current")
_VRtrIfIpReasBytesTxHigh32_Type = Counter32
_VRtrIfIpReasBytesTxHigh32_Object = MibTableColumn
vRtrIfIpReasBytesTxHigh32 = _VRtrIfIpReasBytesTxHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 39),
    _VRtrIfIpReasBytesTxHigh32_Type()
)
vRtrIfIpReasBytesTxHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasBytesTxHigh32.setStatus("current")
_VRtrIfRxPkts_Type = Counter64
_VRtrIfRxPkts_Object = MibTableColumn
vRtrIfRxPkts = _VRtrIfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 40),
    _VRtrIfRxPkts_Type()
)
vRtrIfRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfRxPkts.setStatus("current")
_VRtrIfRxPktsLow32_Type = Counter32
_VRtrIfRxPktsLow32_Object = MibTableColumn
vRtrIfRxPktsLow32 = _VRtrIfRxPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 41),
    _VRtrIfRxPktsLow32_Type()
)
vRtrIfRxPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfRxPktsLow32.setStatus("current")
_VRtrIfRxPktsHigh32_Type = Counter32
_VRtrIfRxPktsHigh32_Object = MibTableColumn
vRtrIfRxPktsHigh32 = _VRtrIfRxPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 42),
    _VRtrIfRxPktsHigh32_Type()
)
vRtrIfRxPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfRxPktsHigh32.setStatus("current")
_VRtrIfRxBytes_Type = Counter64
_VRtrIfRxBytes_Object = MibTableColumn
vRtrIfRxBytes = _VRtrIfRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 43),
    _VRtrIfRxBytes_Type()
)
vRtrIfRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfRxBytes.setStatus("current")
_VRtrIfRxBytesLow32_Type = Counter32
_VRtrIfRxBytesLow32_Object = MibTableColumn
vRtrIfRxBytesLow32 = _VRtrIfRxBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 44),
    _VRtrIfRxBytesLow32_Type()
)
vRtrIfRxBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfRxBytesLow32.setStatus("current")
_VRtrIfRxBytesHigh32_Type = Counter32
_VRtrIfRxBytesHigh32_Object = MibTableColumn
vRtrIfRxBytesHigh32 = _VRtrIfRxBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 45),
    _VRtrIfRxBytesHigh32_Type()
)
vRtrIfRxBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfRxBytesHigh32.setStatus("current")
_VRtrIfTxV4Pkts_Type = Counter64
_VRtrIfTxV4Pkts_Object = MibTableColumn
vRtrIfTxV4Pkts = _VRtrIfTxV4Pkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 46),
    _VRtrIfTxV4Pkts_Type()
)
vRtrIfTxV4Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV4Pkts.setStatus("current")
_VRtrIfTxV4PktsLow32_Type = Counter32
_VRtrIfTxV4PktsLow32_Object = MibTableColumn
vRtrIfTxV4PktsLow32 = _VRtrIfTxV4PktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 47),
    _VRtrIfTxV4PktsLow32_Type()
)
vRtrIfTxV4PktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV4PktsLow32.setStatus("current")
_VRtrIfTxV4PktsHigh32_Type = Counter32
_VRtrIfTxV4PktsHigh32_Object = MibTableColumn
vRtrIfTxV4PktsHigh32 = _VRtrIfTxV4PktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 48),
    _VRtrIfTxV4PktsHigh32_Type()
)
vRtrIfTxV4PktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV4PktsHigh32.setStatus("current")
_VRtrIfTxV4Bytes_Type = Counter64
_VRtrIfTxV4Bytes_Object = MibTableColumn
vRtrIfTxV4Bytes = _VRtrIfTxV4Bytes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 49),
    _VRtrIfTxV4Bytes_Type()
)
vRtrIfTxV4Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV4Bytes.setStatus("current")
_VRtrIfTxV4BytesLow32_Type = Counter32
_VRtrIfTxV4BytesLow32_Object = MibTableColumn
vRtrIfTxV4BytesLow32 = _VRtrIfTxV4BytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 50),
    _VRtrIfTxV4BytesLow32_Type()
)
vRtrIfTxV4BytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV4BytesLow32.setStatus("current")
_VRtrIfTxV4BytesHigh32_Type = Counter32
_VRtrIfTxV4BytesHigh32_Object = MibTableColumn
vRtrIfTxV4BytesHigh32 = _VRtrIfTxV4BytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 51),
    _VRtrIfTxV4BytesHigh32_Type()
)
vRtrIfTxV4BytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV4BytesHigh32.setStatus("current")
_VRtrIfTxV6Pkts_Type = Counter64
_VRtrIfTxV6Pkts_Object = MibTableColumn
vRtrIfTxV6Pkts = _VRtrIfTxV6Pkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 52),
    _VRtrIfTxV6Pkts_Type()
)
vRtrIfTxV6Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV6Pkts.setStatus("current")
_VRtrIfTxV6PktsLow32_Type = Counter32
_VRtrIfTxV6PktsLow32_Object = MibTableColumn
vRtrIfTxV6PktsLow32 = _VRtrIfTxV6PktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 53),
    _VRtrIfTxV6PktsLow32_Type()
)
vRtrIfTxV6PktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV6PktsLow32.setStatus("current")
_VRtrIfTxV6PktsHigh32_Type = Counter32
_VRtrIfTxV6PktsHigh32_Object = MibTableColumn
vRtrIfTxV6PktsHigh32 = _VRtrIfTxV6PktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 54),
    _VRtrIfTxV6PktsHigh32_Type()
)
vRtrIfTxV6PktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV6PktsHigh32.setStatus("current")
_VRtrIfTxV6Bytes_Type = Counter64
_VRtrIfTxV6Bytes_Object = MibTableColumn
vRtrIfTxV6Bytes = _VRtrIfTxV6Bytes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 55),
    _VRtrIfTxV6Bytes_Type()
)
vRtrIfTxV6Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV6Bytes.setStatus("current")
_VRtrIfTxV6BytesLow32_Type = Counter32
_VRtrIfTxV6BytesLow32_Object = MibTableColumn
vRtrIfTxV6BytesLow32 = _VRtrIfTxV6BytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 56),
    _VRtrIfTxV6BytesLow32_Type()
)
vRtrIfTxV6BytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV6BytesLow32.setStatus("current")
_VRtrIfTxV6BytesHigh32_Type = Counter32
_VRtrIfTxV6BytesHigh32_Object = MibTableColumn
vRtrIfTxV6BytesHigh32 = _VRtrIfTxV6BytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 57),
    _VRtrIfTxV6BytesHigh32_Type()
)
vRtrIfTxV6BytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV6BytesHigh32.setStatus("current")
_VRtrIfTxV4DiscardPkts_Type = Counter64
_VRtrIfTxV4DiscardPkts_Object = MibTableColumn
vRtrIfTxV4DiscardPkts = _VRtrIfTxV4DiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 58),
    _VRtrIfTxV4DiscardPkts_Type()
)
vRtrIfTxV4DiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV4DiscardPkts.setStatus("current")
_VRtrIfTxV4DiscardPktsLow32_Type = Counter32
_VRtrIfTxV4DiscardPktsLow32_Object = MibTableColumn
vRtrIfTxV4DiscardPktsLow32 = _VRtrIfTxV4DiscardPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 59),
    _VRtrIfTxV4DiscardPktsLow32_Type()
)
vRtrIfTxV4DiscardPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV4DiscardPktsLow32.setStatus("current")
_VRtrIfTxV4DiscardPktsHigh32_Type = Counter32
_VRtrIfTxV4DiscardPktsHigh32_Object = MibTableColumn
vRtrIfTxV4DiscardPktsHigh32 = _VRtrIfTxV4DiscardPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 60),
    _VRtrIfTxV4DiscardPktsHigh32_Type()
)
vRtrIfTxV4DiscardPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV4DiscardPktsHigh32.setStatus("current")
_VRtrIfTxV4DiscardBytes_Type = Counter64
_VRtrIfTxV4DiscardBytes_Object = MibTableColumn
vRtrIfTxV4DiscardBytes = _VRtrIfTxV4DiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 61),
    _VRtrIfTxV4DiscardBytes_Type()
)
vRtrIfTxV4DiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV4DiscardBytes.setStatus("current")
_VRtrIfTxV4DiscardBytesLow32_Type = Counter32
_VRtrIfTxV4DiscardBytesLow32_Object = MibTableColumn
vRtrIfTxV4DiscardBytesLow32 = _VRtrIfTxV4DiscardBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 62),
    _VRtrIfTxV4DiscardBytesLow32_Type()
)
vRtrIfTxV4DiscardBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV4DiscardBytesLow32.setStatus("current")
_VRtrIfTxV4DiscardBytesHigh32_Type = Counter32
_VRtrIfTxV4DiscardBytesHigh32_Object = MibTableColumn
vRtrIfTxV4DiscardBytesHigh32 = _VRtrIfTxV4DiscardBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 63),
    _VRtrIfTxV4DiscardBytesHigh32_Type()
)
vRtrIfTxV4DiscardBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV4DiscardBytesHigh32.setStatus("current")
_VRtrIfTxV6DiscardPkts_Type = Counter64
_VRtrIfTxV6DiscardPkts_Object = MibTableColumn
vRtrIfTxV6DiscardPkts = _VRtrIfTxV6DiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 64),
    _VRtrIfTxV6DiscardPkts_Type()
)
vRtrIfTxV6DiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV6DiscardPkts.setStatus("current")
_VRtrIfTxV6DiscardPktsLow32_Type = Counter32
_VRtrIfTxV6DiscardPktsLow32_Object = MibTableColumn
vRtrIfTxV6DiscardPktsLow32 = _VRtrIfTxV6DiscardPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 65),
    _VRtrIfTxV6DiscardPktsLow32_Type()
)
vRtrIfTxV6DiscardPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV6DiscardPktsLow32.setStatus("current")
_VRtrIfTxV6DiscardPktsHigh32_Type = Counter32
_VRtrIfTxV6DiscardPktsHigh32_Object = MibTableColumn
vRtrIfTxV6DiscardPktsHigh32 = _VRtrIfTxV6DiscardPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 66),
    _VRtrIfTxV6DiscardPktsHigh32_Type()
)
vRtrIfTxV6DiscardPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV6DiscardPktsHigh32.setStatus("current")
_VRtrIfTxV6DiscardBytes_Type = Counter64
_VRtrIfTxV6DiscardBytes_Object = MibTableColumn
vRtrIfTxV6DiscardBytes = _VRtrIfTxV6DiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 67),
    _VRtrIfTxV6DiscardBytes_Type()
)
vRtrIfTxV6DiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV6DiscardBytes.setStatus("current")
_VRtrIfTxV6DiscardBytesLow32_Type = Counter32
_VRtrIfTxV6DiscardBytesLow32_Object = MibTableColumn
vRtrIfTxV6DiscardBytesLow32 = _VRtrIfTxV6DiscardBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 68),
    _VRtrIfTxV6DiscardBytesLow32_Type()
)
vRtrIfTxV6DiscardBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV6DiscardBytesLow32.setStatus("current")
_VRtrIfTxV6DiscardBytesHigh32_Type = Counter32
_VRtrIfTxV6DiscardBytesHigh32_Object = MibTableColumn
vRtrIfTxV6DiscardBytesHigh32 = _VRtrIfTxV6DiscardBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 69),
    _VRtrIfTxV6DiscardBytesHigh32_Type()
)
vRtrIfTxV6DiscardBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxV6DiscardBytesHigh32.setStatus("current")
_VRtrIfIpReasV6FragPktsRcvd_Type = Counter64
_VRtrIfIpReasV6FragPktsRcvd_Object = MibTableColumn
vRtrIfIpReasV6FragPktsRcvd = _VRtrIfIpReasV6FragPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 70),
    _VRtrIfIpReasV6FragPktsRcvd_Type()
)
vRtrIfIpReasV6FragPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragPktsRcvd.setStatus("current")
_VRtrIfIpReasV6FragPktsRcvdLow32_Type = Counter32
_VRtrIfIpReasV6FragPktsRcvdLow32_Object = MibTableColumn
vRtrIfIpReasV6FragPktsRcvdLow32 = _VRtrIfIpReasV6FragPktsRcvdLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 71),
    _VRtrIfIpReasV6FragPktsRcvdLow32_Type()
)
vRtrIfIpReasV6FragPktsRcvdLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragPktsRcvdLow32.setStatus("current")
_VRtrIfIpReasV6FragPktsRcvdHigh32_Type = Counter32
_VRtrIfIpReasV6FragPktsRcvdHigh32_Object = MibTableColumn
vRtrIfIpReasV6FragPktsRcvdHigh32 = _VRtrIfIpReasV6FragPktsRcvdHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 72),
    _VRtrIfIpReasV6FragPktsRcvdHigh32_Type()
)
vRtrIfIpReasV6FragPktsRcvdHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragPktsRcvdHigh32.setStatus("current")
_VRtrIfIpReasV6FragBytesRcvd_Type = Counter64
_VRtrIfIpReasV6FragBytesRcvd_Object = MibTableColumn
vRtrIfIpReasV6FragBytesRcvd = _VRtrIfIpReasV6FragBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 73),
    _VRtrIfIpReasV6FragBytesRcvd_Type()
)
vRtrIfIpReasV6FragBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragBytesRcvd.setStatus("current")
_VRtrIfIpReasV6FragBytesRcvdL32_Type = Counter32
_VRtrIfIpReasV6FragBytesRcvdL32_Object = MibTableColumn
vRtrIfIpReasV6FragBytesRcvdL32 = _VRtrIfIpReasV6FragBytesRcvdL32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 74),
    _VRtrIfIpReasV6FragBytesRcvdL32_Type()
)
vRtrIfIpReasV6FragBytesRcvdL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragBytesRcvdL32.setStatus("current")
_VRtrIfIpReasV6FragBytesRcvdH32_Type = Counter32
_VRtrIfIpReasV6FragBytesRcvdH32_Object = MibTableColumn
vRtrIfIpReasV6FragBytesRcvdH32 = _VRtrIfIpReasV6FragBytesRcvdH32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 75),
    _VRtrIfIpReasV6FragBytesRcvdH32_Type()
)
vRtrIfIpReasV6FragBytesRcvdH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragBytesRcvdH32.setStatus("current")
_VRtrIfIpReasV6FragPktsReas_Type = Counter64
_VRtrIfIpReasV6FragPktsReas_Object = MibTableColumn
vRtrIfIpReasV6FragPktsReas = _VRtrIfIpReasV6FragPktsReas_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 76),
    _VRtrIfIpReasV6FragPktsReas_Type()
)
vRtrIfIpReasV6FragPktsReas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragPktsReas.setStatus("current")
_VRtrIfIpReasV6FragPktsReasLow32_Type = Counter32
_VRtrIfIpReasV6FragPktsReasLow32_Object = MibTableColumn
vRtrIfIpReasV6FragPktsReasLow32 = _VRtrIfIpReasV6FragPktsReasLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 77),
    _VRtrIfIpReasV6FragPktsReasLow32_Type()
)
vRtrIfIpReasV6FragPktsReasLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragPktsReasLow32.setStatus("current")
_VRtrIfIpReasV6FragPktsReasHigh32_Type = Counter32
_VRtrIfIpReasV6FragPktsReasHigh32_Object = MibTableColumn
vRtrIfIpReasV6FragPktsReasHigh32 = _VRtrIfIpReasV6FragPktsReasHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 78),
    _VRtrIfIpReasV6FragPktsReasHigh32_Type()
)
vRtrIfIpReasV6FragPktsReasHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragPktsReasHigh32.setStatus("current")
_VRtrIfIpReasV6FragBytesReas_Type = Counter64
_VRtrIfIpReasV6FragBytesReas_Object = MibTableColumn
vRtrIfIpReasV6FragBytesReas = _VRtrIfIpReasV6FragBytesReas_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 79),
    _VRtrIfIpReasV6FragBytesReas_Type()
)
vRtrIfIpReasV6FragBytesReas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragBytesReas.setStatus("current")
_VRtrIfIpReasV6FragBytesReasL32_Type = Counter32
_VRtrIfIpReasV6FragBytesReasL32_Object = MibTableColumn
vRtrIfIpReasV6FragBytesReasL32 = _VRtrIfIpReasV6FragBytesReasL32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 80),
    _VRtrIfIpReasV6FragBytesReasL32_Type()
)
vRtrIfIpReasV6FragBytesReasL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragBytesReasL32.setStatus("current")
_VRtrIfIpReasV6FragBytesReasH32_Type = Counter32
_VRtrIfIpReasV6FragBytesReasH32_Object = MibTableColumn
vRtrIfIpReasV6FragBytesReasH32 = _VRtrIfIpReasV6FragBytesReasH32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 81),
    _VRtrIfIpReasV6FragBytesReasH32_Type()
)
vRtrIfIpReasV6FragBytesReasH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragBytesReasH32.setStatus("current")
_VRtrIfIpReasV6FragReasErrors_Type = Counter64
_VRtrIfIpReasV6FragReasErrors_Object = MibTableColumn
vRtrIfIpReasV6FragReasErrors = _VRtrIfIpReasV6FragReasErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 82),
    _VRtrIfIpReasV6FragReasErrors_Type()
)
vRtrIfIpReasV6FragReasErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragReasErrors.setStatus("current")
_VRtrIfIpReasV6FragReasErrorsL32_Type = Counter32
_VRtrIfIpReasV6FragReasErrorsL32_Object = MibTableColumn
vRtrIfIpReasV6FragReasErrorsL32 = _VRtrIfIpReasV6FragReasErrorsL32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 83),
    _VRtrIfIpReasV6FragReasErrorsL32_Type()
)
vRtrIfIpReasV6FragReasErrorsL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragReasErrorsL32.setStatus("current")
_VRtrIfIpReasV6FragReasErrorsH32_Type = Counter32
_VRtrIfIpReasV6FragReasErrorsH32_Object = MibTableColumn
vRtrIfIpReasV6FragReasErrorsH32 = _VRtrIfIpReasV6FragReasErrorsH32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 84),
    _VRtrIfIpReasV6FragReasErrorsH32_Type()
)
vRtrIfIpReasV6FragReasErrorsH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragReasErrorsH32.setStatus("current")
_VRtrIfIpReasV6FragDisc_Type = Counter64
_VRtrIfIpReasV6FragDisc_Object = MibTableColumn
vRtrIfIpReasV6FragDisc = _VRtrIfIpReasV6FragDisc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 85),
    _VRtrIfIpReasV6FragDisc_Type()
)
vRtrIfIpReasV6FragDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragDisc.setStatus("current")
_VRtrIfIpReasV6FragDiscLow32_Type = Counter32
_VRtrIfIpReasV6FragDiscLow32_Object = MibTableColumn
vRtrIfIpReasV6FragDiscLow32 = _VRtrIfIpReasV6FragDiscLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 86),
    _VRtrIfIpReasV6FragDiscLow32_Type()
)
vRtrIfIpReasV6FragDiscLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragDiscLow32.setStatus("current")
_VRtrIfIpReasV6FragDiscHigh32_Type = Counter32
_VRtrIfIpReasV6FragDiscHigh32_Object = MibTableColumn
vRtrIfIpReasV6FragDiscHigh32 = _VRtrIfIpReasV6FragDiscHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 87),
    _VRtrIfIpReasV6FragDiscHigh32_Type()
)
vRtrIfIpReasV6FragDiscHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6FragDiscHigh32.setStatus("current")
_VRtrIfIpReasV6OutBufRes_Type = Counter64
_VRtrIfIpReasV6OutBufRes_Object = MibTableColumn
vRtrIfIpReasV6OutBufRes = _VRtrIfIpReasV6OutBufRes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 88),
    _VRtrIfIpReasV6OutBufRes_Type()
)
vRtrIfIpReasV6OutBufRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6OutBufRes.setStatus("current")
_VRtrIfIpReasV6OutBufResLow32_Type = Counter32
_VRtrIfIpReasV6OutBufResLow32_Object = MibTableColumn
vRtrIfIpReasV6OutBufResLow32 = _VRtrIfIpReasV6OutBufResLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 89),
    _VRtrIfIpReasV6OutBufResLow32_Type()
)
vRtrIfIpReasV6OutBufResLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6OutBufResLow32.setStatus("current")
_VRtrIfIpReasV6OutBufResHigh32_Type = Counter32
_VRtrIfIpReasV6OutBufResHigh32_Object = MibTableColumn
vRtrIfIpReasV6OutBufResHigh32 = _VRtrIfIpReasV6OutBufResHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 90),
    _VRtrIfIpReasV6OutBufResHigh32_Type()
)
vRtrIfIpReasV6OutBufResHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6OutBufResHigh32.setStatus("current")
_VRtrIfIpReasV6PktsRx_Type = Counter64
_VRtrIfIpReasV6PktsRx_Object = MibTableColumn
vRtrIfIpReasV6PktsRx = _VRtrIfIpReasV6PktsRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 91),
    _VRtrIfIpReasV6PktsRx_Type()
)
vRtrIfIpReasV6PktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6PktsRx.setStatus("current")
_VRtrIfIpReasV6PktsRxLow32_Type = Counter32
_VRtrIfIpReasV6PktsRxLow32_Object = MibTableColumn
vRtrIfIpReasV6PktsRxLow32 = _VRtrIfIpReasV6PktsRxLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 92),
    _VRtrIfIpReasV6PktsRxLow32_Type()
)
vRtrIfIpReasV6PktsRxLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6PktsRxLow32.setStatus("current")
_VRtrIfIpReasV6PktsRxHigh32_Type = Counter32
_VRtrIfIpReasV6PktsRxHigh32_Object = MibTableColumn
vRtrIfIpReasV6PktsRxHigh32 = _VRtrIfIpReasV6PktsRxHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 93),
    _VRtrIfIpReasV6PktsRxHigh32_Type()
)
vRtrIfIpReasV6PktsRxHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6PktsRxHigh32.setStatus("current")
_VRtrIfIpReasV6BytesRx_Type = Counter64
_VRtrIfIpReasV6BytesRx_Object = MibTableColumn
vRtrIfIpReasV6BytesRx = _VRtrIfIpReasV6BytesRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 94),
    _VRtrIfIpReasV6BytesRx_Type()
)
vRtrIfIpReasV6BytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6BytesRx.setStatus("current")
_VRtrIfIpReasV6BytesRxLow32_Type = Counter32
_VRtrIfIpReasV6BytesRxLow32_Object = MibTableColumn
vRtrIfIpReasV6BytesRxLow32 = _VRtrIfIpReasV6BytesRxLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 95),
    _VRtrIfIpReasV6BytesRxLow32_Type()
)
vRtrIfIpReasV6BytesRxLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6BytesRxLow32.setStatus("current")
_VRtrIfIpReasV6BytesRxHigh32_Type = Counter32
_VRtrIfIpReasV6BytesRxHigh32_Object = MibTableColumn
vRtrIfIpReasV6BytesRxHigh32 = _VRtrIfIpReasV6BytesRxHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 96),
    _VRtrIfIpReasV6BytesRxHigh32_Type()
)
vRtrIfIpReasV6BytesRxHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6BytesRxHigh32.setStatus("current")
_VRtrIfIpReasV6PktsTx_Type = Counter64
_VRtrIfIpReasV6PktsTx_Object = MibTableColumn
vRtrIfIpReasV6PktsTx = _VRtrIfIpReasV6PktsTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 97),
    _VRtrIfIpReasV6PktsTx_Type()
)
vRtrIfIpReasV6PktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6PktsTx.setStatus("current")
_VRtrIfIpReasV6PktsTxLow32_Type = Counter32
_VRtrIfIpReasV6PktsTxLow32_Object = MibTableColumn
vRtrIfIpReasV6PktsTxLow32 = _VRtrIfIpReasV6PktsTxLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 98),
    _VRtrIfIpReasV6PktsTxLow32_Type()
)
vRtrIfIpReasV6PktsTxLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6PktsTxLow32.setStatus("current")
_VRtrIfIpReasV6PktsTxHigh32_Type = Counter32
_VRtrIfIpReasV6PktsTxHigh32_Object = MibTableColumn
vRtrIfIpReasV6PktsTxHigh32 = _VRtrIfIpReasV6PktsTxHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 99),
    _VRtrIfIpReasV6PktsTxHigh32_Type()
)
vRtrIfIpReasV6PktsTxHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6PktsTxHigh32.setStatus("current")
_VRtrIfIpReasV6BytesTx_Type = Counter64
_VRtrIfIpReasV6BytesTx_Object = MibTableColumn
vRtrIfIpReasV6BytesTx = _VRtrIfIpReasV6BytesTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 100),
    _VRtrIfIpReasV6BytesTx_Type()
)
vRtrIfIpReasV6BytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6BytesTx.setStatus("current")
_VRtrIfIpReasV6BytesTxLow32_Type = Counter32
_VRtrIfIpReasV6BytesTxLow32_Object = MibTableColumn
vRtrIfIpReasV6BytesTxLow32 = _VRtrIfIpReasV6BytesTxLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 101),
    _VRtrIfIpReasV6BytesTxLow32_Type()
)
vRtrIfIpReasV6BytesTxLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6BytesTxLow32.setStatus("current")
_VRtrIfIpReasV6BytesTxHigh32_Type = Counter32
_VRtrIfIpReasV6BytesTxHigh32_Object = MibTableColumn
vRtrIfIpReasV6BytesTxHigh32 = _VRtrIfIpReasV6BytesTxHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 102),
    _VRtrIfIpReasV6BytesTxHigh32_Type()
)
vRtrIfIpReasV6BytesTxHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIpReasV6BytesTxHigh32.setStatus("current")
_VRtrIfSpeed_Type = Counter64
_VRtrIfSpeed_Object = MibTableColumn
vRtrIfSpeed = _VRtrIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 54, 1, 103),
    _VRtrIfSpeed_Type()
)
vRtrIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfSpeed.setStatus("current")
_VRtrIfExtTable_Object = MibTable
vRtrIfExtTable = _VRtrIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61)
)
if mibBuilder.loadTexts:
    vRtrIfExtTable.setStatus("current")
_VRtrIfExtEntry_Object = MibTableRow
vRtrIfExtEntry = _VRtrIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61, 1)
)
if mibBuilder.loadTexts:
    vRtrIfExtEntry.setStatus("current")


class _VRtrIfLsrIpLoadBalancing_Type(Integer32):
    """Custom type vRtrIfLsrIpLoadBalancing based on Integer32"""
    defaultValue = 0

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
        *(("system", 0),
          ("label-only", 1),
          ("label-ip", 2),
          ("ip-only", 3))
    )


_VRtrIfLsrIpLoadBalancing_Type.__name__ = "Integer32"
_VRtrIfLsrIpLoadBalancing_Object = MibTableColumn
vRtrIfLsrIpLoadBalancing = _VRtrIfLsrIpLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61, 1, 1),
    _VRtrIfLsrIpLoadBalancing_Type()
)
vRtrIfLsrIpLoadBalancing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfLsrIpLoadBalancing.setStatus("current")


class _VRtrIfIngressIpv4Flowspec_Type(TruthValue):
    """Custom type vRtrIfIngressIpv4Flowspec based on TruthValue"""
    defaultValue = 2


_VRtrIfIngressIpv4Flowspec_Type.__name__ = "TruthValue"
_VRtrIfIngressIpv4Flowspec_Object = MibTableColumn
vRtrIfIngressIpv4Flowspec = _VRtrIfIngressIpv4Flowspec_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61, 1, 2),
    _VRtrIfIngressIpv4Flowspec_Type()
)
vRtrIfIngressIpv4Flowspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIngressIpv4Flowspec.setStatus("current")


class _VRtrIfInfo_Type(OctetString):
    """Custom type vRtrIfInfo based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 257),
    )


_VRtrIfInfo_Type.__name__ = "OctetString"
_VRtrIfInfo_Object = MibTableColumn
vRtrIfInfo = _VRtrIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61, 1, 3),
    _VRtrIfInfo_Type()
)
vRtrIfInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfInfo.setStatus("current")


class _VRtrIfInfoEncrypted_Type(TruthValue):
    """Custom type vRtrIfInfoEncrypted based on TruthValue"""
    defaultValue = 1


_VRtrIfInfoEncrypted_Type.__name__ = "TruthValue"
_VRtrIfInfoEncrypted_Object = MibTableColumn
vRtrIfInfoEncrypted = _VRtrIfInfoEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61, 1, 4),
    _VRtrIfInfoEncrypted_Type()
)
vRtrIfInfoEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfInfoEncrypted.setStatus("obsolete")


class _VRtrIfQosRouteLookup_Type(Integer32):
    """Custom type vRtrIfQosRouteLookup based on Integer32"""
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
        *(("none", 0),
          ("destination", 1),
          ("source", 2))
    )


_VRtrIfQosRouteLookup_Type.__name__ = "Integer32"
_VRtrIfQosRouteLookup_Object = MibTableColumn
vRtrIfQosRouteLookup = _VRtrIfQosRouteLookup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61, 1, 5),
    _VRtrIfQosRouteLookup_Type()
)
vRtrIfQosRouteLookup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfQosRouteLookup.setStatus("current")


class _VRtrIfIpv6QosRouteLookup_Type(Integer32):
    """Custom type vRtrIfIpv6QosRouteLookup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("destination", 1))
    )


_VRtrIfIpv6QosRouteLookup_Type.__name__ = "Integer32"
_VRtrIfIpv6QosRouteLookup_Object = MibTableColumn
vRtrIfIpv6QosRouteLookup = _VRtrIfIpv6QosRouteLookup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61, 1, 6),
    _VRtrIfIpv6QosRouteLookup_Type()
)
vRtrIfIpv6QosRouteLookup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIpv6QosRouteLookup.setStatus("current")
_VRtrIfStatusString_Type = DisplayString
_VRtrIfStatusString_Object = MibTableColumn
vRtrIfStatusString = _VRtrIfStatusString_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61, 1, 7),
    _VRtrIfStatusString_Type()
)
vRtrIfStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfStatusString.setStatus("current")


class _VRtrIfIpv6uRPFCheckState_Type(TmnxEnabledDisabled):
    """Custom type vRtrIfIpv6uRPFCheckState based on TmnxEnabledDisabled"""
    defaultValue = 2


_VRtrIfIpv6uRPFCheckState_Type.__name__ = "TmnxEnabledDisabled"
_VRtrIfIpv6uRPFCheckState_Object = MibTableColumn
vRtrIfIpv6uRPFCheckState = _VRtrIfIpv6uRPFCheckState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61, 1, 8),
    _VRtrIfIpv6uRPFCheckState_Type()
)
vRtrIfIpv6uRPFCheckState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIpv6uRPFCheckState.setStatus("current")


class _VRtrIfIpv6uRPFCheckMode_Type(Integer32):
    """Custom type vRtrIfIpv6uRPFCheckMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("loose", 2))
    )


_VRtrIfIpv6uRPFCheckMode_Type.__name__ = "Integer32"
_VRtrIfIpv6uRPFCheckMode_Object = MibTableColumn
vRtrIfIpv6uRPFCheckMode = _VRtrIfIpv6uRPFCheckMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61, 1, 9),
    _VRtrIfIpv6uRPFCheckMode_Type()
)
vRtrIfIpv6uRPFCheckMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIpv6uRPFCheckMode.setStatus("current")


class _VRtrIfTmsOffRampVprn_Type(TmnxServId):
    """Custom type vRtrIfTmsOffRampVprn based on TmnxServId"""
    defaultValue = 0


_VRtrIfTmsOffRampVprn_Type.__name__ = "TmnxServId"
_VRtrIfTmsOffRampVprn_Object = MibTableColumn
vRtrIfTmsOffRampVprn = _VRtrIfTmsOffRampVprn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61, 1, 10),
    _VRtrIfTmsOffRampVprn_Type()
)
vRtrIfTmsOffRampVprn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfTmsOffRampVprn.setStatus("current")


class _VRtrIfTmsMgmtVprn_Type(TmnxServId):
    """Custom type vRtrIfTmsMgmtVprn based on TmnxServId"""
    defaultValue = 0


_VRtrIfTmsMgmtVprn_Type.__name__ = "TmnxServId"
_VRtrIfTmsMgmtVprn_Object = MibTableColumn
vRtrIfTmsMgmtVprn = _VRtrIfTmsMgmtVprn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 61, 1, 11),
    _VRtrIfTmsMgmtVprn_Type()
)
vRtrIfTmsMgmtVprn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfTmsMgmtVprn.setStatus("current")
_TnVRtrMobGatewayObjs_ObjectIdentity = ObjectIdentity
tnVRtrMobGatewayObjs = _TnVRtrMobGatewayObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 69)
)
_VRtrIfBfdExtTableLastChanged_Type = TimeStamp
_VRtrIfBfdExtTableLastChanged_Object = MibScalar
vRtrIfBfdExtTableLastChanged = _VRtrIfBfdExtTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 70),
    _VRtrIfBfdExtTableLastChanged_Type()
)
vRtrIfBfdExtTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdExtTableLastChanged.setStatus("current")
_VRtrIfBfdExtTable_Object = MibTable
vRtrIfBfdExtTable = _VRtrIfBfdExtTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 71)
)
if mibBuilder.loadTexts:
    vRtrIfBfdExtTable.setStatus("current")
_VRtrIfBfdExtEntry_Object = MibTableRow
vRtrIfBfdExtEntry = _VRtrIfBfdExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 71, 1)
)
vRtrIfBfdExtEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (0, "TN-VRTR-MIB", "vRtrIfIndex"),
    (0, "TN-VRTR-MIB", "vRtrIfBfdExtAddressType"),
)
if mibBuilder.loadTexts:
    vRtrIfBfdExtEntry.setStatus("current")
_VRtrIfBfdExtAddressType_Type = InetAddressType
_VRtrIfBfdExtAddressType_Object = MibTableColumn
vRtrIfBfdExtAddressType = _VRtrIfBfdExtAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 71, 1, 1),
    _VRtrIfBfdExtAddressType_Type()
)
vRtrIfBfdExtAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfBfdExtAddressType.setStatus("current")
_VRtrIfBfdExtAdminState_Type = TmnxAdminState
_VRtrIfBfdExtAdminState_Object = MibTableColumn
vRtrIfBfdExtAdminState = _VRtrIfBfdExtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 71, 1, 2),
    _VRtrIfBfdExtAdminState_Type()
)
vRtrIfBfdExtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfBfdExtAdminState.setStatus("current")


class _VRtrIfBfdExtTransmitInterval_Type(Unsigned32):
    """Custom type vRtrIfBfdExtTransmitInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_VRtrIfBfdExtTransmitInterval_Type.__name__ = "Unsigned32"
_VRtrIfBfdExtTransmitInterval_Object = MibTableColumn
vRtrIfBfdExtTransmitInterval = _VRtrIfBfdExtTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 71, 1, 3),
    _VRtrIfBfdExtTransmitInterval_Type()
)
vRtrIfBfdExtTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfBfdExtTransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdExtTransmitInterval.setUnits("milliseconds")


class _VRtrIfBfdExtReceiveInterval_Type(Unsigned32):
    """Custom type vRtrIfBfdExtReceiveInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_VRtrIfBfdExtReceiveInterval_Type.__name__ = "Unsigned32"
_VRtrIfBfdExtReceiveInterval_Object = MibTableColumn
vRtrIfBfdExtReceiveInterval = _VRtrIfBfdExtReceiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 71, 1, 4),
    _VRtrIfBfdExtReceiveInterval_Type()
)
vRtrIfBfdExtReceiveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfBfdExtReceiveInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdExtReceiveInterval.setUnits("milliseconds")


class _VRtrIfBfdExtMultiplier_Type(Unsigned32):
    """Custom type vRtrIfBfdExtMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_VRtrIfBfdExtMultiplier_Type.__name__ = "Unsigned32"
_VRtrIfBfdExtMultiplier_Object = MibTableColumn
vRtrIfBfdExtMultiplier = _VRtrIfBfdExtMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 71, 1, 5),
    _VRtrIfBfdExtMultiplier_Type()
)
vRtrIfBfdExtMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfBfdExtMultiplier.setStatus("current")


class _VRtrIfBfdExtEchoInterval_Type(Unsigned32):
    """Custom type vRtrIfBfdExtEchoInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 100000),
    )


_VRtrIfBfdExtEchoInterval_Type.__name__ = "Unsigned32"
_VRtrIfBfdExtEchoInterval_Object = MibTableColumn
vRtrIfBfdExtEchoInterval = _VRtrIfBfdExtEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 71, 1, 6),
    _VRtrIfBfdExtEchoInterval_Type()
)
vRtrIfBfdExtEchoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfBfdExtEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdExtEchoInterval.setUnits("milliseconds")


class _VRtrIfBfdExtType_Type(Integer32):
    """Custom type vRtrIfBfdExtType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpmNp", 1),
          ("auto", 2),
          ("iomHw", 3))
    )


_VRtrIfBfdExtType_Type.__name__ = "Integer32"
_VRtrIfBfdExtType_Object = MibTableColumn
vRtrIfBfdExtType = _VRtrIfBfdExtType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 71, 1, 7),
    _VRtrIfBfdExtType_Type()
)
vRtrIfBfdExtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfBfdExtType.setStatus("current")
_VRtrIfStatsExtTable_Object = MibTable
vRtrIfStatsExtTable = _VRtrIfStatsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 74)
)
if mibBuilder.loadTexts:
    vRtrIfStatsExtTable.setStatus("current")
_VRtrIfStatsExtEntry_Object = MibTableRow
vRtrIfStatsExtEntry = _VRtrIfStatsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 74, 1)
)
if mibBuilder.loadTexts:
    vRtrIfStatsExtEntry.setStatus("current")
_VRtrIfTxPkts_Type = Counter64
_VRtrIfTxPkts_Object = MibTableColumn
vRtrIfTxPkts = _VRtrIfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 74, 1, 1),
    _VRtrIfTxPkts_Type()
)
vRtrIfTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxPkts.setStatus("current")
_VRtrIfTxPktsLow32_Type = Counter32
_VRtrIfTxPktsLow32_Object = MibTableColumn
vRtrIfTxPktsLow32 = _VRtrIfTxPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 74, 1, 2),
    _VRtrIfTxPktsLow32_Type()
)
vRtrIfTxPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxPktsLow32.setStatus("current")
_VRtrIfTxPktsHigh32_Type = Counter32
_VRtrIfTxPktsHigh32_Object = MibTableColumn
vRtrIfTxPktsHigh32 = _VRtrIfTxPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 74, 1, 3),
    _VRtrIfTxPktsHigh32_Type()
)
vRtrIfTxPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxPktsHigh32.setStatus("current")
_VRtrIfTxBytes_Type = Counter64
_VRtrIfTxBytes_Object = MibTableColumn
vRtrIfTxBytes = _VRtrIfTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 74, 1, 4),
    _VRtrIfTxBytes_Type()
)
vRtrIfTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxBytes.setStatus("current")
_VRtrIfTxBytesLow32_Type = Counter32
_VRtrIfTxBytesLow32_Object = MibTableColumn
vRtrIfTxBytesLow32 = _VRtrIfTxBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 74, 1, 5),
    _VRtrIfTxBytesLow32_Type()
)
vRtrIfTxBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxBytesLow32.setStatus("current")
_VRtrIfTxBytesHigh32_Type = Counter32
_VRtrIfTxBytesHigh32_Object = MibTableColumn
vRtrIfTxBytesHigh32 = _VRtrIfTxBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 74, 1, 6),
    _VRtrIfTxBytesHigh32_Type()
)
vRtrIfTxBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTxBytesHigh32.setStatus("current")
_VRtrIfQosTable_Object = MibTable
vRtrIfQosTable = _VRtrIfQosTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 78)
)
if mibBuilder.loadTexts:
    vRtrIfQosTable.setStatus("current")
_VRtrIfQosEntry_Object = MibTableRow
vRtrIfQosEntry = _VRtrIfQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 78, 1)
)
if mibBuilder.loadTexts:
    vRtrIfQosEntry.setStatus("current")


class _VRtrIfQosNetworkPolicyId_Type(TNetworkPolicyID):
    """Custom type vRtrIfQosNetworkPolicyId based on TNetworkPolicyID"""
    defaultValue = 1


_VRtrIfQosNetworkPolicyId_Type.__name__ = "TNetworkPolicyID"
_VRtrIfQosNetworkPolicyId_Object = MibTableColumn
vRtrIfQosNetworkPolicyId = _VRtrIfQosNetworkPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 78, 1, 1),
    _VRtrIfQosNetworkPolicyId_Type()
)
vRtrIfQosNetworkPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfQosNetworkPolicyId.setStatus("current")
_VRtrIfBfdSessExtTable_Object = MibTable
vRtrIfBfdSessExtTable = _VRtrIfBfdSessExtTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92)
)
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtTable.setStatus("current")
_VRtrIfBfdSessExtEntry_Object = MibTableRow
vRtrIfBfdSessExtEntry = _VRtrIfBfdSessExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1)
)
vRtrIfBfdSessExtEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrIfBfdSessExtLinkType"),
    (0, "TN-VRTR-MIB", "vRtrIfBfdSessExtRxInfoId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (0, "TN-VRTR-MIB", "vRtrIfIndex"),
    (0, "TN-VRTR-MIB", "vRtrIfBfdSessExtLclAddrType"),
    (0, "TN-VRTR-MIB", "vRtrIfBfdSessExtLclAddr"),
    (0, "TN-VRTR-MIB", "vRtrIfBfdSessExtRemAddrType"),
    (0, "TN-VRTR-MIB", "vRtrIfBfdSessExtRemAddr"),
)
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtEntry.setStatus("current")


class _VRtrIfBfdSessExtLinkType_Type(Integer32):
    """Custom type vRtrIfBfdSessExtLinkType based on Integer32"""
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
        *(("pointToPoint", 0),
          ("head", 1),
          ("tail", 2),
          ("client", 3),
          ("ccOnly", 4),
          ("ccWithCv", 5),
          ("microBfd", 6))
    )


_VRtrIfBfdSessExtLinkType_Type.__name__ = "Integer32"
_VRtrIfBfdSessExtLinkType_Object = MibTableColumn
vRtrIfBfdSessExtLinkType = _VRtrIfBfdSessExtLinkType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 1),
    _VRtrIfBfdSessExtLinkType_Type()
)
vRtrIfBfdSessExtLinkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLinkType.setStatus("current")
_VRtrIfBfdSessExtRxInfoId_Type = Unsigned32
_VRtrIfBfdSessExtRxInfoId_Object = MibTableColumn
vRtrIfBfdSessExtRxInfoId = _VRtrIfBfdSessExtRxInfoId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 2),
    _VRtrIfBfdSessExtRxInfoId_Type()
)
vRtrIfBfdSessExtRxInfoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRxInfoId.setStatus("current")
_VRtrIfBfdSessExtLclAddrType_Type = InetAddressType
_VRtrIfBfdSessExtLclAddrType_Object = MibTableColumn
vRtrIfBfdSessExtLclAddrType = _VRtrIfBfdSessExtLclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 3),
    _VRtrIfBfdSessExtLclAddrType_Type()
)
vRtrIfBfdSessExtLclAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLclAddrType.setStatus("current")


class _VRtrIfBfdSessExtLclAddr_Type(InetAddress):
    """Custom type vRtrIfBfdSessExtLclAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrIfBfdSessExtLclAddr_Type.__name__ = "InetAddress"
_VRtrIfBfdSessExtLclAddr_Object = MibTableColumn
vRtrIfBfdSessExtLclAddr = _VRtrIfBfdSessExtLclAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 4),
    _VRtrIfBfdSessExtLclAddr_Type()
)
vRtrIfBfdSessExtLclAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLclAddr.setStatus("current")
_VRtrIfBfdSessExtRemAddrType_Type = InetAddressType
_VRtrIfBfdSessExtRemAddrType_Object = MibTableColumn
vRtrIfBfdSessExtRemAddrType = _VRtrIfBfdSessExtRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 5),
    _VRtrIfBfdSessExtRemAddrType_Type()
)
vRtrIfBfdSessExtRemAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemAddrType.setStatus("current")


class _VRtrIfBfdSessExtRemAddr_Type(InetAddress):
    """Custom type vRtrIfBfdSessExtRemAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrIfBfdSessExtRemAddr_Type.__name__ = "InetAddress"
_VRtrIfBfdSessExtRemAddr_Object = MibTableColumn
vRtrIfBfdSessExtRemAddr = _VRtrIfBfdSessExtRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 6),
    _VRtrIfBfdSessExtRemAddr_Type()
)
vRtrIfBfdSessExtRemAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemAddr.setStatus("current")
_VRtrIfBfdSessExtOperState_Type = TmnxOperState
_VRtrIfBfdSessExtOperState_Object = MibTableColumn
vRtrIfBfdSessExtOperState = _VRtrIfBfdSessExtOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 7),
    _VRtrIfBfdSessExtOperState_Type()
)
vRtrIfBfdSessExtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtOperState.setStatus("current")


class _VRtrIfBfdSessExtState_Type(Integer32):
    """Custom type vRtrIfBfdSessExtState based on Integer32"""
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
        *(("adminDown", 0),
          ("down", 1),
          ("init", 2),
          ("up", 3))
    )


_VRtrIfBfdSessExtState_Type.__name__ = "Integer32"
_VRtrIfBfdSessExtState_Object = MibTableColumn
vRtrIfBfdSessExtState = _VRtrIfBfdSessExtState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 8),
    _VRtrIfBfdSessExtState_Type()
)
vRtrIfBfdSessExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtState.setStatus("current")


class _VRtrIfBfdSessExtOperFlags_Type(Bits):
    """Custom type vRtrIfBfdSessExtOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("noProtocols", 0),
          ("noHeartBeat", 1),
          ("echoFailed", 2),
          ("nbrSignalDown", 3),
          ("fwdPlaneReset", 4),
          ("pathDown", 5),
          ("nbrAdminDown", 6),
          ("adminClear", 7),
          ("misConnDefect", 8))
    )

_VRtrIfBfdSessExtOperFlags_Type.__name__ = "Bits"
_VRtrIfBfdSessExtOperFlags_Object = MibTableColumn
vRtrIfBfdSessExtOperFlags = _VRtrIfBfdSessExtOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 9),
    _VRtrIfBfdSessExtOperFlags_Type()
)
vRtrIfBfdSessExtOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtOperFlags.setStatus("current")
_VRtrIfBfdSessExtMesgRecv_Type = Counter32
_VRtrIfBfdSessExtMesgRecv_Object = MibTableColumn
vRtrIfBfdSessExtMesgRecv = _VRtrIfBfdSessExtMesgRecv_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 10),
    _VRtrIfBfdSessExtMesgRecv_Type()
)
vRtrIfBfdSessExtMesgRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtMesgRecv.setStatus("current")
_VRtrIfBfdSessExtMesgSent_Type = Counter32
_VRtrIfBfdSessExtMesgSent_Object = MibTableColumn
vRtrIfBfdSessExtMesgSent = _VRtrIfBfdSessExtMesgSent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 11),
    _VRtrIfBfdSessExtMesgSent_Type()
)
vRtrIfBfdSessExtMesgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtMesgSent.setStatus("current")
_VRtrIfBfdSessExtLastDownTime_Type = TimeStamp
_VRtrIfBfdSessExtLastDownTime_Object = MibTableColumn
vRtrIfBfdSessExtLastDownTime = _VRtrIfBfdSessExtLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 12),
    _VRtrIfBfdSessExtLastDownTime_Type()
)
vRtrIfBfdSessExtLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLastDownTime.setStatus("current")
_VRtrIfBfdSessExtLastUpTime_Type = TimeStamp
_VRtrIfBfdSessExtLastUpTime_Object = MibTableColumn
vRtrIfBfdSessExtLastUpTime = _VRtrIfBfdSessExtLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 13),
    _VRtrIfBfdSessExtLastUpTime_Type()
)
vRtrIfBfdSessExtLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLastUpTime.setStatus("current")
_VRtrIfBfdSessExtUpCount_Type = Counter32
_VRtrIfBfdSessExtUpCount_Object = MibTableColumn
vRtrIfBfdSessExtUpCount = _VRtrIfBfdSessExtUpCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 14),
    _VRtrIfBfdSessExtUpCount_Type()
)
vRtrIfBfdSessExtUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtUpCount.setStatus("current")
_VRtrIfBfdSessExtDownCount_Type = Counter32
_VRtrIfBfdSessExtDownCount_Object = MibTableColumn
vRtrIfBfdSessExtDownCount = _VRtrIfBfdSessExtDownCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 15),
    _VRtrIfBfdSessExtDownCount_Type()
)
vRtrIfBfdSessExtDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtDownCount.setStatus("current")
_VRtrIfBfdSessExtLclDisc_Type = Unsigned32
_VRtrIfBfdSessExtLclDisc_Object = MibTableColumn
vRtrIfBfdSessExtLclDisc = _VRtrIfBfdSessExtLclDisc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 16),
    _VRtrIfBfdSessExtLclDisc_Type()
)
vRtrIfBfdSessExtLclDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLclDisc.setStatus("current")
_VRtrIfBfdSessExtRemDisc_Type = Unsigned32
_VRtrIfBfdSessExtRemDisc_Object = MibTableColumn
vRtrIfBfdSessExtRemDisc = _VRtrIfBfdSessExtRemDisc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 17),
    _VRtrIfBfdSessExtRemDisc_Type()
)
vRtrIfBfdSessExtRemDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemDisc.setStatus("current")


class _VRtrIfBfdSessExtProtocols_Type(Bits):
    """Custom type vRtrIfBfdSessExtProtocols based on Bits"""
    namedValues = NamedValues(
        *(("ospfv2", 0),
          ("pim", 1),
          ("isis", 2),
          ("staticRoute", 3),
          ("mcRing", 4),
          ("rsvp", 5),
          ("bgp", 6),
          ("vrrp", 7),
          ("srrp", 8),
          ("mcep", 9),
          ("ldp", 10),
          ("ipsecTunnel", 11),
          ("ospfv3", 12),
          ("mcIpsec", 13),
          ("mcMobile", 14),
          ("mplsTp", 15),
          ("lag", 16))
    )

_VRtrIfBfdSessExtProtocols_Type.__name__ = "Bits"
_VRtrIfBfdSessExtProtocols_Object = MibTableColumn
vRtrIfBfdSessExtProtocols = _VRtrIfBfdSessExtProtocols_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 18),
    _VRtrIfBfdSessExtProtocols_Type()
)
vRtrIfBfdSessExtProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtProtocols.setStatus("current")
_VRtrIfBfdSessExtTxInterval_Type = Unsigned32
_VRtrIfBfdSessExtTxInterval_Object = MibTableColumn
vRtrIfBfdSessExtTxInterval = _VRtrIfBfdSessExtTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 19),
    _VRtrIfBfdSessExtTxInterval_Type()
)
vRtrIfBfdSessExtTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtTxInterval.setUnits("milliseconds")
_VRtrIfBfdSessExtRxInterval_Type = Unsigned32
_VRtrIfBfdSessExtRxInterval_Object = MibTableColumn
vRtrIfBfdSessExtRxInterval = _VRtrIfBfdSessExtRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 20),
    _VRtrIfBfdSessExtRxInterval_Type()
)
vRtrIfBfdSessExtRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRxInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRxInterval.setUnits("milliseconds")


class _VRtrIfBfdSessExtType_Type(Integer32):
    """Custom type vRtrIfBfdSessExtType based on Integer32"""
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
        *(("iom", 1),
          ("cpm", 2),
          ("cpmNp", 3),
          ("iomHw", 4))
    )


_VRtrIfBfdSessExtType_Type.__name__ = "Integer32"
_VRtrIfBfdSessExtType_Object = MibTableColumn
vRtrIfBfdSessExtType = _VRtrIfBfdSessExtType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 21),
    _VRtrIfBfdSessExtType_Type()
)
vRtrIfBfdSessExtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtType.setStatus("current")
_VRtrIfBfdSessExtVerMismatch_Type = Counter32
_VRtrIfBfdSessExtVerMismatch_Object = MibTableColumn
vRtrIfBfdSessExtVerMismatch = _VRtrIfBfdSessExtVerMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 22),
    _VRtrIfBfdSessExtVerMismatch_Type()
)
vRtrIfBfdSessExtVerMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtVerMismatch.setStatus("current")
_VRtrIfBfdSessExtTimeSinceLastRx_Type = Unsigned32
_VRtrIfBfdSessExtTimeSinceLastRx_Object = MibTableColumn
vRtrIfBfdSessExtTimeSinceLastRx = _VRtrIfBfdSessExtTimeSinceLastRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 23),
    _VRtrIfBfdSessExtTimeSinceLastRx_Type()
)
vRtrIfBfdSessExtTimeSinceLastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtTimeSinceLastRx.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtTimeSinceLastRx.setUnits("milliseconds")
_VRtrIfBfdSessExtTimeSinceLastTx_Type = Unsigned32
_VRtrIfBfdSessExtTimeSinceLastTx_Object = MibTableColumn
vRtrIfBfdSessExtTimeSinceLastTx = _VRtrIfBfdSessExtTimeSinceLastTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 24),
    _VRtrIfBfdSessExtTimeSinceLastTx_Type()
)
vRtrIfBfdSessExtTimeSinceLastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtTimeSinceLastTx.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtTimeSinceLastTx.setUnits("milliseconds")
_VRtrIfBfdSessExtRemoteLspNum_Type = Unsigned32
_VRtrIfBfdSessExtRemoteLspNum_Object = MibTableColumn
vRtrIfBfdSessExtRemoteLspNum = _VRtrIfBfdSessExtRemoteLspNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 25),
    _VRtrIfBfdSessExtRemoteLspNum_Type()
)
vRtrIfBfdSessExtRemoteLspNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemoteLspNum.setStatus("current")
_VRtrIfBfdSessExtRemoteTunnelNum_Type = Unsigned32
_VRtrIfBfdSessExtRemoteTunnelNum_Object = MibTableColumn
vRtrIfBfdSessExtRemoteTunnelNum = _VRtrIfBfdSessExtRemoteTunnelNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 26),
    _VRtrIfBfdSessExtRemoteTunnelNum_Type()
)
vRtrIfBfdSessExtRemoteTunnelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemoteTunnelNum.setStatus("current")
_VRtrIfBfdSessExtRemoteNodeId_Type = TmnxMplsTpNodeID
_VRtrIfBfdSessExtRemoteNodeId_Object = MibTableColumn
vRtrIfBfdSessExtRemoteNodeId = _VRtrIfBfdSessExtRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 27),
    _VRtrIfBfdSessExtRemoteNodeId_Type()
)
vRtrIfBfdSessExtRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemoteNodeId.setStatus("current")
_VRtrIfBfdSessExtRemoteGlobalId_Type = TmnxMplsTpGlobalID
_VRtrIfBfdSessExtRemoteGlobalId_Object = MibTableColumn
vRtrIfBfdSessExtRemoteGlobalId = _VRtrIfBfdSessExtRemoteGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 28),
    _VRtrIfBfdSessExtRemoteGlobalId_Type()
)
vRtrIfBfdSessExtRemoteGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemoteGlobalId.setStatus("current")
_VRtrIfBfdSessExtLspPathTunnelId_Type = Unsigned32
_VRtrIfBfdSessExtLspPathTunnelId_Object = MibTableColumn
vRtrIfBfdSessExtLspPathTunnelId = _VRtrIfBfdSessExtLspPathTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 29),
    _VRtrIfBfdSessExtLspPathTunnelId_Type()
)
vRtrIfBfdSessExtLspPathTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLspPathTunnelId.setStatus("current")


class _VRtrIfBfdSessExtLspPathId_Type(Integer32):
    """Custom type vRtrIfBfdSessExtLspPathId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("working", 1),
          ("protecting", 2))
    )


_VRtrIfBfdSessExtLspPathId_Type.__name__ = "Integer32"
_VRtrIfBfdSessExtLspPathId_Object = MibTableColumn
vRtrIfBfdSessExtLspPathId = _VRtrIfBfdSessExtLspPathId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 92, 1, 30),
    _VRtrIfBfdSessExtLspPathId_Type()
)
vRtrIfBfdSessExtLspPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLspPathId.setStatus("current")
_VRtrIfBfdSessForwardInfoTable_Object = MibTable
vRtrIfBfdSessForwardInfoTable = _VRtrIfBfdSessForwardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95)
)
if mibBuilder.loadTexts:
    vRtrIfBfdSessForwardInfoTable.setStatus("current")
_VRtrIfBfdSessForwardInfoEntry_Object = MibTableRow
vRtrIfBfdSessForwardInfoEntry = _VRtrIfBfdSessForwardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1)
)
if mibBuilder.loadTexts:
    vRtrIfBfdSessForwardInfoEntry.setStatus("current")


class _VRtrIfBfdSessExtLclState_Type(Integer32):
    """Custom type vRtrIfBfdSessExtLclState based on Integer32"""
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
        *(("adminDown", 0),
          ("down", 1),
          ("init", 2),
          ("up", 3))
    )


_VRtrIfBfdSessExtLclState_Type.__name__ = "Integer32"
_VRtrIfBfdSessExtLclState_Object = MibTableColumn
vRtrIfBfdSessExtLclState = _VRtrIfBfdSessExtLclState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 1),
    _VRtrIfBfdSessExtLclState_Type()
)
vRtrIfBfdSessExtLclState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLclState.setStatus("current")


class _VRtrIfBfdSessExtLclMode_Type(Integer32):
    """Custom type vRtrIfBfdSessExtLclMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("async", 0),
          ("demand", 1))
    )


_VRtrIfBfdSessExtLclMode_Type.__name__ = "Integer32"
_VRtrIfBfdSessExtLclMode_Object = MibTableColumn
vRtrIfBfdSessExtLclMode = _VRtrIfBfdSessExtLclMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 2),
    _VRtrIfBfdSessExtLclMode_Type()
)
vRtrIfBfdSessExtLclMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLclMode.setStatus("current")


class _VRtrIfBfdSessExtLclDiag_Type(Integer32):
    """Custom type vRtrIfBfdSessExtLclDiag based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("detTimeExp", 1),
          ("echoFuncFail", 2),
          ("nbSigSessDown", 3),
          ("fwdPlnRst", 4),
          ("pathDown", 5),
          ("conPathDown", 6),
          ("adminDown", 7),
          ("rvConPathDown", 8))
    )


_VRtrIfBfdSessExtLclDiag_Type.__name__ = "Integer32"
_VRtrIfBfdSessExtLclDiag_Object = MibTableColumn
vRtrIfBfdSessExtLclDiag = _VRtrIfBfdSessExtLclDiag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 3),
    _VRtrIfBfdSessExtLclDiag_Type()
)
vRtrIfBfdSessExtLclDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLclDiag.setStatus("current")
_VRtrIfBfdSessExtLclMinTx_Type = Unsigned32
_VRtrIfBfdSessExtLclMinTx_Object = MibTableColumn
vRtrIfBfdSessExtLclMinTx = _VRtrIfBfdSessExtLclMinTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 4),
    _VRtrIfBfdSessExtLclMinTx_Type()
)
vRtrIfBfdSessExtLclMinTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLclMinTx.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLclMinTx.setUnits("milliseconds")
_VRtrIfBfdSessExtLclMinRx_Type = Unsigned32
_VRtrIfBfdSessExtLclMinRx_Object = MibTableColumn
vRtrIfBfdSessExtLclMinRx = _VRtrIfBfdSessExtLclMinRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 5),
    _VRtrIfBfdSessExtLclMinRx_Type()
)
vRtrIfBfdSessExtLclMinRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLclMinRx.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLclMinRx.setUnits("milliseconds")
_VRtrIfBfdSessExtLclMult_Type = Unsigned32
_VRtrIfBfdSessExtLclMult_Object = MibTableColumn
vRtrIfBfdSessExtLclMult = _VRtrIfBfdSessExtLclMult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 6),
    _VRtrIfBfdSessExtLclMult_Type()
)
vRtrIfBfdSessExtLclMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLclMult.setStatus("current")


class _VRtrIfBfdSessExtRemState_Type(Integer32):
    """Custom type vRtrIfBfdSessExtRemState based on Integer32"""
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
        *(("adminDown", 0),
          ("down", 1),
          ("init", 2),
          ("up", 3))
    )


_VRtrIfBfdSessExtRemState_Type.__name__ = "Integer32"
_VRtrIfBfdSessExtRemState_Object = MibTableColumn
vRtrIfBfdSessExtRemState = _VRtrIfBfdSessExtRemState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 7),
    _VRtrIfBfdSessExtRemState_Type()
)
vRtrIfBfdSessExtRemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemState.setStatus("current")


class _VRtrIfBfdSessExtRemMode_Type(Integer32):
    """Custom type vRtrIfBfdSessExtRemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("async", 0),
          ("demand", 1))
    )


_VRtrIfBfdSessExtRemMode_Type.__name__ = "Integer32"
_VRtrIfBfdSessExtRemMode_Object = MibTableColumn
vRtrIfBfdSessExtRemMode = _VRtrIfBfdSessExtRemMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 8),
    _VRtrIfBfdSessExtRemMode_Type()
)
vRtrIfBfdSessExtRemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemMode.setStatus("current")


class _VRtrIfBfdSessExtRemDiag_Type(Integer32):
    """Custom type vRtrIfBfdSessExtRemDiag based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("detTimeExp", 1),
          ("echoFuncFail", 2),
          ("nbSigSessDown", 3),
          ("fwdPlnRst", 4),
          ("pathDown", 5),
          ("conPathDown", 6),
          ("adminDown", 7),
          ("rvConPathDown", 8))
    )


_VRtrIfBfdSessExtRemDiag_Type.__name__ = "Integer32"
_VRtrIfBfdSessExtRemDiag_Object = MibTableColumn
vRtrIfBfdSessExtRemDiag = _VRtrIfBfdSessExtRemDiag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 9),
    _VRtrIfBfdSessExtRemDiag_Type()
)
vRtrIfBfdSessExtRemDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemDiag.setStatus("current")
_VRtrIfBfdSessExtRemMinTx_Type = Unsigned32
_VRtrIfBfdSessExtRemMinTx_Object = MibTableColumn
vRtrIfBfdSessExtRemMinTx = _VRtrIfBfdSessExtRemMinTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 10),
    _VRtrIfBfdSessExtRemMinTx_Type()
)
vRtrIfBfdSessExtRemMinTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemMinTx.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemMinTx.setUnits("milliseconds")
_VRtrIfBfdSessExtRemMinRx_Type = Unsigned32
_VRtrIfBfdSessExtRemMinRx_Object = MibTableColumn
vRtrIfBfdSessExtRemMinRx = _VRtrIfBfdSessExtRemMinRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 11),
    _VRtrIfBfdSessExtRemMinRx_Type()
)
vRtrIfBfdSessExtRemMinRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemMinRx.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemMinRx.setUnits("milliseconds")
_VRtrIfBfdSessExtRemMult_Type = Unsigned32
_VRtrIfBfdSessExtRemMult_Object = MibTableColumn
vRtrIfBfdSessExtRemMult = _VRtrIfBfdSessExtRemMult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 12),
    _VRtrIfBfdSessExtRemMult_Type()
)
vRtrIfBfdSessExtRemMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtRemMult.setStatus("current")
_VRtrIfBfdSessExtLastRecv_Type = TimeStamp
_VRtrIfBfdSessExtLastRecv_Object = MibTableColumn
vRtrIfBfdSessExtLastRecv = _VRtrIfBfdSessExtLastRecv_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 13),
    _VRtrIfBfdSessExtLastRecv_Type()
)
vRtrIfBfdSessExtLastRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLastRecv.setStatus("current")
_VRtrIfBfdSessExtLastSent_Type = TimeStamp
_VRtrIfBfdSessExtLastSent_Object = MibTableColumn
vRtrIfBfdSessExtLastSent = _VRtrIfBfdSessExtLastSent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 95, 1, 14),
    _VRtrIfBfdSessExtLastSent_Type()
)
vRtrIfBfdSessExtLastSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessExtLastSent.setStatus("current")
_VRtrConfScalar1_Type = Unsigned32
_VRtrConfScalar1_Object = MibScalar
vRtrConfScalar1 = _VRtrConfScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 101),
    _VRtrConfScalar1_Type()
)
vRtrConfScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrConfScalar1.setStatus("current")
_VRtrConfScalar2_Type = Unsigned32
_VRtrConfScalar2_Object = MibScalar
vRtrConfScalar2 = _VRtrConfScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 3, 102),
    _VRtrConfScalar2_Type()
)
vRtrConfScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrConfScalar2.setStatus("current")
vRtrConfEntry.registerAugmentions(
    ("TN-VRTR-MIB",
     "vRtrStatEntry")
)
vRtrStatEntry.setIndexNames(*vRtrConfEntry.getIndexNames())
vRtrIfEntry.registerAugmentions(
    ("TN-VRTR-MIB",
     "vRtrIfExtEntry")
)
vRtrIfExtEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrIfStatsEntry.registerAugmentions(
    ("TN-VRTR-MIB",
     "vRtrIfStatsExtEntry")
)
vRtrIfStatsExtEntry.setIndexNames(*vRtrIfStatsEntry.getIndexNames())
vRtrIfEntry.registerAugmentions(
    ("TN-VRTR-MIB",
     "vRtrIfQosEntry")
)
vRtrIfQosEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrIfBfdSessExtEntry.registerAugmentions(
    ("TN-VRTR-MIB",
     "vRtrIfBfdSessForwardInfoEntry")
)
vRtrIfBfdSessForwardInfoEntry.setIndexNames(*vRtrIfBfdSessExtEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-VRTR-MIB",
    **{"TmnxVPNId": TmnxVPNId,
       "TmnxInetAddrState": TmnxInetAddrState,
       "TDSCPAppId": TDSCPAppId,
       "TDot1pAppId": TDot1pAppId,
       "TmnxVrtrSingleSfmOverloadState": TmnxVrtrSingleSfmOverloadState,
       "TmnxInetCidrNextHopType": TmnxInetCidrNextHopType,
       "TmnxInetCidrNextHopOwner": TmnxInetCidrNextHopOwner,
       "TmnxL3RouteOwner": TmnxL3RouteOwner,
       "tnVRtrMIBModule": tnVRtrMIBModule,
       "tnVRtrObjs": tnVRtrObjs,
       "vRtrConfTable": vRtrConfTable,
       "vRtrConfEntry": vRtrConfEntry,
       "vRtrID": vRtrID,
       "vRtrRowStatus": vRtrRowStatus,
       "vRtrAdminState": vRtrAdminState,
       "vRtrName": vRtrName,
       "vRtrMaxNumRoutes": vRtrMaxNumRoutes,
       "vRtrBgpStatus": vRtrBgpStatus,
       "vRtrMplsStatus": vRtrMplsStatus,
       "vRtrOspfStatus": vRtrOspfStatus,
       "vRtrRipStatus": vRtrRipStatus,
       "vRtrRsvpStatus": vRtrRsvpStatus,
       "vRtrEcmpMaxRoutes": vRtrEcmpMaxRoutes,
       "vRtrAS": vRtrAS,
       "vRtrNewIfIndex": vRtrNewIfIndex,
       "vRtrLdpStatus": vRtrLdpStatus,
       "vRtrIsIsStatus": vRtrIsIsStatus,
       "vRtrRouterId": vRtrRouterId,
       "vRtrTriggeredPolicy": vRtrTriggeredPolicy,
       "vRtrConfederationAS": vRtrConfederationAS,
       "vRtrRouteDistinguisher": vRtrRouteDistinguisher,
       "vRtrMidRouteThreshold": vRtrMidRouteThreshold,
       "vRtrHighRouteThreshold": vRtrHighRouteThreshold,
       "vRtrIllegalLabelThreshold": vRtrIllegalLabelThreshold,
       "vRtrVpnId": vRtrVpnId,
       "vRtrDescription": vRtrDescription,
       "vRtrGracefulRestart": vRtrGracefulRestart,
       "vRtrGracefulRestartType": vRtrGracefulRestartType,
       "vRtrType": vRtrType,
       "vRtrServiceId": vRtrServiceId,
       "vRtrCustId": vRtrCustId,
       "vRtrIgmpStatus": vRtrIgmpStatus,
       "vRtrMaxNumRoutesLogOnly": vRtrMaxNumRoutesLogOnly,
       "vRtrVrfTarget": vRtrVrfTarget,
       "vRtrVrfExportTarget": vRtrVrfExportTarget,
       "vRtrVrfImportTarget": vRtrVrfImportTarget,
       "vRtrPimStatus": vRtrPimStatus,
       "vRtrMaxMcastNumRoutes": vRtrMaxMcastNumRoutes,
       "vRtrMaxMcastNumRoutesLogOnly": vRtrMaxMcastNumRoutesLogOnly,
       "vRtrMcastMidRouteThreshold": vRtrMcastMidRouteThreshold,
       "vRtrIgnoreIcmpRedirect": vRtrIgnoreIcmpRedirect,
       "vRtrOspfv3Status": vRtrOspfv3Status,
       "vRtrMsdpStatus": vRtrMsdpStatus,
       "vRtrVprnType": vRtrVprnType,
       "vRtrSecondaryVrfId": vRtrSecondaryVrfId,
       "vRtrMldStatus": vRtrMldStatus,
       "vRtrIPv6MaxNumRoutes": vRtrIPv6MaxNumRoutes,
       "vRtrIPv6MidRouteThreshold": vRtrIPv6MidRouteThreshold,
       "vRtrIPv6HighRouteThreshold": vRtrIPv6HighRouteThreshold,
       "vRtrIPv6MaxNumRoutesLogOnly": vRtrIPv6MaxNumRoutesLogOnly,
       "vRtrIPv6IgnoreIcmpRedirect": vRtrIPv6IgnoreIcmpRedirect,
       "vRtrMcPathMgmtPlcyName": vRtrMcPathMgmtPlcyName,
       "vRtrIgnoreNextHopMetric": vRtrIgnoreNextHopMetric,
       "vRtrMvpnVrfTarget": vRtrMvpnVrfTarget,
       "vRtrMvpnVrfExportTarget": vRtrMvpnVrfExportTarget,
       "vRtrMvpnVrfImportTarget": vRtrMvpnVrfImportTarget,
       "vRtrMvpnVrfTargetUnicast": vRtrMvpnVrfTargetUnicast,
       "vRtrMvpnVrfExportTargetUnicast": vRtrMvpnVrfExportTargetUnicast,
       "vRtrMvpnVrfImportTargetUnicast": vRtrMvpnVrfImportTargetUnicast,
       "vRtrAS4Byte": vRtrAS4Byte,
       "vRtrConfederationAS4Byte": vRtrConfederationAS4Byte,
       "vRtrMvpnCMcastImportRT": vRtrMvpnCMcastImportRT,
       "vRtrInterASMvpn": vRtrInterASMvpn,
       "vRtrStatTable": vRtrStatTable,
       "vRtrStatEntry": vRtrStatEntry,
       "vRtrOperState": vRtrOperState,
       "vRtrDirectRoutes": vRtrDirectRoutes,
       "vRtrDirectActiveRoutes": vRtrDirectActiveRoutes,
       "vRtrStaticRoutes": vRtrStaticRoutes,
       "vRtrStaticActiveRoutes": vRtrStaticActiveRoutes,
       "vRtrOSPFRoutes": vRtrOSPFRoutes,
       "vRtrOSPFActiveRoutes": vRtrOSPFActiveRoutes,
       "vRtrBGPRoutes": vRtrBGPRoutes,
       "vRtrBGPActiveRoutes": vRtrBGPActiveRoutes,
       "vRtrISISRoutes": vRtrISISRoutes,
       "vRtrISISActiveRoutes": vRtrISISActiveRoutes,
       "vRtrRIPRoutes": vRtrRIPRoutes,
       "vRtrRIPActiveRoutes": vRtrRIPActiveRoutes,
       "vRtrAggregateRoutes": vRtrAggregateRoutes,
       "vRtrAggregateActiveRoutes": vRtrAggregateActiveRoutes,
       "vRtrStatConfiguredIfs": vRtrStatConfiguredIfs,
       "vRtrStatActiveIfs": vRtrStatActiveIfs,
       "vRtrStatIllegalLabels": vRtrStatIllegalLabels,
       "vRtrStatCurrNumRoutes": vRtrStatCurrNumRoutes,
       "vRtrStatBGPVpnRoutes": vRtrStatBGPVpnRoutes,
       "vRtrStatBGPVpnActiveRoutes": vRtrStatBGPVpnActiveRoutes,
       "vRtrStatTotalLdpTunnels": vRtrStatTotalLdpTunnels,
       "vRtrStatTotalSdpTunnels": vRtrStatTotalSdpTunnels,
       "vRtrStatActiveLdpTunnels": vRtrStatActiveLdpTunnels,
       "vRtrStatActiveSdpTunnels": vRtrStatActiveSdpTunnels,
       "vRtrMulticastRoutes": vRtrMulticastRoutes,
       "vRtrStatActiveARPEntries": vRtrStatActiveARPEntries,
       "vRtrStatTotalARPEntries": vRtrStatTotalARPEntries,
       "vRtrV6DirectRoutes": vRtrV6DirectRoutes,
       "vRtrV6DirectActiveRoutes": vRtrV6DirectActiveRoutes,
       "vRtrV6StaticRoutes": vRtrV6StaticRoutes,
       "vRtrV6StaticActiveRoutes": vRtrV6StaticActiveRoutes,
       "vRtrV6OSPFRoutes": vRtrV6OSPFRoutes,
       "vRtrV6OSPFActiveRoutes": vRtrV6OSPFActiveRoutes,
       "vRtrV6BGPRoutes": vRtrV6BGPRoutes,
       "vRtrV6BGPActiveRoutes": vRtrV6BGPActiveRoutes,
       "vRtrV6ISISRoutes": vRtrV6ISISRoutes,
       "vRtrV6ISISActiveRoutes": vRtrV6ISISActiveRoutes,
       "vRtrV6RIPRoutes": vRtrV6RIPRoutes,
       "vRtrV6RIPActiveRoutes": vRtrV6RIPActiveRoutes,
       "vRtrV6AggregateRoutes": vRtrV6AggregateRoutes,
       "vRtrV6AggregateActiveRoutes": vRtrV6AggregateActiveRoutes,
       "vRtrV6StatConfiguredIfs": vRtrV6StatConfiguredIfs,
       "vRtrV6StatActiveIfs": vRtrV6StatActiveIfs,
       "vRtrV6StatIllegalLabels": vRtrV6StatIllegalLabels,
       "vRtrV6StatCurrNumRoutes": vRtrV6StatCurrNumRoutes,
       "vRtrV6StatBGPVpnRoutes": vRtrV6StatBGPVpnRoutes,
       "vRtrV6StatBGPVpnActiveRoutes": vRtrV6StatBGPVpnActiveRoutes,
       "vRtrV6StatTotalLdpTunnels": vRtrV6StatTotalLdpTunnels,
       "vRtrV6StatTotalSdpTunnels": vRtrV6StatTotalSdpTunnels,
       "vRtrV6StatActiveLdpTunnels": vRtrV6StatActiveLdpTunnels,
       "vRtrV6StatActiveSdpTunnels": vRtrV6StatActiveSdpTunnels,
       "vRtrV6MulticastRoutes": vRtrV6MulticastRoutes,
       "vRtrV6StatActiveNbrEntries": vRtrV6StatActiveNbrEntries,
       "vRtrV6StatTotalNbrEntries": vRtrV6StatTotalNbrEntries,
       "vRtrSubMgmtRoutes": vRtrSubMgmtRoutes,
       "vRtrSubMgmtActiveRoutes": vRtrSubMgmtActiveRoutes,
       "vRtrStatTotalRsvpTunnels": vRtrStatTotalRsvpTunnels,
       "vRtrStatActiveRsvpTunnels": vRtrStatActiveRsvpTunnels,
       "vRtrV6StatTotalRsvpTunnels": vRtrV6StatTotalRsvpTunnels,
       "vRtrV6StatActiveRsvpTunnels": vRtrV6StatActiveRsvpTunnels,
       "vRtrHostRoutes": vRtrHostRoutes,
       "vRtrHostActiveRoutes": vRtrHostActiveRoutes,
       "vRtrV6HostRoutes": vRtrV6HostRoutes,
       "vRtrV6HostActiveRoutes": vRtrV6HostActiveRoutes,
       "vRtrStatLocalARPEntries": vRtrStatLocalARPEntries,
       "vRtrStatStaticARPEntries": vRtrStatStaticARPEntries,
       "vRtrStatDynamicARPEntries": vRtrStatDynamicARPEntries,
       "vRtrStatManagedARPEntries": vRtrStatManagedARPEntries,
       "vRtrStatInternalARPEntries": vRtrStatInternalARPEntries,
       "vRtrManagedRoutes": vRtrManagedRoutes,
       "vRtrManagedActiveRoutes": vRtrManagedActiveRoutes,
       "vRtrLDPRoutes": vRtrLDPRoutes,
       "vRtrLDPActiveRoutes": vRtrLDPActiveRoutes,
       "vRtrVPNLeakRoutes": vRtrVPNLeakRoutes,
       "vRtrVPNLeakActiveRoutes": vRtrVPNLeakActiveRoutes,
       "vRtrV6VPNLeakRoutes": vRtrV6VPNLeakRoutes,
       "vRtrV6VPNLeakActiveRoutes": vRtrV6VPNLeakActiveRoutes,
       "vRtrV6SubMgmtRoutes": vRtrV6SubMgmtRoutes,
       "vRtrV6SubMgmtActiveRoutes": vRtrV6SubMgmtActiveRoutes,
       "vRtrMobileHostRoutes": vRtrMobileHostRoutes,
       "vRtrMobileHostActiveRoutes": vRtrMobileHostActiveRoutes,
       "vRtrV6MobileHostRoutes": vRtrV6MobileHostRoutes,
       "vRtrV6MobileHostActiveRoutes": vRtrV6MobileHostActiveRoutes,
       "vRtrStatTotalBgpTunnels": vRtrStatTotalBgpTunnels,
       "vRtrStatActiveBgpTunnels": vRtrStatActiveBgpTunnels,
       "vRtrNatRoutes": vRtrNatRoutes,
       "vRtrNatActiveRoutes": vRtrNatActiveRoutes,
       "vRtrV6NatRoutes": vRtrV6NatRoutes,
       "vRtrV6NatActiveRoutes": vRtrV6NatActiveRoutes,
       "vRtrPeriodicRoutes": vRtrPeriodicRoutes,
       "vRtrPeriodicActiveRoutes": vRtrPeriodicActiveRoutes,
       "vRtrV6PeriodicRoutes": vRtrV6PeriodicRoutes,
       "vRtrV6PeriodicActiveRoutes": vRtrV6PeriodicActiveRoutes,
       "vRtrStatTotalMplsTpTunnels": vRtrStatTotalMplsTpTunnels,
       "vRtrStatActiveMplsTpTunnels": vRtrStatActiveMplsTpTunnels,
       "vRtrIfTotalNumber": vRtrIfTotalNumber,
       "vRtrIfTable": vRtrIfTable,
       "vRtrIfEntry": vRtrIfEntry,
       "vRtrIfIndex": vRtrIfIndex,
       "vRtrIfRowStatus": vRtrIfRowStatus,
       "vRtrIfType": vRtrIfType,
       "vRtrIfName": vRtrIfName,
       "vRtrIfPortID": vRtrIfPortID,
       "vRtrIfChannelID": vRtrIfChannelID,
       "vRtrIfEncapValue": vRtrIfEncapValue,
       "vRtrIfAdminState": vRtrIfAdminState,
       "vRtrIfOperState": vRtrIfOperState,
       "vRtrIfAlias": vRtrIfAlias,
       "vRtrIfPhysicalAddress": vRtrIfPhysicalAddress,
       "vRtrIfArpTimeout": vRtrIfArpTimeout,
       "vRtrIfIcmpMaskReply": vRtrIfIcmpMaskReply,
       "vRtrIfIcmpRedirects": vRtrIfIcmpRedirects,
       "vRtrIfIcmpNumRedirects": vRtrIfIcmpNumRedirects,
       "vRtrIfIcmpRedirectsTime": vRtrIfIcmpRedirectsTime,
       "vRtrIfIcmpUnreachables": vRtrIfIcmpUnreachables,
       "vRtrIfIcmpNumUnreachables": vRtrIfIcmpNumUnreachables,
       "vRtrIfIcmpUnreachablesTime": vRtrIfIcmpUnreachablesTime,
       "vRtrIfIcmpTtlExpired": vRtrIfIcmpTtlExpired,
       "vRtrIfIcmpNumTtlExpired": vRtrIfIcmpNumTtlExpired,
       "vRtrIfIcmpTtlExpiredTime": vRtrIfIcmpTtlExpiredTime,
       "vRtrIfNtpBroadcast": vRtrIfNtpBroadcast,
       "vRtrIfUnnumbered": vRtrIfUnnumbered,
       "vRtrIfMtu": vRtrIfMtu,
       "vRtrIfQosPolicyId": vRtrIfQosPolicyId,
       "vRtrIfIngressFilterId": vRtrIfIngressFilterId,
       "vRtrIfEgressFilterId": vRtrIfEgressFilterId,
       "vRtrIfDirectedBroadcast": vRtrIfDirectedBroadcast,
       "vRtrIfMplsStatus": vRtrIfMplsStatus,
       "vRtrIfUnnumberedIf": vRtrIfUnnumberedIf,
       "vRtrIfCflowd": vRtrIfCflowd,
       "vRtrIfVPNClass": vRtrIfVPNClass,
       "vRtrIfDescription": vRtrIfDescription,
       "vRtrIfProtocol": vRtrIfProtocol,
       "vRtrIfTosMarkingTrusted": vRtrIfTosMarkingTrusted,
       "vRtrIfServiceId": vRtrIfServiceId,
       "vRtrIfArpPopulate": vRtrIfArpPopulate,
       "vRtrIfIPv6ConfigAllowed": vRtrIfIPv6ConfigAllowed,
       "vRtrIfIPv6OperState": vRtrIfIPv6OperState,
       "vRtrIfIPv6IngressFilterId": vRtrIfIPv6IngressFilterId,
       "vRtrIfIPv6EgressFilterId": vRtrIfIPv6EgressFilterId,
       "vRtrIfIcmpV6Redirects": vRtrIfIcmpV6Redirects,
       "vRtrIfIcmpV6NumRedirects": vRtrIfIcmpV6NumRedirects,
       "vRtrIfIcmpV6RedirectsTime": vRtrIfIcmpV6RedirectsTime,
       "vRtrIfIcmpV6Unreachables": vRtrIfIcmpV6Unreachables,
       "vRtrIfIcmpV6NumUnreachables": vRtrIfIcmpV6NumUnreachables,
       "vRtrIfIcmpV6UnreachablesTime": vRtrIfIcmpV6UnreachablesTime,
       "vRtrIfIcmpV6TimeExceeded": vRtrIfIcmpV6TimeExceeded,
       "vRtrIfIcmpV6NumTimeExceeded": vRtrIfIcmpV6NumTimeExceeded,
       "vRtrIfIcmpV6TimeExceededTime": vRtrIfIcmpV6TimeExceededTime,
       "vRtrIfIcmpV6PktTooBig": vRtrIfIcmpV6PktTooBig,
       "vRtrIfIcmpV6NumPktTooBig": vRtrIfIcmpV6NumPktTooBig,
       "vRtrIfIcmpV6PktTooBigTime": vRtrIfIcmpV6PktTooBigTime,
       "vRtrIfIcmpV6ParamProblem": vRtrIfIcmpV6ParamProblem,
       "vRtrIfIcmpV6NumParamProblem": vRtrIfIcmpV6NumParamProblem,
       "vRtrIfIcmpV6ParamProblemTime": vRtrIfIcmpV6ParamProblemTime,
       "vRtrIfLinkLocalAddressType": vRtrIfLinkLocalAddressType,
       "vRtrIfLinkLocalAddress": vRtrIfLinkLocalAddress,
       "vRtrIfLinkLocalAddressState": vRtrIfLinkLocalAddressState,
       "vRtrIfLastOperStateChange": vRtrIfLastOperStateChange,
       "vRtrIfOperMtu": vRtrIfOperMtu,
       "vRtrIfGlobalIndex": vRtrIfGlobalIndex,
       "vRtrIfDelaySeconds": vRtrIfDelaySeconds,
       "vRtrIfDelayUpTimer": vRtrIfDelayUpTimer,
       "vRtrIfLocalDhcpServerName": vRtrIfLocalDhcpServerName,
       "vRtrIfInitDelayEnable": vRtrIfInitDelayEnable,
       "vRtrIfCpmProtPolicyId": vRtrIfCpmProtPolicyId,
       "vRtrIfCpmProtUncfgdProtoDropCnt": vRtrIfCpmProtUncfgdProtoDropCnt,
       "vRtrIfLdpSyncTimer": vRtrIfLdpSyncTimer,
       "vRtrIfStripLabel": vRtrIfStripLabel,
       "vRtrIfuRPFCheckState": vRtrIfuRPFCheckState,
       "vRtrIfuRPFCheckMode": vRtrIfuRPFCheckMode,
       "vRtrIfQosQGrp": vRtrIfQosQGrp,
       "vRtrIfAdminLinkLocalAddrType": vRtrIfAdminLinkLocalAddrType,
       "vRtrIfAdminLinkLocalAddr": vRtrIfAdminLinkLocalAddr,
       "vRtrIfAdmLnkLclAddrPreferred": vRtrIfAdmLnkLclAddrPreferred,
       "vRtrIfOperDownReason": vRtrIfOperDownReason,
       "vRtrIfNameTable": vRtrIfNameTable,
       "vRtrIfNameEntry": vRtrIfNameEntry,
       "vRtrIfNameIndex": vRtrIfNameIndex,
       "vRtrIpAddrTable": vRtrIpAddrTable,
       "vRtrIpAddrEntry": vRtrIpAddrEntry,
       "vRiaIndex": vRiaIndex,
       "vRiaRowStatus": vRiaRowStatus,
       "vRiaIpAddress": vRiaIpAddress,
       "vRiaNetMask": vRiaNetMask,
       "vRiaBcastAddrFormat": vRiaBcastAddrFormat,
       "vRiaReasmMaxSize": vRiaReasmMaxSize,
       "vRiaIgpInhibit": vRiaIgpInhibit,
       "vRiaInetAddressType": vRiaInetAddressType,
       "vRiaInetAddress": vRiaInetAddress,
       "vRiaInetPrefixLen": vRiaInetPrefixLen,
       "vRiaInetAddrState": vRiaInetAddrState,
       "vRiaInetEui64": vRiaInetEui64,
       "vRiaInetOperAddress": vRiaInetOperAddress,
       "vRiaInetGwAddressType": vRiaInetGwAddressType,
       "vRiaInetGwAddress": vRiaInetGwAddress,
       "vRiaInetRemoteIpType": vRiaInetRemoteIpType,
       "vRiaInetRemoteIp": vRiaInetRemoteIp,
       "vRiaInetAddrPreferred": vRiaInetAddrPreferred,
       "vRiaSubscrPrefix": vRiaSubscrPrefix,
       "vRiaSubscrPrefixType": vRiaSubscrPrefixType,
       "vRiaSubscrHostRoutePopulate": vRiaSubscrHostRoutePopulate,
       "vRiaTrackSrrpInstance": vRiaTrackSrrpInstance,
       "vRiaHoldUpTime": vRiaHoldUpTime,
       "tnVRtrGlobalObjs": tnVRtrGlobalObjs,
       "vRtrNextVRtrID": vRtrNextVRtrID,
       "vRtrConfiguredVRtrs": vRtrConfiguredVRtrs,
       "vRtrActiveVRtrs": vRtrActiveVRtrs,
       "vRtrRouteThresholdSoakTime": vRtrRouteThresholdSoakTime,
       "vRtrMaxARPEntries": vRtrMaxARPEntries,
       "vRtrIPv6RouteThresholdSoakTime": vRtrIPv6RouteThresholdSoakTime,
       "vRtrIfGlobalIndexTable": vRtrIfGlobalIndexTable,
       "vRtrIfGlobalIndexEntry": vRtrIfGlobalIndexEntry,
       "vRtrIfGlobalIndexvRtrID": vRtrIfGlobalIndexvRtrID,
       "vRtrIfGlobalIndexvRtrIfIndex": vRtrIfGlobalIndexvRtrIfIndex,
       "vRtrIfStatsTable": vRtrIfStatsTable,
       "vRtrIfStatsEntry": vRtrIfStatsEntry,
       "vRtrIfuRPFCheckFailPkts": vRtrIfuRPFCheckFailPkts,
       "vRtrIfuRPFCheckFailPktsLow32": vRtrIfuRPFCheckFailPktsLow32,
       "vRtrIfuRPFCheckFailPktsHigh32": vRtrIfuRPFCheckFailPktsHigh32,
       "vRtrIfuRPFCheckFailBytes": vRtrIfuRPFCheckFailBytes,
       "vRtrIfuRPFCheckFailBytesLow32": vRtrIfuRPFCheckFailBytesLow32,
       "vRtrIfuRPFCheckFailBytesHigh32": vRtrIfuRPFCheckFailBytesHigh32,
       "vRtrIfIpReasFragPktsRcvd": vRtrIfIpReasFragPktsRcvd,
       "vRtrIfIpReasFragPktsRcvdLow32": vRtrIfIpReasFragPktsRcvdLow32,
       "vRtrIfIpReasFragPktsRcvdHigh32": vRtrIfIpReasFragPktsRcvdHigh32,
       "vRtrIfIpReasFragBytesRcvd": vRtrIfIpReasFragBytesRcvd,
       "vRtrIfIpReasFragBytesRcvdLow32": vRtrIfIpReasFragBytesRcvdLow32,
       "vRtrIfIpReasFragBytesRcvdHigh32": vRtrIfIpReasFragBytesRcvdHigh32,
       "vRtrIfIpReasFragPktsReas": vRtrIfIpReasFragPktsReas,
       "vRtrIfIpReasFragPktsReasLow32": vRtrIfIpReasFragPktsReasLow32,
       "vRtrIfIpReasFragPktsReasHigh32": vRtrIfIpReasFragPktsReasHigh32,
       "vRtrIfIpReasFragBytesReas": vRtrIfIpReasFragBytesReas,
       "vRtrIfIpReasFragBytesReasLow32": vRtrIfIpReasFragBytesReasLow32,
       "vRtrIfIpReasFragBytesReasHigh32": vRtrIfIpReasFragBytesReasHigh32,
       "vRtrIfIpReasFragReasErrors": vRtrIfIpReasFragReasErrors,
       "vRtrIfIpReasFragReasErrorsLow32": vRtrIfIpReasFragReasErrorsLow32,
       "vRtrIfIpReasFragReasErrorsHigh32": vRtrIfIpReasFragReasErrorsHigh32,
       "vRtrIfIpReasFragDisc": vRtrIfIpReasFragDisc,
       "vRtrIfIpReasFragDiscLow32": vRtrIfIpReasFragDiscLow32,
       "vRtrIfIpReasFragDiscHigh32": vRtrIfIpReasFragDiscHigh32,
       "vRtrIfIpReasOutBufRes": vRtrIfIpReasOutBufRes,
       "vRtrIfIpReasOutBufResLow32": vRtrIfIpReasOutBufResLow32,
       "vRtrIfIpReasOutBufResHigh32": vRtrIfIpReasOutBufResHigh32,
       "vRtrIfIpReasPktsRx": vRtrIfIpReasPktsRx,
       "vRtrIfIpReasPktsRxLow32": vRtrIfIpReasPktsRxLow32,
       "vRtrIfIpReasPktsRxHigh32": vRtrIfIpReasPktsRxHigh32,
       "vRtrIfIpReasBytesRx": vRtrIfIpReasBytesRx,
       "vRtrIfIpReasBytesRxLow32": vRtrIfIpReasBytesRxLow32,
       "vRtrIfIpReasBytesRxHigh32": vRtrIfIpReasBytesRxHigh32,
       "vRtrIfIpReasPktsTx": vRtrIfIpReasPktsTx,
       "vRtrIfIpReasPktsTxLow32": vRtrIfIpReasPktsTxLow32,
       "vRtrIfIpReasPktsTxHigh32": vRtrIfIpReasPktsTxHigh32,
       "vRtrIfIpReasBytesTx": vRtrIfIpReasBytesTx,
       "vRtrIfIpReasBytesTxLow32": vRtrIfIpReasBytesTxLow32,
       "vRtrIfIpReasBytesTxHigh32": vRtrIfIpReasBytesTxHigh32,
       "vRtrIfRxPkts": vRtrIfRxPkts,
       "vRtrIfRxPktsLow32": vRtrIfRxPktsLow32,
       "vRtrIfRxPktsHigh32": vRtrIfRxPktsHigh32,
       "vRtrIfRxBytes": vRtrIfRxBytes,
       "vRtrIfRxBytesLow32": vRtrIfRxBytesLow32,
       "vRtrIfRxBytesHigh32": vRtrIfRxBytesHigh32,
       "vRtrIfTxV4Pkts": vRtrIfTxV4Pkts,
       "vRtrIfTxV4PktsLow32": vRtrIfTxV4PktsLow32,
       "vRtrIfTxV4PktsHigh32": vRtrIfTxV4PktsHigh32,
       "vRtrIfTxV4Bytes": vRtrIfTxV4Bytes,
       "vRtrIfTxV4BytesLow32": vRtrIfTxV4BytesLow32,
       "vRtrIfTxV4BytesHigh32": vRtrIfTxV4BytesHigh32,
       "vRtrIfTxV6Pkts": vRtrIfTxV6Pkts,
       "vRtrIfTxV6PktsLow32": vRtrIfTxV6PktsLow32,
       "vRtrIfTxV6PktsHigh32": vRtrIfTxV6PktsHigh32,
       "vRtrIfTxV6Bytes": vRtrIfTxV6Bytes,
       "vRtrIfTxV6BytesLow32": vRtrIfTxV6BytesLow32,
       "vRtrIfTxV6BytesHigh32": vRtrIfTxV6BytesHigh32,
       "vRtrIfTxV4DiscardPkts": vRtrIfTxV4DiscardPkts,
       "vRtrIfTxV4DiscardPktsLow32": vRtrIfTxV4DiscardPktsLow32,
       "vRtrIfTxV4DiscardPktsHigh32": vRtrIfTxV4DiscardPktsHigh32,
       "vRtrIfTxV4DiscardBytes": vRtrIfTxV4DiscardBytes,
       "vRtrIfTxV4DiscardBytesLow32": vRtrIfTxV4DiscardBytesLow32,
       "vRtrIfTxV4DiscardBytesHigh32": vRtrIfTxV4DiscardBytesHigh32,
       "vRtrIfTxV6DiscardPkts": vRtrIfTxV6DiscardPkts,
       "vRtrIfTxV6DiscardPktsLow32": vRtrIfTxV6DiscardPktsLow32,
       "vRtrIfTxV6DiscardPktsHigh32": vRtrIfTxV6DiscardPktsHigh32,
       "vRtrIfTxV6DiscardBytes": vRtrIfTxV6DiscardBytes,
       "vRtrIfTxV6DiscardBytesLow32": vRtrIfTxV6DiscardBytesLow32,
       "vRtrIfTxV6DiscardBytesHigh32": vRtrIfTxV6DiscardBytesHigh32,
       "vRtrIfIpReasV6FragPktsRcvd": vRtrIfIpReasV6FragPktsRcvd,
       "vRtrIfIpReasV6FragPktsRcvdLow32": vRtrIfIpReasV6FragPktsRcvdLow32,
       "vRtrIfIpReasV6FragPktsRcvdHigh32": vRtrIfIpReasV6FragPktsRcvdHigh32,
       "vRtrIfIpReasV6FragBytesRcvd": vRtrIfIpReasV6FragBytesRcvd,
       "vRtrIfIpReasV6FragBytesRcvdL32": vRtrIfIpReasV6FragBytesRcvdL32,
       "vRtrIfIpReasV6FragBytesRcvdH32": vRtrIfIpReasV6FragBytesRcvdH32,
       "vRtrIfIpReasV6FragPktsReas": vRtrIfIpReasV6FragPktsReas,
       "vRtrIfIpReasV6FragPktsReasLow32": vRtrIfIpReasV6FragPktsReasLow32,
       "vRtrIfIpReasV6FragPktsReasHigh32": vRtrIfIpReasV6FragPktsReasHigh32,
       "vRtrIfIpReasV6FragBytesReas": vRtrIfIpReasV6FragBytesReas,
       "vRtrIfIpReasV6FragBytesReasL32": vRtrIfIpReasV6FragBytesReasL32,
       "vRtrIfIpReasV6FragBytesReasH32": vRtrIfIpReasV6FragBytesReasH32,
       "vRtrIfIpReasV6FragReasErrors": vRtrIfIpReasV6FragReasErrors,
       "vRtrIfIpReasV6FragReasErrorsL32": vRtrIfIpReasV6FragReasErrorsL32,
       "vRtrIfIpReasV6FragReasErrorsH32": vRtrIfIpReasV6FragReasErrorsH32,
       "vRtrIfIpReasV6FragDisc": vRtrIfIpReasV6FragDisc,
       "vRtrIfIpReasV6FragDiscLow32": vRtrIfIpReasV6FragDiscLow32,
       "vRtrIfIpReasV6FragDiscHigh32": vRtrIfIpReasV6FragDiscHigh32,
       "vRtrIfIpReasV6OutBufRes": vRtrIfIpReasV6OutBufRes,
       "vRtrIfIpReasV6OutBufResLow32": vRtrIfIpReasV6OutBufResLow32,
       "vRtrIfIpReasV6OutBufResHigh32": vRtrIfIpReasV6OutBufResHigh32,
       "vRtrIfIpReasV6PktsRx": vRtrIfIpReasV6PktsRx,
       "vRtrIfIpReasV6PktsRxLow32": vRtrIfIpReasV6PktsRxLow32,
       "vRtrIfIpReasV6PktsRxHigh32": vRtrIfIpReasV6PktsRxHigh32,
       "vRtrIfIpReasV6BytesRx": vRtrIfIpReasV6BytesRx,
       "vRtrIfIpReasV6BytesRxLow32": vRtrIfIpReasV6BytesRxLow32,
       "vRtrIfIpReasV6BytesRxHigh32": vRtrIfIpReasV6BytesRxHigh32,
       "vRtrIfIpReasV6PktsTx": vRtrIfIpReasV6PktsTx,
       "vRtrIfIpReasV6PktsTxLow32": vRtrIfIpReasV6PktsTxLow32,
       "vRtrIfIpReasV6PktsTxHigh32": vRtrIfIpReasV6PktsTxHigh32,
       "vRtrIfIpReasV6BytesTx": vRtrIfIpReasV6BytesTx,
       "vRtrIfIpReasV6BytesTxLow32": vRtrIfIpReasV6BytesTxLow32,
       "vRtrIfIpReasV6BytesTxHigh32": vRtrIfIpReasV6BytesTxHigh32,
       "vRtrIfSpeed": vRtrIfSpeed,
       "vRtrIfExtTable": vRtrIfExtTable,
       "vRtrIfExtEntry": vRtrIfExtEntry,
       "vRtrIfLsrIpLoadBalancing": vRtrIfLsrIpLoadBalancing,
       "vRtrIfIngressIpv4Flowspec": vRtrIfIngressIpv4Flowspec,
       "vRtrIfInfo": vRtrIfInfo,
       "vRtrIfInfoEncrypted": vRtrIfInfoEncrypted,
       "vRtrIfQosRouteLookup": vRtrIfQosRouteLookup,
       "vRtrIfIpv6QosRouteLookup": vRtrIfIpv6QosRouteLookup,
       "vRtrIfStatusString": vRtrIfStatusString,
       "vRtrIfIpv6uRPFCheckState": vRtrIfIpv6uRPFCheckState,
       "vRtrIfIpv6uRPFCheckMode": vRtrIfIpv6uRPFCheckMode,
       "vRtrIfTmsOffRampVprn": vRtrIfTmsOffRampVprn,
       "vRtrIfTmsMgmtVprn": vRtrIfTmsMgmtVprn,
       "tnVRtrMobGatewayObjs": tnVRtrMobGatewayObjs,
       "vRtrIfBfdExtTableLastChanged": vRtrIfBfdExtTableLastChanged,
       "vRtrIfBfdExtTable": vRtrIfBfdExtTable,
       "vRtrIfBfdExtEntry": vRtrIfBfdExtEntry,
       "vRtrIfBfdExtAddressType": vRtrIfBfdExtAddressType,
       "vRtrIfBfdExtAdminState": vRtrIfBfdExtAdminState,
       "vRtrIfBfdExtTransmitInterval": vRtrIfBfdExtTransmitInterval,
       "vRtrIfBfdExtReceiveInterval": vRtrIfBfdExtReceiveInterval,
       "vRtrIfBfdExtMultiplier": vRtrIfBfdExtMultiplier,
       "vRtrIfBfdExtEchoInterval": vRtrIfBfdExtEchoInterval,
       "vRtrIfBfdExtType": vRtrIfBfdExtType,
       "vRtrIfStatsExtTable": vRtrIfStatsExtTable,
       "vRtrIfStatsExtEntry": vRtrIfStatsExtEntry,
       "vRtrIfTxPkts": vRtrIfTxPkts,
       "vRtrIfTxPktsLow32": vRtrIfTxPktsLow32,
       "vRtrIfTxPktsHigh32": vRtrIfTxPktsHigh32,
       "vRtrIfTxBytes": vRtrIfTxBytes,
       "vRtrIfTxBytesLow32": vRtrIfTxBytesLow32,
       "vRtrIfTxBytesHigh32": vRtrIfTxBytesHigh32,
       "vRtrIfQosTable": vRtrIfQosTable,
       "vRtrIfQosEntry": vRtrIfQosEntry,
       "vRtrIfQosNetworkPolicyId": vRtrIfQosNetworkPolicyId,
       "vRtrIfBfdSessExtTable": vRtrIfBfdSessExtTable,
       "vRtrIfBfdSessExtEntry": vRtrIfBfdSessExtEntry,
       "vRtrIfBfdSessExtLinkType": vRtrIfBfdSessExtLinkType,
       "vRtrIfBfdSessExtRxInfoId": vRtrIfBfdSessExtRxInfoId,
       "vRtrIfBfdSessExtLclAddrType": vRtrIfBfdSessExtLclAddrType,
       "vRtrIfBfdSessExtLclAddr": vRtrIfBfdSessExtLclAddr,
       "vRtrIfBfdSessExtRemAddrType": vRtrIfBfdSessExtRemAddrType,
       "vRtrIfBfdSessExtRemAddr": vRtrIfBfdSessExtRemAddr,
       "vRtrIfBfdSessExtOperState": vRtrIfBfdSessExtOperState,
       "vRtrIfBfdSessExtState": vRtrIfBfdSessExtState,
       "vRtrIfBfdSessExtOperFlags": vRtrIfBfdSessExtOperFlags,
       "vRtrIfBfdSessExtMesgRecv": vRtrIfBfdSessExtMesgRecv,
       "vRtrIfBfdSessExtMesgSent": vRtrIfBfdSessExtMesgSent,
       "vRtrIfBfdSessExtLastDownTime": vRtrIfBfdSessExtLastDownTime,
       "vRtrIfBfdSessExtLastUpTime": vRtrIfBfdSessExtLastUpTime,
       "vRtrIfBfdSessExtUpCount": vRtrIfBfdSessExtUpCount,
       "vRtrIfBfdSessExtDownCount": vRtrIfBfdSessExtDownCount,
       "vRtrIfBfdSessExtLclDisc": vRtrIfBfdSessExtLclDisc,
       "vRtrIfBfdSessExtRemDisc": vRtrIfBfdSessExtRemDisc,
       "vRtrIfBfdSessExtProtocols": vRtrIfBfdSessExtProtocols,
       "vRtrIfBfdSessExtTxInterval": vRtrIfBfdSessExtTxInterval,
       "vRtrIfBfdSessExtRxInterval": vRtrIfBfdSessExtRxInterval,
       "vRtrIfBfdSessExtType": vRtrIfBfdSessExtType,
       "vRtrIfBfdSessExtVerMismatch": vRtrIfBfdSessExtVerMismatch,
       "vRtrIfBfdSessExtTimeSinceLastRx": vRtrIfBfdSessExtTimeSinceLastRx,
       "vRtrIfBfdSessExtTimeSinceLastTx": vRtrIfBfdSessExtTimeSinceLastTx,
       "vRtrIfBfdSessExtRemoteLspNum": vRtrIfBfdSessExtRemoteLspNum,
       "vRtrIfBfdSessExtRemoteTunnelNum": vRtrIfBfdSessExtRemoteTunnelNum,
       "vRtrIfBfdSessExtRemoteNodeId": vRtrIfBfdSessExtRemoteNodeId,
       "vRtrIfBfdSessExtRemoteGlobalId": vRtrIfBfdSessExtRemoteGlobalId,
       "vRtrIfBfdSessExtLspPathTunnelId": vRtrIfBfdSessExtLspPathTunnelId,
       "vRtrIfBfdSessExtLspPathId": vRtrIfBfdSessExtLspPathId,
       "vRtrIfBfdSessForwardInfoTable": vRtrIfBfdSessForwardInfoTable,
       "vRtrIfBfdSessForwardInfoEntry": vRtrIfBfdSessForwardInfoEntry,
       "vRtrIfBfdSessExtLclState": vRtrIfBfdSessExtLclState,
       "vRtrIfBfdSessExtLclMode": vRtrIfBfdSessExtLclMode,
       "vRtrIfBfdSessExtLclDiag": vRtrIfBfdSessExtLclDiag,
       "vRtrIfBfdSessExtLclMinTx": vRtrIfBfdSessExtLclMinTx,
       "vRtrIfBfdSessExtLclMinRx": vRtrIfBfdSessExtLclMinRx,
       "vRtrIfBfdSessExtLclMult": vRtrIfBfdSessExtLclMult,
       "vRtrIfBfdSessExtRemState": vRtrIfBfdSessExtRemState,
       "vRtrIfBfdSessExtRemMode": vRtrIfBfdSessExtRemMode,
       "vRtrIfBfdSessExtRemDiag": vRtrIfBfdSessExtRemDiag,
       "vRtrIfBfdSessExtRemMinTx": vRtrIfBfdSessExtRemMinTx,
       "vRtrIfBfdSessExtRemMinRx": vRtrIfBfdSessExtRemMinRx,
       "vRtrIfBfdSessExtRemMult": vRtrIfBfdSessExtRemMult,
       "vRtrIfBfdSessExtLastRecv": vRtrIfBfdSessExtLastRecv,
       "vRtrIfBfdSessExtLastSent": vRtrIfBfdSessExtLastSent,
       "vRtrConfScalar1": vRtrConfScalar1,
       "vRtrConfScalar2": vRtrConfScalar2}
)
