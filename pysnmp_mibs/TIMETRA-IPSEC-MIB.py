# SNMP MIB module (TIMETRA-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-IPSEC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:01:18 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
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
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxEsaIdOrZero,
 TmnxEsaVmIdOrZero,
 TmnxHwIndexOrZero,
 tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxEsaId,
 tmnxEsaVmId,
 tmnxIPsecIsaGrpId,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxEsaIdOrZero",
    "TmnxEsaVmIdOrZero",
    "TmnxHwIndexOrZero",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxEsaId",
    "tmnxEsaVmId",
    "tmnxIPsecIsaGrpId",
    "tmnxMDASlotNum")

(TFilterID,) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TFilterID")

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

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(TEntryId,
 TItemDescription,
 TItemLongDescription,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TTcpUdpPort,
 TmnxAdminState,
 TmnxAuthAlgorithm,
 TmnxBfdSessOperState,
 TmnxEnabledDisabled,
 TmnxEncrAlgorithm,
 TmnxIPsecDirection,
 TmnxIPsecKeyingType,
 TmnxIPsecTunnelTemplateId,
 TmnxIPsecTunnelTemplateIdOrZero,
 TmnxIkePolicyAuthMethod,
 TmnxIkePolicyAutoEapMethod,
 TmnxIkePolicyAutoEapOwnMethod,
 TmnxIkePolicyDHGroupOrZero,
 TmnxIkePolicyOwnAuthMethod,
 TmnxOperState,
 TmnxServId,
 TmnxTunnelGroupIdOrZero,
 TmnxVRtrID,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TEntryId",
    "TItemDescription",
    "TItemLongDescription",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TTcpUdpPort",
    "TmnxAdminState",
    "TmnxAuthAlgorithm",
    "TmnxBfdSessOperState",
    "TmnxEnabledDisabled",
    "TmnxEncrAlgorithm",
    "TmnxIPsecDirection",
    "TmnxIPsecKeyingType",
    "TmnxIPsecTunnelTemplateId",
    "TmnxIPsecTunnelTemplateIdOrZero",
    "TmnxIkePolicyAuthMethod",
    "TmnxIkePolicyAutoEapMethod",
    "TmnxIkePolicyAutoEapOwnMethod",
    "TmnxIkePolicyDHGroupOrZero",
    "TmnxIkePolicyOwnAuthMethod",
    "TmnxOperState",
    "TmnxServId",
    "TmnxTunnelGroupIdOrZero",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraIPsecMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 48)
)
if mibBuilder.loadTexts:
    timetraIPsecMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxIPsecTransformId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )



class TmnxIPsecTransformIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )



class TmnxIPsecIkeTransformId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class TmnxIPsecIkeTransformIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )



class TmnxIkePolicyId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )



class TmnxIkePolicyIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )



class TmnxIkeVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )



class TmnxIkePolicyIkeMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("aggressive", 2))
    )



class TmnxIkePolicyDHGroup(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              14,
              15,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group5", 5),
          ("group14", 14),
          ("group15", 15),
          ("group19", 19),
          ("group20", 20),
          ("group21", 21))
    )



class TmnxIPsecTransformPfsDhGrp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              5,
              14,
              15,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("inherit", -1),
          ("disablePfs", 0),
          ("group1", 1),
          ("group2", 2),
          ("group5", 5),
          ("group14", 14),
          ("group15", 15),
          ("group19", 19),
          ("group20", 20),
          ("group21", 21))
    )



class TmnxIPsecPolicyId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )



class TmnxIPsecPolicyIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )



class TmnxIPsecDirection2(TextualConvention, Integer32):
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
        *(("inbound", 1),
          ("outbound", 2),
          ("bidirectional", 3))
    )



class TmnxIPsecProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ah", 1),
          ("esp", 2))
    )



class TmnxIPsecLocalIdType(TextualConvention, Integer32):
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
          ("ipv4", 1),
          ("fqdn", 2),
          ("dn", 3),
          ("ipv6", 4))
    )



class TmnxCertRevStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crl", 1),
          ("ocsp", 2))
    )



class TmnxCertRevStatusOrNone(TextualConvention, Integer32):
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
        *(("none", 0),
          ("crl", 1),
          ("ocsp", 2))
    )



class TmnxIkePolicyRelayUnSolCfgAttr(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("internalIp4Address", 0),
          ("internalIp4Netmask", 1),
          ("internalIp4Dns", 2),
          ("internalIp6Address", 3),
          ("internalIp6Dns", 4))
    )


class TmnxIpsecTrafficSelSide(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )



class TmnxIPsecHistStatsType(TextualConvention, Integer32):
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
              100,
              101,
              102,
              103,
              104,
              105,
              120,
              121,
              122,
              123,
              124,
              125,
              140,
              141,
              142,
              143,
              144,
              145,
              160,
              161,
              162,
              163,
              164,
              165,
              200,
              201,
              202,
              203,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              400,
              401,
              402,
              403,
              404,
              405,
              420,
              421,
              422,
              423,
              424,
              425,
              440,
              441,
              442,
              443,
              444,
              445,
              460,
              461,
              462,
              463,
              464,
              465,
              500,
              501,
              600,
              700,
              701,
              702)
        )
    )
    namedValues = NamedValues(
        *(("numOfTotalIPsecTnls", 1),
          ("numOfIPsecSL2LTnls", 2),
          ("numOfIPsecDL2LTnls", 3),
          ("numOfIPsecRATnls", 4),
          ("numOfAccumGreTnls", 5),
          ("numOfAccumIpTnls", 6),
          ("numOfAccumL2tpv3Tnls", 7),
          ("numOfIPsecEncrPkts", 100),
          ("numOfIPsecDecrPkts", 101),
          ("numOfIPsecEnDecrPkts", 102),
          ("numOfIPsecEncrBits", 103),
          ("numOfIPsecDecrBits", 104),
          ("numOfIPsecEnDecrBits", 105),
          ("numOfGreTnlEncapPkts", 120),
          ("numOfGreTnlDecapPkts", 121),
          ("numOfGreTnlEnDecapPkts", 122),
          ("numOfGreTnlEncapBits", 123),
          ("numOfGreTnlDecapBits", 124),
          ("numOfGreTnlEnDecapBits", 125),
          ("numOfIpTnlEncapPkts", 140),
          ("numOfIpTnlDecapPkts", 141),
          ("numOfIpTnlEnDecapPkts", 142),
          ("numOfIpTnlEncapBits", 143),
          ("numOfIpTnlDecapBits", 144),
          ("numOfIpTnlEnDecapBits", 145),
          ("numOfL2tpv3TnlEncapPkts", 160),
          ("numOfL2tpv3TnlDecapPkts", 161),
          ("numOfL2tpv3TnlEnDecapPkts", 162),
          ("numOfL2tpv3TnlEncapBits", 163),
          ("numOfL2tpv3TnlDecapBits", 164),
          ("numOfL2tpv3TnlEnDecapBits", 165),
          ("numOfNewTotalIPsecTnls", 200),
          ("numOfNewIPsecSL2LTnls", 201),
          ("numOfNewIPsecDL2LTnls", 202),
          ("numOfNewIPsecRATnls", 203),
          ("numOfIkeAuthFails", 300),
          ("numOfIkeNoPrpslFails", 301),
          ("numOfIkeAddrAsgFails", 302),
          ("numOfIkeInvldTsFails", 303),
          ("numOfIkeInvldKeFails", 304),
          ("numOfIkeDpdTimeoutFails", 305),
          ("numOfIkeOtherReasonFails", 306),
          ("numOfAccumIPsecEncrPkts", 400),
          ("numOfAccumIPsecDecrPkts", 401),
          ("numOfAccumIPsecEnDecrPkts", 402),
          ("numOfAccumIPsecEncrKBs", 403),
          ("numOfAccumIPsecDecrKBs", 404),
          ("numOfAccumIPsecEnDecrKBs", 405),
          ("numOfAccumGreTnlEncapPkts", 420),
          ("numOfAccumGreTnlDecapPkts", 421),
          ("numOfAccumGreTnlEnDecapPkts", 422),
          ("numOfAccumGreTnlEncapKBs", 423),
          ("numOfAccumGreTnlDecapKBs", 424),
          ("numOfAccumGreTnlEnDecapKBs", 425),
          ("numOfAccumIpTnlEncapPkts", 440),
          ("numOfAccumIpTnlDecapPkts", 441),
          ("numOfAccumIpTnlEnDecapPkts", 442),
          ("numOfAccumIpTnlEncapKBs", 443),
          ("numOfAccumIpTnlDecapKBs", 444),
          ("numOfAccumIpTnlEnDecapKBs", 445),
          ("numOfAccumL2tpv3TnlEncapPkts", 460),
          ("numOfAccumL2tpv3TnlDecapPkts", 461),
          ("numOfAccumL2tpv3TnlEnDecapPkts", 462),
          ("numOfAccumL2tpv3TnlEncapKBs", 463),
          ("numOfAccumL2tpv3TnlDecapKBs", 464),
          ("numOfAccumL2tpv3TnlEnDecapKBs", 465),
          ("isaCtrolPlaneCpuUsageBp", 500),
          ("isaDataPlaneCpuUsageBp", 501),
          ("numOfIsaMemAllocFailures", 600),
          ("ikev2IkeSaInitExchgPktsDrops", 700),
          ("ikev2IkeAuthExchgPktsDrops", 701),
          ("ikev2CrtCldInfoExchgPktsDrops", 702))
    )



class TmnxIPsecOperState(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 1),
          ("inService", 2),
          ("outOfService", 3),
          ("transition", 4),
          ("limited", 5))
    )



class TIPsecMulticastProtocol(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("mld", 0),
          ("igmp", 1))
    )


# MIB Managed Objects in the order of their OIDs

_TmnxIPsecConformance_ObjectIdentity = ObjectIdentity
tmnxIPsecConformance = _TmnxIPsecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48)
)
_TmnxIPsecCompliances_ObjectIdentity = ObjectIdentity
tmnxIPsecCompliances = _TmnxIPsecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1)
)
_TmnxIPsecGroups_ObjectIdentity = ObjectIdentity
tmnxIPsecGroups = _TmnxIPsecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2)
)
_TmnxIPsecNotifGroups_ObjectIdentity = ObjectIdentity
tmnxIPsecNotifGroups = _TmnxIPsecNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3)
)
_TmnxIPsecMGCompliances_ObjectIdentity = ObjectIdentity
tmnxIPsecMGCompliances = _TmnxIPsecMGCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 4)
)
_TmnxIPsecMGGroups_ObjectIdentity = ObjectIdentity
tmnxIPsecMGGroups = _TmnxIPsecMGGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 5)
)
_TmnxIPsecObjects_ObjectIdentity = ObjectIdentity
tmnxIPsecObjects = _TmnxIPsecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48)
)
_TmnxIPsecTransformTblLastChanged_Type = TimeStamp
_TmnxIPsecTransformTblLastChanged_Object = MibScalar
tmnxIPsecTransformTblLastChanged = _TmnxIPsecTransformTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 1),
    _TmnxIPsecTransformTblLastChanged_Type()
)
tmnxIPsecTransformTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTransformTblLastChanged.setStatus("current")
_TmnxIPsecTransformTable_Object = MibTable
tmnxIPsecTransformTable = _TmnxIPsecTransformTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2)
)
if mibBuilder.loadTexts:
    tmnxIPsecTransformTable.setStatus("current")
_TmnxIPsecTransformEntry_Object = MibTableRow
tmnxIPsecTransformEntry = _TmnxIPsecTransformEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1)
)
tmnxIPsecTransformEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTransformId"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTransformEntry.setStatus("current")
_TmnxIPsecTransformId_Type = TmnxIPsecTransformId
_TmnxIPsecTransformId_Object = MibTableColumn
tmnxIPsecTransformId = _TmnxIPsecTransformId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1, 1),
    _TmnxIPsecTransformId_Type()
)
tmnxIPsecTransformId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTransformId.setStatus("current")
_TmnxIPsecTransformRowStatus_Type = RowStatus
_TmnxIPsecTransformRowStatus_Object = MibTableColumn
tmnxIPsecTransformRowStatus = _TmnxIPsecTransformRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1, 2),
    _TmnxIPsecTransformRowStatus_Type()
)
tmnxIPsecTransformRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTransformRowStatus.setStatus("current")
_TmnxIPsecTransformLastChanged_Type = TimeStamp
_TmnxIPsecTransformLastChanged_Object = MibTableColumn
tmnxIPsecTransformLastChanged = _TmnxIPsecTransformLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1, 3),
    _TmnxIPsecTransformLastChanged_Type()
)
tmnxIPsecTransformLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTransformLastChanged.setStatus("current")


class _TmnxIPsecTransformAuthAlgorithm_Type(TmnxAuthAlgorithm):
    """Custom type tmnxIPsecTransformAuthAlgorithm based on TmnxAuthAlgorithm"""
    defaultValue = 3


_TmnxIPsecTransformAuthAlgorithm_Type.__name__ = "TmnxAuthAlgorithm"
_TmnxIPsecTransformAuthAlgorithm_Object = MibTableColumn
tmnxIPsecTransformAuthAlgorithm = _TmnxIPsecTransformAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1, 4),
    _TmnxIPsecTransformAuthAlgorithm_Type()
)
tmnxIPsecTransformAuthAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTransformAuthAlgorithm.setStatus("current")


class _TmnxIPsecTransformEncrAlgorithm_Type(TmnxEncrAlgorithm):
    """Custom type tmnxIPsecTransformEncrAlgorithm based on TmnxEncrAlgorithm"""
    defaultValue = 4


_TmnxIPsecTransformEncrAlgorithm_Type.__name__ = "TmnxEncrAlgorithm"
_TmnxIPsecTransformEncrAlgorithm_Object = MibTableColumn
tmnxIPsecTransformEncrAlgorithm = _TmnxIPsecTransformEncrAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1, 5),
    _TmnxIPsecTransformEncrAlgorithm_Type()
)
tmnxIPsecTransformEncrAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTransformEncrAlgorithm.setStatus("current")


class _TmnxIPsecTransformPfsDhGroup_Type(TmnxIPsecTransformPfsDhGrp):
    """Custom type tmnxIPsecTransformPfsDhGroup based on TmnxIPsecTransformPfsDhGrp"""
    defaultValue = -1


_TmnxIPsecTransformPfsDhGroup_Type.__name__ = "TmnxIPsecTransformPfsDhGrp"
_TmnxIPsecTransformPfsDhGroup_Object = MibTableColumn
tmnxIPsecTransformPfsDhGroup = _TmnxIPsecTransformPfsDhGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1, 6),
    _TmnxIPsecTransformPfsDhGroup_Type()
)
tmnxIPsecTransformPfsDhGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTransformPfsDhGroup.setStatus("current")


class _TmnxIPsecTransformLifeTime_Type(Unsigned32):
    """Custom type tmnxIPsecTransformLifeTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1200, 31536000),
    )


_TmnxIPsecTransformLifeTime_Type.__name__ = "Unsigned32"
_TmnxIPsecTransformLifeTime_Object = MibTableColumn
tmnxIPsecTransformLifeTime = _TmnxIPsecTransformLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1, 7),
    _TmnxIPsecTransformLifeTime_Type()
)
tmnxIPsecTransformLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTransformLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecTransformLifeTime.setUnits("seconds")
_TmnxIkePolicyTableLastChanged_Type = TimeStamp
_TmnxIkePolicyTableLastChanged_Object = MibScalar
tmnxIkePolicyTableLastChanged = _TmnxIkePolicyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 3),
    _TmnxIkePolicyTableLastChanged_Type()
)
tmnxIkePolicyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIkePolicyTableLastChanged.setStatus("current")
_TmnxIkePolicyTable_Object = MibTable
tmnxIkePolicyTable = _TmnxIkePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4)
)
if mibBuilder.loadTexts:
    tmnxIkePolicyTable.setStatus("current")
_TmnxIkePolicyEntry_Object = MibTableRow
tmnxIkePolicyEntry = _TmnxIkePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1)
)
tmnxIkePolicyEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tmnxIkePolicyId"),
)
if mibBuilder.loadTexts:
    tmnxIkePolicyEntry.setStatus("current")
_TmnxIkePolicyId_Type = TmnxIkePolicyId
_TmnxIkePolicyId_Object = MibTableColumn
tmnxIkePolicyId = _TmnxIkePolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 1),
    _TmnxIkePolicyId_Type()
)
tmnxIkePolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIkePolicyId.setStatus("current")
_TmnxIkePolicyRowStatus_Type = RowStatus
_TmnxIkePolicyRowStatus_Object = MibTableColumn
tmnxIkePolicyRowStatus = _TmnxIkePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 2),
    _TmnxIkePolicyRowStatus_Type()
)
tmnxIkePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyRowStatus.setStatus("current")
_TmnxIkePolicyLastChanged_Type = TimeStamp
_TmnxIkePolicyLastChanged_Object = MibTableColumn
tmnxIkePolicyLastChanged = _TmnxIkePolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 3),
    _TmnxIkePolicyLastChanged_Type()
)
tmnxIkePolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIkePolicyLastChanged.setStatus("current")


class _TmnxIkePolicyDescription_Type(TItemDescription):
    """Custom type tmnxIkePolicyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxIkePolicyDescription_Type.__name__ = "TItemDescription"
_TmnxIkePolicyDescription_Object = MibTableColumn
tmnxIkePolicyDescription = _TmnxIkePolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 4),
    _TmnxIkePolicyDescription_Type()
)
tmnxIkePolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyDescription.setStatus("current")


class _TmnxIkePolicyIkeMode_Type(TmnxIkePolicyIkeMode):
    """Custom type tmnxIkePolicyIkeMode based on TmnxIkePolicyIkeMode"""
    defaultValue = 1


_TmnxIkePolicyIkeMode_Type.__name__ = "TmnxIkePolicyIkeMode"
_TmnxIkePolicyIkeMode_Object = MibTableColumn
tmnxIkePolicyIkeMode = _TmnxIkePolicyIkeMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 5),
    _TmnxIkePolicyIkeMode_Type()
)
tmnxIkePolicyIkeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyIkeMode.setStatus("current")


class _TmnxIkePolicyDHGroup_Type(TmnxIkePolicyDHGroup):
    """Custom type tmnxIkePolicyDHGroup based on TmnxIkePolicyDHGroup"""
    defaultValue = 2


_TmnxIkePolicyDHGroup_Type.__name__ = "TmnxIkePolicyDHGroup"
_TmnxIkePolicyDHGroup_Object = MibTableColumn
tmnxIkePolicyDHGroup = _TmnxIkePolicyDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 6),
    _TmnxIkePolicyDHGroup_Type()
)
tmnxIkePolicyDHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyDHGroup.setStatus("obsolete")


class _TmnxIkePolicyPFSEnabled_Type(TruthValue):
    """Custom type tmnxIkePolicyPFSEnabled based on TruthValue"""
    defaultValue = 2


_TmnxIkePolicyPFSEnabled_Type.__name__ = "TruthValue"
_TmnxIkePolicyPFSEnabled_Object = MibTableColumn
tmnxIkePolicyPFSEnabled = _TmnxIkePolicyPFSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 7),
    _TmnxIkePolicyPFSEnabled_Type()
)
tmnxIkePolicyPFSEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyPFSEnabled.setStatus("current")


class _TmnxIkePolicyPFSDHGroup_Type(TmnxIkePolicyDHGroup):
    """Custom type tmnxIkePolicyPFSDHGroup based on TmnxIkePolicyDHGroup"""
    defaultValue = 2


_TmnxIkePolicyPFSDHGroup_Type.__name__ = "TmnxIkePolicyDHGroup"
_TmnxIkePolicyPFSDHGroup_Object = MibTableColumn
tmnxIkePolicyPFSDHGroup = _TmnxIkePolicyPFSDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 8),
    _TmnxIkePolicyPFSDHGroup_Type()
)
tmnxIkePolicyPFSDHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyPFSDHGroup.setStatus("current")


class _TmnxIkePolicyAuthAlgorithm_Type(TmnxAuthAlgorithm):
    """Custom type tmnxIkePolicyAuthAlgorithm based on TmnxAuthAlgorithm"""
    defaultValue = 3


_TmnxIkePolicyAuthAlgorithm_Type.__name__ = "TmnxAuthAlgorithm"
_TmnxIkePolicyAuthAlgorithm_Object = MibTableColumn
tmnxIkePolicyAuthAlgorithm = _TmnxIkePolicyAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 9),
    _TmnxIkePolicyAuthAlgorithm_Type()
)
tmnxIkePolicyAuthAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyAuthAlgorithm.setStatus("obsolete")


class _TmnxIkePolicyEncrAlgorithm_Type(TmnxEncrAlgorithm):
    """Custom type tmnxIkePolicyEncrAlgorithm based on TmnxEncrAlgorithm"""
    defaultValue = 4


_TmnxIkePolicyEncrAlgorithm_Type.__name__ = "TmnxEncrAlgorithm"
_TmnxIkePolicyEncrAlgorithm_Object = MibTableColumn
tmnxIkePolicyEncrAlgorithm = _TmnxIkePolicyEncrAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 10),
    _TmnxIkePolicyEncrAlgorithm_Type()
)
tmnxIkePolicyEncrAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyEncrAlgorithm.setStatus("obsolete")


class _TmnxIkePolicyIsakmpLifeTime_Type(Unsigned32):
    """Custom type tmnxIkePolicyIsakmpLifeTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 172800),
    )


_TmnxIkePolicyIsakmpLifeTime_Type.__name__ = "Unsigned32"
_TmnxIkePolicyIsakmpLifeTime_Object = MibTableColumn
tmnxIkePolicyIsakmpLifeTime = _TmnxIkePolicyIsakmpLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 11),
    _TmnxIkePolicyIsakmpLifeTime_Type()
)
tmnxIkePolicyIsakmpLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyIsakmpLifeTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxIkePolicyIsakmpLifeTime.setUnits("seconds")


class _TmnxIkePolicyIPsecLifeTime_Type(Unsigned32):
    """Custom type tmnxIkePolicyIPsecLifeTime based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 31536000),
    )


_TmnxIkePolicyIPsecLifeTime_Type.__name__ = "Unsigned32"
_TmnxIkePolicyIPsecLifeTime_Object = MibTableColumn
tmnxIkePolicyIPsecLifeTime = _TmnxIkePolicyIPsecLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 12),
    _TmnxIkePolicyIPsecLifeTime_Type()
)
tmnxIkePolicyIPsecLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyIPsecLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIkePolicyIPsecLifeTime.setUnits("seconds")


class _TmnxIkePolicyNatTraversal_Type(Integer32):
    """Custom type tmnxIkePolicyNatTraversal based on Integer32"""
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
        *(("enable", 1),
          ("disable", 2),
          ("force", 3))
    )


_TmnxIkePolicyNatTraversal_Type.__name__ = "Integer32"
_TmnxIkePolicyNatTraversal_Object = MibTableColumn
tmnxIkePolicyNatTraversal = _TmnxIkePolicyNatTraversal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 13),
    _TmnxIkePolicyNatTraversal_Type()
)
tmnxIkePolicyNatTraversal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyNatTraversal.setStatus("current")


class _TmnxIkePolicyNatTKeepAliveIntvl_Type(Unsigned32):
    """Custom type tmnxIkePolicyNatTKeepAliveIntvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 600),
    )


_TmnxIkePolicyNatTKeepAliveIntvl_Type.__name__ = "Unsigned32"
_TmnxIkePolicyNatTKeepAliveIntvl_Object = MibTableColumn
tmnxIkePolicyNatTKeepAliveIntvl = _TmnxIkePolicyNatTKeepAliveIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 14),
    _TmnxIkePolicyNatTKeepAliveIntvl_Type()
)
tmnxIkePolicyNatTKeepAliveIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyNatTKeepAliveIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIkePolicyNatTKeepAliveIntvl.setUnits("seconds")


class _TmnxIkePolicyNatTBehindNatOnly_Type(TruthValue):
    """Custom type tmnxIkePolicyNatTBehindNatOnly based on TruthValue"""
    defaultValue = 1


_TmnxIkePolicyNatTBehindNatOnly_Type.__name__ = "TruthValue"
_TmnxIkePolicyNatTBehindNatOnly_Object = MibTableColumn
tmnxIkePolicyNatTBehindNatOnly = _TmnxIkePolicyNatTBehindNatOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 15),
    _TmnxIkePolicyNatTBehindNatOnly_Type()
)
tmnxIkePolicyNatTBehindNatOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyNatTBehindNatOnly.setStatus("current")


class _TmnxIkePolicyDpd_Type(Integer32):
    """Custom type tmnxIkePolicyDpd based on Integer32"""
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
        *(("enable", 1),
          ("disable", 2),
          ("replyOnly", 3))
    )


_TmnxIkePolicyDpd_Type.__name__ = "Integer32"
_TmnxIkePolicyDpd_Object = MibTableColumn
tmnxIkePolicyDpd = _TmnxIkePolicyDpd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 16),
    _TmnxIkePolicyDpd_Type()
)
tmnxIkePolicyDpd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyDpd.setStatus("current")


class _TmnxIkePolicyDpdInterval_Type(Unsigned32):
    """Custom type tmnxIkePolicyDpdInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_TmnxIkePolicyDpdInterval_Type.__name__ = "Unsigned32"
_TmnxIkePolicyDpdInterval_Object = MibTableColumn
tmnxIkePolicyDpdInterval = _TmnxIkePolicyDpdInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 17),
    _TmnxIkePolicyDpdInterval_Type()
)
tmnxIkePolicyDpdInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyDpdInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIkePolicyDpdInterval.setUnits("seconds")


class _TmnxIkePolicyDpdMaxRetries_Type(Unsigned32):
    """Custom type tmnxIkePolicyDpdMaxRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_TmnxIkePolicyDpdMaxRetries_Type.__name__ = "Unsigned32"
_TmnxIkePolicyDpdMaxRetries_Object = MibTableColumn
tmnxIkePolicyDpdMaxRetries = _TmnxIkePolicyDpdMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 18),
    _TmnxIkePolicyDpdMaxRetries_Type()
)
tmnxIkePolicyDpdMaxRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyDpdMaxRetries.setStatus("current")


class _TmnxIkePolicyAuthMethod_Type(TmnxIkePolicyAuthMethod):
    """Custom type tmnxIkePolicyAuthMethod based on TmnxIkePolicyAuthMethod"""
    defaultValue = 1


_TmnxIkePolicyAuthMethod_Type.__name__ = "TmnxIkePolicyAuthMethod"
_TmnxIkePolicyAuthMethod_Object = MibTableColumn
tmnxIkePolicyAuthMethod = _TmnxIkePolicyAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 19),
    _TmnxIkePolicyAuthMethod_Type()
)
tmnxIkePolicyAuthMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyAuthMethod.setStatus("current")


class _TmnxIkePolicyIkeVersion_Type(TmnxIkeVersion):
    """Custom type tmnxIkePolicyIkeVersion based on TmnxIkeVersion"""
    defaultValue = 1


_TmnxIkePolicyIkeVersion_Type.__name__ = "TmnxIkeVersion"
_TmnxIkePolicyIkeVersion_Object = MibTableColumn
tmnxIkePolicyIkeVersion = _TmnxIkePolicyIkeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 20),
    _TmnxIkePolicyIkeVersion_Type()
)
tmnxIkePolicyIkeVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyIkeVersion.setStatus("current")


class _TmnxIkePolicyOwnAuthMethod_Type(TmnxIkePolicyOwnAuthMethod):
    """Custom type tmnxIkePolicyOwnAuthMethod based on TmnxIkePolicyOwnAuthMethod"""
    defaultValue = 0


_TmnxIkePolicyOwnAuthMethod_Type.__name__ = "TmnxIkePolicyOwnAuthMethod"
_TmnxIkePolicyOwnAuthMethod_Object = MibTableColumn
tmnxIkePolicyOwnAuthMethod = _TmnxIkePolicyOwnAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 21),
    _TmnxIkePolicyOwnAuthMethod_Type()
)
tmnxIkePolicyOwnAuthMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyOwnAuthMethod.setStatus("current")


class _TmnxIkePolicyMatchPeerToCert_Type(TruthValue):
    """Custom type tmnxIkePolicyMatchPeerToCert based on TruthValue"""
    defaultValue = 2


_TmnxIkePolicyMatchPeerToCert_Type.__name__ = "TruthValue"
_TmnxIkePolicyMatchPeerToCert_Object = MibTableColumn
tmnxIkePolicyMatchPeerToCert = _TmnxIkePolicyMatchPeerToCert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 22),
    _TmnxIkePolicyMatchPeerToCert_Type()
)
tmnxIkePolicyMatchPeerToCert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyMatchPeerToCert.setStatus("current")


class _TmnxIkePolicyRelayUnSolCfgAttr_Type(TmnxIkePolicyRelayUnSolCfgAttr):
    """Custom type tmnxIkePolicyRelayUnSolCfgAttr based on TmnxIkePolicyRelayUnSolCfgAttr"""
    defaultBinValue = "0"


_TmnxIkePolicyRelayUnSolCfgAttr_Type.__name__ = "TmnxIkePolicyRelayUnSolCfgAttr"
_TmnxIkePolicyRelayUnSolCfgAttr_Object = MibTableColumn
tmnxIkePolicyRelayUnSolCfgAttr = _TmnxIkePolicyRelayUnSolCfgAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 23),
    _TmnxIkePolicyRelayUnSolCfgAttr_Type()
)
tmnxIkePolicyRelayUnSolCfgAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyRelayUnSolCfgAttr.setStatus("current")


class _TmnxIkePolicyAutoEapMethod_Type(TmnxIkePolicyAutoEapMethod):
    """Custom type tmnxIkePolicyAutoEapMethod based on TmnxIkePolicyAutoEapMethod"""
    defaultValue = 2


_TmnxIkePolicyAutoEapMethod_Type.__name__ = "TmnxIkePolicyAutoEapMethod"
_TmnxIkePolicyAutoEapMethod_Object = MibTableColumn
tmnxIkePolicyAutoEapMethod = _TmnxIkePolicyAutoEapMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 24),
    _TmnxIkePolicyAutoEapMethod_Type()
)
tmnxIkePolicyAutoEapMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyAutoEapMethod.setStatus("current")


class _TmnxIkePolicyAutoEapOwnMethod_Type(TmnxIkePolicyAutoEapOwnMethod):
    """Custom type tmnxIkePolicyAutoEapOwnMethod based on TmnxIkePolicyAutoEapOwnMethod"""
    defaultValue = 2


_TmnxIkePolicyAutoEapOwnMethod_Type.__name__ = "TmnxIkePolicyAutoEapOwnMethod"
_TmnxIkePolicyAutoEapOwnMethod_Object = MibTableColumn
tmnxIkePolicyAutoEapOwnMethod = _TmnxIkePolicyAutoEapOwnMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 25),
    _TmnxIkePolicyAutoEapOwnMethod_Type()
)
tmnxIkePolicyAutoEapOwnMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyAutoEapOwnMethod.setStatus("current")


class _TmnxIkePolicyLockout_Type(TmnxEnabledDisabled):
    """Custom type tmnxIkePolicyLockout based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxIkePolicyLockout_Type.__name__ = "TmnxEnabledDisabled"
_TmnxIkePolicyLockout_Object = MibTableColumn
tmnxIkePolicyLockout = _TmnxIkePolicyLockout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 26),
    _TmnxIkePolicyLockout_Type()
)
tmnxIkePolicyLockout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyLockout.setStatus("current")


class _TmnxIkePolicyLockoutFailedAtempt_Type(Unsigned32):
    """Custom type tmnxIkePolicyLockoutFailedAtempt based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TmnxIkePolicyLockoutFailedAtempt_Type.__name__ = "Unsigned32"
_TmnxIkePolicyLockoutFailedAtempt_Object = MibTableColumn
tmnxIkePolicyLockoutFailedAtempt = _TmnxIkePolicyLockoutFailedAtempt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 27),
    _TmnxIkePolicyLockoutFailedAtempt_Type()
)
tmnxIkePolicyLockoutFailedAtempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyLockoutFailedAtempt.setStatus("current")


class _TmnxIkePolicyLockoutDuration_Type(Unsigned32):
    """Custom type tmnxIkePolicyLockoutDuration based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxIkePolicyLockoutDuration_Type.__name__ = "Unsigned32"
_TmnxIkePolicyLockoutDuration_Object = MibTableColumn
tmnxIkePolicyLockoutDuration = _TmnxIkePolicyLockoutDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 28),
    _TmnxIkePolicyLockoutDuration_Type()
)
tmnxIkePolicyLockoutDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyLockoutDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIkePolicyLockoutDuration.setUnits("minutes")


class _TmnxIkePolicyLockoutBlock_Type(Unsigned32):
    """Custom type tmnxIkePolicyLockoutBlock based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1440),
    )


_TmnxIkePolicyLockoutBlock_Type.__name__ = "Unsigned32"
_TmnxIkePolicyLockoutBlock_Object = MibTableColumn
tmnxIkePolicyLockoutBlock = _TmnxIkePolicyLockoutBlock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 29),
    _TmnxIkePolicyLockoutBlock_Type()
)
tmnxIkePolicyLockoutBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyLockoutBlock.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIkePolicyLockoutBlock.setUnits("minutes")


class _TmnxIkePolicyLockoutMaxPortPerIp_Type(Unsigned32):
    """Custom type tmnxIkePolicyLockoutMaxPortPerIp based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
    )


_TmnxIkePolicyLockoutMaxPortPerIp_Type.__name__ = "Unsigned32"
_TmnxIkePolicyLockoutMaxPortPerIp_Object = MibTableColumn
tmnxIkePolicyLockoutMaxPortPerIp = _TmnxIkePolicyLockoutMaxPortPerIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 30),
    _TmnxIkePolicyLockoutMaxPortPerIp_Type()
)
tmnxIkePolicyLockoutMaxPortPerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyLockoutMaxPortPerIp.setStatus("current")


class _TmnxIkePolicyV2Fragment_Type(TmnxEnabledDisabled):
    """Custom type tmnxIkePolicyV2Fragment based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxIkePolicyV2Fragment_Type.__name__ = "TmnxEnabledDisabled"
_TmnxIkePolicyV2Fragment_Object = MibTableColumn
tmnxIkePolicyV2Fragment = _TmnxIkePolicyV2Fragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 31),
    _TmnxIkePolicyV2Fragment_Type()
)
tmnxIkePolicyV2Fragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyV2Fragment.setStatus("current")


class _TmnxIkePolicyV2FragmentMtu_Type(Unsigned32):
    """Custom type tmnxIkePolicyV2FragmentMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9000),
    )


_TmnxIkePolicyV2FragmentMtu_Type.__name__ = "Unsigned32"
_TmnxIkePolicyV2FragmentMtu_Object = MibTableColumn
tmnxIkePolicyV2FragmentMtu = _TmnxIkePolicyV2FragmentMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 32),
    _TmnxIkePolicyV2FragmentMtu_Type()
)
tmnxIkePolicyV2FragmentMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyV2FragmentMtu.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIkePolicyV2FragmentMtu.setUnits("octets")


class _TmnxIkePolicyV2FragReassembTmOut_Type(Unsigned32):
    """Custom type tmnxIkePolicyV2FragReassembTmOut based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxIkePolicyV2FragReassembTmOut_Type.__name__ = "Unsigned32"
_TmnxIkePolicyV2FragReassembTmOut_Object = MibTableColumn
tmnxIkePolicyV2FragReassembTmOut = _TmnxIkePolicyV2FragReassembTmOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 33),
    _TmnxIkePolicyV2FragReassembTmOut_Type()
)
tmnxIkePolicyV2FragReassembTmOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyV2FragReassembTmOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIkePolicyV2FragReassembTmOut.setUnits("seconds")


class _TmnxIkePolicySndIdrAftEapSuccess_Type(TruthValue):
    """Custom type tmnxIkePolicySndIdrAftEapSuccess based on TruthValue"""
    defaultValue = 1


_TmnxIkePolicySndIdrAftEapSuccess_Type.__name__ = "TruthValue"
_TmnxIkePolicySndIdrAftEapSuccess_Object = MibTableColumn
tmnxIkePolicySndIdrAftEapSuccess = _TmnxIkePolicySndIdrAftEapSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 34),
    _TmnxIkePolicySndIdrAftEapSuccess_Type()
)
tmnxIkePolicySndIdrAftEapSuccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicySndIdrAftEapSuccess.setStatus("current")


class _TmnxIkePolicyIkev1Ph1RespDelNtfy_Type(TruthValue):
    """Custom type tmnxIkePolicyIkev1Ph1RespDelNtfy based on TruthValue"""
    defaultValue = 1


_TmnxIkePolicyIkev1Ph1RespDelNtfy_Type.__name__ = "TruthValue"
_TmnxIkePolicyIkev1Ph1RespDelNtfy_Object = MibTableColumn
tmnxIkePolicyIkev1Ph1RespDelNtfy = _TmnxIkePolicyIkev1Ph1RespDelNtfy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 35),
    _TmnxIkePolicyIkev1Ph1RespDelNtfy_Type()
)
tmnxIkePolicyIkev1Ph1RespDelNtfy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyIkev1Ph1RespDelNtfy.setStatus("current")


class _TmnxIkePolicyLimitInitExchange_Type(TruthValue):
    """Custom type tmnxIkePolicyLimitInitExchange based on TruthValue"""
    defaultValue = 1


_TmnxIkePolicyLimitInitExchange_Type.__name__ = "TruthValue"
_TmnxIkePolicyLimitInitExchange_Object = MibTableColumn
tmnxIkePolicyLimitInitExchange = _TmnxIkePolicyLimitInitExchange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 36),
    _TmnxIkePolicyLimitInitExchange_Type()
)
tmnxIkePolicyLimitInitExchange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyLimitInitExchange.setStatus("current")


class _TmnxIkePolicyReducedMaxExchgTt_Type(Unsigned32):
    """Custom type tmnxIkePolicyReducedMaxExchgTt based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 60),
    )


_TmnxIkePolicyReducedMaxExchgTt_Type.__name__ = "Unsigned32"
_TmnxIkePolicyReducedMaxExchgTt_Object = MibTableColumn
tmnxIkePolicyReducedMaxExchgTt = _TmnxIkePolicyReducedMaxExchgTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 37),
    _TmnxIkePolicyReducedMaxExchgTt_Type()
)
tmnxIkePolicyReducedMaxExchgTt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyReducedMaxExchgTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIkePolicyReducedMaxExchgTt.setUnits("seconds")
_TmnxIPsecTunnelTableLastChanged_Type = TimeStamp
_TmnxIPsecTunnelTableLastChanged_Object = MibScalar
tmnxIPsecTunnelTableLastChanged = _TmnxIPsecTunnelTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 5),
    _TmnxIPsecTunnelTableLastChanged_Type()
)
tmnxIPsecTunnelTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelTableLastChanged.setStatus("current")
_TmnxIPsecTunnelTable_Object = MibTable
tmnxIPsecTunnelTable = _TmnxIPsecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6)
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelTable.setStatus("current")
_TmnxIPsecTunnelEntry_Object = MibTableRow
tmnxIPsecTunnelEntry = _TmnxIPsecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1)
)
tmnxIPsecTunnelEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelEntry.setStatus("current")
_TmnxIPsecTunnelName_Type = TNamedItem
_TmnxIPsecTunnelName_Object = MibTableColumn
tmnxIPsecTunnelName = _TmnxIPsecTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 1),
    _TmnxIPsecTunnelName_Type()
)
tmnxIPsecTunnelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelName.setStatus("current")
_TmnxIPsecTunnelRowStatus_Type = RowStatus
_TmnxIPsecTunnelRowStatus_Object = MibTableColumn
tmnxIPsecTunnelRowStatus = _TmnxIPsecTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 2),
    _TmnxIPsecTunnelRowStatus_Type()
)
tmnxIPsecTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelRowStatus.setStatus("current")
_TmnxIPsecTunnelLastChanged_Type = TimeStamp
_TmnxIPsecTunnelLastChanged_Object = MibTableColumn
tmnxIPsecTunnelLastChanged = _TmnxIPsecTunnelLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 3),
    _TmnxIPsecTunnelLastChanged_Type()
)
tmnxIPsecTunnelLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelLastChanged.setStatus("current")


class _TmnxIPsecTunnelDescription_Type(TItemDescription):
    """Custom type tmnxIPsecTunnelDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxIPsecTunnelDescription_Type.__name__ = "TItemDescription"
_TmnxIPsecTunnelDescription_Object = MibTableColumn
tmnxIPsecTunnelDescription = _TmnxIPsecTunnelDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 4),
    _TmnxIPsecTunnelDescription_Type()
)
tmnxIPsecTunnelDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelDescription.setStatus("current")


class _TmnxIPsecTunnelLclGwAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecTunnelLclGwAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecTunnelLclGwAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecTunnelLclGwAddrType_Object = MibTableColumn
tmnxIPsecTunnelLclGwAddrType = _TmnxIPsecTunnelLclGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 5),
    _TmnxIPsecTunnelLclGwAddrType_Type()
)
tmnxIPsecTunnelLclGwAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelLclGwAddrType.setStatus("current")


class _TmnxIPsecTunnelLclGwAddr_Type(InetAddress):
    """Custom type tmnxIPsecTunnelLclGwAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecTunnelLclGwAddr_Type.__name__ = "InetAddress"
_TmnxIPsecTunnelLclGwAddr_Object = MibTableColumn
tmnxIPsecTunnelLclGwAddr = _TmnxIPsecTunnelLclGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 6),
    _TmnxIPsecTunnelLclGwAddr_Type()
)
tmnxIPsecTunnelLclGwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelLclGwAddr.setStatus("current")


class _TmnxIPsecTunnelRemGwAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecTunnelRemGwAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecTunnelRemGwAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecTunnelRemGwAddrType_Object = MibTableColumn
tmnxIPsecTunnelRemGwAddrType = _TmnxIPsecTunnelRemGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 7),
    _TmnxIPsecTunnelRemGwAddrType_Type()
)
tmnxIPsecTunnelRemGwAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelRemGwAddrType.setStatus("current")


class _TmnxIPsecTunnelRemGwAddr_Type(InetAddress):
    """Custom type tmnxIPsecTunnelRemGwAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecTunnelRemGwAddr_Type.__name__ = "InetAddress"
_TmnxIPsecTunnelRemGwAddr_Object = MibTableColumn
tmnxIPsecTunnelRemGwAddr = _TmnxIPsecTunnelRemGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 8),
    _TmnxIPsecTunnelRemGwAddr_Type()
)
tmnxIPsecTunnelRemGwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelRemGwAddr.setStatus("current")


class _TmnxIPsecTunnelPublicSvcId_Type(TmnxServId):
    """Custom type tmnxIPsecTunnelPublicSvcId based on TmnxServId"""
    defaultValue = 0


_TmnxIPsecTunnelPublicSvcId_Type.__name__ = "TmnxServId"
_TmnxIPsecTunnelPublicSvcId_Object = MibTableColumn
tmnxIPsecTunnelPublicSvcId = _TmnxIPsecTunnelPublicSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 9),
    _TmnxIPsecTunnelPublicSvcId_Type()
)
tmnxIPsecTunnelPublicSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelPublicSvcId.setStatus("current")


class _TmnxIPsecTunnelSecurityPolicyId_Type(TmnxIPsecPolicyIdOrZero):
    """Custom type tmnxIPsecTunnelSecurityPolicyId based on TmnxIPsecPolicyIdOrZero"""
    defaultValue = 0


_TmnxIPsecTunnelSecurityPolicyId_Type.__name__ = "TmnxIPsecPolicyIdOrZero"
_TmnxIPsecTunnelSecurityPolicyId_Object = MibTableColumn
tmnxIPsecTunnelSecurityPolicyId = _TmnxIPsecTunnelSecurityPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 10),
    _TmnxIPsecTunnelSecurityPolicyId_Type()
)
tmnxIPsecTunnelSecurityPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelSecurityPolicyId.setStatus("current")


class _TmnxIPsecTunnelKeyingType_Type(TmnxIPsecKeyingType):
    """Custom type tmnxIPsecTunnelKeyingType based on TmnxIPsecKeyingType"""
    defaultValue = 0


_TmnxIPsecTunnelKeyingType_Type.__name__ = "TmnxIPsecKeyingType"
_TmnxIPsecTunnelKeyingType_Object = MibTableColumn
tmnxIPsecTunnelKeyingType = _TmnxIPsecTunnelKeyingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 11),
    _TmnxIPsecTunnelKeyingType_Type()
)
tmnxIPsecTunnelKeyingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelKeyingType.setStatus("current")


class _TmnxIPsecTunnelDynTransformId1_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tmnxIPsecTunnelDynTransformId1 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TmnxIPsecTunnelDynTransformId1_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TmnxIPsecTunnelDynTransformId1_Object = MibTableColumn
tmnxIPsecTunnelDynTransformId1 = _TmnxIPsecTunnelDynTransformId1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 12),
    _TmnxIPsecTunnelDynTransformId1_Type()
)
tmnxIPsecTunnelDynTransformId1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelDynTransformId1.setStatus("current")


class _TmnxIPsecTunnelDynTransformId2_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tmnxIPsecTunnelDynTransformId2 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TmnxIPsecTunnelDynTransformId2_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TmnxIPsecTunnelDynTransformId2_Object = MibTableColumn
tmnxIPsecTunnelDynTransformId2 = _TmnxIPsecTunnelDynTransformId2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 13),
    _TmnxIPsecTunnelDynTransformId2_Type()
)
tmnxIPsecTunnelDynTransformId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelDynTransformId2.setStatus("current")


class _TmnxIPsecTunnelDynTransformId3_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tmnxIPsecTunnelDynTransformId3 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TmnxIPsecTunnelDynTransformId3_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TmnxIPsecTunnelDynTransformId3_Object = MibTableColumn
tmnxIPsecTunnelDynTransformId3 = _TmnxIPsecTunnelDynTransformId3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 14),
    _TmnxIPsecTunnelDynTransformId3_Type()
)
tmnxIPsecTunnelDynTransformId3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelDynTransformId3.setStatus("current")


class _TmnxIPsecTunnelDynTransformId4_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tmnxIPsecTunnelDynTransformId4 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TmnxIPsecTunnelDynTransformId4_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TmnxIPsecTunnelDynTransformId4_Object = MibTableColumn
tmnxIPsecTunnelDynTransformId4 = _TmnxIPsecTunnelDynTransformId4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 15),
    _TmnxIPsecTunnelDynTransformId4_Type()
)
tmnxIPsecTunnelDynTransformId4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelDynTransformId4.setStatus("current")


class _TmnxIPsecTunnelIkePolicyId_Type(TmnxIkePolicyIdOrZero):
    """Custom type tmnxIPsecTunnelIkePolicyId based on TmnxIkePolicyIdOrZero"""
    defaultValue = 0


_TmnxIPsecTunnelIkePolicyId_Type.__name__ = "TmnxIkePolicyIdOrZero"
_TmnxIPsecTunnelIkePolicyId_Object = MibTableColumn
tmnxIPsecTunnelIkePolicyId = _TmnxIPsecTunnelIkePolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 16),
    _TmnxIPsecTunnelIkePolicyId_Type()
)
tmnxIPsecTunnelIkePolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIkePolicyId.setStatus("current")


class _TmnxIPsecTunnelIkePreSharedKey_Type(OctetString):
    """Custom type tmnxIPsecTunnelIkePreSharedKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxIPsecTunnelIkePreSharedKey_Type.__name__ = "OctetString"
_TmnxIPsecTunnelIkePreSharedKey_Object = MibTableColumn
tmnxIPsecTunnelIkePreSharedKey = _TmnxIPsecTunnelIkePreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 17),
    _TmnxIPsecTunnelIkePreSharedKey_Type()
)
tmnxIPsecTunnelIkePreSharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIkePreSharedKey.setStatus("current")


class _TmnxIPsecTunnelAdminState_Type(TmnxAdminState):
    """Custom type tmnxIPsecTunnelAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIPsecTunnelAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIPsecTunnelAdminState_Object = MibTableColumn
tmnxIPsecTunnelAdminState = _TmnxIPsecTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 18),
    _TmnxIPsecTunnelAdminState_Type()
)
tmnxIPsecTunnelAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelAdminState.setStatus("current")
_TmnxIPsecTunnelOperState_Type = TmnxIPsecOperState
_TmnxIPsecTunnelOperState_Object = MibTableColumn
tmnxIPsecTunnelOperState = _TmnxIPsecTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 19),
    _TmnxIPsecTunnelOperState_Type()
)
tmnxIPsecTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelOperState.setStatus("current")


class _TmnxIPsecTunnelOperFlags_Type(Bits):
    """Custom type tmnxIPsecTunnelOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("unresolvedLocalIp", 0),
          ("tunnelAdminDown", 1),
          ("sapDown", 2),
          ("unresolvedPublicSvc", 3),
          ("bfdSessionDown", 4),
          ("reserved1", 5),
          ("unresolvedDstIp", 6),
          ("invalidCertFile", 7),
          ("invalidKeyFile", 8),
          ("trustAnchorsDown", 9),
          ("certProfileDown", 10),
          ("invalidCertKeyCombo", 11))
    )

_TmnxIPsecTunnelOperFlags_Type.__name__ = "Bits"
_TmnxIPsecTunnelOperFlags_Object = MibTableColumn
tmnxIPsecTunnelOperFlags = _TmnxIPsecTunnelOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 20),
    _TmnxIPsecTunnelOperFlags_Type()
)
tmnxIPsecTunnelOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelOperFlags.setStatus("current")


class _TmnxIPsecTunnelReplayWindow_Type(Unsigned32):
    """Custom type tmnxIPsecTunnelReplayWindow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
    )


_TmnxIPsecTunnelReplayWindow_Type.__name__ = "Unsigned32"
_TmnxIPsecTunnelReplayWindow_Object = MibTableColumn
tmnxIPsecTunnelReplayWindow = _TmnxIPsecTunnelReplayWindow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 21),
    _TmnxIPsecTunnelReplayWindow_Type()
)
tmnxIPsecTunnelReplayWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelReplayWindow.setStatus("current")


class _TmnxIPsecTunnelAutoEstablish_Type(TruthValue):
    """Custom type tmnxIPsecTunnelAutoEstablish based on TruthValue"""
    defaultValue = 2


_TmnxIPsecTunnelAutoEstablish_Type.__name__ = "TruthValue"
_TmnxIPsecTunnelAutoEstablish_Object = MibTableColumn
tmnxIPsecTunnelAutoEstablish = _TmnxIPsecTunnelAutoEstablish_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 22),
    _TmnxIPsecTunnelAutoEstablish_Type()
)
tmnxIPsecTunnelAutoEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelAutoEstablish.setStatus("current")


class _TmnxIPsecTunnelBfdDesignate_Type(TruthValue):
    """Custom type tmnxIPsecTunnelBfdDesignate based on TruthValue"""
    defaultValue = 2


_TmnxIPsecTunnelBfdDesignate_Type.__name__ = "TruthValue"
_TmnxIPsecTunnelBfdDesignate_Object = MibTableColumn
tmnxIPsecTunnelBfdDesignate = _TmnxIPsecTunnelBfdDesignate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 23),
    _TmnxIPsecTunnelBfdDesignate_Type()
)
tmnxIPsecTunnelBfdDesignate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdDesignate.setStatus("current")


class _TmnxIPsecTunnelCertTrustAnchor_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecTunnelCertTrustAnchor based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecTunnelCertTrustAnchor_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecTunnelCertTrustAnchor_Object = MibTableColumn
tmnxIPsecTunnelCertTrustAnchor = _TmnxIPsecTunnelCertTrustAnchor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 24),
    _TmnxIPsecTunnelCertTrustAnchor_Type()
)
tmnxIPsecTunnelCertTrustAnchor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCertTrustAnchor.setStatus("obsolete")


class _TmnxIPsecTunnelCertFile_Type(DisplayString):
    """Custom type tmnxIPsecTunnelCertFile based on DisplayString"""
    defaultHexValue = ""


_TmnxIPsecTunnelCertFile_Type.__name__ = "DisplayString"
_TmnxIPsecTunnelCertFile_Object = MibTableColumn
tmnxIPsecTunnelCertFile = _TmnxIPsecTunnelCertFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 25),
    _TmnxIPsecTunnelCertFile_Type()
)
tmnxIPsecTunnelCertFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCertFile.setStatus("obsolete")


class _TmnxIPsecTunnelKeyFile_Type(DisplayString):
    """Custom type tmnxIPsecTunnelKeyFile based on DisplayString"""
    defaultHexValue = ""


_TmnxIPsecTunnelKeyFile_Type.__name__ = "DisplayString"
_TmnxIPsecTunnelKeyFile_Object = MibTableColumn
tmnxIPsecTunnelKeyFile = _TmnxIPsecTunnelKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 26),
    _TmnxIPsecTunnelKeyFile_Type()
)
tmnxIPsecTunnelKeyFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelKeyFile.setStatus("obsolete")


class _TmnxIPsecTunnelLocalIdType_Type(TmnxIPsecLocalIdType):
    """Custom type tmnxIPsecTunnelLocalIdType based on TmnxIPsecLocalIdType"""
    defaultValue = 0


_TmnxIPsecTunnelLocalIdType_Type.__name__ = "TmnxIPsecLocalIdType"
_TmnxIPsecTunnelLocalIdType_Object = MibTableColumn
tmnxIPsecTunnelLocalIdType = _TmnxIPsecTunnelLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 27),
    _TmnxIPsecTunnelLocalIdType_Type()
)
tmnxIPsecTunnelLocalIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelLocalIdType.setStatus("current")


class _TmnxIPsecTunnelLocalIdValue_Type(DisplayString):
    """Custom type tmnxIPsecTunnelLocalIdValue based on DisplayString"""
    defaultHexValue = ""


_TmnxIPsecTunnelLocalIdValue_Type.__name__ = "DisplayString"
_TmnxIPsecTunnelLocalIdValue_Object = MibTableColumn
tmnxIPsecTunnelLocalIdValue = _TmnxIPsecTunnelLocalIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 28),
    _TmnxIPsecTunnelLocalIdValue_Type()
)
tmnxIPsecTunnelLocalIdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelLocalIdValue.setStatus("current")


class _TmnxIPsecTunnelClearDfBit_Type(TruthValue):
    """Custom type tmnxIPsecTunnelClearDfBit based on TruthValue"""
    defaultValue = 2


_TmnxIPsecTunnelClearDfBit_Type.__name__ = "TruthValue"
_TmnxIPsecTunnelClearDfBit_Object = MibTableColumn
tmnxIPsecTunnelClearDfBit = _TmnxIPsecTunnelClearDfBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 29),
    _TmnxIPsecTunnelClearDfBit_Type()
)
tmnxIPsecTunnelClearDfBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelClearDfBit.setStatus("current")


class _TmnxIPsecTunnelIpMtu_Type(Unsigned32):
    """Custom type tmnxIPsecTunnelIpMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TmnxIPsecTunnelIpMtu_Type.__name__ = "Unsigned32"
_TmnxIPsecTunnelIpMtu_Object = MibTableColumn
tmnxIPsecTunnelIpMtu = _TmnxIPsecTunnelIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 30),
    _TmnxIPsecTunnelIpMtu_Type()
)
tmnxIPsecTunnelIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIpMtu.setStatus("current")
_TmnxIPsecTunnelHostISA_Type = TmnxHwIndexOrZero
_TmnxIPsecTunnelHostISA_Object = MibTableColumn
tmnxIPsecTunnelHostISA = _TmnxIPsecTunnelHostISA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 31),
    _TmnxIPsecTunnelHostISA_Type()
)
tmnxIPsecTunnelHostISA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelHostISA.setStatus("current")


class _TmnxIPsecTunnelCSVPrimary_Type(TmnxCertRevStatus):
    """Custom type tmnxIPsecTunnelCSVPrimary based on TmnxCertRevStatus"""
    defaultValue = 1


_TmnxIPsecTunnelCSVPrimary_Type.__name__ = "TmnxCertRevStatus"
_TmnxIPsecTunnelCSVPrimary_Object = MibTableColumn
tmnxIPsecTunnelCSVPrimary = _TmnxIPsecTunnelCSVPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 32),
    _TmnxIPsecTunnelCSVPrimary_Type()
)
tmnxIPsecTunnelCSVPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCSVPrimary.setStatus("current")


class _TmnxIPsecTunnelCSVSecondary_Type(TmnxCertRevStatusOrNone):
    """Custom type tmnxIPsecTunnelCSVSecondary based on TmnxCertRevStatusOrNone"""
    defaultValue = 0


_TmnxIPsecTunnelCSVSecondary_Type.__name__ = "TmnxCertRevStatusOrNone"
_TmnxIPsecTunnelCSVSecondary_Object = MibTableColumn
tmnxIPsecTunnelCSVSecondary = _TmnxIPsecTunnelCSVSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 33),
    _TmnxIPsecTunnelCSVSecondary_Type()
)
tmnxIPsecTunnelCSVSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCSVSecondary.setStatus("current")


class _TmnxIPsecTunnelCSVDefResult_Type(Integer32):
    """Custom type tmnxIPsecTunnelCSVDefResult based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("revoked", 0),
          ("good", 1))
    )


_TmnxIPsecTunnelCSVDefResult_Type.__name__ = "Integer32"
_TmnxIPsecTunnelCSVDefResult_Object = MibTableColumn
tmnxIPsecTunnelCSVDefResult = _TmnxIPsecTunnelCSVDefResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 34),
    _TmnxIPsecTunnelCSVDefResult_Type()
)
tmnxIPsecTunnelCSVDefResult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCSVDefResult.setStatus("current")


class _TmnxIPsecTunnelCertProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecTunnelCertProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecTunnelCertProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecTunnelCertProfile_Object = MibTableColumn
tmnxIPsecTunnelCertProfile = _TmnxIPsecTunnelCertProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 35),
    _TmnxIPsecTunnelCertProfile_Type()
)
tmnxIPsecTunnelCertProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCertProfile.setStatus("current")
_TmnxIPsecTunnelMatchTrustAnchor_Type = TNamedItemOrEmpty
_TmnxIPsecTunnelMatchTrustAnchor_Object = MibTableColumn
tmnxIPsecTunnelMatchTrustAnchor = _TmnxIPsecTunnelMatchTrustAnchor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 36),
    _TmnxIPsecTunnelMatchTrustAnchor_Type()
)
tmnxIPsecTunnelMatchTrustAnchor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelMatchTrustAnchor.setStatus("current")


class _TmnxIPsecTunnelCertTrstAnchrProf_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecTunnelCertTrstAnchrProf based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecTunnelCertTrstAnchrProf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecTunnelCertTrstAnchrProf_Object = MibTableColumn
tmnxIPsecTunnelCertTrstAnchrProf = _TmnxIPsecTunnelCertTrstAnchrProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 37),
    _TmnxIPsecTunnelCertTrstAnchrProf_Type()
)
tmnxIPsecTunnelCertTrstAnchrProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCertTrstAnchrProf.setStatus("current")


class _TmnxIPsecTunnelEncapIpMtu_Type(Unsigned32):
    """Custom type tmnxIPsecTunnelEncapIpMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TmnxIPsecTunnelEncapIpMtu_Type.__name__ = "Unsigned32"
_TmnxIPsecTunnelEncapIpMtu_Object = MibTableColumn
tmnxIPsecTunnelEncapIpMtu = _TmnxIPsecTunnelEncapIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 38),
    _TmnxIPsecTunnelEncapIpMtu_Type()
)
tmnxIPsecTunnelEncapIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelEncapIpMtu.setStatus("current")


class _TmnxIPsecTunnelIcmp6Pkt2Big_Type(TruthValue):
    """Custom type tmnxIPsecTunnelIcmp6Pkt2Big based on TruthValue"""
    defaultValue = 1


_TmnxIPsecTunnelIcmp6Pkt2Big_Type.__name__ = "TruthValue"
_TmnxIPsecTunnelIcmp6Pkt2Big_Object = MibTableColumn
tmnxIPsecTunnelIcmp6Pkt2Big = _TmnxIPsecTunnelIcmp6Pkt2Big_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 40),
    _TmnxIPsecTunnelIcmp6Pkt2Big_Type()
)
tmnxIPsecTunnelIcmp6Pkt2Big.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIcmp6Pkt2Big.setStatus("current")


class _TmnxIPsecTunnelIcmp6NumPkt2Big_Type(Unsigned32):
    """Custom type tmnxIPsecTunnelIcmp6NumPkt2Big based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TmnxIPsecTunnelIcmp6NumPkt2Big_Type.__name__ = "Unsigned32"
_TmnxIPsecTunnelIcmp6NumPkt2Big_Object = MibTableColumn
tmnxIPsecTunnelIcmp6NumPkt2Big = _TmnxIPsecTunnelIcmp6NumPkt2Big_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 41),
    _TmnxIPsecTunnelIcmp6NumPkt2Big_Type()
)
tmnxIPsecTunnelIcmp6NumPkt2Big.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIcmp6NumPkt2Big.setStatus("current")


class _TmnxIPsecTunnelIcmp6Pkt2BigTime_Type(Unsigned32):
    """Custom type tmnxIPsecTunnelIcmp6Pkt2BigTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxIPsecTunnelIcmp6Pkt2BigTime_Type.__name__ = "Unsigned32"
_TmnxIPsecTunnelIcmp6Pkt2BigTime_Object = MibTableColumn
tmnxIPsecTunnelIcmp6Pkt2BigTime = _TmnxIPsecTunnelIcmp6Pkt2BigTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 42),
    _TmnxIPsecTunnelIcmp6Pkt2BigTime_Type()
)
tmnxIPsecTunnelIcmp6Pkt2BigTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIcmp6Pkt2BigTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIcmp6Pkt2BigTime.setUnits("seconds")
_TmnxIPsecTunnelOperChanged_Type = TimeStamp
_TmnxIPsecTunnelOperChanged_Object = MibTableColumn
tmnxIPsecTunnelOperChanged = _TmnxIPsecTunnelOperChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 43),
    _TmnxIPsecTunnelOperChanged_Type()
)
tmnxIPsecTunnelOperChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelOperChanged.setStatus("current")


class _TmnxIPsecTunnelPubTcpMssAdjust_Type(Integer32):
    """Custom type tmnxIPsecTunnelPubTcpMssAdjust based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TmnxIPsecTunnelPubTcpMssAdjust_Type.__name__ = "Integer32"
_TmnxIPsecTunnelPubTcpMssAdjust_Object = MibTableColumn
tmnxIPsecTunnelPubTcpMssAdjust = _TmnxIPsecTunnelPubTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 49),
    _TmnxIPsecTunnelPubTcpMssAdjust_Type()
)
tmnxIPsecTunnelPubTcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelPubTcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelPubTcpMssAdjust.setUnits("octets")


class _TmnxIPsecTunnelPrivTcpMssAdjust_Type(Integer32):
    """Custom type tmnxIPsecTunnelPrivTcpMssAdjust based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(512, 9000),
    )


_TmnxIPsecTunnelPrivTcpMssAdjust_Type.__name__ = "Integer32"
_TmnxIPsecTunnelPrivTcpMssAdjust_Object = MibTableColumn
tmnxIPsecTunnelPrivTcpMssAdjust = _TmnxIPsecTunnelPrivTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 50),
    _TmnxIPsecTunnelPrivTcpMssAdjust_Type()
)
tmnxIPsecTunnelPrivTcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelPrivTcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelPrivTcpMssAdjust.setUnits("octets")


class _TmnxIPsecTunnelMaxNumPh1SaKeys_Type(Unsigned32):
    """Custom type tmnxIPsecTunnelMaxNumPh1SaKeys based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TmnxIPsecTunnelMaxNumPh1SaKeys_Type.__name__ = "Unsigned32"
_TmnxIPsecTunnelMaxNumPh1SaKeys_Object = MibTableColumn
tmnxIPsecTunnelMaxNumPh1SaKeys = _TmnxIPsecTunnelMaxNumPh1SaKeys_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 51),
    _TmnxIPsecTunnelMaxNumPh1SaKeys_Type()
)
tmnxIPsecTunnelMaxNumPh1SaKeys.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelMaxNumPh1SaKeys.setStatus("current")


class _TmnxIPsecTunnelMaxNumPh2SaKeys_Type(Unsigned32):
    """Custom type tmnxIPsecTunnelMaxNumPh2SaKeys based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_TmnxIPsecTunnelMaxNumPh2SaKeys_Type.__name__ = "Unsigned32"
_TmnxIPsecTunnelMaxNumPh2SaKeys_Object = MibTableColumn
tmnxIPsecTunnelMaxNumPh2SaKeys = _TmnxIPsecTunnelMaxNumPh2SaKeys_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 52),
    _TmnxIPsecTunnelMaxNumPh2SaKeys_Type()
)
tmnxIPsecTunnelMaxNumPh2SaKeys.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelMaxNumPh2SaKeys.setStatus("current")


class _TmnxIPsecTunnelPublicSvcName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxIPsecTunnelPublicSvcName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecTunnelPublicSvcName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxIPsecTunnelPublicSvcName_Object = MibTableColumn
tmnxIPsecTunnelPublicSvcName = _TmnxIPsecTunnelPublicSvcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 53),
    _TmnxIPsecTunnelPublicSvcName_Type()
)
tmnxIPsecTunnelPublicSvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelPublicSvcName.setStatus("current")


class _TmnxIPsecTunnelSecPlyStrictMatch_Type(TruthValue):
    """Custom type tmnxIPsecTunnelSecPlyStrictMatch based on TruthValue"""
    defaultValue = 2


_TmnxIPsecTunnelSecPlyStrictMatch_Type.__name__ = "TruthValue"
_TmnxIPsecTunnelSecPlyStrictMatch_Object = MibTableColumn
tmnxIPsecTunnelSecPlyStrictMatch = _TmnxIPsecTunnelSecPlyStrictMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 54),
    _TmnxIPsecTunnelSecPlyStrictMatch_Type()
)
tmnxIPsecTunnelSecPlyStrictMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelSecPlyStrictMatch.setStatus("current")
_TmnxIPsecTunnelHostEsa_Type = TmnxEsaIdOrZero
_TmnxIPsecTunnelHostEsa_Object = MibTableColumn
tmnxIPsecTunnelHostEsa = _TmnxIPsecTunnelHostEsa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 56),
    _TmnxIPsecTunnelHostEsa_Type()
)
tmnxIPsecTunnelHostEsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelHostEsa.setStatus("current")
_TmnxIPsecTunnelHostEsaVm_Type = TmnxEsaVmIdOrZero
_TmnxIPsecTunnelHostEsaVm_Object = MibTableColumn
tmnxIPsecTunnelHostEsaVm = _TmnxIPsecTunnelHostEsaVm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 57),
    _TmnxIPsecTunnelHostEsaVm_Type()
)
tmnxIPsecTunnelHostEsaVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelHostEsaVm.setStatus("current")
_TmnxIPsecTunnelStatsTable_Object = MibTable
tmnxIPsecTunnelStatsTable = _TmnxIPsecTunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7)
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelStatsTable.setStatus("current")
_TmnxIPsecTunnelStatsEntry_Object = MibTableRow
tmnxIPsecTunnelStatsEntry = _TmnxIPsecTunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1)
)
tmnxIPsecTunnelStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelStatsEntry.setStatus("current")


class _TmnxIPsecTunnelIsakmpState_Type(Integer32):
    """Custom type tmnxIPsecTunnelIsakmpState based on Integer32"""
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


_TmnxIPsecTunnelIsakmpState_Type.__name__ = "Integer32"
_TmnxIPsecTunnelIsakmpState_Object = MibTableColumn
tmnxIPsecTunnelIsakmpState = _TmnxIPsecTunnelIsakmpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 1),
    _TmnxIPsecTunnelIsakmpState_Type()
)
tmnxIPsecTunnelIsakmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIsakmpState.setStatus("current")
_TmnxIPsecTunnelIsakmpEstabTime_Type = TimeStamp
_TmnxIPsecTunnelIsakmpEstabTime_Object = MibTableColumn
tmnxIPsecTunnelIsakmpEstabTime = _TmnxIPsecTunnelIsakmpEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 2),
    _TmnxIPsecTunnelIsakmpEstabTime_Type()
)
tmnxIPsecTunnelIsakmpEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIsakmpEstabTime.setStatus("current")
_TmnxIPsecTunnelIsakmpNegLifeTime_Type = Unsigned32
_TmnxIPsecTunnelIsakmpNegLifeTime_Object = MibTableColumn
tmnxIPsecTunnelIsakmpNegLifeTime = _TmnxIPsecTunnelIsakmpNegLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 3),
    _TmnxIPsecTunnelIsakmpNegLifeTime_Type()
)
tmnxIPsecTunnelIsakmpNegLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIsakmpNegLifeTime.setStatus("current")
_TmnxIPsecTunnelNumDpdTx_Type = Counter32
_TmnxIPsecTunnelNumDpdTx_Object = MibTableColumn
tmnxIPsecTunnelNumDpdTx = _TmnxIPsecTunnelNumDpdTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 4),
    _TmnxIPsecTunnelNumDpdTx_Type()
)
tmnxIPsecTunnelNumDpdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumDpdTx.setStatus("current")
_TmnxIPsecTunnelNumDpdRx_Type = Counter32
_TmnxIPsecTunnelNumDpdRx_Object = MibTableColumn
tmnxIPsecTunnelNumDpdRx = _TmnxIPsecTunnelNumDpdRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 5),
    _TmnxIPsecTunnelNumDpdRx_Type()
)
tmnxIPsecTunnelNumDpdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumDpdRx.setStatus("current")
_TmnxIPsecTunnelNumDpdAckTx_Type = Counter32
_TmnxIPsecTunnelNumDpdAckTx_Object = MibTableColumn
tmnxIPsecTunnelNumDpdAckTx = _TmnxIPsecTunnelNumDpdAckTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 6),
    _TmnxIPsecTunnelNumDpdAckTx_Type()
)
tmnxIPsecTunnelNumDpdAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumDpdAckTx.setStatus("current")
_TmnxIPsecTunnelNumDpdAckRx_Type = Counter32
_TmnxIPsecTunnelNumDpdAckRx_Object = MibTableColumn
tmnxIPsecTunnelNumDpdAckRx = _TmnxIPsecTunnelNumDpdAckRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 7),
    _TmnxIPsecTunnelNumDpdAckRx_Type()
)
tmnxIPsecTunnelNumDpdAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumDpdAckRx.setStatus("current")
_TmnxIPsecTunnelNumExpRx_Type = Counter32
_TmnxIPsecTunnelNumExpRx_Object = MibTableColumn
tmnxIPsecTunnelNumExpRx = _TmnxIPsecTunnelNumExpRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 8),
    _TmnxIPsecTunnelNumExpRx_Type()
)
tmnxIPsecTunnelNumExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumExpRx.setStatus("current")
_TmnxIPsecTunnelNumInvalidDpdRx_Type = Counter32
_TmnxIPsecTunnelNumInvalidDpdRx_Object = MibTableColumn
tmnxIPsecTunnelNumInvalidDpdRx = _TmnxIPsecTunnelNumInvalidDpdRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 9),
    _TmnxIPsecTunnelNumInvalidDpdRx_Type()
)
tmnxIPsecTunnelNumInvalidDpdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumInvalidDpdRx.setStatus("current")
_TmnxIPsecTunnelNumCtrlPktsTx_Type = Counter32
_TmnxIPsecTunnelNumCtrlPktsTx_Object = MibTableColumn
tmnxIPsecTunnelNumCtrlPktsTx = _TmnxIPsecTunnelNumCtrlPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 10),
    _TmnxIPsecTunnelNumCtrlPktsTx_Type()
)
tmnxIPsecTunnelNumCtrlPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumCtrlPktsTx.setStatus("current")
_TmnxIPsecTunnelNumCtrlPktsRx_Type = Counter32
_TmnxIPsecTunnelNumCtrlPktsRx_Object = MibTableColumn
tmnxIPsecTunnelNumCtrlPktsRx = _TmnxIPsecTunnelNumCtrlPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 11),
    _TmnxIPsecTunnelNumCtrlPktsRx_Type()
)
tmnxIPsecTunnelNumCtrlPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumCtrlPktsRx.setStatus("current")
_TmnxIPsecTunnelNumCtrlTxErrors_Type = Counter32
_TmnxIPsecTunnelNumCtrlTxErrors_Object = MibTableColumn
tmnxIPsecTunnelNumCtrlTxErrors = _TmnxIPsecTunnelNumCtrlTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 12),
    _TmnxIPsecTunnelNumCtrlTxErrors_Type()
)
tmnxIPsecTunnelNumCtrlTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumCtrlTxErrors.setStatus("current")
_TmnxIPsecTunnelNumCtrlRxErrors_Type = Counter32
_TmnxIPsecTunnelNumCtrlRxErrors_Object = MibTableColumn
tmnxIPsecTunnelNumCtrlRxErrors = _TmnxIPsecTunnelNumCtrlRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 13),
    _TmnxIPsecTunnelNumCtrlRxErrors_Type()
)
tmnxIPsecTunnelNumCtrlRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumCtrlRxErrors.setStatus("current")
_TmnxIPsecTunnelMatCertEntryId_Type = Integer32
_TmnxIPsecTunnelMatCertEntryId_Object = MibTableColumn
tmnxIPsecTunnelMatCertEntryId = _TmnxIPsecTunnelMatCertEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 14),
    _TmnxIPsecTunnelMatCertEntryId_Type()
)
tmnxIPsecTunnelMatCertEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelMatCertEntryId.setStatus("current")
_TmnxIPsecTunnelCertProfName_Type = TNamedItemOrEmpty
_TmnxIPsecTunnelCertProfName_Object = MibTableColumn
tmnxIPsecTunnelCertProfName = _TmnxIPsecTunnelCertProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 15),
    _TmnxIPsecTunnelCertProfName_Type()
)
tmnxIPsecTunnelCertProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCertProfName.setStatus("current")
_TmnxIPsecTunnelStatIsakmpAuthAlg_Type = TmnxAuthAlgorithm
_TmnxIPsecTunnelStatIsakmpAuthAlg_Object = MibTableColumn
tmnxIPsecTunnelStatIsakmpAuthAlg = _TmnxIPsecTunnelStatIsakmpAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 17),
    _TmnxIPsecTunnelStatIsakmpAuthAlg_Type()
)
tmnxIPsecTunnelStatIsakmpAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelStatIsakmpAuthAlg.setStatus("current")
_TmnxIPsecTunnelStatIsakmpEncrAlg_Type = TmnxEncrAlgorithm
_TmnxIPsecTunnelStatIsakmpEncrAlg_Object = MibTableColumn
tmnxIPsecTunnelStatIsakmpEncrAlg = _TmnxIPsecTunnelStatIsakmpEncrAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 18),
    _TmnxIPsecTunnelStatIsakmpEncrAlg_Type()
)
tmnxIPsecTunnelStatIsakmpEncrAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelStatIsakmpEncrAlg.setStatus("current")
_TmnxIPsecTunnelStatIsakmpPfsDhGp_Type = TmnxIkePolicyDHGroupOrZero
_TmnxIPsecTunnelStatIsakmpPfsDhGp_Object = MibTableColumn
tmnxIPsecTunnelStatIsakmpPfsDhGp = _TmnxIPsecTunnelStatIsakmpPfsDhGp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 19),
    _TmnxIPsecTunnelStatIsakmpPfsDhGp_Type()
)
tmnxIPsecTunnelStatIsakmpPfsDhGp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelStatIsakmpPfsDhGp.setStatus("current")


class _TmnxIPsecTunnelStatIkeTranPrfAlg_Type(Integer32):
    """Custom type tmnxIPsecTunnelStatIkeTranPrfAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("sha1", 3),
          ("sha256", 4),
          ("sha384", 5),
          ("sha512", 6),
          ("aesXcbc", 7),
          ("sameAsAuth", 8))
    )


_TmnxIPsecTunnelStatIkeTranPrfAlg_Type.__name__ = "Integer32"
_TmnxIPsecTunnelStatIkeTranPrfAlg_Object = MibTableColumn
tmnxIPsecTunnelStatIkeTranPrfAlg = _TmnxIPsecTunnelStatIkeTranPrfAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 20),
    _TmnxIPsecTunnelStatIkeTranPrfAlg_Type()
)
tmnxIPsecTunnelStatIkeTranPrfAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelStatIkeTranPrfAlg.setStatus("current")
_TmnxIPsecPolicyTableLastChanged_Type = TimeStamp
_TmnxIPsecPolicyTableLastChanged_Object = MibScalar
tmnxIPsecPolicyTableLastChanged = _TmnxIPsecPolicyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 8),
    _TmnxIPsecPolicyTableLastChanged_Type()
)
tmnxIPsecPolicyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyTableLastChanged.setStatus("current")
_TmnxIPsecPolicyTable_Object = MibTable
tmnxIPsecPolicyTable = _TmnxIPsecPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 9)
)
if mibBuilder.loadTexts:
    tmnxIPsecPolicyTable.setStatus("current")
_TmnxIPsecPolicyEntry_Object = MibTableRow
tmnxIPsecPolicyEntry = _TmnxIPsecPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 9, 1)
)
tmnxIPsecPolicyEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyId"),
)
if mibBuilder.loadTexts:
    tmnxIPsecPolicyEntry.setStatus("current")
_TmnxIPsecPolicyId_Type = TmnxIPsecPolicyId
_TmnxIPsecPolicyId_Object = MibTableColumn
tmnxIPsecPolicyId = _TmnxIPsecPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 9, 1, 1),
    _TmnxIPsecPolicyId_Type()
)
tmnxIPsecPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyId.setStatus("current")
_TmnxIPsecPolicyRowStatus_Type = RowStatus
_TmnxIPsecPolicyRowStatus_Object = MibTableColumn
tmnxIPsecPolicyRowStatus = _TmnxIPsecPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 9, 1, 2),
    _TmnxIPsecPolicyRowStatus_Type()
)
tmnxIPsecPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyRowStatus.setStatus("current")
_TmnxIPsecPolicyLastChanged_Type = TimeStamp
_TmnxIPsecPolicyLastChanged_Object = MibTableColumn
tmnxIPsecPolicyLastChanged = _TmnxIPsecPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 9, 1, 3),
    _TmnxIPsecPolicyLastChanged_Type()
)
tmnxIPsecPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyLastChanged.setStatus("current")
_TmnxIPsecPlcyParamsTblLastChangd_Type = TimeStamp
_TmnxIPsecPlcyParamsTblLastChangd_Object = MibScalar
tmnxIPsecPlcyParamsTblLastChangd = _TmnxIPsecPlcyParamsTblLastChangd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 10),
    _TmnxIPsecPlcyParamsTblLastChangd_Type()
)
tmnxIPsecPlcyParamsTblLastChangd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsTblLastChangd.setStatus("current")
_TmnxIPsecPolicyParamsTable_Object = MibTable
tmnxIPsecPolicyParamsTable = _TmnxIPsecPolicyParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11)
)
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsTable.setStatus("current")
_TmnxIPsecPolicyParamsEntry_Object = MibTableRow
tmnxIPsecPolicyParamsEntry = _TmnxIPsecPolicyParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1)
)
tmnxIPsecPolicyParamsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsId"),
)
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsEntry.setStatus("current")


class _TmnxIPsecPolicyParamsId_Type(Unsigned32):
    """Custom type tmnxIPsecPolicyParamsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxIPsecPolicyParamsId_Type.__name__ = "Unsigned32"
_TmnxIPsecPolicyParamsId_Object = MibTableColumn
tmnxIPsecPolicyParamsId = _TmnxIPsecPolicyParamsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 1),
    _TmnxIPsecPolicyParamsId_Type()
)
tmnxIPsecPolicyParamsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsId.setStatus("current")
_TmnxIPsecPolicyParamsRowStatus_Type = RowStatus
_TmnxIPsecPolicyParamsRowStatus_Object = MibTableColumn
tmnxIPsecPolicyParamsRowStatus = _TmnxIPsecPolicyParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 2),
    _TmnxIPsecPolicyParamsRowStatus_Type()
)
tmnxIPsecPolicyParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsRowStatus.setStatus("current")
_TmnxIPsecPolicyParamsLastChanged_Type = TimeStamp
_TmnxIPsecPolicyParamsLastChanged_Object = MibTableColumn
tmnxIPsecPolicyParamsLastChanged = _TmnxIPsecPolicyParamsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 3),
    _TmnxIPsecPolicyParamsLastChanged_Type()
)
tmnxIPsecPolicyParamsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsLastChanged.setStatus("current")


class _TmnxIPsecPolicyParamsLclAddrAny_Type(TruthValue):
    """Custom type tmnxIPsecPolicyParamsLclAddrAny based on TruthValue"""
    defaultValue = 2


_TmnxIPsecPolicyParamsLclAddrAny_Type.__name__ = "TruthValue"
_TmnxIPsecPolicyParamsLclAddrAny_Object = MibTableColumn
tmnxIPsecPolicyParamsLclAddrAny = _TmnxIPsecPolicyParamsLclAddrAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 4),
    _TmnxIPsecPolicyParamsLclAddrAny_Type()
)
tmnxIPsecPolicyParamsLclAddrAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsLclAddrAny.setStatus("current")


class _TmnxIPsecPolicyParamsLclAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecPolicyParamsLclAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecPolicyParamsLclAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecPolicyParamsLclAddrType_Object = MibTableColumn
tmnxIPsecPolicyParamsLclAddrType = _TmnxIPsecPolicyParamsLclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 5),
    _TmnxIPsecPolicyParamsLclAddrType_Type()
)
tmnxIPsecPolicyParamsLclAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsLclAddrType.setStatus("current")


class _TmnxIPsecPolicyParamsLclAddr_Type(InetAddress):
    """Custom type tmnxIPsecPolicyParamsLclAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecPolicyParamsLclAddr_Type.__name__ = "InetAddress"
_TmnxIPsecPolicyParamsLclAddr_Object = MibTableColumn
tmnxIPsecPolicyParamsLclAddr = _TmnxIPsecPolicyParamsLclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 6),
    _TmnxIPsecPolicyParamsLclAddr_Type()
)
tmnxIPsecPolicyParamsLclAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsLclAddr.setStatus("current")


class _TmnxIPsecPolicyParamsLclAPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxIPsecPolicyParamsLclAPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxIPsecPolicyParamsLclAPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxIPsecPolicyParamsLclAPrefLen_Object = MibTableColumn
tmnxIPsecPolicyParamsLclAPrefLen = _TmnxIPsecPolicyParamsLclAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 7),
    _TmnxIPsecPolicyParamsLclAPrefLen_Type()
)
tmnxIPsecPolicyParamsLclAPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsLclAPrefLen.setStatus("current")


class _TmnxIPsecPolicyParamsRemAddrAny_Type(TruthValue):
    """Custom type tmnxIPsecPolicyParamsRemAddrAny based on TruthValue"""
    defaultValue = 2


_TmnxIPsecPolicyParamsRemAddrAny_Type.__name__ = "TruthValue"
_TmnxIPsecPolicyParamsRemAddrAny_Object = MibTableColumn
tmnxIPsecPolicyParamsRemAddrAny = _TmnxIPsecPolicyParamsRemAddrAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 8),
    _TmnxIPsecPolicyParamsRemAddrAny_Type()
)
tmnxIPsecPolicyParamsRemAddrAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsRemAddrAny.setStatus("current")


class _TmnxIPsecPolicyParamsRemAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecPolicyParamsRemAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecPolicyParamsRemAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecPolicyParamsRemAddrType_Object = MibTableColumn
tmnxIPsecPolicyParamsRemAddrType = _TmnxIPsecPolicyParamsRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 9),
    _TmnxIPsecPolicyParamsRemAddrType_Type()
)
tmnxIPsecPolicyParamsRemAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsRemAddrType.setStatus("current")


class _TmnxIPsecPolicyParamsRemAddr_Type(InetAddress):
    """Custom type tmnxIPsecPolicyParamsRemAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecPolicyParamsRemAddr_Type.__name__ = "InetAddress"
_TmnxIPsecPolicyParamsRemAddr_Object = MibTableColumn
tmnxIPsecPolicyParamsRemAddr = _TmnxIPsecPolicyParamsRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 10),
    _TmnxIPsecPolicyParamsRemAddr_Type()
)
tmnxIPsecPolicyParamsRemAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsRemAddr.setStatus("current")


class _TmnxIPsecPolicyParamsRemAPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxIPsecPolicyParamsRemAPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxIPsecPolicyParamsRemAPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxIPsecPolicyParamsRemAPrefLen_Object = MibTableColumn
tmnxIPsecPolicyParamsRemAPrefLen = _TmnxIPsecPolicyParamsRemAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 11),
    _TmnxIPsecPolicyParamsRemAPrefLen_Type()
)
tmnxIPsecPolicyParamsRemAPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsRemAPrefLen.setStatus("current")


class _TmnxIPsecPlcyParamsV6LclAddrAny_Type(TruthValue):
    """Custom type tmnxIPsecPlcyParamsV6LclAddrAny based on TruthValue"""
    defaultValue = 2


_TmnxIPsecPlcyParamsV6LclAddrAny_Type.__name__ = "TruthValue"
_TmnxIPsecPlcyParamsV6LclAddrAny_Object = MibTableColumn
tmnxIPsecPlcyParamsV6LclAddrAny = _TmnxIPsecPlcyParamsV6LclAddrAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 12),
    _TmnxIPsecPlcyParamsV6LclAddrAny_Type()
)
tmnxIPsecPlcyParamsV6LclAddrAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6LclAddrAny.setStatus("current")


class _TmnxIPsecPlcyParamsV6LclAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecPlcyParamsV6LclAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecPlcyParamsV6LclAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecPlcyParamsV6LclAddrType_Object = MibTableColumn
tmnxIPsecPlcyParamsV6LclAddrType = _TmnxIPsecPlcyParamsV6LclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 13),
    _TmnxIPsecPlcyParamsV6LclAddrType_Type()
)
tmnxIPsecPlcyParamsV6LclAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6LclAddrType.setStatus("current")


class _TmnxIPsecPlcyParamsV6LclAddr_Type(InetAddress):
    """Custom type tmnxIPsecPlcyParamsV6LclAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecPlcyParamsV6LclAddr_Type.__name__ = "InetAddress"
_TmnxIPsecPlcyParamsV6LclAddr_Object = MibTableColumn
tmnxIPsecPlcyParamsV6LclAddr = _TmnxIPsecPlcyParamsV6LclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 14),
    _TmnxIPsecPlcyParamsV6LclAddr_Type()
)
tmnxIPsecPlcyParamsV6LclAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6LclAddr.setStatus("current")


class _TmnxIPsecPlcyParamsV6LclAPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxIPsecPlcyParamsV6LclAPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 128),
    )


_TmnxIPsecPlcyParamsV6LclAPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxIPsecPlcyParamsV6LclAPrefLen_Object = MibTableColumn
tmnxIPsecPlcyParamsV6LclAPrefLen = _TmnxIPsecPlcyParamsV6LclAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 15),
    _TmnxIPsecPlcyParamsV6LclAPrefLen_Type()
)
tmnxIPsecPlcyParamsV6LclAPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6LclAPrefLen.setStatus("current")


class _TmnxIPsecPlcyParamsV6RemAddrAny_Type(TruthValue):
    """Custom type tmnxIPsecPlcyParamsV6RemAddrAny based on TruthValue"""
    defaultValue = 2


_TmnxIPsecPlcyParamsV6RemAddrAny_Type.__name__ = "TruthValue"
_TmnxIPsecPlcyParamsV6RemAddrAny_Object = MibTableColumn
tmnxIPsecPlcyParamsV6RemAddrAny = _TmnxIPsecPlcyParamsV6RemAddrAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 16),
    _TmnxIPsecPlcyParamsV6RemAddrAny_Type()
)
tmnxIPsecPlcyParamsV6RemAddrAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6RemAddrAny.setStatus("current")


class _TmnxIPsecPlcyParamsV6RemAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecPlcyParamsV6RemAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecPlcyParamsV6RemAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecPlcyParamsV6RemAddrType_Object = MibTableColumn
tmnxIPsecPlcyParamsV6RemAddrType = _TmnxIPsecPlcyParamsV6RemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 17),
    _TmnxIPsecPlcyParamsV6RemAddrType_Type()
)
tmnxIPsecPlcyParamsV6RemAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6RemAddrType.setStatus("current")


class _TmnxIPsecPlcyParamsV6RemAddr_Type(InetAddress):
    """Custom type tmnxIPsecPlcyParamsV6RemAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecPlcyParamsV6RemAddr_Type.__name__ = "InetAddress"
_TmnxIPsecPlcyParamsV6RemAddr_Object = MibTableColumn
tmnxIPsecPlcyParamsV6RemAddr = _TmnxIPsecPlcyParamsV6RemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 18),
    _TmnxIPsecPlcyParamsV6RemAddr_Type()
)
tmnxIPsecPlcyParamsV6RemAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6RemAddr.setStatus("current")


class _TmnxIPsecPlcyParamsV6RemAPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxIPsecPlcyParamsV6RemAPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 128),
    )


_TmnxIPsecPlcyParamsV6RemAPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxIPsecPlcyParamsV6RemAPrefLen_Object = MibTableColumn
tmnxIPsecPlcyParamsV6RemAPrefLen = _TmnxIPsecPlcyParamsV6RemAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 19),
    _TmnxIPsecPlcyParamsV6RemAPrefLen_Type()
)
tmnxIPsecPlcyParamsV6RemAPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6RemAPrefLen.setStatus("current")
_TmnxIPsecSATableLastChanged_Type = TimeStamp
_TmnxIPsecSATableLastChanged_Object = MibScalar
tmnxIPsecSATableLastChanged = _TmnxIPsecSATableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 12),
    _TmnxIPsecSATableLastChanged_Type()
)
tmnxIPsecSATableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSATableLastChanged.setStatus("current")
_TmnxIPsecSATable_Object = MibTable
tmnxIPsecSATable = _TmnxIPsecSATable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13)
)
if mibBuilder.loadTexts:
    tmnxIPsecSATable.setStatus("current")
_TmnxIPsecSAEntry_Object = MibTableRow
tmnxIPsecSAEntry = _TmnxIPsecSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1)
)
tmnxIPsecSAEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSAId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSADirection"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSAIndex"),
)
if mibBuilder.loadTexts:
    tmnxIPsecSAEntry.setStatus("current")


class _TmnxIPsecSAId_Type(Unsigned32):
    """Custom type tmnxIPsecSAId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxIPsecSAId_Type.__name__ = "Unsigned32"
_TmnxIPsecSAId_Object = MibTableColumn
tmnxIPsecSAId = _TmnxIPsecSAId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 1),
    _TmnxIPsecSAId_Type()
)
tmnxIPsecSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecSAId.setStatus("current")


class _TmnxIPsecSAIndex_Type(Unsigned32):
    """Custom type tmnxIPsecSAIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxIPsecSAIndex_Type.__name__ = "Unsigned32"
_TmnxIPsecSAIndex_Object = MibTableColumn
tmnxIPsecSAIndex = _TmnxIPsecSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 2),
    _TmnxIPsecSAIndex_Type()
)
tmnxIPsecSAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecSAIndex.setStatus("current")
_TmnxIPsecSADirection_Type = TmnxIPsecDirection
_TmnxIPsecSADirection_Object = MibTableColumn
tmnxIPsecSADirection = _TmnxIPsecSADirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 3),
    _TmnxIPsecSADirection_Type()
)
tmnxIPsecSADirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecSADirection.setStatus("current")
_TmnxIPsecSARowStatus_Type = RowStatus
_TmnxIPsecSARowStatus_Object = MibTableColumn
tmnxIPsecSARowStatus = _TmnxIPsecSARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 4),
    _TmnxIPsecSARowStatus_Type()
)
tmnxIPsecSARowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecSARowStatus.setStatus("current")
_TmnxIPsecSALastChanged_Type = TimeStamp
_TmnxIPsecSALastChanged_Object = MibTableColumn
tmnxIPsecSALastChanged = _TmnxIPsecSALastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 5),
    _TmnxIPsecSALastChanged_Type()
)
tmnxIPsecSALastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSALastChanged.setStatus("current")
_TmnxIPsecSAType_Type = TmnxIPsecKeyingType
_TmnxIPsecSAType_Object = MibTableColumn
tmnxIPsecSAType = _TmnxIPsecSAType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 6),
    _TmnxIPsecSAType_Type()
)
tmnxIPsecSAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAType.setStatus("current")


class _TmnxIPsecSAEncryptionKey_Type(OctetString):
    """Custom type tmnxIPsecSAEncryptionKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxIPsecSAEncryptionKey_Type.__name__ = "OctetString"
_TmnxIPsecSAEncryptionKey_Object = MibTableColumn
tmnxIPsecSAEncryptionKey = _TmnxIPsecSAEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 7),
    _TmnxIPsecSAEncryptionKey_Type()
)
tmnxIPsecSAEncryptionKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecSAEncryptionKey.setStatus("current")


class _TmnxIPsecSAAuthenticationKey_Type(OctetString):
    """Custom type tmnxIPsecSAAuthenticationKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxIPsecSAAuthenticationKey_Type.__name__ = "OctetString"
_TmnxIPsecSAAuthenticationKey_Object = MibTableColumn
tmnxIPsecSAAuthenticationKey = _TmnxIPsecSAAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 8),
    _TmnxIPsecSAAuthenticationKey_Type()
)
tmnxIPsecSAAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecSAAuthenticationKey.setStatus("current")
_TmnxIPsecSASpi_Type = Unsigned32
_TmnxIPsecSASpi_Object = MibTableColumn
tmnxIPsecSASpi = _TmnxIPsecSASpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 9),
    _TmnxIPsecSASpi_Type()
)
tmnxIPsecSASpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecSASpi.setStatus("current")
_TmnxIPsecSAManualTransformId_Type = TmnxIPsecTransformIdOrZero
_TmnxIPsecSAManualTransformId_Object = MibTableColumn
tmnxIPsecSAManualTransformId = _TmnxIPsecSAManualTransformId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 10),
    _TmnxIPsecSAManualTransformId_Type()
)
tmnxIPsecSAManualTransformId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecSAManualTransformId.setStatus("current")
_TmnxIPsecSAAuthAlgorithm_Type = TmnxAuthAlgorithm
_TmnxIPsecSAAuthAlgorithm_Object = MibTableColumn
tmnxIPsecSAAuthAlgorithm = _TmnxIPsecSAAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 11),
    _TmnxIPsecSAAuthAlgorithm_Type()
)
tmnxIPsecSAAuthAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAAuthAlgorithm.setStatus("current")
_TmnxIPsecSAEncrAlgorithm_Type = TmnxEncrAlgorithm
_TmnxIPsecSAEncrAlgorithm_Object = MibTableColumn
tmnxIPsecSAEncrAlgorithm = _TmnxIPsecSAEncrAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 12),
    _TmnxIPsecSAEncrAlgorithm_Type()
)
tmnxIPsecSAEncrAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAEncrAlgorithm.setStatus("current")
_TmnxIPsecSAStorageType_Type = StorageType
_TmnxIPsecSAStorageType_Object = MibTableColumn
tmnxIPsecSAStorageType = _TmnxIPsecSAStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 13),
    _TmnxIPsecSAStorageType_Type()
)
tmnxIPsecSAStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStorageType.setStatus("current")
_TmnxIPsecSAEstablishedTime_Type = TimeStamp
_TmnxIPsecSAEstablishedTime_Object = MibTableColumn
tmnxIPsecSAEstablishedTime = _TmnxIPsecSAEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 14),
    _TmnxIPsecSAEstablishedTime_Type()
)
tmnxIPsecSAEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAEstablishedTime.setStatus("current")
_TmnxIPsecSANegotiatedLifeTime_Type = Unsigned32
_TmnxIPsecSANegotiatedLifeTime_Object = MibTableColumn
tmnxIPsecSANegotiatedLifeTime = _TmnxIPsecSANegotiatedLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 15),
    _TmnxIPsecSANegotiatedLifeTime_Type()
)
tmnxIPsecSANegotiatedLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSANegotiatedLifeTime.setStatus("current")
_TmnxIPsecSAStatsTable_Object = MibTable
tmnxIPsecSAStatsTable = _TmnxIPsecSAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14)
)
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsTable.setStatus("current")
_TmnxIPsecSAStatsEntry_Object = MibTableRow
tmnxIPsecSAStatsEntry = _TmnxIPsecSAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1)
)
tmnxIPsecSAStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSAId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSADirection"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSAIndex"),
)
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsEntry.setStatus("current")
_TmnxIPsecSAStatsBytesProcessed_Type = Counter64
_TmnxIPsecSAStatsBytesProcessed_Object = MibTableColumn
tmnxIPsecSAStatsBytesProcessed = _TmnxIPsecSAStatsBytesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 1),
    _TmnxIPsecSAStatsBytesProcessed_Type()
)
tmnxIPsecSAStatsBytesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsBytesProcessed.setStatus("current")
_TmnxIPsecSAStatsBytesProcLow32_Type = Counter32
_TmnxIPsecSAStatsBytesProcLow32_Object = MibTableColumn
tmnxIPsecSAStatsBytesProcLow32 = _TmnxIPsecSAStatsBytesProcLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 2),
    _TmnxIPsecSAStatsBytesProcLow32_Type()
)
tmnxIPsecSAStatsBytesProcLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsBytesProcLow32.setStatus("current")
_TmnxIPsecSAStatsBytesProcHigh32_Type = Counter32
_TmnxIPsecSAStatsBytesProcHigh32_Object = MibTableColumn
tmnxIPsecSAStatsBytesProcHigh32 = _TmnxIPsecSAStatsBytesProcHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 3),
    _TmnxIPsecSAStatsBytesProcHigh32_Type()
)
tmnxIPsecSAStatsBytesProcHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsBytesProcHigh32.setStatus("current")
_TmnxIPsecSAStatsPktsProcessed_Type = Counter64
_TmnxIPsecSAStatsPktsProcessed_Object = MibTableColumn
tmnxIPsecSAStatsPktsProcessed = _TmnxIPsecSAStatsPktsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 4),
    _TmnxIPsecSAStatsPktsProcessed_Type()
)
tmnxIPsecSAStatsPktsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPktsProcessed.setStatus("current")
_TmnxIPsecSAStatsPktsProcLow32_Type = Counter32
_TmnxIPsecSAStatsPktsProcLow32_Object = MibTableColumn
tmnxIPsecSAStatsPktsProcLow32 = _TmnxIPsecSAStatsPktsProcLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 5),
    _TmnxIPsecSAStatsPktsProcLow32_Type()
)
tmnxIPsecSAStatsPktsProcLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPktsProcLow32.setStatus("current")
_TmnxIPsecSAStatsPktsProcHigh32_Type = Counter32
_TmnxIPsecSAStatsPktsProcHigh32_Object = MibTableColumn
tmnxIPsecSAStatsPktsProcHigh32 = _TmnxIPsecSAStatsPktsProcHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 6),
    _TmnxIPsecSAStatsPktsProcHigh32_Type()
)
tmnxIPsecSAStatsPktsProcHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPktsProcHigh32.setStatus("current")
_TmnxIPsecSAStatsCryptoErrors_Type = Counter32
_TmnxIPsecSAStatsCryptoErrors_Object = MibTableColumn
tmnxIPsecSAStatsCryptoErrors = _TmnxIPsecSAStatsCryptoErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 7),
    _TmnxIPsecSAStatsCryptoErrors_Type()
)
tmnxIPsecSAStatsCryptoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsCryptoErrors.setStatus("current")
_TmnxIPsecSAStatsReplayErrors_Type = Counter32
_TmnxIPsecSAStatsReplayErrors_Object = MibTableColumn
tmnxIPsecSAStatsReplayErrors = _TmnxIPsecSAStatsReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 8),
    _TmnxIPsecSAStatsReplayErrors_Type()
)
tmnxIPsecSAStatsReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsReplayErrors.setStatus("current")
_TmnxIPsecSAStatsSAErrors_Type = Counter32
_TmnxIPsecSAStatsSAErrors_Object = MibTableColumn
tmnxIPsecSAStatsSAErrors = _TmnxIPsecSAStatsSAErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 9),
    _TmnxIPsecSAStatsSAErrors_Type()
)
tmnxIPsecSAStatsSAErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsSAErrors.setStatus("current")
_TmnxIPsecSAStatsPolicyErrors_Type = Counter32
_TmnxIPsecSAStatsPolicyErrors_Object = MibTableColumn
tmnxIPsecSAStatsPolicyErrors = _TmnxIPsecSAStatsPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 10),
    _TmnxIPsecSAStatsPolicyErrors_Type()
)
tmnxIPsecSAStatsPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPolicyErrors.setStatus("current")
_TmnxIPsecSAStatsEncapOverhead_Type = Counter32
_TmnxIPsecSAStatsEncapOverhead_Object = MibTableColumn
tmnxIPsecSAStatsEncapOverhead = _TmnxIPsecSAStatsEncapOverhead_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 11),
    _TmnxIPsecSAStatsEncapOverhead_Type()
)
tmnxIPsecSAStatsEncapOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsEncapOverhead.setStatus("current")
_TmnxIPsecSAStatsPreEncapFragCnt_Type = Counter64
_TmnxIPsecSAStatsPreEncapFragCnt_Object = MibTableColumn
tmnxIPsecSAStatsPreEncapFragCnt = _TmnxIPsecSAStatsPreEncapFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 12),
    _TmnxIPsecSAStatsPreEncapFragCnt_Type()
)
tmnxIPsecSAStatsPreEncapFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPreEncapFragCnt.setStatus("current")
_TmnxIPsecSAStatsPreEncapFragLtSz_Type = Unsigned32
_TmnxIPsecSAStatsPreEncapFragLtSz_Object = MibTableColumn
tmnxIPsecSAStatsPreEncapFragLtSz = _TmnxIPsecSAStatsPreEncapFragLtSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 13),
    _TmnxIPsecSAStatsPreEncapFragLtSz_Type()
)
tmnxIPsecSAStatsPreEncapFragLtSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPreEncapFragLtSz.setStatus("current")
_TmnxIPsecSAStatsPstEncapFragCnt_Type = Counter64
_TmnxIPsecSAStatsPstEncapFragCnt_Object = MibTableColumn
tmnxIPsecSAStatsPstEncapFragCnt = _TmnxIPsecSAStatsPstEncapFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 14),
    _TmnxIPsecSAStatsPstEncapFragCnt_Type()
)
tmnxIPsecSAStatsPstEncapFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPstEncapFragCnt.setStatus("current")
_TmnxIPsecSAStatsPstEncapFragLtSz_Type = Unsigned32
_TmnxIPsecSAStatsPstEncapFragLtSz_Object = MibTableColumn
tmnxIPsecSAStatsPstEncapFragLtSz = _TmnxIPsecSAStatsPstEncapFragLtSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 15),
    _TmnxIPsecSAStatsPstEncapFragLtSz_Type()
)
tmnxIPsecSAStatsPstEncapFragLtSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPstEncapFragLtSz.setStatus("current")
_TmnxIPsecSAStatsPfsDhGroup_Type = TmnxIkePolicyDHGroupOrZero
_TmnxIPsecSAStatsPfsDhGroup_Object = MibTableColumn
tmnxIPsecSAStatsPfsDhGroup = _TmnxIPsecSAStatsPfsDhGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 17),
    _TmnxIPsecSAStatsPfsDhGroup_Type()
)
tmnxIPsecSAStatsPfsDhGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPfsDhGroup.setStatus("current")
_TmnxIPsecSAStatsMulticastIfName_Type = TNamedItemOrEmpty
_TmnxIPsecSAStatsMulticastIfName_Object = MibTableColumn
tmnxIPsecSAStatsMulticastIfName = _TmnxIPsecSAStatsMulticastIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 18),
    _TmnxIPsecSAStatsMulticastIfName_Type()
)
tmnxIPsecSAStatsMulticastIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsMulticastIfName.setStatus("current")
_TmnxIPsecSAStatsMulticastProt_Type = TIPsecMulticastProtocol
_TmnxIPsecSAStatsMulticastProt_Object = MibTableColumn
tmnxIPsecSAStatsMulticastProt = _TmnxIPsecSAStatsMulticastProt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 19),
    _TmnxIPsecSAStatsMulticastProt_Type()
)
tmnxIPsecSAStatsMulticastProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsMulticastProt.setStatus("current")
_TmnxIPsecMdaDpStatsTable_Object = MibTable
tmnxIPsecMdaDpStatsTable = _TmnxIPsecMdaDpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15)
)
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsTable.setStatus("current")
_TmnxIPsecMdaDpStatsEntry_Object = MibTableRow
tmnxIPsecMdaDpStatsEntry = _TmnxIPsecMdaDpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1)
)
tmnxIPsecMdaDpStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEntry.setStatus("current")
_TmnxIPsecMdaDpStatsEncryptPkts_Type = Counter64
_TmnxIPsecMdaDpStatsEncryptPkts_Object = MibTableColumn
tmnxIPsecMdaDpStatsEncryptPkts = _TmnxIPsecMdaDpStatsEncryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 1),
    _TmnxIPsecMdaDpStatsEncryptPkts_Type()
)
tmnxIPsecMdaDpStatsEncryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEncryptPkts.setStatus("current")
_TmnxIPsecMdaDpStatsEncryptPktsLow32_Type = Counter32
_TmnxIPsecMdaDpStatsEncryptPktsLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsEncryptPktsLow32 = _TmnxIPsecMdaDpStatsEncryptPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 2),
    _TmnxIPsecMdaDpStatsEncryptPktsLow32_Type()
)
tmnxIPsecMdaDpStatsEncryptPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEncryptPktsLow32.setStatus("current")
_TmnxIPsecMdaDpStatsEncryptPktsHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsEncryptPktsHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsEncryptPktsHigh32 = _TmnxIPsecMdaDpStatsEncryptPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 3),
    _TmnxIPsecMdaDpStatsEncryptPktsHigh32_Type()
)
tmnxIPsecMdaDpStatsEncryptPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEncryptPktsHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsEncryptBytes_Type = Counter64
_TmnxIPsecMdaDpStatsEncryptBytes_Object = MibTableColumn
tmnxIPsecMdaDpStatsEncryptBytes = _TmnxIPsecMdaDpStatsEncryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 4),
    _TmnxIPsecMdaDpStatsEncryptBytes_Type()
)
tmnxIPsecMdaDpStatsEncryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEncryptBytes.setStatus("current")
_TmnxIPsecMdaDpStatsEncryptBytesLow32_Type = Counter32
_TmnxIPsecMdaDpStatsEncryptBytesLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsEncryptBytesLow32 = _TmnxIPsecMdaDpStatsEncryptBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 5),
    _TmnxIPsecMdaDpStatsEncryptBytesLow32_Type()
)
tmnxIPsecMdaDpStatsEncryptBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEncryptBytesLow32.setStatus("current")
_TmnxIPsecMdaDpStatsEncryptBytesHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsEncryptBytesHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsEncryptBytesHigh32 = _TmnxIPsecMdaDpStatsEncryptBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 6),
    _TmnxIPsecMdaDpStatsEncryptBytesHigh32_Type()
)
tmnxIPsecMdaDpStatsEncryptBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEncryptBytesHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsDecryptPkts_Type = Counter64
_TmnxIPsecMdaDpStatsDecryptPkts_Object = MibTableColumn
tmnxIPsecMdaDpStatsDecryptPkts = _TmnxIPsecMdaDpStatsDecryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 7),
    _TmnxIPsecMdaDpStatsDecryptPkts_Type()
)
tmnxIPsecMdaDpStatsDecryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsDecryptPkts.setStatus("current")
_TmnxIPsecMdaDpStatsDecryptPktsLow32_Type = Counter32
_TmnxIPsecMdaDpStatsDecryptPktsLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsDecryptPktsLow32 = _TmnxIPsecMdaDpStatsDecryptPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 8),
    _TmnxIPsecMdaDpStatsDecryptPktsLow32_Type()
)
tmnxIPsecMdaDpStatsDecryptPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsDecryptPktsLow32.setStatus("current")
_TmnxIPsecMdaDpStatsDecryptPktsHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsDecryptPktsHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsDecryptPktsHigh32 = _TmnxIPsecMdaDpStatsDecryptPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 9),
    _TmnxIPsecMdaDpStatsDecryptPktsHigh32_Type()
)
tmnxIPsecMdaDpStatsDecryptPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsDecryptPktsHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsDecryptBytes_Type = Counter64
_TmnxIPsecMdaDpStatsDecryptBytes_Object = MibTableColumn
tmnxIPsecMdaDpStatsDecryptBytes = _TmnxIPsecMdaDpStatsDecryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 10),
    _TmnxIPsecMdaDpStatsDecryptBytes_Type()
)
tmnxIPsecMdaDpStatsDecryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsDecryptBytes.setStatus("current")
_TmnxIPsecMdaDpStatsDecryptBytesLow32_Type = Counter32
_TmnxIPsecMdaDpStatsDecryptBytesLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsDecryptBytesLow32 = _TmnxIPsecMdaDpStatsDecryptBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 11),
    _TmnxIPsecMdaDpStatsDecryptBytesLow32_Type()
)
tmnxIPsecMdaDpStatsDecryptBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsDecryptBytesLow32.setStatus("current")
_TmnxIPsecMdaDpStatsDecryptBytesHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsDecryptBytesHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsDecryptBytesHigh32 = _TmnxIPsecMdaDpStatsDecryptBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 12),
    _TmnxIPsecMdaDpStatsDecryptBytesHigh32_Type()
)
tmnxIPsecMdaDpStatsDecryptBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsDecryptBytesHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsTxPktErrs_Type = Counter32
_TmnxIPsecMdaDpStatsTxPktErrs_Object = MibTableColumn
tmnxIPsecMdaDpStatsTxPktErrs = _TmnxIPsecMdaDpStatsTxPktErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 13),
    _TmnxIPsecMdaDpStatsTxPktErrs_Type()
)
tmnxIPsecMdaDpStatsTxPktErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsTxPktErrs.setStatus("current")
_TmnxIPsecMdaDpStatsOutBDropPkts_Type = Counter64
_TmnxIPsecMdaDpStatsOutBDropPkts_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBDropPkts = _TmnxIPsecMdaDpStatsOutBDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 14),
    _TmnxIPsecMdaDpStatsOutBDropPkts_Type()
)
tmnxIPsecMdaDpStatsOutBDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBDropPkts.setStatus("current")
_TmnxIPsecMdaDpStatsOutBDropPktsLow32_Type = Counter32
_TmnxIPsecMdaDpStatsOutBDropPktsLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBDropPktsLow32 = _TmnxIPsecMdaDpStatsOutBDropPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 15),
    _TmnxIPsecMdaDpStatsOutBDropPktsLow32_Type()
)
tmnxIPsecMdaDpStatsOutBDropPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBDropPktsLow32.setStatus("current")
_TmnxIPsecMdaDpStatsOutBDropPktsHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsOutBDropPktsHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBDropPktsHigh32 = _TmnxIPsecMdaDpStatsOutBDropPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 16),
    _TmnxIPsecMdaDpStatsOutBDropPktsHigh32_Type()
)
tmnxIPsecMdaDpStatsOutBDropPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBDropPktsHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsOutBSAMisses_Type = Counter64
_TmnxIPsecMdaDpStatsOutBSAMisses_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBSAMisses = _TmnxIPsecMdaDpStatsOutBSAMisses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 17),
    _TmnxIPsecMdaDpStatsOutBSAMisses_Type()
)
tmnxIPsecMdaDpStatsOutBSAMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBSAMisses.setStatus("current")
_TmnxIPsecMdaDpStatsOutBSAMissesLow32_Type = Counter32
_TmnxIPsecMdaDpStatsOutBSAMissesLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBSAMissesLow32 = _TmnxIPsecMdaDpStatsOutBSAMissesLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 18),
    _TmnxIPsecMdaDpStatsOutBSAMissesLow32_Type()
)
tmnxIPsecMdaDpStatsOutBSAMissesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBSAMissesLow32.setStatus("current")
_TmnxIPsecMdaDpStatsOutBSAMissesHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsOutBSAMissesHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBSAMissesHigh32 = _TmnxIPsecMdaDpStatsOutBSAMissesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 19),
    _TmnxIPsecMdaDpStatsOutBSAMissesHigh32_Type()
)
tmnxIPsecMdaDpStatsOutBSAMissesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBSAMissesHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsOutBPolicyEntryMisses_Type = Counter32
_TmnxIPsecMdaDpStatsOutBPolicyEntryMisses_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBPolicyEntryMisses = _TmnxIPsecMdaDpStatsOutBPolicyEntryMisses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 20),
    _TmnxIPsecMdaDpStatsOutBPolicyEntryMisses_Type()
)
tmnxIPsecMdaDpStatsOutBPolicyEntryMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBPolicyEntryMisses.setStatus("current")
_TmnxIPsecMdaDpStatsInBDropPkts_Type = Counter64
_TmnxIPsecMdaDpStatsInBDropPkts_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBDropPkts = _TmnxIPsecMdaDpStatsInBDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 21),
    _TmnxIPsecMdaDpStatsInBDropPkts_Type()
)
tmnxIPsecMdaDpStatsInBDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBDropPkts.setStatus("current")
_TmnxIPsecMdaDpStatsInBDropPktsLow32_Type = Counter32
_TmnxIPsecMdaDpStatsInBDropPktsLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBDropPktsLow32 = _TmnxIPsecMdaDpStatsInBDropPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 22),
    _TmnxIPsecMdaDpStatsInBDropPktsLow32_Type()
)
tmnxIPsecMdaDpStatsInBDropPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBDropPktsLow32.setStatus("current")
_TmnxIPsecMdaDpStatsInBDropPktsHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsInBDropPktsHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBDropPktsHigh32 = _TmnxIPsecMdaDpStatsInBDropPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 23),
    _TmnxIPsecMdaDpStatsInBDropPktsHigh32_Type()
)
tmnxIPsecMdaDpStatsInBDropPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBDropPktsHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsInBSAMisses_Type = Counter64
_TmnxIPsecMdaDpStatsInBSAMisses_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBSAMisses = _TmnxIPsecMdaDpStatsInBSAMisses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 24),
    _TmnxIPsecMdaDpStatsInBSAMisses_Type()
)
tmnxIPsecMdaDpStatsInBSAMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBSAMisses.setStatus("current")
_TmnxIPsecMdaDpStatsInBSAMissesLow32_Type = Counter32
_TmnxIPsecMdaDpStatsInBSAMissesLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBSAMissesLow32 = _TmnxIPsecMdaDpStatsInBSAMissesLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 25),
    _TmnxIPsecMdaDpStatsInBSAMissesLow32_Type()
)
tmnxIPsecMdaDpStatsInBSAMissesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBSAMissesLow32.setStatus("current")
_TmnxIPsecMdaDpStatsInBSAMissesHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsInBSAMissesHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBSAMissesHigh32 = _TmnxIPsecMdaDpStatsInBSAMissesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 26),
    _TmnxIPsecMdaDpStatsInBSAMissesHigh32_Type()
)
tmnxIPsecMdaDpStatsInBSAMissesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBSAMissesHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsInBIPDstSrcMismatches_Type = Counter32
_TmnxIPsecMdaDpStatsInBIPDstSrcMismatches_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBIPDstSrcMismatches = _TmnxIPsecMdaDpStatsInBIPDstSrcMismatches_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 27),
    _TmnxIPsecMdaDpStatsInBIPDstSrcMismatches_Type()
)
tmnxIPsecMdaDpStatsInBIPDstSrcMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBIPDstSrcMismatches.setStatus("current")
_TmnxIPsecMdaDpInFragments_Type = Counter64
_TmnxIPsecMdaDpInFragments_Object = MibTableColumn
tmnxIPsecMdaDpInFragments = _TmnxIPsecMdaDpInFragments_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 28),
    _TmnxIPsecMdaDpInFragments_Type()
)
tmnxIPsecMdaDpInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpInFragments.setStatus("current")
_TmnxIPsecMdaDpInFragmentsLow32_Type = Counter32
_TmnxIPsecMdaDpInFragmentsLow32_Object = MibTableColumn
tmnxIPsecMdaDpInFragmentsLow32 = _TmnxIPsecMdaDpInFragmentsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 29),
    _TmnxIPsecMdaDpInFragmentsLow32_Type()
)
tmnxIPsecMdaDpInFragmentsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpInFragmentsLow32.setStatus("current")
_TmnxIPsecMdaDpInFragmentsHigh32_Type = Counter32
_TmnxIPsecMdaDpInFragmentsHigh32_Object = MibTableColumn
tmnxIPsecMdaDpInFragmentsHigh32 = _TmnxIPsecMdaDpInFragmentsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 30),
    _TmnxIPsecMdaDpInFragmentsHigh32_Type()
)
tmnxIPsecMdaDpInFragmentsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpInFragmentsHigh32.setStatus("current")
_TmnxIPsecMdaDpPktsReassem_Type = Counter64
_TmnxIPsecMdaDpPktsReassem_Object = MibTableColumn
tmnxIPsecMdaDpPktsReassem = _TmnxIPsecMdaDpPktsReassem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 31),
    _TmnxIPsecMdaDpPktsReassem_Type()
)
tmnxIPsecMdaDpPktsReassem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpPktsReassem.setStatus("current")
_TmnxIPsecMdaDpPktsReassemLow32_Type = Counter32
_TmnxIPsecMdaDpPktsReassemLow32_Object = MibTableColumn
tmnxIPsecMdaDpPktsReassemLow32 = _TmnxIPsecMdaDpPktsReassemLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 32),
    _TmnxIPsecMdaDpPktsReassemLow32_Type()
)
tmnxIPsecMdaDpPktsReassemLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpPktsReassemLow32.setStatus("current")
_TmnxIPsecMdaDpPktsReassemHigh32_Type = Counter32
_TmnxIPsecMdaDpPktsReassemHigh32_Object = MibTableColumn
tmnxIPsecMdaDpPktsReassemHigh32 = _TmnxIPsecMdaDpPktsReassemHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 33),
    _TmnxIPsecMdaDpPktsReassemHigh32_Type()
)
tmnxIPsecMdaDpPktsReassemHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpPktsReassemHigh32.setStatus("current")
_TmnxIPsecMdaDpFragDropTime_Type = Counter64
_TmnxIPsecMdaDpFragDropTime_Object = MibTableColumn
tmnxIPsecMdaDpFragDropTime = _TmnxIPsecMdaDpFragDropTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 34),
    _TmnxIPsecMdaDpFragDropTime_Type()
)
tmnxIPsecMdaDpFragDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpFragDropTime.setStatus("current")
_TmnxIPsecMdaDpFragDropTimeLow32_Type = Counter32
_TmnxIPsecMdaDpFragDropTimeLow32_Object = MibTableColumn
tmnxIPsecMdaDpFragDropTimeLow32 = _TmnxIPsecMdaDpFragDropTimeLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 35),
    _TmnxIPsecMdaDpFragDropTimeLow32_Type()
)
tmnxIPsecMdaDpFragDropTimeLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpFragDropTimeLow32.setStatus("current")
_TmnxIPsecMdaDpFragDropTimeHigh32_Type = Counter32
_TmnxIPsecMdaDpFragDropTimeHigh32_Object = MibTableColumn
tmnxIPsecMdaDpFragDropTimeHigh32 = _TmnxIPsecMdaDpFragDropTimeHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 36),
    _TmnxIPsecMdaDpFragDropTimeHigh32_Type()
)
tmnxIPsecMdaDpFragDropTimeHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpFragDropTimeHigh32.setStatus("current")
_TmnxIPsecMdaDpFragDropped_Type = Counter64
_TmnxIPsecMdaDpFragDropped_Object = MibTableColumn
tmnxIPsecMdaDpFragDropped = _TmnxIPsecMdaDpFragDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 37),
    _TmnxIPsecMdaDpFragDropped_Type()
)
tmnxIPsecMdaDpFragDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpFragDropped.setStatus("current")
_TmnxIPsecMdaDpFragDroppedLow32_Type = Counter32
_TmnxIPsecMdaDpFragDroppedLow32_Object = MibTableColumn
tmnxIPsecMdaDpFragDroppedLow32 = _TmnxIPsecMdaDpFragDroppedLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 38),
    _TmnxIPsecMdaDpFragDroppedLow32_Type()
)
tmnxIPsecMdaDpFragDroppedLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpFragDroppedLow32.setStatus("current")
_TmnxIPsecMdaDpFragDroppedHigh32_Type = Counter32
_TmnxIPsecMdaDpFragDroppedHigh32_Object = MibTableColumn
tmnxIPsecMdaDpFragDroppedHigh32 = _TmnxIPsecMdaDpFragDroppedHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 39),
    _TmnxIPsecMdaDpFragDroppedHigh32_Type()
)
tmnxIPsecMdaDpFragDroppedHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpFragDroppedHigh32.setStatus("current")
_TmnxIPsecMdaDpGreTnlInPkts_Type = Counter64
_TmnxIPsecMdaDpGreTnlInPkts_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInPkts = _TmnxIPsecMdaDpGreTnlInPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 40),
    _TmnxIPsecMdaDpGreTnlInPkts_Type()
)
tmnxIPsecMdaDpGreTnlInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInPkts.setStatus("current")
_TmnxIPsecMdaDpGreTnlInPktsLo_Type = Counter32
_TmnxIPsecMdaDpGreTnlInPktsLo_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInPktsLo = _TmnxIPsecMdaDpGreTnlInPktsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 41),
    _TmnxIPsecMdaDpGreTnlInPktsLo_Type()
)
tmnxIPsecMdaDpGreTnlInPktsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInPktsLo.setStatus("current")
_TmnxIPsecMdaDpGreTnlInPktsHi_Type = Counter32
_TmnxIPsecMdaDpGreTnlInPktsHi_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInPktsHi = _TmnxIPsecMdaDpGreTnlInPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 42),
    _TmnxIPsecMdaDpGreTnlInPktsHi_Type()
)
tmnxIPsecMdaDpGreTnlInPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInPktsHi.setStatus("current")
_TmnxIPsecMdaDpGreTnlInBytes_Type = Counter64
_TmnxIPsecMdaDpGreTnlInBytes_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInBytes = _TmnxIPsecMdaDpGreTnlInBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 43),
    _TmnxIPsecMdaDpGreTnlInBytes_Type()
)
tmnxIPsecMdaDpGreTnlInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInBytes.setStatus("current")
_TmnxIPsecMdaDpGreTnlInBytesLo_Type = Counter32
_TmnxIPsecMdaDpGreTnlInBytesLo_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInBytesLo = _TmnxIPsecMdaDpGreTnlInBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 44),
    _TmnxIPsecMdaDpGreTnlInBytesLo_Type()
)
tmnxIPsecMdaDpGreTnlInBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInBytesLo.setStatus("current")
_TmnxIPsecMdaDpGreTnlInBytesHi_Type = Counter32
_TmnxIPsecMdaDpGreTnlInBytesHi_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInBytesHi = _TmnxIPsecMdaDpGreTnlInBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 45),
    _TmnxIPsecMdaDpGreTnlInBytesHi_Type()
)
tmnxIPsecMdaDpGreTnlInBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInBytesHi.setStatus("current")
_TmnxIPsecMdaDpGreTnlInErrs_Type = Counter64
_TmnxIPsecMdaDpGreTnlInErrs_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInErrs = _TmnxIPsecMdaDpGreTnlInErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 46),
    _TmnxIPsecMdaDpGreTnlInErrs_Type()
)
tmnxIPsecMdaDpGreTnlInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInErrs.setStatus("current")
_TmnxIPsecMdaDpGreTnlInErrsLo_Type = Counter32
_TmnxIPsecMdaDpGreTnlInErrsLo_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInErrsLo = _TmnxIPsecMdaDpGreTnlInErrsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 47),
    _TmnxIPsecMdaDpGreTnlInErrsLo_Type()
)
tmnxIPsecMdaDpGreTnlInErrsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInErrsLo.setStatus("current")
_TmnxIPsecMdaDpGreTnlInErrsHi_Type = Counter32
_TmnxIPsecMdaDpGreTnlInErrsHi_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInErrsHi = _TmnxIPsecMdaDpGreTnlInErrsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 48),
    _TmnxIPsecMdaDpGreTnlInErrsHi_Type()
)
tmnxIPsecMdaDpGreTnlInErrsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInErrsHi.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutPkts_Type = Counter64
_TmnxIPsecMdaDpGreTnlOutPkts_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutPkts = _TmnxIPsecMdaDpGreTnlOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 49),
    _TmnxIPsecMdaDpGreTnlOutPkts_Type()
)
tmnxIPsecMdaDpGreTnlOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutPkts.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutPktsLo_Type = Counter32
_TmnxIPsecMdaDpGreTnlOutPktsLo_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutPktsLo = _TmnxIPsecMdaDpGreTnlOutPktsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 50),
    _TmnxIPsecMdaDpGreTnlOutPktsLo_Type()
)
tmnxIPsecMdaDpGreTnlOutPktsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutPktsLo.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutPktsHi_Type = Counter32
_TmnxIPsecMdaDpGreTnlOutPktsHi_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutPktsHi = _TmnxIPsecMdaDpGreTnlOutPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 51),
    _TmnxIPsecMdaDpGreTnlOutPktsHi_Type()
)
tmnxIPsecMdaDpGreTnlOutPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutPktsHi.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutBytes_Type = Counter64
_TmnxIPsecMdaDpGreTnlOutBytes_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutBytes = _TmnxIPsecMdaDpGreTnlOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 52),
    _TmnxIPsecMdaDpGreTnlOutBytes_Type()
)
tmnxIPsecMdaDpGreTnlOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutBytes.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutBytesLo_Type = Counter32
_TmnxIPsecMdaDpGreTnlOutBytesLo_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutBytesLo = _TmnxIPsecMdaDpGreTnlOutBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 53),
    _TmnxIPsecMdaDpGreTnlOutBytesLo_Type()
)
tmnxIPsecMdaDpGreTnlOutBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutBytesLo.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutBytesHi_Type = Counter32
_TmnxIPsecMdaDpGreTnlOutBytesHi_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutBytesHi = _TmnxIPsecMdaDpGreTnlOutBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 54),
    _TmnxIPsecMdaDpGreTnlOutBytesHi_Type()
)
tmnxIPsecMdaDpGreTnlOutBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutBytesHi.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutErrs_Type = Counter64
_TmnxIPsecMdaDpGreTnlOutErrs_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutErrs = _TmnxIPsecMdaDpGreTnlOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 55),
    _TmnxIPsecMdaDpGreTnlOutErrs_Type()
)
tmnxIPsecMdaDpGreTnlOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutErrs.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutErrsLo_Type = Counter32
_TmnxIPsecMdaDpGreTnlOutErrsLo_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutErrsLo = _TmnxIPsecMdaDpGreTnlOutErrsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 56),
    _TmnxIPsecMdaDpGreTnlOutErrsLo_Type()
)
tmnxIPsecMdaDpGreTnlOutErrsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutErrsLo.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutErrsHi_Type = Counter32
_TmnxIPsecMdaDpGreTnlOutErrsHi_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutErrsHi = _TmnxIPsecMdaDpGreTnlOutErrsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 57),
    _TmnxIPsecMdaDpGreTnlOutErrsHi_Type()
)
tmnxIPsecMdaDpGreTnlOutErrsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutErrsHi.setStatus("current")
_TmnxIPsecMdaDpPktsDropDfSet_Type = Counter64
_TmnxIPsecMdaDpPktsDropDfSet_Object = MibTableColumn
tmnxIPsecMdaDpPktsDropDfSet = _TmnxIPsecMdaDpPktsDropDfSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 58),
    _TmnxIPsecMdaDpPktsDropDfSet_Type()
)
tmnxIPsecMdaDpPktsDropDfSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpPktsDropDfSet.setStatus("current")
_TmnxIPsecMdaDpPktsDropDfSetLo_Type = Counter32
_TmnxIPsecMdaDpPktsDropDfSetLo_Object = MibTableColumn
tmnxIPsecMdaDpPktsDropDfSetLo = _TmnxIPsecMdaDpPktsDropDfSetLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 59),
    _TmnxIPsecMdaDpPktsDropDfSetLo_Type()
)
tmnxIPsecMdaDpPktsDropDfSetLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpPktsDropDfSetLo.setStatus("current")
_TmnxIPsecMdaDpPktsDropDfSetHi_Type = Counter32
_TmnxIPsecMdaDpPktsDropDfSetHi_Object = MibTableColumn
tmnxIPsecMdaDpPktsDropDfSetHi = _TmnxIPsecMdaDpPktsDropDfSetHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 60),
    _TmnxIPsecMdaDpPktsDropDfSetHi_Type()
)
tmnxIPsecMdaDpPktsDropDfSetHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpPktsDropDfSetHi.setStatus("current")
_TmnxIPsecMdaDpStaticIPsecTnls_Type = Counter32
_TmnxIPsecMdaDpStaticIPsecTnls_Object = MibTableColumn
tmnxIPsecMdaDpStaticIPsecTnls = _TmnxIPsecMdaDpStaticIPsecTnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 61),
    _TmnxIPsecMdaDpStaticIPsecTnls_Type()
)
tmnxIPsecMdaDpStaticIPsecTnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStaticIPsecTnls.setStatus("current")
_TmnxIPsecMdaDpDynIPsecTnls_Type = Counter32
_TmnxIPsecMdaDpDynIPsecTnls_Object = MibTableColumn
tmnxIPsecMdaDpDynIPsecTnls = _TmnxIPsecMdaDpDynIPsecTnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 62),
    _TmnxIPsecMdaDpDynIPsecTnls_Type()
)
tmnxIPsecMdaDpDynIPsecTnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpDynIPsecTnls.setStatus("current")
_TmnxIPsecMdaDpIpGreTnls_Type = Counter32
_TmnxIPsecMdaDpIpGreTnls_Object = MibTableColumn
tmnxIPsecMdaDpIpGreTnls = _TmnxIPsecMdaDpIpGreTnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 63),
    _TmnxIPsecMdaDpIpGreTnls_Type()
)
tmnxIPsecMdaDpIpGreTnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpIpGreTnls.setStatus("current")
_TmnxIPsecMdaDpIpv4Tnls_Type = Counter32
_TmnxIPsecMdaDpIpv4Tnls_Object = MibTableColumn
tmnxIPsecMdaDpIpv4Tnls = _TmnxIPsecMdaDpIpv4Tnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 64),
    _TmnxIPsecMdaDpIpv4Tnls_Type()
)
tmnxIPsecMdaDpIpv4Tnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpIpv4Tnls.setStatus("current")
_TmnxIPsecMdaDpL2tpv3TnlInPkts_Type = Counter64
_TmnxIPsecMdaDpL2tpv3TnlInPkts_Object = MibTableColumn
tmnxIPsecMdaDpL2tpv3TnlInPkts = _TmnxIPsecMdaDpL2tpv3TnlInPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 65),
    _TmnxIPsecMdaDpL2tpv3TnlInPkts_Type()
)
tmnxIPsecMdaDpL2tpv3TnlInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpL2tpv3TnlInPkts.setStatus("current")
_TmnxIPsecMdaDpL2tpv3TnlInBytes_Type = Counter64
_TmnxIPsecMdaDpL2tpv3TnlInBytes_Object = MibTableColumn
tmnxIPsecMdaDpL2tpv3TnlInBytes = _TmnxIPsecMdaDpL2tpv3TnlInBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 66),
    _TmnxIPsecMdaDpL2tpv3TnlInBytes_Type()
)
tmnxIPsecMdaDpL2tpv3TnlInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpL2tpv3TnlInBytes.setStatus("current")
_TmnxIPsecMdaDpL2tpv3TnlInErrs_Type = Counter64
_TmnxIPsecMdaDpL2tpv3TnlInErrs_Object = MibTableColumn
tmnxIPsecMdaDpL2tpv3TnlInErrs = _TmnxIPsecMdaDpL2tpv3TnlInErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 67),
    _TmnxIPsecMdaDpL2tpv3TnlInErrs_Type()
)
tmnxIPsecMdaDpL2tpv3TnlInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpL2tpv3TnlInErrs.setStatus("current")
_TmnxIPsecMdaDpL2tpv3TnlInCookErr_Type = Counter64
_TmnxIPsecMdaDpL2tpv3TnlInCookErr_Object = MibTableColumn
tmnxIPsecMdaDpL2tpv3TnlInCookErr = _TmnxIPsecMdaDpL2tpv3TnlInCookErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 68),
    _TmnxIPsecMdaDpL2tpv3TnlInCookErr_Type()
)
tmnxIPsecMdaDpL2tpv3TnlInCookErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpL2tpv3TnlInCookErr.setStatus("current")
_TmnxIPsecMdaDpL2tpv3TnlInSeIdErr_Type = Counter64
_TmnxIPsecMdaDpL2tpv3TnlInSeIdErr_Object = MibTableColumn
tmnxIPsecMdaDpL2tpv3TnlInSeIdErr = _TmnxIPsecMdaDpL2tpv3TnlInSeIdErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 69),
    _TmnxIPsecMdaDpL2tpv3TnlInSeIdErr_Type()
)
tmnxIPsecMdaDpL2tpv3TnlInSeIdErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpL2tpv3TnlInSeIdErr.setStatus("current")
_TmnxIPsecMdaDpL2tpv3TnlOutPkts_Type = Counter64
_TmnxIPsecMdaDpL2tpv3TnlOutPkts_Object = MibTableColumn
tmnxIPsecMdaDpL2tpv3TnlOutPkts = _TmnxIPsecMdaDpL2tpv3TnlOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 70),
    _TmnxIPsecMdaDpL2tpv3TnlOutPkts_Type()
)
tmnxIPsecMdaDpL2tpv3TnlOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpL2tpv3TnlOutPkts.setStatus("current")
_TmnxIPsecMdaDpL2tpv3TnlOutBytes_Type = Counter64
_TmnxIPsecMdaDpL2tpv3TnlOutBytes_Object = MibTableColumn
tmnxIPsecMdaDpL2tpv3TnlOutBytes = _TmnxIPsecMdaDpL2tpv3TnlOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 71),
    _TmnxIPsecMdaDpL2tpv3TnlOutBytes_Type()
)
tmnxIPsecMdaDpL2tpv3TnlOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpL2tpv3TnlOutBytes.setStatus("current")
_TmnxIPsecMdaDpL2tpv3TnlOutErrs_Type = Counter64
_TmnxIPsecMdaDpL2tpv3TnlOutErrs_Object = MibTableColumn
tmnxIPsecMdaDpL2tpv3TnlOutErrs = _TmnxIPsecMdaDpL2tpv3TnlOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 72),
    _TmnxIPsecMdaDpL2tpv3TnlOutErrs_Type()
)
tmnxIPsecMdaDpL2tpv3TnlOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpL2tpv3TnlOutErrs.setStatus("current")
_TmnxIPsecMdaDpL2tpv3Tnls_Type = Counter32
_TmnxIPsecMdaDpL2tpv3Tnls_Object = MibTableColumn
tmnxIPsecMdaDpL2tpv3Tnls = _TmnxIPsecMdaDpL2tpv3Tnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 73),
    _TmnxIPsecMdaDpL2tpv3Tnls_Type()
)
tmnxIPsecMdaDpL2tpv3Tnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpL2tpv3Tnls.setStatus("current")
_TIPsecTnlTempTblLastChanged_Type = TimeStamp
_TIPsecTnlTempTblLastChanged_Object = MibScalar
tIPsecTnlTempTblLastChanged = _TIPsecTnlTempTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 16),
    _TIPsecTnlTempTblLastChanged_Type()
)
tIPsecTnlTempTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTnlTempTblLastChanged.setStatus("current")
_TIPsecTnlTempTable_Object = MibTable
tIPsecTnlTempTable = _TIPsecTnlTempTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17)
)
if mibBuilder.loadTexts:
    tIPsecTnlTempTable.setStatus("current")
_TIPsecTnlTempEntry_Object = MibTableRow
tIPsecTnlTempEntry = _TIPsecTnlTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1)
)
tIPsecTnlTempEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTnlTempId"),
)
if mibBuilder.loadTexts:
    tIPsecTnlTempEntry.setStatus("current")
_TIPsecTnlTempId_Type = TmnxIPsecTunnelTemplateId
_TIPsecTnlTempId_Object = MibTableColumn
tIPsecTnlTempId = _TIPsecTnlTempId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 1),
    _TIPsecTnlTempId_Type()
)
tIPsecTnlTempId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecTnlTempId.setStatus("current")
_TIPsecTnlTempRowStatus_Type = RowStatus
_TIPsecTnlTempRowStatus_Object = MibTableColumn
tIPsecTnlTempRowStatus = _TIPsecTnlTempRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 2),
    _TIPsecTnlTempRowStatus_Type()
)
tIPsecTnlTempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempRowStatus.setStatus("current")
_TIPsecTnlTempLastChanged_Type = TimeStamp
_TIPsecTnlTempLastChanged_Object = MibTableColumn
tIPsecTnlTempLastChanged = _TIPsecTnlTempLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 3),
    _TIPsecTnlTempLastChanged_Type()
)
tIPsecTnlTempLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTnlTempLastChanged.setStatus("current")


class _TIPsecTnlTempDescr_Type(TItemDescription):
    """Custom type tIPsecTnlTempDescr based on TItemDescription"""
    defaultValue = OctetString("")


_TIPsecTnlTempDescr_Type.__name__ = "TItemDescription"
_TIPsecTnlTempDescr_Object = MibTableColumn
tIPsecTnlTempDescr = _TIPsecTnlTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 4),
    _TIPsecTnlTempDescr_Type()
)
tIPsecTnlTempDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempDescr.setStatus("current")


class _TIPsecTnlTempReverseRoute_Type(Integer32):
    """Custom type tIPsecTnlTempReverseRoute based on Integer32"""
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
          ("reverseRoute", 1),
          ("useSecurityPolicy", 2))
    )


_TIPsecTnlTempReverseRoute_Type.__name__ = "Integer32"
_TIPsecTnlTempReverseRoute_Object = MibTableColumn
tIPsecTnlTempReverseRoute = _TIPsecTnlTempReverseRoute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 5),
    _TIPsecTnlTempReverseRoute_Type()
)
tIPsecTnlTempReverseRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempReverseRoute.setStatus("current")


class _TIPsecTnlTempDynKeyTransformId1_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tIPsecTnlTempDynKeyTransformId1 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TIPsecTnlTempDynKeyTransformId1_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TIPsecTnlTempDynKeyTransformId1_Object = MibTableColumn
tIPsecTnlTempDynKeyTransformId1 = _TIPsecTnlTempDynKeyTransformId1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 6),
    _TIPsecTnlTempDynKeyTransformId1_Type()
)
tIPsecTnlTempDynKeyTransformId1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempDynKeyTransformId1.setStatus("current")


class _TIPsecTnlTempDynKeyTransformId2_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tIPsecTnlTempDynKeyTransformId2 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TIPsecTnlTempDynKeyTransformId2_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TIPsecTnlTempDynKeyTransformId2_Object = MibTableColumn
tIPsecTnlTempDynKeyTransformId2 = _TIPsecTnlTempDynKeyTransformId2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 7),
    _TIPsecTnlTempDynKeyTransformId2_Type()
)
tIPsecTnlTempDynKeyTransformId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempDynKeyTransformId2.setStatus("current")


class _TIPsecTnlTempDynKeyTransformId3_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tIPsecTnlTempDynKeyTransformId3 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TIPsecTnlTempDynKeyTransformId3_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TIPsecTnlTempDynKeyTransformId3_Object = MibTableColumn
tIPsecTnlTempDynKeyTransformId3 = _TIPsecTnlTempDynKeyTransformId3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 8),
    _TIPsecTnlTempDynKeyTransformId3_Type()
)
tIPsecTnlTempDynKeyTransformId3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempDynKeyTransformId3.setStatus("current")


class _TIPsecTnlTempDynKeyTransformId4_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tIPsecTnlTempDynKeyTransformId4 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TIPsecTnlTempDynKeyTransformId4_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TIPsecTnlTempDynKeyTransformId4_Object = MibTableColumn
tIPsecTnlTempDynKeyTransformId4 = _TIPsecTnlTempDynKeyTransformId4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 9),
    _TIPsecTnlTempDynKeyTransformId4_Type()
)
tIPsecTnlTempDynKeyTransformId4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempDynKeyTransformId4.setStatus("current")


class _TIPsecTnlTempReplayWindow_Type(Unsigned32):
    """Custom type tIPsecTnlTempReplayWindow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
    )


_TIPsecTnlTempReplayWindow_Type.__name__ = "Unsigned32"
_TIPsecTnlTempReplayWindow_Object = MibTableColumn
tIPsecTnlTempReplayWindow = _TIPsecTnlTempReplayWindow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 10),
    _TIPsecTnlTempReplayWindow_Type()
)
tIPsecTnlTempReplayWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempReplayWindow.setStatus("current")


class _TIPsecTnlTempIpMtu_Type(Unsigned32):
    """Custom type tIPsecTnlTempIpMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TIPsecTnlTempIpMtu_Type.__name__ = "Unsigned32"
_TIPsecTnlTempIpMtu_Object = MibTableColumn
tIPsecTnlTempIpMtu = _TIPsecTnlTempIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 11),
    _TIPsecTnlTempIpMtu_Type()
)
tIPsecTnlTempIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempIpMtu.setStatus("current")


class _TIPsecTnlTempEncapIpMtu_Type(Unsigned32):
    """Custom type tIPsecTnlTempEncapIpMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TIPsecTnlTempEncapIpMtu_Type.__name__ = "Unsigned32"
_TIPsecTnlTempEncapIpMtu_Object = MibTableColumn
tIPsecTnlTempEncapIpMtu = _TIPsecTnlTempEncapIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 12),
    _TIPsecTnlTempEncapIpMtu_Type()
)
tIPsecTnlTempEncapIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempEncapIpMtu.setStatus("current")


class _TIPsecTnlTempIcmp6Pkt2Big_Type(TruthValue):
    """Custom type tIPsecTnlTempIcmp6Pkt2Big based on TruthValue"""
    defaultValue = 1


_TIPsecTnlTempIcmp6Pkt2Big_Type.__name__ = "TruthValue"
_TIPsecTnlTempIcmp6Pkt2Big_Object = MibTableColumn
tIPsecTnlTempIcmp6Pkt2Big = _TIPsecTnlTempIcmp6Pkt2Big_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 14),
    _TIPsecTnlTempIcmp6Pkt2Big_Type()
)
tIPsecTnlTempIcmp6Pkt2Big.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempIcmp6Pkt2Big.setStatus("current")


class _TIPsecTnlTempIcmp6NumPkt2Big_Type(Unsigned32):
    """Custom type tIPsecTnlTempIcmp6NumPkt2Big based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TIPsecTnlTempIcmp6NumPkt2Big_Type.__name__ = "Unsigned32"
_TIPsecTnlTempIcmp6NumPkt2Big_Object = MibTableColumn
tIPsecTnlTempIcmp6NumPkt2Big = _TIPsecTnlTempIcmp6NumPkt2Big_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 15),
    _TIPsecTnlTempIcmp6NumPkt2Big_Type()
)
tIPsecTnlTempIcmp6NumPkt2Big.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempIcmp6NumPkt2Big.setStatus("current")


class _TIPsecTnlTempIcmp6Pkt2BigTime_Type(Unsigned32):
    """Custom type tIPsecTnlTempIcmp6Pkt2BigTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TIPsecTnlTempIcmp6Pkt2BigTime_Type.__name__ = "Unsigned32"
_TIPsecTnlTempIcmp6Pkt2BigTime_Object = MibTableColumn
tIPsecTnlTempIcmp6Pkt2BigTime = _TIPsecTnlTempIcmp6Pkt2BigTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 16),
    _TIPsecTnlTempIcmp6Pkt2BigTime_Type()
)
tIPsecTnlTempIcmp6Pkt2BigTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempIcmp6Pkt2BigTime.setStatus("current")
if mibBuilder.loadTexts:
    tIPsecTnlTempIcmp6Pkt2BigTime.setUnits("seconds")


class _TIPsecTnlTempClearDfBit_Type(TruthValue):
    """Custom type tIPsecTnlTempClearDfBit based on TruthValue"""
    defaultValue = 2


_TIPsecTnlTempClearDfBit_Type.__name__ = "TruthValue"
_TIPsecTnlTempClearDfBit_Object = MibTableColumn
tIPsecTnlTempClearDfBit = _TIPsecTnlTempClearDfBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 17),
    _TIPsecTnlTempClearDfBit_Type()
)
tIPsecTnlTempClearDfBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempClearDfBit.setStatus("current")


class _TIPsecTnlTempPublicTcpMssAdjust_Type(Integer32):
    """Custom type tIPsecTnlTempPublicTcpMssAdjust based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TIPsecTnlTempPublicTcpMssAdjust_Type.__name__ = "Integer32"
_TIPsecTnlTempPublicTcpMssAdjust_Object = MibTableColumn
tIPsecTnlTempPublicTcpMssAdjust = _TIPsecTnlTempPublicTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 23),
    _TIPsecTnlTempPublicTcpMssAdjust_Type()
)
tIPsecTnlTempPublicTcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempPublicTcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    tIPsecTnlTempPublicTcpMssAdjust.setUnits("octets")


class _TIPsecTnlTempPrivateTcpMssAdjust_Type(Integer32):
    """Custom type tIPsecTnlTempPrivateTcpMssAdjust based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(512, 9000),
    )


_TIPsecTnlTempPrivateTcpMssAdjust_Type.__name__ = "Integer32"
_TIPsecTnlTempPrivateTcpMssAdjust_Object = MibTableColumn
tIPsecTnlTempPrivateTcpMssAdjust = _TIPsecTnlTempPrivateTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 24),
    _TIPsecTnlTempPrivateTcpMssAdjust_Type()
)
tIPsecTnlTempPrivateTcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempPrivateTcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    tIPsecTnlTempPrivateTcpMssAdjust.setUnits("octets")


class _TIPsecTnlTempIgnoreDefaultRoute_Type(TruthValue):
    """Custom type tIPsecTnlTempIgnoreDefaultRoute based on TruthValue"""
    defaultValue = 2


_TIPsecTnlTempIgnoreDefaultRoute_Type.__name__ = "TruthValue"
_TIPsecTnlTempIgnoreDefaultRoute_Object = MibTableColumn
tIPsecTnlTempIgnoreDefaultRoute = _TIPsecTnlTempIgnoreDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 25),
    _TIPsecTnlTempIgnoreDefaultRoute_Type()
)
tIPsecTnlTempIgnoreDefaultRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempIgnoreDefaultRoute.setStatus("current")
_TmnxIPsecGWTblLastChgd_Type = TimeStamp
_TmnxIPsecGWTblLastChgd_Object = MibScalar
tmnxIPsecGWTblLastChgd = _TmnxIPsecGWTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 18),
    _TmnxIPsecGWTblLastChgd_Type()
)
tmnxIPsecGWTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWTblLastChgd.setStatus("current")
_TmnxIPsecGWTable_Object = MibTable
tmnxIPsecGWTable = _TmnxIPsecGWTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19)
)
if mibBuilder.loadTexts:
    tmnxIPsecGWTable.setStatus("current")
_TmnxIPsecGWEntry_Object = MibTableRow
tmnxIPsecGWEntry = _TmnxIPsecGWEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1)
)
tmnxIPsecGWEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxIPsecGWEntry.setStatus("current")
_TmnxIPsecGWRowStatus_Type = RowStatus
_TmnxIPsecGWRowStatus_Object = MibTableColumn
tmnxIPsecGWRowStatus = _TmnxIPsecGWRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 1),
    _TmnxIPsecGWRowStatus_Type()
)
tmnxIPsecGWRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWRowStatus.setStatus("current")
_TmnxIPsecGWLastMgmtChange_Type = TimeStamp
_TmnxIPsecGWLastMgmtChange_Object = MibTableColumn
tmnxIPsecGWLastMgmtChange = _TmnxIPsecGWLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 2),
    _TmnxIPsecGWLastMgmtChange_Type()
)
tmnxIPsecGWLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWLastMgmtChange.setStatus("current")


class _TmnxIPsecGWAdminState_Type(TmnxAdminState):
    """Custom type tmnxIPsecGWAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIPsecGWAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIPsecGWAdminState_Object = MibTableColumn
tmnxIPsecGWAdminState = _TmnxIPsecGWAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 3),
    _TmnxIPsecGWAdminState_Type()
)
tmnxIPsecGWAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWAdminState.setStatus("current")
_TmnxIPsecGWOperState_Type = TmnxIPsecOperState
_TmnxIPsecGWOperState_Object = MibTableColumn
tmnxIPsecGWOperState = _TmnxIPsecGWOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 4),
    _TmnxIPsecGWOperState_Type()
)
tmnxIPsecGWOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWOperState.setStatus("current")


class _TmnxIPsecGWTunnelPolicyTemp_Type(TmnxIPsecTunnelTemplateIdOrZero):
    """Custom type tmnxIPsecGWTunnelPolicyTemp based on TmnxIPsecTunnelTemplateIdOrZero"""
    defaultValue = 0


_TmnxIPsecGWTunnelPolicyTemp_Type.__name__ = "TmnxIPsecTunnelTemplateIdOrZero"
_TmnxIPsecGWTunnelPolicyTemp_Object = MibTableColumn
tmnxIPsecGWTunnelPolicyTemp = _TmnxIPsecGWTunnelPolicyTemp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 5),
    _TmnxIPsecGWTunnelPolicyTemp_Type()
)
tmnxIPsecGWTunnelPolicyTemp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWTunnelPolicyTemp.setStatus("current")


class _TmnxIPsecGWSecureService_Type(TmnxServId):
    """Custom type tmnxIPsecGWSecureService based on TmnxServId"""
    defaultValue = 0


_TmnxIPsecGWSecureService_Type.__name__ = "TmnxServId"
_TmnxIPsecGWSecureService_Object = MibTableColumn
tmnxIPsecGWSecureService = _TmnxIPsecGWSecureService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 6),
    _TmnxIPsecGWSecureService_Type()
)
tmnxIPsecGWSecureService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWSecureService.setStatus("current")


class _TmnxIPsecGWIfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWIfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWIfName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWIfName_Object = MibTableColumn
tmnxIPsecGWIfName = _TmnxIPsecGWIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 7),
    _TmnxIPsecGWIfName_Type()
)
tmnxIPsecGWIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWIfName.setStatus("current")


class _TmnxIPsecGWInetAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWInetAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWInetAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWInetAddrType_Object = MibTableColumn
tmnxIPsecGWInetAddrType = _TmnxIPsecGWInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 8),
    _TmnxIPsecGWInetAddrType_Type()
)
tmnxIPsecGWInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWInetAddrType.setStatus("current")


class _TmnxIPsecGWInetAddress_Type(InetAddress):
    """Custom type tmnxIPsecGWInetAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecGWInetAddress_Type.__name__ = "InetAddress"
_TmnxIPsecGWInetAddress_Object = MibTableColumn
tmnxIPsecGWInetAddress = _TmnxIPsecGWInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 9),
    _TmnxIPsecGWInetAddress_Type()
)
tmnxIPsecGWInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWInetAddress.setStatus("current")


class _TmnxIPsecGWIkePolicyId_Type(TmnxIkePolicyIdOrZero):
    """Custom type tmnxIPsecGWIkePolicyId based on TmnxIkePolicyIdOrZero"""
    defaultValue = 0


_TmnxIPsecGWIkePolicyId_Type.__name__ = "TmnxIkePolicyIdOrZero"
_TmnxIPsecGWIkePolicyId_Object = MibTableColumn
tmnxIPsecGWIkePolicyId = _TmnxIPsecGWIkePolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 10),
    _TmnxIPsecGWIkePolicyId_Type()
)
tmnxIPsecGWIkePolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWIkePolicyId.setStatus("current")


class _TmnxIPsecGWIkePreShared_Type(OctetString):
    """Custom type tmnxIPsecGWIkePreShared based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxIPsecGWIkePreShared_Type.__name__ = "OctetString"
_TmnxIPsecGWIkePreShared_Object = MibTableColumn
tmnxIPsecGWIkePreShared = _TmnxIPsecGWIkePreShared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 11),
    _TmnxIPsecGWIkePreShared_Type()
)
tmnxIPsecGWIkePreShared.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWIkePreShared.setStatus("current")


class _TmnxIPsecGWLclX509Cert_Type(DisplayString):
    """Custom type tmnxIPsecGWLclX509Cert based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxIPsecGWLclX509Cert_Type.__name__ = "DisplayString"
_TmnxIPsecGWLclX509Cert_Object = MibTableColumn
tmnxIPsecGWLclX509Cert = _TmnxIPsecGWLclX509Cert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 12),
    _TmnxIPsecGWLclX509Cert_Type()
)
tmnxIPsecGWLclX509Cert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWLclX509Cert.setStatus("obsolete")


class _TmnxIPsecGWLclPrivateKey_Type(DisplayString):
    """Custom type tmnxIPsecGWLclPrivateKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxIPsecGWLclPrivateKey_Type.__name__ = "DisplayString"
_TmnxIPsecGWLclPrivateKey_Object = MibTableColumn
tmnxIPsecGWLclPrivateKey = _TmnxIPsecGWLclPrivateKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 13),
    _TmnxIPsecGWLclPrivateKey_Type()
)
tmnxIPsecGWLclPrivateKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWLclPrivateKey.setStatus("obsolete")


class _TmnxIPsecGWOperFlags_Type(Bits):
    """Custom type tmnxIPsecGWOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("localIpUnreachable", 0),
          ("gatewayAdminDown", 1),
          ("x509CertUnavailable", 2),
          ("privateKeyUnavailable", 3),
          ("caCertUnavailable", 4),
          ("caCRLUnavailable", 5),
          ("trustAnchorsDown", 6),
          ("certProfileDown", 7),
          ("invalidCertKeyCombo", 8),
          ("ikeNotReady", 9))
    )

_TmnxIPsecGWOperFlags_Type.__name__ = "Bits"
_TmnxIPsecGWOperFlags_Object = MibTableColumn
tmnxIPsecGWOperFlags = _TmnxIPsecGWOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 14),
    _TmnxIPsecGWOperFlags_Type()
)
tmnxIPsecGWOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWOperFlags.setStatus("current")


class _TmnxIPsecGWCACert_Type(DisplayString):
    """Custom type tmnxIPsecGWCACert based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxIPsecGWCACert_Type.__name__ = "DisplayString"
_TmnxIPsecGWCACert_Object = MibTableColumn
tmnxIPsecGWCACert = _TmnxIPsecGWCACert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 15),
    _TmnxIPsecGWCACert_Type()
)
tmnxIPsecGWCACert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCACert.setStatus("obsolete")


class _TmnxIPsecGWCACertRevocList_Type(DisplayString):
    """Custom type tmnxIPsecGWCACertRevocList based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxIPsecGWCACertRevocList_Type.__name__ = "DisplayString"
_TmnxIPsecGWCACertRevocList_Object = MibTableColumn
tmnxIPsecGWCACertRevocList = _TmnxIPsecGWCACertRevocList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 16),
    _TmnxIPsecGWCACertRevocList_Type()
)
tmnxIPsecGWCACertRevocList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCACertRevocList.setStatus("obsolete")
_TmnxIPsecGWName_Type = TNamedItem
_TmnxIPsecGWName_Object = MibTableColumn
tmnxIPsecGWName = _TmnxIPsecGWName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 17),
    _TmnxIPsecGWName_Type()
)
tmnxIPsecGWName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWName.setStatus("current")


class _TmnxIPsecGWCertTrustAnchor_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWCertTrustAnchor based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWCertTrustAnchor_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWCertTrustAnchor_Object = MibTableColumn
tmnxIPsecGWCertTrustAnchor = _TmnxIPsecGWCertTrustAnchor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 18),
    _TmnxIPsecGWCertTrustAnchor_Type()
)
tmnxIPsecGWCertTrustAnchor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCertTrustAnchor.setStatus("obsolete")


class _TmnxIPsecGWLocalIdType_Type(TmnxIPsecLocalIdType):
    """Custom type tmnxIPsecGWLocalIdType based on TmnxIPsecLocalIdType"""
    defaultValue = 0


_TmnxIPsecGWLocalIdType_Type.__name__ = "TmnxIPsecLocalIdType"
_TmnxIPsecGWLocalIdType_Object = MibTableColumn
tmnxIPsecGWLocalIdType = _TmnxIPsecGWLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 19),
    _TmnxIPsecGWLocalIdType_Type()
)
tmnxIPsecGWLocalIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWLocalIdType.setStatus("current")


class _TmnxIPsecGWLocalIdValue_Type(DisplayString):
    """Custom type tmnxIPsecGWLocalIdValue based on DisplayString"""
    defaultHexValue = ""


_TmnxIPsecGWLocalIdValue_Type.__name__ = "DisplayString"
_TmnxIPsecGWLocalIdValue_Object = MibTableColumn
tmnxIPsecGWLocalIdValue = _TmnxIPsecGWLocalIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 20),
    _TmnxIPsecGWLocalIdValue_Type()
)
tmnxIPsecGWLocalIdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWLocalIdValue.setStatus("current")


class _TmnxIPsecGWCSVPrimary_Type(TmnxCertRevStatus):
    """Custom type tmnxIPsecGWCSVPrimary based on TmnxCertRevStatus"""
    defaultValue = 1


_TmnxIPsecGWCSVPrimary_Type.__name__ = "TmnxCertRevStatus"
_TmnxIPsecGWCSVPrimary_Object = MibTableColumn
tmnxIPsecGWCSVPrimary = _TmnxIPsecGWCSVPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 21),
    _TmnxIPsecGWCSVPrimary_Type()
)
tmnxIPsecGWCSVPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCSVPrimary.setStatus("current")


class _TmnxIPsecGWCSVSecondary_Type(TmnxCertRevStatusOrNone):
    """Custom type tmnxIPsecGWCSVSecondary based on TmnxCertRevStatusOrNone"""
    defaultValue = 0


_TmnxIPsecGWCSVSecondary_Type.__name__ = "TmnxCertRevStatusOrNone"
_TmnxIPsecGWCSVSecondary_Object = MibTableColumn
tmnxIPsecGWCSVSecondary = _TmnxIPsecGWCSVSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 22),
    _TmnxIPsecGWCSVSecondary_Type()
)
tmnxIPsecGWCSVSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCSVSecondary.setStatus("current")


class _TmnxIPsecGWCSVDefResult_Type(Integer32):
    """Custom type tmnxIPsecGWCSVDefResult based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("revoked", 0),
          ("good", 1))
    )


_TmnxIPsecGWCSVDefResult_Type.__name__ = "Integer32"
_TmnxIPsecGWCSVDefResult_Object = MibTableColumn
tmnxIPsecGWCSVDefResult = _TmnxIPsecGWCSVDefResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 23),
    _TmnxIPsecGWCSVDefResult_Type()
)
tmnxIPsecGWCSVDefResult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCSVDefResult.setStatus("current")


class _TmnxIPsecGWRadAcctgPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWRadAcctgPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWRadAcctgPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWRadAcctgPolicy_Object = MibTableColumn
tmnxIPsecGWRadAcctgPolicy = _TmnxIPsecGWRadAcctgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 24),
    _TmnxIPsecGWRadAcctgPolicy_Type()
)
tmnxIPsecGWRadAcctgPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWRadAcctgPolicy.setStatus("current")


class _TmnxIPsecGWRadAuthPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWRadAuthPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWRadAuthPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWRadAuthPolicy_Object = MibTableColumn
tmnxIPsecGWRadAuthPolicy = _TmnxIPsecGWRadAuthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 25),
    _TmnxIPsecGWRadAuthPolicy_Type()
)
tmnxIPsecGWRadAuthPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWRadAuthPolicy.setStatus("current")


class _TmnxIPsecGWCertProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWCertProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWCertProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWCertProfile_Object = MibTableColumn
tmnxIPsecGWCertProfile = _TmnxIPsecGWCertProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 26),
    _TmnxIPsecGWCertProfile_Type()
)
tmnxIPsecGWCertProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCertProfile.setStatus("current")


class _TmnxIPsecGWCertTrstAnchrProf_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWCertTrstAnchrProf based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWCertTrstAnchrProf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWCertTrstAnchrProf_Object = MibTableColumn
tmnxIPsecGWCertTrstAnchrProf = _TmnxIPsecGWCertTrstAnchrProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 27),
    _TmnxIPsecGWCertTrstAnchrProf_Type()
)
tmnxIPsecGWCertTrstAnchrProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCertTrstAnchrProf.setStatus("current")


class _TmnxIPsecGWClientDatabaseName_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWClientDatabaseName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxIPsecGWClientDatabaseName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWClientDatabaseName_Object = MibTableColumn
tmnxIPsecGWClientDatabaseName = _TmnxIPsecGWClientDatabaseName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 28),
    _TmnxIPsecGWClientDatabaseName_Type()
)
tmnxIPsecGWClientDatabaseName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWClientDatabaseName.setStatus("current")


class _TmnxIPsecGWClientDatabasFallback_Type(TruthValue):
    """Custom type tmnxIPsecGWClientDatabasFallback based on TruthValue"""
    defaultValue = 1


_TmnxIPsecGWClientDatabasFallback_Type.__name__ = "TruthValue"
_TmnxIPsecGWClientDatabasFallback_Object = MibTableColumn
tmnxIPsecGWClientDatabasFallback = _TmnxIPsecGWClientDatabasFallback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 29),
    _TmnxIPsecGWClientDatabasFallback_Type()
)
tmnxIPsecGWClientDatabasFallback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWClientDatabasFallback.setStatus("current")


class _TmnxIPsecGWMaxNumPh1SaKeys_Type(Unsigned32):
    """Custom type tmnxIPsecGWMaxNumPh1SaKeys based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TmnxIPsecGWMaxNumPh1SaKeys_Type.__name__ = "Unsigned32"
_TmnxIPsecGWMaxNumPh1SaKeys_Object = MibTableColumn
tmnxIPsecGWMaxNumPh1SaKeys = _TmnxIPsecGWMaxNumPh1SaKeys_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 30),
    _TmnxIPsecGWMaxNumPh1SaKeys_Type()
)
tmnxIPsecGWMaxNumPh1SaKeys.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWMaxNumPh1SaKeys.setStatus("current")


class _TmnxIPsecGWMaxNumPh2SaKeys_Type(Unsigned32):
    """Custom type tmnxIPsecGWMaxNumPh2SaKeys based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_TmnxIPsecGWMaxNumPh2SaKeys_Type.__name__ = "Unsigned32"
_TmnxIPsecGWMaxNumPh2SaKeys_Object = MibTableColumn
tmnxIPsecGWMaxNumPh2SaKeys = _TmnxIPsecGWMaxNumPh2SaKeys_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 31),
    _TmnxIPsecGWMaxNumPh2SaKeys_Type()
)
tmnxIPsecGWMaxNumPh2SaKeys.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWMaxNumPh2SaKeys.setStatus("current")


class _TmnxIPsecGWSecureServiceName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxIPsecGWSecureServiceName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWSecureServiceName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxIPsecGWSecureServiceName_Object = MibTableColumn
tmnxIPsecGWSecureServiceName = _TmnxIPsecGWSecureServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 32),
    _TmnxIPsecGWSecureServiceName_Type()
)
tmnxIPsecGWSecureServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWSecureServiceName.setStatus("current")
_TIPsecRUTnlTable_Object = MibTable
tIPsecRUTnlTable = _TIPsecRUTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20)
)
if mibBuilder.loadTexts:
    tIPsecRUTnlTable.setStatus("current")
_TIPsecRUTnlEntry_Object = MibTableRow
tIPsecRUTnlEntry = _TIPsecRUTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1)
)
tIPsecRUTnlEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlPort"),
)
if mibBuilder.loadTexts:
    tIPsecRUTnlEntry.setStatus("current")
_TIPsecRUTnlInetAddrType_Type = InetAddressType
_TIPsecRUTnlInetAddrType_Object = MibTableColumn
tIPsecRUTnlInetAddrType = _TIPsecRUTnlInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 1),
    _TIPsecRUTnlInetAddrType_Type()
)
tIPsecRUTnlInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUTnlInetAddrType.setStatus("current")


class _TIPsecRUTnlInetAddress_Type(InetAddress):
    """Custom type tIPsecRUTnlInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecRUTnlInetAddress_Type.__name__ = "InetAddress"
_TIPsecRUTnlInetAddress_Object = MibTableColumn
tIPsecRUTnlInetAddress = _TIPsecRUTnlInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 2),
    _TIPsecRUTnlInetAddress_Type()
)
tIPsecRUTnlInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUTnlInetAddress.setStatus("current")
_TIPsecRUTnlPort_Type = TTcpUdpPort
_TIPsecRUTnlPort_Object = MibTableColumn
tIPsecRUTnlPort = _TIPsecRUTnlPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 3),
    _TIPsecRUTnlPort_Type()
)
tIPsecRUTnlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUTnlPort.setStatus("current")
_TIPsecRUTnlPrivateIpAddrType_Type = InetAddressType
_TIPsecRUTnlPrivateIpAddrType_Object = MibTableColumn
tIPsecRUTnlPrivateIpAddrType = _TIPsecRUTnlPrivateIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 4),
    _TIPsecRUTnlPrivateIpAddrType_Type()
)
tIPsecRUTnlPrivateIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateIpAddrType.setStatus("current")


class _TIPsecRUTnlPrivateIpAddr_Type(InetAddress):
    """Custom type tIPsecRUTnlPrivateIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecRUTnlPrivateIpAddr_Type.__name__ = "InetAddress"
_TIPsecRUTnlPrivateIpAddr_Object = MibTableColumn
tIPsecRUTnlPrivateIpAddr = _TIPsecRUTnlPrivateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 5),
    _TIPsecRUTnlPrivateIpAddr_Type()
)
tIPsecRUTnlPrivateIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateIpAddr.setStatus("current")
_TIPsecRUTnlPrivateIpPrefixLen_Type = InetAddressPrefixLength
_TIPsecRUTnlPrivateIpPrefixLen_Object = MibTableColumn
tIPsecRUTnlPrivateIpPrefixLen = _TIPsecRUTnlPrivateIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 6),
    _TIPsecRUTnlPrivateIpPrefixLen_Type()
)
tIPsecRUTnlPrivateIpPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateIpPrefixLen.setStatus("current")
_TIPsecRUTnlTempId_Type = TmnxIPsecTunnelTemplateId
_TIPsecRUTnlTempId_Object = MibTableColumn
tIPsecRUTnlTempId = _TIPsecRUTnlTempId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 7),
    _TIPsecRUTnlTempId_Type()
)
tIPsecRUTnlTempId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlTempId.setStatus("current")


class _TIPsecRUTnlIPsecSALifeTime_Type(Unsigned32):
    """Custom type tIPsecRUTnlIPsecSALifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 31536000),
    )


_TIPsecRUTnlIPsecSALifeTime_Type.__name__ = "Unsigned32"
_TIPsecRUTnlIPsecSALifeTime_Object = MibTableColumn
tIPsecRUTnlIPsecSALifeTime = _TIPsecRUTnlIPsecSALifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 8),
    _TIPsecRUTnlIPsecSALifeTime_Type()
)
tIPsecRUTnlIPsecSALifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlIPsecSALifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tIPsecRUTnlIPsecSALifeTime.setUnits("seconds")
_TIPsecRUTnlPfsDHGroup_Type = TmnxIkePolicyDHGroupOrZero
_TIPsecRUTnlPfsDHGroup_Object = MibTableColumn
tIPsecRUTnlPfsDHGroup = _TIPsecRUTnlPfsDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 9),
    _TIPsecRUTnlPfsDHGroup_Type()
)
tIPsecRUTnlPfsDHGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPfsDHGroup.setStatus("current")


class _TIPsecRUTnlReplayWindow_Type(Unsigned32):
    """Custom type tIPsecRUTnlReplayWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
    )


_TIPsecRUTnlReplayWindow_Type.__name__ = "Unsigned32"
_TIPsecRUTnlReplayWindow_Object = MibTableColumn
tIPsecRUTnlReplayWindow = _TIPsecRUTnlReplayWindow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 10),
    _TIPsecRUTnlReplayWindow_Type()
)
tIPsecRUTnlReplayWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlReplayWindow.setStatus("current")
_TIPsecRUTnlPrivateSvcId_Type = TmnxServId
_TIPsecRUTnlPrivateSvcId_Object = MibTableColumn
tIPsecRUTnlPrivateSvcId = _TIPsecRUTnlPrivateSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 11),
    _TIPsecRUTnlPrivateSvcId_Type()
)
tIPsecRUTnlPrivateSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateSvcId.setStatus("current")
_TIPsecRUTnlPrivateIfIndex_Type = InterfaceIndex
_TIPsecRUTnlPrivateIfIndex_Object = MibTableColumn
tIPsecRUTnlPrivateIfIndex = _TIPsecRUTnlPrivateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 12),
    _TIPsecRUTnlPrivateIfIndex_Type()
)
tIPsecRUTnlPrivateIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateIfIndex.setStatus("current")
_TIPsecRUTnlHasBiDirectionalSA_Type = TruthValue
_TIPsecRUTnlHasBiDirectionalSA_Object = MibTableColumn
tIPsecRUTnlHasBiDirectionalSA = _TIPsecRUTnlHasBiDirectionalSA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 13),
    _TIPsecRUTnlHasBiDirectionalSA_Type()
)
tIPsecRUTnlHasBiDirectionalSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlHasBiDirectionalSA.setStatus("current")
_TIPsecRUTnlHostISA_Type = TmnxHwIndexOrZero
_TIPsecRUTnlHostISA_Object = MibTableColumn
tIPsecRUTnlHostISA = _TIPsecRUTnlHostISA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 14),
    _TIPsecRUTnlHostISA_Type()
)
tIPsecRUTnlHostISA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlHostISA.setStatus("current")
_TIPsecRUTnlMatchTrustAnchor_Type = TNamedItemOrEmpty
_TIPsecRUTnlMatchTrustAnchor_Object = MibTableColumn
tIPsecRUTnlMatchTrustAnchor = _TIPsecRUTnlMatchTrustAnchor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 15),
    _TIPsecRUTnlMatchTrustAnchor_Type()
)
tIPsecRUTnlMatchTrustAnchor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlMatchTrustAnchor.setStatus("current")
_TIPsecRUTnlOperChanged_Type = TimeStamp
_TIPsecRUTnlOperChanged_Object = MibTableColumn
tIPsecRUTnlOperChanged = _TIPsecRUTnlOperChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 16),
    _TIPsecRUTnlOperChanged_Type()
)
tIPsecRUTnlOperChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlOperChanged.setStatus("current")


class _TIPsecRUTnlIkeIdType_Type(Integer32):
    """Custom type tIPsecRUTnlIkeIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ipv4Addr", 1),
          ("fqdn", 2),
          ("rfc822Addr", 3),
          ("ipv6Addr", 5),
          ("derAsn1Dn", 9),
          ("derAsn1Gn", 10),
          ("keyId", 11))
    )


_TIPsecRUTnlIkeIdType_Type.__name__ = "Integer32"
_TIPsecRUTnlIkeIdType_Object = MibTableColumn
tIPsecRUTnlIkeIdType = _TIPsecRUTnlIkeIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 17),
    _TIPsecRUTnlIkeIdType_Type()
)
tIPsecRUTnlIkeIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlIkeIdType.setStatus("current")
_TIPsecRUTnlIkeIdValue_Type = DisplayString
_TIPsecRUTnlIkeIdValue_Object = MibTableColumn
tIPsecRUTnlIkeIdValue = _TIPsecRUTnlIkeIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 18),
    _TIPsecRUTnlIkeIdValue_Type()
)
tIPsecRUTnlIkeIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlIkeIdValue.setStatus("current")
_TIPsecRUTnlPrivateIpAddr2Type_Type = InetAddressType
_TIPsecRUTnlPrivateIpAddr2Type_Object = MibTableColumn
tIPsecRUTnlPrivateIpAddr2Type = _TIPsecRUTnlPrivateIpAddr2Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 19),
    _TIPsecRUTnlPrivateIpAddr2Type_Type()
)
tIPsecRUTnlPrivateIpAddr2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateIpAddr2Type.setStatus("current")


class _TIPsecRUTnlPrivateIpAddr2_Type(InetAddress):
    """Custom type tIPsecRUTnlPrivateIpAddr2 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TIPsecRUTnlPrivateIpAddr2_Type.__name__ = "InetAddress"
_TIPsecRUTnlPrivateIpAddr2_Object = MibTableColumn
tIPsecRUTnlPrivateIpAddr2 = _TIPsecRUTnlPrivateIpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 20),
    _TIPsecRUTnlPrivateIpAddr2_Type()
)
tIPsecRUTnlPrivateIpAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateIpAddr2.setStatus("current")
_TIPsecRUTnlPrivateIpPrefixLen2_Type = InetAddressPrefixLength
_TIPsecRUTnlPrivateIpPrefixLen2_Object = MibTableColumn
tIPsecRUTnlPrivateIpPrefixLen2 = _TIPsecRUTnlPrivateIpPrefixLen2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 21),
    _TIPsecRUTnlPrivateIpPrefixLen2_Type()
)
tIPsecRUTnlPrivateIpPrefixLen2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateIpPrefixLen2.setStatus("current")
_TIPsecRUTnlInUseTsList_Type = TNamedItem
_TIPsecRUTnlInUseTsList_Object = MibTableColumn
tIPsecRUTnlInUseTsList = _TIPsecRUTnlInUseTsList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 22),
    _TIPsecRUTnlInUseTsList_Type()
)
tIPsecRUTnlInUseTsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlInUseTsList.setStatus("current")
_TIPsecRUTnlInUsePreSharedKey_Type = TLNamedItemOrEmpty
_TIPsecRUTnlInUsePreSharedKey_Object = MibTableColumn
tIPsecRUTnlInUsePreSharedKey = _TIPsecRUTnlInUsePreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 23),
    _TIPsecRUTnlInUsePreSharedKey_Type()
)
tIPsecRUTnlInUsePreSharedKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlInUsePreSharedKey.setStatus("current")
_TIPsecRUTnlPubTcpMss_Type = Integer32
_TIPsecRUTnlPubTcpMss_Object = MibTableColumn
tIPsecRUTnlPubTcpMss = _TIPsecRUTnlPubTcpMss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 24),
    _TIPsecRUTnlPubTcpMss_Type()
)
tIPsecRUTnlPubTcpMss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPubTcpMss.setStatus("current")
if mibBuilder.loadTexts:
    tIPsecRUTnlPubTcpMss.setUnits("octets")
_TIPsecRUTnlPrivTcpMss_Type = Integer32
_TIPsecRUTnlPrivTcpMss_Object = MibTableColumn
tIPsecRUTnlPrivTcpMss = _TIPsecRUTnlPrivTcpMss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 25),
    _TIPsecRUTnlPrivTcpMss_Type()
)
tIPsecRUTnlPrivTcpMss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivTcpMss.setStatus("current")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivTcpMss.setUnits("octets")
_TIPsecRUTnlInUseIkePolicy_Type = TmnxIkePolicyIdOrZero
_TIPsecRUTnlInUseIkePolicy_Object = MibTableColumn
tIPsecRUTnlInUseIkePolicy = _TIPsecRUTnlInUseIkePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 26),
    _TIPsecRUTnlInUseIkePolicy_Type()
)
tIPsecRUTnlInUseIkePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlInUseIkePolicy.setStatus("current")
_TIPsecRUTnlHostEsa_Type = TmnxEsaIdOrZero
_TIPsecRUTnlHostEsa_Object = MibTableColumn
tIPsecRUTnlHostEsa = _TIPsecRUTnlHostEsa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 27),
    _TIPsecRUTnlHostEsa_Type()
)
tIPsecRUTnlHostEsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlHostEsa.setStatus("current")
_TIPsecRUTnlHostEsaVm_Type = TmnxEsaVmIdOrZero
_TIPsecRUTnlHostEsaVm_Object = MibTableColumn
tIPsecRUTnlHostEsaVm = _TIPsecRUTnlHostEsaVm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 28),
    _TIPsecRUTnlHostEsaVm_Type()
)
tIPsecRUTnlHostEsaVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlHostEsaVm.setStatus("current")
_TIPsecRUTnlStatsTable_Object = MibTable
tIPsecRUTnlStatsTable = _TIPsecRUTnlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21)
)
if mibBuilder.loadTexts:
    tIPsecRUTnlStatsTable.setStatus("current")
_TIPsecRUTnlStatsEntry_Object = MibTableRow
tIPsecRUTnlStatsEntry = _TIPsecRUTnlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1)
)
tIPsecRUTnlStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlPort"),
)
if mibBuilder.loadTexts:
    tIPsecRUTnlStatsEntry.setStatus("current")


class _TIPsecRUTnlIsakmpState_Type(Integer32):
    """Custom type tIPsecRUTnlIsakmpState based on Integer32"""
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


_TIPsecRUTnlIsakmpState_Type.__name__ = "Integer32"
_TIPsecRUTnlIsakmpState_Object = MibTableColumn
tIPsecRUTnlIsakmpState = _TIPsecRUTnlIsakmpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 1),
    _TIPsecRUTnlIsakmpState_Type()
)
tIPsecRUTnlIsakmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlIsakmpState.setStatus("current")
_TIPsecRUTnlIsakmpEstabTime_Type = TimeStamp
_TIPsecRUTnlIsakmpEstabTime_Object = MibTableColumn
tIPsecRUTnlIsakmpEstabTime = _TIPsecRUTnlIsakmpEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 2),
    _TIPsecRUTnlIsakmpEstabTime_Type()
)
tIPsecRUTnlIsakmpEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlIsakmpEstabTime.setStatus("current")
_TIPsecRUTnlIsakmpNegLifeTime_Type = Unsigned32
_TIPsecRUTnlIsakmpNegLifeTime_Object = MibTableColumn
tIPsecRUTnlIsakmpNegLifeTime = _TIPsecRUTnlIsakmpNegLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 3),
    _TIPsecRUTnlIsakmpNegLifeTime_Type()
)
tIPsecRUTnlIsakmpNegLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlIsakmpNegLifeTime.setStatus("current")
_TIPsecRUTnlNumDpdTx_Type = Counter32
_TIPsecRUTnlNumDpdTx_Object = MibTableColumn
tIPsecRUTnlNumDpdTx = _TIPsecRUTnlNumDpdTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 4),
    _TIPsecRUTnlNumDpdTx_Type()
)
tIPsecRUTnlNumDpdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumDpdTx.setStatus("current")
_TIPsecRUTnlNumDpdRx_Type = Counter32
_TIPsecRUTnlNumDpdRx_Object = MibTableColumn
tIPsecRUTnlNumDpdRx = _TIPsecRUTnlNumDpdRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 5),
    _TIPsecRUTnlNumDpdRx_Type()
)
tIPsecRUTnlNumDpdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumDpdRx.setStatus("current")
_TIPsecRUTnlNumDpdAckTx_Type = Counter32
_TIPsecRUTnlNumDpdAckTx_Object = MibTableColumn
tIPsecRUTnlNumDpdAckTx = _TIPsecRUTnlNumDpdAckTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 6),
    _TIPsecRUTnlNumDpdAckTx_Type()
)
tIPsecRUTnlNumDpdAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumDpdAckTx.setStatus("current")
_TIPsecRUTnlNumDpdAckRx_Type = Counter32
_TIPsecRUTnlNumDpdAckRx_Object = MibTableColumn
tIPsecRUTnlNumDpdAckRx = _TIPsecRUTnlNumDpdAckRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 7),
    _TIPsecRUTnlNumDpdAckRx_Type()
)
tIPsecRUTnlNumDpdAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumDpdAckRx.setStatus("current")
_TIPsecRUTnlNumExpRx_Type = Counter32
_TIPsecRUTnlNumExpRx_Object = MibTableColumn
tIPsecRUTnlNumExpRx = _TIPsecRUTnlNumExpRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 8),
    _TIPsecRUTnlNumExpRx_Type()
)
tIPsecRUTnlNumExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumExpRx.setStatus("current")
_TIPsecRUTnlNumInvalidDpdRx_Type = Counter32
_TIPsecRUTnlNumInvalidDpdRx_Object = MibTableColumn
tIPsecRUTnlNumInvalidDpdRx = _TIPsecRUTnlNumInvalidDpdRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 9),
    _TIPsecRUTnlNumInvalidDpdRx_Type()
)
tIPsecRUTnlNumInvalidDpdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumInvalidDpdRx.setStatus("current")
_TIPsecRUTnlNumCtrlPktsTx_Type = Counter32
_TIPsecRUTnlNumCtrlPktsTx_Object = MibTableColumn
tIPsecRUTnlNumCtrlPktsTx = _TIPsecRUTnlNumCtrlPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 10),
    _TIPsecRUTnlNumCtrlPktsTx_Type()
)
tIPsecRUTnlNumCtrlPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumCtrlPktsTx.setStatus("current")
_TIPsecRUTnlNumCtrlPktsRx_Type = Counter32
_TIPsecRUTnlNumCtrlPktsRx_Object = MibTableColumn
tIPsecRUTnlNumCtrlPktsRx = _TIPsecRUTnlNumCtrlPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 11),
    _TIPsecRUTnlNumCtrlPktsRx_Type()
)
tIPsecRUTnlNumCtrlPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumCtrlPktsRx.setStatus("current")
_TIPsecRUTnlNumCtrlTxErrors_Type = Counter32
_TIPsecRUTnlNumCtrlTxErrors_Object = MibTableColumn
tIPsecRUTnlNumCtrlTxErrors = _TIPsecRUTnlNumCtrlTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 12),
    _TIPsecRUTnlNumCtrlTxErrors_Type()
)
tIPsecRUTnlNumCtrlTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumCtrlTxErrors.setStatus("current")
_TIPsecRUTnlNumCtrlRxErrors_Type = Counter32
_TIPsecRUTnlNumCtrlRxErrors_Object = MibTableColumn
tIPsecRUTnlNumCtrlRxErrors = _TIPsecRUTnlNumCtrlRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 13),
    _TIPsecRUTnlNumCtrlRxErrors_Type()
)
tIPsecRUTnlNumCtrlRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumCtrlRxErrors.setStatus("current")
_TIPsecRUTnlMatCertEntryId_Type = Integer32
_TIPsecRUTnlMatCertEntryId_Object = MibTableColumn
tIPsecRUTnlMatCertEntryId = _TIPsecRUTnlMatCertEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 14),
    _TIPsecRUTnlMatCertEntryId_Type()
)
tIPsecRUTnlMatCertEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlMatCertEntryId.setStatus("current")
_TIPsecRUTnlCertProfName_Type = TNamedItemOrEmpty
_TIPsecRUTnlCertProfName_Object = MibTableColumn
tIPsecRUTnlCertProfName = _TIPsecRUTnlCertProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 15),
    _TIPsecRUTnlCertProfName_Type()
)
tIPsecRUTnlCertProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlCertProfName.setStatus("current")


class _TIPsecRUTnlClientDBClientId_Type(Unsigned32):
    """Custom type tIPsecRUTnlClientDBClientId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8000),
    )


_TIPsecRUTnlClientDBClientId_Type.__name__ = "Unsigned32"
_TIPsecRUTnlClientDBClientId_Object = MibTableColumn
tIPsecRUTnlClientDBClientId = _TIPsecRUTnlClientDBClientId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 17),
    _TIPsecRUTnlClientDBClientId_Type()
)
tIPsecRUTnlClientDBClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlClientDBClientId.setStatus("current")
_TIPsecRUTnlStatsIsakmpAuthAlg_Type = TmnxAuthAlgorithm
_TIPsecRUTnlStatsIsakmpAuthAlg_Object = MibTableColumn
tIPsecRUTnlStatsIsakmpAuthAlg = _TIPsecRUTnlStatsIsakmpAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 18),
    _TIPsecRUTnlStatsIsakmpAuthAlg_Type()
)
tIPsecRUTnlStatsIsakmpAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlStatsIsakmpAuthAlg.setStatus("current")
_TIPsecRUTnlStatsIsakmpEncrAlg_Type = TmnxEncrAlgorithm
_TIPsecRUTnlStatsIsakmpEncrAlg_Object = MibTableColumn
tIPsecRUTnlStatsIsakmpEncrAlg = _TIPsecRUTnlStatsIsakmpEncrAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 19),
    _TIPsecRUTnlStatsIsakmpEncrAlg_Type()
)
tIPsecRUTnlStatsIsakmpEncrAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlStatsIsakmpEncrAlg.setStatus("current")
_TIPsecRUTnlStatsIsakmpPfsDhGrp_Type = TmnxIkePolicyDHGroupOrZero
_TIPsecRUTnlStatsIsakmpPfsDhGrp_Object = MibTableColumn
tIPsecRUTnlStatsIsakmpPfsDhGrp = _TIPsecRUTnlStatsIsakmpPfsDhGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 20),
    _TIPsecRUTnlStatsIsakmpPfsDhGrp_Type()
)
tIPsecRUTnlStatsIsakmpPfsDhGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlStatsIsakmpPfsDhGrp.setStatus("current")


class _TIPsecRUTnlStatsIkeTranPrfAlg_Type(Integer32):
    """Custom type tIPsecRUTnlStatsIkeTranPrfAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("sha1", 3),
          ("sha256", 4),
          ("sha384", 5),
          ("sha512", 6),
          ("aesXcbc", 7),
          ("sameAsAuth", 8))
    )


_TIPsecRUTnlStatsIkeTranPrfAlg_Type.__name__ = "Integer32"
_TIPsecRUTnlStatsIkeTranPrfAlg_Object = MibTableColumn
tIPsecRUTnlStatsIkeTranPrfAlg = _TIPsecRUTnlStatsIkeTranPrfAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 21),
    _TIPsecRUTnlStatsIkeTranPrfAlg_Type()
)
tIPsecRUTnlStatsIkeTranPrfAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlStatsIkeTranPrfAlg.setStatus("current")
_TIPsecRUSATable_Object = MibTable
tIPsecRUSATable = _TIPsecRUSATable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22)
)
if mibBuilder.loadTexts:
    tIPsecRUSATable.setStatus("current")
_TIPsecRUSAEntry_Object = MibTableRow
tIPsecRUSAEntry = _TIPsecRUSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1)
)
tIPsecRUSAEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlPort"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSAId"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSADirection"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSAIndex"),
)
if mibBuilder.loadTexts:
    tIPsecRUSAEntry.setStatus("current")


class _TIPsecRUSAId_Type(Unsigned32):
    """Custom type tIPsecRUSAId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TIPsecRUSAId_Type.__name__ = "Unsigned32"
_TIPsecRUSAId_Object = MibTableColumn
tIPsecRUSAId = _TIPsecRUSAId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 1),
    _TIPsecRUSAId_Type()
)
tIPsecRUSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSAId.setStatus("current")


class _TIPsecRUSAIndex_Type(Unsigned32):
    """Custom type tIPsecRUSAIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TIPsecRUSAIndex_Type.__name__ = "Unsigned32"
_TIPsecRUSAIndex_Object = MibTableColumn
tIPsecRUSAIndex = _TIPsecRUSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 2),
    _TIPsecRUSAIndex_Type()
)
tIPsecRUSAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSAIndex.setStatus("current")
_TIPsecRUSADirection_Type = TmnxIPsecDirection
_TIPsecRUSADirection_Object = MibTableColumn
tIPsecRUSADirection = _TIPsecRUSADirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 3),
    _TIPsecRUSADirection_Type()
)
tIPsecRUSADirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSADirection.setStatus("current")


class _TIPsecRUSAEncryptionKey_Type(OctetString):
    """Custom type tIPsecRUSAEncryptionKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TIPsecRUSAEncryptionKey_Type.__name__ = "OctetString"
_TIPsecRUSAEncryptionKey_Object = MibTableColumn
tIPsecRUSAEncryptionKey = _TIPsecRUSAEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 4),
    _TIPsecRUSAEncryptionKey_Type()
)
tIPsecRUSAEncryptionKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAEncryptionKey.setStatus("current")


class _TIPsecRUSAAuthenticationKey_Type(OctetString):
    """Custom type tIPsecRUSAAuthenticationKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TIPsecRUSAAuthenticationKey_Type.__name__ = "OctetString"
_TIPsecRUSAAuthenticationKey_Object = MibTableColumn
tIPsecRUSAAuthenticationKey = _TIPsecRUSAAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 5),
    _TIPsecRUSAAuthenticationKey_Type()
)
tIPsecRUSAAuthenticationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAAuthenticationKey.setStatus("current")
_TIPsecRUSASpi_Type = Unsigned32
_TIPsecRUSASpi_Object = MibTableColumn
tIPsecRUSASpi = _TIPsecRUSASpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 6),
    _TIPsecRUSASpi_Type()
)
tIPsecRUSASpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSASpi.setStatus("current")
_TIPsecRUSAAuthAlgorithm_Type = TmnxAuthAlgorithm
_TIPsecRUSAAuthAlgorithm_Object = MibTableColumn
tIPsecRUSAAuthAlgorithm = _TIPsecRUSAAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 7),
    _TIPsecRUSAAuthAlgorithm_Type()
)
tIPsecRUSAAuthAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAAuthAlgorithm.setStatus("current")
_TIPsecRUSAEncrAlgorithm_Type = TmnxEncrAlgorithm
_TIPsecRUSAEncrAlgorithm_Object = MibTableColumn
tIPsecRUSAEncrAlgorithm = _TIPsecRUSAEncrAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 8),
    _TIPsecRUSAEncrAlgorithm_Type()
)
tIPsecRUSAEncrAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAEncrAlgorithm.setStatus("current")
_TIPsecRUSAEstablishedTime_Type = TimeStamp
_TIPsecRUSAEstablishedTime_Object = MibTableColumn
tIPsecRUSAEstablishedTime = _TIPsecRUSAEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 9),
    _TIPsecRUSAEstablishedTime_Type()
)
tIPsecRUSAEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAEstablishedTime.setStatus("current")
_TIPsecRUSANegotiatedLifeTime_Type = Unsigned32
_TIPsecRUSANegotiatedLifeTime_Object = MibTableColumn
tIPsecRUSANegotiatedLifeTime = _TIPsecRUSANegotiatedLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 10),
    _TIPsecRUSANegotiatedLifeTime_Type()
)
tIPsecRUSANegotiatedLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSANegotiatedLifeTime.setStatus("current")
_TIPsecRUSALclAddrType_Type = InetAddressType
_TIPsecRUSALclAddrType_Object = MibTableColumn
tIPsecRUSALclAddrType = _TIPsecRUSALclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 11),
    _TIPsecRUSALclAddrType_Type()
)
tIPsecRUSALclAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSALclAddrType.setStatus("obsolete")


class _TIPsecRUSALclAddr_Type(InetAddress):
    """Custom type tIPsecRUSALclAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecRUSALclAddr_Type.__name__ = "InetAddress"
_TIPsecRUSALclAddr_Object = MibTableColumn
tIPsecRUSALclAddr = _TIPsecRUSALclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 12),
    _TIPsecRUSALclAddr_Type()
)
tIPsecRUSALclAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSALclAddr.setStatus("obsolete")
_TIPsecRUSALclAPrefLen_Type = InetAddressPrefixLength
_TIPsecRUSALclAPrefLen_Object = MibTableColumn
tIPsecRUSALclAPrefLen = _TIPsecRUSALclAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 13),
    _TIPsecRUSALclAPrefLen_Type()
)
tIPsecRUSALclAPrefLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSALclAPrefLen.setStatus("obsolete")
_TIPsecRUSARemAddrType_Type = InetAddressType
_TIPsecRUSARemAddrType_Object = MibTableColumn
tIPsecRUSARemAddrType = _TIPsecRUSARemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 14),
    _TIPsecRUSARemAddrType_Type()
)
tIPsecRUSARemAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSARemAddrType.setStatus("obsolete")


class _TIPsecRUSARemAddr_Type(InetAddress):
    """Custom type tIPsecRUSARemAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecRUSARemAddr_Type.__name__ = "InetAddress"
_TIPsecRUSARemAddr_Object = MibTableColumn
tIPsecRUSARemAddr = _TIPsecRUSARemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 15),
    _TIPsecRUSARemAddr_Type()
)
tIPsecRUSARemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSARemAddr.setStatus("obsolete")
_TIPsecRUSARemAPrefLen_Type = InetAddressPrefixLength
_TIPsecRUSARemAPrefLen_Object = MibTableColumn
tIPsecRUSARemAPrefLen = _TIPsecRUSARemAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 16),
    _TIPsecRUSARemAPrefLen_Type()
)
tIPsecRUSARemAPrefLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSARemAPrefLen.setStatus("obsolete")
_TIPsecRUSAStatsTable_Object = MibTable
tIPsecRUSAStatsTable = _TIPsecRUSAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23)
)
if mibBuilder.loadTexts:
    tIPsecRUSAStatsTable.setStatus("current")
_TIPsecRUSAStatsEntry_Object = MibTableRow
tIPsecRUSAStatsEntry = _TIPsecRUSAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1)
)
tIPsecRUSAStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlPort"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSAId"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSADirection"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSAIndex"),
)
if mibBuilder.loadTexts:
    tIPsecRUSAStatsEntry.setStatus("current")
_TIPsecRUSAStatsBytesProcessed_Type = Counter64
_TIPsecRUSAStatsBytesProcessed_Object = MibTableColumn
tIPsecRUSAStatsBytesProcessed = _TIPsecRUSAStatsBytesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 1),
    _TIPsecRUSAStatsBytesProcessed_Type()
)
tIPsecRUSAStatsBytesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsBytesProcessed.setStatus("current")
_TIPsecRUSAStatsBytesProcLow32_Type = Counter32
_TIPsecRUSAStatsBytesProcLow32_Object = MibTableColumn
tIPsecRUSAStatsBytesProcLow32 = _TIPsecRUSAStatsBytesProcLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 2),
    _TIPsecRUSAStatsBytesProcLow32_Type()
)
tIPsecRUSAStatsBytesProcLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsBytesProcLow32.setStatus("current")
_TIPsecRUSAStatsBytesProcHigh32_Type = Counter32
_TIPsecRUSAStatsBytesProcHigh32_Object = MibTableColumn
tIPsecRUSAStatsBytesProcHigh32 = _TIPsecRUSAStatsBytesProcHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 3),
    _TIPsecRUSAStatsBytesProcHigh32_Type()
)
tIPsecRUSAStatsBytesProcHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsBytesProcHigh32.setStatus("current")
_TIPsecRUSAStatsPktsProcessed_Type = Counter64
_TIPsecRUSAStatsPktsProcessed_Object = MibTableColumn
tIPsecRUSAStatsPktsProcessed = _TIPsecRUSAStatsPktsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 4),
    _TIPsecRUSAStatsPktsProcessed_Type()
)
tIPsecRUSAStatsPktsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPktsProcessed.setStatus("current")
_TIPsecRUSAStatsPktsProcLow32_Type = Counter32
_TIPsecRUSAStatsPktsProcLow32_Object = MibTableColumn
tIPsecRUSAStatsPktsProcLow32 = _TIPsecRUSAStatsPktsProcLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 5),
    _TIPsecRUSAStatsPktsProcLow32_Type()
)
tIPsecRUSAStatsPktsProcLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPktsProcLow32.setStatus("current")
_TIPsecRUSAStatsPktsProcHigh32_Type = Counter32
_TIPsecRUSAStatsPktsProcHigh32_Object = MibTableColumn
tIPsecRUSAStatsPktsProcHigh32 = _TIPsecRUSAStatsPktsProcHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 6),
    _TIPsecRUSAStatsPktsProcHigh32_Type()
)
tIPsecRUSAStatsPktsProcHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPktsProcHigh32.setStatus("current")
_TIPsecRUSAStatsCryptoErrors_Type = Counter32
_TIPsecRUSAStatsCryptoErrors_Object = MibTableColumn
tIPsecRUSAStatsCryptoErrors = _TIPsecRUSAStatsCryptoErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 7),
    _TIPsecRUSAStatsCryptoErrors_Type()
)
tIPsecRUSAStatsCryptoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsCryptoErrors.setStatus("current")
_TIPsecRUSAStatsReplayErrors_Type = Counter32
_TIPsecRUSAStatsReplayErrors_Object = MibTableColumn
tIPsecRUSAStatsReplayErrors = _TIPsecRUSAStatsReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 8),
    _TIPsecRUSAStatsReplayErrors_Type()
)
tIPsecRUSAStatsReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsReplayErrors.setStatus("current")
_TIPsecRUSAStatsSAErrors_Type = Counter32
_TIPsecRUSAStatsSAErrors_Object = MibTableColumn
tIPsecRUSAStatsSAErrors = _TIPsecRUSAStatsSAErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 9),
    _TIPsecRUSAStatsSAErrors_Type()
)
tIPsecRUSAStatsSAErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsSAErrors.setStatus("current")
_TIPsecRUSAStatsPolicyErrors_Type = Counter32
_TIPsecRUSAStatsPolicyErrors_Object = MibTableColumn
tIPsecRUSAStatsPolicyErrors = _TIPsecRUSAStatsPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 10),
    _TIPsecRUSAStatsPolicyErrors_Type()
)
tIPsecRUSAStatsPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPolicyErrors.setStatus("current")
_TIPsecRUSAStatsEncapOverhead_Type = Counter32
_TIPsecRUSAStatsEncapOverhead_Object = MibTableColumn
tIPsecRUSAStatsEncapOverhead = _TIPsecRUSAStatsEncapOverhead_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 11),
    _TIPsecRUSAStatsEncapOverhead_Type()
)
tIPsecRUSAStatsEncapOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsEncapOverhead.setStatus("current")
_TIPsecRUSAStatsPreEncapFragCnt_Type = Counter64
_TIPsecRUSAStatsPreEncapFragCnt_Object = MibTableColumn
tIPsecRUSAStatsPreEncapFragCnt = _TIPsecRUSAStatsPreEncapFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 12),
    _TIPsecRUSAStatsPreEncapFragCnt_Type()
)
tIPsecRUSAStatsPreEncapFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPreEncapFragCnt.setStatus("current")
_TIPsecRUSAStatsPreEncapFragLtSz_Type = Unsigned32
_TIPsecRUSAStatsPreEncapFragLtSz_Object = MibTableColumn
tIPsecRUSAStatsPreEncapFragLtSz = _TIPsecRUSAStatsPreEncapFragLtSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 13),
    _TIPsecRUSAStatsPreEncapFragLtSz_Type()
)
tIPsecRUSAStatsPreEncapFragLtSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPreEncapFragLtSz.setStatus("current")
_TIPsecRUSAStatsPostEncapFragCnt_Type = Counter64
_TIPsecRUSAStatsPostEncapFragCnt_Object = MibTableColumn
tIPsecRUSAStatsPostEncapFragCnt = _TIPsecRUSAStatsPostEncapFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 14),
    _TIPsecRUSAStatsPostEncapFragCnt_Type()
)
tIPsecRUSAStatsPostEncapFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPostEncapFragCnt.setStatus("current")
_TIPsecRUSAStatsPostEncapFragLtSz_Type = Unsigned32
_TIPsecRUSAStatsPostEncapFragLtSz_Object = MibTableColumn
tIPsecRUSAStatsPostEncapFragLtSz = _TIPsecRUSAStatsPostEncapFragLtSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 15),
    _TIPsecRUSAStatsPostEncapFragLtSz_Type()
)
tIPsecRUSAStatsPostEncapFragLtSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPostEncapFragLtSz.setStatus("current")
_TIPsecRUSAStatsPfsDhGroup_Type = TmnxIkePolicyDHGroupOrZero
_TIPsecRUSAStatsPfsDhGroup_Object = MibTableColumn
tIPsecRUSAStatsPfsDhGroup = _TIPsecRUSAStatsPfsDhGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 17),
    _TIPsecRUSAStatsPfsDhGroup_Type()
)
tIPsecRUSAStatsPfsDhGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPfsDhGroup.setStatus("current")
_TIPsecRUSAStatsMulticastIfName_Type = TNamedItemOrEmpty
_TIPsecRUSAStatsMulticastIfName_Object = MibTableColumn
tIPsecRUSAStatsMulticastIfName = _TIPsecRUSAStatsMulticastIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 18),
    _TIPsecRUSAStatsMulticastIfName_Type()
)
tIPsecRUSAStatsMulticastIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsMulticastIfName.setStatus("current")
_TIPsecRUSAStatsMulticastProt_Type = TIPsecMulticastProtocol
_TIPsecRUSAStatsMulticastProt_Object = MibTableColumn
tIPsecRUSAStatsMulticastProt = _TIPsecRUSAStatsMulticastProt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 19),
    _TIPsecRUSAStatsMulticastProt_Type()
)
tIPsecRUSAStatsMulticastProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsMulticastProt.setStatus("current")
_TmnxIPsecTunnelCountObjs_ObjectIdentity = ObjectIdentity
tmnxIPsecTunnelCountObjs = _TmnxIPsecTunnelCountObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24)
)
_TmnxIPsecPskTunnels_Type = Gauge32
_TmnxIPsecPskTunnels_Object = MibScalar
tmnxIPsecPskTunnels = _TmnxIPsecPskTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 1),
    _TmnxIPsecPskTunnels_Type()
)
tmnxIPsecPskTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecPskTunnels.setStatus("current")
_TmnxIPsecGWPskTunnels_Type = Gauge32
_TmnxIPsecGWPskTunnels_Object = MibScalar
tmnxIPsecGWPskTunnels = _TmnxIPsecGWPskTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 2),
    _TmnxIPsecGWPskTunnels_Type()
)
tmnxIPsecGWPskTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWPskTunnels.setStatus("current")
_TmnxIPsecGWPskXAuthTunnels_Type = Gauge32
_TmnxIPsecGWPskXAuthTunnels_Object = MibScalar
tmnxIPsecGWPskXAuthTunnels = _TmnxIPsecGWPskXAuthTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 3),
    _TmnxIPsecGWPskXAuthTunnels_Type()
)
tmnxIPsecGWPskXAuthTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWPskXAuthTunnels.setStatus("current")
_TmnxIPsecGWCertTunnels_Type = Gauge32
_TmnxIPsecGWCertTunnels_Object = MibScalar
tmnxIPsecGWCertTunnels = _TmnxIPsecGWCertTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 4),
    _TmnxIPsecGWCertTunnels_Type()
)
tmnxIPsecGWCertTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWCertTunnels.setStatus("current")
_TmnxIPsecGWPskRadiusTunnels_Type = Gauge32
_TmnxIPsecGWPskRadiusTunnels_Object = MibScalar
tmnxIPsecGWPskRadiusTunnels = _TmnxIPsecGWPskRadiusTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 5),
    _TmnxIPsecGWPskRadiusTunnels_Type()
)
tmnxIPsecGWPskRadiusTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWPskRadiusTunnels.setStatus("current")
_TmnxIPsecGWCertRadiusTunnels_Type = Gauge32
_TmnxIPsecGWCertRadiusTunnels_Object = MibScalar
tmnxIPsecGWCertRadiusTunnels = _TmnxIPsecGWCertRadiusTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 6),
    _TmnxIPsecGWCertRadiusTunnels_Type()
)
tmnxIPsecGWCertRadiusTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWCertRadiusTunnels.setStatus("current")
_TmnxIPsecGWEapTunnels_Type = Gauge32
_TmnxIPsecGWEapTunnels_Object = MibScalar
tmnxIPsecGWEapTunnels = _TmnxIPsecGWEapTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 7),
    _TmnxIPsecGWEapTunnels_Type()
)
tmnxIPsecGWEapTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWEapTunnels.setStatus("current")
_TmnxIPsecGWAutoEapRadiusTunnels_Type = Gauge32
_TmnxIPsecGWAutoEapRadiusTunnels_Object = MibScalar
tmnxIPsecGWAutoEapRadiusTunnels = _TmnxIPsecGWAutoEapRadiusTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 8),
    _TmnxIPsecGWAutoEapRadiusTunnels_Type()
)
tmnxIPsecGWAutoEapRadiusTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWAutoEapRadiusTunnels.setStatus("current")
_TmnxIPsecGWAutoEapTunnels_Type = Gauge32
_TmnxIPsecGWAutoEapTunnels_Object = MibScalar
tmnxIPsecGWAutoEapTunnels = _TmnxIPsecGWAutoEapTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 9),
    _TmnxIPsecGWAutoEapTunnels_Type()
)
tmnxIPsecGWAutoEapTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWAutoEapTunnels.setStatus("current")
_TmnxIPsecTunnelBfdTableLastChgd_Type = TimeStamp
_TmnxIPsecTunnelBfdTableLastChgd_Object = MibScalar
tmnxIPsecTunnelBfdTableLastChgd = _TmnxIPsecTunnelBfdTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 25),
    _TmnxIPsecTunnelBfdTableLastChgd_Type()
)
tmnxIPsecTunnelBfdTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdTableLastChgd.setStatus("obsolete")
_TmnxIPsecTunnelBfdTable_Object = MibTable
tmnxIPsecTunnelBfdTable = _TmnxIPsecTunnelBfdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26)
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdTable.setStatus("obsolete")
_TmnxIPsecTunnelBfdEntry_Object = MibTableRow
tmnxIPsecTunnelBfdEntry = _TmnxIPsecTunnelBfdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1)
)
tmnxIPsecTunnelBfdEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdSvcId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdIfName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdDstAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdDstAddr"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdEntry.setStatus("current")
_TmnxIPsecTunnelBfdSvcId_Type = TmnxServId
_TmnxIPsecTunnelBfdSvcId_Object = MibTableColumn
tmnxIPsecTunnelBfdSvcId = _TmnxIPsecTunnelBfdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 1),
    _TmnxIPsecTunnelBfdSvcId_Type()
)
tmnxIPsecTunnelBfdSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdSvcId.setStatus("obsolete")
_TmnxIPsecTunnelBfdIfName_Type = TNamedItem
_TmnxIPsecTunnelBfdIfName_Object = MibTableColumn
tmnxIPsecTunnelBfdIfName = _TmnxIPsecTunnelBfdIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 2),
    _TmnxIPsecTunnelBfdIfName_Type()
)
tmnxIPsecTunnelBfdIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdIfName.setStatus("obsolete")
_TmnxIPsecTunnelBfdDstAddrType_Type = InetAddressType
_TmnxIPsecTunnelBfdDstAddrType_Object = MibTableColumn
tmnxIPsecTunnelBfdDstAddrType = _TmnxIPsecTunnelBfdDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 3),
    _TmnxIPsecTunnelBfdDstAddrType_Type()
)
tmnxIPsecTunnelBfdDstAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdDstAddrType.setStatus("obsolete")


class _TmnxIPsecTunnelBfdDstAddr_Type(InetAddress):
    """Custom type tmnxIPsecTunnelBfdDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecTunnelBfdDstAddr_Type.__name__ = "InetAddress"
_TmnxIPsecTunnelBfdDstAddr_Object = MibTableColumn
tmnxIPsecTunnelBfdDstAddr = _TmnxIPsecTunnelBfdDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 4),
    _TmnxIPsecTunnelBfdDstAddr_Type()
)
tmnxIPsecTunnelBfdDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdDstAddr.setStatus("obsolete")
_TmnxIPsecTunnelBfdRowStatus_Type = RowStatus
_TmnxIPsecTunnelBfdRowStatus_Object = MibTableColumn
tmnxIPsecTunnelBfdRowStatus = _TmnxIPsecTunnelBfdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 5),
    _TmnxIPsecTunnelBfdRowStatus_Type()
)
tmnxIPsecTunnelBfdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdRowStatus.setStatus("obsolete")
_TmnxIPsecTunnelBfdLastChanged_Type = TimeStamp
_TmnxIPsecTunnelBfdLastChanged_Object = MibTableColumn
tmnxIPsecTunnelBfdLastChanged = _TmnxIPsecTunnelBfdLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 6),
    _TmnxIPsecTunnelBfdLastChanged_Type()
)
tmnxIPsecTunnelBfdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdLastChanged.setStatus("obsolete")
_TmnxIPsecTunnelBfdSrcAddrType_Type = InetAddressType
_TmnxIPsecTunnelBfdSrcAddrType_Object = MibTableColumn
tmnxIPsecTunnelBfdSrcAddrType = _TmnxIPsecTunnelBfdSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 7),
    _TmnxIPsecTunnelBfdSrcAddrType_Type()
)
tmnxIPsecTunnelBfdSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdSrcAddrType.setStatus("obsolete")


class _TmnxIPsecTunnelBfdSrcAddr_Type(InetAddress):
    """Custom type tmnxIPsecTunnelBfdSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecTunnelBfdSrcAddr_Type.__name__ = "InetAddress"
_TmnxIPsecTunnelBfdSrcAddr_Object = MibTableColumn
tmnxIPsecTunnelBfdSrcAddr = _TmnxIPsecTunnelBfdSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 8),
    _TmnxIPsecTunnelBfdSrcAddr_Type()
)
tmnxIPsecTunnelBfdSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdSrcAddr.setStatus("obsolete")
_TmnxIPsecTunnelBfdSessOperState_Type = TmnxBfdSessOperState
_TmnxIPsecTunnelBfdSessOperState_Object = MibTableColumn
tmnxIPsecTunnelBfdSessOperState = _TmnxIPsecTunnelBfdSessOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 9),
    _TmnxIPsecTunnelBfdSessOperState_Type()
)
tmnxIPsecTunnelBfdSessOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdSessOperState.setStatus("obsolete")
_TIPsecRadAuthPlcyTblLastChgd_Type = TimeStamp
_TIPsecRadAuthPlcyTblLastChgd_Object = MibScalar
tIPsecRadAuthPlcyTblLastChgd = _TIPsecRadAuthPlcyTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 27),
    _TIPsecRadAuthPlcyTblLastChgd_Type()
)
tIPsecRadAuthPlcyTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyTblLastChgd.setStatus("current")
_TIPsecRadAuthPlcyTable_Object = MibTable
tIPsecRadAuthPlcyTable = _TIPsecRadAuthPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28)
)
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyTable.setStatus("current")
_TIPsecRadAuthPlcyEntry_Object = MibTableRow
tIPsecRadAuthPlcyEntry = _TIPsecRadAuthPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1)
)
tIPsecRadAuthPlcyEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyName"),
)
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyEntry.setStatus("current")
_TIPsecRadAuthPlcyName_Type = TNamedItem
_TIPsecRadAuthPlcyName_Object = MibTableColumn
tIPsecRadAuthPlcyName = _TIPsecRadAuthPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1, 1),
    _TIPsecRadAuthPlcyName_Type()
)
tIPsecRadAuthPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyName.setStatus("current")
_TIPsecRadAuthPlcyRowStatus_Type = RowStatus
_TIPsecRadAuthPlcyRowStatus_Object = MibTableColumn
tIPsecRadAuthPlcyRowStatus = _TIPsecRadAuthPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1, 2),
    _TIPsecRadAuthPlcyRowStatus_Type()
)
tIPsecRadAuthPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyRowStatus.setStatus("current")
_TIPsecRadAuthPlcyLastMgmtChange_Type = TimeStamp
_TIPsecRadAuthPlcyLastMgmtChange_Object = MibTableColumn
tIPsecRadAuthPlcyLastMgmtChange = _TIPsecRadAuthPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1, 3),
    _TIPsecRadAuthPlcyLastMgmtChange_Type()
)
tIPsecRadAuthPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyLastMgmtChange.setStatus("current")


class _TIPsecRadAuthPlcyInclAttr_Type(Bits):
    """Custom type tIPsecRadAuthPlcyInclAttr based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("callingStationId", 0),
          ("calledStationId", 1),
          ("nasPortId", 2),
          ("nasIdentifier", 3),
          ("nasIpAddr", 4),
          ("certSubjectKeyId", 5))
    )

_TIPsecRadAuthPlcyInclAttr_Type.__name__ = "Bits"
_TIPsecRadAuthPlcyInclAttr_Object = MibTableColumn
tIPsecRadAuthPlcyInclAttr = _TIPsecRadAuthPlcyInclAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1, 4),
    _TIPsecRadAuthPlcyInclAttr_Type()
)
tIPsecRadAuthPlcyInclAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyInclAttr.setStatus("current")


class _TIPsecRadAuthPlcyRadSrvPlcy_Type(TNamedItemOrEmpty):
    """Custom type tIPsecRadAuthPlcyRadSrvPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TIPsecRadAuthPlcyRadSrvPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecRadAuthPlcyRadSrvPlcy_Object = MibTableColumn
tIPsecRadAuthPlcyRadSrvPlcy = _TIPsecRadAuthPlcyRadSrvPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1, 5),
    _TIPsecRadAuthPlcyRadSrvPlcy_Type()
)
tIPsecRadAuthPlcyRadSrvPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyRadSrvPlcy.setStatus("current")


class _TIPsecRadAuthPlcyPassword_Type(DisplayString):
    """Custom type tIPsecRadAuthPlcyPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TIPsecRadAuthPlcyPassword_Type.__name__ = "DisplayString"
_TIPsecRadAuthPlcyPassword_Object = MibTableColumn
tIPsecRadAuthPlcyPassword = _TIPsecRadAuthPlcyPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1, 6),
    _TIPsecRadAuthPlcyPassword_Type()
)
tIPsecRadAuthPlcyPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyPassword.setStatus("current")
_TIPsecRadAcctPlcyTblLastChgd_Type = TimeStamp
_TIPsecRadAcctPlcyTblLastChgd_Object = MibScalar
tIPsecRadAcctPlcyTblLastChgd = _TIPsecRadAcctPlcyTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 29),
    _TIPsecRadAcctPlcyTblLastChgd_Type()
)
tIPsecRadAcctPlcyTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyTblLastChgd.setStatus("current")
_TIPsecRadAcctPlcyTable_Object = MibTable
tIPsecRadAcctPlcyTable = _TIPsecRadAcctPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30)
)
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyTable.setStatus("current")
_TIPsecRadAcctPlcyEntry_Object = MibTableRow
tIPsecRadAcctPlcyEntry = _TIPsecRadAcctPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1)
)
tIPsecRadAcctPlcyEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyName"),
)
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyEntry.setStatus("current")
_TIPsecRadAcctPlcyName_Type = TNamedItem
_TIPsecRadAcctPlcyName_Object = MibTableColumn
tIPsecRadAcctPlcyName = _TIPsecRadAcctPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1, 1),
    _TIPsecRadAcctPlcyName_Type()
)
tIPsecRadAcctPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyName.setStatus("current")
_TIPsecRadAcctPlcyRowStatus_Type = RowStatus
_TIPsecRadAcctPlcyRowStatus_Object = MibTableColumn
tIPsecRadAcctPlcyRowStatus = _TIPsecRadAcctPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1, 2),
    _TIPsecRadAcctPlcyRowStatus_Type()
)
tIPsecRadAcctPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyRowStatus.setStatus("current")
_TIPsecRadAcctPlcyLastMgmtChange_Type = TimeStamp
_TIPsecRadAcctPlcyLastMgmtChange_Object = MibTableColumn
tIPsecRadAcctPlcyLastMgmtChange = _TIPsecRadAcctPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1, 3),
    _TIPsecRadAcctPlcyLastMgmtChange_Type()
)
tIPsecRadAcctPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyLastMgmtChange.setStatus("current")


class _TIPsecRadAcctPlcyInclAttr_Type(Bits):
    """Custom type tIPsecRadAcctPlcyInclAttr based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("callingStationId", 0),
          ("calledStationId", 1),
          ("nasPortId", 2),
          ("nasIdentifier", 3),
          ("nasIpAddr", 4),
          ("framedIpAddr", 5),
          ("framedIpv6Prefix", 6),
          ("acctStats", 7))
    )

_TIPsecRadAcctPlcyInclAttr_Type.__name__ = "Bits"
_TIPsecRadAcctPlcyInclAttr_Object = MibTableColumn
tIPsecRadAcctPlcyInclAttr = _TIPsecRadAcctPlcyInclAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1, 4),
    _TIPsecRadAcctPlcyInclAttr_Type()
)
tIPsecRadAcctPlcyInclAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyInclAttr.setStatus("current")


class _TIPsecRadAcctPlcyRadSrvPlcy_Type(TNamedItemOrEmpty):
    """Custom type tIPsecRadAcctPlcyRadSrvPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TIPsecRadAcctPlcyRadSrvPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecRadAcctPlcyRadSrvPlcy_Object = MibTableColumn
tIPsecRadAcctPlcyRadSrvPlcy = _TIPsecRadAcctPlcyRadSrvPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1, 5),
    _TIPsecRadAcctPlcyRadSrvPlcy_Type()
)
tIPsecRadAcctPlcyRadSrvPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyRadSrvPlcy.setStatus("current")


class _TIPsecRadAcctPlcyUpdateInterval_Type(Unsigned32):
    """Custom type tIPsecRadAcctPlcyUpdateInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 259200),
    )


_TIPsecRadAcctPlcyUpdateInterval_Type.__name__ = "Unsigned32"
_TIPsecRadAcctPlcyUpdateInterval_Object = MibTableColumn
tIPsecRadAcctPlcyUpdateInterval = _TIPsecRadAcctPlcyUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1, 6),
    _TIPsecRadAcctPlcyUpdateInterval_Type()
)
tIPsecRadAcctPlcyUpdateInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyUpdateInterval.setUnits("minutes")


class _TIPsecRadAcctPlcyJitter_Type(Integer32):
    """Custom type tIPsecRadAcctPlcyJitter based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 3600),
    )


_TIPsecRadAcctPlcyJitter_Type.__name__ = "Integer32"
_TIPsecRadAcctPlcyJitter_Object = MibTableColumn
tIPsecRadAcctPlcyJitter = _TIPsecRadAcctPlcyJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1, 7),
    _TIPsecRadAcctPlcyJitter_Type()
)
tIPsecRadAcctPlcyJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyJitter.setStatus("current")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyJitter.setUnits("seconds")
_TmnxIPsecTnlDstAddrTblLastChngd_Type = TimeStamp
_TmnxIPsecTnlDstAddrTblLastChngd_Object = MibScalar
tmnxIPsecTnlDstAddrTblLastChngd = _TmnxIPsecTnlDstAddrTblLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 31),
    _TmnxIPsecTnlDstAddrTblLastChngd_Type()
)
tmnxIPsecTnlDstAddrTblLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrTblLastChngd.setStatus("current")
_TmnxIPsecTnlDstAddrTable_Object = MibTable
tmnxIPsecTnlDstAddrTable = _TmnxIPsecTnlDstAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32)
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrTable.setStatus("current")
_TmnxIPsecTnlDstAddrEntry_Object = MibTableRow
tmnxIPsecTnlDstAddrEntry = _TmnxIPsecTnlDstAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32, 1)
)
tmnxIPsecTnlDstAddrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstAddr"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrEntry.setStatus("current")
_TmnxIPsecTnlDstAddrType_Type = InetAddressType
_TmnxIPsecTnlDstAddrType_Object = MibTableColumn
tmnxIPsecTnlDstAddrType = _TmnxIPsecTnlDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32, 1, 1),
    _TmnxIPsecTnlDstAddrType_Type()
)
tmnxIPsecTnlDstAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrType.setStatus("current")


class _TmnxIPsecTnlDstAddr_Type(InetAddress):
    """Custom type tmnxIPsecTnlDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecTnlDstAddr_Type.__name__ = "InetAddress"
_TmnxIPsecTnlDstAddr_Object = MibTableColumn
tmnxIPsecTnlDstAddr = _TmnxIPsecTnlDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32, 1, 2),
    _TmnxIPsecTnlDstAddr_Type()
)
tmnxIPsecTnlDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddr.setStatus("current")
_TmnxIPsecTnlDstAddrRowStatus_Type = RowStatus
_TmnxIPsecTnlDstAddrRowStatus_Object = MibTableColumn
tmnxIPsecTnlDstAddrRowStatus = _TmnxIPsecTnlDstAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32, 1, 3),
    _TmnxIPsecTnlDstAddrRowStatus_Type()
)
tmnxIPsecTnlDstAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrRowStatus.setStatus("current")
_TmnxIPsecTnlDstAddrLastChanged_Type = TimeStamp
_TmnxIPsecTnlDstAddrLastChanged_Object = MibTableColumn
tmnxIPsecTnlDstAddrLastChanged = _TmnxIPsecTnlDstAddrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32, 1, 4),
    _TmnxIPsecTnlDstAddrLastChanged_Type()
)
tmnxIPsecTnlDstAddrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrLastChanged.setStatus("current")
_TmnxIPsecTnlDstAddrResolved_Type = TruthValue
_TmnxIPsecTnlDstAddrResolved_Object = MibTableColumn
tmnxIPsecTnlDstAddrResolved = _TmnxIPsecTnlDstAddrResolved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32, 1, 5),
    _TmnxIPsecTnlDstAddrResolved_Type()
)
tmnxIPsecTnlDstAddrResolved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrResolved.setStatus("current")
_TIPsecCertProfileTblLastChgd_Type = TimeStamp
_TIPsecCertProfileTblLastChgd_Object = MibScalar
tIPsecCertProfileTblLastChgd = _TIPsecCertProfileTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 33),
    _TIPsecCertProfileTblLastChgd_Type()
)
tIPsecCertProfileTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfileTblLastChgd.setStatus("current")
_TIPsecCertProfileTable_Object = MibTable
tIPsecCertProfileTable = _TIPsecCertProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34)
)
if mibBuilder.loadTexts:
    tIPsecCertProfileTable.setStatus("current")
_TIPsecCertProfileEntry_Object = MibTableRow
tIPsecCertProfileEntry = _TIPsecCertProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1)
)
tIPsecCertProfileEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfileName"),
)
if mibBuilder.loadTexts:
    tIPsecCertProfileEntry.setStatus("current")
_TIPsecCertProfileName_Type = TNamedItem
_TIPsecCertProfileName_Object = MibTableColumn
tIPsecCertProfileName = _TIPsecCertProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1, 1),
    _TIPsecCertProfileName_Type()
)
tIPsecCertProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecCertProfileName.setStatus("current")
_TIPsecCertProfileRowStatus_Type = RowStatus
_TIPsecCertProfileRowStatus_Object = MibTableColumn
tIPsecCertProfileRowStatus = _TIPsecCertProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1, 2),
    _TIPsecCertProfileRowStatus_Type()
)
tIPsecCertProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertProfileRowStatus.setStatus("current")
_TIPsecCertProfileLastChgd_Type = TimeStamp
_TIPsecCertProfileLastChgd_Object = MibTableColumn
tIPsecCertProfileLastChgd = _TIPsecCertProfileLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1, 3),
    _TIPsecCertProfileLastChgd_Type()
)
tIPsecCertProfileLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfileLastChgd.setStatus("current")


class _TIPsecCertProfileAdminState_Type(TmnxAdminState):
    """Custom type tIPsecCertProfileAdminState based on TmnxAdminState"""
    defaultValue = 3


_TIPsecCertProfileAdminState_Type.__name__ = "TmnxAdminState"
_TIPsecCertProfileAdminState_Object = MibTableColumn
tIPsecCertProfileAdminState = _TIPsecCertProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1, 4),
    _TIPsecCertProfileAdminState_Type()
)
tIPsecCertProfileAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertProfileAdminState.setStatus("current")
_TIPsecCertProfileOperState_Type = TmnxOperState
_TIPsecCertProfileOperState_Object = MibTableColumn
tIPsecCertProfileOperState = _TIPsecCertProfileOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1, 5),
    _TIPsecCertProfileOperState_Type()
)
tIPsecCertProfileOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfileOperState.setStatus("current")


class _TIPsecCertProfileOperFlags_Type(Bits):
    """Custom type tIPsecCertProfileOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("profileAdminDown", 0),
          ("invalidCertFile", 1),
          ("invalidKeyFile", 2),
          ("invalidCertKeyCombo", 3),
          ("caProfileOperDown", 4),
          ("invalidCAProfEntry", 5))
    )

_TIPsecCertProfileOperFlags_Type.__name__ = "Bits"
_TIPsecCertProfileOperFlags_Object = MibTableColumn
tIPsecCertProfileOperFlags = _TIPsecCertProfileOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1, 6),
    _TIPsecCertProfileOperFlags_Type()
)
tIPsecCertProfileOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfileOperFlags.setStatus("current")
_TIPsecCertProfEntryIdTblLastChgd_Type = TimeStamp
_TIPsecCertProfEntryIdTblLastChgd_Object = MibScalar
tIPsecCertProfEntryIdTblLastChgd = _TIPsecCertProfEntryIdTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 35),
    _TIPsecCertProfEntryIdTblLastChgd_Type()
)
tIPsecCertProfEntryIdTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdTblLastChgd.setStatus("current")
_TIPsecCertProfEntryIdTable_Object = MibTable
tIPsecCertProfEntryIdTable = _TIPsecCertProfEntryIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36)
)
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdTable.setStatus("current")
_TIPsecCertProfEntryIdEntry_Object = MibTableRow
tIPsecCertProfEntryIdEntry = _TIPsecCertProfEntryIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1)
)
tIPsecCertProfEntryIdEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfileName"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryId"),
)
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdEntry.setStatus("current")


class _TIPsecCertProfEntryId_Type(Integer32):
    """Custom type tIPsecCertProfEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TIPsecCertProfEntryId_Type.__name__ = "Integer32"
_TIPsecCertProfEntryId_Object = MibTableColumn
tIPsecCertProfEntryId = _TIPsecCertProfEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 1),
    _TIPsecCertProfEntryId_Type()
)
tIPsecCertProfEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryId.setStatus("current")
_TIPsecCertProfEntryIdRowStatus_Type = RowStatus
_TIPsecCertProfEntryIdRowStatus_Object = MibTableColumn
tIPsecCertProfEntryIdRowStatus = _TIPsecCertProfEntryIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 2),
    _TIPsecCertProfEntryIdRowStatus_Type()
)
tIPsecCertProfEntryIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdRowStatus.setStatus("current")
_TIPsecCertProfEntryIdLastChgd_Type = TimeStamp
_TIPsecCertProfEntryIdLastChgd_Object = MibTableColumn
tIPsecCertProfEntryIdLastChgd = _TIPsecCertProfEntryIdLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 3),
    _TIPsecCertProfEntryIdLastChgd_Type()
)
tIPsecCertProfEntryIdLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdLastChgd.setStatus("current")


class _TIPsecCertProfEntryIdCertFile_Type(DisplayString):
    """Custom type tIPsecCertProfEntryIdCertFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_TIPsecCertProfEntryIdCertFile_Type.__name__ = "DisplayString"
_TIPsecCertProfEntryIdCertFile_Object = MibTableColumn
tIPsecCertProfEntryIdCertFile = _TIPsecCertProfEntryIdCertFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 4),
    _TIPsecCertProfEntryIdCertFile_Type()
)
tIPsecCertProfEntryIdCertFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdCertFile.setStatus("current")


class _TIPsecCertProfEntryIdKeyFile_Type(DisplayString):
    """Custom type tIPsecCertProfEntryIdKeyFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_TIPsecCertProfEntryIdKeyFile_Type.__name__ = "DisplayString"
_TIPsecCertProfEntryIdKeyFile_Object = MibTableColumn
tIPsecCertProfEntryIdKeyFile = _TIPsecCertProfEntryIdKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 5),
    _TIPsecCertProfEntryIdKeyFile_Type()
)
tIPsecCertProfEntryIdKeyFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdKeyFile.setStatus("current")


class _TIPsecCertProfEntryIdCompChain_Type(Integer32):
    """Custom type tIPsecCertProfEntryIdCompChain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("partial", 1),
          ("complete", 2))
    )


_TIPsecCertProfEntryIdCompChain_Type.__name__ = "Integer32"
_TIPsecCertProfEntryIdCompChain_Object = MibTableColumn
tIPsecCertProfEntryIdCompChain = _TIPsecCertProfEntryIdCompChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 6),
    _TIPsecCertProfEntryIdCompChain_Type()
)
tIPsecCertProfEntryIdCompChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdCompChain.setStatus("current")


class _TIPsecCertProfEntryIdOperFlags_Type(Bits):
    """Custom type tIPsecCertProfEntryIdOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("profileAdminDown", 0),
          ("invalidCertFile", 1),
          ("invalidKeyFile", 2),
          ("invalidCertKeyCombo", 3),
          ("caProfileOperDown", 4),
          ("invalidCAProfEntry", 5))
    )

_TIPsecCertProfEntryIdOperFlags_Type.__name__ = "Bits"
_TIPsecCertProfEntryIdOperFlags_Object = MibTableColumn
tIPsecCertProfEntryIdOperFlags = _TIPsecCertProfEntryIdOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 7),
    _TIPsecCertProfEntryIdOperFlags_Type()
)
tIPsecCertProfEntryIdOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdOperFlags.setStatus("current")


class _TIPsecCertProfEntryIdRsaSign_Type(Integer32):
    """Custom type tIPsecCertProfEntryIdRsaSign based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pkcs1", 1),
          ("pss", 2))
    )


_TIPsecCertProfEntryIdRsaSign_Type.__name__ = "Integer32"
_TIPsecCertProfEntryIdRsaSign_Object = MibTableColumn
tIPsecCertProfEntryIdRsaSign = _TIPsecCertProfEntryIdRsaSign_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 8),
    _TIPsecCertProfEntryIdRsaSign_Type()
)
tIPsecCertProfEntryIdRsaSign.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdRsaSign.setStatus("current")
_TIPsecCompChainCAProfTable_Object = MibTable
tIPsecCompChainCAProfTable = _TIPsecCompChainCAProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 37)
)
if mibBuilder.loadTexts:
    tIPsecCompChainCAProfTable.setStatus("current")
_TIPsecCompChainCAProfEntry_Object = MibTableRow
tIPsecCompChainCAProfEntry = _TIPsecCompChainCAProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 37, 1)
)
tIPsecCompChainCAProfEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfileName"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryId"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCompChainCAProfOrder"),
)
if mibBuilder.loadTexts:
    tIPsecCompChainCAProfEntry.setStatus("current")
_TIPsecCompChainCAProfOrder_Type = Integer32
_TIPsecCompChainCAProfOrder_Object = MibTableColumn
tIPsecCompChainCAProfOrder = _TIPsecCompChainCAProfOrder_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 37, 1, 1),
    _TIPsecCompChainCAProfOrder_Type()
)
tIPsecCompChainCAProfOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecCompChainCAProfOrder.setStatus("current")
_TIPsecCompChainCAProfName_Type = TNamedItem
_TIPsecCompChainCAProfName_Object = MibTableColumn
tIPsecCompChainCAProfName = _TIPsecCompChainCAProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 37, 1, 2),
    _TIPsecCompChainCAProfName_Type()
)
tIPsecCompChainCAProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCompChainCAProfName.setStatus("current")
_TIPsecCertChainCAProfTblLastChgd_Type = TimeStamp
_TIPsecCertChainCAProfTblLastChgd_Object = MibScalar
tIPsecCertChainCAProfTblLastChgd = _TIPsecCertChainCAProfTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 41),
    _TIPsecCertChainCAProfTblLastChgd_Type()
)
tIPsecCertChainCAProfTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertChainCAProfTblLastChgd.setStatus("current")
_TIPsecCertChainCAProfTable_Object = MibTable
tIPsecCertChainCAProfTable = _TIPsecCertChainCAProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 42)
)
if mibBuilder.loadTexts:
    tIPsecCertChainCAProfTable.setStatus("current")
_TIPsecCertChainCAProfEntry_Object = MibTableRow
tIPsecCertChainCAProfEntry = _TIPsecCertChainCAProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 42, 1)
)
tIPsecCertChainCAProfEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfileName"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryId"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertChainCAProfName"),
)
if mibBuilder.loadTexts:
    tIPsecCertChainCAProfEntry.setStatus("current")
_TIPsecCertChainCAProfName_Type = TNamedItem
_TIPsecCertChainCAProfName_Object = MibTableColumn
tIPsecCertChainCAProfName = _TIPsecCertChainCAProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 42, 1, 1),
    _TIPsecCertChainCAProfName_Type()
)
tIPsecCertChainCAProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecCertChainCAProfName.setStatus("current")
_TIPsecCertChainCAProfRowStatus_Type = RowStatus
_TIPsecCertChainCAProfRowStatus_Object = MibTableColumn
tIPsecCertChainCAProfRowStatus = _TIPsecCertChainCAProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 42, 1, 2),
    _TIPsecCertChainCAProfRowStatus_Type()
)
tIPsecCertChainCAProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertChainCAProfRowStatus.setStatus("current")
_TIPsecCertChainCAProfLastChgd_Type = TimeStamp
_TIPsecCertChainCAProfLastChgd_Object = MibTableColumn
tIPsecCertChainCAProfLastChgd = _TIPsecCertChainCAProfLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 42, 1, 3),
    _TIPsecCertChainCAProfLastChgd_Type()
)
tIPsecCertChainCAProfLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertChainCAProfLastChgd.setStatus("current")
_TIPsecTsListTblLastChgd_Type = TimeStamp
_TIPsecTsListTblLastChgd_Object = MibScalar
tIPsecTsListTblLastChgd = _TIPsecTsListTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 43),
    _TIPsecTsListTblLastChgd_Type()
)
tIPsecTsListTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTsListTblLastChgd.setStatus("current")
_TIPsecTsListTable_Object = MibTable
tIPsecTsListTable = _TIPsecTsListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 44)
)
if mibBuilder.loadTexts:
    tIPsecTsListTable.setStatus("current")
_TIPsecTsListEntry_Object = MibTableRow
tIPsecTsListEntry = _TIPsecTsListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 44, 1)
)
tIPsecTsListEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTsListName"),
)
if mibBuilder.loadTexts:
    tIPsecTsListEntry.setStatus("current")
_TIPsecTsListName_Type = TNamedItem
_TIPsecTsListName_Object = MibTableColumn
tIPsecTsListName = _TIPsecTsListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 44, 1, 1),
    _TIPsecTsListName_Type()
)
tIPsecTsListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecTsListName.setStatus("current")
_TIPsecTsListRowStatus_Type = RowStatus
_TIPsecTsListRowStatus_Object = MibTableColumn
tIPsecTsListRowStatus = _TIPsecTsListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 44, 1, 2),
    _TIPsecTsListRowStatus_Type()
)
tIPsecTsListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRowStatus.setStatus("current")
_TIPsecTsListLastChgd_Type = TimeStamp
_TIPsecTsListLastChgd_Object = MibTableColumn
tIPsecTsListLastChgd = _TIPsecTsListLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 44, 1, 3),
    _TIPsecTsListLastChgd_Type()
)
tIPsecTsListLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTsListLastChgd.setStatus("current")
_TIPsecTsListLclEntryTblLastChgd_Type = TimeStamp
_TIPsecTsListLclEntryTblLastChgd_Object = MibScalar
tIPsecTsListLclEntryTblLastChgd = _TIPsecTsListLclEntryTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 45),
    _TIPsecTsListLclEntryTblLastChgd_Type()
)
tIPsecTsListLclEntryTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryTblLastChgd.setStatus("current")
_TIPsecTsListLclEntryTable_Object = MibTable
tIPsecTsListLclEntryTable = _TIPsecTsListLclEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46)
)
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryTable.setStatus("current")
_TIPsecTsListLclEntryEntry_Object = MibTableRow
tIPsecTsListLclEntryEntry = _TIPsecTsListLclEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1)
)
tIPsecTsListLclEntryEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTsListName"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryId"),
)
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryEntry.setStatus("current")


class _TIPsecTsListLclEntryId_Type(Integer32):
    """Custom type tIPsecTsListLclEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TIPsecTsListLclEntryId_Type.__name__ = "Integer32"
_TIPsecTsListLclEntryId_Object = MibTableColumn
tIPsecTsListLclEntryId = _TIPsecTsListLclEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 1),
    _TIPsecTsListLclEntryId_Type()
)
tIPsecTsListLclEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryId.setStatus("current")
_TIPsecTsListLclEntryRowStatus_Type = RowStatus
_TIPsecTsListLclEntryRowStatus_Object = MibTableColumn
tIPsecTsListLclEntryRowStatus = _TIPsecTsListLclEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 2),
    _TIPsecTsListLclEntryRowStatus_Type()
)
tIPsecTsListLclEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryRowStatus.setStatus("current")
_TIPsecTsListLclEntryLastChgd_Type = TimeStamp
_TIPsecTsListLclEntryLastChgd_Object = MibTableColumn
tIPsecTsListLclEntryLastChgd = _TIPsecTsListLclEntryLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 3),
    _TIPsecTsListLclEntryLastChgd_Type()
)
tIPsecTsListLclEntryLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryLastChgd.setStatus("current")


class _TIPsecTsListLclEntryFrAddrType_Type(InetAddressType):
    """Custom type tIPsecTsListLclEntryFrAddrType based on InetAddressType"""
    defaultValue = 0


_TIPsecTsListLclEntryFrAddrType_Type.__name__ = "InetAddressType"
_TIPsecTsListLclEntryFrAddrType_Object = MibTableColumn
tIPsecTsListLclEntryFrAddrType = _TIPsecTsListLclEntryFrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 5),
    _TIPsecTsListLclEntryFrAddrType_Type()
)
tIPsecTsListLclEntryFrAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryFrAddrType.setStatus("current")


class _TIPsecTsListLclEntryFrAddr_Type(InetAddress):
    """Custom type tIPsecTsListLclEntryFrAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecTsListLclEntryFrAddr_Type.__name__ = "InetAddress"
_TIPsecTsListLclEntryFrAddr_Object = MibTableColumn
tIPsecTsListLclEntryFrAddr = _TIPsecTsListLclEntryFrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 6),
    _TIPsecTsListLclEntryFrAddr_Type()
)
tIPsecTsListLclEntryFrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryFrAddr.setStatus("current")


class _TIPsecTsListLclEntryToAddrType_Type(InetAddressType):
    """Custom type tIPsecTsListLclEntryToAddrType based on InetAddressType"""
    defaultValue = 0


_TIPsecTsListLclEntryToAddrType_Type.__name__ = "InetAddressType"
_TIPsecTsListLclEntryToAddrType_Object = MibTableColumn
tIPsecTsListLclEntryToAddrType = _TIPsecTsListLclEntryToAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 7),
    _TIPsecTsListLclEntryToAddrType_Type()
)
tIPsecTsListLclEntryToAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryToAddrType.setStatus("current")


class _TIPsecTsListLclEntryToAddr_Type(InetAddress):
    """Custom type tIPsecTsListLclEntryToAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecTsListLclEntryToAddr_Type.__name__ = "InetAddress"
_TIPsecTsListLclEntryToAddr_Object = MibTableColumn
tIPsecTsListLclEntryToAddr = _TIPsecTsListLclEntryToAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 8),
    _TIPsecTsListLclEntryToAddr_Type()
)
tIPsecTsListLclEntryToAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryToAddr.setStatus("current")


class _TIPsecTsListLclEntryPfxAddrType_Type(InetAddressType):
    """Custom type tIPsecTsListLclEntryPfxAddrType based on InetAddressType"""
    defaultValue = 0


_TIPsecTsListLclEntryPfxAddrType_Type.__name__ = "InetAddressType"
_TIPsecTsListLclEntryPfxAddrType_Object = MibTableColumn
tIPsecTsListLclEntryPfxAddrType = _TIPsecTsListLclEntryPfxAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 9),
    _TIPsecTsListLclEntryPfxAddrType_Type()
)
tIPsecTsListLclEntryPfxAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryPfxAddrType.setStatus("current")


class _TIPsecTsListLclEntryPfxAddr_Type(InetAddress):
    """Custom type tIPsecTsListLclEntryPfxAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecTsListLclEntryPfxAddr_Type.__name__ = "InetAddress"
_TIPsecTsListLclEntryPfxAddr_Object = MibTableColumn
tIPsecTsListLclEntryPfxAddr = _TIPsecTsListLclEntryPfxAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 10),
    _TIPsecTsListLclEntryPfxAddr_Type()
)
tIPsecTsListLclEntryPfxAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryPfxAddr.setStatus("current")


class _TIPsecTsListLclEntryPfxLen_Type(InetAddressPrefixLength):
    """Custom type tIPsecTsListLclEntryPfxLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TIPsecTsListLclEntryPfxLen_Type.__name__ = "InetAddressPrefixLength"
_TIPsecTsListLclEntryPfxLen_Object = MibTableColumn
tIPsecTsListLclEntryPfxLen = _TIPsecTsListLclEntryPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 11),
    _TIPsecTsListLclEntryPfxLen_Type()
)
tIPsecTsListLclEntryPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryPfxLen.setStatus("current")


class _TIPsecTsListLclEntryMinPort_Type(InetPortNumber):
    """Custom type tIPsecTsListLclEntryMinPort based on InetPortNumber"""
    defaultValue = 0


_TIPsecTsListLclEntryMinPort_Type.__name__ = "InetPortNumber"
_TIPsecTsListLclEntryMinPort_Object = MibTableColumn
tIPsecTsListLclEntryMinPort = _TIPsecTsListLclEntryMinPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 12),
    _TIPsecTsListLclEntryMinPort_Type()
)
tIPsecTsListLclEntryMinPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryMinPort.setStatus("current")


class _TIPsecTsListLclEntryMaxPort_Type(InetPortNumber):
    """Custom type tIPsecTsListLclEntryMaxPort based on InetPortNumber"""
    defaultValue = 65535


_TIPsecTsListLclEntryMaxPort_Type.__name__ = "InetPortNumber"
_TIPsecTsListLclEntryMaxPort_Object = MibTableColumn
tIPsecTsListLclEntryMaxPort = _TIPsecTsListLclEntryMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 13),
    _TIPsecTsListLclEntryMaxPort_Type()
)
tIPsecTsListLclEntryMaxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryMaxPort.setStatus("current")


class _TIPsecTsListLclEntryMinMhType_Type(Unsigned32):
    """Custom type tIPsecTsListLclEntryMinMhType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TIPsecTsListLclEntryMinMhType_Type.__name__ = "Unsigned32"
_TIPsecTsListLclEntryMinMhType_Object = MibTableColumn
tIPsecTsListLclEntryMinMhType = _TIPsecTsListLclEntryMinMhType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 14),
    _TIPsecTsListLclEntryMinMhType_Type()
)
tIPsecTsListLclEntryMinMhType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryMinMhType.setStatus("current")


class _TIPsecTsListLclEntryMaxMhType_Type(Unsigned32):
    """Custom type tIPsecTsListLclEntryMaxMhType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TIPsecTsListLclEntryMaxMhType_Type.__name__ = "Unsigned32"
_TIPsecTsListLclEntryMaxMhType_Object = MibTableColumn
tIPsecTsListLclEntryMaxMhType = _TIPsecTsListLclEntryMaxMhType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 15),
    _TIPsecTsListLclEntryMaxMhType_Type()
)
tIPsecTsListLclEntryMaxMhType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryMaxMhType.setStatus("current")


class _TIPsecTsListLclEntryMinIcmpType_Type(Unsigned32):
    """Custom type tIPsecTsListLclEntryMinIcmpType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TIPsecTsListLclEntryMinIcmpType_Type.__name__ = "Unsigned32"
_TIPsecTsListLclEntryMinIcmpType_Object = MibTableColumn
tIPsecTsListLclEntryMinIcmpType = _TIPsecTsListLclEntryMinIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 16),
    _TIPsecTsListLclEntryMinIcmpType_Type()
)
tIPsecTsListLclEntryMinIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryMinIcmpType.setStatus("current")


class _TIPsecTsListLclEntryMaxIcmpType_Type(Unsigned32):
    """Custom type tIPsecTsListLclEntryMaxIcmpType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TIPsecTsListLclEntryMaxIcmpType_Type.__name__ = "Unsigned32"
_TIPsecTsListLclEntryMaxIcmpType_Object = MibTableColumn
tIPsecTsListLclEntryMaxIcmpType = _TIPsecTsListLclEntryMaxIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 17),
    _TIPsecTsListLclEntryMaxIcmpType_Type()
)
tIPsecTsListLclEntryMaxIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryMaxIcmpType.setStatus("current")


class _TIPsecTsListLclEntryMinIcmpCode_Type(Unsigned32):
    """Custom type tIPsecTsListLclEntryMinIcmpCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TIPsecTsListLclEntryMinIcmpCode_Type.__name__ = "Unsigned32"
_TIPsecTsListLclEntryMinIcmpCode_Object = MibTableColumn
tIPsecTsListLclEntryMinIcmpCode = _TIPsecTsListLclEntryMinIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 18),
    _TIPsecTsListLclEntryMinIcmpCode_Type()
)
tIPsecTsListLclEntryMinIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryMinIcmpCode.setStatus("current")


class _TIPsecTsListLclEntryMaxIcmpCode_Type(Unsigned32):
    """Custom type tIPsecTsListLclEntryMaxIcmpCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TIPsecTsListLclEntryMaxIcmpCode_Type.__name__ = "Unsigned32"
_TIPsecTsListLclEntryMaxIcmpCode_Object = MibTableColumn
tIPsecTsListLclEntryMaxIcmpCode = _TIPsecTsListLclEntryMaxIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 19),
    _TIPsecTsListLclEntryMaxIcmpCode_Type()
)
tIPsecTsListLclEntryMaxIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryMaxIcmpCode.setStatus("current")


class _TIPsecTsListLclEntryProtocolId_Type(Integer32):
    """Custom type tIPsecTsListLclEntryProtocolId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TIPsecTsListLclEntryProtocolId_Type.__name__ = "Integer32"
_TIPsecTsListLclEntryProtocolId_Object = MibTableColumn
tIPsecTsListLclEntryProtocolId = _TIPsecTsListLclEntryProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 20),
    _TIPsecTsListLclEntryProtocolId_Type()
)
tIPsecTsListLclEntryProtocolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryProtocolId.setStatus("current")
_TIPsecGWTsNegSelPlcyTblLastChgd_Type = TimeStamp
_TIPsecGWTsNegSelPlcyTblLastChgd_Object = MibScalar
tIPsecGWTsNegSelPlcyTblLastChgd = _TIPsecGWTsNegSelPlcyTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 47),
    _TIPsecGWTsNegSelPlcyTblLastChgd_Type()
)
tIPsecGWTsNegSelPlcyTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyTblLastChgd.setStatus("current")
_TIPsecGWTsNegSelPlcyTable_Object = MibTable
tIPsecGWTsNegSelPlcyTable = _TIPsecGWTsNegSelPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 48)
)
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyTable.setStatus("current")
_TIPsecGWTsNegSelPlcyEntry_Object = MibTableRow
tIPsecGWTsNegSelPlcyEntry = _TIPsecGWTsNegSelPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 48, 1)
)
tIPsecGWTsNegSelPlcyEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecGWTsNegSelPlcyName"),
)
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyEntry.setStatus("current")
_TIPsecGWTsNegSelPlcyName_Type = TNamedItemOrEmpty
_TIPsecGWTsNegSelPlcyName_Object = MibTableColumn
tIPsecGWTsNegSelPlcyName = _TIPsecGWTsNegSelPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 48, 1, 1),
    _TIPsecGWTsNegSelPlcyName_Type()
)
tIPsecGWTsNegSelPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyName.setStatus("current")
_TIPsecGWTsNegSelPlcyRowStatus_Type = RowStatus
_TIPsecGWTsNegSelPlcyRowStatus_Object = MibTableColumn
tIPsecGWTsNegSelPlcyRowStatus = _TIPsecGWTsNegSelPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 48, 1, 2),
    _TIPsecGWTsNegSelPlcyRowStatus_Type()
)
tIPsecGWTsNegSelPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyRowStatus.setStatus("current")
_TIPsecGWTsNegSelPlcyLastChgd_Type = TimeStamp
_TIPsecGWTsNegSelPlcyLastChgd_Object = MibTableColumn
tIPsecGWTsNegSelPlcyLastChgd = _TIPsecGWTsNegSelPlcyLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 48, 1, 3),
    _TIPsecGWTsNegSelPlcyLastChgd_Type()
)
tIPsecGWTsNegSelPlcyLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyLastChgd.setStatus("current")


class _TIPsecGWTsNegSelPlcyTsList_Type(TNamedItemOrEmpty):
    """Custom type tIPsecGWTsNegSelPlcyTsList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPsecGWTsNegSelPlcyTsList_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecGWTsNegSelPlcyTsList_Object = MibTableColumn
tIPsecGWTsNegSelPlcyTsList = _TIPsecGWTsNegSelPlcyTsList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 48, 1, 4),
    _TIPsecGWTsNegSelPlcyTsList_Type()
)
tIPsecGWTsNegSelPlcyTsList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyTsList.setStatus("current")
_TIPsecTrustAnchorProfTblLastChgd_Type = TimeStamp
_TIPsecTrustAnchorProfTblLastChgd_Object = MibScalar
tIPsecTrustAnchorProfTblLastChgd = _TIPsecTrustAnchorProfTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 49),
    _TIPsecTrustAnchorProfTblLastChgd_Type()
)
tIPsecTrustAnchorProfTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorProfTblLastChgd.setStatus("current")
_TIPsecTrustAnchorProfTable_Object = MibTable
tIPsecTrustAnchorProfTable = _TIPsecTrustAnchorProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 50)
)
if mibBuilder.loadTexts:
    tIPsecTrustAnchorProfTable.setStatus("current")
_TIPsecTrustAnchorProfEntry_Object = MibTableRow
tIPsecTrustAnchorProfEntry = _TIPsecTrustAnchorProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 50, 1)
)
tIPsecTrustAnchorProfEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorProfName"),
)
if mibBuilder.loadTexts:
    tIPsecTrustAnchorProfEntry.setStatus("current")
_TIPsecTrustAnchorProfName_Type = TNamedItem
_TIPsecTrustAnchorProfName_Object = MibTableColumn
tIPsecTrustAnchorProfName = _TIPsecTrustAnchorProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 50, 1, 1),
    _TIPsecTrustAnchorProfName_Type()
)
tIPsecTrustAnchorProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorProfName.setStatus("current")
_TIPsecTrustAnchorProfRowStatus_Type = RowStatus
_TIPsecTrustAnchorProfRowStatus_Object = MibTableColumn
tIPsecTrustAnchorProfRowStatus = _TIPsecTrustAnchorProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 50, 1, 2),
    _TIPsecTrustAnchorProfRowStatus_Type()
)
tIPsecTrustAnchorProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorProfRowStatus.setStatus("current")
_TIPsecTrustAnchorProfLastChgd_Type = TimeStamp
_TIPsecTrustAnchorProfLastChgd_Object = MibTableColumn
tIPsecTrustAnchorProfLastChgd = _TIPsecTrustAnchorProfLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 50, 1, 3),
    _TIPsecTrustAnchorProfLastChgd_Type()
)
tIPsecTrustAnchorProfLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorProfLastChgd.setStatus("current")
_TIPsecTrustAnchorCAProfDown_Type = Integer32
_TIPsecTrustAnchorCAProfDown_Object = MibTableColumn
tIPsecTrustAnchorCAProfDown = _TIPsecTrustAnchorCAProfDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 50, 1, 4),
    _TIPsecTrustAnchorCAProfDown_Type()
)
tIPsecTrustAnchorCAProfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorCAProfDown.setStatus("current")
_TIPsecTrustAnchorsTblLastChgd_Type = TimeStamp
_TIPsecTrustAnchorsTblLastChgd_Object = MibScalar
tIPsecTrustAnchorsTblLastChgd = _TIPsecTrustAnchorsTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 51),
    _TIPsecTrustAnchorsTblLastChgd_Type()
)
tIPsecTrustAnchorsTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorsTblLastChgd.setStatus("current")
_TIPsecTrustAnchorsTable_Object = MibTable
tIPsecTrustAnchorsTable = _TIPsecTrustAnchorsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 52)
)
if mibBuilder.loadTexts:
    tIPsecTrustAnchorsTable.setStatus("current")
_TIPsecTrustAnchorsEntry_Object = MibTableRow
tIPsecTrustAnchorsEntry = _TIPsecTrustAnchorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 52, 1)
)
tIPsecTrustAnchorsEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorProfName"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorsCAProfile"),
)
if mibBuilder.loadTexts:
    tIPsecTrustAnchorsEntry.setStatus("current")
_TIPsecTrustAnchorsCAProfile_Type = TNamedItem
_TIPsecTrustAnchorsCAProfile_Object = MibTableColumn
tIPsecTrustAnchorsCAProfile = _TIPsecTrustAnchorsCAProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 52, 1, 1),
    _TIPsecTrustAnchorsCAProfile_Type()
)
tIPsecTrustAnchorsCAProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorsCAProfile.setStatus("current")
_TIPsecTrustAnchorsRowStatus_Type = RowStatus
_TIPsecTrustAnchorsRowStatus_Object = MibTableColumn
tIPsecTrustAnchorsRowStatus = _TIPsecTrustAnchorsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 52, 1, 2),
    _TIPsecTrustAnchorsRowStatus_Type()
)
tIPsecTrustAnchorsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorsRowStatus.setStatus("current")
_TIPsecTrustAnchorsLastChgd_Type = TimeStamp
_TIPsecTrustAnchorsLastChgd_Object = MibTableColumn
tIPsecTrustAnchorsLastChgd = _TIPsecTrustAnchorsLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 52, 1, 3),
    _TIPsecTrustAnchorsLastChgd_Type()
)
tIPsecTrustAnchorsLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorsLastChgd.setStatus("current")
_TIPsecRUSATrafficSelTable_Object = MibTable
tIPsecRUSATrafficSelTable = _TIPsecRUSATrafficSelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53)
)
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelTable.setStatus("current")
_TIPsecRUSATrafficSelEntry_Object = MibTableRow
tIPsecRUSATrafficSelEntry = _TIPsecRUSATrafficSelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1)
)
tIPsecRUSATrafficSelEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlPort"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSAId"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSADirection"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSAIndex"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelSide"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelFrAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelFrAddr"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelToAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelToAddr"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelMinPort"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelMaxPort"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelProtocolId"),
)
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelEntry.setStatus("current")
_TIPsecRUSATrafficSelSide_Type = TmnxIpsecTrafficSelSide
_TIPsecRUSATrafficSelSide_Object = MibTableColumn
tIPsecRUSATrafficSelSide = _TIPsecRUSATrafficSelSide_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 1),
    _TIPsecRUSATrafficSelSide_Type()
)
tIPsecRUSATrafficSelSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelSide.setStatus("current")
_TIPsecRUSATrafficSelFrAddrType_Type = InetAddressType
_TIPsecRUSATrafficSelFrAddrType_Object = MibTableColumn
tIPsecRUSATrafficSelFrAddrType = _TIPsecRUSATrafficSelFrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 2),
    _TIPsecRUSATrafficSelFrAddrType_Type()
)
tIPsecRUSATrafficSelFrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelFrAddrType.setStatus("current")


class _TIPsecRUSATrafficSelFrAddr_Type(InetAddress):
    """Custom type tIPsecRUSATrafficSelFrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecRUSATrafficSelFrAddr_Type.__name__ = "InetAddress"
_TIPsecRUSATrafficSelFrAddr_Object = MibTableColumn
tIPsecRUSATrafficSelFrAddr = _TIPsecRUSATrafficSelFrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 3),
    _TIPsecRUSATrafficSelFrAddr_Type()
)
tIPsecRUSATrafficSelFrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelFrAddr.setStatus("current")
_TIPsecRUSATrafficSelToAddrType_Type = InetAddressType
_TIPsecRUSATrafficSelToAddrType_Object = MibTableColumn
tIPsecRUSATrafficSelToAddrType = _TIPsecRUSATrafficSelToAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 4),
    _TIPsecRUSATrafficSelToAddrType_Type()
)
tIPsecRUSATrafficSelToAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelToAddrType.setStatus("current")


class _TIPsecRUSATrafficSelToAddr_Type(InetAddress):
    """Custom type tIPsecRUSATrafficSelToAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecRUSATrafficSelToAddr_Type.__name__ = "InetAddress"
_TIPsecRUSATrafficSelToAddr_Object = MibTableColumn
tIPsecRUSATrafficSelToAddr = _TIPsecRUSATrafficSelToAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 5),
    _TIPsecRUSATrafficSelToAddr_Type()
)
tIPsecRUSATrafficSelToAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelToAddr.setStatus("current")
_TIPsecRUSATrafficSelLastChgd_Type = TimeStamp
_TIPsecRUSATrafficSelLastChgd_Object = MibTableColumn
tIPsecRUSATrafficSelLastChgd = _TIPsecRUSATrafficSelLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 6),
    _TIPsecRUSATrafficSelLastChgd_Type()
)
tIPsecRUSATrafficSelLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelLastChgd.setStatus("current")
_TIPsecRUSATrafficSelMinPort_Type = InetPortNumber
_TIPsecRUSATrafficSelMinPort_Object = MibTableColumn
tIPsecRUSATrafficSelMinPort = _TIPsecRUSATrafficSelMinPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 7),
    _TIPsecRUSATrafficSelMinPort_Type()
)
tIPsecRUSATrafficSelMinPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelMinPort.setStatus("current")
_TIPsecRUSATrafficSelMaxPort_Type = InetPortNumber
_TIPsecRUSATrafficSelMaxPort_Object = MibTableColumn
tIPsecRUSATrafficSelMaxPort = _TIPsecRUSATrafficSelMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 8),
    _TIPsecRUSATrafficSelMaxPort_Type()
)
tIPsecRUSATrafficSelMaxPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelMaxPort.setStatus("current")


class _TIPsecRUSATrafficSelProtocolId_Type(Unsigned32):
    """Custom type tIPsecRUSATrafficSelProtocolId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TIPsecRUSATrafficSelProtocolId_Type.__name__ = "Unsigned32"
_TIPsecRUSATrafficSelProtocolId_Object = MibTableColumn
tIPsecRUSATrafficSelProtocolId = _TIPsecRUSATrafficSelProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 9),
    _TIPsecRUSATrafficSelProtocolId_Type()
)
tIPsecRUSATrafficSelProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelProtocolId.setStatus("current")
_TmnxIPsecGWDhcpTblLastChgd_Type = TimeStamp
_TmnxIPsecGWDhcpTblLastChgd_Object = MibScalar
tmnxIPsecGWDhcpTblLastChgd = _TmnxIPsecGWDhcpTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 54),
    _TmnxIPsecGWDhcpTblLastChgd_Type()
)
tmnxIPsecGWDhcpTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpTblLastChgd.setStatus("current")
_TmnxIPsecGWDhcpTable_Object = MibTable
tmnxIPsecGWDhcpTable = _TmnxIPsecGWDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55)
)
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpTable.setStatus("current")
_TmnxIPsecGWDhcpEntry_Object = MibTableRow
tmnxIPsecGWDhcpEntry = _TmnxIPsecGWDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1)
)
tmnxIPsecGWDhcpEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpEntry.setStatus("current")
_TmnxIPsecGWDhcpRowStatus_Type = RowStatus
_TmnxIPsecGWDhcpRowStatus_Object = MibTableColumn
tmnxIPsecGWDhcpRowStatus = _TmnxIPsecGWDhcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 1),
    _TmnxIPsecGWDhcpRowStatus_Type()
)
tmnxIPsecGWDhcpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpRowStatus.setStatus("current")
_TmnxIPsecGWDhcpLastChgd_Type = TimeStamp
_TmnxIPsecGWDhcpLastChgd_Object = MibTableColumn
tmnxIPsecGWDhcpLastChgd = _TmnxIPsecGWDhcpLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 2),
    _TmnxIPsecGWDhcpLastChgd_Type()
)
tmnxIPsecGWDhcpLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpLastChgd.setStatus("current")


class _TmnxIPsecGWDhcpAdminState_Type(TmnxAdminState):
    """Custom type tmnxIPsecGWDhcpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIPsecGWDhcpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIPsecGWDhcpAdminState_Object = MibTableColumn
tmnxIPsecGWDhcpAdminState = _TmnxIPsecGWDhcpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 3),
    _TmnxIPsecGWDhcpAdminState_Type()
)
tmnxIPsecGWDhcpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpAdminState.setStatus("current")


class _TmnxIPsecGWDhcpGiAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpGiAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpGiAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpGiAddrType_Object = MibTableColumn
tmnxIPsecGWDhcpGiAddrType = _TmnxIPsecGWDhcpGiAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 4),
    _TmnxIPsecGWDhcpGiAddrType_Type()
)
tmnxIPsecGWDhcpGiAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpGiAddrType.setStatus("current")


class _TmnxIPsecGWDhcpGiAddr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpGiAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxIPsecGWDhcpGiAddr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpGiAddr_Object = MibTableColumn
tmnxIPsecGWDhcpGiAddr = _TmnxIPsecGWDhcpGiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 5),
    _TmnxIPsecGWDhcpGiAddr_Type()
)
tmnxIPsecGWDhcpGiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpGiAddr.setStatus("current")


class _TmnxIPsecGWDhcpSendRelease_Type(TruthValue):
    """Custom type tmnxIPsecGWDhcpSendRelease based on TruthValue"""
    defaultValue = 1


_TmnxIPsecGWDhcpSendRelease_Type.__name__ = "TruthValue"
_TmnxIPsecGWDhcpSendRelease_Object = MibTableColumn
tmnxIPsecGWDhcpSendRelease = _TmnxIPsecGWDhcpSendRelease_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 6),
    _TmnxIPsecGWDhcpSendRelease_Type()
)
tmnxIPsecGWDhcpSendRelease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSendRelease.setStatus("current")


class _TmnxIPsecGWDhcpServiceId_Type(TmnxServId):
    """Custom type tmnxIPsecGWDhcpServiceId based on TmnxServId"""
    defaultValue = 0


_TmnxIPsecGWDhcpServiceId_Type.__name__ = "TmnxServId"
_TmnxIPsecGWDhcpServiceId_Object = MibTableColumn
tmnxIPsecGWDhcpServiceId = _TmnxIPsecGWDhcpServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 7),
    _TmnxIPsecGWDhcpServiceId_Type()
)
tmnxIPsecGWDhcpServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpServiceId.setStatus("current")


class _TmnxIPsecGWDhcpRouterId_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxIPsecGWDhcpRouterId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxIPsecGWDhcpRouterId_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxIPsecGWDhcpRouterId_Object = MibTableColumn
tmnxIPsecGWDhcpRouterId = _TmnxIPsecGWDhcpRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 8),
    _TmnxIPsecGWDhcpRouterId_Type()
)
tmnxIPsecGWDhcpRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpRouterId.setStatus("current")


class _TmnxIPsecGWDhcpSrvr1AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpSrvr1AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpSrvr1AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpSrvr1AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr1AddrType = _TmnxIPsecGWDhcpSrvr1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 9),
    _TmnxIPsecGWDhcpSrvr1AddrType_Type()
)
tmnxIPsecGWDhcpSrvr1AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr1AddrType.setStatus("current")


class _TmnxIPsecGWDhcpSrvr1Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpSrvr1Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxIPsecGWDhcpSrvr1Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpSrvr1Addr_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr1Addr = _TmnxIPsecGWDhcpSrvr1Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 10),
    _TmnxIPsecGWDhcpSrvr1Addr_Type()
)
tmnxIPsecGWDhcpSrvr1Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr1Addr.setStatus("current")


class _TmnxIPsecGWDhcpSrvr2AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpSrvr2AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpSrvr2AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpSrvr2AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr2AddrType = _TmnxIPsecGWDhcpSrvr2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 11),
    _TmnxIPsecGWDhcpSrvr2AddrType_Type()
)
tmnxIPsecGWDhcpSrvr2AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr2AddrType.setStatus("current")


class _TmnxIPsecGWDhcpSrvr2Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpSrvr2Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxIPsecGWDhcpSrvr2Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpSrvr2Addr_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr2Addr = _TmnxIPsecGWDhcpSrvr2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 12),
    _TmnxIPsecGWDhcpSrvr2Addr_Type()
)
tmnxIPsecGWDhcpSrvr2Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr2Addr.setStatus("current")


class _TmnxIPsecGWDhcpSrvr3AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpSrvr3AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpSrvr3AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpSrvr3AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr3AddrType = _TmnxIPsecGWDhcpSrvr3AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 13),
    _TmnxIPsecGWDhcpSrvr3AddrType_Type()
)
tmnxIPsecGWDhcpSrvr3AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr3AddrType.setStatus("current")


class _TmnxIPsecGWDhcpSrvr3Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpSrvr3Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxIPsecGWDhcpSrvr3Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpSrvr3Addr_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr3Addr = _TmnxIPsecGWDhcpSrvr3Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 14),
    _TmnxIPsecGWDhcpSrvr3Addr_Type()
)
tmnxIPsecGWDhcpSrvr3Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr3Addr.setStatus("current")


class _TmnxIPsecGWDhcpSrvr4AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpSrvr4AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpSrvr4AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpSrvr4AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr4AddrType = _TmnxIPsecGWDhcpSrvr4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 15),
    _TmnxIPsecGWDhcpSrvr4AddrType_Type()
)
tmnxIPsecGWDhcpSrvr4AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr4AddrType.setStatus("current")


class _TmnxIPsecGWDhcpSrvr4Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpSrvr4Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxIPsecGWDhcpSrvr4Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpSrvr4Addr_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr4Addr = _TmnxIPsecGWDhcpSrvr4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 16),
    _TmnxIPsecGWDhcpSrvr4Addr_Type()
)
tmnxIPsecGWDhcpSrvr4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr4Addr.setStatus("current")


class _TmnxIPsecGWDhcpSrvr5AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpSrvr5AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpSrvr5AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpSrvr5AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr5AddrType = _TmnxIPsecGWDhcpSrvr5AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 17),
    _TmnxIPsecGWDhcpSrvr5AddrType_Type()
)
tmnxIPsecGWDhcpSrvr5AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr5AddrType.setStatus("current")


class _TmnxIPsecGWDhcpSrvr5Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpSrvr5Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxIPsecGWDhcpSrvr5Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpSrvr5Addr_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr5Addr = _TmnxIPsecGWDhcpSrvr5Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 18),
    _TmnxIPsecGWDhcpSrvr5Addr_Type()
)
tmnxIPsecGWDhcpSrvr5Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr5Addr.setStatus("current")


class _TmnxIPsecGWDhcpSrvr6AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpSrvr6AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpSrvr6AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpSrvr6AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr6AddrType = _TmnxIPsecGWDhcpSrvr6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 19),
    _TmnxIPsecGWDhcpSrvr6AddrType_Type()
)
tmnxIPsecGWDhcpSrvr6AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr6AddrType.setStatus("current")


class _TmnxIPsecGWDhcpSrvr6Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpSrvr6Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxIPsecGWDhcpSrvr6Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpSrvr6Addr_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr6Addr = _TmnxIPsecGWDhcpSrvr6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 20),
    _TmnxIPsecGWDhcpSrvr6Addr_Type()
)
tmnxIPsecGWDhcpSrvr6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr6Addr.setStatus("current")


class _TmnxIPsecGWDhcpSrvr7AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpSrvr7AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpSrvr7AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpSrvr7AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr7AddrType = _TmnxIPsecGWDhcpSrvr7AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 21),
    _TmnxIPsecGWDhcpSrvr7AddrType_Type()
)
tmnxIPsecGWDhcpSrvr7AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr7AddrType.setStatus("current")


class _TmnxIPsecGWDhcpSrvr7Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpSrvr7Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxIPsecGWDhcpSrvr7Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpSrvr7Addr_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr7Addr = _TmnxIPsecGWDhcpSrvr7Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 22),
    _TmnxIPsecGWDhcpSrvr7Addr_Type()
)
tmnxIPsecGWDhcpSrvr7Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr7Addr.setStatus("current")


class _TmnxIPsecGWDhcpSrvr8AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpSrvr8AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpSrvr8AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpSrvr8AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr8AddrType = _TmnxIPsecGWDhcpSrvr8AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 23),
    _TmnxIPsecGWDhcpSrvr8AddrType_Type()
)
tmnxIPsecGWDhcpSrvr8AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr8AddrType.setStatus("current")


class _TmnxIPsecGWDhcpSrvr8Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpSrvr8Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxIPsecGWDhcpSrvr8Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpSrvr8Addr_Object = MibTableColumn
tmnxIPsecGWDhcpSrvr8Addr = _TmnxIPsecGWDhcpSrvr8Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 24),
    _TmnxIPsecGWDhcpSrvr8Addr_Type()
)
tmnxIPsecGWDhcpSrvr8Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpSrvr8Addr.setStatus("current")


class _TmnxIPsecGWDhcpServiceName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxIPsecGWDhcpServiceName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWDhcpServiceName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxIPsecGWDhcpServiceName_Object = MibTableColumn
tmnxIPsecGWDhcpServiceName = _TmnxIPsecGWDhcpServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 55, 1, 25),
    _TmnxIPsecGWDhcpServiceName_Type()
)
tmnxIPsecGWDhcpServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpServiceName.setStatus("current")
_TIPsecGWLclAddrAssignTblLastChgd_Type = TimeStamp
_TIPsecGWLclAddrAssignTblLastChgd_Object = MibScalar
tIPsecGWLclAddrAssignTblLastChgd = _TIPsecGWLclAddrAssignTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 56),
    _TIPsecGWLclAddrAssignTblLastChgd_Type()
)
tIPsecGWLclAddrAssignTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignTblLastChgd.setStatus("current")
_TIPsecGWLclAddrAssignTable_Object = MibTable
tIPsecGWLclAddrAssignTable = _TIPsecGWLclAddrAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57)
)
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignTable.setStatus("current")
_TIPsecGWLclAddrAssignEntry_Object = MibTableRow
tIPsecGWLclAddrAssignEntry = _TIPsecGWLclAddrAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1)
)
tIPsecGWLclAddrAssignEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignEntry.setStatus("current")
_TIPsecGWLclAddrAssignRowStatus_Type = RowStatus
_TIPsecGWLclAddrAssignRowStatus_Object = MibTableColumn
tIPsecGWLclAddrAssignRowStatus = _TIPsecGWLclAddrAssignRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 1),
    _TIPsecGWLclAddrAssignRowStatus_Type()
)
tIPsecGWLclAddrAssignRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignRowStatus.setStatus("current")
_TIPsecGWLclAddrAssignLastChgd_Type = TimeStamp
_TIPsecGWLclAddrAssignLastChgd_Object = MibTableColumn
tIPsecGWLclAddrAssignLastChgd = _TIPsecGWLclAddrAssignLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 2),
    _TIPsecGWLclAddrAssignLastChgd_Type()
)
tIPsecGWLclAddrAssignLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignLastChgd.setStatus("current")


class _TIPsecGWLclAddrAssignAdminState_Type(TmnxAdminState):
    """Custom type tIPsecGWLclAddrAssignAdminState based on TmnxAdminState"""
    defaultValue = 3


_TIPsecGWLclAddrAssignAdminState_Type.__name__ = "TmnxAdminState"
_TIPsecGWLclAddrAssignAdminState_Object = MibTableColumn
tIPsecGWLclAddrAssignAdminState = _TIPsecGWLclAddrAssignAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 3),
    _TIPsecGWLclAddrAssignAdminState_Type()
)
tIPsecGWLclAddrAssignAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignAdminState.setStatus("current")


class _TIPsecGWLclAddrAssignIp4SrvrName_Type(TNamedItemOrEmpty):
    """Custom type tIPsecGWLclAddrAssignIp4SrvrName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPsecGWLclAddrAssignIp4SrvrName_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecGWLclAddrAssignIp4SrvrName_Object = MibTableColumn
tIPsecGWLclAddrAssignIp4SrvrName = _TIPsecGWLclAddrAssignIp4SrvrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 4),
    _TIPsecGWLclAddrAssignIp4SrvrName_Type()
)
tIPsecGWLclAddrAssignIp4SrvrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignIp4SrvrName.setStatus("current")


class _TIPsecGWLclAddrAssignIp4SrvrSvc_Type(TmnxServId):
    """Custom type tIPsecGWLclAddrAssignIp4SrvrSvc based on TmnxServId"""
    defaultValue = 0


_TIPsecGWLclAddrAssignIp4SrvrSvc_Type.__name__ = "TmnxServId"
_TIPsecGWLclAddrAssignIp4SrvrSvc_Object = MibTableColumn
tIPsecGWLclAddrAssignIp4SrvrSvc = _TIPsecGWLclAddrAssignIp4SrvrSvc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 5),
    _TIPsecGWLclAddrAssignIp4SrvrSvc_Type()
)
tIPsecGWLclAddrAssignIp4SrvrSvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignIp4SrvrSvc.setStatus("current")


class _TIPsecGWLclAddrAssignIp4SrvrRtr_Type(TmnxVRtrIDOrZero):
    """Custom type tIPsecGWLclAddrAssignIp4SrvrRtr based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPsecGWLclAddrAssignIp4SrvrRtr_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPsecGWLclAddrAssignIp4SrvrRtr_Object = MibTableColumn
tIPsecGWLclAddrAssignIp4SrvrRtr = _TIPsecGWLclAddrAssignIp4SrvrRtr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 6),
    _TIPsecGWLclAddrAssignIp4SrvrRtr_Type()
)
tIPsecGWLclAddrAssignIp4SrvrRtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignIp4SrvrRtr.setStatus("current")


class _TIPsecGWLclAddrAssignIp4PoolName_Type(TNamedItemOrEmpty):
    """Custom type tIPsecGWLclAddrAssignIp4PoolName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPsecGWLclAddrAssignIp4PoolName_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecGWLclAddrAssignIp4PoolName_Object = MibTableColumn
tIPsecGWLclAddrAssignIp4PoolName = _TIPsecGWLclAddrAssignIp4PoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 7),
    _TIPsecGWLclAddrAssignIp4PoolName_Type()
)
tIPsecGWLclAddrAssignIp4PoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignIp4PoolName.setStatus("current")


class _TIPsecGWLclAddrAssignIp6SrvrName_Type(TNamedItemOrEmpty):
    """Custom type tIPsecGWLclAddrAssignIp6SrvrName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPsecGWLclAddrAssignIp6SrvrName_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecGWLclAddrAssignIp6SrvrName_Object = MibTableColumn
tIPsecGWLclAddrAssignIp6SrvrName = _TIPsecGWLclAddrAssignIp6SrvrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 8),
    _TIPsecGWLclAddrAssignIp6SrvrName_Type()
)
tIPsecGWLclAddrAssignIp6SrvrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignIp6SrvrName.setStatus("current")


class _TIPsecGWLclAddrAssignIp6SrvrSvc_Type(TmnxServId):
    """Custom type tIPsecGWLclAddrAssignIp6SrvrSvc based on TmnxServId"""
    defaultValue = 0


_TIPsecGWLclAddrAssignIp6SrvrSvc_Type.__name__ = "TmnxServId"
_TIPsecGWLclAddrAssignIp6SrvrSvc_Object = MibTableColumn
tIPsecGWLclAddrAssignIp6SrvrSvc = _TIPsecGWLclAddrAssignIp6SrvrSvc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 9),
    _TIPsecGWLclAddrAssignIp6SrvrSvc_Type()
)
tIPsecGWLclAddrAssignIp6SrvrSvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignIp6SrvrSvc.setStatus("current")


class _TIPsecGWLclAddrAssignIp6SrvrRtr_Type(TmnxVRtrIDOrZero):
    """Custom type tIPsecGWLclAddrAssignIp6SrvrRtr based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPsecGWLclAddrAssignIp6SrvrRtr_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPsecGWLclAddrAssignIp6SrvrRtr_Object = MibTableColumn
tIPsecGWLclAddrAssignIp6SrvrRtr = _TIPsecGWLclAddrAssignIp6SrvrRtr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 10),
    _TIPsecGWLclAddrAssignIp6SrvrRtr_Type()
)
tIPsecGWLclAddrAssignIp6SrvrRtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignIp6SrvrRtr.setStatus("current")


class _TIPsecGWLclAddrAssignIp6PoolName_Type(TNamedItemOrEmpty):
    """Custom type tIPsecGWLclAddrAssignIp6PoolName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPsecGWLclAddrAssignIp6PoolName_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecGWLclAddrAssignIp6PoolName_Object = MibTableColumn
tIPsecGWLclAddrAssignIp6PoolName = _TIPsecGWLclAddrAssignIp6PoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 11),
    _TIPsecGWLclAddrAssignIp6PoolName_Type()
)
tIPsecGWLclAddrAssignIp6PoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignIp6PoolName.setStatus("current")


class _TIPsecGWLclAddrAssignIp4PoolNam2_Type(TNamedItemOrEmpty):
    """Custom type tIPsecGWLclAddrAssignIp4PoolNam2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPsecGWLclAddrAssignIp4PoolNam2_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecGWLclAddrAssignIp4PoolNam2_Object = MibTableColumn
tIPsecGWLclAddrAssignIp4PoolNam2 = _TIPsecGWLclAddrAssignIp4PoolNam2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 12),
    _TIPsecGWLclAddrAssignIp4PoolNam2_Type()
)
tIPsecGWLclAddrAssignIp4PoolNam2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignIp4PoolNam2.setStatus("current")


class _TIPsecGWLclAddrAssignIp4SrvrSvcN_Type(TLNamedItemOrEmpty):
    """Custom type tIPsecGWLclAddrAssignIp4SrvrSvcN based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPsecGWLclAddrAssignIp4SrvrSvcN_Type.__name__ = "TLNamedItemOrEmpty"
_TIPsecGWLclAddrAssignIp4SrvrSvcN_Object = MibTableColumn
tIPsecGWLclAddrAssignIp4SrvrSvcN = _TIPsecGWLclAddrAssignIp4SrvrSvcN_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 14),
    _TIPsecGWLclAddrAssignIp4SrvrSvcN_Type()
)
tIPsecGWLclAddrAssignIp4SrvrSvcN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignIp4SrvrSvcN.setStatus("current")


class _TIPsecGWLclAddrAssignIp6SrvrSvcN_Type(TLNamedItemOrEmpty):
    """Custom type tIPsecGWLclAddrAssignIp6SrvrSvcN based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPsecGWLclAddrAssignIp6SrvrSvcN_Type.__name__ = "TLNamedItemOrEmpty"
_TIPsecGWLclAddrAssignIp6SrvrSvcN_Object = MibTableColumn
tIPsecGWLclAddrAssignIp6SrvrSvcN = _TIPsecGWLclAddrAssignIp6SrvrSvcN_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 57, 1, 15),
    _TIPsecGWLclAddrAssignIp6SrvrSvcN_Type()
)
tIPsecGWLclAddrAssignIp6SrvrSvcN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWLclAddrAssignIp6SrvrSvcN.setStatus("current")
_TmnxIPsecGWDhcpV6TblLastChgd_Type = TimeStamp
_TmnxIPsecGWDhcpV6TblLastChgd_Object = MibScalar
tmnxIPsecGWDhcpV6TblLastChgd = _TmnxIPsecGWDhcpV6TblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 58),
    _TmnxIPsecGWDhcpV6TblLastChgd_Type()
)
tmnxIPsecGWDhcpV6TblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6TblLastChgd.setStatus("current")
_TmnxIPsecGWDhcpV6Table_Object = MibTable
tmnxIPsecGWDhcpV6Table = _TmnxIPsecGWDhcpV6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59)
)
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Table.setStatus("current")
_TmnxIPsecGWDhcpV6Entry_Object = MibTableRow
tmnxIPsecGWDhcpV6Entry = _TmnxIPsecGWDhcpV6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1)
)
tmnxIPsecGWDhcpV6Entry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Entry.setStatus("current")
_TmnxIPsecGWDhcpV6RowStatus_Type = RowStatus
_TmnxIPsecGWDhcpV6RowStatus_Object = MibTableColumn
tmnxIPsecGWDhcpV6RowStatus = _TmnxIPsecGWDhcpV6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 1),
    _TmnxIPsecGWDhcpV6RowStatus_Type()
)
tmnxIPsecGWDhcpV6RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6RowStatus.setStatus("current")
_TmnxIPsecGWDhcpV6LastChgd_Type = TimeStamp
_TmnxIPsecGWDhcpV6LastChgd_Object = MibTableColumn
tmnxIPsecGWDhcpV6LastChgd = _TmnxIPsecGWDhcpV6LastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 2),
    _TmnxIPsecGWDhcpV6LastChgd_Type()
)
tmnxIPsecGWDhcpV6LastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6LastChgd.setStatus("current")


class _TmnxIPsecGWDhcpV6AdminState_Type(TmnxAdminState):
    """Custom type tmnxIPsecGWDhcpV6AdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIPsecGWDhcpV6AdminState_Type.__name__ = "TmnxAdminState"
_TmnxIPsecGWDhcpV6AdminState_Object = MibTableColumn
tmnxIPsecGWDhcpV6AdminState = _TmnxIPsecGWDhcpV6AdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 3),
    _TmnxIPsecGWDhcpV6AdminState_Type()
)
tmnxIPsecGWDhcpV6AdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6AdminState.setStatus("current")


class _TmnxIPsecGWDhcpV6LinkAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpV6LinkAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpV6LinkAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpV6LinkAddrType_Object = MibTableColumn
tmnxIPsecGWDhcpV6LinkAddrType = _TmnxIPsecGWDhcpV6LinkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 4),
    _TmnxIPsecGWDhcpV6LinkAddrType_Type()
)
tmnxIPsecGWDhcpV6LinkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6LinkAddrType.setStatus("current")


class _TmnxIPsecGWDhcpV6LinkAddr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpV6LinkAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecGWDhcpV6LinkAddr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpV6LinkAddr_Object = MibTableColumn
tmnxIPsecGWDhcpV6LinkAddr = _TmnxIPsecGWDhcpV6LinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 5),
    _TmnxIPsecGWDhcpV6LinkAddr_Type()
)
tmnxIPsecGWDhcpV6LinkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6LinkAddr.setStatus("current")


class _TmnxIPsecGWDhcpV6SendRelease_Type(TruthValue):
    """Custom type tmnxIPsecGWDhcpV6SendRelease based on TruthValue"""
    defaultValue = 1


_TmnxIPsecGWDhcpV6SendRelease_Type.__name__ = "TruthValue"
_TmnxIPsecGWDhcpV6SendRelease_Object = MibTableColumn
tmnxIPsecGWDhcpV6SendRelease = _TmnxIPsecGWDhcpV6SendRelease_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 6),
    _TmnxIPsecGWDhcpV6SendRelease_Type()
)
tmnxIPsecGWDhcpV6SendRelease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6SendRelease.setStatus("current")


class _TmnxIPsecGWDhcpV6ServiceId_Type(TmnxServId):
    """Custom type tmnxIPsecGWDhcpV6ServiceId based on TmnxServId"""
    defaultValue = 0


_TmnxIPsecGWDhcpV6ServiceId_Type.__name__ = "TmnxServId"
_TmnxIPsecGWDhcpV6ServiceId_Object = MibTableColumn
tmnxIPsecGWDhcpV6ServiceId = _TmnxIPsecGWDhcpV6ServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 7),
    _TmnxIPsecGWDhcpV6ServiceId_Type()
)
tmnxIPsecGWDhcpV6ServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6ServiceId.setStatus("current")


class _TmnxIPsecGWDhcpV6RouterId_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxIPsecGWDhcpV6RouterId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxIPsecGWDhcpV6RouterId_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxIPsecGWDhcpV6RouterId_Object = MibTableColumn
tmnxIPsecGWDhcpV6RouterId = _TmnxIPsecGWDhcpV6RouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 8),
    _TmnxIPsecGWDhcpV6RouterId_Type()
)
tmnxIPsecGWDhcpV6RouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6RouterId.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr1AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpV6Srvr1AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpV6Srvr1AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpV6Srvr1AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr1AddrType = _TmnxIPsecGWDhcpV6Srvr1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 9),
    _TmnxIPsecGWDhcpV6Srvr1AddrType_Type()
)
tmnxIPsecGWDhcpV6Srvr1AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr1AddrType.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr1Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpV6Srvr1Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecGWDhcpV6Srvr1Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpV6Srvr1Addr_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr1Addr = _TmnxIPsecGWDhcpV6Srvr1Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 10),
    _TmnxIPsecGWDhcpV6Srvr1Addr_Type()
)
tmnxIPsecGWDhcpV6Srvr1Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr1Addr.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr2AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpV6Srvr2AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpV6Srvr2AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpV6Srvr2AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr2AddrType = _TmnxIPsecGWDhcpV6Srvr2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 11),
    _TmnxIPsecGWDhcpV6Srvr2AddrType_Type()
)
tmnxIPsecGWDhcpV6Srvr2AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr2AddrType.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr2Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpV6Srvr2Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecGWDhcpV6Srvr2Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpV6Srvr2Addr_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr2Addr = _TmnxIPsecGWDhcpV6Srvr2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 12),
    _TmnxIPsecGWDhcpV6Srvr2Addr_Type()
)
tmnxIPsecGWDhcpV6Srvr2Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr2Addr.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr3AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpV6Srvr3AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpV6Srvr3AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpV6Srvr3AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr3AddrType = _TmnxIPsecGWDhcpV6Srvr3AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 13),
    _TmnxIPsecGWDhcpV6Srvr3AddrType_Type()
)
tmnxIPsecGWDhcpV6Srvr3AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr3AddrType.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr3Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpV6Srvr3Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecGWDhcpV6Srvr3Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpV6Srvr3Addr_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr3Addr = _TmnxIPsecGWDhcpV6Srvr3Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 14),
    _TmnxIPsecGWDhcpV6Srvr3Addr_Type()
)
tmnxIPsecGWDhcpV6Srvr3Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr3Addr.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr4AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpV6Srvr4AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpV6Srvr4AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpV6Srvr4AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr4AddrType = _TmnxIPsecGWDhcpV6Srvr4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 15),
    _TmnxIPsecGWDhcpV6Srvr4AddrType_Type()
)
tmnxIPsecGWDhcpV6Srvr4AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr4AddrType.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr4Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpV6Srvr4Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecGWDhcpV6Srvr4Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpV6Srvr4Addr_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr4Addr = _TmnxIPsecGWDhcpV6Srvr4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 16),
    _TmnxIPsecGWDhcpV6Srvr4Addr_Type()
)
tmnxIPsecGWDhcpV6Srvr4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr4Addr.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr5AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpV6Srvr5AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpV6Srvr5AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpV6Srvr5AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr5AddrType = _TmnxIPsecGWDhcpV6Srvr5AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 17),
    _TmnxIPsecGWDhcpV6Srvr5AddrType_Type()
)
tmnxIPsecGWDhcpV6Srvr5AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr5AddrType.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr5Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpV6Srvr5Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecGWDhcpV6Srvr5Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpV6Srvr5Addr_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr5Addr = _TmnxIPsecGWDhcpV6Srvr5Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 18),
    _TmnxIPsecGWDhcpV6Srvr5Addr_Type()
)
tmnxIPsecGWDhcpV6Srvr5Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr5Addr.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr6AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpV6Srvr6AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpV6Srvr6AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpV6Srvr6AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr6AddrType = _TmnxIPsecGWDhcpV6Srvr6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 19),
    _TmnxIPsecGWDhcpV6Srvr6AddrType_Type()
)
tmnxIPsecGWDhcpV6Srvr6AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr6AddrType.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr6Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpV6Srvr6Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecGWDhcpV6Srvr6Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpV6Srvr6Addr_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr6Addr = _TmnxIPsecGWDhcpV6Srvr6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 20),
    _TmnxIPsecGWDhcpV6Srvr6Addr_Type()
)
tmnxIPsecGWDhcpV6Srvr6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr6Addr.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr7AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpV6Srvr7AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpV6Srvr7AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpV6Srvr7AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr7AddrType = _TmnxIPsecGWDhcpV6Srvr7AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 21),
    _TmnxIPsecGWDhcpV6Srvr7AddrType_Type()
)
tmnxIPsecGWDhcpV6Srvr7AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr7AddrType.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr7Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpV6Srvr7Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecGWDhcpV6Srvr7Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpV6Srvr7Addr_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr7Addr = _TmnxIPsecGWDhcpV6Srvr7Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 22),
    _TmnxIPsecGWDhcpV6Srvr7Addr_Type()
)
tmnxIPsecGWDhcpV6Srvr7Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr7Addr.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr8AddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWDhcpV6Srvr8AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWDhcpV6Srvr8AddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWDhcpV6Srvr8AddrType_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr8AddrType = _TmnxIPsecGWDhcpV6Srvr8AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 23),
    _TmnxIPsecGWDhcpV6Srvr8AddrType_Type()
)
tmnxIPsecGWDhcpV6Srvr8AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr8AddrType.setStatus("current")


class _TmnxIPsecGWDhcpV6Srvr8Addr_Type(InetAddress):
    """Custom type tmnxIPsecGWDhcpV6Srvr8Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecGWDhcpV6Srvr8Addr_Type.__name__ = "InetAddress"
_TmnxIPsecGWDhcpV6Srvr8Addr_Object = MibTableColumn
tmnxIPsecGWDhcpV6Srvr8Addr = _TmnxIPsecGWDhcpV6Srvr8Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 24),
    _TmnxIPsecGWDhcpV6Srvr8Addr_Type()
)
tmnxIPsecGWDhcpV6Srvr8Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Srvr8Addr.setStatus("current")


class _TmnxIPsecGWDhcpV6ServiceName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxIPsecGWDhcpV6ServiceName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWDhcpV6ServiceName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxIPsecGWDhcpV6ServiceName_Object = MibTableColumn
tmnxIPsecGWDhcpV6ServiceName = _TmnxIPsecGWDhcpV6ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 59, 1, 25),
    _TmnxIPsecGWDhcpV6ServiceName_Type()
)
tmnxIPsecGWDhcpV6ServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6ServiceName.setStatus("current")
_TIPsecTsListRmtEntryTblLastChgd_Type = TimeStamp
_TIPsecTsListRmtEntryTblLastChgd_Object = MibScalar
tIPsecTsListRmtEntryTblLastChgd = _TIPsecTsListRmtEntryTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 60),
    _TIPsecTsListRmtEntryTblLastChgd_Type()
)
tIPsecTsListRmtEntryTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryTblLastChgd.setStatus("current")
_TIPsecTsListRmtEntryTable_Object = MibTable
tIPsecTsListRmtEntryTable = _TIPsecTsListRmtEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61)
)
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryTable.setStatus("current")
_TIPsecTsListRmtEntryEntry_Object = MibTableRow
tIPsecTsListRmtEntryEntry = _TIPsecTsListRmtEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1)
)
tIPsecTsListRmtEntryEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTsListName"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryId"),
)
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryEntry.setStatus("current")


class _TIPsecTsListRmtEntryId_Type(Unsigned32):
    """Custom type tIPsecTsListRmtEntryId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TIPsecTsListRmtEntryId_Type.__name__ = "Unsigned32"
_TIPsecTsListRmtEntryId_Object = MibTableColumn
tIPsecTsListRmtEntryId = _TIPsecTsListRmtEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 1),
    _TIPsecTsListRmtEntryId_Type()
)
tIPsecTsListRmtEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryId.setStatus("current")
_TIPsecTsListRmtEntryRowStatus_Type = RowStatus
_TIPsecTsListRmtEntryRowStatus_Object = MibTableColumn
tIPsecTsListRmtEntryRowStatus = _TIPsecTsListRmtEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 2),
    _TIPsecTsListRmtEntryRowStatus_Type()
)
tIPsecTsListRmtEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryRowStatus.setStatus("current")
_TIPsecTsListRmtEntryLastChgd_Type = TimeStamp
_TIPsecTsListRmtEntryLastChgd_Object = MibTableColumn
tIPsecTsListRmtEntryLastChgd = _TIPsecTsListRmtEntryLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 3),
    _TIPsecTsListRmtEntryLastChgd_Type()
)
tIPsecTsListRmtEntryLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryLastChgd.setStatus("current")


class _TIPsecTsListRmtEntryMinAddrType_Type(InetAddressType):
    """Custom type tIPsecTsListRmtEntryMinAddrType based on InetAddressType"""
    defaultValue = 0


_TIPsecTsListRmtEntryMinAddrType_Type.__name__ = "InetAddressType"
_TIPsecTsListRmtEntryMinAddrType_Object = MibTableColumn
tIPsecTsListRmtEntryMinAddrType = _TIPsecTsListRmtEntryMinAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 4),
    _TIPsecTsListRmtEntryMinAddrType_Type()
)
tIPsecTsListRmtEntryMinAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryMinAddrType.setStatus("current")


class _TIPsecTsListRmtEntryMinAddr_Type(InetAddress):
    """Custom type tIPsecTsListRmtEntryMinAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TIPsecTsListRmtEntryMinAddr_Type.__name__ = "InetAddress"
_TIPsecTsListRmtEntryMinAddr_Object = MibTableColumn
tIPsecTsListRmtEntryMinAddr = _TIPsecTsListRmtEntryMinAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 5),
    _TIPsecTsListRmtEntryMinAddr_Type()
)
tIPsecTsListRmtEntryMinAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryMinAddr.setStatus("current")


class _TIPsecTsListRmtEntryMaxAddrType_Type(InetAddressType):
    """Custom type tIPsecTsListRmtEntryMaxAddrType based on InetAddressType"""
    defaultValue = 0


_TIPsecTsListRmtEntryMaxAddrType_Type.__name__ = "InetAddressType"
_TIPsecTsListRmtEntryMaxAddrType_Object = MibTableColumn
tIPsecTsListRmtEntryMaxAddrType = _TIPsecTsListRmtEntryMaxAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 6),
    _TIPsecTsListRmtEntryMaxAddrType_Type()
)
tIPsecTsListRmtEntryMaxAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryMaxAddrType.setStatus("current")


class _TIPsecTsListRmtEntryMaxAddr_Type(InetAddress):
    """Custom type tIPsecTsListRmtEntryMaxAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TIPsecTsListRmtEntryMaxAddr_Type.__name__ = "InetAddress"
_TIPsecTsListRmtEntryMaxAddr_Object = MibTableColumn
tIPsecTsListRmtEntryMaxAddr = _TIPsecTsListRmtEntryMaxAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 7),
    _TIPsecTsListRmtEntryMaxAddr_Type()
)
tIPsecTsListRmtEntryMaxAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryMaxAddr.setStatus("current")


class _TIPsecTsListRmtEntryPfxAddrType_Type(InetAddressType):
    """Custom type tIPsecTsListRmtEntryPfxAddrType based on InetAddressType"""
    defaultValue = 0


_TIPsecTsListRmtEntryPfxAddrType_Type.__name__ = "InetAddressType"
_TIPsecTsListRmtEntryPfxAddrType_Object = MibTableColumn
tIPsecTsListRmtEntryPfxAddrType = _TIPsecTsListRmtEntryPfxAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 8),
    _TIPsecTsListRmtEntryPfxAddrType_Type()
)
tIPsecTsListRmtEntryPfxAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryPfxAddrType.setStatus("current")


class _TIPsecTsListRmtEntryPfxAddr_Type(InetAddress):
    """Custom type tIPsecTsListRmtEntryPfxAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TIPsecTsListRmtEntryPfxAddr_Type.__name__ = "InetAddress"
_TIPsecTsListRmtEntryPfxAddr_Object = MibTableColumn
tIPsecTsListRmtEntryPfxAddr = _TIPsecTsListRmtEntryPfxAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 9),
    _TIPsecTsListRmtEntryPfxAddr_Type()
)
tIPsecTsListRmtEntryPfxAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryPfxAddr.setStatus("current")


class _TIPsecTsListRmtEntryPfxLen_Type(InetAddressPrefixLength):
    """Custom type tIPsecTsListRmtEntryPfxLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TIPsecTsListRmtEntryPfxLen_Type.__name__ = "InetAddressPrefixLength"
_TIPsecTsListRmtEntryPfxLen_Object = MibTableColumn
tIPsecTsListRmtEntryPfxLen = _TIPsecTsListRmtEntryPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 10),
    _TIPsecTsListRmtEntryPfxLen_Type()
)
tIPsecTsListRmtEntryPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryPfxLen.setStatus("current")


class _TIPsecTsListRmtEntryMinPort_Type(InetPortNumber):
    """Custom type tIPsecTsListRmtEntryMinPort based on InetPortNumber"""
    defaultValue = 0


_TIPsecTsListRmtEntryMinPort_Type.__name__ = "InetPortNumber"
_TIPsecTsListRmtEntryMinPort_Object = MibTableColumn
tIPsecTsListRmtEntryMinPort = _TIPsecTsListRmtEntryMinPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 11),
    _TIPsecTsListRmtEntryMinPort_Type()
)
tIPsecTsListRmtEntryMinPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryMinPort.setStatus("current")


class _TIPsecTsListRmtEntryMaxPort_Type(InetPortNumber):
    """Custom type tIPsecTsListRmtEntryMaxPort based on InetPortNumber"""
    defaultValue = 65535


_TIPsecTsListRmtEntryMaxPort_Type.__name__ = "InetPortNumber"
_TIPsecTsListRmtEntryMaxPort_Object = MibTableColumn
tIPsecTsListRmtEntryMaxPort = _TIPsecTsListRmtEntryMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 12),
    _TIPsecTsListRmtEntryMaxPort_Type()
)
tIPsecTsListRmtEntryMaxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryMaxPort.setStatus("current")


class _TIPsecTsListRmtEntryMinMhType_Type(Unsigned32):
    """Custom type tIPsecTsListRmtEntryMinMhType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TIPsecTsListRmtEntryMinMhType_Type.__name__ = "Unsigned32"
_TIPsecTsListRmtEntryMinMhType_Object = MibTableColumn
tIPsecTsListRmtEntryMinMhType = _TIPsecTsListRmtEntryMinMhType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 13),
    _TIPsecTsListRmtEntryMinMhType_Type()
)
tIPsecTsListRmtEntryMinMhType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryMinMhType.setStatus("current")


class _TIPsecTsListRmtEntryMaxMhType_Type(Unsigned32):
    """Custom type tIPsecTsListRmtEntryMaxMhType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TIPsecTsListRmtEntryMaxMhType_Type.__name__ = "Unsigned32"
_TIPsecTsListRmtEntryMaxMhType_Object = MibTableColumn
tIPsecTsListRmtEntryMaxMhType = _TIPsecTsListRmtEntryMaxMhType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 14),
    _TIPsecTsListRmtEntryMaxMhType_Type()
)
tIPsecTsListRmtEntryMaxMhType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryMaxMhType.setStatus("current")


class _TIPsecTsListRmtEntryMinIcmpType_Type(Unsigned32):
    """Custom type tIPsecTsListRmtEntryMinIcmpType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TIPsecTsListRmtEntryMinIcmpType_Type.__name__ = "Unsigned32"
_TIPsecTsListRmtEntryMinIcmpType_Object = MibTableColumn
tIPsecTsListRmtEntryMinIcmpType = _TIPsecTsListRmtEntryMinIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 15),
    _TIPsecTsListRmtEntryMinIcmpType_Type()
)
tIPsecTsListRmtEntryMinIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryMinIcmpType.setStatus("current")


class _TIPsecTsListRmtEntryMaxIcmpType_Type(Unsigned32):
    """Custom type tIPsecTsListRmtEntryMaxIcmpType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TIPsecTsListRmtEntryMaxIcmpType_Type.__name__ = "Unsigned32"
_TIPsecTsListRmtEntryMaxIcmpType_Object = MibTableColumn
tIPsecTsListRmtEntryMaxIcmpType = _TIPsecTsListRmtEntryMaxIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 16),
    _TIPsecTsListRmtEntryMaxIcmpType_Type()
)
tIPsecTsListRmtEntryMaxIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryMaxIcmpType.setStatus("current")


class _TIPsecTsListRmtEntryMinIcmpCode_Type(Unsigned32):
    """Custom type tIPsecTsListRmtEntryMinIcmpCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TIPsecTsListRmtEntryMinIcmpCode_Type.__name__ = "Unsigned32"
_TIPsecTsListRmtEntryMinIcmpCode_Object = MibTableColumn
tIPsecTsListRmtEntryMinIcmpCode = _TIPsecTsListRmtEntryMinIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 17),
    _TIPsecTsListRmtEntryMinIcmpCode_Type()
)
tIPsecTsListRmtEntryMinIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryMinIcmpCode.setStatus("current")


class _TIPsecTsListRmtEntryMaxIcmpCode_Type(Unsigned32):
    """Custom type tIPsecTsListRmtEntryMaxIcmpCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TIPsecTsListRmtEntryMaxIcmpCode_Type.__name__ = "Unsigned32"
_TIPsecTsListRmtEntryMaxIcmpCode_Object = MibTableColumn
tIPsecTsListRmtEntryMaxIcmpCode = _TIPsecTsListRmtEntryMaxIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 18),
    _TIPsecTsListRmtEntryMaxIcmpCode_Type()
)
tIPsecTsListRmtEntryMaxIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryMaxIcmpCode.setStatus("current")


class _TIPsecTsListRmtEntryProtocolId_Type(Integer32):
    """Custom type tIPsecTsListRmtEntryProtocolId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TIPsecTsListRmtEntryProtocolId_Type.__name__ = "Integer32"
_TIPsecTsListRmtEntryProtocolId_Object = MibTableColumn
tIPsecTsListRmtEntryProtocolId = _TIPsecTsListRmtEntryProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 61, 1, 19),
    _TIPsecTsListRmtEntryProtocolId_Type()
)
tIPsecTsListRmtEntryProtocolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRmtEntryProtocolId.setStatus("current")
_TmnxIPsecLockoutClientTable_Object = MibTable
tmnxIPsecLockoutClientTable = _TmnxIPsecLockoutClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 62)
)
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientTable.setStatus("current")
_TmnxIPsecLockoutClientEntry_Object = MibTableRow
tmnxIPsecLockoutClientEntry = _TmnxIPsecLockoutClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 62, 1)
)
tmnxIPsecLockoutClientEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientRtrId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientLclGwAddrT"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientLclGwAddr"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientAddressTyp"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientPort"),
)
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientEntry.setStatus("current")
_TmnxIPsecLockoutClientRtrId_Type = TmnxVRtrID
_TmnxIPsecLockoutClientRtrId_Object = MibTableColumn
tmnxIPsecLockoutClientRtrId = _TmnxIPsecLockoutClientRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 62, 1, 1),
    _TmnxIPsecLockoutClientRtrId_Type()
)
tmnxIPsecLockoutClientRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientRtrId.setStatus("current")
_TmnxIPsecLockoutClientLclGwAddrT_Type = InetAddressType
_TmnxIPsecLockoutClientLclGwAddrT_Object = MibTableColumn
tmnxIPsecLockoutClientLclGwAddrT = _TmnxIPsecLockoutClientLclGwAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 62, 1, 2),
    _TmnxIPsecLockoutClientLclGwAddrT_Type()
)
tmnxIPsecLockoutClientLclGwAddrT.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientLclGwAddrT.setStatus("current")


class _TmnxIPsecLockoutClientLclGwAddr_Type(InetAddress):
    """Custom type tmnxIPsecLockoutClientLclGwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecLockoutClientLclGwAddr_Type.__name__ = "InetAddress"
_TmnxIPsecLockoutClientLclGwAddr_Object = MibTableColumn
tmnxIPsecLockoutClientLclGwAddr = _TmnxIPsecLockoutClientLclGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 62, 1, 3),
    _TmnxIPsecLockoutClientLclGwAddr_Type()
)
tmnxIPsecLockoutClientLclGwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientLclGwAddr.setStatus("current")
_TmnxIPsecLockoutClientAddressTyp_Type = InetAddressType
_TmnxIPsecLockoutClientAddressTyp_Object = MibTableColumn
tmnxIPsecLockoutClientAddressTyp = _TmnxIPsecLockoutClientAddressTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 62, 1, 4),
    _TmnxIPsecLockoutClientAddressTyp_Type()
)
tmnxIPsecLockoutClientAddressTyp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientAddressTyp.setStatus("current")


class _TmnxIPsecLockoutClientAddress_Type(InetAddress):
    """Custom type tmnxIPsecLockoutClientAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecLockoutClientAddress_Type.__name__ = "InetAddress"
_TmnxIPsecLockoutClientAddress_Object = MibTableColumn
tmnxIPsecLockoutClientAddress = _TmnxIPsecLockoutClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 62, 1, 5),
    _TmnxIPsecLockoutClientAddress_Type()
)
tmnxIPsecLockoutClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientAddress.setStatus("current")
_TmnxIPsecLockoutClientPort_Type = InetPortNumber
_TmnxIPsecLockoutClientPort_Object = MibTableColumn
tmnxIPsecLockoutClientPort = _TmnxIPsecLockoutClientPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 62, 1, 6),
    _TmnxIPsecLockoutClientPort_Type()
)
tmnxIPsecLockoutClientPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientPort.setStatus("current")
_TmnxIPsecLockoutClientStatus_Type = TruthValue
_TmnxIPsecLockoutClientStatus_Object = MibTableColumn
tmnxIPsecLockoutClientStatus = _TmnxIPsecLockoutClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 62, 1, 7),
    _TmnxIPsecLockoutClientStatus_Type()
)
tmnxIPsecLockoutClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientStatus.setStatus("current")
_TmnxIPsecLockoutClientFailAtempt_Type = Unsigned32
_TmnxIPsecLockoutClientFailAtempt_Object = MibTableColumn
tmnxIPsecLockoutClientFailAtempt = _TmnxIPsecLockoutClientFailAtempt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 62, 1, 8),
    _TmnxIPsecLockoutClientFailAtempt_Type()
)
tmnxIPsecLockoutClientFailAtempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientFailAtempt.setStatus("current")
_TmnxIPsecLockoutClientDroppedPkt_Type = Unsigned32
_TmnxIPsecLockoutClientDroppedPkt_Object = MibTableColumn
tmnxIPsecLockoutClientDroppedPkt = _TmnxIPsecLockoutClientDroppedPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 62, 1, 9),
    _TmnxIPsecLockoutClientDroppedPkt_Type()
)
tmnxIPsecLockoutClientDroppedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientDroppedPkt.setStatus("current")
_TmnxIPsecLockoutClientRemainTime_Type = Integer32
_TmnxIPsecLockoutClientRemainTime_Object = MibTableColumn
tmnxIPsecLockoutClientRemainTime = _TmnxIPsecLockoutClientRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 62, 1, 10),
    _TmnxIPsecLockoutClientRemainTime_Type()
)
tmnxIPsecLockoutClientRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientRemainTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecLockoutClientRemainTime.setUnits("seconds")
_TIPsecRUTnlDhcpLeaseStatTable_Object = MibTable
tIPsecRUTnlDhcpLeaseStatTable = _TIPsecRUTnlDhcpLeaseStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 63)
)
if mibBuilder.loadTexts:
    tIPsecRUTnlDhcpLeaseStatTable.setStatus("current")
_TIPsecRUTnlDhcpLeaseStatEntry_Object = MibTableRow
tIPsecRUTnlDhcpLeaseStatEntry = _TIPsecRUTnlDhcpLeaseStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 63, 1)
)
tIPsecRUTnlDhcpLeaseStatEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlPort"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlDhcpLeaseStatPrivAddT"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlDhcpLeaseStatPrivAddr"),
)
if mibBuilder.loadTexts:
    tIPsecRUTnlDhcpLeaseStatEntry.setStatus("current")
_TIPsecRUTnlDhcpLeaseStatPrivAddT_Type = InetAddressType
_TIPsecRUTnlDhcpLeaseStatPrivAddT_Object = MibTableColumn
tIPsecRUTnlDhcpLeaseStatPrivAddT = _TIPsecRUTnlDhcpLeaseStatPrivAddT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 63, 1, 1),
    _TIPsecRUTnlDhcpLeaseStatPrivAddT_Type()
)
tIPsecRUTnlDhcpLeaseStatPrivAddT.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUTnlDhcpLeaseStatPrivAddT.setStatus("current")


class _TIPsecRUTnlDhcpLeaseStatPrivAddr_Type(InetAddress):
    """Custom type tIPsecRUTnlDhcpLeaseStatPrivAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TIPsecRUTnlDhcpLeaseStatPrivAddr_Type.__name__ = "InetAddress"
_TIPsecRUTnlDhcpLeaseStatPrivAddr_Object = MibTableColumn
tIPsecRUTnlDhcpLeaseStatPrivAddr = _TIPsecRUTnlDhcpLeaseStatPrivAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 63, 1, 2),
    _TIPsecRUTnlDhcpLeaseStatPrivAddr_Type()
)
tIPsecRUTnlDhcpLeaseStatPrivAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUTnlDhcpLeaseStatPrivAddr.setStatus("current")
_TIPsecRUTnlDhcpLeaseStatSverAddT_Type = InetAddressType
_TIPsecRUTnlDhcpLeaseStatSverAddT_Object = MibTableColumn
tIPsecRUTnlDhcpLeaseStatSverAddT = _TIPsecRUTnlDhcpLeaseStatSverAddT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 63, 1, 3),
    _TIPsecRUTnlDhcpLeaseStatSverAddT_Type()
)
tIPsecRUTnlDhcpLeaseStatSverAddT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlDhcpLeaseStatSverAddT.setStatus("current")


class _TIPsecRUTnlDhcpLeaseStatSverAddr_Type(InetAddress):
    """Custom type tIPsecRUTnlDhcpLeaseStatSverAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TIPsecRUTnlDhcpLeaseStatSverAddr_Type.__name__ = "InetAddress"
_TIPsecRUTnlDhcpLeaseStatSverAddr_Object = MibTableColumn
tIPsecRUTnlDhcpLeaseStatSverAddr = _TIPsecRUTnlDhcpLeaseStatSverAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 63, 1, 4),
    _TIPsecRUTnlDhcpLeaseStatSverAddr_Type()
)
tIPsecRUTnlDhcpLeaseStatSverAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlDhcpLeaseStatSverAddr.setStatus("current")
_TIPsecRUTnlDhcpLeaseStatAcquirTm_Type = DateAndTime
_TIPsecRUTnlDhcpLeaseStatAcquirTm_Object = MibTableColumn
tIPsecRUTnlDhcpLeaseStatAcquirTm = _TIPsecRUTnlDhcpLeaseStatAcquirTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 63, 1, 5),
    _TIPsecRUTnlDhcpLeaseStatAcquirTm_Type()
)
tIPsecRUTnlDhcpLeaseStatAcquirTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlDhcpLeaseStatAcquirTm.setStatus("current")
_TIPsecRUTnlDhcpLeaseStatRenewTm_Type = DateAndTime
_TIPsecRUTnlDhcpLeaseStatRenewTm_Object = MibTableColumn
tIPsecRUTnlDhcpLeaseStatRenewTm = _TIPsecRUTnlDhcpLeaseStatRenewTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 63, 1, 6),
    _TIPsecRUTnlDhcpLeaseStatRenewTm_Type()
)
tIPsecRUTnlDhcpLeaseStatRenewTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlDhcpLeaseStatRenewTm.setStatus("current")
_TIPsecRUTnlDhcpLeaseStatRebindTm_Type = DateAndTime
_TIPsecRUTnlDhcpLeaseStatRebindTm_Object = MibTableColumn
tIPsecRUTnlDhcpLeaseStatRebindTm = _TIPsecRUTnlDhcpLeaseStatRebindTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 63, 1, 7),
    _TIPsecRUTnlDhcpLeaseStatRebindTm_Type()
)
tIPsecRUTnlDhcpLeaseStatRebindTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlDhcpLeaseStatRebindTm.setStatus("current")
_TIPsecRUTnlDhcpLeaseStatPrivPref_Type = DateAndTime
_TIPsecRUTnlDhcpLeaseStatPrivPref_Object = MibTableColumn
tIPsecRUTnlDhcpLeaseStatPrivPref = _TIPsecRUTnlDhcpLeaseStatPrivPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 63, 1, 8),
    _TIPsecRUTnlDhcpLeaseStatPrivPref_Type()
)
tIPsecRUTnlDhcpLeaseStatPrivPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlDhcpLeaseStatPrivPref.setStatus("current")
_TIPsecRUTnlDhcpLeaseStatPrivVald_Type = DateAndTime
_TIPsecRUTnlDhcpLeaseStatPrivVald_Object = MibTableColumn
tIPsecRUTnlDhcpLeaseStatPrivVald = _TIPsecRUTnlDhcpLeaseStatPrivVald_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 63, 1, 9),
    _TIPsecRUTnlDhcpLeaseStatPrivVald_Type()
)
tIPsecRUTnlDhcpLeaseStatPrivVald.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlDhcpLeaseStatPrivVald.setStatus("current")
_TIPsecClientDatabaseTableLstChgd_Type = TimeStamp
_TIPsecClientDatabaseTableLstChgd_Object = MibScalar
tIPsecClientDatabaseTableLstChgd = _TIPsecClientDatabaseTableLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 64),
    _TIPsecClientDatabaseTableLstChgd_Type()
)
tIPsecClientDatabaseTableLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecClientDatabaseTableLstChgd.setStatus("current")
_TIPsecClientDatabaseTable_Object = MibTable
tIPsecClientDatabaseTable = _TIPsecClientDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 65)
)
if mibBuilder.loadTexts:
    tIPsecClientDatabaseTable.setStatus("current")
_TIPsecClientDatabaseEntry_Object = MibTableRow
tIPsecClientDatabaseEntry = _TIPsecClientDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 65, 1)
)
tIPsecClientDatabaseEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecClientDatabaseName"),
)
if mibBuilder.loadTexts:
    tIPsecClientDatabaseEntry.setStatus("current")
_TIPsecClientDatabaseName_Type = TNamedItem
_TIPsecClientDatabaseName_Object = MibTableColumn
tIPsecClientDatabaseName = _TIPsecClientDatabaseName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 65, 1, 1),
    _TIPsecClientDatabaseName_Type()
)
tIPsecClientDatabaseName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecClientDatabaseName.setStatus("current")
_TIPsecClientDatabaseLastChanged_Type = TimeStamp
_TIPsecClientDatabaseLastChanged_Object = MibTableColumn
tIPsecClientDatabaseLastChanged = _TIPsecClientDatabaseLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 65, 1, 2),
    _TIPsecClientDatabaseLastChanged_Type()
)
tIPsecClientDatabaseLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecClientDatabaseLastChanged.setStatus("current")
_TIPsecClientDatabaseRowStatus_Type = RowStatus
_TIPsecClientDatabaseRowStatus_Object = MibTableColumn
tIPsecClientDatabaseRowStatus = _TIPsecClientDatabaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 65, 1, 3),
    _TIPsecClientDatabaseRowStatus_Type()
)
tIPsecClientDatabaseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDatabaseRowStatus.setStatus("current")


class _TIPsecClientDatabaseAdminState_Type(TmnxAdminState):
    """Custom type tIPsecClientDatabaseAdminState based on TmnxAdminState"""
    defaultValue = 3


_TIPsecClientDatabaseAdminState_Type.__name__ = "TmnxAdminState"
_TIPsecClientDatabaseAdminState_Object = MibTableColumn
tIPsecClientDatabaseAdminState = _TIPsecClientDatabaseAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 65, 1, 4),
    _TIPsecClientDatabaseAdminState_Type()
)
tIPsecClientDatabaseAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDatabaseAdminState.setStatus("current")


class _TIPsecClientDatabaseDescription_Type(TItemDescription):
    """Custom type tIPsecClientDatabaseDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TIPsecClientDatabaseDescription_Type.__name__ = "TItemDescription"
_TIPsecClientDatabaseDescription_Object = MibTableColumn
tIPsecClientDatabaseDescription = _TIPsecClientDatabaseDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 65, 1, 5),
    _TIPsecClientDatabaseDescription_Type()
)
tIPsecClientDatabaseDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDatabaseDescription.setStatus("current")


class _TIPsecClientDatabaseMatchType_Type(Bits):
    """Custom type tIPsecClientDatabaseMatchType based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("idi", 0),
          ("peerIpPrefix", 1))
    )

_TIPsecClientDatabaseMatchType_Type.__name__ = "Bits"
_TIPsecClientDatabaseMatchType_Object = MibTableColumn
tIPsecClientDatabaseMatchType = _TIPsecClientDatabaseMatchType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 65, 1, 6),
    _TIPsecClientDatabaseMatchType_Type()
)
tIPsecClientDatabaseMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDatabaseMatchType.setStatus("current")
_TIPsecClientDBClientTableLstChgd_Type = TimeStamp
_TIPsecClientDBClientTableLstChgd_Object = MibScalar
tIPsecClientDBClientTableLstChgd = _TIPsecClientDBClientTableLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 66),
    _TIPsecClientDBClientTableLstChgd_Type()
)
tIPsecClientDBClientTableLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecClientDBClientTableLstChgd.setStatus("current")
_TIPsecClientDBClientTable_Object = MibTable
tIPsecClientDBClientTable = _TIPsecClientDBClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67)
)
if mibBuilder.loadTexts:
    tIPsecClientDBClientTable.setStatus("current")
_TIPsecClientDBClientEntry_Object = MibTableRow
tIPsecClientDBClientEntry = _TIPsecClientDBClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1)
)
tIPsecClientDBClientEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecClientDatabaseName"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecClientDBClientIndex"),
)
if mibBuilder.loadTexts:
    tIPsecClientDBClientEntry.setStatus("current")


class _TIPsecClientDBClientIndex_Type(Unsigned32):
    """Custom type tIPsecClientDBClientIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8000),
    )


_TIPsecClientDBClientIndex_Type.__name__ = "Unsigned32"
_TIPsecClientDBClientIndex_Object = MibTableColumn
tIPsecClientDBClientIndex = _TIPsecClientDBClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 1),
    _TIPsecClientDBClientIndex_Type()
)
tIPsecClientDBClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecClientDBClientIndex.setStatus("current")
_TIPsecClientDBClientLastChanged_Type = TimeStamp
_TIPsecClientDBClientLastChanged_Object = MibTableColumn
tIPsecClientDBClientLastChanged = _TIPsecClientDBClientLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 2),
    _TIPsecClientDBClientLastChanged_Type()
)
tIPsecClientDBClientLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecClientDBClientLastChanged.setStatus("current")
_TIPsecClientDBClientRowStatus_Type = RowStatus
_TIPsecClientDBClientRowStatus_Object = MibTableColumn
tIPsecClientDBClientRowStatus = _TIPsecClientDBClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 3),
    _TIPsecClientDBClientRowStatus_Type()
)
tIPsecClientDBClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientRowStatus.setStatus("current")


class _TIPsecClientDBClientAdminState_Type(TmnxAdminState):
    """Custom type tIPsecClientDBClientAdminState based on TmnxAdminState"""
    defaultValue = 3


_TIPsecClientDBClientAdminState_Type.__name__ = "TmnxAdminState"
_TIPsecClientDBClientAdminState_Object = MibTableColumn
tIPsecClientDBClientAdminState = _TIPsecClientDBClientAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 4),
    _TIPsecClientDBClientAdminState_Type()
)
tIPsecClientDBClientAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientAdminState.setStatus("current")


class _TIPsecClientDBClientName_Type(TNamedItemOrEmpty):
    """Custom type tIPsecClientDBClientName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TIPsecClientDBClientName_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecClientDBClientName_Object = MibTableColumn
tIPsecClientDBClientName = _TIPsecClientDBClientName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 5),
    _TIPsecClientDBClientName_Type()
)
tIPsecClientDBClientName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientName.setStatus("current")


class _TIPsecClientDBClientIdIdiType_Type(Integer32):
    """Custom type tIPsecClientDBClientIdIdiType based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("any", 2),
          ("ipv4Pfx", 3),
          ("ipv4PfxAny", 4),
          ("ipv6Pfx", 5),
          ("ipv6PfxAny", 6),
          ("fqdn", 7),
          ("fqdnSuffix", 8),
          ("rfc822", 9),
          ("rfc822Suffix", 10))
    )


_TIPsecClientDBClientIdIdiType_Type.__name__ = "Integer32"
_TIPsecClientDBClientIdIdiType_Object = MibTableColumn
tIPsecClientDBClientIdIdiType = _TIPsecClientDBClientIdIdiType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 6),
    _TIPsecClientDBClientIdIdiType_Type()
)
tIPsecClientDBClientIdIdiType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientIdIdiType.setStatus("current")


class _TIPsecClientDBClientIdIdiValue_Type(DisplayString):
    """Custom type tIPsecClientDBClientIdIdiValue based on DisplayString"""
    defaultHexValue = ""


_TIPsecClientDBClientIdIdiValue_Type.__name__ = "DisplayString"
_TIPsecClientDBClientIdIdiValue_Object = MibTableColumn
tIPsecClientDBClientIdIdiValue = _TIPsecClientDBClientIdIdiValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 7),
    _TIPsecClientDBClientIdIdiValue_Type()
)
tIPsecClientDBClientIdIdiValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientIdIdiValue.setStatus("current")


class _TIPsecClientDBClientIdPeer4PfAny_Type(TruthValue):
    """Custom type tIPsecClientDBClientIdPeer4PfAny based on TruthValue"""
    defaultValue = 2


_TIPsecClientDBClientIdPeer4PfAny_Type.__name__ = "TruthValue"
_TIPsecClientDBClientIdPeer4PfAny_Object = MibTableColumn
tIPsecClientDBClientIdPeer4PfAny = _TIPsecClientDBClientIdPeer4PfAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 8),
    _TIPsecClientDBClientIdPeer4PfAny_Type()
)
tIPsecClientDBClientIdPeer4PfAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientIdPeer4PfAny.setStatus("current")


class _TIPsecClientDBClientIdPeer6PfAny_Type(TruthValue):
    """Custom type tIPsecClientDBClientIdPeer6PfAny based on TruthValue"""
    defaultValue = 2


_TIPsecClientDBClientIdPeer6PfAny_Type.__name__ = "TruthValue"
_TIPsecClientDBClientIdPeer6PfAny_Object = MibTableColumn
tIPsecClientDBClientIdPeer6PfAny = _TIPsecClientDBClientIdPeer6PfAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 9),
    _TIPsecClientDBClientIdPeer6PfAny_Type()
)
tIPsecClientDBClientIdPeer6PfAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientIdPeer6PfAny.setStatus("current")


class _TIPsecClientDBClientIdPeerPfxTyp_Type(InetAddressType):
    """Custom type tIPsecClientDBClientIdPeerPfxTyp based on InetAddressType"""
    defaultValue = 0


_TIPsecClientDBClientIdPeerPfxTyp_Type.__name__ = "InetAddressType"
_TIPsecClientDBClientIdPeerPfxTyp_Object = MibTableColumn
tIPsecClientDBClientIdPeerPfxTyp = _TIPsecClientDBClientIdPeerPfxTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 10),
    _TIPsecClientDBClientIdPeerPfxTyp_Type()
)
tIPsecClientDBClientIdPeerPfxTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientIdPeerPfxTyp.setStatus("current")


class _TIPsecClientDBClientIdPeerPfx_Type(InetAddress):
    """Custom type tIPsecClientDBClientIdPeerPfx based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TIPsecClientDBClientIdPeerPfx_Type.__name__ = "InetAddress"
_TIPsecClientDBClientIdPeerPfx_Object = MibTableColumn
tIPsecClientDBClientIdPeerPfx = _TIPsecClientDBClientIdPeerPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 11),
    _TIPsecClientDBClientIdPeerPfx_Type()
)
tIPsecClientDBClientIdPeerPfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientIdPeerPfx.setStatus("current")


class _TIPsecClientDBClientIdPeerPfxLen_Type(InetAddressPrefixLength):
    """Custom type tIPsecClientDBClientIdPeerPfxLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TIPsecClientDBClientIdPeerPfxLen_Type.__name__ = "InetAddressPrefixLength"
_TIPsecClientDBClientIdPeerPfxLen_Object = MibTableColumn
tIPsecClientDBClientIdPeerPfxLen = _TIPsecClientDBClientIdPeerPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 12),
    _TIPsecClientDBClientIdPeerPfxLen_Type()
)
tIPsecClientDBClientIdPeerPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientIdPeerPfxLen.setStatus("current")


class _TIPsecClientDBClientTnlTempltId_Type(TmnxIPsecTunnelTemplateIdOrZero):
    """Custom type tIPsecClientDBClientTnlTempltId based on TmnxIPsecTunnelTemplateIdOrZero"""
    defaultValue = 0


_TIPsecClientDBClientTnlTempltId_Type.__name__ = "TmnxIPsecTunnelTemplateIdOrZero"
_TIPsecClientDBClientTnlTempltId_Object = MibTableColumn
tIPsecClientDBClientTnlTempltId = _TIPsecClientDBClientTnlTempltId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 13),
    _TIPsecClientDBClientTnlTempltId_Type()
)
tIPsecClientDBClientTnlTempltId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientTnlTempltId.setStatus("current")


class _TIPsecClientDBClientPrivateSvcId_Type(TmnxServId):
    """Custom type tIPsecClientDBClientPrivateSvcId based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_TIPsecClientDBClientPrivateSvcId_Type.__name__ = "TmnxServId"
_TIPsecClientDBClientPrivateSvcId_Object = MibTableColumn
tIPsecClientDBClientPrivateSvcId = _TIPsecClientDBClientPrivateSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 14),
    _TIPsecClientDBClientPrivateSvcId_Type()
)
tIPsecClientDBClientPrivateSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientPrivateSvcId.setStatus("current")


class _TIPsecClientDBClientPrivIfName_Type(TNamedItemOrEmpty):
    """Custom type tIPsecClientDBClientPrivIfName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TIPsecClientDBClientPrivIfName_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecClientDBClientPrivIfName_Object = MibTableColumn
tIPsecClientDBClientPrivIfName = _TIPsecClientDBClientPrivIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 15),
    _TIPsecClientDBClientPrivIfName_Type()
)
tIPsecClientDBClientPrivIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientPrivIfName.setStatus("current")


class _TIPsecClientDBClientTsListName_Type(TNamedItemOrEmpty):
    """Custom type tIPsecClientDBClientTsListName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TIPsecClientDBClientTsListName_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecClientDBClientTsListName_Object = MibTableColumn
tIPsecClientDBClientTsListName = _TIPsecClientDBClientTsListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 16),
    _TIPsecClientDBClientTsListName_Type()
)
tIPsecClientDBClientTsListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientTsListName.setStatus("current")


class _TIPsecClientDBClientPreSharedKey_Type(OctetString):
    """Custom type tIPsecClientDBClientPreSharedKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TIPsecClientDBClientPreSharedKey_Type.__name__ = "OctetString"
_TIPsecClientDBClientPreSharedKey_Object = MibTableColumn
tIPsecClientDBClientPreSharedKey = _TIPsecClientDBClientPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 17),
    _TIPsecClientDBClientPreSharedKey_Type()
)
tIPsecClientDBClientPreSharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientPreSharedKey.setStatus("current")


class _TIPsecClientDBClientPrivateSvcNm_Type(TLNamedItemOrEmpty):
    """Custom type tIPsecClientDBClientPrivateSvcNm based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPsecClientDBClientPrivateSvcNm_Type.__name__ = "TLNamedItemOrEmpty"
_TIPsecClientDBClientPrivateSvcNm_Object = MibTableColumn
tIPsecClientDBClientPrivateSvcNm = _TIPsecClientDBClientPrivateSvcNm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 67, 1, 18),
    _TIPsecClientDBClientPrivateSvcNm_Type()
)
tIPsecClientDBClientPrivateSvcNm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecClientDBClientPrivateSvcNm.setStatus("current")
_TmnxIPsecIkeTransformTableLstChg_Type = TimeStamp
_TmnxIPsecIkeTransformTableLstChg_Object = MibScalar
tmnxIPsecIkeTransformTableLstChg = _TmnxIPsecIkeTransformTableLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 68),
    _TmnxIPsecIkeTransformTableLstChg_Type()
)
tmnxIPsecIkeTransformTableLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformTableLstChg.setStatus("current")
_TmnxIPsecIkeTransformTable_Object = MibTable
tmnxIPsecIkeTransformTable = _TmnxIPsecIkeTransformTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 69)
)
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformTable.setStatus("current")
_TmnxIPsecIkeTransformEntry_Object = MibTableRow
tmnxIPsecIkeTransformEntry = _TmnxIPsecIkeTransformEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 69, 1)
)
tmnxIPsecIkeTransformEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecIkeTransformId"),
)
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformEntry.setStatus("current")
_TmnxIPsecIkeTransformId_Type = TmnxIPsecIkeTransformId
_TmnxIPsecIkeTransformId_Object = MibTableColumn
tmnxIPsecIkeTransformId = _TmnxIPsecIkeTransformId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 69, 1, 1),
    _TmnxIPsecIkeTransformId_Type()
)
tmnxIPsecIkeTransformId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformId.setStatus("current")
_TmnxIPsecIkeTransformRowStatus_Type = RowStatus
_TmnxIPsecIkeTransformRowStatus_Object = MibTableColumn
tmnxIPsecIkeTransformRowStatus = _TmnxIPsecIkeTransformRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 69, 1, 2),
    _TmnxIPsecIkeTransformRowStatus_Type()
)
tmnxIPsecIkeTransformRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformRowStatus.setStatus("current")
_TmnxIPsecIkeTransformLastChange_Type = TimeStamp
_TmnxIPsecIkeTransformLastChange_Object = MibTableColumn
tmnxIPsecIkeTransformLastChange = _TmnxIPsecIkeTransformLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 69, 1, 3),
    _TmnxIPsecIkeTransformLastChange_Type()
)
tmnxIPsecIkeTransformLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformLastChange.setStatus("current")


class _TmnxIPsecIkeTransformAuthAlg_Type(Integer32):
    """Custom type tmnxIPsecIkeTransformAuthAlg based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("sha1", 3),
          ("sha256", 4),
          ("sha384", 5),
          ("sha512", 6),
          ("aesXcbc", 7),
          ("authEncryption", 8))
    )


_TmnxIPsecIkeTransformAuthAlg_Type.__name__ = "Integer32"
_TmnxIPsecIkeTransformAuthAlg_Object = MibTableColumn
tmnxIPsecIkeTransformAuthAlg = _TmnxIPsecIkeTransformAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 69, 1, 4),
    _TmnxIPsecIkeTransformAuthAlg_Type()
)
tmnxIPsecIkeTransformAuthAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformAuthAlg.setStatus("current")


class _TmnxIPsecIkeTransformEncrAlg_Type(Integer32):
    """Custom type tmnxIPsecIkeTransformEncrAlg based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              9,
              13,
              15)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("des3", 3),
          ("aes128", 4),
          ("aes192", 5),
          ("aes256", 6),
          ("aes128Gcm8", 7),
          ("aes128Gcm16", 9),
          ("aes256Gcm8", 13),
          ("aes256Gcm16", 15))
    )


_TmnxIPsecIkeTransformEncrAlg_Type.__name__ = "Integer32"
_TmnxIPsecIkeTransformEncrAlg_Object = MibTableColumn
tmnxIPsecIkeTransformEncrAlg = _TmnxIPsecIkeTransformEncrAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 69, 1, 5),
    _TmnxIPsecIkeTransformEncrAlg_Type()
)
tmnxIPsecIkeTransformEncrAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformEncrAlg.setStatus("current")


class _TmnxIPsecIkeTransformDhGroup_Type(TmnxIkePolicyDHGroup):
    """Custom type tmnxIPsecIkeTransformDhGroup based on TmnxIkePolicyDHGroup"""
    defaultValue = 2


_TmnxIPsecIkeTransformDhGroup_Type.__name__ = "TmnxIkePolicyDHGroup"
_TmnxIPsecIkeTransformDhGroup_Object = MibTableColumn
tmnxIPsecIkeTransformDhGroup = _TmnxIPsecIkeTransformDhGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 69, 1, 6),
    _TmnxIPsecIkeTransformDhGroup_Type()
)
tmnxIPsecIkeTransformDhGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformDhGroup.setStatus("current")


class _TmnxIPsecIkeTransformIsakmpLifeT_Type(Unsigned32):
    """Custom type tmnxIPsecIkeTransformIsakmpLifeT based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 31536000),
    )


_TmnxIPsecIkeTransformIsakmpLifeT_Type.__name__ = "Unsigned32"
_TmnxIPsecIkeTransformIsakmpLifeT_Object = MibTableColumn
tmnxIPsecIkeTransformIsakmpLifeT = _TmnxIPsecIkeTransformIsakmpLifeT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 69, 1, 7),
    _TmnxIPsecIkeTransformIsakmpLifeT_Type()
)
tmnxIPsecIkeTransformIsakmpLifeT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformIsakmpLifeT.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformIsakmpLifeT.setUnits("seconds")


class _TmnxIPsecIkeTransformPrfAlg_Type(Integer32):
    """Custom type tmnxIPsecIkeTransformPrfAlg based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("sha1", 3),
          ("sha256", 4),
          ("sha384", 5),
          ("sha512", 6),
          ("aesXcbc", 7),
          ("sameAsAuth", 8))
    )


_TmnxIPsecIkeTransformPrfAlg_Type.__name__ = "Integer32"
_TmnxIPsecIkeTransformPrfAlg_Object = MibTableColumn
tmnxIPsecIkeTransformPrfAlg = _TmnxIPsecIkeTransformPrfAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 69, 1, 8),
    _TmnxIPsecIkeTransformPrfAlg_Type()
)
tmnxIPsecIkeTransformPrfAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformPrfAlg.setStatus("current")
_TmnxIkePlcyIkeTransformTbLstChg_Type = TimeStamp
_TmnxIkePlcyIkeTransformTbLstChg_Object = MibScalar
tmnxIkePlcyIkeTransformTbLstChg = _TmnxIkePlcyIkeTransformTbLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 70),
    _TmnxIkePlcyIkeTransformTbLstChg_Type()
)
tmnxIkePlcyIkeTransformTbLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIkePlcyIkeTransformTbLstChg.setStatus("current")
_TmnxIkePlcyIkeTransformTable_Object = MibTable
tmnxIkePlcyIkeTransformTable = _TmnxIkePlcyIkeTransformTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 71)
)
if mibBuilder.loadTexts:
    tmnxIkePlcyIkeTransformTable.setStatus("current")
_TmnxIkePlcyIkeTransformEntry_Object = MibTableRow
tmnxIkePlcyIkeTransformEntry = _TmnxIkePlcyIkeTransformEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 71, 1)
)
tmnxIkePlcyIkeTransformEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tmnxIkePolicyId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIkePlcyIkeTransformIndex"),
)
if mibBuilder.loadTexts:
    tmnxIkePlcyIkeTransformEntry.setStatus("current")


class _TmnxIkePlcyIkeTransformIndex_Type(Unsigned32):
    """Custom type tmnxIkePlcyIkeTransformIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxIkePlcyIkeTransformIndex_Type.__name__ = "Unsigned32"
_TmnxIkePlcyIkeTransformIndex_Object = MibTableColumn
tmnxIkePlcyIkeTransformIndex = _TmnxIkePlcyIkeTransformIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 71, 1, 1),
    _TmnxIkePlcyIkeTransformIndex_Type()
)
tmnxIkePlcyIkeTransformIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIkePlcyIkeTransformIndex.setStatus("current")
_TmnxIkePlcyIkeTransformLstChange_Type = TimeStamp
_TmnxIkePlcyIkeTransformLstChange_Object = MibTableColumn
tmnxIkePlcyIkeTransformLstChange = _TmnxIkePlcyIkeTransformLstChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 71, 1, 2),
    _TmnxIkePlcyIkeTransformLstChange_Type()
)
tmnxIkePlcyIkeTransformLstChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIkePlcyIkeTransformLstChange.setStatus("current")


class _TmnxIkePlcyIkeTransformId_Type(TmnxIPsecIkeTransformIdOrZero):
    """Custom type tmnxIkePlcyIkeTransformId based on TmnxIPsecIkeTransformIdOrZero"""
    defaultValue = 0


_TmnxIkePlcyIkeTransformId_Type.__name__ = "TmnxIPsecIkeTransformIdOrZero"
_TmnxIkePlcyIkeTransformId_Object = MibTableColumn
tmnxIkePlcyIkeTransformId = _TmnxIkePlcyIkeTransformId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 71, 1, 3),
    _TmnxIkePlcyIkeTransformId_Type()
)
tmnxIkePlcyIkeTransformId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIkePlcyIkeTransformId.setStatus("current")
_TmnxIPsecGWHistStatsTable_Object = MibTable
tmnxIPsecGWHistStatsTable = _TmnxIPsecGWHistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 72)
)
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsTable.setStatus("current")
_TmnxIPsecGWHistStatsEntry_Object = MibTableRow
tmnxIPsecGWHistStatsEntry = _TmnxIPsecGWHistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 72, 1)
)
tmnxIPsecGWHistStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecGWHistStatsType"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecGWHistStatsIntvIdx"),
)
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsEntry.setStatus("current")
_TmnxIPsecGWHistStatsType_Type = TmnxIPsecHistStatsType
_TmnxIPsecGWHistStatsType_Object = MibTableColumn
tmnxIPsecGWHistStatsType = _TmnxIPsecGWHistStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 72, 1, 1),
    _TmnxIPsecGWHistStatsType_Type()
)
tmnxIPsecGWHistStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsType.setStatus("current")
_TmnxIPsecGWHistStatsIntvIdx_Type = Unsigned32
_TmnxIPsecGWHistStatsIntvIdx_Object = MibTableColumn
tmnxIPsecGWHistStatsIntvIdx = _TmnxIPsecGWHistStatsIntvIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 72, 1, 2),
    _TmnxIPsecGWHistStatsIntvIdx_Type()
)
tmnxIPsecGWHistStatsIntvIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsIntvIdx.setStatus("current")
_TmnxIPsecGWHistStatsValue64_Type = CounterBasedGauge64
_TmnxIPsecGWHistStatsValue64_Object = MibTableColumn
tmnxIPsecGWHistStatsValue64 = _TmnxIPsecGWHistStatsValue64_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 72, 1, 3),
    _TmnxIPsecGWHistStatsValue64_Type()
)
tmnxIPsecGWHistStatsValue64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsValue64.setStatus("current")
_TmnxIPsecGWHistStatsValue32_Type = Integer32
_TmnxIPsecGWHistStatsValue32_Object = MibTableColumn
tmnxIPsecGWHistStatsValue32 = _TmnxIPsecGWHistStatsValue32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 72, 1, 4),
    _TmnxIPsecGWHistStatsValue32_Type()
)
tmnxIPsecGWHistStatsValue32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsValue32.setStatus("current")
_TmnxIPsecGWHistStatsIntvStTm_Type = DateAndTime
_TmnxIPsecGWHistStatsIntvStTm_Object = MibTableColumn
tmnxIPsecGWHistStatsIntvStTm = _TmnxIPsecGWHistStatsIntvStTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 72, 1, 5),
    _TmnxIPsecGWHistStatsIntvStTm_Type()
)
tmnxIPsecGWHistStatsIntvStTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsIntvStTm.setStatus("current")
_TmnxIPsecGWHistStatsIntvDur_Type = Unsigned32
_TmnxIPsecGWHistStatsIntvDur_Object = MibTableColumn
tmnxIPsecGWHistStatsIntvDur = _TmnxIPsecGWHistStatsIntvDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 72, 1, 6),
    _TmnxIPsecGWHistStatsIntvDur_Type()
)
tmnxIPsecGWHistStatsIntvDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsIntvDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsIntvDur.setUnits("seconds")
_TmnxIPsecGWHistStatsFstFTm_Type = DateAndTime
_TmnxIPsecGWHistStatsFstFTm_Object = MibTableColumn
tmnxIPsecGWHistStatsFstFTm = _TmnxIPsecGWHistStatsFstFTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 72, 1, 7),
    _TmnxIPsecGWHistStatsFstFTm_Type()
)
tmnxIPsecGWHistStatsFstFTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsFstFTm.setStatus("current")


class _TmnxIPsecGWHistStatsFstFDesc_Type(TItemLongDescription):
    """Custom type tmnxIPsecGWHistStatsFstFDesc based on TItemLongDescription"""
    subtypeSpec = TItemLongDescription.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_TmnxIPsecGWHistStatsFstFDesc_Type.__name__ = "TItemLongDescription"
_TmnxIPsecGWHistStatsFstFDesc_Object = MibTableColumn
tmnxIPsecGWHistStatsFstFDesc = _TmnxIPsecGWHistStatsFstFDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 72, 1, 8),
    _TmnxIPsecGWHistStatsFstFDesc_Type()
)
tmnxIPsecGWHistStatsFstFDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsFstFDesc.setStatus("current")
_TmnxIPsecGWHistStatsLstFTm_Type = DateAndTime
_TmnxIPsecGWHistStatsLstFTm_Object = MibTableColumn
tmnxIPsecGWHistStatsLstFTm = _TmnxIPsecGWHistStatsLstFTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 72, 1, 9),
    _TmnxIPsecGWHistStatsLstFTm_Type()
)
tmnxIPsecGWHistStatsLstFTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsLstFTm.setStatus("current")


class _TmnxIPsecGWHistStatsLstFDesc_Type(TItemLongDescription):
    """Custom type tmnxIPsecGWHistStatsLstFDesc based on TItemLongDescription"""
    subtypeSpec = TItemLongDescription.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_TmnxIPsecGWHistStatsLstFDesc_Type.__name__ = "TItemLongDescription"
_TmnxIPsecGWHistStatsLstFDesc_Object = MibTableColumn
tmnxIPsecGWHistStatsLstFDesc = _TmnxIPsecGWHistStatsLstFDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 72, 1, 10),
    _TmnxIPsecGWHistStatsLstFDesc_Type()
)
tmnxIPsecGWHistStatsLstFDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWHistStatsLstFDesc.setStatus("current")
_TmnxIPsecIsaHistStatsTable_Object = MibTable
tmnxIPsecIsaHistStatsTable = _TmnxIPsecIsaHistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 73)
)
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsTable.setStatus("current")
_TmnxIPsecIsaHistStatsEntry_Object = MibTableRow
tmnxIPsecIsaHistStatsEntry = _TmnxIPsecIsaHistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 73, 1)
)
tmnxIPsecIsaHistStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecIsaHistStatsType"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecIsaHistStatsIntvIdx"),
)
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsEntry.setStatus("current")
_TmnxIPsecIsaHistStatsType_Type = TmnxIPsecHistStatsType
_TmnxIPsecIsaHistStatsType_Object = MibTableColumn
tmnxIPsecIsaHistStatsType = _TmnxIPsecIsaHistStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 73, 1, 1),
    _TmnxIPsecIsaHistStatsType_Type()
)
tmnxIPsecIsaHistStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsType.setStatus("current")
_TmnxIPsecIsaHistStatsIntvIdx_Type = Unsigned32
_TmnxIPsecIsaHistStatsIntvIdx_Object = MibTableColumn
tmnxIPsecIsaHistStatsIntvIdx = _TmnxIPsecIsaHistStatsIntvIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 73, 1, 2),
    _TmnxIPsecIsaHistStatsIntvIdx_Type()
)
tmnxIPsecIsaHistStatsIntvIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsIntvIdx.setStatus("current")
_TmnxIPsecIsaHistStatsValue64_Type = CounterBasedGauge64
_TmnxIPsecIsaHistStatsValue64_Object = MibTableColumn
tmnxIPsecIsaHistStatsValue64 = _TmnxIPsecIsaHistStatsValue64_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 73, 1, 3),
    _TmnxIPsecIsaHistStatsValue64_Type()
)
tmnxIPsecIsaHistStatsValue64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsValue64.setStatus("current")
_TmnxIPsecIsaHistStatsValue32_Type = Integer32
_TmnxIPsecIsaHistStatsValue32_Object = MibTableColumn
tmnxIPsecIsaHistStatsValue32 = _TmnxIPsecIsaHistStatsValue32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 73, 1, 4),
    _TmnxIPsecIsaHistStatsValue32_Type()
)
tmnxIPsecIsaHistStatsValue32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsValue32.setStatus("current")
_TmnxIPsecIsaHistStatsIntvStTm_Type = DateAndTime
_TmnxIPsecIsaHistStatsIntvStTm_Object = MibTableColumn
tmnxIPsecIsaHistStatsIntvStTm = _TmnxIPsecIsaHistStatsIntvStTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 73, 1, 5),
    _TmnxIPsecIsaHistStatsIntvStTm_Type()
)
tmnxIPsecIsaHistStatsIntvStTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsIntvStTm.setStatus("current")
_TmnxIPsecIsaHistStatsIntvDur_Type = Unsigned32
_TmnxIPsecIsaHistStatsIntvDur_Object = MibTableColumn
tmnxIPsecIsaHistStatsIntvDur = _TmnxIPsecIsaHistStatsIntvDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 73, 1, 6),
    _TmnxIPsecIsaHistStatsIntvDur_Type()
)
tmnxIPsecIsaHistStatsIntvDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsIntvDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsIntvDur.setUnits("seconds")
_TmnxIPsecIsaHistStatsFstFTm_Type = DateAndTime
_TmnxIPsecIsaHistStatsFstFTm_Object = MibTableColumn
tmnxIPsecIsaHistStatsFstFTm = _TmnxIPsecIsaHistStatsFstFTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 73, 1, 7),
    _TmnxIPsecIsaHistStatsFstFTm_Type()
)
tmnxIPsecIsaHistStatsFstFTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsFstFTm.setStatus("current")


class _TmnxIPsecIsaHistStatsFstFDesc_Type(TItemLongDescription):
    """Custom type tmnxIPsecIsaHistStatsFstFDesc based on TItemLongDescription"""
    subtypeSpec = TItemLongDescription.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_TmnxIPsecIsaHistStatsFstFDesc_Type.__name__ = "TItemLongDescription"
_TmnxIPsecIsaHistStatsFstFDesc_Object = MibTableColumn
tmnxIPsecIsaHistStatsFstFDesc = _TmnxIPsecIsaHistStatsFstFDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 73, 1, 8),
    _TmnxIPsecIsaHistStatsFstFDesc_Type()
)
tmnxIPsecIsaHistStatsFstFDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsFstFDesc.setStatus("current")
_TmnxIPsecIsaHistStatsLstFTm_Type = DateAndTime
_TmnxIPsecIsaHistStatsLstFTm_Object = MibTableColumn
tmnxIPsecIsaHistStatsLstFTm = _TmnxIPsecIsaHistStatsLstFTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 73, 1, 9),
    _TmnxIPsecIsaHistStatsLstFTm_Type()
)
tmnxIPsecIsaHistStatsLstFTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsLstFTm.setStatus("current")


class _TmnxIPsecIsaHistStatsLstFDesc_Type(TItemLongDescription):
    """Custom type tmnxIPsecIsaHistStatsLstFDesc based on TItemLongDescription"""
    subtypeSpec = TItemLongDescription.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_TmnxIPsecIsaHistStatsLstFDesc_Type.__name__ = "TItemLongDescription"
_TmnxIPsecIsaHistStatsLstFDesc_Object = MibTableColumn
tmnxIPsecIsaHistStatsLstFDesc = _TmnxIPsecIsaHistStatsLstFDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 73, 1, 10),
    _TmnxIPsecIsaHistStatsLstFDesc_Type()
)
tmnxIPsecIsaHistStatsLstFDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaHistStatsLstFDesc.setStatus("current")
_TmnxIPsecSvcLevelCfgTableLastChg_Type = TimeStamp
_TmnxIPsecSvcLevelCfgTableLastChg_Object = MibScalar
tmnxIPsecSvcLevelCfgTableLastChg = _TmnxIPsecSvcLevelCfgTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 74),
    _TmnxIPsecSvcLevelCfgTableLastChg_Type()
)
tmnxIPsecSvcLevelCfgTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSvcLevelCfgTableLastChg.setStatus("current")
_TmnxIPsecSvcLevelCfgTable_Object = MibTable
tmnxIPsecSvcLevelCfgTable = _TmnxIPsecSvcLevelCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 75)
)
if mibBuilder.loadTexts:
    tmnxIPsecSvcLevelCfgTable.setStatus("current")
_TmnxIPsecSvcLevelCfgEntry_Object = MibTableRow
tmnxIPsecSvcLevelCfgEntry = _TmnxIPsecSvcLevelCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 75, 1)
)
tmnxIPsecSvcLevelCfgEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tmnxIPsecSvcLevelCfgEntry.setStatus("current")


class _TmnxIPsecSvcLevelCfgRsvRtrOvrd_Type(TruthValue):
    """Custom type tmnxIPsecSvcLevelCfgRsvRtrOvrd based on TruthValue"""
    defaultValue = 2


_TmnxIPsecSvcLevelCfgRsvRtrOvrd_Type.__name__ = "TruthValue"
_TmnxIPsecSvcLevelCfgRsvRtrOvrd_Object = MibTableColumn
tmnxIPsecSvcLevelCfgRsvRtrOvrd = _TmnxIPsecSvcLevelCfgRsvRtrOvrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 75, 1, 1),
    _TmnxIPsecSvcLevelCfgRsvRtrOvrd_Type()
)
tmnxIPsecSvcLevelCfgRsvRtrOvrd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecSvcLevelCfgRsvRtrOvrd.setStatus("obsolete")


class _TmnxIPsecSvcLevelCfgRROvrdType_Type(Integer32):
    """Custom type tmnxIPsecSvcLevelCfgRROvrdType based on Integer32"""
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
          ("sameIdi", 1),
          ("anyIdi", 2))
    )


_TmnxIPsecSvcLevelCfgRROvrdType_Type.__name__ = "Integer32"
_TmnxIPsecSvcLevelCfgRROvrdType_Object = MibTableColumn
tmnxIPsecSvcLevelCfgRROvrdType = _TmnxIPsecSvcLevelCfgRROvrdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 75, 1, 2),
    _TmnxIPsecSvcLevelCfgRROvrdType_Type()
)
tmnxIPsecSvcLevelCfgRROvrdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecSvcLevelCfgRROvrdType.setStatus("current")
_TmnxIPsecTnlGrpHistStatsTable_Object = MibTable
tmnxIPsecTnlGrpHistStatsTable = _TmnxIPsecTnlGrpHistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 76)
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsTable.setStatus("current")
_TmnxIPsecTnlGrpHistStatsEntry_Object = MibTableRow
tmnxIPsecTnlGrpHistStatsEntry = _TmnxIPsecTnlGrpHistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 76, 1)
)
tmnxIPsecTnlGrpHistStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTnlGrpHistStatsType"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTnlGrpHistStatsIntvIdx"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsEntry.setStatus("current")
_TmnxIPsecTnlGrpHistStatsType_Type = TmnxIPsecHistStatsType
_TmnxIPsecTnlGrpHistStatsType_Object = MibTableColumn
tmnxIPsecTnlGrpHistStatsType = _TmnxIPsecTnlGrpHistStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 76, 1, 1),
    _TmnxIPsecTnlGrpHistStatsType_Type()
)
tmnxIPsecTnlGrpHistStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsType.setStatus("current")
_TmnxIPsecTnlGrpHistStatsIntvIdx_Type = Unsigned32
_TmnxIPsecTnlGrpHistStatsIntvIdx_Object = MibTableColumn
tmnxIPsecTnlGrpHistStatsIntvIdx = _TmnxIPsecTnlGrpHistStatsIntvIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 76, 1, 2),
    _TmnxIPsecTnlGrpHistStatsIntvIdx_Type()
)
tmnxIPsecTnlGrpHistStatsIntvIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsIntvIdx.setStatus("current")
_TmnxIPsecTnlGrpHistStatsValue64_Type = CounterBasedGauge64
_TmnxIPsecTnlGrpHistStatsValue64_Object = MibTableColumn
tmnxIPsecTnlGrpHistStatsValue64 = _TmnxIPsecTnlGrpHistStatsValue64_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 76, 1, 3),
    _TmnxIPsecTnlGrpHistStatsValue64_Type()
)
tmnxIPsecTnlGrpHistStatsValue64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsValue64.setStatus("current")
_TmnxIPsecTnlGrpHistStatsValue32_Type = Integer32
_TmnxIPsecTnlGrpHistStatsValue32_Object = MibTableColumn
tmnxIPsecTnlGrpHistStatsValue32 = _TmnxIPsecTnlGrpHistStatsValue32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 76, 1, 4),
    _TmnxIPsecTnlGrpHistStatsValue32_Type()
)
tmnxIPsecTnlGrpHistStatsValue32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsValue32.setStatus("current")
_TmnxIPsecTnlGrpHistStatsIntvStTm_Type = DateAndTime
_TmnxIPsecTnlGrpHistStatsIntvStTm_Object = MibTableColumn
tmnxIPsecTnlGrpHistStatsIntvStTm = _TmnxIPsecTnlGrpHistStatsIntvStTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 76, 1, 5),
    _TmnxIPsecTnlGrpHistStatsIntvStTm_Type()
)
tmnxIPsecTnlGrpHistStatsIntvStTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsIntvStTm.setStatus("current")
_TmnxIPsecTnlGrpHistStatsIntvDur_Type = Unsigned32
_TmnxIPsecTnlGrpHistStatsIntvDur_Object = MibTableColumn
tmnxIPsecTnlGrpHistStatsIntvDur = _TmnxIPsecTnlGrpHistStatsIntvDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 76, 1, 6),
    _TmnxIPsecTnlGrpHistStatsIntvDur_Type()
)
tmnxIPsecTnlGrpHistStatsIntvDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsIntvDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsIntvDur.setUnits("seconds")
_TmnxIPsecTnlGrpHistStatsFstFTm_Type = DateAndTime
_TmnxIPsecTnlGrpHistStatsFstFTm_Object = MibTableColumn
tmnxIPsecTnlGrpHistStatsFstFTm = _TmnxIPsecTnlGrpHistStatsFstFTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 76, 1, 7),
    _TmnxIPsecTnlGrpHistStatsFstFTm_Type()
)
tmnxIPsecTnlGrpHistStatsFstFTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsFstFTm.setStatus("current")
_TmnxIPsecTnlGrpHistStatsFstFDesc_Type = TItemDescription
_TmnxIPsecTnlGrpHistStatsFstFDesc_Object = MibTableColumn
tmnxIPsecTnlGrpHistStatsFstFDesc = _TmnxIPsecTnlGrpHistStatsFstFDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 76, 1, 8),
    _TmnxIPsecTnlGrpHistStatsFstFDesc_Type()
)
tmnxIPsecTnlGrpHistStatsFstFDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsFstFDesc.setStatus("current")
_TmnxIPsecTnlGrpHistStatsLstFTm_Type = DateAndTime
_TmnxIPsecTnlGrpHistStatsLstFTm_Object = MibTableColumn
tmnxIPsecTnlGrpHistStatsLstFTm = _TmnxIPsecTnlGrpHistStatsLstFTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 76, 1, 9),
    _TmnxIPsecTnlGrpHistStatsLstFTm_Type()
)
tmnxIPsecTnlGrpHistStatsLstFTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsLstFTm.setStatus("current")
_TmnxIPsecTnlGrpHistStatsLstFDesc_Type = TItemDescription
_TmnxIPsecTnlGrpHistStatsLstFDesc_Object = MibTableColumn
tmnxIPsecTnlGrpHistStatsLstFDesc = _TmnxIPsecTnlGrpHistStatsLstFDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 76, 1, 10),
    _TmnxIPsecTnlGrpHistStatsLstFDesc_Type()
)
tmnxIPsecTnlGrpHistStatsLstFDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlGrpHistStatsLstFDesc.setStatus("current")
_TmnxIPsecSysHistStatsTable_Object = MibTable
tmnxIPsecSysHistStatsTable = _TmnxIPsecSysHistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 77)
)
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsTable.setStatus("current")
_TmnxIPsecSysHistStatsEntry_Object = MibTableRow
tmnxIPsecSysHistStatsEntry = _TmnxIPsecSysHistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 77, 1)
)
tmnxIPsecSysHistStatsEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSysHistStatsType"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSysHistStatsIntvIdx"),
)
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsEntry.setStatus("current")
_TmnxIPsecSysHistStatsType_Type = TmnxIPsecHistStatsType
_TmnxIPsecSysHistStatsType_Object = MibTableColumn
tmnxIPsecSysHistStatsType = _TmnxIPsecSysHistStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 77, 1, 1),
    _TmnxIPsecSysHistStatsType_Type()
)
tmnxIPsecSysHistStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsType.setStatus("current")
_TmnxIPsecSysHistStatsIntvIdx_Type = Unsigned32
_TmnxIPsecSysHistStatsIntvIdx_Object = MibTableColumn
tmnxIPsecSysHistStatsIntvIdx = _TmnxIPsecSysHistStatsIntvIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 77, 1, 2),
    _TmnxIPsecSysHistStatsIntvIdx_Type()
)
tmnxIPsecSysHistStatsIntvIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsIntvIdx.setStatus("current")
_TmnxIPsecSysHistStatsValue64_Type = CounterBasedGauge64
_TmnxIPsecSysHistStatsValue64_Object = MibTableColumn
tmnxIPsecSysHistStatsValue64 = _TmnxIPsecSysHistStatsValue64_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 77, 1, 3),
    _TmnxIPsecSysHistStatsValue64_Type()
)
tmnxIPsecSysHistStatsValue64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsValue64.setStatus("current")
_TmnxIPsecSysHistStatsValue32_Type = Integer32
_TmnxIPsecSysHistStatsValue32_Object = MibTableColumn
tmnxIPsecSysHistStatsValue32 = _TmnxIPsecSysHistStatsValue32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 77, 1, 4),
    _TmnxIPsecSysHistStatsValue32_Type()
)
tmnxIPsecSysHistStatsValue32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsValue32.setStatus("current")
_TmnxIPsecSysHistStatsIntvStTm_Type = DateAndTime
_TmnxIPsecSysHistStatsIntvStTm_Object = MibTableColumn
tmnxIPsecSysHistStatsIntvStTm = _TmnxIPsecSysHistStatsIntvStTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 77, 1, 5),
    _TmnxIPsecSysHistStatsIntvStTm_Type()
)
tmnxIPsecSysHistStatsIntvStTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsIntvStTm.setStatus("current")
_TmnxIPsecSysHistStatsIntvDur_Type = Unsigned32
_TmnxIPsecSysHistStatsIntvDur_Object = MibTableColumn
tmnxIPsecSysHistStatsIntvDur = _TmnxIPsecSysHistStatsIntvDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 77, 1, 6),
    _TmnxIPsecSysHistStatsIntvDur_Type()
)
tmnxIPsecSysHistStatsIntvDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsIntvDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsIntvDur.setUnits("seconds")
_TmnxIPsecSysHistStatsFstFTm_Type = DateAndTime
_TmnxIPsecSysHistStatsFstFTm_Object = MibTableColumn
tmnxIPsecSysHistStatsFstFTm = _TmnxIPsecSysHistStatsFstFTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 77, 1, 7),
    _TmnxIPsecSysHistStatsFstFTm_Type()
)
tmnxIPsecSysHistStatsFstFTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsFstFTm.setStatus("current")
_TmnxIPsecSysHistStatsFstFDesc_Type = TItemDescription
_TmnxIPsecSysHistStatsFstFDesc_Object = MibTableColumn
tmnxIPsecSysHistStatsFstFDesc = _TmnxIPsecSysHistStatsFstFDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 77, 1, 8),
    _TmnxIPsecSysHistStatsFstFDesc_Type()
)
tmnxIPsecSysHistStatsFstFDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsFstFDesc.setStatus("current")
_TmnxIPsecSysHistStatsLstFTm_Type = DateAndTime
_TmnxIPsecSysHistStatsLstFTm_Object = MibTableColumn
tmnxIPsecSysHistStatsLstFTm = _TmnxIPsecSysHistStatsLstFTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 77, 1, 9),
    _TmnxIPsecSysHistStatsLstFTm_Type()
)
tmnxIPsecSysHistStatsLstFTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsLstFTm.setStatus("current")
_TmnxIPsecSysHistStatsLstFDesc_Type = TItemDescription
_TmnxIPsecSysHistStatsLstFDesc_Object = MibTableColumn
tmnxIPsecSysHistStatsLstFDesc = _TmnxIPsecSysHistStatsLstFDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 77, 1, 10),
    _TmnxIPsecSysHistStatsLstFDesc_Type()
)
tmnxIPsecSysHistStatsLstFDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSysHistStatsLstFDesc.setStatus("current")
_TmnxIPsecTnlHistStatsTable_Object = MibTable
tmnxIPsecTnlHistStatsTable = _TmnxIPsecTnlHistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 78)
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlHistStatsTable.setStatus("current")
_TmnxIPsecTnlHistStatsEntry_Object = MibTableRow
tmnxIPsecTnlHistStatsEntry = _TmnxIPsecTnlHistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 78, 1)
)
tmnxIPsecTnlHistStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTnlHistStatsType"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTnlHistStatsIntvIdx"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlHistStatsEntry.setStatus("current")
_TmnxIPsecTnlHistStatsType_Type = TmnxIPsecHistStatsType
_TmnxIPsecTnlHistStatsType_Object = MibTableColumn
tmnxIPsecTnlHistStatsType = _TmnxIPsecTnlHistStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 78, 1, 1),
    _TmnxIPsecTnlHistStatsType_Type()
)
tmnxIPsecTnlHistStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTnlHistStatsType.setStatus("current")
_TmnxIPsecTnlHistStatsIntvIdx_Type = Unsigned32
_TmnxIPsecTnlHistStatsIntvIdx_Object = MibTableColumn
tmnxIPsecTnlHistStatsIntvIdx = _TmnxIPsecTnlHistStatsIntvIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 78, 1, 2),
    _TmnxIPsecTnlHistStatsIntvIdx_Type()
)
tmnxIPsecTnlHistStatsIntvIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTnlHistStatsIntvIdx.setStatus("current")
_TmnxIPsecTnlHistStatsValue64_Type = CounterBasedGauge64
_TmnxIPsecTnlHistStatsValue64_Object = MibTableColumn
tmnxIPsecTnlHistStatsValue64 = _TmnxIPsecTnlHistStatsValue64_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 78, 1, 3),
    _TmnxIPsecTnlHistStatsValue64_Type()
)
tmnxIPsecTnlHistStatsValue64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlHistStatsValue64.setStatus("current")
_TmnxIPsecTnlHistStatsIntvStTm_Type = DateAndTime
_TmnxIPsecTnlHistStatsIntvStTm_Object = MibTableColumn
tmnxIPsecTnlHistStatsIntvStTm = _TmnxIPsecTnlHistStatsIntvStTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 78, 1, 4),
    _TmnxIPsecTnlHistStatsIntvStTm_Type()
)
tmnxIPsecTnlHistStatsIntvStTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlHistStatsIntvStTm.setStatus("current")
_TmnxIPsecTnlHistStatsIntvDur_Type = Unsigned32
_TmnxIPsecTnlHistStatsIntvDur_Object = MibTableColumn
tmnxIPsecTnlHistStatsIntvDur = _TmnxIPsecTnlHistStatsIntvDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 78, 1, 5),
    _TmnxIPsecTnlHistStatsIntvDur_Type()
)
tmnxIPsecTnlHistStatsIntvDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlHistStatsIntvDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecTnlHistStatsIntvDur.setUnits("seconds")
_TmnxIPsecRUTnlHistStatsTable_Object = MibTable
tmnxIPsecRUTnlHistStatsTable = _TmnxIPsecRUTnlHistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 79)
)
if mibBuilder.loadTexts:
    tmnxIPsecRUTnlHistStatsTable.setStatus("current")
_TmnxIPsecRUTnlHistStatsEntry_Object = MibTableRow
tmnxIPsecRUTnlHistStatsEntry = _TmnxIPsecRUTnlHistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 79, 1)
)
tmnxIPsecRUTnlHistStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlPort"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecRUTnlHistStatsType"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecRUTnlHistStatsIntvIdx"),
)
if mibBuilder.loadTexts:
    tmnxIPsecRUTnlHistStatsEntry.setStatus("current")
_TmnxIPsecRUTnlHistStatsType_Type = TmnxIPsecHistStatsType
_TmnxIPsecRUTnlHistStatsType_Object = MibTableColumn
tmnxIPsecRUTnlHistStatsType = _TmnxIPsecRUTnlHistStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 79, 1, 1),
    _TmnxIPsecRUTnlHistStatsType_Type()
)
tmnxIPsecRUTnlHistStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecRUTnlHistStatsType.setStatus("current")
_TmnxIPsecRUTnlHistStatsIntvIdx_Type = Unsigned32
_TmnxIPsecRUTnlHistStatsIntvIdx_Object = MibTableColumn
tmnxIPsecRUTnlHistStatsIntvIdx = _TmnxIPsecRUTnlHistStatsIntvIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 79, 1, 2),
    _TmnxIPsecRUTnlHistStatsIntvIdx_Type()
)
tmnxIPsecRUTnlHistStatsIntvIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecRUTnlHistStatsIntvIdx.setStatus("current")
_TmnxIPsecRUTnlHistStatsValue64_Type = CounterBasedGauge64
_TmnxIPsecRUTnlHistStatsValue64_Object = MibTableColumn
tmnxIPsecRUTnlHistStatsValue64 = _TmnxIPsecRUTnlHistStatsValue64_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 79, 1, 3),
    _TmnxIPsecRUTnlHistStatsValue64_Type()
)
tmnxIPsecRUTnlHistStatsValue64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecRUTnlHistStatsValue64.setStatus("current")
_TmnxIPsecRUTnlHistStatsIntvStTm_Type = DateAndTime
_TmnxIPsecRUTnlHistStatsIntvStTm_Object = MibTableColumn
tmnxIPsecRUTnlHistStatsIntvStTm = _TmnxIPsecRUTnlHistStatsIntvStTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 79, 1, 4),
    _TmnxIPsecRUTnlHistStatsIntvStTm_Type()
)
tmnxIPsecRUTnlHistStatsIntvStTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecRUTnlHistStatsIntvStTm.setStatus("current")
_TmnxIPsecRUTnlHistStatsIntvDur_Type = Unsigned32
_TmnxIPsecRUTnlHistStatsIntvDur_Object = MibTableColumn
tmnxIPsecRUTnlHistStatsIntvDur = _TmnxIPsecRUTnlHistStatsIntvDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 79, 1, 5),
    _TmnxIPsecRUTnlHistStatsIntvDur_Type()
)
tmnxIPsecRUTnlHistStatsIntvDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecRUTnlHistStatsIntvDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecRUTnlHistStatsIntvDur.setUnits("seconds")
_TmnxIPsecGWStatsTable_Object = MibTable
tmnxIPsecGWStatsTable = _TmnxIPsecGWStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 80)
)
if mibBuilder.loadTexts:
    tmnxIPsecGWStatsTable.setStatus("current")
_TmnxIPsecGWStatsEntry_Object = MibTableRow
tmnxIPsecGWStatsEntry = _TmnxIPsecGWStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 80, 1)
)
tmnxIPsecGWStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxIPsecGWStatsEntry.setStatus("current")
_TmnxIPsecGWStatsNumOfDl2lTnls_Type = Unsigned32
_TmnxIPsecGWStatsNumOfDl2lTnls_Object = MibTableColumn
tmnxIPsecGWStatsNumOfDl2lTnls = _TmnxIPsecGWStatsNumOfDl2lTnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 80, 1, 1),
    _TmnxIPsecGWStatsNumOfDl2lTnls_Type()
)
tmnxIPsecGWStatsNumOfDl2lTnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWStatsNumOfDl2lTnls.setStatus("current")
_TmnxIPsecGWStatsNumOfRaTnls_Type = Unsigned32
_TmnxIPsecGWStatsNumOfRaTnls_Object = MibTableColumn
tmnxIPsecGWStatsNumOfRaTnls = _TmnxIPsecGWStatsNumOfRaTnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 80, 1, 2),
    _TmnxIPsecGWStatsNumOfRaTnls_Type()
)
tmnxIPsecGWStatsNumOfRaTnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWStatsNumOfRaTnls.setStatus("current")
_TmnxIPsecNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxIPsecNotifyObjs = _TmnxIPsecNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100)
)
_TIPsecNotifRUTnlInetAddrType_Type = InetAddressType
_TIPsecNotifRUTnlInetAddrType_Object = MibScalar
tIPsecNotifRUTnlInetAddrType = _TIPsecNotifRUTnlInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 1),
    _TIPsecNotifRUTnlInetAddrType_Type()
)
tIPsecNotifRUTnlInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifRUTnlInetAddrType.setStatus("current")


class _TIPsecNotifRUTnlInetAddress_Type(InetAddress):
    """Custom type tIPsecNotifRUTnlInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecNotifRUTnlInetAddress_Type.__name__ = "InetAddress"
_TIPsecNotifRUTnlInetAddress_Object = MibScalar
tIPsecNotifRUTnlInetAddress = _TIPsecNotifRUTnlInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 2),
    _TIPsecNotifRUTnlInetAddress_Type()
)
tIPsecNotifRUTnlInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifRUTnlInetAddress.setStatus("current")
_TIPsecNotifRUTnlPort_Type = TTcpUdpPort
_TIPsecNotifRUTnlPort_Object = MibScalar
tIPsecNotifRUTnlPort = _TIPsecNotifRUTnlPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 3),
    _TIPsecNotifRUTnlPort_Type()
)
tIPsecNotifRUTnlPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifRUTnlPort.setStatus("current")
_TIPsecNotifReason_Type = DisplayString
_TIPsecNotifReason_Object = MibScalar
tIPsecNotifReason = _TIPsecNotifReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 4),
    _TIPsecNotifReason_Type()
)
tIPsecNotifReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifReason.setStatus("current")
_TIPsecNotifBfdIntfSvcId_Type = TmnxServId
_TIPsecNotifBfdIntfSvcId_Object = MibScalar
tIPsecNotifBfdIntfSvcId = _TIPsecNotifBfdIntfSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 5),
    _TIPsecNotifBfdIntfSvcId_Type()
)
tIPsecNotifBfdIntfSvcId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifBfdIntfSvcId.setStatus("current")
_TIPsecNotifBfdIntfIfName_Type = TNamedItem
_TIPsecNotifBfdIntfIfName_Object = MibScalar
tIPsecNotifBfdIntfIfName = _TIPsecNotifBfdIntfIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 6),
    _TIPsecNotifBfdIntfIfName_Type()
)
tIPsecNotifBfdIntfIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifBfdIntfIfName.setStatus("current")
_TIPsecNotifBfdIntfDestIpType_Type = InetAddressType
_TIPsecNotifBfdIntfDestIpType_Object = MibScalar
tIPsecNotifBfdIntfDestIpType = _TIPsecNotifBfdIntfDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 7),
    _TIPsecNotifBfdIntfDestIpType_Type()
)
tIPsecNotifBfdIntfDestIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifBfdIntfDestIpType.setStatus("current")


class _TIPsecNotifBfdIntfDestIp_Type(InetAddress):
    """Custom type tIPsecNotifBfdIntfDestIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecNotifBfdIntfDestIp_Type.__name__ = "InetAddress"
_TIPsecNotifBfdIntfDestIp_Object = MibScalar
tIPsecNotifBfdIntfDestIp = _TIPsecNotifBfdIntfDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 8),
    _TIPsecNotifBfdIntfDestIp_Type()
)
tIPsecNotifBfdIntfDestIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifBfdIntfDestIp.setStatus("current")
_TIPsecNotifBfdIntfSessState_Type = TmnxBfdSessOperState
_TIPsecNotifBfdIntfSessState_Object = MibScalar
tIPsecNotifBfdIntfSessState = _TIPsecNotifBfdIntfSessState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 9),
    _TIPsecNotifBfdIntfSessState_Type()
)
tIPsecNotifBfdIntfSessState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifBfdIntfSessState.setStatus("current")
_TIPsecRadAcctPlcyFailReason_Type = DisplayString
_TIPsecRadAcctPlcyFailReason_Object = MibScalar
tIPsecRadAcctPlcyFailReason = _TIPsecRadAcctPlcyFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 10),
    _TIPsecRadAcctPlcyFailReason_Type()
)
tIPsecRadAcctPlcyFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyFailReason.setStatus("current")
_TIPsecNotifIPsecTunnelName_Type = TNamedItem
_TIPsecNotifIPsecTunnelName_Object = MibScalar
tIPsecNotifIPsecTunnelName = _TIPsecNotifIPsecTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 11),
    _TIPsecNotifIPsecTunnelName_Type()
)
tIPsecNotifIPsecTunnelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifIPsecTunnelName.setStatus("current")
_TIPsecNotifConfigIpMtu_Type = Unsigned32
_TIPsecNotifConfigIpMtu_Object = MibScalar
tIPsecNotifConfigIpMtu = _TIPsecNotifConfigIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 12),
    _TIPsecNotifConfigIpMtu_Type()
)
tIPsecNotifConfigIpMtu.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifConfigIpMtu.setStatus("current")
_TIPsecNotifEncapOverhead_Type = Unsigned32
_TIPsecNotifEncapOverhead_Object = MibScalar
tIPsecNotifEncapOverhead = _TIPsecNotifEncapOverhead_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 13),
    _TIPsecNotifEncapOverhead_Type()
)
tIPsecNotifEncapOverhead.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifEncapOverhead.setStatus("current")
_TIPsecNotifConfigEncapIpMtu_Type = Unsigned32
_TIPsecNotifConfigEncapIpMtu_Object = MibScalar
tIPsecNotifConfigEncapIpMtu = _TIPsecNotifConfigEncapIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 14),
    _TIPsecNotifConfigEncapIpMtu_Type()
)
tIPsecNotifConfigEncapIpMtu.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifConfigEncapIpMtu.setStatus("current")
_TIPsecNotifCertProfileName_Type = TNamedItem
_TIPsecNotifCertProfileName_Object = MibScalar
tIPsecNotifCertProfileName = _TIPsecNotifCertProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 15),
    _TIPsecNotifCertProfileName_Type()
)
tIPsecNotifCertProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifCertProfileName.setStatus("current")
_TIPsecNotifCertProfEntryId_Type = TEntryId
_TIPsecNotifCertProfEntryId_Object = MibScalar
tIPsecNotifCertProfEntryId = _TIPsecNotifCertProfEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 16),
    _TIPsecNotifCertProfEntryId_Type()
)
tIPsecNotifCertProfEntryId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifCertProfEntryId.setStatus("current")
_TIPsecNotifCaProfNames_Type = DisplayString
_TIPsecNotifCaProfNames_Object = MibScalar
tIPsecNotifCaProfNames = _TIPsecNotifCaProfNames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 17),
    _TIPsecNotifCaProfNames_Type()
)
tIPsecNotifCaProfNames.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifCaProfNames.setStatus("current")


class _TIPsecNotifTunnelType_Type(Integer32):
    """Custom type tIPsecNotifTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("secure-interface", 2),
          ("dynamic", 3))
    )


_TIPsecNotifTunnelType_Type.__name__ = "Integer32"
_TIPsecNotifTunnelType_Object = MibScalar
tIPsecNotifTunnelType = _TIPsecNotifTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 18),
    _TIPsecNotifTunnelType_Type()
)
tIPsecNotifTunnelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifTunnelType.setStatus("current")
_TIPsecNotifTunnelIdentifier_Type = DisplayString
_TIPsecNotifTunnelIdentifier_Object = MibScalar
tIPsecNotifTunnelIdentifier = _TIPsecNotifTunnelIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 19),
    _TIPsecNotifTunnelIdentifier_Type()
)
tIPsecNotifTunnelIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifTunnelIdentifier.setStatus("current")
_TmnxIPsecScalarsObjs_ObjectIdentity = ObjectIdentity
tmnxIPsecScalarsObjs = _TmnxIPsecScalarsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 101)
)


class _TmnxIPsecScalarObjsShowKeys_Type(TruthValue):
    """Custom type tmnxIPsecScalarObjsShowKeys based on TruthValue"""
    defaultValue = 2


_TmnxIPsecScalarObjsShowKeys_Type.__name__ = "TruthValue"
_TmnxIPsecScalarObjsShowKeys_Object = MibScalar
tmnxIPsecScalarObjsShowKeys = _TmnxIPsecScalarObjsShowKeys_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 101, 1),
    _TmnxIPsecScalarObjsShowKeys_Type()
)
tmnxIPsecScalarObjsShowKeys.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecScalarObjsShowKeys.setStatus("current")
_TmnxIPsecTnlBfdSessTableLChg_Type = TimeStamp
_TmnxIPsecTnlBfdSessTableLChg_Object = MibScalar
tmnxIPsecTnlBfdSessTableLChg = _TmnxIPsecTnlBfdSessTableLChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 102),
    _TmnxIPsecTnlBfdSessTableLChg_Type()
)
tmnxIPsecTnlBfdSessTableLChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessTableLChg.setStatus("current")
_TmnxIPsecTnlBfdSessTable_Object = MibTable
tmnxIPsecTnlBfdSessTable = _TmnxIPsecTnlBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 103)
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessTable.setStatus("current")
_TmnxIPsecTnlBfdSessEntry_Object = MibTableRow
tmnxIPsecTnlBfdSessEntry = _TmnxIPsecTnlBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 103, 1)
)
tmnxIPsecTnlBfdSessEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessEntry.setStatus("current")
_TmnxIPsecTnlBfdSessRowStatus_Type = RowStatus
_TmnxIPsecTnlBfdSessRowStatus_Object = MibTableColumn
tmnxIPsecTnlBfdSessRowStatus = _TmnxIPsecTnlBfdSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 103, 1, 1),
    _TmnxIPsecTnlBfdSessRowStatus_Type()
)
tmnxIPsecTnlBfdSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessRowStatus.setStatus("current")


class _TmnxIPsecTnlBfdSessSvcId_Type(TmnxServId):
    """Custom type tmnxIPsecTnlBfdSessSvcId based on TmnxServId"""
    defaultValue = 0


_TmnxIPsecTnlBfdSessSvcId_Type.__name__ = "TmnxServId"
_TmnxIPsecTnlBfdSessSvcId_Object = MibTableColumn
tmnxIPsecTnlBfdSessSvcId = _TmnxIPsecTnlBfdSessSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 103, 1, 2),
    _TmnxIPsecTnlBfdSessSvcId_Type()
)
tmnxIPsecTnlBfdSessSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessSvcId.setStatus("current")


class _TmnxIPsecTnlBfdSessSvcName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxIPsecTnlBfdSessSvcName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecTnlBfdSessSvcName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxIPsecTnlBfdSessSvcName_Object = MibTableColumn
tmnxIPsecTnlBfdSessSvcName = _TmnxIPsecTnlBfdSessSvcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 103, 1, 3),
    _TmnxIPsecTnlBfdSessSvcName_Type()
)
tmnxIPsecTnlBfdSessSvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessSvcName.setStatus("current")


class _TmnxIPsecTnlBfdSessIfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecTnlBfdSessIfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecTnlBfdSessIfName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecTnlBfdSessIfName_Object = MibTableColumn
tmnxIPsecTnlBfdSessIfName = _TmnxIPsecTnlBfdSessIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 103, 1, 4),
    _TmnxIPsecTnlBfdSessIfName_Type()
)
tmnxIPsecTnlBfdSessIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessIfName.setStatus("current")


class _TmnxIPsecTnlBfdSessDstAddrT_Type(InetAddressType):
    """Custom type tmnxIPsecTnlBfdSessDstAddrT based on InetAddressType"""
    defaultValue = 1


_TmnxIPsecTnlBfdSessDstAddrT_Type.__name__ = "InetAddressType"
_TmnxIPsecTnlBfdSessDstAddrT_Object = MibTableColumn
tmnxIPsecTnlBfdSessDstAddrT = _TmnxIPsecTnlBfdSessDstAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 103, 1, 5),
    _TmnxIPsecTnlBfdSessDstAddrT_Type()
)
tmnxIPsecTnlBfdSessDstAddrT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessDstAddrT.setStatus("current")


class _TmnxIPsecTnlBfdSessDstAddr_Type(InetAddress):
    """Custom type tmnxIPsecTnlBfdSessDstAddr based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_TmnxIPsecTnlBfdSessDstAddr_Type.__name__ = "InetAddress"
_TmnxIPsecTnlBfdSessDstAddr_Object = MibTableColumn
tmnxIPsecTnlBfdSessDstAddr = _TmnxIPsecTnlBfdSessDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 103, 1, 6),
    _TmnxIPsecTnlBfdSessDstAddr_Type()
)
tmnxIPsecTnlBfdSessDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessDstAddr.setStatus("current")
_TmnxIPsecTnlBfdSessStatTable_Object = MibTable
tmnxIPsecTnlBfdSessStatTable = _TmnxIPsecTnlBfdSessStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 104)
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessStatTable.setStatus("current")
_TmnxIPsecTnlBfdSessStatEntry_Object = MibTableRow
tmnxIPsecTnlBfdSessStatEntry = _TmnxIPsecTnlBfdSessStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 104, 1)
)
tmnxIPsecTnlBfdSessStatEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessStatEntry.setStatus("current")
_TmnxIPsecTnlBfdSessStatSrcAddrT_Type = InetAddressType
_TmnxIPsecTnlBfdSessStatSrcAddrT_Object = MibTableColumn
tmnxIPsecTnlBfdSessStatSrcAddrT = _TmnxIPsecTnlBfdSessStatSrcAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 104, 1, 1),
    _TmnxIPsecTnlBfdSessStatSrcAddrT_Type()
)
tmnxIPsecTnlBfdSessStatSrcAddrT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessStatSrcAddrT.setStatus("current")


class _TmnxIPsecTnlBfdSessStatSrcAddr_Type(InetAddress):
    """Custom type tmnxIPsecTnlBfdSessStatSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecTnlBfdSessStatSrcAddr_Type.__name__ = "InetAddress"
_TmnxIPsecTnlBfdSessStatSrcAddr_Object = MibTableColumn
tmnxIPsecTnlBfdSessStatSrcAddr = _TmnxIPsecTnlBfdSessStatSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 104, 1, 2),
    _TmnxIPsecTnlBfdSessStatSrcAddr_Type()
)
tmnxIPsecTnlBfdSessStatSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessStatSrcAddr.setStatus("current")
_TmnxIPsecTnlBfdSessStatOperState_Type = TmnxBfdSessOperState
_TmnxIPsecTnlBfdSessStatOperState_Object = MibTableColumn
tmnxIPsecTnlBfdSessStatOperState = _TmnxIPsecTnlBfdSessStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 104, 1, 3),
    _TmnxIPsecTnlBfdSessStatOperState_Type()
)
tmnxIPsecTnlBfdSessStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessStatOperState.setStatus("current")
_TmnxVRtIPsecTnlTableLastChanged_Type = TimeStamp
_TmnxVRtIPsecTnlTableLastChanged_Object = MibScalar
tmnxVRtIPsecTnlTableLastChanged = _TmnxVRtIPsecTnlTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 105),
    _TmnxVRtIPsecTnlTableLastChanged_Type()
)
tmnxVRtIPsecTnlTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlTableLastChanged.setStatus("current")
_TmnxVRtIPsecTnlTable_Object = MibTable
tmnxVRtIPsecTnlTable = _TmnxVRtIPsecTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106)
)
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlTable.setStatus("current")
_TmnxVRtIPsecTnlEntry_Object = MibTableRow
tmnxVRtIPsecTnlEntry = _TmnxVRtIPsecTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1)
)
tmnxVRtIPsecTnlEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlName"),
)
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlEntry.setStatus("current")
_TmnxVRtIPsecTnlName_Type = TNamedItem
_TmnxVRtIPsecTnlName_Object = MibTableColumn
tmnxVRtIPsecTnlName = _TmnxVRtIPsecTnlName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 1),
    _TmnxVRtIPsecTnlName_Type()
)
tmnxVRtIPsecTnlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlName.setStatus("current")
_TmnxVRtIPsecTnlRowStatus_Type = RowStatus
_TmnxVRtIPsecTnlRowStatus_Object = MibTableColumn
tmnxVRtIPsecTnlRowStatus = _TmnxVRtIPsecTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 2),
    _TmnxVRtIPsecTnlRowStatus_Type()
)
tmnxVRtIPsecTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlRowStatus.setStatus("current")
_TmnxVRtIPsecTnlLastChanged_Type = TimeStamp
_TmnxVRtIPsecTnlLastChanged_Object = MibTableColumn
tmnxVRtIPsecTnlLastChanged = _TmnxVRtIPsecTnlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 3),
    _TmnxVRtIPsecTnlLastChanged_Type()
)
tmnxVRtIPsecTnlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlLastChanged.setStatus("current")


class _TmnxVRtIPsecTnlAdminState_Type(TmnxAdminState):
    """Custom type tmnxVRtIPsecTnlAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxVRtIPsecTnlAdminState_Type.__name__ = "TmnxAdminState"
_TmnxVRtIPsecTnlAdminState_Object = MibTableColumn
tmnxVRtIPsecTnlAdminState = _TmnxVRtIPsecTnlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 4),
    _TmnxVRtIPsecTnlAdminState_Type()
)
tmnxVRtIPsecTnlAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlAdminState.setStatus("current")
_TmnxVRtIPsecTnlOperState_Type = TmnxIPsecOperState
_TmnxVRtIPsecTnlOperState_Object = MibTableColumn
tmnxVRtIPsecTnlOperState = _TmnxVRtIPsecTnlOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 5),
    _TmnxVRtIPsecTnlOperState_Type()
)
tmnxVRtIPsecTnlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlOperState.setStatus("current")


class _TmnxVRtIPsecTnlDescription_Type(TItemDescription):
    """Custom type tmnxVRtIPsecTnlDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxVRtIPsecTnlDescription_Type.__name__ = "TItemDescription"
_TmnxVRtIPsecTnlDescription_Object = MibTableColumn
tmnxVRtIPsecTnlDescription = _TmnxVRtIPsecTnlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 6),
    _TmnxVRtIPsecTnlDescription_Type()
)
tmnxVRtIPsecTnlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlDescription.setStatus("current")
_TmnxVRtIPsecTnlLclGwAddrType_Type = InetAddressType
_TmnxVRtIPsecTnlLclGwAddrType_Object = MibTableColumn
tmnxVRtIPsecTnlLclGwAddrType = _TmnxVRtIPsecTnlLclGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 7),
    _TmnxVRtIPsecTnlLclGwAddrType_Type()
)
tmnxVRtIPsecTnlLclGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlLclGwAddrType.setStatus("current")


class _TmnxVRtIPsecTnlLclGwAddr_Type(InetAddress):
    """Custom type tmnxVRtIPsecTnlLclGwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVRtIPsecTnlLclGwAddr_Type.__name__ = "InetAddress"
_TmnxVRtIPsecTnlLclGwAddr_Object = MibTableColumn
tmnxVRtIPsecTnlLclGwAddr = _TmnxVRtIPsecTnlLclGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 8),
    _TmnxVRtIPsecTnlLclGwAddr_Type()
)
tmnxVRtIPsecTnlLclGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlLclGwAddr.setStatus("current")


class _TmnxVRtIPsecTnlRemGwAddrType_Type(InetAddressType):
    """Custom type tmnxVRtIPsecTnlRemGwAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxVRtIPsecTnlRemGwAddrType_Type.__name__ = "InetAddressType"
_TmnxVRtIPsecTnlRemGwAddrType_Object = MibTableColumn
tmnxVRtIPsecTnlRemGwAddrType = _TmnxVRtIPsecTnlRemGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 9),
    _TmnxVRtIPsecTnlRemGwAddrType_Type()
)
tmnxVRtIPsecTnlRemGwAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlRemGwAddrType.setStatus("current")


class _TmnxVRtIPsecTnlRemGwAddr_Type(InetAddress):
    """Custom type tmnxVRtIPsecTnlRemGwAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVRtIPsecTnlRemGwAddr_Type.__name__ = "InetAddress"
_TmnxVRtIPsecTnlRemGwAddr_Object = MibTableColumn
tmnxVRtIPsecTnlRemGwAddr = _TmnxVRtIPsecTnlRemGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 10),
    _TmnxVRtIPsecTnlRemGwAddr_Type()
)
tmnxVRtIPsecTnlRemGwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlRemGwAddr.setStatus("current")


class _TmnxVRtIPsecTnlSecurityPolicyId_Type(TmnxIPsecPolicyIdOrZero):
    """Custom type tmnxVRtIPsecTnlSecurityPolicyId based on TmnxIPsecPolicyIdOrZero"""
    defaultValue = 0


_TmnxVRtIPsecTnlSecurityPolicyId_Type.__name__ = "TmnxIPsecPolicyIdOrZero"
_TmnxVRtIPsecTnlSecurityPolicyId_Object = MibTableColumn
tmnxVRtIPsecTnlSecurityPolicyId = _TmnxVRtIPsecTnlSecurityPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 11),
    _TmnxVRtIPsecTnlSecurityPolicyId_Type()
)
tmnxVRtIPsecTnlSecurityPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlSecurityPolicyId.setStatus("current")


class _TmnxVRtIPsecTnlKeyingType_Type(TmnxIPsecKeyingType):
    """Custom type tmnxVRtIPsecTnlKeyingType based on TmnxIPsecKeyingType"""
    defaultValue = 0


_TmnxVRtIPsecTnlKeyingType_Type.__name__ = "TmnxIPsecKeyingType"
_TmnxVRtIPsecTnlKeyingType_Object = MibTableColumn
tmnxVRtIPsecTnlKeyingType = _TmnxVRtIPsecTnlKeyingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 12),
    _TmnxVRtIPsecTnlKeyingType_Type()
)
tmnxVRtIPsecTnlKeyingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlKeyingType.setStatus("current")


class _TmnxVRtIPsecTnlDynTransformId1_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tmnxVRtIPsecTnlDynTransformId1 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TmnxVRtIPsecTnlDynTransformId1_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TmnxVRtIPsecTnlDynTransformId1_Object = MibTableColumn
tmnxVRtIPsecTnlDynTransformId1 = _TmnxVRtIPsecTnlDynTransformId1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 13),
    _TmnxVRtIPsecTnlDynTransformId1_Type()
)
tmnxVRtIPsecTnlDynTransformId1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlDynTransformId1.setStatus("current")


class _TmnxVRtIPsecTnlDynTransformId2_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tmnxVRtIPsecTnlDynTransformId2 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TmnxVRtIPsecTnlDynTransformId2_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TmnxVRtIPsecTnlDynTransformId2_Object = MibTableColumn
tmnxVRtIPsecTnlDynTransformId2 = _TmnxVRtIPsecTnlDynTransformId2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 14),
    _TmnxVRtIPsecTnlDynTransformId2_Type()
)
tmnxVRtIPsecTnlDynTransformId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlDynTransformId2.setStatus("current")


class _TmnxVRtIPsecTnlDynTransformId3_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tmnxVRtIPsecTnlDynTransformId3 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TmnxVRtIPsecTnlDynTransformId3_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TmnxVRtIPsecTnlDynTransformId3_Object = MibTableColumn
tmnxVRtIPsecTnlDynTransformId3 = _TmnxVRtIPsecTnlDynTransformId3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 15),
    _TmnxVRtIPsecTnlDynTransformId3_Type()
)
tmnxVRtIPsecTnlDynTransformId3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlDynTransformId3.setStatus("current")


class _TmnxVRtIPsecTnlDynTransformId4_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tmnxVRtIPsecTnlDynTransformId4 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TmnxVRtIPsecTnlDynTransformId4_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TmnxVRtIPsecTnlDynTransformId4_Object = MibTableColumn
tmnxVRtIPsecTnlDynTransformId4 = _TmnxVRtIPsecTnlDynTransformId4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 16),
    _TmnxVRtIPsecTnlDynTransformId4_Type()
)
tmnxVRtIPsecTnlDynTransformId4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlDynTransformId4.setStatus("current")


class _TmnxVRtIPsecTnlIkePolicyId_Type(TmnxIkePolicyIdOrZero):
    """Custom type tmnxVRtIPsecTnlIkePolicyId based on TmnxIkePolicyIdOrZero"""
    defaultValue = 0


_TmnxVRtIPsecTnlIkePolicyId_Type.__name__ = "TmnxIkePolicyIdOrZero"
_TmnxVRtIPsecTnlIkePolicyId_Object = MibTableColumn
tmnxVRtIPsecTnlIkePolicyId = _TmnxVRtIPsecTnlIkePolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 17),
    _TmnxVRtIPsecTnlIkePolicyId_Type()
)
tmnxVRtIPsecTnlIkePolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIkePolicyId.setStatus("current")


class _TmnxVRtIPsecTnlIkePreSharedKey_Type(OctetString):
    """Custom type tmnxVRtIPsecTnlIkePreSharedKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxVRtIPsecTnlIkePreSharedKey_Type.__name__ = "OctetString"
_TmnxVRtIPsecTnlIkePreSharedKey_Object = MibTableColumn
tmnxVRtIPsecTnlIkePreSharedKey = _TmnxVRtIPsecTnlIkePreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 18),
    _TmnxVRtIPsecTnlIkePreSharedKey_Type()
)
tmnxVRtIPsecTnlIkePreSharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIkePreSharedKey.setStatus("current")


class _TmnxVRtIPsecTnlOperFlags_Type(Bits):
    """Custom type tmnxVRtIPsecTnlOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("unresolvedLocalIp", 0),
          ("tunnelAdminDown", 1),
          ("sapDown", 2),
          ("unresolvedPublicSvc", 3),
          ("bfdSessionDown", 4),
          ("reserved1", 5),
          ("unresolvedDstIp", 6),
          ("invalidCertFile", 7),
          ("invalidKeyFile", 8),
          ("trustAnchorsDown", 9),
          ("certProfileDown", 10),
          ("invalidCertKeyCombo", 11),
          ("securedIntfSourceAddrUnresolved", 12))
    )

_TmnxVRtIPsecTnlOperFlags_Type.__name__ = "Bits"
_TmnxVRtIPsecTnlOperFlags_Object = MibTableColumn
tmnxVRtIPsecTnlOperFlags = _TmnxVRtIPsecTnlOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 19),
    _TmnxVRtIPsecTnlOperFlags_Type()
)
tmnxVRtIPsecTnlOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlOperFlags.setStatus("current")


class _TmnxVRtIPsecTnlReplayWindow_Type(Unsigned32):
    """Custom type tmnxVRtIPsecTnlReplayWindow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
    )


_TmnxVRtIPsecTnlReplayWindow_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecTnlReplayWindow_Object = MibTableColumn
tmnxVRtIPsecTnlReplayWindow = _TmnxVRtIPsecTnlReplayWindow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 20),
    _TmnxVRtIPsecTnlReplayWindow_Type()
)
tmnxVRtIPsecTnlReplayWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlReplayWindow.setStatus("current")


class _TmnxVRtIPsecTnlAutoEstablish_Type(TruthValue):
    """Custom type tmnxVRtIPsecTnlAutoEstablish based on TruthValue"""
    defaultValue = 2


_TmnxVRtIPsecTnlAutoEstablish_Type.__name__ = "TruthValue"
_TmnxVRtIPsecTnlAutoEstablish_Object = MibTableColumn
tmnxVRtIPsecTnlAutoEstablish = _TmnxVRtIPsecTnlAutoEstablish_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 21),
    _TmnxVRtIPsecTnlAutoEstablish_Type()
)
tmnxVRtIPsecTnlAutoEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlAutoEstablish.setStatus("current")


class _TmnxVRtIPsecTnlBfdDesignate_Type(TruthValue):
    """Custom type tmnxVRtIPsecTnlBfdDesignate based on TruthValue"""
    defaultValue = 2


_TmnxVRtIPsecTnlBfdDesignate_Type.__name__ = "TruthValue"
_TmnxVRtIPsecTnlBfdDesignate_Object = MibTableColumn
tmnxVRtIPsecTnlBfdDesignate = _TmnxVRtIPsecTnlBfdDesignate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 22),
    _TmnxVRtIPsecTnlBfdDesignate_Type()
)
tmnxVRtIPsecTnlBfdDesignate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdDesignate.setStatus("current")


class _TmnxVRtIPsecTnlLocalIdType_Type(TmnxIPsecLocalIdType):
    """Custom type tmnxVRtIPsecTnlLocalIdType based on TmnxIPsecLocalIdType"""
    defaultValue = 0


_TmnxVRtIPsecTnlLocalIdType_Type.__name__ = "TmnxIPsecLocalIdType"
_TmnxVRtIPsecTnlLocalIdType_Object = MibTableColumn
tmnxVRtIPsecTnlLocalIdType = _TmnxVRtIPsecTnlLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 23),
    _TmnxVRtIPsecTnlLocalIdType_Type()
)
tmnxVRtIPsecTnlLocalIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlLocalIdType.setStatus("current")


class _TmnxVRtIPsecTnlLocalIdValue_Type(DisplayString):
    """Custom type tmnxVRtIPsecTnlLocalIdValue based on DisplayString"""
    defaultHexValue = ""


_TmnxVRtIPsecTnlLocalIdValue_Type.__name__ = "DisplayString"
_TmnxVRtIPsecTnlLocalIdValue_Object = MibTableColumn
tmnxVRtIPsecTnlLocalIdValue = _TmnxVRtIPsecTnlLocalIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 24),
    _TmnxVRtIPsecTnlLocalIdValue_Type()
)
tmnxVRtIPsecTnlLocalIdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlLocalIdValue.setStatus("current")


class _TmnxVRtIPsecTnlClearDfBit_Type(TruthValue):
    """Custom type tmnxVRtIPsecTnlClearDfBit based on TruthValue"""
    defaultValue = 2


_TmnxVRtIPsecTnlClearDfBit_Type.__name__ = "TruthValue"
_TmnxVRtIPsecTnlClearDfBit_Object = MibTableColumn
tmnxVRtIPsecTnlClearDfBit = _TmnxVRtIPsecTnlClearDfBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 25),
    _TmnxVRtIPsecTnlClearDfBit_Type()
)
tmnxVRtIPsecTnlClearDfBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlClearDfBit.setStatus("current")


class _TmnxVRtIPsecTnlIpMtu_Type(Unsigned32):
    """Custom type tmnxVRtIPsecTnlIpMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TmnxVRtIPsecTnlIpMtu_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecTnlIpMtu_Object = MibTableColumn
tmnxVRtIPsecTnlIpMtu = _TmnxVRtIPsecTnlIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 26),
    _TmnxVRtIPsecTnlIpMtu_Type()
)
tmnxVRtIPsecTnlIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIpMtu.setStatus("current")
_TmnxVRtIPsecTnlHostISA_Type = TmnxHwIndexOrZero
_TmnxVRtIPsecTnlHostISA_Object = MibTableColumn
tmnxVRtIPsecTnlHostISA = _TmnxVRtIPsecTnlHostISA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 27),
    _TmnxVRtIPsecTnlHostISA_Type()
)
tmnxVRtIPsecTnlHostISA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlHostISA.setStatus("current")


class _TmnxVRtIPsecTnlCSVPrimary_Type(TmnxCertRevStatus):
    """Custom type tmnxVRtIPsecTnlCSVPrimary based on TmnxCertRevStatus"""
    defaultValue = 1


_TmnxVRtIPsecTnlCSVPrimary_Type.__name__ = "TmnxCertRevStatus"
_TmnxVRtIPsecTnlCSVPrimary_Object = MibTableColumn
tmnxVRtIPsecTnlCSVPrimary = _TmnxVRtIPsecTnlCSVPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 28),
    _TmnxVRtIPsecTnlCSVPrimary_Type()
)
tmnxVRtIPsecTnlCSVPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlCSVPrimary.setStatus("current")


class _TmnxVRtIPsecTnlCSVSecondary_Type(TmnxCertRevStatusOrNone):
    """Custom type tmnxVRtIPsecTnlCSVSecondary based on TmnxCertRevStatusOrNone"""
    defaultValue = 0


_TmnxVRtIPsecTnlCSVSecondary_Type.__name__ = "TmnxCertRevStatusOrNone"
_TmnxVRtIPsecTnlCSVSecondary_Object = MibTableColumn
tmnxVRtIPsecTnlCSVSecondary = _TmnxVRtIPsecTnlCSVSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 29),
    _TmnxVRtIPsecTnlCSVSecondary_Type()
)
tmnxVRtIPsecTnlCSVSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlCSVSecondary.setStatus("current")


class _TmnxVRtIPsecTnlCSVDefResult_Type(Integer32):
    """Custom type tmnxVRtIPsecTnlCSVDefResult based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("revoked", 0),
          ("good", 1))
    )


_TmnxVRtIPsecTnlCSVDefResult_Type.__name__ = "Integer32"
_TmnxVRtIPsecTnlCSVDefResult_Object = MibTableColumn
tmnxVRtIPsecTnlCSVDefResult = _TmnxVRtIPsecTnlCSVDefResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 30),
    _TmnxVRtIPsecTnlCSVDefResult_Type()
)
tmnxVRtIPsecTnlCSVDefResult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlCSVDefResult.setStatus("current")


class _TmnxVRtIPsecTnlCertProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxVRtIPsecTnlCertProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxVRtIPsecTnlCertProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxVRtIPsecTnlCertProfile_Object = MibTableColumn
tmnxVRtIPsecTnlCertProfile = _TmnxVRtIPsecTnlCertProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 31),
    _TmnxVRtIPsecTnlCertProfile_Type()
)
tmnxVRtIPsecTnlCertProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlCertProfile.setStatus("current")
_TmnxVRtIPsecTnlMatchTrustAnchor_Type = TNamedItemOrEmpty
_TmnxVRtIPsecTnlMatchTrustAnchor_Object = MibTableColumn
tmnxVRtIPsecTnlMatchTrustAnchor = _TmnxVRtIPsecTnlMatchTrustAnchor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 32),
    _TmnxVRtIPsecTnlMatchTrustAnchor_Type()
)
tmnxVRtIPsecTnlMatchTrustAnchor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlMatchTrustAnchor.setStatus("current")


class _TmnxVRtIPsecTnlCertTrstAnchrProf_Type(TNamedItemOrEmpty):
    """Custom type tmnxVRtIPsecTnlCertTrstAnchrProf based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxVRtIPsecTnlCertTrstAnchrProf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxVRtIPsecTnlCertTrstAnchrProf_Object = MibTableColumn
tmnxVRtIPsecTnlCertTrstAnchrProf = _TmnxVRtIPsecTnlCertTrstAnchrProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 33),
    _TmnxVRtIPsecTnlCertTrstAnchrProf_Type()
)
tmnxVRtIPsecTnlCertTrstAnchrProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlCertTrstAnchrProf.setStatus("current")


class _TmnxVRtIPsecTnlEncapIpMtu_Type(Unsigned32):
    """Custom type tmnxVRtIPsecTnlEncapIpMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TmnxVRtIPsecTnlEncapIpMtu_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecTnlEncapIpMtu_Object = MibTableColumn
tmnxVRtIPsecTnlEncapIpMtu = _TmnxVRtIPsecTnlEncapIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 34),
    _TmnxVRtIPsecTnlEncapIpMtu_Type()
)
tmnxVRtIPsecTnlEncapIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlEncapIpMtu.setStatus("current")


class _TmnxVRtIPsecTnlPropagateIpv6PMTU_Type(TruthValue):
    """Custom type tmnxVRtIPsecTnlPropagateIpv6PMTU based on TruthValue"""
    defaultValue = 2


_TmnxVRtIPsecTnlPropagateIpv6PMTU_Type.__name__ = "TruthValue"
_TmnxVRtIPsecTnlPropagateIpv6PMTU_Object = MibTableColumn
tmnxVRtIPsecTnlPropagateIpv6PMTU = _TmnxVRtIPsecTnlPropagateIpv6PMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 35),
    _TmnxVRtIPsecTnlPropagateIpv6PMTU_Type()
)
tmnxVRtIPsecTnlPropagateIpv6PMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlPropagateIpv6PMTU.setStatus("current")


class _TmnxVRtIPsecTnlIcmp6Pkt2Big_Type(TruthValue):
    """Custom type tmnxVRtIPsecTnlIcmp6Pkt2Big based on TruthValue"""
    defaultValue = 1


_TmnxVRtIPsecTnlIcmp6Pkt2Big_Type.__name__ = "TruthValue"
_TmnxVRtIPsecTnlIcmp6Pkt2Big_Object = MibTableColumn
tmnxVRtIPsecTnlIcmp6Pkt2Big = _TmnxVRtIPsecTnlIcmp6Pkt2Big_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 36),
    _TmnxVRtIPsecTnlIcmp6Pkt2Big_Type()
)
tmnxVRtIPsecTnlIcmp6Pkt2Big.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIcmp6Pkt2Big.setStatus("current")


class _TmnxVRtIPsecTnlIcmp6NumPkt2Big_Type(Unsigned32):
    """Custom type tmnxVRtIPsecTnlIcmp6NumPkt2Big based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TmnxVRtIPsecTnlIcmp6NumPkt2Big_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecTnlIcmp6NumPkt2Big_Object = MibTableColumn
tmnxVRtIPsecTnlIcmp6NumPkt2Big = _TmnxVRtIPsecTnlIcmp6NumPkt2Big_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 37),
    _TmnxVRtIPsecTnlIcmp6NumPkt2Big_Type()
)
tmnxVRtIPsecTnlIcmp6NumPkt2Big.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIcmp6NumPkt2Big.setStatus("current")


class _TmnxVRtIPsecTnlIcmp6Pkt2BigTime_Type(Unsigned32):
    """Custom type tmnxVRtIPsecTnlIcmp6Pkt2BigTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxVRtIPsecTnlIcmp6Pkt2BigTime_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecTnlIcmp6Pkt2BigTime_Object = MibTableColumn
tmnxVRtIPsecTnlIcmp6Pkt2BigTime = _TmnxVRtIPsecTnlIcmp6Pkt2BigTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 38),
    _TmnxVRtIPsecTnlIcmp6Pkt2BigTime_Type()
)
tmnxVRtIPsecTnlIcmp6Pkt2BigTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIcmp6Pkt2BigTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIcmp6Pkt2BigTime.setUnits("seconds")
_TmnxVRtIPsecTnlOperChanged_Type = TimeStamp
_TmnxVRtIPsecTnlOperChanged_Object = MibTableColumn
tmnxVRtIPsecTnlOperChanged = _TmnxVRtIPsecTnlOperChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 39),
    _TmnxVRtIPsecTnlOperChanged_Type()
)
tmnxVRtIPsecTnlOperChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlOperChanged.setStatus("current")


class _TmnxVRtIPsecTnlPropagateIpv4PMTU_Type(TruthValue):
    """Custom type tmnxVRtIPsecTnlPropagateIpv4PMTU based on TruthValue"""
    defaultValue = 2


_TmnxVRtIPsecTnlPropagateIpv4PMTU_Type.__name__ = "TruthValue"
_TmnxVRtIPsecTnlPropagateIpv4PMTU_Object = MibTableColumn
tmnxVRtIPsecTnlPropagateIpv4PMTU = _TmnxVRtIPsecTnlPropagateIpv4PMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 40),
    _TmnxVRtIPsecTnlPropagateIpv4PMTU_Type()
)
tmnxVRtIPsecTnlPropagateIpv4PMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlPropagateIpv4PMTU.setStatus("current")


class _TmnxVRtIPsecTnlIcmpFragReq_Type(TruthValue):
    """Custom type tmnxVRtIPsecTnlIcmpFragReq based on TruthValue"""
    defaultValue = 1


_TmnxVRtIPsecTnlIcmpFragReq_Type.__name__ = "TruthValue"
_TmnxVRtIPsecTnlIcmpFragReq_Object = MibTableColumn
tmnxVRtIPsecTnlIcmpFragReq = _TmnxVRtIPsecTnlIcmpFragReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 41),
    _TmnxVRtIPsecTnlIcmpFragReq_Type()
)
tmnxVRtIPsecTnlIcmpFragReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIcmpFragReq.setStatus("current")


class _TmnxVRtIPsecTnlIcmpFragReqNum_Type(Unsigned32):
    """Custom type tmnxVRtIPsecTnlIcmpFragReqNum based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TmnxVRtIPsecTnlIcmpFragReqNum_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecTnlIcmpFragReqNum_Object = MibTableColumn
tmnxVRtIPsecTnlIcmpFragReqNum = _TmnxVRtIPsecTnlIcmpFragReqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 42),
    _TmnxVRtIPsecTnlIcmpFragReqNum_Type()
)
tmnxVRtIPsecTnlIcmpFragReqNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIcmpFragReqNum.setStatus("current")


class _TmnxVRtIPsecTnlIcmpFragReqTime_Type(Unsigned32):
    """Custom type tmnxVRtIPsecTnlIcmpFragReqTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxVRtIPsecTnlIcmpFragReqTime_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecTnlIcmpFragReqTime_Object = MibTableColumn
tmnxVRtIPsecTnlIcmpFragReqTime = _TmnxVRtIPsecTnlIcmpFragReqTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 43),
    _TmnxVRtIPsecTnlIcmpFragReqTime_Type()
)
tmnxVRtIPsecTnlIcmpFragReqTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIcmpFragReqTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIcmpFragReqTime.setUnits("seconds")


class _TmnxVRtIPsecTnlPMTUDiscoverAging_Type(Unsigned32):
    """Custom type tmnxVRtIPsecTnlPMTUDiscoverAging based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 3600),
    )


_TmnxVRtIPsecTnlPMTUDiscoverAging_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecTnlPMTUDiscoverAging_Object = MibTableColumn
tmnxVRtIPsecTnlPMTUDiscoverAging = _TmnxVRtIPsecTnlPMTUDiscoverAging_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 44),
    _TmnxVRtIPsecTnlPMTUDiscoverAging_Type()
)
tmnxVRtIPsecTnlPMTUDiscoverAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlPMTUDiscoverAging.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlPMTUDiscoverAging.setUnits("seconds")


class _TmnxVRtIPsecTnlPubTcpMssAdjust_Type(Integer32):
    """Custom type tmnxVRtIPsecTnlPubTcpMssAdjust based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TmnxVRtIPsecTnlPubTcpMssAdjust_Type.__name__ = "Integer32"
_TmnxVRtIPsecTnlPubTcpMssAdjust_Object = MibTableColumn
tmnxVRtIPsecTnlPubTcpMssAdjust = _TmnxVRtIPsecTnlPubTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 45),
    _TmnxVRtIPsecTnlPubTcpMssAdjust_Type()
)
tmnxVRtIPsecTnlPubTcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlPubTcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlPubTcpMssAdjust.setUnits("octets")


class _TmnxVRtIPsecTnlPrivTcpMssAdjust_Type(Integer32):
    """Custom type tmnxVRtIPsecTnlPrivTcpMssAdjust based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(512, 9000),
    )


_TmnxVRtIPsecTnlPrivTcpMssAdjust_Type.__name__ = "Integer32"
_TmnxVRtIPsecTnlPrivTcpMssAdjust_Object = MibTableColumn
tmnxVRtIPsecTnlPrivTcpMssAdjust = _TmnxVRtIPsecTnlPrivTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 46),
    _TmnxVRtIPsecTnlPrivTcpMssAdjust_Type()
)
tmnxVRtIPsecTnlPrivTcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlPrivTcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlPrivTcpMssAdjust.setUnits("octets")


class _TmnxVRtIPsecTnlMaxNumPh1SaKeys_Type(Unsigned32):
    """Custom type tmnxVRtIPsecTnlMaxNumPh1SaKeys based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TmnxVRtIPsecTnlMaxNumPh1SaKeys_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecTnlMaxNumPh1SaKeys_Object = MibTableColumn
tmnxVRtIPsecTnlMaxNumPh1SaKeys = _TmnxVRtIPsecTnlMaxNumPh1SaKeys_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 47),
    _TmnxVRtIPsecTnlMaxNumPh1SaKeys_Type()
)
tmnxVRtIPsecTnlMaxNumPh1SaKeys.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlMaxNumPh1SaKeys.setStatus("current")


class _TmnxVRtIPsecTnlMaxNumPh2SaKeys_Type(Unsigned32):
    """Custom type tmnxVRtIPsecTnlMaxNumPh2SaKeys based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_TmnxVRtIPsecTnlMaxNumPh2SaKeys_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecTnlMaxNumPh2SaKeys_Object = MibTableColumn
tmnxVRtIPsecTnlMaxNumPh2SaKeys = _TmnxVRtIPsecTnlMaxNumPh2SaKeys_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 48),
    _TmnxVRtIPsecTnlMaxNumPh2SaKeys_Type()
)
tmnxVRtIPsecTnlMaxNumPh2SaKeys.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlMaxNumPh2SaKeys.setStatus("current")


class _TmnxVRtIPsecTnlSecPlyStrictMatch_Type(TruthValue):
    """Custom type tmnxVRtIPsecTnlSecPlyStrictMatch based on TruthValue"""
    defaultValue = 2


_TmnxVRtIPsecTnlSecPlyStrictMatch_Type.__name__ = "TruthValue"
_TmnxVRtIPsecTnlSecPlyStrictMatch_Object = MibTableColumn
tmnxVRtIPsecTnlSecPlyStrictMatch = _TmnxVRtIPsecTnlSecPlyStrictMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 49),
    _TmnxVRtIPsecTnlSecPlyStrictMatch_Type()
)
tmnxVRtIPsecTnlSecPlyStrictMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlSecPlyStrictMatch.setStatus("current")


class _TmnxVRtIPsecTnlPrivateSvcName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxVRtIPsecTnlPrivateSvcName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxVRtIPsecTnlPrivateSvcName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxVRtIPsecTnlPrivateSvcName_Object = MibTableColumn
tmnxVRtIPsecTnlPrivateSvcName = _TmnxVRtIPsecTnlPrivateSvcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 50),
    _TmnxVRtIPsecTnlPrivateSvcName_Type()
)
tmnxVRtIPsecTnlPrivateSvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlPrivateSvcName.setStatus("current")


class _TmnxVRtIPsecTnlPrivSap_Type(Unsigned32):
    """Custom type tmnxVRtIPsecTnlPrivSap based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TmnxVRtIPsecTnlPrivSap_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecTnlPrivSap_Object = MibTableColumn
tmnxVRtIPsecTnlPrivSap = _TmnxVRtIPsecTnlPrivSap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 51),
    _TmnxVRtIPsecTnlPrivSap_Type()
)
tmnxVRtIPsecTnlPrivSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlPrivSap.setStatus("current")


class _TmnxVRtIPsecTnlLclGwAddrOvrdType_Type(InetAddressType):
    """Custom type tmnxVRtIPsecTnlLclGwAddrOvrdType based on InetAddressType"""
    defaultValue = 0


_TmnxVRtIPsecTnlLclGwAddrOvrdType_Type.__name__ = "InetAddressType"
_TmnxVRtIPsecTnlLclGwAddrOvrdType_Object = MibTableColumn
tmnxVRtIPsecTnlLclGwAddrOvrdType = _TmnxVRtIPsecTnlLclGwAddrOvrdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 52),
    _TmnxVRtIPsecTnlLclGwAddrOvrdType_Type()
)
tmnxVRtIPsecTnlLclGwAddrOvrdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlLclGwAddrOvrdType.setStatus("current")


class _TmnxVRtIPsecTnlLclGwAddrOvrd_Type(InetAddress):
    """Custom type tmnxVRtIPsecTnlLclGwAddrOvrd based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVRtIPsecTnlLclGwAddrOvrd_Type.__name__ = "InetAddress"
_TmnxVRtIPsecTnlLclGwAddrOvrd_Object = MibTableColumn
tmnxVRtIPsecTnlLclGwAddrOvrd = _TmnxVRtIPsecTnlLclGwAddrOvrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 53),
    _TmnxVRtIPsecTnlLclGwAddrOvrd_Type()
)
tmnxVRtIPsecTnlLclGwAddrOvrd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlLclGwAddrOvrd.setStatus("current")
_TmnxVRtIPsecTnlHostEsa_Type = TmnxEsaIdOrZero
_TmnxVRtIPsecTnlHostEsa_Object = MibTableColumn
tmnxVRtIPsecTnlHostEsa = _TmnxVRtIPsecTnlHostEsa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 54),
    _TmnxVRtIPsecTnlHostEsa_Type()
)
tmnxVRtIPsecTnlHostEsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlHostEsa.setStatus("current")
_TmnxVRtIPsecTnlHostEsaVm_Type = TmnxEsaVmIdOrZero
_TmnxVRtIPsecTnlHostEsaVm_Object = MibTableColumn
tmnxVRtIPsecTnlHostEsaVm = _TmnxVRtIPsecTnlHostEsaVm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 106, 1, 55),
    _TmnxVRtIPsecTnlHostEsaVm_Type()
)
tmnxVRtIPsecTnlHostEsaVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlHostEsaVm.setStatus("current")
_TmnxVRtIPsecTnlBfdTableLChg_Type = TimeStamp
_TmnxVRtIPsecTnlBfdTableLChg_Object = MibScalar
tmnxVRtIPsecTnlBfdTableLChg = _TmnxVRtIPsecTnlBfdTableLChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 107),
    _TmnxVRtIPsecTnlBfdTableLChg_Type()
)
tmnxVRtIPsecTnlBfdTableLChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdTableLChg.setStatus("current")
_TmnxVRtIPsecTnlBfdTable_Object = MibTable
tmnxVRtIPsecTnlBfdTable = _TmnxVRtIPsecTnlBfdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 108)
)
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdTable.setStatus("current")
_TmnxVRtIPsecTnlBfdEntry_Object = MibTableRow
tmnxVRtIPsecTnlBfdEntry = _TmnxVRtIPsecTnlBfdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 108, 1)
)
tmnxVRtIPsecTnlBfdEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlName"),
)
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdEntry.setStatus("current")
_TmnxVRtIPsecTnlBfdRowStatus_Type = RowStatus
_TmnxVRtIPsecTnlBfdRowStatus_Object = MibTableColumn
tmnxVRtIPsecTnlBfdRowStatus = _TmnxVRtIPsecTnlBfdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 108, 1, 1),
    _TmnxVRtIPsecTnlBfdRowStatus_Type()
)
tmnxVRtIPsecTnlBfdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdRowStatus.setStatus("current")


class _TmnxVRtIPsecTnlBfdSvcName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxVRtIPsecTnlBfdSvcName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxVRtIPsecTnlBfdSvcName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxVRtIPsecTnlBfdSvcName_Object = MibTableColumn
tmnxVRtIPsecTnlBfdSvcName = _TmnxVRtIPsecTnlBfdSvcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 108, 1, 2),
    _TmnxVRtIPsecTnlBfdSvcName_Type()
)
tmnxVRtIPsecTnlBfdSvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdSvcName.setStatus("current")


class _TmnxVRtIPsecTnlBfdIfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxVRtIPsecTnlBfdIfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxVRtIPsecTnlBfdIfName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxVRtIPsecTnlBfdIfName_Object = MibTableColumn
tmnxVRtIPsecTnlBfdIfName = _TmnxVRtIPsecTnlBfdIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 108, 1, 3),
    _TmnxVRtIPsecTnlBfdIfName_Type()
)
tmnxVRtIPsecTnlBfdIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdIfName.setStatus("current")


class _TmnxVRtIPsecTnlBfdDstAddrT_Type(InetAddressType):
    """Custom type tmnxVRtIPsecTnlBfdDstAddrT based on InetAddressType"""
    defaultValue = 1


_TmnxVRtIPsecTnlBfdDstAddrT_Type.__name__ = "InetAddressType"
_TmnxVRtIPsecTnlBfdDstAddrT_Object = MibTableColumn
tmnxVRtIPsecTnlBfdDstAddrT = _TmnxVRtIPsecTnlBfdDstAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 108, 1, 4),
    _TmnxVRtIPsecTnlBfdDstAddrT_Type()
)
tmnxVRtIPsecTnlBfdDstAddrT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdDstAddrT.setStatus("current")


class _TmnxVRtIPsecTnlBfdDstAddr_Type(InetAddress):
    """Custom type tmnxVRtIPsecTnlBfdDstAddr based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_TmnxVRtIPsecTnlBfdDstAddr_Type.__name__ = "InetAddress"
_TmnxVRtIPsecTnlBfdDstAddr_Object = MibTableColumn
tmnxVRtIPsecTnlBfdDstAddr = _TmnxVRtIPsecTnlBfdDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 108, 1, 5),
    _TmnxVRtIPsecTnlBfdDstAddr_Type()
)
tmnxVRtIPsecTnlBfdDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdDstAddr.setStatus("current")
_TmnxVRtIPsecTnlBfdStatTable_Object = MibTable
tmnxVRtIPsecTnlBfdStatTable = _TmnxVRtIPsecTnlBfdStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 109)
)
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdStatTable.setStatus("current")
_TmnxVRtIPsecTnlBfdStatEntry_Object = MibTableRow
tmnxVRtIPsecTnlBfdStatEntry = _TmnxVRtIPsecTnlBfdStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 109, 1)
)
tmnxVRtIPsecTnlBfdStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlName"),
)
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdStatEntry.setStatus("current")
_TmnxVRtIPsecTnlBfdStatSrcAddrT_Type = InetAddressType
_TmnxVRtIPsecTnlBfdStatSrcAddrT_Object = MibTableColumn
tmnxVRtIPsecTnlBfdStatSrcAddrT = _TmnxVRtIPsecTnlBfdStatSrcAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 109, 1, 1),
    _TmnxVRtIPsecTnlBfdStatSrcAddrT_Type()
)
tmnxVRtIPsecTnlBfdStatSrcAddrT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdStatSrcAddrT.setStatus("current")


class _TmnxVRtIPsecTnlBfdStatSrcAddr_Type(InetAddress):
    """Custom type tmnxVRtIPsecTnlBfdStatSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxVRtIPsecTnlBfdStatSrcAddr_Type.__name__ = "InetAddress"
_TmnxVRtIPsecTnlBfdStatSrcAddr_Object = MibTableColumn
tmnxVRtIPsecTnlBfdStatSrcAddr = _TmnxVRtIPsecTnlBfdStatSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 109, 1, 2),
    _TmnxVRtIPsecTnlBfdStatSrcAddr_Type()
)
tmnxVRtIPsecTnlBfdStatSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdStatSrcAddr.setStatus("current")
_TmnxVRtIPsecTnlBfdStatOperState_Type = TmnxBfdSessOperState
_TmnxVRtIPsecTnlBfdStatOperState_Object = MibTableColumn
tmnxVRtIPsecTnlBfdStatOperState = _TmnxVRtIPsecTnlBfdStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 109, 1, 3),
    _TmnxVRtIPsecTnlBfdStatOperState_Type()
)
tmnxVRtIPsecTnlBfdStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlBfdStatOperState.setStatus("current")
_TmnxVRtIPsecSATableLastChanged_Type = TimeStamp
_TmnxVRtIPsecSATableLastChanged_Object = MibScalar
tmnxVRtIPsecSATableLastChanged = _TmnxVRtIPsecSATableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 112),
    _TmnxVRtIPsecSATableLastChanged_Type()
)
tmnxVRtIPsecSATableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSATableLastChanged.setStatus("current")
_TmnxVRtIPsecSATable_Object = MibTable
tmnxVRtIPsecSATable = _TmnxVRtIPsecSATable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113)
)
if mibBuilder.loadTexts:
    tmnxVRtIPsecSATable.setStatus("current")
_TmnxVRtIPsecSAEntry_Object = MibTableRow
tmnxVRtIPsecSAEntry = _TmnxVRtIPsecSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1)
)
tmnxVRtIPsecSAEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSADirection"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAIndex"),
)
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAEntry.setStatus("current")


class _TmnxVRtIPsecSAId_Type(Unsigned32):
    """Custom type tmnxVRtIPsecSAId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxVRtIPsecSAId_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecSAId_Object = MibTableColumn
tmnxVRtIPsecSAId = _TmnxVRtIPsecSAId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 1),
    _TmnxVRtIPsecSAId_Type()
)
tmnxVRtIPsecSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAId.setStatus("current")
_TmnxVRtIPsecSADirection_Type = TmnxIPsecDirection
_TmnxVRtIPsecSADirection_Object = MibTableColumn
tmnxVRtIPsecSADirection = _TmnxVRtIPsecSADirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 2),
    _TmnxVRtIPsecSADirection_Type()
)
tmnxVRtIPsecSADirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSADirection.setStatus("current")


class _TmnxVRtIPsecSAIndex_Type(Unsigned32):
    """Custom type tmnxVRtIPsecSAIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxVRtIPsecSAIndex_Type.__name__ = "Unsigned32"
_TmnxVRtIPsecSAIndex_Object = MibTableColumn
tmnxVRtIPsecSAIndex = _TmnxVRtIPsecSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 3),
    _TmnxVRtIPsecSAIndex_Type()
)
tmnxVRtIPsecSAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAIndex.setStatus("current")
_TmnxVRtIPsecSARowStatus_Type = RowStatus
_TmnxVRtIPsecSARowStatus_Object = MibTableColumn
tmnxVRtIPsecSARowStatus = _TmnxVRtIPsecSARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 4),
    _TmnxVRtIPsecSARowStatus_Type()
)
tmnxVRtIPsecSARowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSARowStatus.setStatus("current")
_TmnxVRtIPsecSALastChanged_Type = TimeStamp
_TmnxVRtIPsecSALastChanged_Object = MibTableColumn
tmnxVRtIPsecSALastChanged = _TmnxVRtIPsecSALastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 5),
    _TmnxVRtIPsecSALastChanged_Type()
)
tmnxVRtIPsecSALastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSALastChanged.setStatus("current")
_TmnxVRtIPsecSAType_Type = TmnxIPsecKeyingType
_TmnxVRtIPsecSAType_Object = MibTableColumn
tmnxVRtIPsecSAType = _TmnxVRtIPsecSAType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 6),
    _TmnxVRtIPsecSAType_Type()
)
tmnxVRtIPsecSAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAType.setStatus("current")


class _TmnxVRtIPsecSAEncryptionKey_Type(OctetString):
    """Custom type tmnxVRtIPsecSAEncryptionKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxVRtIPsecSAEncryptionKey_Type.__name__ = "OctetString"
_TmnxVRtIPsecSAEncryptionKey_Object = MibTableColumn
tmnxVRtIPsecSAEncryptionKey = _TmnxVRtIPsecSAEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 7),
    _TmnxVRtIPsecSAEncryptionKey_Type()
)
tmnxVRtIPsecSAEncryptionKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAEncryptionKey.setStatus("current")


class _TmnxVRtIPsecSAAuthenticationKey_Type(OctetString):
    """Custom type tmnxVRtIPsecSAAuthenticationKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxVRtIPsecSAAuthenticationKey_Type.__name__ = "OctetString"
_TmnxVRtIPsecSAAuthenticationKey_Object = MibTableColumn
tmnxVRtIPsecSAAuthenticationKey = _TmnxVRtIPsecSAAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 8),
    _TmnxVRtIPsecSAAuthenticationKey_Type()
)
tmnxVRtIPsecSAAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAAuthenticationKey.setStatus("current")
_TmnxVRtIPsecSASpi_Type = Unsigned32
_TmnxVRtIPsecSASpi_Object = MibTableColumn
tmnxVRtIPsecSASpi = _TmnxVRtIPsecSASpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 9),
    _TmnxVRtIPsecSASpi_Type()
)
tmnxVRtIPsecSASpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSASpi.setStatus("current")
_TmnxVRtIPsecSAManualTransformId_Type = TmnxIPsecTransformIdOrZero
_TmnxVRtIPsecSAManualTransformId_Object = MibTableColumn
tmnxVRtIPsecSAManualTransformId = _TmnxVRtIPsecSAManualTransformId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 10),
    _TmnxVRtIPsecSAManualTransformId_Type()
)
tmnxVRtIPsecSAManualTransformId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAManualTransformId.setStatus("current")
_TmnxVRtIPsecSAAuthAlgorithm_Type = TmnxAuthAlgorithm
_TmnxVRtIPsecSAAuthAlgorithm_Object = MibTableColumn
tmnxVRtIPsecSAAuthAlgorithm = _TmnxVRtIPsecSAAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 11),
    _TmnxVRtIPsecSAAuthAlgorithm_Type()
)
tmnxVRtIPsecSAAuthAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAAuthAlgorithm.setStatus("current")
_TmnxVRtIPsecSAEncrAlgorithm_Type = TmnxEncrAlgorithm
_TmnxVRtIPsecSAEncrAlgorithm_Object = MibTableColumn
tmnxVRtIPsecSAEncrAlgorithm = _TmnxVRtIPsecSAEncrAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 12),
    _TmnxVRtIPsecSAEncrAlgorithm_Type()
)
tmnxVRtIPsecSAEncrAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAEncrAlgorithm.setStatus("current")
_TmnxVRtIPsecSAStorageType_Type = StorageType
_TmnxVRtIPsecSAStorageType_Object = MibTableColumn
tmnxVRtIPsecSAStorageType = _TmnxVRtIPsecSAStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 13),
    _TmnxVRtIPsecSAStorageType_Type()
)
tmnxVRtIPsecSAStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStorageType.setStatus("current")
_TmnxVRtIPsecSAEstablishedTime_Type = TimeStamp
_TmnxVRtIPsecSAEstablishedTime_Object = MibTableColumn
tmnxVRtIPsecSAEstablishedTime = _TmnxVRtIPsecSAEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 14),
    _TmnxVRtIPsecSAEstablishedTime_Type()
)
tmnxVRtIPsecSAEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAEstablishedTime.setStatus("current")
_TmnxVRtIPsecSANegotiatedLifeTime_Type = Unsigned32
_TmnxVRtIPsecSANegotiatedLifeTime_Object = MibTableColumn
tmnxVRtIPsecSANegotiatedLifeTime = _TmnxVRtIPsecSANegotiatedLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 113, 1, 15),
    _TmnxVRtIPsecSANegotiatedLifeTime_Type()
)
tmnxVRtIPsecSANegotiatedLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSANegotiatedLifeTime.setStatus("current")
_TmnxVRtIPsecSAStTable_Object = MibTable
tmnxVRtIPsecSAStTable = _TmnxVRtIPsecSAStTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114)
)
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStTable.setStatus("current")
_TmnxVRtIPsecSAStEntry_Object = MibTableRow
tmnxVRtIPsecSAStEntry = _TmnxVRtIPsecSAStEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1)
)
tmnxVRtIPsecSAStEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSADirection"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAIndex"),
)
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStEntry.setStatus("current")
_TmnxVRtIPsecSAStBytesProcessed_Type = Counter64
_TmnxVRtIPsecSAStBytesProcessed_Object = MibTableColumn
tmnxVRtIPsecSAStBytesProcessed = _TmnxVRtIPsecSAStBytesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 1),
    _TmnxVRtIPsecSAStBytesProcessed_Type()
)
tmnxVRtIPsecSAStBytesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStBytesProcessed.setStatus("current")
_TmnxVRtIPsecSAStBytesProcLow32_Type = Counter32
_TmnxVRtIPsecSAStBytesProcLow32_Object = MibTableColumn
tmnxVRtIPsecSAStBytesProcLow32 = _TmnxVRtIPsecSAStBytesProcLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 2),
    _TmnxVRtIPsecSAStBytesProcLow32_Type()
)
tmnxVRtIPsecSAStBytesProcLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStBytesProcLow32.setStatus("current")
_TmnxVRtIPsecSAStBytesProcHigh32_Type = Counter32
_TmnxVRtIPsecSAStBytesProcHigh32_Object = MibTableColumn
tmnxVRtIPsecSAStBytesProcHigh32 = _TmnxVRtIPsecSAStBytesProcHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 3),
    _TmnxVRtIPsecSAStBytesProcHigh32_Type()
)
tmnxVRtIPsecSAStBytesProcHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStBytesProcHigh32.setStatus("current")
_TmnxVRtIPsecSAStPktsProcessed_Type = Counter64
_TmnxVRtIPsecSAStPktsProcessed_Object = MibTableColumn
tmnxVRtIPsecSAStPktsProcessed = _TmnxVRtIPsecSAStPktsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 4),
    _TmnxVRtIPsecSAStPktsProcessed_Type()
)
tmnxVRtIPsecSAStPktsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStPktsProcessed.setStatus("current")
_TmnxVRtIPsecSAStPktsProcLow32_Type = Counter32
_TmnxVRtIPsecSAStPktsProcLow32_Object = MibTableColumn
tmnxVRtIPsecSAStPktsProcLow32 = _TmnxVRtIPsecSAStPktsProcLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 5),
    _TmnxVRtIPsecSAStPktsProcLow32_Type()
)
tmnxVRtIPsecSAStPktsProcLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStPktsProcLow32.setStatus("current")
_TmnxVRtIPsecSAStPktsProcHigh32_Type = Counter32
_TmnxVRtIPsecSAStPktsProcHigh32_Object = MibTableColumn
tmnxVRtIPsecSAStPktsProcHigh32 = _TmnxVRtIPsecSAStPktsProcHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 6),
    _TmnxVRtIPsecSAStPktsProcHigh32_Type()
)
tmnxVRtIPsecSAStPktsProcHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStPktsProcHigh32.setStatus("current")
_TmnxVRtIPsecSAStCryptoErrors_Type = Counter32
_TmnxVRtIPsecSAStCryptoErrors_Object = MibTableColumn
tmnxVRtIPsecSAStCryptoErrors = _TmnxVRtIPsecSAStCryptoErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 7),
    _TmnxVRtIPsecSAStCryptoErrors_Type()
)
tmnxVRtIPsecSAStCryptoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStCryptoErrors.setStatus("current")
_TmnxVRtIPsecSAStReplayErrors_Type = Counter32
_TmnxVRtIPsecSAStReplayErrors_Object = MibTableColumn
tmnxVRtIPsecSAStReplayErrors = _TmnxVRtIPsecSAStReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 8),
    _TmnxVRtIPsecSAStReplayErrors_Type()
)
tmnxVRtIPsecSAStReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStReplayErrors.setStatus("current")
_TmnxVRtIPsecSAStSAErrors_Type = Counter32
_TmnxVRtIPsecSAStSAErrors_Object = MibTableColumn
tmnxVRtIPsecSAStSAErrors = _TmnxVRtIPsecSAStSAErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 9),
    _TmnxVRtIPsecSAStSAErrors_Type()
)
tmnxVRtIPsecSAStSAErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStSAErrors.setStatus("current")
_TmnxVRtIPsecSAStPolicyErrors_Type = Counter32
_TmnxVRtIPsecSAStPolicyErrors_Object = MibTableColumn
tmnxVRtIPsecSAStPolicyErrors = _TmnxVRtIPsecSAStPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 10),
    _TmnxVRtIPsecSAStPolicyErrors_Type()
)
tmnxVRtIPsecSAStPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStPolicyErrors.setStatus("current")
_TmnxVRtIPsecSAStEncapOverhead_Type = Counter32
_TmnxVRtIPsecSAStEncapOverhead_Object = MibTableColumn
tmnxVRtIPsecSAStEncapOverhead = _TmnxVRtIPsecSAStEncapOverhead_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 11),
    _TmnxVRtIPsecSAStEncapOverhead_Type()
)
tmnxVRtIPsecSAStEncapOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStEncapOverhead.setStatus("current")
_TmnxVRtIPsecSAStPreEncapFragCnt_Type = Counter64
_TmnxVRtIPsecSAStPreEncapFragCnt_Object = MibTableColumn
tmnxVRtIPsecSAStPreEncapFragCnt = _TmnxVRtIPsecSAStPreEncapFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 12),
    _TmnxVRtIPsecSAStPreEncapFragCnt_Type()
)
tmnxVRtIPsecSAStPreEncapFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStPreEncapFragCnt.setStatus("current")
_TmnxVRtIPsecSAStPreEncapFragLtSz_Type = Unsigned32
_TmnxVRtIPsecSAStPreEncapFragLtSz_Object = MibTableColumn
tmnxVRtIPsecSAStPreEncapFragLtSz = _TmnxVRtIPsecSAStPreEncapFragLtSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 13),
    _TmnxVRtIPsecSAStPreEncapFragLtSz_Type()
)
tmnxVRtIPsecSAStPreEncapFragLtSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStPreEncapFragLtSz.setStatus("current")
_TmnxVRtIPsecSAStPstEncapFragCnt_Type = Counter64
_TmnxVRtIPsecSAStPstEncapFragCnt_Object = MibTableColumn
tmnxVRtIPsecSAStPstEncapFragCnt = _TmnxVRtIPsecSAStPstEncapFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 14),
    _TmnxVRtIPsecSAStPstEncapFragCnt_Type()
)
tmnxVRtIPsecSAStPstEncapFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStPstEncapFragCnt.setStatus("current")
_TmnxVRtIPsecSAStPstEncapFragLtSz_Type = Unsigned32
_TmnxVRtIPsecSAStPstEncapFragLtSz_Object = MibTableColumn
tmnxVRtIPsecSAStPstEncapFragLtSz = _TmnxVRtIPsecSAStPstEncapFragLtSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 15),
    _TmnxVRtIPsecSAStPstEncapFragLtSz_Type()
)
tmnxVRtIPsecSAStPstEncapFragLtSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStPstEncapFragLtSz.setStatus("current")
_TmnxVRtIPsecSAStTempPrivMtu_Type = Unsigned32
_TmnxVRtIPsecSAStTempPrivMtu_Object = MibTableColumn
tmnxVRtIPsecSAStTempPrivMtu = _TmnxVRtIPsecSAStTempPrivMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 16),
    _TmnxVRtIPsecSAStTempPrivMtu_Type()
)
tmnxVRtIPsecSAStTempPrivMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStTempPrivMtu.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStTempPrivMtu.setUnits("bytes")
_TmnxVRtIPsecSAStPfsDhGroup_Type = TmnxIkePolicyDHGroupOrZero
_TmnxVRtIPsecSAStPfsDhGroup_Object = MibTableColumn
tmnxVRtIPsecSAStPfsDhGroup = _TmnxVRtIPsecSAStPfsDhGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 17),
    _TmnxVRtIPsecSAStPfsDhGroup_Type()
)
tmnxVRtIPsecSAStPfsDhGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStPfsDhGroup.setStatus("current")
_TmnxVRtIPsecSAStMulticastIfName_Type = TNamedItemOrEmpty
_TmnxVRtIPsecSAStMulticastIfName_Object = MibTableColumn
tmnxVRtIPsecSAStMulticastIfName = _TmnxVRtIPsecSAStMulticastIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 18),
    _TmnxVRtIPsecSAStMulticastIfName_Type()
)
tmnxVRtIPsecSAStMulticastIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStMulticastIfName.setStatus("current")
_TmnxVRtIPsecSAStMulticastProt_Type = TIPsecMulticastProtocol
_TmnxVRtIPsecSAStMulticastProt_Object = MibTableColumn
tmnxVRtIPsecSAStMulticastProt = _TmnxVRtIPsecSAStMulticastProt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 114, 1, 19),
    _TmnxVRtIPsecSAStMulticastProt_Type()
)
tmnxVRtIPsecSAStMulticastProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecSAStMulticastProt.setStatus("current")
_TmnxVRtSecPlcyTableLastChanged_Type = TimeStamp
_TmnxVRtSecPlcyTableLastChanged_Object = MibScalar
tmnxVRtSecPlcyTableLastChanged = _TmnxVRtSecPlcyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 115),
    _TmnxVRtSecPlcyTableLastChanged_Type()
)
tmnxVRtSecPlcyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyTableLastChanged.setStatus("current")
_TmnxVRtSecPlcyTable_Object = MibTable
tmnxVRtSecPlcyTable = _TmnxVRtSecPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 116)
)
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyTable.setStatus("current")
_TmnxVRtSecPlcyEntry_Object = MibTableRow
tmnxVRtSecPlcyEntry = _TmnxVRtSecPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 116, 1)
)
tmnxVRtSecPlcyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyId"),
)
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyEntry.setStatus("current")
_TmnxVRtSecPlcyId_Type = TmnxIPsecPolicyId
_TmnxVRtSecPlcyId_Object = MibTableColumn
tmnxVRtSecPlcyId = _TmnxVRtSecPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 116, 1, 1),
    _TmnxVRtSecPlcyId_Type()
)
tmnxVRtSecPlcyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyId.setStatus("current")
_TmnxVRtSecPlcyRowStatus_Type = RowStatus
_TmnxVRtSecPlcyRowStatus_Object = MibTableColumn
tmnxVRtSecPlcyRowStatus = _TmnxVRtSecPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 116, 1, 2),
    _TmnxVRtSecPlcyRowStatus_Type()
)
tmnxVRtSecPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyRowStatus.setStatus("current")
_TmnxVRtSecPlcyLastChanged_Type = TimeStamp
_TmnxVRtSecPlcyLastChanged_Object = MibTableColumn
tmnxVRtSecPlcyLastChanged = _TmnxVRtSecPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 116, 1, 3),
    _TmnxVRtSecPlcyLastChanged_Type()
)
tmnxVRtSecPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyLastChanged.setStatus("current")
_TmnxVRtSecPlcyParamTblLastChangd_Type = TimeStamp
_TmnxVRtSecPlcyParamTblLastChangd_Object = MibScalar
tmnxVRtSecPlcyParamTblLastChangd = _TmnxVRtSecPlcyParamTblLastChangd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 117),
    _TmnxVRtSecPlcyParamTblLastChangd_Type()
)
tmnxVRtSecPlcyParamTblLastChangd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamTblLastChangd.setStatus("current")
_TmnxVRtSecPlcyParamTable_Object = MibTable
tmnxVRtSecPlcyParamTable = _TmnxVRtSecPlcyParamTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118)
)
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamTable.setStatus("current")
_TmnxVRtSecPlcyParamEntry_Object = MibTableRow
tmnxVRtSecPlcyParamEntry = _TmnxVRtSecPlcyParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1)
)
tmnxVRtSecPlcyParamEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParamId"),
)
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamEntry.setStatus("current")


class _TmnxVRtSecPlcyParamId_Type(Unsigned32):
    """Custom type tmnxVRtSecPlcyParamId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxVRtSecPlcyParamId_Type.__name__ = "Unsigned32"
_TmnxVRtSecPlcyParamId_Object = MibTableColumn
tmnxVRtSecPlcyParamId = _TmnxVRtSecPlcyParamId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 1),
    _TmnxVRtSecPlcyParamId_Type()
)
tmnxVRtSecPlcyParamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamId.setStatus("current")
_TmnxVRtSecPlcyParamRowStatus_Type = RowStatus
_TmnxVRtSecPlcyParamRowStatus_Object = MibTableColumn
tmnxVRtSecPlcyParamRowStatus = _TmnxVRtSecPlcyParamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 2),
    _TmnxVRtSecPlcyParamRowStatus_Type()
)
tmnxVRtSecPlcyParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamRowStatus.setStatus("current")
_TmnxVRtSecPlcyParamLastChanged_Type = TimeStamp
_TmnxVRtSecPlcyParamLastChanged_Object = MibTableColumn
tmnxVRtSecPlcyParamLastChanged = _TmnxVRtSecPlcyParamLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 3),
    _TmnxVRtSecPlcyParamLastChanged_Type()
)
tmnxVRtSecPlcyParamLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamLastChanged.setStatus("current")


class _TmnxVRtSecPlcyParamLclAddrAny_Type(TruthValue):
    """Custom type tmnxVRtSecPlcyParamLclAddrAny based on TruthValue"""
    defaultValue = 2


_TmnxVRtSecPlcyParamLclAddrAny_Type.__name__ = "TruthValue"
_TmnxVRtSecPlcyParamLclAddrAny_Object = MibTableColumn
tmnxVRtSecPlcyParamLclAddrAny = _TmnxVRtSecPlcyParamLclAddrAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 4),
    _TmnxVRtSecPlcyParamLclAddrAny_Type()
)
tmnxVRtSecPlcyParamLclAddrAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamLclAddrAny.setStatus("current")


class _TmnxVRtSecPlcyParamLclAddrType_Type(InetAddressType):
    """Custom type tmnxVRtSecPlcyParamLclAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxVRtSecPlcyParamLclAddrType_Type.__name__ = "InetAddressType"
_TmnxVRtSecPlcyParamLclAddrType_Object = MibTableColumn
tmnxVRtSecPlcyParamLclAddrType = _TmnxVRtSecPlcyParamLclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 5),
    _TmnxVRtSecPlcyParamLclAddrType_Type()
)
tmnxVRtSecPlcyParamLclAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamLclAddrType.setStatus("current")


class _TmnxVRtSecPlcyParamLclAddr_Type(InetAddress):
    """Custom type tmnxVRtSecPlcyParamLclAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxVRtSecPlcyParamLclAddr_Type.__name__ = "InetAddress"
_TmnxVRtSecPlcyParamLclAddr_Object = MibTableColumn
tmnxVRtSecPlcyParamLclAddr = _TmnxVRtSecPlcyParamLclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 6),
    _TmnxVRtSecPlcyParamLclAddr_Type()
)
tmnxVRtSecPlcyParamLclAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamLclAddr.setStatus("current")


class _TmnxVRtSecPlcyParamLclAPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxVRtSecPlcyParamLclAPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxVRtSecPlcyParamLclAPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxVRtSecPlcyParamLclAPrefLen_Object = MibTableColumn
tmnxVRtSecPlcyParamLclAPrefLen = _TmnxVRtSecPlcyParamLclAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 7),
    _TmnxVRtSecPlcyParamLclAPrefLen_Type()
)
tmnxVRtSecPlcyParamLclAPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamLclAPrefLen.setStatus("current")


class _TmnxVRtSecPlcyParamRemAddrAny_Type(TruthValue):
    """Custom type tmnxVRtSecPlcyParamRemAddrAny based on TruthValue"""
    defaultValue = 2


_TmnxVRtSecPlcyParamRemAddrAny_Type.__name__ = "TruthValue"
_TmnxVRtSecPlcyParamRemAddrAny_Object = MibTableColumn
tmnxVRtSecPlcyParamRemAddrAny = _TmnxVRtSecPlcyParamRemAddrAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 8),
    _TmnxVRtSecPlcyParamRemAddrAny_Type()
)
tmnxVRtSecPlcyParamRemAddrAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamRemAddrAny.setStatus("current")


class _TmnxVRtSecPlcyParamRemAddrType_Type(InetAddressType):
    """Custom type tmnxVRtSecPlcyParamRemAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxVRtSecPlcyParamRemAddrType_Type.__name__ = "InetAddressType"
_TmnxVRtSecPlcyParamRemAddrType_Object = MibTableColumn
tmnxVRtSecPlcyParamRemAddrType = _TmnxVRtSecPlcyParamRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 9),
    _TmnxVRtSecPlcyParamRemAddrType_Type()
)
tmnxVRtSecPlcyParamRemAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamRemAddrType.setStatus("current")


class _TmnxVRtSecPlcyParamRemAddr_Type(InetAddress):
    """Custom type tmnxVRtSecPlcyParamRemAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxVRtSecPlcyParamRemAddr_Type.__name__ = "InetAddress"
_TmnxVRtSecPlcyParamRemAddr_Object = MibTableColumn
tmnxVRtSecPlcyParamRemAddr = _TmnxVRtSecPlcyParamRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 10),
    _TmnxVRtSecPlcyParamRemAddr_Type()
)
tmnxVRtSecPlcyParamRemAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamRemAddr.setStatus("current")


class _TmnxVRtSecPlcyParamRemAPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxVRtSecPlcyParamRemAPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxVRtSecPlcyParamRemAPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxVRtSecPlcyParamRemAPrefLen_Object = MibTableColumn
tmnxVRtSecPlcyParamRemAPrefLen = _TmnxVRtSecPlcyParamRemAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 11),
    _TmnxVRtSecPlcyParamRemAPrefLen_Type()
)
tmnxVRtSecPlcyParamRemAPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParamRemAPrefLen.setStatus("current")


class _TmnxVRtSecPlcyParam6LclAddrAny_Type(TruthValue):
    """Custom type tmnxVRtSecPlcyParam6LclAddrAny based on TruthValue"""
    defaultValue = 2


_TmnxVRtSecPlcyParam6LclAddrAny_Type.__name__ = "TruthValue"
_TmnxVRtSecPlcyParam6LclAddrAny_Object = MibTableColumn
tmnxVRtSecPlcyParam6LclAddrAny = _TmnxVRtSecPlcyParam6LclAddrAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 12),
    _TmnxVRtSecPlcyParam6LclAddrAny_Type()
)
tmnxVRtSecPlcyParam6LclAddrAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParam6LclAddrAny.setStatus("current")


class _TmnxVRtSecPlcyParam6LclAddrType_Type(InetAddressType):
    """Custom type tmnxVRtSecPlcyParam6LclAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxVRtSecPlcyParam6LclAddrType_Type.__name__ = "InetAddressType"
_TmnxVRtSecPlcyParam6LclAddrType_Object = MibTableColumn
tmnxVRtSecPlcyParam6LclAddrType = _TmnxVRtSecPlcyParam6LclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 13),
    _TmnxVRtSecPlcyParam6LclAddrType_Type()
)
tmnxVRtSecPlcyParam6LclAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParam6LclAddrType.setStatus("current")


class _TmnxVRtSecPlcyParam6LclAddr_Type(InetAddress):
    """Custom type tmnxVRtSecPlcyParam6LclAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxVRtSecPlcyParam6LclAddr_Type.__name__ = "InetAddress"
_TmnxVRtSecPlcyParam6LclAddr_Object = MibTableColumn
tmnxVRtSecPlcyParam6LclAddr = _TmnxVRtSecPlcyParam6LclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 14),
    _TmnxVRtSecPlcyParam6LclAddr_Type()
)
tmnxVRtSecPlcyParam6LclAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParam6LclAddr.setStatus("current")


class _TmnxVRtSecPlcyParam6LclAPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxVRtSecPlcyParam6LclAPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 128),
    )


_TmnxVRtSecPlcyParam6LclAPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxVRtSecPlcyParam6LclAPrefLen_Object = MibTableColumn
tmnxVRtSecPlcyParam6LclAPrefLen = _TmnxVRtSecPlcyParam6LclAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 15),
    _TmnxVRtSecPlcyParam6LclAPrefLen_Type()
)
tmnxVRtSecPlcyParam6LclAPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParam6LclAPrefLen.setStatus("current")


class _TmnxVRtSecPlcyParam6RemAddrAny_Type(TruthValue):
    """Custom type tmnxVRtSecPlcyParam6RemAddrAny based on TruthValue"""
    defaultValue = 2


_TmnxVRtSecPlcyParam6RemAddrAny_Type.__name__ = "TruthValue"
_TmnxVRtSecPlcyParam6RemAddrAny_Object = MibTableColumn
tmnxVRtSecPlcyParam6RemAddrAny = _TmnxVRtSecPlcyParam6RemAddrAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 16),
    _TmnxVRtSecPlcyParam6RemAddrAny_Type()
)
tmnxVRtSecPlcyParam6RemAddrAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParam6RemAddrAny.setStatus("current")


class _TmnxVRtSecPlcyParam6RemAddrType_Type(InetAddressType):
    """Custom type tmnxVRtSecPlcyParam6RemAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxVRtSecPlcyParam6RemAddrType_Type.__name__ = "InetAddressType"
_TmnxVRtSecPlcyParam6RemAddrType_Object = MibTableColumn
tmnxVRtSecPlcyParam6RemAddrType = _TmnxVRtSecPlcyParam6RemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 17),
    _TmnxVRtSecPlcyParam6RemAddrType_Type()
)
tmnxVRtSecPlcyParam6RemAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParam6RemAddrType.setStatus("current")


class _TmnxVRtSecPlcyParam6RemAddr_Type(InetAddress):
    """Custom type tmnxVRtSecPlcyParam6RemAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxVRtSecPlcyParam6RemAddr_Type.__name__ = "InetAddress"
_TmnxVRtSecPlcyParam6RemAddr_Object = MibTableColumn
tmnxVRtSecPlcyParam6RemAddr = _TmnxVRtSecPlcyParam6RemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 18),
    _TmnxVRtSecPlcyParam6RemAddr_Type()
)
tmnxVRtSecPlcyParam6RemAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParam6RemAddr.setStatus("current")


class _TmnxVRtSecPlcyParam6RemAPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxVRtSecPlcyParam6RemAPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 128),
    )


_TmnxVRtSecPlcyParam6RemAPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxVRtSecPlcyParam6RemAPrefLen_Object = MibTableColumn
tmnxVRtSecPlcyParam6RemAPrefLen = _TmnxVRtSecPlcyParam6RemAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 118, 1, 19),
    _TmnxVRtSecPlcyParam6RemAPrefLen_Type()
)
tmnxVRtSecPlcyParam6RemAPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtSecPlcyParam6RemAPrefLen.setStatus("current")
_TmnxVRtIfIPsecTblLstCgd_Type = TimeStamp
_TmnxVRtIfIPsecTblLstCgd_Object = MibScalar
tmnxVRtIfIPsecTblLstCgd = _TmnxVRtIfIPsecTblLstCgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 119),
    _TmnxVRtIfIPsecTblLstCgd_Type()
)
tmnxVRtIfIPsecTblLstCgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIfIPsecTblLstCgd.setStatus("current")
_TmnxVRtIfIPsecTable_Object = MibTable
tmnxVRtIfIPsecTable = _TmnxVRtIfIPsecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 120)
)
if mibBuilder.loadTexts:
    tmnxVRtIfIPsecTable.setStatus("current")
_TmnxVRtIfIPsecEntry_Object = MibTableRow
tmnxVRtIfIPsecEntry = _TmnxVRtIfIPsecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 120, 1)
)
tmnxVRtIfIPsecEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxVRtIfIPsecEntry.setStatus("current")
_TmnxVRtIfIPsecRowStatus_Type = RowStatus
_TmnxVRtIfIPsecRowStatus_Object = MibTableColumn
tmnxVRtIfIPsecRowStatus = _TmnxVRtIfIPsecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 120, 1, 1),
    _TmnxVRtIfIPsecRowStatus_Type()
)
tmnxVRtIfIPsecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIfIPsecRowStatus.setStatus("current")
_TmnxVRtIfIPsecLastChgd_Type = TimeStamp
_TmnxVRtIfIPsecLastChgd_Object = MibTableColumn
tmnxVRtIfIPsecLastChgd = _TmnxVRtIfIPsecLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 120, 1, 2),
    _TmnxVRtIfIPsecLastChgd_Type()
)
tmnxVRtIfIPsecLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIfIPsecLastChgd.setStatus("current")


class _TmnxVRtIfIPsecAdminState_Type(TmnxAdminState):
    """Custom type tmnxVRtIfIPsecAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxVRtIfIPsecAdminState_Type.__name__ = "TmnxAdminState"
_TmnxVRtIfIPsecAdminState_Object = MibTableColumn
tmnxVRtIfIPsecAdminState = _TmnxVRtIfIPsecAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 120, 1, 3),
    _TmnxVRtIfIPsecAdminState_Type()
)
tmnxVRtIfIPsecAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIfIPsecAdminState.setStatus("current")


class _TmnxVRtIfIPsecIpFilterInExcptId_Type(TFilterID):
    """Custom type tmnxVRtIfIPsecIpFilterInExcptId based on TFilterID"""
    defaultValue = 0


_TmnxVRtIfIPsecIpFilterInExcptId_Type.__name__ = "TFilterID"
_TmnxVRtIfIPsecIpFilterInExcptId_Object = MibTableColumn
tmnxVRtIfIPsecIpFilterInExcptId = _TmnxVRtIfIPsecIpFilterInExcptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 120, 1, 4),
    _TmnxVRtIfIPsecIpFilterInExcptId_Type()
)
tmnxVRtIfIPsecIpFilterInExcptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIfIPsecIpFilterInExcptId.setStatus("current")


class _TmnxVRtIfIPsecIsaTnlGroup_Type(TmnxTunnelGroupIdOrZero):
    """Custom type tmnxVRtIfIPsecIsaTnlGroup based on TmnxTunnelGroupIdOrZero"""
    defaultValue = 0


_TmnxVRtIfIPsecIsaTnlGroup_Type.__name__ = "TmnxTunnelGroupIdOrZero"
_TmnxVRtIfIPsecIsaTnlGroup_Object = MibTableColumn
tmnxVRtIfIPsecIsaTnlGroup = _TmnxVRtIfIPsecIsaTnlGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 120, 1, 5),
    _TmnxVRtIfIPsecIsaTnlGroup_Type()
)
tmnxVRtIfIPsecIsaTnlGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIfIPsecIsaTnlGroup.setStatus("current")


class _TmnxVRtIfIPsecPubSap_Type(Unsigned32):
    """Custom type tmnxVRtIfIPsecPubSap based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TmnxVRtIfIPsecPubSap_Type.__name__ = "Unsigned32"
_TmnxVRtIfIPsecPubSap_Object = MibTableColumn
tmnxVRtIfIPsecPubSap = _TmnxVRtIfIPsecPubSap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 120, 1, 6),
    _TmnxVRtIfIPsecPubSap_Type()
)
tmnxVRtIfIPsecPubSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIfIPsecPubSap.setStatus("current")


class _TmnxVRtIfIPsecIpv6FilterInExcId_Type(TFilterID):
    """Custom type tmnxVRtIfIPsecIpv6FilterInExcId based on TFilterID"""
    defaultValue = 0


_TmnxVRtIfIPsecIpv6FilterInExcId_Type.__name__ = "TFilterID"
_TmnxVRtIfIPsecIpv6FilterInExcId_Object = MibTableColumn
tmnxVRtIfIPsecIpv6FilterInExcId = _TmnxVRtIfIPsecIpv6FilterInExcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 120, 1, 7),
    _TmnxVRtIfIPsecIpv6FilterInExcId_Type()
)
tmnxVRtIfIPsecIpv6FilterInExcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVRtIfIPsecIpv6FilterInExcId.setStatus("current")
_TmnxVRtIPsecTnlStatsTable_Object = MibTable
tmnxVRtIPsecTnlStatsTable = _TmnxVRtIPsecTnlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121)
)
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlStatsTable.setStatus("current")
_TmnxVRtIPsecTnlStatsEntry_Object = MibTableRow
tmnxVRtIPsecTnlStatsEntry = _TmnxVRtIPsecTnlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1)
)
tmnxVRtIPsecTnlStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlName"),
)
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlStatsEntry.setStatus("current")


class _TmnxVRtIPsecTnlIsakmpState_Type(Integer32):
    """Custom type tmnxVRtIPsecTnlIsakmpState based on Integer32"""
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


_TmnxVRtIPsecTnlIsakmpState_Type.__name__ = "Integer32"
_TmnxVRtIPsecTnlIsakmpState_Object = MibTableColumn
tmnxVRtIPsecTnlIsakmpState = _TmnxVRtIPsecTnlIsakmpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 1),
    _TmnxVRtIPsecTnlIsakmpState_Type()
)
tmnxVRtIPsecTnlIsakmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIsakmpState.setStatus("current")
_TmnxVRtIPsecTnlIsakmpEstabTime_Type = TimeStamp
_TmnxVRtIPsecTnlIsakmpEstabTime_Object = MibTableColumn
tmnxVRtIPsecTnlIsakmpEstabTime = _TmnxVRtIPsecTnlIsakmpEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 2),
    _TmnxVRtIPsecTnlIsakmpEstabTime_Type()
)
tmnxVRtIPsecTnlIsakmpEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIsakmpEstabTime.setStatus("current")
_TmnxVRtIPsecTnlIsakmpNegLifeTime_Type = Unsigned32
_TmnxVRtIPsecTnlIsakmpNegLifeTime_Object = MibTableColumn
tmnxVRtIPsecTnlIsakmpNegLifeTime = _TmnxVRtIPsecTnlIsakmpNegLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 3),
    _TmnxVRtIPsecTnlIsakmpNegLifeTime_Type()
)
tmnxVRtIPsecTnlIsakmpNegLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlIsakmpNegLifeTime.setStatus("current")
_TmnxVRtIPsecTnlNumDpdTx_Type = Counter32
_TmnxVRtIPsecTnlNumDpdTx_Object = MibTableColumn
tmnxVRtIPsecTnlNumDpdTx = _TmnxVRtIPsecTnlNumDpdTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 4),
    _TmnxVRtIPsecTnlNumDpdTx_Type()
)
tmnxVRtIPsecTnlNumDpdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlNumDpdTx.setStatus("current")
_TmnxVRtIPsecTnlNumDpdRx_Type = Counter32
_TmnxVRtIPsecTnlNumDpdRx_Object = MibTableColumn
tmnxVRtIPsecTnlNumDpdRx = _TmnxVRtIPsecTnlNumDpdRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 5),
    _TmnxVRtIPsecTnlNumDpdRx_Type()
)
tmnxVRtIPsecTnlNumDpdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlNumDpdRx.setStatus("current")
_TmnxVRtIPsecTnlNumDpdAckTx_Type = Counter32
_TmnxVRtIPsecTnlNumDpdAckTx_Object = MibTableColumn
tmnxVRtIPsecTnlNumDpdAckTx = _TmnxVRtIPsecTnlNumDpdAckTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 6),
    _TmnxVRtIPsecTnlNumDpdAckTx_Type()
)
tmnxVRtIPsecTnlNumDpdAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlNumDpdAckTx.setStatus("current")
_TmnxVRtIPsecTnlNumDpdAckRx_Type = Counter32
_TmnxVRtIPsecTnlNumDpdAckRx_Object = MibTableColumn
tmnxVRtIPsecTnlNumDpdAckRx = _TmnxVRtIPsecTnlNumDpdAckRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 7),
    _TmnxVRtIPsecTnlNumDpdAckRx_Type()
)
tmnxVRtIPsecTnlNumDpdAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlNumDpdAckRx.setStatus("current")
_TmnxVRtIPsecTnlNumExpRx_Type = Counter32
_TmnxVRtIPsecTnlNumExpRx_Object = MibTableColumn
tmnxVRtIPsecTnlNumExpRx = _TmnxVRtIPsecTnlNumExpRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 8),
    _TmnxVRtIPsecTnlNumExpRx_Type()
)
tmnxVRtIPsecTnlNumExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlNumExpRx.setStatus("current")
_TmnxVRtIPsecTnlNumInvalidDpdRx_Type = Counter32
_TmnxVRtIPsecTnlNumInvalidDpdRx_Object = MibTableColumn
tmnxVRtIPsecTnlNumInvalidDpdRx = _TmnxVRtIPsecTnlNumInvalidDpdRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 9),
    _TmnxVRtIPsecTnlNumInvalidDpdRx_Type()
)
tmnxVRtIPsecTnlNumInvalidDpdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlNumInvalidDpdRx.setStatus("current")
_TmnxVRtIPsecTnlNumCtrlPktsTx_Type = Counter32
_TmnxVRtIPsecTnlNumCtrlPktsTx_Object = MibTableColumn
tmnxVRtIPsecTnlNumCtrlPktsTx = _TmnxVRtIPsecTnlNumCtrlPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 10),
    _TmnxVRtIPsecTnlNumCtrlPktsTx_Type()
)
tmnxVRtIPsecTnlNumCtrlPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlNumCtrlPktsTx.setStatus("current")
_TmnxVRtIPsecTnlNumCtrlPktsRx_Type = Counter32
_TmnxVRtIPsecTnlNumCtrlPktsRx_Object = MibTableColumn
tmnxVRtIPsecTnlNumCtrlPktsRx = _TmnxVRtIPsecTnlNumCtrlPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 11),
    _TmnxVRtIPsecTnlNumCtrlPktsRx_Type()
)
tmnxVRtIPsecTnlNumCtrlPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlNumCtrlPktsRx.setStatus("current")
_TmnxVRtIPsecTnlNumCtrlTxErrors_Type = Counter32
_TmnxVRtIPsecTnlNumCtrlTxErrors_Object = MibTableColumn
tmnxVRtIPsecTnlNumCtrlTxErrors = _TmnxVRtIPsecTnlNumCtrlTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 12),
    _TmnxVRtIPsecTnlNumCtrlTxErrors_Type()
)
tmnxVRtIPsecTnlNumCtrlTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlNumCtrlTxErrors.setStatus("current")
_TmnxVRtIPsecTnlNumCtrlRxErrors_Type = Counter32
_TmnxVRtIPsecTnlNumCtrlRxErrors_Object = MibTableColumn
tmnxVRtIPsecTnlNumCtrlRxErrors = _TmnxVRtIPsecTnlNumCtrlRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 13),
    _TmnxVRtIPsecTnlNumCtrlRxErrors_Type()
)
tmnxVRtIPsecTnlNumCtrlRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlNumCtrlRxErrors.setStatus("current")
_TmnxVRtIPsecTnlMatCertEntryId_Type = Integer32
_TmnxVRtIPsecTnlMatCertEntryId_Object = MibTableColumn
tmnxVRtIPsecTnlMatCertEntryId = _TmnxVRtIPsecTnlMatCertEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 14),
    _TmnxVRtIPsecTnlMatCertEntryId_Type()
)
tmnxVRtIPsecTnlMatCertEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlMatCertEntryId.setStatus("current")
_TmnxVRtIPsecTnlCertProfName_Type = TNamedItemOrEmpty
_TmnxVRtIPsecTnlCertProfName_Object = MibTableColumn
tmnxVRtIPsecTnlCertProfName = _TmnxVRtIPsecTnlCertProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 15),
    _TmnxVRtIPsecTnlCertProfName_Type()
)
tmnxVRtIPsecTnlCertProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlCertProfName.setStatus("current")
_TmnxVRtIPsecTnlStatIsakmpAuthAlg_Type = TmnxAuthAlgorithm
_TmnxVRtIPsecTnlStatIsakmpAuthAlg_Object = MibTableColumn
tmnxVRtIPsecTnlStatIsakmpAuthAlg = _TmnxVRtIPsecTnlStatIsakmpAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 17),
    _TmnxVRtIPsecTnlStatIsakmpAuthAlg_Type()
)
tmnxVRtIPsecTnlStatIsakmpAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlStatIsakmpAuthAlg.setStatus("current")
_TmnxVRtIPsecTnlStatIsakmpEncrAlg_Type = TmnxEncrAlgorithm
_TmnxVRtIPsecTnlStatIsakmpEncrAlg_Object = MibTableColumn
tmnxVRtIPsecTnlStatIsakmpEncrAlg = _TmnxVRtIPsecTnlStatIsakmpEncrAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 18),
    _TmnxVRtIPsecTnlStatIsakmpEncrAlg_Type()
)
tmnxVRtIPsecTnlStatIsakmpEncrAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlStatIsakmpEncrAlg.setStatus("current")
_TmnxVRtIPsecTnlStatIsakmpPfsDhGp_Type = TmnxIkePolicyDHGroupOrZero
_TmnxVRtIPsecTnlStatIsakmpPfsDhGp_Object = MibTableColumn
tmnxVRtIPsecTnlStatIsakmpPfsDhGp = _TmnxVRtIPsecTnlStatIsakmpPfsDhGp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 19),
    _TmnxVRtIPsecTnlStatIsakmpPfsDhGp_Type()
)
tmnxVRtIPsecTnlStatIsakmpPfsDhGp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlStatIsakmpPfsDhGp.setStatus("current")


class _TmnxVRtIPsecTnlStatIkeTranPrfAlg_Type(Integer32):
    """Custom type tmnxVRtIPsecTnlStatIkeTranPrfAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("sha1", 3),
          ("sha256", 4),
          ("sha384", 5),
          ("sha512", 6),
          ("aesXcbc", 7),
          ("sameAsAuth", 8))
    )


_TmnxVRtIPsecTnlStatIkeTranPrfAlg_Type.__name__ = "Integer32"
_TmnxVRtIPsecTnlStatIkeTranPrfAlg_Object = MibTableColumn
tmnxVRtIPsecTnlStatIkeTranPrfAlg = _TmnxVRtIPsecTnlStatIkeTranPrfAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 121, 1, 20),
    _TmnxVRtIPsecTnlStatIkeTranPrfAlg_Type()
)
tmnxVRtIPsecTnlStatIkeTranPrfAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVRtIPsecTnlStatIkeTranPrfAlg.setStatus("current")
_TmnxIPsecLOClientEsaTable_Object = MibTable
tmnxIPsecLOClientEsaTable = _TmnxIPsecLOClientEsaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 122)
)
if mibBuilder.loadTexts:
    tmnxIPsecLOClientEsaTable.setStatus("current")
_TmnxIPsecLOClientEsaEntry_Object = MibTableRow
tmnxIPsecLOClientEsaEntry = _TmnxIPsecLOClientEsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 122, 1)
)
tmnxIPsecLOClientEsaEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxEsaId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxEsaVmId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientRtrId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientLclGwAddrT"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientLclGwAddr"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientAddressTyp"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientPort"),
)
if mibBuilder.loadTexts:
    tmnxIPsecLOClientEsaEntry.setStatus("current")
_TmnxIPsecLOClientEsaStatus_Type = TruthValue
_TmnxIPsecLOClientEsaStatus_Object = MibTableColumn
tmnxIPsecLOClientEsaStatus = _TmnxIPsecLOClientEsaStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 122, 1, 1),
    _TmnxIPsecLOClientEsaStatus_Type()
)
tmnxIPsecLOClientEsaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecLOClientEsaStatus.setStatus("current")
_TmnxIPsecLOClientEsaFailAtempt_Type = Unsigned32
_TmnxIPsecLOClientEsaFailAtempt_Object = MibTableColumn
tmnxIPsecLOClientEsaFailAtempt = _TmnxIPsecLOClientEsaFailAtempt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 122, 1, 2),
    _TmnxIPsecLOClientEsaFailAtempt_Type()
)
tmnxIPsecLOClientEsaFailAtempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecLOClientEsaFailAtempt.setStatus("current")
_TmnxIPsecLOClientEsaDroppedPkt_Type = Unsigned32
_TmnxIPsecLOClientEsaDroppedPkt_Object = MibTableColumn
tmnxIPsecLOClientEsaDroppedPkt = _TmnxIPsecLOClientEsaDroppedPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 122, 1, 3),
    _TmnxIPsecLOClientEsaDroppedPkt_Type()
)
tmnxIPsecLOClientEsaDroppedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecLOClientEsaDroppedPkt.setStatus("current")
_TmnxIPsecLOClientEsaRemainTime_Type = Integer32
_TmnxIPsecLOClientEsaRemainTime_Object = MibTableColumn
tmnxIPsecLOClientEsaRemainTime = _TmnxIPsecLOClientEsaRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 122, 1, 4),
    _TmnxIPsecLOClientEsaRemainTime_Type()
)
tmnxIPsecLOClientEsaRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecLOClientEsaRemainTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecLOClientEsaRemainTime.setUnits("seconds")
_TmnxIPsecEsaHistStatsTable_Object = MibTable
tmnxIPsecEsaHistStatsTable = _TmnxIPsecEsaHistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 123)
)
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsTable.setStatus("current")
_TmnxIPsecEsaHistStatsEntry_Object = MibTableRow
tmnxIPsecEsaHistStatsEntry = _TmnxIPsecEsaHistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 123, 1)
)
tmnxIPsecEsaHistStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxEsaId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxEsaVmId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecEsaHistStatsType"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecEsaHistStatsIntvIdx"),
)
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsEntry.setStatus("current")
_TmnxIPsecEsaHistStatsType_Type = TmnxIPsecHistStatsType
_TmnxIPsecEsaHistStatsType_Object = MibTableColumn
tmnxIPsecEsaHistStatsType = _TmnxIPsecEsaHistStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 123, 1, 1),
    _TmnxIPsecEsaHistStatsType_Type()
)
tmnxIPsecEsaHistStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsType.setStatus("current")
_TmnxIPsecEsaHistStatsIntvIdx_Type = Unsigned32
_TmnxIPsecEsaHistStatsIntvIdx_Object = MibTableColumn
tmnxIPsecEsaHistStatsIntvIdx = _TmnxIPsecEsaHistStatsIntvIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 123, 1, 2),
    _TmnxIPsecEsaHistStatsIntvIdx_Type()
)
tmnxIPsecEsaHistStatsIntvIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsIntvIdx.setStatus("current")
_TmnxIPsecEsaHistStatsValue64_Type = CounterBasedGauge64
_TmnxIPsecEsaHistStatsValue64_Object = MibTableColumn
tmnxIPsecEsaHistStatsValue64 = _TmnxIPsecEsaHistStatsValue64_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 123, 1, 3),
    _TmnxIPsecEsaHistStatsValue64_Type()
)
tmnxIPsecEsaHistStatsValue64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsValue64.setStatus("current")
_TmnxIPsecEsaHistStatsValue32_Type = Integer32
_TmnxIPsecEsaHistStatsValue32_Object = MibTableColumn
tmnxIPsecEsaHistStatsValue32 = _TmnxIPsecEsaHistStatsValue32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 123, 1, 4),
    _TmnxIPsecEsaHistStatsValue32_Type()
)
tmnxIPsecEsaHistStatsValue32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsValue32.setStatus("current")
_TmnxIPsecEsaHistStatsIntvStTm_Type = DateAndTime
_TmnxIPsecEsaHistStatsIntvStTm_Object = MibTableColumn
tmnxIPsecEsaHistStatsIntvStTm = _TmnxIPsecEsaHistStatsIntvStTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 123, 1, 5),
    _TmnxIPsecEsaHistStatsIntvStTm_Type()
)
tmnxIPsecEsaHistStatsIntvStTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsIntvStTm.setStatus("current")
_TmnxIPsecEsaHistStatsIntvDur_Type = Unsigned32
_TmnxIPsecEsaHistStatsIntvDur_Object = MibTableColumn
tmnxIPsecEsaHistStatsIntvDur = _TmnxIPsecEsaHistStatsIntvDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 123, 1, 6),
    _TmnxIPsecEsaHistStatsIntvDur_Type()
)
tmnxIPsecEsaHistStatsIntvDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsIntvDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsIntvDur.setUnits("seconds")
_TmnxIPsecEsaHistStatsFstFTm_Type = DateAndTime
_TmnxIPsecEsaHistStatsFstFTm_Object = MibTableColumn
tmnxIPsecEsaHistStatsFstFTm = _TmnxIPsecEsaHistStatsFstFTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 123, 1, 7),
    _TmnxIPsecEsaHistStatsFstFTm_Type()
)
tmnxIPsecEsaHistStatsFstFTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsFstFTm.setStatus("current")


class _TmnxIPsecEsaHistStatsFstFDesc_Type(TItemLongDescription):
    """Custom type tmnxIPsecEsaHistStatsFstFDesc based on TItemLongDescription"""
    subtypeSpec = TItemLongDescription.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_TmnxIPsecEsaHistStatsFstFDesc_Type.__name__ = "TItemLongDescription"
_TmnxIPsecEsaHistStatsFstFDesc_Object = MibTableColumn
tmnxIPsecEsaHistStatsFstFDesc = _TmnxIPsecEsaHistStatsFstFDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 123, 1, 8),
    _TmnxIPsecEsaHistStatsFstFDesc_Type()
)
tmnxIPsecEsaHistStatsFstFDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsFstFDesc.setStatus("current")
_TmnxIPsecEsaHistStatsLstFTm_Type = DateAndTime
_TmnxIPsecEsaHistStatsLstFTm_Object = MibTableColumn
tmnxIPsecEsaHistStatsLstFTm = _TmnxIPsecEsaHistStatsLstFTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 123, 1, 9),
    _TmnxIPsecEsaHistStatsLstFTm_Type()
)
tmnxIPsecEsaHistStatsLstFTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsLstFTm.setStatus("current")


class _TmnxIPsecEsaHistStatsLstFDesc_Type(TItemLongDescription):
    """Custom type tmnxIPsecEsaHistStatsLstFDesc based on TItemLongDescription"""
    subtypeSpec = TItemLongDescription.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_TmnxIPsecEsaHistStatsLstFDesc_Type.__name__ = "TItemLongDescription"
_TmnxIPsecEsaHistStatsLstFDesc_Object = MibTableColumn
tmnxIPsecEsaHistStatsLstFDesc = _TmnxIPsecEsaHistStatsLstFDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 123, 1, 10),
    _TmnxIPsecEsaHistStatsLstFDesc_Type()
)
tmnxIPsecEsaHistStatsLstFDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaHistStatsLstFDesc.setStatus("current")
_TmnxIPsecEsaDpStatsTable_Object = MibTable
tmnxIPsecEsaDpStatsTable = _TmnxIPsecEsaDpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124)
)
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsTable.setStatus("current")
_TmnxIPsecEsaDpStatsEntry_Object = MibTableRow
tmnxIPsecEsaDpStatsEntry = _TmnxIPsecEsaDpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1)
)
tmnxIPsecEsaDpStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxEsaId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxEsaVmId"),
)
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsEntry.setStatus("current")
_TmnxIPsecEsaDpStatsEncryptPkts_Type = Counter64
_TmnxIPsecEsaDpStatsEncryptPkts_Object = MibTableColumn
tmnxIPsecEsaDpStatsEncryptPkts = _TmnxIPsecEsaDpStatsEncryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 1),
    _TmnxIPsecEsaDpStatsEncryptPkts_Type()
)
tmnxIPsecEsaDpStatsEncryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsEncryptPkts.setStatus("current")
_TmnxIPsecEsaDpStatsEncryptBytes_Type = Counter64
_TmnxIPsecEsaDpStatsEncryptBytes_Object = MibTableColumn
tmnxIPsecEsaDpStatsEncryptBytes = _TmnxIPsecEsaDpStatsEncryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 2),
    _TmnxIPsecEsaDpStatsEncryptBytes_Type()
)
tmnxIPsecEsaDpStatsEncryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsEncryptBytes.setStatus("current")
_TmnxIPsecEsaDpStatsDecryptPkts_Type = Counter64
_TmnxIPsecEsaDpStatsDecryptPkts_Object = MibTableColumn
tmnxIPsecEsaDpStatsDecryptPkts = _TmnxIPsecEsaDpStatsDecryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 3),
    _TmnxIPsecEsaDpStatsDecryptPkts_Type()
)
tmnxIPsecEsaDpStatsDecryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsDecryptPkts.setStatus("current")
_TmnxIPsecEsaDpStatsDecryptBytes_Type = Counter64
_TmnxIPsecEsaDpStatsDecryptBytes_Object = MibTableColumn
tmnxIPsecEsaDpStatsDecryptBytes = _TmnxIPsecEsaDpStatsDecryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 4),
    _TmnxIPsecEsaDpStatsDecryptBytes_Type()
)
tmnxIPsecEsaDpStatsDecryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsDecryptBytes.setStatus("current")
_TmnxIPsecEsaDpStatsTxPktErrs_Type = Counter32
_TmnxIPsecEsaDpStatsTxPktErrs_Object = MibTableColumn
tmnxIPsecEsaDpStatsTxPktErrs = _TmnxIPsecEsaDpStatsTxPktErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 5),
    _TmnxIPsecEsaDpStatsTxPktErrs_Type()
)
tmnxIPsecEsaDpStatsTxPktErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsTxPktErrs.setStatus("current")
_TmnxIPsecEsaDpStatsOutBDropPkts_Type = Counter64
_TmnxIPsecEsaDpStatsOutBDropPkts_Object = MibTableColumn
tmnxIPsecEsaDpStatsOutBDropPkts = _TmnxIPsecEsaDpStatsOutBDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 6),
    _TmnxIPsecEsaDpStatsOutBDropPkts_Type()
)
tmnxIPsecEsaDpStatsOutBDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsOutBDropPkts.setStatus("current")
_TmnxIPsecEsaDpStatsOutBSAMisses_Type = Counter64
_TmnxIPsecEsaDpStatsOutBSAMisses_Object = MibTableColumn
tmnxIPsecEsaDpStatsOutBSAMisses = _TmnxIPsecEsaDpStatsOutBSAMisses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 7),
    _TmnxIPsecEsaDpStatsOutBSAMisses_Type()
)
tmnxIPsecEsaDpStatsOutBSAMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsOutBSAMisses.setStatus("current")
_TmnxIPsecEsaDpStatsOutBPEMisses_Type = Counter32
_TmnxIPsecEsaDpStatsOutBPEMisses_Object = MibTableColumn
tmnxIPsecEsaDpStatsOutBPEMisses = _TmnxIPsecEsaDpStatsOutBPEMisses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 8),
    _TmnxIPsecEsaDpStatsOutBPEMisses_Type()
)
tmnxIPsecEsaDpStatsOutBPEMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsOutBPEMisses.setStatus("current")
_TmnxIPsecEsaDpStatsInBDropPkts_Type = Counter64
_TmnxIPsecEsaDpStatsInBDropPkts_Object = MibTableColumn
tmnxIPsecEsaDpStatsInBDropPkts = _TmnxIPsecEsaDpStatsInBDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 9),
    _TmnxIPsecEsaDpStatsInBDropPkts_Type()
)
tmnxIPsecEsaDpStatsInBDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsInBDropPkts.setStatus("current")
_TmnxIPsecEsaDpStatsInBSAMisses_Type = Counter64
_TmnxIPsecEsaDpStatsInBSAMisses_Object = MibTableColumn
tmnxIPsecEsaDpStatsInBSAMisses = _TmnxIPsecEsaDpStatsInBSAMisses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 10),
    _TmnxIPsecEsaDpStatsInBSAMisses_Type()
)
tmnxIPsecEsaDpStatsInBSAMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsInBSAMisses.setStatus("current")
_TmnxIPsecEsaDpStatsInBIPMismatch_Type = Counter32
_TmnxIPsecEsaDpStatsInBIPMismatch_Object = MibTableColumn
tmnxIPsecEsaDpStatsInBIPMismatch = _TmnxIPsecEsaDpStatsInBIPMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 11),
    _TmnxIPsecEsaDpStatsInBIPMismatch_Type()
)
tmnxIPsecEsaDpStatsInBIPMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStatsInBIPMismatch.setStatus("current")
_TmnxIPsecEsaDpInFragments_Type = Counter64
_TmnxIPsecEsaDpInFragments_Object = MibTableColumn
tmnxIPsecEsaDpInFragments = _TmnxIPsecEsaDpInFragments_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 12),
    _TmnxIPsecEsaDpInFragments_Type()
)
tmnxIPsecEsaDpInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpInFragments.setStatus("current")
_TmnxIPsecEsaDpPktsReassem_Type = Counter64
_TmnxIPsecEsaDpPktsReassem_Object = MibTableColumn
tmnxIPsecEsaDpPktsReassem = _TmnxIPsecEsaDpPktsReassem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 13),
    _TmnxIPsecEsaDpPktsReassem_Type()
)
tmnxIPsecEsaDpPktsReassem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpPktsReassem.setStatus("current")
_TmnxIPsecEsaDpFragDropTime_Type = Counter64
_TmnxIPsecEsaDpFragDropTime_Object = MibTableColumn
tmnxIPsecEsaDpFragDropTime = _TmnxIPsecEsaDpFragDropTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 14),
    _TmnxIPsecEsaDpFragDropTime_Type()
)
tmnxIPsecEsaDpFragDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpFragDropTime.setStatus("current")
_TmnxIPsecEsaDpFragDropped_Type = Counter64
_TmnxIPsecEsaDpFragDropped_Object = MibTableColumn
tmnxIPsecEsaDpFragDropped = _TmnxIPsecEsaDpFragDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 15),
    _TmnxIPsecEsaDpFragDropped_Type()
)
tmnxIPsecEsaDpFragDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpFragDropped.setStatus("current")
_TmnxIPsecEsaDpGreTnlInPkts_Type = Counter64
_TmnxIPsecEsaDpGreTnlInPkts_Object = MibTableColumn
tmnxIPsecEsaDpGreTnlInPkts = _TmnxIPsecEsaDpGreTnlInPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 16),
    _TmnxIPsecEsaDpGreTnlInPkts_Type()
)
tmnxIPsecEsaDpGreTnlInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpGreTnlInPkts.setStatus("current")
_TmnxIPsecEsaDpGreTnlInBytes_Type = Counter64
_TmnxIPsecEsaDpGreTnlInBytes_Object = MibTableColumn
tmnxIPsecEsaDpGreTnlInBytes = _TmnxIPsecEsaDpGreTnlInBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 17),
    _TmnxIPsecEsaDpGreTnlInBytes_Type()
)
tmnxIPsecEsaDpGreTnlInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpGreTnlInBytes.setStatus("current")
_TmnxIPsecEsaDpGreTnlInErrs_Type = Counter64
_TmnxIPsecEsaDpGreTnlInErrs_Object = MibTableColumn
tmnxIPsecEsaDpGreTnlInErrs = _TmnxIPsecEsaDpGreTnlInErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 18),
    _TmnxIPsecEsaDpGreTnlInErrs_Type()
)
tmnxIPsecEsaDpGreTnlInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpGreTnlInErrs.setStatus("current")
_TmnxIPsecEsaDpGreTnlOutPkts_Type = Counter64
_TmnxIPsecEsaDpGreTnlOutPkts_Object = MibTableColumn
tmnxIPsecEsaDpGreTnlOutPkts = _TmnxIPsecEsaDpGreTnlOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 19),
    _TmnxIPsecEsaDpGreTnlOutPkts_Type()
)
tmnxIPsecEsaDpGreTnlOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpGreTnlOutPkts.setStatus("current")
_TmnxIPsecEsaDpGreTnlOutBytes_Type = Counter64
_TmnxIPsecEsaDpGreTnlOutBytes_Object = MibTableColumn
tmnxIPsecEsaDpGreTnlOutBytes = _TmnxIPsecEsaDpGreTnlOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 20),
    _TmnxIPsecEsaDpGreTnlOutBytes_Type()
)
tmnxIPsecEsaDpGreTnlOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpGreTnlOutBytes.setStatus("current")
_TmnxIPsecEsaDpGreTnlOutErrs_Type = Counter64
_TmnxIPsecEsaDpGreTnlOutErrs_Object = MibTableColumn
tmnxIPsecEsaDpGreTnlOutErrs = _TmnxIPsecEsaDpGreTnlOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 21),
    _TmnxIPsecEsaDpGreTnlOutErrs_Type()
)
tmnxIPsecEsaDpGreTnlOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpGreTnlOutErrs.setStatus("current")
_TmnxIPsecEsaDpPktsDropDfSet_Type = Counter64
_TmnxIPsecEsaDpPktsDropDfSet_Object = MibTableColumn
tmnxIPsecEsaDpPktsDropDfSet = _TmnxIPsecEsaDpPktsDropDfSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 22),
    _TmnxIPsecEsaDpPktsDropDfSet_Type()
)
tmnxIPsecEsaDpPktsDropDfSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpPktsDropDfSet.setStatus("current")
_TmnxIPsecEsaDpStaticIPsecTnls_Type = Counter32
_TmnxIPsecEsaDpStaticIPsecTnls_Object = MibTableColumn
tmnxIPsecEsaDpStaticIPsecTnls = _TmnxIPsecEsaDpStaticIPsecTnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 23),
    _TmnxIPsecEsaDpStaticIPsecTnls_Type()
)
tmnxIPsecEsaDpStaticIPsecTnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpStaticIPsecTnls.setStatus("current")
_TmnxIPsecEsaDpDynIPsecTnls_Type = Counter32
_TmnxIPsecEsaDpDynIPsecTnls_Object = MibTableColumn
tmnxIPsecEsaDpDynIPsecTnls = _TmnxIPsecEsaDpDynIPsecTnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 24),
    _TmnxIPsecEsaDpDynIPsecTnls_Type()
)
tmnxIPsecEsaDpDynIPsecTnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpDynIPsecTnls.setStatus("current")
_TmnxIPsecEsaDpIpGreTnls_Type = Counter32
_TmnxIPsecEsaDpIpGreTnls_Object = MibTableColumn
tmnxIPsecEsaDpIpGreTnls = _TmnxIPsecEsaDpIpGreTnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 25),
    _TmnxIPsecEsaDpIpGreTnls_Type()
)
tmnxIPsecEsaDpIpGreTnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpIpGreTnls.setStatus("current")
_TmnxIPsecEsaDpIpv4Tnls_Type = Counter32
_TmnxIPsecEsaDpIpv4Tnls_Object = MibTableColumn
tmnxIPsecEsaDpIpv4Tnls = _TmnxIPsecEsaDpIpv4Tnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 26),
    _TmnxIPsecEsaDpIpv4Tnls_Type()
)
tmnxIPsecEsaDpIpv4Tnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpIpv4Tnls.setStatus("current")
_TmnxIPsecEsaDpL2tpv3TnlInPkts_Type = Counter64
_TmnxIPsecEsaDpL2tpv3TnlInPkts_Object = MibTableColumn
tmnxIPsecEsaDpL2tpv3TnlInPkts = _TmnxIPsecEsaDpL2tpv3TnlInPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 27),
    _TmnxIPsecEsaDpL2tpv3TnlInPkts_Type()
)
tmnxIPsecEsaDpL2tpv3TnlInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpL2tpv3TnlInPkts.setStatus("current")
_TmnxIPsecEsaDpL2tpv3TnlInBytes_Type = Counter64
_TmnxIPsecEsaDpL2tpv3TnlInBytes_Object = MibTableColumn
tmnxIPsecEsaDpL2tpv3TnlInBytes = _TmnxIPsecEsaDpL2tpv3TnlInBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 28),
    _TmnxIPsecEsaDpL2tpv3TnlInBytes_Type()
)
tmnxIPsecEsaDpL2tpv3TnlInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpL2tpv3TnlInBytes.setStatus("current")
_TmnxIPsecEsaDpL2tpv3TnlInErrs_Type = Counter64
_TmnxIPsecEsaDpL2tpv3TnlInErrs_Object = MibTableColumn
tmnxIPsecEsaDpL2tpv3TnlInErrs = _TmnxIPsecEsaDpL2tpv3TnlInErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 29),
    _TmnxIPsecEsaDpL2tpv3TnlInErrs_Type()
)
tmnxIPsecEsaDpL2tpv3TnlInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpL2tpv3TnlInErrs.setStatus("current")
_TmnxIPsecEsaDpL2tpv3TnlInCookErr_Type = Counter64
_TmnxIPsecEsaDpL2tpv3TnlInCookErr_Object = MibTableColumn
tmnxIPsecEsaDpL2tpv3TnlInCookErr = _TmnxIPsecEsaDpL2tpv3TnlInCookErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 30),
    _TmnxIPsecEsaDpL2tpv3TnlInCookErr_Type()
)
tmnxIPsecEsaDpL2tpv3TnlInCookErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpL2tpv3TnlInCookErr.setStatus("current")
_TmnxIPsecEsaDpL2tpv3TnlInSeIdErr_Type = Counter64
_TmnxIPsecEsaDpL2tpv3TnlInSeIdErr_Object = MibTableColumn
tmnxIPsecEsaDpL2tpv3TnlInSeIdErr = _TmnxIPsecEsaDpL2tpv3TnlInSeIdErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 31),
    _TmnxIPsecEsaDpL2tpv3TnlInSeIdErr_Type()
)
tmnxIPsecEsaDpL2tpv3TnlInSeIdErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpL2tpv3TnlInSeIdErr.setStatus("current")
_TmnxIPsecEsaDpL2tpv3TnlOutPkts_Type = Counter64
_TmnxIPsecEsaDpL2tpv3TnlOutPkts_Object = MibTableColumn
tmnxIPsecEsaDpL2tpv3TnlOutPkts = _TmnxIPsecEsaDpL2tpv3TnlOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 32),
    _TmnxIPsecEsaDpL2tpv3TnlOutPkts_Type()
)
tmnxIPsecEsaDpL2tpv3TnlOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpL2tpv3TnlOutPkts.setStatus("current")
_TmnxIPsecEsaDpL2tpv3TnlOutBytes_Type = Counter64
_TmnxIPsecEsaDpL2tpv3TnlOutBytes_Object = MibTableColumn
tmnxIPsecEsaDpL2tpv3TnlOutBytes = _TmnxIPsecEsaDpL2tpv3TnlOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 33),
    _TmnxIPsecEsaDpL2tpv3TnlOutBytes_Type()
)
tmnxIPsecEsaDpL2tpv3TnlOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpL2tpv3TnlOutBytes.setStatus("current")
_TmnxIPsecEsaDpL2tpv3TnlOutErrs_Type = Counter64
_TmnxIPsecEsaDpL2tpv3TnlOutErrs_Object = MibTableColumn
tmnxIPsecEsaDpL2tpv3TnlOutErrs = _TmnxIPsecEsaDpL2tpv3TnlOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 34),
    _TmnxIPsecEsaDpL2tpv3TnlOutErrs_Type()
)
tmnxIPsecEsaDpL2tpv3TnlOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpL2tpv3TnlOutErrs.setStatus("current")
_TmnxIPsecEsaDpL2tpv3Tnls_Type = Counter32
_TmnxIPsecEsaDpL2tpv3Tnls_Object = MibTableColumn
tmnxIPsecEsaDpL2tpv3Tnls = _TmnxIPsecEsaDpL2tpv3Tnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 124, 1, 35),
    _TmnxIPsecEsaDpL2tpv3Tnls_Type()
)
tmnxIPsecEsaDpL2tpv3Tnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecEsaDpL2tpv3Tnls.setStatus("current")
_TmnxIPsecNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxIPsecNotifyPrefix = _TmnxIPsecNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48)
)
_TmnxIPsecNotifications_ObjectIdentity = ObjectIdentity
tmnxIPsecNotifications = _TmnxIPsecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0)
)

# Managed Objects groups

tmnxIPsecV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 1)
)
tmnxIPsecV6v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformTblLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyTableLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyDescription"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyIkeMode"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyPFSEnabled"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyPFSDHGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyIPsecLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyNatTraversal"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyNatTKeepAliveIntvl"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyNatTBehindNatOnly"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyDpd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyDpdInterval"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyDpdMaxRetries"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelTableLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelDescription"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelLclGwAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelLclGwAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelRemGwAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelRemGwAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelPublicSvcId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelSecurityPolicyId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelKeyingType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelDynTransformId1"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelDynTransformId2"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelDynTransformId3"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelDynTransformId4"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIkePolicyId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIkePreSharedKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelOperFlags"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelReplayWindow"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIsakmpState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIsakmpEstabTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIsakmpNegLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumDpdTx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumDpdAckTx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumDpdAckRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumExpRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumInvalidDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumCtrlPktsTx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumCtrlPktsRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumCtrlTxErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumCtrlRxErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyTableLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsTblLastChangd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsLclAddrAny"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsLclAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsLclAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsLclAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsRemAddrAny"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsRemAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsRemAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsRemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSATableLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSARowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSALastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAEncryptionKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAAuthenticationKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSASpi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAManualTransformId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStorageType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAEstablishedTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSANegotiatedLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsBytesProcessed"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsBytesProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsBytesProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPktsProcessed"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPktsProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPktsProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsCryptoErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsReplayErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsSAErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPolicyErrors"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV6v0Group.setStatus("current")

tmnxIPsecMdaDpStatsV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 2)
)
tmnxIPsecMdaDpStatsV6v1Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsEncryptPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsEncryptPktsLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsEncryptPktsHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsEncryptBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsEncryptBytesLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsEncryptBytesHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsDecryptPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsDecryptPktsLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsDecryptPktsHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsDecryptBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsDecryptBytesLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsDecryptBytesHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsTxPktErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBDropPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBDropPktsLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBDropPktsHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBSAMisses"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBSAMissesLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBSAMissesHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBPolicyEntryMisses"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBDropPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBDropPktsLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBDropPktsHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBSAMisses"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBSAMissesLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBSAMissesHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBIPDstSrcMismatches"))
)
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsV6v1Group.setStatus("current")

tIPsecTnlTempGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 3)
)
tIPsecTnlTempGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDescr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDynKeyTransformId1"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDynKeyTransformId2"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDynKeyTransformId3"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDynKeyTransformId4"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempReplayWindow"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempReverseRoute"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempTblLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyAuthMethod"))
)
if mibBuilder.loadTexts:
    tIPsecTnlTempGroup.setStatus("current")

tmnxIPsecGWGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 4)
)
tmnxIPsecGWGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelAutoEstablish"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLastMgmtChange"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWSecureService"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWTunnelPolicyTemp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIkePolicyId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIkePreShared"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclX509Cert"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclPrivateKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperFlags"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCACert"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCACertRevocList"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAAuthenticationKey"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEncryptionKey"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEstablishedTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSANegotiatedLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSASpi"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcessed"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsCryptoErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcessed"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPolicyErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsReplayErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsSAErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIPsecSALifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpEstabTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpNegLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlPktsRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlPktsTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlRxErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlTxErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdAckRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdAckTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumExpRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumInvalidDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPfsDHGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlHasBiDirectionalSA"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIfIndex"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpPrefixLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateSvcId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlReplayWindow"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlTempId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskXAuthTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPskTunnels"))
)
if mibBuilder.loadTexts:
    tmnxIPsecGWGroup.setStatus("obsolete")

tmnxIPsecNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 5)
)
tmnxIPsecNotifyObjsGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlPort"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifReason"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfDestIp"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfDestIpType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfIfName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfSessState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfSvcId"))
)
if mibBuilder.loadTexts:
    tmnxIPsecNotifyObjsGroup.setStatus("current")

tmnxIPsecTnlBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 6)
)
tmnxIPsecTnlBfdGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdDesignate"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdSrcAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdSrcAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdSessOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdTableLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdGroup.setStatus("current")

tmnxIPsecIkeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 7)
)
tmnxIPsecIkeGroup.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyIkeVersion")
)
if mibBuilder.loadTexts:
    tmnxIPsecIkeGroup.setStatus("current")

tmnxIPsecCertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 8)
)
tmnxIPsecCertGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLocalIdType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLocalIdValue"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelLocalIdType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelLocalIdValue"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelClearDfBit"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyOwnAuthMethod"))
)
if mibBuilder.loadTexts:
    tmnxIPsecCertGroup.setStatus("current")

tmnxIpsecObsoletedV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 9)
)
tmnxIpsecObsoletedV10v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCACert"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCACertRevocList"))
)
if mibBuilder.loadTexts:
    tmnxIpsecObsoletedV10v0Group.setStatus("current")

tmnxIPsecGWV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 10)
)
tmnxIPsecGWV10v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelAutoEstablish"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLastMgmtChange"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWSecureService"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWTunnelPolicyTemp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIkePolicyId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIkePreShared"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclX509Cert"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclPrivateKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperFlags"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAAuthenticationKey"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEncryptionKey"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEstablishedTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSANegotiatedLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSASpi"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcessed"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsCryptoErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcessed"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPolicyErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsReplayErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsSAErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIPsecSALifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpEstabTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpNegLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlPktsRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlPktsTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlRxErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlTxErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdAckRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdAckTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumExpRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumInvalidDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPfsDHGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlHasBiDirectionalSA"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIfIndex"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpPrefixLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateSvcId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlReplayWindow"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlTempId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskXAuthTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCertTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPskTunnels"))
)
if mibBuilder.loadTexts:
    tmnxIPsecGWV10v0Group.setStatus("obsolete")

tmnxIPsecMdaDpStatsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 11)
)
tmnxIPsecMdaDpStatsV10v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStaticIPsecTnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpDynIPsecTnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpIpGreTnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpIpv4Tnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInBytesHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInBytesLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInErrsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInErrsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInPktsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInPktsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutBytesHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutBytesLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutErrsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutErrsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutPktsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutPktsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpFragDropTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpFragDropTimeHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpFragDropTimeLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpFragDropped"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpFragDroppedHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpFragDroppedLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpInFragments"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpInFragmentsHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpInFragmentsLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpPktsReassem"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpPktsReassemHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpPktsReassemLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpPktsDropDfSet"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpPktsDropDfSetLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpPktsDropDfSetHi"))
)
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsV10v0Group.setStatus("current")

tmnxIPsecMdaDpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 12)
)
tmnxIPsecMdaDpGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInBytesHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInBytesLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInErrsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInErrsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInPktsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInPktsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutBytesHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutBytesLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutErrsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutErrsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutPktsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutPktsLo"))
)
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGroup.setStatus("current")

tmnxIPsecV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 13)
)
tmnxIPsecV10v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelHostISA"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlHostISA"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV10v0Group.setStatus("current")

tmnxIPsecV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 14)
)
tmnxIPsecV11v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCSVPrimary"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCSVSecondary"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCSVDefResult"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCSVPrimary"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCSVSecondary"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCSVDefResult"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV11v0Group.setStatus("current")

tmnxIPsecIkev2RatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 15)
)
tmnxIPsecIkev2RatGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskRadiusTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCertRadiusTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWEapTunnels"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyLastMgmtChange"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyInclAttr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyRadSrvPlcy"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyLastMgmtChange"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyPassword"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyInclAttr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyRadSrvPlcy"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWRadAuthPolicy"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWRadAcctgPolicy"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyMatchPeerToCert"))
)
if mibBuilder.loadTexts:
    tmnxIPsecIkev2RatGroup.setStatus("current")

tIPsecIkev2RaTunNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 16)
)
tIPsecIkev2RaTunNotifyObjsGroup.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyFailReason")
)
if mibBuilder.loadTexts:
    tIPsecIkev2RaTunNotifyObjsGroup.setStatus("current")

tmnxIPsecTnlDstv12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 17)
)
tmnxIPsecTnlDstv12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstAddrLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstAddrRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstAddrTblLastChngd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstAddrResolved"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstv12v0Group.setStatus("current")

tmnxIPsecV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 18)
)
tmnxIPsecV12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6LclAddrAny"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6LclAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6LclAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6LclAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6RemAddrAny"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6RemAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6RemAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6RemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelEncapIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIcmp6Pkt2Big"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIcmp6NumPkt2Big"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIcmp6Pkt2BigTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempEncapIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempIcmp6Pkt2Big"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempIcmp6NumPkt2Big"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempIcmp6Pkt2BigTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempClearDfBit"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV12v0Group.setStatus("current")

tIPsecIkev2CertAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 19)
)
tIPsecIkev2CertAuthGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecCompChainCAProfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCertTrstAnchrProf"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCertTrstAnchrProf"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorsTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorsRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorsLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorProfTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorProfRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorProfLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelMatchTrustAnchor"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlMatchTrustAnchor"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdCertFile"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdCompChain"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCertProfile"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCertProfile"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdKeyFile"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfileTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfileRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfileLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfileAdminState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfileOperState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfileOperFlags"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorCAProfDown"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelMatCertEntryId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCertProfName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlMatCertEntryId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlCertProfName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdOperFlags"))
)
if mibBuilder.loadTexts:
    tIPsecIkev2CertAuthGroup.setStatus("current")

tIPsecIkev2CertAuthChainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 20)
)
tIPsecIkev2CertAuthChainGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecCertChainCAProfTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertChainCAProfRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertChainCAProfLastChgd"))
)
if mibBuilder.loadTexts:
    tIPsecIkev2CertAuthChainGroup.setStatus("current")

tIPsecTsReductionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 21)
)
tIPsecTsReductionGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecGWTsNegSelPlcyLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWTsNegSelPlcyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWTsNegSelPlcyTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWTsNegSelPlcyTsList"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryFrAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryFrAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryPfxAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryPfxAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryPfxLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryToAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryToAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListTblLastChgd"))
)
if mibBuilder.loadTexts:
    tIPsecTsReductionGroup.setStatus("current")

tIPsecRUSATrafficSelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 22)
)
tIPsecRUSATrafficSelGroup.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelLastChgd")
)
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelGroup.setStatus("current")

tmnxIPsecGWV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 23)
)
tmnxIPsecGWV12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelAutoEstablish"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLastMgmtChange"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWSecureService"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWTunnelPolicyTemp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIkePolicyId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIkePreShared"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperFlags"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAAuthenticationKey"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEncryptionKey"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEstablishedTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSANegotiatedLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSASpi"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcessed"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsCryptoErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcessed"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPolicyErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsReplayErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsSAErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIPsecSALifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpEstabTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpNegLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlPktsRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlPktsTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlRxErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlTxErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdAckRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdAckTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumExpRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumInvalidDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPfsDHGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlHasBiDirectionalSA"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIfIndex"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpPrefixLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateSvcId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlReplayWindow"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlTempId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskXAuthTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCertTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPskTunnels"))
)
if mibBuilder.loadTexts:
    tmnxIPsecGWV12v0Group.setStatus("current")

tmnxIpsecObsoletedV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 24)
)
tmnxIpsecObsoletedV12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddrType"))
)
if mibBuilder.loadTexts:
    tmnxIpsecObsoletedV12v0Group.setStatus("current")

tIkev2SendUnSolCfgAttr12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 26)
)
tIkev2SendUnSolCfgAttr12v0Group.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyRelayUnSolCfgAttr")
)
if mibBuilder.loadTexts:
    tIkev2SendUnSolCfgAttr12v0Group.setStatus("current")

tmnxIPsecSAStatsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 27)
)
tmnxIPsecSAStatsV12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsEncapOverhead"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPreEncapFragCnt"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPreEncapFragLtSz"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPstEncapFragCnt"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPstEncapFragLtSz"))
)
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsV12v0Group.setStatus("current")

tmnxIPsecRUSAStatsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 28)
)
tmnxIPsecRUSAStatsV12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsEncapOverhead"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPreEncapFragCnt"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPreEncapFragLtSz"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPostEncapFragCnt"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPostEncapFragLtSz"))
)
if mibBuilder.loadTexts:
    tmnxIPsecRUSAStatsV12v0Group.setStatus("current")

tmnxIPsecEncapNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 29)
)
tmnxIPsecEncapNotifyObjsGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifIPsecTunnelName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifConfigIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifEncapOverhead"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifConfigEncapIpMtu"))
)
if mibBuilder.loadTexts:
    tmnxIPsecEncapNotifyObjsGroup.setStatus("current")

tmnxIPsecTnlOperChgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 30)
)
tmnxIPsecTnlOperChgGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelOperChanged"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlOperChanged"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlOperChgGroup.setStatus("current")

tmnxIkePolicyAutoEapRadiusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 31)
)
tmnxIkePolicyAutoEapRadiusGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWAutoEapRadiusTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyAutoEapMethod"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyAutoEapOwnMethod"))
)
if mibBuilder.loadTexts:
    tmnxIkePolicyAutoEapRadiusGroup.setStatus("current")

tmnxIkePolicyAutoEapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 32)
)
tmnxIkePolicyAutoEapGroup.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWAutoEapTunnels")
)
if mibBuilder.loadTexts:
    tmnxIkePolicyAutoEapGroup.setStatus("current")

tmnxIPsecGWDhcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 33)
)
tmnxIPsecGWDhcpGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpGiAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpGiAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSendRelease"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpServiceId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpRouterId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr1AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr1Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr2AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr2Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr3AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr3Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr4AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr4Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr5AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr5Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr6AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr6Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr7AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr7Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr8AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpSrvr8Addr"))
)
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpGroup.setStatus("current")

tmnxIPsecGWDhcpV6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 34)
)
tmnxIPsecGWDhcpV6Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6TblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6RowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6LastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6AdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6LinkAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6LinkAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6SendRelease"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6ServiceId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6RouterId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr1AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr1Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr2AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr2Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr3AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr3Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr4AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr4Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr5AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr5Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr6AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr6Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr7AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr7Addr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr8AddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Srvr8Addr"))
)
if mibBuilder.loadTexts:
    tmnxIPsecGWDhcpV6Group.setStatus("current")

tmnxSecNotifyObjsV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 35)
)
tmnxSecNotifyObjsV13v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfileName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfEntryId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCaProfNames"))
)
if mibBuilder.loadTexts:
    tmnxSecNotifyObjsV13v0Group.setStatus("current")

tmnxIPsecGWLclAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 37)
)
tmnxIPsecGWLclAddrGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignAdminState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignIp4SrvrName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignIp4SrvrSvc"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignIp4SrvrRtr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignIp4PoolName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignIp6SrvrName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignIp6SrvrSvc"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignIp6SrvrRtr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignIp6PoolName"))
)
if mibBuilder.loadTexts:
    tmnxIPsecGWLclAddrGroup.setStatus("current")

tmnxIPsecRadInterimUpdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 38)
)
tmnxIPsecRadInterimUpdGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyUpdateInterval"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyJitter"))
)
if mibBuilder.loadTexts:
    tmnxIPsecRadInterimUpdGroup.setStatus("current")

tmnxIPsecIkev2IdiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 39)
)
tmnxIPsecIkev2IdiGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIkeIdType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIkeIdValue"))
)
if mibBuilder.loadTexts:
    tmnxIPsecIkev2IdiGroup.setStatus("current")

tmnxIPsecGWPrivIp2V13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 40)
)
tmnxIPsecGWPrivIp2V13v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddr2Type"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddr2"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpPrefixLen2"))
)
if mibBuilder.loadTexts:
    tmnxIPsecGWPrivIp2V13v0Group.setStatus("current")

tmnxIPsecGWLAAIpPool2V14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 41)
)
tmnxIPsecGWLAAIpPool2V14v0Group.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignIp4PoolNam2")
)
if mibBuilder.loadTexts:
    tmnxIPsecGWLAAIpPool2V14v0Group.setStatus("current")

tIPsecTrafficSelectorV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 43)
)
tIPsecTrafficSelectorV14v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryMinPort"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryMaxPort"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryMinMhType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryMaxMhType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryMinIcmpType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryMaxIcmpType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryMinIcmpCode"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryMaxIcmpCode"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryProtocolId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryMinAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryMinAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryMaxAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryMaxAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryPfxAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryPfxAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryPfxLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryMinPort"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryMaxPort"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryMinMhType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryMaxMhType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryMinIcmpType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryMaxIcmpType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryMinIcmpCode"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryMaxIcmpCode"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRmtEntryProtocolId"))
)
if mibBuilder.loadTexts:
    tIPsecTrafficSelectorV14v0Group.setStatus("current")

tmnxIkePolicyLockoutV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 44)
)
tmnxIkePolicyLockoutV14v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIkePolicyLockout"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyLockoutFailedAtempt"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyLockoutDuration"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyLockoutBlock"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyLockoutMaxPortPerIp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientFailAtempt"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientDroppedPkt"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecLockoutClientRemainTime"))
)
if mibBuilder.loadTexts:
    tmnxIkePolicyLockoutV14v0Group.setStatus("current")

tIPsecRUTnlDhcpLeaseStatV14v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 45)
)
tIPsecRUTnlDhcpLeaseStatV14v0Grp.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUTnlDhcpLeaseStatSverAddT"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlDhcpLeaseStatSverAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlDhcpLeaseStatAcquirTm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlDhcpLeaseStatRenewTm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlDhcpLeaseStatRebindTm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlDhcpLeaseStatPrivPref"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlDhcpLeaseStatPrivVald"))
)
if mibBuilder.loadTexts:
    tIPsecRUTnlDhcpLeaseStatV14v0Grp.setStatus("current")

tIPsecClientDatabaseV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 46)
)
tIPsecClientDatabaseV14v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecClientDatabaseTableLstChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDatabaseLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDatabaseRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDatabaseAdminState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDatabaseDescription"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDatabaseMatchType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientTableLstChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientAdminState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientIdIdiType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientIdIdiValue"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientIdPeer4PfAny"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientIdPeer6PfAny"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientIdPeerPfxTyp"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientIdPeerPfx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientIdPeerPfxLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientTnlTempltId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientPrivateSvcId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientPrivIfName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientTsListName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientPreSharedKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWClientDatabaseName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWClientDatabasFallback"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlClientDBClientId"))
)
if mibBuilder.loadTexts:
    tIPsecClientDatabaseV14v0Group.setStatus("current")

tmnxIkePolicyV2FragV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 47)
)
tmnxIkePolicyV2FragV14v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIkePolicyV2Fragment"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyV2FragmentMtu"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyV2FragReassembTmOut"))
)
if mibBuilder.loadTexts:
    tmnxIkePolicyV2FragV14v0Group.setStatus("current")

tmnxIPsecMdaDpStatsV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 48)
)
tmnxIPsecMdaDpStatsV14v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpL2tpv3TnlInPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpL2tpv3TnlInBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpL2tpv3TnlInErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpL2tpv3TnlInCookErr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpL2tpv3TnlInSeIdErr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpL2tpv3TnlOutPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpL2tpv3TnlOutBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpL2tpv3TnlOutErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpL2tpv3Tnls"))
)
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsV14v0Group.setStatus("current")

tmnxIPsecRUTnlInUseCfgsV14v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 49)
)
tmnxIPsecRUTnlInUseCfgsV14v0Grp.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUTnlInUseTsList"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlInUsePreSharedKey"))
)
if mibBuilder.loadTexts:
    tmnxIPsecRUTnlInUseCfgsV14v0Grp.setStatus("current")

tmnxIPsecIkeTransformV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 50)
)
tmnxIPsecIkeTransformV15v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeTransformTableLstChg"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeTransformRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeTransformLastChange"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeTransformAuthAlg"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeTransformEncrAlg"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeTransformDhGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeTransformIsakmpLifeT"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePlcyIkeTransformTbLstChg"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePlcyIkeTransformLstChange"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePlcyIkeTransformId"))
)
if mibBuilder.loadTexts:
    tmnxIPsecIkeTransformV15v0Group.setStatus("current")

tmnxIPsecIkePolicyV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 51)
)
tmnxIPsecIkePolicyV14v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIkePolicySndIdrAftEapSuccess"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyIkev1Ph1RespDelNtfy"))
)
if mibBuilder.loadTexts:
    tmnxIPsecIkePolicyV14v0Group.setStatus("current")

tmnxIPsecHistStatsV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 52)
)
tmnxIPsecHistStatsV15v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWHistStatsValue64"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWHistStatsValue32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWHistStatsIntvStTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWHistStatsIntvDur"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWHistStatsFstFTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWHistStatsFstFDesc"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWHistStatsLstFTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWHistStatsLstFDesc"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIsaHistStatsValue64"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIsaHistStatsValue32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIsaHistStatsIntvStTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIsaHistStatsIntvDur"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIsaHistStatsFstFTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIsaHistStatsFstFDesc"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIsaHistStatsLstFTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIsaHistStatsLstFDesc"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlGrpHistStatsValue64"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlGrpHistStatsValue32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlGrpHistStatsIntvStTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlGrpHistStatsIntvDur"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlGrpHistStatsFstFTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlGrpHistStatsFstFDesc"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlGrpHistStatsLstFTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlGrpHistStatsLstFDesc"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSysHistStatsValue64"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSysHistStatsValue32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSysHistStatsIntvStTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSysHistStatsIntvDur"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSysHistStatsFstFTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSysHistStatsFstFDesc"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSysHistStatsLstFTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSysHistStatsLstFDesc"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlHistStatsValue64"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlHistStatsIntvStTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlHistStatsIntvDur"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecRUTnlHistStatsValue64"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecRUTnlHistStatsIntvStTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecRUTnlHistStatsIntvDur"))
)
if mibBuilder.loadTexts:
    tmnxIPsecHistStatsV15v0Group.setStatus("current")

tmnxIPsecCertObsoleteV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 53)
)
tmnxIPsecCertObsoleteV15v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCertTrustAnchor"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCertFile"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelKeyFile"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclX509Cert"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclPrivateKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCertTrustAnchor"))
)
if mibBuilder.loadTexts:
    tmnxIPsecCertObsoleteV15v0Group.setStatus("current")

tIPsecTcpMssAdjustV15v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 54)
)
tIPsecTcpMssAdjustV15v0Grp.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecTnlTempPublicTcpMssAdjust"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempPrivateTcpMssAdjust"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelPubTcpMssAdjust"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelPrivTcpMssAdjust"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPubTcpMss"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivTcpMss"))
)
if mibBuilder.loadTexts:
    tIPsecTcpMssAdjustV15v0Grp.setStatus("current")

tmnxIkePolicyObsoleteV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 55)
)
tmnxIkePolicyObsoleteV15v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIkePolicyDHGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyIsakmpLifeTime"))
)
if mibBuilder.loadTexts:
    tmnxIkePolicyObsoleteV15v0Group.setStatus("current")

tmnxIPsecSvcLevelCfgV14v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 56)
)
tmnxIPsecSvcLevelCfgV14v0Grp.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIPsecSvcLevelCfgTableLastChg")
)
if mibBuilder.loadTexts:
    tmnxIPsecSvcLevelCfgV14v0Grp.setStatus("current")

tmnxIPsecTransformV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 57)
)
tmnxIPsecTransformV15v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformPfsDhGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelStatIsakmpAuthAlg"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelStatIsakmpEncrAlg"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelStatIsakmpPfsDhGp"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlStatsIsakmpAuthAlg"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlStatsIsakmpEncrAlg"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlStatsIsakmpPfsDhGrp"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPfsDhGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPfsDhGroup"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTransformV15v0Group.setStatus("current")

tmnxIPsecEmbmsV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 58)
)
tmnxIPsecEmbmsV15v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsMulticastIfName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsMulticastProt"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsMulticastIfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsMulticastProt"))
)
if mibBuilder.loadTexts:
    tmnxIPsecEmbmsV15v0Group.setStatus("current")

tmnxIPsecGWStatsV15v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 59)
)
tmnxIPsecGWStatsV15v0Grp.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUTnlInUseIkePolicy"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWStatsNumOfDl2lTnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWStatsNumOfRaTnls"))
)
if mibBuilder.loadTexts:
    tmnxIPsecGWStatsV15v0Grp.setStatus("current")

tmnxIPsecNoOfSaKeysV16v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 60)
)
tmnxIPsecNoOfSaKeysV16v0Grp.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWMaxNumPh1SaKeys"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWMaxNumPh2SaKeys"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelMaxNumPh1SaKeys"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelMaxNumPh2SaKeys"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecScalarObjsShowKeys"))
)
if mibBuilder.loadTexts:
    tmnxIPsecNoOfSaKeysV16v0Grp.setStatus("current")

tmnxIPsecSvcNameV16v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 61)
)
tmnxIPsecSvcNameV16v0Grp.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelPublicSvcName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWSecureServiceName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpServiceName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6ServiceName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignIp4SrvrSvcN"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWLclAddrAssignIp6SrvrSvcN"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDBClientPrivateSvcNm"))
)
if mibBuilder.loadTexts:
    tmnxIPsecSvcNameV16v0Grp.setStatus("current")

tmnxIPsecTnlBfdSessV16v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 62)
)
tmnxIPsecTnlBfdSessV16v0Grp.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdSessTableLChg"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdSessRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdSessSvcId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdSessSvcName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdSessIfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdSessDstAddrT"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdSessDstAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdSessStatSrcAddrT"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdSessStatSrcAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdSessStatOperState"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdSessV16v0Grp.setStatus("current")

tmnxIPsecTnlBfdObsoleteV16v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 63)
)
tmnxIPsecTnlBfdObsoleteV16v0Grp.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdSrcAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdSrcAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdSessOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdTableLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdObsoleteV16v0Grp.setStatus("current")

tmnxIkePolicyV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 64)
)
tmnxIkePolicyV15v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIkePolicyLimitInitExchange"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyReducedMaxExchgTt"))
)
if mibBuilder.loadTexts:
    tmnxIkePolicyV15v0Group.setStatus("current")

tmnxIPsecCertProfV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 65)
)
tmnxIPsecCertProfV16v0Group.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdRsaSign")
)
if mibBuilder.loadTexts:
    tmnxIPsecCertProfV16v0Group.setStatus("current")

tmnxIkeTransformV16v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 67)
)
tmnxIkeTransformV16v0Grp.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeTransformPrfAlg"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelStatIkeTranPrfAlg"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlStatsIkeTranPrfAlg"))
)
if mibBuilder.loadTexts:
    tmnxIkeTransformV16v0Grp.setStatus("current")

tmnxIPsecTunnelV15v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 68)
)
tmnxIPsecTunnelV15v0Grp.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelSecPlyStrictMatch")
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelV15v0Grp.setStatus("current")

tmnxVRtrIdIPsecTnlV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 69)
)
tmnxVRtrIdIPsecTnlV19v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlTableLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlDescription"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlLclGwAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlLclGwAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlRemGwAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlRemGwAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlSecurityPolicyId"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlKeyingType"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlDynTransformId1"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlDynTransformId2"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlDynTransformId3"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlDynTransformId4"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlIkePolicyId"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlIkePreSharedKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlOperFlags"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlReplayWindow"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlAutoEstablish"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlBfdDesignate"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlLocalIdType"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlLocalIdValue"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlClearDfBit"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlHostISA"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlCSVPrimary"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlCSVSecondary"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlCSVDefResult"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlCertProfile"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlMatchTrustAnchor"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlCertTrstAnchrProf"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlEncapIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlPropagateIpv6PMTU"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlIcmp6Pkt2Big"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlIcmp6NumPkt2Big"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlIcmp6Pkt2BigTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlOperChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlPropagateIpv4PMTU"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlIcmpFragReq"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlIcmpFragReqNum"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlIcmpFragReqTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlPMTUDiscoverAging"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlPubTcpMssAdjust"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlPrivTcpMssAdjust"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlMaxNumPh1SaKeys"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlMaxNumPh2SaKeys"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlSecPlyStrictMatch"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlPrivateSvcName"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlPrivSap"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlBfdTableLChg"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlBfdRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlBfdSvcName"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlBfdIfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlBfdDstAddrT"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlBfdDstAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlBfdStatSrcAddrT"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlBfdStatSrcAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlBfdStatOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSATableLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSARowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSALastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAType"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAEncryptionKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAAuthenticationKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSASpi"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAManualTransformId"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStorageType"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAEstablishedTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSANegotiatedLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStBytesProcessed"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStBytesProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStBytesProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStPktsProcessed"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStPktsProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStPktsProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStCryptoErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStReplayErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStSAErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStPolicyErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStEncapOverhead"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStPreEncapFragCnt"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStPreEncapFragLtSz"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStPstEncapFragCnt"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStPstEncapFragLtSz"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStPfsDhGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStTempPrivMtu"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStMulticastIfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecSAStMulticastProt"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyTableLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParamTblLastChangd"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParamRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParamLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParamLclAddrAny"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParamLclAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParamLclAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParamLclAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParamRemAddrAny"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParamRemAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParamRemAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParamRemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParam6LclAddrAny"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParam6LclAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParam6LclAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParam6LclAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParam6RemAddrAny"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParam6RemAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParam6RemAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtSecPlcyParam6RemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIfIPsecTblLstCgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIfIPsecRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIfIPsecLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIfIPsecAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIfIPsecIpFilterInExcptId"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIfIPsecIsaTnlGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIfIPsecPubSap"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIfIPsecIpv6FilterInExcId"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlLclGwAddrOvrd"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlLclGwAddrOvrdType"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlIsakmpState"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlIsakmpEstabTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlIsakmpNegLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlNumDpdTx"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlNumDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlNumDpdAckTx"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlNumDpdAckRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlNumExpRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlNumInvalidDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlNumCtrlPktsTx"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlNumCtrlPktsRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlNumCtrlTxErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlNumCtrlRxErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlMatCertEntryId"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlCertProfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlStatIsakmpAuthAlg"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlStatIsakmpEncrAlg"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlStatIsakmpPfsDhGp"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlStatIkeTranPrfAlg"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIdIPsecTnlV19v0Group.setStatus("current")

tIPsecTnlTempGroupV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 71)
)
tIPsecTnlTempGroupV19v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDescr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDynKeyTransformId1"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDynKeyTransformId2"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDynKeyTransformId3"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDynKeyTransformId4"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempReplayWindow"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempReverseRoute"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempTblLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyAuthMethod"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempIgnoreDefaultRoute"))
)
if mibBuilder.loadTexts:
    tIPsecTnlTempGroupV19v0Group.setStatus("current")

tmnxIPsecNotifyObjsV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 72)
)
tmnxIPsecNotifyObjsV19v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifTunnelType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifTunnelIdentifier"))
)
if mibBuilder.loadTexts:
    tmnxIPsecNotifyObjsV19v0Group.setStatus("current")

tmnxIPsecTunnelEsaVmV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 73)
)
tmnxIPsecTunnelEsaVmV19v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelHostEsa"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelHostEsaVm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlHostEsa"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlHostEsaVm"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlHostEsa"),
        ("TIMETRA-IPSEC-MIB", "tmnxVRtIPsecTnlHostEsaVm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecLOClientEsaStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecLOClientEsaFailAtempt"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecLOClientEsaDroppedPkt"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecLOClientEsaRemainTime"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelEsaVmV19v0Group.setStatus("current")

tmnxIPsecTunnelEsaVmV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 74)
)
tmnxIPsecTunnelEsaVmV20v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaHistStatsValue64"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaHistStatsValue32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaHistStatsIntvStTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaHistStatsIntvDur"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaHistStatsFstFTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaHistStatsFstFDesc"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaHistStatsLstFTm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaHistStatsLstFDesc"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpStatsEncryptPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpStatsEncryptBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpStatsDecryptPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpStatsDecryptBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpStatsTxPktErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpStatsOutBDropPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpStatsOutBSAMisses"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpStatsOutBPEMisses"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpStatsInBDropPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpStatsInBSAMisses"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpStatsInBIPMismatch"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpInFragments"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpPktsReassem"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpFragDropTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpFragDropped"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpGreTnlInPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpGreTnlInBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpGreTnlInErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpGreTnlOutPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpGreTnlOutBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpGreTnlOutErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpPktsDropDfSet"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpStaticIPsecTnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpDynIPsecTnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpIpGreTnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpIpv4Tnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpL2tpv3TnlInPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpL2tpv3TnlInBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpL2tpv3TnlInErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpL2tpv3TnlInCookErr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpL2tpv3TnlInSeIdErr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpL2tpv3TnlOutPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpL2tpv3TnlOutBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpL2tpv3TnlOutErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEsaDpL2tpv3Tnls"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelEsaVmV20v0Group.setStatus("current")

tmnxIPsecObsoleteV20v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 75)
)
tmnxIPsecObsoleteV20v0Grp.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIPsecSvcLevelCfgRsvRtrOvrd")
)
if mibBuilder.loadTexts:
    tmnxIPsecObsoleteV20v0Grp.setStatus("current")

tmnxIPsecSvcLevelCfgV20v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 76)
)
tmnxIPsecSvcLevelCfgV20v0Grp.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIPsecSvcLevelCfgRROvrdType")
)
if mibBuilder.loadTexts:
    tmnxIPsecSvcLevelCfgV20v0Grp.setStatus("current")


# Notification objects

tIPsecRUTnlFailToCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 1)
)
tIPsecRUTnlFailToCreate.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlPort"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifReason"))
)
if mibBuilder.loadTexts:
    tIPsecRUTnlFailToCreate.setStatus(
        "current"
    )

tIPsecRUSAFailToAddRoute = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 2)
)
tIPsecRUSAFailToAddRoute.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifReason"))
)
if mibBuilder.loadTexts:
    tIPsecRUSAFailToAddRoute.setStatus(
        "current"
    )

tIPsecBfdIntfSessStateChgd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 3)
)
tIPsecBfdIntfSessStateChgd.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfSvcId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfIfName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfDestIpType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfDestIp"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfSessState"))
)
if mibBuilder.loadTexts:
    tIPsecBfdIntfSessStateChgd.setStatus(
        "current"
    )

tIPsecRadAcctPlcyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 4)
)
tIPsecRadAcctPlcyFailure.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyFailReason"))
)
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyFailure.setStatus(
        "current"
    )

tIPSecTrustAnchorPrfOprChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 5)
)
tIPSecTrustAnchorPrfOprChg.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorCAProfDown")
)
if mibBuilder.loadTexts:
    tIPSecTrustAnchorPrfOprChg.setStatus(
        "current"
    )

tIPsecTunnelEncapIpMtuTooSmall = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 6)
)
tIPsecTunnelEncapIpMtuTooSmall.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifIPsecTunnelName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifConfigIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifEncapOverhead"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifConfigEncapIpMtu"))
)
if mibBuilder.loadTexts:
    tIPsecTunnelEncapIpMtuTooSmall.setStatus(
        "current"
    )

tIPsecRuTnlEncapIpMtuTooSmall = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 7)
)
tIPsecRuTnlEncapIpMtuTooSmall.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlPort"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifConfigIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifEncapOverhead"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifConfigEncapIpMtu"))
)
if mibBuilder.loadTexts:
    tIPsecRuTnlEncapIpMtuTooSmall.setStatus(
        "current"
    )

tmnxSecNotifCmptedCertHashChngd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 8)
)
tmnxSecNotifCmptedCertHashChngd.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfileName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfEntryId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCaProfNames"))
)
if mibBuilder.loadTexts:
    tmnxSecNotifCmptedCertHashChngd.setStatus(
        "current"
    )

tmnxSecNotifCmptedCertChnChngd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 9)
)
tmnxSecNotifCmptedCertChnChngd.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfileName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfEntryId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCaProfNames"))
)
if mibBuilder.loadTexts:
    tmnxSecNotifCmptedCertChnChngd.setStatus(
        "current"
    )

tmnxSecNotifSendChnNotInCmptChn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 10)
)
tmnxSecNotifSendChnNotInCmptChn.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfileName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfEntryId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCaProfNames"))
)
if mibBuilder.loadTexts:
    tmnxSecNotifSendChnNotInCmptChn.setStatus(
        "current"
    )

tmnxIPsecTunnelOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 11)
)
tmnxIPsecTunnelOperStateChange.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelOperFlags"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelOperStateChange.setStatus(
        "current"
    )

tmnxIPsecGWOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 12)
)
tmnxIPsecGWOperStateChange.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperFlags"))
)
if mibBuilder.loadTexts:
    tmnxIPsecGWOperStateChange.setStatus(
        "current"
    )

tIPsecRUTnlRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 13)
)
tIPsecRUTnlRemoved.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlPort"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifReason"))
)
if mibBuilder.loadTexts:
    tIPsecRUTnlRemoved.setStatus(
        "current"
    )

tIPsecTunnelProtocolFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 14)
)
tIPsecTunnelProtocolFailed.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifTunnelType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifTunnelIdentifier"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifReason"))
)
if mibBuilder.loadTexts:
    tIPsecTunnelProtocolFailed.setStatus(
        "current"
    )


# Notifications groups

tmnxSecurityNotificationV13v0Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 36)
)
tmnxSecurityNotificationV13v0Grp.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxSecNotifCmptedCertHashChngd"),
        ("TIMETRA-IPSEC-MIB", "tmnxSecNotifCmptedCertChnChngd"),
        ("TIMETRA-IPSEC-MIB", "tmnxSecNotifSendChnNotInCmptChn"))
)
if mibBuilder.loadTexts:
    tmnxSecurityNotificationV13v0Grp.setStatus(
        "current"
    )

tmnxIPsecNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3, 1)
)
tmnxIPsecNotifGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUTnlFailToCreate"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlRemoved"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAFailToAddRoute"),
        ("TIMETRA-IPSEC-MIB", "tIPsecBfdIntfSessStateChgd"))
)
if mibBuilder.loadTexts:
    tmnxIPsecNotifGroup.setStatus(
        "current"
    )

tIPsecIkev2RaTunNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3, 2)
)
tIPsecIkev2RaTunNotifGroup.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyFailure")
)
if mibBuilder.loadTexts:
    tIPsecIkev2RaTunNotifGroup.setStatus(
        "current"
    )

tIPSecTrustAnchorProfNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3, 3)
)
tIPSecTrustAnchorProfNotifGroup.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPSecTrustAnchorPrfOprChg")
)
if mibBuilder.loadTexts:
    tIPSecTrustAnchorProfNotifGroup.setStatus(
        "current"
    )

tIPSecTunnelEncapNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3, 4)
)
tIPSecTunnelEncapNotifGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecTunnelEncapIpMtuTooSmall"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRuTnlEncapIpMtuTooSmall"))
)
if mibBuilder.loadTexts:
    tIPSecTunnelEncapNotifGroup.setStatus(
        "current"
    )

tmnxIPSecTunnelNotifV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3, 5)
)
tmnxIPSecTunnelNotifV11v0Group.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelOperStateChange")
)
if mibBuilder.loadTexts:
    tmnxIPSecTunnelNotifV11v0Group.setStatus(
        "current"
    )

tmnxIPSecGWNotifV13v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3, 6)
)
tmnxIPSecGWNotifV13v0Group.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperStateChange")
)
if mibBuilder.loadTexts:
    tmnxIPSecGWNotifV13v0Group.setStatus(
        "current"
    )

tmnxIPsecTunnelNotifV19v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3, 7)
)
tmnxIPsecTunnelNotifV19v0Group.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPsecTunnelProtocolFailed")
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNotifV19v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxIPsecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 1)
)
tmnxIPsecCompliance.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group")
)
if mibBuilder.loadTexts:
    tmnxIPsecCompliance.setStatus(
        "obsolete"
    )

tmnxIPsecV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 2)
)
tmnxIPsecV6v1Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxIPsecV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 3)
)
tmnxIPsecV7v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxIPsecV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 4)
)
tmnxIPsecV8v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGroup"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxIPsecV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 5)
)
tmnxIPsecV9v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecCertGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGroup"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxIPsecV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 6)
)
tmnxIPsecV10v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecCertGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlOperChgGroup"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxIPsecV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 7)
)
tmnxIPsecV11v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecCertGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecV11v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkev2RatGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecIkev2RaTunNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecIkev2RaTunNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlOperChgGroup"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxIPsecV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 8)
)
tmnxIPsecV12v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWV12v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecCertGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecV11v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkev2RatGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecIkev2RaTunNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecIkev2RaTunNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstv12v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecV12v0Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecIkev2CertAuthGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecIkev2CertAuthChainGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsReductionGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelGroup"),
        ("TIMETRA-IPSEC-MIB", "tIkev2SendUnSolCfgAttr12v0Group"),
        ("TIMETRA-IPSEC-MIB", "tIPSecTrustAnchorProfNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsV12v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecRUSAStatsV12v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEncapNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPSecTunnelEncapNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlOperChgGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyAutoEapRadiusGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyAutoEapGroup"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV12v0Compliance.setStatus(
        "current"
    )

tmnxIPsecV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 9)
)
tmnxIPsecV13v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWDhcpV6Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxSecurityNotificationV13v0Grp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclAddrGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecRadInterimUpdGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkev2IdiGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPrivIp2V13v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPSecGWNotifV13v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPSecTunnelNotifV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV13v0Compliance.setStatus(
        "current"
    )

tmnxIPsecV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 10)
)
tmnxIPsecV14v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLAAIpPool2V14v0Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrafficSelectorV14v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyLockoutV14v0Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlDhcpLeaseStatV14v0Grp"),
        ("TIMETRA-IPSEC-MIB", "tIPsecClientDatabaseV14v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyV2FragV14v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV14v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecRUTnlInUseCfgsV14v0Grp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkePolicyV14v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSvcLevelCfgV14v0Grp"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV14v0Compliance.setStatus(
        "current"
    )

tmnxIPsecV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 11)
)
tmnxIPsecV15v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeTransformV15v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecHistStatsV15v0Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTcpMssAdjustV15v0Grp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyObsoleteV15v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformV15v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEmbmsV15v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWStatsV15v0Grp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyV15v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelV15v0Grp"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV15v0Compliance.setStatus(
        "current"
    )

tmnxIPsecV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 12)
)
tmnxIPsecV16v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecNoOfSaKeysV16v0Grp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSvcNameV16v0Grp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdSessV16v0Grp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecCertProfV16v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkeTransformV16v0Grp"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV16v0Compliance.setStatus(
        "current"
    )

tmnxIPsecV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 13)
)
tmnxIPsecV19v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxVRtrIdIPsecTnlV19v0Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroupV19v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsV19v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNotifV19v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelEsaVmV19v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV19v0Compliance.setStatus(
        "current"
    )

tmnxIPsecV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 14)
)
tmnxIPsecV20v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxVRtrIdIPsecTnlV19v0Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroupV19v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsV19v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNotifV19v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelEsaVmV19v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelEsaVmV20v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSvcLevelCfgV20v0Grp"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV20v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-IPSEC-MIB",
    **{"TmnxIPsecTransformId": TmnxIPsecTransformId,
       "TmnxIPsecTransformIdOrZero": TmnxIPsecTransformIdOrZero,
       "TmnxIPsecIkeTransformId": TmnxIPsecIkeTransformId,
       "TmnxIPsecIkeTransformIdOrZero": TmnxIPsecIkeTransformIdOrZero,
       "TmnxIkePolicyId": TmnxIkePolicyId,
       "TmnxIkePolicyIdOrZero": TmnxIkePolicyIdOrZero,
       "TmnxIkeVersion": TmnxIkeVersion,
       "TmnxIkePolicyIkeMode": TmnxIkePolicyIkeMode,
       "TmnxIkePolicyDHGroup": TmnxIkePolicyDHGroup,
       "TmnxIPsecTransformPfsDhGrp": TmnxIPsecTransformPfsDhGrp,
       "TmnxIPsecPolicyId": TmnxIPsecPolicyId,
       "TmnxIPsecPolicyIdOrZero": TmnxIPsecPolicyIdOrZero,
       "TmnxIPsecDirection2": TmnxIPsecDirection2,
       "TmnxIPsecProtocol": TmnxIPsecProtocol,
       "TmnxIPsecLocalIdType": TmnxIPsecLocalIdType,
       "TmnxCertRevStatus": TmnxCertRevStatus,
       "TmnxCertRevStatusOrNone": TmnxCertRevStatusOrNone,
       "TmnxIkePolicyRelayUnSolCfgAttr": TmnxIkePolicyRelayUnSolCfgAttr,
       "TmnxIpsecTrafficSelSide": TmnxIpsecTrafficSelSide,
       "TmnxIPsecHistStatsType": TmnxIPsecHistStatsType,
       "TmnxIPsecOperState": TmnxIPsecOperState,
       "TIPsecMulticastProtocol": TIPsecMulticastProtocol,
       "timetraIPsecMIBModule": timetraIPsecMIBModule,
       "tmnxIPsecConformance": tmnxIPsecConformance,
       "tmnxIPsecCompliances": tmnxIPsecCompliances,
       "tmnxIPsecCompliance": tmnxIPsecCompliance,
       "tmnxIPsecV6v1Compliance": tmnxIPsecV6v1Compliance,
       "tmnxIPsecV7v0Compliance": tmnxIPsecV7v0Compliance,
       "tmnxIPsecV8v0Compliance": tmnxIPsecV8v0Compliance,
       "tmnxIPsecV9v0Compliance": tmnxIPsecV9v0Compliance,
       "tmnxIPsecV10v0Compliance": tmnxIPsecV10v0Compliance,
       "tmnxIPsecV11v0Compliance": tmnxIPsecV11v0Compliance,
       "tmnxIPsecV12v0Compliance": tmnxIPsecV12v0Compliance,
       "tmnxIPsecV13v0Compliance": tmnxIPsecV13v0Compliance,
       "tmnxIPsecV14v0Compliance": tmnxIPsecV14v0Compliance,
       "tmnxIPsecV15v0Compliance": tmnxIPsecV15v0Compliance,
       "tmnxIPsecV16v0Compliance": tmnxIPsecV16v0Compliance,
       "tmnxIPsecV19v0Compliance": tmnxIPsecV19v0Compliance,
       "tmnxIPsecV20v0Compliance": tmnxIPsecV20v0Compliance,
       "tmnxIPsecGroups": tmnxIPsecGroups,
       "tmnxIPsecV6v0Group": tmnxIPsecV6v0Group,
       "tmnxIPsecMdaDpStatsV6v1Group": tmnxIPsecMdaDpStatsV6v1Group,
       "tIPsecTnlTempGroup": tIPsecTnlTempGroup,
       "tmnxIPsecGWGroup": tmnxIPsecGWGroup,
       "tmnxIPsecNotifyObjsGroup": tmnxIPsecNotifyObjsGroup,
       "tmnxIPsecTnlBfdGroup": tmnxIPsecTnlBfdGroup,
       "tmnxIPsecIkeGroup": tmnxIPsecIkeGroup,
       "tmnxIPsecCertGroup": tmnxIPsecCertGroup,
       "tmnxIpsecObsoletedV10v0Group": tmnxIpsecObsoletedV10v0Group,
       "tmnxIPsecGWV10v0Group": tmnxIPsecGWV10v0Group,
       "tmnxIPsecMdaDpStatsV10v0Group": tmnxIPsecMdaDpStatsV10v0Group,
       "tmnxIPsecMdaDpGroup": tmnxIPsecMdaDpGroup,
       "tmnxIPsecV10v0Group": tmnxIPsecV10v0Group,
       "tmnxIPsecV11v0Group": tmnxIPsecV11v0Group,
       "tmnxIPsecIkev2RatGroup": tmnxIPsecIkev2RatGroup,
       "tIPsecIkev2RaTunNotifyObjsGroup": tIPsecIkev2RaTunNotifyObjsGroup,
       "tmnxIPsecTnlDstv12v0Group": tmnxIPsecTnlDstv12v0Group,
       "tmnxIPsecV12v0Group": tmnxIPsecV12v0Group,
       "tIPsecIkev2CertAuthGroup": tIPsecIkev2CertAuthGroup,
       "tIPsecIkev2CertAuthChainGroup": tIPsecIkev2CertAuthChainGroup,
       "tIPsecTsReductionGroup": tIPsecTsReductionGroup,
       "tIPsecRUSATrafficSelGroup": tIPsecRUSATrafficSelGroup,
       "tmnxIPsecGWV12v0Group": tmnxIPsecGWV12v0Group,
       "tmnxIpsecObsoletedV12v0Group": tmnxIpsecObsoletedV12v0Group,
       "tIkev2SendUnSolCfgAttr12v0Group": tIkev2SendUnSolCfgAttr12v0Group,
       "tmnxIPsecSAStatsV12v0Group": tmnxIPsecSAStatsV12v0Group,
       "tmnxIPsecRUSAStatsV12v0Group": tmnxIPsecRUSAStatsV12v0Group,
       "tmnxIPsecEncapNotifyObjsGroup": tmnxIPsecEncapNotifyObjsGroup,
       "tmnxIPsecTnlOperChgGroup": tmnxIPsecTnlOperChgGroup,
       "tmnxIkePolicyAutoEapRadiusGroup": tmnxIkePolicyAutoEapRadiusGroup,
       "tmnxIkePolicyAutoEapGroup": tmnxIkePolicyAutoEapGroup,
       "tmnxIPsecGWDhcpGroup": tmnxIPsecGWDhcpGroup,
       "tmnxIPsecGWDhcpV6Group": tmnxIPsecGWDhcpV6Group,
       "tmnxSecNotifyObjsV13v0Group": tmnxSecNotifyObjsV13v0Group,
       "tmnxSecurityNotificationV13v0Grp": tmnxSecurityNotificationV13v0Grp,
       "tmnxIPsecGWLclAddrGroup": tmnxIPsecGWLclAddrGroup,
       "tmnxIPsecRadInterimUpdGroup": tmnxIPsecRadInterimUpdGroup,
       "tmnxIPsecIkev2IdiGroup": tmnxIPsecIkev2IdiGroup,
       "tmnxIPsecGWPrivIp2V13v0Group": tmnxIPsecGWPrivIp2V13v0Group,
       "tmnxIPsecGWLAAIpPool2V14v0Group": tmnxIPsecGWLAAIpPool2V14v0Group,
       "tIPsecTrafficSelectorV14v0Group": tIPsecTrafficSelectorV14v0Group,
       "tmnxIkePolicyLockoutV14v0Group": tmnxIkePolicyLockoutV14v0Group,
       "tIPsecRUTnlDhcpLeaseStatV14v0Grp": tIPsecRUTnlDhcpLeaseStatV14v0Grp,
       "tIPsecClientDatabaseV14v0Group": tIPsecClientDatabaseV14v0Group,
       "tmnxIkePolicyV2FragV14v0Group": tmnxIkePolicyV2FragV14v0Group,
       "tmnxIPsecMdaDpStatsV14v0Group": tmnxIPsecMdaDpStatsV14v0Group,
       "tmnxIPsecRUTnlInUseCfgsV14v0Grp": tmnxIPsecRUTnlInUseCfgsV14v0Grp,
       "tmnxIPsecIkeTransformV15v0Group": tmnxIPsecIkeTransformV15v0Group,
       "tmnxIPsecIkePolicyV14v0Group": tmnxIPsecIkePolicyV14v0Group,
       "tmnxIPsecHistStatsV15v0Group": tmnxIPsecHistStatsV15v0Group,
       "tmnxIPsecCertObsoleteV15v0Group": tmnxIPsecCertObsoleteV15v0Group,
       "tIPsecTcpMssAdjustV15v0Grp": tIPsecTcpMssAdjustV15v0Grp,
       "tmnxIkePolicyObsoleteV15v0Group": tmnxIkePolicyObsoleteV15v0Group,
       "tmnxIPsecSvcLevelCfgV14v0Grp": tmnxIPsecSvcLevelCfgV14v0Grp,
       "tmnxIPsecTransformV15v0Group": tmnxIPsecTransformV15v0Group,
       "tmnxIPsecEmbmsV15v0Group": tmnxIPsecEmbmsV15v0Group,
       "tmnxIPsecGWStatsV15v0Grp": tmnxIPsecGWStatsV15v0Grp,
       "tmnxIPsecNoOfSaKeysV16v0Grp": tmnxIPsecNoOfSaKeysV16v0Grp,
       "tmnxIPsecSvcNameV16v0Grp": tmnxIPsecSvcNameV16v0Grp,
       "tmnxIPsecTnlBfdSessV16v0Grp": tmnxIPsecTnlBfdSessV16v0Grp,
       "tmnxIPsecTnlBfdObsoleteV16v0Grp": tmnxIPsecTnlBfdObsoleteV16v0Grp,
       "tmnxIkePolicyV15v0Group": tmnxIkePolicyV15v0Group,
       "tmnxIPsecCertProfV16v0Group": tmnxIPsecCertProfV16v0Group,
       "tmnxIkeTransformV16v0Grp": tmnxIkeTransformV16v0Grp,
       "tmnxIPsecTunnelV15v0Grp": tmnxIPsecTunnelV15v0Grp,
       "tmnxVRtrIdIPsecTnlV19v0Group": tmnxVRtrIdIPsecTnlV19v0Group,
       "tIPsecTnlTempGroupV19v0Group": tIPsecTnlTempGroupV19v0Group,
       "tmnxIPsecNotifyObjsV19v0Group": tmnxIPsecNotifyObjsV19v0Group,
       "tmnxIPsecTunnelEsaVmV19v0Group": tmnxIPsecTunnelEsaVmV19v0Group,
       "tmnxIPsecTunnelEsaVmV20v0Group": tmnxIPsecTunnelEsaVmV20v0Group,
       "tmnxIPsecObsoleteV20v0Grp": tmnxIPsecObsoleteV20v0Grp,
       "tmnxIPsecSvcLevelCfgV20v0Grp": tmnxIPsecSvcLevelCfgV20v0Grp,
       "tmnxIPsecNotifGroups": tmnxIPsecNotifGroups,
       "tmnxIPsecNotifGroup": tmnxIPsecNotifGroup,
       "tIPsecIkev2RaTunNotifGroup": tIPsecIkev2RaTunNotifGroup,
       "tIPSecTrustAnchorProfNotifGroup": tIPSecTrustAnchorProfNotifGroup,
       "tIPSecTunnelEncapNotifGroup": tIPSecTunnelEncapNotifGroup,
       "tmnxIPSecTunnelNotifV11v0Group": tmnxIPSecTunnelNotifV11v0Group,
       "tmnxIPSecGWNotifV13v0Group": tmnxIPSecGWNotifV13v0Group,
       "tmnxIPsecTunnelNotifV19v0Group": tmnxIPsecTunnelNotifV19v0Group,
       "tmnxIPsecMGCompliances": tmnxIPsecMGCompliances,
       "tmnxIPsecMGGroups": tmnxIPsecMGGroups,
       "tmnxIPsecObjects": tmnxIPsecObjects,
       "tmnxIPsecTransformTblLastChanged": tmnxIPsecTransformTblLastChanged,
       "tmnxIPsecTransformTable": tmnxIPsecTransformTable,
       "tmnxIPsecTransformEntry": tmnxIPsecTransformEntry,
       "tmnxIPsecTransformId": tmnxIPsecTransformId,
       "tmnxIPsecTransformRowStatus": tmnxIPsecTransformRowStatus,
       "tmnxIPsecTransformLastChanged": tmnxIPsecTransformLastChanged,
       "tmnxIPsecTransformAuthAlgorithm": tmnxIPsecTransformAuthAlgorithm,
       "tmnxIPsecTransformEncrAlgorithm": tmnxIPsecTransformEncrAlgorithm,
       "tmnxIPsecTransformPfsDhGroup": tmnxIPsecTransformPfsDhGroup,
       "tmnxIPsecTransformLifeTime": tmnxIPsecTransformLifeTime,
       "tmnxIkePolicyTableLastChanged": tmnxIkePolicyTableLastChanged,
       "tmnxIkePolicyTable": tmnxIkePolicyTable,
       "tmnxIkePolicyEntry": tmnxIkePolicyEntry,
       "tmnxIkePolicyId": tmnxIkePolicyId,
       "tmnxIkePolicyRowStatus": tmnxIkePolicyRowStatus,
       "tmnxIkePolicyLastChanged": tmnxIkePolicyLastChanged,
       "tmnxIkePolicyDescription": tmnxIkePolicyDescription,
       "tmnxIkePolicyIkeMode": tmnxIkePolicyIkeMode,
       "tmnxIkePolicyDHGroup": tmnxIkePolicyDHGroup,
       "tmnxIkePolicyPFSEnabled": tmnxIkePolicyPFSEnabled,
       "tmnxIkePolicyPFSDHGroup": tmnxIkePolicyPFSDHGroup,
       "tmnxIkePolicyAuthAlgorithm": tmnxIkePolicyAuthAlgorithm,
       "tmnxIkePolicyEncrAlgorithm": tmnxIkePolicyEncrAlgorithm,
       "tmnxIkePolicyIsakmpLifeTime": tmnxIkePolicyIsakmpLifeTime,
       "tmnxIkePolicyIPsecLifeTime": tmnxIkePolicyIPsecLifeTime,
       "tmnxIkePolicyNatTraversal": tmnxIkePolicyNatTraversal,
       "tmnxIkePolicyNatTKeepAliveIntvl": tmnxIkePolicyNatTKeepAliveIntvl,
       "tmnxIkePolicyNatTBehindNatOnly": tmnxIkePolicyNatTBehindNatOnly,
       "tmnxIkePolicyDpd": tmnxIkePolicyDpd,
       "tmnxIkePolicyDpdInterval": tmnxIkePolicyDpdInterval,
       "tmnxIkePolicyDpdMaxRetries": tmnxIkePolicyDpdMaxRetries,
       "tmnxIkePolicyAuthMethod": tmnxIkePolicyAuthMethod,
       "tmnxIkePolicyIkeVersion": tmnxIkePolicyIkeVersion,
       "tmnxIkePolicyOwnAuthMethod": tmnxIkePolicyOwnAuthMethod,
       "tmnxIkePolicyMatchPeerToCert": tmnxIkePolicyMatchPeerToCert,
       "tmnxIkePolicyRelayUnSolCfgAttr": tmnxIkePolicyRelayUnSolCfgAttr,
       "tmnxIkePolicyAutoEapMethod": tmnxIkePolicyAutoEapMethod,
       "tmnxIkePolicyAutoEapOwnMethod": tmnxIkePolicyAutoEapOwnMethod,
       "tmnxIkePolicyLockout": tmnxIkePolicyLockout,
       "tmnxIkePolicyLockoutFailedAtempt": tmnxIkePolicyLockoutFailedAtempt,
       "tmnxIkePolicyLockoutDuration": tmnxIkePolicyLockoutDuration,
       "tmnxIkePolicyLockoutBlock": tmnxIkePolicyLockoutBlock,
       "tmnxIkePolicyLockoutMaxPortPerIp": tmnxIkePolicyLockoutMaxPortPerIp,
       "tmnxIkePolicyV2Fragment": tmnxIkePolicyV2Fragment,
       "tmnxIkePolicyV2FragmentMtu": tmnxIkePolicyV2FragmentMtu,
       "tmnxIkePolicyV2FragReassembTmOut": tmnxIkePolicyV2FragReassembTmOut,
       "tmnxIkePolicySndIdrAftEapSuccess": tmnxIkePolicySndIdrAftEapSuccess,
       "tmnxIkePolicyIkev1Ph1RespDelNtfy": tmnxIkePolicyIkev1Ph1RespDelNtfy,
       "tmnxIkePolicyLimitInitExchange": tmnxIkePolicyLimitInitExchange,
       "tmnxIkePolicyReducedMaxExchgTt": tmnxIkePolicyReducedMaxExchgTt,
       "tmnxIPsecTunnelTableLastChanged": tmnxIPsecTunnelTableLastChanged,
       "tmnxIPsecTunnelTable": tmnxIPsecTunnelTable,
       "tmnxIPsecTunnelEntry": tmnxIPsecTunnelEntry,
       "tmnxIPsecTunnelName": tmnxIPsecTunnelName,
       "tmnxIPsecTunnelRowStatus": tmnxIPsecTunnelRowStatus,
       "tmnxIPsecTunnelLastChanged": tmnxIPsecTunnelLastChanged,
       "tmnxIPsecTunnelDescription": tmnxIPsecTunnelDescription,
       "tmnxIPsecTunnelLclGwAddrType": tmnxIPsecTunnelLclGwAddrType,
       "tmnxIPsecTunnelLclGwAddr": tmnxIPsecTunnelLclGwAddr,
       "tmnxIPsecTunnelRemGwAddrType": tmnxIPsecTunnelRemGwAddrType,
       "tmnxIPsecTunnelRemGwAddr": tmnxIPsecTunnelRemGwAddr,
       "tmnxIPsecTunnelPublicSvcId": tmnxIPsecTunnelPublicSvcId,
       "tmnxIPsecTunnelSecurityPolicyId": tmnxIPsecTunnelSecurityPolicyId,
       "tmnxIPsecTunnelKeyingType": tmnxIPsecTunnelKeyingType,
       "tmnxIPsecTunnelDynTransformId1": tmnxIPsecTunnelDynTransformId1,
       "tmnxIPsecTunnelDynTransformId2": tmnxIPsecTunnelDynTransformId2,
       "tmnxIPsecTunnelDynTransformId3": tmnxIPsecTunnelDynTransformId3,
       "tmnxIPsecTunnelDynTransformId4": tmnxIPsecTunnelDynTransformId4,
       "tmnxIPsecTunnelIkePolicyId": tmnxIPsecTunnelIkePolicyId,
       "tmnxIPsecTunnelIkePreSharedKey": tmnxIPsecTunnelIkePreSharedKey,
       "tmnxIPsecTunnelAdminState": tmnxIPsecTunnelAdminState,
       "tmnxIPsecTunnelOperState": tmnxIPsecTunnelOperState,
       "tmnxIPsecTunnelOperFlags": tmnxIPsecTunnelOperFlags,
       "tmnxIPsecTunnelReplayWindow": tmnxIPsecTunnelReplayWindow,
       "tmnxIPsecTunnelAutoEstablish": tmnxIPsecTunnelAutoEstablish,
       "tmnxIPsecTunnelBfdDesignate": tmnxIPsecTunnelBfdDesignate,
       "tmnxIPsecTunnelCertTrustAnchor": tmnxIPsecTunnelCertTrustAnchor,
       "tmnxIPsecTunnelCertFile": tmnxIPsecTunnelCertFile,
       "tmnxIPsecTunnelKeyFile": tmnxIPsecTunnelKeyFile,
       "tmnxIPsecTunnelLocalIdType": tmnxIPsecTunnelLocalIdType,
       "tmnxIPsecTunnelLocalIdValue": tmnxIPsecTunnelLocalIdValue,
       "tmnxIPsecTunnelClearDfBit": tmnxIPsecTunnelClearDfBit,
       "tmnxIPsecTunnelIpMtu": tmnxIPsecTunnelIpMtu,
       "tmnxIPsecTunnelHostISA": tmnxIPsecTunnelHostISA,
       "tmnxIPsecTunnelCSVPrimary": tmnxIPsecTunnelCSVPrimary,
       "tmnxIPsecTunnelCSVSecondary": tmnxIPsecTunnelCSVSecondary,
       "tmnxIPsecTunnelCSVDefResult": tmnxIPsecTunnelCSVDefResult,
       "tmnxIPsecTunnelCertProfile": tmnxIPsecTunnelCertProfile,
       "tmnxIPsecTunnelMatchTrustAnchor": tmnxIPsecTunnelMatchTrustAnchor,
       "tmnxIPsecTunnelCertTrstAnchrProf": tmnxIPsecTunnelCertTrstAnchrProf,
       "tmnxIPsecTunnelEncapIpMtu": tmnxIPsecTunnelEncapIpMtu,
       "tmnxIPsecTunnelIcmp6Pkt2Big": tmnxIPsecTunnelIcmp6Pkt2Big,
       "tmnxIPsecTunnelIcmp6NumPkt2Big": tmnxIPsecTunnelIcmp6NumPkt2Big,
       "tmnxIPsecTunnelIcmp6Pkt2BigTime": tmnxIPsecTunnelIcmp6Pkt2BigTime,
       "tmnxIPsecTunnelOperChanged": tmnxIPsecTunnelOperChanged,
       "tmnxIPsecTunnelPubTcpMssAdjust": tmnxIPsecTunnelPubTcpMssAdjust,
       "tmnxIPsecTunnelPrivTcpMssAdjust": tmnxIPsecTunnelPrivTcpMssAdjust,
       "tmnxIPsecTunnelMaxNumPh1SaKeys": tmnxIPsecTunnelMaxNumPh1SaKeys,
       "tmnxIPsecTunnelMaxNumPh2SaKeys": tmnxIPsecTunnelMaxNumPh2SaKeys,
       "tmnxIPsecTunnelPublicSvcName": tmnxIPsecTunnelPublicSvcName,
       "tmnxIPsecTunnelSecPlyStrictMatch": tmnxIPsecTunnelSecPlyStrictMatch,
       "tmnxIPsecTunnelHostEsa": tmnxIPsecTunnelHostEsa,
       "tmnxIPsecTunnelHostEsaVm": tmnxIPsecTunnelHostEsaVm,
       "tmnxIPsecTunnelStatsTable": tmnxIPsecTunnelStatsTable,
       "tmnxIPsecTunnelStatsEntry": tmnxIPsecTunnelStatsEntry,
       "tmnxIPsecTunnelIsakmpState": tmnxIPsecTunnelIsakmpState,
       "tmnxIPsecTunnelIsakmpEstabTime": tmnxIPsecTunnelIsakmpEstabTime,
       "tmnxIPsecTunnelIsakmpNegLifeTime": tmnxIPsecTunnelIsakmpNegLifeTime,
       "tmnxIPsecTunnelNumDpdTx": tmnxIPsecTunnelNumDpdTx,
       "tmnxIPsecTunnelNumDpdRx": tmnxIPsecTunnelNumDpdRx,
       "tmnxIPsecTunnelNumDpdAckTx": tmnxIPsecTunnelNumDpdAckTx,
       "tmnxIPsecTunnelNumDpdAckRx": tmnxIPsecTunnelNumDpdAckRx,
       "tmnxIPsecTunnelNumExpRx": tmnxIPsecTunnelNumExpRx,
       "tmnxIPsecTunnelNumInvalidDpdRx": tmnxIPsecTunnelNumInvalidDpdRx,
       "tmnxIPsecTunnelNumCtrlPktsTx": tmnxIPsecTunnelNumCtrlPktsTx,
       "tmnxIPsecTunnelNumCtrlPktsRx": tmnxIPsecTunnelNumCtrlPktsRx,
       "tmnxIPsecTunnelNumCtrlTxErrors": tmnxIPsecTunnelNumCtrlTxErrors,
       "tmnxIPsecTunnelNumCtrlRxErrors": tmnxIPsecTunnelNumCtrlRxErrors,
       "tmnxIPsecTunnelMatCertEntryId": tmnxIPsecTunnelMatCertEntryId,
       "tmnxIPsecTunnelCertProfName": tmnxIPsecTunnelCertProfName,
       "tmnxIPsecTunnelStatIsakmpAuthAlg": tmnxIPsecTunnelStatIsakmpAuthAlg,
       "tmnxIPsecTunnelStatIsakmpEncrAlg": tmnxIPsecTunnelStatIsakmpEncrAlg,
       "tmnxIPsecTunnelStatIsakmpPfsDhGp": tmnxIPsecTunnelStatIsakmpPfsDhGp,
       "tmnxIPsecTunnelStatIkeTranPrfAlg": tmnxIPsecTunnelStatIkeTranPrfAlg,
       "tmnxIPsecPolicyTableLastChanged": tmnxIPsecPolicyTableLastChanged,
       "tmnxIPsecPolicyTable": tmnxIPsecPolicyTable,
       "tmnxIPsecPolicyEntry": tmnxIPsecPolicyEntry,
       "tmnxIPsecPolicyId": tmnxIPsecPolicyId,
       "tmnxIPsecPolicyRowStatus": tmnxIPsecPolicyRowStatus,
       "tmnxIPsecPolicyLastChanged": tmnxIPsecPolicyLastChanged,
       "tmnxIPsecPlcyParamsTblLastChangd": tmnxIPsecPlcyParamsTblLastChangd,
       "tmnxIPsecPolicyParamsTable": tmnxIPsecPolicyParamsTable,
       "tmnxIPsecPolicyParamsEntry": tmnxIPsecPolicyParamsEntry,
       "tmnxIPsecPolicyParamsId": tmnxIPsecPolicyParamsId,
       "tmnxIPsecPolicyParamsRowStatus": tmnxIPsecPolicyParamsRowStatus,
       "tmnxIPsecPolicyParamsLastChanged": tmnxIPsecPolicyParamsLastChanged,
       "tmnxIPsecPolicyParamsLclAddrAny": tmnxIPsecPolicyParamsLclAddrAny,
       "tmnxIPsecPolicyParamsLclAddrType": tmnxIPsecPolicyParamsLclAddrType,
       "tmnxIPsecPolicyParamsLclAddr": tmnxIPsecPolicyParamsLclAddr,
       "tmnxIPsecPolicyParamsLclAPrefLen": tmnxIPsecPolicyParamsLclAPrefLen,
       "tmnxIPsecPolicyParamsRemAddrAny": tmnxIPsecPolicyParamsRemAddrAny,
       "tmnxIPsecPolicyParamsRemAddrType": tmnxIPsecPolicyParamsRemAddrType,
       "tmnxIPsecPolicyParamsRemAddr": tmnxIPsecPolicyParamsRemAddr,
       "tmnxIPsecPolicyParamsRemAPrefLen": tmnxIPsecPolicyParamsRemAPrefLen,
       "tmnxIPsecPlcyParamsV6LclAddrAny": tmnxIPsecPlcyParamsV6LclAddrAny,
       "tmnxIPsecPlcyParamsV6LclAddrType": tmnxIPsecPlcyParamsV6LclAddrType,
       "tmnxIPsecPlcyParamsV6LclAddr": tmnxIPsecPlcyParamsV6LclAddr,
       "tmnxIPsecPlcyParamsV6LclAPrefLen": tmnxIPsecPlcyParamsV6LclAPrefLen,
       "tmnxIPsecPlcyParamsV6RemAddrAny": tmnxIPsecPlcyParamsV6RemAddrAny,
       "tmnxIPsecPlcyParamsV6RemAddrType": tmnxIPsecPlcyParamsV6RemAddrType,
       "tmnxIPsecPlcyParamsV6RemAddr": tmnxIPsecPlcyParamsV6RemAddr,
       "tmnxIPsecPlcyParamsV6RemAPrefLen": tmnxIPsecPlcyParamsV6RemAPrefLen,
       "tmnxIPsecSATableLastChanged": tmnxIPsecSATableLastChanged,
       "tmnxIPsecSATable": tmnxIPsecSATable,
       "tmnxIPsecSAEntry": tmnxIPsecSAEntry,
       "tmnxIPsecSAId": tmnxIPsecSAId,
       "tmnxIPsecSAIndex": tmnxIPsecSAIndex,
       "tmnxIPsecSADirection": tmnxIPsecSADirection,
       "tmnxIPsecSARowStatus": tmnxIPsecSARowStatus,
       "tmnxIPsecSALastChanged": tmnxIPsecSALastChanged,
       "tmnxIPsecSAType": tmnxIPsecSAType,
       "tmnxIPsecSAEncryptionKey": tmnxIPsecSAEncryptionKey,
       "tmnxIPsecSAAuthenticationKey": tmnxIPsecSAAuthenticationKey,
       "tmnxIPsecSASpi": tmnxIPsecSASpi,
       "tmnxIPsecSAManualTransformId": tmnxIPsecSAManualTransformId,
       "tmnxIPsecSAAuthAlgorithm": tmnxIPsecSAAuthAlgorithm,
       "tmnxIPsecSAEncrAlgorithm": tmnxIPsecSAEncrAlgorithm,
       "tmnxIPsecSAStorageType": tmnxIPsecSAStorageType,
       "tmnxIPsecSAEstablishedTime": tmnxIPsecSAEstablishedTime,
       "tmnxIPsecSANegotiatedLifeTime": tmnxIPsecSANegotiatedLifeTime,
       "tmnxIPsecSAStatsTable": tmnxIPsecSAStatsTable,
       "tmnxIPsecSAStatsEntry": tmnxIPsecSAStatsEntry,
       "tmnxIPsecSAStatsBytesProcessed": tmnxIPsecSAStatsBytesProcessed,
       "tmnxIPsecSAStatsBytesProcLow32": tmnxIPsecSAStatsBytesProcLow32,
       "tmnxIPsecSAStatsBytesProcHigh32": tmnxIPsecSAStatsBytesProcHigh32,
       "tmnxIPsecSAStatsPktsProcessed": tmnxIPsecSAStatsPktsProcessed,
       "tmnxIPsecSAStatsPktsProcLow32": tmnxIPsecSAStatsPktsProcLow32,
       "tmnxIPsecSAStatsPktsProcHigh32": tmnxIPsecSAStatsPktsProcHigh32,
       "tmnxIPsecSAStatsCryptoErrors": tmnxIPsecSAStatsCryptoErrors,
       "tmnxIPsecSAStatsReplayErrors": tmnxIPsecSAStatsReplayErrors,
       "tmnxIPsecSAStatsSAErrors": tmnxIPsecSAStatsSAErrors,
       "tmnxIPsecSAStatsPolicyErrors": tmnxIPsecSAStatsPolicyErrors,
       "tmnxIPsecSAStatsEncapOverhead": tmnxIPsecSAStatsEncapOverhead,
       "tmnxIPsecSAStatsPreEncapFragCnt": tmnxIPsecSAStatsPreEncapFragCnt,
       "tmnxIPsecSAStatsPreEncapFragLtSz": tmnxIPsecSAStatsPreEncapFragLtSz,
       "tmnxIPsecSAStatsPstEncapFragCnt": tmnxIPsecSAStatsPstEncapFragCnt,
       "tmnxIPsecSAStatsPstEncapFragLtSz": tmnxIPsecSAStatsPstEncapFragLtSz,
       "tmnxIPsecSAStatsPfsDhGroup": tmnxIPsecSAStatsPfsDhGroup,
       "tmnxIPsecSAStatsMulticastIfName": tmnxIPsecSAStatsMulticastIfName,
       "tmnxIPsecSAStatsMulticastProt": tmnxIPsecSAStatsMulticastProt,
       "tmnxIPsecMdaDpStatsTable": tmnxIPsecMdaDpStatsTable,
       "tmnxIPsecMdaDpStatsEntry": tmnxIPsecMdaDpStatsEntry,
       "tmnxIPsecMdaDpStatsEncryptPkts": tmnxIPsecMdaDpStatsEncryptPkts,
       "tmnxIPsecMdaDpStatsEncryptPktsLow32": tmnxIPsecMdaDpStatsEncryptPktsLow32,
       "tmnxIPsecMdaDpStatsEncryptPktsHigh32": tmnxIPsecMdaDpStatsEncryptPktsHigh32,
       "tmnxIPsecMdaDpStatsEncryptBytes": tmnxIPsecMdaDpStatsEncryptBytes,
       "tmnxIPsecMdaDpStatsEncryptBytesLow32": tmnxIPsecMdaDpStatsEncryptBytesLow32,
       "tmnxIPsecMdaDpStatsEncryptBytesHigh32": tmnxIPsecMdaDpStatsEncryptBytesHigh32,
       "tmnxIPsecMdaDpStatsDecryptPkts": tmnxIPsecMdaDpStatsDecryptPkts,
       "tmnxIPsecMdaDpStatsDecryptPktsLow32": tmnxIPsecMdaDpStatsDecryptPktsLow32,
       "tmnxIPsecMdaDpStatsDecryptPktsHigh32": tmnxIPsecMdaDpStatsDecryptPktsHigh32,
       "tmnxIPsecMdaDpStatsDecryptBytes": tmnxIPsecMdaDpStatsDecryptBytes,
       "tmnxIPsecMdaDpStatsDecryptBytesLow32": tmnxIPsecMdaDpStatsDecryptBytesLow32,
       "tmnxIPsecMdaDpStatsDecryptBytesHigh32": tmnxIPsecMdaDpStatsDecryptBytesHigh32,
       "tmnxIPsecMdaDpStatsTxPktErrs": tmnxIPsecMdaDpStatsTxPktErrs,
       "tmnxIPsecMdaDpStatsOutBDropPkts": tmnxIPsecMdaDpStatsOutBDropPkts,
       "tmnxIPsecMdaDpStatsOutBDropPktsLow32": tmnxIPsecMdaDpStatsOutBDropPktsLow32,
       "tmnxIPsecMdaDpStatsOutBDropPktsHigh32": tmnxIPsecMdaDpStatsOutBDropPktsHigh32,
       "tmnxIPsecMdaDpStatsOutBSAMisses": tmnxIPsecMdaDpStatsOutBSAMisses,
       "tmnxIPsecMdaDpStatsOutBSAMissesLow32": tmnxIPsecMdaDpStatsOutBSAMissesLow32,
       "tmnxIPsecMdaDpStatsOutBSAMissesHigh32": tmnxIPsecMdaDpStatsOutBSAMissesHigh32,
       "tmnxIPsecMdaDpStatsOutBPolicyEntryMisses": tmnxIPsecMdaDpStatsOutBPolicyEntryMisses,
       "tmnxIPsecMdaDpStatsInBDropPkts": tmnxIPsecMdaDpStatsInBDropPkts,
       "tmnxIPsecMdaDpStatsInBDropPktsLow32": tmnxIPsecMdaDpStatsInBDropPktsLow32,
       "tmnxIPsecMdaDpStatsInBDropPktsHigh32": tmnxIPsecMdaDpStatsInBDropPktsHigh32,
       "tmnxIPsecMdaDpStatsInBSAMisses": tmnxIPsecMdaDpStatsInBSAMisses,
       "tmnxIPsecMdaDpStatsInBSAMissesLow32": tmnxIPsecMdaDpStatsInBSAMissesLow32,
       "tmnxIPsecMdaDpStatsInBSAMissesHigh32": tmnxIPsecMdaDpStatsInBSAMissesHigh32,
       "tmnxIPsecMdaDpStatsInBIPDstSrcMismatches": tmnxIPsecMdaDpStatsInBIPDstSrcMismatches,
       "tmnxIPsecMdaDpInFragments": tmnxIPsecMdaDpInFragments,
       "tmnxIPsecMdaDpInFragmentsLow32": tmnxIPsecMdaDpInFragmentsLow32,
       "tmnxIPsecMdaDpInFragmentsHigh32": tmnxIPsecMdaDpInFragmentsHigh32,
       "tmnxIPsecMdaDpPktsReassem": tmnxIPsecMdaDpPktsReassem,
       "tmnxIPsecMdaDpPktsReassemLow32": tmnxIPsecMdaDpPktsReassemLow32,
       "tmnxIPsecMdaDpPktsReassemHigh32": tmnxIPsecMdaDpPktsReassemHigh32,
       "tmnxIPsecMdaDpFragDropTime": tmnxIPsecMdaDpFragDropTime,
       "tmnxIPsecMdaDpFragDropTimeLow32": tmnxIPsecMdaDpFragDropTimeLow32,
       "tmnxIPsecMdaDpFragDropTimeHigh32": tmnxIPsecMdaDpFragDropTimeHigh32,
       "tmnxIPsecMdaDpFragDropped": tmnxIPsecMdaDpFragDropped,
       "tmnxIPsecMdaDpFragDroppedLow32": tmnxIPsecMdaDpFragDroppedLow32,
       "tmnxIPsecMdaDpFragDroppedHigh32": tmnxIPsecMdaDpFragDroppedHigh32,
       "tmnxIPsecMdaDpGreTnlInPkts": tmnxIPsecMdaDpGreTnlInPkts,
       "tmnxIPsecMdaDpGreTnlInPktsLo": tmnxIPsecMdaDpGreTnlInPktsLo,
       "tmnxIPsecMdaDpGreTnlInPktsHi": tmnxIPsecMdaDpGreTnlInPktsHi,
       "tmnxIPsecMdaDpGreTnlInBytes": tmnxIPsecMdaDpGreTnlInBytes,
       "tmnxIPsecMdaDpGreTnlInBytesLo": tmnxIPsecMdaDpGreTnlInBytesLo,
       "tmnxIPsecMdaDpGreTnlInBytesHi": tmnxIPsecMdaDpGreTnlInBytesHi,
       "tmnxIPsecMdaDpGreTnlInErrs": tmnxIPsecMdaDpGreTnlInErrs,
       "tmnxIPsecMdaDpGreTnlInErrsLo": tmnxIPsecMdaDpGreTnlInErrsLo,
       "tmnxIPsecMdaDpGreTnlInErrsHi": tmnxIPsecMdaDpGreTnlInErrsHi,
       "tmnxIPsecMdaDpGreTnlOutPkts": tmnxIPsecMdaDpGreTnlOutPkts,
       "tmnxIPsecMdaDpGreTnlOutPktsLo": tmnxIPsecMdaDpGreTnlOutPktsLo,
       "tmnxIPsecMdaDpGreTnlOutPktsHi": tmnxIPsecMdaDpGreTnlOutPktsHi,
       "tmnxIPsecMdaDpGreTnlOutBytes": tmnxIPsecMdaDpGreTnlOutBytes,
       "tmnxIPsecMdaDpGreTnlOutBytesLo": tmnxIPsecMdaDpGreTnlOutBytesLo,
       "tmnxIPsecMdaDpGreTnlOutBytesHi": tmnxIPsecMdaDpGreTnlOutBytesHi,
       "tmnxIPsecMdaDpGreTnlOutErrs": tmnxIPsecMdaDpGreTnlOutErrs,
       "tmnxIPsecMdaDpGreTnlOutErrsLo": tmnxIPsecMdaDpGreTnlOutErrsLo,
       "tmnxIPsecMdaDpGreTnlOutErrsHi": tmnxIPsecMdaDpGreTnlOutErrsHi,
       "tmnxIPsecMdaDpPktsDropDfSet": tmnxIPsecMdaDpPktsDropDfSet,
       "tmnxIPsecMdaDpPktsDropDfSetLo": tmnxIPsecMdaDpPktsDropDfSetLo,
       "tmnxIPsecMdaDpPktsDropDfSetHi": tmnxIPsecMdaDpPktsDropDfSetHi,
       "tmnxIPsecMdaDpStaticIPsecTnls": tmnxIPsecMdaDpStaticIPsecTnls,
       "tmnxIPsecMdaDpDynIPsecTnls": tmnxIPsecMdaDpDynIPsecTnls,
       "tmnxIPsecMdaDpIpGreTnls": tmnxIPsecMdaDpIpGreTnls,
       "tmnxIPsecMdaDpIpv4Tnls": tmnxIPsecMdaDpIpv4Tnls,
       "tmnxIPsecMdaDpL2tpv3TnlInPkts": tmnxIPsecMdaDpL2tpv3TnlInPkts,
       "tmnxIPsecMdaDpL2tpv3TnlInBytes": tmnxIPsecMdaDpL2tpv3TnlInBytes,
       "tmnxIPsecMdaDpL2tpv3TnlInErrs": tmnxIPsecMdaDpL2tpv3TnlInErrs,
       "tmnxIPsecMdaDpL2tpv3TnlInCookErr": tmnxIPsecMdaDpL2tpv3TnlInCookErr,
       "tmnxIPsecMdaDpL2tpv3TnlInSeIdErr": tmnxIPsecMdaDpL2tpv3TnlInSeIdErr,
       "tmnxIPsecMdaDpL2tpv3TnlOutPkts": tmnxIPsecMdaDpL2tpv3TnlOutPkts,
       "tmnxIPsecMdaDpL2tpv3TnlOutBytes": tmnxIPsecMdaDpL2tpv3TnlOutBytes,
       "tmnxIPsecMdaDpL2tpv3TnlOutErrs": tmnxIPsecMdaDpL2tpv3TnlOutErrs,
       "tmnxIPsecMdaDpL2tpv3Tnls": tmnxIPsecMdaDpL2tpv3Tnls,
       "tIPsecTnlTempTblLastChanged": tIPsecTnlTempTblLastChanged,
       "tIPsecTnlTempTable": tIPsecTnlTempTable,
       "tIPsecTnlTempEntry": tIPsecTnlTempEntry,
       "tIPsecTnlTempId": tIPsecTnlTempId,
       "tIPsecTnlTempRowStatus": tIPsecTnlTempRowStatus,
       "tIPsecTnlTempLastChanged": tIPsecTnlTempLastChanged,
       "tIPsecTnlTempDescr": tIPsecTnlTempDescr,
       "tIPsecTnlTempReverseRoute": tIPsecTnlTempReverseRoute,
       "tIPsecTnlTempDynKeyTransformId1": tIPsecTnlTempDynKeyTransformId1,
       "tIPsecTnlTempDynKeyTransformId2": tIPsecTnlTempDynKeyTransformId2,
       "tIPsecTnlTempDynKeyTransformId3": tIPsecTnlTempDynKeyTransformId3,
       "tIPsecTnlTempDynKeyTransformId4": tIPsecTnlTempDynKeyTransformId4,
       "tIPsecTnlTempReplayWindow": tIPsecTnlTempReplayWindow,
       "tIPsecTnlTempIpMtu": tIPsecTnlTempIpMtu,
       "tIPsecTnlTempEncapIpMtu": tIPsecTnlTempEncapIpMtu,
       "tIPsecTnlTempIcmp6Pkt2Big": tIPsecTnlTempIcmp6Pkt2Big,
       "tIPsecTnlTempIcmp6NumPkt2Big": tIPsecTnlTempIcmp6NumPkt2Big,
       "tIPsecTnlTempIcmp6Pkt2BigTime": tIPsecTnlTempIcmp6Pkt2BigTime,
       "tIPsecTnlTempClearDfBit": tIPsecTnlTempClearDfBit,
       "tIPsecTnlTempPublicTcpMssAdjust": tIPsecTnlTempPublicTcpMssAdjust,
       "tIPsecTnlTempPrivateTcpMssAdjust": tIPsecTnlTempPrivateTcpMssAdjust,
       "tIPsecTnlTempIgnoreDefaultRoute": tIPsecTnlTempIgnoreDefaultRoute,
       "tmnxIPsecGWTblLastChgd": tmnxIPsecGWTblLastChgd,
       "tmnxIPsecGWTable": tmnxIPsecGWTable,
       "tmnxIPsecGWEntry": tmnxIPsecGWEntry,
       "tmnxIPsecGWRowStatus": tmnxIPsecGWRowStatus,
       "tmnxIPsecGWLastMgmtChange": tmnxIPsecGWLastMgmtChange,
       "tmnxIPsecGWAdminState": tmnxIPsecGWAdminState,
       "tmnxIPsecGWOperState": tmnxIPsecGWOperState,
       "tmnxIPsecGWTunnelPolicyTemp": tmnxIPsecGWTunnelPolicyTemp,
       "tmnxIPsecGWSecureService": tmnxIPsecGWSecureService,
       "tmnxIPsecGWIfName": tmnxIPsecGWIfName,
       "tmnxIPsecGWInetAddrType": tmnxIPsecGWInetAddrType,
       "tmnxIPsecGWInetAddress": tmnxIPsecGWInetAddress,
       "tmnxIPsecGWIkePolicyId": tmnxIPsecGWIkePolicyId,
       "tmnxIPsecGWIkePreShared": tmnxIPsecGWIkePreShared,
       "tmnxIPsecGWLclX509Cert": tmnxIPsecGWLclX509Cert,
       "tmnxIPsecGWLclPrivateKey": tmnxIPsecGWLclPrivateKey,
       "tmnxIPsecGWOperFlags": tmnxIPsecGWOperFlags,
       "tmnxIPsecGWCACert": tmnxIPsecGWCACert,
       "tmnxIPsecGWCACertRevocList": tmnxIPsecGWCACertRevocList,
       "tmnxIPsecGWName": tmnxIPsecGWName,
       "tmnxIPsecGWCertTrustAnchor": tmnxIPsecGWCertTrustAnchor,
       "tmnxIPsecGWLocalIdType": tmnxIPsecGWLocalIdType,
       "tmnxIPsecGWLocalIdValue": tmnxIPsecGWLocalIdValue,
       "tmnxIPsecGWCSVPrimary": tmnxIPsecGWCSVPrimary,
       "tmnxIPsecGWCSVSecondary": tmnxIPsecGWCSVSecondary,
       "tmnxIPsecGWCSVDefResult": tmnxIPsecGWCSVDefResult,
       "tmnxIPsecGWRadAcctgPolicy": tmnxIPsecGWRadAcctgPolicy,
       "tmnxIPsecGWRadAuthPolicy": tmnxIPsecGWRadAuthPolicy,
       "tmnxIPsecGWCertProfile": tmnxIPsecGWCertProfile,
       "tmnxIPsecGWCertTrstAnchrProf": tmnxIPsecGWCertTrstAnchrProf,
       "tmnxIPsecGWClientDatabaseName": tmnxIPsecGWClientDatabaseName,
       "tmnxIPsecGWClientDatabasFallback": tmnxIPsecGWClientDatabasFallback,
       "tmnxIPsecGWMaxNumPh1SaKeys": tmnxIPsecGWMaxNumPh1SaKeys,
       "tmnxIPsecGWMaxNumPh2SaKeys": tmnxIPsecGWMaxNumPh2SaKeys,
       "tmnxIPsecGWSecureServiceName": tmnxIPsecGWSecureServiceName,
       "tIPsecRUTnlTable": tIPsecRUTnlTable,
       "tIPsecRUTnlEntry": tIPsecRUTnlEntry,
       "tIPsecRUTnlInetAddrType": tIPsecRUTnlInetAddrType,
       "tIPsecRUTnlInetAddress": tIPsecRUTnlInetAddress,
       "tIPsecRUTnlPort": tIPsecRUTnlPort,
       "tIPsecRUTnlPrivateIpAddrType": tIPsecRUTnlPrivateIpAddrType,
       "tIPsecRUTnlPrivateIpAddr": tIPsecRUTnlPrivateIpAddr,
       "tIPsecRUTnlPrivateIpPrefixLen": tIPsecRUTnlPrivateIpPrefixLen,
       "tIPsecRUTnlTempId": tIPsecRUTnlTempId,
       "tIPsecRUTnlIPsecSALifeTime": tIPsecRUTnlIPsecSALifeTime,
       "tIPsecRUTnlPfsDHGroup": tIPsecRUTnlPfsDHGroup,
       "tIPsecRUTnlReplayWindow": tIPsecRUTnlReplayWindow,
       "tIPsecRUTnlPrivateSvcId": tIPsecRUTnlPrivateSvcId,
       "tIPsecRUTnlPrivateIfIndex": tIPsecRUTnlPrivateIfIndex,
       "tIPsecRUTnlHasBiDirectionalSA": tIPsecRUTnlHasBiDirectionalSA,
       "tIPsecRUTnlHostISA": tIPsecRUTnlHostISA,
       "tIPsecRUTnlMatchTrustAnchor": tIPsecRUTnlMatchTrustAnchor,
       "tIPsecRUTnlOperChanged": tIPsecRUTnlOperChanged,
       "tIPsecRUTnlIkeIdType": tIPsecRUTnlIkeIdType,
       "tIPsecRUTnlIkeIdValue": tIPsecRUTnlIkeIdValue,
       "tIPsecRUTnlPrivateIpAddr2Type": tIPsecRUTnlPrivateIpAddr2Type,
       "tIPsecRUTnlPrivateIpAddr2": tIPsecRUTnlPrivateIpAddr2,
       "tIPsecRUTnlPrivateIpPrefixLen2": tIPsecRUTnlPrivateIpPrefixLen2,
       "tIPsecRUTnlInUseTsList": tIPsecRUTnlInUseTsList,
       "tIPsecRUTnlInUsePreSharedKey": tIPsecRUTnlInUsePreSharedKey,
       "tIPsecRUTnlPubTcpMss": tIPsecRUTnlPubTcpMss,
       "tIPsecRUTnlPrivTcpMss": tIPsecRUTnlPrivTcpMss,
       "tIPsecRUTnlInUseIkePolicy": tIPsecRUTnlInUseIkePolicy,
       "tIPsecRUTnlHostEsa": tIPsecRUTnlHostEsa,
       "tIPsecRUTnlHostEsaVm": tIPsecRUTnlHostEsaVm,
       "tIPsecRUTnlStatsTable": tIPsecRUTnlStatsTable,
       "tIPsecRUTnlStatsEntry": tIPsecRUTnlStatsEntry,
       "tIPsecRUTnlIsakmpState": tIPsecRUTnlIsakmpState,
       "tIPsecRUTnlIsakmpEstabTime": tIPsecRUTnlIsakmpEstabTime,
       "tIPsecRUTnlIsakmpNegLifeTime": tIPsecRUTnlIsakmpNegLifeTime,
       "tIPsecRUTnlNumDpdTx": tIPsecRUTnlNumDpdTx,
       "tIPsecRUTnlNumDpdRx": tIPsecRUTnlNumDpdRx,
       "tIPsecRUTnlNumDpdAckTx": tIPsecRUTnlNumDpdAckTx,
       "tIPsecRUTnlNumDpdAckRx": tIPsecRUTnlNumDpdAckRx,
       "tIPsecRUTnlNumExpRx": tIPsecRUTnlNumExpRx,
       "tIPsecRUTnlNumInvalidDpdRx": tIPsecRUTnlNumInvalidDpdRx,
       "tIPsecRUTnlNumCtrlPktsTx": tIPsecRUTnlNumCtrlPktsTx,
       "tIPsecRUTnlNumCtrlPktsRx": tIPsecRUTnlNumCtrlPktsRx,
       "tIPsecRUTnlNumCtrlTxErrors": tIPsecRUTnlNumCtrlTxErrors,
       "tIPsecRUTnlNumCtrlRxErrors": tIPsecRUTnlNumCtrlRxErrors,
       "tIPsecRUTnlMatCertEntryId": tIPsecRUTnlMatCertEntryId,
       "tIPsecRUTnlCertProfName": tIPsecRUTnlCertProfName,
       "tIPsecRUTnlClientDBClientId": tIPsecRUTnlClientDBClientId,
       "tIPsecRUTnlStatsIsakmpAuthAlg": tIPsecRUTnlStatsIsakmpAuthAlg,
       "tIPsecRUTnlStatsIsakmpEncrAlg": tIPsecRUTnlStatsIsakmpEncrAlg,
       "tIPsecRUTnlStatsIsakmpPfsDhGrp": tIPsecRUTnlStatsIsakmpPfsDhGrp,
       "tIPsecRUTnlStatsIkeTranPrfAlg": tIPsecRUTnlStatsIkeTranPrfAlg,
       "tIPsecRUSATable": tIPsecRUSATable,
       "tIPsecRUSAEntry": tIPsecRUSAEntry,
       "tIPsecRUSAId": tIPsecRUSAId,
       "tIPsecRUSAIndex": tIPsecRUSAIndex,
       "tIPsecRUSADirection": tIPsecRUSADirection,
       "tIPsecRUSAEncryptionKey": tIPsecRUSAEncryptionKey,
       "tIPsecRUSAAuthenticationKey": tIPsecRUSAAuthenticationKey,
       "tIPsecRUSASpi": tIPsecRUSASpi,
       "tIPsecRUSAAuthAlgorithm": tIPsecRUSAAuthAlgorithm,
       "tIPsecRUSAEncrAlgorithm": tIPsecRUSAEncrAlgorithm,
       "tIPsecRUSAEstablishedTime": tIPsecRUSAEstablishedTime,
       "tIPsecRUSANegotiatedLifeTime": tIPsecRUSANegotiatedLifeTime,
       "tIPsecRUSALclAddrType": tIPsecRUSALclAddrType,
       "tIPsecRUSALclAddr": tIPsecRUSALclAddr,
       "tIPsecRUSALclAPrefLen": tIPsecRUSALclAPrefLen,
       "tIPsecRUSARemAddrType": tIPsecRUSARemAddrType,
       "tIPsecRUSARemAddr": tIPsecRUSARemAddr,
       "tIPsecRUSARemAPrefLen": tIPsecRUSARemAPrefLen,
       "tIPsecRUSAStatsTable": tIPsecRUSAStatsTable,
       "tIPsecRUSAStatsEntry": tIPsecRUSAStatsEntry,
       "tIPsecRUSAStatsBytesProcessed": tIPsecRUSAStatsBytesProcessed,
       "tIPsecRUSAStatsBytesProcLow32": tIPsecRUSAStatsBytesProcLow32,
       "tIPsecRUSAStatsBytesProcHigh32": tIPsecRUSAStatsBytesProcHigh32,
       "tIPsecRUSAStatsPktsProcessed": tIPsecRUSAStatsPktsProcessed,
       "tIPsecRUSAStatsPktsProcLow32": tIPsecRUSAStatsPktsProcLow32,
       "tIPsecRUSAStatsPktsProcHigh32": tIPsecRUSAStatsPktsProcHigh32,
       "tIPsecRUSAStatsCryptoErrors": tIPsecRUSAStatsCryptoErrors,
       "tIPsecRUSAStatsReplayErrors": tIPsecRUSAStatsReplayErrors,
       "tIPsecRUSAStatsSAErrors": tIPsecRUSAStatsSAErrors,
       "tIPsecRUSAStatsPolicyErrors": tIPsecRUSAStatsPolicyErrors,
       "tIPsecRUSAStatsEncapOverhead": tIPsecRUSAStatsEncapOverhead,
       "tIPsecRUSAStatsPreEncapFragCnt": tIPsecRUSAStatsPreEncapFragCnt,
       "tIPsecRUSAStatsPreEncapFragLtSz": tIPsecRUSAStatsPreEncapFragLtSz,
       "tIPsecRUSAStatsPostEncapFragCnt": tIPsecRUSAStatsPostEncapFragCnt,
       "tIPsecRUSAStatsPostEncapFragLtSz": tIPsecRUSAStatsPostEncapFragLtSz,
       "tIPsecRUSAStatsPfsDhGroup": tIPsecRUSAStatsPfsDhGroup,
       "tIPsecRUSAStatsMulticastIfName": tIPsecRUSAStatsMulticastIfName,
       "tIPsecRUSAStatsMulticastProt": tIPsecRUSAStatsMulticastProt,
       "tmnxIPsecTunnelCountObjs": tmnxIPsecTunnelCountObjs,
       "tmnxIPsecPskTunnels": tmnxIPsecPskTunnels,
       "tmnxIPsecGWPskTunnels": tmnxIPsecGWPskTunnels,
       "tmnxIPsecGWPskXAuthTunnels": tmnxIPsecGWPskXAuthTunnels,
       "tmnxIPsecGWCertTunnels": tmnxIPsecGWCertTunnels,
       "tmnxIPsecGWPskRadiusTunnels": tmnxIPsecGWPskRadiusTunnels,
       "tmnxIPsecGWCertRadiusTunnels": tmnxIPsecGWCertRadiusTunnels,
       "tmnxIPsecGWEapTunnels": tmnxIPsecGWEapTunnels,
       "tmnxIPsecGWAutoEapRadiusTunnels": tmnxIPsecGWAutoEapRadiusTunnels,
       "tmnxIPsecGWAutoEapTunnels": tmnxIPsecGWAutoEapTunnels,
       "tmnxIPsecTunnelBfdTableLastChgd": tmnxIPsecTunnelBfdTableLastChgd,
       "tmnxIPsecTunnelBfdTable": tmnxIPsecTunnelBfdTable,
       "tmnxIPsecTunnelBfdEntry": tmnxIPsecTunnelBfdEntry,
       "tmnxIPsecTunnelBfdSvcId": tmnxIPsecTunnelBfdSvcId,
       "tmnxIPsecTunnelBfdIfName": tmnxIPsecTunnelBfdIfName,
       "tmnxIPsecTunnelBfdDstAddrType": tmnxIPsecTunnelBfdDstAddrType,
       "tmnxIPsecTunnelBfdDstAddr": tmnxIPsecTunnelBfdDstAddr,
       "tmnxIPsecTunnelBfdRowStatus": tmnxIPsecTunnelBfdRowStatus,
       "tmnxIPsecTunnelBfdLastChanged": tmnxIPsecTunnelBfdLastChanged,
       "tmnxIPsecTunnelBfdSrcAddrType": tmnxIPsecTunnelBfdSrcAddrType,
       "tmnxIPsecTunnelBfdSrcAddr": tmnxIPsecTunnelBfdSrcAddr,
       "tmnxIPsecTunnelBfdSessOperState": tmnxIPsecTunnelBfdSessOperState,
       "tIPsecRadAuthPlcyTblLastChgd": tIPsecRadAuthPlcyTblLastChgd,
       "tIPsecRadAuthPlcyTable": tIPsecRadAuthPlcyTable,
       "tIPsecRadAuthPlcyEntry": tIPsecRadAuthPlcyEntry,
       "tIPsecRadAuthPlcyName": tIPsecRadAuthPlcyName,
       "tIPsecRadAuthPlcyRowStatus": tIPsecRadAuthPlcyRowStatus,
       "tIPsecRadAuthPlcyLastMgmtChange": tIPsecRadAuthPlcyLastMgmtChange,
       "tIPsecRadAuthPlcyInclAttr": tIPsecRadAuthPlcyInclAttr,
       "tIPsecRadAuthPlcyRadSrvPlcy": tIPsecRadAuthPlcyRadSrvPlcy,
       "tIPsecRadAuthPlcyPassword": tIPsecRadAuthPlcyPassword,
       "tIPsecRadAcctPlcyTblLastChgd": tIPsecRadAcctPlcyTblLastChgd,
       "tIPsecRadAcctPlcyTable": tIPsecRadAcctPlcyTable,
       "tIPsecRadAcctPlcyEntry": tIPsecRadAcctPlcyEntry,
       "tIPsecRadAcctPlcyName": tIPsecRadAcctPlcyName,
       "tIPsecRadAcctPlcyRowStatus": tIPsecRadAcctPlcyRowStatus,
       "tIPsecRadAcctPlcyLastMgmtChange": tIPsecRadAcctPlcyLastMgmtChange,
       "tIPsecRadAcctPlcyInclAttr": tIPsecRadAcctPlcyInclAttr,
       "tIPsecRadAcctPlcyRadSrvPlcy": tIPsecRadAcctPlcyRadSrvPlcy,
       "tIPsecRadAcctPlcyUpdateInterval": tIPsecRadAcctPlcyUpdateInterval,
       "tIPsecRadAcctPlcyJitter": tIPsecRadAcctPlcyJitter,
       "tmnxIPsecTnlDstAddrTblLastChngd": tmnxIPsecTnlDstAddrTblLastChngd,
       "tmnxIPsecTnlDstAddrTable": tmnxIPsecTnlDstAddrTable,
       "tmnxIPsecTnlDstAddrEntry": tmnxIPsecTnlDstAddrEntry,
       "tmnxIPsecTnlDstAddrType": tmnxIPsecTnlDstAddrType,
       "tmnxIPsecTnlDstAddr": tmnxIPsecTnlDstAddr,
       "tmnxIPsecTnlDstAddrRowStatus": tmnxIPsecTnlDstAddrRowStatus,
       "tmnxIPsecTnlDstAddrLastChanged": tmnxIPsecTnlDstAddrLastChanged,
       "tmnxIPsecTnlDstAddrResolved": tmnxIPsecTnlDstAddrResolved,
       "tIPsecCertProfileTblLastChgd": tIPsecCertProfileTblLastChgd,
       "tIPsecCertProfileTable": tIPsecCertProfileTable,
       "tIPsecCertProfileEntry": tIPsecCertProfileEntry,
       "tIPsecCertProfileName": tIPsecCertProfileName,
       "tIPsecCertProfileRowStatus": tIPsecCertProfileRowStatus,
       "tIPsecCertProfileLastChgd": tIPsecCertProfileLastChgd,
       "tIPsecCertProfileAdminState": tIPsecCertProfileAdminState,
       "tIPsecCertProfileOperState": tIPsecCertProfileOperState,
       "tIPsecCertProfileOperFlags": tIPsecCertProfileOperFlags,
       "tIPsecCertProfEntryIdTblLastChgd": tIPsecCertProfEntryIdTblLastChgd,
       "tIPsecCertProfEntryIdTable": tIPsecCertProfEntryIdTable,
       "tIPsecCertProfEntryIdEntry": tIPsecCertProfEntryIdEntry,
       "tIPsecCertProfEntryId": tIPsecCertProfEntryId,
       "tIPsecCertProfEntryIdRowStatus": tIPsecCertProfEntryIdRowStatus,
       "tIPsecCertProfEntryIdLastChgd": tIPsecCertProfEntryIdLastChgd,
       "tIPsecCertProfEntryIdCertFile": tIPsecCertProfEntryIdCertFile,
       "tIPsecCertProfEntryIdKeyFile": tIPsecCertProfEntryIdKeyFile,
       "tIPsecCertProfEntryIdCompChain": tIPsecCertProfEntryIdCompChain,
       "tIPsecCertProfEntryIdOperFlags": tIPsecCertProfEntryIdOperFlags,
       "tIPsecCertProfEntryIdRsaSign": tIPsecCertProfEntryIdRsaSign,
       "tIPsecCompChainCAProfTable": tIPsecCompChainCAProfTable,
       "tIPsecCompChainCAProfEntry": tIPsecCompChainCAProfEntry,
       "tIPsecCompChainCAProfOrder": tIPsecCompChainCAProfOrder,
       "tIPsecCompChainCAProfName": tIPsecCompChainCAProfName,
       "tIPsecCertChainCAProfTblLastChgd": tIPsecCertChainCAProfTblLastChgd,
       "tIPsecCertChainCAProfTable": tIPsecCertChainCAProfTable,
       "tIPsecCertChainCAProfEntry": tIPsecCertChainCAProfEntry,
       "tIPsecCertChainCAProfName": tIPsecCertChainCAProfName,
       "tIPsecCertChainCAProfRowStatus": tIPsecCertChainCAProfRowStatus,
       "tIPsecCertChainCAProfLastChgd": tIPsecCertChainCAProfLastChgd,
       "tIPsecTsListTblLastChgd": tIPsecTsListTblLastChgd,
       "tIPsecTsListTable": tIPsecTsListTable,
       "tIPsecTsListEntry": tIPsecTsListEntry,
       "tIPsecTsListName": tIPsecTsListName,
       "tIPsecTsListRowStatus": tIPsecTsListRowStatus,
       "tIPsecTsListLastChgd": tIPsecTsListLastChgd,
       "tIPsecTsListLclEntryTblLastChgd": tIPsecTsListLclEntryTblLastChgd,
       "tIPsecTsListLclEntryTable": tIPsecTsListLclEntryTable,
       "tIPsecTsListLclEntryEntry": tIPsecTsListLclEntryEntry,
       "tIPsecTsListLclEntryId": tIPsecTsListLclEntryId,
       "tIPsecTsListLclEntryRowStatus": tIPsecTsListLclEntryRowStatus,
       "tIPsecTsListLclEntryLastChgd": tIPsecTsListLclEntryLastChgd,
       "tIPsecTsListLclEntryFrAddrType": tIPsecTsListLclEntryFrAddrType,
       "tIPsecTsListLclEntryFrAddr": tIPsecTsListLclEntryFrAddr,
       "tIPsecTsListLclEntryToAddrType": tIPsecTsListLclEntryToAddrType,
       "tIPsecTsListLclEntryToAddr": tIPsecTsListLclEntryToAddr,
       "tIPsecTsListLclEntryPfxAddrType": tIPsecTsListLclEntryPfxAddrType,
       "tIPsecTsListLclEntryPfxAddr": tIPsecTsListLclEntryPfxAddr,
       "tIPsecTsListLclEntryPfxLen": tIPsecTsListLclEntryPfxLen,
       "tIPsecTsListLclEntryMinPort": tIPsecTsListLclEntryMinPort,
       "tIPsecTsListLclEntryMaxPort": tIPsecTsListLclEntryMaxPort,
       "tIPsecTsListLclEntryMinMhType": tIPsecTsListLclEntryMinMhType,
       "tIPsecTsListLclEntryMaxMhType": tIPsecTsListLclEntryMaxMhType,
       "tIPsecTsListLclEntryMinIcmpType": tIPsecTsListLclEntryMinIcmpType,
       "tIPsecTsListLclEntryMaxIcmpType": tIPsecTsListLclEntryMaxIcmpType,
       "tIPsecTsListLclEntryMinIcmpCode": tIPsecTsListLclEntryMinIcmpCode,
       "tIPsecTsListLclEntryMaxIcmpCode": tIPsecTsListLclEntryMaxIcmpCode,
       "tIPsecTsListLclEntryProtocolId": tIPsecTsListLclEntryProtocolId,
       "tIPsecGWTsNegSelPlcyTblLastChgd": tIPsecGWTsNegSelPlcyTblLastChgd,
       "tIPsecGWTsNegSelPlcyTable": tIPsecGWTsNegSelPlcyTable,
       "tIPsecGWTsNegSelPlcyEntry": tIPsecGWTsNegSelPlcyEntry,
       "tIPsecGWTsNegSelPlcyName": tIPsecGWTsNegSelPlcyName,
       "tIPsecGWTsNegSelPlcyRowStatus": tIPsecGWTsNegSelPlcyRowStatus,
       "tIPsecGWTsNegSelPlcyLastChgd": tIPsecGWTsNegSelPlcyLastChgd,
       "tIPsecGWTsNegSelPlcyTsList": tIPsecGWTsNegSelPlcyTsList,
       "tIPsecTrustAnchorProfTblLastChgd": tIPsecTrustAnchorProfTblLastChgd,
       "tIPsecTrustAnchorProfTable": tIPsecTrustAnchorProfTable,
       "tIPsecTrustAnchorProfEntry": tIPsecTrustAnchorProfEntry,
       "tIPsecTrustAnchorProfName": tIPsecTrustAnchorProfName,
       "tIPsecTrustAnchorProfRowStatus": tIPsecTrustAnchorProfRowStatus,
       "tIPsecTrustAnchorProfLastChgd": tIPsecTrustAnchorProfLastChgd,
       "tIPsecTrustAnchorCAProfDown": tIPsecTrustAnchorCAProfDown,
       "tIPsecTrustAnchorsTblLastChgd": tIPsecTrustAnchorsTblLastChgd,
       "tIPsecTrustAnchorsTable": tIPsecTrustAnchorsTable,
       "tIPsecTrustAnchorsEntry": tIPsecTrustAnchorsEntry,
       "tIPsecTrustAnchorsCAProfile": tIPsecTrustAnchorsCAProfile,
       "tIPsecTrustAnchorsRowStatus": tIPsecTrustAnchorsRowStatus,
       "tIPsecTrustAnchorsLastChgd": tIPsecTrustAnchorsLastChgd,
       "tIPsecRUSATrafficSelTable": tIPsecRUSATrafficSelTable,
       "tIPsecRUSATrafficSelEntry": tIPsecRUSATrafficSelEntry,
       "tIPsecRUSATrafficSelSide": tIPsecRUSATrafficSelSide,
       "tIPsecRUSATrafficSelFrAddrType": tIPsecRUSATrafficSelFrAddrType,
       "tIPsecRUSATrafficSelFrAddr": tIPsecRUSATrafficSelFrAddr,
       "tIPsecRUSATrafficSelToAddrType": tIPsecRUSATrafficSelToAddrType,
       "tIPsecRUSATrafficSelToAddr": tIPsecRUSATrafficSelToAddr,
       "tIPsecRUSATrafficSelLastChgd": tIPsecRUSATrafficSelLastChgd,
       "tIPsecRUSATrafficSelMinPort": tIPsecRUSATrafficSelMinPort,
       "tIPsecRUSATrafficSelMaxPort": tIPsecRUSATrafficSelMaxPort,
       "tIPsecRUSATrafficSelProtocolId": tIPsecRUSATrafficSelProtocolId,
       "tmnxIPsecGWDhcpTblLastChgd": tmnxIPsecGWDhcpTblLastChgd,
       "tmnxIPsecGWDhcpTable": tmnxIPsecGWDhcpTable,
       "tmnxIPsecGWDhcpEntry": tmnxIPsecGWDhcpEntry,
       "tmnxIPsecGWDhcpRowStatus": tmnxIPsecGWDhcpRowStatus,
       "tmnxIPsecGWDhcpLastChgd": tmnxIPsecGWDhcpLastChgd,
       "tmnxIPsecGWDhcpAdminState": tmnxIPsecGWDhcpAdminState,
       "tmnxIPsecGWDhcpGiAddrType": tmnxIPsecGWDhcpGiAddrType,
       "tmnxIPsecGWDhcpGiAddr": tmnxIPsecGWDhcpGiAddr,
       "tmnxIPsecGWDhcpSendRelease": tmnxIPsecGWDhcpSendRelease,
       "tmnxIPsecGWDhcpServiceId": tmnxIPsecGWDhcpServiceId,
       "tmnxIPsecGWDhcpRouterId": tmnxIPsecGWDhcpRouterId,
       "tmnxIPsecGWDhcpSrvr1AddrType": tmnxIPsecGWDhcpSrvr1AddrType,
       "tmnxIPsecGWDhcpSrvr1Addr": tmnxIPsecGWDhcpSrvr1Addr,
       "tmnxIPsecGWDhcpSrvr2AddrType": tmnxIPsecGWDhcpSrvr2AddrType,
       "tmnxIPsecGWDhcpSrvr2Addr": tmnxIPsecGWDhcpSrvr2Addr,
       "tmnxIPsecGWDhcpSrvr3AddrType": tmnxIPsecGWDhcpSrvr3AddrType,
       "tmnxIPsecGWDhcpSrvr3Addr": tmnxIPsecGWDhcpSrvr3Addr,
       "tmnxIPsecGWDhcpSrvr4AddrType": tmnxIPsecGWDhcpSrvr4AddrType,
       "tmnxIPsecGWDhcpSrvr4Addr": tmnxIPsecGWDhcpSrvr4Addr,
       "tmnxIPsecGWDhcpSrvr5AddrType": tmnxIPsecGWDhcpSrvr5AddrType,
       "tmnxIPsecGWDhcpSrvr5Addr": tmnxIPsecGWDhcpSrvr5Addr,
       "tmnxIPsecGWDhcpSrvr6AddrType": tmnxIPsecGWDhcpSrvr6AddrType,
       "tmnxIPsecGWDhcpSrvr6Addr": tmnxIPsecGWDhcpSrvr6Addr,
       "tmnxIPsecGWDhcpSrvr7AddrType": tmnxIPsecGWDhcpSrvr7AddrType,
       "tmnxIPsecGWDhcpSrvr7Addr": tmnxIPsecGWDhcpSrvr7Addr,
       "tmnxIPsecGWDhcpSrvr8AddrType": tmnxIPsecGWDhcpSrvr8AddrType,
       "tmnxIPsecGWDhcpSrvr8Addr": tmnxIPsecGWDhcpSrvr8Addr,
       "tmnxIPsecGWDhcpServiceName": tmnxIPsecGWDhcpServiceName,
       "tIPsecGWLclAddrAssignTblLastChgd": tIPsecGWLclAddrAssignTblLastChgd,
       "tIPsecGWLclAddrAssignTable": tIPsecGWLclAddrAssignTable,
       "tIPsecGWLclAddrAssignEntry": tIPsecGWLclAddrAssignEntry,
       "tIPsecGWLclAddrAssignRowStatus": tIPsecGWLclAddrAssignRowStatus,
       "tIPsecGWLclAddrAssignLastChgd": tIPsecGWLclAddrAssignLastChgd,
       "tIPsecGWLclAddrAssignAdminState": tIPsecGWLclAddrAssignAdminState,
       "tIPsecGWLclAddrAssignIp4SrvrName": tIPsecGWLclAddrAssignIp4SrvrName,
       "tIPsecGWLclAddrAssignIp4SrvrSvc": tIPsecGWLclAddrAssignIp4SrvrSvc,
       "tIPsecGWLclAddrAssignIp4SrvrRtr": tIPsecGWLclAddrAssignIp4SrvrRtr,
       "tIPsecGWLclAddrAssignIp4PoolName": tIPsecGWLclAddrAssignIp4PoolName,
       "tIPsecGWLclAddrAssignIp6SrvrName": tIPsecGWLclAddrAssignIp6SrvrName,
       "tIPsecGWLclAddrAssignIp6SrvrSvc": tIPsecGWLclAddrAssignIp6SrvrSvc,
       "tIPsecGWLclAddrAssignIp6SrvrRtr": tIPsecGWLclAddrAssignIp6SrvrRtr,
       "tIPsecGWLclAddrAssignIp6PoolName": tIPsecGWLclAddrAssignIp6PoolName,
       "tIPsecGWLclAddrAssignIp4PoolNam2": tIPsecGWLclAddrAssignIp4PoolNam2,
       "tIPsecGWLclAddrAssignIp4SrvrSvcN": tIPsecGWLclAddrAssignIp4SrvrSvcN,
       "tIPsecGWLclAddrAssignIp6SrvrSvcN": tIPsecGWLclAddrAssignIp6SrvrSvcN,
       "tmnxIPsecGWDhcpV6TblLastChgd": tmnxIPsecGWDhcpV6TblLastChgd,
       "tmnxIPsecGWDhcpV6Table": tmnxIPsecGWDhcpV6Table,
       "tmnxIPsecGWDhcpV6Entry": tmnxIPsecGWDhcpV6Entry,
       "tmnxIPsecGWDhcpV6RowStatus": tmnxIPsecGWDhcpV6RowStatus,
       "tmnxIPsecGWDhcpV6LastChgd": tmnxIPsecGWDhcpV6LastChgd,
       "tmnxIPsecGWDhcpV6AdminState": tmnxIPsecGWDhcpV6AdminState,
       "tmnxIPsecGWDhcpV6LinkAddrType": tmnxIPsecGWDhcpV6LinkAddrType,
       "tmnxIPsecGWDhcpV6LinkAddr": tmnxIPsecGWDhcpV6LinkAddr,
       "tmnxIPsecGWDhcpV6SendRelease": tmnxIPsecGWDhcpV6SendRelease,
       "tmnxIPsecGWDhcpV6ServiceId": tmnxIPsecGWDhcpV6ServiceId,
       "tmnxIPsecGWDhcpV6RouterId": tmnxIPsecGWDhcpV6RouterId,
       "tmnxIPsecGWDhcpV6Srvr1AddrType": tmnxIPsecGWDhcpV6Srvr1AddrType,
       "tmnxIPsecGWDhcpV6Srvr1Addr": tmnxIPsecGWDhcpV6Srvr1Addr,
       "tmnxIPsecGWDhcpV6Srvr2AddrType": tmnxIPsecGWDhcpV6Srvr2AddrType,
       "tmnxIPsecGWDhcpV6Srvr2Addr": tmnxIPsecGWDhcpV6Srvr2Addr,
       "tmnxIPsecGWDhcpV6Srvr3AddrType": tmnxIPsecGWDhcpV6Srvr3AddrType,
       "tmnxIPsecGWDhcpV6Srvr3Addr": tmnxIPsecGWDhcpV6Srvr3Addr,
       "tmnxIPsecGWDhcpV6Srvr4AddrType": tmnxIPsecGWDhcpV6Srvr4AddrType,
       "tmnxIPsecGWDhcpV6Srvr4Addr": tmnxIPsecGWDhcpV6Srvr4Addr,
       "tmnxIPsecGWDhcpV6Srvr5AddrType": tmnxIPsecGWDhcpV6Srvr5AddrType,
       "tmnxIPsecGWDhcpV6Srvr5Addr": tmnxIPsecGWDhcpV6Srvr5Addr,
       "tmnxIPsecGWDhcpV6Srvr6AddrType": tmnxIPsecGWDhcpV6Srvr6AddrType,
       "tmnxIPsecGWDhcpV6Srvr6Addr": tmnxIPsecGWDhcpV6Srvr6Addr,
       "tmnxIPsecGWDhcpV6Srvr7AddrType": tmnxIPsecGWDhcpV6Srvr7AddrType,
       "tmnxIPsecGWDhcpV6Srvr7Addr": tmnxIPsecGWDhcpV6Srvr7Addr,
       "tmnxIPsecGWDhcpV6Srvr8AddrType": tmnxIPsecGWDhcpV6Srvr8AddrType,
       "tmnxIPsecGWDhcpV6Srvr8Addr": tmnxIPsecGWDhcpV6Srvr8Addr,
       "tmnxIPsecGWDhcpV6ServiceName": tmnxIPsecGWDhcpV6ServiceName,
       "tIPsecTsListRmtEntryTblLastChgd": tIPsecTsListRmtEntryTblLastChgd,
       "tIPsecTsListRmtEntryTable": tIPsecTsListRmtEntryTable,
       "tIPsecTsListRmtEntryEntry": tIPsecTsListRmtEntryEntry,
       "tIPsecTsListRmtEntryId": tIPsecTsListRmtEntryId,
       "tIPsecTsListRmtEntryRowStatus": tIPsecTsListRmtEntryRowStatus,
       "tIPsecTsListRmtEntryLastChgd": tIPsecTsListRmtEntryLastChgd,
       "tIPsecTsListRmtEntryMinAddrType": tIPsecTsListRmtEntryMinAddrType,
       "tIPsecTsListRmtEntryMinAddr": tIPsecTsListRmtEntryMinAddr,
       "tIPsecTsListRmtEntryMaxAddrType": tIPsecTsListRmtEntryMaxAddrType,
       "tIPsecTsListRmtEntryMaxAddr": tIPsecTsListRmtEntryMaxAddr,
       "tIPsecTsListRmtEntryPfxAddrType": tIPsecTsListRmtEntryPfxAddrType,
       "tIPsecTsListRmtEntryPfxAddr": tIPsecTsListRmtEntryPfxAddr,
       "tIPsecTsListRmtEntryPfxLen": tIPsecTsListRmtEntryPfxLen,
       "tIPsecTsListRmtEntryMinPort": tIPsecTsListRmtEntryMinPort,
       "tIPsecTsListRmtEntryMaxPort": tIPsecTsListRmtEntryMaxPort,
       "tIPsecTsListRmtEntryMinMhType": tIPsecTsListRmtEntryMinMhType,
       "tIPsecTsListRmtEntryMaxMhType": tIPsecTsListRmtEntryMaxMhType,
       "tIPsecTsListRmtEntryMinIcmpType": tIPsecTsListRmtEntryMinIcmpType,
       "tIPsecTsListRmtEntryMaxIcmpType": tIPsecTsListRmtEntryMaxIcmpType,
       "tIPsecTsListRmtEntryMinIcmpCode": tIPsecTsListRmtEntryMinIcmpCode,
       "tIPsecTsListRmtEntryMaxIcmpCode": tIPsecTsListRmtEntryMaxIcmpCode,
       "tIPsecTsListRmtEntryProtocolId": tIPsecTsListRmtEntryProtocolId,
       "tmnxIPsecLockoutClientTable": tmnxIPsecLockoutClientTable,
       "tmnxIPsecLockoutClientEntry": tmnxIPsecLockoutClientEntry,
       "tmnxIPsecLockoutClientRtrId": tmnxIPsecLockoutClientRtrId,
       "tmnxIPsecLockoutClientLclGwAddrT": tmnxIPsecLockoutClientLclGwAddrT,
       "tmnxIPsecLockoutClientLclGwAddr": tmnxIPsecLockoutClientLclGwAddr,
       "tmnxIPsecLockoutClientAddressTyp": tmnxIPsecLockoutClientAddressTyp,
       "tmnxIPsecLockoutClientAddress": tmnxIPsecLockoutClientAddress,
       "tmnxIPsecLockoutClientPort": tmnxIPsecLockoutClientPort,
       "tmnxIPsecLockoutClientStatus": tmnxIPsecLockoutClientStatus,
       "tmnxIPsecLockoutClientFailAtempt": tmnxIPsecLockoutClientFailAtempt,
       "tmnxIPsecLockoutClientDroppedPkt": tmnxIPsecLockoutClientDroppedPkt,
       "tmnxIPsecLockoutClientRemainTime": tmnxIPsecLockoutClientRemainTime,
       "tIPsecRUTnlDhcpLeaseStatTable": tIPsecRUTnlDhcpLeaseStatTable,
       "tIPsecRUTnlDhcpLeaseStatEntry": tIPsecRUTnlDhcpLeaseStatEntry,
       "tIPsecRUTnlDhcpLeaseStatPrivAddT": tIPsecRUTnlDhcpLeaseStatPrivAddT,
       "tIPsecRUTnlDhcpLeaseStatPrivAddr": tIPsecRUTnlDhcpLeaseStatPrivAddr,
       "tIPsecRUTnlDhcpLeaseStatSverAddT": tIPsecRUTnlDhcpLeaseStatSverAddT,
       "tIPsecRUTnlDhcpLeaseStatSverAddr": tIPsecRUTnlDhcpLeaseStatSverAddr,
       "tIPsecRUTnlDhcpLeaseStatAcquirTm": tIPsecRUTnlDhcpLeaseStatAcquirTm,
       "tIPsecRUTnlDhcpLeaseStatRenewTm": tIPsecRUTnlDhcpLeaseStatRenewTm,
       "tIPsecRUTnlDhcpLeaseStatRebindTm": tIPsecRUTnlDhcpLeaseStatRebindTm,
       "tIPsecRUTnlDhcpLeaseStatPrivPref": tIPsecRUTnlDhcpLeaseStatPrivPref,
       "tIPsecRUTnlDhcpLeaseStatPrivVald": tIPsecRUTnlDhcpLeaseStatPrivVald,
       "tIPsecClientDatabaseTableLstChgd": tIPsecClientDatabaseTableLstChgd,
       "tIPsecClientDatabaseTable": tIPsecClientDatabaseTable,
       "tIPsecClientDatabaseEntry": tIPsecClientDatabaseEntry,
       "tIPsecClientDatabaseName": tIPsecClientDatabaseName,
       "tIPsecClientDatabaseLastChanged": tIPsecClientDatabaseLastChanged,
       "tIPsecClientDatabaseRowStatus": tIPsecClientDatabaseRowStatus,
       "tIPsecClientDatabaseAdminState": tIPsecClientDatabaseAdminState,
       "tIPsecClientDatabaseDescription": tIPsecClientDatabaseDescription,
       "tIPsecClientDatabaseMatchType": tIPsecClientDatabaseMatchType,
       "tIPsecClientDBClientTableLstChgd": tIPsecClientDBClientTableLstChgd,
       "tIPsecClientDBClientTable": tIPsecClientDBClientTable,
       "tIPsecClientDBClientEntry": tIPsecClientDBClientEntry,
       "tIPsecClientDBClientIndex": tIPsecClientDBClientIndex,
       "tIPsecClientDBClientLastChanged": tIPsecClientDBClientLastChanged,
       "tIPsecClientDBClientRowStatus": tIPsecClientDBClientRowStatus,
       "tIPsecClientDBClientAdminState": tIPsecClientDBClientAdminState,
       "tIPsecClientDBClientName": tIPsecClientDBClientName,
       "tIPsecClientDBClientIdIdiType": tIPsecClientDBClientIdIdiType,
       "tIPsecClientDBClientIdIdiValue": tIPsecClientDBClientIdIdiValue,
       "tIPsecClientDBClientIdPeer4PfAny": tIPsecClientDBClientIdPeer4PfAny,
       "tIPsecClientDBClientIdPeer6PfAny": tIPsecClientDBClientIdPeer6PfAny,
       "tIPsecClientDBClientIdPeerPfxTyp": tIPsecClientDBClientIdPeerPfxTyp,
       "tIPsecClientDBClientIdPeerPfx": tIPsecClientDBClientIdPeerPfx,
       "tIPsecClientDBClientIdPeerPfxLen": tIPsecClientDBClientIdPeerPfxLen,
       "tIPsecClientDBClientTnlTempltId": tIPsecClientDBClientTnlTempltId,
       "tIPsecClientDBClientPrivateSvcId": tIPsecClientDBClientPrivateSvcId,
       "tIPsecClientDBClientPrivIfName": tIPsecClientDBClientPrivIfName,
       "tIPsecClientDBClientTsListName": tIPsecClientDBClientTsListName,
       "tIPsecClientDBClientPreSharedKey": tIPsecClientDBClientPreSharedKey,
       "tIPsecClientDBClientPrivateSvcNm": tIPsecClientDBClientPrivateSvcNm,
       "tmnxIPsecIkeTransformTableLstChg": tmnxIPsecIkeTransformTableLstChg,
       "tmnxIPsecIkeTransformTable": tmnxIPsecIkeTransformTable,
       "tmnxIPsecIkeTransformEntry": tmnxIPsecIkeTransformEntry,
       "tmnxIPsecIkeTransformId": tmnxIPsecIkeTransformId,
       "tmnxIPsecIkeTransformRowStatus": tmnxIPsecIkeTransformRowStatus,
       "tmnxIPsecIkeTransformLastChange": tmnxIPsecIkeTransformLastChange,
       "tmnxIPsecIkeTransformAuthAlg": tmnxIPsecIkeTransformAuthAlg,
       "tmnxIPsecIkeTransformEncrAlg": tmnxIPsecIkeTransformEncrAlg,
       "tmnxIPsecIkeTransformDhGroup": tmnxIPsecIkeTransformDhGroup,
       "tmnxIPsecIkeTransformIsakmpLifeT": tmnxIPsecIkeTransformIsakmpLifeT,
       "tmnxIPsecIkeTransformPrfAlg": tmnxIPsecIkeTransformPrfAlg,
       "tmnxIkePlcyIkeTransformTbLstChg": tmnxIkePlcyIkeTransformTbLstChg,
       "tmnxIkePlcyIkeTransformTable": tmnxIkePlcyIkeTransformTable,
       "tmnxIkePlcyIkeTransformEntry": tmnxIkePlcyIkeTransformEntry,
       "tmnxIkePlcyIkeTransformIndex": tmnxIkePlcyIkeTransformIndex,
       "tmnxIkePlcyIkeTransformLstChange": tmnxIkePlcyIkeTransformLstChange,
       "tmnxIkePlcyIkeTransformId": tmnxIkePlcyIkeTransformId,
       "tmnxIPsecGWHistStatsTable": tmnxIPsecGWHistStatsTable,
       "tmnxIPsecGWHistStatsEntry": tmnxIPsecGWHistStatsEntry,
       "tmnxIPsecGWHistStatsType": tmnxIPsecGWHistStatsType,
       "tmnxIPsecGWHistStatsIntvIdx": tmnxIPsecGWHistStatsIntvIdx,
       "tmnxIPsecGWHistStatsValue64": tmnxIPsecGWHistStatsValue64,
       "tmnxIPsecGWHistStatsValue32": tmnxIPsecGWHistStatsValue32,
       "tmnxIPsecGWHistStatsIntvStTm": tmnxIPsecGWHistStatsIntvStTm,
       "tmnxIPsecGWHistStatsIntvDur": tmnxIPsecGWHistStatsIntvDur,
       "tmnxIPsecGWHistStatsFstFTm": tmnxIPsecGWHistStatsFstFTm,
       "tmnxIPsecGWHistStatsFstFDesc": tmnxIPsecGWHistStatsFstFDesc,
       "tmnxIPsecGWHistStatsLstFTm": tmnxIPsecGWHistStatsLstFTm,
       "tmnxIPsecGWHistStatsLstFDesc": tmnxIPsecGWHistStatsLstFDesc,
       "tmnxIPsecIsaHistStatsTable": tmnxIPsecIsaHistStatsTable,
       "tmnxIPsecIsaHistStatsEntry": tmnxIPsecIsaHistStatsEntry,
       "tmnxIPsecIsaHistStatsType": tmnxIPsecIsaHistStatsType,
       "tmnxIPsecIsaHistStatsIntvIdx": tmnxIPsecIsaHistStatsIntvIdx,
       "tmnxIPsecIsaHistStatsValue64": tmnxIPsecIsaHistStatsValue64,
       "tmnxIPsecIsaHistStatsValue32": tmnxIPsecIsaHistStatsValue32,
       "tmnxIPsecIsaHistStatsIntvStTm": tmnxIPsecIsaHistStatsIntvStTm,
       "tmnxIPsecIsaHistStatsIntvDur": tmnxIPsecIsaHistStatsIntvDur,
       "tmnxIPsecIsaHistStatsFstFTm": tmnxIPsecIsaHistStatsFstFTm,
       "tmnxIPsecIsaHistStatsFstFDesc": tmnxIPsecIsaHistStatsFstFDesc,
       "tmnxIPsecIsaHistStatsLstFTm": tmnxIPsecIsaHistStatsLstFTm,
       "tmnxIPsecIsaHistStatsLstFDesc": tmnxIPsecIsaHistStatsLstFDesc,
       "tmnxIPsecSvcLevelCfgTableLastChg": tmnxIPsecSvcLevelCfgTableLastChg,
       "tmnxIPsecSvcLevelCfgTable": tmnxIPsecSvcLevelCfgTable,
       "tmnxIPsecSvcLevelCfgEntry": tmnxIPsecSvcLevelCfgEntry,
       "tmnxIPsecSvcLevelCfgRsvRtrOvrd": tmnxIPsecSvcLevelCfgRsvRtrOvrd,
       "tmnxIPsecSvcLevelCfgRROvrdType": tmnxIPsecSvcLevelCfgRROvrdType,
       "tmnxIPsecTnlGrpHistStatsTable": tmnxIPsecTnlGrpHistStatsTable,
       "tmnxIPsecTnlGrpHistStatsEntry": tmnxIPsecTnlGrpHistStatsEntry,
       "tmnxIPsecTnlGrpHistStatsType": tmnxIPsecTnlGrpHistStatsType,
       "tmnxIPsecTnlGrpHistStatsIntvIdx": tmnxIPsecTnlGrpHistStatsIntvIdx,
       "tmnxIPsecTnlGrpHistStatsValue64": tmnxIPsecTnlGrpHistStatsValue64,
       "tmnxIPsecTnlGrpHistStatsValue32": tmnxIPsecTnlGrpHistStatsValue32,
       "tmnxIPsecTnlGrpHistStatsIntvStTm": tmnxIPsecTnlGrpHistStatsIntvStTm,
       "tmnxIPsecTnlGrpHistStatsIntvDur": tmnxIPsecTnlGrpHistStatsIntvDur,
       "tmnxIPsecTnlGrpHistStatsFstFTm": tmnxIPsecTnlGrpHistStatsFstFTm,
       "tmnxIPsecTnlGrpHistStatsFstFDesc": tmnxIPsecTnlGrpHistStatsFstFDesc,
       "tmnxIPsecTnlGrpHistStatsLstFTm": tmnxIPsecTnlGrpHistStatsLstFTm,
       "tmnxIPsecTnlGrpHistStatsLstFDesc": tmnxIPsecTnlGrpHistStatsLstFDesc,
       "tmnxIPsecSysHistStatsTable": tmnxIPsecSysHistStatsTable,
       "tmnxIPsecSysHistStatsEntry": tmnxIPsecSysHistStatsEntry,
       "tmnxIPsecSysHistStatsType": tmnxIPsecSysHistStatsType,
       "tmnxIPsecSysHistStatsIntvIdx": tmnxIPsecSysHistStatsIntvIdx,
       "tmnxIPsecSysHistStatsValue64": tmnxIPsecSysHistStatsValue64,
       "tmnxIPsecSysHistStatsValue32": tmnxIPsecSysHistStatsValue32,
       "tmnxIPsecSysHistStatsIntvStTm": tmnxIPsecSysHistStatsIntvStTm,
       "tmnxIPsecSysHistStatsIntvDur": tmnxIPsecSysHistStatsIntvDur,
       "tmnxIPsecSysHistStatsFstFTm": tmnxIPsecSysHistStatsFstFTm,
       "tmnxIPsecSysHistStatsFstFDesc": tmnxIPsecSysHistStatsFstFDesc,
       "tmnxIPsecSysHistStatsLstFTm": tmnxIPsecSysHistStatsLstFTm,
       "tmnxIPsecSysHistStatsLstFDesc": tmnxIPsecSysHistStatsLstFDesc,
       "tmnxIPsecTnlHistStatsTable": tmnxIPsecTnlHistStatsTable,
       "tmnxIPsecTnlHistStatsEntry": tmnxIPsecTnlHistStatsEntry,
       "tmnxIPsecTnlHistStatsType": tmnxIPsecTnlHistStatsType,
       "tmnxIPsecTnlHistStatsIntvIdx": tmnxIPsecTnlHistStatsIntvIdx,
       "tmnxIPsecTnlHistStatsValue64": tmnxIPsecTnlHistStatsValue64,
       "tmnxIPsecTnlHistStatsIntvStTm": tmnxIPsecTnlHistStatsIntvStTm,
       "tmnxIPsecTnlHistStatsIntvDur": tmnxIPsecTnlHistStatsIntvDur,
       "tmnxIPsecRUTnlHistStatsTable": tmnxIPsecRUTnlHistStatsTable,
       "tmnxIPsecRUTnlHistStatsEntry": tmnxIPsecRUTnlHistStatsEntry,
       "tmnxIPsecRUTnlHistStatsType": tmnxIPsecRUTnlHistStatsType,
       "tmnxIPsecRUTnlHistStatsIntvIdx": tmnxIPsecRUTnlHistStatsIntvIdx,
       "tmnxIPsecRUTnlHistStatsValue64": tmnxIPsecRUTnlHistStatsValue64,
       "tmnxIPsecRUTnlHistStatsIntvStTm": tmnxIPsecRUTnlHistStatsIntvStTm,
       "tmnxIPsecRUTnlHistStatsIntvDur": tmnxIPsecRUTnlHistStatsIntvDur,
       "tmnxIPsecGWStatsTable": tmnxIPsecGWStatsTable,
       "tmnxIPsecGWStatsEntry": tmnxIPsecGWStatsEntry,
       "tmnxIPsecGWStatsNumOfDl2lTnls": tmnxIPsecGWStatsNumOfDl2lTnls,
       "tmnxIPsecGWStatsNumOfRaTnls": tmnxIPsecGWStatsNumOfRaTnls,
       "tmnxIPsecNotifyObjs": tmnxIPsecNotifyObjs,
       "tIPsecNotifRUTnlInetAddrType": tIPsecNotifRUTnlInetAddrType,
       "tIPsecNotifRUTnlInetAddress": tIPsecNotifRUTnlInetAddress,
       "tIPsecNotifRUTnlPort": tIPsecNotifRUTnlPort,
       "tIPsecNotifReason": tIPsecNotifReason,
       "tIPsecNotifBfdIntfSvcId": tIPsecNotifBfdIntfSvcId,
       "tIPsecNotifBfdIntfIfName": tIPsecNotifBfdIntfIfName,
       "tIPsecNotifBfdIntfDestIpType": tIPsecNotifBfdIntfDestIpType,
       "tIPsecNotifBfdIntfDestIp": tIPsecNotifBfdIntfDestIp,
       "tIPsecNotifBfdIntfSessState": tIPsecNotifBfdIntfSessState,
       "tIPsecRadAcctPlcyFailReason": tIPsecRadAcctPlcyFailReason,
       "tIPsecNotifIPsecTunnelName": tIPsecNotifIPsecTunnelName,
       "tIPsecNotifConfigIpMtu": tIPsecNotifConfigIpMtu,
       "tIPsecNotifEncapOverhead": tIPsecNotifEncapOverhead,
       "tIPsecNotifConfigEncapIpMtu": tIPsecNotifConfigEncapIpMtu,
       "tIPsecNotifCertProfileName": tIPsecNotifCertProfileName,
       "tIPsecNotifCertProfEntryId": tIPsecNotifCertProfEntryId,
       "tIPsecNotifCaProfNames": tIPsecNotifCaProfNames,
       "tIPsecNotifTunnelType": tIPsecNotifTunnelType,
       "tIPsecNotifTunnelIdentifier": tIPsecNotifTunnelIdentifier,
       "tmnxIPsecScalarsObjs": tmnxIPsecScalarsObjs,
       "tmnxIPsecScalarObjsShowKeys": tmnxIPsecScalarObjsShowKeys,
       "tmnxIPsecTnlBfdSessTableLChg": tmnxIPsecTnlBfdSessTableLChg,
       "tmnxIPsecTnlBfdSessTable": tmnxIPsecTnlBfdSessTable,
       "tmnxIPsecTnlBfdSessEntry": tmnxIPsecTnlBfdSessEntry,
       "tmnxIPsecTnlBfdSessRowStatus": tmnxIPsecTnlBfdSessRowStatus,
       "tmnxIPsecTnlBfdSessSvcId": tmnxIPsecTnlBfdSessSvcId,
       "tmnxIPsecTnlBfdSessSvcName": tmnxIPsecTnlBfdSessSvcName,
       "tmnxIPsecTnlBfdSessIfName": tmnxIPsecTnlBfdSessIfName,
       "tmnxIPsecTnlBfdSessDstAddrT": tmnxIPsecTnlBfdSessDstAddrT,
       "tmnxIPsecTnlBfdSessDstAddr": tmnxIPsecTnlBfdSessDstAddr,
       "tmnxIPsecTnlBfdSessStatTable": tmnxIPsecTnlBfdSessStatTable,
       "tmnxIPsecTnlBfdSessStatEntry": tmnxIPsecTnlBfdSessStatEntry,
       "tmnxIPsecTnlBfdSessStatSrcAddrT": tmnxIPsecTnlBfdSessStatSrcAddrT,
       "tmnxIPsecTnlBfdSessStatSrcAddr": tmnxIPsecTnlBfdSessStatSrcAddr,
       "tmnxIPsecTnlBfdSessStatOperState": tmnxIPsecTnlBfdSessStatOperState,
       "tmnxVRtIPsecTnlTableLastChanged": tmnxVRtIPsecTnlTableLastChanged,
       "tmnxVRtIPsecTnlTable": tmnxVRtIPsecTnlTable,
       "tmnxVRtIPsecTnlEntry": tmnxVRtIPsecTnlEntry,
       "tmnxVRtIPsecTnlName": tmnxVRtIPsecTnlName,
       "tmnxVRtIPsecTnlRowStatus": tmnxVRtIPsecTnlRowStatus,
       "tmnxVRtIPsecTnlLastChanged": tmnxVRtIPsecTnlLastChanged,
       "tmnxVRtIPsecTnlAdminState": tmnxVRtIPsecTnlAdminState,
       "tmnxVRtIPsecTnlOperState": tmnxVRtIPsecTnlOperState,
       "tmnxVRtIPsecTnlDescription": tmnxVRtIPsecTnlDescription,
       "tmnxVRtIPsecTnlLclGwAddrType": tmnxVRtIPsecTnlLclGwAddrType,
       "tmnxVRtIPsecTnlLclGwAddr": tmnxVRtIPsecTnlLclGwAddr,
       "tmnxVRtIPsecTnlRemGwAddrType": tmnxVRtIPsecTnlRemGwAddrType,
       "tmnxVRtIPsecTnlRemGwAddr": tmnxVRtIPsecTnlRemGwAddr,
       "tmnxVRtIPsecTnlSecurityPolicyId": tmnxVRtIPsecTnlSecurityPolicyId,
       "tmnxVRtIPsecTnlKeyingType": tmnxVRtIPsecTnlKeyingType,
       "tmnxVRtIPsecTnlDynTransformId1": tmnxVRtIPsecTnlDynTransformId1,
       "tmnxVRtIPsecTnlDynTransformId2": tmnxVRtIPsecTnlDynTransformId2,
       "tmnxVRtIPsecTnlDynTransformId3": tmnxVRtIPsecTnlDynTransformId3,
       "tmnxVRtIPsecTnlDynTransformId4": tmnxVRtIPsecTnlDynTransformId4,
       "tmnxVRtIPsecTnlIkePolicyId": tmnxVRtIPsecTnlIkePolicyId,
       "tmnxVRtIPsecTnlIkePreSharedKey": tmnxVRtIPsecTnlIkePreSharedKey,
       "tmnxVRtIPsecTnlOperFlags": tmnxVRtIPsecTnlOperFlags,
       "tmnxVRtIPsecTnlReplayWindow": tmnxVRtIPsecTnlReplayWindow,
       "tmnxVRtIPsecTnlAutoEstablish": tmnxVRtIPsecTnlAutoEstablish,
       "tmnxVRtIPsecTnlBfdDesignate": tmnxVRtIPsecTnlBfdDesignate,
       "tmnxVRtIPsecTnlLocalIdType": tmnxVRtIPsecTnlLocalIdType,
       "tmnxVRtIPsecTnlLocalIdValue": tmnxVRtIPsecTnlLocalIdValue,
       "tmnxVRtIPsecTnlClearDfBit": tmnxVRtIPsecTnlClearDfBit,
       "tmnxVRtIPsecTnlIpMtu": tmnxVRtIPsecTnlIpMtu,
       "tmnxVRtIPsecTnlHostISA": tmnxVRtIPsecTnlHostISA,
       "tmnxVRtIPsecTnlCSVPrimary": tmnxVRtIPsecTnlCSVPrimary,
       "tmnxVRtIPsecTnlCSVSecondary": tmnxVRtIPsecTnlCSVSecondary,
       "tmnxVRtIPsecTnlCSVDefResult": tmnxVRtIPsecTnlCSVDefResult,
       "tmnxVRtIPsecTnlCertProfile": tmnxVRtIPsecTnlCertProfile,
       "tmnxVRtIPsecTnlMatchTrustAnchor": tmnxVRtIPsecTnlMatchTrustAnchor,
       "tmnxVRtIPsecTnlCertTrstAnchrProf": tmnxVRtIPsecTnlCertTrstAnchrProf,
       "tmnxVRtIPsecTnlEncapIpMtu": tmnxVRtIPsecTnlEncapIpMtu,
       "tmnxVRtIPsecTnlPropagateIpv6PMTU": tmnxVRtIPsecTnlPropagateIpv6PMTU,
       "tmnxVRtIPsecTnlIcmp6Pkt2Big": tmnxVRtIPsecTnlIcmp6Pkt2Big,
       "tmnxVRtIPsecTnlIcmp6NumPkt2Big": tmnxVRtIPsecTnlIcmp6NumPkt2Big,
       "tmnxVRtIPsecTnlIcmp6Pkt2BigTime": tmnxVRtIPsecTnlIcmp6Pkt2BigTime,
       "tmnxVRtIPsecTnlOperChanged": tmnxVRtIPsecTnlOperChanged,
       "tmnxVRtIPsecTnlPropagateIpv4PMTU": tmnxVRtIPsecTnlPropagateIpv4PMTU,
       "tmnxVRtIPsecTnlIcmpFragReq": tmnxVRtIPsecTnlIcmpFragReq,
       "tmnxVRtIPsecTnlIcmpFragReqNum": tmnxVRtIPsecTnlIcmpFragReqNum,
       "tmnxVRtIPsecTnlIcmpFragReqTime": tmnxVRtIPsecTnlIcmpFragReqTime,
       "tmnxVRtIPsecTnlPMTUDiscoverAging": tmnxVRtIPsecTnlPMTUDiscoverAging,
       "tmnxVRtIPsecTnlPubTcpMssAdjust": tmnxVRtIPsecTnlPubTcpMssAdjust,
       "tmnxVRtIPsecTnlPrivTcpMssAdjust": tmnxVRtIPsecTnlPrivTcpMssAdjust,
       "tmnxVRtIPsecTnlMaxNumPh1SaKeys": tmnxVRtIPsecTnlMaxNumPh1SaKeys,
       "tmnxVRtIPsecTnlMaxNumPh2SaKeys": tmnxVRtIPsecTnlMaxNumPh2SaKeys,
       "tmnxVRtIPsecTnlSecPlyStrictMatch": tmnxVRtIPsecTnlSecPlyStrictMatch,
       "tmnxVRtIPsecTnlPrivateSvcName": tmnxVRtIPsecTnlPrivateSvcName,
       "tmnxVRtIPsecTnlPrivSap": tmnxVRtIPsecTnlPrivSap,
       "tmnxVRtIPsecTnlLclGwAddrOvrdType": tmnxVRtIPsecTnlLclGwAddrOvrdType,
       "tmnxVRtIPsecTnlLclGwAddrOvrd": tmnxVRtIPsecTnlLclGwAddrOvrd,
       "tmnxVRtIPsecTnlHostEsa": tmnxVRtIPsecTnlHostEsa,
       "tmnxVRtIPsecTnlHostEsaVm": tmnxVRtIPsecTnlHostEsaVm,
       "tmnxVRtIPsecTnlBfdTableLChg": tmnxVRtIPsecTnlBfdTableLChg,
       "tmnxVRtIPsecTnlBfdTable": tmnxVRtIPsecTnlBfdTable,
       "tmnxVRtIPsecTnlBfdEntry": tmnxVRtIPsecTnlBfdEntry,
       "tmnxVRtIPsecTnlBfdRowStatus": tmnxVRtIPsecTnlBfdRowStatus,
       "tmnxVRtIPsecTnlBfdSvcName": tmnxVRtIPsecTnlBfdSvcName,
       "tmnxVRtIPsecTnlBfdIfName": tmnxVRtIPsecTnlBfdIfName,
       "tmnxVRtIPsecTnlBfdDstAddrT": tmnxVRtIPsecTnlBfdDstAddrT,
       "tmnxVRtIPsecTnlBfdDstAddr": tmnxVRtIPsecTnlBfdDstAddr,
       "tmnxVRtIPsecTnlBfdStatTable": tmnxVRtIPsecTnlBfdStatTable,
       "tmnxVRtIPsecTnlBfdStatEntry": tmnxVRtIPsecTnlBfdStatEntry,
       "tmnxVRtIPsecTnlBfdStatSrcAddrT": tmnxVRtIPsecTnlBfdStatSrcAddrT,
       "tmnxVRtIPsecTnlBfdStatSrcAddr": tmnxVRtIPsecTnlBfdStatSrcAddr,
       "tmnxVRtIPsecTnlBfdStatOperState": tmnxVRtIPsecTnlBfdStatOperState,
       "tmnxVRtIPsecSATableLastChanged": tmnxVRtIPsecSATableLastChanged,
       "tmnxVRtIPsecSATable": tmnxVRtIPsecSATable,
       "tmnxVRtIPsecSAEntry": tmnxVRtIPsecSAEntry,
       "tmnxVRtIPsecSAId": tmnxVRtIPsecSAId,
       "tmnxVRtIPsecSADirection": tmnxVRtIPsecSADirection,
       "tmnxVRtIPsecSAIndex": tmnxVRtIPsecSAIndex,
       "tmnxVRtIPsecSARowStatus": tmnxVRtIPsecSARowStatus,
       "tmnxVRtIPsecSALastChanged": tmnxVRtIPsecSALastChanged,
       "tmnxVRtIPsecSAType": tmnxVRtIPsecSAType,
       "tmnxVRtIPsecSAEncryptionKey": tmnxVRtIPsecSAEncryptionKey,
       "tmnxVRtIPsecSAAuthenticationKey": tmnxVRtIPsecSAAuthenticationKey,
       "tmnxVRtIPsecSASpi": tmnxVRtIPsecSASpi,
       "tmnxVRtIPsecSAManualTransformId": tmnxVRtIPsecSAManualTransformId,
       "tmnxVRtIPsecSAAuthAlgorithm": tmnxVRtIPsecSAAuthAlgorithm,
       "tmnxVRtIPsecSAEncrAlgorithm": tmnxVRtIPsecSAEncrAlgorithm,
       "tmnxVRtIPsecSAStorageType": tmnxVRtIPsecSAStorageType,
       "tmnxVRtIPsecSAEstablishedTime": tmnxVRtIPsecSAEstablishedTime,
       "tmnxVRtIPsecSANegotiatedLifeTime": tmnxVRtIPsecSANegotiatedLifeTime,
       "tmnxVRtIPsecSAStTable": tmnxVRtIPsecSAStTable,
       "tmnxVRtIPsecSAStEntry": tmnxVRtIPsecSAStEntry,
       "tmnxVRtIPsecSAStBytesProcessed": tmnxVRtIPsecSAStBytesProcessed,
       "tmnxVRtIPsecSAStBytesProcLow32": tmnxVRtIPsecSAStBytesProcLow32,
       "tmnxVRtIPsecSAStBytesProcHigh32": tmnxVRtIPsecSAStBytesProcHigh32,
       "tmnxVRtIPsecSAStPktsProcessed": tmnxVRtIPsecSAStPktsProcessed,
       "tmnxVRtIPsecSAStPktsProcLow32": tmnxVRtIPsecSAStPktsProcLow32,
       "tmnxVRtIPsecSAStPktsProcHigh32": tmnxVRtIPsecSAStPktsProcHigh32,
       "tmnxVRtIPsecSAStCryptoErrors": tmnxVRtIPsecSAStCryptoErrors,
       "tmnxVRtIPsecSAStReplayErrors": tmnxVRtIPsecSAStReplayErrors,
       "tmnxVRtIPsecSAStSAErrors": tmnxVRtIPsecSAStSAErrors,
       "tmnxVRtIPsecSAStPolicyErrors": tmnxVRtIPsecSAStPolicyErrors,
       "tmnxVRtIPsecSAStEncapOverhead": tmnxVRtIPsecSAStEncapOverhead,
       "tmnxVRtIPsecSAStPreEncapFragCnt": tmnxVRtIPsecSAStPreEncapFragCnt,
       "tmnxVRtIPsecSAStPreEncapFragLtSz": tmnxVRtIPsecSAStPreEncapFragLtSz,
       "tmnxVRtIPsecSAStPstEncapFragCnt": tmnxVRtIPsecSAStPstEncapFragCnt,
       "tmnxVRtIPsecSAStPstEncapFragLtSz": tmnxVRtIPsecSAStPstEncapFragLtSz,
       "tmnxVRtIPsecSAStTempPrivMtu": tmnxVRtIPsecSAStTempPrivMtu,
       "tmnxVRtIPsecSAStPfsDhGroup": tmnxVRtIPsecSAStPfsDhGroup,
       "tmnxVRtIPsecSAStMulticastIfName": tmnxVRtIPsecSAStMulticastIfName,
       "tmnxVRtIPsecSAStMulticastProt": tmnxVRtIPsecSAStMulticastProt,
       "tmnxVRtSecPlcyTableLastChanged": tmnxVRtSecPlcyTableLastChanged,
       "tmnxVRtSecPlcyTable": tmnxVRtSecPlcyTable,
       "tmnxVRtSecPlcyEntry": tmnxVRtSecPlcyEntry,
       "tmnxVRtSecPlcyId": tmnxVRtSecPlcyId,
       "tmnxVRtSecPlcyRowStatus": tmnxVRtSecPlcyRowStatus,
       "tmnxVRtSecPlcyLastChanged": tmnxVRtSecPlcyLastChanged,
       "tmnxVRtSecPlcyParamTblLastChangd": tmnxVRtSecPlcyParamTblLastChangd,
       "tmnxVRtSecPlcyParamTable": tmnxVRtSecPlcyParamTable,
       "tmnxVRtSecPlcyParamEntry": tmnxVRtSecPlcyParamEntry,
       "tmnxVRtSecPlcyParamId": tmnxVRtSecPlcyParamId,
       "tmnxVRtSecPlcyParamRowStatus": tmnxVRtSecPlcyParamRowStatus,
       "tmnxVRtSecPlcyParamLastChanged": tmnxVRtSecPlcyParamLastChanged,
       "tmnxVRtSecPlcyParamLclAddrAny": tmnxVRtSecPlcyParamLclAddrAny,
       "tmnxVRtSecPlcyParamLclAddrType": tmnxVRtSecPlcyParamLclAddrType,
       "tmnxVRtSecPlcyParamLclAddr": tmnxVRtSecPlcyParamLclAddr,
       "tmnxVRtSecPlcyParamLclAPrefLen": tmnxVRtSecPlcyParamLclAPrefLen,
       "tmnxVRtSecPlcyParamRemAddrAny": tmnxVRtSecPlcyParamRemAddrAny,
       "tmnxVRtSecPlcyParamRemAddrType": tmnxVRtSecPlcyParamRemAddrType,
       "tmnxVRtSecPlcyParamRemAddr": tmnxVRtSecPlcyParamRemAddr,
       "tmnxVRtSecPlcyParamRemAPrefLen": tmnxVRtSecPlcyParamRemAPrefLen,
       "tmnxVRtSecPlcyParam6LclAddrAny": tmnxVRtSecPlcyParam6LclAddrAny,
       "tmnxVRtSecPlcyParam6LclAddrType": tmnxVRtSecPlcyParam6LclAddrType,
       "tmnxVRtSecPlcyParam6LclAddr": tmnxVRtSecPlcyParam6LclAddr,
       "tmnxVRtSecPlcyParam6LclAPrefLen": tmnxVRtSecPlcyParam6LclAPrefLen,
       "tmnxVRtSecPlcyParam6RemAddrAny": tmnxVRtSecPlcyParam6RemAddrAny,
       "tmnxVRtSecPlcyParam6RemAddrType": tmnxVRtSecPlcyParam6RemAddrType,
       "tmnxVRtSecPlcyParam6RemAddr": tmnxVRtSecPlcyParam6RemAddr,
       "tmnxVRtSecPlcyParam6RemAPrefLen": tmnxVRtSecPlcyParam6RemAPrefLen,
       "tmnxVRtIfIPsecTblLstCgd": tmnxVRtIfIPsecTblLstCgd,
       "tmnxVRtIfIPsecTable": tmnxVRtIfIPsecTable,
       "tmnxVRtIfIPsecEntry": tmnxVRtIfIPsecEntry,
       "tmnxVRtIfIPsecRowStatus": tmnxVRtIfIPsecRowStatus,
       "tmnxVRtIfIPsecLastChgd": tmnxVRtIfIPsecLastChgd,
       "tmnxVRtIfIPsecAdminState": tmnxVRtIfIPsecAdminState,
       "tmnxVRtIfIPsecIpFilterInExcptId": tmnxVRtIfIPsecIpFilterInExcptId,
       "tmnxVRtIfIPsecIsaTnlGroup": tmnxVRtIfIPsecIsaTnlGroup,
       "tmnxVRtIfIPsecPubSap": tmnxVRtIfIPsecPubSap,
       "tmnxVRtIfIPsecIpv6FilterInExcId": tmnxVRtIfIPsecIpv6FilterInExcId,
       "tmnxVRtIPsecTnlStatsTable": tmnxVRtIPsecTnlStatsTable,
       "tmnxVRtIPsecTnlStatsEntry": tmnxVRtIPsecTnlStatsEntry,
       "tmnxVRtIPsecTnlIsakmpState": tmnxVRtIPsecTnlIsakmpState,
       "tmnxVRtIPsecTnlIsakmpEstabTime": tmnxVRtIPsecTnlIsakmpEstabTime,
       "tmnxVRtIPsecTnlIsakmpNegLifeTime": tmnxVRtIPsecTnlIsakmpNegLifeTime,
       "tmnxVRtIPsecTnlNumDpdTx": tmnxVRtIPsecTnlNumDpdTx,
       "tmnxVRtIPsecTnlNumDpdRx": tmnxVRtIPsecTnlNumDpdRx,
       "tmnxVRtIPsecTnlNumDpdAckTx": tmnxVRtIPsecTnlNumDpdAckTx,
       "tmnxVRtIPsecTnlNumDpdAckRx": tmnxVRtIPsecTnlNumDpdAckRx,
       "tmnxVRtIPsecTnlNumExpRx": tmnxVRtIPsecTnlNumExpRx,
       "tmnxVRtIPsecTnlNumInvalidDpdRx": tmnxVRtIPsecTnlNumInvalidDpdRx,
       "tmnxVRtIPsecTnlNumCtrlPktsTx": tmnxVRtIPsecTnlNumCtrlPktsTx,
       "tmnxVRtIPsecTnlNumCtrlPktsRx": tmnxVRtIPsecTnlNumCtrlPktsRx,
       "tmnxVRtIPsecTnlNumCtrlTxErrors": tmnxVRtIPsecTnlNumCtrlTxErrors,
       "tmnxVRtIPsecTnlNumCtrlRxErrors": tmnxVRtIPsecTnlNumCtrlRxErrors,
       "tmnxVRtIPsecTnlMatCertEntryId": tmnxVRtIPsecTnlMatCertEntryId,
       "tmnxVRtIPsecTnlCertProfName": tmnxVRtIPsecTnlCertProfName,
       "tmnxVRtIPsecTnlStatIsakmpAuthAlg": tmnxVRtIPsecTnlStatIsakmpAuthAlg,
       "tmnxVRtIPsecTnlStatIsakmpEncrAlg": tmnxVRtIPsecTnlStatIsakmpEncrAlg,
       "tmnxVRtIPsecTnlStatIsakmpPfsDhGp": tmnxVRtIPsecTnlStatIsakmpPfsDhGp,
       "tmnxVRtIPsecTnlStatIkeTranPrfAlg": tmnxVRtIPsecTnlStatIkeTranPrfAlg,
       "tmnxIPsecLOClientEsaTable": tmnxIPsecLOClientEsaTable,
       "tmnxIPsecLOClientEsaEntry": tmnxIPsecLOClientEsaEntry,
       "tmnxIPsecLOClientEsaStatus": tmnxIPsecLOClientEsaStatus,
       "tmnxIPsecLOClientEsaFailAtempt": tmnxIPsecLOClientEsaFailAtempt,
       "tmnxIPsecLOClientEsaDroppedPkt": tmnxIPsecLOClientEsaDroppedPkt,
       "tmnxIPsecLOClientEsaRemainTime": tmnxIPsecLOClientEsaRemainTime,
       "tmnxIPsecEsaHistStatsTable": tmnxIPsecEsaHistStatsTable,
       "tmnxIPsecEsaHistStatsEntry": tmnxIPsecEsaHistStatsEntry,
       "tmnxIPsecEsaHistStatsType": tmnxIPsecEsaHistStatsType,
       "tmnxIPsecEsaHistStatsIntvIdx": tmnxIPsecEsaHistStatsIntvIdx,
       "tmnxIPsecEsaHistStatsValue64": tmnxIPsecEsaHistStatsValue64,
       "tmnxIPsecEsaHistStatsValue32": tmnxIPsecEsaHistStatsValue32,
       "tmnxIPsecEsaHistStatsIntvStTm": tmnxIPsecEsaHistStatsIntvStTm,
       "tmnxIPsecEsaHistStatsIntvDur": tmnxIPsecEsaHistStatsIntvDur,
       "tmnxIPsecEsaHistStatsFstFTm": tmnxIPsecEsaHistStatsFstFTm,
       "tmnxIPsecEsaHistStatsFstFDesc": tmnxIPsecEsaHistStatsFstFDesc,
       "tmnxIPsecEsaHistStatsLstFTm": tmnxIPsecEsaHistStatsLstFTm,
       "tmnxIPsecEsaHistStatsLstFDesc": tmnxIPsecEsaHistStatsLstFDesc,
       "tmnxIPsecEsaDpStatsTable": tmnxIPsecEsaDpStatsTable,
       "tmnxIPsecEsaDpStatsEntry": tmnxIPsecEsaDpStatsEntry,
       "tmnxIPsecEsaDpStatsEncryptPkts": tmnxIPsecEsaDpStatsEncryptPkts,
       "tmnxIPsecEsaDpStatsEncryptBytes": tmnxIPsecEsaDpStatsEncryptBytes,
       "tmnxIPsecEsaDpStatsDecryptPkts": tmnxIPsecEsaDpStatsDecryptPkts,
       "tmnxIPsecEsaDpStatsDecryptBytes": tmnxIPsecEsaDpStatsDecryptBytes,
       "tmnxIPsecEsaDpStatsTxPktErrs": tmnxIPsecEsaDpStatsTxPktErrs,
       "tmnxIPsecEsaDpStatsOutBDropPkts": tmnxIPsecEsaDpStatsOutBDropPkts,
       "tmnxIPsecEsaDpStatsOutBSAMisses": tmnxIPsecEsaDpStatsOutBSAMisses,
       "tmnxIPsecEsaDpStatsOutBPEMisses": tmnxIPsecEsaDpStatsOutBPEMisses,
       "tmnxIPsecEsaDpStatsInBDropPkts": tmnxIPsecEsaDpStatsInBDropPkts,
       "tmnxIPsecEsaDpStatsInBSAMisses": tmnxIPsecEsaDpStatsInBSAMisses,
       "tmnxIPsecEsaDpStatsInBIPMismatch": tmnxIPsecEsaDpStatsInBIPMismatch,
       "tmnxIPsecEsaDpInFragments": tmnxIPsecEsaDpInFragments,
       "tmnxIPsecEsaDpPktsReassem": tmnxIPsecEsaDpPktsReassem,
       "tmnxIPsecEsaDpFragDropTime": tmnxIPsecEsaDpFragDropTime,
       "tmnxIPsecEsaDpFragDropped": tmnxIPsecEsaDpFragDropped,
       "tmnxIPsecEsaDpGreTnlInPkts": tmnxIPsecEsaDpGreTnlInPkts,
       "tmnxIPsecEsaDpGreTnlInBytes": tmnxIPsecEsaDpGreTnlInBytes,
       "tmnxIPsecEsaDpGreTnlInErrs": tmnxIPsecEsaDpGreTnlInErrs,
       "tmnxIPsecEsaDpGreTnlOutPkts": tmnxIPsecEsaDpGreTnlOutPkts,
       "tmnxIPsecEsaDpGreTnlOutBytes": tmnxIPsecEsaDpGreTnlOutBytes,
       "tmnxIPsecEsaDpGreTnlOutErrs": tmnxIPsecEsaDpGreTnlOutErrs,
       "tmnxIPsecEsaDpPktsDropDfSet": tmnxIPsecEsaDpPktsDropDfSet,
       "tmnxIPsecEsaDpStaticIPsecTnls": tmnxIPsecEsaDpStaticIPsecTnls,
       "tmnxIPsecEsaDpDynIPsecTnls": tmnxIPsecEsaDpDynIPsecTnls,
       "tmnxIPsecEsaDpIpGreTnls": tmnxIPsecEsaDpIpGreTnls,
       "tmnxIPsecEsaDpIpv4Tnls": tmnxIPsecEsaDpIpv4Tnls,
       "tmnxIPsecEsaDpL2tpv3TnlInPkts": tmnxIPsecEsaDpL2tpv3TnlInPkts,
       "tmnxIPsecEsaDpL2tpv3TnlInBytes": tmnxIPsecEsaDpL2tpv3TnlInBytes,
       "tmnxIPsecEsaDpL2tpv3TnlInErrs": tmnxIPsecEsaDpL2tpv3TnlInErrs,
       "tmnxIPsecEsaDpL2tpv3TnlInCookErr": tmnxIPsecEsaDpL2tpv3TnlInCookErr,
       "tmnxIPsecEsaDpL2tpv3TnlInSeIdErr": tmnxIPsecEsaDpL2tpv3TnlInSeIdErr,
       "tmnxIPsecEsaDpL2tpv3TnlOutPkts": tmnxIPsecEsaDpL2tpv3TnlOutPkts,
       "tmnxIPsecEsaDpL2tpv3TnlOutBytes": tmnxIPsecEsaDpL2tpv3TnlOutBytes,
       "tmnxIPsecEsaDpL2tpv3TnlOutErrs": tmnxIPsecEsaDpL2tpv3TnlOutErrs,
       "tmnxIPsecEsaDpL2tpv3Tnls": tmnxIPsecEsaDpL2tpv3Tnls,
       "tmnxIPsecNotifyPrefix": tmnxIPsecNotifyPrefix,
       "tmnxIPsecNotifications": tmnxIPsecNotifications,
       "tIPsecRUTnlFailToCreate": tIPsecRUTnlFailToCreate,
       "tIPsecRUSAFailToAddRoute": tIPsecRUSAFailToAddRoute,
       "tIPsecBfdIntfSessStateChgd": tIPsecBfdIntfSessStateChgd,
       "tIPsecRadAcctPlcyFailure": tIPsecRadAcctPlcyFailure,
       "tIPSecTrustAnchorPrfOprChg": tIPSecTrustAnchorPrfOprChg,
       "tIPsecTunnelEncapIpMtuTooSmall": tIPsecTunnelEncapIpMtuTooSmall,
       "tIPsecRuTnlEncapIpMtuTooSmall": tIPsecRuTnlEncapIpMtuTooSmall,
       "tmnxSecNotifCmptedCertHashChngd": tmnxSecNotifCmptedCertHashChngd,
       "tmnxSecNotifCmptedCertChnChngd": tmnxSecNotifCmptedCertChnChngd,
       "tmnxSecNotifSendChnNotInCmptChn": tmnxSecNotifSendChnNotInCmptChn,
       "tmnxIPsecTunnelOperStateChange": tmnxIPsecTunnelOperStateChange,
       "tmnxIPsecGWOperStateChange": tmnxIPsecGWOperStateChange,
       "tIPsecRUTnlRemoved": tIPsecRUTnlRemoved,
       "tIPsecTunnelProtocolFailed": tIPsecTunnelProtocolFailed}
)
