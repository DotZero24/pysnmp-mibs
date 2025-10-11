# SNMP MIB module (TIMETRA-WLAN-GW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-WLAN-GW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:03:43 2025
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
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-LSR-MIB",
    "MplsLabel")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxChassisIndex,
 TmnxChassisIndexOrZero,
 TmnxSlotNum,
 TmnxSlotNumOrZero,
 tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxChassisIndex",
    "TmnxChassisIndexOrZero",
    "TmnxSlotNum",
    "TmnxSlotNumOrZero",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(iesIfIndex,
 svcId,
 svcTlsInfoEntry) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "iesIfIndex",
    "svcId",
    "svcTlsInfoEntry")

(TmnxMobApn,
 TmnxMobApnDomainName,
 TmnxMobApnOrZero,
 TmnxMobArp,
 TmnxMobArpValue,
 TmnxMobBearerId,
 TmnxMobExtQci,
 TmnxMobImsiStr,
 TmnxMobMccOrEmpty,
 TmnxMobMncOrEmpty,
 TmnxMobPathMgmtState,
 TmnxMobProfGbrRate,
 TmnxMobProfIpTtl,
 TmnxMobProfKeepAliveResponse,
 TmnxMobProfKeepAliveRetryCount,
 TmnxMobProfKeepAliveTimeout,
 TmnxMobProfMbrRate,
 TmnxMobProfMsgReTxRetryCount,
 TmnxMobProfMsgReTxTimeout,
 TmnxMobQci,
 TmnxMobQciValue,
 TmnxMobService) = mibBuilder.importSymbols(
    "TIMETRA-TC-MG-MIB",
    "TmnxMobApn",
    "TmnxMobApnDomainName",
    "TmnxMobApnOrZero",
    "TmnxMobArp",
    "TmnxMobArpValue",
    "TmnxMobBearerId",
    "TmnxMobExtQci",
    "TmnxMobImsiStr",
    "TmnxMobMccOrEmpty",
    "TmnxMobMncOrEmpty",
    "TmnxMobPathMgmtState",
    "TmnxMobProfGbrRate",
    "TmnxMobProfIpTtl",
    "TmnxMobProfKeepAliveResponse",
    "TmnxMobProfKeepAliveRetryCount",
    "TmnxMobProfKeepAliveTimeout",
    "TmnxMobProfMbrRate",
    "TmnxMobProfMsgReTxRetryCount",
    "TmnxMobProfMsgReTxTimeout",
    "TmnxMobQci",
    "TmnxMobQciValue",
    "TmnxMobService")

(QTagFullRange,
 QTagFullRangeOrNone,
 SvcISID,
 TAdaptationRule,
 TCIRRate,
 TDirectionIngEgr,
 TIpProtocol,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPIRRate,
 TPolicyID,
 TPortSchedulerPIR,
 TQosOverrideType,
 TQosQueueCIRRateOverride,
 TQosQueuePIRRateOverride,
 TmnxActionType,
 TmnxAdminState,
 TmnxBsxIsaAaGroupIndexOrZero,
 TmnxEnabledDisabled,
 TmnxEnabledDisabledAdminState,
 TmnxEnabledDisabledOrNA,
 TmnxEncapVal,
 TmnxEsaNum,
 TmnxEsaVappNum,
 TmnxHttpRedirectUrl,
 TmnxIsaScalingProfile,
 TmnxMacSpecification,
 TmnxNatWaterMark,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrID,
 TmnxVRtrIDOrZero,
 TmnxWlanGwIsaGrpId,
 TmnxWlanGwIsaGrpIdOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "QTagFullRange",
    "QTagFullRangeOrNone",
    "SvcISID",
    "TAdaptationRule",
    "TCIRRate",
    "TDirectionIngEgr",
    "TIpProtocol",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPIRRate",
    "TPolicyID",
    "TPortSchedulerPIR",
    "TQosOverrideType",
    "TQosQueueCIRRateOverride",
    "TQosQueuePIRRateOverride",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxBsxIsaAaGroupIndexOrZero",
    "TmnxEnabledDisabled",
    "TmnxEnabledDisabledAdminState",
    "TmnxEnabledDisabledOrNA",
    "TmnxEncapVal",
    "TmnxEsaNum",
    "TmnxEsaVappNum",
    "TmnxHttpRedirectUrl",
    "TmnxIsaScalingProfile",
    "TmnxMacSpecification",
    "TmnxNatWaterMark",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero",
    "TmnxWlanGwIsaGrpId",
    "TmnxWlanGwIsaGrpIdOrZero")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraWlanGwMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 81)
)
if mibBuilder.loadTexts:
    timetraWlanGwMIBModule.setRevisions(
        ("2019-04-01 00:00",
         "2017-01-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2012-02-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxWlanGwAmbr(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 10000000),
    )



class TmnxWlanGwBurstSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131071),
    )



class TmnxWlanGwIsaIomOperState(TextualConvention, Integer32):
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
        *(("unavail", 0),
          ("primary", 1),
          ("backup", 2),
          ("busy", 3))
    )



class TmnxWlanGwMgwInterfaceType(TextualConvention, Integer32):
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
        *(("gn", 1),
          ("s2a", 2),
          ("s2b", 3),
          ("s11", 4))
    )



class TmnxWlanGwDsmFilterDefaultAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2))
    )



class TmnxWlanGwDsmFilterAction(TextualConvention, Integer32):
    status = "current"
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
          ("drop", 1),
          ("forward", 2),
          ("httpRedirect", 3),
          ("reserved4", 4))
    )



class TmnxWlanGwQoSOperState(TextualConvention, Integer32):
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
        *(("adminDown", 0),
          ("active", 1),
          ("pending", 2),
          ("problem", 3))
    )



class TmnxWlanGwGtpSeIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class TmnxWlanGwSsidType(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("open", 1),
          ("closed", 2))
    )



class TmnxWlanGwUeAddressFamily(TextualConvention, Integer32):
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
        *(("notSpecified", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4-only", 3),
          ("ipv6-only", 4),
          ("ipv4v6", 5))
    )



class TmnxWlanGwUeEncapsulation(TextualConvention, Integer32):
    status = "current"
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
        *(("notSpecified", 0),
          ("gre", 1),
          ("l2tp", 2),
          ("l2", 3),
          ("vxlan", 4))
    )



class TmnxWlanGwUeIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class TmnxWlanGwChargingCharBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bit0", 0),
          ("bit1", 1),
          ("bit2", 2),
          ("bit3", 3),
          ("bit4", 4),
          ("bit5", 5),
          ("bit6", 6),
          ("bit7", 7),
          ("bit8", 8),
          ("bit9", 9),
          ("bit10", 10),
          ("bit11", 11),
          ("bit12", 12),
          ("bit13", 13),
          ("bit14", 14),
          ("bit15", 15))
    )


class TmnxWlanGwSubIfIpsAddrFamily(TextualConvention, Integer32):
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
        *(("dhcpv6", 0),
          ("slaac", 1),
          ("dhcpv4", 2))
    )



class TmnxWlanGwVlanIdleTimeoutAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remove", 0),
          ("shcv", 1))
    )



class TmnxWlanGwWatermarkEntity(TextualConvention, Integer32):
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
        *(("userEquipment", 1),
          ("bridgeDomain", 2),
          ("radiusProxyClient", 3))
    )



class TmnxGtpInterfaceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uplink", 0),
          ("s11", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxWlanGwConformance_ObjectIdentity = ObjectIdentity
tmnxWlanGwConformance = _TmnxWlanGwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81)
)
_TmnxWlanGwCompliances_ObjectIdentity = ObjectIdentity
tmnxWlanGwCompliances = _TmnxWlanGwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1)
)
_TmnxWlanGwGroups_ObjectIdentity = ObjectIdentity
tmnxWlanGwGroups = _TmnxWlanGwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2)
)
_TmnxGtpCompliances_ObjectIdentity = ObjectIdentity
tmnxGtpCompliances = _TmnxGtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 3)
)
_TmnxGtpGroups_ObjectIdentity = ObjectIdentity
tmnxGtpGroups = _TmnxGtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 4)
)
_TmnxWlanGw_ObjectIdentity = ObjectIdentity
tmnxWlanGw = _TmnxWlanGw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81)
)
_TmnxWlanGwObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwObjs = _TmnxWlanGwObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1)
)
_TmnxWlanGwIsaObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwIsaObjs = _TmnxWlanGwIsaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1)
)
_TmnxWlanGwGrpTable_Object = MibTable
tmnxWlanGwGrpTable = _TmnxWlanGwGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwGrpTable.setStatus("current")
_TmnxWlanGwGrpEntry_Object = MibTableRow
tmnxWlanGwGrpEntry = _TmnxWlanGwGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1)
)
tmnxWlanGwGrpEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwGrpEntry.setStatus("current")
_TmnxWlanGwGrpId_Type = TmnxWlanGwIsaGrpId
_TmnxWlanGwGrpId_Object = MibTableColumn
tmnxWlanGwGrpId = _TmnxWlanGwGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 1),
    _TmnxWlanGwGrpId_Type()
)
tmnxWlanGwGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpId.setStatus("current")
_TmnxWlanGwGrpRowStatus_Type = RowStatus
_TmnxWlanGwGrpRowStatus_Object = MibTableColumn
tmnxWlanGwGrpRowStatus = _TmnxWlanGwGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 2),
    _TmnxWlanGwGrpRowStatus_Type()
)
tmnxWlanGwGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpRowStatus.setStatus("current")
_TmnxWlanGwGrpLastMgmtChange_Type = TimeStamp
_TmnxWlanGwGrpLastMgmtChange_Object = MibTableColumn
tmnxWlanGwGrpLastMgmtChange = _TmnxWlanGwGrpLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 3),
    _TmnxWlanGwGrpLastMgmtChange_Type()
)
tmnxWlanGwGrpLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpLastMgmtChange.setStatus("current")


class _TmnxWlanGwGrpDescription_Type(TItemDescription):
    """Custom type tmnxWlanGwGrpDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWlanGwGrpDescription_Type.__name__ = "TItemDescription"
_TmnxWlanGwGrpDescription_Object = MibTableColumn
tmnxWlanGwGrpDescription = _TmnxWlanGwGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 4),
    _TmnxWlanGwGrpDescription_Type()
)
tmnxWlanGwGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpDescription.setStatus("current")


class _TmnxWlanGwGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxWlanGwGrpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxWlanGwGrpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxWlanGwGrpAdminState_Object = MibTableColumn
tmnxWlanGwGrpAdminState = _TmnxWlanGwGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 5),
    _TmnxWlanGwGrpAdminState_Type()
)
tmnxWlanGwGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpAdminState.setStatus("current")


class _TmnxWlanGwGrpActiveIomLimit_Type(Unsigned32):
    """Custom type tmnxWlanGwGrpActiveIomLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(8, 14),
    )


_TmnxWlanGwGrpActiveIomLimit_Type.__name__ = "Unsigned32"
_TmnxWlanGwGrpActiveIomLimit_Object = MibTableColumn
tmnxWlanGwGrpActiveIomLimit = _TmnxWlanGwGrpActiveIomLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 6),
    _TmnxWlanGwGrpActiveIomLimit_Type()
)
tmnxWlanGwGrpActiveIomLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpActiveIomLimit.setStatus("current")


class _TmnxWlanGwGrpPortPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwGrpPortPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwGrpPortPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwGrpPortPlcy_Object = MibTableColumn
tmnxWlanGwGrpPortPlcy = _TmnxWlanGwGrpPortPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 7),
    _TmnxWlanGwGrpPortPlcy_Type()
)
tmnxWlanGwGrpPortPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpPortPlcy.setStatus("current")


class _TmnxWlanGwGrpTunnelPortPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwGrpTunnelPortPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwGrpTunnelPortPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwGrpTunnelPortPlcy_Object = MibTableColumn
tmnxWlanGwGrpTunnelPortPlcy = _TmnxWlanGwGrpTunnelPortPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 8),
    _TmnxWlanGwGrpTunnelPortPlcy_Type()
)
tmnxWlanGwGrpTunnelPortPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpTunnelPortPlcy.setStatus("current")


class _TmnxWlanGwGrpIsaAaGroup_Type(TmnxBsxIsaAaGroupIndexOrZero):
    """Custom type tmnxWlanGwGrpIsaAaGroup based on TmnxBsxIsaAaGroupIndexOrZero"""
    defaultValue = 0


_TmnxWlanGwGrpIsaAaGroup_Type.__name__ = "TmnxBsxIsaAaGroupIndexOrZero"
_TmnxWlanGwGrpIsaAaGroup_Object = MibTableColumn
tmnxWlanGwGrpIsaAaGroup = _TmnxWlanGwGrpIsaAaGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 9),
    _TmnxWlanGwGrpIsaAaGroup_Type()
)
tmnxWlanGwGrpIsaAaGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpIsaAaGroup.setStatus("current")
_TmnxWlanGwGrpOperState_Type = TmnxOperState
_TmnxWlanGwGrpOperState_Object = MibTableColumn
tmnxWlanGwGrpOperState = _TmnxWlanGwGrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 50),
    _TmnxWlanGwGrpOperState_Type()
)
tmnxWlanGwGrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpOperState.setStatus("current")
_TmnxWlanGwGrpDegraded_Type = TruthValue
_TmnxWlanGwGrpDegraded_Object = MibTableColumn
tmnxWlanGwGrpDegraded = _TmnxWlanGwGrpDegraded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 51),
    _TmnxWlanGwGrpDegraded_Type()
)
tmnxWlanGwGrpDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpDegraded.setStatus("current")


class _TmnxWlanGwGrpRedundancyUnit_Type(Integer32):
    """Custom type tmnxWlanGwGrpRedundancyUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iom", 1),
          ("mda", 2))
    )


_TmnxWlanGwGrpRedundancyUnit_Type.__name__ = "Integer32"
_TmnxWlanGwGrpRedundancyUnit_Object = MibTableColumn
tmnxWlanGwGrpRedundancyUnit = _TmnxWlanGwGrpRedundancyUnit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 54),
    _TmnxWlanGwGrpRedundancyUnit_Type()
)
tmnxWlanGwGrpRedundancyUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpRedundancyUnit.setStatus("current")


class _TmnxWlanGwGrpActiveMdaLimit_Type(Unsigned32):
    """Custom type tmnxWlanGwGrpActiveMdaLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_TmnxWlanGwGrpActiveMdaLimit_Type.__name__ = "Unsigned32"
_TmnxWlanGwGrpActiveMdaLimit_Object = MibTableColumn
tmnxWlanGwGrpActiveMdaLimit = _TmnxWlanGwGrpActiveMdaLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 55),
    _TmnxWlanGwGrpActiveMdaLimit_Type()
)
tmnxWlanGwGrpActiveMdaLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpActiveMdaLimit.setStatus("current")


class _TmnxWlanGwGrpScalingProfile_Type(TmnxIsaScalingProfile):
    """Custom type tmnxWlanGwGrpScalingProfile based on TmnxIsaScalingProfile"""
    defaultValue = 1


_TmnxWlanGwGrpScalingProfile_Type.__name__ = "TmnxIsaScalingProfile"
_TmnxWlanGwGrpScalingProfile_Object = MibTableColumn
tmnxWlanGwGrpScalingProfile = _TmnxWlanGwGrpScalingProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 56),
    _TmnxWlanGwGrpScalingProfile_Type()
)
tmnxWlanGwGrpScalingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpScalingProfile.setStatus("current")


class _TmnxWlanGwGrpIsaAaOversub_Type(Unsigned32):
    """Custom type tmnxWlanGwGrpIsaAaOversub based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxWlanGwGrpIsaAaOversub_Type.__name__ = "Unsigned32"
_TmnxWlanGwGrpIsaAaOversub_Object = MibTableColumn
tmnxWlanGwGrpIsaAaOversub = _TmnxWlanGwGrpIsaAaOversub_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 57),
    _TmnxWlanGwGrpIsaAaOversub_Type()
)
tmnxWlanGwGrpIsaAaOversub.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpIsaAaOversub.setStatus("current")
_TmnxWlanGwIomTable_Object = MibTable
tmnxWlanGwIomTable = _TmnxWlanGwIomTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxWlanGwIomTable.setStatus("current")
_TmnxWlanGwIomEntry_Object = MibTableRow
tmnxWlanGwIomEntry = _TmnxWlanGwIomEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 2, 1)
)
tmnxWlanGwIomEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwIomEntry.setStatus("current")
_TmnxWlanGwIomRowStatus_Type = RowStatus
_TmnxWlanGwIomRowStatus_Object = MibTableColumn
tmnxWlanGwIomRowStatus = _TmnxWlanGwIomRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 2, 1, 1),
    _TmnxWlanGwIomRowStatus_Type()
)
tmnxWlanGwIomRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwIomRowStatus.setStatus("current")
_TmnxWlanGwIomLastMgmtChange_Type = TimeStamp
_TmnxWlanGwIomLastMgmtChange_Object = MibTableColumn
tmnxWlanGwIomLastMgmtChange = _TmnxWlanGwIomLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 2, 1, 2),
    _TmnxWlanGwIomLastMgmtChange_Type()
)
tmnxWlanGwIomLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIomLastMgmtChange.setStatus("current")
_TmnxWlanGwIomOperState_Type = TmnxWlanGwIsaIomOperState
_TmnxWlanGwIomOperState_Object = MibTableColumn
tmnxWlanGwIomOperState = _TmnxWlanGwIomOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 2, 1, 3),
    _TmnxWlanGwIomOperState_Type()
)
tmnxWlanGwIomOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIomOperState.setStatus("current")


class _TmnxWlanGwIomApplication_Type(Bits):
    """Custom type tmnxWlanGwIomApplication based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("loadBalancing", 0),
          ("ueAnchoring", 1))
    )

_TmnxWlanGwIomApplication_Type.__name__ = "Bits"
_TmnxWlanGwIomApplication_Object = MibTableColumn
tmnxWlanGwIomApplication = _TmnxWlanGwIomApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 2, 1, 4),
    _TmnxWlanGwIomApplication_Type()
)
tmnxWlanGwIomApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwIomApplication.setStatus("current")
_TmnxWlanGwIsaMemberTable_Object = MibTable
tmnxWlanGwIsaMemberTable = _TmnxWlanGwIsaMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberTable.setStatus("current")
_TmnxWlanGwIsaMemberEntry_Object = MibTableRow
tmnxWlanGwIsaMemberEntry = _TmnxWlanGwIsaMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1)
)
tmnxWlanGwIsaMemberEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberEntry.setStatus("current")
_TmnxWlanGwIsaMemberId_Type = Unsigned32
_TmnxWlanGwIsaMemberId_Object = MibTableColumn
tmnxWlanGwIsaMemberId = _TmnxWlanGwIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 1),
    _TmnxWlanGwIsaMemberId_Type()
)
tmnxWlanGwIsaMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberId.setStatus("current")
_TmnxWlanGwIsaMemberChassisIndex_Type = TmnxChassisIndexOrZero
_TmnxWlanGwIsaMemberChassisIndex_Object = MibTableColumn
tmnxWlanGwIsaMemberChassisIndex = _TmnxWlanGwIsaMemberChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 2),
    _TmnxWlanGwIsaMemberChassisIndex_Type()
)
tmnxWlanGwIsaMemberChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberChassisIndex.setStatus("current")
_TmnxWlanGwIsaMemberCardSlotNum_Type = TmnxSlotNumOrZero
_TmnxWlanGwIsaMemberCardSlotNum_Object = MibTableColumn
tmnxWlanGwIsaMemberCardSlotNum = _TmnxWlanGwIsaMemberCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 3),
    _TmnxWlanGwIsaMemberCardSlotNum_Type()
)
tmnxWlanGwIsaMemberCardSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberCardSlotNum.setStatus("current")
_TmnxWlanGwIsaMemberSlotNum_Type = Unsigned32
_TmnxWlanGwIsaMemberSlotNum_Object = MibTableColumn
tmnxWlanGwIsaMemberSlotNum = _TmnxWlanGwIsaMemberSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 4),
    _TmnxWlanGwIsaMemberSlotNum_Type()
)
tmnxWlanGwIsaMemberSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberSlotNum.setStatus("current")
_TmnxWlanGwIsaMemberNumSoftGreTu_Type = Gauge32
_TmnxWlanGwIsaMemberNumSoftGreTu_Object = MibTableColumn
tmnxWlanGwIsaMemberNumSoftGreTu = _TmnxWlanGwIsaMemberNumSoftGreTu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 5),
    _TmnxWlanGwIsaMemberNumSoftGreTu_Type()
)
tmnxWlanGwIsaMemberNumSoftGreTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberNumSoftGreTu.setStatus("current")
_TmnxWlanGwIsaMemberNumUe_Type = Gauge32
_TmnxWlanGwIsaMemberNumUe_Object = MibTableColumn
tmnxWlanGwIsaMemberNumUe = _TmnxWlanGwIsaMemberNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 6),
    _TmnxWlanGwIsaMemberNumUe_Type()
)
tmnxWlanGwIsaMemberNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberNumUe.setStatus("current")
_TmnxWlanGwIsaMemberEegMemberAct_Type = Gauge32
_TmnxWlanGwIsaMemberEegMemberAct_Object = MibTableColumn
tmnxWlanGwIsaMemberEegMemberAct = _TmnxWlanGwIsaMemberEegMemberAct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 7),
    _TmnxWlanGwIsaMemberEegMemberAct_Type()
)
tmnxWlanGwIsaMemberEegMemberAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberEegMemberAct.setStatus("current")
_TmnxWlanGwIsaMemberEegMemberPend_Type = Gauge32
_TmnxWlanGwIsaMemberEegMemberPend_Object = MibTableColumn
tmnxWlanGwIsaMemberEegMemberPend = _TmnxWlanGwIsaMemberEegMemberPend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 8),
    _TmnxWlanGwIsaMemberEegMemberPend_Type()
)
tmnxWlanGwIsaMemberEegMemberPend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberEegMemberPend.setStatus("current")
_TmnxWlanGwIsaMemberTuQosProblem_Type = Gauge32
_TmnxWlanGwIsaMemberTuQosProblem_Object = MibTableColumn
tmnxWlanGwIsaMemberTuQosProblem = _TmnxWlanGwIsaMemberTuQosProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 9),
    _TmnxWlanGwIsaMemberTuQosProblem_Type()
)
tmnxWlanGwIsaMemberTuQosProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberTuQosProblem.setStatus("current")
_TmnxWlanGwIsaMemberEsaNum_Type = TmnxEsaNum
_TmnxWlanGwIsaMemberEsaNum_Object = MibTableColumn
tmnxWlanGwIsaMemberEsaNum = _TmnxWlanGwIsaMemberEsaNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 10),
    _TmnxWlanGwIsaMemberEsaNum_Type()
)
tmnxWlanGwIsaMemberEsaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberEsaNum.setStatus("current")
_TmnxWlanGwIsaMemberEsaVappNum_Type = TmnxEsaVappNum
_TmnxWlanGwIsaMemberEsaVappNum_Object = MibTableColumn
tmnxWlanGwIsaMemberEsaVappNum = _TmnxWlanGwIsaMemberEsaVappNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 11),
    _TmnxWlanGwIsaMemberEsaVappNum_Type()
)
tmnxWlanGwIsaMemberEsaVappNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberEsaVappNum.setStatus("current")
_TmnxWlanGwIsaMemberStatsTable_Object = MibTable
tmnxWlanGwIsaMemberStatsTable = _TmnxWlanGwIsaMemberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsTable.setStatus("obsolete")
_TmnxWlanGwIsaMemberStatsEntry_Object = MibTableRow
tmnxWlanGwIsaMemberStatsEntry = _TmnxWlanGwIsaMemberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4, 1)
)
tmnxWlanGwIsaMemberStatsEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsType"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsEntry.setStatus("obsolete")


class _TmnxWlanGwIsaMemberStatsType_Type(Unsigned32):
    """Custom type tmnxWlanGwIsaMemberStatsType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_TmnxWlanGwIsaMemberStatsType_Type.__name__ = "Unsigned32"
_TmnxWlanGwIsaMemberStatsType_Object = MibTableColumn
tmnxWlanGwIsaMemberStatsType = _TmnxWlanGwIsaMemberStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4, 1, 1),
    _TmnxWlanGwIsaMemberStatsType_Type()
)
tmnxWlanGwIsaMemberStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsType.setStatus("current")


class _TmnxWlanGwIsaMemberStatsName_Type(DisplayString):
    """Custom type tmnxWlanGwIsaMemberStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxWlanGwIsaMemberStatsName_Type.__name__ = "DisplayString"
_TmnxWlanGwIsaMemberStatsName_Object = MibTableColumn
tmnxWlanGwIsaMemberStatsName = _TmnxWlanGwIsaMemberStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4, 1, 2),
    _TmnxWlanGwIsaMemberStatsName_Type()
)
tmnxWlanGwIsaMemberStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsName.setStatus("obsolete")
_TmnxWlanGwIsaMemberStatsVal_Type = Counter32
_TmnxWlanGwIsaMemberStatsVal_Object = MibTableColumn
tmnxWlanGwIsaMemberStatsVal = _TmnxWlanGwIsaMemberStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4, 1, 3),
    _TmnxWlanGwIsaMemberStatsVal_Type()
)
tmnxWlanGwIsaMemberStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsVal.setStatus("obsolete")
_TmnxWlanGwIsaMemberStatsValHw_Type = Counter32
_TmnxWlanGwIsaMemberStatsValHw_Object = MibTableColumn
tmnxWlanGwIsaMemberStatsValHw = _TmnxWlanGwIsaMemberStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4, 1, 4),
    _TmnxWlanGwIsaMemberStatsValHw_Type()
)
tmnxWlanGwIsaMemberStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsValHw.setStatus("obsolete")
_TmnxWlanGwIsaMemberStatsValue_Type = Counter64
_TmnxWlanGwIsaMemberStatsValue_Object = MibTableColumn
tmnxWlanGwIsaMemberStatsValue = _TmnxWlanGwIsaMemberStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4, 1, 5),
    _TmnxWlanGwIsaMemberStatsValue_Type()
)
tmnxWlanGwIsaMemberStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsValue.setStatus("obsolete")
_TmnxWlanGwMdaTable_Object = MibTable
tmnxWlanGwMdaTable = _TmnxWlanGwMdaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMdaTable.setStatus("current")
_TmnxWlanGwMdaEntry_Object = MibTableRow
tmnxWlanGwMdaEntry = _TmnxWlanGwMdaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 7, 1)
)
tmnxWlanGwMdaEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMdaEntry.setStatus("current")
_TmnxWlanGwMdaRowStatus_Type = RowStatus
_TmnxWlanGwMdaRowStatus_Object = MibTableColumn
tmnxWlanGwMdaRowStatus = _TmnxWlanGwMdaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 7, 1, 1),
    _TmnxWlanGwMdaRowStatus_Type()
)
tmnxWlanGwMdaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMdaRowStatus.setStatus("current")
_TmnxWlanGwMdaLastMgmtChange_Type = TimeStamp
_TmnxWlanGwMdaLastMgmtChange_Object = MibTableColumn
tmnxWlanGwMdaLastMgmtChange = _TmnxWlanGwMdaLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 7, 1, 2),
    _TmnxWlanGwMdaLastMgmtChange_Type()
)
tmnxWlanGwMdaLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMdaLastMgmtChange.setStatus("current")
_TmnxWlanGwIsaStatsTable_Object = MibTable
tmnxWlanGwIsaStatsTable = _TmnxWlanGwIsaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaStatsTable.setStatus("current")
_TmnxWlanGwIsaStatsEntry_Object = MibTableRow
tmnxWlanGwIsaStatsEntry = _TmnxWlanGwIsaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 8, 1)
)
tmnxWlanGwIsaStatsEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaStatsType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaStatsId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaStatsEntry.setStatus("current")


class _TmnxWlanGwIsaStatsType_Type(Integer32):
    """Custom type tmnxWlanGwIsaStatsType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("packetErrors", 0),
          ("hostErrors", 1),
          ("bdErrors", 2),
          ("forwarding", 3),
          ("reassembly", 4),
          ("aa", 5),
          ("radius", 6),
          ("arp", 7),
          ("dhcp", 8),
          ("dhcp6", 9),
          ("icmp", 10),
          ("icmp6", 11))
    )


_TmnxWlanGwIsaStatsType_Type.__name__ = "Integer32"
_TmnxWlanGwIsaStatsType_Object = MibTableColumn
tmnxWlanGwIsaStatsType = _TmnxWlanGwIsaStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 8, 1, 1),
    _TmnxWlanGwIsaStatsType_Type()
)
tmnxWlanGwIsaStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaStatsType.setStatus("current")


class _TmnxWlanGwIsaStatsId_Type(Unsigned32):
    """Custom type tmnxWlanGwIsaStatsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_TmnxWlanGwIsaStatsId_Type.__name__ = "Unsigned32"
_TmnxWlanGwIsaStatsId_Object = MibTableColumn
tmnxWlanGwIsaStatsId = _TmnxWlanGwIsaStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 8, 1, 2),
    _TmnxWlanGwIsaStatsId_Type()
)
tmnxWlanGwIsaStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaStatsId.setStatus("current")


class _TmnxWlanGwIsaStatsName_Type(DisplayString):
    """Custom type tmnxWlanGwIsaStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxWlanGwIsaStatsName_Type.__name__ = "DisplayString"
_TmnxWlanGwIsaStatsName_Object = MibTableColumn
tmnxWlanGwIsaStatsName = _TmnxWlanGwIsaStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 8, 1, 3),
    _TmnxWlanGwIsaStatsName_Type()
)
tmnxWlanGwIsaStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaStatsName.setStatus("current")
_TmnxWlanGwIsaStatsValue_Type = Counter64
_TmnxWlanGwIsaStatsValue_Object = MibTableColumn
tmnxWlanGwIsaStatsValue = _TmnxWlanGwIsaStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 8, 1, 4),
    _TmnxWlanGwIsaStatsValue_Type()
)
tmnxWlanGwIsaStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaStatsValue.setStatus("current")
_TmnxWlanGwGrpWmTable_Object = MibTable
tmnxWlanGwGrpWmTable = _TmnxWlanGwGrpWmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxWlanGwGrpWmTable.setStatus("current")
_TmnxWlanGwGrpWmEntry_Object = MibTableRow
tmnxWlanGwGrpWmEntry = _TmnxWlanGwGrpWmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 9, 1)
)
tmnxWlanGwGrpWmEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpWmEntity"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwGrpWmEntry.setStatus("current")
_TmnxWlanGwGrpWmEntity_Type = TmnxWlanGwWatermarkEntity
_TmnxWlanGwGrpWmEntity_Object = MibTableColumn
tmnxWlanGwGrpWmEntity = _TmnxWlanGwGrpWmEntity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 9, 1, 1),
    _TmnxWlanGwGrpWmEntity_Type()
)
tmnxWlanGwGrpWmEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpWmEntity.setStatus("current")
_TmnxWlanGwGrpWmRowStatus_Type = RowStatus
_TmnxWlanGwGrpWmRowStatus_Object = MibTableColumn
tmnxWlanGwGrpWmRowStatus = _TmnxWlanGwGrpWmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 9, 1, 2),
    _TmnxWlanGwGrpWmRowStatus_Type()
)
tmnxWlanGwGrpWmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpWmRowStatus.setStatus("current")
_TmnxWlanGwGrpWmLastMgmtChange_Type = TimeStamp
_TmnxWlanGwGrpWmLastMgmtChange_Object = MibTableColumn
tmnxWlanGwGrpWmLastMgmtChange = _TmnxWlanGwGrpWmLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 9, 1, 3),
    _TmnxWlanGwGrpWmLastMgmtChange_Type()
)
tmnxWlanGwGrpWmLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpWmLastMgmtChange.setStatus("current")


class _TmnxWlanGwGrpWmHi_Type(TmnxNatWaterMark):
    """Custom type tmnxWlanGwGrpWmHi based on TmnxNatWaterMark"""
    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxWlanGwGrpWmHi_Type.__name__ = "TmnxNatWaterMark"
_TmnxWlanGwGrpWmHi_Object = MibTableColumn
tmnxWlanGwGrpWmHi = _TmnxWlanGwGrpWmHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 9, 1, 4),
    _TmnxWlanGwGrpWmHi_Type()
)
tmnxWlanGwGrpWmHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpWmHi.setStatus("current")


class _TmnxWlanGwGrpWmLo_Type(TmnxNatWaterMark):
    """Custom type tmnxWlanGwGrpWmLo based on TmnxNatWaterMark"""
    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxWlanGwGrpWmLo_Type.__name__ = "TmnxNatWaterMark"
_TmnxWlanGwGrpWmLo_Object = MibTableColumn
tmnxWlanGwGrpWmLo = _TmnxWlanGwGrpWmLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 9, 1, 5),
    _TmnxWlanGwGrpWmLo_Type()
)
tmnxWlanGwGrpWmLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpWmLo.setStatus("current")
_TmnxWlanGwIsaResrcStatsTable_Object = MibTable
tmnxWlanGwIsaResrcStatsTable = _TmnxWlanGwIsaResrcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaResrcStatsTable.setStatus("current")
_TmnxWlanGwIsaResrcStatsEntry_Object = MibTableRow
tmnxWlanGwIsaResrcStatsEntry = _TmnxWlanGwIsaResrcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 10, 1)
)
tmnxWlanGwIsaResrcStatsEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaResrcStatsId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaResrcStatsEntry.setStatus("current")


class _TmnxWlanGwIsaResrcStatsId_Type(Unsigned32):
    """Custom type tmnxWlanGwIsaResrcStatsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_TmnxWlanGwIsaResrcStatsId_Type.__name__ = "Unsigned32"
_TmnxWlanGwIsaResrcStatsId_Object = MibTableColumn
tmnxWlanGwIsaResrcStatsId = _TmnxWlanGwIsaResrcStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 10, 1, 1),
    _TmnxWlanGwIsaResrcStatsId_Type()
)
tmnxWlanGwIsaResrcStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaResrcStatsId.setStatus("current")


class _TmnxWlanGwIsaResrcStatsName_Type(DisplayString):
    """Custom type tmnxWlanGwIsaResrcStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxWlanGwIsaResrcStatsName_Type.__name__ = "DisplayString"
_TmnxWlanGwIsaResrcStatsName_Object = MibTableColumn
tmnxWlanGwIsaResrcStatsName = _TmnxWlanGwIsaResrcStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 10, 1, 2),
    _TmnxWlanGwIsaResrcStatsName_Type()
)
tmnxWlanGwIsaResrcStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaResrcStatsName.setStatus("current")
_TmnxWlanGwIsaResrcStatsMaxValue_Type = Counter64
_TmnxWlanGwIsaResrcStatsMaxValue_Object = MibTableColumn
tmnxWlanGwIsaResrcStatsMaxValue = _TmnxWlanGwIsaResrcStatsMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 10, 1, 3),
    _TmnxWlanGwIsaResrcStatsMaxValue_Type()
)
tmnxWlanGwIsaResrcStatsMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaResrcStatsMaxValue.setStatus("current")
_TmnxWlanGwIsaResrcStatsValue_Type = Counter64
_TmnxWlanGwIsaResrcStatsValue_Object = MibTableColumn
tmnxWlanGwIsaResrcStatsValue = _TmnxWlanGwIsaResrcStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 10, 1, 4),
    _TmnxWlanGwIsaResrcStatsValue_Type()
)
tmnxWlanGwIsaResrcStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaResrcStatsValue.setStatus("current")
_TmnxWlanGwIsaResrcStatsPeakValue_Type = Counter64
_TmnxWlanGwIsaResrcStatsPeakValue_Object = MibTableColumn
tmnxWlanGwIsaResrcStatsPeakValue = _TmnxWlanGwIsaResrcStatsPeakValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 10, 1, 5),
    _TmnxWlanGwIsaResrcStatsPeakValue_Type()
)
tmnxWlanGwIsaResrcStatsPeakValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaResrcStatsPeakValue.setStatus("current")


class _TmnxWlanGwIsaResrcStatsPeakTime_Type(DateAndTime):
    """Custom type tmnxWlanGwIsaResrcStatsPeakTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwIsaResrcStatsPeakTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwIsaResrcStatsPeakTime_Object = MibTableColumn
tmnxWlanGwIsaResrcStatsPeakTime = _TmnxWlanGwIsaResrcStatsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 10, 1, 6),
    _TmnxWlanGwIsaResrcStatsPeakTime_Type()
)
tmnxWlanGwIsaResrcStatsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaResrcStatsPeakTime.setStatus("current")
_TmnxWlanGwEsaObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwEsaObjs = _TmnxWlanGwEsaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 11)
)
_TmnxWlanGwVappTable_Object = MibTable
tmnxWlanGwVappTable = _TmnxWlanGwVappTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVappTable.setStatus("current")
_TmnxWlanGwVappEntry_Object = MibTableRow
tmnxWlanGwVappEntry = _TmnxWlanGwVappEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 11, 1, 1)
)
tmnxWlanGwVappEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwEsaNum"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwEsaVappNum"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwVappEntry.setStatus("current")


class _TmnxWlanGwEsaNum_Type(TmnxEsaNum):
    """Custom type tmnxWlanGwEsaNum based on TmnxEsaNum"""
    subtypeSpec = TmnxEsaNum.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxWlanGwEsaNum_Type.__name__ = "TmnxEsaNum"
_TmnxWlanGwEsaNum_Object = MibTableColumn
tmnxWlanGwEsaNum = _TmnxWlanGwEsaNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 11, 1, 1, 1),
    _TmnxWlanGwEsaNum_Type()
)
tmnxWlanGwEsaNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwEsaNum.setStatus("current")


class _TmnxWlanGwEsaVappNum_Type(TmnxEsaVappNum):
    """Custom type tmnxWlanGwEsaVappNum based on TmnxEsaVappNum"""
    subtypeSpec = TmnxEsaVappNum.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxWlanGwEsaVappNum_Type.__name__ = "TmnxEsaVappNum"
_TmnxWlanGwEsaVappNum_Object = MibTableColumn
tmnxWlanGwEsaVappNum = _TmnxWlanGwEsaVappNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 11, 1, 1, 2),
    _TmnxWlanGwEsaVappNum_Type()
)
tmnxWlanGwEsaVappNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwEsaVappNum.setStatus("current")
_TmnxWlanGwVappRowStatus_Type = RowStatus
_TmnxWlanGwVappRowStatus_Object = MibTableColumn
tmnxWlanGwVappRowStatus = _TmnxWlanGwVappRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 11, 1, 1, 3),
    _TmnxWlanGwVappRowStatus_Type()
)
tmnxWlanGwVappRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVappRowStatus.setStatus("current")
_TmnxWlanGwVappLastMgmtChange_Type = TimeStamp
_TmnxWlanGwVappLastMgmtChange_Object = MibTableColumn
tmnxWlanGwVappLastMgmtChange = _TmnxWlanGwVappLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 11, 1, 1, 4),
    _TmnxWlanGwVappLastMgmtChange_Type()
)
tmnxWlanGwVappLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVappLastMgmtChange.setStatus("current")
_TmnxWlanGwSoftGreObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwSoftGreObjs = _TmnxWlanGwSoftGreObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2)
)
_TmnxWlanGwSoftGreIfTable_Object = MibTable
tmnxWlanGwSoftGreIfTable = _TmnxWlanGwSoftGreIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfTable.setStatus("current")
_TmnxWlanGwSoftGreIfEntry_Object = MibTableRow
tmnxWlanGwSoftGreIfEntry = _TmnxWlanGwSoftGreIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1)
)
tmnxWlanGwSoftGreIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfEntry.setStatus("current")
_TmnxWlanGwSoftGreIfLastCh_Type = TimeStamp
_TmnxWlanGwSoftGreIfLastCh_Object = MibTableColumn
tmnxWlanGwSoftGreIfLastCh = _TmnxWlanGwSoftGreIfLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 1),
    _TmnxWlanGwSoftGreIfLastCh_Type()
)
tmnxWlanGwSoftGreIfLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfLastCh.setStatus("current")


class _TmnxWlanGwSoftGreIfAdminState_Type(TmnxAdminState):
    """Custom type tmnxWlanGwSoftGreIfAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxWlanGwSoftGreIfAdminState_Type.__name__ = "TmnxAdminState"
_TmnxWlanGwSoftGreIfAdminState_Object = MibTableColumn
tmnxWlanGwSoftGreIfAdminState = _TmnxWlanGwSoftGreIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 2),
    _TmnxWlanGwSoftGreIfAdminState_Type()
)
tmnxWlanGwSoftGreIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfAdminState.setStatus("current")


class _TmnxWlanGwSoftGreIfRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxWlanGwSoftGreIfRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxWlanGwSoftGreIfRouter_Object = MibTableColumn
tmnxWlanGwSoftGreIfRouter = _TmnxWlanGwSoftGreIfRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 3),
    _TmnxWlanGwSoftGreIfRouter_Type()
)
tmnxWlanGwSoftGreIfRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfRouter.setStatus("current")


class _TmnxWlanGwSoftGreIfGwAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreIfGwAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfGwAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreIfGwAddrType_Object = MibTableColumn
tmnxWlanGwSoftGreIfGwAddrType = _TmnxWlanGwSoftGreIfGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 4),
    _TmnxWlanGwSoftGreIfGwAddrType_Type()
)
tmnxWlanGwSoftGreIfGwAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfGwAddrType.setStatus("current")


class _TmnxWlanGwSoftGreIfGwAddr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreIfGwAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreIfGwAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreIfGwAddr_Object = MibTableColumn
tmnxWlanGwSoftGreIfGwAddr = _TmnxWlanGwSoftGreIfGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 5),
    _TmnxWlanGwSoftGreIfGwAddr_Type()
)
tmnxWlanGwSoftGreIfGwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfGwAddr.setStatus("current")


class _TmnxWlanGwSoftGreIfGrpId_Type(TmnxWlanGwIsaGrpIdOrZero):
    """Custom type tmnxWlanGwSoftGreIfGrpId based on TmnxWlanGwIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfGrpId_Type.__name__ = "TmnxWlanGwIsaGrpIdOrZero"
_TmnxWlanGwSoftGreIfGrpId_Object = MibTableColumn
tmnxWlanGwSoftGreIfGrpId = _TmnxWlanGwSoftGreIfGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 6),
    _TmnxWlanGwSoftGreIfGrpId_Type()
)
tmnxWlanGwSoftGreIfGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfGrpId.setStatus("current")


class _TmnxWlanGwSoftGreIfShapingType_Type(Integer32):
    """Custom type tmnxWlanGwSoftGreIfShapingType based on Integer32"""
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
          ("perTunnel", 1),
          ("perRetailer", 2))
    )


_TmnxWlanGwSoftGreIfShapingType_Type.__name__ = "Integer32"
_TmnxWlanGwSoftGreIfShapingType_Object = MibTableColumn
tmnxWlanGwSoftGreIfShapingType = _TmnxWlanGwSoftGreIfShapingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 7),
    _TmnxWlanGwSoftGreIfShapingType_Type()
)
tmnxWlanGwSoftGreIfShapingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfShapingType.setStatus("current")


class _TmnxWlanGwSoftGreIfShapeMultiUe_Type(TruthValue):
    """Custom type tmnxWlanGwSoftGreIfShapeMultiUe based on TruthValue"""
    defaultValue = 2


_TmnxWlanGwSoftGreIfShapeMultiUe_Type.__name__ = "TruthValue"
_TmnxWlanGwSoftGreIfShapeMultiUe_Object = MibTableColumn
tmnxWlanGwSoftGreIfShapeMultiUe = _TmnxWlanGwSoftGreIfShapeMultiUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 8),
    _TmnxWlanGwSoftGreIfShapeMultiUe_Type()
)
tmnxWlanGwSoftGreIfShapeMultiUe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfShapeMultiUe.setStatus("current")


class _TmnxWlanGwSoftGreIfEQosPlcy_Type(TPolicyID):
    """Custom type tmnxWlanGwSoftGreIfEQosPlcy based on TPolicyID"""
    defaultValue = 1

    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxWlanGwSoftGreIfEQosPlcy_Type.__name__ = "TPolicyID"
_TmnxWlanGwSoftGreIfEQosPlcy_Object = MibTableColumn
tmnxWlanGwSoftGreIfEQosPlcy = _TmnxWlanGwSoftGreIfEQosPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 9),
    _TmnxWlanGwSoftGreIfEQosPlcy_Type()
)
tmnxWlanGwSoftGreIfEQosPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfEQosPlcy.setStatus("current")


class _TmnxWlanGwSoftGreIfESchedPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSoftGreIfESchedPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSoftGreIfESchedPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSoftGreIfESchedPlcy_Object = MibTableColumn
tmnxWlanGwSoftGreIfESchedPlcy = _TmnxWlanGwSoftGreIfESchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 10),
    _TmnxWlanGwSoftGreIfESchedPlcy_Type()
)
tmnxWlanGwSoftGreIfESchedPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfESchedPlcy.setStatus("current")


class _TmnxWlanGwSoftGreIfEAggRateLimit_Type(TPortSchedulerPIR):
    """Custom type tmnxWlanGwSoftGreIfEAggRateLimit based on TPortSchedulerPIR"""
    defaultValue = -1


_TmnxWlanGwSoftGreIfEAggRateLimit_Type.__name__ = "TPortSchedulerPIR"
_TmnxWlanGwSoftGreIfEAggRateLimit_Object = MibTableColumn
tmnxWlanGwSoftGreIfEAggRateLimit = _TmnxWlanGwSoftGreIfEAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 11),
    _TmnxWlanGwSoftGreIfEAggRateLimit_Type()
)
tmnxWlanGwSoftGreIfEAggRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfEAggRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfEAggRateLimit.setUnits("kilobps")


class _TmnxWlanGwSoftGreIfMobTrigger_Type(Bits):
    """Custom type tmnxWlanGwSoftGreIfMobTrigger based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("data", 0),
          ("iapp", 1),
          ("control", 2))
    )

_TmnxWlanGwSoftGreIfMobTrigger_Type.__name__ = "Bits"
_TmnxWlanGwSoftGreIfMobTrigger_Object = MibTableColumn
tmnxWlanGwSoftGreIfMobTrigger = _TmnxWlanGwSoftGreIfMobTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 12),
    _TmnxWlanGwSoftGreIfMobTrigger_Type()
)
tmnxWlanGwSoftGreIfMobTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfMobTrigger.setStatus("current")


class _TmnxWlanGwSoftGreIfMobHoldTime_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreIfMobHoldTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxWlanGwSoftGreIfMobHoldTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreIfMobHoldTime_Object = MibTableColumn
tmnxWlanGwSoftGreIfMobHoldTime = _TmnxWlanGwSoftGreIfMobHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 13),
    _TmnxWlanGwSoftGreIfMobHoldTime_Type()
)
tmnxWlanGwSoftGreIfMobHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfMobHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfMobHoldTime.setUnits("seconds")


class _TmnxWlanGwSoftGreIfDefRetailSvc_Type(TmnxServId):
    """Custom type tmnxWlanGwSoftGreIfDefRetailSvc based on TmnxServId"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfDefRetailSvc_Type.__name__ = "TmnxServId"
_TmnxWlanGwSoftGreIfDefRetailSvc_Object = MibTableColumn
tmnxWlanGwSoftGreIfDefRetailSvc = _TmnxWlanGwSoftGreIfDefRetailSvc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 14),
    _TmnxWlanGwSoftGreIfDefRetailSvc_Type()
)
tmnxWlanGwSoftGreIfDefRetailSvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfDefRetailSvc.setStatus("current")


class _TmnxWlanGwSoftGreIfTcpMssAdjust_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreIfTcpMssAdjust based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(160, 10240),
    )


_TmnxWlanGwSoftGreIfTcpMssAdjust_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreIfTcpMssAdjust_Object = MibTableColumn
tmnxWlanGwSoftGreIfTcpMssAdjust = _TmnxWlanGwSoftGreIfTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 15),
    _TmnxWlanGwSoftGreIfTcpMssAdjust_Type()
)
tmnxWlanGwSoftGreIfTcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfTcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfTcpMssAdjust.setUnits("bytes")


class _TmnxWlanGwSoftGreIfEHoldTime_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreIfEHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxWlanGwSoftGreIfEHoldTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreIfEHoldTime_Object = MibTableColumn
tmnxWlanGwSoftGreIfEHoldTime = _TmnxWlanGwSoftGreIfEHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 16),
    _TmnxWlanGwSoftGreIfEHoldTime_Type()
)
tmnxWlanGwSoftGreIfEHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfEHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfEHoldTime.setUnits("seconds")


class _TmnxWlanGwSoftGreIfDataTrigg_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwSoftGreIfDataTrigg based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwSoftGreIfDataTrigg_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwSoftGreIfDataTrigg_Object = MibTableColumn
tmnxWlanGwSoftGreIfDataTrigg = _TmnxWlanGwSoftGreIfDataTrigg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 18),
    _TmnxWlanGwSoftGreIfDataTrigg_Type()
)
tmnxWlanGwSoftGreIfDataTrigg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfDataTrigg.setStatus("obsolete")


class _TmnxWlanGwSoftGreIfAuthPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSoftGreIfAuthPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSoftGreIfAuthPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSoftGreIfAuthPlcy_Object = MibTableColumn
tmnxWlanGwSoftGreIfAuthPlcy = _TmnxWlanGwSoftGreIfAuthPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 19),
    _TmnxWlanGwSoftGreIfAuthPlcy_Type()
)
tmnxWlanGwSoftGreIfAuthPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfAuthPlcy.setStatus("obsolete")


class _TmnxWlanGwSoftGreIfAuthHoldTime_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreIfAuthHoldTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TmnxWlanGwSoftGreIfAuthHoldTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreIfAuthHoldTime_Object = MibTableColumn
tmnxWlanGwSoftGreIfAuthHoldTime = _TmnxWlanGwSoftGreIfAuthHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 20),
    _TmnxWlanGwSoftGreIfAuthHoldTime_Type()
)
tmnxWlanGwSoftGreIfAuthHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfAuthHoldTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfAuthHoldTime.setUnits("seconds")


class _TmnxWlanGwSoftGreIfRadProxVrtr_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxWlanGwSoftGreIfRadProxVrtr based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfRadProxVrtr_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxWlanGwSoftGreIfRadProxVrtr_Object = MibTableColumn
tmnxWlanGwSoftGreIfRadProxVrtr = _TmnxWlanGwSoftGreIfRadProxVrtr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 21),
    _TmnxWlanGwSoftGreIfRadProxVrtr_Type()
)
tmnxWlanGwSoftGreIfRadProxVrtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfRadProxVrtr.setStatus("obsolete")


class _TmnxWlanGwSoftGreIfRadProxSrv_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSoftGreIfRadProxSrv based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSoftGreIfRadProxSrv_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSoftGreIfRadProxSrv_Object = MibTableColumn
tmnxWlanGwSoftGreIfRadProxSrv = _TmnxWlanGwSoftGreIfRadProxSrv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 22),
    _TmnxWlanGwSoftGreIfRadProxSrv_Type()
)
tmnxWlanGwSoftGreIfRadProxSrv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfRadProxSrv.setStatus("obsolete")


class _TmnxWlanGwSoftGreIfRadProxMacFmt_Type(TmnxMacSpecification):
    """Custom type tmnxWlanGwSoftGreIfRadProxMacFmt based on TmnxMacSpecification"""
    defaultValue = OctetString("aa:")

    subtypeSpec = TmnxMacSpecification.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 7),
    )


_TmnxWlanGwSoftGreIfRadProxMacFmt_Type.__name__ = "TmnxMacSpecification"
_TmnxWlanGwSoftGreIfRadProxMacFmt_Object = MibTableColumn
tmnxWlanGwSoftGreIfRadProxMacFmt = _TmnxWlanGwSoftGreIfRadProxMacFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 23),
    _TmnxWlanGwSoftGreIfRadProxMacFmt_Type()
)
tmnxWlanGwSoftGreIfRadProxMacFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfRadProxMacFmt.setStatus("obsolete")


class _TmnxWlanGwSoftGreIfSsidType_Type(TmnxWlanGwSsidType):
    """Custom type tmnxWlanGwSoftGreIfSsidType based on TmnxWlanGwSsidType"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfSsidType_Type.__name__ = "TmnxWlanGwSsidType"
_TmnxWlanGwSoftGreIfSsidType_Object = MibTableColumn
tmnxWlanGwSoftGreIfSsidType = _TmnxWlanGwSoftGreIfSsidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 28),
    _TmnxWlanGwSoftGreIfSsidType_Type()
)
tmnxWlanGwSoftGreIfSsidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfSsidType.setStatus("current")


class _TmnxWlanGwSoftGreIfGwV6AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreIfGwV6AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfGwV6AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreIfGwV6AddrType_Object = MibTableColumn
tmnxWlanGwSoftGreIfGwV6AddrType = _TmnxWlanGwSoftGreIfGwV6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 29),
    _TmnxWlanGwSoftGreIfGwV6AddrType_Type()
)
tmnxWlanGwSoftGreIfGwV6AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfGwV6AddrType.setStatus("current")


class _TmnxWlanGwSoftGreIfGwV6Addr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreIfGwV6Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreIfGwV6Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreIfGwV6Addr_Object = MibTableColumn
tmnxWlanGwSoftGreIfGwV6Addr = _TmnxWlanGwSoftGreIfGwV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 30),
    _TmnxWlanGwSoftGreIfGwV6Addr_Type()
)
tmnxWlanGwSoftGreIfGwV6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfGwV6Addr.setStatus("current")


class _TmnxWlanGwSoftGreIfMobArpAp_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwSoftGreIfMobArpAp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwSoftGreIfMobArpAp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwSoftGreIfMobArpAp_Object = MibTableColumn
tmnxWlanGwSoftGreIfMobArpAp = _TmnxWlanGwSoftGreIfMobArpAp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 32),
    _TmnxWlanGwSoftGreIfMobArpAp_Type()
)
tmnxWlanGwSoftGreIfMobArpAp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfMobArpAp.setStatus("current")


class _TmnxWlanGwSoftGreIfDownIfGrpDeg_Type(TruthValue):
    """Custom type tmnxWlanGwSoftGreIfDownIfGrpDeg based on TruthValue"""
    defaultValue = 2


_TmnxWlanGwSoftGreIfDownIfGrpDeg_Type.__name__ = "TruthValue"
_TmnxWlanGwSoftGreIfDownIfGrpDeg_Object = MibTableColumn
tmnxWlanGwSoftGreIfDownIfGrpDeg = _TmnxWlanGwSoftGreIfDownIfGrpDeg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 35),
    _TmnxWlanGwSoftGreIfDownIfGrpDeg_Type()
)
tmnxWlanGwSoftGreIfDownIfGrpDeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfDownIfGrpDeg.setStatus("current")


class _TmnxWlanGwSoftGreIfL2ApEncapType_Type(Integer32):
    """Custom type tmnxWlanGwSoftGreIfL2ApEncapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("dot1q", 2),
          ("qinq", 10))
    )


_TmnxWlanGwSoftGreIfL2ApEncapType_Type.__name__ = "Integer32"
_TmnxWlanGwSoftGreIfL2ApEncapType_Object = MibTableColumn
tmnxWlanGwSoftGreIfL2ApEncapType = _TmnxWlanGwSoftGreIfL2ApEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 36),
    _TmnxWlanGwSoftGreIfL2ApEncapType_Type()
)
tmnxWlanGwSoftGreIfL2ApEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfL2ApEncapType.setStatus("current")


class _TmnxWlanGwSoftGreIfMultiTuType_Type(TruthValue):
    """Custom type tmnxWlanGwSoftGreIfMultiTuType based on TruthValue"""
    defaultValue = 2


_TmnxWlanGwSoftGreIfMultiTuType_Type.__name__ = "TruthValue"
_TmnxWlanGwSoftGreIfMultiTuType_Object = MibTableColumn
tmnxWlanGwSoftGreIfMultiTuType = _TmnxWlanGwSoftGreIfMultiTuType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 37),
    _TmnxWlanGwSoftGreIfMultiTuType_Type()
)
tmnxWlanGwSoftGreIfMultiTuType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfMultiTuType.setStatus("current")


class _TmnxWlanGwSoftGreIfL2tpLrnCookie_Type(Integer32):
    """Custom type tmnxWlanGwSoftGreIfL2tpLrnCookie based on Integer32"""
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
        *(("ifMatch", 1),
          ("never", 2),
          ("always", 3))
    )


_TmnxWlanGwSoftGreIfL2tpLrnCookie_Type.__name__ = "Integer32"
_TmnxWlanGwSoftGreIfL2tpLrnCookie_Object = MibTableColumn
tmnxWlanGwSoftGreIfL2tpLrnCookie = _TmnxWlanGwSoftGreIfL2tpLrnCookie_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 38),
    _TmnxWlanGwSoftGreIfL2tpLrnCookie_Type()
)
tmnxWlanGwSoftGreIfL2tpLrnCookie.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfL2tpLrnCookie.setStatus("current")


class _TmnxWlanGwSoftGreIfL2tpCookie_Type(OctetString):
    """Custom type tmnxWlanGwSoftGreIfL2tpCookie based on OctetString"""
    defaultHexValue = "0000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_TmnxWlanGwSoftGreIfL2tpCookie_Type.__name__ = "OctetString"
_TmnxWlanGwSoftGreIfL2tpCookie_Object = MibTableColumn
tmnxWlanGwSoftGreIfL2tpCookie = _TmnxWlanGwSoftGreIfL2tpCookie_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 39),
    _TmnxWlanGwSoftGreIfL2tpCookie_Type()
)
tmnxWlanGwSoftGreIfL2tpCookie.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfL2tpCookie.setStatus("current")


class _TmnxWlanGwSoftGreIfMaxLanextBd_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreIfMaxLanextBd based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131071),
    )


_TmnxWlanGwSoftGreIfMaxLanextBd_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreIfMaxLanextBd_Object = MibTableColumn
tmnxWlanGwSoftGreIfMaxLanextBd = _TmnxWlanGwSoftGreIfMaxLanextBd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 40),
    _TmnxWlanGwSoftGreIfMaxLanextBd_Type()
)
tmnxWlanGwSoftGreIfMaxLanextBd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfMaxLanextBd.setStatus("current")
_TmnxWlanGwSoftGreIfNumSoftGreTu_Type = Gauge32
_TmnxWlanGwSoftGreIfNumSoftGreTu_Object = MibTableColumn
tmnxWlanGwSoftGreIfNumSoftGreTu = _TmnxWlanGwSoftGreIfNumSoftGreTu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 100),
    _TmnxWlanGwSoftGreIfNumSoftGreTu_Type()
)
tmnxWlanGwSoftGreIfNumSoftGreTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfNumSoftGreTu.setStatus("current")


class _TmnxWlanGwSoftGreIfLearnApMac_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwSoftGreIfLearnApMac based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwSoftGreIfLearnApMac_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwSoftGreIfLearnApMac_Object = MibTableColumn
tmnxWlanGwSoftGreIfLearnApMac = _TmnxWlanGwSoftGreIfLearnApMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 110),
    _TmnxWlanGwSoftGreIfLearnApMac_Type()
)
tmnxWlanGwSoftGreIfLearnApMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfLearnApMac.setStatus("current")


class _TmnxWlanGwSoftGreIfLearnApMacDA_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwSoftGreIfLearnApMacDA based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwSoftGreIfLearnApMacDA_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwSoftGreIfLearnApMacDA_Object = MibTableColumn
tmnxWlanGwSoftGreIfLearnApMacDA = _TmnxWlanGwSoftGreIfLearnApMacDA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 111),
    _TmnxWlanGwSoftGreIfLearnApMacDA_Type()
)
tmnxWlanGwSoftGreIfLearnApMacDA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfLearnApMacDA.setStatus("current")


class _TmnxWlanGwSoftGreIfMobInterVlan_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwSoftGreIfMobInterVlan based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwSoftGreIfMobInterVlan_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwSoftGreIfMobInterVlan_Object = MibTableColumn
tmnxWlanGwSoftGreIfMobInterVlan = _TmnxWlanGwSoftGreIfMobInterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 112),
    _TmnxWlanGwSoftGreIfMobInterVlan_Type()
)
tmnxWlanGwSoftGreIfMobInterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfMobInterVlan.setStatus("current")


class _TmnxWlanGwSoftGreIfL2ApAutoSubId_Type(Integer32):
    """Custom type tmnxWlanGwSoftGreIfL2ApAutoSubId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("include-ap-tags", 0),
          ("sap-only", 1))
    )


_TmnxWlanGwSoftGreIfL2ApAutoSubId_Type.__name__ = "Integer32"
_TmnxWlanGwSoftGreIfL2ApAutoSubId_Object = MibTableColumn
tmnxWlanGwSoftGreIfL2ApAutoSubId = _TmnxWlanGwSoftGreIfL2ApAutoSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 113),
    _TmnxWlanGwSoftGreIfL2ApAutoSubId_Type()
)
tmnxWlanGwSoftGreIfL2ApAutoSubId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfL2ApAutoSubId.setStatus("current")
_TmnxWlanGwSoftGreTuTable_Object = MibTable
tmnxWlanGwSoftGreTuTable = _TmnxWlanGwSoftGreTuTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuTable.setStatus("current")
_TmnxWlanGwSoftGreTuEntry_Object = MibTableRow
tmnxWlanGwSoftGreTuEntry = _TmnxWlanGwSoftGreTuEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1)
)
tmnxWlanGwSoftGreTuEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddrTyp"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddr"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuEntry.setStatus("current")
_TmnxWlanGwSoftGreTuRemoteAddrTyp_Type = InetAddressType
_TmnxWlanGwSoftGreTuRemoteAddrTyp_Object = MibTableColumn
tmnxWlanGwSoftGreTuRemoteAddrTyp = _TmnxWlanGwSoftGreTuRemoteAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 1),
    _TmnxWlanGwSoftGreTuRemoteAddrTyp_Type()
)
tmnxWlanGwSoftGreTuRemoteAddrTyp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuRemoteAddrTyp.setStatus("current")


class _TmnxWlanGwSoftGreTuRemoteAddr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreTuRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreTuRemoteAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreTuRemoteAddr_Object = MibTableColumn
tmnxWlanGwSoftGreTuRemoteAddr = _TmnxWlanGwSoftGreTuRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 2),
    _TmnxWlanGwSoftGreTuRemoteAddr_Type()
)
tmnxWlanGwSoftGreTuRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuRemoteAddr.setStatus("current")
_TmnxWlanGwSoftGreTuLocalAddrType_Type = InetAddressType
_TmnxWlanGwSoftGreTuLocalAddrType_Object = MibTableColumn
tmnxWlanGwSoftGreTuLocalAddrType = _TmnxWlanGwSoftGreTuLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 3),
    _TmnxWlanGwSoftGreTuLocalAddrType_Type()
)
tmnxWlanGwSoftGreTuLocalAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuLocalAddrType.setStatus("current")


class _TmnxWlanGwSoftGreTuLocalAddr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreTuLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreTuLocalAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreTuLocalAddr_Object = MibTableColumn
tmnxWlanGwSoftGreTuLocalAddr = _TmnxWlanGwSoftGreTuLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 4),
    _TmnxWlanGwSoftGreTuLocalAddr_Type()
)
tmnxWlanGwSoftGreTuLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuLocalAddr.setStatus("current")


class _TmnxWlanGwSoftGreTuEstabTime_Type(DateAndTime):
    """Custom type tmnxWlanGwSoftGreTuEstabTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwSoftGreTuEstabTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwSoftGreTuEstabTime_Object = MibTableColumn
tmnxWlanGwSoftGreTuEstabTime = _TmnxWlanGwSoftGreTuEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 5),
    _TmnxWlanGwSoftGreTuEstabTime_Type()
)
tmnxWlanGwSoftGreTuEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuEstabTime.setStatus("current")
_TmnxWlanGwSoftGreTuIsaGroup_Type = TmnxWlanGwIsaGrpIdOrZero
_TmnxWlanGwSoftGreTuIsaGroup_Object = MibTableColumn
tmnxWlanGwSoftGreTuIsaGroup = _TmnxWlanGwSoftGreTuIsaGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 6),
    _TmnxWlanGwSoftGreTuIsaGroup_Type()
)
tmnxWlanGwSoftGreTuIsaGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuIsaGroup.setStatus("current")
_TmnxWlanGwSoftGreTuIsaMember_Type = Unsigned32
_TmnxWlanGwSoftGreTuIsaMember_Object = MibTableColumn
tmnxWlanGwSoftGreTuIsaMember = _TmnxWlanGwSoftGreTuIsaMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 7),
    _TmnxWlanGwSoftGreTuIsaMember_Type()
)
tmnxWlanGwSoftGreTuIsaMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuIsaMember.setStatus("current")
_TmnxWlanGwSoftGreTuNumUe_Type = Gauge32
_TmnxWlanGwSoftGreTuNumUe_Object = MibTableColumn
tmnxWlanGwSoftGreTuNumUe = _TmnxWlanGwSoftGreTuNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 8),
    _TmnxWlanGwSoftGreTuNumUe_Type()
)
tmnxWlanGwSoftGreTuNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuNumUe.setStatus("current")
_TmnxWlanGwSoftGreTuApMacAddress_Type = MacAddress
_TmnxWlanGwSoftGreTuApMacAddress_Object = MibTableColumn
tmnxWlanGwSoftGreTuApMacAddress = _TmnxWlanGwSoftGreTuApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 10),
    _TmnxWlanGwSoftGreTuApMacAddress_Type()
)
tmnxWlanGwSoftGreTuApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuApMacAddress.setStatus("current")
_TmnxWlanGwSoftGreTuApLearnFailed_Type = TruthValue
_TmnxWlanGwSoftGreTuApLearnFailed_Object = MibTableColumn
tmnxWlanGwSoftGreTuApLearnFailed = _TmnxWlanGwSoftGreTuApLearnFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 11),
    _TmnxWlanGwSoftGreTuApLearnFailed_Type()
)
tmnxWlanGwSoftGreTuApLearnFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuApLearnFailed.setStatus("current")


class _TmnxWlanGwSoftGreTuEncap_Type(Integer32):
    """Custom type tmnxWlanGwSoftGreTuEncap based on Integer32"""
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
        *(("gre", 1),
          ("l2tp", 2),
          ("l2", 3),
          ("vxlan", 4))
    )


_TmnxWlanGwSoftGreTuEncap_Type.__name__ = "Integer32"
_TmnxWlanGwSoftGreTuEncap_Object = MibTableColumn
tmnxWlanGwSoftGreTuEncap = _TmnxWlanGwSoftGreTuEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 12),
    _TmnxWlanGwSoftGreTuEncap_Type()
)
tmnxWlanGwSoftGreTuEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuEncap.setStatus("current")
_TmnxWlanGwSoftGreTuEncapTag1_Type = QTagFullRangeOrNone
_TmnxWlanGwSoftGreTuEncapTag1_Object = MibTableColumn
tmnxWlanGwSoftGreTuEncapTag1 = _TmnxWlanGwSoftGreTuEncapTag1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 13),
    _TmnxWlanGwSoftGreTuEncapTag1_Type()
)
tmnxWlanGwSoftGreTuEncapTag1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuEncapTag1.setStatus("current")
_TmnxWlanGwSoftGreTuEncapTag2_Type = QTagFullRangeOrNone
_TmnxWlanGwSoftGreTuEncapTag2_Object = MibTableColumn
tmnxWlanGwSoftGreTuEncapTag2 = _TmnxWlanGwSoftGreTuEncapTag2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 14),
    _TmnxWlanGwSoftGreTuEncapTag2_Type()
)
tmnxWlanGwSoftGreTuEncapTag2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuEncapTag2.setStatus("current")
_TmnxWlanGwSoftGreTuService_Type = TmnxServId
_TmnxWlanGwSoftGreTuService_Object = MibTableColumn
tmnxWlanGwSoftGreTuService = _TmnxWlanGwSoftGreTuService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 15),
    _TmnxWlanGwSoftGreTuService_Type()
)
tmnxWlanGwSoftGreTuService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuService.setStatus("current")
_TmnxWlanGwSoftGreTuInterface_Type = InterfaceIndexOrZero
_TmnxWlanGwSoftGreTuInterface_Object = MibTableColumn
tmnxWlanGwSoftGreTuInterface = _TmnxWlanGwSoftGreTuInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 16),
    _TmnxWlanGwSoftGreTuInterface_Type()
)
tmnxWlanGwSoftGreTuInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuInterface.setStatus("current")
_TmnxWlanGwSoftGreTuApSapPortId_Type = TmnxPortID
_TmnxWlanGwSoftGreTuApSapPortId_Object = MibTableColumn
tmnxWlanGwSoftGreTuApSapPortId = _TmnxWlanGwSoftGreTuApSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 17),
    _TmnxWlanGwSoftGreTuApSapPortId_Type()
)
tmnxWlanGwSoftGreTuApSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuApSapPortId.setStatus("current")
_TmnxWlanGwSoftGreTuApSapEncapVal_Type = TmnxEncapVal
_TmnxWlanGwSoftGreTuApSapEncapVal_Object = MibTableColumn
tmnxWlanGwSoftGreTuApSapEncapVal = _TmnxWlanGwSoftGreTuApSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 18),
    _TmnxWlanGwSoftGreTuApSapEncapVal_Type()
)
tmnxWlanGwSoftGreTuApSapEncapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuApSapEncapVal.setStatus("current")
_TmnxWlanGwTuQosTable_Object = MibTable
tmnxWlanGwTuQosTable = _TmnxWlanGwTuQosTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosTable.setStatus("current")
_TmnxWlanGwTuQosEntry_Object = MibTableRow
tmnxWlanGwTuQosEntry = _TmnxWlanGwTuQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1)
)
tmnxWlanGwTuQosEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddrTyp"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosRetailService"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosEntry.setStatus("current")
_TmnxWlanGwTuQosRetailService_Type = TmnxServId
_TmnxWlanGwTuQosRetailService_Object = MibTableColumn
tmnxWlanGwTuQosRetailService = _TmnxWlanGwTuQosRetailService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 1),
    _TmnxWlanGwTuQosRetailService_Type()
)
tmnxWlanGwTuQosRetailService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosRetailService.setStatus("current")
_TmnxWlanGwTuQosEegSvcId_Type = TmnxServId
_TmnxWlanGwTuQosEegSvcId_Object = MibTableColumn
tmnxWlanGwTuQosEegSvcId = _TmnxWlanGwTuQosEegSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 2),
    _TmnxWlanGwTuQosEegSvcId_Type()
)
tmnxWlanGwTuQosEegSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosEegSvcId.setStatus("current")
_TmnxWlanGwTuQosEegPortId_Type = TmnxPortID
_TmnxWlanGwTuQosEegPortId_Object = MibTableColumn
tmnxWlanGwTuQosEegPortId = _TmnxWlanGwTuQosEegPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 3),
    _TmnxWlanGwTuQosEegPortId_Type()
)
tmnxWlanGwTuQosEegPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosEegPortId.setStatus("current")
_TmnxWlanGwTuQosEegEncapValue_Type = TmnxEncapVal
_TmnxWlanGwTuQosEegEncapValue_Object = MibTableColumn
tmnxWlanGwTuQosEegEncapValue = _TmnxWlanGwTuQosEegEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 4),
    _TmnxWlanGwTuQosEegEncapValue_Type()
)
tmnxWlanGwTuQosEegEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosEegEncapValue.setStatus("current")
_TmnxWlanGwTuQosEegName_Type = TNamedItemOrEmpty
_TmnxWlanGwTuQosEegName_Object = MibTableColumn
tmnxWlanGwTuQosEegName = _TmnxWlanGwTuQosEegName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 5),
    _TmnxWlanGwTuQosEegName_Type()
)
tmnxWlanGwTuQosEegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosEegName.setStatus("current")
_TmnxWlanGwTuQosEegMember_Type = SvcISID
_TmnxWlanGwTuQosEegMember_Object = MibTableColumn
tmnxWlanGwTuQosEegMember = _TmnxWlanGwTuQosEegMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 6),
    _TmnxWlanGwTuQosEegMember_Type()
)
tmnxWlanGwTuQosEegMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosEegMember.setStatus("current")
_TmnxWlanGwTuQosState_Type = TmnxWlanGwQoSOperState
_TmnxWlanGwTuQosState_Object = MibTableColumn
tmnxWlanGwTuQosState = _TmnxWlanGwTuQosState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 7),
    _TmnxWlanGwTuQosState_Type()
)
tmnxWlanGwTuQosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosState.setStatus("current")
_TmnxWlanGwTuQosNumUe_Type = Gauge32
_TmnxWlanGwTuQosNumUe_Object = MibTableColumn
tmnxWlanGwTuQosNumUe = _TmnxWlanGwTuQosNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 8),
    _TmnxWlanGwTuQosNumUe_Type()
)
tmnxWlanGwTuQosNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosNumUe.setStatus("current")
_TmnxWlanGwTuQosRemainingHoldTime_Type = Gauge32
_TmnxWlanGwTuQosRemainingHoldTime_Object = MibTableColumn
tmnxWlanGwTuQosRemainingHoldTime = _TmnxWlanGwTuQosRemainingHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 9),
    _TmnxWlanGwTuQosRemainingHoldTime_Type()
)
tmnxWlanGwTuQosRemainingHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosRemainingHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosRemainingHoldTime.setUnits("seconds")
_TmnxWlanGwSoftGreTuUeTable_Object = MibTable
tmnxWlanGwSoftGreTuUeTable = _TmnxWlanGwSoftGreTuUeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuUeTable.setStatus("current")
_TmnxWlanGwSoftGreTuUeEntry_Object = MibTableRow
tmnxWlanGwSoftGreTuUeEntry = _TmnxWlanGwSoftGreTuUeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 4, 1)
)
tmnxWlanGwSoftGreTuUeEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddrTyp"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeMacAddress"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuUeEntry.setStatus("current")
_TmnxWlanGwSoftGreTuUeSsid_Type = TNamedItemOrEmpty
_TmnxWlanGwSoftGreTuUeSsid_Object = MibTableColumn
tmnxWlanGwSoftGreTuUeSsid = _TmnxWlanGwSoftGreTuUeSsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 4, 1, 1),
    _TmnxWlanGwSoftGreTuUeSsid_Type()
)
tmnxWlanGwSoftGreTuUeSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuUeSsid.setStatus("current")
_TmnxWlanGwSoftGreXtTable_Object = MibTable
tmnxWlanGwSoftGreXtTable = _TmnxWlanGwSoftGreXtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtTable.setStatus("obsolete")
_TmnxWlanGwSoftGreXtEntry_Object = MibTableRow
tmnxWlanGwSoftGreXtEntry = _TmnxWlanGwSoftGreXtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtEntry.setStatus("obsolete")
_TmnxWlanGwSoftGreXtLastCh_Type = TimeStamp
_TmnxWlanGwSoftGreXtLastCh_Object = MibTableColumn
tmnxWlanGwSoftGreXtLastCh = _TmnxWlanGwSoftGreXtLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 1),
    _TmnxWlanGwSoftGreXtLastCh_Type()
)
tmnxWlanGwSoftGreXtLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtLastCh.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtDhcp_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwSoftGreXtDhcp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwSoftGreXtDhcp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwSoftGreXtDhcp_Object = MibTableColumn
tmnxWlanGwSoftGreXtDhcp = _TmnxWlanGwSoftGreXtDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 2),
    _TmnxWlanGwSoftGreXtDhcp_Type()
)
tmnxWlanGwSoftGreXtDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtDhcp.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreXtAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreXtAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreXtAddrType_Object = MibTableColumn
tmnxWlanGwSoftGreXtAddrType = _TmnxWlanGwSoftGreXtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 3),
    _TmnxWlanGwSoftGreXtAddrType_Type()
)
tmnxWlanGwSoftGreXtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtAddrType.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtAddr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreXtAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreXtAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreXtAddr_Object = MibTableColumn
tmnxWlanGwSoftGreXtAddr = _TmnxWlanGwSoftGreXtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 4),
    _TmnxWlanGwSoftGreXtAddr_Type()
)
tmnxWlanGwSoftGreXtAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtAddr.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtLeaseTime_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreXtLeaseTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwSoftGreXtLeaseTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreXtLeaseTime_Object = MibTableColumn
tmnxWlanGwSoftGreXtLeaseTime = _TmnxWlanGwSoftGreXtLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 5),
    _TmnxWlanGwSoftGreXtLeaseTime_Type()
)
tmnxWlanGwSoftGreXtLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtLeaseTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtLeaseTime.setUnits("seconds")


class _TmnxWlanGwSoftGreXtActLeaseTime_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreXtActLeaseTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwSoftGreXtActLeaseTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreXtActLeaseTime_Object = MibTableColumn
tmnxWlanGwSoftGreXtActLeaseTime = _TmnxWlanGwSoftGreXtActLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 6),
    _TmnxWlanGwSoftGreXtActLeaseTime_Type()
)
tmnxWlanGwSoftGreXtActLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtActLeaseTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtActLeaseTime.setUnits("seconds")


class _TmnxWlanGwSoftGreXtDns1AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreXtDns1AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreXtDns1AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreXtDns1AddrType_Object = MibTableColumn
tmnxWlanGwSoftGreXtDns1AddrType = _TmnxWlanGwSoftGreXtDns1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 7),
    _TmnxWlanGwSoftGreXtDns1AddrType_Type()
)
tmnxWlanGwSoftGreXtDns1AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtDns1AddrType.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtDns1Addr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreXtDns1Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreXtDns1Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreXtDns1Addr_Object = MibTableColumn
tmnxWlanGwSoftGreXtDns1Addr = _TmnxWlanGwSoftGreXtDns1Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 8),
    _TmnxWlanGwSoftGreXtDns1Addr_Type()
)
tmnxWlanGwSoftGreXtDns1Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtDns1Addr.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtDns2AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreXtDns2AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreXtDns2AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreXtDns2AddrType_Object = MibTableColumn
tmnxWlanGwSoftGreXtDns2AddrType = _TmnxWlanGwSoftGreXtDns2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 9),
    _TmnxWlanGwSoftGreXtDns2AddrType_Type()
)
tmnxWlanGwSoftGreXtDns2AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtDns2AddrType.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtDns2Addr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreXtDns2Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreXtDns2Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreXtDns2Addr_Object = MibTableColumn
tmnxWlanGwSoftGreXtDns2Addr = _TmnxWlanGwSoftGreXtDns2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 10),
    _TmnxWlanGwSoftGreXtDns2Addr_Type()
)
tmnxWlanGwSoftGreXtDns2Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtDns2Addr.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtNb1AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreXtNb1AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreXtNb1AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreXtNb1AddrType_Object = MibTableColumn
tmnxWlanGwSoftGreXtNb1AddrType = _TmnxWlanGwSoftGreXtNb1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 11),
    _TmnxWlanGwSoftGreXtNb1AddrType_Type()
)
tmnxWlanGwSoftGreXtNb1AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtNb1AddrType.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtNb1Addr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreXtNb1Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreXtNb1Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreXtNb1Addr_Object = MibTableColumn
tmnxWlanGwSoftGreXtNb1Addr = _TmnxWlanGwSoftGreXtNb1Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 12),
    _TmnxWlanGwSoftGreXtNb1Addr_Type()
)
tmnxWlanGwSoftGreXtNb1Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtNb1Addr.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtNb2AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreXtNb2AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreXtNb2AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreXtNb2AddrType_Object = MibTableColumn
tmnxWlanGwSoftGreXtNb2AddrType = _TmnxWlanGwSoftGreXtNb2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 13),
    _TmnxWlanGwSoftGreXtNb2AddrType_Type()
)
tmnxWlanGwSoftGreXtNb2AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtNb2AddrType.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtNb2Addr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreXtNb2Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreXtNb2Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreXtNb2Addr_Object = MibTableColumn
tmnxWlanGwSoftGreXtNb2Addr = _TmnxWlanGwSoftGreXtNb2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 14),
    _TmnxWlanGwSoftGreXtNb2Addr_Type()
)
tmnxWlanGwSoftGreXtNb2Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtNb2Addr.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtHttpRdrPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSoftGreXtHttpRdrPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSoftGreXtHttpRdrPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSoftGreXtHttpRdrPlcy_Object = MibTableColumn
tmnxWlanGwSoftGreXtHttpRdrPlcy = _TmnxWlanGwSoftGreXtHttpRdrPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 21),
    _TmnxWlanGwSoftGreXtHttpRdrPlcy_Type()
)
tmnxWlanGwSoftGreXtHttpRdrPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtHttpRdrPlcy.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtNatPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSoftGreXtNatPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSoftGreXtNatPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSoftGreXtNatPlcy_Object = MibTableColumn
tmnxWlanGwSoftGreXtNatPlcy = _TmnxWlanGwSoftGreXtNatPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 22),
    _TmnxWlanGwSoftGreXtNatPlcy_Type()
)
tmnxWlanGwSoftGreXtNatPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtNatPlcy.setStatus("obsolete")
_TmnxWlanGwVlanTable_Object = MibTable
tmnxWlanGwVlanTable = _TmnxWlanGwVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanTable.setStatus("current")
_TmnxWlanGwVlanEntry_Object = MibTableRow
tmnxWlanGwVlanEntry = _TmnxWlanGwVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1)
)
tmnxWlanGwVlanEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanTagStart"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanTagEnd"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanEntry.setStatus("current")


class _TmnxWlanGwVlanTagStart_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanTagStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TmnxWlanGwVlanTagStart_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanTagStart_Object = MibTableColumn
tmnxWlanGwVlanTagStart = _TmnxWlanGwVlanTagStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 1),
    _TmnxWlanGwVlanTagStart_Type()
)
tmnxWlanGwVlanTagStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanTagStart.setStatus("current")


class _TmnxWlanGwVlanTagEnd_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanTagEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TmnxWlanGwVlanTagEnd_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanTagEnd_Object = MibTableColumn
tmnxWlanGwVlanTagEnd = _TmnxWlanGwVlanTagEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 2),
    _TmnxWlanGwVlanTagEnd_Type()
)
tmnxWlanGwVlanTagEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanTagEnd.setStatus("current")
_TmnxWlanGwVlanRowStatus_Type = RowStatus
_TmnxWlanGwVlanRowStatus_Object = MibTableColumn
tmnxWlanGwVlanRowStatus = _TmnxWlanGwVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 3),
    _TmnxWlanGwVlanRowStatus_Type()
)
tmnxWlanGwVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanRowStatus.setStatus("current")
_TmnxWlanGwVlanLastCh_Type = TimeStamp
_TmnxWlanGwVlanLastCh_Object = MibTableColumn
tmnxWlanGwVlanLastCh = _TmnxWlanGwVlanLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 4),
    _TmnxWlanGwVlanLastCh_Type()
)
tmnxWlanGwVlanLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLastCh.setStatus("current")


class _TmnxWlanGwVlanRetailService_Type(TmnxServId):
    """Custom type tmnxWlanGwVlanRetailService based on TmnxServId"""
    defaultValue = 0


_TmnxWlanGwVlanRetailService_Type.__name__ = "TmnxServId"
_TmnxWlanGwVlanRetailService_Object = MibTableColumn
tmnxWlanGwVlanRetailService = _TmnxWlanGwVlanRetailService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 5),
    _TmnxWlanGwVlanRetailService_Type()
)
tmnxWlanGwVlanRetailService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanRetailService.setStatus("current")


class _TmnxWlanGwVlanDhcp_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanDhcp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanDhcp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanDhcp_Object = MibTableColumn
tmnxWlanGwVlanDhcp = _TmnxWlanGwVlanDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 6),
    _TmnxWlanGwVlanDhcp_Type()
)
tmnxWlanGwVlanDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp.setStatus("current")


class _TmnxWlanGwVlanAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwVlanAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwVlanAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwVlanAddrType_Object = MibTableColumn
tmnxWlanGwVlanAddrType = _TmnxWlanGwVlanAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 7),
    _TmnxWlanGwVlanAddrType_Type()
)
tmnxWlanGwVlanAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAddrType.setStatus("current")


class _TmnxWlanGwVlanAddr_Type(InetAddress):
    """Custom type tmnxWlanGwVlanAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwVlanAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwVlanAddr_Object = MibTableColumn
tmnxWlanGwVlanAddr = _TmnxWlanGwVlanAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 8),
    _TmnxWlanGwVlanAddr_Type()
)
tmnxWlanGwVlanAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAddr.setStatus("current")


class _TmnxWlanGwVlanLeaseTime_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanLeaseTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwVlanLeaseTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanLeaseTime_Object = MibTableColumn
tmnxWlanGwVlanLeaseTime = _TmnxWlanGwVlanLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 9),
    _TmnxWlanGwVlanLeaseTime_Type()
)
tmnxWlanGwVlanLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeaseTime.setUnits("seconds")


class _TmnxWlanGwVlanActLeaseTime_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanActLeaseTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwVlanActLeaseTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanActLeaseTime_Object = MibTableColumn
tmnxWlanGwVlanActLeaseTime = _TmnxWlanGwVlanActLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 10),
    _TmnxWlanGwVlanActLeaseTime_Type()
)
tmnxWlanGwVlanActLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanActLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanActLeaseTime.setUnits("seconds")


class _TmnxWlanGwVlanDns1AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwVlanDns1AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwVlanDns1AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwVlanDns1AddrType_Object = MibTableColumn
tmnxWlanGwVlanDns1AddrType = _TmnxWlanGwVlanDns1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 11),
    _TmnxWlanGwVlanDns1AddrType_Type()
)
tmnxWlanGwVlanDns1AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDns1AddrType.setStatus("current")


class _TmnxWlanGwVlanDns1Addr_Type(InetAddress):
    """Custom type tmnxWlanGwVlanDns1Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwVlanDns1Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwVlanDns1Addr_Object = MibTableColumn
tmnxWlanGwVlanDns1Addr = _TmnxWlanGwVlanDns1Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 12),
    _TmnxWlanGwVlanDns1Addr_Type()
)
tmnxWlanGwVlanDns1Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDns1Addr.setStatus("current")


class _TmnxWlanGwVlanDns2AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwVlanDns2AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwVlanDns2AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwVlanDns2AddrType_Object = MibTableColumn
tmnxWlanGwVlanDns2AddrType = _TmnxWlanGwVlanDns2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 13),
    _TmnxWlanGwVlanDns2AddrType_Type()
)
tmnxWlanGwVlanDns2AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDns2AddrType.setStatus("current")


class _TmnxWlanGwVlanDns2Addr_Type(InetAddress):
    """Custom type tmnxWlanGwVlanDns2Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwVlanDns2Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwVlanDns2Addr_Object = MibTableColumn
tmnxWlanGwVlanDns2Addr = _TmnxWlanGwVlanDns2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 14),
    _TmnxWlanGwVlanDns2Addr_Type()
)
tmnxWlanGwVlanDns2Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDns2Addr.setStatus("current")


class _TmnxWlanGwVlanNb1AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwVlanNb1AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwVlanNb1AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwVlanNb1AddrType_Object = MibTableColumn
tmnxWlanGwVlanNb1AddrType = _TmnxWlanGwVlanNb1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 15),
    _TmnxWlanGwVlanNb1AddrType_Type()
)
tmnxWlanGwVlanNb1AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanNb1AddrType.setStatus("current")


class _TmnxWlanGwVlanNb1Addr_Type(InetAddress):
    """Custom type tmnxWlanGwVlanNb1Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwVlanNb1Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwVlanNb1Addr_Object = MibTableColumn
tmnxWlanGwVlanNb1Addr = _TmnxWlanGwVlanNb1Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 16),
    _TmnxWlanGwVlanNb1Addr_Type()
)
tmnxWlanGwVlanNb1Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanNb1Addr.setStatus("current")


class _TmnxWlanGwVlanNb2AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwVlanNb2AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwVlanNb2AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwVlanNb2AddrType_Object = MibTableColumn
tmnxWlanGwVlanNb2AddrType = _TmnxWlanGwVlanNb2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 17),
    _TmnxWlanGwVlanNb2AddrType_Type()
)
tmnxWlanGwVlanNb2AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanNb2AddrType.setStatus("current")


class _TmnxWlanGwVlanNb2Addr_Type(InetAddress):
    """Custom type tmnxWlanGwVlanNb2Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwVlanNb2Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwVlanNb2Addr_Object = MibTableColumn
tmnxWlanGwVlanNb2Addr = _TmnxWlanGwVlanNb2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 18),
    _TmnxWlanGwVlanNb2Addr_Type()
)
tmnxWlanGwVlanNb2Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanNb2Addr.setStatus("current")


class _TmnxWlanGwVlanHttpRdrPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanHttpRdrPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanHttpRdrPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanHttpRdrPlcy_Object = MibTableColumn
tmnxWlanGwVlanHttpRdrPlcy = _TmnxWlanGwVlanHttpRdrPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 21),
    _TmnxWlanGwVlanHttpRdrPlcy_Type()
)
tmnxWlanGwVlanHttpRdrPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanHttpRdrPlcy.setStatus("current")


class _TmnxWlanGwVlanNatPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanNatPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanNatPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanNatPlcy_Object = MibTableColumn
tmnxWlanGwVlanNatPlcy = _TmnxWlanGwVlanNatPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 22),
    _TmnxWlanGwVlanNatPlcy_Type()
)
tmnxWlanGwVlanNatPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanNatPlcy.setStatus("current")


class _TmnxWlanGwVlanDataTrigg_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanDataTrigg based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanDataTrigg_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanDataTrigg_Object = MibTableColumn
tmnxWlanGwVlanDataTrigg = _TmnxWlanGwVlanDataTrigg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 30),
    _TmnxWlanGwVlanDataTrigg_Type()
)
tmnxWlanGwVlanDataTrigg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDataTrigg.setStatus("current")


class _TmnxWlanGwVlanAuthPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanAuthPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanAuthPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanAuthPlcy_Object = MibTableColumn
tmnxWlanGwVlanAuthPlcy = _TmnxWlanGwVlanAuthPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 31),
    _TmnxWlanGwVlanAuthPlcy_Type()
)
tmnxWlanGwVlanAuthPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAuthPlcy.setStatus("current")


class _TmnxWlanGwVlanAuthHoldTime_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanAuthHoldTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TmnxWlanGwVlanAuthHoldTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanAuthHoldTime_Object = MibTableColumn
tmnxWlanGwVlanAuthHoldTime = _TmnxWlanGwVlanAuthHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 32),
    _TmnxWlanGwVlanAuthHoldTime_Type()
)
tmnxWlanGwVlanAuthHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAuthHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAuthHoldTime.setUnits("seconds")


class _TmnxWlanGwVlanRadProxVrtr_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxWlanGwVlanRadProxVrtr based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxWlanGwVlanRadProxVrtr_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxWlanGwVlanRadProxVrtr_Object = MibTableColumn
tmnxWlanGwVlanRadProxVrtr = _TmnxWlanGwVlanRadProxVrtr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 34),
    _TmnxWlanGwVlanRadProxVrtr_Type()
)
tmnxWlanGwVlanRadProxVrtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanRadProxVrtr.setStatus("current")


class _TmnxWlanGwVlanRadProxSrv_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanRadProxSrv based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanRadProxSrv_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanRadProxSrv_Object = MibTableColumn
tmnxWlanGwVlanRadProxSrv = _TmnxWlanGwVlanRadProxSrv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 35),
    _TmnxWlanGwVlanRadProxSrv_Type()
)
tmnxWlanGwVlanRadProxSrv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanRadProxSrv.setStatus("current")


class _TmnxWlanGwVlanRadProxMacFmt_Type(TmnxMacSpecification):
    """Custom type tmnxWlanGwVlanRadProxMacFmt based on TmnxMacSpecification"""
    defaultValue = OctetString("aa:")

    subtypeSpec = TmnxMacSpecification.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 7),
    )


_TmnxWlanGwVlanRadProxMacFmt_Type.__name__ = "TmnxMacSpecification"
_TmnxWlanGwVlanRadProxMacFmt_Object = MibTableColumn
tmnxWlanGwVlanRadProxMacFmt = _TmnxWlanGwVlanRadProxMacFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 36),
    _TmnxWlanGwVlanRadProxMacFmt_Type()
)
tmnxWlanGwVlanRadProxMacFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanRadProxMacFmt.setStatus("current")


class _TmnxWlanGwVlanSsidType_Type(TmnxWlanGwSsidType):
    """Custom type tmnxWlanGwVlanSsidType based on TmnxWlanGwSsidType"""
    defaultValue = 0


_TmnxWlanGwVlanSsidType_Type.__name__ = "TmnxWlanGwSsidType"
_TmnxWlanGwVlanSsidType_Object = MibTableColumn
tmnxWlanGwVlanSsidType = _TmnxWlanGwVlanSsidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 39),
    _TmnxWlanGwVlanSsidType_Type()
)
tmnxWlanGwVlanSsidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSsidType.setStatus("current")


class _TmnxWlanGwVlanAuthOnDhcp_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanAuthOnDhcp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanAuthOnDhcp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanAuthOnDhcp_Object = MibTableColumn
tmnxWlanGwVlanAuthOnDhcp = _TmnxWlanGwVlanAuthOnDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 40),
    _TmnxWlanGwVlanAuthOnDhcp_Type()
)
tmnxWlanGwVlanAuthOnDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAuthOnDhcp.setStatus("current")


class _TmnxWlanGwVlanL2Service_Type(TmnxServId):
    """Custom type tmnxWlanGwVlanL2Service based on TmnxServId"""
    defaultValue = 0


_TmnxWlanGwVlanL2Service_Type.__name__ = "TmnxServId"
_TmnxWlanGwVlanL2Service_Object = MibTableColumn
tmnxWlanGwVlanL2Service = _TmnxWlanGwVlanL2Service_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 41),
    _TmnxWlanGwVlanL2Service_Type()
)
tmnxWlanGwVlanL2Service.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanL2Service.setStatus("current")


class _TmnxWlanGwVlanL2AdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanL2AdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanL2AdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanL2AdminState_Object = MibTableColumn
tmnxWlanGwVlanL2AdminState = _TmnxWlanGwVlanL2AdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 42),
    _TmnxWlanGwVlanL2AdminState_Type()
)
tmnxWlanGwVlanL2AdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanL2AdminState.setStatus("current")


class _TmnxWlanGwVlanL2Description_Type(TItemDescription):
    """Custom type tmnxWlanGwVlanL2Description based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanL2Description_Type.__name__ = "TItemDescription"
_TmnxWlanGwVlanL2Description_Object = MibTableColumn
tmnxWlanGwVlanL2Description = _TmnxWlanGwVlanL2Description_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 43),
    _TmnxWlanGwVlanL2Description_Type()
)
tmnxWlanGwVlanL2Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanL2Description.setStatus("current")


class _TmnxWlanGwVlanIdleTimeoutAction_Type(TmnxWlanGwVlanIdleTimeoutAction):
    """Custom type tmnxWlanGwVlanIdleTimeoutAction based on TmnxWlanGwVlanIdleTimeoutAction"""
    defaultValue = 0


_TmnxWlanGwVlanIdleTimeoutAction_Type.__name__ = "TmnxWlanGwVlanIdleTimeoutAction"
_TmnxWlanGwVlanIdleTimeoutAction_Object = MibTableColumn
tmnxWlanGwVlanIdleTimeoutAction = _TmnxWlanGwVlanIdleTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 44),
    _TmnxWlanGwVlanIdleTimeoutAction_Type()
)
tmnxWlanGwVlanIdleTimeoutAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanIdleTimeoutAction.setStatus("current")


class _TmnxWlanGwVlanAddrFromPool_Type(TruthValue):
    """Custom type tmnxWlanGwVlanAddrFromPool based on TruthValue"""
    defaultValue = 2


_TmnxWlanGwVlanAddrFromPool_Type.__name__ = "TruthValue"
_TmnxWlanGwVlanAddrFromPool_Object = MibTableColumn
tmnxWlanGwVlanAddrFromPool = _TmnxWlanGwVlanAddrFromPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 45),
    _TmnxWlanGwVlanAddrFromPool_Type()
)
tmnxWlanGwVlanAddrFromPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAddrFromPool.setStatus("current")


class _TmnxWlanGwVlanAuthVlanMismatchTo_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanAuthVlanMismatchTo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 60),
    )


_TmnxWlanGwVlanAuthVlanMismatchTo_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanAuthVlanMismatchTo_Object = MibTableColumn
tmnxWlanGwVlanAuthVlanMismatchTo = _TmnxWlanGwVlanAuthVlanMismatchTo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 46),
    _TmnxWlanGwVlanAuthVlanMismatchTo_Type()
)
tmnxWlanGwVlanAuthVlanMismatchTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAuthVlanMismatchTo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAuthVlanMismatchTo.setUnits("seconds")
_TmnxWlanGwSubIfTable_Object = MibTable
tmnxWlanGwSubIfTable = _TmnxWlanGwSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfTable.setStatus("current")
_TmnxWlanGwSubIfEntry_Object = MibTableRow
tmnxWlanGwSubIfEntry = _TmnxWlanGwSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1)
)
tmnxWlanGwSubIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfEntry.setStatus("current")
_TmnxWlanGwSubIfRowStatus_Type = RowStatus
_TmnxWlanGwSubIfRowStatus_Object = MibTableColumn
tmnxWlanGwSubIfRowStatus = _TmnxWlanGwSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 1),
    _TmnxWlanGwSubIfRowStatus_Type()
)
tmnxWlanGwSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRowStatus.setStatus("current")
_TmnxWlanGwSubIfLastCh_Type = TimeStamp
_TmnxWlanGwSubIfLastCh_Object = MibTableColumn
tmnxWlanGwSubIfLastCh = _TmnxWlanGwSubIfLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 2),
    _TmnxWlanGwSubIfLastCh_Type()
)
tmnxWlanGwSubIfLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfLastCh.setStatus("current")


class _TmnxWlanGwSubIfRedExpPrefixType_Type(InetAddressType):
    """Custom type tmnxWlanGwSubIfRedExpPrefixType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSubIfRedExpPrefixType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSubIfRedExpPrefixType_Object = MibTableColumn
tmnxWlanGwSubIfRedExpPrefixType = _TmnxWlanGwSubIfRedExpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 3),
    _TmnxWlanGwSubIfRedExpPrefixType_Type()
)
tmnxWlanGwSubIfRedExpPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedExpPrefixType.setStatus("current")


class _TmnxWlanGwSubIfRedExpPrefix_Type(InetAddress):
    """Custom type tmnxWlanGwSubIfRedExpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSubIfRedExpPrefix_Type.__name__ = "InetAddress"
_TmnxWlanGwSubIfRedExpPrefix_Object = MibTableColumn
tmnxWlanGwSubIfRedExpPrefix = _TmnxWlanGwSubIfRedExpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 4),
    _TmnxWlanGwSubIfRedExpPrefix_Type()
)
tmnxWlanGwSubIfRedExpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedExpPrefix.setStatus("current")


class _TmnxWlanGwSubIfRedExpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxWlanGwSubIfRedExpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxWlanGwSubIfRedExpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxWlanGwSubIfRedExpPrefixLen_Object = MibTableColumn
tmnxWlanGwSubIfRedExpPrefixLen = _TmnxWlanGwSubIfRedExpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 5),
    _TmnxWlanGwSubIfRedExpPrefixLen_Type()
)
tmnxWlanGwSubIfRedExpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedExpPrefixLen.setStatus("current")


class _TmnxWlanGwSubIfRedMonPrefixType_Type(InetAddressType):
    """Custom type tmnxWlanGwSubIfRedMonPrefixType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSubIfRedMonPrefixType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSubIfRedMonPrefixType_Object = MibTableColumn
tmnxWlanGwSubIfRedMonPrefixType = _TmnxWlanGwSubIfRedMonPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 6),
    _TmnxWlanGwSubIfRedMonPrefixType_Type()
)
tmnxWlanGwSubIfRedMonPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedMonPrefixType.setStatus("current")


class _TmnxWlanGwSubIfRedMonPrefix_Type(InetAddress):
    """Custom type tmnxWlanGwSubIfRedMonPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSubIfRedMonPrefix_Type.__name__ = "InetAddress"
_TmnxWlanGwSubIfRedMonPrefix_Object = MibTableColumn
tmnxWlanGwSubIfRedMonPrefix = _TmnxWlanGwSubIfRedMonPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 7),
    _TmnxWlanGwSubIfRedMonPrefix_Type()
)
tmnxWlanGwSubIfRedMonPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedMonPrefix.setStatus("current")


class _TmnxWlanGwSubIfRedMonPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxWlanGwSubIfRedMonPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxWlanGwSubIfRedMonPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxWlanGwSubIfRedMonPrefixLen_Object = MibTableColumn
tmnxWlanGwSubIfRedMonPrefixLen = _TmnxWlanGwSubIfRedMonPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 8),
    _TmnxWlanGwSubIfRedMonPrefixLen_Type()
)
tmnxWlanGwSubIfRedMonPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedMonPrefixLen.setStatus("current")


class _TmnxWlanGwSubIfRedAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwSubIfRedAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwSubIfRedAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwSubIfRedAdminState_Object = MibTableColumn
tmnxWlanGwSubIfRedAdminState = _TmnxWlanGwSubIfRedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 9),
    _TmnxWlanGwSubIfRedAdminState_Type()
)
tmnxWlanGwSubIfRedAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedAdminState.setStatus("current")
_TmnxWlanGwSubIfRedActive_Type = TruthValue
_TmnxWlanGwSubIfRedActive_Object = MibTableColumn
tmnxWlanGwSubIfRedActive = _TmnxWlanGwSubIfRedActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 10),
    _TmnxWlanGwSubIfRedActive_Type()
)
tmnxWlanGwSubIfRedActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedActive.setStatus("current")


class _TmnxWlanGwSubIfRedSwitch_Type(TmnxActionType):
    """Custom type tmnxWlanGwSubIfRedSwitch based on TmnxActionType"""
    defaultValue = 2


_TmnxWlanGwSubIfRedSwitch_Type.__name__ = "TmnxActionType"
_TmnxWlanGwSubIfRedSwitch_Object = MibTableColumn
tmnxWlanGwSubIfRedSwitch = _TmnxWlanGwSubIfRedSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 11),
    _TmnxWlanGwSubIfRedSwitch_Type()
)
tmnxWlanGwSubIfRedSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedSwitch.setStatus("current")
_TmnxWlanGwL2ApTable_Object = MibTable
tmnxWlanGwL2ApTable = _TmnxWlanGwL2ApTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxWlanGwL2ApTable.setStatus("current")
_TmnxWlanGwL2ApEntry_Object = MibTableRow
tmnxWlanGwL2ApEntry = _TmnxWlanGwL2ApEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 8, 1)
)
tmnxWlanGwL2ApEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwL2ApEntry.setStatus("current")
_TmnxWlanGwL2ApRowStatus_Type = RowStatus
_TmnxWlanGwL2ApRowStatus_Object = MibTableColumn
tmnxWlanGwL2ApRowStatus = _TmnxWlanGwL2ApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 8, 1, 1),
    _TmnxWlanGwL2ApRowStatus_Type()
)
tmnxWlanGwL2ApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwL2ApRowStatus.setStatus("current")
_TmnxWlanGwL2ApLastCh_Type = TimeStamp
_TmnxWlanGwL2ApLastCh_Object = MibTableColumn
tmnxWlanGwL2ApLastCh = _TmnxWlanGwL2ApLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 8, 1, 2),
    _TmnxWlanGwL2ApLastCh_Type()
)
tmnxWlanGwL2ApLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwL2ApLastCh.setStatus("current")


class _TmnxWlanGwL2ApAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwL2ApAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwL2ApAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwL2ApAdminState_Object = MibTableColumn
tmnxWlanGwL2ApAdminState = _TmnxWlanGwL2ApAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 8, 1, 3),
    _TmnxWlanGwL2ApAdminState_Type()
)
tmnxWlanGwL2ApAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwL2ApAdminState.setStatus("current")


class _TmnxWlanGwL2ApEncapType_Type(Integer32):
    """Custom type tmnxWlanGwL2ApEncapType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("null", 1),
          ("dot1q", 2),
          ("qinq", 10))
    )


_TmnxWlanGwL2ApEncapType_Type.__name__ = "Integer32"
_TmnxWlanGwL2ApEncapType_Object = MibTableColumn
tmnxWlanGwL2ApEncapType = _TmnxWlanGwL2ApEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 8, 1, 4),
    _TmnxWlanGwL2ApEncapType_Type()
)
tmnxWlanGwL2ApEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwL2ApEncapType.setStatus("current")


class _TmnxWlanGwL2ApEpipeSapTemplate_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwL2ApEpipeSapTemplate based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwL2ApEpipeSapTemplate_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwL2ApEpipeSapTemplate_Object = MibTableColumn
tmnxWlanGwL2ApEpipeSapTemplate = _TmnxWlanGwL2ApEpipeSapTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 8, 1, 5),
    _TmnxWlanGwL2ApEpipeSapTemplate_Type()
)
tmnxWlanGwL2ApEpipeSapTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwL2ApEpipeSapTemplate.setStatus("current")
_TmnxWlanGwL2ApId_Type = Unsigned32
_TmnxWlanGwL2ApId_Object = MibTableColumn
tmnxWlanGwL2ApId = _TmnxWlanGwL2ApId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 8, 1, 6),
    _TmnxWlanGwL2ApId_Type()
)
tmnxWlanGwL2ApId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwL2ApId.setStatus("current")
_TmnxWlanGwSubIfPmTable_Object = MibTable
tmnxWlanGwSubIfPmTable = _TmnxWlanGwSubIfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmTable.setStatus("current")
_TmnxWlanGwSubIfPmEntry_Object = MibTableRow
tmnxWlanGwSubIfPmEntry = _TmnxWlanGwSubIfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmEntry.setStatus("current")
_TmnxWlanGwSubIfPmLastChanged_Type = TimeStamp
_TmnxWlanGwSubIfPmLastChanged_Object = MibTableColumn
tmnxWlanGwSubIfPmLastChanged = _TmnxWlanGwSubIfPmLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 1),
    _TmnxWlanGwSubIfPmLastChanged_Type()
)
tmnxWlanGwSubIfPmLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmLastChanged.setStatus("current")


class _TmnxWlanGwSubIfPmWatermarkHigh_Type(Unsigned32):
    """Custom type tmnxWlanGwSubIfPmWatermarkHigh based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(51, 99),
    )


_TmnxWlanGwSubIfPmWatermarkHigh_Type.__name__ = "Unsigned32"
_TmnxWlanGwSubIfPmWatermarkHigh_Object = MibTableColumn
tmnxWlanGwSubIfPmWatermarkHigh = _TmnxWlanGwSubIfPmWatermarkHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 2),
    _TmnxWlanGwSubIfPmWatermarkHigh_Type()
)
tmnxWlanGwSubIfPmWatermarkHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmWatermarkHigh.setStatus("current")


class _TmnxWlanGwSubIfPmWatermarkLow_Type(Unsigned32):
    """Custom type tmnxWlanGwSubIfPmWatermarkLow based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 98),
    )


_TmnxWlanGwSubIfPmWatermarkLow_Type.__name__ = "Unsigned32"
_TmnxWlanGwSubIfPmWatermarkLow_Object = MibTableColumn
tmnxWlanGwSubIfPmWatermarkLow = _TmnxWlanGwSubIfPmWatermarkLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 3),
    _TmnxWlanGwSubIfPmWatermarkLow_Type()
)
tmnxWlanGwSubIfPmWatermarkLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmWatermarkLow.setStatus("current")


class _TmnxWlanGwSubIfPmWlanGwGroup_Type(TmnxWlanGwIsaGrpIdOrZero):
    """Custom type tmnxWlanGwSubIfPmWlanGwGroup based on TmnxWlanGwIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxWlanGwSubIfPmWlanGwGroup_Type.__name__ = "TmnxWlanGwIsaGrpIdOrZero"
_TmnxWlanGwSubIfPmWlanGwGroup_Object = MibTableColumn
tmnxWlanGwSubIfPmWlanGwGroup = _TmnxWlanGwSubIfPmWlanGwGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 4),
    _TmnxWlanGwSubIfPmWlanGwGroup_Type()
)
tmnxWlanGwSubIfPmWlanGwGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmWlanGwGroup.setStatus("current")


class _TmnxWlanGwSubIfPmD6cServer1_Type(InetAddressIPv6):
    """Custom type tmnxWlanGwSubIfPmD6cServer1 based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxWlanGwSubIfPmD6cServer1_Type.__name__ = "InetAddressIPv6"
_TmnxWlanGwSubIfPmD6cServer1_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cServer1 = _TmnxWlanGwSubIfPmD6cServer1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 5),
    _TmnxWlanGwSubIfPmD6cServer1_Type()
)
tmnxWlanGwSubIfPmD6cServer1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cServer1.setStatus("current")


class _TmnxWlanGwSubIfPmD6cServer2_Type(InetAddressIPv6):
    """Custom type tmnxWlanGwSubIfPmD6cServer2 based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxWlanGwSubIfPmD6cServer2_Type.__name__ = "InetAddressIPv6"
_TmnxWlanGwSubIfPmD6cServer2_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cServer2 = _TmnxWlanGwSubIfPmD6cServer2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 6),
    _TmnxWlanGwSubIfPmD6cServer2_Type()
)
tmnxWlanGwSubIfPmD6cServer2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cServer2.setStatus("current")


class _TmnxWlanGwSubIfPmD6cServer3_Type(InetAddressIPv6):
    """Custom type tmnxWlanGwSubIfPmD6cServer3 based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxWlanGwSubIfPmD6cServer3_Type.__name__ = "InetAddressIPv6"
_TmnxWlanGwSubIfPmD6cServer3_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cServer3 = _TmnxWlanGwSubIfPmD6cServer3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 7),
    _TmnxWlanGwSubIfPmD6cServer3_Type()
)
tmnxWlanGwSubIfPmD6cServer3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cServer3.setStatus("current")


class _TmnxWlanGwSubIfPmD6cServer4_Type(InetAddressIPv6):
    """Custom type tmnxWlanGwSubIfPmD6cServer4 based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxWlanGwSubIfPmD6cServer4_Type.__name__ = "InetAddressIPv6"
_TmnxWlanGwSubIfPmD6cServer4_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cServer4 = _TmnxWlanGwSubIfPmD6cServer4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 8),
    _TmnxWlanGwSubIfPmD6cServer4_Type()
)
tmnxWlanGwSubIfPmD6cServer4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cServer4.setStatus("current")


class _TmnxWlanGwSubIfPmD6cServer5_Type(InetAddressIPv6):
    """Custom type tmnxWlanGwSubIfPmD6cServer5 based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxWlanGwSubIfPmD6cServer5_Type.__name__ = "InetAddressIPv6"
_TmnxWlanGwSubIfPmD6cServer5_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cServer5 = _TmnxWlanGwSubIfPmD6cServer5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 9),
    _TmnxWlanGwSubIfPmD6cServer5_Type()
)
tmnxWlanGwSubIfPmD6cServer5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cServer5.setStatus("current")


class _TmnxWlanGwSubIfPmD6cServer6_Type(InetAddressIPv6):
    """Custom type tmnxWlanGwSubIfPmD6cServer6 based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxWlanGwSubIfPmD6cServer6_Type.__name__ = "InetAddressIPv6"
_TmnxWlanGwSubIfPmD6cServer6_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cServer6 = _TmnxWlanGwSubIfPmD6cServer6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 10),
    _TmnxWlanGwSubIfPmD6cServer6_Type()
)
tmnxWlanGwSubIfPmD6cServer6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cServer6.setStatus("current")


class _TmnxWlanGwSubIfPmD6cServer7_Type(InetAddressIPv6):
    """Custom type tmnxWlanGwSubIfPmD6cServer7 based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxWlanGwSubIfPmD6cServer7_Type.__name__ = "InetAddressIPv6"
_TmnxWlanGwSubIfPmD6cServer7_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cServer7 = _TmnxWlanGwSubIfPmD6cServer7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 11),
    _TmnxWlanGwSubIfPmD6cServer7_Type()
)
tmnxWlanGwSubIfPmD6cServer7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cServer7.setStatus("current")


class _TmnxWlanGwSubIfPmD6cServer8_Type(InetAddressIPv6):
    """Custom type tmnxWlanGwSubIfPmD6cServer8 based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxWlanGwSubIfPmD6cServer8_Type.__name__ = "InetAddressIPv6"
_TmnxWlanGwSubIfPmD6cServer8_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cServer8 = _TmnxWlanGwSubIfPmD6cServer8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 12),
    _TmnxWlanGwSubIfPmD6cServer8_Type()
)
tmnxWlanGwSubIfPmD6cServer8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cServer8.setStatus("current")


class _TmnxWlanGwSubIfPmD6cLeaseQuery_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwSubIfPmD6cLeaseQuery based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwSubIfPmD6cLeaseQuery_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwSubIfPmD6cLeaseQuery_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cLeaseQuery = _TmnxWlanGwSubIfPmD6cLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 13),
    _TmnxWlanGwSubIfPmD6cLeaseQuery_Type()
)
tmnxWlanGwSubIfPmD6cLeaseQuery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cLeaseQuery.setStatus("current")


class _TmnxWlanGwSubIfPmD6cLeaseQueryMR_Type(Unsigned32):
    """Custom type tmnxWlanGwSubIfPmD6cLeaseQueryMR based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxWlanGwSubIfPmD6cLeaseQueryMR_Type.__name__ = "Unsigned32"
_TmnxWlanGwSubIfPmD6cLeaseQueryMR_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cLeaseQueryMR = _TmnxWlanGwSubIfPmD6cLeaseQueryMR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 14),
    _TmnxWlanGwSubIfPmD6cLeaseQueryMR_Type()
)
tmnxWlanGwSubIfPmD6cLeaseQueryMR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cLeaseQueryMR.setStatus("current")


class _TmnxWlanGwSubIfPmD6cSourceIp_Type(InetAddressIPv6):
    """Custom type tmnxWlanGwSubIfPmD6cSourceIp based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxWlanGwSubIfPmD6cSourceIp_Type.__name__ = "InetAddressIPv6"
_TmnxWlanGwSubIfPmD6cSourceIp_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cSourceIp = _TmnxWlanGwSubIfPmD6cSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 15),
    _TmnxWlanGwSubIfPmD6cSourceIp_Type()
)
tmnxWlanGwSubIfPmD6cSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cSourceIp.setStatus("current")


class _TmnxWlanGwSubIfPmD6cSlaacPoolNm_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSubIfPmD6cSlaacPoolNm based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSubIfPmD6cSlaacPoolNm_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSubIfPmD6cSlaacPoolNm_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cSlaacPoolNm = _TmnxWlanGwSubIfPmD6cSlaacPoolNm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 16),
    _TmnxWlanGwSubIfPmD6cSlaacPoolNm_Type()
)
tmnxWlanGwSubIfPmD6cSlaacPoolNm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cSlaacPoolNm.setStatus("current")


class _TmnxWlanGwSubIfPmD6cSlaacLinkAdd_Type(InetAddressIPv6):
    """Custom type tmnxWlanGwSubIfPmD6cSlaacLinkAdd based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxWlanGwSubIfPmD6cSlaacLinkAdd_Type.__name__ = "InetAddressIPv6"
_TmnxWlanGwSubIfPmD6cSlaacLinkAdd_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cSlaacLinkAdd = _TmnxWlanGwSubIfPmD6cSlaacLinkAdd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 17),
    _TmnxWlanGwSubIfPmD6cSlaacLinkAdd_Type()
)
tmnxWlanGwSubIfPmD6cSlaacLinkAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cSlaacLinkAdd.setStatus("current")


class _TmnxWlanGwSubIfPmD6cSlaacAdminSt_Type(TmnxAdminState):
    """Custom type tmnxWlanGwSubIfPmD6cSlaacAdminSt based on TmnxAdminState"""
    defaultValue = 3


_TmnxWlanGwSubIfPmD6cSlaacAdminSt_Type.__name__ = "TmnxAdminState"
_TmnxWlanGwSubIfPmD6cSlaacAdminSt_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cSlaacAdminSt = _TmnxWlanGwSubIfPmD6cSlaacAdminSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 18),
    _TmnxWlanGwSubIfPmD6cSlaacAdminSt_Type()
)
tmnxWlanGwSubIfPmD6cSlaacAdminSt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cSlaacAdminSt.setStatus("current")


class _TmnxWlanGwSubIfPmD6cIaNaPoolNm_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSubIfPmD6cIaNaPoolNm based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSubIfPmD6cIaNaPoolNm_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSubIfPmD6cIaNaPoolNm_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cIaNaPoolNm = _TmnxWlanGwSubIfPmD6cIaNaPoolNm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 19),
    _TmnxWlanGwSubIfPmD6cIaNaPoolNm_Type()
)
tmnxWlanGwSubIfPmD6cIaNaPoolNm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cIaNaPoolNm.setStatus("current")


class _TmnxWlanGwSubIfPmD6cIaNaLinkAdd_Type(InetAddressIPv6):
    """Custom type tmnxWlanGwSubIfPmD6cIaNaLinkAdd based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxWlanGwSubIfPmD6cIaNaLinkAdd_Type.__name__ = "InetAddressIPv6"
_TmnxWlanGwSubIfPmD6cIaNaLinkAdd_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cIaNaLinkAdd = _TmnxWlanGwSubIfPmD6cIaNaLinkAdd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 20),
    _TmnxWlanGwSubIfPmD6cIaNaLinkAdd_Type()
)
tmnxWlanGwSubIfPmD6cIaNaLinkAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cIaNaLinkAdd.setStatus("current")


class _TmnxWlanGwSubIfPmD6cIaNaAdminSt_Type(TmnxAdminState):
    """Custom type tmnxWlanGwSubIfPmD6cIaNaAdminSt based on TmnxAdminState"""
    defaultValue = 3


_TmnxWlanGwSubIfPmD6cIaNaAdminSt_Type.__name__ = "TmnxAdminState"
_TmnxWlanGwSubIfPmD6cIaNaAdminSt_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cIaNaAdminSt = _TmnxWlanGwSubIfPmD6cIaNaAdminSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 21),
    _TmnxWlanGwSubIfPmD6cIaNaAdminSt_Type()
)
tmnxWlanGwSubIfPmD6cIaNaAdminSt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cIaNaAdminSt.setStatus("current")


class _TmnxWlanGwSubIfPmD6cD4natPoolNm_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSubIfPmD6cD4natPoolNm based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSubIfPmD6cD4natPoolNm_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSubIfPmD6cD4natPoolNm_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cD4natPoolNm = _TmnxWlanGwSubIfPmD6cD4natPoolNm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 22),
    _TmnxWlanGwSubIfPmD6cD4natPoolNm_Type()
)
tmnxWlanGwSubIfPmD6cD4natPoolNm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cD4natPoolNm.setStatus("current")


class _TmnxWlanGwSubIfPmD6cD4natLinkAdd_Type(InetAddressIPv6):
    """Custom type tmnxWlanGwSubIfPmD6cD4natLinkAdd based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxWlanGwSubIfPmD6cD4natLinkAdd_Type.__name__ = "InetAddressIPv6"
_TmnxWlanGwSubIfPmD6cD4natLinkAdd_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cD4natLinkAdd = _TmnxWlanGwSubIfPmD6cD4natLinkAdd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 23),
    _TmnxWlanGwSubIfPmD6cD4natLinkAdd_Type()
)
tmnxWlanGwSubIfPmD6cD4natLinkAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cD4natLinkAdd.setStatus("current")


class _TmnxWlanGwSubIfPmD6cD4natAdminSt_Type(TmnxAdminState):
    """Custom type tmnxWlanGwSubIfPmD6cD4natAdminSt based on TmnxAdminState"""
    defaultValue = 3


_TmnxWlanGwSubIfPmD6cD4natAdminSt_Type.__name__ = "TmnxAdminState"
_TmnxWlanGwSubIfPmD6cD4natAdminSt_Object = MibTableColumn
tmnxWlanGwSubIfPmD6cD4natAdminSt = _TmnxWlanGwSubIfPmD6cD4natAdminSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 9, 1, 24),
    _TmnxWlanGwSubIfPmD6cD4natAdminSt_Type()
)
tmnxWlanGwSubIfPmD6cD4natAdminSt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmD6cD4natAdminSt.setStatus("current")
_TmnxWlanGwSubIfIpsTable_Object = MibTable
tmnxWlanGwSubIfIpsTable = _TmnxWlanGwSubIfIpsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsTable.setStatus("current")
_TmnxWlanGwSubIfIpsEntry_Object = MibTableRow
tmnxWlanGwSubIfIpsEntry = _TmnxWlanGwSubIfIpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1)
)
tmnxWlanGwSubIfIpsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsSubnetAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsSubnetAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsSubnetPrefLen"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsEntry.setStatus("current")
_TmnxWlanGwSubIfIpsSubIfIndex_Type = InterfaceIndex
_TmnxWlanGwSubIfIpsSubIfIndex_Object = MibTableColumn
tmnxWlanGwSubIfIpsSubIfIndex = _TmnxWlanGwSubIfIpsSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 1),
    _TmnxWlanGwSubIfIpsSubIfIndex_Type()
)
tmnxWlanGwSubIfIpsSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsSubIfIndex.setStatus("current")
_TmnxWlanGwSubIfIpsSubnetAddrType_Type = InetAddressType
_TmnxWlanGwSubIfIpsSubnetAddrType_Object = MibTableColumn
tmnxWlanGwSubIfIpsSubnetAddrType = _TmnxWlanGwSubIfIpsSubnetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 2),
    _TmnxWlanGwSubIfIpsSubnetAddrType_Type()
)
tmnxWlanGwSubIfIpsSubnetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsSubnetAddrType.setStatus("current")


class _TmnxWlanGwSubIfIpsSubnetAddr_Type(InetAddress):
    """Custom type tmnxWlanGwSubIfIpsSubnetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSubIfIpsSubnetAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwSubIfIpsSubnetAddr_Object = MibTableColumn
tmnxWlanGwSubIfIpsSubnetAddr = _TmnxWlanGwSubIfIpsSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 3),
    _TmnxWlanGwSubIfIpsSubnetAddr_Type()
)
tmnxWlanGwSubIfIpsSubnetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsSubnetAddr.setStatus("current")
_TmnxWlanGwSubIfIpsSubnetPrefLen_Type = InetAddressPrefixLength
_TmnxWlanGwSubIfIpsSubnetPrefLen_Object = MibTableColumn
tmnxWlanGwSubIfIpsSubnetPrefLen = _TmnxWlanGwSubIfIpsSubnetPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 4),
    _TmnxWlanGwSubIfIpsSubnetPrefLen_Type()
)
tmnxWlanGwSubIfIpsSubnetPrefLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsSubnetPrefLen.setStatus("current")
_TmnxWlanGwSubIfIpsAddrFamily_Type = TmnxWlanGwSubIfIpsAddrFamily
_TmnxWlanGwSubIfIpsAddrFamily_Object = MibTableColumn
tmnxWlanGwSubIfIpsAddrFamily = _TmnxWlanGwSubIfIpsAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 5),
    _TmnxWlanGwSubIfIpsAddrFamily_Type()
)
tmnxWlanGwSubIfIpsAddrFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsAddrFamily.setStatus("current")


class _TmnxWlanGwSubIfIpsPoolIsOld_Type(TruthValue):
    """Custom type tmnxWlanGwSubIfIpsPoolIsOld based on TruthValue"""
    defaultValue = 2


_TmnxWlanGwSubIfIpsPoolIsOld_Type.__name__ = "TruthValue"
_TmnxWlanGwSubIfIpsPoolIsOld_Object = MibTableColumn
tmnxWlanGwSubIfIpsPoolIsOld = _TmnxWlanGwSubIfIpsPoolIsOld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 6),
    _TmnxWlanGwSubIfIpsPoolIsOld_Type()
)
tmnxWlanGwSubIfIpsPoolIsOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsPoolIsOld.setStatus("current")


class _TmnxWlanGwSubIfIpsUsageLevelPct_Type(Unsigned32):
    """Custom type tmnxWlanGwSubIfIpsUsageLevelPct based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxWlanGwSubIfIpsUsageLevelPct_Type.__name__ = "Unsigned32"
_TmnxWlanGwSubIfIpsUsageLevelPct_Object = MibTableColumn
tmnxWlanGwSubIfIpsUsageLevelPct = _TmnxWlanGwSubIfIpsUsageLevelPct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 7),
    _TmnxWlanGwSubIfIpsUsageLevelPct_Type()
)
tmnxWlanGwSubIfIpsUsageLevelPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsUsageLevelPct.setStatus("current")


class _TmnxWlanGwSubIfIpsDHCPv6Options_Type(OctetString):
    """Custom type tmnxWlanGwSubIfIpsDHCPv6Options based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_TmnxWlanGwSubIfIpsDHCPv6Options_Type.__name__ = "OctetString"
_TmnxWlanGwSubIfIpsDHCPv6Options_Object = MibTableColumn
tmnxWlanGwSubIfIpsDHCPv6Options = _TmnxWlanGwSubIfIpsDHCPv6Options_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 8),
    _TmnxWlanGwSubIfIpsDHCPv6Options_Type()
)
tmnxWlanGwSubIfIpsDHCPv6Options.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsDHCPv6Options.setStatus("current")


class _TmnxWlanGwSubIfIpsRemLeaseTime_Type(Unsigned32):
    """Custom type tmnxWlanGwSubIfIpsRemLeaseTime based on Unsigned32"""
    defaultValue = 0


_TmnxWlanGwSubIfIpsRemLeaseTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwSubIfIpsRemLeaseTime_Object = MibTableColumn
tmnxWlanGwSubIfIpsRemLeaseTime = _TmnxWlanGwSubIfIpsRemLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 9),
    _TmnxWlanGwSubIfIpsRemLeaseTime_Type()
)
tmnxWlanGwSubIfIpsRemLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsRemLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsRemLeaseTime.setUnits("seconds")
_TmnxWlanGwSubIfIpsIsaGrpId_Type = TmnxWlanGwIsaGrpIdOrZero
_TmnxWlanGwSubIfIpsIsaGrpId_Object = MibTableColumn
tmnxWlanGwSubIfIpsIsaGrpId = _TmnxWlanGwSubIfIpsIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 10),
    _TmnxWlanGwSubIfIpsIsaGrpId_Type()
)
tmnxWlanGwSubIfIpsIsaGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsIsaGrpId.setStatus("current")
_TmnxWlanGwSubIfIpsIsaMemberId_Type = Unsigned32
_TmnxWlanGwSubIfIpsIsaMemberId_Object = MibTableColumn
tmnxWlanGwSubIfIpsIsaMemberId = _TmnxWlanGwSubIfIpsIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 11),
    _TmnxWlanGwSubIfIpsIsaMemberId_Type()
)
tmnxWlanGwSubIfIpsIsaMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsIsaMemberId.setStatus("current")
_TmnxWlanGwSubIfIpsServiceId_Type = TmnxServId
_TmnxWlanGwSubIfIpsServiceId_Object = MibTableColumn
tmnxWlanGwSubIfIpsServiceId = _TmnxWlanGwSubIfIpsServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 12),
    _TmnxWlanGwSubIfIpsServiceId_Type()
)
tmnxWlanGwSubIfIpsServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsServiceId.setStatus("current")
_TmnxWlanGwSubIfIpsIpv4Addr_Type = InetAddressIPv4
_TmnxWlanGwSubIfIpsIpv4Addr_Object = MibTableColumn
tmnxWlanGwSubIfIpsIpv4Addr = _TmnxWlanGwSubIfIpsIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 13),
    _TmnxWlanGwSubIfIpsIpv4Addr_Type()
)
tmnxWlanGwSubIfIpsIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsIpv4Addr.setStatus("current")
_TmnxWlanGwSubIfIpsIpv4PrefLen_Type = InetAddressPrefixLength
_TmnxWlanGwSubIfIpsIpv4PrefLen_Object = MibTableColumn
tmnxWlanGwSubIfIpsIpv4PrefLen = _TmnxWlanGwSubIfIpsIpv4PrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 14),
    _TmnxWlanGwSubIfIpsIpv4PrefLen_Type()
)
tmnxWlanGwSubIfIpsIpv4PrefLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsIpv4PrefLen.setStatus("current")
_TmnxWlanGwSubIfIpsIpv4DefGwAddr_Type = InetAddressIPv4
_TmnxWlanGwSubIfIpsIpv4DefGwAddr_Object = MibTableColumn
tmnxWlanGwSubIfIpsIpv4DefGwAddr = _TmnxWlanGwSubIfIpsIpv4DefGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 15),
    _TmnxWlanGwSubIfIpsIpv4DefGwAddr_Type()
)
tmnxWlanGwSubIfIpsIpv4DefGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsIpv4DefGwAddr.setStatus("current")
_TmnxWlanGwSubIfIpsDnsServer1_Type = InetAddressIPv6
_TmnxWlanGwSubIfIpsDnsServer1_Object = MibTableColumn
tmnxWlanGwSubIfIpsDnsServer1 = _TmnxWlanGwSubIfIpsDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 16),
    _TmnxWlanGwSubIfIpsDnsServer1_Type()
)
tmnxWlanGwSubIfIpsDnsServer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsDnsServer1.setStatus("current")
_TmnxWlanGwSubIfIpsDnsServer2_Type = InetAddressIPv6
_TmnxWlanGwSubIfIpsDnsServer2_Object = MibTableColumn
tmnxWlanGwSubIfIpsDnsServer2 = _TmnxWlanGwSubIfIpsDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 10, 1, 17),
    _TmnxWlanGwSubIfIpsDnsServer2_Type()
)
tmnxWlanGwSubIfIpsDnsServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfIpsDnsServer2.setStatus("current")
_TmnxWlanGwTuQosOvrTable_Object = MibTable
tmnxWlanGwTuQosOvrTable = _TmnxWlanGwTuQosOvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 11)
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosOvrTable.setStatus("current")
_TmnxWlanGwTuQosOvrEntry_Object = MibTableRow
tmnxWlanGwTuQosOvrEntry = _TmnxWlanGwTuQosOvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 11, 1)
)
tmnxWlanGwTuQosOvrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddrTyp"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosRetailService"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosOvrDirection"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosOvrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosOvrTypeName"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosOvrEntry.setStatus("current")
_TmnxWlanGwTuQosOvrDirection_Type = TDirectionIngEgr
_TmnxWlanGwTuQosOvrDirection_Object = MibTableColumn
tmnxWlanGwTuQosOvrDirection = _TmnxWlanGwTuQosOvrDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 11, 1, 1),
    _TmnxWlanGwTuQosOvrDirection_Type()
)
tmnxWlanGwTuQosOvrDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosOvrDirection.setStatus("current")
_TmnxWlanGwTuQosOvrType_Type = TQosOverrideType
_TmnxWlanGwTuQosOvrType_Object = MibTableColumn
tmnxWlanGwTuQosOvrType = _TmnxWlanGwTuQosOvrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 11, 1, 2),
    _TmnxWlanGwTuQosOvrType_Type()
)
tmnxWlanGwTuQosOvrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosOvrType.setStatus("current")
_TmnxWlanGwTuQosOvrTypeName_Type = TNamedItemOrEmpty
_TmnxWlanGwTuQosOvrTypeName_Object = MibTableColumn
tmnxWlanGwTuQosOvrTypeName = _TmnxWlanGwTuQosOvrTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 11, 1, 3),
    _TmnxWlanGwTuQosOvrTypeName_Type()
)
tmnxWlanGwTuQosOvrTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosOvrTypeName.setStatus("current")
_TmnxWlanGwTuQosOvrPIR_Type = TQosQueuePIRRateOverride
_TmnxWlanGwTuQosOvrPIR_Object = MibTableColumn
tmnxWlanGwTuQosOvrPIR = _TmnxWlanGwTuQosOvrPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 11, 1, 4),
    _TmnxWlanGwTuQosOvrPIR_Type()
)
tmnxWlanGwTuQosOvrPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosOvrPIR.setStatus("current")
_TmnxWlanGwTuQosOvrCIR_Type = TQosQueueCIRRateOverride
_TmnxWlanGwTuQosOvrCIR_Object = MibTableColumn
tmnxWlanGwTuQosOvrCIR = _TmnxWlanGwTuQosOvrCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 11, 1, 5),
    _TmnxWlanGwTuQosOvrCIR_Type()
)
tmnxWlanGwTuQosOvrCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosOvrCIR.setStatus("current")
_TmnxWlanGwTuQosOvrAggRateLimit_Type = TQosQueuePIRRateOverride
_TmnxWlanGwTuQosOvrAggRateLimit_Object = MibTableColumn
tmnxWlanGwTuQosOvrAggRateLimit = _TmnxWlanGwTuQosOvrAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 11, 1, 6),
    _TmnxWlanGwTuQosOvrAggRateLimit_Type()
)
tmnxWlanGwTuQosOvrAggRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosOvrAggRateLimit.setStatus("current")
_TmnxWlanGwGrpIfGwAddrTable_Object = MibTable
tmnxWlanGwGrpIfGwAddrTable = _TmnxWlanGwGrpIfGwAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 12)
)
if mibBuilder.loadTexts:
    tmnxWlanGwGrpIfGwAddrTable.setStatus("current")
_TmnxWlanGwGrpIfGwAddrEntry_Object = MibTableRow
tmnxWlanGwGrpIfGwAddrEntry = _TmnxWlanGwGrpIfGwAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 12, 1)
)
tmnxWlanGwGrpIfGwAddrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpIfGwAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpIfGwAddr"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwGrpIfGwAddrEntry.setStatus("current")
_TmnxWlanGwGrpIfGwAddrType_Type = InetAddressType
_TmnxWlanGwGrpIfGwAddrType_Object = MibTableColumn
tmnxWlanGwGrpIfGwAddrType = _TmnxWlanGwGrpIfGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 12, 1, 1),
    _TmnxWlanGwGrpIfGwAddrType_Type()
)
tmnxWlanGwGrpIfGwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpIfGwAddrType.setStatus("current")


class _TmnxWlanGwGrpIfGwAddr_Type(InetAddress):
    """Custom type tmnxWlanGwGrpIfGwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwGrpIfGwAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwGrpIfGwAddr_Object = MibTableColumn
tmnxWlanGwGrpIfGwAddr = _TmnxWlanGwGrpIfGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 12, 1, 2),
    _TmnxWlanGwGrpIfGwAddr_Type()
)
tmnxWlanGwGrpIfGwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpIfGwAddr.setStatus("current")
_TmnxWlanGwGrpIfGwAddrRowStatus_Type = RowStatus
_TmnxWlanGwGrpIfGwAddrRowStatus_Object = MibTableColumn
tmnxWlanGwGrpIfGwAddrRowStatus = _TmnxWlanGwGrpIfGwAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 12, 1, 3),
    _TmnxWlanGwGrpIfGwAddrRowStatus_Type()
)
tmnxWlanGwGrpIfGwAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpIfGwAddrRowStatus.setStatus("current")


class _TmnxWlanGwGrpIfGwAddrPurpose_Type(Bits):
    """Custom type tmnxWlanGwGrpIfGwAddrPurpose based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("xconnect", 0)
    )

_TmnxWlanGwGrpIfGwAddrPurpose_Type.__name__ = "Bits"
_TmnxWlanGwGrpIfGwAddrPurpose_Object = MibTableColumn
tmnxWlanGwGrpIfGwAddrPurpose = _TmnxWlanGwGrpIfGwAddrPurpose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 12, 1, 4),
    _TmnxWlanGwGrpIfGwAddrPurpose_Type()
)
tmnxWlanGwGrpIfGwAddrPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpIfGwAddrPurpose.setStatus("current")
_TmnxWlanGwIfRetailTable_Object = MibTable
tmnxWlanGwIfRetailTable = _TmnxWlanGwIfRetailTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailTable.setStatus("obsolete")
_TmnxWlanGwIfRetailEntry_Object = MibTableRow
tmnxWlanGwIfRetailEntry = _TmnxWlanGwIfRetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3, 1)
)
tmnxWlanGwIfRetailEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailTagStart"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailTagEnd"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailEntry.setStatus("obsolete")
_TmnxWlanGwIfRetailTagStart_Type = QTagFullRange
_TmnxWlanGwIfRetailTagStart_Object = MibTableColumn
tmnxWlanGwIfRetailTagStart = _TmnxWlanGwIfRetailTagStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3, 1, 1),
    _TmnxWlanGwIfRetailTagStart_Type()
)
tmnxWlanGwIfRetailTagStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailTagStart.setStatus("obsolete")
_TmnxWlanGwIfRetailTagEnd_Type = QTagFullRange
_TmnxWlanGwIfRetailTagEnd_Object = MibTableColumn
tmnxWlanGwIfRetailTagEnd = _TmnxWlanGwIfRetailTagEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3, 1, 2),
    _TmnxWlanGwIfRetailTagEnd_Type()
)
tmnxWlanGwIfRetailTagEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailTagEnd.setStatus("obsolete")
_TmnxWlanGwIfRetailRowStatus_Type = RowStatus
_TmnxWlanGwIfRetailRowStatus_Object = MibTableColumn
tmnxWlanGwIfRetailRowStatus = _TmnxWlanGwIfRetailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3, 1, 3),
    _TmnxWlanGwIfRetailRowStatus_Type()
)
tmnxWlanGwIfRetailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailRowStatus.setStatus("obsolete")
_TmnxWlanGwIfRetailLastCh_Type = TimeStamp
_TmnxWlanGwIfRetailLastCh_Object = MibTableColumn
tmnxWlanGwIfRetailLastCh = _TmnxWlanGwIfRetailLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3, 1, 4),
    _TmnxWlanGwIfRetailLastCh_Type()
)
tmnxWlanGwIfRetailLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailLastCh.setStatus("obsolete")
_TmnxWlanGwIfRetailService_Type = TmnxServId
_TmnxWlanGwIfRetailService_Object = MibTableColumn
tmnxWlanGwIfRetailService = _TmnxWlanGwIfRetailService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3, 1, 5),
    _TmnxWlanGwIfRetailService_Type()
)
tmnxWlanGwIfRetailService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailService.setStatus("obsolete")
_TmnxWlanGwUeTable_Object = MibTable
tmnxWlanGwUeTable = _TmnxWlanGwUeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeTable.setStatus("current")
_TmnxWlanGwUeEntry_Object = MibTableRow
tmnxWlanGwUeEntry = _TmnxWlanGwUeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1)
)
tmnxWlanGwUeEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeMacAddress"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeEntry.setStatus("current")
_TmnxWlanGwUeMacAddress_Type = MacAddress
_TmnxWlanGwUeMacAddress_Object = MibTableColumn
tmnxWlanGwUeMacAddress = _TmnxWlanGwUeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 1),
    _TmnxWlanGwUeMacAddress_Type()
)
tmnxWlanGwUeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwUeMacAddress.setStatus("current")
_TmnxWlanGwUeQTag_Type = QTagFullRangeOrNone
_TmnxWlanGwUeQTag_Object = MibTableColumn
tmnxWlanGwUeQTag = _TmnxWlanGwUeQTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 3),
    _TmnxWlanGwUeQTag_Type()
)
tmnxWlanGwUeQTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQTag.setStatus("current")
_TmnxWlanGwUeMplsLabel_Type = MplsLabel
_TmnxWlanGwUeMplsLabel_Object = MibTableColumn
tmnxWlanGwUeMplsLabel = _TmnxWlanGwUeMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 4),
    _TmnxWlanGwUeMplsLabel_Type()
)
tmnxWlanGwUeMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeMplsLabel.setStatus("current")
_TmnxWlanGwUeTuRouter_Type = TmnxVRtrID
_TmnxWlanGwUeTuRouter_Object = MibTableColumn
tmnxWlanGwUeTuRouter = _TmnxWlanGwUeTuRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 5),
    _TmnxWlanGwUeTuRouter_Type()
)
tmnxWlanGwUeTuRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeTuRouter.setStatus("current")
_TmnxWlanGwUeTuAddrType_Type = InetAddressType
_TmnxWlanGwUeTuAddrType_Object = MibTableColumn
tmnxWlanGwUeTuAddrType = _TmnxWlanGwUeTuAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 6),
    _TmnxWlanGwUeTuAddrType_Type()
)
tmnxWlanGwUeTuAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeTuAddrType.setStatus("current")


class _TmnxWlanGwUeTuRemoteAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeTuRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeTuRemoteAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeTuRemoteAddr_Object = MibTableColumn
tmnxWlanGwUeTuRemoteAddr = _TmnxWlanGwUeTuRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 7),
    _TmnxWlanGwUeTuRemoteAddr_Type()
)
tmnxWlanGwUeTuRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeTuRemoteAddr.setStatus("current")


class _TmnxWlanGwUeTuLocalAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeTuLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeTuLocalAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeTuLocalAddr_Object = MibTableColumn
tmnxWlanGwUeTuLocalAddr = _TmnxWlanGwUeTuLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 8),
    _TmnxWlanGwUeTuLocalAddr_Type()
)
tmnxWlanGwUeTuLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeTuLocalAddr.setStatus("current")
_TmnxWlanGwUeTuQosRetailService_Type = TmnxServId
_TmnxWlanGwUeTuQosRetailService_Object = MibTableColumn
tmnxWlanGwUeTuQosRetailService = _TmnxWlanGwUeTuQosRetailService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 9),
    _TmnxWlanGwUeTuQosRetailService_Type()
)
tmnxWlanGwUeTuQosRetailService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeTuQosRetailService.setStatus("current")
_TmnxWlanGwUeSsid_Type = TNamedItemOrEmpty
_TmnxWlanGwUeSsid_Object = MibTableColumn
tmnxWlanGwUeSsid = _TmnxWlanGwUeSsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 10),
    _TmnxWlanGwUeSsid_Type()
)
tmnxWlanGwUeSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeSsid.setStatus("current")
_TmnxWlanGwUePrevApAddrType_Type = InetAddressType
_TmnxWlanGwUePrevApAddrType_Object = MibTableColumn
tmnxWlanGwUePrevApAddrType = _TmnxWlanGwUePrevApAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 11),
    _TmnxWlanGwUePrevApAddrType_Type()
)
tmnxWlanGwUePrevApAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUePrevApAddrType.setStatus("current")


class _TmnxWlanGwUePrevApAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUePrevApAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUePrevApAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUePrevApAddr_Object = MibTableColumn
tmnxWlanGwUePrevApAddr = _TmnxWlanGwUePrevApAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 12),
    _TmnxWlanGwUePrevApAddr_Type()
)
tmnxWlanGwUePrevApAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUePrevApAddr.setStatus("current")


class _TmnxWlanGwUeLastMoveTime_Type(DateAndTime):
    """Custom type tmnxWlanGwUeLastMoveTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwUeLastMoveTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwUeLastMoveTime_Object = MibTableColumn
tmnxWlanGwUeLastMoveTime = _TmnxWlanGwUeLastMoveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 13),
    _TmnxWlanGwUeLastMoveTime_Type()
)
tmnxWlanGwUeLastMoveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeLastMoveTime.setStatus("current")
_TmnxWlanGwUeImsi_Type = TmnxMobImsiStr
_TmnxWlanGwUeImsi_Object = MibTableColumn
tmnxWlanGwUeImsi = _TmnxWlanGwUeImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 15),
    _TmnxWlanGwUeImsi_Type()
)
tmnxWlanGwUeImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeImsi.setStatus("current")
_TmnxWlanGwUeService_Type = TmnxServId
_TmnxWlanGwUeService_Object = MibTableColumn
tmnxWlanGwUeService = _TmnxWlanGwUeService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 16),
    _TmnxWlanGwUeService_Type()
)
tmnxWlanGwUeService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeService.setStatus("current")
_TmnxWlanGwUeSapPortId_Type = TmnxPortID
_TmnxWlanGwUeSapPortId_Object = MibTableColumn
tmnxWlanGwUeSapPortId = _TmnxWlanGwUeSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 17),
    _TmnxWlanGwUeSapPortId_Type()
)
tmnxWlanGwUeSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeSapPortId.setStatus("current")
_TmnxWlanGwUeSapPortEncapValue_Type = TmnxEncapVal
_TmnxWlanGwUeSapPortEncapValue_Object = MibTableColumn
tmnxWlanGwUeSapPortEncapValue = _TmnxWlanGwUeSapPortEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 18),
    _TmnxWlanGwUeSapPortEncapValue_Type()
)
tmnxWlanGwUeSapPortEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeSapPortEncapValue.setStatus("current")
_TmnxWlanGwUeEncapsulation_Type = TmnxWlanGwUeEncapsulation
_TmnxWlanGwUeEncapsulation_Object = MibTableColumn
tmnxWlanGwUeEncapsulation = _TmnxWlanGwUeEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 19),
    _TmnxWlanGwUeEncapsulation_Type()
)
tmnxWlanGwUeEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeEncapsulation.setStatus("current")
_TmnxWlanGwSsidTable_Object = MibTable
tmnxWlanGwSsidTable = _TmnxWlanGwSsidTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSsidTable.setStatus("current")
_TmnxWlanGwSsidEntry_Object = MibTableRow
tmnxWlanGwSsidEntry = _TmnxWlanGwSsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 5, 1)
)
tmnxWlanGwSsidEntry.setIndexNames(
    (1, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSsid"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwSsidEntry.setStatus("current")
_TmnxWlanGwSsid_Type = TNamedItem
_TmnxWlanGwSsid_Object = MibTableColumn
tmnxWlanGwSsid = _TmnxWlanGwSsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 5, 1, 1),
    _TmnxWlanGwSsid_Type()
)
tmnxWlanGwSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwSsid.setStatus("current")
_TmnxWlanGwSsidNumUe_Type = Gauge32
_TmnxWlanGwSsidNumUe_Object = MibTableColumn
tmnxWlanGwSsidNumUe = _TmnxWlanGwSsidNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 5, 1, 2),
    _TmnxWlanGwSsidNumUe_Type()
)
tmnxWlanGwSsidNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSsidNumUe.setStatus("current")
_TmnxWlanGwMgwObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwMgwObjs = _TmnxWlanGwMgwObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6)
)
_TmnxWlanGwMgwProfTable_Object = MibTable
tmnxWlanGwMgwProfTable = _TmnxWlanGwMgwProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfTable.setStatus("current")
_TmnxWlanGwMgwProfEntry_Object = MibTableRow
tmnxWlanGwMgwProfEntry = _TmnxWlanGwMgwProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1)
)
tmnxWlanGwMgwProfEntry.setIndexNames(
    (1, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfName"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfEntry.setStatus("current")
_TmnxWlanGwMgwProfName_Type = TNamedItem
_TmnxWlanGwMgwProfName_Object = MibTableColumn
tmnxWlanGwMgwProfName = _TmnxWlanGwMgwProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 1),
    _TmnxWlanGwMgwProfName_Type()
)
tmnxWlanGwMgwProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfName.setStatus("current")
_TmnxWlanGwMgwProfRowStatus_Type = RowStatus
_TmnxWlanGwMgwProfRowStatus_Object = MibTableColumn
tmnxWlanGwMgwProfRowStatus = _TmnxWlanGwMgwProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 2),
    _TmnxWlanGwMgwProfRowStatus_Type()
)
tmnxWlanGwMgwProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfRowStatus.setStatus("current")
_TmnxWlanGwMgwProfLastChanged_Type = TimeStamp
_TmnxWlanGwMgwProfLastChanged_Object = MibTableColumn
tmnxWlanGwMgwProfLastChanged = _TmnxWlanGwMgwProfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 3),
    _TmnxWlanGwMgwProfLastChanged_Type()
)
tmnxWlanGwMgwProfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfLastChanged.setStatus("current")


class _TmnxWlanGwMgwProfDescription_Type(TItemDescription):
    """Custom type tmnxWlanGwMgwProfDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWlanGwMgwProfDescription_Type.__name__ = "TItemDescription"
_TmnxWlanGwMgwProfDescription_Object = MibTableColumn
tmnxWlanGwMgwProfDescription = _TmnxWlanGwMgwProfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 4),
    _TmnxWlanGwMgwProfDescription_Type()
)
tmnxWlanGwMgwProfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfDescription.setStatus("current")


class _TmnxWlanGwMgwProfMsgReTxTimeout_Type(TmnxMobProfMsgReTxTimeout):
    """Custom type tmnxWlanGwMgwProfMsgReTxTimeout based on TmnxMobProfMsgReTxTimeout"""
    defaultValue = 5


_TmnxWlanGwMgwProfMsgReTxTimeout_Type.__name__ = "TmnxMobProfMsgReTxTimeout"
_TmnxWlanGwMgwProfMsgReTxTimeout_Object = MibTableColumn
tmnxWlanGwMgwProfMsgReTxTimeout = _TmnxWlanGwMgwProfMsgReTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 5),
    _TmnxWlanGwMgwProfMsgReTxTimeout_Type()
)
tmnxWlanGwMgwProfMsgReTxTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfMsgReTxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfMsgReTxTimeout.setUnits("seconds")


class _TmnxWlanGwMgwProfMsgReTxRetryCnt_Type(TmnxMobProfMsgReTxRetryCount):
    """Custom type tmnxWlanGwMgwProfMsgReTxRetryCnt based on TmnxMobProfMsgReTxRetryCount"""
    defaultValue = 3


_TmnxWlanGwMgwProfMsgReTxRetryCnt_Type.__name__ = "TmnxMobProfMsgReTxRetryCount"
_TmnxWlanGwMgwProfMsgReTxRetryCnt_Object = MibTableColumn
tmnxWlanGwMgwProfMsgReTxRetryCnt = _TmnxWlanGwMgwProfMsgReTxRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 6),
    _TmnxWlanGwMgwProfMsgReTxRetryCnt_Type()
)
tmnxWlanGwMgwProfMsgReTxRetryCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfMsgReTxRetryCnt.setStatus("current")


class _TmnxWlanGwMgwProfKeepAlvTimeout_Type(TmnxMobProfKeepAliveTimeout):
    """Custom type tmnxWlanGwMgwProfKeepAlvTimeout based on TmnxMobProfKeepAliveTimeout"""
    defaultValue = 60


_TmnxWlanGwMgwProfKeepAlvTimeout_Type.__name__ = "TmnxMobProfKeepAliveTimeout"
_TmnxWlanGwMgwProfKeepAlvTimeout_Object = MibTableColumn
tmnxWlanGwMgwProfKeepAlvTimeout = _TmnxWlanGwMgwProfKeepAlvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 7),
    _TmnxWlanGwMgwProfKeepAlvTimeout_Type()
)
tmnxWlanGwMgwProfKeepAlvTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfKeepAlvTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfKeepAlvTimeout.setUnits("seconds")


class _TmnxWlanGwMgwProfKeepAlvRetryCnt_Type(TmnxMobProfKeepAliveRetryCount):
    """Custom type tmnxWlanGwMgwProfKeepAlvRetryCnt based on TmnxMobProfKeepAliveRetryCount"""
    defaultValue = 4


_TmnxWlanGwMgwProfKeepAlvRetryCnt_Type.__name__ = "TmnxMobProfKeepAliveRetryCount"
_TmnxWlanGwMgwProfKeepAlvRetryCnt_Object = MibTableColumn
tmnxWlanGwMgwProfKeepAlvRetryCnt = _TmnxWlanGwMgwProfKeepAlvRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 8),
    _TmnxWlanGwMgwProfKeepAlvRetryCnt_Type()
)
tmnxWlanGwMgwProfKeepAlvRetryCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfKeepAlvRetryCnt.setStatus("current")


class _TmnxWlanGwMgwProfKeepAlvResp_Type(TmnxMobProfKeepAliveResponse):
    """Custom type tmnxWlanGwMgwProfKeepAlvResp based on TmnxMobProfKeepAliveResponse"""
    defaultValue = 5


_TmnxWlanGwMgwProfKeepAlvResp_Type.__name__ = "TmnxMobProfKeepAliveResponse"
_TmnxWlanGwMgwProfKeepAlvResp_Object = MibTableColumn
tmnxWlanGwMgwProfKeepAlvResp = _TmnxWlanGwMgwProfKeepAlvResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 9),
    _TmnxWlanGwMgwProfKeepAlvResp_Type()
)
tmnxWlanGwMgwProfKeepAlvResp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfKeepAlvResp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfKeepAlvResp.setUnits("seconds")


class _TmnxWlanGwMgwProfTtl_Type(TmnxMobProfIpTtl):
    """Custom type tmnxWlanGwMgwProfTtl based on TmnxMobProfIpTtl"""
    defaultValue = 255


_TmnxWlanGwMgwProfTtl_Type.__name__ = "TmnxMobProfIpTtl"
_TmnxWlanGwMgwProfTtl_Object = MibTableColumn
tmnxWlanGwMgwProfTtl = _TmnxWlanGwMgwProfTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 10),
    _TmnxWlanGwMgwProfTtl_Type()
)
tmnxWlanGwMgwProfTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfTtl.setUnits("hops")


class _TmnxWlanGwMgwProfInterfaceType_Type(TmnxWlanGwMgwInterfaceType):
    """Custom type tmnxWlanGwMgwProfInterfaceType based on TmnxWlanGwMgwInterfaceType"""
    defaultValue = 2


_TmnxWlanGwMgwProfInterfaceType_Type.__name__ = "TmnxWlanGwMgwInterfaceType"
_TmnxWlanGwMgwProfInterfaceType_Object = MibTableColumn
tmnxWlanGwMgwProfInterfaceType = _TmnxWlanGwMgwProfInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 12),
    _TmnxWlanGwMgwProfInterfaceType_Type()
)
tmnxWlanGwMgwProfInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfInterfaceType.setStatus("current")


class _TmnxWlanGwMgwProfChrgCharHome_Type(TmnxWlanGwChargingCharBits):
    """Custom type tmnxWlanGwMgwProfChrgCharHome based on TmnxWlanGwChargingCharBits"""
    defaultBinValue = "0"


_TmnxWlanGwMgwProfChrgCharHome_Type.__name__ = "TmnxWlanGwChargingCharBits"
_TmnxWlanGwMgwProfChrgCharHome_Object = MibTableColumn
tmnxWlanGwMgwProfChrgCharHome = _TmnxWlanGwMgwProfChrgCharHome_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 15),
    _TmnxWlanGwMgwProfChrgCharHome_Type()
)
tmnxWlanGwMgwProfChrgCharHome.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfChrgCharHome.setStatus("current")


class _TmnxWlanGwMgwProfChrgCharRoam_Type(TmnxWlanGwChargingCharBits):
    """Custom type tmnxWlanGwMgwProfChrgCharRoam based on TmnxWlanGwChargingCharBits"""
    defaultBinValue = "0"


_TmnxWlanGwMgwProfChrgCharRoam_Type.__name__ = "TmnxWlanGwChargingCharBits"
_TmnxWlanGwMgwProfChrgCharRoam_Object = MibTableColumn
tmnxWlanGwMgwProfChrgCharRoam = _TmnxWlanGwMgwProfChrgCharRoam_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 16),
    _TmnxWlanGwMgwProfChrgCharRoam_Type()
)
tmnxWlanGwMgwProfChrgCharRoam.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfChrgCharRoam.setStatus("current")


class _TmnxWlanGwMgwProfSeHoldTime_Type(Integer32):
    """Custom type tmnxWlanGwMgwProfSeHoldTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3600),
    )


_TmnxWlanGwMgwProfSeHoldTime_Type.__name__ = "Integer32"
_TmnxWlanGwMgwProfSeHoldTime_Object = MibTableColumn
tmnxWlanGwMgwProfSeHoldTime = _TmnxWlanGwMgwProfSeHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 20),
    _TmnxWlanGwMgwProfSeHoldTime_Type()
)
tmnxWlanGwMgwProfSeHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfSeHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfSeHoldTime.setUnits("seconds")


class _TmnxWlanGwMgwProfReportWlanLoc_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwMgwProfReportWlanLoc based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwMgwProfReportWlanLoc_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwMgwProfReportWlanLoc_Object = MibTableColumn
tmnxWlanGwMgwProfReportWlanLoc = _TmnxWlanGwMgwProfReportWlanLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 21),
    _TmnxWlanGwMgwProfReportWlanLoc_Type()
)
tmnxWlanGwMgwProfReportWlanLoc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfReportWlanLoc.setStatus("current")


class _TmnxWlanGwMgwProfProtocolCfgOpt_Type(Integer32):
    """Custom type tmnxWlanGwMgwProfProtocolCfgOpt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pco", 1),
          ("apco", 2))
    )


_TmnxWlanGwMgwProfProtocolCfgOpt_Type.__name__ = "Integer32"
_TmnxWlanGwMgwProfProtocolCfgOpt_Object = MibTableColumn
tmnxWlanGwMgwProfProtocolCfgOpt = _TmnxWlanGwMgwProfProtocolCfgOpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 22),
    _TmnxWlanGwMgwProfProtocolCfgOpt_Type()
)
tmnxWlanGwMgwProfProtocolCfgOpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfProtocolCfgOpt.setStatus("current")


class _TmnxWlanGwMgwProfPythonPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwMgwProfPythonPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwMgwProfPythonPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwMgwProfPythonPolicy_Object = MibTableColumn
tmnxWlanGwMgwProfPythonPolicy = _TmnxWlanGwMgwProfPythonPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 23),
    _TmnxWlanGwMgwProfPythonPolicy_Type()
)
tmnxWlanGwMgwProfPythonPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfPythonPolicy.setStatus("current")


class _TmnxWlanGwMgwProfRatType_Type(Unsigned32):
    """Custom type tmnxWlanGwMgwProfRatType based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxWlanGwMgwProfRatType_Type.__name__ = "Unsigned32"
_TmnxWlanGwMgwProfRatType_Object = MibTableColumn
tmnxWlanGwMgwProfRatType = _TmnxWlanGwMgwProfRatType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 24),
    _TmnxWlanGwMgwProfRatType_Type()
)
tmnxWlanGwMgwProfRatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfRatType.setStatus("current")


class _TmnxWlanGwMgwProfIpv4Mtu_Type(Unsigned32):
    """Custom type tmnxWlanGwMgwProfIpv4Mtu based on Unsigned32"""
    defaultValue = 1400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9000),
    )


_TmnxWlanGwMgwProfIpv4Mtu_Type.__name__ = "Unsigned32"
_TmnxWlanGwMgwProfIpv4Mtu_Object = MibTableColumn
tmnxWlanGwMgwProfIpv4Mtu = _TmnxWlanGwMgwProfIpv4Mtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 25),
    _TmnxWlanGwMgwProfIpv4Mtu_Type()
)
tmnxWlanGwMgwProfIpv4Mtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfIpv4Mtu.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfIpv4Mtu.setUnits("bytes")


class _TmnxWlanGwMgwProfEndMarkerCount_Type(Unsigned32):
    """Custom type tmnxWlanGwMgwProfEndMarkerCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TmnxWlanGwMgwProfEndMarkerCount_Type.__name__ = "Unsigned32"
_TmnxWlanGwMgwProfEndMarkerCount_Object = MibTableColumn
tmnxWlanGwMgwProfEndMarkerCount = _TmnxWlanGwMgwProfEndMarkerCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 26),
    _TmnxWlanGwMgwProfEndMarkerCount_Type()
)
tmnxWlanGwMgwProfEndMarkerCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfEndMarkerCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfEndMarkerCount.setUnits("packets")


class _TmnxWlanGwMgwProfChangeRepAction_Type(Integer32):
    """Custom type tmnxWlanGwMgwProfChangeRepAction based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TmnxWlanGwMgwProfChangeRepAction_Type.__name__ = "Integer32"
_TmnxWlanGwMgwProfChangeRepAction_Object = MibTableColumn
tmnxWlanGwMgwProfChangeRepAction = _TmnxWlanGwMgwProfChangeRepAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 27),
    _TmnxWlanGwMgwProfChangeRepAction_Type()
)
tmnxWlanGwMgwProfChangeRepAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfChangeRepAction.setStatus("current")
_TmnxWlanGwMgwAddrTable_Object = MibTable
tmnxWlanGwMgwAddrTable = _TmnxWlanGwMgwAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrTable.setStatus("current")
_TmnxWlanGwMgwAddrEntry_Object = MibTableRow
tmnxWlanGwMgwAddrEntry = _TmnxWlanGwMgwAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1)
)
tmnxWlanGwMgwAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrEntry.setStatus("current")
_TmnxWlanGwMgwAddrType_Type = InetAddressType
_TmnxWlanGwMgwAddrType_Object = MibTableColumn
tmnxWlanGwMgwAddrType = _TmnxWlanGwMgwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1, 1),
    _TmnxWlanGwMgwAddrType_Type()
)
tmnxWlanGwMgwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrType.setStatus("current")


class _TmnxWlanGwMgwAddr_Type(InetAddress):
    """Custom type tmnxWlanGwMgwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwMgwAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwMgwAddr_Object = MibTableColumn
tmnxWlanGwMgwAddr = _TmnxWlanGwMgwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1, 2),
    _TmnxWlanGwMgwAddr_Type()
)
tmnxWlanGwMgwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddr.setStatus("current")


class _TmnxWlanGwMgwAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxWlanGwMgwAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxWlanGwMgwAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxWlanGwMgwAddrPrefixLen_Object = MibTableColumn
tmnxWlanGwMgwAddrPrefixLen = _TmnxWlanGwMgwAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1, 3),
    _TmnxWlanGwMgwAddrPrefixLen_Type()
)
tmnxWlanGwMgwAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrPrefixLen.setStatus("current")
_TmnxWlanGwMgwAddrRowStatus_Type = RowStatus
_TmnxWlanGwMgwAddrRowStatus_Object = MibTableColumn
tmnxWlanGwMgwAddrRowStatus = _TmnxWlanGwMgwAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1, 4),
    _TmnxWlanGwMgwAddrRowStatus_Type()
)
tmnxWlanGwMgwAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrRowStatus.setStatus("current")
_TmnxWlanGwMgwAddrLastMgmtChange_Type = TimeStamp
_TmnxWlanGwMgwAddrLastMgmtChange_Object = MibTableColumn
tmnxWlanGwMgwAddrLastMgmtChange = _TmnxWlanGwMgwAddrLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1, 5),
    _TmnxWlanGwMgwAddrLastMgmtChange_Type()
)
tmnxWlanGwMgwAddrLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrLastMgmtChange.setStatus("current")
_TmnxWlanGwMgwAddrProfile_Type = TNamedItem
_TmnxWlanGwMgwAddrProfile_Object = MibTableColumn
tmnxWlanGwMgwAddrProfile = _TmnxWlanGwMgwAddrProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1, 6),
    _TmnxWlanGwMgwAddrProfile_Type()
)
tmnxWlanGwMgwAddrProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrProfile.setStatus("current")
_TmnxWlanGwMgwTable_Object = MibTable
tmnxWlanGwMgwTable = _TmnxWlanGwMgwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwTable.setStatus("current")
_TmnxWlanGwMgwEntry_Object = MibTableRow
tmnxWlanGwMgwEntry = _TmnxWlanGwMgwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1)
)
tmnxWlanGwMgwEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRemoteAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRemotePort"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwEntry.setStatus("current")
_TmnxWlanGwMgwRemoteAddrType_Type = InetAddressType
_TmnxWlanGwMgwRemoteAddrType_Object = MibTableColumn
tmnxWlanGwMgwRemoteAddrType = _TmnxWlanGwMgwRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 1),
    _TmnxWlanGwMgwRemoteAddrType_Type()
)
tmnxWlanGwMgwRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwRemoteAddrType.setStatus("current")


class _TmnxWlanGwMgwRemoteAddr_Type(InetAddress):
    """Custom type tmnxWlanGwMgwRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwMgwRemoteAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwMgwRemoteAddr_Object = MibTableColumn
tmnxWlanGwMgwRemoteAddr = _TmnxWlanGwMgwRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 2),
    _TmnxWlanGwMgwRemoteAddr_Type()
)
tmnxWlanGwMgwRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwRemoteAddr.setStatus("current")
_TmnxWlanGwMgwRemotePort_Type = InetPortNumber
_TmnxWlanGwMgwRemotePort_Object = MibTableColumn
tmnxWlanGwMgwRemotePort = _TmnxWlanGwMgwRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 3),
    _TmnxWlanGwMgwRemotePort_Type()
)
tmnxWlanGwMgwRemotePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwRemotePort.setStatus("current")
_TmnxWlanGwMgwLocalAddrType_Type = InetAddressType
_TmnxWlanGwMgwLocalAddrType_Object = MibTableColumn
tmnxWlanGwMgwLocalAddrType = _TmnxWlanGwMgwLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 4),
    _TmnxWlanGwMgwLocalAddrType_Type()
)
tmnxWlanGwMgwLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwLocalAddrType.setStatus("current")


class _TmnxWlanGwMgwLocalAddr_Type(InetAddress):
    """Custom type tmnxWlanGwMgwLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwMgwLocalAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwMgwLocalAddr_Object = MibTableColumn
tmnxWlanGwMgwLocalAddr = _TmnxWlanGwMgwLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 5),
    _TmnxWlanGwMgwLocalAddr_Type()
)
tmnxWlanGwMgwLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwLocalAddr.setStatus("current")


class _TmnxWlanGwMgwTime_Type(DateAndTime):
    """Custom type tmnxWlanGwMgwTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwMgwTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwMgwTime_Object = MibTableColumn
tmnxWlanGwMgwTime = _TmnxWlanGwMgwTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 6),
    _TmnxWlanGwMgwTime_Type()
)
tmnxWlanGwMgwTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwTime.setStatus("current")
_TmnxWlanGwMgwProfile_Type = TNamedItemOrEmpty
_TmnxWlanGwMgwProfile_Object = MibTableColumn
tmnxWlanGwMgwProfile = _TmnxWlanGwMgwProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 7),
    _TmnxWlanGwMgwProfile_Type()
)
tmnxWlanGwMgwProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfile.setStatus("current")


class _TmnxWlanGwMgwControl_Type(Integer32):
    """Custom type tmnxWlanGwMgwControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gtpv1C", 1),
          ("gtpv2C", 2))
    )


_TmnxWlanGwMgwControl_Type.__name__ = "Integer32"
_TmnxWlanGwMgwControl_Object = MibTableColumn
tmnxWlanGwMgwControl = _TmnxWlanGwMgwControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 8),
    _TmnxWlanGwMgwControl_Type()
)
tmnxWlanGwMgwControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwControl.setStatus("current")
_TmnxWlanGwMgwRestartCnt_Type = Gauge32
_TmnxWlanGwMgwRestartCnt_Object = MibTableColumn
tmnxWlanGwMgwRestartCnt = _TmnxWlanGwMgwRestartCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 9),
    _TmnxWlanGwMgwRestartCnt_Type()
)
tmnxWlanGwMgwRestartCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwRestartCnt.setStatus("current")
_TmnxWlanGwMgwState_Type = TmnxMobPathMgmtState
_TmnxWlanGwMgwState_Object = MibTableColumn
tmnxWlanGwMgwState = _TmnxWlanGwMgwState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 10),
    _TmnxWlanGwMgwState_Type()
)
tmnxWlanGwMgwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwState.setStatus("current")
_TmnxWlanGwMgwInterfaceType_Type = TmnxWlanGwMgwInterfaceType
_TmnxWlanGwMgwInterfaceType_Object = MibTableColumn
tmnxWlanGwMgwInterfaceType = _TmnxWlanGwMgwInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 11),
    _TmnxWlanGwMgwInterfaceType_Type()
)
tmnxWlanGwMgwInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwInterfaceType.setStatus("current")
_TmnxWlanMgwStatsTable_Object = MibTable
tmnxWlanMgwStatsTable = _TmnxWlanMgwStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsTable.setStatus("current")
_TmnxWlanMgwStatsEntry_Object = MibTableRow
tmnxWlanMgwStatsEntry = _TmnxWlanMgwStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4, 1)
)
tmnxWlanMgwStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRemoteAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRemotePort"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanMgwStatsId"),
)
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsEntry.setStatus("current")


class _TmnxWlanMgwStatsId_Type(Unsigned32):
    """Custom type tmnxWlanMgwStatsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TmnxWlanMgwStatsId_Type.__name__ = "Unsigned32"
_TmnxWlanMgwStatsId_Object = MibTableColumn
tmnxWlanMgwStatsId = _TmnxWlanMgwStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4, 1, 1),
    _TmnxWlanMgwStatsId_Type()
)
tmnxWlanMgwStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsId.setStatus("current")


class _TmnxWlanMgwStatsName_Type(DisplayString):
    """Custom type tmnxWlanMgwStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxWlanMgwStatsName_Type.__name__ = "DisplayString"
_TmnxWlanMgwStatsName_Object = MibTableColumn
tmnxWlanMgwStatsName = _TmnxWlanMgwStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4, 1, 2),
    _TmnxWlanMgwStatsName_Type()
)
tmnxWlanMgwStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsName.setStatus("current")
_TmnxWlanMgwStatsVal_Type = Counter64
_TmnxWlanMgwStatsVal_Object = MibTableColumn
tmnxWlanMgwStatsVal = _TmnxWlanMgwStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4, 1, 3),
    _TmnxWlanMgwStatsVal_Type()
)
tmnxWlanMgwStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsVal.setStatus("current")
_TmnxWlanMgwStatsValLw_Type = Counter32
_TmnxWlanMgwStatsValLw_Object = MibTableColumn
tmnxWlanMgwStatsValLw = _TmnxWlanMgwStatsValLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4, 1, 4),
    _TmnxWlanMgwStatsValLw_Type()
)
tmnxWlanMgwStatsValLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsValLw.setStatus("current")
_TmnxWlanMgwStatsValHw_Type = Counter32
_TmnxWlanMgwStatsValHw_Object = MibTableColumn
tmnxWlanMgwStatsValHw = _TmnxWlanMgwStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4, 1, 5),
    _TmnxWlanMgwStatsValHw_Type()
)
tmnxWlanMgwStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsValHw.setStatus("current")
_TmnxWlanGwGtpSeTable_Object = MibTable
tmnxWlanGwGtpSeTable = _TmnxWlanGwGtpSeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5)
)
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeTable.setStatus("current")
_TmnxWlanGwGtpSeEntry_Object = MibTableRow
tmnxWlanGwGtpSeEntry = _TmnxWlanGwGtpSeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1)
)
tmnxWlanGwGtpSeEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeImsi"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeApn"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeEntry.setStatus("current")


class _TmnxWlanGwGtpSeImsi_Type(TmnxMobImsiStr):
    """Custom type tmnxWlanGwGtpSeImsi based on TmnxMobImsiStr"""
    subtypeSpec = TmnxMobImsiStr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 15),
    )


_TmnxWlanGwGtpSeImsi_Type.__name__ = "TmnxMobImsiStr"
_TmnxWlanGwGtpSeImsi_Object = MibTableColumn
tmnxWlanGwGtpSeImsi = _TmnxWlanGwGtpSeImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 1),
    _TmnxWlanGwGtpSeImsi_Type()
)
tmnxWlanGwGtpSeImsi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeImsi.setStatus("current")
_TmnxWlanGwGtpSeApn_Type = TmnxMobApn
_TmnxWlanGwGtpSeApn_Object = MibTableColumn
tmnxWlanGwGtpSeApn = _TmnxWlanGwGtpSeApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 2),
    _TmnxWlanGwGtpSeApn_Type()
)
tmnxWlanGwGtpSeApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeApn.setStatus("current")
_TmnxWlanGwGtpSeMgwRouter_Type = TmnxVRtrIDOrZero
_TmnxWlanGwGtpSeMgwRouter_Object = MibTableColumn
tmnxWlanGwGtpSeMgwRouter = _TmnxWlanGwGtpSeMgwRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 3),
    _TmnxWlanGwGtpSeMgwRouter_Type()
)
tmnxWlanGwGtpSeMgwRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeMgwRouter.setStatus("current")
_TmnxWlanGwGtpSeMgwAddrType_Type = InetAddressType
_TmnxWlanGwGtpSeMgwAddrType_Object = MibTableColumn
tmnxWlanGwGtpSeMgwAddrType = _TmnxWlanGwGtpSeMgwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 4),
    _TmnxWlanGwGtpSeMgwAddrType_Type()
)
tmnxWlanGwGtpSeMgwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeMgwAddrType.setStatus("current")


class _TmnxWlanGwGtpSeMgwAddr_Type(InetAddress):
    """Custom type tmnxWlanGwGtpSeMgwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwGtpSeMgwAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwGtpSeMgwAddr_Object = MibTableColumn
tmnxWlanGwGtpSeMgwAddr = _TmnxWlanGwGtpSeMgwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 5),
    _TmnxWlanGwGtpSeMgwAddr_Type()
)
tmnxWlanGwGtpSeMgwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeMgwAddr.setStatus("current")
_TmnxWlanGwGtpSeRemoteCtrlTeid_Type = Unsigned32
_TmnxWlanGwGtpSeRemoteCtrlTeid_Object = MibTableColumn
tmnxWlanGwGtpSeRemoteCtrlTeid = _TmnxWlanGwGtpSeRemoteCtrlTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 6),
    _TmnxWlanGwGtpSeRemoteCtrlTeid_Type()
)
tmnxWlanGwGtpSeRemoteCtrlTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeRemoteCtrlTeid.setStatus("current")
_TmnxWlanGwGtpSeLocalCtrlTeid_Type = Unsigned32
_TmnxWlanGwGtpSeLocalCtrlTeid_Object = MibTableColumn
tmnxWlanGwGtpSeLocalCtrlTeid = _TmnxWlanGwGtpSeLocalCtrlTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 7),
    _TmnxWlanGwGtpSeLocalCtrlTeid_Type()
)
tmnxWlanGwGtpSeLocalCtrlTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeLocalCtrlTeid.setStatus("current")
_TmnxWlanGwGtpSeChrgChar_Type = TmnxWlanGwChargingCharBits
_TmnxWlanGwGtpSeChrgChar_Object = MibTableColumn
tmnxWlanGwGtpSeChrgChar = _TmnxWlanGwGtpSeChrgChar_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 10),
    _TmnxWlanGwGtpSeChrgChar_Type()
)
tmnxWlanGwGtpSeChrgChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeChrgChar.setStatus("current")
_TmnxWlanGwGtpSeQosUplinkAmbr_Type = TmnxWlanGwAmbr
_TmnxWlanGwGtpSeQosUplinkAmbr_Object = MibTableColumn
tmnxWlanGwGtpSeQosUplinkAmbr = _TmnxWlanGwGtpSeQosUplinkAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 11),
    _TmnxWlanGwGtpSeQosUplinkAmbr_Type()
)
tmnxWlanGwGtpSeQosUplinkAmbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeQosUplinkAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeQosUplinkAmbr.setUnits("kilobps")
_TmnxWlanGwGtpSeQosDwnlinkAmbr_Type = TmnxWlanGwAmbr
_TmnxWlanGwGtpSeQosDwnlinkAmbr_Object = MibTableColumn
tmnxWlanGwGtpSeQosDwnlinkAmbr = _TmnxWlanGwGtpSeQosDwnlinkAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 12),
    _TmnxWlanGwGtpSeQosDwnlinkAmbr_Type()
)
tmnxWlanGwGtpSeQosDwnlinkAmbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeQosDwnlinkAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeQosDwnlinkAmbr.setUnits("kilobps")
_TmnxWlanGwBcTable_Object = MibTable
tmnxWlanGwBcTable = _TmnxWlanGwBcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6)
)
if mibBuilder.loadTexts:
    tmnxWlanGwBcTable.setStatus("current")
_TmnxWlanGwBcEntry_Object = MibTableRow
tmnxWlanGwBcEntry = _TmnxWlanGwBcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1)
)
tmnxWlanGwBcEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeImsi"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeApn"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwBcEntry.setStatus("current")
_TmnxWlanGwBcId_Type = TmnxMobBearerId
_TmnxWlanGwBcId_Object = MibTableColumn
tmnxWlanGwBcId = _TmnxWlanGwBcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 1),
    _TmnxWlanGwBcId_Type()
)
tmnxWlanGwBcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwBcId.setStatus("current")
_TmnxWlanGwBcRemoteTeid_Type = Unsigned32
_TmnxWlanGwBcRemoteTeid_Object = MibTableColumn
tmnxWlanGwBcRemoteTeid = _TmnxWlanGwBcRemoteTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 2),
    _TmnxWlanGwBcRemoteTeid_Type()
)
tmnxWlanGwBcRemoteTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcRemoteTeid.setStatus("current")
_TmnxWlanGwBcLocalTeid_Type = Unsigned32
_TmnxWlanGwBcLocalTeid_Object = MibTableColumn
tmnxWlanGwBcLocalTeid = _TmnxWlanGwBcLocalTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 3),
    _TmnxWlanGwBcLocalTeid_Type()
)
tmnxWlanGwBcLocalTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcLocalTeid.setStatus("current")
_TmnxWlanGwBcQosUlGbr_Type = Unsigned32
_TmnxWlanGwBcQosUlGbr_Object = MibTableColumn
tmnxWlanGwBcQosUlGbr = _TmnxWlanGwBcQosUlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 10),
    _TmnxWlanGwBcQosUlGbr_Type()
)
tmnxWlanGwBcQosUlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosUlGbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosUlGbr.setUnits("kilobps")
_TmnxWlanGwBcQosUlMbr_Type = Unsigned32
_TmnxWlanGwBcQosUlMbr_Object = MibTableColumn
tmnxWlanGwBcQosUlMbr = _TmnxWlanGwBcQosUlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 11),
    _TmnxWlanGwBcQosUlMbr_Type()
)
tmnxWlanGwBcQosUlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosUlMbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosUlMbr.setUnits("kilobps")
_TmnxWlanGwBcQosDlGbr_Type = Unsigned32
_TmnxWlanGwBcQosDlGbr_Object = MibTableColumn
tmnxWlanGwBcQosDlGbr = _TmnxWlanGwBcQosDlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 12),
    _TmnxWlanGwBcQosDlGbr_Type()
)
tmnxWlanGwBcQosDlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosDlGbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosDlGbr.setUnits("kilobps")
_TmnxWlanGwBcQosDlMbr_Type = Unsigned32
_TmnxWlanGwBcQosDlMbr_Object = MibTableColumn
tmnxWlanGwBcQosDlMbr = _TmnxWlanGwBcQosDlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 13),
    _TmnxWlanGwBcQosDlMbr_Type()
)
tmnxWlanGwBcQosDlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosDlMbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosDlMbr.setUnits("kilobps")
_TmnxWlanGwBcQosQci_Type = TmnxMobQci
_TmnxWlanGwBcQosQci_Object = MibTableColumn
tmnxWlanGwBcQosQci = _TmnxWlanGwBcQosQci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 14),
    _TmnxWlanGwBcQosQci_Type()
)
tmnxWlanGwBcQosQci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosQci.setStatus("current")
_TmnxWlanGwBcQosArp_Type = TmnxMobArp
_TmnxWlanGwBcQosArp_Object = MibTableColumn
tmnxWlanGwBcQosArp = _TmnxWlanGwBcQosArp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 15),
    _TmnxWlanGwBcQosArp_Type()
)
tmnxWlanGwBcQosArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosArp.setStatus("current")
_TmnxWlanGwMgwCacheTable_Object = MibTable
tmnxWlanGwMgwCacheTable = _TmnxWlanGwMgwCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 7)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheTable.setStatus("obsolete")
_TmnxWlanGwMgwCacheEntry_Object = MibTableRow
tmnxWlanGwMgwCacheEntry = _TmnxWlanGwMgwCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 7, 1)
)
tmnxWlanGwMgwCacheEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwCacheApn"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwCacheAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwCacheAddr"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheEntry.setStatus("obsolete")
_TmnxWlanGwMgwCacheApn_Type = TmnxMobApnDomainName
_TmnxWlanGwMgwCacheApn_Object = MibTableColumn
tmnxWlanGwMgwCacheApn = _TmnxWlanGwMgwCacheApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 7, 1, 1),
    _TmnxWlanGwMgwCacheApn_Type()
)
tmnxWlanGwMgwCacheApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheApn.setStatus("obsolete")
_TmnxWlanGwMgwCacheAddrType_Type = InetAddressType
_TmnxWlanGwMgwCacheAddrType_Object = MibTableColumn
tmnxWlanGwMgwCacheAddrType = _TmnxWlanGwMgwCacheAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 7, 1, 2),
    _TmnxWlanGwMgwCacheAddrType_Type()
)
tmnxWlanGwMgwCacheAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheAddrType.setStatus("obsolete")


class _TmnxWlanGwMgwCacheAddr_Type(InetAddress):
    """Custom type tmnxWlanGwMgwCacheAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwMgwCacheAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwMgwCacheAddr_Object = MibTableColumn
tmnxWlanGwMgwCacheAddr = _TmnxWlanGwMgwCacheAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 7, 1, 3),
    _TmnxWlanGwMgwCacheAddr_Type()
)
tmnxWlanGwMgwCacheAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheAddr.setStatus("obsolete")
_TmnxWlanGwMgwCacheTtl_Type = Unsigned32
_TmnxWlanGwMgwCacheTtl_Object = MibTableColumn
tmnxWlanGwMgwCacheTtl = _TmnxWlanGwMgwCacheTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 7, 1, 4),
    _TmnxWlanGwMgwCacheTtl_Type()
)
tmnxWlanGwMgwCacheTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheTtl.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheTtl.setUnits("seconds")
_TmnxWlanGwGtpStatsTable_Object = MibTable
tmnxWlanGwGtpStatsTable = _TmnxWlanGwGtpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8)
)
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsTable.setStatus("current")
_TmnxWlanGwGtpStatsEntry_Object = MibTableRow
tmnxWlanGwGtpStatsEntry = _TmnxWlanGwGtpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8, 1)
)
tmnxWlanGwGtpStatsEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpStatsId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsEntry.setStatus("current")


class _TmnxWlanGwGtpStatsId_Type(Unsigned32):
    """Custom type tmnxWlanGwGtpStatsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 71),
    )


_TmnxWlanGwGtpStatsId_Type.__name__ = "Unsigned32"
_TmnxWlanGwGtpStatsId_Object = MibTableColumn
tmnxWlanGwGtpStatsId = _TmnxWlanGwGtpStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8, 1, 1),
    _TmnxWlanGwGtpStatsId_Type()
)
tmnxWlanGwGtpStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsId.setStatus("current")


class _TmnxWlanGwGtpStatsName_Type(DisplayString):
    """Custom type tmnxWlanGwGtpStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 56),
    )


_TmnxWlanGwGtpStatsName_Type.__name__ = "DisplayString"
_TmnxWlanGwGtpStatsName_Object = MibTableColumn
tmnxWlanGwGtpStatsName = _TmnxWlanGwGtpStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8, 1, 2),
    _TmnxWlanGwGtpStatsName_Type()
)
tmnxWlanGwGtpStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsName.setStatus("current")
_TmnxWlanGwGtpStatsVal_Type = Counter64
_TmnxWlanGwGtpStatsVal_Object = MibTableColumn
tmnxWlanGwGtpStatsVal = _TmnxWlanGwGtpStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8, 1, 3),
    _TmnxWlanGwGtpStatsVal_Type()
)
tmnxWlanGwGtpStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsVal.setStatus("current")
_TmnxWlanGwGtpStatsValLw_Type = Counter32
_TmnxWlanGwGtpStatsValLw_Object = MibTableColumn
tmnxWlanGwGtpStatsValLw = _TmnxWlanGwGtpStatsValLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8, 1, 4),
    _TmnxWlanGwGtpStatsValLw_Type()
)
tmnxWlanGwGtpStatsValLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsValLw.setStatus("current")
_TmnxWlanGwGtpStatsValHw_Type = Counter32
_TmnxWlanGwGtpStatsValHw_Object = MibTableColumn
tmnxWlanGwGtpStatsValHw = _TmnxWlanGwGtpStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8, 1, 5),
    _TmnxWlanGwGtpStatsValHw_Type()
)
tmnxWlanGwGtpStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsValHw.setStatus("current")
_TmnxWlanGwMgwArecCacheTable_Object = MibTable
tmnxWlanGwMgwArecCacheTable = _TmnxWlanGwMgwArecCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheTable.setStatus("current")
_TmnxWlanGwMgwArecCacheEntry_Object = MibTableRow
tmnxWlanGwMgwArecCacheEntry = _TmnxWlanGwMgwArecCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10, 1)
)
tmnxWlanGwMgwArecCacheEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwArecCacheApn"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwArecCacheIndex"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheEntry.setStatus("current")
_TmnxWlanGwMgwArecCacheApn_Type = TmnxMobApnDomainName
_TmnxWlanGwMgwArecCacheApn_Object = MibTableColumn
tmnxWlanGwMgwArecCacheApn = _TmnxWlanGwMgwArecCacheApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10, 1, 1),
    _TmnxWlanGwMgwArecCacheApn_Type()
)
tmnxWlanGwMgwArecCacheApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheApn.setStatus("current")
_TmnxWlanGwMgwArecCacheIndex_Type = Unsigned32
_TmnxWlanGwMgwArecCacheIndex_Object = MibTableColumn
tmnxWlanGwMgwArecCacheIndex = _TmnxWlanGwMgwArecCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10, 1, 2),
    _TmnxWlanGwMgwArecCacheIndex_Type()
)
tmnxWlanGwMgwArecCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheIndex.setStatus("current")
_TmnxWlanGwMgwArecCacheAddrType_Type = InetAddressType
_TmnxWlanGwMgwArecCacheAddrType_Object = MibTableColumn
tmnxWlanGwMgwArecCacheAddrType = _TmnxWlanGwMgwArecCacheAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10, 1, 3),
    _TmnxWlanGwMgwArecCacheAddrType_Type()
)
tmnxWlanGwMgwArecCacheAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheAddrType.setStatus("current")


class _TmnxWlanGwMgwArecCacheAddr_Type(InetAddress):
    """Custom type tmnxWlanGwMgwArecCacheAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwMgwArecCacheAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwMgwArecCacheAddr_Object = MibTableColumn
tmnxWlanGwMgwArecCacheAddr = _TmnxWlanGwMgwArecCacheAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10, 1, 4),
    _TmnxWlanGwMgwArecCacheAddr_Type()
)
tmnxWlanGwMgwArecCacheAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheAddr.setStatus("current")
_TmnxWlanGwMgwArecCacheTtl_Type = Unsigned32
_TmnxWlanGwMgwArecCacheTtl_Object = MibTableColumn
tmnxWlanGwMgwArecCacheTtl = _TmnxWlanGwMgwArecCacheTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10, 1, 5),
    _TmnxWlanGwMgwArecCacheTtl_Type()
)
tmnxWlanGwMgwArecCacheTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheTtl.setUnits("seconds")
_TmnxWlanGwMgwSnaptrCacheTable_Object = MibTable
tmnxWlanGwMgwSnaptrCacheTable = _TmnxWlanGwMgwSnaptrCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheTable.setStatus("current")
_TmnxWlanGwMgwSnaptrCacheEntry_Object = MibTableRow
tmnxWlanGwMgwSnaptrCacheEntry = _TmnxWlanGwMgwSnaptrCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1)
)
tmnxWlanGwMgwSnaptrCacheEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheApn"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheOrder"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheIndex"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheEntry.setStatus("current")
_TmnxWlanGwMgwSnaptrCacheApn_Type = TmnxMobApnDomainName
_TmnxWlanGwMgwSnaptrCacheApn_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheApn = _TmnxWlanGwMgwSnaptrCacheApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 1),
    _TmnxWlanGwMgwSnaptrCacheApn_Type()
)
tmnxWlanGwMgwSnaptrCacheApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheApn.setStatus("current")
_TmnxWlanGwMgwSnaptrCacheOrder_Type = Unsigned32
_TmnxWlanGwMgwSnaptrCacheOrder_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheOrder = _TmnxWlanGwMgwSnaptrCacheOrder_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 2),
    _TmnxWlanGwMgwSnaptrCacheOrder_Type()
)
tmnxWlanGwMgwSnaptrCacheOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheOrder.setStatus("current")
_TmnxWlanGwMgwSnaptrCacheIndex_Type = Unsigned32
_TmnxWlanGwMgwSnaptrCacheIndex_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheIndex = _TmnxWlanGwMgwSnaptrCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 3),
    _TmnxWlanGwMgwSnaptrCacheIndex_Type()
)
tmnxWlanGwMgwSnaptrCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheIndex.setStatus("current")
_TmnxWlanGwMgwSnaptrCachePref_Type = Unsigned32
_TmnxWlanGwMgwSnaptrCachePref_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCachePref = _TmnxWlanGwMgwSnaptrCachePref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 4),
    _TmnxWlanGwMgwSnaptrCachePref_Type()
)
tmnxWlanGwMgwSnaptrCachePref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCachePref.setStatus("current")


class _TmnxWlanGwMgwSnaptrCacheService_Type(TmnxMobService):
    """Custom type tmnxWlanGwMgwSnaptrCacheService based on TmnxMobService"""
    subtypeSpec = TmnxMobService.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_TmnxWlanGwMgwSnaptrCacheService_Type.__name__ = "TmnxMobService"
_TmnxWlanGwMgwSnaptrCacheService_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheService = _TmnxWlanGwMgwSnaptrCacheService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 5),
    _TmnxWlanGwMgwSnaptrCacheService_Type()
)
tmnxWlanGwMgwSnaptrCacheService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheService.setStatus("current")


class _TmnxWlanGwMgwSnaptrCacheNext_Type(Integer32):
    """Custom type tmnxWlanGwMgwSnaptrCacheNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dnsSrv", 1),
          ("dnsA", 2),
          ("dnsNaptr", 3))
    )


_TmnxWlanGwMgwSnaptrCacheNext_Type.__name__ = "Integer32"
_TmnxWlanGwMgwSnaptrCacheNext_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheNext = _TmnxWlanGwMgwSnaptrCacheNext_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 6),
    _TmnxWlanGwMgwSnaptrCacheNext_Type()
)
tmnxWlanGwMgwSnaptrCacheNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheNext.setStatus("current")
_TmnxWlanGwMgwSnaptrCacheRepl_Type = TmnxMobApnDomainName
_TmnxWlanGwMgwSnaptrCacheRepl_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheRepl = _TmnxWlanGwMgwSnaptrCacheRepl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 7),
    _TmnxWlanGwMgwSnaptrCacheRepl_Type()
)
tmnxWlanGwMgwSnaptrCacheRepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheRepl.setStatus("current")
_TmnxWlanGwMgwSnaptrCacheTtl_Type = Unsigned32
_TmnxWlanGwMgwSnaptrCacheTtl_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheTtl = _TmnxWlanGwMgwSnaptrCacheTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 8),
    _TmnxWlanGwMgwSnaptrCacheTtl_Type()
)
tmnxWlanGwMgwSnaptrCacheTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheTtl.setUnits("seconds")
_TmnxWlanGwMgwSrvCacheTable_Object = MibTable
tmnxWlanGwMgwSrvCacheTable = _TmnxWlanGwMgwSrvCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheTable.setStatus("current")
_TmnxWlanGwMgwSrvCacheEntry_Object = MibTableRow
tmnxWlanGwMgwSrvCacheEntry = _TmnxWlanGwMgwSrvCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1)
)
tmnxWlanGwMgwSrvCacheEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCacheApn"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCachePriority"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCacheIndex"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheEntry.setStatus("current")
_TmnxWlanGwMgwSrvCacheApn_Type = TmnxMobApnDomainName
_TmnxWlanGwMgwSrvCacheApn_Object = MibTableColumn
tmnxWlanGwMgwSrvCacheApn = _TmnxWlanGwMgwSrvCacheApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 1),
    _TmnxWlanGwMgwSrvCacheApn_Type()
)
tmnxWlanGwMgwSrvCacheApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheApn.setStatus("current")


class _TmnxWlanGwMgwSrvCachePriority_Type(Unsigned32):
    """Custom type tmnxWlanGwMgwSrvCachePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxWlanGwMgwSrvCachePriority_Type.__name__ = "Unsigned32"
_TmnxWlanGwMgwSrvCachePriority_Object = MibTableColumn
tmnxWlanGwMgwSrvCachePriority = _TmnxWlanGwMgwSrvCachePriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 2),
    _TmnxWlanGwMgwSrvCachePriority_Type()
)
tmnxWlanGwMgwSrvCachePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCachePriority.setStatus("current")
_TmnxWlanGwMgwSrvCacheIndex_Type = Unsigned32
_TmnxWlanGwMgwSrvCacheIndex_Object = MibTableColumn
tmnxWlanGwMgwSrvCacheIndex = _TmnxWlanGwMgwSrvCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 3),
    _TmnxWlanGwMgwSrvCacheIndex_Type()
)
tmnxWlanGwMgwSrvCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheIndex.setStatus("current")


class _TmnxWlanGwMgwSrvCacheWeight_Type(Unsigned32):
    """Custom type tmnxWlanGwMgwSrvCacheWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxWlanGwMgwSrvCacheWeight_Type.__name__ = "Unsigned32"
_TmnxWlanGwMgwSrvCacheWeight_Object = MibTableColumn
tmnxWlanGwMgwSrvCacheWeight = _TmnxWlanGwMgwSrvCacheWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 4),
    _TmnxWlanGwMgwSrvCacheWeight_Type()
)
tmnxWlanGwMgwSrvCacheWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheWeight.setStatus("current")
_TmnxWlanGwMgwSrvCachePort_Type = InetPortNumber
_TmnxWlanGwMgwSrvCachePort_Object = MibTableColumn
tmnxWlanGwMgwSrvCachePort = _TmnxWlanGwMgwSrvCachePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 5),
    _TmnxWlanGwMgwSrvCachePort_Type()
)
tmnxWlanGwMgwSrvCachePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCachePort.setStatus("current")
_TmnxWlanGwMgwSrvCacheTarget_Type = TmnxMobApnDomainName
_TmnxWlanGwMgwSrvCacheTarget_Object = MibTableColumn
tmnxWlanGwMgwSrvCacheTarget = _TmnxWlanGwMgwSrvCacheTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 6),
    _TmnxWlanGwMgwSrvCacheTarget_Type()
)
tmnxWlanGwMgwSrvCacheTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheTarget.setStatus("current")
_TmnxWlanGwMgwSrvCacheTtl_Type = Unsigned32
_TmnxWlanGwMgwSrvCacheTtl_Object = MibTableColumn
tmnxWlanGwMgwSrvCacheTtl = _TmnxWlanGwMgwSrvCacheTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 7),
    _TmnxWlanGwMgwSrvCacheTtl_Type()
)
tmnxWlanGwMgwSrvCacheTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheTtl.setUnits("seconds")
_TmnxWlanGwPgwTable_Object = MibTable
tmnxWlanGwPgwTable = _TmnxWlanGwPgwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20)
)
if mibBuilder.loadTexts:
    tmnxWlanGwPgwTable.setStatus("current")
_TmnxWlanGwPgwEntry_Object = MibTableRow
tmnxWlanGwPgwEntry = _TmnxWlanGwPgwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwPgwEntry.setStatus("current")
_TmnxWlanGwPgwLastChanged_Type = TimeStamp
_TmnxWlanGwPgwLastChanged_Object = MibTableColumn
tmnxWlanGwPgwLastChanged = _TmnxWlanGwPgwLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 1),
    _TmnxWlanGwPgwLastChanged_Type()
)
tmnxWlanGwPgwLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwLastChanged.setStatus("current")


class _TmnxWlanGwPgwQosUplinkGbrRate_Type(TmnxMobProfGbrRate):
    """Custom type tmnxWlanGwPgwQosUplinkGbrRate based on TmnxMobProfGbrRate"""
    defaultValue = 0


_TmnxWlanGwPgwQosUplinkGbrRate_Type.__name__ = "TmnxMobProfGbrRate"
_TmnxWlanGwPgwQosUplinkGbrRate_Object = MibTableColumn
tmnxWlanGwPgwQosUplinkGbrRate = _TmnxWlanGwPgwQosUplinkGbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 2),
    _TmnxWlanGwPgwQosUplinkGbrRate_Type()
)
tmnxWlanGwPgwQosUplinkGbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosUplinkGbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosUplinkGbrRate.setUnits("kilobps")


class _TmnxWlanGwPgwQosUplinkMbrRate_Type(TmnxMobProfMbrRate):
    """Custom type tmnxWlanGwPgwQosUplinkMbrRate based on TmnxMobProfMbrRate"""
    defaultValue = 0


_TmnxWlanGwPgwQosUplinkMbrRate_Type.__name__ = "TmnxMobProfMbrRate"
_TmnxWlanGwPgwQosUplinkMbrRate_Object = MibTableColumn
tmnxWlanGwPgwQosUplinkMbrRate = _TmnxWlanGwPgwQosUplinkMbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 3),
    _TmnxWlanGwPgwQosUplinkMbrRate_Type()
)
tmnxWlanGwPgwQosUplinkMbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosUplinkMbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosUplinkMbrRate.setUnits("kilobps")


class _TmnxWlanGwPgwQosDwnlinkGbrRate_Type(TmnxMobProfGbrRate):
    """Custom type tmnxWlanGwPgwQosDwnlinkGbrRate based on TmnxMobProfGbrRate"""
    defaultValue = 0


_TmnxWlanGwPgwQosDwnlinkGbrRate_Type.__name__ = "TmnxMobProfGbrRate"
_TmnxWlanGwPgwQosDwnlinkGbrRate_Object = MibTableColumn
tmnxWlanGwPgwQosDwnlinkGbrRate = _TmnxWlanGwPgwQosDwnlinkGbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 4),
    _TmnxWlanGwPgwQosDwnlinkGbrRate_Type()
)
tmnxWlanGwPgwQosDwnlinkGbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosDwnlinkGbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosDwnlinkGbrRate.setUnits("kilobps")


class _TmnxWlanGwPgwQosDwnlinkMbrRate_Type(TmnxMobProfMbrRate):
    """Custom type tmnxWlanGwPgwQosDwnlinkMbrRate based on TmnxMobProfMbrRate"""
    defaultValue = 0


_TmnxWlanGwPgwQosDwnlinkMbrRate_Type.__name__ = "TmnxMobProfMbrRate"
_TmnxWlanGwPgwQosDwnlinkMbrRate_Object = MibTableColumn
tmnxWlanGwPgwQosDwnlinkMbrRate = _TmnxWlanGwPgwQosDwnlinkMbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 5),
    _TmnxWlanGwPgwQosDwnlinkMbrRate_Type()
)
tmnxWlanGwPgwQosDwnlinkMbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosDwnlinkMbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosDwnlinkMbrRate.setUnits("kilobps")


class _TmnxWlanGwPgwQosArpValue_Type(TmnxMobArpValue):
    """Custom type tmnxWlanGwPgwQosArpValue based on TmnxMobArpValue"""
    defaultValue = 1


_TmnxWlanGwPgwQosArpValue_Type.__name__ = "TmnxMobArpValue"
_TmnxWlanGwPgwQosArpValue_Object = MibTableColumn
tmnxWlanGwPgwQosArpValue = _TmnxWlanGwPgwQosArpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 6),
    _TmnxWlanGwPgwQosArpValue_Type()
)
tmnxWlanGwPgwQosArpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosArpValue.setStatus("current")


class _TmnxWlanGwPgwQosQciValue_Type(TmnxMobQci):
    """Custom type tmnxWlanGwPgwQosQciValue based on TmnxMobQci"""
    defaultValue = 8


_TmnxWlanGwPgwQosQciValue_Type.__name__ = "TmnxMobQci"
_TmnxWlanGwPgwQosQciValue_Object = MibTableColumn
tmnxWlanGwPgwQosQciValue = _TmnxWlanGwPgwQosQciValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 7),
    _TmnxWlanGwPgwQosQciValue_Type()
)
tmnxWlanGwPgwQosQciValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosQciValue.setStatus("current")


class _TmnxWlanGwPgwQosUplinkAmbr_Type(TmnxWlanGwAmbr):
    """Custom type tmnxWlanGwPgwQosUplinkAmbr based on TmnxWlanGwAmbr"""
    defaultValue = 10000


_TmnxWlanGwPgwQosUplinkAmbr_Type.__name__ = "TmnxWlanGwAmbr"
_TmnxWlanGwPgwQosUplinkAmbr_Object = MibTableColumn
tmnxWlanGwPgwQosUplinkAmbr = _TmnxWlanGwPgwQosUplinkAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 8),
    _TmnxWlanGwPgwQosUplinkAmbr_Type()
)
tmnxWlanGwPgwQosUplinkAmbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosUplinkAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosUplinkAmbr.setUnits("kilobps")


class _TmnxWlanGwPgwQosDwnlinkAmbr_Type(TmnxWlanGwAmbr):
    """Custom type tmnxWlanGwPgwQosDwnlinkAmbr based on TmnxWlanGwAmbr"""
    defaultValue = 20000


_TmnxWlanGwPgwQosDwnlinkAmbr_Type.__name__ = "TmnxWlanGwAmbr"
_TmnxWlanGwPgwQosDwnlinkAmbr_Object = MibTableColumn
tmnxWlanGwPgwQosDwnlinkAmbr = _TmnxWlanGwPgwQosDwnlinkAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 9),
    _TmnxWlanGwPgwQosDwnlinkAmbr_Type()
)
tmnxWlanGwPgwQosDwnlinkAmbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosDwnlinkAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosDwnlinkAmbr.setUnits("kilobps")
_TmnxWlanGwGgsnTable_Object = MibTable
tmnxWlanGwGgsnTable = _TmnxWlanGwGgsnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21)
)
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnTable.setStatus("current")
_TmnxWlanGwGgsnEntry_Object = MibTableRow
tmnxWlanGwGgsnEntry = _TmnxWlanGwGgsnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnEntry.setStatus("current")
_TmnxWlanGwGgsnLastChanged_Type = TimeStamp
_TmnxWlanGwGgsnLastChanged_Object = MibTableColumn
tmnxWlanGwGgsnLastChanged = _TmnxWlanGwGgsnLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 1),
    _TmnxWlanGwGgsnLastChanged_Type()
)
tmnxWlanGwGgsnLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnLastChanged.setStatus("current")


class _TmnxWlanGwGgsnQosUplinkGbrRate_Type(TmnxMobProfGbrRate):
    """Custom type tmnxWlanGwGgsnQosUplinkGbrRate based on TmnxMobProfGbrRate"""
    defaultValue = 5000


_TmnxWlanGwGgsnQosUplinkGbrRate_Type.__name__ = "TmnxMobProfGbrRate"
_TmnxWlanGwGgsnQosUplinkGbrRate_Object = MibTableColumn
tmnxWlanGwGgsnQosUplinkGbrRate = _TmnxWlanGwGgsnQosUplinkGbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 2),
    _TmnxWlanGwGgsnQosUplinkGbrRate_Type()
)
tmnxWlanGwGgsnQosUplinkGbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosUplinkGbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosUplinkGbrRate.setUnits("kilobps")


class _TmnxWlanGwGgsnQosUplinkMbrRate_Type(TmnxMobProfMbrRate):
    """Custom type tmnxWlanGwGgsnQosUplinkMbrRate based on TmnxMobProfMbrRate"""
    defaultValue = 5000


_TmnxWlanGwGgsnQosUplinkMbrRate_Type.__name__ = "TmnxMobProfMbrRate"
_TmnxWlanGwGgsnQosUplinkMbrRate_Object = MibTableColumn
tmnxWlanGwGgsnQosUplinkMbrRate = _TmnxWlanGwGgsnQosUplinkMbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 3),
    _TmnxWlanGwGgsnQosUplinkMbrRate_Type()
)
tmnxWlanGwGgsnQosUplinkMbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosUplinkMbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosUplinkMbrRate.setUnits("kilobps")


class _TmnxWlanGwGgsnQosDwnlinkGbrRate_Type(TmnxMobProfGbrRate):
    """Custom type tmnxWlanGwGgsnQosDwnlinkGbrRate based on TmnxMobProfGbrRate"""
    defaultValue = 2000


_TmnxWlanGwGgsnQosDwnlinkGbrRate_Type.__name__ = "TmnxMobProfGbrRate"
_TmnxWlanGwGgsnQosDwnlinkGbrRate_Object = MibTableColumn
tmnxWlanGwGgsnQosDwnlinkGbrRate = _TmnxWlanGwGgsnQosDwnlinkGbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 4),
    _TmnxWlanGwGgsnQosDwnlinkGbrRate_Type()
)
tmnxWlanGwGgsnQosDwnlinkGbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosDwnlinkGbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosDwnlinkGbrRate.setUnits("kilobps")


class _TmnxWlanGwGgsnQosDwnlinkMbrRate_Type(TmnxMobProfMbrRate):
    """Custom type tmnxWlanGwGgsnQosDwnlinkMbrRate based on TmnxMobProfMbrRate"""
    defaultValue = 2000


_TmnxWlanGwGgsnQosDwnlinkMbrRate_Type.__name__ = "TmnxMobProfMbrRate"
_TmnxWlanGwGgsnQosDwnlinkMbrRate_Object = MibTableColumn
tmnxWlanGwGgsnQosDwnlinkMbrRate = _TmnxWlanGwGgsnQosDwnlinkMbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 5),
    _TmnxWlanGwGgsnQosDwnlinkMbrRate_Type()
)
tmnxWlanGwGgsnQosDwnlinkMbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosDwnlinkMbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosDwnlinkMbrRate.setUnits("kilobps")


class _TmnxWlanGwGgsnQosArpValue_Type(TmnxMobArpValue):
    """Custom type tmnxWlanGwGgsnQosArpValue based on TmnxMobArpValue"""
    defaultValue = 1

    subtypeSpec = TmnxMobArpValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TmnxWlanGwGgsnQosArpValue_Type.__name__ = "TmnxMobArpValue"
_TmnxWlanGwGgsnQosArpValue_Object = MibTableColumn
tmnxWlanGwGgsnQosArpValue = _TmnxWlanGwGgsnQosArpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 6),
    _TmnxWlanGwGgsnQosArpValue_Type()
)
tmnxWlanGwGgsnQosArpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosArpValue.setStatus("current")


class _TmnxWlanGwGgsnQosUplinkAmbr_Type(TmnxWlanGwAmbr):
    """Custom type tmnxWlanGwGgsnQosUplinkAmbr based on TmnxWlanGwAmbr"""
    defaultValue = -2


_TmnxWlanGwGgsnQosUplinkAmbr_Type.__name__ = "TmnxWlanGwAmbr"
_TmnxWlanGwGgsnQosUplinkAmbr_Object = MibTableColumn
tmnxWlanGwGgsnQosUplinkAmbr = _TmnxWlanGwGgsnQosUplinkAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 7),
    _TmnxWlanGwGgsnQosUplinkAmbr_Type()
)
tmnxWlanGwGgsnQosUplinkAmbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosUplinkAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosUplinkAmbr.setUnits("kilobps")


class _TmnxWlanGwGgsnQosDwnlinkAmbr_Type(TmnxWlanGwAmbr):
    """Custom type tmnxWlanGwGgsnQosDwnlinkAmbr based on TmnxWlanGwAmbr"""
    defaultValue = -2


_TmnxWlanGwGgsnQosDwnlinkAmbr_Type.__name__ = "TmnxWlanGwAmbr"
_TmnxWlanGwGgsnQosDwnlinkAmbr_Object = MibTableColumn
tmnxWlanGwGgsnQosDwnlinkAmbr = _TmnxWlanGwGgsnQosDwnlinkAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 8),
    _TmnxWlanGwGgsnQosDwnlinkAmbr_Type()
)
tmnxWlanGwGgsnQosDwnlinkAmbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosDwnlinkAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosDwnlinkAmbr.setUnits("kilobps")
_TmnxWlanGwMmeTable_Object = MibTable
tmnxWlanGwMmeTable = _TmnxWlanGwMmeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 22)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMmeTable.setStatus("current")
_TmnxWlanGwMmeEntry_Object = MibTableRow
tmnxWlanGwMmeEntry = _TmnxWlanGwMmeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 22, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMmeEntry.setStatus("current")
_TmnxWlanGwMmeLastChanged_Type = TimeStamp
_TmnxWlanGwMmeLastChanged_Object = MibTableColumn
tmnxWlanGwMmeLastChanged = _TmnxWlanGwMmeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 22, 1, 1),
    _TmnxWlanGwMmeLastChanged_Type()
)
tmnxWlanGwMmeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeLastChanged.setStatus("current")


class _TmnxWlanGwMmeQosUplinkGbrRate_Type(TmnxMobProfGbrRate):
    """Custom type tmnxWlanGwMmeQosUplinkGbrRate based on TmnxMobProfGbrRate"""
    defaultValue = 0


_TmnxWlanGwMmeQosUplinkGbrRate_Type.__name__ = "TmnxMobProfGbrRate"
_TmnxWlanGwMmeQosUplinkGbrRate_Object = MibTableColumn
tmnxWlanGwMmeQosUplinkGbrRate = _TmnxWlanGwMmeQosUplinkGbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 22, 1, 2),
    _TmnxWlanGwMmeQosUplinkGbrRate_Type()
)
tmnxWlanGwMmeQosUplinkGbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosUplinkGbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosUplinkGbrRate.setUnits("kilobps")


class _TmnxWlanGwMmeQosUplinkMbrRate_Type(TmnxMobProfMbrRate):
    """Custom type tmnxWlanGwMmeQosUplinkMbrRate based on TmnxMobProfMbrRate"""
    defaultValue = 0


_TmnxWlanGwMmeQosUplinkMbrRate_Type.__name__ = "TmnxMobProfMbrRate"
_TmnxWlanGwMmeQosUplinkMbrRate_Object = MibTableColumn
tmnxWlanGwMmeQosUplinkMbrRate = _TmnxWlanGwMmeQosUplinkMbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 22, 1, 3),
    _TmnxWlanGwMmeQosUplinkMbrRate_Type()
)
tmnxWlanGwMmeQosUplinkMbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosUplinkMbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosUplinkMbrRate.setUnits("kilobps")


class _TmnxWlanGwMmeQosDwnlinkGbrRate_Type(TmnxMobProfGbrRate):
    """Custom type tmnxWlanGwMmeQosDwnlinkGbrRate based on TmnxMobProfGbrRate"""
    defaultValue = 0


_TmnxWlanGwMmeQosDwnlinkGbrRate_Type.__name__ = "TmnxMobProfGbrRate"
_TmnxWlanGwMmeQosDwnlinkGbrRate_Object = MibTableColumn
tmnxWlanGwMmeQosDwnlinkGbrRate = _TmnxWlanGwMmeQosDwnlinkGbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 22, 1, 4),
    _TmnxWlanGwMmeQosDwnlinkGbrRate_Type()
)
tmnxWlanGwMmeQosDwnlinkGbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosDwnlinkGbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosDwnlinkGbrRate.setUnits("kilobps")


class _TmnxWlanGwMmeQosDwnlinkMbrRate_Type(TmnxMobProfMbrRate):
    """Custom type tmnxWlanGwMmeQosDwnlinkMbrRate based on TmnxMobProfMbrRate"""
    defaultValue = 0


_TmnxWlanGwMmeQosDwnlinkMbrRate_Type.__name__ = "TmnxMobProfMbrRate"
_TmnxWlanGwMmeQosDwnlinkMbrRate_Object = MibTableColumn
tmnxWlanGwMmeQosDwnlinkMbrRate = _TmnxWlanGwMmeQosDwnlinkMbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 22, 1, 5),
    _TmnxWlanGwMmeQosDwnlinkMbrRate_Type()
)
tmnxWlanGwMmeQosDwnlinkMbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosDwnlinkMbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosDwnlinkMbrRate.setUnits("kilobps")


class _TmnxWlanGwMmeQosArpValue_Type(TmnxMobArpValue):
    """Custom type tmnxWlanGwMmeQosArpValue based on TmnxMobArpValue"""
    defaultValue = 1


_TmnxWlanGwMmeQosArpValue_Type.__name__ = "TmnxMobArpValue"
_TmnxWlanGwMmeQosArpValue_Object = MibTableColumn
tmnxWlanGwMmeQosArpValue = _TmnxWlanGwMmeQosArpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 22, 1, 6),
    _TmnxWlanGwMmeQosArpValue_Type()
)
tmnxWlanGwMmeQosArpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosArpValue.setStatus("current")


class _TmnxWlanGwMmeQosQciValue_Type(TmnxMobQciValue):
    """Custom type tmnxWlanGwMmeQosQciValue based on TmnxMobQciValue"""
    defaultValue = 8


_TmnxWlanGwMmeQosQciValue_Type.__name__ = "TmnxMobQciValue"
_TmnxWlanGwMmeQosQciValue_Object = MibTableColumn
tmnxWlanGwMmeQosQciValue = _TmnxWlanGwMmeQosQciValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 22, 1, 7),
    _TmnxWlanGwMmeQosQciValue_Type()
)
tmnxWlanGwMmeQosQciValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosQciValue.setStatus("current")


class _TmnxWlanGwMmeQosUplinkAmbr_Type(TmnxWlanGwAmbr):
    """Custom type tmnxWlanGwMmeQosUplinkAmbr based on TmnxWlanGwAmbr"""
    defaultValue = 10000


_TmnxWlanGwMmeQosUplinkAmbr_Type.__name__ = "TmnxWlanGwAmbr"
_TmnxWlanGwMmeQosUplinkAmbr_Object = MibTableColumn
tmnxWlanGwMmeQosUplinkAmbr = _TmnxWlanGwMmeQosUplinkAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 22, 1, 8),
    _TmnxWlanGwMmeQosUplinkAmbr_Type()
)
tmnxWlanGwMmeQosUplinkAmbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosUplinkAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosUplinkAmbr.setUnits("kilobps")


class _TmnxWlanGwMmeQosDwnlinkAmbr_Type(TmnxWlanGwAmbr):
    """Custom type tmnxWlanGwMmeQosDwnlinkAmbr based on TmnxWlanGwAmbr"""
    defaultValue = 20000


_TmnxWlanGwMmeQosDwnlinkAmbr_Type.__name__ = "TmnxWlanGwAmbr"
_TmnxWlanGwMmeQosDwnlinkAmbr_Object = MibTableColumn
tmnxWlanGwMmeQosDwnlinkAmbr = _TmnxWlanGwMmeQosDwnlinkAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 22, 1, 9),
    _TmnxWlanGwMmeQosDwnlinkAmbr_Type()
)
tmnxWlanGwMmeQosDwnlinkAmbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosDwnlinkAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeQosDwnlinkAmbr.setUnits("kilobps")
_TmnxWlanGwSysCfgObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwSysCfgObjs = _TmnxWlanGwSysCfgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 7)
)


class _TmnxWlanGwSysCfgServingNwMcc_Type(TmnxMobMccOrEmpty):
    """Custom type tmnxWlanGwSysCfgServingNwMcc based on TmnxMobMccOrEmpty"""
    defaultHexValue = ""


_TmnxWlanGwSysCfgServingNwMcc_Type.__name__ = "TmnxMobMccOrEmpty"
_TmnxWlanGwSysCfgServingNwMcc_Object = MibScalar
tmnxWlanGwSysCfgServingNwMcc = _TmnxWlanGwSysCfgServingNwMcc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 7, 1),
    _TmnxWlanGwSysCfgServingNwMcc_Type()
)
tmnxWlanGwSysCfgServingNwMcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanGwSysCfgServingNwMcc.setStatus("current")


class _TmnxWlanGwSysCfgServingNwMnc_Type(TmnxMobMncOrEmpty):
    """Custom type tmnxWlanGwSysCfgServingNwMnc based on TmnxMobMncOrEmpty"""
    defaultHexValue = ""


_TmnxWlanGwSysCfgServingNwMnc_Type.__name__ = "TmnxMobMncOrEmpty"
_TmnxWlanGwSysCfgServingNwMnc_Object = MibScalar
tmnxWlanGwSysCfgServingNwMnc = _TmnxWlanGwSysCfgServingNwMnc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 7, 2),
    _TmnxWlanGwSysCfgServingNwMnc_Type()
)
tmnxWlanGwSysCfgServingNwMnc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanGwSysCfgServingNwMnc.setStatus("current")


class _TmnxWlanGwSysCfgMgwMaxHeldSe_Type(Unsigned32):
    """Custom type tmnxWlanGwSysCfgMgwMaxHeldSe based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_TmnxWlanGwSysCfgMgwMaxHeldSe_Type.__name__ = "Unsigned32"
_TmnxWlanGwSysCfgMgwMaxHeldSe_Object = MibScalar
tmnxWlanGwSysCfgMgwMaxHeldSe = _TmnxWlanGwSysCfgMgwMaxHeldSe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 7, 5),
    _TmnxWlanGwSysCfgMgwMaxHeldSe_Type()
)
tmnxWlanGwSysCfgMgwMaxHeldSe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanGwSysCfgMgwMaxHeldSe.setStatus("current")


class _TmnxWlanGwSysCfgVirtChassisId_Type(DisplayString):
    """Custom type tmnxWlanGwSysCfgVirtChassisId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxWlanGwSysCfgVirtChassisId_Type.__name__ = "DisplayString"
_TmnxWlanGwSysCfgVirtChassisId_Object = MibScalar
tmnxWlanGwSysCfgVirtChassisId = _TmnxWlanGwSysCfgVirtChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 7, 15),
    _TmnxWlanGwSysCfgVirtChassisId_Type()
)
tmnxWlanGwSysCfgVirtChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanGwSysCfgVirtChassisId.setStatus("current")
_TmnxWlanGwTable_Object = MibTable
tmnxWlanGwTable = _TmnxWlanGwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxWlanGwTable.setStatus("current")
_TmnxWlanGwEntry_Object = MibTableRow
tmnxWlanGwEntry = _TmnxWlanGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1)
)
tmnxWlanGwEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwEntry.setStatus("current")
_TmnxWlanGwRowStatus_Type = RowStatus
_TmnxWlanGwRowStatus_Object = MibTableColumn
tmnxWlanGwRowStatus = _TmnxWlanGwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1, 1),
    _TmnxWlanGwRowStatus_Type()
)
tmnxWlanGwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwRowStatus.setStatus("current")
_TmnxWlanGwLastCh_Type = TimeStamp
_TmnxWlanGwLastCh_Object = MibTableColumn
tmnxWlanGwLastCh = _TmnxWlanGwLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1, 2),
    _TmnxWlanGwLastCh_Type()
)
tmnxWlanGwLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwLastCh.setStatus("current")


class _TmnxWlanGwApn_Type(TmnxMobApnOrZero):
    """Custom type tmnxWlanGwApn based on TmnxMobApnOrZero"""
    defaultValue = OctetString("")

    subtypeSpec = TmnxMobApnOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxWlanGwApn_Type.__name__ = "TmnxMobApnOrZero"
_TmnxWlanGwApn_Object = MibTableColumn
tmnxWlanGwApn = _TmnxWlanGwApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1, 3),
    _TmnxWlanGwApn_Type()
)
tmnxWlanGwApn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwApn.setStatus("current")


class _TmnxWlanGwMobAcctInterimUpdate_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwMobAcctInterimUpdate based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwMobAcctInterimUpdate_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwMobAcctInterimUpdate_Object = MibTableColumn
tmnxWlanGwMobAcctInterimUpdate = _TmnxWlanGwMobAcctInterimUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1, 10),
    _TmnxWlanGwMobAcctInterimUpdate_Type()
)
tmnxWlanGwMobAcctInterimUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMobAcctInterimUpdate.setStatus("current")


class _TmnxWlanGwPdnType_Type(Integer32):
    """Custom type tmnxWlanGwPdnType based on Integer32"""
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
        *(("ipv4", 0),
          ("ipv6", 1),
          ("ipv4v6", 2))
    )


_TmnxWlanGwPdnType_Type.__name__ = "Integer32"
_TmnxWlanGwPdnType_Object = MibTableColumn
tmnxWlanGwPdnType = _TmnxWlanGwPdnType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1, 11),
    _TmnxWlanGwPdnType_Type()
)
tmnxWlanGwPdnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPdnType.setStatus("current")


class _TmnxWlanGwMobAcctIntUpdtInclCnts_Type(TruthValue):
    """Custom type tmnxWlanGwMobAcctIntUpdtInclCnts based on TruthValue"""
    defaultValue = 2


_TmnxWlanGwMobAcctIntUpdtInclCnts_Type.__name__ = "TruthValue"
_TmnxWlanGwMobAcctIntUpdtInclCnts_Object = MibTableColumn
tmnxWlanGwMobAcctIntUpdtInclCnts = _TmnxWlanGwMobAcctIntUpdtInclCnts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1, 12),
    _TmnxWlanGwMobAcctIntUpdtInclCnts_Type()
)
tmnxWlanGwMobAcctIntUpdtInclCnts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMobAcctIntUpdtInclCnts.setStatus("current")


class _TmnxWlanGwMobAcctIntUpdtHoldDown_Type(Unsigned32):
    """Custom type tmnxWlanGwMobAcctIntUpdtHoldDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 86400),
    )


_TmnxWlanGwMobAcctIntUpdtHoldDown_Type.__name__ = "Unsigned32"
_TmnxWlanGwMobAcctIntUpdtHoldDown_Object = MibTableColumn
tmnxWlanGwMobAcctIntUpdtHoldDown = _TmnxWlanGwMobAcctIntUpdtHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1, 13),
    _TmnxWlanGwMobAcctIntUpdtHoldDown_Type()
)
tmnxWlanGwMobAcctIntUpdtHoldDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMobAcctIntUpdtHoldDown.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMobAcctIntUpdtHoldDown.setUnits("seconds")
_TmnxWlanGwDsmSubObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwDsmSubObjs = _TmnxWlanGwDsmSubObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9)
)
_TmnxWlanGwVlanDsmTable_Object = MibTable
tmnxWlanGwVlanDsmTable = _TmnxWlanGwVlanDsmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmTable.setStatus("current")
_TmnxWlanGwVlanDsmEntry_Object = MibTableRow
tmnxWlanGwVlanDsmEntry = _TmnxWlanGwVlanDsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmEntry.setStatus("current")
_TmnxWlanGwVlanDsmLastCh_Type = TimeStamp
_TmnxWlanGwVlanDsmLastCh_Object = MibTableColumn
tmnxWlanGwVlanDsmLastCh = _TmnxWlanGwVlanDsmLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 1),
    _TmnxWlanGwVlanDsmLastCh_Type()
)
tmnxWlanGwVlanDsmLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmLastCh.setStatus("current")


class _TmnxWlanGwVlanDsmAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanDsmAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanDsmAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanDsmAdminState_Object = MibTableColumn
tmnxWlanGwVlanDsmAdminState = _TmnxWlanGwVlanDsmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 2),
    _TmnxWlanGwVlanDsmAdminState_Type()
)
tmnxWlanGwVlanDsmAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmAdminState.setStatus("current")


class _TmnxWlanGwVlanDsmAcctPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanDsmAcctPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanDsmAcctPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanDsmAcctPlcy_Object = MibTableColumn
tmnxWlanGwVlanDsmAcctPlcy = _TmnxWlanGwVlanDsmAcctPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 3),
    _TmnxWlanGwVlanDsmAcctPlcy_Type()
)
tmnxWlanGwVlanDsmAcctPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmAcctPlcy.setStatus("current")


class _TmnxWlanGwVlanDsmEgressPolicer_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanDsmEgressPolicer based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanDsmEgressPolicer_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanDsmEgressPolicer_Object = MibTableColumn
tmnxWlanGwVlanDsmEgressPolicer = _TmnxWlanGwVlanDsmEgressPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 4),
    _TmnxWlanGwVlanDsmEgressPolicer_Type()
)
tmnxWlanGwVlanDsmEgressPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmEgressPolicer.setStatus("current")


class _TmnxWlanGwVlanDsmIngressPolicer_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanDsmIngressPolicer based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanDsmIngressPolicer_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanDsmIngressPolicer_Object = MibTableColumn
tmnxWlanGwVlanDsmIngressPolicer = _TmnxWlanGwVlanDsmIngressPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 5),
    _TmnxWlanGwVlanDsmIngressPolicer_Type()
)
tmnxWlanGwVlanDsmIngressPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmIngressPolicer.setStatus("current")


class _TmnxWlanGwVlanDsmIpFilter_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanDsmIpFilter based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanDsmIpFilter_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanDsmIpFilter_Object = MibTableColumn
tmnxWlanGwVlanDsmIpFilter = _TmnxWlanGwVlanDsmIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 6),
    _TmnxWlanGwVlanDsmIpFilter_Type()
)
tmnxWlanGwVlanDsmIpFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmIpFilter.setStatus("current")


class _TmnxWlanGwVlanDsmOneTimeRdrUrl_Type(TmnxHttpRedirectUrl):
    """Custom type tmnxWlanGwVlanDsmOneTimeRdrUrl based on TmnxHttpRedirectUrl"""
    defaultHexValue = ""


_TmnxWlanGwVlanDsmOneTimeRdrUrl_Type.__name__ = "TmnxHttpRedirectUrl"
_TmnxWlanGwVlanDsmOneTimeRdrUrl_Object = MibTableColumn
tmnxWlanGwVlanDsmOneTimeRdrUrl = _TmnxWlanGwVlanDsmOneTimeRdrUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 7),
    _TmnxWlanGwVlanDsmOneTimeRdrUrl_Type()
)
tmnxWlanGwVlanDsmOneTimeRdrUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmOneTimeRdrUrl.setStatus("current")


class _TmnxWlanGwVlanDsmOneTimeRdrPort_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanDsmOneTimeRdrPort based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxWlanGwVlanDsmOneTimeRdrPort_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanDsmOneTimeRdrPort_Object = MibTableColumn
tmnxWlanGwVlanDsmOneTimeRdrPort = _TmnxWlanGwVlanDsmOneTimeRdrPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 8),
    _TmnxWlanGwVlanDsmOneTimeRdrPort_Type()
)
tmnxWlanGwVlanDsmOneTimeRdrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmOneTimeRdrPort.setStatus("current")


class _TmnxWlanGwVlanDsmAcctUpdInterv_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanDsmAcctUpdInterv based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 259200),
    )


_TmnxWlanGwVlanDsmAcctUpdInterv_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanDsmAcctUpdInterv_Object = MibTableColumn
tmnxWlanGwVlanDsmAcctUpdInterv = _TmnxWlanGwVlanDsmAcctUpdInterv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 9),
    _TmnxWlanGwVlanDsmAcctUpdInterv_Type()
)
tmnxWlanGwVlanDsmAcctUpdInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmAcctUpdInterv.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmAcctUpdInterv.setUnits("minutes")


class _TmnxWlanGwVlanDsmDefAppProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanDsmDefAppProfile based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanDsmDefAppProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanDsmDefAppProfile_Object = MibTableColumn
tmnxWlanGwVlanDsmDefAppProfile = _TmnxWlanGwVlanDsmDefAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 10),
    _TmnxWlanGwVlanDsmDefAppProfile_Type()
)
tmnxWlanGwVlanDsmDefAppProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmDefAppProfile.setStatus("current")


class _TmnxWlanGwVlanDsmAaAcctStats_Type(TruthValue):
    """Custom type tmnxWlanGwVlanDsmAaAcctStats based on TruthValue"""
    defaultValue = 2


_TmnxWlanGwVlanDsmAaAcctStats_Type.__name__ = "TruthValue"
_TmnxWlanGwVlanDsmAaAcctStats_Object = MibTableColumn
tmnxWlanGwVlanDsmAaAcctStats = _TmnxWlanGwVlanDsmAaAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 11),
    _TmnxWlanGwVlanDsmAaAcctStats_Type()
)
tmnxWlanGwVlanDsmAaAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmAaAcctStats.setStatus("current")
_TmnxWlanGwDsmIpFilTable_Object = MibTable
tmnxWlanGwDsmIpFilTable = _TmnxWlanGwDsmIpFilTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2)
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilTable.setStatus("current")
_TmnxWlanGwDsmIpFilEntry_Object = MibTableRow
tmnxWlanGwDsmIpFilEntry = _TmnxWlanGwDsmIpFilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1)
)
tmnxWlanGwDsmIpFilEntry.setIndexNames(
    (1, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilName"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilEntry.setStatus("current")
_TmnxWlanGwDsmIpFilName_Type = TNamedItem
_TmnxWlanGwDsmIpFilName_Object = MibTableColumn
tmnxWlanGwDsmIpFilName = _TmnxWlanGwDsmIpFilName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1, 1),
    _TmnxWlanGwDsmIpFilName_Type()
)
tmnxWlanGwDsmIpFilName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilName.setStatus("current")
_TmnxWlanGwDsmIpFilRowStatus_Type = RowStatus
_TmnxWlanGwDsmIpFilRowStatus_Object = MibTableColumn
tmnxWlanGwDsmIpFilRowStatus = _TmnxWlanGwDsmIpFilRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1, 2),
    _TmnxWlanGwDsmIpFilRowStatus_Type()
)
tmnxWlanGwDsmIpFilRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilRowStatus.setStatus("current")
_TmnxWlanGwDsmIpFilLastCh_Type = TimeStamp
_TmnxWlanGwDsmIpFilLastCh_Object = MibTableColumn
tmnxWlanGwDsmIpFilLastCh = _TmnxWlanGwDsmIpFilLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1, 3),
    _TmnxWlanGwDsmIpFilLastCh_Type()
)
tmnxWlanGwDsmIpFilLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilLastCh.setStatus("current")


class _TmnxWlanGwDsmIpFilDescription_Type(TItemDescription):
    """Custom type tmnxWlanGwDsmIpFilDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWlanGwDsmIpFilDescription_Type.__name__ = "TItemDescription"
_TmnxWlanGwDsmIpFilDescription_Object = MibTableColumn
tmnxWlanGwDsmIpFilDescription = _TmnxWlanGwDsmIpFilDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1, 4),
    _TmnxWlanGwDsmIpFilDescription_Type()
)
tmnxWlanGwDsmIpFilDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilDescription.setStatus("current")


class _TmnxWlanGwDsmIpFilDefaultAction_Type(TmnxWlanGwDsmFilterDefaultAction):
    """Custom type tmnxWlanGwDsmIpFilDefaultAction based on TmnxWlanGwDsmFilterDefaultAction"""
    defaultValue = 1


_TmnxWlanGwDsmIpFilDefaultAction_Type.__name__ = "TmnxWlanGwDsmFilterDefaultAction"
_TmnxWlanGwDsmIpFilDefaultAction_Object = MibTableColumn
tmnxWlanGwDsmIpFilDefaultAction = _TmnxWlanGwDsmIpFilDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1, 5),
    _TmnxWlanGwDsmIpFilDefaultAction_Type()
)
tmnxWlanGwDsmIpFilDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilDefaultAction.setStatus("current")


class _TmnxWlanGwDsmIpFilDefaultAction6_Type(TmnxWlanGwDsmFilterDefaultAction):
    """Custom type tmnxWlanGwDsmIpFilDefaultAction6 based on TmnxWlanGwDsmFilterDefaultAction"""
    defaultValue = 1


_TmnxWlanGwDsmIpFilDefaultAction6_Type.__name__ = "TmnxWlanGwDsmFilterDefaultAction"
_TmnxWlanGwDsmIpFilDefaultAction6_Object = MibTableColumn
tmnxWlanGwDsmIpFilDefaultAction6 = _TmnxWlanGwDsmIpFilDefaultAction6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1, 6),
    _TmnxWlanGwDsmIpFilDefaultAction6_Type()
)
tmnxWlanGwDsmIpFilDefaultAction6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilDefaultAction6.setStatus("current")


class _TmnxWlanGwDsmIpFilType_Type(Integer32):
    """Custom type tmnxWlanGwDsmIpFilType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dsm", 0),
          ("reserved1", 1))
    )


_TmnxWlanGwDsmIpFilType_Type.__name__ = "Integer32"
_TmnxWlanGwDsmIpFilType_Object = MibTableColumn
tmnxWlanGwDsmIpFilType = _TmnxWlanGwDsmIpFilType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1, 7),
    _TmnxWlanGwDsmIpFilType_Type()
)
tmnxWlanGwDsmIpFilType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilType.setStatus("current")
_TmnxWlanGwDsmIpFilN3Table_Object = MibTable
tmnxWlanGwDsmIpFilN3Table = _TmnxWlanGwDsmIpFilN3Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3Table.setStatus("current")
_TmnxWlanGwDsmIpFilN3Entry_Object = MibTableRow
tmnxWlanGwDsmIpFilN3Entry = _TmnxWlanGwDsmIpFilN3Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1)
)
tmnxWlanGwDsmIpFilN3Entry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilName"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3Index"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3Entry.setStatus("current")


class _TmnxWlanGwDsmIpFilN3Index_Type(Unsigned32):
    """Custom type tmnxWlanGwDsmIpFilN3Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TmnxWlanGwDsmIpFilN3Index_Type.__name__ = "Unsigned32"
_TmnxWlanGwDsmIpFilN3Index_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3Index = _TmnxWlanGwDsmIpFilN3Index_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 1),
    _TmnxWlanGwDsmIpFilN3Index_Type()
)
tmnxWlanGwDsmIpFilN3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3Index.setStatus("current")
_TmnxWlanGwDsmIpFilN3RowStatus_Type = RowStatus
_TmnxWlanGwDsmIpFilN3RowStatus_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3RowStatus = _TmnxWlanGwDsmIpFilN3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 2),
    _TmnxWlanGwDsmIpFilN3RowStatus_Type()
)
tmnxWlanGwDsmIpFilN3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3RowStatus.setStatus("current")
_TmnxWlanGwDsmIpFilN3LastCh_Type = TimeStamp
_TmnxWlanGwDsmIpFilN3LastCh_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3LastCh = _TmnxWlanGwDsmIpFilN3LastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 3),
    _TmnxWlanGwDsmIpFilN3LastCh_Type()
)
tmnxWlanGwDsmIpFilN3LastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3LastCh.setStatus("current")


class _TmnxWlanGwDsmIpFilN3Description_Type(TItemDescription):
    """Custom type tmnxWlanGwDsmIpFilN3Description based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWlanGwDsmIpFilN3Description_Type.__name__ = "TItemDescription"
_TmnxWlanGwDsmIpFilN3Description_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3Description = _TmnxWlanGwDsmIpFilN3Description_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 4),
    _TmnxWlanGwDsmIpFilN3Description_Type()
)
tmnxWlanGwDsmIpFilN3Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3Description.setStatus("current")


class _TmnxWlanGwDsmIpFilN3Action_Type(TmnxWlanGwDsmFilterAction):
    """Custom type tmnxWlanGwDsmIpFilN3Action based on TmnxWlanGwDsmFilterAction"""
    defaultValue = 0


_TmnxWlanGwDsmIpFilN3Action_Type.__name__ = "TmnxWlanGwDsmFilterAction"
_TmnxWlanGwDsmIpFilN3Action_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3Action = _TmnxWlanGwDsmIpFilN3Action_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 5),
    _TmnxWlanGwDsmIpFilN3Action_Type()
)
tmnxWlanGwDsmIpFilN3Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3Action.setStatus("current")


class _TmnxWlanGwDsmIpFilN3Protocol_Type(TIpProtocol):
    """Custom type tmnxWlanGwDsmIpFilN3Protocol based on TIpProtocol"""
    defaultValue = -1


_TmnxWlanGwDsmIpFilN3Protocol_Type.__name__ = "TIpProtocol"
_TmnxWlanGwDsmIpFilN3Protocol_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3Protocol = _TmnxWlanGwDsmIpFilN3Protocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 6),
    _TmnxWlanGwDsmIpFilN3Protocol_Type()
)
tmnxWlanGwDsmIpFilN3Protocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3Protocol.setStatus("current")


class _TmnxWlanGwDsmIpFilN3DestAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwDsmIpFilN3DestAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwDsmIpFilN3DestAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwDsmIpFilN3DestAddrType_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3DestAddrType = _TmnxWlanGwDsmIpFilN3DestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 7),
    _TmnxWlanGwDsmIpFilN3DestAddrType_Type()
)
tmnxWlanGwDsmIpFilN3DestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3DestAddrType.setStatus("current")


class _TmnxWlanGwDsmIpFilN3DestAddr_Type(InetAddress):
    """Custom type tmnxWlanGwDsmIpFilN3DestAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxWlanGwDsmIpFilN3DestAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwDsmIpFilN3DestAddr_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3DestAddr = _TmnxWlanGwDsmIpFilN3DestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 8),
    _TmnxWlanGwDsmIpFilN3DestAddr_Type()
)
tmnxWlanGwDsmIpFilN3DestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3DestAddr.setStatus("current")


class _TmnxWlanGwDsmIpFilN3DestPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxWlanGwDsmIpFilN3DestPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxWlanGwDsmIpFilN3DestPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxWlanGwDsmIpFilN3DestPrefLen_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3DestPrefLen = _TmnxWlanGwDsmIpFilN3DestPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 9),
    _TmnxWlanGwDsmIpFilN3DestPrefLen_Type()
)
tmnxWlanGwDsmIpFilN3DestPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3DestPrefLen.setStatus("current")


class _TmnxWlanGwDsmIpFilN3DestPortOp_Type(Integer32):
    """Custom type tmnxWlanGwDsmIpFilN3DestPortOp based on Integer32"""
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
          ("eq", 1))
    )


_TmnxWlanGwDsmIpFilN3DestPortOp_Type.__name__ = "Integer32"
_TmnxWlanGwDsmIpFilN3DestPortOp_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3DestPortOp = _TmnxWlanGwDsmIpFilN3DestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 10),
    _TmnxWlanGwDsmIpFilN3DestPortOp_Type()
)
tmnxWlanGwDsmIpFilN3DestPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3DestPortOp.setStatus("current")


class _TmnxWlanGwDsmIpFilN3DestPort1_Type(InetPortNumber):
    """Custom type tmnxWlanGwDsmIpFilN3DestPort1 based on InetPortNumber"""
    defaultValue = 0


_TmnxWlanGwDsmIpFilN3DestPort1_Type.__name__ = "InetPortNumber"
_TmnxWlanGwDsmIpFilN3DestPort1_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3DestPort1 = _TmnxWlanGwDsmIpFilN3DestPort1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 11),
    _TmnxWlanGwDsmIpFilN3DestPort1_Type()
)
tmnxWlanGwDsmIpFilN3DestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3DestPort1.setStatus("current")
_TmnxWlanGwDsmIpFilN3IngHitCount_Type = Counter64
_TmnxWlanGwDsmIpFilN3IngHitCount_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3IngHitCount = _TmnxWlanGwDsmIpFilN3IngHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 17),
    _TmnxWlanGwDsmIpFilN3IngHitCount_Type()
)
tmnxWlanGwDsmIpFilN3IngHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3IngHitCount.setStatus("current")


class _TmnxWlanGwDsmIpFilN3RedirectURL_Type(TmnxHttpRedirectUrl):
    """Custom type tmnxWlanGwDsmIpFilN3RedirectURL based on TmnxHttpRedirectUrl"""
    defaultHexValue = ""


_TmnxWlanGwDsmIpFilN3RedirectURL_Type.__name__ = "TmnxHttpRedirectUrl"
_TmnxWlanGwDsmIpFilN3RedirectURL_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3RedirectURL = _TmnxWlanGwDsmIpFilN3RedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 18),
    _TmnxWlanGwDsmIpFilN3RedirectURL_Type()
)
tmnxWlanGwDsmIpFilN3RedirectURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3RedirectURL.setStatus("current")
_TmnxWlanGwPolicerTable_Object = MibTable
tmnxWlanGwPolicerTable = _TmnxWlanGwPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerTable.setStatus("current")
_TmnxWlanGwPolicerEntry_Object = MibTableRow
tmnxWlanGwPolicerEntry = _TmnxWlanGwPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1)
)
tmnxWlanGwPolicerEntry.setIndexNames(
    (1, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerName"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerEntry.setStatus("current")
_TmnxWlanGwPolicerName_Type = TNamedItem
_TmnxWlanGwPolicerName_Object = MibTableColumn
tmnxWlanGwPolicerName = _TmnxWlanGwPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 1),
    _TmnxWlanGwPolicerName_Type()
)
tmnxWlanGwPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerName.setStatus("current")
_TmnxWlanGwPolicerRowLastChange_Type = TimeStamp
_TmnxWlanGwPolicerRowLastChange_Object = MibTableColumn
tmnxWlanGwPolicerRowLastChange = _TmnxWlanGwPolicerRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 2),
    _TmnxWlanGwPolicerRowLastChange_Type()
)
tmnxWlanGwPolicerRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerRowLastChange.setStatus("current")
_TmnxWlanGwPolicerRowStatus_Type = RowStatus
_TmnxWlanGwPolicerRowStatus_Object = MibTableColumn
tmnxWlanGwPolicerRowStatus = _TmnxWlanGwPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 3),
    _TmnxWlanGwPolicerRowStatus_Type()
)
tmnxWlanGwPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerRowStatus.setStatus("current")


class _TmnxWlanGwPolicerDescription_Type(TItemDescription):
    """Custom type tmnxWlanGwPolicerDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWlanGwPolicerDescription_Type.__name__ = "TItemDescription"
_TmnxWlanGwPolicerDescription_Object = MibTableColumn
tmnxWlanGwPolicerDescription = _TmnxWlanGwPolicerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 4),
    _TmnxWlanGwPolicerDescription_Type()
)
tmnxWlanGwPolicerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerDescription.setStatus("current")


class _TmnxWlanGwPolicerType_Type(Integer32):
    """Custom type tmnxWlanGwPolicerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("singleBucketBandwidth", 0),
          ("dualBucketBandwidth", 1))
    )


_TmnxWlanGwPolicerType_Type.__name__ = "Integer32"
_TmnxWlanGwPolicerType_Object = MibTableColumn
tmnxWlanGwPolicerType = _TmnxWlanGwPolicerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 5),
    _TmnxWlanGwPolicerType_Type()
)
tmnxWlanGwPolicerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerType.setStatus("current")


class _TmnxWlanGwPolicerAction_Type(Integer32):
    """Custom type tmnxWlanGwPolicerAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permitDeny", 0),
          ("priorityMark", 1))
    )


_TmnxWlanGwPolicerAction_Type.__name__ = "Integer32"
_TmnxWlanGwPolicerAction_Object = MibTableColumn
tmnxWlanGwPolicerAction = _TmnxWlanGwPolicerAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 6),
    _TmnxWlanGwPolicerAction_Type()
)
tmnxWlanGwPolicerAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerAction.setStatus("current")


class _TmnxWlanGwPolicerAdminPIR_Type(TPIRRate):
    """Custom type tmnxWlanGwPolicerAdminPIR based on TPIRRate"""
    defaultValue = -1


_TmnxWlanGwPolicerAdminPIR_Type.__name__ = "TPIRRate"
_TmnxWlanGwPolicerAdminPIR_Object = MibTableColumn
tmnxWlanGwPolicerAdminPIR = _TmnxWlanGwPolicerAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 7),
    _TmnxWlanGwPolicerAdminPIR_Type()
)
tmnxWlanGwPolicerAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerAdminPIR.setUnits("kilobps")


class _TmnxWlanGwPolicerAdminCIR_Type(TCIRRate):
    """Custom type tmnxWlanGwPolicerAdminCIR based on TCIRRate"""
    defaultValue = 0


_TmnxWlanGwPolicerAdminCIR_Type.__name__ = "TCIRRate"
_TmnxWlanGwPolicerAdminCIR_Object = MibTableColumn
tmnxWlanGwPolicerAdminCIR = _TmnxWlanGwPolicerAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 8),
    _TmnxWlanGwPolicerAdminCIR_Type()
)
tmnxWlanGwPolicerAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerAdminCIR.setUnits("kilobps")


class _TmnxWlanGwPolicerMBS_Type(TmnxWlanGwBurstSize):
    """Custom type tmnxWlanGwPolicerMBS based on TmnxWlanGwBurstSize"""
    defaultValue = 0


_TmnxWlanGwPolicerMBS_Type.__name__ = "TmnxWlanGwBurstSize"
_TmnxWlanGwPolicerMBS_Object = MibTableColumn
tmnxWlanGwPolicerMBS = _TmnxWlanGwPolicerMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 9),
    _TmnxWlanGwPolicerMBS_Type()
)
tmnxWlanGwPolicerMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerMBS.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerMBS.setUnits("kilobytes")


class _TmnxWlanGwPolicerCBS_Type(TmnxWlanGwBurstSize):
    """Custom type tmnxWlanGwPolicerCBS based on TmnxWlanGwBurstSize"""
    defaultValue = 0


_TmnxWlanGwPolicerCBS_Type.__name__ = "TmnxWlanGwBurstSize"
_TmnxWlanGwPolicerCBS_Object = MibTableColumn
tmnxWlanGwPolicerCBS = _TmnxWlanGwPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 10),
    _TmnxWlanGwPolicerCBS_Type()
)
tmnxWlanGwPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerCBS.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerCBS.setUnits("kilobytes")


class _TmnxWlanGwPolicerPIRAdaptation_Type(TAdaptationRule):
    """Custom type tmnxWlanGwPolicerPIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TmnxWlanGwPolicerPIRAdaptation_Type.__name__ = "TAdaptationRule"
_TmnxWlanGwPolicerPIRAdaptation_Object = MibTableColumn
tmnxWlanGwPolicerPIRAdaptation = _TmnxWlanGwPolicerPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 11),
    _TmnxWlanGwPolicerPIRAdaptation_Type()
)
tmnxWlanGwPolicerPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerPIRAdaptation.setStatus("current")


class _TmnxWlanGwPolicerCIRAdaptation_Type(TAdaptationRule):
    """Custom type tmnxWlanGwPolicerCIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TmnxWlanGwPolicerCIRAdaptation_Type.__name__ = "TAdaptationRule"
_TmnxWlanGwPolicerCIRAdaptation_Object = MibTableColumn
tmnxWlanGwPolicerCIRAdaptation = _TmnxWlanGwPolicerCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 12),
    _TmnxWlanGwPolicerCIRAdaptation_Type()
)
tmnxWlanGwPolicerCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerCIRAdaptation.setStatus("current")
_TmnxWlanGwDsmIpFil6N3Table_Object = MibTable
tmnxWlanGwDsmIpFil6N3Table = _TmnxWlanGwDsmIpFil6N3Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8)
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3Table.setStatus("current")
_TmnxWlanGwDsmIpFil6N3Entry_Object = MibTableRow
tmnxWlanGwDsmIpFil6N3Entry = _TmnxWlanGwDsmIpFil6N3Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1)
)
tmnxWlanGwDsmIpFil6N3Entry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilName"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3Index"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3Entry.setStatus("current")


class _TmnxWlanGwDsmIpFil6N3Index_Type(Unsigned32):
    """Custom type tmnxWlanGwDsmIpFil6N3Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TmnxWlanGwDsmIpFil6N3Index_Type.__name__ = "Unsigned32"
_TmnxWlanGwDsmIpFil6N3Index_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3Index = _TmnxWlanGwDsmIpFil6N3Index_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 1),
    _TmnxWlanGwDsmIpFil6N3Index_Type()
)
tmnxWlanGwDsmIpFil6N3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3Index.setStatus("current")
_TmnxWlanGwDsmIpFil6N3RowStatus_Type = RowStatus
_TmnxWlanGwDsmIpFil6N3RowStatus_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3RowStatus = _TmnxWlanGwDsmIpFil6N3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 2),
    _TmnxWlanGwDsmIpFil6N3RowStatus_Type()
)
tmnxWlanGwDsmIpFil6N3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3RowStatus.setStatus("current")
_TmnxWlanGwDsmIpFil6N3LastCh_Type = TimeStamp
_TmnxWlanGwDsmIpFil6N3LastCh_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3LastCh = _TmnxWlanGwDsmIpFil6N3LastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 3),
    _TmnxWlanGwDsmIpFil6N3LastCh_Type()
)
tmnxWlanGwDsmIpFil6N3LastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3LastCh.setStatus("current")


class _TmnxWlanGwDsmIpFil6N3Description_Type(TItemDescription):
    """Custom type tmnxWlanGwDsmIpFil6N3Description based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWlanGwDsmIpFil6N3Description_Type.__name__ = "TItemDescription"
_TmnxWlanGwDsmIpFil6N3Description_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3Description = _TmnxWlanGwDsmIpFil6N3Description_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 4),
    _TmnxWlanGwDsmIpFil6N3Description_Type()
)
tmnxWlanGwDsmIpFil6N3Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3Description.setStatus("current")


class _TmnxWlanGwDsmIpFil6N3Action_Type(TmnxWlanGwDsmFilterAction):
    """Custom type tmnxWlanGwDsmIpFil6N3Action based on TmnxWlanGwDsmFilterAction"""
    defaultValue = 0


_TmnxWlanGwDsmIpFil6N3Action_Type.__name__ = "TmnxWlanGwDsmFilterAction"
_TmnxWlanGwDsmIpFil6N3Action_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3Action = _TmnxWlanGwDsmIpFil6N3Action_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 5),
    _TmnxWlanGwDsmIpFil6N3Action_Type()
)
tmnxWlanGwDsmIpFil6N3Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3Action.setStatus("current")


class _TmnxWlanGwDsmIpFil6N3Protocol_Type(TIpProtocol):
    """Custom type tmnxWlanGwDsmIpFil6N3Protocol based on TIpProtocol"""
    defaultValue = -1


_TmnxWlanGwDsmIpFil6N3Protocol_Type.__name__ = "TIpProtocol"
_TmnxWlanGwDsmIpFil6N3Protocol_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3Protocol = _TmnxWlanGwDsmIpFil6N3Protocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 6),
    _TmnxWlanGwDsmIpFil6N3Protocol_Type()
)
tmnxWlanGwDsmIpFil6N3Protocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3Protocol.setStatus("current")


class _TmnxWlanGwDsmIpFil6N3DestAddrTyp_Type(InetAddressType):
    """Custom type tmnxWlanGwDsmIpFil6N3DestAddrTyp based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwDsmIpFil6N3DestAddrTyp_Type.__name__ = "InetAddressType"
_TmnxWlanGwDsmIpFil6N3DestAddrTyp_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3DestAddrTyp = _TmnxWlanGwDsmIpFil6N3DestAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 7),
    _TmnxWlanGwDsmIpFil6N3DestAddrTyp_Type()
)
tmnxWlanGwDsmIpFil6N3DestAddrTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3DestAddrTyp.setStatus("current")


class _TmnxWlanGwDsmIpFil6N3DestAddr_Type(InetAddress):
    """Custom type tmnxWlanGwDsmIpFil6N3DestAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwDsmIpFil6N3DestAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwDsmIpFil6N3DestAddr_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3DestAddr = _TmnxWlanGwDsmIpFil6N3DestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 8),
    _TmnxWlanGwDsmIpFil6N3DestAddr_Type()
)
tmnxWlanGwDsmIpFil6N3DestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3DestAddr.setStatus("current")


class _TmnxWlanGwDsmIpFil6N3DestPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxWlanGwDsmIpFil6N3DestPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxWlanGwDsmIpFil6N3DestPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxWlanGwDsmIpFil6N3DestPrefLen_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3DestPrefLen = _TmnxWlanGwDsmIpFil6N3DestPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 9),
    _TmnxWlanGwDsmIpFil6N3DestPrefLen_Type()
)
tmnxWlanGwDsmIpFil6N3DestPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3DestPrefLen.setStatus("current")


class _TmnxWlanGwDsmIpFil6N3DestPortOp_Type(Integer32):
    """Custom type tmnxWlanGwDsmIpFil6N3DestPortOp based on Integer32"""
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
          ("eq", 1))
    )


_TmnxWlanGwDsmIpFil6N3DestPortOp_Type.__name__ = "Integer32"
_TmnxWlanGwDsmIpFil6N3DestPortOp_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3DestPortOp = _TmnxWlanGwDsmIpFil6N3DestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 10),
    _TmnxWlanGwDsmIpFil6N3DestPortOp_Type()
)
tmnxWlanGwDsmIpFil6N3DestPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3DestPortOp.setStatus("current")


class _TmnxWlanGwDsmIpFil6N3DestPort1_Type(InetPortNumber):
    """Custom type tmnxWlanGwDsmIpFil6N3DestPort1 based on InetPortNumber"""
    defaultValue = 0


_TmnxWlanGwDsmIpFil6N3DestPort1_Type.__name__ = "InetPortNumber"
_TmnxWlanGwDsmIpFil6N3DestPort1_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3DestPort1 = _TmnxWlanGwDsmIpFil6N3DestPort1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 11),
    _TmnxWlanGwDsmIpFil6N3DestPort1_Type()
)
tmnxWlanGwDsmIpFil6N3DestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3DestPort1.setStatus("current")
_TmnxWlanGwDsmIpFil6N3IngHitCount_Type = Counter64
_TmnxWlanGwDsmIpFil6N3IngHitCount_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3IngHitCount = _TmnxWlanGwDsmIpFil6N3IngHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 17),
    _TmnxWlanGwDsmIpFil6N3IngHitCount_Type()
)
tmnxWlanGwDsmIpFil6N3IngHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3IngHitCount.setStatus("current")


class _TmnxWlanGwDsmIpFil6N3RedirectURL_Type(TmnxHttpRedirectUrl):
    """Custom type tmnxWlanGwDsmIpFil6N3RedirectURL based on TmnxHttpRedirectUrl"""
    defaultHexValue = ""


_TmnxWlanGwDsmIpFil6N3RedirectURL_Type.__name__ = "TmnxHttpRedirectUrl"
_TmnxWlanGwDsmIpFil6N3RedirectURL_Object = MibTableColumn
tmnxWlanGwDsmIpFil6N3RedirectURL = _TmnxWlanGwDsmIpFil6N3RedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 8, 1, 18),
    _TmnxWlanGwDsmIpFil6N3RedirectURL_Type()
)
tmnxWlanGwDsmIpFil6N3RedirectURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3RedirectURL.setStatus("current")
_TmnxWlanGwDsmTable_Object = MibTable
tmnxWlanGwDsmTable = _TmnxWlanGwDsmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 9)
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmTable.setStatus("current")
_TmnxWlanGwDsmEntry_Object = MibTableRow
tmnxWlanGwDsmEntry = _TmnxWlanGwDsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmEntry.setStatus("current")
_TmnxWlanGwDsmLastCh_Type = TimeStamp
_TmnxWlanGwDsmLastCh_Object = MibTableColumn
tmnxWlanGwDsmLastCh = _TmnxWlanGwDsmLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 9, 1, 1),
    _TmnxWlanGwDsmLastCh_Type()
)
tmnxWlanGwDsmLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmLastCh.setStatus("current")


class _TmnxWlanGwDsmIpv6TcpMssAdjust_Type(Unsigned32):
    """Custom type tmnxWlanGwDsmIpv6TcpMssAdjust based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(160, 10240),
    )


_TmnxWlanGwDsmIpv6TcpMssAdjust_Type.__name__ = "Unsigned32"
_TmnxWlanGwDsmIpv6TcpMssAdjust_Object = MibTableColumn
tmnxWlanGwDsmIpv6TcpMssAdjust = _TmnxWlanGwDsmIpv6TcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 9, 1, 2),
    _TmnxWlanGwDsmIpv6TcpMssAdjust_Type()
)
tmnxWlanGwDsmIpv6TcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpv6TcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpv6TcpMssAdjust.setUnits("bytes")
_TmnxWlanGwGtpIsaObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwGtpIsaObjs = _TmnxWlanGwGtpIsaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 10)
)
_TmnxWlanGwUeObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwUeObjs = _TmnxWlanGwUeObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11)
)
_TmnxWlanGwUeNextQryId_Type = Unsigned32
_TmnxWlanGwUeNextQryId_Object = MibScalar
tmnxWlanGwUeNextQryId = _TmnxWlanGwUeNextQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 1),
    _TmnxWlanGwUeNextQryId_Type()
)
tmnxWlanGwUeNextQryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeNextQryId.setStatus("current")
_TmnxWlanGwUeMaxQryId_Type = Unsigned32
_TmnxWlanGwUeMaxQryId_Object = MibScalar
tmnxWlanGwUeMaxQryId = _TmnxWlanGwUeMaxQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 2),
    _TmnxWlanGwUeMaxQryId_Type()
)
tmnxWlanGwUeMaxQryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeMaxQryId.setStatus("current")
_TmnxWlanGwUeQryTable_Object = MibTable
tmnxWlanGwUeQryTable = _TmnxWlanGwUeQryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryTable.setStatus("current")
_TmnxWlanGwUeQryEntry_Object = MibTableRow
tmnxWlanGwUeQryEntry = _TmnxWlanGwUeQryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1)
)
tmnxWlanGwUeQryEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryEntry.setStatus("current")
_TmnxWlanGwUeQryId_Type = Unsigned32
_TmnxWlanGwUeQryId_Object = MibTableColumn
tmnxWlanGwUeQryId = _TmnxWlanGwUeQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 1),
    _TmnxWlanGwUeQryId_Type()
)
tmnxWlanGwUeQryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryId.setStatus("current")
_TmnxWlanGwUeQryRowStatus_Type = RowStatus
_TmnxWlanGwUeQryRowStatus_Object = MibTableColumn
tmnxWlanGwUeQryRowStatus = _TmnxWlanGwUeQryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 2),
    _TmnxWlanGwUeQryRowStatus_Type()
)
tmnxWlanGwUeQryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryRowStatus.setStatus("current")


class _TmnxWlanGwUeQryWhereState_Type(Bits):
    """Custom type tmnxWlanGwUeQryWhereState based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bDataTriggered", 0),
          ("bDhcpTriggered", 1),
          ("bIpAssigned", 2),
          ("bAuthorizedOnly", 3),
          ("bIpAssignedAuthorized", 4),
          ("bAlreadySignedIn", 5),
          ("bPortal", 6),
          ("bDistributedSubMgmt", 7),
          ("bEsmUser", 8),
          ("bL2User", 9),
          ("bGtpAuthorized", 10),
          ("bDeletePending", 11),
          ("bXcon", 12))
    )

_TmnxWlanGwUeQryWhereState_Type.__name__ = "Bits"
_TmnxWlanGwUeQryWhereState_Object = MibTableColumn
tmnxWlanGwUeQryWhereState = _TmnxWlanGwUeQryWhereState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 3),
    _TmnxWlanGwUeQryWhereState_Type()
)
tmnxWlanGwUeQryWhereState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereState.setStatus("current")


class _TmnxWlanGwUeQryWhereMacAddress_Type(MacAddress):
    """Custom type tmnxWlanGwUeQryWhereMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxWlanGwUeQryWhereMacAddress_Type.__name__ = "MacAddress"
_TmnxWlanGwUeQryWhereMacAddress_Object = MibTableColumn
tmnxWlanGwUeQryWhereMacAddress = _TmnxWlanGwUeQryWhereMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 4),
    _TmnxWlanGwUeQryWhereMacAddress_Type()
)
tmnxWlanGwUeQryWhereMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereMacAddress.setStatus("current")


class _TmnxWlanGwUeQryWhereAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwUeQryWhereAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwUeQryWhereAddrType_Object = MibTableColumn
tmnxWlanGwUeQryWhereAddrType = _TmnxWlanGwUeQryWhereAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 5),
    _TmnxWlanGwUeQryWhereAddrType_Type()
)
tmnxWlanGwUeQryWhereAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereAddrType.setStatus("current")


class _TmnxWlanGwUeQryWhereAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeQryWhereAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeQryWhereAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeQryWhereAddr_Object = MibTableColumn
tmnxWlanGwUeQryWhereAddr = _TmnxWlanGwUeQryWhereAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 6),
    _TmnxWlanGwUeQryWhereAddr_Type()
)
tmnxWlanGwUeQryWhereAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereAddr.setStatus("current")


class _TmnxWlanGwUeQryWhereIsaGrp_Type(TmnxWlanGwIsaGrpIdOrZero):
    """Custom type tmnxWlanGwUeQryWhereIsaGrp based on TmnxWlanGwIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereIsaGrp_Type.__name__ = "TmnxWlanGwIsaGrpIdOrZero"
_TmnxWlanGwUeQryWhereIsaGrp_Object = MibTableColumn
tmnxWlanGwUeQryWhereIsaGrp = _TmnxWlanGwUeQryWhereIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 7),
    _TmnxWlanGwUeQryWhereIsaGrp_Type()
)
tmnxWlanGwUeQryWhereIsaGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereIsaGrp.setStatus("current")


class _TmnxWlanGwUeQryWhereMemberId_Type(Unsigned32):
    """Custom type tmnxWlanGwUeQryWhereMemberId based on Unsigned32"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereMemberId_Type.__name__ = "Unsigned32"
_TmnxWlanGwUeQryWhereMemberId_Object = MibTableColumn
tmnxWlanGwUeQryWhereMemberId = _TmnxWlanGwUeQryWhereMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 8),
    _TmnxWlanGwUeQryWhereMemberId_Type()
)
tmnxWlanGwUeQryWhereMemberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereMemberId.setStatus("current")


class _TmnxWlanGwUeQryWhereQTag_Type(QTagFullRangeOrNone):
    """Custom type tmnxWlanGwUeQryWhereQTag based on QTagFullRangeOrNone"""
    defaultValue = -1


_TmnxWlanGwUeQryWhereQTag_Type.__name__ = "QTagFullRangeOrNone"
_TmnxWlanGwUeQryWhereQTag_Object = MibTableColumn
tmnxWlanGwUeQryWhereQTag = _TmnxWlanGwUeQryWhereQTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 9),
    _TmnxWlanGwUeQryWhereQTag_Type()
)
tmnxWlanGwUeQryWhereQTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereQTag.setStatus("current")


class _TmnxWlanGwUeQryWhereTuRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxWlanGwUeQryWhereTuRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereTuRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxWlanGwUeQryWhereTuRouter_Object = MibTableColumn
tmnxWlanGwUeQryWhereTuRouter = _TmnxWlanGwUeQryWhereTuRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 10),
    _TmnxWlanGwUeQryWhereTuRouter_Type()
)
tmnxWlanGwUeQryWhereTuRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereTuRouter.setStatus("current")


class _TmnxWlanGwUeQryWhereTuRemAddrTyp_Type(InetAddressType):
    """Custom type tmnxWlanGwUeQryWhereTuRemAddrTyp based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereTuRemAddrTyp_Type.__name__ = "InetAddressType"
_TmnxWlanGwUeQryWhereTuRemAddrTyp_Object = MibTableColumn
tmnxWlanGwUeQryWhereTuRemAddrTyp = _TmnxWlanGwUeQryWhereTuRemAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 11),
    _TmnxWlanGwUeQryWhereTuRemAddrTyp_Type()
)
tmnxWlanGwUeQryWhereTuRemAddrTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereTuRemAddrTyp.setStatus("current")


class _TmnxWlanGwUeQryWhereTuRemAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeQryWhereTuRemAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeQryWhereTuRemAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeQryWhereTuRemAddr_Object = MibTableColumn
tmnxWlanGwUeQryWhereTuRemAddr = _TmnxWlanGwUeQryWhereTuRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 12),
    _TmnxWlanGwUeQryWhereTuRemAddr_Type()
)
tmnxWlanGwUeQryWhereTuRemAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereTuRemAddr.setStatus("current")


class _TmnxWlanGwUeQryWhereTuLocAddrTyp_Type(InetAddressType):
    """Custom type tmnxWlanGwUeQryWhereTuLocAddrTyp based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereTuLocAddrTyp_Type.__name__ = "InetAddressType"
_TmnxWlanGwUeQryWhereTuLocAddrTyp_Object = MibTableColumn
tmnxWlanGwUeQryWhereTuLocAddrTyp = _TmnxWlanGwUeQryWhereTuLocAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 13),
    _TmnxWlanGwUeQryWhereTuLocAddrTyp_Type()
)
tmnxWlanGwUeQryWhereTuLocAddrTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereTuLocAddrTyp.setStatus("current")


class _TmnxWlanGwUeQryWhereTuLocAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeQryWhereTuLocAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeQryWhereTuLocAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeQryWhereTuLocAddr_Object = MibTableColumn
tmnxWlanGwUeQryWhereTuLocAddr = _TmnxWlanGwUeQryWhereTuLocAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 14),
    _TmnxWlanGwUeQryWhereTuLocAddr_Type()
)
tmnxWlanGwUeQryWhereTuLocAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereTuLocAddr.setStatus("current")


class _TmnxWlanGwUeQryWhereEncap_Type(TmnxWlanGwUeEncapsulation):
    """Custom type tmnxWlanGwUeQryWhereEncap based on TmnxWlanGwUeEncapsulation"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereEncap_Type.__name__ = "TmnxWlanGwUeEncapsulation"
_TmnxWlanGwUeQryWhereEncap_Object = MibTableColumn
tmnxWlanGwUeQryWhereEncap = _TmnxWlanGwUeQryWhereEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 15),
    _TmnxWlanGwUeQryWhereEncap_Type()
)
tmnxWlanGwUeQryWhereEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereEncap.setStatus("current")


class _TmnxWlanGwUeQryWhereSlaacPrefTyp_Type(InetAddressType):
    """Custom type tmnxWlanGwUeQryWhereSlaacPrefTyp based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereSlaacPrefTyp_Type.__name__ = "InetAddressType"
_TmnxWlanGwUeQryWhereSlaacPrefTyp_Object = MibTableColumn
tmnxWlanGwUeQryWhereSlaacPrefTyp = _TmnxWlanGwUeQryWhereSlaacPrefTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 16),
    _TmnxWlanGwUeQryWhereSlaacPrefTyp_Type()
)
tmnxWlanGwUeQryWhereSlaacPrefTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereSlaacPrefTyp.setStatus("current")


class _TmnxWlanGwUeQryWhereSlaacPref_Type(InetAddress):
    """Custom type tmnxWlanGwUeQryWhereSlaacPref based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeQryWhereSlaacPref_Type.__name__ = "InetAddress"
_TmnxWlanGwUeQryWhereSlaacPref_Object = MibTableColumn
tmnxWlanGwUeQryWhereSlaacPref = _TmnxWlanGwUeQryWhereSlaacPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 17),
    _TmnxWlanGwUeQryWhereSlaacPref_Type()
)
tmnxWlanGwUeQryWhereSlaacPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereSlaacPref.setStatus("current")


class _TmnxWlanGwUeQryWhereDhcp6AddrTyp_Type(InetAddressType):
    """Custom type tmnxWlanGwUeQryWhereDhcp6AddrTyp based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereDhcp6AddrTyp_Type.__name__ = "InetAddressType"
_TmnxWlanGwUeQryWhereDhcp6AddrTyp_Object = MibTableColumn
tmnxWlanGwUeQryWhereDhcp6AddrTyp = _TmnxWlanGwUeQryWhereDhcp6AddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 18),
    _TmnxWlanGwUeQryWhereDhcp6AddrTyp_Type()
)
tmnxWlanGwUeQryWhereDhcp6AddrTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereDhcp6AddrTyp.setStatus("current")


class _TmnxWlanGwUeQryWhereDhcp6Addr_Type(InetAddress):
    """Custom type tmnxWlanGwUeQryWhereDhcp6Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeQryWhereDhcp6Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeQryWhereDhcp6Addr_Object = MibTableColumn
tmnxWlanGwUeQryWhereDhcp6Addr = _TmnxWlanGwUeQryWhereDhcp6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 19),
    _TmnxWlanGwUeQryWhereDhcp6Addr_Type()
)
tmnxWlanGwUeQryWhereDhcp6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereDhcp6Addr.setStatus("current")


class _TmnxWlanGwUeQryWhereBridgeId_Type(Unsigned32):
    """Custom type tmnxWlanGwUeQryWhereBridgeId based on Unsigned32"""
    defaultValue = 4294967295


_TmnxWlanGwUeQryWhereBridgeId_Type.__name__ = "Unsigned32"
_TmnxWlanGwUeQryWhereBridgeId_Object = MibTableColumn
tmnxWlanGwUeQryWhereBridgeId = _TmnxWlanGwUeQryWhereBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 25),
    _TmnxWlanGwUeQryWhereBridgeId_Type()
)
tmnxWlanGwUeQryWhereBridgeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereBridgeId.setStatus("current")


class _TmnxWlanGwUeQryWhereAddrFamily_Type(TmnxWlanGwUeAddressFamily):
    """Custom type tmnxWlanGwUeQryWhereAddrFamily based on TmnxWlanGwUeAddressFamily"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereAddrFamily_Type.__name__ = "TmnxWlanGwUeAddressFamily"
_TmnxWlanGwUeQryWhereAddrFamily_Object = MibTableColumn
tmnxWlanGwUeQryWhereAddrFamily = _TmnxWlanGwUeQryWhereAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 26),
    _TmnxWlanGwUeQryWhereAddrFamily_Type()
)
tmnxWlanGwUeQryWhereAddrFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereAddrFamily.setStatus("current")
_TmnxWlanGwUeQryName_Type = TNamedItem
_TmnxWlanGwUeQryName_Object = MibTableColumn
tmnxWlanGwUeQryName = _TmnxWlanGwUeQryName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 27),
    _TmnxWlanGwUeQryName_Type()
)
tmnxWlanGwUeQryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryName.setStatus("current")
_TmnxWlanGwUeQryNumResults_Type = Gauge32
_TmnxWlanGwUeQryNumResults_Object = MibTableColumn
tmnxWlanGwUeQryNumResults = _TmnxWlanGwUeQryNumResults_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 200),
    _TmnxWlanGwUeQryNumResults_Type()
)
tmnxWlanGwUeQryNumResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryNumResults.setStatus("current")
_TmnxWlanGwUeResTable_Object = MibTable
tmnxWlanGwUeResTable = _TmnxWlanGwUeResTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTable.setStatus("current")
_TmnxWlanGwUeResEntry_Object = MibTableRow
tmnxWlanGwUeResEntry = _TmnxWlanGwUeResEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1)
)
tmnxWlanGwUeResEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeResEntry.setStatus("current")
_TmnxWlanGwUeResId_Type = TmnxWlanGwUeIdentifier
_TmnxWlanGwUeResId_Object = MibTableColumn
tmnxWlanGwUeResId = _TmnxWlanGwUeResId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 1),
    _TmnxWlanGwUeResId_Type()
)
tmnxWlanGwUeResId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResId.setStatus("current")
_TmnxWlanGwUeResMacAddress_Type = MacAddress
_TmnxWlanGwUeResMacAddress_Object = MibTableColumn
tmnxWlanGwUeResMacAddress = _TmnxWlanGwUeResMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 2),
    _TmnxWlanGwUeResMacAddress_Type()
)
tmnxWlanGwUeResMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResMacAddress.setStatus("current")
_TmnxWlanGwUeResQTag_Type = QTagFullRangeOrNone
_TmnxWlanGwUeResQTag_Object = MibTableColumn
tmnxWlanGwUeResQTag = _TmnxWlanGwUeResQTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 3),
    _TmnxWlanGwUeResQTag_Type()
)
tmnxWlanGwUeResQTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResQTag.setStatus("current")
_TmnxWlanGwUeResAddrType_Type = InetAddressType
_TmnxWlanGwUeResAddrType_Object = MibTableColumn
tmnxWlanGwUeResAddrType = _TmnxWlanGwUeResAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 4),
    _TmnxWlanGwUeResAddrType_Type()
)
tmnxWlanGwUeResAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResAddrType.setStatus("current")


class _TmnxWlanGwUeResAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeResAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeResAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeResAddr_Object = MibTableColumn
tmnxWlanGwUeResAddr = _TmnxWlanGwUeResAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 5),
    _TmnxWlanGwUeResAddr_Type()
)
tmnxWlanGwUeResAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResAddr.setStatus("current")


class _TmnxWlanGwUeResState_Type(Integer32):
    """Custom type tmnxWlanGwUeResState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("new", 1),
          ("dataTriggered", 2),
          ("dhcpTriggered", 3),
          ("ipAssigned", 4),
          ("authorizedOnly", 5),
          ("ipAssignedAuthorized", 6),
          ("alreadySignedIn", 7),
          ("portal", 8),
          ("distributedSubMgmt", 9),
          ("esmUser", 10),
          ("l2User", 11),
          ("gtpAuthorized", 12),
          ("deletePending", 13),
          ("xCon", 14))
    )


_TmnxWlanGwUeResState_Type.__name__ = "Integer32"
_TmnxWlanGwUeResState_Object = MibTableColumn
tmnxWlanGwUeResState = _TmnxWlanGwUeResState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 6),
    _TmnxWlanGwUeResState_Type()
)
tmnxWlanGwUeResState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResState.setStatus("current")
_TmnxWlanGwUeResIsaGrp_Type = TmnxWlanGwIsaGrpIdOrZero
_TmnxWlanGwUeResIsaGrp_Object = MibTableColumn
tmnxWlanGwUeResIsaGrp = _TmnxWlanGwUeResIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 7),
    _TmnxWlanGwUeResIsaGrp_Type()
)
tmnxWlanGwUeResIsaGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIsaGrp.setStatus("current")
_TmnxWlanGwUeResIsaMemberId_Type = Unsigned32
_TmnxWlanGwUeResIsaMemberId_Object = MibTableColumn
tmnxWlanGwUeResIsaMemberId = _TmnxWlanGwUeResIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 8),
    _TmnxWlanGwUeResIsaMemberId_Type()
)
tmnxWlanGwUeResIsaMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIsaMemberId.setStatus("current")
_TmnxWlanGwUeResTuRouter_Type = TmnxVRtrIDOrZero
_TmnxWlanGwUeResTuRouter_Object = MibTableColumn
tmnxWlanGwUeResTuRouter = _TmnxWlanGwUeResTuRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 9),
    _TmnxWlanGwUeResTuRouter_Type()
)
tmnxWlanGwUeResTuRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTuRouter.setStatus("current")
_TmnxWlanGwUeResTuAddrType_Type = InetAddressType
_TmnxWlanGwUeResTuAddrType_Object = MibTableColumn
tmnxWlanGwUeResTuAddrType = _TmnxWlanGwUeResTuAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 10),
    _TmnxWlanGwUeResTuAddrType_Type()
)
tmnxWlanGwUeResTuAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTuAddrType.setStatus("current")


class _TmnxWlanGwUeResTuRemoteAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeResTuRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeResTuRemoteAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeResTuRemoteAddr_Object = MibTableColumn
tmnxWlanGwUeResTuRemoteAddr = _TmnxWlanGwUeResTuRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 11),
    _TmnxWlanGwUeResTuRemoteAddr_Type()
)
tmnxWlanGwUeResTuRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTuRemoteAddr.setStatus("current")


class _TmnxWlanGwUeResTuLocalAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeResTuLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeResTuLocalAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeResTuLocalAddr_Object = MibTableColumn
tmnxWlanGwUeResTuLocalAddr = _TmnxWlanGwUeResTuLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 12),
    _TmnxWlanGwUeResTuLocalAddr_Type()
)
tmnxWlanGwUeResTuLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTuLocalAddr.setStatus("current")
_TmnxWlanGwUeResEncapsulation_Type = TmnxWlanGwUeEncapsulation
_TmnxWlanGwUeResEncapsulation_Object = MibTableColumn
tmnxWlanGwUeResEncapsulation = _TmnxWlanGwUeResEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 13),
    _TmnxWlanGwUeResEncapsulation_Type()
)
tmnxWlanGwUeResEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResEncapsulation.setStatus("current")
_TmnxWlanGwUeResApMacAddress_Type = MacAddress
_TmnxWlanGwUeResApMacAddress_Object = MibTableColumn
tmnxWlanGwUeResApMacAddress = _TmnxWlanGwUeResApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 100),
    _TmnxWlanGwUeResApMacAddress_Type()
)
tmnxWlanGwUeResApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResApMacAddress.setStatus("current")
_TmnxWlanGwUeResSsid_Type = TNamedItemOrEmpty
_TmnxWlanGwUeResSsid_Object = MibTableColumn
tmnxWlanGwUeResSsid = _TmnxWlanGwUeResSsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 101),
    _TmnxWlanGwUeResSsid_Type()
)
tmnxWlanGwUeResSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResSsid.setStatus("current")
_TmnxWlanGwUeResMplsLabel_Type = MplsLabel
_TmnxWlanGwUeResMplsLabel_Object = MibTableColumn
tmnxWlanGwUeResMplsLabel = _TmnxWlanGwUeResMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 102),
    _TmnxWlanGwUeResMplsLabel_Type()
)
tmnxWlanGwUeResMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResMplsLabel.setStatus("current")


class _TmnxWlanGwUeResLastMoveTime_Type(DateAndTime):
    """Custom type tmnxWlanGwUeResLastMoveTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwUeResLastMoveTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwUeResLastMoveTime_Object = MibTableColumn
tmnxWlanGwUeResLastMoveTime = _TmnxWlanGwUeResLastMoveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 103),
    _TmnxWlanGwUeResLastMoveTime_Type()
)
tmnxWlanGwUeResLastMoveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResLastMoveTime.setStatus("current")


class _TmnxWlanGwUeResExpirationTime_Type(DateAndTime):
    """Custom type tmnxWlanGwUeResExpirationTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwUeResExpirationTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwUeResExpirationTime_Object = MibTableColumn
tmnxWlanGwUeResExpirationTime = _TmnxWlanGwUeResExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 104),
    _TmnxWlanGwUeResExpirationTime_Type()
)
tmnxWlanGwUeResExpirationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResExpirationTime.setStatus("current")
_TmnxWlanGwUeResIdleTimeout_Type = Unsigned32
_TmnxWlanGwUeResIdleTimeout_Object = MibTableColumn
tmnxWlanGwUeResIdleTimeout = _TmnxWlanGwUeResIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 105),
    _TmnxWlanGwUeResIdleTimeout_Type()
)
tmnxWlanGwUeResIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIdleTimeout.setUnits("seconds")


class _TmnxWlanGwUeResSessionTimeout_Type(DateAndTime):
    """Custom type tmnxWlanGwUeResSessionTimeout based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwUeResSessionTimeout_Type.__name__ = "DateAndTime"
_TmnxWlanGwUeResSessionTimeout_Object = MibTableColumn
tmnxWlanGwUeResSessionTimeout = _TmnxWlanGwUeResSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 106),
    _TmnxWlanGwUeResSessionTimeout_Type()
)
tmnxWlanGwUeResSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResSessionTimeout.setStatus("current")
_TmnxWlanGwUeResNatPlcy_Type = TNamedItemOrEmpty
_TmnxWlanGwUeResNatPlcy_Object = MibTableColumn
tmnxWlanGwUeResNatPlcy = _TmnxWlanGwUeResNatPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 107),
    _TmnxWlanGwUeResNatPlcy_Type()
)
tmnxWlanGwUeResNatPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResNatPlcy.setStatus("current")
_TmnxWlanGwUeResHttpRdrPlcy_Type = TNamedItemOrEmpty
_TmnxWlanGwUeResHttpRdrPlcy_Object = MibTableColumn
tmnxWlanGwUeResHttpRdrPlcy = _TmnxWlanGwUeResHttpRdrPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 108),
    _TmnxWlanGwUeResHttpRdrPlcy_Type()
)
tmnxWlanGwUeResHttpRdrPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResHttpRdrPlcy.setStatus("current")
_TmnxWlanGwUeResDsmIpFilter_Type = TNamedItemOrEmpty
_TmnxWlanGwUeResDsmIpFilter_Object = MibTableColumn
tmnxWlanGwUeResDsmIpFilter = _TmnxWlanGwUeResDsmIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 109),
    _TmnxWlanGwUeResDsmIpFilter_Type()
)
tmnxWlanGwUeResDsmIpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDsmIpFilter.setStatus("current")
_TmnxWlanGwUeResDsmAcctPlcy_Type = TNamedItemOrEmpty
_TmnxWlanGwUeResDsmAcctPlcy_Object = MibTableColumn
tmnxWlanGwUeResDsmAcctPlcy = _TmnxWlanGwUeResDsmAcctPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 110),
    _TmnxWlanGwUeResDsmAcctPlcy_Type()
)
tmnxWlanGwUeResDsmAcctPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDsmAcctPlcy.setStatus("current")
_TmnxWlanGwUeResDsmAcctUpdInterv_Type = Unsigned32
_TmnxWlanGwUeResDsmAcctUpdInterv_Object = MibTableColumn
tmnxWlanGwUeResDsmAcctUpdInterv = _TmnxWlanGwUeResDsmAcctUpdInterv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 111),
    _TmnxWlanGwUeResDsmAcctUpdInterv_Type()
)
tmnxWlanGwUeResDsmAcctUpdInterv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDsmAcctUpdInterv.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDsmAcctUpdInterv.setUnits("seconds")


class _TmnxWlanGwUeResAcctUpdate_Type(DateAndTime):
    """Custom type tmnxWlanGwUeResAcctUpdate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwUeResAcctUpdate_Type.__name__ = "DateAndTime"
_TmnxWlanGwUeResAcctUpdate_Object = MibTableColumn
tmnxWlanGwUeResAcctUpdate = _TmnxWlanGwUeResAcctUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 112),
    _TmnxWlanGwUeResAcctUpdate_Type()
)
tmnxWlanGwUeResAcctUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResAcctUpdate.setStatus("current")
_TmnxWlanGwUeResIngOperPir_Type = TPIRRate
_TmnxWlanGwUeResIngOperPir_Object = MibTableColumn
tmnxWlanGwUeResIngOperPir = _TmnxWlanGwUeResIngOperPir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 113),
    _TmnxWlanGwUeResIngOperPir_Type()
)
tmnxWlanGwUeResIngOperPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIngOperPir.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIngOperPir.setUnits("kilobps")
_TmnxWlanGwUeResIngOperCir_Type = TCIRRate
_TmnxWlanGwUeResIngOperCir_Object = MibTableColumn
tmnxWlanGwUeResIngOperCir = _TmnxWlanGwUeResIngOperCir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 114),
    _TmnxWlanGwUeResIngOperCir_Type()
)
tmnxWlanGwUeResIngOperCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIngOperCir.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIngOperCir.setUnits("kilobps")
_TmnxWlanGwUeResEgrOperPir_Type = TPIRRate
_TmnxWlanGwUeResEgrOperPir_Object = MibTableColumn
tmnxWlanGwUeResEgrOperPir = _TmnxWlanGwUeResEgrOperPir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 115),
    _TmnxWlanGwUeResEgrOperPir_Type()
)
tmnxWlanGwUeResEgrOperPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResEgrOperPir.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResEgrOperPir.setUnits("kilobps")
_TmnxWlanGwUeResEgrOperCir_Type = TCIRRate
_TmnxWlanGwUeResEgrOperCir_Object = MibTableColumn
tmnxWlanGwUeResEgrOperCir = _TmnxWlanGwUeResEgrOperCir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 116),
    _TmnxWlanGwUeResEgrOperCir_Type()
)
tmnxWlanGwUeResEgrOperCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResEgrOperCir.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResEgrOperCir.setUnits("kilobps")
_TmnxWlanGwUeResDsmAppProfile_Type = TNamedItemOrEmpty
_TmnxWlanGwUeResDsmAppProfile_Object = MibTableColumn
tmnxWlanGwUeResDsmAppProfile = _TmnxWlanGwUeResDsmAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 130),
    _TmnxWlanGwUeResDsmAppProfile_Type()
)
tmnxWlanGwUeResDsmAppProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDsmAppProfile.setStatus("current")
_TmnxWlanGwUeResRxPkts_Type = Counter64
_TmnxWlanGwUeResRxPkts_Object = MibTableColumn
tmnxWlanGwUeResRxPkts = _TmnxWlanGwUeResRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 200),
    _TmnxWlanGwUeResRxPkts_Type()
)
tmnxWlanGwUeResRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResRxPkts.setStatus("current")
_TmnxWlanGwUeResRxOctets_Type = Counter64
_TmnxWlanGwUeResRxOctets_Object = MibTableColumn
tmnxWlanGwUeResRxOctets = _TmnxWlanGwUeResRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 201),
    _TmnxWlanGwUeResRxOctets_Type()
)
tmnxWlanGwUeResRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResRxOctets.setStatus("current")
_TmnxWlanGwUeResTxPkts_Type = Counter64
_TmnxWlanGwUeResTxPkts_Object = MibTableColumn
tmnxWlanGwUeResTxPkts = _TmnxWlanGwUeResTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 202),
    _TmnxWlanGwUeResTxPkts_Type()
)
tmnxWlanGwUeResTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTxPkts.setStatus("current")
_TmnxWlanGwUeResTxOctets_Type = Counter64
_TmnxWlanGwUeResTxOctets_Object = MibTableColumn
tmnxWlanGwUeResTxOctets = _TmnxWlanGwUeResTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 203),
    _TmnxWlanGwUeResTxOctets_Type()
)
tmnxWlanGwUeResTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTxOctets.setStatus("current")
_TmnxWlanGwUeResSlaacAddrType_Type = InetAddressType
_TmnxWlanGwUeResSlaacAddrType_Object = MibTableColumn
tmnxWlanGwUeResSlaacAddrType = _TmnxWlanGwUeResSlaacAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 300),
    _TmnxWlanGwUeResSlaacAddrType_Type()
)
tmnxWlanGwUeResSlaacAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResSlaacAddrType.setStatus("current")


class _TmnxWlanGwUeResSlaacPref_Type(InetAddress):
    """Custom type tmnxWlanGwUeResSlaacPref based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeResSlaacPref_Type.__name__ = "InetAddress"
_TmnxWlanGwUeResSlaacPref_Object = MibTableColumn
tmnxWlanGwUeResSlaacPref = _TmnxWlanGwUeResSlaacPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 301),
    _TmnxWlanGwUeResSlaacPref_Type()
)
tmnxWlanGwUeResSlaacPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResSlaacPref.setStatus("current")


class _TmnxWlanGwUeResSlaacAddr1_Type(InetAddress):
    """Custom type tmnxWlanGwUeResSlaacAddr1 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeResSlaacAddr1_Type.__name__ = "InetAddress"
_TmnxWlanGwUeResSlaacAddr1_Object = MibTableColumn
tmnxWlanGwUeResSlaacAddr1 = _TmnxWlanGwUeResSlaacAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 302),
    _TmnxWlanGwUeResSlaacAddr1_Type()
)
tmnxWlanGwUeResSlaacAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResSlaacAddr1.setStatus("current")


class _TmnxWlanGwUeResSlaacAddr2_Type(InetAddress):
    """Custom type tmnxWlanGwUeResSlaacAddr2 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeResSlaacAddr2_Type.__name__ = "InetAddress"
_TmnxWlanGwUeResSlaacAddr2_Object = MibTableColumn
tmnxWlanGwUeResSlaacAddr2 = _TmnxWlanGwUeResSlaacAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 303),
    _TmnxWlanGwUeResSlaacAddr2_Type()
)
tmnxWlanGwUeResSlaacAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResSlaacAddr2.setStatus("current")


class _TmnxWlanGwUeResSlaacAddr3_Type(InetAddress):
    """Custom type tmnxWlanGwUeResSlaacAddr3 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeResSlaacAddr3_Type.__name__ = "InetAddress"
_TmnxWlanGwUeResSlaacAddr3_Object = MibTableColumn
tmnxWlanGwUeResSlaacAddr3 = _TmnxWlanGwUeResSlaacAddr3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 304),
    _TmnxWlanGwUeResSlaacAddr3_Type()
)
tmnxWlanGwUeResSlaacAddr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResSlaacAddr3.setStatus("current")
_TmnxWlanGwUeResDhcp6AddrType_Type = InetAddressType
_TmnxWlanGwUeResDhcp6AddrType_Object = MibTableColumn
tmnxWlanGwUeResDhcp6AddrType = _TmnxWlanGwUeResDhcp6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 305),
    _TmnxWlanGwUeResDhcp6AddrType_Type()
)
tmnxWlanGwUeResDhcp6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDhcp6AddrType.setStatus("current")


class _TmnxWlanGwUeResDhcp6Addr_Type(InetAddress):
    """Custom type tmnxWlanGwUeResDhcp6Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeResDhcp6Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeResDhcp6Addr_Object = MibTableColumn
tmnxWlanGwUeResDhcp6Addr = _TmnxWlanGwUeResDhcp6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 306),
    _TmnxWlanGwUeResDhcp6Addr_Type()
)
tmnxWlanGwUeResDhcp6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDhcp6Addr.setStatus("current")
_TmnxWlanGwUeResDhcp6AddrDepr_Type = TruthValue
_TmnxWlanGwUeResDhcp6AddrDepr_Object = MibTableColumn
tmnxWlanGwUeResDhcp6AddrDepr = _TmnxWlanGwUeResDhcp6AddrDepr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 307),
    _TmnxWlanGwUeResDhcp6AddrDepr_Type()
)
tmnxWlanGwUeResDhcp6AddrDepr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDhcp6AddrDepr.setStatus("current")
_TmnxWlanGwUeResDhcp6IAID_Type = Unsigned32
_TmnxWlanGwUeResDhcp6IAID_Object = MibTableColumn
tmnxWlanGwUeResDhcp6IAID = _TmnxWlanGwUeResDhcp6IAID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 308),
    _TmnxWlanGwUeResDhcp6IAID_Type()
)
tmnxWlanGwUeResDhcp6IAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDhcp6IAID.setStatus("current")
_TmnxWlanGwUeResDhcp6IAIDValid_Type = TruthValue
_TmnxWlanGwUeResDhcp6IAIDValid_Object = MibTableColumn
tmnxWlanGwUeResDhcp6IAIDValid = _TmnxWlanGwUeResDhcp6IAIDValid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 309),
    _TmnxWlanGwUeResDhcp6IAIDValid_Type()
)
tmnxWlanGwUeResDhcp6IAIDValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDhcp6IAIDValid.setStatus("current")


class _TmnxWlanGwUeResSlaacLeaseExpire_Type(DateAndTime):
    """Custom type tmnxWlanGwUeResSlaacLeaseExpire based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwUeResSlaacLeaseExpire_Type.__name__ = "DateAndTime"
_TmnxWlanGwUeResSlaacLeaseExpire_Object = MibTableColumn
tmnxWlanGwUeResSlaacLeaseExpire = _TmnxWlanGwUeResSlaacLeaseExpire_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 310),
    _TmnxWlanGwUeResSlaacLeaseExpire_Type()
)
tmnxWlanGwUeResSlaacLeaseExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResSlaacLeaseExpire.setStatus("current")


class _TmnxWlanGwUeResDhcp6LeaseExpire_Type(DateAndTime):
    """Custom type tmnxWlanGwUeResDhcp6LeaseExpire based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwUeResDhcp6LeaseExpire_Type.__name__ = "DateAndTime"
_TmnxWlanGwUeResDhcp6LeaseExpire_Object = MibTableColumn
tmnxWlanGwUeResDhcp6LeaseExpire = _TmnxWlanGwUeResDhcp6LeaseExpire_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 311),
    _TmnxWlanGwUeResDhcp6LeaseExpire_Type()
)
tmnxWlanGwUeResDhcp6LeaseExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDhcp6LeaseExpire.setStatus("current")
_TmnxWlanGwUeResDhcpAddrDepr_Type = TruthValue
_TmnxWlanGwUeResDhcpAddrDepr_Object = MibTableColumn
tmnxWlanGwUeResDhcpAddrDepr = _TmnxWlanGwUeResDhcpAddrDepr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 400),
    _TmnxWlanGwUeResDhcpAddrDepr_Type()
)
tmnxWlanGwUeResDhcpAddrDepr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDhcpAddrDepr.setStatus("current")
_TmnxWlanGwUeResBridgeId_Type = Unsigned32
_TmnxWlanGwUeResBridgeId_Object = MibTableColumn
tmnxWlanGwUeResBridgeId = _TmnxWlanGwUeResBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 410),
    _TmnxWlanGwUeResBridgeId_Type()
)
tmnxWlanGwUeResBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResBridgeId.setStatus("current")
_TmnxWlanGwUeResAddrFamily_Type = TmnxWlanGwUeAddressFamily
_TmnxWlanGwUeResAddrFamily_Object = MibTableColumn
tmnxWlanGwUeResAddrFamily = _TmnxWlanGwUeResAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 420),
    _TmnxWlanGwUeResAddrFamily_Type()
)
tmnxWlanGwUeResAddrFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResAddrFamily.setStatus("current")
_TmnxWlanGwVplsTable_Object = MibTable
tmnxWlanGwVplsTable = _TmnxWlanGwVplsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVplsTable.setStatus("current")
_TmnxWlanGwVplsEntry_Object = MibTableRow
tmnxWlanGwVplsEntry = _TmnxWlanGwVplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 12, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVplsEntry.setStatus("current")
_TmnxWlanGwVplsLastMgmtChange_Type = TimeStamp
_TmnxWlanGwVplsLastMgmtChange_Object = MibTableColumn
tmnxWlanGwVplsLastMgmtChange = _TmnxWlanGwVplsLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 12, 1, 1),
    _TmnxWlanGwVplsLastMgmtChange_Type()
)
tmnxWlanGwVplsLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVplsLastMgmtChange.setStatus("current")


class _TmnxWlanGwVplsAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVplsAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVplsAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVplsAdminState_Object = MibTableColumn
tmnxWlanGwVplsAdminState = _TmnxWlanGwVplsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 12, 1, 2),
    _TmnxWlanGwVplsAdminState_Type()
)
tmnxWlanGwVplsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanGwVplsAdminState.setStatus("current")


class _TmnxWlanGwVplsDescription_Type(TItemDescription):
    """Custom type tmnxWlanGwVplsDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxWlanGwVplsDescription_Type.__name__ = "TItemDescription"
_TmnxWlanGwVplsDescription_Object = MibTableColumn
tmnxWlanGwVplsDescription = _TmnxWlanGwVplsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 12, 1, 3),
    _TmnxWlanGwVplsDescription_Type()
)
tmnxWlanGwVplsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanGwVplsDescription.setStatus("current")


class _TmnxWlanGwVplsSapTemplate_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVplsSapTemplate based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxWlanGwVplsSapTemplate_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVplsSapTemplate_Object = MibTableColumn
tmnxWlanGwVplsSapTemplate = _TmnxWlanGwVplsSapTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 12, 1, 4),
    _TmnxWlanGwVplsSapTemplate_Type()
)
tmnxWlanGwVplsSapTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanGwVplsSapTemplate.setStatus("current")
_TmnxWlanGwVlanSubObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwVlanSubObjs = _TmnxWlanGwVlanSubObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13)
)
_TmnxWlanGwVlanDhcp6Table_Object = MibTable
tmnxWlanGwVlanDhcp6Table = _TmnxWlanGwVlanDhcp6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 2)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6Table.setStatus("current")
_TmnxWlanGwVlanDhcp6Entry_Object = MibTableRow
tmnxWlanGwVlanDhcp6Entry = _TmnxWlanGwVlanDhcp6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6Entry.setStatus("current")
_TmnxWlanGwVlanDhcp6LastChanged_Type = TimeStamp
_TmnxWlanGwVlanDhcp6LastChanged_Object = MibTableColumn
tmnxWlanGwVlanDhcp6LastChanged = _TmnxWlanGwVlanDhcp6LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 2, 1, 1),
    _TmnxWlanGwVlanDhcp6LastChanged_Type()
)
tmnxWlanGwVlanDhcp6LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6LastChanged.setStatus("current")


class _TmnxWlanGwVlanDhcp6InitPrefLt_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanDhcp6InitPrefLt based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwVlanDhcp6InitPrefLt_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanDhcp6InitPrefLt_Object = MibTableColumn
tmnxWlanGwVlanDhcp6InitPrefLt = _TmnxWlanGwVlanDhcp6InitPrefLt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 2, 1, 2),
    _TmnxWlanGwVlanDhcp6InitPrefLt_Type()
)
tmnxWlanGwVlanDhcp6InitPrefLt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6InitPrefLt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6InitPrefLt.setUnits("seconds")


class _TmnxWlanGwVlanDhcp6ActPrefLt_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanDhcp6ActPrefLt based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwVlanDhcp6ActPrefLt_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanDhcp6ActPrefLt_Object = MibTableColumn
tmnxWlanGwVlanDhcp6ActPrefLt = _TmnxWlanGwVlanDhcp6ActPrefLt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 2, 1, 3),
    _TmnxWlanGwVlanDhcp6ActPrefLt_Type()
)
tmnxWlanGwVlanDhcp6ActPrefLt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6ActPrefLt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6ActPrefLt.setUnits("seconds")


class _TmnxWlanGwVlanDhcp6InitValidLt_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanDhcp6InitValidLt based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwVlanDhcp6InitValidLt_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanDhcp6InitValidLt_Object = MibTableColumn
tmnxWlanGwVlanDhcp6InitValidLt = _TmnxWlanGwVlanDhcp6InitValidLt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 2, 1, 4),
    _TmnxWlanGwVlanDhcp6InitValidLt_Type()
)
tmnxWlanGwVlanDhcp6InitValidLt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6InitValidLt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6InitValidLt.setUnits("seconds")


class _TmnxWlanGwVlanDhcp6ActValidLt_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanDhcp6ActValidLt based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwVlanDhcp6ActValidLt_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanDhcp6ActValidLt_Object = MibTableColumn
tmnxWlanGwVlanDhcp6ActValidLt = _TmnxWlanGwVlanDhcp6ActValidLt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 2, 1, 5),
    _TmnxWlanGwVlanDhcp6ActValidLt_Type()
)
tmnxWlanGwVlanDhcp6ActValidLt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6ActValidLt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6ActValidLt.setUnits("seconds")


class _TmnxWlanGwVlanDhcp6AdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanDhcp6AdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanDhcp6AdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanDhcp6AdminState_Object = MibTableColumn
tmnxWlanGwVlanDhcp6AdminState = _TmnxWlanGwVlanDhcp6AdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 2, 1, 6),
    _TmnxWlanGwVlanDhcp6AdminState_Type()
)
tmnxWlanGwVlanDhcp6AdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6AdminState.setStatus("current")
_TmnxWlanGwVlanSlaacTable_Object = MibTable
tmnxWlanGwVlanSlaacTable = _TmnxWlanGwVlanSlaacTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacTable.setStatus("current")
_TmnxWlanGwVlanSlaacEntry_Object = MibTableRow
tmnxWlanGwVlanSlaacEntry = _TmnxWlanGwVlanSlaacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacEntry.setStatus("current")
_TmnxWlanGwVlanSlaacLastChanged_Type = TimeStamp
_TmnxWlanGwVlanSlaacLastChanged_Object = MibTableColumn
tmnxWlanGwVlanSlaacLastChanged = _TmnxWlanGwVlanSlaacLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 3, 1, 1),
    _TmnxWlanGwVlanSlaacLastChanged_Type()
)
tmnxWlanGwVlanSlaacLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacLastChanged.setStatus("current")


class _TmnxWlanGwVlanSlaacInitPrefLt_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanSlaacInitPrefLt based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwVlanSlaacInitPrefLt_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanSlaacInitPrefLt_Object = MibTableColumn
tmnxWlanGwVlanSlaacInitPrefLt = _TmnxWlanGwVlanSlaacInitPrefLt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 3, 1, 2),
    _TmnxWlanGwVlanSlaacInitPrefLt_Type()
)
tmnxWlanGwVlanSlaacInitPrefLt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacInitPrefLt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacInitPrefLt.setUnits("seconds")


class _TmnxWlanGwVlanSlaacActPrefLt_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanSlaacActPrefLt based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwVlanSlaacActPrefLt_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanSlaacActPrefLt_Object = MibTableColumn
tmnxWlanGwVlanSlaacActPrefLt = _TmnxWlanGwVlanSlaacActPrefLt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 3, 1, 3),
    _TmnxWlanGwVlanSlaacActPrefLt_Type()
)
tmnxWlanGwVlanSlaacActPrefLt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacActPrefLt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacActPrefLt.setUnits("seconds")


class _TmnxWlanGwVlanSlaacInitValidLt_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanSlaacInitValidLt based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwVlanSlaacInitValidLt_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanSlaacInitValidLt_Object = MibTableColumn
tmnxWlanGwVlanSlaacInitValidLt = _TmnxWlanGwVlanSlaacInitValidLt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 3, 1, 4),
    _TmnxWlanGwVlanSlaacInitValidLt_Type()
)
tmnxWlanGwVlanSlaacInitValidLt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacInitValidLt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacInitValidLt.setUnits("seconds")


class _TmnxWlanGwVlanSlaacActValidLt_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanSlaacActValidLt based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwVlanSlaacActValidLt_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanSlaacActValidLt_Object = MibTableColumn
tmnxWlanGwVlanSlaacActValidLt = _TmnxWlanGwVlanSlaacActValidLt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 3, 1, 5),
    _TmnxWlanGwVlanSlaacActValidLt_Type()
)
tmnxWlanGwVlanSlaacActValidLt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacActValidLt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacActValidLt.setUnits("seconds")


class _TmnxWlanGwVlanSlaacAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanSlaacAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanSlaacAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanSlaacAdminState_Object = MibTableColumn
tmnxWlanGwVlanSlaacAdminState = _TmnxWlanGwVlanSlaacAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 3, 1, 6),
    _TmnxWlanGwVlanSlaacAdminState_Type()
)
tmnxWlanGwVlanSlaacAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacAdminState.setStatus("current")
_TmnxWlanGwVlanBrgTable_Object = MibTable
tmnxWlanGwVlanBrgTable = _TmnxWlanGwVlanBrgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanBrgTable.setStatus("current")
_TmnxWlanGwVlanBrgEntry_Object = MibTableRow
tmnxWlanGwVlanBrgEntry = _TmnxWlanGwVlanBrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanBrgEntry.setStatus("current")
_TmnxWlanGwVlanBrgLastChanged_Type = TimeStamp
_TmnxWlanGwVlanBrgLastChanged_Object = MibTableColumn
tmnxWlanGwVlanBrgLastChanged = _TmnxWlanGwVlanBrgLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 4, 1, 1),
    _TmnxWlanGwVlanBrgLastChanged_Type()
)
tmnxWlanGwVlanBrgLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanBrgLastChanged.setStatus("current")


class _TmnxWlanGwVlanBrgAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanBrgAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanBrgAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanBrgAdminState_Object = MibTableColumn
tmnxWlanGwVlanBrgAdminState = _TmnxWlanGwVlanBrgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 4, 1, 2),
    _TmnxWlanGwVlanBrgAdminState_Type()
)
tmnxWlanGwVlanBrgAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanBrgAdminState.setStatus("current")


class _TmnxWlanGwVlanBrgDefBrgProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanBrgDefBrgProfile based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanBrgDefBrgProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanBrgDefBrgProfile_Object = MibTableColumn
tmnxWlanGwVlanBrgDefBrgProfile = _TmnxWlanGwVlanBrgDefBrgProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 4, 1, 3),
    _TmnxWlanGwVlanBrgDefBrgProfile_Type()
)
tmnxWlanGwVlanBrgDefBrgProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanBrgDefBrgProfile.setStatus("current")


class _TmnxWlanGwVlanBrgAuthedBrgOnly_Type(TruthValue):
    """Custom type tmnxWlanGwVlanBrgAuthedBrgOnly based on TruthValue"""
    defaultValue = 2


_TmnxWlanGwVlanBrgAuthedBrgOnly_Type.__name__ = "TruthValue"
_TmnxWlanGwVlanBrgAuthedBrgOnly_Object = MibTableColumn
tmnxWlanGwVlanBrgAuthedBrgOnly = _TmnxWlanGwVlanBrgAuthedBrgOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 4, 1, 4),
    _TmnxWlanGwVlanBrgAuthedBrgOnly_Type()
)
tmnxWlanGwVlanBrgAuthedBrgOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanBrgAuthedBrgOnly.setStatus("current")
_TmnxWlanGwVlanLeTable_Object = MibTable
tmnxWlanGwVlanLeTable = _TmnxWlanGwVlanLeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeTable.setStatus("current")
_TmnxWlanGwVlanLeEntry_Object = MibTableRow
tmnxWlanGwVlanLeEntry = _TmnxWlanGwVlanLeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeEntry.setStatus("current")
_TmnxWlanGwVlanLeLastChanged_Type = TimeStamp
_TmnxWlanGwVlanLeLastChanged_Object = MibTableColumn
tmnxWlanGwVlanLeLastChanged = _TmnxWlanGwVlanLeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1, 1),
    _TmnxWlanGwVlanLeLastChanged_Type()
)
tmnxWlanGwVlanLeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeLastChanged.setStatus("current")


class _TmnxWlanGwVlanLeAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxWlanGwVlanLeAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxWlanGwVlanLeAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxWlanGwVlanLeAdminState_Object = MibTableColumn
tmnxWlanGwVlanLeAdminState = _TmnxWlanGwVlanLeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1, 2),
    _TmnxWlanGwVlanLeAdminState_Type()
)
tmnxWlanGwVlanLeAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeAdminState.setStatus("current")


class _TmnxWlanGwVlanLeMacTranslation_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanLeMacTranslation based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanLeMacTranslation_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanLeMacTranslation_Object = MibTableColumn
tmnxWlanGwVlanLeMacTranslation = _TmnxWlanGwVlanLeMacTranslation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1, 3),
    _TmnxWlanGwVlanLeMacTranslation_Type()
)
tmnxWlanGwVlanLeMacTranslation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeMacTranslation.setStatus("current")


class _TmnxWlanGwVlanLeBdMacPrefix_Type(MacAddress):
    """Custom type tmnxWlanGwVlanLeBdMacPrefix based on MacAddress"""
    defaultHexValue = "FFFFFF000000"


_TmnxWlanGwVlanLeBdMacPrefix_Type.__name__ = "MacAddress"
_TmnxWlanGwVlanLeBdMacPrefix_Object = MibTableColumn
tmnxWlanGwVlanLeBdMacPrefix = _TmnxWlanGwVlanLeBdMacPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1, 4),
    _TmnxWlanGwVlanLeBdMacPrefix_Type()
)
tmnxWlanGwVlanLeBdMacPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeBdMacPrefix.setStatus("current")


class _TmnxWlanGwVlanLeBdMacPrefixLen_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanLeBdMacPrefixLen based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
    )


_TmnxWlanGwVlanLeBdMacPrefixLen_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanLeBdMacPrefixLen_Object = MibTableColumn
tmnxWlanGwVlanLeBdMacPrefixLen = _TmnxWlanGwVlanLeBdMacPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1, 5),
    _TmnxWlanGwVlanLeBdMacPrefixLen_Type()
)
tmnxWlanGwVlanLeBdMacPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeBdMacPrefixLen.setStatus("current")


class _TmnxWlanGwVlanLeAssistAddrRes_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanLeAssistAddrRes based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanLeAssistAddrRes_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanLeAssistAddrRes_Object = MibTableColumn
tmnxWlanGwVlanLeAssistAddrRes = _TmnxWlanGwVlanLeAssistAddrRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1, 7),
    _TmnxWlanGwVlanLeAssistAddrRes_Type()
)
tmnxWlanGwVlanLeAssistAddrRes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeAssistAddrRes.setStatus("current")


class _TmnxWlanGwVlanLeNetwPolicer_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanLeNetwPolicer based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanLeNetwPolicer_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanLeNetwPolicer_Object = MibTableColumn
tmnxWlanGwVlanLeNetwPolicer = _TmnxWlanGwVlanLeNetwPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1, 8),
    _TmnxWlanGwVlanLeNetwPolicer_Type()
)
tmnxWlanGwVlanLeNetwPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeNetwPolicer.setStatus("current")


class _TmnxWlanGwVlanLeNetwMaxMac_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanLeNetwMaxMac based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TmnxWlanGwVlanLeNetwMaxMac_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanLeNetwMaxMac_Object = MibTableColumn
tmnxWlanGwVlanLeNetwMaxMac = _TmnxWlanGwVlanLeNetwMaxMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1, 10),
    _TmnxWlanGwVlanLeNetwMaxMac_Type()
)
tmnxWlanGwVlanLeNetwMaxMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeNetwMaxMac.setStatus("current")


class _TmnxWlanGwVlanLeNetwAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxWlanGwVlanLeNetwAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 1


_TmnxWlanGwVlanLeNetwAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxWlanGwVlanLeNetwAdminState_Object = MibTableColumn
tmnxWlanGwVlanLeNetwAdminState = _TmnxWlanGwVlanLeNetwAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1, 11),
    _TmnxWlanGwVlanLeNetwAdminState_Type()
)
tmnxWlanGwVlanLeNetwAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeNetwAdminState.setStatus("current")


class _TmnxWlanGwVlanLeAccsPolicer_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanLeAccsPolicer based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanLeAccsPolicer_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanLeAccsPolicer_Object = MibTableColumn
tmnxWlanGwVlanLeAccsPolicer = _TmnxWlanGwVlanLeAccsPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1, 12),
    _TmnxWlanGwVlanLeAccsPolicer_Type()
)
tmnxWlanGwVlanLeAccsPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeAccsPolicer.setStatus("current")


class _TmnxWlanGwVlanLeAccsMaxMac_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanLeAccsMaxMac based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TmnxWlanGwVlanLeAccsMaxMac_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanLeAccsMaxMac_Object = MibTableColumn
tmnxWlanGwVlanLeAccsMaxMac = _TmnxWlanGwVlanLeAccsMaxMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1, 14),
    _TmnxWlanGwVlanLeAccsMaxMac_Type()
)
tmnxWlanGwVlanLeAccsMaxMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeAccsMaxMac.setStatus("current")


class _TmnxWlanGwVlanLeAccsMultiAccess_Type(TruthValue):
    """Custom type tmnxWlanGwVlanLeAccsMultiAccess based on TruthValue"""
    defaultValue = 2


_TmnxWlanGwVlanLeAccsMultiAccess_Type.__name__ = "TruthValue"
_TmnxWlanGwVlanLeAccsMultiAccess_Object = MibTableColumn
tmnxWlanGwVlanLeAccsMultiAccess = _TmnxWlanGwVlanLeAccsMultiAccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 13, 5, 1, 20),
    _TmnxWlanGwVlanLeAccsMultiAccess_Type()
)
tmnxWlanGwVlanLeAccsMultiAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeAccsMultiAccess.setStatus("current")
_TmnxWlanGwTuObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwTuObjs = _TmnxWlanGwTuObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14)
)
_TmnxWlanGwTuNextQryId_Type = Unsigned32
_TmnxWlanGwTuNextQryId_Object = MibScalar
tmnxWlanGwTuNextQryId = _TmnxWlanGwTuNextQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 1),
    _TmnxWlanGwTuNextQryId_Type()
)
tmnxWlanGwTuNextQryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuNextQryId.setStatus("current")
_TmnxWlanGwTuMaxQryId_Type = Unsigned32
_TmnxWlanGwTuMaxQryId_Object = MibScalar
tmnxWlanGwTuMaxQryId = _TmnxWlanGwTuMaxQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 2),
    _TmnxWlanGwTuMaxQryId_Type()
)
tmnxWlanGwTuMaxQryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuMaxQryId.setStatus("current")
_TmnxWlanGwTuQryTable_Object = MibTable
tmnxWlanGwTuQryTable = _TmnxWlanGwTuQryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryTable.setStatus("current")
_TmnxWlanGwTuQryEntry_Object = MibTableRow
tmnxWlanGwTuQryEntry = _TmnxWlanGwTuQryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1)
)
tmnxWlanGwTuQryEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryEntry.setStatus("current")
_TmnxWlanGwTuQryId_Type = Unsigned32
_TmnxWlanGwTuQryId_Object = MibTableColumn
tmnxWlanGwTuQryId = _TmnxWlanGwTuQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 1),
    _TmnxWlanGwTuQryId_Type()
)
tmnxWlanGwTuQryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryId.setStatus("current")
_TmnxWlanGwTuQryRowStatus_Type = RowStatus
_TmnxWlanGwTuQryRowStatus_Object = MibTableColumn
tmnxWlanGwTuQryRowStatus = _TmnxWlanGwTuQryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 2),
    _TmnxWlanGwTuQryRowStatus_Type()
)
tmnxWlanGwTuQryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryRowStatus.setStatus("current")


class _TmnxWlanGwTuQryWhereTuRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxWlanGwTuQryWhereTuRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxWlanGwTuQryWhereTuRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxWlanGwTuQryWhereTuRouter_Object = MibTableColumn
tmnxWlanGwTuQryWhereTuRouter = _TmnxWlanGwTuQryWhereTuRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 3),
    _TmnxWlanGwTuQryWhereTuRouter_Type()
)
tmnxWlanGwTuQryWhereTuRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereTuRouter.setStatus("current")


class _TmnxWlanGwTuQryWhereRemAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwTuQryWhereRemAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwTuQryWhereRemAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwTuQryWhereRemAddrType_Object = MibTableColumn
tmnxWlanGwTuQryWhereRemAddrType = _TmnxWlanGwTuQryWhereRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 4),
    _TmnxWlanGwTuQryWhereRemAddrType_Type()
)
tmnxWlanGwTuQryWhereRemAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereRemAddrType.setStatus("current")


class _TmnxWlanGwTuQryWhereRemAddr_Type(InetAddress):
    """Custom type tmnxWlanGwTuQryWhereRemAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwTuQryWhereRemAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwTuQryWhereRemAddr_Object = MibTableColumn
tmnxWlanGwTuQryWhereRemAddr = _TmnxWlanGwTuQryWhereRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 5),
    _TmnxWlanGwTuQryWhereRemAddr_Type()
)
tmnxWlanGwTuQryWhereRemAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereRemAddr.setStatus("current")


class _TmnxWlanGwTuQryWhereLocAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwTuQryWhereLocAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwTuQryWhereLocAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwTuQryWhereLocAddrType_Object = MibTableColumn
tmnxWlanGwTuQryWhereLocAddrType = _TmnxWlanGwTuQryWhereLocAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 6),
    _TmnxWlanGwTuQryWhereLocAddrType_Type()
)
tmnxWlanGwTuQryWhereLocAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereLocAddrType.setStatus("current")


class _TmnxWlanGwTuQryWhereLocAddr_Type(InetAddress):
    """Custom type tmnxWlanGwTuQryWhereLocAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwTuQryWhereLocAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwTuQryWhereLocAddr_Object = MibTableColumn
tmnxWlanGwTuQryWhereLocAddr = _TmnxWlanGwTuQryWhereLocAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 7),
    _TmnxWlanGwTuQryWhereLocAddr_Type()
)
tmnxWlanGwTuQryWhereLocAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereLocAddr.setStatus("current")


class _TmnxWlanGwTuQryWhereAddrFamily_Type(InetAddressType):
    """Custom type tmnxWlanGwTuQryWhereAddrFamily based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwTuQryWhereAddrFamily_Type.__name__ = "InetAddressType"
_TmnxWlanGwTuQryWhereAddrFamily_Object = MibTableColumn
tmnxWlanGwTuQryWhereAddrFamily = _TmnxWlanGwTuQryWhereAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 8),
    _TmnxWlanGwTuQryWhereAddrFamily_Type()
)
tmnxWlanGwTuQryWhereAddrFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereAddrFamily.setStatus("current")


class _TmnxWlanGwTuQryWhereEncap_Type(Bits):
    """Custom type tmnxWlanGwTuQryWhereEncap based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("gre", 0),
          ("l2tp", 1),
          ("l2", 2),
          ("vxlan", 3))
    )

_TmnxWlanGwTuQryWhereEncap_Type.__name__ = "Bits"
_TmnxWlanGwTuQryWhereEncap_Object = MibTableColumn
tmnxWlanGwTuQryWhereEncap = _TmnxWlanGwTuQryWhereEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 15),
    _TmnxWlanGwTuQryWhereEncap_Type()
)
tmnxWlanGwTuQryWhereEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereEncap.setStatus("current")


class _TmnxWlanGwTuQryWhereEncapTag1_Type(QTagFullRangeOrNone):
    """Custom type tmnxWlanGwTuQryWhereEncapTag1 based on QTagFullRangeOrNone"""
    defaultValue = -1


_TmnxWlanGwTuQryWhereEncapTag1_Type.__name__ = "QTagFullRangeOrNone"
_TmnxWlanGwTuQryWhereEncapTag1_Object = MibTableColumn
tmnxWlanGwTuQryWhereEncapTag1 = _TmnxWlanGwTuQryWhereEncapTag1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 16),
    _TmnxWlanGwTuQryWhereEncapTag1_Type()
)
tmnxWlanGwTuQryWhereEncapTag1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereEncapTag1.setStatus("current")


class _TmnxWlanGwTuQryWhereEncapTag2_Type(QTagFullRangeOrNone):
    """Custom type tmnxWlanGwTuQryWhereEncapTag2 based on QTagFullRangeOrNone"""
    defaultValue = -1


_TmnxWlanGwTuQryWhereEncapTag2_Type.__name__ = "QTagFullRangeOrNone"
_TmnxWlanGwTuQryWhereEncapTag2_Object = MibTableColumn
tmnxWlanGwTuQryWhereEncapTag2 = _TmnxWlanGwTuQryWhereEncapTag2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 17),
    _TmnxWlanGwTuQryWhereEncapTag2_Type()
)
tmnxWlanGwTuQryWhereEncapTag2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereEncapTag2.setStatus("current")


class _TmnxWlanGwTuQryWhereApSapPortId_Type(TmnxPortID):
    """Custom type tmnxWlanGwTuQryWhereApSapPortId based on TmnxPortID"""
    defaultValue = 503316480


_TmnxWlanGwTuQryWhereApSapPortId_Type.__name__ = "TmnxPortID"
_TmnxWlanGwTuQryWhereApSapPortId_Object = MibTableColumn
tmnxWlanGwTuQryWhereApSapPortId = _TmnxWlanGwTuQryWhereApSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 18),
    _TmnxWlanGwTuQryWhereApSapPortId_Type()
)
tmnxWlanGwTuQryWhereApSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereApSapPortId.setStatus("current")


class _TmnxWlanGwTuQryWhereApSapEncap_Type(TmnxEncapVal):
    """Custom type tmnxWlanGwTuQryWhereApSapEncap based on TmnxEncapVal"""
    defaultValue = 0


_TmnxWlanGwTuQryWhereApSapEncap_Type.__name__ = "TmnxEncapVal"
_TmnxWlanGwTuQryWhereApSapEncap_Object = MibTableColumn
tmnxWlanGwTuQryWhereApSapEncap = _TmnxWlanGwTuQryWhereApSapEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 19),
    _TmnxWlanGwTuQryWhereApSapEncap_Type()
)
tmnxWlanGwTuQryWhereApSapEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereApSapEncap.setStatus("current")


class _TmnxWlanGwTuQryWhereNumUeMin_Type(Unsigned32):
    """Custom type tmnxWlanGwTuQryWhereNumUeMin based on Unsigned32"""
    defaultValue = 0


_TmnxWlanGwTuQryWhereNumUeMin_Type.__name__ = "Unsigned32"
_TmnxWlanGwTuQryWhereNumUeMin_Object = MibTableColumn
tmnxWlanGwTuQryWhereNumUeMin = _TmnxWlanGwTuQryWhereNumUeMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 20),
    _TmnxWlanGwTuQryWhereNumUeMin_Type()
)
tmnxWlanGwTuQryWhereNumUeMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereNumUeMin.setStatus("current")


class _TmnxWlanGwTuQryWhereNumUeMax_Type(Unsigned32):
    """Custom type tmnxWlanGwTuQryWhereNumUeMax based on Unsigned32"""
    defaultValue = 4294967295


_TmnxWlanGwTuQryWhereNumUeMax_Type.__name__ = "Unsigned32"
_TmnxWlanGwTuQryWhereNumUeMax_Object = MibTableColumn
tmnxWlanGwTuQryWhereNumUeMax = _TmnxWlanGwTuQryWhereNumUeMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 21),
    _TmnxWlanGwTuQryWhereNumUeMax_Type()
)
tmnxWlanGwTuQryWhereNumUeMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereNumUeMax.setStatus("current")


class _TmnxWlanGwTuQryWhereApLearnFail_Type(Integer32):
    """Custom type tmnxWlanGwTuQryWhereApLearnFail based on Integer32"""
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
        *(("dontCare", 0),
          ("true", 1),
          ("false", 2))
    )


_TmnxWlanGwTuQryWhereApLearnFail_Type.__name__ = "Integer32"
_TmnxWlanGwTuQryWhereApLearnFail_Object = MibTableColumn
tmnxWlanGwTuQryWhereApLearnFail = _TmnxWlanGwTuQryWhereApLearnFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 22),
    _TmnxWlanGwTuQryWhereApLearnFail_Type()
)
tmnxWlanGwTuQryWhereApLearnFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereApLearnFail.setStatus("current")


class _TmnxWlanGwTuQryWhereUeType_Type(Bits):
    """Custom type tmnxWlanGwTuQryWhereUeType based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("migrant", 0),
          ("dsm", 1),
          ("l2w", 2),
          ("esm", 3),
          ("xcon", 4))
    )

_TmnxWlanGwTuQryWhereUeType_Type.__name__ = "Bits"
_TmnxWlanGwTuQryWhereUeType_Object = MibTableColumn
tmnxWlanGwTuQryWhereUeType = _TmnxWlanGwTuQryWhereUeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 23),
    _TmnxWlanGwTuQryWhereUeType_Type()
)
tmnxWlanGwTuQryWhereUeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryWhereUeType.setStatus("current")


class _TmnxWlanGwTuQryDoGetNumResults_Type(TruthValue):
    """Custom type tmnxWlanGwTuQryDoGetNumResults based on TruthValue"""
    defaultValue = 2


_TmnxWlanGwTuQryDoGetNumResults_Type.__name__ = "TruthValue"
_TmnxWlanGwTuQryDoGetNumResults_Object = MibTableColumn
tmnxWlanGwTuQryDoGetNumResults = _TmnxWlanGwTuQryDoGetNumResults_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 199),
    _TmnxWlanGwTuQryDoGetNumResults_Type()
)
tmnxWlanGwTuQryDoGetNumResults.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryDoGetNumResults.setStatus("current")
_TmnxWlanGwTuQryNumResults_Type = Gauge32
_TmnxWlanGwTuQryNumResults_Object = MibTableColumn
tmnxWlanGwTuQryNumResults = _TmnxWlanGwTuQryNumResults_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 200),
    _TmnxWlanGwTuQryNumResults_Type()
)
tmnxWlanGwTuQryNumResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryNumResults.setStatus("current")
_TmnxWlanGwTuQryName_Type = TNamedItem
_TmnxWlanGwTuQryName_Object = MibTableColumn
tmnxWlanGwTuQryName = _TmnxWlanGwTuQryName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 201),
    _TmnxWlanGwTuQryName_Type()
)
tmnxWlanGwTuQryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryName.setStatus("current")
_TmnxWlanGwTuQryVolatile_Type = TruthValue
_TmnxWlanGwTuQryVolatile_Object = MibTableColumn
tmnxWlanGwTuQryVolatile = _TmnxWlanGwTuQryVolatile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 3, 1, 202),
    _TmnxWlanGwTuQryVolatile_Type()
)
tmnxWlanGwTuQryVolatile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQryVolatile.setStatus("current")
_TmnxWlanGwTuTable_Object = MibTable
tmnxWlanGwTuTable = _TmnxWlanGwTuTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuTable.setStatus("current")
_TmnxWlanGwTuEntry_Object = MibTableRow
tmnxWlanGwTuEntry = _TmnxWlanGwTuEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1)
)
tmnxWlanGwTuEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuRouter"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuEncap"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuRemoteAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuLocalAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuLocalAddr"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuEntry.setStatus("current")
_TmnxWlanGwTuRouter_Type = TmnxVRtrID
_TmnxWlanGwTuRouter_Object = MibTableColumn
tmnxWlanGwTuRouter = _TmnxWlanGwTuRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 1),
    _TmnxWlanGwTuRouter_Type()
)
tmnxWlanGwTuRouter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwTuRouter.setStatus("current")
_TmnxWlanGwTuEncap_Type = TmnxWlanGwUeEncapsulation
_TmnxWlanGwTuEncap_Object = MibTableColumn
tmnxWlanGwTuEncap = _TmnxWlanGwTuEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 2),
    _TmnxWlanGwTuEncap_Type()
)
tmnxWlanGwTuEncap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwTuEncap.setStatus("current")
_TmnxWlanGwTuRemoteAddrType_Type = InetAddressType
_TmnxWlanGwTuRemoteAddrType_Object = MibTableColumn
tmnxWlanGwTuRemoteAddrType = _TmnxWlanGwTuRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 3),
    _TmnxWlanGwTuRemoteAddrType_Type()
)
tmnxWlanGwTuRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwTuRemoteAddrType.setStatus("current")


class _TmnxWlanGwTuRemoteAddr_Type(InetAddress):
    """Custom type tmnxWlanGwTuRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwTuRemoteAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwTuRemoteAddr_Object = MibTableColumn
tmnxWlanGwTuRemoteAddr = _TmnxWlanGwTuRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 4),
    _TmnxWlanGwTuRemoteAddr_Type()
)
tmnxWlanGwTuRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwTuRemoteAddr.setStatus("current")
_TmnxWlanGwTuLocalAddrType_Type = InetAddressType
_TmnxWlanGwTuLocalAddrType_Object = MibTableColumn
tmnxWlanGwTuLocalAddrType = _TmnxWlanGwTuLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 5),
    _TmnxWlanGwTuLocalAddrType_Type()
)
tmnxWlanGwTuLocalAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwTuLocalAddrType.setStatus("current")


class _TmnxWlanGwTuLocalAddr_Type(InetAddress):
    """Custom type tmnxWlanGwTuLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwTuLocalAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwTuLocalAddr_Object = MibTableColumn
tmnxWlanGwTuLocalAddr = _TmnxWlanGwTuLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 6),
    _TmnxWlanGwTuLocalAddr_Type()
)
tmnxWlanGwTuLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwTuLocalAddr.setStatus("current")


class _TmnxWlanGwTuFirstMoveTime_Type(DateAndTime):
    """Custom type tmnxWlanGwTuFirstMoveTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwTuFirstMoveTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwTuFirstMoveTime_Object = MibTableColumn
tmnxWlanGwTuFirstMoveTime = _TmnxWlanGwTuFirstMoveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 7),
    _TmnxWlanGwTuFirstMoveTime_Type()
)
tmnxWlanGwTuFirstMoveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuFirstMoveTime.setStatus("current")
_TmnxWlanGwTuIsaGroup_Type = TmnxWlanGwIsaGrpIdOrZero
_TmnxWlanGwTuIsaGroup_Object = MibTableColumn
tmnxWlanGwTuIsaGroup = _TmnxWlanGwTuIsaGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 8),
    _TmnxWlanGwTuIsaGroup_Type()
)
tmnxWlanGwTuIsaGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuIsaGroup.setStatus("current")
_TmnxWlanGwTuIsaMember_Type = Unsigned32
_TmnxWlanGwTuIsaMember_Object = MibTableColumn
tmnxWlanGwTuIsaMember = _TmnxWlanGwTuIsaMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 9),
    _TmnxWlanGwTuIsaMember_Type()
)
tmnxWlanGwTuIsaMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuIsaMember.setStatus("current")
_TmnxWlanGwTuService_Type = TmnxServId
_TmnxWlanGwTuService_Object = MibTableColumn
tmnxWlanGwTuService = _TmnxWlanGwTuService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 10),
    _TmnxWlanGwTuService_Type()
)
tmnxWlanGwTuService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuService.setStatus("current")
_TmnxWlanGwTuInterface_Type = InterfaceIndexOrZero
_TmnxWlanGwTuInterface_Object = MibTableColumn
tmnxWlanGwTuInterface = _TmnxWlanGwTuInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 11),
    _TmnxWlanGwTuInterface_Type()
)
tmnxWlanGwTuInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuInterface.setStatus("current")
_TmnxWlanGwTuApMacAddress_Type = MacAddress
_TmnxWlanGwTuApMacAddress_Object = MibTableColumn
tmnxWlanGwTuApMacAddress = _TmnxWlanGwTuApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 12),
    _TmnxWlanGwTuApMacAddress_Type()
)
tmnxWlanGwTuApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuApMacAddress.setStatus("current")
_TmnxWlanGwTuApLearnFailed_Type = TruthValue
_TmnxWlanGwTuApLearnFailed_Object = MibTableColumn
tmnxWlanGwTuApLearnFailed = _TmnxWlanGwTuApLearnFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 13),
    _TmnxWlanGwTuApLearnFailed_Type()
)
tmnxWlanGwTuApLearnFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuApLearnFailed.setStatus("current")
_TmnxWlanGwTuEncapTag1_Type = QTagFullRangeOrNone
_TmnxWlanGwTuEncapTag1_Object = MibTableColumn
tmnxWlanGwTuEncapTag1 = _TmnxWlanGwTuEncapTag1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 15),
    _TmnxWlanGwTuEncapTag1_Type()
)
tmnxWlanGwTuEncapTag1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuEncapTag1.setStatus("current")
_TmnxWlanGwTuEncapTag2_Type = QTagFullRangeOrNone
_TmnxWlanGwTuEncapTag2_Object = MibTableColumn
tmnxWlanGwTuEncapTag2 = _TmnxWlanGwTuEncapTag2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 16),
    _TmnxWlanGwTuEncapTag2_Type()
)
tmnxWlanGwTuEncapTag2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuEncapTag2.setStatus("current")
_TmnxWlanGwTuApSapPortId_Type = TmnxPortID
_TmnxWlanGwTuApSapPortId_Object = MibTableColumn
tmnxWlanGwTuApSapPortId = _TmnxWlanGwTuApSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 17),
    _TmnxWlanGwTuApSapPortId_Type()
)
tmnxWlanGwTuApSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuApSapPortId.setStatus("current")
_TmnxWlanGwTuApSapEncapVal_Type = TmnxEncapVal
_TmnxWlanGwTuApSapEncapVal_Object = MibTableColumn
tmnxWlanGwTuApSapEncapVal = _TmnxWlanGwTuApSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 18),
    _TmnxWlanGwTuApSapEncapVal_Type()
)
tmnxWlanGwTuApSapEncapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuApSapEncapVal.setStatus("current")
_TmnxWlanGwTuRemoteUdpPort_Type = InetPortNumber
_TmnxWlanGwTuRemoteUdpPort_Object = MibTableColumn
tmnxWlanGwTuRemoteUdpPort = _TmnxWlanGwTuRemoteUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 19),
    _TmnxWlanGwTuRemoteUdpPort_Type()
)
tmnxWlanGwTuRemoteUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuRemoteUdpPort.setStatus("current")
_TmnxWlanGwTuNumUe_Type = Gauge32
_TmnxWlanGwTuNumUe_Object = MibTableColumn
tmnxWlanGwTuNumUe = _TmnxWlanGwTuNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 50),
    _TmnxWlanGwTuNumUe_Type()
)
tmnxWlanGwTuNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuNumUe.setStatus("current")
_TmnxWlanGwTuNumUeMigrant_Type = Gauge32
_TmnxWlanGwTuNumUeMigrant_Object = MibTableColumn
tmnxWlanGwTuNumUeMigrant = _TmnxWlanGwTuNumUeMigrant_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 51),
    _TmnxWlanGwTuNumUeMigrant_Type()
)
tmnxWlanGwTuNumUeMigrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuNumUeMigrant.setStatus("current")
_TmnxWlanGwTuNumUeDsm_Type = Gauge32
_TmnxWlanGwTuNumUeDsm_Object = MibTableColumn
tmnxWlanGwTuNumUeDsm = _TmnxWlanGwTuNumUeDsm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 52),
    _TmnxWlanGwTuNumUeDsm_Type()
)
tmnxWlanGwTuNumUeDsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuNumUeDsm.setStatus("current")
_TmnxWlanGwTuNumUeL2w_Type = Gauge32
_TmnxWlanGwTuNumUeL2w_Object = MibTableColumn
tmnxWlanGwTuNumUeL2w = _TmnxWlanGwTuNumUeL2w_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 53),
    _TmnxWlanGwTuNumUeL2w_Type()
)
tmnxWlanGwTuNumUeL2w.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuNumUeL2w.setStatus("current")
_TmnxWlanGwTuNumUeEsm_Type = Gauge32
_TmnxWlanGwTuNumUeEsm_Object = MibTableColumn
tmnxWlanGwTuNumUeEsm = _TmnxWlanGwTuNumUeEsm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 54),
    _TmnxWlanGwTuNumUeEsm_Type()
)
tmnxWlanGwTuNumUeEsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuNumUeEsm.setStatus("current")
_TmnxWlanGwTuNumUeXcon_Type = Gauge32
_TmnxWlanGwTuNumUeXcon_Object = MibTableColumn
tmnxWlanGwTuNumUeXcon = _TmnxWlanGwTuNumUeXcon_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 14, 4, 1, 55),
    _TmnxWlanGwTuNumUeXcon_Type()
)
tmnxWlanGwTuNumUeXcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuNumUeXcon.setStatus("current")
_TmnxWlanGwBdUeTable_Object = MibTable
tmnxWlanGwBdUeTable = _TmnxWlanGwBdUeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeTable.setStatus("current")
_TmnxWlanGwBdUeEntry_Object = MibTableRow
tmnxWlanGwBdUeEntry = _TmnxWlanGwBdUeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1)
)
tmnxWlanGwBdUeEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdBridgeId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeMacAddress"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeEntry.setStatus("current")
_TmnxWlanGwBdBridgeId_Type = Unsigned32
_TmnxWlanGwBdBridgeId_Object = MibTableColumn
tmnxWlanGwBdBridgeId = _TmnxWlanGwBdBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 1),
    _TmnxWlanGwBdBridgeId_Type()
)
tmnxWlanGwBdBridgeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwBdBridgeId.setStatus("current")
_TmnxWlanGwBdUeMacAddress_Type = MacAddress
_TmnxWlanGwBdUeMacAddress_Object = MibTableColumn
tmnxWlanGwBdUeMacAddress = _TmnxWlanGwBdUeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 2),
    _TmnxWlanGwBdUeMacAddress_Type()
)
tmnxWlanGwBdUeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeMacAddress.setStatus("current")
_TmnxWlanGwBdUeQTag_Type = QTagFullRangeOrNone
_TmnxWlanGwBdUeQTag_Object = MibTableColumn
tmnxWlanGwBdUeQTag = _TmnxWlanGwBdUeQTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 3),
    _TmnxWlanGwBdUeQTag_Type()
)
tmnxWlanGwBdUeQTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeQTag.setStatus("current")
_TmnxWlanGwBdUeMplsLabel_Type = MplsLabel
_TmnxWlanGwBdUeMplsLabel_Object = MibTableColumn
tmnxWlanGwBdUeMplsLabel = _TmnxWlanGwBdUeMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 4),
    _TmnxWlanGwBdUeMplsLabel_Type()
)
tmnxWlanGwBdUeMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeMplsLabel.setStatus("current")
_TmnxWlanGwBdUeTuRouter_Type = TmnxVRtrID
_TmnxWlanGwBdUeTuRouter_Object = MibTableColumn
tmnxWlanGwBdUeTuRouter = _TmnxWlanGwBdUeTuRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 5),
    _TmnxWlanGwBdUeTuRouter_Type()
)
tmnxWlanGwBdUeTuRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeTuRouter.setStatus("current")
_TmnxWlanGwBdUeTuAddrType_Type = InetAddressType
_TmnxWlanGwBdUeTuAddrType_Object = MibTableColumn
tmnxWlanGwBdUeTuAddrType = _TmnxWlanGwBdUeTuAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 6),
    _TmnxWlanGwBdUeTuAddrType_Type()
)
tmnxWlanGwBdUeTuAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeTuAddrType.setStatus("current")


class _TmnxWlanGwBdUeTuRemoteAddr_Type(InetAddress):
    """Custom type tmnxWlanGwBdUeTuRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwBdUeTuRemoteAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwBdUeTuRemoteAddr_Object = MibTableColumn
tmnxWlanGwBdUeTuRemoteAddr = _TmnxWlanGwBdUeTuRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 7),
    _TmnxWlanGwBdUeTuRemoteAddr_Type()
)
tmnxWlanGwBdUeTuRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeTuRemoteAddr.setStatus("current")


class _TmnxWlanGwBdUeTuLocalAddr_Type(InetAddress):
    """Custom type tmnxWlanGwBdUeTuLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwBdUeTuLocalAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwBdUeTuLocalAddr_Object = MibTableColumn
tmnxWlanGwBdUeTuLocalAddr = _TmnxWlanGwBdUeTuLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 8),
    _TmnxWlanGwBdUeTuLocalAddr_Type()
)
tmnxWlanGwBdUeTuLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeTuLocalAddr.setStatus("current")
_TmnxWlanGwBdUeTuQosRetailService_Type = TmnxServId
_TmnxWlanGwBdUeTuQosRetailService_Object = MibTableColumn
tmnxWlanGwBdUeTuQosRetailService = _TmnxWlanGwBdUeTuQosRetailService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 9),
    _TmnxWlanGwBdUeTuQosRetailService_Type()
)
tmnxWlanGwBdUeTuQosRetailService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeTuQosRetailService.setStatus("current")
_TmnxWlanGwBdUeSsid_Type = TNamedItemOrEmpty
_TmnxWlanGwBdUeSsid_Object = MibTableColumn
tmnxWlanGwBdUeSsid = _TmnxWlanGwBdUeSsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 10),
    _TmnxWlanGwBdUeSsid_Type()
)
tmnxWlanGwBdUeSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeSsid.setStatus("current")
_TmnxWlanGwBdUePrevApAddrType_Type = InetAddressType
_TmnxWlanGwBdUePrevApAddrType_Object = MibTableColumn
tmnxWlanGwBdUePrevApAddrType = _TmnxWlanGwBdUePrevApAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 11),
    _TmnxWlanGwBdUePrevApAddrType_Type()
)
tmnxWlanGwBdUePrevApAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUePrevApAddrType.setStatus("current")


class _TmnxWlanGwBdUePrevApAddr_Type(InetAddress):
    """Custom type tmnxWlanGwBdUePrevApAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwBdUePrevApAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwBdUePrevApAddr_Object = MibTableColumn
tmnxWlanGwBdUePrevApAddr = _TmnxWlanGwBdUePrevApAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 12),
    _TmnxWlanGwBdUePrevApAddr_Type()
)
tmnxWlanGwBdUePrevApAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUePrevApAddr.setStatus("current")


class _TmnxWlanGwBdUeLastMoveTime_Type(DateAndTime):
    """Custom type tmnxWlanGwBdUeLastMoveTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwBdUeLastMoveTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwBdUeLastMoveTime_Object = MibTableColumn
tmnxWlanGwBdUeLastMoveTime = _TmnxWlanGwBdUeLastMoveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 13),
    _TmnxWlanGwBdUeLastMoveTime_Type()
)
tmnxWlanGwBdUeLastMoveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeLastMoveTime.setStatus("current")
_TmnxWlanGwBdUeImsi_Type = TmnxMobImsiStr
_TmnxWlanGwBdUeImsi_Object = MibTableColumn
tmnxWlanGwBdUeImsi = _TmnxWlanGwBdUeImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 15),
    _TmnxWlanGwBdUeImsi_Type()
)
tmnxWlanGwBdUeImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeImsi.setStatus("current")
_TmnxWlanGwBdUeService_Type = TmnxServId
_TmnxWlanGwBdUeService_Object = MibTableColumn
tmnxWlanGwBdUeService = _TmnxWlanGwBdUeService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 16),
    _TmnxWlanGwBdUeService_Type()
)
tmnxWlanGwBdUeService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeService.setStatus("current")
_TmnxWlanGwBdUeSapPortId_Type = TmnxPortID
_TmnxWlanGwBdUeSapPortId_Object = MibTableColumn
tmnxWlanGwBdUeSapPortId = _TmnxWlanGwBdUeSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 17),
    _TmnxWlanGwBdUeSapPortId_Type()
)
tmnxWlanGwBdUeSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeSapPortId.setStatus("current")
_TmnxWlanGwBdUeSapPortEncapValue_Type = TmnxEncapVal
_TmnxWlanGwBdUeSapPortEncapValue_Object = MibTableColumn
tmnxWlanGwBdUeSapPortEncapValue = _TmnxWlanGwBdUeSapPortEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 18),
    _TmnxWlanGwBdUeSapPortEncapValue_Type()
)
tmnxWlanGwBdUeSapPortEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeSapPortEncapValue.setStatus("current")
_TmnxWlanGwBdUeEncapsulation_Type = TmnxWlanGwUeEncapsulation
_TmnxWlanGwBdUeEncapsulation_Object = MibTableColumn
tmnxWlanGwBdUeEncapsulation = _TmnxWlanGwBdUeEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 15, 1, 19),
    _TmnxWlanGwBdUeEncapsulation_Type()
)
tmnxWlanGwBdUeEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdUeEncapsulation.setStatus("current")
_TmnxWlanGwXcnctTable_Object = MibTable
tmnxWlanGwXcnctTable = _TmnxWlanGwXcnctTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 16)
)
if mibBuilder.loadTexts:
    tmnxWlanGwXcnctTable.setStatus("current")
_TmnxWlanGwXcnctEntry_Object = MibTableRow
tmnxWlanGwXcnctEntry = _TmnxWlanGwXcnctEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 16, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwXcnctEntry.setStatus("current")
_TmnxWlanGwXcnctLastCh_Type = TimeStamp
_TmnxWlanGwXcnctLastCh_Object = MibTableColumn
tmnxWlanGwXcnctLastCh = _TmnxWlanGwXcnctLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 16, 1, 1),
    _TmnxWlanGwXcnctLastCh_Type()
)
tmnxWlanGwXcnctLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwXcnctLastCh.setStatus("current")


class _TmnxWlanGwXcnctIsaGroup_Type(TmnxWlanGwIsaGrpIdOrZero):
    """Custom type tmnxWlanGwXcnctIsaGroup based on TmnxWlanGwIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxWlanGwXcnctIsaGroup_Type.__name__ = "TmnxWlanGwIsaGrpIdOrZero"
_TmnxWlanGwXcnctIsaGroup_Object = MibTableColumn
tmnxWlanGwXcnctIsaGroup = _TmnxWlanGwXcnctIsaGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 16, 1, 2),
    _TmnxWlanGwXcnctIsaGroup_Type()
)
tmnxWlanGwXcnctIsaGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwXcnctIsaGroup.setStatus("current")


class _TmnxWlanGwXcnctTnlSrcIpAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwXcnctTnlSrcIpAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwXcnctTnlSrcIpAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwXcnctTnlSrcIpAddrType_Object = MibTableColumn
tmnxWlanGwXcnctTnlSrcIpAddrType = _TmnxWlanGwXcnctTnlSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 16, 1, 3),
    _TmnxWlanGwXcnctTnlSrcIpAddrType_Type()
)
tmnxWlanGwXcnctTnlSrcIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwXcnctTnlSrcIpAddrType.setStatus("current")


class _TmnxWlanGwXcnctTnlSrcIpAddr_Type(InetAddress):
    """Custom type tmnxWlanGwXcnctTnlSrcIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwXcnctTnlSrcIpAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwXcnctTnlSrcIpAddr_Object = MibTableColumn
tmnxWlanGwXcnctTnlSrcIpAddr = _TmnxWlanGwXcnctTnlSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 16, 1, 4),
    _TmnxWlanGwXcnctTnlSrcIpAddr_Type()
)
tmnxWlanGwXcnctTnlSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwXcnctTnlSrcIpAddr.setStatus("current")


class _TmnxWlanGwXcnctTnlSrcIpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxWlanGwXcnctTnlSrcIpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxWlanGwXcnctTnlSrcIpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxWlanGwXcnctTnlSrcIpPrefixLen_Object = MibTableColumn
tmnxWlanGwXcnctTnlSrcIpPrefixLen = _TmnxWlanGwXcnctTnlSrcIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 16, 1, 5),
    _TmnxWlanGwXcnctTnlSrcIpPrefixLen_Type()
)
tmnxWlanGwXcnctTnlSrcIpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwXcnctTnlSrcIpPrefixLen.setStatus("current")


class _TmnxWlanGwXcnctAdminState_Type(TmnxAdminState):
    """Custom type tmnxWlanGwXcnctAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxWlanGwXcnctAdminState_Type.__name__ = "TmnxAdminState"
_TmnxWlanGwXcnctAdminState_Object = MibTableColumn
tmnxWlanGwXcnctAdminState = _TmnxWlanGwXcnctAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 16, 1, 6),
    _TmnxWlanGwXcnctAdminState_Type()
)
tmnxWlanGwXcnctAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwXcnctAdminState.setStatus("current")
_TmnxWlanGwLeTable_Object = MibTable
tmnxWlanGwLeTable = _TmnxWlanGwLeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 17)
)
if mibBuilder.loadTexts:
    tmnxWlanGwLeTable.setStatus("current")
_TmnxWlanGwLeEntry_Object = MibTableRow
tmnxWlanGwLeEntry = _TmnxWlanGwLeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 17, 1)
)
tmnxWlanGwLeEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwLeEntry.setStatus("current")
_TmnxWlanGwLeRowStatus_Type = RowStatus
_TmnxWlanGwLeRowStatus_Object = MibTableColumn
tmnxWlanGwLeRowStatus = _TmnxWlanGwLeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 17, 1, 1),
    _TmnxWlanGwLeRowStatus_Type()
)
tmnxWlanGwLeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwLeRowStatus.setStatus("current")
_TmnxWlanGwLeLastChanged_Type = TimeStamp
_TmnxWlanGwLeLastChanged_Object = MibTableColumn
tmnxWlanGwLeLastChanged = _TmnxWlanGwLeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 17, 1, 2),
    _TmnxWlanGwLeLastChanged_Type()
)
tmnxWlanGwLeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwLeLastChanged.setStatus("current")


class _TmnxWlanGwLeAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxWlanGwLeAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxWlanGwLeAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxWlanGwLeAdminState_Object = MibTableColumn
tmnxWlanGwLeAdminState = _TmnxWlanGwLeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 17, 1, 3),
    _TmnxWlanGwLeAdminState_Type()
)
tmnxWlanGwLeAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwLeAdminState.setStatus("current")


class _TmnxWlanGwLeWlanGwGrpId_Type(TmnxWlanGwIsaGrpIdOrZero):
    """Custom type tmnxWlanGwLeWlanGwGrpId based on TmnxWlanGwIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxWlanGwLeWlanGwGrpId_Type.__name__ = "TmnxWlanGwIsaGrpIdOrZero"
_TmnxWlanGwLeWlanGwGrpId_Object = MibTableColumn
tmnxWlanGwLeWlanGwGrpId = _TmnxWlanGwLeWlanGwGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 17, 1, 4),
    _TmnxWlanGwLeWlanGwGrpId_Type()
)
tmnxWlanGwLeWlanGwGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwLeWlanGwGrpId.setStatus("current")


class _TmnxWlanGwLeVtepStartType_Type(InetAddressType):
    """Custom type tmnxWlanGwLeVtepStartType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwLeVtepStartType_Type.__name__ = "InetAddressType"
_TmnxWlanGwLeVtepStartType_Object = MibTableColumn
tmnxWlanGwLeVtepStartType = _TmnxWlanGwLeVtepStartType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 17, 1, 5),
    _TmnxWlanGwLeVtepStartType_Type()
)
tmnxWlanGwLeVtepStartType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwLeVtepStartType.setStatus("current")


class _TmnxWlanGwLeVtepStart_Type(InetAddress):
    """Custom type tmnxWlanGwLeVtepStart based on InetAddress"""
    defaultValue = OctetString("")

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwLeVtepStart_Type.__name__ = "InetAddress"
_TmnxWlanGwLeVtepStart_Object = MibTableColumn
tmnxWlanGwLeVtepStart = _TmnxWlanGwLeVtepStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 17, 1, 6),
    _TmnxWlanGwLeVtepStart_Type()
)
tmnxWlanGwLeVtepStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwLeVtepStart.setStatus("current")


class _TmnxWlanGwLeVtepEndType_Type(InetAddressType):
    """Custom type tmnxWlanGwLeVtepEndType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwLeVtepEndType_Type.__name__ = "InetAddressType"
_TmnxWlanGwLeVtepEndType_Object = MibTableColumn
tmnxWlanGwLeVtepEndType = _TmnxWlanGwLeVtepEndType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 17, 1, 7),
    _TmnxWlanGwLeVtepEndType_Type()
)
tmnxWlanGwLeVtepEndType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwLeVtepEndType.setStatus("current")


class _TmnxWlanGwLeVtepEnd_Type(InetAddress):
    """Custom type tmnxWlanGwLeVtepEnd based on InetAddress"""
    defaultValue = OctetString("")

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwLeVtepEnd_Type.__name__ = "InetAddress"
_TmnxWlanGwLeVtepEnd_Object = MibTableColumn
tmnxWlanGwLeVtepEnd = _TmnxWlanGwLeVtepEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 17, 1, 8),
    _TmnxWlanGwLeVtepEnd_Type()
)
tmnxWlanGwLeVtepEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwLeVtepEnd.setStatus("current")


class _TmnxWlanGwLeVxlanPort_Type(InetPortNumber):
    """Custom type tmnxWlanGwLeVxlanPort based on InetPortNumber"""
    defaultValue = 4789

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4789, 4789),
        ValueRangeConstraint(8472, 8472),
    )


_TmnxWlanGwLeVxlanPort_Type.__name__ = "InetPortNumber"
_TmnxWlanGwLeVxlanPort_Object = MibTableColumn
tmnxWlanGwLeVxlanPort = _TmnxWlanGwLeVxlanPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 17, 1, 9),
    _TmnxWlanGwLeVxlanPort_Type()
)
tmnxWlanGwLeVxlanPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwLeVxlanPort.setStatus("current")
_TmnxWlanGwBdTable_Object = MibTable
tmnxWlanGwBdTable = _TmnxWlanGwBdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18)
)
if mibBuilder.loadTexts:
    tmnxWlanGwBdTable.setStatus("current")
_TmnxWlanGwBdEntry_Object = MibTableRow
tmnxWlanGwBdEntry = _TmnxWlanGwBdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1)
)
tmnxWlanGwBdEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdBridgeId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwBdEntry.setStatus("current")
_TmnxWlanGwBdVNI_Type = Unsigned32
_TmnxWlanGwBdVNI_Object = MibTableColumn
tmnxWlanGwBdVNI = _TmnxWlanGwBdVNI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 1),
    _TmnxWlanGwBdVNI_Type()
)
tmnxWlanGwBdVNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdVNI.setStatus("current")
_TmnxWlanGwBdRT_Type = TNamedItemOrEmpty
_TmnxWlanGwBdRT_Object = MibTableColumn
tmnxWlanGwBdRT = _TmnxWlanGwBdRT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 2),
    _TmnxWlanGwBdRT_Type()
)
tmnxWlanGwBdRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdRT.setStatus("current")
_TmnxWlanGwBdRD_Type = TmnxVPNRouteDistinguisher
_TmnxWlanGwBdRD_Object = MibTableColumn
tmnxWlanGwBdRD = _TmnxWlanGwBdRD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 3),
    _TmnxWlanGwBdRD_Type()
)
tmnxWlanGwBdRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdRD.setStatus("current")
_TmnxWlanGwBdWlanGwGrpId_Type = TmnxWlanGwIsaGrpIdOrZero
_TmnxWlanGwBdWlanGwGrpId_Object = MibTableColumn
tmnxWlanGwBdWlanGwGrpId = _TmnxWlanGwBdWlanGwGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 4),
    _TmnxWlanGwBdWlanGwGrpId_Type()
)
tmnxWlanGwBdWlanGwGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdWlanGwGrpId.setStatus("current")
_TmnxWlanGwBdIsaMemberId_Type = Unsigned32
_TmnxWlanGwBdIsaMemberId_Object = MibTableColumn
tmnxWlanGwBdIsaMemberId = _TmnxWlanGwBdIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 5),
    _TmnxWlanGwBdIsaMemberId_Type()
)
tmnxWlanGwBdIsaMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdIsaMemberId.setStatus("current")
_TmnxWlanGwBdVlanTag_Type = QTagFullRangeOrNone
_TmnxWlanGwBdVlanTag_Object = MibTableColumn
tmnxWlanGwBdVlanTag = _TmnxWlanGwBdVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 6),
    _TmnxWlanGwBdVlanTag_Type()
)
tmnxWlanGwBdVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdVlanTag.setStatus("current")
_TmnxWlanGwBdService_Type = TmnxServId
_TmnxWlanGwBdService_Object = MibTableColumn
tmnxWlanGwBdService = _TmnxWlanGwBdService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 7),
    _TmnxWlanGwBdService_Type()
)
tmnxWlanGwBdService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdService.setStatus("current")
_TmnxWlanGwBdInterface_Type = InterfaceIndex
_TmnxWlanGwBdInterface_Object = MibTableColumn
tmnxWlanGwBdInterface = _TmnxWlanGwBdInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 8),
    _TmnxWlanGwBdInterface_Type()
)
tmnxWlanGwBdInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdInterface.setStatus("current")
_TmnxWlanGwBdMacTranslation_Type = TmnxEnabledDisabledOrNA
_TmnxWlanGwBdMacTranslation_Object = MibTableColumn
tmnxWlanGwBdMacTranslation = _TmnxWlanGwBdMacTranslation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 9),
    _TmnxWlanGwBdMacTranslation_Type()
)
tmnxWlanGwBdMacTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdMacTranslation.setStatus("current")
_TmnxWlanGwBdBdMac_Type = MacAddress
_TmnxWlanGwBdBdMac_Object = MibTableColumn
tmnxWlanGwBdBdMac = _TmnxWlanGwBdBdMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 10),
    _TmnxWlanGwBdBdMac_Type()
)
tmnxWlanGwBdBdMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdBdMac.setStatus("current")
_TmnxWlanGwBdAssistAddrRes_Type = TmnxEnabledDisabledOrNA
_TmnxWlanGwBdAssistAddrRes_Object = MibTableColumn
tmnxWlanGwBdAssistAddrRes = _TmnxWlanGwBdAssistAddrRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 11),
    _TmnxWlanGwBdAssistAddrRes_Type()
)
tmnxWlanGwBdAssistAddrRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdAssistAddrRes.setStatus("current")


class _TmnxWlanGwBdNetwMaxMac_Type(Unsigned32):
    """Custom type tmnxWlanGwBdNetwMaxMac based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_TmnxWlanGwBdNetwMaxMac_Type.__name__ = "Unsigned32"
_TmnxWlanGwBdNetwMaxMac_Object = MibTableColumn
tmnxWlanGwBdNetwMaxMac = _TmnxWlanGwBdNetwMaxMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 12),
    _TmnxWlanGwBdNetwMaxMac_Type()
)
tmnxWlanGwBdNetwMaxMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdNetwMaxMac.setStatus("current")
_TmnxWlanGwBdNetwAdminState_Type = TmnxEnabledDisabledOrNA
_TmnxWlanGwBdNetwAdminState_Object = MibTableColumn
tmnxWlanGwBdNetwAdminState = _TmnxWlanGwBdNetwAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 13),
    _TmnxWlanGwBdNetwAdminState_Type()
)
tmnxWlanGwBdNetwAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdNetwAdminState.setStatus("current")


class _TmnxWlanGwBdAccsMaxMac_Type(Unsigned32):
    """Custom type tmnxWlanGwBdAccsMaxMac based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TmnxWlanGwBdAccsMaxMac_Type.__name__ = "Unsigned32"
_TmnxWlanGwBdAccsMaxMac_Object = MibTableColumn
tmnxWlanGwBdAccsMaxMac = _TmnxWlanGwBdAccsMaxMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 14),
    _TmnxWlanGwBdAccsMaxMac_Type()
)
tmnxWlanGwBdAccsMaxMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdAccsMaxMac.setStatus("current")
_TmnxWlanGwBdAccsPolicer_Type = TNamedItemOrEmpty
_TmnxWlanGwBdAccsPolicer_Object = MibTableColumn
tmnxWlanGwBdAccsPolicer = _TmnxWlanGwBdAccsPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 16),
    _TmnxWlanGwBdAccsPolicer_Type()
)
tmnxWlanGwBdAccsPolicer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdAccsPolicer.setStatus("current")
_TmnxWlanGwBdNetwPolicer_Type = TNamedItemOrEmpty
_TmnxWlanGwBdNetwPolicer_Object = MibTableColumn
tmnxWlanGwBdNetwPolicer = _TmnxWlanGwBdNetwPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 18, 1, 18),
    _TmnxWlanGwBdNetwPolicer_Type()
)
tmnxWlanGwBdNetwPolicer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBdNetwPolicer.setStatus("current")
_TmnxWlanGwVlanXcnctTable_Object = MibTable
tmnxWlanGwVlanXcnctTable = _TmnxWlanGwVlanXcnctTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 19)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanXcnctTable.setStatus("current")
_TmnxWlanGwVlanXcnctEntry_Object = MibTableRow
tmnxWlanGwVlanXcnctEntry = _TmnxWlanGwVlanXcnctEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 19, 1)
)
tmnxWlanGwVlanXcnctEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanTagStart"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanTagEnd"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanXcnctEntry.setStatus("current")
_TmnxWlanGwVlanXcnctLastChanged_Type = TimeStamp
_TmnxWlanGwVlanXcnctLastChanged_Object = MibTableColumn
tmnxWlanGwVlanXcnctLastChanged = _TmnxWlanGwVlanXcnctLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 19, 1, 1),
    _TmnxWlanGwVlanXcnctLastChanged_Type()
)
tmnxWlanGwVlanXcnctLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanXcnctLastChanged.setStatus("current")


class _TmnxWlanGwVlanXcnctAccPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanXcnctAccPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxWlanGwVlanXcnctAccPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanXcnctAccPolicy_Object = MibTableColumn
tmnxWlanGwVlanXcnctAccPolicy = _TmnxWlanGwVlanXcnctAccPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 19, 1, 2),
    _TmnxWlanGwVlanXcnctAccPolicy_Type()
)
tmnxWlanGwVlanXcnctAccPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanXcnctAccPolicy.setStatus("current")


class _TmnxWlanGwVlanXcnctAdminState_Type(TmnxAdminState):
    """Custom type tmnxWlanGwVlanXcnctAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxWlanGwVlanXcnctAdminState_Type.__name__ = "TmnxAdminState"
_TmnxWlanGwVlanXcnctAdminState_Object = MibTableColumn
tmnxWlanGwVlanXcnctAdminState = _TmnxWlanGwVlanXcnctAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 19, 1, 3),
    _TmnxWlanGwVlanXcnctAdminState_Type()
)
tmnxWlanGwVlanXcnctAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanXcnctAdminState.setStatus("current")


class _TmnxWlanGwVlanXcnctAcctUpdInterv_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanXcnctAcctUpdInterv based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 259200),
    )


_TmnxWlanGwVlanXcnctAcctUpdInterv_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanXcnctAcctUpdInterv_Object = MibTableColumn
tmnxWlanGwVlanXcnctAcctUpdInterv = _TmnxWlanGwVlanXcnctAcctUpdInterv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 19, 1, 4),
    _TmnxWlanGwVlanXcnctAcctUpdInterv_Type()
)
tmnxWlanGwVlanXcnctAcctUpdInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanXcnctAcctUpdInterv.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanXcnctAcctUpdInterv.setUnits("minutes")


class _TmnxWlanGwVlanXcnctMobAcctUpd_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanXcnctMobAcctUpd based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanXcnctMobAcctUpd_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanXcnctMobAcctUpd_Object = MibTableColumn
tmnxWlanGwVlanXcnctMobAcctUpd = _TmnxWlanGwVlanXcnctMobAcctUpd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 19, 1, 5),
    _TmnxWlanGwVlanXcnctMobAcctUpd_Type()
)
tmnxWlanGwVlanXcnctMobAcctUpd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanXcnctMobAcctUpd.setStatus("current")
_TmnxWlanGwTuBdUeTable_Object = MibTable
tmnxWlanGwTuBdUeTable = _TmnxWlanGwTuBdUeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 20)
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuBdUeTable.setStatus("current")
_TmnxWlanGwTuBdUeEntry_Object = MibTableRow
tmnxWlanGwTuBdUeEntry = _TmnxWlanGwTuBdUeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 20, 1)
)
tmnxWlanGwTuBdUeEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddrTyp"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdBridgeId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeMacAddress"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuBdUeEntry.setStatus("current")
_TmnxWlanGwTuBdUeSsid_Type = TNamedItemOrEmpty
_TmnxWlanGwTuBdUeSsid_Object = MibTableColumn
tmnxWlanGwTuBdUeSsid = _TmnxWlanGwTuBdUeSsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 20, 1, 1),
    _TmnxWlanGwTuBdUeSsid_Type()
)
tmnxWlanGwTuBdUeSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuBdUeSsid.setStatus("current")
_TmnxWlanGwGrpTableLastCh_Type = TimeStamp
_TmnxWlanGwGrpTableLastCh_Object = MibScalar
tmnxWlanGwGrpTableLastCh = _TmnxWlanGwGrpTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 100),
    _TmnxWlanGwGrpTableLastCh_Type()
)
tmnxWlanGwGrpTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpTableLastCh.setStatus("current")
_TmnxWlanGwIomTableLastCh_Type = TimeStamp
_TmnxWlanGwIomTableLastCh_Object = MibScalar
tmnxWlanGwIomTableLastCh = _TmnxWlanGwIomTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 101),
    _TmnxWlanGwIomTableLastCh_Type()
)
tmnxWlanGwIomTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIomTableLastCh.setStatus("current")
_TmnxWlanGwSoftGreIfTableLastCh_Type = TimeStamp
_TmnxWlanGwSoftGreIfTableLastCh_Object = MibScalar
tmnxWlanGwSoftGreIfTableLastCh = _TmnxWlanGwSoftGreIfTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 102),
    _TmnxWlanGwSoftGreIfTableLastCh_Type()
)
tmnxWlanGwSoftGreIfTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfTableLastCh.setStatus("current")
_TmnxWlanGwIfRetailTableLastCh_Type = TimeStamp
_TmnxWlanGwIfRetailTableLastCh_Object = MibScalar
tmnxWlanGwIfRetailTableLastCh = _TmnxWlanGwIfRetailTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 103),
    _TmnxWlanGwIfRetailTableLastCh_Type()
)
tmnxWlanGwIfRetailTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailTableLastCh.setStatus("obsolete")
_TmnxWlanGwMgwProfTableLastCh_Type = TimeStamp
_TmnxWlanGwMgwProfTableLastCh_Object = MibScalar
tmnxWlanGwMgwProfTableLastCh = _TmnxWlanGwMgwProfTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 104),
    _TmnxWlanGwMgwProfTableLastCh_Type()
)
tmnxWlanGwMgwProfTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfTableLastCh.setStatus("current")
_TmnxWlanGwMgwAddrTableLastCh_Type = TimeStamp
_TmnxWlanGwMgwAddrTableLastCh_Object = MibScalar
tmnxWlanGwMgwAddrTableLastCh = _TmnxWlanGwMgwAddrTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 105),
    _TmnxWlanGwMgwAddrTableLastCh_Type()
)
tmnxWlanGwMgwAddrTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrTableLastCh.setStatus("current")
_TmnxWlanGwTableLastCh_Type = TimeStamp
_TmnxWlanGwTableLastCh_Object = MibScalar
tmnxWlanGwTableLastCh = _TmnxWlanGwTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 106),
    _TmnxWlanGwTableLastCh_Type()
)
tmnxWlanGwTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTableLastCh.setStatus("current")
_TmnxWlanGwVlanTableLastCh_Type = TimeStamp
_TmnxWlanGwVlanTableLastCh_Object = MibScalar
tmnxWlanGwVlanTableLastCh = _TmnxWlanGwVlanTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 107),
    _TmnxWlanGwVlanTableLastCh_Type()
)
tmnxWlanGwVlanTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanTableLastCh.setStatus("current")
_TmnxWlanGwPgwTableLastCh_Type = TimeStamp
_TmnxWlanGwPgwTableLastCh_Object = MibScalar
tmnxWlanGwPgwTableLastCh = _TmnxWlanGwPgwTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 108),
    _TmnxWlanGwPgwTableLastCh_Type()
)
tmnxWlanGwPgwTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwTableLastCh.setStatus("current")
_TmnxWlanGwGgsnTableLastCh_Type = TimeStamp
_TmnxWlanGwGgsnTableLastCh_Object = MibScalar
tmnxWlanGwGgsnTableLastCh = _TmnxWlanGwGgsnTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 109),
    _TmnxWlanGwGgsnTableLastCh_Type()
)
tmnxWlanGwGgsnTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnTableLastCh.setStatus("current")
_TmnxWlanGwSubIfTableLastCh_Type = TimeStamp
_TmnxWlanGwSubIfTableLastCh_Object = MibScalar
tmnxWlanGwSubIfTableLastCh = _TmnxWlanGwSubIfTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 110),
    _TmnxWlanGwSubIfTableLastCh_Type()
)
tmnxWlanGwSubIfTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfTableLastCh.setStatus("current")
_TmnxWlanGwVlanDsmTableLastCh_Type = TimeStamp
_TmnxWlanGwVlanDsmTableLastCh_Object = MibScalar
tmnxWlanGwVlanDsmTableLastCh = _TmnxWlanGwVlanDsmTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 111),
    _TmnxWlanGwVlanDsmTableLastCh_Type()
)
tmnxWlanGwVlanDsmTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmTableLastCh.setStatus("current")
_TmnxWlanGwDsmIpFilTableLastCh_Type = TimeStamp
_TmnxWlanGwDsmIpFilTableLastCh_Object = MibScalar
tmnxWlanGwDsmIpFilTableLastCh = _TmnxWlanGwDsmIpFilTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 112),
    _TmnxWlanGwDsmIpFilTableLastCh_Type()
)
tmnxWlanGwDsmIpFilTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilTableLastCh.setStatus("current")
_TmnxWlanGwDsmIpFilN3TableLastCh_Type = TimeStamp
_TmnxWlanGwDsmIpFilN3TableLastCh_Object = MibScalar
tmnxWlanGwDsmIpFilN3TableLastCh = _TmnxWlanGwDsmIpFilN3TableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 113),
    _TmnxWlanGwDsmIpFilN3TableLastCh_Type()
)
tmnxWlanGwDsmIpFilN3TableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3TableLastCh.setStatus("current")
_TmnxWlanGwPolicerTableLastCh_Type = TimeStamp
_TmnxWlanGwPolicerTableLastCh_Object = MibScalar
tmnxWlanGwPolicerTableLastCh = _TmnxWlanGwPolicerTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 114),
    _TmnxWlanGwPolicerTableLastCh_Type()
)
tmnxWlanGwPolicerTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerTableLastCh.setStatus("current")
_TmnxWlanGwL2ApTableLastCh_Type = TimeStamp
_TmnxWlanGwL2ApTableLastCh_Object = MibScalar
tmnxWlanGwL2ApTableLastCh = _TmnxWlanGwL2ApTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 117),
    _TmnxWlanGwL2ApTableLastCh_Type()
)
tmnxWlanGwL2ApTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwL2ApTableLastCh.setStatus("current")
_TmnxWlanGwVplsTableLastCh_Type = TimeStamp
_TmnxWlanGwVplsTableLastCh_Object = MibScalar
tmnxWlanGwVplsTableLastCh = _TmnxWlanGwVplsTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 118),
    _TmnxWlanGwVplsTableLastCh_Type()
)
tmnxWlanGwVplsTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVplsTableLastCh.setStatus("current")
_TmnxWlanGwDsmIpFil6N3TableLastCh_Type = TimeStamp
_TmnxWlanGwDsmIpFil6N3TableLastCh_Object = MibScalar
tmnxWlanGwDsmIpFil6N3TableLastCh = _TmnxWlanGwDsmIpFil6N3TableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 119),
    _TmnxWlanGwDsmIpFil6N3TableLastCh_Type()
)
tmnxWlanGwDsmIpFil6N3TableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFil6N3TableLastCh.setStatus("current")
_TmnxWlanGwVlanBrgTableLastCh_Type = TimeStamp
_TmnxWlanGwVlanBrgTableLastCh_Object = MibScalar
tmnxWlanGwVlanBrgTableLastCh = _TmnxWlanGwVlanBrgTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 121),
    _TmnxWlanGwVlanBrgTableLastCh_Type()
)
tmnxWlanGwVlanBrgTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanBrgTableLastCh.setStatus("current")
_TmnxWlanGwSubIfPmTableLastCh_Type = TimeStamp
_TmnxWlanGwSubIfPmTableLastCh_Object = MibScalar
tmnxWlanGwSubIfPmTableLastCh = _TmnxWlanGwSubIfPmTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 122),
    _TmnxWlanGwSubIfPmTableLastCh_Type()
)
tmnxWlanGwSubIfPmTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmTableLastCh.setStatus("current")
_TmnxWlanGwVlanDhcp6TableLastCh_Type = TimeStamp
_TmnxWlanGwVlanDhcp6TableLastCh_Object = MibScalar
tmnxWlanGwVlanDhcp6TableLastCh = _TmnxWlanGwVlanDhcp6TableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 123),
    _TmnxWlanGwVlanDhcp6TableLastCh_Type()
)
tmnxWlanGwVlanDhcp6TableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp6TableLastCh.setStatus("current")
_TmnxWlanGwVlanSlaacTableLastCh_Type = TimeStamp
_TmnxWlanGwVlanSlaacTableLastCh_Object = MibScalar
tmnxWlanGwVlanSlaacTableLastCh = _TmnxWlanGwVlanSlaacTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 124),
    _TmnxWlanGwVlanSlaacTableLastCh_Type()
)
tmnxWlanGwVlanSlaacTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanSlaacTableLastCh.setStatus("current")
_TmnxWlanGwDsmTableLastCh_Type = TimeStamp
_TmnxWlanGwDsmTableLastCh_Object = MibScalar
tmnxWlanGwDsmTableLastCh = _TmnxWlanGwDsmTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 125),
    _TmnxWlanGwDsmTableLastCh_Type()
)
tmnxWlanGwDsmTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmTableLastCh.setStatus("current")
_TmnxWlanGwMdaTableLastCh_Type = TimeStamp
_TmnxWlanGwMdaTableLastCh_Object = MibScalar
tmnxWlanGwMdaTableLastCh = _TmnxWlanGwMdaTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 127),
    _TmnxWlanGwMdaTableLastCh_Type()
)
tmnxWlanGwMdaTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMdaTableLastCh.setStatus("current")
_TmnxWlanGwXcnctTableLastCh_Type = TimeStamp
_TmnxWlanGwXcnctTableLastCh_Object = MibScalar
tmnxWlanGwXcnctTableLastCh = _TmnxWlanGwXcnctTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 128),
    _TmnxWlanGwXcnctTableLastCh_Type()
)
tmnxWlanGwXcnctTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwXcnctTableLastCh.setStatus("current")
_TmnxWlanGwVlanXcnctTableLastCh_Type = TimeStamp
_TmnxWlanGwVlanXcnctTableLastCh_Object = MibScalar
tmnxWlanGwVlanXcnctTableLastCh = _TmnxWlanGwVlanXcnctTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 129),
    _TmnxWlanGwVlanXcnctTableLastCh_Type()
)
tmnxWlanGwVlanXcnctTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanXcnctTableLastCh.setStatus("current")
_TmnxWlanGwVlanLeTableLastCh_Type = TimeStamp
_TmnxWlanGwVlanLeTableLastCh_Object = MibScalar
tmnxWlanGwVlanLeTableLastCh = _TmnxWlanGwVlanLeTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 130),
    _TmnxWlanGwVlanLeTableLastCh_Type()
)
tmnxWlanGwVlanLeTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeTableLastCh.setStatus("current")
_TmnxWlanGwMmeTableLastChanged_Type = TimeStamp
_TmnxWlanGwMmeTableLastChanged_Object = MibScalar
tmnxWlanGwMmeTableLastChanged = _TmnxWlanGwMmeTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 131),
    _TmnxWlanGwMmeTableLastChanged_Type()
)
tmnxWlanGwMmeTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMmeTableLastChanged.setStatus("current")
_TmnxWlanGwGrpIfGwAddrTableLastCh_Type = TimeStamp
_TmnxWlanGwGrpIfGwAddrTableLastCh_Object = MibScalar
tmnxWlanGwGrpIfGwAddrTableLastCh = _TmnxWlanGwGrpIfGwAddrTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 132),
    _TmnxWlanGwGrpIfGwAddrTableLastCh_Type()
)
tmnxWlanGwGrpIfGwAddrTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpIfGwAddrTableLastCh.setStatus("current")
_TmnxWlanGwResrcProblem_Type = TruthValue
_TmnxWlanGwResrcProblem_Object = MibScalar
tmnxWlanGwResrcProblem = _TmnxWlanGwResrcProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 200),
    _TmnxWlanGwResrcProblem_Type()
)
tmnxWlanGwResrcProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwResrcProblem.setStatus("current")
_TmnxWlanGwNumSoftGreTu_Type = Gauge32
_TmnxWlanGwNumSoftGreTu_Object = MibScalar
tmnxWlanGwNumSoftGreTu = _TmnxWlanGwNumSoftGreTu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 201),
    _TmnxWlanGwNumSoftGreTu_Type()
)
tmnxWlanGwNumSoftGreTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwNumSoftGreTu.setStatus("current")
_TmnxWlanGwPeakNumSoftGreTu_Type = Gauge32
_TmnxWlanGwPeakNumSoftGreTu_Object = MibScalar
tmnxWlanGwPeakNumSoftGreTu = _TmnxWlanGwPeakNumSoftGreTu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 202),
    _TmnxWlanGwPeakNumSoftGreTu_Type()
)
tmnxWlanGwPeakNumSoftGreTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwPeakNumSoftGreTu.setStatus("current")
_TmnxWlanGwNumUe_Type = Gauge32
_TmnxWlanGwNumUe_Object = MibScalar
tmnxWlanGwNumUe = _TmnxWlanGwNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 203),
    _TmnxWlanGwNumUe_Type()
)
tmnxWlanGwNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwNumUe.setStatus("current")
_TmnxWlanGwPeakNumUe_Type = Gauge32
_TmnxWlanGwPeakNumUe_Object = MibScalar
tmnxWlanGwPeakNumUe = _TmnxWlanGwPeakNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 204),
    _TmnxWlanGwPeakNumUe_Type()
)
tmnxWlanGwPeakNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwPeakNumUe.setStatus("current")
_TmnxWlanGwNumMgw_Type = Gauge32
_TmnxWlanGwNumMgw_Object = MibScalar
tmnxWlanGwNumMgw = _TmnxWlanGwNumMgw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 205),
    _TmnxWlanGwNumMgw_Type()
)
tmnxWlanGwNumMgw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwNumMgw.setStatus("current")
_TmnxWlanGwMgwNumHeldSe_Type = Gauge32
_TmnxWlanGwMgwNumHeldSe_Object = MibScalar
tmnxWlanGwMgwNumHeldSe = _TmnxWlanGwMgwNumHeldSe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 210),
    _TmnxWlanGwMgwNumHeldSe_Type()
)
tmnxWlanGwMgwNumHeldSe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwNumHeldSe.setStatus("current")
_TmnxGtpNumMme_Type = Gauge32
_TmnxGtpNumMme_Object = MibScalar
tmnxGtpNumMme = _TmnxGtpNumMme_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 211),
    _TmnxGtpNumMme_Type()
)
tmnxGtpNumMme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpNumMme.setStatus("current")
_TmnxGtpNumEnodeB_Type = Gauge32
_TmnxGtpNumEnodeB_Object = MibScalar
tmnxGtpNumEnodeB = _TmnxGtpNumEnodeB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 212),
    _TmnxGtpNumEnodeB_Type()
)
tmnxGtpNumEnodeB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpNumEnodeB.setStatus("current")
_TmnxGtpNumS11Sessions_Type = Gauge32
_TmnxGtpNumS11Sessions_Object = MibScalar
tmnxGtpNumS11Sessions = _TmnxGtpNumS11Sessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 213),
    _TmnxGtpNumS11Sessions_Type()
)
tmnxGtpNumS11Sessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpNumS11Sessions.setStatus("current")
_TmnxGtpNumUplinks_Type = Gauge32
_TmnxGtpNumUplinks_Object = MibScalar
tmnxGtpNumUplinks = _TmnxGtpNumUplinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 214),
    _TmnxGtpNumUplinks_Type()
)
tmnxGtpNumUplinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpNumUplinks.setStatus("current")
_TmnxGtpNumS11IdleSessions_Type = Gauge32
_TmnxGtpNumS11IdleSessions_Object = MibScalar
tmnxGtpNumS11IdleSessions = _TmnxGtpNumS11IdleSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 215),
    _TmnxGtpNumS11IdleSessions_Type()
)
tmnxGtpNumS11IdleSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpNumS11IdleSessions.setStatus("current")
_TmnxWlanGwVappTableLastCh_Type = TimeStamp
_TmnxWlanGwVappTableLastCh_Object = MibScalar
tmnxWlanGwVappTableLastCh = _TmnxWlanGwVappTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 216),
    _TmnxWlanGwVappTableLastCh_Type()
)
tmnxWlanGwVappTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVappTableLastCh.setStatus("current")
_TmnxWlanGwNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwNotificationObjs = _TmnxWlanGwNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2)
)


class _TmnxWlanGwNotifyDescription_Type(DisplayString):
    """Custom type tmnxWlanGwNotifyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxWlanGwNotifyDescription_Type.__name__ = "DisplayString"
_TmnxWlanGwNotifyDescription_Object = MibScalar
tmnxWlanGwNotifyDescription = _TmnxWlanGwNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 1),
    _TmnxWlanGwNotifyDescription_Type()
)
tmnxWlanGwNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyDescription.setStatus("current")
_TmnxWlanGwNotifyTrue_Type = TruthValue
_TmnxWlanGwNotifyTrue_Object = MibScalar
tmnxWlanGwNotifyTrue = _TmnxWlanGwNotifyTrue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 2),
    _TmnxWlanGwNotifyTrue_Type()
)
tmnxWlanGwNotifyTrue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyTrue.setStatus("current")


class _TmnxWlanGwNotify3gppRelease_Type(DisplayString):
    """Custom type tmnxWlanGwNotify3gppRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_TmnxWlanGwNotify3gppRelease_Type.__name__ = "DisplayString"
_TmnxWlanGwNotify3gppRelease_Object = MibScalar
tmnxWlanGwNotify3gppRelease = _TmnxWlanGwNotify3gppRelease_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 3),
    _TmnxWlanGwNotify3gppRelease_Type()
)
tmnxWlanGwNotify3gppRelease.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotify3gppRelease.setStatus("current")
_TmnxWlanGwNotifyMdaSlotNum_Type = Unsigned32
_TmnxWlanGwNotifyMdaSlotNum_Object = MibScalar
tmnxWlanGwNotifyMdaSlotNum = _TmnxWlanGwNotifyMdaSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 4),
    _TmnxWlanGwNotifyMdaSlotNum_Type()
)
tmnxWlanGwNotifyMdaSlotNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyMdaSlotNum.setStatus("current")
_TmnxWlanGwNotifySubIfIndex_Type = InterfaceIndex
_TmnxWlanGwNotifySubIfIndex_Object = MibScalar
tmnxWlanGwNotifySubIfIndex = _TmnxWlanGwNotifySubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 5),
    _TmnxWlanGwNotifySubIfIndex_Type()
)
tmnxWlanGwNotifySubIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifySubIfIndex.setStatus("current")
_TmnxWlanGwNotifyAddrFamily_Type = TmnxWlanGwSubIfIpsAddrFamily
_TmnxWlanGwNotifyAddrFamily_Object = MibScalar
tmnxWlanGwNotifyAddrFamily = _TmnxWlanGwNotifyAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 6),
    _TmnxWlanGwNotifyAddrFamily_Type()
)
tmnxWlanGwNotifyAddrFamily.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyAddrFamily.setStatus("current")
_TmnxWlanGwNotifyIsaGrpId_Type = TmnxWlanGwIsaGrpIdOrZero
_TmnxWlanGwNotifyIsaGrpId_Object = MibScalar
tmnxWlanGwNotifyIsaGrpId = _TmnxWlanGwNotifyIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 7),
    _TmnxWlanGwNotifyIsaGrpId_Type()
)
tmnxWlanGwNotifyIsaGrpId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyIsaGrpId.setStatus("current")
_TmnxWlanGwNotifyIsaMemberId_Type = Unsigned32
_TmnxWlanGwNotifyIsaMemberId_Object = MibScalar
tmnxWlanGwNotifyIsaMemberId = _TmnxWlanGwNotifyIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 8),
    _TmnxWlanGwNotifyIsaMemberId_Type()
)
tmnxWlanGwNotifyIsaMemberId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyIsaMemberId.setStatus("current")
_TmnxWlanGwNotifyD6cServer1_Type = InetAddressIPv6
_TmnxWlanGwNotifyD6cServer1_Object = MibScalar
tmnxWlanGwNotifyD6cServer1 = _TmnxWlanGwNotifyD6cServer1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 9),
    _TmnxWlanGwNotifyD6cServer1_Type()
)
tmnxWlanGwNotifyD6cServer1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyD6cServer1.setStatus("current")
_TmnxWlanGwNotifyD6cServer2_Type = InetAddressIPv6
_TmnxWlanGwNotifyD6cServer2_Object = MibScalar
tmnxWlanGwNotifyD6cServer2 = _TmnxWlanGwNotifyD6cServer2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 10),
    _TmnxWlanGwNotifyD6cServer2_Type()
)
tmnxWlanGwNotifyD6cServer2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyD6cServer2.setStatus("current")
_TmnxWlanGwNotifyD6cServer3_Type = InetAddressIPv6
_TmnxWlanGwNotifyD6cServer3_Object = MibScalar
tmnxWlanGwNotifyD6cServer3 = _TmnxWlanGwNotifyD6cServer3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 11),
    _TmnxWlanGwNotifyD6cServer3_Type()
)
tmnxWlanGwNotifyD6cServer3.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyD6cServer3.setStatus("current")
_TmnxWlanGwNotifyD6cServer4_Type = InetAddressIPv6
_TmnxWlanGwNotifyD6cServer4_Object = MibScalar
tmnxWlanGwNotifyD6cServer4 = _TmnxWlanGwNotifyD6cServer4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 12),
    _TmnxWlanGwNotifyD6cServer4_Type()
)
tmnxWlanGwNotifyD6cServer4.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyD6cServer4.setStatus("current")
_TmnxWlanGwNotifyD6cServer5_Type = InetAddressIPv6
_TmnxWlanGwNotifyD6cServer5_Object = MibScalar
tmnxWlanGwNotifyD6cServer5 = _TmnxWlanGwNotifyD6cServer5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 13),
    _TmnxWlanGwNotifyD6cServer5_Type()
)
tmnxWlanGwNotifyD6cServer5.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyD6cServer5.setStatus("current")
_TmnxWlanGwNotifyD6cServer6_Type = InetAddressIPv6
_TmnxWlanGwNotifyD6cServer6_Object = MibScalar
tmnxWlanGwNotifyD6cServer6 = _TmnxWlanGwNotifyD6cServer6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 14),
    _TmnxWlanGwNotifyD6cServer6_Type()
)
tmnxWlanGwNotifyD6cServer6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyD6cServer6.setStatus("current")
_TmnxWlanGwNotifyD6cServer7_Type = InetAddressIPv6
_TmnxWlanGwNotifyD6cServer7_Object = MibScalar
tmnxWlanGwNotifyD6cServer7 = _TmnxWlanGwNotifyD6cServer7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 15),
    _TmnxWlanGwNotifyD6cServer7_Type()
)
tmnxWlanGwNotifyD6cServer7.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyD6cServer7.setStatus("current")
_TmnxWlanGwNotifyD6cServer8_Type = InetAddressIPv6
_TmnxWlanGwNotifyD6cServer8_Object = MibScalar
tmnxWlanGwNotifyD6cServer8 = _TmnxWlanGwNotifyD6cServer8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 16),
    _TmnxWlanGwNotifyD6cServer8_Type()
)
tmnxWlanGwNotifyD6cServer8.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyD6cServer8.setStatus("current")
_TmnxWlanGwNotifySubnetAddrType_Type = InetAddressType
_TmnxWlanGwNotifySubnetAddrType_Object = MibScalar
tmnxWlanGwNotifySubnetAddrType = _TmnxWlanGwNotifySubnetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 17),
    _TmnxWlanGwNotifySubnetAddrType_Type()
)
tmnxWlanGwNotifySubnetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifySubnetAddrType.setStatus("current")


class _TmnxWlanGwNotifySubnetAddr_Type(InetAddress):
    """Custom type tmnxWlanGwNotifySubnetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwNotifySubnetAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwNotifySubnetAddr_Object = MibScalar
tmnxWlanGwNotifySubnetAddr = _TmnxWlanGwNotifySubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 18),
    _TmnxWlanGwNotifySubnetAddr_Type()
)
tmnxWlanGwNotifySubnetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifySubnetAddr.setStatus("current")
_TmnxWlanGwNotifySubnetPrefLen_Type = InetAddressPrefixLength
_TmnxWlanGwNotifySubnetPrefLen_Object = MibScalar
tmnxWlanGwNotifySubnetPrefLen = _TmnxWlanGwNotifySubnetPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 19),
    _TmnxWlanGwNotifySubnetPrefLen_Type()
)
tmnxWlanGwNotifySubnetPrefLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifySubnetPrefLen.setStatus("current")


class _TmnxWlanGwNotifyGtpMsgType_Type(Unsigned32):
    """Custom type tmnxWlanGwNotifyGtpMsgType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxWlanGwNotifyGtpMsgType_Type.__name__ = "Unsigned32"
_TmnxWlanGwNotifyGtpMsgType_Object = MibScalar
tmnxWlanGwNotifyGtpMsgType = _TmnxWlanGwNotifyGtpMsgType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 20),
    _TmnxWlanGwNotifyGtpMsgType_Type()
)
tmnxWlanGwNotifyGtpMsgType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyGtpMsgType.setStatus("current")
_TmnxWlanGwNotifyGtpMsgDirection_Type = TDirectionIngEgr
_TmnxWlanGwNotifyGtpMsgDirection_Object = MibScalar
tmnxWlanGwNotifyGtpMsgDirection = _TmnxWlanGwNotifyGtpMsgDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 21),
    _TmnxWlanGwNotifyGtpMsgDirection_Type()
)
tmnxWlanGwNotifyGtpMsgDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyGtpMsgDirection.setStatus("current")
_TmnxWlanGwNotifyImsi_Type = TmnxMobImsiStr
_TmnxWlanGwNotifyImsi_Object = MibScalar
tmnxWlanGwNotifyImsi = _TmnxWlanGwNotifyImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 22),
    _TmnxWlanGwNotifyImsi_Type()
)
tmnxWlanGwNotifyImsi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyImsi.setStatus("current")
_TmnxWlanGwNotifyTeid_Type = Unsigned32
_TmnxWlanGwNotifyTeid_Object = MibScalar
tmnxWlanGwNotifyTeid = _TmnxWlanGwNotifyTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 23),
    _TmnxWlanGwNotifyTeid_Type()
)
tmnxWlanGwNotifyTeid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyTeid.setStatus("current")
_TmnxWlanGwNotifyBdBridgeId_Type = Unsigned32
_TmnxWlanGwNotifyBdBridgeId_Object = MibScalar
tmnxWlanGwNotifyBdBridgeId = _TmnxWlanGwNotifyBdBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 24),
    _TmnxWlanGwNotifyBdBridgeId_Type()
)
tmnxWlanGwNotifyBdBridgeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyBdBridgeId.setStatus("current")
_TmnxWlanGwNotifyUeMacAddress_Type = MacAddress
_TmnxWlanGwNotifyUeMacAddress_Object = MibScalar
tmnxWlanGwNotifyUeMacAddress = _TmnxWlanGwNotifyUeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 25),
    _TmnxWlanGwNotifyUeMacAddress_Type()
)
tmnxWlanGwNotifyUeMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyUeMacAddress.setStatus("current")
_TmnxWlanGwNotifyChassisIndex_Type = TmnxChassisIndex
_TmnxWlanGwNotifyChassisIndex_Object = MibScalar
tmnxWlanGwNotifyChassisIndex = _TmnxWlanGwNotifyChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 26),
    _TmnxWlanGwNotifyChassisIndex_Type()
)
tmnxWlanGwNotifyChassisIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyChassisIndex.setStatus("current")
_TmnxWlanGwNotifyCardSlotNum_Type = TmnxSlotNum
_TmnxWlanGwNotifyCardSlotNum_Object = MibScalar
tmnxWlanGwNotifyCardSlotNum = _TmnxWlanGwNotifyCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 27),
    _TmnxWlanGwNotifyCardSlotNum_Type()
)
tmnxWlanGwNotifyCardSlotNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyCardSlotNum.setStatus("current")
_TmnxWlanGwNotifyEntity_Type = TmnxWlanGwWatermarkEntity
_TmnxWlanGwNotifyEntity_Object = MibScalar
tmnxWlanGwNotifyEntity = _TmnxWlanGwNotifyEntity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 29),
    _TmnxWlanGwNotifyEntity_Type()
)
tmnxWlanGwNotifyEntity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyEntity.setStatus("current")
_TmnxWlanGwNotifyEsaNum_Type = TmnxEsaNum
_TmnxWlanGwNotifyEsaNum_Object = MibScalar
tmnxWlanGwNotifyEsaNum = _TmnxWlanGwNotifyEsaNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 30),
    _TmnxWlanGwNotifyEsaNum_Type()
)
tmnxWlanGwNotifyEsaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyEsaNum.setStatus("current")
_TmnxWlanGwNotifyEsaVappNum_Type = TmnxEsaVappNum
_TmnxWlanGwNotifyEsaVappNum_Object = MibScalar
tmnxWlanGwNotifyEsaVappNum = _TmnxWlanGwNotifyEsaVappNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 31),
    _TmnxWlanGwNotifyEsaVappNum_Type()
)
tmnxWlanGwNotifyEsaVappNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyEsaVappNum.setStatus("current")
_TmnxGtpObjs_ObjectIdentity = ObjectIdentity
tmnxGtpObjs = _TmnxGtpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3)
)
_TmnxGtpS11ItfTableLastChanged_Type = TimeStamp
_TmnxGtpS11ItfTableLastChanged_Object = MibScalar
tmnxGtpS11ItfTableLastChanged = _TmnxGtpS11ItfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 1),
    _TmnxGtpS11ItfTableLastChanged_Type()
)
tmnxGtpS11ItfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11ItfTableLastChanged.setStatus("current")
_TmnxGtpS11ItfTable_Object = MibTable
tmnxGtpS11ItfTable = _TmnxGtpS11ItfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxGtpS11ItfTable.setStatus("current")
_TmnxGtpS11ItfEntry_Object = MibTableRow
tmnxGtpS11ItfEntry = _TmnxGtpS11ItfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 2, 1)
)
tmnxGtpS11ItfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxGtpS11ItfName"),
)
if mibBuilder.loadTexts:
    tmnxGtpS11ItfEntry.setStatus("current")
_TmnxGtpS11ItfName_Type = TNamedItem
_TmnxGtpS11ItfName_Object = MibTableColumn
tmnxGtpS11ItfName = _TmnxGtpS11ItfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 2, 1, 1),
    _TmnxGtpS11ItfName_Type()
)
tmnxGtpS11ItfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGtpS11ItfName.setStatus("current")
_TmnxGtpS11ItfRowStatus_Type = RowStatus
_TmnxGtpS11ItfRowStatus_Object = MibTableColumn
tmnxGtpS11ItfRowStatus = _TmnxGtpS11ItfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 2, 1, 2),
    _TmnxGtpS11ItfRowStatus_Type()
)
tmnxGtpS11ItfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGtpS11ItfRowStatus.setStatus("current")
_TmnxGtpS11ItfLastChanged_Type = TimeStamp
_TmnxGtpS11ItfLastChanged_Object = MibTableColumn
tmnxGtpS11ItfLastChanged = _TmnxGtpS11ItfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 2, 1, 3),
    _TmnxGtpS11ItfLastChanged_Type()
)
tmnxGtpS11ItfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11ItfLastChanged.setStatus("current")


class _TmnxGtpS11ItfApnPolicyName_Type(TNamedItemOrEmpty):
    """Custom type tmnxGtpS11ItfApnPolicyName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxGtpS11ItfApnPolicyName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxGtpS11ItfApnPolicyName_Object = MibTableColumn
tmnxGtpS11ItfApnPolicyName = _TmnxGtpS11ItfApnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 2, 1, 4),
    _TmnxGtpS11ItfApnPolicyName_Type()
)
tmnxGtpS11ItfApnPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGtpS11ItfApnPolicyName.setStatus("current")
_TmnxGtpPpmTableLastChanged_Type = TimeStamp
_TmnxGtpPpmTableLastChanged_Object = MibScalar
tmnxGtpPpmTableLastChanged = _TmnxGtpPpmTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 3),
    _TmnxGtpPpmTableLastChanged_Type()
)
tmnxGtpPpmTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpPpmTableLastChanged.setStatus("current")
_TmnxGtpPpmTable_Object = MibTable
tmnxGtpPpmTable = _TmnxGtpPpmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxGtpPpmTable.setStatus("current")
_TmnxGtpPpmEntry_Object = MibTableRow
tmnxGtpPpmEntry = _TmnxGtpPpmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 4, 1)
)
tmnxGtpPpmEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxGtpPpmGtpItfType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxGtpPpmAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxGtpPpmAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxGtpPpmAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxGtpPpmEntry.setStatus("current")
_TmnxGtpPpmGtpItfType_Type = TmnxGtpInterfaceType
_TmnxGtpPpmGtpItfType_Object = MibTableColumn
tmnxGtpPpmGtpItfType = _TmnxGtpPpmGtpItfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 4, 1, 1),
    _TmnxGtpPpmGtpItfType_Type()
)
tmnxGtpPpmGtpItfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGtpPpmGtpItfType.setStatus("current")
_TmnxGtpPpmAddrType_Type = InetAddressType
_TmnxGtpPpmAddrType_Object = MibTableColumn
tmnxGtpPpmAddrType = _TmnxGtpPpmAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 4, 1, 2),
    _TmnxGtpPpmAddrType_Type()
)
tmnxGtpPpmAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGtpPpmAddrType.setStatus("current")


class _TmnxGtpPpmAddr_Type(InetAddress):
    """Custom type tmnxGtpPpmAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxGtpPpmAddr_Type.__name__ = "InetAddress"
_TmnxGtpPpmAddr_Object = MibTableColumn
tmnxGtpPpmAddr = _TmnxGtpPpmAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 4, 1, 3),
    _TmnxGtpPpmAddr_Type()
)
tmnxGtpPpmAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGtpPpmAddr.setStatus("current")


class _TmnxGtpPpmAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxGtpPpmAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxGtpPpmAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxGtpPpmAddrPrefixLen_Object = MibTableColumn
tmnxGtpPpmAddrPrefixLen = _TmnxGtpPpmAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 4, 1, 4),
    _TmnxGtpPpmAddrPrefixLen_Type()
)
tmnxGtpPpmAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGtpPpmAddrPrefixLen.setStatus("current")
_TmnxGtpPpmRowStatus_Type = RowStatus
_TmnxGtpPpmRowStatus_Object = MibTableColumn
tmnxGtpPpmRowStatus = _TmnxGtpPpmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 4, 1, 5),
    _TmnxGtpPpmRowStatus_Type()
)
tmnxGtpPpmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGtpPpmRowStatus.setStatus("current")
_TmnxGtpPpmLastChanged_Type = TimeStamp
_TmnxGtpPpmLastChanged_Object = MibTableColumn
tmnxGtpPpmLastChanged = _TmnxGtpPpmLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 4, 1, 6),
    _TmnxGtpPpmLastChanged_Type()
)
tmnxGtpPpmLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpPpmLastChanged.setStatus("current")


class _TmnxGtpPpmProfileName_Type(TNamedItemOrEmpty):
    """Custom type tmnxGtpPpmProfileName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxGtpPpmProfileName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxGtpPpmProfileName_Object = MibTableColumn
tmnxGtpPpmProfileName = _TmnxGtpPpmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 4, 1, 7),
    _TmnxGtpPpmProfileName_Type()
)
tmnxGtpPpmProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGtpPpmProfileName.setStatus("current")
_TmnxGtpS11SeTableLastChanged_Type = TimeStamp
_TmnxGtpS11SeTableLastChanged_Object = MibScalar
tmnxGtpS11SeTableLastChanged = _TmnxGtpS11SeTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 5),
    _TmnxGtpS11SeTableLastChanged_Type()
)
tmnxGtpS11SeTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SeTableLastChanged.setStatus("current")
_TmnxGtpS11SeTable_Object = MibTable
tmnxGtpS11SeTable = _TmnxGtpS11SeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxGtpS11SeTable.setStatus("current")
_TmnxGtpS11SeEntry_Object = MibTableRow
tmnxGtpS11SeEntry = _TmnxGtpS11SeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1)
)
tmnxGtpS11SeEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeImsi"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeApn"),
)
if mibBuilder.loadTexts:
    tmnxGtpS11SeEntry.setStatus("current")


class _TmnxGtpS11SeImsi_Type(TmnxMobImsiStr):
    """Custom type tmnxGtpS11SeImsi based on TmnxMobImsiStr"""
    subtypeSpec = TmnxMobImsiStr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 15),
    )


_TmnxGtpS11SeImsi_Type.__name__ = "TmnxMobImsiStr"
_TmnxGtpS11SeImsi_Object = MibTableColumn
tmnxGtpS11SeImsi = _TmnxGtpS11SeImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 1),
    _TmnxGtpS11SeImsi_Type()
)
tmnxGtpS11SeImsi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGtpS11SeImsi.setStatus("current")
_TmnxGtpS11SeApn_Type = TmnxMobApn
_TmnxGtpS11SeApn_Object = MibTableColumn
tmnxGtpS11SeApn = _TmnxGtpS11SeApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 2),
    _TmnxGtpS11SeApn_Type()
)
tmnxGtpS11SeApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGtpS11SeApn.setStatus("current")
_TmnxGtpS11SePeerRouter_Type = TmnxVRtrIDOrZero
_TmnxGtpS11SePeerRouter_Object = MibTableColumn
tmnxGtpS11SePeerRouter = _TmnxGtpS11SePeerRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 3),
    _TmnxGtpS11SePeerRouter_Type()
)
tmnxGtpS11SePeerRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SePeerRouter.setStatus("current")
_TmnxGtpS11SePeerAddrType_Type = InetAddressType
_TmnxGtpS11SePeerAddrType_Object = MibTableColumn
tmnxGtpS11SePeerAddrType = _TmnxGtpS11SePeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 4),
    _TmnxGtpS11SePeerAddrType_Type()
)
tmnxGtpS11SePeerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SePeerAddrType.setStatus("current")


class _TmnxGtpS11SePeerAddr_Type(InetAddress):
    """Custom type tmnxGtpS11SePeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxGtpS11SePeerAddr_Type.__name__ = "InetAddress"
_TmnxGtpS11SePeerAddr_Object = MibTableColumn
tmnxGtpS11SePeerAddr = _TmnxGtpS11SePeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 5),
    _TmnxGtpS11SePeerAddr_Type()
)
tmnxGtpS11SePeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SePeerAddr.setStatus("current")
_TmnxGtpS11SeRemoteCtrlTeid_Type = Unsigned32
_TmnxGtpS11SeRemoteCtrlTeid_Object = MibTableColumn
tmnxGtpS11SeRemoteCtrlTeid = _TmnxGtpS11SeRemoteCtrlTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 6),
    _TmnxGtpS11SeRemoteCtrlTeid_Type()
)
tmnxGtpS11SeRemoteCtrlTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SeRemoteCtrlTeid.setStatus("current")
_TmnxGtpS11SeLocalCtrlTeid_Type = Unsigned32
_TmnxGtpS11SeLocalCtrlTeid_Object = MibTableColumn
tmnxGtpS11SeLocalCtrlTeid = _TmnxGtpS11SeLocalCtrlTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 7),
    _TmnxGtpS11SeLocalCtrlTeid_Type()
)
tmnxGtpS11SeLocalCtrlTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SeLocalCtrlTeid.setStatus("current")
_TmnxGtpS11SeChrgChar_Type = TmnxWlanGwChargingCharBits
_TmnxGtpS11SeChrgChar_Object = MibTableColumn
tmnxGtpS11SeChrgChar = _TmnxGtpS11SeChrgChar_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 10),
    _TmnxGtpS11SeChrgChar_Type()
)
tmnxGtpS11SeChrgChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SeChrgChar.setStatus("current")
_TmnxGtpS11SeQosUplinkAmbr_Type = TmnxWlanGwAmbr
_TmnxGtpS11SeQosUplinkAmbr_Object = MibTableColumn
tmnxGtpS11SeQosUplinkAmbr = _TmnxGtpS11SeQosUplinkAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 11),
    _TmnxGtpS11SeQosUplinkAmbr_Type()
)
tmnxGtpS11SeQosUplinkAmbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SeQosUplinkAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxGtpS11SeQosUplinkAmbr.setUnits("kilobps")
_TmnxGtpS11SeQosDwnlinkAmbr_Type = TmnxWlanGwAmbr
_TmnxGtpS11SeQosDwnlinkAmbr_Object = MibTableColumn
tmnxGtpS11SeQosDwnlinkAmbr = _TmnxGtpS11SeQosDwnlinkAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 12),
    _TmnxGtpS11SeQosDwnlinkAmbr_Type()
)
tmnxGtpS11SeQosDwnlinkAmbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SeQosDwnlinkAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxGtpS11SeQosDwnlinkAmbr.setUnits("kilobps")
_TmnxGtpS11SePdnTeid_Type = Unsigned32
_TmnxGtpS11SePdnTeid_Object = MibTableColumn
tmnxGtpS11SePdnTeid = _TmnxGtpS11SePdnTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 13),
    _TmnxGtpS11SePdnTeid_Type()
)
tmnxGtpS11SePdnTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SePdnTeid.setStatus("current")


class _TmnxGtpS11SeUliCgi_Type(OctetString):
    """Custom type tmnxGtpS11SeUliCgi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 7),
    )


_TmnxGtpS11SeUliCgi_Type.__name__ = "OctetString"
_TmnxGtpS11SeUliCgi_Object = MibTableColumn
tmnxGtpS11SeUliCgi = _TmnxGtpS11SeUliCgi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 14),
    _TmnxGtpS11SeUliCgi_Type()
)
tmnxGtpS11SeUliCgi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SeUliCgi.setStatus("current")


class _TmnxGtpS11SeUliSai_Type(OctetString):
    """Custom type tmnxGtpS11SeUliSai based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 7),
    )


_TmnxGtpS11SeUliSai_Type.__name__ = "OctetString"
_TmnxGtpS11SeUliSai_Object = MibTableColumn
tmnxGtpS11SeUliSai = _TmnxGtpS11SeUliSai_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 15),
    _TmnxGtpS11SeUliSai_Type()
)
tmnxGtpS11SeUliSai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SeUliSai.setStatus("current")


class _TmnxGtpS11SeUliRai_Type(OctetString):
    """Custom type tmnxGtpS11SeUliRai based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 7),
    )


_TmnxGtpS11SeUliRai_Type.__name__ = "OctetString"
_TmnxGtpS11SeUliRai_Object = MibTableColumn
tmnxGtpS11SeUliRai = _TmnxGtpS11SeUliRai_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 16),
    _TmnxGtpS11SeUliRai_Type()
)
tmnxGtpS11SeUliRai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SeUliRai.setStatus("current")


class _TmnxGtpS11SeUliTai_Type(OctetString):
    """Custom type tmnxGtpS11SeUliTai based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
    )


_TmnxGtpS11SeUliTai_Type.__name__ = "OctetString"
_TmnxGtpS11SeUliTai_Object = MibTableColumn
tmnxGtpS11SeUliTai = _TmnxGtpS11SeUliTai_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 17),
    _TmnxGtpS11SeUliTai_Type()
)
tmnxGtpS11SeUliTai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SeUliTai.setStatus("current")


class _TmnxGtpS11SeUliEcgi_Type(OctetString):
    """Custom type tmnxGtpS11SeUliEcgi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 7),
    )


_TmnxGtpS11SeUliEcgi_Type.__name__ = "OctetString"
_TmnxGtpS11SeUliEcgi_Object = MibTableColumn
tmnxGtpS11SeUliEcgi = _TmnxGtpS11SeUliEcgi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 6, 1, 18),
    _TmnxGtpS11SeUliEcgi_Type()
)
tmnxGtpS11SeUliEcgi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11SeUliEcgi.setStatus("current")
_TmnxGtpS11BcTableLastChanged_Type = TimeStamp
_TmnxGtpS11BcTableLastChanged_Object = MibScalar
tmnxGtpS11BcTableLastChanged = _TmnxGtpS11BcTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 7),
    _TmnxGtpS11BcTableLastChanged_Type()
)
tmnxGtpS11BcTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11BcTableLastChanged.setStatus("current")
_TmnxGtpS11BcTable_Object = MibTable
tmnxGtpS11BcTable = _TmnxGtpS11BcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8)
)
if mibBuilder.loadTexts:
    tmnxGtpS11BcTable.setStatus("current")
_TmnxGtpS11BcEntry_Object = MibTableRow
tmnxGtpS11BcEntry = _TmnxGtpS11BcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8, 1)
)
tmnxGtpS11BcEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeImsi"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeApn"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxGtpS11BcId"),
)
if mibBuilder.loadTexts:
    tmnxGtpS11BcEntry.setStatus("current")
_TmnxGtpS11BcId_Type = TmnxMobBearerId
_TmnxGtpS11BcId_Object = MibTableColumn
tmnxGtpS11BcId = _TmnxGtpS11BcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8, 1, 1),
    _TmnxGtpS11BcId_Type()
)
tmnxGtpS11BcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGtpS11BcId.setStatus("current")
_TmnxGtpS11BcRemoteTeid_Type = Unsigned32
_TmnxGtpS11BcRemoteTeid_Object = MibTableColumn
tmnxGtpS11BcRemoteTeid = _TmnxGtpS11BcRemoteTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8, 1, 2),
    _TmnxGtpS11BcRemoteTeid_Type()
)
tmnxGtpS11BcRemoteTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11BcRemoteTeid.setStatus("current")
_TmnxGtpS11BcLocalTeid_Type = Unsigned32
_TmnxGtpS11BcLocalTeid_Object = MibTableColumn
tmnxGtpS11BcLocalTeid = _TmnxGtpS11BcLocalTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8, 1, 3),
    _TmnxGtpS11BcLocalTeid_Type()
)
tmnxGtpS11BcLocalTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11BcLocalTeid.setStatus("current")
_TmnxGtpS11BcQosUlGbr_Type = Unsigned32
_TmnxGtpS11BcQosUlGbr_Object = MibTableColumn
tmnxGtpS11BcQosUlGbr = _TmnxGtpS11BcQosUlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8, 1, 10),
    _TmnxGtpS11BcQosUlGbr_Type()
)
tmnxGtpS11BcQosUlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11BcQosUlGbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxGtpS11BcQosUlGbr.setUnits("kilobps")
_TmnxGtpS11BcQosUlMbr_Type = Unsigned32
_TmnxGtpS11BcQosUlMbr_Object = MibTableColumn
tmnxGtpS11BcQosUlMbr = _TmnxGtpS11BcQosUlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8, 1, 11),
    _TmnxGtpS11BcQosUlMbr_Type()
)
tmnxGtpS11BcQosUlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11BcQosUlMbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxGtpS11BcQosUlMbr.setUnits("kilobps")
_TmnxGtpS11BcQosDlGbr_Type = Unsigned32
_TmnxGtpS11BcQosDlGbr_Object = MibTableColumn
tmnxGtpS11BcQosDlGbr = _TmnxGtpS11BcQosDlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8, 1, 12),
    _TmnxGtpS11BcQosDlGbr_Type()
)
tmnxGtpS11BcQosDlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11BcQosDlGbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxGtpS11BcQosDlGbr.setUnits("kilobps")
_TmnxGtpS11BcQosDlMbr_Type = Unsigned32
_TmnxGtpS11BcQosDlMbr_Object = MibTableColumn
tmnxGtpS11BcQosDlMbr = _TmnxGtpS11BcQosDlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8, 1, 13),
    _TmnxGtpS11BcQosDlMbr_Type()
)
tmnxGtpS11BcQosDlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11BcQosDlMbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxGtpS11BcQosDlMbr.setUnits("kilobps")
_TmnxGtpS11BcQosQci_Type = TmnxMobExtQci
_TmnxGtpS11BcQosQci_Object = MibTableColumn
tmnxGtpS11BcQosQci = _TmnxGtpS11BcQosQci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8, 1, 14),
    _TmnxGtpS11BcQosQci_Type()
)
tmnxGtpS11BcQosQci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11BcQosQci.setStatus("current")
_TmnxGtpS11BcQosArp_Type = TmnxMobArp
_TmnxGtpS11BcQosArp_Object = MibTableColumn
tmnxGtpS11BcQosArp = _TmnxGtpS11BcQosArp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8, 1, 15),
    _TmnxGtpS11BcQosArp_Type()
)
tmnxGtpS11BcQosArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11BcQosArp.setStatus("current")
_TmnxGtpS11BcRemoteAddrType_Type = InetAddressType
_TmnxGtpS11BcRemoteAddrType_Object = MibTableColumn
tmnxGtpS11BcRemoteAddrType = _TmnxGtpS11BcRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8, 1, 16),
    _TmnxGtpS11BcRemoteAddrType_Type()
)
tmnxGtpS11BcRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11BcRemoteAddrType.setStatus("current")


class _TmnxGtpS11BcRemoteAddr_Type(InetAddress):
    """Custom type tmnxGtpS11BcRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxGtpS11BcRemoteAddr_Type.__name__ = "InetAddress"
_TmnxGtpS11BcRemoteAddr_Object = MibTableColumn
tmnxGtpS11BcRemoteAddr = _TmnxGtpS11BcRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 8, 1, 17),
    _TmnxGtpS11BcRemoteAddr_Type()
)
tmnxGtpS11BcRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpS11BcRemoteAddr.setStatus("current")
_TmnxGtpUplinkTableLastChanged_Type = TimeStamp
_TmnxGtpUplinkTableLastChanged_Object = MibScalar
tmnxGtpUplinkTableLastChanged = _TmnxGtpUplinkTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 9),
    _TmnxGtpUplinkTableLastChanged_Type()
)
tmnxGtpUplinkTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpUplinkTableLastChanged.setStatus("current")
_TmnxGtpUplinkTable_Object = MibTable
tmnxGtpUplinkTable = _TmnxGtpUplinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 10)
)
if mibBuilder.loadTexts:
    tmnxGtpUplinkTable.setStatus("current")
_TmnxGtpUplinkEntry_Object = MibTableRow
tmnxGtpUplinkEntry = _TmnxGtpUplinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 10, 1)
)
tmnxGtpUplinkEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxGtpUplinkEntry.setStatus("current")
_TmnxGtpUplinkRowStatus_Type = RowStatus
_TmnxGtpUplinkRowStatus_Object = MibTableColumn
tmnxGtpUplinkRowStatus = _TmnxGtpUplinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 10, 1, 1),
    _TmnxGtpUplinkRowStatus_Type()
)
tmnxGtpUplinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGtpUplinkRowStatus.setStatus("current")
_TmnxGtpUplinkLastChanged_Type = TimeStamp
_TmnxGtpUplinkLastChanged_Object = MibTableColumn
tmnxGtpUplinkLastChanged = _TmnxGtpUplinkLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 10, 1, 2),
    _TmnxGtpUplinkLastChanged_Type()
)
tmnxGtpUplinkLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGtpUplinkLastChanged.setStatus("current")


class _TmnxGtpUplinkApn_Type(TmnxMobApnOrZero):
    """Custom type tmnxGtpUplinkApn based on TmnxMobApnOrZero"""
    defaultValue = OctetString("")

    subtypeSpec = TmnxMobApnOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxGtpUplinkApn_Type.__name__ = "TmnxMobApnOrZero"
_TmnxGtpUplinkApn_Object = MibTableColumn
tmnxGtpUplinkApn = _TmnxGtpUplinkApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 10, 1, 3),
    _TmnxGtpUplinkApn_Type()
)
tmnxGtpUplinkApn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGtpUplinkApn.setStatus("current")


class _TmnxGtpUplinkPdnType_Type(Integer32):
    """Custom type tmnxGtpUplinkPdnType based on Integer32"""
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
        *(("ipv4", 0),
          ("ipv6", 1),
          ("ipv4v6", 2))
    )


_TmnxGtpUplinkPdnType_Type.__name__ = "Integer32"
_TmnxGtpUplinkPdnType_Object = MibTableColumn
tmnxGtpUplinkPdnType = _TmnxGtpUplinkPdnType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 3, 10, 1, 4),
    _TmnxGtpUplinkPdnType_Type()
)
tmnxGtpUplinkPdnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGtpUplinkPdnType.setStatus("current")
_TmnxWlanGwNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxWlanGwNotifyPrefix = _TmnxWlanGwNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81)
)
_TmnxWlanGwNotifications_ObjectIdentity = ObjectIdentity
tmnxWlanGwNotifications = _TmnxWlanGwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0)
)
tmnxWlanGwSoftGreIfEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwSoftGreXtEntry")
)
tmnxWlanGwSoftGreXtEntry.setIndexNames(*tmnxWlanGwSoftGreIfEntry.getIndexNames())
tmnxWlanGwSubIfEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwSubIfPmEntry")
)
tmnxWlanGwSubIfPmEntry.setIndexNames(*tmnxWlanGwSubIfEntry.getIndexNames())
tmnxWlanGwMgwProfEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwPgwEntry")
)
tmnxWlanGwPgwEntry.setIndexNames(*tmnxWlanGwMgwProfEntry.getIndexNames())
tmnxWlanGwMgwProfEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwGgsnEntry")
)
tmnxWlanGwGgsnEntry.setIndexNames(*tmnxWlanGwMgwProfEntry.getIndexNames())
tmnxWlanGwMgwProfEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwMmeEntry")
)
tmnxWlanGwMmeEntry.setIndexNames(*tmnxWlanGwMgwProfEntry.getIndexNames())
tmnxWlanGwVlanEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwVlanDsmEntry")
)
tmnxWlanGwVlanDsmEntry.setIndexNames(*tmnxWlanGwVlanEntry.getIndexNames())
tmnxWlanGwEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwDsmEntry")
)
tmnxWlanGwDsmEntry.setIndexNames(*tmnxWlanGwEntry.getIndexNames())
svcTlsInfoEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwVplsEntry")
)
tmnxWlanGwVplsEntry.setIndexNames(*svcTlsInfoEntry.getIndexNames())
tmnxWlanGwVlanEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwVlanDhcp6Entry")
)
tmnxWlanGwVlanDhcp6Entry.setIndexNames(*tmnxWlanGwVlanEntry.getIndexNames())
tmnxWlanGwVlanEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwVlanSlaacEntry")
)
tmnxWlanGwVlanSlaacEntry.setIndexNames(*tmnxWlanGwVlanEntry.getIndexNames())
tmnxWlanGwVlanEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwVlanBrgEntry")
)
tmnxWlanGwVlanBrgEntry.setIndexNames(*tmnxWlanGwVlanEntry.getIndexNames())
tmnxWlanGwVlanEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwVlanLeEntry")
)
tmnxWlanGwVlanLeEntry.setIndexNames(*tmnxWlanGwVlanEntry.getIndexNames())
tmnxWlanGwEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwXcnctEntry")
)
tmnxWlanGwXcnctEntry.setIndexNames(*tmnxWlanGwEntry.getIndexNames())

# Managed Objects groups

tmnxWlanGwIsaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 1)
)
tmnxWlanGwIsaGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpActiveIomLimit"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpPortPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpTunnelPortPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpOperState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomOperState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberChassisIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberCardSlotNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberSlotNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberEegMemberAct"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberEegMemberPend"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberTuQosProblem"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsVal"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsValHw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwResrcProblem"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaGroup.setStatus("obsolete")

tmnxWlanGwSoftGreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 2)
)
tmnxWlanGwSoftGreGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfShapingType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfShapeMultiUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfEQosPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfESchedPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfEAggRateLimit"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMobTrigger"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMobHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfDefRetailSvc"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfTcpMssAdjust"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfEHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuEstabTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuIsaMember"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegSvcId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegPortId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegEncapValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegMember"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosRemainingHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuUeSsid"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreGroup.setStatus("obsolete")

tmnxWlanGwObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 3)
)
tmnxWlanGwObjGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQTag"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeMplsLabel"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuRemoteAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuLocalAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuQosRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeSsid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUePrevApAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUePrevApAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeLastMoveTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSsidNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPeakNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPeakNumUe"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwObjGroup.setStatus("obsolete")

tmnxWlanGwMgwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 4)
)
tmnxWlanGwMgwGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeImsi"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfKeepAlvRetryCnt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfMsgReTxTimeout"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfMsgReTxRetryCnt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfKeepAlvTimeout"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfKeepAlvResp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfTtl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfInterfaceType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddrTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddrRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddrLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddrProfile"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwLocalAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwLocalAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfile"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwControl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRestartCnt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwInterfaceType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanMgwStatsName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanMgwStatsVal"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanMgwStatsValLw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanMgwStatsValHw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeMgwRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeMgwAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeMgwAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeRemoteCtrlTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeLocalCtrlTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcRemoteTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcLocalTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSysCfgServingNwMcc"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSysCfgServingNwMnc"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwApn"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumMgw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpStatsName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpStatsVal"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpStatsValLw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpStatsValHw"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwGroup.setStatus("current")

tmnxWlanGwSoftGreV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 5)
)
tmnxWlanGwSoftGreV11v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfSsidType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfDataTrigg"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfAuthPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfAuthHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRadProxVrtr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRadProxSrv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRadProxMacFmt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwV6AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwV6Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDhcp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtActLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtHttpRdrPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNatPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDhcp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanActLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanHttpRdrPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNatPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanSsidType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDataTrigg"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAuthPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAuthHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRadProxVrtr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRadProxSrv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRadProxMacFmt"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreV11v0Group.setStatus("obsolete")

tmnxWlanGwMgwV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 6)
)
tmnxWlanGwMgwV11v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwArecCacheAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwArecCacheAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwArecCacheTtl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCachePref"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheNext"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheRepl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheTtl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCacheWeight"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCachePort"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCacheTarget"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCacheTtl"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwV11v0Group.setStatus("current")

tmnxWlanGwMgwQosIeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 10)
)
tmnxWlanGwMgwQosIeGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosUplinkGbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosUplinkMbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosDwnlinkGbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosDwnlinkMbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosArpValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosQciValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnQosUplinkGbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnQosUplinkMbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnQosDwnlinkGbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnQosDwnlinkMbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnQosArpValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcQosUlGbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcQosUlMbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcQosDlGbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcQosDlMbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcQosArp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcQosQci"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwQosIeGroup.setStatus("current")

tmnxWlanGwMgwChargingCharGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 11)
)
tmnxWlanGwMgwChargingCharGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfChrgCharHome"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfChrgCharRoam"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeChrgChar"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwChargingCharGroup.setStatus("current")

tmnxWlanGwMobilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 15)
)
tmnxWlanGwMobilityGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobAcctInterimUpdate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMobArpAp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuApMacAddress"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuApLearnFailed"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMobilityGroup.setStatus("current")

tmnxWlanGwMgwSeHoldTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 16)
)
tmnxWlanGwMgwSeHoldTimeGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfSeHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSysCfgMgwMaxHeldSe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwNumHeldSe"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSeHoldTimeGroup.setStatus("current")

tmnxWlanGwV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 17)
)
tmnxWlanGwV12v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpDegraded"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQTag"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeMplsLabel"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuRemoteAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuLocalAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuQosRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeSsid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUePrevApAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUePrevApAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeLastMoveTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSsidNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPeakNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPeakNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfReportWlanLoc"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfProtocolCfgOpt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeSapPortId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeSapPortEncapValue"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV12v0Group.setStatus("current")

tmnxWlanGwSoftGreV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 18)
)
tmnxWlanGwSoftGreV12v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfShapingType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfShapeMultiUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfEQosPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfESchedPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfEAggRateLimit"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMobTrigger"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMobHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfDefRetailSvc"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfTcpMssAdjust"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfEHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuEstabTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuIsaMember"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegSvcId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegPortId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegEncapValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegMember"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosRemainingHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuUeSsid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfSsidType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwV6AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwV6Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDhcp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanActLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanHttpRdrPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNatPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanSsidType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDataTrigg"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAuthPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAuthHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRadProxVrtr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRadProxSrv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRadProxMacFmt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfDownIfGrpDeg"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreV12v0Group.setStatus("current")

tmnxWlanGwRedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 19)
)
tmnxWlanGwRedGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedExpPrefixType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedExpPrefix"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedExpPrefixLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedMonPrefixType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedMonPrefix"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedMonPrefixLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedActive"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedSwitch"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwRedGroup.setStatus("current")

tmnxWlanGwDsmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 20)
)
tmnxWlanGwDsmGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpIsaAaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAuthOnDhcp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmAcctPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmEgressPolicer"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmIngressPolicer"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmIpFilter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmOneTimeRdrUrl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmOneTimeRdrPort"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmAcctUpdInterv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmDefAppProfile"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilDefaultAction"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilDefaultAction6"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3TableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3RowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3LastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3Description"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3Action"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3Protocol"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3DestAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3DestAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3DestPrefLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3DestPortOp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3DestPort1"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3TableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3RowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3LastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3Description"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3Action"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3Protocol"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3DestAddrTyp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3DestAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3DestPrefLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3DestPortOp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3DestPort1"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpv6TcpMssAdjust"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerRowLastChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerAction"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerAdminPIR"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerAdminCIR"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerMBS"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerCBS"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerPIRAdaptation"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerCIRAdaptation"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerTableLastCh"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmGroup.setStatus("current")

tmnxWlanGwUeQryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 23)
)
tmnxWlanGwUeQryGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeNextQryId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeMaxQryId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereMacAddress"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereIsaGrp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereQTag"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereTuRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereTuRemAddrTyp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereTuRemAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereTuLocAddrTyp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereTuLocAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereEncap"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereSlaacPrefTyp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereSlaacPref"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereDhcp6AddrTyp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereDhcp6Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryNumResults"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResMacAddress"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResIsaGrp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResIsaMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResQTag"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResTuRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResTuAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResTuLocalAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResEncapsulation"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResTuRemoteAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResSsid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResApMacAddress"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResMplsLabel"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResLastMoveTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResExpirationTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResIdleTimeout"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResSessionTimeout"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResNatPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResHttpRdrPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDsmIpFilter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDsmAcctPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDsmAcctUpdInterv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResAcctUpdate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResIngOperPir"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResIngOperCir"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResEgrOperPir"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResEgrOperCir"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDsmAppProfile"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResRxPkts"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResRxOctets"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResTxPkts"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResTxOctets"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResSlaacAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResSlaacPref"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResSlaacAddr1"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResSlaacAddr2"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResSlaacAddr3"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDhcp6AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDhcp6Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDhcp6AddrDepr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDhcp6IAID"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDhcp6IAIDValid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResSlaacLeaseExpire"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDhcp6LeaseExpire"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDhcpAddrDepr"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryGroup.setStatus("current")

tmnxWlanGwDsmV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 25)
)
tmnxWlanGwDsmV13v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanL2Service"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanL2AdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanL2Description"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVplsAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVplsDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVplsSapTemplate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVplsTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVplsLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPdnType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmWatermarkHigh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmWatermarkLow"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmWlanGwGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cServer1"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cServer2"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cServer3"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cServer4"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cServer5"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cServer6"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cServer7"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cServer8"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cLeaseQuery"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cLeaseQueryMR"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cSourceIp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cSlaacPoolNm"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cSlaacLinkAdd"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cSlaacAdminSt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cIaNaPoolNm"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cIaNaLinkAdd"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cIaNaAdminSt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsSubIfIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsSubnetAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsSubnetAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsSubnetPrefLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsAddrFamily"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsPoolIsOld"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsUsageLevelPct"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsDHCPv6Options"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsRemLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsIsaGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsIsaMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsServiceId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDhcp6TableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDhcp6LastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDhcp6InitPrefLt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDhcp6ActPrefLt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDhcp6InitValidLt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDhcp6ActValidLt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDhcp6AdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanSlaacTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanSlaacLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanSlaacInitPrefLt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanSlaacActPrefLt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanSlaacInitValidLt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanSlaacActValidLt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanSlaacAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSysCfgVirtChassisId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanIdleTimeoutAction"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmV13v0Group.setStatus("current")

tmnxWlanGwL2ApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 26)
)
tmnxWlanGwL2ApGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfL2ApEncapType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfL2ApAutoSubId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuEncap"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuEncapTag1"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuEncapTag2"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuInterface"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuApSapEncapVal"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuApSapPortId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeEncapsulation"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2ApRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2ApLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2ApAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2ApEncapType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2ApEpipeSapTemplate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2ApId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2ApTableLastCh"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwL2ApGroup.setStatus("current")

tmnxWlanGwL2tpv3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 27)
)
tmnxWlanGwL2tpv3Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMultiTuType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfL2tpLrnCookie"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfL2tpCookie"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwL2tpv3Group.setStatus("current")

tmnxWlanGwV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 28)
)
tmnxWlanGwV14v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfPythonPolicy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfRatType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanBrgLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanBrgAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanBrgDefBrgProfile"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanBrgAuthedBrgOnly"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanBrgTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmAaAcctStats"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAddrFromPool"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosOvrPIR"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosOvrCIR"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosOvrAggRateLimit"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfLearnApMac"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfLearnApMacDA"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAuthVlanMismatchTo"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsIpv4Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsIpv4PrefLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsIpv4DefGwAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsDnsServer1"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsDnsServer2"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV14v0Group.setStatus("current")

tmnxWlanGwMgwAmbrIeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 29)
)
tmnxWlanGwMgwAmbrIeGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosUplinkAmbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosDwnlinkAmbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnQosUplinkAmbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnQosDwnlinkAmbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeQosUplinkAmbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeQosDwnlinkAmbr"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAmbrIeGroup.setStatus("current")

tmnxWlanGwVsrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 30)
)
tmnxWlanGwVsrGroup.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomApplication")
)
if mibBuilder.loadTexts:
    tmnxWlanGwVsrGroup.setStatus("current")

tmnxWlanGwDsmV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 32)
)
tmnxWlanGwDsmV14v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cD4natPoolNm"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cD4natLinkAdd"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmD6cD4natAdminSt"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmV14v0Group.setStatus("current")

tmnxWlanGwMdaRedundancyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 33)
)
tmnxWlanGwMdaRedundancyGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpRedundancyUnit"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpActiveMdaLimit"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMdaLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMdaRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMdaTableLastCh"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMdaRedundancyGroup.setStatus("current")

tmnxWlanGwInterVlanMobGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 34)
)
tmnxWlanGwInterVlanMobGroup.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMobInterVlan")
)
if mibBuilder.loadTexts:
    tmnxWlanGwInterVlanMobGroup.setStatus("current")

tmnxWlanGwTunnelQueryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 35)
)
tmnxWlanGwTunnelQueryGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuNextQryId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuMaxQryId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereTuRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereRemAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereRemAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereLocAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereLocAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereAddrFamily"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereEncap"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereEncapTag1"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereEncapTag2"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereApSapPortId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereApSapEncap"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereNumUeMin"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereNumUeMax"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereApLearnFail"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryWhereUeType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryDoGetNumResults"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryNumResults"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuFirstMoveTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuIsaMember"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuInterface"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuApMacAddress"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuApLearnFailed"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuEncapTag1"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuEncapTag2"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuApSapPortId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuApSapEncapVal"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuRemoteUdpPort"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuNumUeMigrant"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuNumUeDsm"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuNumUeL2w"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuNumUeEsm"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuNumUeXcon"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwTunnelQueryGroup.setStatus("current")

tmnxWlanGwHomeUeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 36)
)
tmnxWlanGwHomeUeGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereBridgeId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResBridgeId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeQTag"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeMplsLabel"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeTuRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeTuAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeTuRemoteAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeTuLocalAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeTuQosRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeSsid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUePrevApAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUePrevApAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeLastMoveTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeImsi"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeSapPortId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeSapPortEncapValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdUeEncapsulation"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwHomeUeGroup.setStatus("current")

tmnxWlanGwXconnectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 37)
)
tmnxWlanGwXconnectGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwXcnctLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwXcnctIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwXcnctTnlSrcIpAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwXcnctTnlSrcIpAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwXcnctTnlSrcIpPrefixLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwXcnctAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwXcnctTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanXcnctAccPolicy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanXcnctLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanXcnctAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanXcnctTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanXcnctAcctUpdInterv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanXcnctMobAcctUpd"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwXconnectGroup.setStatus("current")

tmnxWlanGwMobilityV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 38)
)
tmnxWlanGwMobilityV15v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobAcctIntUpdtInclCnts"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobAcctIntUpdtHoldDown"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMobilityV15v0Group.setStatus("current")

tmnxWlanGwLeV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 39)
)
tmnxWlanGwLeV15v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLeRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLeLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLeAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLeWlanGwGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLeVtepStartType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLeVtepStart"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLeVtepEndType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLeVtepEnd"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLeVxlanPort"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdVNI"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdRT"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdRD"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdWlanGwGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdIsaMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMaxLanextBd"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeMacTranslation"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeBdMacPrefix"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeBdMacPrefixLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeAssistAddrRes"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeNetwPolicer"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeNetwMaxMac"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeNetwAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeAccsPolicer"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeAccsMaxMac"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuBdUeSsid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeAccsMultiAccess"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdVlanTag"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdInterface"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdMacTranslation"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdBdMac"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdAssistAddrRes"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdNetwMaxMac"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdNetwAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdAccsMaxMac"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwLeV15v0Group.setStatus("current")

tmnxWlanGwDsmV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 40)
)
tmnxWlanGwDsmV15v0Group.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilType")
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmV15v0Group.setStatus("current")

tmnxWlanGwIsaV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 41)
)
tmnxWlanGwIsaV16v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaStatsName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaStatsValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpWmLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpWmRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpWmHi"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpWmLo"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpIsaAaOversub"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaResrcStatsName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaResrcStatsMaxValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaResrcStatsValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaResrcStatsPeakValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaResrcStatsPeakTime"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaV16v0Group.setStatus("obsolete")

tmnxWlanGwIsaScalingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 42)
)
tmnxWlanGwIsaScalingGroup.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpScalingProfile")
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaScalingGroup.setStatus("current")

tmnxWlanGwUeQryV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 43)
)
tmnxWlanGwUeQryV16v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereAddrFamily"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResAddrFamily"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryV16v0Group.setStatus("current")

tmnxWlanGwGrpIfGwAddrV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 44)
)
tmnxWlanGwGrpIfGwAddrV16v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpIfGwAddrRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpIfGwAddrTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpIfGwAddrPurpose"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwGrpIfGwAddrV16v0Group.setStatus("current")

tmnxWlanGwLePolicerV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 46)
)
tmnxWlanGwLePolicerV16v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdAccsPolicer"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdNetwPolicer"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwLePolicerV16v0Group.setStatus("current")

tmnxWlanGwQryNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 48)
)
tmnxWlanGwQryNameGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQryVolatile"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwQryNameGroup.setStatus("current")

tmnxWlanGwIsaV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 49)
)
tmnxWlanGwIsaV19v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpActiveIomLimit"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpPortPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpTunnelPortPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpOperState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomOperState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberChassisIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberCardSlotNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberSlotNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberEegMemberAct"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberEegMemberPend"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberTuQosProblem"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwResrcProblem"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaStatsName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaStatsValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpWmLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpWmRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpWmHi"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpWmLo"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpIsaAaOversub"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaResrcStatsName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaResrcStatsMaxValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaResrcStatsValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaResrcStatsPeakValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaResrcStatsPeakTime"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaV19v0Group.setStatus("current")

tmnxWlanGwDsmV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 50)
)
tmnxWlanGwDsmV19v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3IngHitCount"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3RedirectURL"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3IngHitCount"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFil6N3RedirectURL"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmV19v0Group.setStatus("current")

tmnxWlanGwEsaV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 51)
)
tmnxWlanGwEsaV19v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVappLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVappRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVappTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberEsaNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberEsaVappNum"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwEsaV19v0Group.setStatus("current")

tmnxWlanGwObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 98)
)
tmnxWlanGwObsoletedGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwCacheTtl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfDataTrigg"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfAuthPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfAuthHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRadProxVrtr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRadProxSrv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRadProxMacFmt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDhcp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtActLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtHttpRdrPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNatPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsVal"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsValHw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsValue"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwObsoletedGroup.setStatus("current")

tmnxWlanGwNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 99)
)
tmnxWlanGwNotifyObjsGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyTrue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotify3gppRelease"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyMdaSlotNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifySubIfIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyAddrFamily"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer1"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer2"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer3"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer4"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer5"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer6"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer7"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer8"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifySubnetAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifySubnetAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifySubnetPrefLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyGtpMsgType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyGtpMsgDirection"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyImsi"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyTeid"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyObjsGroup.setStatus("current")

tmnxWlanGwNotifyObjsV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 3, 101)
)
tmnxWlanGwNotifyObjsV15v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyBdBridgeId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyUeMacAddress"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyObjsV15v0Group.setStatus("current")

tmnxWlanGwNotifyObjsV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 3, 103)
)
tmnxWlanGwNotifyObjsV16v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyChassisIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyCardSlotNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyEntity"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyObjsV16v0Group.setStatus("current")

tmnxWlanGwNotifyObjsV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 3, 105)
)
tmnxWlanGwNotifyObjsV19v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyEsaNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyEsaVappNum"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyObjsV19v0Group.setStatus("current")

tmnxGtpV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 4, 1)
)
tmnxGtpV15v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11ItfTableLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11ItfRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11ItfLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11ItfApnPolicyName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpPpmTableLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpPpmRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpPpmLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpPpmProfileName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeTableLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SePeerRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SePeerAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SePeerAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeRemoteCtrlTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeLocalCtrlTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeChrgChar"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeQosUplinkAmbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeQosDwnlinkAmbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11BcTableLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11BcRemoteTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11BcLocalTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11BcQosUlGbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11BcQosUlMbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11BcQosDlGbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11BcQosDlMbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11BcQosQci"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11BcQosArp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11BcRemoteAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11BcRemoteAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMmeTableLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMmeLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMmeQosUplinkGbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMmeQosUplinkMbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMmeQosDwnlinkGbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMmeQosDwnlinkMbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMmeQosArpValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMmeQosQciValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMmeQosUplinkAmbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMmeQosDwnlinkAmbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpNumMme"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpNumEnodeB"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpNumS11Sessions"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpNumUplinks"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpUplinkTableLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpUplinkRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpUplinkLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpUplinkApn"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpUplinkPdnType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfIpv4Mtu"))
)
if mibBuilder.loadTexts:
    tmnxGtpV15v0Group.setStatus("current")

tmnxGtpAccMobV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 4, 2)
)
tmnxGtpAccMobV16v0Group.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfEndMarkerCount")
)
if mibBuilder.loadTexts:
    tmnxGtpAccMobV16v0Group.setStatus("current")

tmnxGtpAccMobChngRepV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 4, 3)
)
tmnxGtpAccMobChngRepV16v0Group.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfChangeRepAction")
)
if mibBuilder.loadTexts:
    tmnxGtpAccMobChngRepV16v0Group.setStatus("current")

tmnxGtpAccV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 4, 4)
)
tmnxGtpAccV16v0Group.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SePdnTeid")
)
if mibBuilder.loadTexts:
    tmnxGtpAccV16v0Group.setStatus("current")

tmnxGtpAccMobUliV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 4, 5)
)
tmnxGtpAccMobUliV16v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeUliCgi"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeUliSai"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeUliRai"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeUliTai"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpS11SeUliEcgi"))
)
if mibBuilder.loadTexts:
    tmnxGtpAccMobUliV16v0Group.setStatus("current")

tmnxGtpNumSessionV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 4, 6)
)
tmnxGtpNumSessionV16v0Group.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxGtpNumS11IdleSessions")
)
if mibBuilder.loadTexts:
    tmnxGtpNumSessionV16v0Group.setStatus("current")


# Notification objects

tmnxWlanGwResrcProblemDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 1)
)
tmnxWlanGwResrcProblemDetected.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwResrcProblem")
)
if mibBuilder.loadTexts:
    tmnxWlanGwResrcProblemDetected.setStatus(
        "current"
    )

tmnxWlanGwResrcProblemCause = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 2)
)
tmnxWlanGwResrcProblemCause.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription")
)
if mibBuilder.loadTexts:
    tmnxWlanGwResrcProblemCause.setStatus(
        "current"
    )

tmnxWlanGwTuQosProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 3)
)
tmnxWlanGwTuQosProblem.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberTuQosProblem")
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosProblem.setStatus(
        "current"
    )

tmnxWlanGwGrpOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 4)
)
tmnxWlanGwGrpOperStateChanged.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpOperState")
)
if mibBuilder.loadTexts:
    tmnxWlanGwGrpOperStateChanged.setStatus(
        "current"
    )

tmnxWlanGwIomActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 5)
)
tmnxWlanGwIomActive.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyTrue"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwIomActive.setStatus(
        "current"
    )

tmnxWlanGwMgwConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 10)
)
tmnxWlanGwMgwConnected.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyTrue"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwConnected.setStatus(
        "current"
    )

tmnxWlanGwMgwRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 11)
)
tmnxWlanGwMgwRestarted.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRestartCnt")
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwRestarted.setStatus(
        "current"
    )

tmnxWlanGwNumMgwHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 12)
)
tmnxWlanGwNumMgwHi.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumMgw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyTrue"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwNumMgwHi.setStatus(
        "current"
    )

tmnxWlanGwMgwStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 13)
)
tmnxWlanGwMgwStateChanged.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwState")
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwStateChanged.setStatus(
        "current"
    )

tmnxWlanGwQosRadiusGtpMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 14)
)
tmnxWlanGwQosRadiusGtpMismatch.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwInterfaceType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotify3gppRelease"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwQosRadiusGtpMismatch.setStatus(
        "current"
    )

tmnxWlanGwSubIfRedActiveChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 15)
)
tmnxWlanGwSubIfRedActiveChanged.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedActive"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedActiveChanged.setStatus(
        "current"
    )

tmnxWlanGwDsmGtpTunnelSetupFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 16)
)
tmnxWlanGwDsmGtpTunnelSetupFail.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyMdaSlotNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmGtpTunnelSetupFail.setStatus(
        "current"
    )

tmnxWlanGwSubIfPmStartD6cFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 17)
)
tmnxWlanGwSubIfPmStartD6cFailed.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifySubIfIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyAddrFamily"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmStartD6cFailed.setStatus(
        "current"
    )

tmnxWlanGwSubIfPmNewPlReqFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 18)
)
tmnxWlanGwSubIfPmNewPlReqFailed.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifySubIfIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyAddrFamily"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmNewPlReqFailed.setStatus(
        "current"
    )

tmnxWlanGwSubIfPmAddNewPlFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 19)
)
tmnxWlanGwSubIfPmAddNewPlFailed.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifySubnetAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifySubnetAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifySubnetPrefLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifySubIfIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyAddrFamily"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmAddNewPlFailed.setStatus(
        "current"
    )

tmnxWlanGwSubIfPmCrIntObjFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 20)
)
tmnxWlanGwSubIfPmCrIntObjFailed.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsSubnetAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsSubnetAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsSubnetPrefLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsSubIfIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyAddrFamily"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmCrIntObjFailed.setStatus(
        "current"
    )

tmnxWlanGwSubIfPmPoolTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 21)
)
tmnxWlanGwSubIfPmPoolTimeout.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsRemLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyAddrFamily"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmPoolTimeout.setStatus(
        "current"
    )

tmnxWlanGwSubIfPmPoolUsageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 22)
)
tmnxWlanGwSubIfPmPoolUsageLow.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfIpsUsageLevelPct"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyAddrFamily"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmPoolUsageLow.setStatus(
        "current"
    )

tmnxWlanGwSubIfPmLsQryRtryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 23)
)
tmnxWlanGwSubIfPmLsQryRtryFailed.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifySubIfIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyAddrFamily"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer1"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer2"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer3"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer4"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer5"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer6"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer7"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyD6cServer8"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmLsQryRtryFailed.setStatus(
        "current"
    )

tmnxWlanGwGtpMessageDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 24)
)
tmnxWlanGwGtpMessageDropped.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwControl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyGtpMsgType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyGtpMsgDirection"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyImsi"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwGtpMessageDropped.setStatus(
        "current"
    )

tmnxWlanGwSubIfPmPoolPartialUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 25)
)
tmnxWlanGwSubIfPmPoolPartialUse.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifySubIfIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyAddrFamily"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfPmPoolPartialUse.setStatus(
        "current"
    )

tmnxWlanGwBdCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 26)
)
tmnxWlanGwBdCreated.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyBdBridgeId")
)
if mibBuilder.loadTexts:
    tmnxWlanGwBdCreated.setStatus(
        "current"
    )

tmnxWlanGwBdDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 27)
)
tmnxWlanGwBdDeleted.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyBdBridgeId")
)
if mibBuilder.loadTexts:
    tmnxWlanGwBdDeleted.setStatus(
        "current"
    )

tmnxWlanGwUeCreationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 28)
)
tmnxWlanGwUeCreationFail.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyBdBridgeId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyUeMacAddress"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeCreationFail.setStatus(
        "current"
    )

tmnxWlanGwUeReplacement = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 29)
)
tmnxWlanGwUeReplacement.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyBdBridgeId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyUeMacAddress"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeReplacement.setStatus(
        "current"
    )

tmnxWlanGwGrpMemberUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 30)
)
tmnxWlanGwGrpMemberUsageHigh.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyEntity"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyTrue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyIsaMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyChassisIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyCardSlotNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyMdaSlotNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyEsaNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyEsaVappNum"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwGrpMemberUsageHigh.setStatus(
        "current"
    )


# Notifications groups

tmnxWlanGwNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 100)
)
tmnxWlanGwNotifyGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwResrcProblemDetected"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwResrcProblemCause"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosProblem"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpOperStateChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomActive"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwConnected"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRestarted"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumMgwHi"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwStateChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwQosRadiusGtpMismatch"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmGtpTunnelSetupFail"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedActiveChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmStartD6cFailed"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmNewPlReqFailed"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmAddNewPlFailed"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmCrIntObjFailed"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmPoolTimeout"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmPoolUsageLow"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmLsQryRtryFailed"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpMessageDropped"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfPmPoolPartialUse"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyGroup.setStatus(
        "current"
    )

tmnxWlanGwNotifyV15v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 3, 102)
)
tmnxWlanGwNotifyV15v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdCreated"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBdDeleted"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeCreationFail"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeReplacement"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyV15v0Group.setStatus(
        "current"
    )

tmnxWlanGwNotifyV16v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 3, 104)
)
tmnxWlanGwNotifyV16v0Group.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpMemberUsageHigh")
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyV16v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxWlanGwCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 1)
)
tmnxWlanGwCompliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObjGroup"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwCompliance.setStatus(
        "obsolete"
    )

tmnxWlanGwNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 2)
)
tmnxWlanGwNotifyCompliance.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyGroup")
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyCompliance.setStatus(
        "obsolete"
    )

tmnxWlanGwV10Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 3)
)
tmnxWlanGwV10Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObjGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwGroup"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV10Compliance.setStatus(
        "obsolete"
    )

tmnxWlanGwV11Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 4)
)
tmnxWlanGwV11Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreV11v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObjGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwV11v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwQosIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwChargingCharGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObsoletedGroup"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV11Compliance.setStatus(
        "obsolete"
    )

tmnxWlanGwV12Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 5)
)
tmnxWlanGwV12Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwRedGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwV11v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwQosIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwChargingCharGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobilityGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSeHoldTimeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObsoletedGroup"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV12Compliance.setStatus(
        "obsolete"
    )

tmnxWlanGwV13Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 6)
)
tmnxWlanGwV13Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwRedGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwV11v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwQosIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwChargingCharGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobilityGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSeHoldTimeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV13v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2ApGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2tpv3Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObsoletedGroup"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV13Compliance.setStatus(
        "obsolete"
    )

tmnxWlanGwV14Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 7)
)
tmnxWlanGwV14Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwRedGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwV11v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwQosIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwChargingCharGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobilityGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSeHoldTimeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV13v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2ApGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2tpv3Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwV14v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAmbrIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVsrGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObsoletedGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV14v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMdaRedundancyGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwInterVlanMobGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTunnelQueryGroup"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV14Compliance.setStatus(
        "obsolete"
    )

tmnxWlanGwV15Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 8)
)
tmnxWlanGwV15Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwRedGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwV11v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwQosIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwChargingCharGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobilityGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobilityV15v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSeHoldTimeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV13v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2ApGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2tpv3Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwV14v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAmbrIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVsrGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObsoletedGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV14v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMdaRedundancyGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwInterVlanMobGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTunnelQueryGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwHomeUeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwXconnectGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLeV15v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV15v0Group"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV15Compliance.setStatus(
        "obsolete"
    )

tmnxWlanGwNotifyV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 9)
)
tmnxWlanGwNotifyV15v0Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyV15v0Group"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyV15v0Compliance.setStatus(
        "obsolete"
    )

tmnxWlanGwV16Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 10)
)
tmnxWlanGwV16Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwRedGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwV11v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwQosIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwChargingCharGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobilityGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobilityV15v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSeHoldTimeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV13v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2ApGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2tpv3Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwV14v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAmbrIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVsrGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObsoletedGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV14v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMdaRedundancyGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwInterVlanMobGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTunnelQueryGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwHomeUeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwXconnectGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLeV15v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV15v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaV16v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaScalingGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryV16v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpIfGwAddrV16v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLePolicerV16v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwQryNameGroup"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV16Compliance.setStatus(
        "obsolete"
    )

tmnxWlanGwNotifyV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 11)
)
tmnxWlanGwNotifyV16v0Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyV15v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyV16v0Group"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyV16v0Compliance.setStatus(
        "current"
    )

tmnxWlanGwV17Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 12)
)
tmnxWlanGwV17Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwRedGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwV11v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwQosIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwChargingCharGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobilityGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobilityV15v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSeHoldTimeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV13v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2ApGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwL2tpv3Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwV14v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAmbrIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVsrGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObsoletedGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV14v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMdaRedundancyGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwInterVlanMobGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTunnelQueryGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwHomeUeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwXconnectGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLeV15v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV15v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaScalingGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryV16v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpIfGwAddrV16v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLePolicerV16v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwQryNameGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaV19v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmV19v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwEsaV19v0Group"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV17Compliance.setStatus(
        "current"
    )

tmnxGtpV15Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 3, 1)
)
tmnxGtpV15Compliance.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxGtpV15v0Group")
)
if mibBuilder.loadTexts:
    tmnxGtpV15Compliance.setStatus(
        "current"
    )

tmnxGtpV16Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 3, 2)
)
tmnxGtpV16Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxGtpAccV16v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpAccMobV16v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpAccMobChngRepV16v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpAccMobUliV16v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxGtpNumSessionV16v0Group"))
)
if mibBuilder.loadTexts:
    tmnxGtpV16Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-WLAN-GW-MIB",
    **{"TmnxWlanGwAmbr": TmnxWlanGwAmbr,
       "TmnxWlanGwBurstSize": TmnxWlanGwBurstSize,
       "TmnxWlanGwIsaIomOperState": TmnxWlanGwIsaIomOperState,
       "TmnxWlanGwMgwInterfaceType": TmnxWlanGwMgwInterfaceType,
       "TmnxWlanGwDsmFilterDefaultAction": TmnxWlanGwDsmFilterDefaultAction,
       "TmnxWlanGwDsmFilterAction": TmnxWlanGwDsmFilterAction,
       "TmnxWlanGwQoSOperState": TmnxWlanGwQoSOperState,
       "TmnxWlanGwGtpSeIdentifier": TmnxWlanGwGtpSeIdentifier,
       "TmnxWlanGwSsidType": TmnxWlanGwSsidType,
       "TmnxWlanGwUeAddressFamily": TmnxWlanGwUeAddressFamily,
       "TmnxWlanGwUeEncapsulation": TmnxWlanGwUeEncapsulation,
       "TmnxWlanGwUeIdentifier": TmnxWlanGwUeIdentifier,
       "TmnxWlanGwChargingCharBits": TmnxWlanGwChargingCharBits,
       "TmnxWlanGwSubIfIpsAddrFamily": TmnxWlanGwSubIfIpsAddrFamily,
       "TmnxWlanGwVlanIdleTimeoutAction": TmnxWlanGwVlanIdleTimeoutAction,
       "TmnxWlanGwWatermarkEntity": TmnxWlanGwWatermarkEntity,
       "TmnxGtpInterfaceType": TmnxGtpInterfaceType,
       "timetraWlanGwMIBModule": timetraWlanGwMIBModule,
       "tmnxWlanGwConformance": tmnxWlanGwConformance,
       "tmnxWlanGwCompliances": tmnxWlanGwCompliances,
       "tmnxWlanGwCompliance": tmnxWlanGwCompliance,
       "tmnxWlanGwNotifyCompliance": tmnxWlanGwNotifyCompliance,
       "tmnxWlanGwV10Compliance": tmnxWlanGwV10Compliance,
       "tmnxWlanGwV11Compliance": tmnxWlanGwV11Compliance,
       "tmnxWlanGwV12Compliance": tmnxWlanGwV12Compliance,
       "tmnxWlanGwV13Compliance": tmnxWlanGwV13Compliance,
       "tmnxWlanGwV14Compliance": tmnxWlanGwV14Compliance,
       "tmnxWlanGwV15Compliance": tmnxWlanGwV15Compliance,
       "tmnxWlanGwNotifyV15v0Compliance": tmnxWlanGwNotifyV15v0Compliance,
       "tmnxWlanGwV16Compliance": tmnxWlanGwV16Compliance,
       "tmnxWlanGwNotifyV16v0Compliance": tmnxWlanGwNotifyV16v0Compliance,
       "tmnxWlanGwV17Compliance": tmnxWlanGwV17Compliance,
       "tmnxWlanGwGroups": tmnxWlanGwGroups,
       "tmnxWlanGwIsaGroup": tmnxWlanGwIsaGroup,
       "tmnxWlanGwSoftGreGroup": tmnxWlanGwSoftGreGroup,
       "tmnxWlanGwObjGroup": tmnxWlanGwObjGroup,
       "tmnxWlanGwMgwGroup": tmnxWlanGwMgwGroup,
       "tmnxWlanGwSoftGreV11v0Group": tmnxWlanGwSoftGreV11v0Group,
       "tmnxWlanGwMgwV11v0Group": tmnxWlanGwMgwV11v0Group,
       "tmnxWlanGwMgwQosIeGroup": tmnxWlanGwMgwQosIeGroup,
       "tmnxWlanGwMgwChargingCharGroup": tmnxWlanGwMgwChargingCharGroup,
       "tmnxWlanGwMobilityGroup": tmnxWlanGwMobilityGroup,
       "tmnxWlanGwMgwSeHoldTimeGroup": tmnxWlanGwMgwSeHoldTimeGroup,
       "tmnxWlanGwV12v0Group": tmnxWlanGwV12v0Group,
       "tmnxWlanGwSoftGreV12v0Group": tmnxWlanGwSoftGreV12v0Group,
       "tmnxWlanGwRedGroup": tmnxWlanGwRedGroup,
       "tmnxWlanGwDsmGroup": tmnxWlanGwDsmGroup,
       "tmnxWlanGwUeQryGroup": tmnxWlanGwUeQryGroup,
       "tmnxWlanGwDsmV13v0Group": tmnxWlanGwDsmV13v0Group,
       "tmnxWlanGwL2ApGroup": tmnxWlanGwL2ApGroup,
       "tmnxWlanGwL2tpv3Group": tmnxWlanGwL2tpv3Group,
       "tmnxWlanGwV14v0Group": tmnxWlanGwV14v0Group,
       "tmnxWlanGwMgwAmbrIeGroup": tmnxWlanGwMgwAmbrIeGroup,
       "tmnxWlanGwVsrGroup": tmnxWlanGwVsrGroup,
       "tmnxWlanGwDsmV14v0Group": tmnxWlanGwDsmV14v0Group,
       "tmnxWlanGwMdaRedundancyGroup": tmnxWlanGwMdaRedundancyGroup,
       "tmnxWlanGwInterVlanMobGroup": tmnxWlanGwInterVlanMobGroup,
       "tmnxWlanGwTunnelQueryGroup": tmnxWlanGwTunnelQueryGroup,
       "tmnxWlanGwHomeUeGroup": tmnxWlanGwHomeUeGroup,
       "tmnxWlanGwXconnectGroup": tmnxWlanGwXconnectGroup,
       "tmnxWlanGwMobilityV15v0Group": tmnxWlanGwMobilityV15v0Group,
       "tmnxWlanGwLeV15v0Group": tmnxWlanGwLeV15v0Group,
       "tmnxWlanGwDsmV15v0Group": tmnxWlanGwDsmV15v0Group,
       "tmnxWlanGwIsaV16v0Group": tmnxWlanGwIsaV16v0Group,
       "tmnxWlanGwIsaScalingGroup": tmnxWlanGwIsaScalingGroup,
       "tmnxWlanGwUeQryV16v0Group": tmnxWlanGwUeQryV16v0Group,
       "tmnxWlanGwGrpIfGwAddrV16v0Group": tmnxWlanGwGrpIfGwAddrV16v0Group,
       "tmnxWlanGwLePolicerV16v0Group": tmnxWlanGwLePolicerV16v0Group,
       "tmnxWlanGwQryNameGroup": tmnxWlanGwQryNameGroup,
       "tmnxWlanGwIsaV19v0Group": tmnxWlanGwIsaV19v0Group,
       "tmnxWlanGwDsmV19v0Group": tmnxWlanGwDsmV19v0Group,
       "tmnxWlanGwEsaV19v0Group": tmnxWlanGwEsaV19v0Group,
       "tmnxWlanGwObsoletedGroup": tmnxWlanGwObsoletedGroup,
       "tmnxWlanGwNotifyObjsGroup": tmnxWlanGwNotifyObjsGroup,
       "tmnxWlanGwNotifyGroup": tmnxWlanGwNotifyGroup,
       "tmnxGtpCompliances": tmnxGtpCompliances,
       "tmnxGtpV15Compliance": tmnxGtpV15Compliance,
       "tmnxGtpV16Compliance": tmnxGtpV16Compliance,
       "tmnxWlanGwNotifyObjsV15v0Group": tmnxWlanGwNotifyObjsV15v0Group,
       "tmnxWlanGwNotifyV15v0Group": tmnxWlanGwNotifyV15v0Group,
       "tmnxWlanGwNotifyObjsV16v0Group": tmnxWlanGwNotifyObjsV16v0Group,
       "tmnxWlanGwNotifyV16v0Group": tmnxWlanGwNotifyV16v0Group,
       "tmnxWlanGwNotifyObjsV19v0Group": tmnxWlanGwNotifyObjsV19v0Group,
       "tmnxGtpGroups": tmnxGtpGroups,
       "tmnxGtpV15v0Group": tmnxGtpV15v0Group,
       "tmnxGtpAccMobV16v0Group": tmnxGtpAccMobV16v0Group,
       "tmnxGtpAccMobChngRepV16v0Group": tmnxGtpAccMobChngRepV16v0Group,
       "tmnxGtpAccV16v0Group": tmnxGtpAccV16v0Group,
       "tmnxGtpAccMobUliV16v0Group": tmnxGtpAccMobUliV16v0Group,
       "tmnxGtpNumSessionV16v0Group": tmnxGtpNumSessionV16v0Group,
       "tmnxWlanGw": tmnxWlanGw,
       "tmnxWlanGwObjs": tmnxWlanGwObjs,
       "tmnxWlanGwIsaObjs": tmnxWlanGwIsaObjs,
       "tmnxWlanGwGrpTable": tmnxWlanGwGrpTable,
       "tmnxWlanGwGrpEntry": tmnxWlanGwGrpEntry,
       "tmnxWlanGwGrpId": tmnxWlanGwGrpId,
       "tmnxWlanGwGrpRowStatus": tmnxWlanGwGrpRowStatus,
       "tmnxWlanGwGrpLastMgmtChange": tmnxWlanGwGrpLastMgmtChange,
       "tmnxWlanGwGrpDescription": tmnxWlanGwGrpDescription,
       "tmnxWlanGwGrpAdminState": tmnxWlanGwGrpAdminState,
       "tmnxWlanGwGrpActiveIomLimit": tmnxWlanGwGrpActiveIomLimit,
       "tmnxWlanGwGrpPortPlcy": tmnxWlanGwGrpPortPlcy,
       "tmnxWlanGwGrpTunnelPortPlcy": tmnxWlanGwGrpTunnelPortPlcy,
       "tmnxWlanGwGrpIsaAaGroup": tmnxWlanGwGrpIsaAaGroup,
       "tmnxWlanGwGrpOperState": tmnxWlanGwGrpOperState,
       "tmnxWlanGwGrpDegraded": tmnxWlanGwGrpDegraded,
       "tmnxWlanGwGrpRedundancyUnit": tmnxWlanGwGrpRedundancyUnit,
       "tmnxWlanGwGrpActiveMdaLimit": tmnxWlanGwGrpActiveMdaLimit,
       "tmnxWlanGwGrpScalingProfile": tmnxWlanGwGrpScalingProfile,
       "tmnxWlanGwGrpIsaAaOversub": tmnxWlanGwGrpIsaAaOversub,
       "tmnxWlanGwIomTable": tmnxWlanGwIomTable,
       "tmnxWlanGwIomEntry": tmnxWlanGwIomEntry,
       "tmnxWlanGwIomRowStatus": tmnxWlanGwIomRowStatus,
       "tmnxWlanGwIomLastMgmtChange": tmnxWlanGwIomLastMgmtChange,
       "tmnxWlanGwIomOperState": tmnxWlanGwIomOperState,
       "tmnxWlanGwIomApplication": tmnxWlanGwIomApplication,
       "tmnxWlanGwIsaMemberTable": tmnxWlanGwIsaMemberTable,
       "tmnxWlanGwIsaMemberEntry": tmnxWlanGwIsaMemberEntry,
       "tmnxWlanGwIsaMemberId": tmnxWlanGwIsaMemberId,
       "tmnxWlanGwIsaMemberChassisIndex": tmnxWlanGwIsaMemberChassisIndex,
       "tmnxWlanGwIsaMemberCardSlotNum": tmnxWlanGwIsaMemberCardSlotNum,
       "tmnxWlanGwIsaMemberSlotNum": tmnxWlanGwIsaMemberSlotNum,
       "tmnxWlanGwIsaMemberNumSoftGreTu": tmnxWlanGwIsaMemberNumSoftGreTu,
       "tmnxWlanGwIsaMemberNumUe": tmnxWlanGwIsaMemberNumUe,
       "tmnxWlanGwIsaMemberEegMemberAct": tmnxWlanGwIsaMemberEegMemberAct,
       "tmnxWlanGwIsaMemberEegMemberPend": tmnxWlanGwIsaMemberEegMemberPend,
       "tmnxWlanGwIsaMemberTuQosProblem": tmnxWlanGwIsaMemberTuQosProblem,
       "tmnxWlanGwIsaMemberEsaNum": tmnxWlanGwIsaMemberEsaNum,
       "tmnxWlanGwIsaMemberEsaVappNum": tmnxWlanGwIsaMemberEsaVappNum,
       "tmnxWlanGwIsaMemberStatsTable": tmnxWlanGwIsaMemberStatsTable,
       "tmnxWlanGwIsaMemberStatsEntry": tmnxWlanGwIsaMemberStatsEntry,
       "tmnxWlanGwIsaMemberStatsType": tmnxWlanGwIsaMemberStatsType,
       "tmnxWlanGwIsaMemberStatsName": tmnxWlanGwIsaMemberStatsName,
       "tmnxWlanGwIsaMemberStatsVal": tmnxWlanGwIsaMemberStatsVal,
       "tmnxWlanGwIsaMemberStatsValHw": tmnxWlanGwIsaMemberStatsValHw,
       "tmnxWlanGwIsaMemberStatsValue": tmnxWlanGwIsaMemberStatsValue,
       "tmnxWlanGwMdaTable": tmnxWlanGwMdaTable,
       "tmnxWlanGwMdaEntry": tmnxWlanGwMdaEntry,
       "tmnxWlanGwMdaRowStatus": tmnxWlanGwMdaRowStatus,
       "tmnxWlanGwMdaLastMgmtChange": tmnxWlanGwMdaLastMgmtChange,
       "tmnxWlanGwIsaStatsTable": tmnxWlanGwIsaStatsTable,
       "tmnxWlanGwIsaStatsEntry": tmnxWlanGwIsaStatsEntry,
       "tmnxWlanGwIsaStatsType": tmnxWlanGwIsaStatsType,
       "tmnxWlanGwIsaStatsId": tmnxWlanGwIsaStatsId,
       "tmnxWlanGwIsaStatsName": tmnxWlanGwIsaStatsName,
       "tmnxWlanGwIsaStatsValue": tmnxWlanGwIsaStatsValue,
       "tmnxWlanGwGrpWmTable": tmnxWlanGwGrpWmTable,
       "tmnxWlanGwGrpWmEntry": tmnxWlanGwGrpWmEntry,
       "tmnxWlanGwGrpWmEntity": tmnxWlanGwGrpWmEntity,
       "tmnxWlanGwGrpWmRowStatus": tmnxWlanGwGrpWmRowStatus,
       "tmnxWlanGwGrpWmLastMgmtChange": tmnxWlanGwGrpWmLastMgmtChange,
       "tmnxWlanGwGrpWmHi": tmnxWlanGwGrpWmHi,
       "tmnxWlanGwGrpWmLo": tmnxWlanGwGrpWmLo,
       "tmnxWlanGwIsaResrcStatsTable": tmnxWlanGwIsaResrcStatsTable,
       "tmnxWlanGwIsaResrcStatsEntry": tmnxWlanGwIsaResrcStatsEntry,
       "tmnxWlanGwIsaResrcStatsId": tmnxWlanGwIsaResrcStatsId,
       "tmnxWlanGwIsaResrcStatsName": tmnxWlanGwIsaResrcStatsName,
       "tmnxWlanGwIsaResrcStatsMaxValue": tmnxWlanGwIsaResrcStatsMaxValue,
       "tmnxWlanGwIsaResrcStatsValue": tmnxWlanGwIsaResrcStatsValue,
       "tmnxWlanGwIsaResrcStatsPeakValue": tmnxWlanGwIsaResrcStatsPeakValue,
       "tmnxWlanGwIsaResrcStatsPeakTime": tmnxWlanGwIsaResrcStatsPeakTime,
       "tmnxWlanGwEsaObjs": tmnxWlanGwEsaObjs,
       "tmnxWlanGwVappTable": tmnxWlanGwVappTable,
       "tmnxWlanGwVappEntry": tmnxWlanGwVappEntry,
       "tmnxWlanGwEsaNum": tmnxWlanGwEsaNum,
       "tmnxWlanGwEsaVappNum": tmnxWlanGwEsaVappNum,
       "tmnxWlanGwVappRowStatus": tmnxWlanGwVappRowStatus,
       "tmnxWlanGwVappLastMgmtChange": tmnxWlanGwVappLastMgmtChange,
       "tmnxWlanGwSoftGreObjs": tmnxWlanGwSoftGreObjs,
       "tmnxWlanGwSoftGreIfTable": tmnxWlanGwSoftGreIfTable,
       "tmnxWlanGwSoftGreIfEntry": tmnxWlanGwSoftGreIfEntry,
       "tmnxWlanGwSoftGreIfLastCh": tmnxWlanGwSoftGreIfLastCh,
       "tmnxWlanGwSoftGreIfAdminState": tmnxWlanGwSoftGreIfAdminState,
       "tmnxWlanGwSoftGreIfRouter": tmnxWlanGwSoftGreIfRouter,
       "tmnxWlanGwSoftGreIfGwAddrType": tmnxWlanGwSoftGreIfGwAddrType,
       "tmnxWlanGwSoftGreIfGwAddr": tmnxWlanGwSoftGreIfGwAddr,
       "tmnxWlanGwSoftGreIfGrpId": tmnxWlanGwSoftGreIfGrpId,
       "tmnxWlanGwSoftGreIfShapingType": tmnxWlanGwSoftGreIfShapingType,
       "tmnxWlanGwSoftGreIfShapeMultiUe": tmnxWlanGwSoftGreIfShapeMultiUe,
       "tmnxWlanGwSoftGreIfEQosPlcy": tmnxWlanGwSoftGreIfEQosPlcy,
       "tmnxWlanGwSoftGreIfESchedPlcy": tmnxWlanGwSoftGreIfESchedPlcy,
       "tmnxWlanGwSoftGreIfEAggRateLimit": tmnxWlanGwSoftGreIfEAggRateLimit,
       "tmnxWlanGwSoftGreIfMobTrigger": tmnxWlanGwSoftGreIfMobTrigger,
       "tmnxWlanGwSoftGreIfMobHoldTime": tmnxWlanGwSoftGreIfMobHoldTime,
       "tmnxWlanGwSoftGreIfDefRetailSvc": tmnxWlanGwSoftGreIfDefRetailSvc,
       "tmnxWlanGwSoftGreIfTcpMssAdjust": tmnxWlanGwSoftGreIfTcpMssAdjust,
       "tmnxWlanGwSoftGreIfEHoldTime": tmnxWlanGwSoftGreIfEHoldTime,
       "tmnxWlanGwSoftGreIfDataTrigg": tmnxWlanGwSoftGreIfDataTrigg,
       "tmnxWlanGwSoftGreIfAuthPlcy": tmnxWlanGwSoftGreIfAuthPlcy,
       "tmnxWlanGwSoftGreIfAuthHoldTime": tmnxWlanGwSoftGreIfAuthHoldTime,
       "tmnxWlanGwSoftGreIfRadProxVrtr": tmnxWlanGwSoftGreIfRadProxVrtr,
       "tmnxWlanGwSoftGreIfRadProxSrv": tmnxWlanGwSoftGreIfRadProxSrv,
       "tmnxWlanGwSoftGreIfRadProxMacFmt": tmnxWlanGwSoftGreIfRadProxMacFmt,
       "tmnxWlanGwSoftGreIfSsidType": tmnxWlanGwSoftGreIfSsidType,
       "tmnxWlanGwSoftGreIfGwV6AddrType": tmnxWlanGwSoftGreIfGwV6AddrType,
       "tmnxWlanGwSoftGreIfGwV6Addr": tmnxWlanGwSoftGreIfGwV6Addr,
       "tmnxWlanGwSoftGreIfMobArpAp": tmnxWlanGwSoftGreIfMobArpAp,
       "tmnxWlanGwSoftGreIfDownIfGrpDeg": tmnxWlanGwSoftGreIfDownIfGrpDeg,
       "tmnxWlanGwSoftGreIfL2ApEncapType": tmnxWlanGwSoftGreIfL2ApEncapType,
       "tmnxWlanGwSoftGreIfMultiTuType": tmnxWlanGwSoftGreIfMultiTuType,
       "tmnxWlanGwSoftGreIfL2tpLrnCookie": tmnxWlanGwSoftGreIfL2tpLrnCookie,
       "tmnxWlanGwSoftGreIfL2tpCookie": tmnxWlanGwSoftGreIfL2tpCookie,
       "tmnxWlanGwSoftGreIfMaxLanextBd": tmnxWlanGwSoftGreIfMaxLanextBd,
       "tmnxWlanGwSoftGreIfNumSoftGreTu": tmnxWlanGwSoftGreIfNumSoftGreTu,
       "tmnxWlanGwSoftGreIfLearnApMac": tmnxWlanGwSoftGreIfLearnApMac,
       "tmnxWlanGwSoftGreIfLearnApMacDA": tmnxWlanGwSoftGreIfLearnApMacDA,
       "tmnxWlanGwSoftGreIfMobInterVlan": tmnxWlanGwSoftGreIfMobInterVlan,
       "tmnxWlanGwSoftGreIfL2ApAutoSubId": tmnxWlanGwSoftGreIfL2ApAutoSubId,
       "tmnxWlanGwSoftGreTuTable": tmnxWlanGwSoftGreTuTable,
       "tmnxWlanGwSoftGreTuEntry": tmnxWlanGwSoftGreTuEntry,
       "tmnxWlanGwSoftGreTuRemoteAddrTyp": tmnxWlanGwSoftGreTuRemoteAddrTyp,
       "tmnxWlanGwSoftGreTuRemoteAddr": tmnxWlanGwSoftGreTuRemoteAddr,
       "tmnxWlanGwSoftGreTuLocalAddrType": tmnxWlanGwSoftGreTuLocalAddrType,
       "tmnxWlanGwSoftGreTuLocalAddr": tmnxWlanGwSoftGreTuLocalAddr,
       "tmnxWlanGwSoftGreTuEstabTime": tmnxWlanGwSoftGreTuEstabTime,
       "tmnxWlanGwSoftGreTuIsaGroup": tmnxWlanGwSoftGreTuIsaGroup,
       "tmnxWlanGwSoftGreTuIsaMember": tmnxWlanGwSoftGreTuIsaMember,
       "tmnxWlanGwSoftGreTuNumUe": tmnxWlanGwSoftGreTuNumUe,
       "tmnxWlanGwSoftGreTuApMacAddress": tmnxWlanGwSoftGreTuApMacAddress,
       "tmnxWlanGwSoftGreTuApLearnFailed": tmnxWlanGwSoftGreTuApLearnFailed,
       "tmnxWlanGwSoftGreTuEncap": tmnxWlanGwSoftGreTuEncap,
       "tmnxWlanGwSoftGreTuEncapTag1": tmnxWlanGwSoftGreTuEncapTag1,
       "tmnxWlanGwSoftGreTuEncapTag2": tmnxWlanGwSoftGreTuEncapTag2,
       "tmnxWlanGwSoftGreTuService": tmnxWlanGwSoftGreTuService,
       "tmnxWlanGwSoftGreTuInterface": tmnxWlanGwSoftGreTuInterface,
       "tmnxWlanGwSoftGreTuApSapPortId": tmnxWlanGwSoftGreTuApSapPortId,
       "tmnxWlanGwSoftGreTuApSapEncapVal": tmnxWlanGwSoftGreTuApSapEncapVal,
       "tmnxWlanGwTuQosTable": tmnxWlanGwTuQosTable,
       "tmnxWlanGwTuQosEntry": tmnxWlanGwTuQosEntry,
       "tmnxWlanGwTuQosRetailService": tmnxWlanGwTuQosRetailService,
       "tmnxWlanGwTuQosEegSvcId": tmnxWlanGwTuQosEegSvcId,
       "tmnxWlanGwTuQosEegPortId": tmnxWlanGwTuQosEegPortId,
       "tmnxWlanGwTuQosEegEncapValue": tmnxWlanGwTuQosEegEncapValue,
       "tmnxWlanGwTuQosEegName": tmnxWlanGwTuQosEegName,
       "tmnxWlanGwTuQosEegMember": tmnxWlanGwTuQosEegMember,
       "tmnxWlanGwTuQosState": tmnxWlanGwTuQosState,
       "tmnxWlanGwTuQosNumUe": tmnxWlanGwTuQosNumUe,
       "tmnxWlanGwTuQosRemainingHoldTime": tmnxWlanGwTuQosRemainingHoldTime,
       "tmnxWlanGwSoftGreTuUeTable": tmnxWlanGwSoftGreTuUeTable,
       "tmnxWlanGwSoftGreTuUeEntry": tmnxWlanGwSoftGreTuUeEntry,
       "tmnxWlanGwSoftGreTuUeSsid": tmnxWlanGwSoftGreTuUeSsid,
       "tmnxWlanGwSoftGreXtTable": tmnxWlanGwSoftGreXtTable,
       "tmnxWlanGwSoftGreXtEntry": tmnxWlanGwSoftGreXtEntry,
       "tmnxWlanGwSoftGreXtLastCh": tmnxWlanGwSoftGreXtLastCh,
       "tmnxWlanGwSoftGreXtDhcp": tmnxWlanGwSoftGreXtDhcp,
       "tmnxWlanGwSoftGreXtAddrType": tmnxWlanGwSoftGreXtAddrType,
       "tmnxWlanGwSoftGreXtAddr": tmnxWlanGwSoftGreXtAddr,
       "tmnxWlanGwSoftGreXtLeaseTime": tmnxWlanGwSoftGreXtLeaseTime,
       "tmnxWlanGwSoftGreXtActLeaseTime": tmnxWlanGwSoftGreXtActLeaseTime,
       "tmnxWlanGwSoftGreXtDns1AddrType": tmnxWlanGwSoftGreXtDns1AddrType,
       "tmnxWlanGwSoftGreXtDns1Addr": tmnxWlanGwSoftGreXtDns1Addr,
       "tmnxWlanGwSoftGreXtDns2AddrType": tmnxWlanGwSoftGreXtDns2AddrType,
       "tmnxWlanGwSoftGreXtDns2Addr": tmnxWlanGwSoftGreXtDns2Addr,
       "tmnxWlanGwSoftGreXtNb1AddrType": tmnxWlanGwSoftGreXtNb1AddrType,
       "tmnxWlanGwSoftGreXtNb1Addr": tmnxWlanGwSoftGreXtNb1Addr,
       "tmnxWlanGwSoftGreXtNb2AddrType": tmnxWlanGwSoftGreXtNb2AddrType,
       "tmnxWlanGwSoftGreXtNb2Addr": tmnxWlanGwSoftGreXtNb2Addr,
       "tmnxWlanGwSoftGreXtHttpRdrPlcy": tmnxWlanGwSoftGreXtHttpRdrPlcy,
       "tmnxWlanGwSoftGreXtNatPlcy": tmnxWlanGwSoftGreXtNatPlcy,
       "tmnxWlanGwVlanTable": tmnxWlanGwVlanTable,
       "tmnxWlanGwVlanEntry": tmnxWlanGwVlanEntry,
       "tmnxWlanGwVlanTagStart": tmnxWlanGwVlanTagStart,
       "tmnxWlanGwVlanTagEnd": tmnxWlanGwVlanTagEnd,
       "tmnxWlanGwVlanRowStatus": tmnxWlanGwVlanRowStatus,
       "tmnxWlanGwVlanLastCh": tmnxWlanGwVlanLastCh,
       "tmnxWlanGwVlanRetailService": tmnxWlanGwVlanRetailService,
       "tmnxWlanGwVlanDhcp": tmnxWlanGwVlanDhcp,
       "tmnxWlanGwVlanAddrType": tmnxWlanGwVlanAddrType,
       "tmnxWlanGwVlanAddr": tmnxWlanGwVlanAddr,
       "tmnxWlanGwVlanLeaseTime": tmnxWlanGwVlanLeaseTime,
       "tmnxWlanGwVlanActLeaseTime": tmnxWlanGwVlanActLeaseTime,
       "tmnxWlanGwVlanDns1AddrType": tmnxWlanGwVlanDns1AddrType,
       "tmnxWlanGwVlanDns1Addr": tmnxWlanGwVlanDns1Addr,
       "tmnxWlanGwVlanDns2AddrType": tmnxWlanGwVlanDns2AddrType,
       "tmnxWlanGwVlanDns2Addr": tmnxWlanGwVlanDns2Addr,
       "tmnxWlanGwVlanNb1AddrType": tmnxWlanGwVlanNb1AddrType,
       "tmnxWlanGwVlanNb1Addr": tmnxWlanGwVlanNb1Addr,
       "tmnxWlanGwVlanNb2AddrType": tmnxWlanGwVlanNb2AddrType,
       "tmnxWlanGwVlanNb2Addr": tmnxWlanGwVlanNb2Addr,
       "tmnxWlanGwVlanHttpRdrPlcy": tmnxWlanGwVlanHttpRdrPlcy,
       "tmnxWlanGwVlanNatPlcy": tmnxWlanGwVlanNatPlcy,
       "tmnxWlanGwVlanDataTrigg": tmnxWlanGwVlanDataTrigg,
       "tmnxWlanGwVlanAuthPlcy": tmnxWlanGwVlanAuthPlcy,
       "tmnxWlanGwVlanAuthHoldTime": tmnxWlanGwVlanAuthHoldTime,
       "tmnxWlanGwVlanRadProxVrtr": tmnxWlanGwVlanRadProxVrtr,
       "tmnxWlanGwVlanRadProxSrv": tmnxWlanGwVlanRadProxSrv,
       "tmnxWlanGwVlanRadProxMacFmt": tmnxWlanGwVlanRadProxMacFmt,
       "tmnxWlanGwVlanSsidType": tmnxWlanGwVlanSsidType,
       "tmnxWlanGwVlanAuthOnDhcp": tmnxWlanGwVlanAuthOnDhcp,
       "tmnxWlanGwVlanL2Service": tmnxWlanGwVlanL2Service,
       "tmnxWlanGwVlanL2AdminState": tmnxWlanGwVlanL2AdminState,
       "tmnxWlanGwVlanL2Description": tmnxWlanGwVlanL2Description,
       "tmnxWlanGwVlanIdleTimeoutAction": tmnxWlanGwVlanIdleTimeoutAction,
       "tmnxWlanGwVlanAddrFromPool": tmnxWlanGwVlanAddrFromPool,
       "tmnxWlanGwVlanAuthVlanMismatchTo": tmnxWlanGwVlanAuthVlanMismatchTo,
       "tmnxWlanGwSubIfTable": tmnxWlanGwSubIfTable,
       "tmnxWlanGwSubIfEntry": tmnxWlanGwSubIfEntry,
       "tmnxWlanGwSubIfRowStatus": tmnxWlanGwSubIfRowStatus,
       "tmnxWlanGwSubIfLastCh": tmnxWlanGwSubIfLastCh,
       "tmnxWlanGwSubIfRedExpPrefixType": tmnxWlanGwSubIfRedExpPrefixType,
       "tmnxWlanGwSubIfRedExpPrefix": tmnxWlanGwSubIfRedExpPrefix,
       "tmnxWlanGwSubIfRedExpPrefixLen": tmnxWlanGwSubIfRedExpPrefixLen,
       "tmnxWlanGwSubIfRedMonPrefixType": tmnxWlanGwSubIfRedMonPrefixType,
       "tmnxWlanGwSubIfRedMonPrefix": tmnxWlanGwSubIfRedMonPrefix,
       "tmnxWlanGwSubIfRedMonPrefixLen": tmnxWlanGwSubIfRedMonPrefixLen,
       "tmnxWlanGwSubIfRedAdminState": tmnxWlanGwSubIfRedAdminState,
       "tmnxWlanGwSubIfRedActive": tmnxWlanGwSubIfRedActive,
       "tmnxWlanGwSubIfRedSwitch": tmnxWlanGwSubIfRedSwitch,
       "tmnxWlanGwL2ApTable": tmnxWlanGwL2ApTable,
       "tmnxWlanGwL2ApEntry": tmnxWlanGwL2ApEntry,
       "tmnxWlanGwL2ApRowStatus": tmnxWlanGwL2ApRowStatus,
       "tmnxWlanGwL2ApLastCh": tmnxWlanGwL2ApLastCh,
       "tmnxWlanGwL2ApAdminState": tmnxWlanGwL2ApAdminState,
       "tmnxWlanGwL2ApEncapType": tmnxWlanGwL2ApEncapType,
       "tmnxWlanGwL2ApEpipeSapTemplate": tmnxWlanGwL2ApEpipeSapTemplate,
       "tmnxWlanGwL2ApId": tmnxWlanGwL2ApId,
       "tmnxWlanGwSubIfPmTable": tmnxWlanGwSubIfPmTable,
       "tmnxWlanGwSubIfPmEntry": tmnxWlanGwSubIfPmEntry,
       "tmnxWlanGwSubIfPmLastChanged": tmnxWlanGwSubIfPmLastChanged,
       "tmnxWlanGwSubIfPmWatermarkHigh": tmnxWlanGwSubIfPmWatermarkHigh,
       "tmnxWlanGwSubIfPmWatermarkLow": tmnxWlanGwSubIfPmWatermarkLow,
       "tmnxWlanGwSubIfPmWlanGwGroup": tmnxWlanGwSubIfPmWlanGwGroup,
       "tmnxWlanGwSubIfPmD6cServer1": tmnxWlanGwSubIfPmD6cServer1,
       "tmnxWlanGwSubIfPmD6cServer2": tmnxWlanGwSubIfPmD6cServer2,
       "tmnxWlanGwSubIfPmD6cServer3": tmnxWlanGwSubIfPmD6cServer3,
       "tmnxWlanGwSubIfPmD6cServer4": tmnxWlanGwSubIfPmD6cServer4,
       "tmnxWlanGwSubIfPmD6cServer5": tmnxWlanGwSubIfPmD6cServer5,
       "tmnxWlanGwSubIfPmD6cServer6": tmnxWlanGwSubIfPmD6cServer6,
       "tmnxWlanGwSubIfPmD6cServer7": tmnxWlanGwSubIfPmD6cServer7,
       "tmnxWlanGwSubIfPmD6cServer8": tmnxWlanGwSubIfPmD6cServer8,
       "tmnxWlanGwSubIfPmD6cLeaseQuery": tmnxWlanGwSubIfPmD6cLeaseQuery,
       "tmnxWlanGwSubIfPmD6cLeaseQueryMR": tmnxWlanGwSubIfPmD6cLeaseQueryMR,
       "tmnxWlanGwSubIfPmD6cSourceIp": tmnxWlanGwSubIfPmD6cSourceIp,
       "tmnxWlanGwSubIfPmD6cSlaacPoolNm": tmnxWlanGwSubIfPmD6cSlaacPoolNm,
       "tmnxWlanGwSubIfPmD6cSlaacLinkAdd": tmnxWlanGwSubIfPmD6cSlaacLinkAdd,
       "tmnxWlanGwSubIfPmD6cSlaacAdminSt": tmnxWlanGwSubIfPmD6cSlaacAdminSt,
       "tmnxWlanGwSubIfPmD6cIaNaPoolNm": tmnxWlanGwSubIfPmD6cIaNaPoolNm,
       "tmnxWlanGwSubIfPmD6cIaNaLinkAdd": tmnxWlanGwSubIfPmD6cIaNaLinkAdd,
       "tmnxWlanGwSubIfPmD6cIaNaAdminSt": tmnxWlanGwSubIfPmD6cIaNaAdminSt,
       "tmnxWlanGwSubIfPmD6cD4natPoolNm": tmnxWlanGwSubIfPmD6cD4natPoolNm,
       "tmnxWlanGwSubIfPmD6cD4natLinkAdd": tmnxWlanGwSubIfPmD6cD4natLinkAdd,
       "tmnxWlanGwSubIfPmD6cD4natAdminSt": tmnxWlanGwSubIfPmD6cD4natAdminSt,
       "tmnxWlanGwSubIfIpsTable": tmnxWlanGwSubIfIpsTable,
       "tmnxWlanGwSubIfIpsEntry": tmnxWlanGwSubIfIpsEntry,
       "tmnxWlanGwSubIfIpsSubIfIndex": tmnxWlanGwSubIfIpsSubIfIndex,
       "tmnxWlanGwSubIfIpsSubnetAddrType": tmnxWlanGwSubIfIpsSubnetAddrType,
       "tmnxWlanGwSubIfIpsSubnetAddr": tmnxWlanGwSubIfIpsSubnetAddr,
       "tmnxWlanGwSubIfIpsSubnetPrefLen": tmnxWlanGwSubIfIpsSubnetPrefLen,
       "tmnxWlanGwSubIfIpsAddrFamily": tmnxWlanGwSubIfIpsAddrFamily,
       "tmnxWlanGwSubIfIpsPoolIsOld": tmnxWlanGwSubIfIpsPoolIsOld,
       "tmnxWlanGwSubIfIpsUsageLevelPct": tmnxWlanGwSubIfIpsUsageLevelPct,
       "tmnxWlanGwSubIfIpsDHCPv6Options": tmnxWlanGwSubIfIpsDHCPv6Options,
       "tmnxWlanGwSubIfIpsRemLeaseTime": tmnxWlanGwSubIfIpsRemLeaseTime,
       "tmnxWlanGwSubIfIpsIsaGrpId": tmnxWlanGwSubIfIpsIsaGrpId,
       "tmnxWlanGwSubIfIpsIsaMemberId": tmnxWlanGwSubIfIpsIsaMemberId,
       "tmnxWlanGwSubIfIpsServiceId": tmnxWlanGwSubIfIpsServiceId,
       "tmnxWlanGwSubIfIpsIpv4Addr": tmnxWlanGwSubIfIpsIpv4Addr,
       "tmnxWlanGwSubIfIpsIpv4PrefLen": tmnxWlanGwSubIfIpsIpv4PrefLen,
       "tmnxWlanGwSubIfIpsIpv4DefGwAddr": tmnxWlanGwSubIfIpsIpv4DefGwAddr,
       "tmnxWlanGwSubIfIpsDnsServer1": tmnxWlanGwSubIfIpsDnsServer1,
       "tmnxWlanGwSubIfIpsDnsServer2": tmnxWlanGwSubIfIpsDnsServer2,
       "tmnxWlanGwTuQosOvrTable": tmnxWlanGwTuQosOvrTable,
       "tmnxWlanGwTuQosOvrEntry": tmnxWlanGwTuQosOvrEntry,
       "tmnxWlanGwTuQosOvrDirection": tmnxWlanGwTuQosOvrDirection,
       "tmnxWlanGwTuQosOvrType": tmnxWlanGwTuQosOvrType,
       "tmnxWlanGwTuQosOvrTypeName": tmnxWlanGwTuQosOvrTypeName,
       "tmnxWlanGwTuQosOvrPIR": tmnxWlanGwTuQosOvrPIR,
       "tmnxWlanGwTuQosOvrCIR": tmnxWlanGwTuQosOvrCIR,
       "tmnxWlanGwTuQosOvrAggRateLimit": tmnxWlanGwTuQosOvrAggRateLimit,
       "tmnxWlanGwGrpIfGwAddrTable": tmnxWlanGwGrpIfGwAddrTable,
       "tmnxWlanGwGrpIfGwAddrEntry": tmnxWlanGwGrpIfGwAddrEntry,
       "tmnxWlanGwGrpIfGwAddrType": tmnxWlanGwGrpIfGwAddrType,
       "tmnxWlanGwGrpIfGwAddr": tmnxWlanGwGrpIfGwAddr,
       "tmnxWlanGwGrpIfGwAddrRowStatus": tmnxWlanGwGrpIfGwAddrRowStatus,
       "tmnxWlanGwGrpIfGwAddrPurpose": tmnxWlanGwGrpIfGwAddrPurpose,
       "tmnxWlanGwIfRetailTable": tmnxWlanGwIfRetailTable,
       "tmnxWlanGwIfRetailEntry": tmnxWlanGwIfRetailEntry,
       "tmnxWlanGwIfRetailTagStart": tmnxWlanGwIfRetailTagStart,
       "tmnxWlanGwIfRetailTagEnd": tmnxWlanGwIfRetailTagEnd,
       "tmnxWlanGwIfRetailRowStatus": tmnxWlanGwIfRetailRowStatus,
       "tmnxWlanGwIfRetailLastCh": tmnxWlanGwIfRetailLastCh,
       "tmnxWlanGwIfRetailService": tmnxWlanGwIfRetailService,
       "tmnxWlanGwUeTable": tmnxWlanGwUeTable,
       "tmnxWlanGwUeEntry": tmnxWlanGwUeEntry,
       "tmnxWlanGwUeMacAddress": tmnxWlanGwUeMacAddress,
       "tmnxWlanGwUeQTag": tmnxWlanGwUeQTag,
       "tmnxWlanGwUeMplsLabel": tmnxWlanGwUeMplsLabel,
       "tmnxWlanGwUeTuRouter": tmnxWlanGwUeTuRouter,
       "tmnxWlanGwUeTuAddrType": tmnxWlanGwUeTuAddrType,
       "tmnxWlanGwUeTuRemoteAddr": tmnxWlanGwUeTuRemoteAddr,
       "tmnxWlanGwUeTuLocalAddr": tmnxWlanGwUeTuLocalAddr,
       "tmnxWlanGwUeTuQosRetailService": tmnxWlanGwUeTuQosRetailService,
       "tmnxWlanGwUeSsid": tmnxWlanGwUeSsid,
       "tmnxWlanGwUePrevApAddrType": tmnxWlanGwUePrevApAddrType,
       "tmnxWlanGwUePrevApAddr": tmnxWlanGwUePrevApAddr,
       "tmnxWlanGwUeLastMoveTime": tmnxWlanGwUeLastMoveTime,
       "tmnxWlanGwUeImsi": tmnxWlanGwUeImsi,
       "tmnxWlanGwUeService": tmnxWlanGwUeService,
       "tmnxWlanGwUeSapPortId": tmnxWlanGwUeSapPortId,
       "tmnxWlanGwUeSapPortEncapValue": tmnxWlanGwUeSapPortEncapValue,
       "tmnxWlanGwUeEncapsulation": tmnxWlanGwUeEncapsulation,
       "tmnxWlanGwSsidTable": tmnxWlanGwSsidTable,
       "tmnxWlanGwSsidEntry": tmnxWlanGwSsidEntry,
       "tmnxWlanGwSsid": tmnxWlanGwSsid,
       "tmnxWlanGwSsidNumUe": tmnxWlanGwSsidNumUe,
       "tmnxWlanGwMgwObjs": tmnxWlanGwMgwObjs,
       "tmnxWlanGwMgwProfTable": tmnxWlanGwMgwProfTable,
       "tmnxWlanGwMgwProfEntry": tmnxWlanGwMgwProfEntry,
       "tmnxWlanGwMgwProfName": tmnxWlanGwMgwProfName,
       "tmnxWlanGwMgwProfRowStatus": tmnxWlanGwMgwProfRowStatus,
       "tmnxWlanGwMgwProfLastChanged": tmnxWlanGwMgwProfLastChanged,
       "tmnxWlanGwMgwProfDescription": tmnxWlanGwMgwProfDescription,
       "tmnxWlanGwMgwProfMsgReTxTimeout": tmnxWlanGwMgwProfMsgReTxTimeout,
       "tmnxWlanGwMgwProfMsgReTxRetryCnt": tmnxWlanGwMgwProfMsgReTxRetryCnt,
       "tmnxWlanGwMgwProfKeepAlvTimeout": tmnxWlanGwMgwProfKeepAlvTimeout,
       "tmnxWlanGwMgwProfKeepAlvRetryCnt": tmnxWlanGwMgwProfKeepAlvRetryCnt,
       "tmnxWlanGwMgwProfKeepAlvResp": tmnxWlanGwMgwProfKeepAlvResp,
       "tmnxWlanGwMgwProfTtl": tmnxWlanGwMgwProfTtl,
       "tmnxWlanGwMgwProfInterfaceType": tmnxWlanGwMgwProfInterfaceType,
       "tmnxWlanGwMgwProfChrgCharHome": tmnxWlanGwMgwProfChrgCharHome,
       "tmnxWlanGwMgwProfChrgCharRoam": tmnxWlanGwMgwProfChrgCharRoam,
       "tmnxWlanGwMgwProfSeHoldTime": tmnxWlanGwMgwProfSeHoldTime,
       "tmnxWlanGwMgwProfReportWlanLoc": tmnxWlanGwMgwProfReportWlanLoc,
       "tmnxWlanGwMgwProfProtocolCfgOpt": tmnxWlanGwMgwProfProtocolCfgOpt,
       "tmnxWlanGwMgwProfPythonPolicy": tmnxWlanGwMgwProfPythonPolicy,
       "tmnxWlanGwMgwProfRatType": tmnxWlanGwMgwProfRatType,
       "tmnxWlanGwMgwProfIpv4Mtu": tmnxWlanGwMgwProfIpv4Mtu,
       "tmnxWlanGwMgwProfEndMarkerCount": tmnxWlanGwMgwProfEndMarkerCount,
       "tmnxWlanGwMgwProfChangeRepAction": tmnxWlanGwMgwProfChangeRepAction,
       "tmnxWlanGwMgwAddrTable": tmnxWlanGwMgwAddrTable,
       "tmnxWlanGwMgwAddrEntry": tmnxWlanGwMgwAddrEntry,
       "tmnxWlanGwMgwAddrType": tmnxWlanGwMgwAddrType,
       "tmnxWlanGwMgwAddr": tmnxWlanGwMgwAddr,
       "tmnxWlanGwMgwAddrPrefixLen": tmnxWlanGwMgwAddrPrefixLen,
       "tmnxWlanGwMgwAddrRowStatus": tmnxWlanGwMgwAddrRowStatus,
       "tmnxWlanGwMgwAddrLastMgmtChange": tmnxWlanGwMgwAddrLastMgmtChange,
       "tmnxWlanGwMgwAddrProfile": tmnxWlanGwMgwAddrProfile,
       "tmnxWlanGwMgwTable": tmnxWlanGwMgwTable,
       "tmnxWlanGwMgwEntry": tmnxWlanGwMgwEntry,
       "tmnxWlanGwMgwRemoteAddrType": tmnxWlanGwMgwRemoteAddrType,
       "tmnxWlanGwMgwRemoteAddr": tmnxWlanGwMgwRemoteAddr,
       "tmnxWlanGwMgwRemotePort": tmnxWlanGwMgwRemotePort,
       "tmnxWlanGwMgwLocalAddrType": tmnxWlanGwMgwLocalAddrType,
       "tmnxWlanGwMgwLocalAddr": tmnxWlanGwMgwLocalAddr,
       "tmnxWlanGwMgwTime": tmnxWlanGwMgwTime,
       "tmnxWlanGwMgwProfile": tmnxWlanGwMgwProfile,
       "tmnxWlanGwMgwControl": tmnxWlanGwMgwControl,
       "tmnxWlanGwMgwRestartCnt": tmnxWlanGwMgwRestartCnt,
       "tmnxWlanGwMgwState": tmnxWlanGwMgwState,
       "tmnxWlanGwMgwInterfaceType": tmnxWlanGwMgwInterfaceType,
       "tmnxWlanMgwStatsTable": tmnxWlanMgwStatsTable,
       "tmnxWlanMgwStatsEntry": tmnxWlanMgwStatsEntry,
       "tmnxWlanMgwStatsId": tmnxWlanMgwStatsId,
       "tmnxWlanMgwStatsName": tmnxWlanMgwStatsName,
       "tmnxWlanMgwStatsVal": tmnxWlanMgwStatsVal,
       "tmnxWlanMgwStatsValLw": tmnxWlanMgwStatsValLw,
       "tmnxWlanMgwStatsValHw": tmnxWlanMgwStatsValHw,
       "tmnxWlanGwGtpSeTable": tmnxWlanGwGtpSeTable,
       "tmnxWlanGwGtpSeEntry": tmnxWlanGwGtpSeEntry,
       "tmnxWlanGwGtpSeImsi": tmnxWlanGwGtpSeImsi,
       "tmnxWlanGwGtpSeApn": tmnxWlanGwGtpSeApn,
       "tmnxWlanGwGtpSeMgwRouter": tmnxWlanGwGtpSeMgwRouter,
       "tmnxWlanGwGtpSeMgwAddrType": tmnxWlanGwGtpSeMgwAddrType,
       "tmnxWlanGwGtpSeMgwAddr": tmnxWlanGwGtpSeMgwAddr,
       "tmnxWlanGwGtpSeRemoteCtrlTeid": tmnxWlanGwGtpSeRemoteCtrlTeid,
       "tmnxWlanGwGtpSeLocalCtrlTeid": tmnxWlanGwGtpSeLocalCtrlTeid,
       "tmnxWlanGwGtpSeChrgChar": tmnxWlanGwGtpSeChrgChar,
       "tmnxWlanGwGtpSeQosUplinkAmbr": tmnxWlanGwGtpSeQosUplinkAmbr,
       "tmnxWlanGwGtpSeQosDwnlinkAmbr": tmnxWlanGwGtpSeQosDwnlinkAmbr,
       "tmnxWlanGwBcTable": tmnxWlanGwBcTable,
       "tmnxWlanGwBcEntry": tmnxWlanGwBcEntry,
       "tmnxWlanGwBcId": tmnxWlanGwBcId,
       "tmnxWlanGwBcRemoteTeid": tmnxWlanGwBcRemoteTeid,
       "tmnxWlanGwBcLocalTeid": tmnxWlanGwBcLocalTeid,
       "tmnxWlanGwBcQosUlGbr": tmnxWlanGwBcQosUlGbr,
       "tmnxWlanGwBcQosUlMbr": tmnxWlanGwBcQosUlMbr,
       "tmnxWlanGwBcQosDlGbr": tmnxWlanGwBcQosDlGbr,
       "tmnxWlanGwBcQosDlMbr": tmnxWlanGwBcQosDlMbr,
       "tmnxWlanGwBcQosQci": tmnxWlanGwBcQosQci,
       "tmnxWlanGwBcQosArp": tmnxWlanGwBcQosArp,
       "tmnxWlanGwMgwCacheTable": tmnxWlanGwMgwCacheTable,
       "tmnxWlanGwMgwCacheEntry": tmnxWlanGwMgwCacheEntry,
       "tmnxWlanGwMgwCacheApn": tmnxWlanGwMgwCacheApn,
       "tmnxWlanGwMgwCacheAddrType": tmnxWlanGwMgwCacheAddrType,
       "tmnxWlanGwMgwCacheAddr": tmnxWlanGwMgwCacheAddr,
       "tmnxWlanGwMgwCacheTtl": tmnxWlanGwMgwCacheTtl,
       "tmnxWlanGwGtpStatsTable": tmnxWlanGwGtpStatsTable,
       "tmnxWlanGwGtpStatsEntry": tmnxWlanGwGtpStatsEntry,
       "tmnxWlanGwGtpStatsId": tmnxWlanGwGtpStatsId,
       "tmnxWlanGwGtpStatsName": tmnxWlanGwGtpStatsName,
       "tmnxWlanGwGtpStatsVal": tmnxWlanGwGtpStatsVal,
       "tmnxWlanGwGtpStatsValLw": tmnxWlanGwGtpStatsValLw,
       "tmnxWlanGwGtpStatsValHw": tmnxWlanGwGtpStatsValHw,
       "tmnxWlanGwMgwArecCacheTable": tmnxWlanGwMgwArecCacheTable,
       "tmnxWlanGwMgwArecCacheEntry": tmnxWlanGwMgwArecCacheEntry,
       "tmnxWlanGwMgwArecCacheApn": tmnxWlanGwMgwArecCacheApn,
       "tmnxWlanGwMgwArecCacheIndex": tmnxWlanGwMgwArecCacheIndex,
       "tmnxWlanGwMgwArecCacheAddrType": tmnxWlanGwMgwArecCacheAddrType,
       "tmnxWlanGwMgwArecCacheAddr": tmnxWlanGwMgwArecCacheAddr,
       "tmnxWlanGwMgwArecCacheTtl": tmnxWlanGwMgwArecCacheTtl,
       "tmnxWlanGwMgwSnaptrCacheTable": tmnxWlanGwMgwSnaptrCacheTable,
       "tmnxWlanGwMgwSnaptrCacheEntry": tmnxWlanGwMgwSnaptrCacheEntry,
       "tmnxWlanGwMgwSnaptrCacheApn": tmnxWlanGwMgwSnaptrCacheApn,
       "tmnxWlanGwMgwSnaptrCacheOrder": tmnxWlanGwMgwSnaptrCacheOrder,
       "tmnxWlanGwMgwSnaptrCacheIndex": tmnxWlanGwMgwSnaptrCacheIndex,
       "tmnxWlanGwMgwSnaptrCachePref": tmnxWlanGwMgwSnaptrCachePref,
       "tmnxWlanGwMgwSnaptrCacheService": tmnxWlanGwMgwSnaptrCacheService,
       "tmnxWlanGwMgwSnaptrCacheNext": tmnxWlanGwMgwSnaptrCacheNext,
       "tmnxWlanGwMgwSnaptrCacheRepl": tmnxWlanGwMgwSnaptrCacheRepl,
       "tmnxWlanGwMgwSnaptrCacheTtl": tmnxWlanGwMgwSnaptrCacheTtl,
       "tmnxWlanGwMgwSrvCacheTable": tmnxWlanGwMgwSrvCacheTable,
       "tmnxWlanGwMgwSrvCacheEntry": tmnxWlanGwMgwSrvCacheEntry,
       "tmnxWlanGwMgwSrvCacheApn": tmnxWlanGwMgwSrvCacheApn,
       "tmnxWlanGwMgwSrvCachePriority": tmnxWlanGwMgwSrvCachePriority,
       "tmnxWlanGwMgwSrvCacheIndex": tmnxWlanGwMgwSrvCacheIndex,
       "tmnxWlanGwMgwSrvCacheWeight": tmnxWlanGwMgwSrvCacheWeight,
       "tmnxWlanGwMgwSrvCachePort": tmnxWlanGwMgwSrvCachePort,
       "tmnxWlanGwMgwSrvCacheTarget": tmnxWlanGwMgwSrvCacheTarget,
       "tmnxWlanGwMgwSrvCacheTtl": tmnxWlanGwMgwSrvCacheTtl,
       "tmnxWlanGwPgwTable": tmnxWlanGwPgwTable,
       "tmnxWlanGwPgwEntry": tmnxWlanGwPgwEntry,
       "tmnxWlanGwPgwLastChanged": tmnxWlanGwPgwLastChanged,
       "tmnxWlanGwPgwQosUplinkGbrRate": tmnxWlanGwPgwQosUplinkGbrRate,
       "tmnxWlanGwPgwQosUplinkMbrRate": tmnxWlanGwPgwQosUplinkMbrRate,
       "tmnxWlanGwPgwQosDwnlinkGbrRate": tmnxWlanGwPgwQosDwnlinkGbrRate,
       "tmnxWlanGwPgwQosDwnlinkMbrRate": tmnxWlanGwPgwQosDwnlinkMbrRate,
       "tmnxWlanGwPgwQosArpValue": tmnxWlanGwPgwQosArpValue,
       "tmnxWlanGwPgwQosQciValue": tmnxWlanGwPgwQosQciValue,
       "tmnxWlanGwPgwQosUplinkAmbr": tmnxWlanGwPgwQosUplinkAmbr,
       "tmnxWlanGwPgwQosDwnlinkAmbr": tmnxWlanGwPgwQosDwnlinkAmbr,
       "tmnxWlanGwGgsnTable": tmnxWlanGwGgsnTable,
       "tmnxWlanGwGgsnEntry": tmnxWlanGwGgsnEntry,
       "tmnxWlanGwGgsnLastChanged": tmnxWlanGwGgsnLastChanged,
       "tmnxWlanGwGgsnQosUplinkGbrRate": tmnxWlanGwGgsnQosUplinkGbrRate,
       "tmnxWlanGwGgsnQosUplinkMbrRate": tmnxWlanGwGgsnQosUplinkMbrRate,
       "tmnxWlanGwGgsnQosDwnlinkGbrRate": tmnxWlanGwGgsnQosDwnlinkGbrRate,
       "tmnxWlanGwGgsnQosDwnlinkMbrRate": tmnxWlanGwGgsnQosDwnlinkMbrRate,
       "tmnxWlanGwGgsnQosArpValue": tmnxWlanGwGgsnQosArpValue,
       "tmnxWlanGwGgsnQosUplinkAmbr": tmnxWlanGwGgsnQosUplinkAmbr,
       "tmnxWlanGwGgsnQosDwnlinkAmbr": tmnxWlanGwGgsnQosDwnlinkAmbr,
       "tmnxWlanGwMmeTable": tmnxWlanGwMmeTable,
       "tmnxWlanGwMmeEntry": tmnxWlanGwMmeEntry,
       "tmnxWlanGwMmeLastChanged": tmnxWlanGwMmeLastChanged,
       "tmnxWlanGwMmeQosUplinkGbrRate": tmnxWlanGwMmeQosUplinkGbrRate,
       "tmnxWlanGwMmeQosUplinkMbrRate": tmnxWlanGwMmeQosUplinkMbrRate,
       "tmnxWlanGwMmeQosDwnlinkGbrRate": tmnxWlanGwMmeQosDwnlinkGbrRate,
       "tmnxWlanGwMmeQosDwnlinkMbrRate": tmnxWlanGwMmeQosDwnlinkMbrRate,
       "tmnxWlanGwMmeQosArpValue": tmnxWlanGwMmeQosArpValue,
       "tmnxWlanGwMmeQosQciValue": tmnxWlanGwMmeQosQciValue,
       "tmnxWlanGwMmeQosUplinkAmbr": tmnxWlanGwMmeQosUplinkAmbr,
       "tmnxWlanGwMmeQosDwnlinkAmbr": tmnxWlanGwMmeQosDwnlinkAmbr,
       "tmnxWlanGwSysCfgObjs": tmnxWlanGwSysCfgObjs,
       "tmnxWlanGwSysCfgServingNwMcc": tmnxWlanGwSysCfgServingNwMcc,
       "tmnxWlanGwSysCfgServingNwMnc": tmnxWlanGwSysCfgServingNwMnc,
       "tmnxWlanGwSysCfgMgwMaxHeldSe": tmnxWlanGwSysCfgMgwMaxHeldSe,
       "tmnxWlanGwSysCfgVirtChassisId": tmnxWlanGwSysCfgVirtChassisId,
       "tmnxWlanGwTable": tmnxWlanGwTable,
       "tmnxWlanGwEntry": tmnxWlanGwEntry,
       "tmnxWlanGwRowStatus": tmnxWlanGwRowStatus,
       "tmnxWlanGwLastCh": tmnxWlanGwLastCh,
       "tmnxWlanGwApn": tmnxWlanGwApn,
       "tmnxWlanGwMobAcctInterimUpdate": tmnxWlanGwMobAcctInterimUpdate,
       "tmnxWlanGwPdnType": tmnxWlanGwPdnType,
       "tmnxWlanGwMobAcctIntUpdtInclCnts": tmnxWlanGwMobAcctIntUpdtInclCnts,
       "tmnxWlanGwMobAcctIntUpdtHoldDown": tmnxWlanGwMobAcctIntUpdtHoldDown,
       "tmnxWlanGwDsmSubObjs": tmnxWlanGwDsmSubObjs,
       "tmnxWlanGwVlanDsmTable": tmnxWlanGwVlanDsmTable,
       "tmnxWlanGwVlanDsmEntry": tmnxWlanGwVlanDsmEntry,
       "tmnxWlanGwVlanDsmLastCh": tmnxWlanGwVlanDsmLastCh,
       "tmnxWlanGwVlanDsmAdminState": tmnxWlanGwVlanDsmAdminState,
       "tmnxWlanGwVlanDsmAcctPlcy": tmnxWlanGwVlanDsmAcctPlcy,
       "tmnxWlanGwVlanDsmEgressPolicer": tmnxWlanGwVlanDsmEgressPolicer,
       "tmnxWlanGwVlanDsmIngressPolicer": tmnxWlanGwVlanDsmIngressPolicer,
       "tmnxWlanGwVlanDsmIpFilter": tmnxWlanGwVlanDsmIpFilter,
       "tmnxWlanGwVlanDsmOneTimeRdrUrl": tmnxWlanGwVlanDsmOneTimeRdrUrl,
       "tmnxWlanGwVlanDsmOneTimeRdrPort": tmnxWlanGwVlanDsmOneTimeRdrPort,
       "tmnxWlanGwVlanDsmAcctUpdInterv": tmnxWlanGwVlanDsmAcctUpdInterv,
       "tmnxWlanGwVlanDsmDefAppProfile": tmnxWlanGwVlanDsmDefAppProfile,
       "tmnxWlanGwVlanDsmAaAcctStats": tmnxWlanGwVlanDsmAaAcctStats,
       "tmnxWlanGwDsmIpFilTable": tmnxWlanGwDsmIpFilTable,
       "tmnxWlanGwDsmIpFilEntry": tmnxWlanGwDsmIpFilEntry,
       "tmnxWlanGwDsmIpFilName": tmnxWlanGwDsmIpFilName,
       "tmnxWlanGwDsmIpFilRowStatus": tmnxWlanGwDsmIpFilRowStatus,
       "tmnxWlanGwDsmIpFilLastCh": tmnxWlanGwDsmIpFilLastCh,
       "tmnxWlanGwDsmIpFilDescription": tmnxWlanGwDsmIpFilDescription,
       "tmnxWlanGwDsmIpFilDefaultAction": tmnxWlanGwDsmIpFilDefaultAction,
       "tmnxWlanGwDsmIpFilDefaultAction6": tmnxWlanGwDsmIpFilDefaultAction6,
       "tmnxWlanGwDsmIpFilType": tmnxWlanGwDsmIpFilType,
       "tmnxWlanGwDsmIpFilN3Table": tmnxWlanGwDsmIpFilN3Table,
       "tmnxWlanGwDsmIpFilN3Entry": tmnxWlanGwDsmIpFilN3Entry,
       "tmnxWlanGwDsmIpFilN3Index": tmnxWlanGwDsmIpFilN3Index,
       "tmnxWlanGwDsmIpFilN3RowStatus": tmnxWlanGwDsmIpFilN3RowStatus,
       "tmnxWlanGwDsmIpFilN3LastCh": tmnxWlanGwDsmIpFilN3LastCh,
       "tmnxWlanGwDsmIpFilN3Description": tmnxWlanGwDsmIpFilN3Description,
       "tmnxWlanGwDsmIpFilN3Action": tmnxWlanGwDsmIpFilN3Action,
       "tmnxWlanGwDsmIpFilN3Protocol": tmnxWlanGwDsmIpFilN3Protocol,
       "tmnxWlanGwDsmIpFilN3DestAddrType": tmnxWlanGwDsmIpFilN3DestAddrType,
       "tmnxWlanGwDsmIpFilN3DestAddr": tmnxWlanGwDsmIpFilN3DestAddr,
       "tmnxWlanGwDsmIpFilN3DestPrefLen": tmnxWlanGwDsmIpFilN3DestPrefLen,
       "tmnxWlanGwDsmIpFilN3DestPortOp": tmnxWlanGwDsmIpFilN3DestPortOp,
       "tmnxWlanGwDsmIpFilN3DestPort1": tmnxWlanGwDsmIpFilN3DestPort1,
       "tmnxWlanGwDsmIpFilN3IngHitCount": tmnxWlanGwDsmIpFilN3IngHitCount,
       "tmnxWlanGwDsmIpFilN3RedirectURL": tmnxWlanGwDsmIpFilN3RedirectURL,
       "tmnxWlanGwPolicerTable": tmnxWlanGwPolicerTable,
       "tmnxWlanGwPolicerEntry": tmnxWlanGwPolicerEntry,
       "tmnxWlanGwPolicerName": tmnxWlanGwPolicerName,
       "tmnxWlanGwPolicerRowLastChange": tmnxWlanGwPolicerRowLastChange,
       "tmnxWlanGwPolicerRowStatus": tmnxWlanGwPolicerRowStatus,
       "tmnxWlanGwPolicerDescription": tmnxWlanGwPolicerDescription,
       "tmnxWlanGwPolicerType": tmnxWlanGwPolicerType,
       "tmnxWlanGwPolicerAction": tmnxWlanGwPolicerAction,
       "tmnxWlanGwPolicerAdminPIR": tmnxWlanGwPolicerAdminPIR,
       "tmnxWlanGwPolicerAdminCIR": tmnxWlanGwPolicerAdminCIR,
       "tmnxWlanGwPolicerMBS": tmnxWlanGwPolicerMBS,
       "tmnxWlanGwPolicerCBS": tmnxWlanGwPolicerCBS,
       "tmnxWlanGwPolicerPIRAdaptation": tmnxWlanGwPolicerPIRAdaptation,
       "tmnxWlanGwPolicerCIRAdaptation": tmnxWlanGwPolicerCIRAdaptation,
       "tmnxWlanGwDsmIpFil6N3Table": tmnxWlanGwDsmIpFil6N3Table,
       "tmnxWlanGwDsmIpFil6N3Entry": tmnxWlanGwDsmIpFil6N3Entry,
       "tmnxWlanGwDsmIpFil6N3Index": tmnxWlanGwDsmIpFil6N3Index,
       "tmnxWlanGwDsmIpFil6N3RowStatus": tmnxWlanGwDsmIpFil6N3RowStatus,
       "tmnxWlanGwDsmIpFil6N3LastCh": tmnxWlanGwDsmIpFil6N3LastCh,
       "tmnxWlanGwDsmIpFil6N3Description": tmnxWlanGwDsmIpFil6N3Description,
       "tmnxWlanGwDsmIpFil6N3Action": tmnxWlanGwDsmIpFil6N3Action,
       "tmnxWlanGwDsmIpFil6N3Protocol": tmnxWlanGwDsmIpFil6N3Protocol,
       "tmnxWlanGwDsmIpFil6N3DestAddrTyp": tmnxWlanGwDsmIpFil6N3DestAddrTyp,
       "tmnxWlanGwDsmIpFil6N3DestAddr": tmnxWlanGwDsmIpFil6N3DestAddr,
       "tmnxWlanGwDsmIpFil6N3DestPrefLen": tmnxWlanGwDsmIpFil6N3DestPrefLen,
       "tmnxWlanGwDsmIpFil6N3DestPortOp": tmnxWlanGwDsmIpFil6N3DestPortOp,
       "tmnxWlanGwDsmIpFil6N3DestPort1": tmnxWlanGwDsmIpFil6N3DestPort1,
       "tmnxWlanGwDsmIpFil6N3IngHitCount": tmnxWlanGwDsmIpFil6N3IngHitCount,
       "tmnxWlanGwDsmIpFil6N3RedirectURL": tmnxWlanGwDsmIpFil6N3RedirectURL,
       "tmnxWlanGwDsmTable": tmnxWlanGwDsmTable,
       "tmnxWlanGwDsmEntry": tmnxWlanGwDsmEntry,
       "tmnxWlanGwDsmLastCh": tmnxWlanGwDsmLastCh,
       "tmnxWlanGwDsmIpv6TcpMssAdjust": tmnxWlanGwDsmIpv6TcpMssAdjust,
       "tmnxWlanGwGtpIsaObjs": tmnxWlanGwGtpIsaObjs,
       "tmnxWlanGwUeObjs": tmnxWlanGwUeObjs,
       "tmnxWlanGwUeNextQryId": tmnxWlanGwUeNextQryId,
       "tmnxWlanGwUeMaxQryId": tmnxWlanGwUeMaxQryId,
       "tmnxWlanGwUeQryTable": tmnxWlanGwUeQryTable,
       "tmnxWlanGwUeQryEntry": tmnxWlanGwUeQryEntry,
       "tmnxWlanGwUeQryId": tmnxWlanGwUeQryId,
       "tmnxWlanGwUeQryRowStatus": tmnxWlanGwUeQryRowStatus,
       "tmnxWlanGwUeQryWhereState": tmnxWlanGwUeQryWhereState,
       "tmnxWlanGwUeQryWhereMacAddress": tmnxWlanGwUeQryWhereMacAddress,
       "tmnxWlanGwUeQryWhereAddrType": tmnxWlanGwUeQryWhereAddrType,
       "tmnxWlanGwUeQryWhereAddr": tmnxWlanGwUeQryWhereAddr,
       "tmnxWlanGwUeQryWhereIsaGrp": tmnxWlanGwUeQryWhereIsaGrp,
       "tmnxWlanGwUeQryWhereMemberId": tmnxWlanGwUeQryWhereMemberId,
       "tmnxWlanGwUeQryWhereQTag": tmnxWlanGwUeQryWhereQTag,
       "tmnxWlanGwUeQryWhereTuRouter": tmnxWlanGwUeQryWhereTuRouter,
       "tmnxWlanGwUeQryWhereTuRemAddrTyp": tmnxWlanGwUeQryWhereTuRemAddrTyp,
       "tmnxWlanGwUeQryWhereTuRemAddr": tmnxWlanGwUeQryWhereTuRemAddr,
       "tmnxWlanGwUeQryWhereTuLocAddrTyp": tmnxWlanGwUeQryWhereTuLocAddrTyp,
       "tmnxWlanGwUeQryWhereTuLocAddr": tmnxWlanGwUeQryWhereTuLocAddr,
       "tmnxWlanGwUeQryWhereEncap": tmnxWlanGwUeQryWhereEncap,
       "tmnxWlanGwUeQryWhereSlaacPrefTyp": tmnxWlanGwUeQryWhereSlaacPrefTyp,
       "tmnxWlanGwUeQryWhereSlaacPref": tmnxWlanGwUeQryWhereSlaacPref,
       "tmnxWlanGwUeQryWhereDhcp6AddrTyp": tmnxWlanGwUeQryWhereDhcp6AddrTyp,
       "tmnxWlanGwUeQryWhereDhcp6Addr": tmnxWlanGwUeQryWhereDhcp6Addr,
       "tmnxWlanGwUeQryWhereBridgeId": tmnxWlanGwUeQryWhereBridgeId,
       "tmnxWlanGwUeQryWhereAddrFamily": tmnxWlanGwUeQryWhereAddrFamily,
       "tmnxWlanGwUeQryName": tmnxWlanGwUeQryName,
       "tmnxWlanGwUeQryNumResults": tmnxWlanGwUeQryNumResults,
       "tmnxWlanGwUeResTable": tmnxWlanGwUeResTable,
       "tmnxWlanGwUeResEntry": tmnxWlanGwUeResEntry,
       "tmnxWlanGwUeResId": tmnxWlanGwUeResId,
       "tmnxWlanGwUeResMacAddress": tmnxWlanGwUeResMacAddress,
       "tmnxWlanGwUeResQTag": tmnxWlanGwUeResQTag,
       "tmnxWlanGwUeResAddrType": tmnxWlanGwUeResAddrType,
       "tmnxWlanGwUeResAddr": tmnxWlanGwUeResAddr,
       "tmnxWlanGwUeResState": tmnxWlanGwUeResState,
       "tmnxWlanGwUeResIsaGrp": tmnxWlanGwUeResIsaGrp,
       "tmnxWlanGwUeResIsaMemberId": tmnxWlanGwUeResIsaMemberId,
       "tmnxWlanGwUeResTuRouter": tmnxWlanGwUeResTuRouter,
       "tmnxWlanGwUeResTuAddrType": tmnxWlanGwUeResTuAddrType,
       "tmnxWlanGwUeResTuRemoteAddr": tmnxWlanGwUeResTuRemoteAddr,
       "tmnxWlanGwUeResTuLocalAddr": tmnxWlanGwUeResTuLocalAddr,
       "tmnxWlanGwUeResEncapsulation": tmnxWlanGwUeResEncapsulation,
       "tmnxWlanGwUeResApMacAddress": tmnxWlanGwUeResApMacAddress,
       "tmnxWlanGwUeResSsid": tmnxWlanGwUeResSsid,
       "tmnxWlanGwUeResMplsLabel": tmnxWlanGwUeResMplsLabel,
       "tmnxWlanGwUeResLastMoveTime": tmnxWlanGwUeResLastMoveTime,
       "tmnxWlanGwUeResExpirationTime": tmnxWlanGwUeResExpirationTime,
       "tmnxWlanGwUeResIdleTimeout": tmnxWlanGwUeResIdleTimeout,
       "tmnxWlanGwUeResSessionTimeout": tmnxWlanGwUeResSessionTimeout,
       "tmnxWlanGwUeResNatPlcy": tmnxWlanGwUeResNatPlcy,
       "tmnxWlanGwUeResHttpRdrPlcy": tmnxWlanGwUeResHttpRdrPlcy,
       "tmnxWlanGwUeResDsmIpFilter": tmnxWlanGwUeResDsmIpFilter,
       "tmnxWlanGwUeResDsmAcctPlcy": tmnxWlanGwUeResDsmAcctPlcy,
       "tmnxWlanGwUeResDsmAcctUpdInterv": tmnxWlanGwUeResDsmAcctUpdInterv,
       "tmnxWlanGwUeResAcctUpdate": tmnxWlanGwUeResAcctUpdate,
       "tmnxWlanGwUeResIngOperPir": tmnxWlanGwUeResIngOperPir,
       "tmnxWlanGwUeResIngOperCir": tmnxWlanGwUeResIngOperCir,
       "tmnxWlanGwUeResEgrOperPir": tmnxWlanGwUeResEgrOperPir,
       "tmnxWlanGwUeResEgrOperCir": tmnxWlanGwUeResEgrOperCir,
       "tmnxWlanGwUeResDsmAppProfile": tmnxWlanGwUeResDsmAppProfile,
       "tmnxWlanGwUeResRxPkts": tmnxWlanGwUeResRxPkts,
       "tmnxWlanGwUeResRxOctets": tmnxWlanGwUeResRxOctets,
       "tmnxWlanGwUeResTxPkts": tmnxWlanGwUeResTxPkts,
       "tmnxWlanGwUeResTxOctets": tmnxWlanGwUeResTxOctets,
       "tmnxWlanGwUeResSlaacAddrType": tmnxWlanGwUeResSlaacAddrType,
       "tmnxWlanGwUeResSlaacPref": tmnxWlanGwUeResSlaacPref,
       "tmnxWlanGwUeResSlaacAddr1": tmnxWlanGwUeResSlaacAddr1,
       "tmnxWlanGwUeResSlaacAddr2": tmnxWlanGwUeResSlaacAddr2,
       "tmnxWlanGwUeResSlaacAddr3": tmnxWlanGwUeResSlaacAddr3,
       "tmnxWlanGwUeResDhcp6AddrType": tmnxWlanGwUeResDhcp6AddrType,
       "tmnxWlanGwUeResDhcp6Addr": tmnxWlanGwUeResDhcp6Addr,
       "tmnxWlanGwUeResDhcp6AddrDepr": tmnxWlanGwUeResDhcp6AddrDepr,
       "tmnxWlanGwUeResDhcp6IAID": tmnxWlanGwUeResDhcp6IAID,
       "tmnxWlanGwUeResDhcp6IAIDValid": tmnxWlanGwUeResDhcp6IAIDValid,
       "tmnxWlanGwUeResSlaacLeaseExpire": tmnxWlanGwUeResSlaacLeaseExpire,
       "tmnxWlanGwUeResDhcp6LeaseExpire": tmnxWlanGwUeResDhcp6LeaseExpire,
       "tmnxWlanGwUeResDhcpAddrDepr": tmnxWlanGwUeResDhcpAddrDepr,
       "tmnxWlanGwUeResBridgeId": tmnxWlanGwUeResBridgeId,
       "tmnxWlanGwUeResAddrFamily": tmnxWlanGwUeResAddrFamily,
       "tmnxWlanGwVplsTable": tmnxWlanGwVplsTable,
       "tmnxWlanGwVplsEntry": tmnxWlanGwVplsEntry,
       "tmnxWlanGwVplsLastMgmtChange": tmnxWlanGwVplsLastMgmtChange,
       "tmnxWlanGwVplsAdminState": tmnxWlanGwVplsAdminState,
       "tmnxWlanGwVplsDescription": tmnxWlanGwVplsDescription,
       "tmnxWlanGwVplsSapTemplate": tmnxWlanGwVplsSapTemplate,
       "tmnxWlanGwVlanSubObjs": tmnxWlanGwVlanSubObjs,
       "tmnxWlanGwVlanDhcp6Table": tmnxWlanGwVlanDhcp6Table,
       "tmnxWlanGwVlanDhcp6Entry": tmnxWlanGwVlanDhcp6Entry,
       "tmnxWlanGwVlanDhcp6LastChanged": tmnxWlanGwVlanDhcp6LastChanged,
       "tmnxWlanGwVlanDhcp6InitPrefLt": tmnxWlanGwVlanDhcp6InitPrefLt,
       "tmnxWlanGwVlanDhcp6ActPrefLt": tmnxWlanGwVlanDhcp6ActPrefLt,
       "tmnxWlanGwVlanDhcp6InitValidLt": tmnxWlanGwVlanDhcp6InitValidLt,
       "tmnxWlanGwVlanDhcp6ActValidLt": tmnxWlanGwVlanDhcp6ActValidLt,
       "tmnxWlanGwVlanDhcp6AdminState": tmnxWlanGwVlanDhcp6AdminState,
       "tmnxWlanGwVlanSlaacTable": tmnxWlanGwVlanSlaacTable,
       "tmnxWlanGwVlanSlaacEntry": tmnxWlanGwVlanSlaacEntry,
       "tmnxWlanGwVlanSlaacLastChanged": tmnxWlanGwVlanSlaacLastChanged,
       "tmnxWlanGwVlanSlaacInitPrefLt": tmnxWlanGwVlanSlaacInitPrefLt,
       "tmnxWlanGwVlanSlaacActPrefLt": tmnxWlanGwVlanSlaacActPrefLt,
       "tmnxWlanGwVlanSlaacInitValidLt": tmnxWlanGwVlanSlaacInitValidLt,
       "tmnxWlanGwVlanSlaacActValidLt": tmnxWlanGwVlanSlaacActValidLt,
       "tmnxWlanGwVlanSlaacAdminState": tmnxWlanGwVlanSlaacAdminState,
       "tmnxWlanGwVlanBrgTable": tmnxWlanGwVlanBrgTable,
       "tmnxWlanGwVlanBrgEntry": tmnxWlanGwVlanBrgEntry,
       "tmnxWlanGwVlanBrgLastChanged": tmnxWlanGwVlanBrgLastChanged,
       "tmnxWlanGwVlanBrgAdminState": tmnxWlanGwVlanBrgAdminState,
       "tmnxWlanGwVlanBrgDefBrgProfile": tmnxWlanGwVlanBrgDefBrgProfile,
       "tmnxWlanGwVlanBrgAuthedBrgOnly": tmnxWlanGwVlanBrgAuthedBrgOnly,
       "tmnxWlanGwVlanLeTable": tmnxWlanGwVlanLeTable,
       "tmnxWlanGwVlanLeEntry": tmnxWlanGwVlanLeEntry,
       "tmnxWlanGwVlanLeLastChanged": tmnxWlanGwVlanLeLastChanged,
       "tmnxWlanGwVlanLeAdminState": tmnxWlanGwVlanLeAdminState,
       "tmnxWlanGwVlanLeMacTranslation": tmnxWlanGwVlanLeMacTranslation,
       "tmnxWlanGwVlanLeBdMacPrefix": tmnxWlanGwVlanLeBdMacPrefix,
       "tmnxWlanGwVlanLeBdMacPrefixLen": tmnxWlanGwVlanLeBdMacPrefixLen,
       "tmnxWlanGwVlanLeAssistAddrRes": tmnxWlanGwVlanLeAssistAddrRes,
       "tmnxWlanGwVlanLeNetwPolicer": tmnxWlanGwVlanLeNetwPolicer,
       "tmnxWlanGwVlanLeNetwMaxMac": tmnxWlanGwVlanLeNetwMaxMac,
       "tmnxWlanGwVlanLeNetwAdminState": tmnxWlanGwVlanLeNetwAdminState,
       "tmnxWlanGwVlanLeAccsPolicer": tmnxWlanGwVlanLeAccsPolicer,
       "tmnxWlanGwVlanLeAccsMaxMac": tmnxWlanGwVlanLeAccsMaxMac,
       "tmnxWlanGwVlanLeAccsMultiAccess": tmnxWlanGwVlanLeAccsMultiAccess,
       "tmnxWlanGwTuObjs": tmnxWlanGwTuObjs,
       "tmnxWlanGwTuNextQryId": tmnxWlanGwTuNextQryId,
       "tmnxWlanGwTuMaxQryId": tmnxWlanGwTuMaxQryId,
       "tmnxWlanGwTuQryTable": tmnxWlanGwTuQryTable,
       "tmnxWlanGwTuQryEntry": tmnxWlanGwTuQryEntry,
       "tmnxWlanGwTuQryId": tmnxWlanGwTuQryId,
       "tmnxWlanGwTuQryRowStatus": tmnxWlanGwTuQryRowStatus,
       "tmnxWlanGwTuQryWhereTuRouter": tmnxWlanGwTuQryWhereTuRouter,
       "tmnxWlanGwTuQryWhereRemAddrType": tmnxWlanGwTuQryWhereRemAddrType,
       "tmnxWlanGwTuQryWhereRemAddr": tmnxWlanGwTuQryWhereRemAddr,
       "tmnxWlanGwTuQryWhereLocAddrType": tmnxWlanGwTuQryWhereLocAddrType,
       "tmnxWlanGwTuQryWhereLocAddr": tmnxWlanGwTuQryWhereLocAddr,
       "tmnxWlanGwTuQryWhereAddrFamily": tmnxWlanGwTuQryWhereAddrFamily,
       "tmnxWlanGwTuQryWhereEncap": tmnxWlanGwTuQryWhereEncap,
       "tmnxWlanGwTuQryWhereEncapTag1": tmnxWlanGwTuQryWhereEncapTag1,
       "tmnxWlanGwTuQryWhereEncapTag2": tmnxWlanGwTuQryWhereEncapTag2,
       "tmnxWlanGwTuQryWhereApSapPortId": tmnxWlanGwTuQryWhereApSapPortId,
       "tmnxWlanGwTuQryWhereApSapEncap": tmnxWlanGwTuQryWhereApSapEncap,
       "tmnxWlanGwTuQryWhereNumUeMin": tmnxWlanGwTuQryWhereNumUeMin,
       "tmnxWlanGwTuQryWhereNumUeMax": tmnxWlanGwTuQryWhereNumUeMax,
       "tmnxWlanGwTuQryWhereApLearnFail": tmnxWlanGwTuQryWhereApLearnFail,
       "tmnxWlanGwTuQryWhereUeType": tmnxWlanGwTuQryWhereUeType,
       "tmnxWlanGwTuQryDoGetNumResults": tmnxWlanGwTuQryDoGetNumResults,
       "tmnxWlanGwTuQryNumResults": tmnxWlanGwTuQryNumResults,
       "tmnxWlanGwTuQryName": tmnxWlanGwTuQryName,
       "tmnxWlanGwTuQryVolatile": tmnxWlanGwTuQryVolatile,
       "tmnxWlanGwTuTable": tmnxWlanGwTuTable,
       "tmnxWlanGwTuEntry": tmnxWlanGwTuEntry,
       "tmnxWlanGwTuRouter": tmnxWlanGwTuRouter,
       "tmnxWlanGwTuEncap": tmnxWlanGwTuEncap,
       "tmnxWlanGwTuRemoteAddrType": tmnxWlanGwTuRemoteAddrType,
       "tmnxWlanGwTuRemoteAddr": tmnxWlanGwTuRemoteAddr,
       "tmnxWlanGwTuLocalAddrType": tmnxWlanGwTuLocalAddrType,
       "tmnxWlanGwTuLocalAddr": tmnxWlanGwTuLocalAddr,
       "tmnxWlanGwTuFirstMoveTime": tmnxWlanGwTuFirstMoveTime,
       "tmnxWlanGwTuIsaGroup": tmnxWlanGwTuIsaGroup,
       "tmnxWlanGwTuIsaMember": tmnxWlanGwTuIsaMember,
       "tmnxWlanGwTuService": tmnxWlanGwTuService,
       "tmnxWlanGwTuInterface": tmnxWlanGwTuInterface,
       "tmnxWlanGwTuApMacAddress": tmnxWlanGwTuApMacAddress,
       "tmnxWlanGwTuApLearnFailed": tmnxWlanGwTuApLearnFailed,
       "tmnxWlanGwTuEncapTag1": tmnxWlanGwTuEncapTag1,
       "tmnxWlanGwTuEncapTag2": tmnxWlanGwTuEncapTag2,
       "tmnxWlanGwTuApSapPortId": tmnxWlanGwTuApSapPortId,
       "tmnxWlanGwTuApSapEncapVal": tmnxWlanGwTuApSapEncapVal,
       "tmnxWlanGwTuRemoteUdpPort": tmnxWlanGwTuRemoteUdpPort,
       "tmnxWlanGwTuNumUe": tmnxWlanGwTuNumUe,
       "tmnxWlanGwTuNumUeMigrant": tmnxWlanGwTuNumUeMigrant,
       "tmnxWlanGwTuNumUeDsm": tmnxWlanGwTuNumUeDsm,
       "tmnxWlanGwTuNumUeL2w": tmnxWlanGwTuNumUeL2w,
       "tmnxWlanGwTuNumUeEsm": tmnxWlanGwTuNumUeEsm,
       "tmnxWlanGwTuNumUeXcon": tmnxWlanGwTuNumUeXcon,
       "tmnxWlanGwBdUeTable": tmnxWlanGwBdUeTable,
       "tmnxWlanGwBdUeEntry": tmnxWlanGwBdUeEntry,
       "tmnxWlanGwBdBridgeId": tmnxWlanGwBdBridgeId,
       "tmnxWlanGwBdUeMacAddress": tmnxWlanGwBdUeMacAddress,
       "tmnxWlanGwBdUeQTag": tmnxWlanGwBdUeQTag,
       "tmnxWlanGwBdUeMplsLabel": tmnxWlanGwBdUeMplsLabel,
       "tmnxWlanGwBdUeTuRouter": tmnxWlanGwBdUeTuRouter,
       "tmnxWlanGwBdUeTuAddrType": tmnxWlanGwBdUeTuAddrType,
       "tmnxWlanGwBdUeTuRemoteAddr": tmnxWlanGwBdUeTuRemoteAddr,
       "tmnxWlanGwBdUeTuLocalAddr": tmnxWlanGwBdUeTuLocalAddr,
       "tmnxWlanGwBdUeTuQosRetailService": tmnxWlanGwBdUeTuQosRetailService,
       "tmnxWlanGwBdUeSsid": tmnxWlanGwBdUeSsid,
       "tmnxWlanGwBdUePrevApAddrType": tmnxWlanGwBdUePrevApAddrType,
       "tmnxWlanGwBdUePrevApAddr": tmnxWlanGwBdUePrevApAddr,
       "tmnxWlanGwBdUeLastMoveTime": tmnxWlanGwBdUeLastMoveTime,
       "tmnxWlanGwBdUeImsi": tmnxWlanGwBdUeImsi,
       "tmnxWlanGwBdUeService": tmnxWlanGwBdUeService,
       "tmnxWlanGwBdUeSapPortId": tmnxWlanGwBdUeSapPortId,
       "tmnxWlanGwBdUeSapPortEncapValue": tmnxWlanGwBdUeSapPortEncapValue,
       "tmnxWlanGwBdUeEncapsulation": tmnxWlanGwBdUeEncapsulation,
       "tmnxWlanGwXcnctTable": tmnxWlanGwXcnctTable,
       "tmnxWlanGwXcnctEntry": tmnxWlanGwXcnctEntry,
       "tmnxWlanGwXcnctLastCh": tmnxWlanGwXcnctLastCh,
       "tmnxWlanGwXcnctIsaGroup": tmnxWlanGwXcnctIsaGroup,
       "tmnxWlanGwXcnctTnlSrcIpAddrType": tmnxWlanGwXcnctTnlSrcIpAddrType,
       "tmnxWlanGwXcnctTnlSrcIpAddr": tmnxWlanGwXcnctTnlSrcIpAddr,
       "tmnxWlanGwXcnctTnlSrcIpPrefixLen": tmnxWlanGwXcnctTnlSrcIpPrefixLen,
       "tmnxWlanGwXcnctAdminState": tmnxWlanGwXcnctAdminState,
       "tmnxWlanGwLeTable": tmnxWlanGwLeTable,
       "tmnxWlanGwLeEntry": tmnxWlanGwLeEntry,
       "tmnxWlanGwLeRowStatus": tmnxWlanGwLeRowStatus,
       "tmnxWlanGwLeLastChanged": tmnxWlanGwLeLastChanged,
       "tmnxWlanGwLeAdminState": tmnxWlanGwLeAdminState,
       "tmnxWlanGwLeWlanGwGrpId": tmnxWlanGwLeWlanGwGrpId,
       "tmnxWlanGwLeVtepStartType": tmnxWlanGwLeVtepStartType,
       "tmnxWlanGwLeVtepStart": tmnxWlanGwLeVtepStart,
       "tmnxWlanGwLeVtepEndType": tmnxWlanGwLeVtepEndType,
       "tmnxWlanGwLeVtepEnd": tmnxWlanGwLeVtepEnd,
       "tmnxWlanGwLeVxlanPort": tmnxWlanGwLeVxlanPort,
       "tmnxWlanGwBdTable": tmnxWlanGwBdTable,
       "tmnxWlanGwBdEntry": tmnxWlanGwBdEntry,
       "tmnxWlanGwBdVNI": tmnxWlanGwBdVNI,
       "tmnxWlanGwBdRT": tmnxWlanGwBdRT,
       "tmnxWlanGwBdRD": tmnxWlanGwBdRD,
       "tmnxWlanGwBdWlanGwGrpId": tmnxWlanGwBdWlanGwGrpId,
       "tmnxWlanGwBdIsaMemberId": tmnxWlanGwBdIsaMemberId,
       "tmnxWlanGwBdVlanTag": tmnxWlanGwBdVlanTag,
       "tmnxWlanGwBdService": tmnxWlanGwBdService,
       "tmnxWlanGwBdInterface": tmnxWlanGwBdInterface,
       "tmnxWlanGwBdMacTranslation": tmnxWlanGwBdMacTranslation,
       "tmnxWlanGwBdBdMac": tmnxWlanGwBdBdMac,
       "tmnxWlanGwBdAssistAddrRes": tmnxWlanGwBdAssistAddrRes,
       "tmnxWlanGwBdNetwMaxMac": tmnxWlanGwBdNetwMaxMac,
       "tmnxWlanGwBdNetwAdminState": tmnxWlanGwBdNetwAdminState,
       "tmnxWlanGwBdAccsMaxMac": tmnxWlanGwBdAccsMaxMac,
       "tmnxWlanGwBdAccsPolicer": tmnxWlanGwBdAccsPolicer,
       "tmnxWlanGwBdNetwPolicer": tmnxWlanGwBdNetwPolicer,
       "tmnxWlanGwVlanXcnctTable": tmnxWlanGwVlanXcnctTable,
       "tmnxWlanGwVlanXcnctEntry": tmnxWlanGwVlanXcnctEntry,
       "tmnxWlanGwVlanXcnctLastChanged": tmnxWlanGwVlanXcnctLastChanged,
       "tmnxWlanGwVlanXcnctAccPolicy": tmnxWlanGwVlanXcnctAccPolicy,
       "tmnxWlanGwVlanXcnctAdminState": tmnxWlanGwVlanXcnctAdminState,
       "tmnxWlanGwVlanXcnctAcctUpdInterv": tmnxWlanGwVlanXcnctAcctUpdInterv,
       "tmnxWlanGwVlanXcnctMobAcctUpd": tmnxWlanGwVlanXcnctMobAcctUpd,
       "tmnxWlanGwTuBdUeTable": tmnxWlanGwTuBdUeTable,
       "tmnxWlanGwTuBdUeEntry": tmnxWlanGwTuBdUeEntry,
       "tmnxWlanGwTuBdUeSsid": tmnxWlanGwTuBdUeSsid,
       "tmnxWlanGwGrpTableLastCh": tmnxWlanGwGrpTableLastCh,
       "tmnxWlanGwIomTableLastCh": tmnxWlanGwIomTableLastCh,
       "tmnxWlanGwSoftGreIfTableLastCh": tmnxWlanGwSoftGreIfTableLastCh,
       "tmnxWlanGwIfRetailTableLastCh": tmnxWlanGwIfRetailTableLastCh,
       "tmnxWlanGwMgwProfTableLastCh": tmnxWlanGwMgwProfTableLastCh,
       "tmnxWlanGwMgwAddrTableLastCh": tmnxWlanGwMgwAddrTableLastCh,
       "tmnxWlanGwTableLastCh": tmnxWlanGwTableLastCh,
       "tmnxWlanGwVlanTableLastCh": tmnxWlanGwVlanTableLastCh,
       "tmnxWlanGwPgwTableLastCh": tmnxWlanGwPgwTableLastCh,
       "tmnxWlanGwGgsnTableLastCh": tmnxWlanGwGgsnTableLastCh,
       "tmnxWlanGwSubIfTableLastCh": tmnxWlanGwSubIfTableLastCh,
       "tmnxWlanGwVlanDsmTableLastCh": tmnxWlanGwVlanDsmTableLastCh,
       "tmnxWlanGwDsmIpFilTableLastCh": tmnxWlanGwDsmIpFilTableLastCh,
       "tmnxWlanGwDsmIpFilN3TableLastCh": tmnxWlanGwDsmIpFilN3TableLastCh,
       "tmnxWlanGwPolicerTableLastCh": tmnxWlanGwPolicerTableLastCh,
       "tmnxWlanGwL2ApTableLastCh": tmnxWlanGwL2ApTableLastCh,
       "tmnxWlanGwVplsTableLastCh": tmnxWlanGwVplsTableLastCh,
       "tmnxWlanGwDsmIpFil6N3TableLastCh": tmnxWlanGwDsmIpFil6N3TableLastCh,
       "tmnxWlanGwVlanBrgTableLastCh": tmnxWlanGwVlanBrgTableLastCh,
       "tmnxWlanGwSubIfPmTableLastCh": tmnxWlanGwSubIfPmTableLastCh,
       "tmnxWlanGwVlanDhcp6TableLastCh": tmnxWlanGwVlanDhcp6TableLastCh,
       "tmnxWlanGwVlanSlaacTableLastCh": tmnxWlanGwVlanSlaacTableLastCh,
       "tmnxWlanGwDsmTableLastCh": tmnxWlanGwDsmTableLastCh,
       "tmnxWlanGwMdaTableLastCh": tmnxWlanGwMdaTableLastCh,
       "tmnxWlanGwXcnctTableLastCh": tmnxWlanGwXcnctTableLastCh,
       "tmnxWlanGwVlanXcnctTableLastCh": tmnxWlanGwVlanXcnctTableLastCh,
       "tmnxWlanGwVlanLeTableLastCh": tmnxWlanGwVlanLeTableLastCh,
       "tmnxWlanGwMmeTableLastChanged": tmnxWlanGwMmeTableLastChanged,
       "tmnxWlanGwGrpIfGwAddrTableLastCh": tmnxWlanGwGrpIfGwAddrTableLastCh,
       "tmnxWlanGwResrcProblem": tmnxWlanGwResrcProblem,
       "tmnxWlanGwNumSoftGreTu": tmnxWlanGwNumSoftGreTu,
       "tmnxWlanGwPeakNumSoftGreTu": tmnxWlanGwPeakNumSoftGreTu,
       "tmnxWlanGwNumUe": tmnxWlanGwNumUe,
       "tmnxWlanGwPeakNumUe": tmnxWlanGwPeakNumUe,
       "tmnxWlanGwNumMgw": tmnxWlanGwNumMgw,
       "tmnxWlanGwMgwNumHeldSe": tmnxWlanGwMgwNumHeldSe,
       "tmnxGtpNumMme": tmnxGtpNumMme,
       "tmnxGtpNumEnodeB": tmnxGtpNumEnodeB,
       "tmnxGtpNumS11Sessions": tmnxGtpNumS11Sessions,
       "tmnxGtpNumUplinks": tmnxGtpNumUplinks,
       "tmnxGtpNumS11IdleSessions": tmnxGtpNumS11IdleSessions,
       "tmnxWlanGwVappTableLastCh": tmnxWlanGwVappTableLastCh,
       "tmnxWlanGwNotificationObjs": tmnxWlanGwNotificationObjs,
       "tmnxWlanGwNotifyDescription": tmnxWlanGwNotifyDescription,
       "tmnxWlanGwNotifyTrue": tmnxWlanGwNotifyTrue,
       "tmnxWlanGwNotify3gppRelease": tmnxWlanGwNotify3gppRelease,
       "tmnxWlanGwNotifyMdaSlotNum": tmnxWlanGwNotifyMdaSlotNum,
       "tmnxWlanGwNotifySubIfIndex": tmnxWlanGwNotifySubIfIndex,
       "tmnxWlanGwNotifyAddrFamily": tmnxWlanGwNotifyAddrFamily,
       "tmnxWlanGwNotifyIsaGrpId": tmnxWlanGwNotifyIsaGrpId,
       "tmnxWlanGwNotifyIsaMemberId": tmnxWlanGwNotifyIsaMemberId,
       "tmnxWlanGwNotifyD6cServer1": tmnxWlanGwNotifyD6cServer1,
       "tmnxWlanGwNotifyD6cServer2": tmnxWlanGwNotifyD6cServer2,
       "tmnxWlanGwNotifyD6cServer3": tmnxWlanGwNotifyD6cServer3,
       "tmnxWlanGwNotifyD6cServer4": tmnxWlanGwNotifyD6cServer4,
       "tmnxWlanGwNotifyD6cServer5": tmnxWlanGwNotifyD6cServer5,
       "tmnxWlanGwNotifyD6cServer6": tmnxWlanGwNotifyD6cServer6,
       "tmnxWlanGwNotifyD6cServer7": tmnxWlanGwNotifyD6cServer7,
       "tmnxWlanGwNotifyD6cServer8": tmnxWlanGwNotifyD6cServer8,
       "tmnxWlanGwNotifySubnetAddrType": tmnxWlanGwNotifySubnetAddrType,
       "tmnxWlanGwNotifySubnetAddr": tmnxWlanGwNotifySubnetAddr,
       "tmnxWlanGwNotifySubnetPrefLen": tmnxWlanGwNotifySubnetPrefLen,
       "tmnxWlanGwNotifyGtpMsgType": tmnxWlanGwNotifyGtpMsgType,
       "tmnxWlanGwNotifyGtpMsgDirection": tmnxWlanGwNotifyGtpMsgDirection,
       "tmnxWlanGwNotifyImsi": tmnxWlanGwNotifyImsi,
       "tmnxWlanGwNotifyTeid": tmnxWlanGwNotifyTeid,
       "tmnxWlanGwNotifyBdBridgeId": tmnxWlanGwNotifyBdBridgeId,
       "tmnxWlanGwNotifyUeMacAddress": tmnxWlanGwNotifyUeMacAddress,
       "tmnxWlanGwNotifyChassisIndex": tmnxWlanGwNotifyChassisIndex,
       "tmnxWlanGwNotifyCardSlotNum": tmnxWlanGwNotifyCardSlotNum,
       "tmnxWlanGwNotifyEntity": tmnxWlanGwNotifyEntity,
       "tmnxWlanGwNotifyEsaNum": tmnxWlanGwNotifyEsaNum,
       "tmnxWlanGwNotifyEsaVappNum": tmnxWlanGwNotifyEsaVappNum,
       "tmnxGtpObjs": tmnxGtpObjs,
       "tmnxGtpS11ItfTableLastChanged": tmnxGtpS11ItfTableLastChanged,
       "tmnxGtpS11ItfTable": tmnxGtpS11ItfTable,
       "tmnxGtpS11ItfEntry": tmnxGtpS11ItfEntry,
       "tmnxGtpS11ItfName": tmnxGtpS11ItfName,
       "tmnxGtpS11ItfRowStatus": tmnxGtpS11ItfRowStatus,
       "tmnxGtpS11ItfLastChanged": tmnxGtpS11ItfLastChanged,
       "tmnxGtpS11ItfApnPolicyName": tmnxGtpS11ItfApnPolicyName,
       "tmnxGtpPpmTableLastChanged": tmnxGtpPpmTableLastChanged,
       "tmnxGtpPpmTable": tmnxGtpPpmTable,
       "tmnxGtpPpmEntry": tmnxGtpPpmEntry,
       "tmnxGtpPpmGtpItfType": tmnxGtpPpmGtpItfType,
       "tmnxGtpPpmAddrType": tmnxGtpPpmAddrType,
       "tmnxGtpPpmAddr": tmnxGtpPpmAddr,
       "tmnxGtpPpmAddrPrefixLen": tmnxGtpPpmAddrPrefixLen,
       "tmnxGtpPpmRowStatus": tmnxGtpPpmRowStatus,
       "tmnxGtpPpmLastChanged": tmnxGtpPpmLastChanged,
       "tmnxGtpPpmProfileName": tmnxGtpPpmProfileName,
       "tmnxGtpS11SeTableLastChanged": tmnxGtpS11SeTableLastChanged,
       "tmnxGtpS11SeTable": tmnxGtpS11SeTable,
       "tmnxGtpS11SeEntry": tmnxGtpS11SeEntry,
       "tmnxGtpS11SeImsi": tmnxGtpS11SeImsi,
       "tmnxGtpS11SeApn": tmnxGtpS11SeApn,
       "tmnxGtpS11SePeerRouter": tmnxGtpS11SePeerRouter,
       "tmnxGtpS11SePeerAddrType": tmnxGtpS11SePeerAddrType,
       "tmnxGtpS11SePeerAddr": tmnxGtpS11SePeerAddr,
       "tmnxGtpS11SeRemoteCtrlTeid": tmnxGtpS11SeRemoteCtrlTeid,
       "tmnxGtpS11SeLocalCtrlTeid": tmnxGtpS11SeLocalCtrlTeid,
       "tmnxGtpS11SeChrgChar": tmnxGtpS11SeChrgChar,
       "tmnxGtpS11SeQosUplinkAmbr": tmnxGtpS11SeQosUplinkAmbr,
       "tmnxGtpS11SeQosDwnlinkAmbr": tmnxGtpS11SeQosDwnlinkAmbr,
       "tmnxGtpS11SePdnTeid": tmnxGtpS11SePdnTeid,
       "tmnxGtpS11SeUliCgi": tmnxGtpS11SeUliCgi,
       "tmnxGtpS11SeUliSai": tmnxGtpS11SeUliSai,
       "tmnxGtpS11SeUliRai": tmnxGtpS11SeUliRai,
       "tmnxGtpS11SeUliTai": tmnxGtpS11SeUliTai,
       "tmnxGtpS11SeUliEcgi": tmnxGtpS11SeUliEcgi,
       "tmnxGtpS11BcTableLastChanged": tmnxGtpS11BcTableLastChanged,
       "tmnxGtpS11BcTable": tmnxGtpS11BcTable,
       "tmnxGtpS11BcEntry": tmnxGtpS11BcEntry,
       "tmnxGtpS11BcId": tmnxGtpS11BcId,
       "tmnxGtpS11BcRemoteTeid": tmnxGtpS11BcRemoteTeid,
       "tmnxGtpS11BcLocalTeid": tmnxGtpS11BcLocalTeid,
       "tmnxGtpS11BcQosUlGbr": tmnxGtpS11BcQosUlGbr,
       "tmnxGtpS11BcQosUlMbr": tmnxGtpS11BcQosUlMbr,
       "tmnxGtpS11BcQosDlGbr": tmnxGtpS11BcQosDlGbr,
       "tmnxGtpS11BcQosDlMbr": tmnxGtpS11BcQosDlMbr,
       "tmnxGtpS11BcQosQci": tmnxGtpS11BcQosQci,
       "tmnxGtpS11BcQosArp": tmnxGtpS11BcQosArp,
       "tmnxGtpS11BcRemoteAddrType": tmnxGtpS11BcRemoteAddrType,
       "tmnxGtpS11BcRemoteAddr": tmnxGtpS11BcRemoteAddr,
       "tmnxGtpUplinkTableLastChanged": tmnxGtpUplinkTableLastChanged,
       "tmnxGtpUplinkTable": tmnxGtpUplinkTable,
       "tmnxGtpUplinkEntry": tmnxGtpUplinkEntry,
       "tmnxGtpUplinkRowStatus": tmnxGtpUplinkRowStatus,
       "tmnxGtpUplinkLastChanged": tmnxGtpUplinkLastChanged,
       "tmnxGtpUplinkApn": tmnxGtpUplinkApn,
       "tmnxGtpUplinkPdnType": tmnxGtpUplinkPdnType,
       "tmnxWlanGwNotifyPrefix": tmnxWlanGwNotifyPrefix,
       "tmnxWlanGwNotifications": tmnxWlanGwNotifications,
       "tmnxWlanGwResrcProblemDetected": tmnxWlanGwResrcProblemDetected,
       "tmnxWlanGwResrcProblemCause": tmnxWlanGwResrcProblemCause,
       "tmnxWlanGwTuQosProblem": tmnxWlanGwTuQosProblem,
       "tmnxWlanGwGrpOperStateChanged": tmnxWlanGwGrpOperStateChanged,
       "tmnxWlanGwIomActive": tmnxWlanGwIomActive,
       "tmnxWlanGwMgwConnected": tmnxWlanGwMgwConnected,
       "tmnxWlanGwMgwRestarted": tmnxWlanGwMgwRestarted,
       "tmnxWlanGwNumMgwHi": tmnxWlanGwNumMgwHi,
       "tmnxWlanGwMgwStateChanged": tmnxWlanGwMgwStateChanged,
       "tmnxWlanGwQosRadiusGtpMismatch": tmnxWlanGwQosRadiusGtpMismatch,
       "tmnxWlanGwSubIfRedActiveChanged": tmnxWlanGwSubIfRedActiveChanged,
       "tmnxWlanGwDsmGtpTunnelSetupFail": tmnxWlanGwDsmGtpTunnelSetupFail,
       "tmnxWlanGwSubIfPmStartD6cFailed": tmnxWlanGwSubIfPmStartD6cFailed,
       "tmnxWlanGwSubIfPmNewPlReqFailed": tmnxWlanGwSubIfPmNewPlReqFailed,
       "tmnxWlanGwSubIfPmAddNewPlFailed": tmnxWlanGwSubIfPmAddNewPlFailed,
       "tmnxWlanGwSubIfPmCrIntObjFailed": tmnxWlanGwSubIfPmCrIntObjFailed,
       "tmnxWlanGwSubIfPmPoolTimeout": tmnxWlanGwSubIfPmPoolTimeout,
       "tmnxWlanGwSubIfPmPoolUsageLow": tmnxWlanGwSubIfPmPoolUsageLow,
       "tmnxWlanGwSubIfPmLsQryRtryFailed": tmnxWlanGwSubIfPmLsQryRtryFailed,
       "tmnxWlanGwGtpMessageDropped": tmnxWlanGwGtpMessageDropped,
       "tmnxWlanGwSubIfPmPoolPartialUse": tmnxWlanGwSubIfPmPoolPartialUse,
       "tmnxWlanGwBdCreated": tmnxWlanGwBdCreated,
       "tmnxWlanGwBdDeleted": tmnxWlanGwBdDeleted,
       "tmnxWlanGwUeCreationFail": tmnxWlanGwUeCreationFail,
       "tmnxWlanGwUeReplacement": tmnxWlanGwUeReplacement,
       "tmnxWlanGwGrpMemberUsageHigh": tmnxWlanGwGrpMemberUsageHigh}
)
