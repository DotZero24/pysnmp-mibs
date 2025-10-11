# SNMP MIB module (ALU-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/ALU-SECURITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:53:49 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(tmnxCpmFlashHwIndex,
 tmnxCpmFlashOperStatus) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCpmFlashHwIndex",
    "tmnxCpmFlashOperStatus")

(TEntryId,
 TFilterLogId,
 TItemMatch) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TEntryId",
    "TFilterLogId",
    "TItemMatch")

(tmnxMcPeerIpAddr,
 tmnxMcPeerIpType,
 tmnxMcPeerSrcIpAddr) = mibBuilder.importSymbols(
    "TIMETRA-MC-REDUNDANCY-MIB",
    "tmnxMcPeerIpAddr",
    "tmnxMcPeerIpType",
    "tmnxMcPeerSrcIpAddr")

(sdpBindId,) = mibBuilder.importSymbols(
    "TIMETRA-SDP-MIB",
    "sdpBindId")

(SdpId,
 svcId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "SdpId",
    "svcId")

(Dot1PPriority,
 Dot1PPriorityMask,
 InterfaceIndex,
 IpAddressPrefixLength,
 ServiceAccessPoint,
 TBurstSize,
 TCIRRate,
 TCpmProtPolicyID,
 TDSCPNameOrEmpty,
 TIpOption,
 TIpProtocol,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TOperator,
 TPIRRate,
 TPIRRateOrZero,
 TTcpUdpPort,
 TTcpUdpPortOperator,
 TmnxActionType,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "Dot1PPriority",
    "Dot1PPriorityMask",
    "InterfaceIndex",
    "IpAddressPrefixLength",
    "ServiceAccessPoint",
    "TBurstSize",
    "TCIRRate",
    "TCpmProtPolicyID",
    "TDSCPNameOrEmpty",
    "TIpOption",
    "TIpProtocol",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TOperator",
    "TPIRRate",
    "TPIRRateOrZero",
    "TTcpUdpPort",
    "TTcpUdpPortOperator",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVRtrIDOrZero")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

aluZoneModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 15)
)
if mibBuilder.loadTexts:
    aluZoneModule.setRevisions(
        ("1911-07-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TSecurityLogId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TSecurityLogProfileId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class TIPOperator(TextualConvention, Integer32):
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
          ("eq", 1),
          ("range", 2))
    )



class TZoneType(TextualConvention, Integer32):
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
          ("network", 1),
          ("service", 2),
          ("global", 3))
    )



class TPlcyState(TextualConvention, Integer32):
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
          ("empty", 1),
          ("draft", 2),
          ("commited", 3))
    )



class TPoolType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("srcNatPool", 1))
    )



class TAlgType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("auto", 1),
          ("ftp", 2),
          ("tftp", 3))
    )



class TSecurityPolicerId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )



class AluMcFwAuthAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sha256", 1),
          ("sha512", 2))
    )



class AluMcFwEncrAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 1),
          ("aes256", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AluSecurityMIBConformance_ObjectIdentity = ObjectIdentity
aluSecurityMIBConformance = _AluSecurityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17)
)
_AluSecurityAdminConformance_ObjectIdentity = ObjectIdentity
aluSecurityAdminConformance = _AluSecurityAdminConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1)
)
_AluSecurityAdminCompliances_ObjectIdentity = ObjectIdentity
aluSecurityAdminCompliances = _AluSecurityAdminCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 1)
)
_AluSecurityAdminGroups_ObjectIdentity = ObjectIdentity
aluSecurityAdminGroups = _AluSecurityAdminGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 2)
)
_AluSecurityLogGroups_ObjectIdentity = ObjectIdentity
aluSecurityLogGroups = _AluSecurityLogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 3)
)
_AluSecurityMcGroups_ObjectIdentity = ObjectIdentity
aluSecurityMcGroups = _AluSecurityMcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 4)
)
_AluSecurityOperConformance_ObjectIdentity = ObjectIdentity
aluSecurityOperConformance = _AluSecurityOperConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2)
)
_AluSecurityOperCompliances_ObjectIdentity = ObjectIdentity
aluSecurityOperCompliances = _AluSecurityOperCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2, 1)
)
_AluSecurityOperGroups_ObjectIdentity = ObjectIdentity
aluSecurityOperGroups = _AluSecurityOperGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2, 2)
)
_AluSecurityNotifyGroups_ObjectIdentity = ObjectIdentity
aluSecurityNotifyGroups = _AluSecurityNotifyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2, 3)
)
_AluSecurityStatsConformance_ObjectIdentity = ObjectIdentity
aluSecurityStatsConformance = _AluSecurityStatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 3)
)
_AluSecurityObjs_ObjectIdentity = ObjectIdentity
aluSecurityObjs = _AluSecurityObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17)
)
_AluSecurityAdminObjs_ObjectIdentity = ObjectIdentity
aluSecurityAdminObjs = _AluSecurityAdminObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1)
)


class _AluSecPlcyAdminControlApply_Type(Integer32):
    """Custom type aluSecPlcyAdminControlApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("initialize", 2),
          ("commit", 3))
    )


_AluSecPlcyAdminControlApply_Type.__name__ = "Integer32"
_AluSecPlcyAdminControlApply_Object = MibScalar
aluSecPlcyAdminControlApply = _AluSecPlcyAdminControlApply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 1),
    _AluSecPlcyAdminControlApply_Type()
)
aluSecPlcyAdminControlApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSecPlcyAdminControlApply.setStatus("current")


class _AluSecPlcyBypass_Type(TruthValue):
    """Custom type aluSecPlcyBypass based on TruthValue"""
    defaultValue = 2


_AluSecPlcyBypass_Type.__name__ = "TruthValue"
_AluSecPlcyBypass_Object = MibScalar
aluSecPlcyBypass = _AluSecPlcyBypass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 2),
    _AluSecPlcyBypass_Type()
)
aluSecPlcyBypass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyBypass.setStatus("current")
_AluZoneConfigTable_Object = MibTable
aluZoneConfigTable = _AluZoneConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4)
)
if mibBuilder.loadTexts:
    aluZoneConfigTable.setStatus("current")
_AluZoneConfigEntry_Object = MibTableRow
aluZoneConfigEntry = _AluZoneConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1)
)
aluZoneConfigEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluZoneConfigId"),
)
if mibBuilder.loadTexts:
    aluZoneConfigEntry.setStatus("current")


class _AluZoneConfigId_Type(Unsigned32):
    """Custom type aluZoneConfigId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_AluZoneConfigId_Type.__name__ = "Unsigned32"
_AluZoneConfigId_Object = MibTableColumn
aluZoneConfigId = _AluZoneConfigId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 1),
    _AluZoneConfigId_Type()
)
aluZoneConfigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluZoneConfigId.setStatus("current")


class _AluZoneConfigName_Type(TNamedItemOrEmpty):
    """Custom type aluZoneConfigName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluZoneConfigName_Type.__name__ = "TNamedItemOrEmpty"
_AluZoneConfigName_Object = MibTableColumn
aluZoneConfigName = _AluZoneConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 2),
    _AluZoneConfigName_Type()
)
aluZoneConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigName.setStatus("current")
_AluZoneConfigRowStatus_Type = RowStatus
_AluZoneConfigRowStatus_Object = MibTableColumn
aluZoneConfigRowStatus = _AluZoneConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 3),
    _AluZoneConfigRowStatus_Type()
)
aluZoneConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigRowStatus.setStatus("current")


class _AluZoneConfigDescription_Type(TItemDescription):
    """Custom type aluZoneConfigDescription based on TItemDescription"""
    defaultHexValue = ""


_AluZoneConfigDescription_Type.__name__ = "TItemDescription"
_AluZoneConfigDescription_Object = MibTableColumn
aluZoneConfigDescription = _AluZoneConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 4),
    _AluZoneConfigDescription_Type()
)
aluZoneConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigDescription.setStatus("current")


class _AluZoneConfigControlApply_Type(Integer32):
    """Custom type aluZoneConfigControlApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("initialize", 2),
          ("commit", 3))
    )


_AluZoneConfigControlApply_Type.__name__ = "Integer32"
_AluZoneConfigControlApply_Object = MibTableColumn
aluZoneConfigControlApply = _AluZoneConfigControlApply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 5),
    _AluZoneConfigControlApply_Type()
)
aluZoneConfigControlApply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigControlApply.setStatus("current")


class _AluZoneConfigType_Type(TZoneType):
    """Custom type aluZoneConfigType based on TZoneType"""
    defaultValue = 1


_AluZoneConfigType_Type.__name__ = "TZoneType"
_AluZoneConfigType_Object = MibTableColumn
aluZoneConfigType = _AluZoneConfigType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 6),
    _AluZoneConfigType_Type()
)
aluZoneConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigType.setStatus("current")


class _AluZoneConfigSvcId_Type(TmnxServId):
    """Custom type aluZoneConfigSvcId based on TmnxServId"""
    defaultValue = 0


_AluZoneConfigSvcId_Type.__name__ = "TmnxServId"
_AluZoneConfigSvcId_Object = MibTableColumn
aluZoneConfigSvcId = _AluZoneConfigSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 7),
    _AluZoneConfigSvcId_Type()
)
aluZoneConfigSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigSvcId.setStatus("current")


class _AluZoneConfigState_Type(TPlcyState):
    """Custom type aluZoneConfigState based on TPlcyState"""
    defaultValue = 0


_AluZoneConfigState_Type.__name__ = "TPlcyState"
_AluZoneConfigState_Object = MibTableColumn
aluZoneConfigState = _AluZoneConfigState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 8),
    _AluZoneConfigState_Type()
)
aluZoneConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneConfigState.setStatus("current")


class _AluZoneConfigBypass_Type(TruthValue):
    """Custom type aluZoneConfigBypass based on TruthValue"""
    defaultValue = 2


_AluZoneConfigBypass_Type.__name__ = "TruthValue"
_AluZoneConfigBypass_Object = MibTableColumn
aluZoneConfigBypass = _AluZoneConfigBypass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 9),
    _AluZoneConfigBypass_Type()
)
aluZoneConfigBypass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigBypass.setStatus("current")


class _AluZoneConfigInTcpSessLimit_Type(Unsigned32):
    """Custom type aluZoneConfigInTcpSessLimit based on Unsigned32"""
    defaultValue = 0


_AluZoneConfigInTcpSessLimit_Type.__name__ = "Unsigned32"
_AluZoneConfigInTcpSessLimit_Object = MibTableColumn
aluZoneConfigInTcpSessLimit = _AluZoneConfigInTcpSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 10),
    _AluZoneConfigInTcpSessLimit_Type()
)
aluZoneConfigInTcpSessLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigInTcpSessLimit.setStatus("current")


class _AluZoneConfigInUdpSessLimit_Type(Unsigned32):
    """Custom type aluZoneConfigInUdpSessLimit based on Unsigned32"""
    defaultValue = 0


_AluZoneConfigInUdpSessLimit_Type.__name__ = "Unsigned32"
_AluZoneConfigInUdpSessLimit_Object = MibTableColumn
aluZoneConfigInUdpSessLimit = _AluZoneConfigInUdpSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 11),
    _AluZoneConfigInUdpSessLimit_Type()
)
aluZoneConfigInUdpSessLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigInUdpSessLimit.setStatus("current")


class _AluZoneConfigInIcmpSessLimit_Type(Unsigned32):
    """Custom type aluZoneConfigInIcmpSessLimit based on Unsigned32"""
    defaultValue = 0


_AluZoneConfigInIcmpSessLimit_Type.__name__ = "Unsigned32"
_AluZoneConfigInIcmpSessLimit_Object = MibTableColumn
aluZoneConfigInIcmpSessLimit = _AluZoneConfigInIcmpSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 12),
    _AluZoneConfigInIcmpSessLimit_Type()
)
aluZoneConfigInIcmpSessLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigInIcmpSessLimit.setStatus("current")


class _AluZoneConfigInOthSessLimit_Type(Unsigned32):
    """Custom type aluZoneConfigInOthSessLimit based on Unsigned32"""
    defaultValue = 0


_AluZoneConfigInOthSessLimit_Type.__name__ = "Unsigned32"
_AluZoneConfigInOthSessLimit_Object = MibTableColumn
aluZoneConfigInOthSessLimit = _AluZoneConfigInOthSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 13),
    _AluZoneConfigInOthSessLimit_Type()
)
aluZoneConfigInOthSessLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigInOthSessLimit.setStatus("current")


class _AluZoneConfigOutTcpSessLimit_Type(Unsigned32):
    """Custom type aluZoneConfigOutTcpSessLimit based on Unsigned32"""
    defaultValue = 0


_AluZoneConfigOutTcpSessLimit_Type.__name__ = "Unsigned32"
_AluZoneConfigOutTcpSessLimit_Object = MibTableColumn
aluZoneConfigOutTcpSessLimit = _AluZoneConfigOutTcpSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 14),
    _AluZoneConfigOutTcpSessLimit_Type()
)
aluZoneConfigOutTcpSessLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigOutTcpSessLimit.setStatus("current")


class _AluZoneConfigOutUdpSessLimit_Type(Unsigned32):
    """Custom type aluZoneConfigOutUdpSessLimit based on Unsigned32"""
    defaultValue = 0


_AluZoneConfigOutUdpSessLimit_Type.__name__ = "Unsigned32"
_AluZoneConfigOutUdpSessLimit_Object = MibTableColumn
aluZoneConfigOutUdpSessLimit = _AluZoneConfigOutUdpSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 15),
    _AluZoneConfigOutUdpSessLimit_Type()
)
aluZoneConfigOutUdpSessLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigOutUdpSessLimit.setStatus("current")


class _AluZoneConfigOutIcmpSessLimit_Type(Unsigned32):
    """Custom type aluZoneConfigOutIcmpSessLimit based on Unsigned32"""
    defaultValue = 0


_AluZoneConfigOutIcmpSessLimit_Type.__name__ = "Unsigned32"
_AluZoneConfigOutIcmpSessLimit_Object = MibTableColumn
aluZoneConfigOutIcmpSessLimit = _AluZoneConfigOutIcmpSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 16),
    _AluZoneConfigOutIcmpSessLimit_Type()
)
aluZoneConfigOutIcmpSessLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigOutIcmpSessLimit.setStatus("current")


class _AluZoneConfigOutOthSessLimit_Type(Unsigned32):
    """Custom type aluZoneConfigOutOthSessLimit based on Unsigned32"""
    defaultValue = 0


_AluZoneConfigOutOthSessLimit_Type.__name__ = "Unsigned32"
_AluZoneConfigOutOthSessLimit_Object = MibTableColumn
aluZoneConfigOutOthSessLimit = _AluZoneConfigOutOthSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 17),
    _AluZoneConfigOutOthSessLimit_Type()
)
aluZoneConfigOutOthSessLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigOutOthSessLimit.setStatus("current")


class _AluZoneConfigLogId_Type(TSecurityLogId):
    """Custom type aluZoneConfigLogId based on TSecurityLogId"""
    defaultValue = 0


_AluZoneConfigLogId_Type.__name__ = "TSecurityLogId"
_AluZoneConfigLogId_Object = MibTableColumn
aluZoneConfigLogId = _AluZoneConfigLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 18),
    _AluZoneConfigLogId_Type()
)
aluZoneConfigLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigLogId.setStatus("current")


class _AluZoneConfigAutoBind_Type(TruthValue):
    """Custom type aluZoneConfigAutoBind based on TruthValue"""
    defaultValue = 2


_AluZoneConfigAutoBind_Type.__name__ = "TruthValue"
_AluZoneConfigAutoBind_Object = MibTableColumn
aluZoneConfigAutoBind = _AluZoneConfigAutoBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 4, 1, 19),
    _AluZoneConfigAutoBind_Type()
)
aluZoneConfigAutoBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneConfigAutoBind.setStatus("current")
_AluZonePlcyConfigTable_Object = MibTable
aluZonePlcyConfigTable = _AluZonePlcyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 5)
)
if mibBuilder.loadTexts:
    aluZonePlcyConfigTable.setStatus("current")
_AluZonePlcyConfigEntry_Object = MibTableRow
aluZonePlcyConfigEntry = _AluZonePlcyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 5, 1)
)
aluZonePlcyConfigEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluZoneConfigId"),
    (0, "ALU-SECURITY-MIB", "aluZonePlcyConfigEntryId"),
)
if mibBuilder.loadTexts:
    aluZonePlcyConfigEntry.setStatus("current")


class _AluZonePlcyConfigEntryId_Type(Unsigned32):
    """Custom type aluZonePlcyConfigEntryId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZonePlcyConfigEntryId_Type.__name__ = "Unsigned32"
_AluZonePlcyConfigEntryId_Object = MibTableColumn
aluZonePlcyConfigEntryId = _AluZonePlcyConfigEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 5, 1, 1),
    _AluZonePlcyConfigEntryId_Type()
)
aluZonePlcyConfigEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluZonePlcyConfigEntryId.setStatus("current")
_AluZonePlcyConfigRowStatus_Type = RowStatus
_AluZonePlcyConfigRowStatus_Object = MibTableColumn
aluZonePlcyConfigRowStatus = _AluZonePlcyConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 5, 1, 2),
    _AluZonePlcyConfigRowStatus_Type()
)
aluZonePlcyConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZonePlcyConfigRowStatus.setStatus("current")


class _AluZonePlcyConfigSecPlcyId_Type(Unsigned32):
    """Custom type aluZonePlcyConfigSecPlcyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluZonePlcyConfigSecPlcyId_Type.__name__ = "Unsigned32"
_AluZonePlcyConfigSecPlcyId_Object = MibTableColumn
aluZonePlcyConfigSecPlcyId = _AluZonePlcyConfigSecPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 5, 1, 3),
    _AluZonePlcyConfigSecPlcyId_Type()
)
aluZonePlcyConfigSecPlcyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZonePlcyConfigSecPlcyId.setStatus("current")
_AluZoneNatPoolConfigTable_Object = MibTable
aluZoneNatPoolConfigTable = _AluZoneNatPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 6)
)
if mibBuilder.loadTexts:
    aluZoneNatPoolConfigTable.setStatus("current")
_AluZoneNatPoolConfigEntry_Object = MibTableRow
aluZoneNatPoolConfigEntry = _AluZoneNatPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 6, 1)
)
aluZoneNatPoolConfigEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluZoneConfigId"),
    (0, "ALU-SECURITY-MIB", "aluZoneNatPoolConfigId"),
)
if mibBuilder.loadTexts:
    aluZoneNatPoolConfigEntry.setStatus("current")


class _AluZoneNatPoolConfigId_Type(Unsigned32):
    """Custom type aluZoneNatPoolConfigId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AluZoneNatPoolConfigId_Type.__name__ = "Unsigned32"
_AluZoneNatPoolConfigId_Object = MibTableColumn
aluZoneNatPoolConfigId = _AluZoneNatPoolConfigId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 6, 1, 1),
    _AluZoneNatPoolConfigId_Type()
)
aluZoneNatPoolConfigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluZoneNatPoolConfigId.setStatus("current")
_AluZoneNatPoolConfigName_Type = TNamedItemOrEmpty
_AluZoneNatPoolConfigName_Object = MibTableColumn
aluZoneNatPoolConfigName = _AluZoneNatPoolConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 6, 1, 2),
    _AluZoneNatPoolConfigName_Type()
)
aluZoneNatPoolConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolConfigName.setStatus("current")
_AluZoneNatPoolConfigRowStatus_Type = RowStatus
_AluZoneNatPoolConfigRowStatus_Object = MibTableColumn
aluZoneNatPoolConfigRowStatus = _AluZoneNatPoolConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 6, 1, 3),
    _AluZoneNatPoolConfigRowStatus_Type()
)
aluZoneNatPoolConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolConfigRowStatus.setStatus("current")


class _AluZoneNatPoolConfigDescription_Type(TItemDescription):
    """Custom type aluZoneNatPoolConfigDescription based on TItemDescription"""
    defaultHexValue = ""


_AluZoneNatPoolConfigDescription_Type.__name__ = "TItemDescription"
_AluZoneNatPoolConfigDescription_Object = MibTableColumn
aluZoneNatPoolConfigDescription = _AluZoneNatPoolConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 6, 1, 4),
    _AluZoneNatPoolConfigDescription_Type()
)
aluZoneNatPoolConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolConfigDescription.setStatus("current")


class _AluZoneNatPoolConfigType_Type(TPoolType):
    """Custom type aluZoneNatPoolConfigType based on TPoolType"""
    defaultValue = 1


_AluZoneNatPoolConfigType_Type.__name__ = "TPoolType"
_AluZoneNatPoolConfigType_Object = MibTableColumn
aluZoneNatPoolConfigType = _AluZoneNatPoolConfigType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 6, 1, 5),
    _AluZoneNatPoolConfigType_Type()
)
aluZoneNatPoolConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolConfigType.setStatus("current")


class _AluZoneNatPoolConfigDirection_Type(Integer32):
    """Custom type aluZoneNatPoolConfigDirection based on Integer32"""
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
        *(("unknown", 0),
          ("zoneInbound", 1),
          ("zoneOutbound", 2))
    )


_AluZoneNatPoolConfigDirection_Type.__name__ = "Integer32"
_AluZoneNatPoolConfigDirection_Object = MibTableColumn
aluZoneNatPoolConfigDirection = _AluZoneNatPoolConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 6, 1, 6),
    _AluZoneNatPoolConfigDirection_Type()
)
aluZoneNatPoolConfigDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolConfigDirection.setStatus("current")
_AluZoneNatPoolParamsConfigTable_Object = MibTable
aluZoneNatPoolParamsConfigTable = _AluZoneNatPoolParamsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 7)
)
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsConfigTable.setStatus("current")
_AluZoneNatPoolParamsConfigEntry_Object = MibTableRow
aluZoneNatPoolParamsConfigEntry = _AluZoneNatPoolParamsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 7, 1)
)
aluZoneNatPoolParamsConfigEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluZoneConfigId"),
    (0, "ALU-SECURITY-MIB", "aluZoneNatPoolConfigId"),
    (0, "ALU-SECURITY-MIB", "aluZoneNatPoolParamsConfigEntryId"),
)
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsConfigEntry.setStatus("current")


class _AluZoneNatPoolParamsConfigEntryId_Type(Unsigned32):
    """Custom type aluZoneNatPoolParamsConfigEntryId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZoneNatPoolParamsConfigEntryId_Type.__name__ = "Unsigned32"
_AluZoneNatPoolParamsConfigEntryId_Object = MibTableColumn
aluZoneNatPoolParamsConfigEntryId = _AluZoneNatPoolParamsConfigEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 7, 1, 1),
    _AluZoneNatPoolParamsConfigEntryId_Type()
)
aluZoneNatPoolParamsConfigEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsConfigEntryId.setStatus("current")
_AluZoneNatPoolParamsConfigRowStatus_Type = RowStatus
_AluZoneNatPoolParamsConfigRowStatus_Object = MibTableColumn
aluZoneNatPoolParamsConfigRowStatus = _AluZoneNatPoolParamsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 7, 1, 2),
    _AluZoneNatPoolParamsConfigRowStatus_Type()
)
aluZoneNatPoolParamsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsConfigRowStatus.setStatus("current")


class _AluZoneNatPoolParamsConfigIPAddrValue1_Type(IpAddress):
    """Custom type aluZoneNatPoolParamsConfigIPAddrValue1 based on IpAddress"""
    defaultHexValue = "00000000"


_AluZoneNatPoolParamsConfigIPAddrValue1_Type.__name__ = "IpAddress"
_AluZoneNatPoolParamsConfigIPAddrValue1_Object = MibTableColumn
aluZoneNatPoolParamsConfigIPAddrValue1 = _AluZoneNatPoolParamsConfigIPAddrValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 7, 1, 3),
    _AluZoneNatPoolParamsConfigIPAddrValue1_Type()
)
aluZoneNatPoolParamsConfigIPAddrValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsConfigIPAddrValue1.setStatus("current")


class _AluZoneNatPoolParamsConfigIPAddrValue2_Type(IpAddress):
    """Custom type aluZoneNatPoolParamsConfigIPAddrValue2 based on IpAddress"""
    defaultHexValue = "00000000"


_AluZoneNatPoolParamsConfigIPAddrValue2_Type.__name__ = "IpAddress"
_AluZoneNatPoolParamsConfigIPAddrValue2_Object = MibTableColumn
aluZoneNatPoolParamsConfigIPAddrValue2 = _AluZoneNatPoolParamsConfigIPAddrValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 7, 1, 4),
    _AluZoneNatPoolParamsConfigIPAddrValue2_Type()
)
aluZoneNatPoolParamsConfigIPAddrValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsConfigIPAddrValue2.setStatus("current")


class _AluZoneNatPoolParamsConfigIPOperator_Type(TIPOperator):
    """Custom type aluZoneNatPoolParamsConfigIPOperator based on TIPOperator"""
    defaultValue = 0


_AluZoneNatPoolParamsConfigIPOperator_Type.__name__ = "TIPOperator"
_AluZoneNatPoolParamsConfigIPOperator_Object = MibTableColumn
aluZoneNatPoolParamsConfigIPOperator = _AluZoneNatPoolParamsConfigIPOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 7, 1, 5),
    _AluZoneNatPoolParamsConfigIPOperator_Type()
)
aluZoneNatPoolParamsConfigIPOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsConfigIPOperator.setStatus("current")


class _AluZoneNatPoolParamsConfigIPInterfaceIndex_Type(InterfaceIndexOrZero):
    """Custom type aluZoneNatPoolParamsConfigIPInterfaceIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_AluZoneNatPoolParamsConfigIPInterfaceIndex_Type.__name__ = "InterfaceIndexOrZero"
_AluZoneNatPoolParamsConfigIPInterfaceIndex_Object = MibTableColumn
aluZoneNatPoolParamsConfigIPInterfaceIndex = _AluZoneNatPoolParamsConfigIPInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 7, 1, 6),
    _AluZoneNatPoolParamsConfigIPInterfaceIndex_Type()
)
aluZoneNatPoolParamsConfigIPInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsConfigIPInterfaceIndex.setStatus("current")


class _AluZoneNatPoolParamsConfigPortOperator_Type(TTcpUdpPortOperator):
    """Custom type aluZoneNatPoolParamsConfigPortOperator based on TTcpUdpPortOperator"""
    defaultValue = 0


_AluZoneNatPoolParamsConfigPortOperator_Type.__name__ = "TTcpUdpPortOperator"
_AluZoneNatPoolParamsConfigPortOperator_Object = MibTableColumn
aluZoneNatPoolParamsConfigPortOperator = _AluZoneNatPoolParamsConfigPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 7, 1, 7),
    _AluZoneNatPoolParamsConfigPortOperator_Type()
)
aluZoneNatPoolParamsConfigPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsConfigPortOperator.setStatus("current")


class _AluZoneNatPoolParamsConfigPortValue1_Type(TTcpUdpPort):
    """Custom type aluZoneNatPoolParamsConfigPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_AluZoneNatPoolParamsConfigPortValue1_Type.__name__ = "TTcpUdpPort"
_AluZoneNatPoolParamsConfigPortValue1_Object = MibTableColumn
aluZoneNatPoolParamsConfigPortValue1 = _AluZoneNatPoolParamsConfigPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 7, 1, 8),
    _AluZoneNatPoolParamsConfigPortValue1_Type()
)
aluZoneNatPoolParamsConfigPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsConfigPortValue1.setStatus("current")


class _AluZoneNatPoolParamsConfigPortValue2_Type(TTcpUdpPort):
    """Custom type aluZoneNatPoolParamsConfigPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_AluZoneNatPoolParamsConfigPortValue2_Type.__name__ = "TTcpUdpPort"
_AluZoneNatPoolParamsConfigPortValue2_Object = MibTableColumn
aluZoneNatPoolParamsConfigPortValue2 = _AluZoneNatPoolParamsConfigPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 7, 1, 9),
    _AluZoneNatPoolParamsConfigPortValue2_Type()
)
aluZoneNatPoolParamsConfigPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsConfigPortValue2.setStatus("current")
_AluSecPlcyConfigTable_Object = MibTable
aluSecPlcyConfigTable = _AluSecPlcyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 8)
)
if mibBuilder.loadTexts:
    aluSecPlcyConfigTable.setStatus("current")
_AluSecPlcyConfigEntry_Object = MibTableRow
aluSecPlcyConfigEntry = _AluSecPlcyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 8, 1)
)
aluSecPlcyConfigEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecPlcyConfigId"),
)
if mibBuilder.loadTexts:
    aluSecPlcyConfigEntry.setStatus("current")


class _AluSecPlcyConfigId_Type(Unsigned32):
    """Custom type aluSecPlcyConfigId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecPlcyConfigId_Type.__name__ = "Unsigned32"
_AluSecPlcyConfigId_Object = MibTableColumn
aluSecPlcyConfigId = _AluSecPlcyConfigId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 8, 1, 1),
    _AluSecPlcyConfigId_Type()
)
aluSecPlcyConfigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecPlcyConfigId.setStatus("current")
_AluSecPlcyConfigRowStatus_Type = RowStatus
_AluSecPlcyConfigRowStatus_Object = MibTableColumn
aluSecPlcyConfigRowStatus = _AluSecPlcyConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 8, 1, 2),
    _AluSecPlcyConfigRowStatus_Type()
)
aluSecPlcyConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyConfigRowStatus.setStatus("current")


class _AluSecPlcyConfigName_Type(TNamedItemOrEmpty):
    """Custom type aluSecPlcyConfigName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSecPlcyConfigName_Type.__name__ = "TNamedItemOrEmpty"
_AluSecPlcyConfigName_Object = MibTableColumn
aluSecPlcyConfigName = _AluSecPlcyConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 8, 1, 3),
    _AluSecPlcyConfigName_Type()
)
aluSecPlcyConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyConfigName.setStatus("current")


class _AluSecPlcyConfigDescription_Type(TItemDescription):
    """Custom type aluSecPlcyConfigDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecPlcyConfigDescription_Type.__name__ = "TItemDescription"
_AluSecPlcyConfigDescription_Object = MibTableColumn
aluSecPlcyConfigDescription = _AluSecPlcyConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 8, 1, 4),
    _AluSecPlcyConfigDescription_Type()
)
aluSecPlcyConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyConfigDescription.setStatus("current")
_AluSecPlcyParamsConfigTable_Object = MibTable
aluSecPlcyParamsConfigTable = _AluSecPlcyParamsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9)
)
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigTable.setStatus("current")
_AluSecPlcyParamsConfigEntry_Object = MibTableRow
aluSecPlcyParamsConfigEntry = _AluSecPlcyParamsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1)
)
aluSecPlcyParamsConfigEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecPlcyConfigId"),
    (0, "ALU-SECURITY-MIB", "aluSecPlcyParamsConfigRuleId"),
)
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigEntry.setStatus("current")


class _AluSecPlcyParamsConfigRuleId_Type(Unsigned32):
    """Custom type aluSecPlcyParamsConfigRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecPlcyParamsConfigRuleId_Type.__name__ = "Unsigned32"
_AluSecPlcyParamsConfigRuleId_Object = MibTableColumn
aluSecPlcyParamsConfigRuleId = _AluSecPlcyParamsConfigRuleId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 1),
    _AluSecPlcyParamsConfigRuleId_Type()
)
aluSecPlcyParamsConfigRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigRuleId.setStatus("current")
_AluSecPlcyParamsConfigRowStatus_Type = RowStatus
_AluSecPlcyParamsConfigRowStatus_Object = MibTableColumn
aluSecPlcyParamsConfigRowStatus = _AluSecPlcyParamsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 2),
    _AluSecPlcyParamsConfigRowStatus_Type()
)
aluSecPlcyParamsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigRowStatus.setStatus("current")


class _AluSecPlcyParamsConfigDescription_Type(TItemDescription):
    """Custom type aluSecPlcyParamsConfigDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecPlcyParamsConfigDescription_Type.__name__ = "TItemDescription"
_AluSecPlcyParamsConfigDescription_Object = MibTableColumn
aluSecPlcyParamsConfigDescription = _AluSecPlcyParamsConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 3),
    _AluSecPlcyParamsConfigDescription_Type()
)
aluSecPlcyParamsConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigDescription.setStatus("current")


class _AluSecPlcyParamsConfigMatchSrcIPAddrValue1_Type(IpAddress):
    """Custom type aluSecPlcyParamsConfigMatchSrcIPAddrValue1 based on IpAddress"""
    defaultHexValue = "00000000"


_AluSecPlcyParamsConfigMatchSrcIPAddrValue1_Type.__name__ = "IpAddress"
_AluSecPlcyParamsConfigMatchSrcIPAddrValue1_Object = MibTableColumn
aluSecPlcyParamsConfigMatchSrcIPAddrValue1 = _AluSecPlcyParamsConfigMatchSrcIPAddrValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 4),
    _AluSecPlcyParamsConfigMatchSrcIPAddrValue1_Type()
)
aluSecPlcyParamsConfigMatchSrcIPAddrValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchSrcIPAddrValue1.setStatus("current")


class _AluSecPlcyParamsConfigMatchSrcIPAddrValue2_Type(IpAddress):
    """Custom type aluSecPlcyParamsConfigMatchSrcIPAddrValue2 based on IpAddress"""
    defaultHexValue = "00000000"


_AluSecPlcyParamsConfigMatchSrcIPAddrValue2_Type.__name__ = "IpAddress"
_AluSecPlcyParamsConfigMatchSrcIPAddrValue2_Object = MibTableColumn
aluSecPlcyParamsConfigMatchSrcIPAddrValue2 = _AluSecPlcyParamsConfigMatchSrcIPAddrValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 5),
    _AluSecPlcyParamsConfigMatchSrcIPAddrValue2_Type()
)
aluSecPlcyParamsConfigMatchSrcIPAddrValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchSrcIPAddrValue2.setStatus("current")


class _AluSecPlcyParamsConfigMatchSrcIPOperator_Type(TIPOperator):
    """Custom type aluSecPlcyParamsConfigMatchSrcIPOperator based on TIPOperator"""
    defaultValue = 0


_AluSecPlcyParamsConfigMatchSrcIPOperator_Type.__name__ = "TIPOperator"
_AluSecPlcyParamsConfigMatchSrcIPOperator_Object = MibTableColumn
aluSecPlcyParamsConfigMatchSrcIPOperator = _AluSecPlcyParamsConfigMatchSrcIPOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 6),
    _AluSecPlcyParamsConfigMatchSrcIPOperator_Type()
)
aluSecPlcyParamsConfigMatchSrcIPOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchSrcIPOperator.setStatus("current")


class _AluSecPlcyParamsConfigMatchSrcIPHostGroup_Type(Unsigned32):
    """Custom type aluSecPlcyParamsConfigMatchSrcIPHostGroup based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSecPlcyParamsConfigMatchSrcIPHostGroup_Type.__name__ = "Unsigned32"
_AluSecPlcyParamsConfigMatchSrcIPHostGroup_Object = MibTableColumn
aluSecPlcyParamsConfigMatchSrcIPHostGroup = _AluSecPlcyParamsConfigMatchSrcIPHostGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 7),
    _AluSecPlcyParamsConfigMatchSrcIPHostGroup_Type()
)
aluSecPlcyParamsConfigMatchSrcIPHostGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchSrcIPHostGroup.setStatus("current")


class _AluSecPlcyParamsConfigMatchDstIPAddrValue1_Type(IpAddress):
    """Custom type aluSecPlcyParamsConfigMatchDstIPAddrValue1 based on IpAddress"""
    defaultHexValue = "00000000"


_AluSecPlcyParamsConfigMatchDstIPAddrValue1_Type.__name__ = "IpAddress"
_AluSecPlcyParamsConfigMatchDstIPAddrValue1_Object = MibTableColumn
aluSecPlcyParamsConfigMatchDstIPAddrValue1 = _AluSecPlcyParamsConfigMatchDstIPAddrValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 8),
    _AluSecPlcyParamsConfigMatchDstIPAddrValue1_Type()
)
aluSecPlcyParamsConfigMatchDstIPAddrValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchDstIPAddrValue1.setStatus("current")


class _AluSecPlcyParamsConfigMatchDstIPAddrValue2_Type(IpAddress):
    """Custom type aluSecPlcyParamsConfigMatchDstIPAddrValue2 based on IpAddress"""
    defaultHexValue = "00000000"


_AluSecPlcyParamsConfigMatchDstIPAddrValue2_Type.__name__ = "IpAddress"
_AluSecPlcyParamsConfigMatchDstIPAddrValue2_Object = MibTableColumn
aluSecPlcyParamsConfigMatchDstIPAddrValue2 = _AluSecPlcyParamsConfigMatchDstIPAddrValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 9),
    _AluSecPlcyParamsConfigMatchDstIPAddrValue2_Type()
)
aluSecPlcyParamsConfigMatchDstIPAddrValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchDstIPAddrValue2.setStatus("current")


class _AluSecPlcyParamsConfigMatchDstIPOperator_Type(TIPOperator):
    """Custom type aluSecPlcyParamsConfigMatchDstIPOperator based on TIPOperator"""
    defaultValue = 0


_AluSecPlcyParamsConfigMatchDstIPOperator_Type.__name__ = "TIPOperator"
_AluSecPlcyParamsConfigMatchDstIPOperator_Object = MibTableColumn
aluSecPlcyParamsConfigMatchDstIPOperator = _AluSecPlcyParamsConfigMatchDstIPOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 10),
    _AluSecPlcyParamsConfigMatchDstIPOperator_Type()
)
aluSecPlcyParamsConfigMatchDstIPOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchDstIPOperator.setStatus("current")


class _AluSecPlcyParamsConfigMatchDstIPHostGroup_Type(Unsigned32):
    """Custom type aluSecPlcyParamsConfigMatchDstIPHostGroup based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSecPlcyParamsConfigMatchDstIPHostGroup_Type.__name__ = "Unsigned32"
_AluSecPlcyParamsConfigMatchDstIPHostGroup_Object = MibTableColumn
aluSecPlcyParamsConfigMatchDstIPHostGroup = _AluSecPlcyParamsConfigMatchDstIPHostGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 11),
    _AluSecPlcyParamsConfigMatchDstIPHostGroup_Type()
)
aluSecPlcyParamsConfigMatchDstIPHostGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchDstIPHostGroup.setStatus("current")


class _AluSecPlcyParamsConfigMatchProtocol_Type(TIpProtocol):
    """Custom type aluSecPlcyParamsConfigMatchProtocol based on TIpProtocol"""
    defaultValue = -1


_AluSecPlcyParamsConfigMatchProtocol_Type.__name__ = "TIpProtocol"
_AluSecPlcyParamsConfigMatchProtocol_Object = MibTableColumn
aluSecPlcyParamsConfigMatchProtocol = _AluSecPlcyParamsConfigMatchProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 12),
    _AluSecPlcyParamsConfigMatchProtocol_Type()
)
aluSecPlcyParamsConfigMatchProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchProtocol.setStatus("current")


class _AluSecPlcyParamsConfigMatchSrcPortValue1_Type(TTcpUdpPort):
    """Custom type aluSecPlcyParamsConfigMatchSrcPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_AluSecPlcyParamsConfigMatchSrcPortValue1_Type.__name__ = "TTcpUdpPort"
_AluSecPlcyParamsConfigMatchSrcPortValue1_Object = MibTableColumn
aluSecPlcyParamsConfigMatchSrcPortValue1 = _AluSecPlcyParamsConfigMatchSrcPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 13),
    _AluSecPlcyParamsConfigMatchSrcPortValue1_Type()
)
aluSecPlcyParamsConfigMatchSrcPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchSrcPortValue1.setStatus("current")


class _AluSecPlcyParamsConfigMatchSrcPortValue2_Type(TTcpUdpPort):
    """Custom type aluSecPlcyParamsConfigMatchSrcPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_AluSecPlcyParamsConfigMatchSrcPortValue2_Type.__name__ = "TTcpUdpPort"
_AluSecPlcyParamsConfigMatchSrcPortValue2_Object = MibTableColumn
aluSecPlcyParamsConfigMatchSrcPortValue2 = _AluSecPlcyParamsConfigMatchSrcPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 14),
    _AluSecPlcyParamsConfigMatchSrcPortValue2_Type()
)
aluSecPlcyParamsConfigMatchSrcPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchSrcPortValue2.setStatus("current")


class _AluSecPlcyParamsConfigMatchSrcPortOp_Type(TOperator):
    """Custom type aluSecPlcyParamsConfigMatchSrcPortOp based on TOperator"""
    defaultValue = 0


_AluSecPlcyParamsConfigMatchSrcPortOp_Type.__name__ = "TOperator"
_AluSecPlcyParamsConfigMatchSrcPortOp_Object = MibTableColumn
aluSecPlcyParamsConfigMatchSrcPortOp = _AluSecPlcyParamsConfigMatchSrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 15),
    _AluSecPlcyParamsConfigMatchSrcPortOp_Type()
)
aluSecPlcyParamsConfigMatchSrcPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchSrcPortOp.setStatus("current")


class _AluSecPlcyParamsConfigMatchDstPortValue1_Type(TTcpUdpPort):
    """Custom type aluSecPlcyParamsConfigMatchDstPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_AluSecPlcyParamsConfigMatchDstPortValue1_Type.__name__ = "TTcpUdpPort"
_AluSecPlcyParamsConfigMatchDstPortValue1_Object = MibTableColumn
aluSecPlcyParamsConfigMatchDstPortValue1 = _AluSecPlcyParamsConfigMatchDstPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 16),
    _AluSecPlcyParamsConfigMatchDstPortValue1_Type()
)
aluSecPlcyParamsConfigMatchDstPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchDstPortValue1.setStatus("current")


class _AluSecPlcyParamsConfigMatchDstPortValue2_Type(TTcpUdpPort):
    """Custom type aluSecPlcyParamsConfigMatchDstPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_AluSecPlcyParamsConfigMatchDstPortValue2_Type.__name__ = "TTcpUdpPort"
_AluSecPlcyParamsConfigMatchDstPortValue2_Object = MibTableColumn
aluSecPlcyParamsConfigMatchDstPortValue2 = _AluSecPlcyParamsConfigMatchDstPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 17),
    _AluSecPlcyParamsConfigMatchDstPortValue2_Type()
)
aluSecPlcyParamsConfigMatchDstPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchDstPortValue2.setStatus("current")


class _AluSecPlcyParamsConfigMatchDstPortOp_Type(TOperator):
    """Custom type aluSecPlcyParamsConfigMatchDstPortOp based on TOperator"""
    defaultValue = 0


_AluSecPlcyParamsConfigMatchDstPortOp_Type.__name__ = "TOperator"
_AluSecPlcyParamsConfigMatchDstPortOp_Object = MibTableColumn
aluSecPlcyParamsConfigMatchDstPortOp = _AluSecPlcyParamsConfigMatchDstPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 18),
    _AluSecPlcyParamsConfigMatchDstPortOp_Type()
)
aluSecPlcyParamsConfigMatchDstPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchDstPortOp.setStatus("current")


class _AluSecPlcyParamsConfigMatchAppGroup_Type(Unsigned32):
    """Custom type aluSecPlcyParamsConfigMatchAppGroup based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSecPlcyParamsConfigMatchAppGroup_Type.__name__ = "Unsigned32"
_AluSecPlcyParamsConfigMatchAppGroup_Object = MibTableColumn
aluSecPlcyParamsConfigMatchAppGroup = _AluSecPlcyParamsConfigMatchAppGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 19),
    _AluSecPlcyParamsConfigMatchAppGroup_Type()
)
aluSecPlcyParamsConfigMatchAppGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchAppGroup.setStatus("current")


class _AluSecPlcyParamsConfigMatchIcmpCode_Type(Integer32):
    """Custom type aluSecPlcyParamsConfigMatchIcmpCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AluSecPlcyParamsConfigMatchIcmpCode_Type.__name__ = "Integer32"
_AluSecPlcyParamsConfigMatchIcmpCode_Object = MibTableColumn
aluSecPlcyParamsConfigMatchIcmpCode = _AluSecPlcyParamsConfigMatchIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 20),
    _AluSecPlcyParamsConfigMatchIcmpCode_Type()
)
aluSecPlcyParamsConfigMatchIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchIcmpCode.setStatus("current")


class _AluSecPlcyParamsConfigMatchIcmpType_Type(Integer32):
    """Custom type aluSecPlcyParamsConfigMatchIcmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AluSecPlcyParamsConfigMatchIcmpType_Type.__name__ = "Integer32"
_AluSecPlcyParamsConfigMatchIcmpType_Object = MibTableColumn
aluSecPlcyParamsConfigMatchIcmpType = _AluSecPlcyParamsConfigMatchIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 21),
    _AluSecPlcyParamsConfigMatchIcmpType_Type()
)
aluSecPlcyParamsConfigMatchIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchIcmpType.setStatus("current")


class _AluSecPlcyParamsConfigMatchIgmpType_Type(Integer32):
    """Custom type aluSecPlcyParamsConfigMatchIgmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AluSecPlcyParamsConfigMatchIgmpType_Type.__name__ = "Integer32"
_AluSecPlcyParamsConfigMatchIgmpType_Object = MibTableColumn
aluSecPlcyParamsConfigMatchIgmpType = _AluSecPlcyParamsConfigMatchIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 22),
    _AluSecPlcyParamsConfigMatchIgmpType_Type()
)
aluSecPlcyParamsConfigMatchIgmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchIgmpType.setStatus("current")


class _AluSecPlcyParamsConfigMatchFlowDirection_Type(Integer32):
    """Custom type aluSecPlcyParamsConfigMatchFlowDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("zoneInbound", 1),
          ("zoneOutbound", 2),
          ("both", 3))
    )


_AluSecPlcyParamsConfigMatchFlowDirection_Type.__name__ = "Integer32"
_AluSecPlcyParamsConfigMatchFlowDirection_Object = MibTableColumn
aluSecPlcyParamsConfigMatchFlowDirection = _AluSecPlcyParamsConfigMatchFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 23),
    _AluSecPlcyParamsConfigMatchFlowDirection_Type()
)
aluSecPlcyParamsConfigMatchFlowDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchFlowDirection.setStatus("current")


class _AluSecPlcyParamsConfigProfileId_Type(Unsigned32):
    """Custom type aluSecPlcyParamsConfigProfileId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSecPlcyParamsConfigProfileId_Type.__name__ = "Unsigned32"
_AluSecPlcyParamsConfigProfileId_Object = MibTableColumn
aluSecPlcyParamsConfigProfileId = _AluSecPlcyParamsConfigProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 24),
    _AluSecPlcyParamsConfigProfileId_Type()
)
aluSecPlcyParamsConfigProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigProfileId.setStatus("current")


class _AluSecPlcyParamsConfigConcurrentFlowLimit_Type(Unsigned32):
    """Custom type aluSecPlcyParamsConfigConcurrentFlowLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSecPlcyParamsConfigConcurrentFlowLimit_Type.__name__ = "Unsigned32"
_AluSecPlcyParamsConfigConcurrentFlowLimit_Object = MibTableColumn
aluSecPlcyParamsConfigConcurrentFlowLimit = _AluSecPlcyParamsConfigConcurrentFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 25),
    _AluSecPlcyParamsConfigConcurrentFlowLimit_Type()
)
aluSecPlcyParamsConfigConcurrentFlowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigConcurrentFlowLimit.setStatus("current")


class _AluSecPlcyParamsConfigCreateRevDirFlow_Type(TruthValue):
    """Custom type aluSecPlcyParamsConfigCreateRevDirFlow based on TruthValue"""
    defaultValue = 1


_AluSecPlcyParamsConfigCreateRevDirFlow_Type.__name__ = "TruthValue"
_AluSecPlcyParamsConfigCreateRevDirFlow_Object = MibTableColumn
aluSecPlcyParamsConfigCreateRevDirFlow = _AluSecPlcyParamsConfigCreateRevDirFlow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 26),
    _AluSecPlcyParamsConfigCreateRevDirFlow_Type()
)
aluSecPlcyParamsConfigCreateRevDirFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigCreateRevDirFlow.setStatus("current")


class _AluSecPlcyParamsConfigAction_Type(Integer32):
    """Custom type aluSecPlcyParamsConfigAction based on Integer32"""
    defaultValue = 3

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
        *(("forward", 0),
          ("drop", 1),
          ("nat", 2),
          ("reject", 3))
    )


_AluSecPlcyParamsConfigAction_Type.__name__ = "Integer32"
_AluSecPlcyParamsConfigAction_Object = MibTableColumn
aluSecPlcyParamsConfigAction = _AluSecPlcyParamsConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 27),
    _AluSecPlcyParamsConfigAction_Type()
)
aluSecPlcyParamsConfigAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigAction.setStatus("current")


class _AluSecPlcyParamsConfigMatchLocal_Type(TruthValue):
    """Custom type aluSecPlcyParamsConfigMatchLocal based on TruthValue"""
    defaultValue = 2


_AluSecPlcyParamsConfigMatchLocal_Type.__name__ = "TruthValue"
_AluSecPlcyParamsConfigMatchLocal_Object = MibTableColumn
aluSecPlcyParamsConfigMatchLocal = _AluSecPlcyParamsConfigMatchLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 28),
    _AluSecPlcyParamsConfigMatchLocal_Type()
)
aluSecPlcyParamsConfigMatchLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigMatchLocal.setStatus("current")


class _AluSecPlcyParamsConfigActionNatDstIPAddr_Type(IpAddress):
    """Custom type aluSecPlcyParamsConfigActionNatDstIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AluSecPlcyParamsConfigActionNatDstIPAddr_Type.__name__ = "IpAddress"
_AluSecPlcyParamsConfigActionNatDstIPAddr_Object = MibTableColumn
aluSecPlcyParamsConfigActionNatDstIPAddr = _AluSecPlcyParamsConfigActionNatDstIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 29),
    _AluSecPlcyParamsConfigActionNatDstIPAddr_Type()
)
aluSecPlcyParamsConfigActionNatDstIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigActionNatDstIPAddr.setStatus("current")


class _AluSecPlcyParamsConfigActionNatDstPort_Type(TTcpUdpPort):
    """Custom type aluSecPlcyParamsConfigActionNatDstPort based on TTcpUdpPort"""
    defaultValue = 0


_AluSecPlcyParamsConfigActionNatDstPort_Type.__name__ = "TTcpUdpPort"
_AluSecPlcyParamsConfigActionNatDstPort_Object = MibTableColumn
aluSecPlcyParamsConfigActionNatDstPort = _AluSecPlcyParamsConfigActionNatDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 30),
    _AluSecPlcyParamsConfigActionNatDstPort_Type()
)
aluSecPlcyParamsConfigActionNatDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigActionNatDstPort.setStatus("current")


class _AluSecPlcyParamsConfigLogControl_Type(Integer32):
    """Custom type aluSecPlcyParamsConfigLogControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suppress", 1),
          ("zone", 2),
          ("log", 3))
    )


_AluSecPlcyParamsConfigLogControl_Type.__name__ = "Integer32"
_AluSecPlcyParamsConfigLogControl_Object = MibTableColumn
aluSecPlcyParamsConfigLogControl = _AluSecPlcyParamsConfigLogControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 31),
    _AluSecPlcyParamsConfigLogControl_Type()
)
aluSecPlcyParamsConfigLogControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigLogControl.setStatus("current")


class _AluSecPlcyParamsConfigLogId_Type(TSecurityLogId):
    """Custom type aluSecPlcyParamsConfigLogId based on TSecurityLogId"""
    defaultValue = 0


_AluSecPlcyParamsConfigLogId_Type.__name__ = "TSecurityLogId"
_AluSecPlcyParamsConfigLogId_Object = MibTableColumn
aluSecPlcyParamsConfigLogId = _AluSecPlcyParamsConfigLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 9, 1, 32),
    _AluSecPlcyParamsConfigLogId_Type()
)
aluSecPlcyParamsConfigLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPlcyParamsConfigLogId.setStatus("current")
_AluSecProfileConfigTable_Object = MibTable
aluSecProfileConfigTable = _AluSecProfileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10)
)
if mibBuilder.loadTexts:
    aluSecProfileConfigTable.setStatus("current")
_AluSecProfileConfigEntry_Object = MibTableRow
aluSecProfileConfigEntry = _AluSecProfileConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1)
)
aluSecProfileConfigEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecProfileConfigId"),
)
if mibBuilder.loadTexts:
    aluSecProfileConfigEntry.setStatus("current")


class _AluSecProfileConfigId_Type(Unsigned32):
    """Custom type aluSecProfileConfigId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecProfileConfigId_Type.__name__ = "Unsigned32"
_AluSecProfileConfigId_Object = MibTableColumn
aluSecProfileConfigId = _AluSecProfileConfigId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 1),
    _AluSecProfileConfigId_Type()
)
aluSecProfileConfigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecProfileConfigId.setStatus("current")
_AluSecProfileConfigRowStatus_Type = RowStatus
_AluSecProfileConfigRowStatus_Object = MibTableColumn
aluSecProfileConfigRowStatus = _AluSecProfileConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 2),
    _AluSecProfileConfigRowStatus_Type()
)
aluSecProfileConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigRowStatus.setStatus("current")


class _AluSecProfileConfigName_Type(TNamedItemOrEmpty):
    """Custom type aluSecProfileConfigName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSecProfileConfigName_Type.__name__ = "TNamedItemOrEmpty"
_AluSecProfileConfigName_Object = MibTableColumn
aluSecProfileConfigName = _AluSecProfileConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 3),
    _AluSecProfileConfigName_Type()
)
aluSecProfileConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigName.setStatus("current")


class _AluSecProfileConfigDescription_Type(TItemDescription):
    """Custom type aluSecProfileConfigDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecProfileConfigDescription_Type.__name__ = "TItemDescription"
_AluSecProfileConfigDescription_Object = MibTableColumn
aluSecProfileConfigDescription = _AluSecProfileConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 4),
    _AluSecProfileConfigDescription_Type()
)
aluSecProfileConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigDescription.setStatus("current")


class _AluSecProfileConfigTcpSynTimeout_Type(Unsigned32):
    """Custom type aluSecProfileConfigTcpSynTimeout based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 86400),
    )


_AluSecProfileConfigTcpSynTimeout_Type.__name__ = "Unsigned32"
_AluSecProfileConfigTcpSynTimeout_Object = MibTableColumn
aluSecProfileConfigTcpSynTimeout = _AluSecProfileConfigTcpSynTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 5),
    _AluSecProfileConfigTcpSynTimeout_Type()
)
aluSecProfileConfigTcpSynTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigTcpSynTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileConfigTcpSynTimeout.setUnits("seconds")


class _AluSecProfileConfigTcpWaitTimeout_Type(Unsigned32):
    """Custom type aluSecProfileConfigTcpWaitTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_AluSecProfileConfigTcpWaitTimeout_Type.__name__ = "Unsigned32"
_AluSecProfileConfigTcpWaitTimeout_Object = MibTableColumn
aluSecProfileConfigTcpWaitTimeout = _AluSecProfileConfigTcpWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 6),
    _AluSecProfileConfigTcpWaitTimeout_Type()
)
aluSecProfileConfigTcpWaitTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigTcpWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileConfigTcpWaitTimeout.setUnits("seconds")


class _AluSecProfileConfigTcpTransTimeout_Type(Unsigned32):
    """Custom type aluSecProfileConfigTcpTransTimeout based on Unsigned32"""
    defaultValue = 240

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_AluSecProfileConfigTcpTransTimeout_Type.__name__ = "Unsigned32"
_AluSecProfileConfigTcpTransTimeout_Object = MibTableColumn
aluSecProfileConfigTcpTransTimeout = _AluSecProfileConfigTcpTransTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 7),
    _AluSecProfileConfigTcpTransTimeout_Type()
)
aluSecProfileConfigTcpTransTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigTcpTransTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileConfigTcpTransTimeout.setUnits("seconds")


class _AluSecProfileConfigTcpEstTimeout_Type(Unsigned32):
    """Custom type aluSecProfileConfigTcpEstTimeout based on Unsigned32"""
    defaultValue = 7440

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_AluSecProfileConfigTcpEstTimeout_Type.__name__ = "Unsigned32"
_AluSecProfileConfigTcpEstTimeout_Object = MibTableColumn
aluSecProfileConfigTcpEstTimeout = _AluSecProfileConfigTcpEstTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 8),
    _AluSecProfileConfigTcpEstTimeout_Type()
)
aluSecProfileConfigTcpEstTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigTcpEstTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileConfigTcpEstTimeout.setUnits("seconds")


class _AluSecProfileConfigUdpTimeout_Type(Unsigned32):
    """Custom type aluSecProfileConfigUdpTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_AluSecProfileConfigUdpTimeout_Type.__name__ = "Unsigned32"
_AluSecProfileConfigUdpTimeout_Object = MibTableColumn
aluSecProfileConfigUdpTimeout = _AluSecProfileConfigUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 9),
    _AluSecProfileConfigUdpTimeout_Type()
)
aluSecProfileConfigUdpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigUdpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileConfigUdpTimeout.setUnits("seconds")


class _AluSecProfileConfigUdpInitTimeout_Type(Unsigned32):
    """Custom type aluSecProfileConfigUdpInitTimeout based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_AluSecProfileConfigUdpInitTimeout_Type.__name__ = "Unsigned32"
_AluSecProfileConfigUdpInitTimeout_Object = MibTableColumn
aluSecProfileConfigUdpInitTimeout = _AluSecProfileConfigUdpInitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 10),
    _AluSecProfileConfigUdpInitTimeout_Type()
)
aluSecProfileConfigUdpInitTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigUdpInitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileConfigUdpInitTimeout.setUnits("seconds")


class _AluSecProfileConfigUdpDnsTimeout_Type(Unsigned32):
    """Custom type aluSecProfileConfigUdpDnsTimeout based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_AluSecProfileConfigUdpDnsTimeout_Type.__name__ = "Unsigned32"
_AluSecProfileConfigUdpDnsTimeout_Object = MibTableColumn
aluSecProfileConfigUdpDnsTimeout = _AluSecProfileConfigUdpDnsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 11),
    _AluSecProfileConfigUdpDnsTimeout_Type()
)
aluSecProfileConfigUdpDnsTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigUdpDnsTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileConfigUdpDnsTimeout.setUnits("seconds")


class _AluSecProfileConfigIcmpTimeout_Type(Unsigned32):
    """Custom type aluSecProfileConfigIcmpTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 240),
    )


_AluSecProfileConfigIcmpTimeout_Type.__name__ = "Unsigned32"
_AluSecProfileConfigIcmpTimeout_Object = MibTableColumn
aluSecProfileConfigIcmpTimeout = _AluSecProfileConfigIcmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 12),
    _AluSecProfileConfigIcmpTimeout_Type()
)
aluSecProfileConfigIcmpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigIcmpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileConfigIcmpTimeout.setUnits("seconds")


class _AluSecProfileConfigOtherTimeout_Type(Unsigned32):
    """Custom type aluSecProfileConfigOtherTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_AluSecProfileConfigOtherTimeout_Type.__name__ = "Unsigned32"
_AluSecProfileConfigOtherTimeout_Object = MibTableColumn
aluSecProfileConfigOtherTimeout = _AluSecProfileConfigOtherTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 13),
    _AluSecProfileConfigOtherTimeout_Type()
)
aluSecProfileConfigOtherTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigOtherTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileConfigOtherTimeout.setUnits("seconds")


class _AluSecProfileConfigAppInspect_Type(TruthValue):
    """Custom type aluSecProfileConfigAppInspect based on TruthValue"""
    defaultValue = 2


_AluSecProfileConfigAppInspect_Type.__name__ = "TruthValue"
_AluSecProfileConfigAppInspect_Object = MibTableColumn
aluSecProfileConfigAppInspect = _AluSecProfileConfigAppInspect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 14),
    _AluSecProfileConfigAppInspect_Type()
)
aluSecProfileConfigAppInspect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigAppInspect.setStatus("current")


class _AluSecProfileConfigInspectTcp_Type(TruthValue):
    """Custom type aluSecProfileConfigInspectTcp based on TruthValue"""
    defaultValue = 2


_AluSecProfileConfigInspectTcp_Type.__name__ = "TruthValue"
_AluSecProfileConfigInspectTcp_Object = MibTableColumn
aluSecProfileConfigInspectTcp = _AluSecProfileConfigInspectTcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 15),
    _AluSecProfileConfigInspectTcp_Type()
)
aluSecProfileConfigInspectTcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigInspectTcp.setStatus("current")


class _AluSecProfileConfigInspectIpOpt_Type(TruthValue):
    """Custom type aluSecProfileConfigInspectIpOpt based on TruthValue"""
    defaultValue = 2


_AluSecProfileConfigInspectIpOpt_Type.__name__ = "TruthValue"
_AluSecProfileConfigInspectIpOpt_Object = MibTableColumn
aluSecProfileConfigInspectIpOpt = _AluSecProfileConfigInspectIpOpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 16),
    _AluSecProfileConfigInspectIpOpt_Type()
)
aluSecProfileConfigInspectIpOpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigInspectIpOpt.setStatus("current")
_AluSecProfileConfigAllowedIpOpt_Type = Unsigned32
_AluSecProfileConfigAllowedIpOpt_Object = MibTableColumn
aluSecProfileConfigAllowedIpOpt = _AluSecProfileConfigAllowedIpOpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 17),
    _AluSecProfileConfigAllowedIpOpt_Type()
)
aluSecProfileConfigAllowedIpOpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigAllowedIpOpt.setStatus("current")


class _AluSecProfileConfigAllowPktFrag_Type(TruthValue):
    """Custom type aluSecProfileConfigAllowPktFrag based on TruthValue"""
    defaultValue = 1


_AluSecProfileConfigAllowPktFrag_Type.__name__ = "TruthValue"
_AluSecProfileConfigAllowPktFrag_Object = MibTableColumn
aluSecProfileConfigAllowPktFrag = _AluSecProfileConfigAllowPktFrag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 18),
    _AluSecProfileConfigAllowPktFrag_Type()
)
aluSecProfileConfigAllowPktFrag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigAllowPktFrag.setStatus("current")


class _AluSecProfileConfigAlg_Type(TAlgType):
    """Custom type aluSecProfileConfigAlg based on TAlgType"""
    defaultValue = 1


_AluSecProfileConfigAlg_Type.__name__ = "TAlgType"
_AluSecProfileConfigAlg_Object = MibTableColumn
aluSecProfileConfigAlg = _AluSecProfileConfigAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 19),
    _AluSecProfileConfigAlg_Type()
)
aluSecProfileConfigAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigAlg.setStatus("current")


class _AluSecProfileConfigIcmpReqLimit_Type(Unsigned32):
    """Custom type aluSecProfileConfigIcmpReqLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_AluSecProfileConfigIcmpReqLimit_Type.__name__ = "Unsigned32"
_AluSecProfileConfigIcmpReqLimit_Object = MibTableColumn
aluSecProfileConfigIcmpReqLimit = _AluSecProfileConfigIcmpReqLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 20),
    _AluSecProfileConfigIcmpReqLimit_Type()
)
aluSecProfileConfigIcmpReqLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigIcmpReqLimit.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileConfigIcmpReqLimit.setUnits("packets")


class _AluSecProfileConfigIcmpErrLimit_Type(TruthValue):
    """Custom type aluSecProfileConfigIcmpErrLimit based on TruthValue"""
    defaultValue = 2


_AluSecProfileConfigIcmpErrLimit_Type.__name__ = "TruthValue"
_AluSecProfileConfigIcmpErrLimit_Object = MibTableColumn
aluSecProfileConfigIcmpErrLimit = _AluSecProfileConfigIcmpErrLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 21),
    _AluSecProfileConfigIcmpErrLimit_Type()
)
aluSecProfileConfigIcmpErrLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigIcmpErrLimit.setStatus("current")


class _AluSecProfileConfigDnsReplyOnly_Type(TruthValue):
    """Custom type aluSecProfileConfigDnsReplyOnly based on TruthValue"""
    defaultValue = 2


_AluSecProfileConfigDnsReplyOnly_Type.__name__ = "TruthValue"
_AluSecProfileConfigDnsReplyOnly_Object = MibTableColumn
aluSecProfileConfigDnsReplyOnly = _AluSecProfileConfigDnsReplyOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 22),
    _AluSecProfileConfigDnsReplyOnly_Type()
)
aluSecProfileConfigDnsReplyOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigDnsReplyOnly.setStatus("current")


class _AluSecProfileConfigTcpTmoStrict_Type(TruthValue):
    """Custom type aluSecProfileConfigTcpTmoStrict based on TruthValue"""
    defaultValue = 2


_AluSecProfileConfigTcpTmoStrict_Type.__name__ = "TruthValue"
_AluSecProfileConfigTcpTmoStrict_Object = MibTableColumn
aluSecProfileConfigTcpTmoStrict = _AluSecProfileConfigTcpTmoStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 23),
    _AluSecProfileConfigTcpTmoStrict_Type()
)
aluSecProfileConfigTcpTmoStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigTcpTmoStrict.setStatus("current")


class _AluSecProfileConfigUdpTmoStrict_Type(TruthValue):
    """Custom type aluSecProfileConfigUdpTmoStrict based on TruthValue"""
    defaultValue = 2


_AluSecProfileConfigUdpTmoStrict_Type.__name__ = "TruthValue"
_AluSecProfileConfigUdpTmoStrict_Object = MibTableColumn
aluSecProfileConfigUdpTmoStrict = _AluSecProfileConfigUdpTmoStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 24),
    _AluSecProfileConfigUdpTmoStrict_Type()
)
aluSecProfileConfigUdpTmoStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigUdpTmoStrict.setStatus("current")


class _AluSecProfileConfigIcmpTmoStrict_Type(TruthValue):
    """Custom type aluSecProfileConfigIcmpTmoStrict based on TruthValue"""
    defaultValue = 1


_AluSecProfileConfigIcmpTmoStrict_Type.__name__ = "TruthValue"
_AluSecProfileConfigIcmpTmoStrict_Object = MibTableColumn
aluSecProfileConfigIcmpTmoStrict = _AluSecProfileConfigIcmpTmoStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 25),
    _AluSecProfileConfigIcmpTmoStrict_Type()
)
aluSecProfileConfigIcmpTmoStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigIcmpTmoStrict.setStatus("current")


class _AluSecProfileConfigDnsTmoStrict_Type(TruthValue):
    """Custom type aluSecProfileConfigDnsTmoStrict based on TruthValue"""
    defaultValue = 1


_AluSecProfileConfigDnsTmoStrict_Type.__name__ = "TruthValue"
_AluSecProfileConfigDnsTmoStrict_Object = MibTableColumn
aluSecProfileConfigDnsTmoStrict = _AluSecProfileConfigDnsTmoStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 26),
    _AluSecProfileConfigDnsTmoStrict_Type()
)
aluSecProfileConfigDnsTmoStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigDnsTmoStrict.setStatus("current")


class _AluSecProfileConfigOthTmoStrict_Type(TruthValue):
    """Custom type aluSecProfileConfigOthTmoStrict based on TruthValue"""
    defaultValue = 2


_AluSecProfileConfigOthTmoStrict_Type.__name__ = "TruthValue"
_AluSecProfileConfigOthTmoStrict_Object = MibTableColumn
aluSecProfileConfigOthTmoStrict = _AluSecProfileConfigOthTmoStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 27),
    _AluSecProfileConfigOthTmoStrict_Type()
)
aluSecProfileConfigOthTmoStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigOthTmoStrict.setStatus("current")


class _AluSecProfileConfigFwdPolicerId_Type(TSecurityPolicerId):
    """Custom type aluSecProfileConfigFwdPolicerId based on TSecurityPolicerId"""
    defaultValue = 0


_AluSecProfileConfigFwdPolicerId_Type.__name__ = "TSecurityPolicerId"
_AluSecProfileConfigFwdPolicerId_Object = MibTableColumn
aluSecProfileConfigFwdPolicerId = _AluSecProfileConfigFwdPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 28),
    _AluSecProfileConfigFwdPolicerId_Type()
)
aluSecProfileConfigFwdPolicerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigFwdPolicerId.setStatus("current")


class _AluSecProfileConfigRevPolicerId_Type(TSecurityPolicerId):
    """Custom type aluSecProfileConfigRevPolicerId based on TSecurityPolicerId"""
    defaultValue = 0


_AluSecProfileConfigRevPolicerId_Type.__name__ = "TSecurityPolicerId"
_AluSecProfileConfigRevPolicerId_Object = MibTableColumn
aluSecProfileConfigRevPolicerId = _AluSecProfileConfigRevPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 10, 1, 29),
    _AluSecProfileConfigRevPolicerId_Type()
)
aluSecProfileConfigRevPolicerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecProfileConfigRevPolicerId.setStatus("current")
_AluSecPlcyLastCommit_Type = TimeStamp
_AluSecPlcyLastCommit_Object = MibScalar
aluSecPlcyLastCommit = _AluSecPlcyLastCommit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 11),
    _AluSecPlcyLastCommit_Type()
)
aluSecPlcyLastCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyLastCommit.setStatus("current")
_AluSecPlcyCount_Type = Unsigned32
_AluSecPlcyCount_Object = MibScalar
aluSecPlcyCount = _AluSecPlcyCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 12),
    _AluSecPlcyCount_Type()
)
aluSecPlcyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyCount.setStatus("current")
_AluSecPlcyProfileCount_Type = Unsigned32
_AluSecPlcyProfileCount_Object = MibScalar
aluSecPlcyProfileCount = _AluSecPlcyProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 13),
    _AluSecPlcyProfileCount_Type()
)
aluSecPlcyProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyProfileCount.setStatus("current")
_AluSecPlcyZoneCount_Type = Unsigned32
_AluSecPlcyZoneCount_Object = MibScalar
aluSecPlcyZoneCount = _AluSecPlcyZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 14),
    _AluSecPlcyZoneCount_Type()
)
aluSecPlcyZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyZoneCount.setStatus("current")
_AluSecActiveSessionCount_Type = Unsigned32
_AluSecActiveSessionCount_Object = MibScalar
aluSecActiveSessionCount = _AluSecActiveSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 15),
    _AluSecActiveSessionCount_Type()
)
aluSecActiveSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecActiveSessionCount.setStatus("current")
_AluSecActiveSessionLimit_Type = Unsigned32
_AluSecActiveSessionLimit_Object = MibScalar
aluSecActiveSessionLimit = _AluSecActiveSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 16),
    _AluSecActiveSessionLimit_Type()
)
aluSecActiveSessionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecActiveSessionLimit.setStatus("current")


class _AluSecActiveSessionHiWtrMrk_Type(Unsigned32):
    """Custom type aluSecActiveSessionHiWtrMrk based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSecActiveSessionHiWtrMrk_Type.__name__ = "Unsigned32"
_AluSecActiveSessionHiWtrMrk_Object = MibScalar
aluSecActiveSessionHiWtrMrk = _AluSecActiveSessionHiWtrMrk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 17),
    _AluSecActiveSessionHiWtrMrk_Type()
)
aluSecActiveSessionHiWtrMrk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecActiveSessionHiWtrMrk.setStatus("current")


class _AluSecActiveSessionLoWtrMrk_Type(Unsigned32):
    """Custom type aluSecActiveSessionLoWtrMrk based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSecActiveSessionLoWtrMrk_Type.__name__ = "Unsigned32"
_AluSecActiveSessionLoWtrMrk_Object = MibScalar
aluSecActiveSessionLoWtrMrk = _AluSecActiveSessionLoWtrMrk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 18),
    _AluSecActiveSessionLoWtrMrk_Type()
)
aluSecActiveSessionLoWtrMrk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecActiveSessionLoWtrMrk.setStatus("current")
_AluSecPlcyState_Type = TPlcyState
_AluSecPlcyState_Object = MibScalar
aluSecPlcyState = _AluSecPlcyState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 19),
    _AluSecPlcyState_Type()
)
aluSecPlcyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyState.setStatus("current")


class _AluSecSessionResourceState_Type(Integer32):
    """Custom type aluSecSessionResourceState based on Integer32"""
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
          ("ok", 1),
          ("alarm", 2))
    )


_AluSecSessionResourceState_Type.__name__ = "Integer32"
_AluSecSessionResourceState_Object = MibScalar
aluSecSessionResourceState = _AluSecSessionResourceState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 20),
    _AluSecSessionResourceState_Type()
)
aluSecSessionResourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionResourceState.setStatus("current")
_AluSecHostGrpConfigTable_Object = MibTable
aluSecHostGrpConfigTable = _AluSecHostGrpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 21)
)
if mibBuilder.loadTexts:
    aluSecHostGrpConfigTable.setStatus("current")
_AluSecHostGrpConfigEntry_Object = MibTableRow
aluSecHostGrpConfigEntry = _AluSecHostGrpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 21, 1)
)
aluSecHostGrpConfigEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecHostGrpConfigId"),
)
if mibBuilder.loadTexts:
    aluSecHostGrpConfigEntry.setStatus("current")


class _AluSecHostGrpConfigId_Type(Unsigned32):
    """Custom type aluSecHostGrpConfigId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AluSecHostGrpConfigId_Type.__name__ = "Unsigned32"
_AluSecHostGrpConfigId_Object = MibTableColumn
aluSecHostGrpConfigId = _AluSecHostGrpConfigId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 21, 1, 1),
    _AluSecHostGrpConfigId_Type()
)
aluSecHostGrpConfigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecHostGrpConfigId.setStatus("current")
_AluSecHostGrpConfigRowStatus_Type = RowStatus
_AluSecHostGrpConfigRowStatus_Object = MibTableColumn
aluSecHostGrpConfigRowStatus = _AluSecHostGrpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 21, 1, 2),
    _AluSecHostGrpConfigRowStatus_Type()
)
aluSecHostGrpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecHostGrpConfigRowStatus.setStatus("current")


class _AluSecHostGrpConfigName_Type(TNamedItemOrEmpty):
    """Custom type aluSecHostGrpConfigName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSecHostGrpConfigName_Type.__name__ = "TNamedItemOrEmpty"
_AluSecHostGrpConfigName_Object = MibTableColumn
aluSecHostGrpConfigName = _AluSecHostGrpConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 21, 1, 3),
    _AluSecHostGrpConfigName_Type()
)
aluSecHostGrpConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecHostGrpConfigName.setStatus("current")


class _AluSecHostGrpConfigDescription_Type(TItemDescription):
    """Custom type aluSecHostGrpConfigDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecHostGrpConfigDescription_Type.__name__ = "TItemDescription"
_AluSecHostGrpConfigDescription_Object = MibTableColumn
aluSecHostGrpConfigDescription = _AluSecHostGrpConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 21, 1, 4),
    _AluSecHostGrpConfigDescription_Type()
)
aluSecHostGrpConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecHostGrpConfigDescription.setStatus("current")
_AluSecHostConfigTable_Object = MibTable
aluSecHostConfigTable = _AluSecHostConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 22)
)
if mibBuilder.loadTexts:
    aluSecHostConfigTable.setStatus("current")
_AluSecHostConfigEntry_Object = MibTableRow
aluSecHostConfigEntry = _AluSecHostConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 22, 1)
)
aluSecHostConfigEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecHostGrpConfigId"),
    (0, "ALU-SECURITY-MIB", "aluSecHostConfigIPAddrValue1"),
)
if mibBuilder.loadTexts:
    aluSecHostConfigEntry.setStatus("current")
_AluSecHostConfigIPAddrValue1_Type = IpAddress
_AluSecHostConfigIPAddrValue1_Object = MibTableColumn
aluSecHostConfigIPAddrValue1 = _AluSecHostConfigIPAddrValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 22, 1, 1),
    _AluSecHostConfigIPAddrValue1_Type()
)
aluSecHostConfigIPAddrValue1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecHostConfigIPAddrValue1.setStatus("current")
_AluSecHostConfigRowStatus_Type = RowStatus
_AluSecHostConfigRowStatus_Object = MibTableColumn
aluSecHostConfigRowStatus = _AluSecHostConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 22, 1, 2),
    _AluSecHostConfigRowStatus_Type()
)
aluSecHostConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecHostConfigRowStatus.setStatus("current")


class _AluSecHostConfigIPAddrValue2_Type(IpAddress):
    """Custom type aluSecHostConfigIPAddrValue2 based on IpAddress"""
    defaultHexValue = "00000000"


_AluSecHostConfigIPAddrValue2_Type.__name__ = "IpAddress"
_AluSecHostConfigIPAddrValue2_Object = MibTableColumn
aluSecHostConfigIPAddrValue2 = _AluSecHostConfigIPAddrValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 22, 1, 3),
    _AluSecHostConfigIPAddrValue2_Type()
)
aluSecHostConfigIPAddrValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecHostConfigIPAddrValue2.setStatus("current")


class _AluSecHostConfigIPOperator_Type(TIPOperator):
    """Custom type aluSecHostConfigIPOperator based on TIPOperator"""
    defaultValue = 0


_AluSecHostConfigIPOperator_Type.__name__ = "TIPOperator"
_AluSecHostConfigIPOperator_Object = MibTableColumn
aluSecHostConfigIPOperator = _AluSecHostConfigIPOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 22, 1, 4),
    _AluSecHostConfigIPOperator_Type()
)
aluSecHostConfigIPOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecHostConfigIPOperator.setStatus("current")
_AluSecAppGrpConfigTable_Object = MibTable
aluSecAppGrpConfigTable = _AluSecAppGrpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 23)
)
if mibBuilder.loadTexts:
    aluSecAppGrpConfigTable.setStatus("current")
_AluSecAppGrpConfigEntry_Object = MibTableRow
aluSecAppGrpConfigEntry = _AluSecAppGrpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 23, 1)
)
aluSecAppGrpConfigEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecAppGrpConfigId"),
)
if mibBuilder.loadTexts:
    aluSecAppGrpConfigEntry.setStatus("current")


class _AluSecAppGrpConfigId_Type(Unsigned32):
    """Custom type aluSecAppGrpConfigId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AluSecAppGrpConfigId_Type.__name__ = "Unsigned32"
_AluSecAppGrpConfigId_Object = MibTableColumn
aluSecAppGrpConfigId = _AluSecAppGrpConfigId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 23, 1, 1),
    _AluSecAppGrpConfigId_Type()
)
aluSecAppGrpConfigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecAppGrpConfigId.setStatus("current")
_AluSecAppGrpConfigRowStatus_Type = RowStatus
_AluSecAppGrpConfigRowStatus_Object = MibTableColumn
aluSecAppGrpConfigRowStatus = _AluSecAppGrpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 23, 1, 2),
    _AluSecAppGrpConfigRowStatus_Type()
)
aluSecAppGrpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppGrpConfigRowStatus.setStatus("current")


class _AluSecAppGrpConfigName_Type(TNamedItemOrEmpty):
    """Custom type aluSecAppGrpConfigName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSecAppGrpConfigName_Type.__name__ = "TNamedItemOrEmpty"
_AluSecAppGrpConfigName_Object = MibTableColumn
aluSecAppGrpConfigName = _AluSecAppGrpConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 23, 1, 3),
    _AluSecAppGrpConfigName_Type()
)
aluSecAppGrpConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppGrpConfigName.setStatus("current")


class _AluSecAppGrpConfigDescription_Type(TItemDescription):
    """Custom type aluSecAppGrpConfigDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecAppGrpConfigDescription_Type.__name__ = "TItemDescription"
_AluSecAppGrpConfigDescription_Object = MibTableColumn
aluSecAppGrpConfigDescription = _AluSecAppGrpConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 23, 1, 4),
    _AluSecAppGrpConfigDescription_Type()
)
aluSecAppGrpConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppGrpConfigDescription.setStatus("current")
_AluSecAppConfigTable_Object = MibTable
aluSecAppConfigTable = _AluSecAppConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24)
)
if mibBuilder.loadTexts:
    aluSecAppConfigTable.setStatus("current")
_AluSecAppConfigEntry_Object = MibTableRow
aluSecAppConfigEntry = _AluSecAppConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24, 1)
)
aluSecAppConfigEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecAppGrpConfigId"),
    (0, "ALU-SECURITY-MIB", "aluSecAppConfigEntryId"),
)
if mibBuilder.loadTexts:
    aluSecAppConfigEntry.setStatus("current")


class _AluSecAppConfigEntryId_Type(Unsigned32):
    """Custom type aluSecAppConfigEntryId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecAppConfigEntryId_Type.__name__ = "Unsigned32"
_AluSecAppConfigEntryId_Object = MibTableColumn
aluSecAppConfigEntryId = _AluSecAppConfigEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24, 1, 1),
    _AluSecAppConfigEntryId_Type()
)
aluSecAppConfigEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecAppConfigEntryId.setStatus("current")
_AluSecAppConfigRowStatus_Type = RowStatus
_AluSecAppConfigRowStatus_Object = MibTableColumn
aluSecAppConfigRowStatus = _AluSecAppConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24, 1, 2),
    _AluSecAppConfigRowStatus_Type()
)
aluSecAppConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppConfigRowStatus.setStatus("current")


class _AluSecAppConfigMatchProtocol_Type(TIpProtocol):
    """Custom type aluSecAppConfigMatchProtocol based on TIpProtocol"""
    defaultValue = -1


_AluSecAppConfigMatchProtocol_Type.__name__ = "TIpProtocol"
_AluSecAppConfigMatchProtocol_Object = MibTableColumn
aluSecAppConfigMatchProtocol = _AluSecAppConfigMatchProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24, 1, 3),
    _AluSecAppConfigMatchProtocol_Type()
)
aluSecAppConfigMatchProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppConfigMatchProtocol.setStatus("current")


class _AluSecAppConfigMatchSrcPortValue1_Type(TTcpUdpPort):
    """Custom type aluSecAppConfigMatchSrcPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_AluSecAppConfigMatchSrcPortValue1_Type.__name__ = "TTcpUdpPort"
_AluSecAppConfigMatchSrcPortValue1_Object = MibTableColumn
aluSecAppConfigMatchSrcPortValue1 = _AluSecAppConfigMatchSrcPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24, 1, 4),
    _AluSecAppConfigMatchSrcPortValue1_Type()
)
aluSecAppConfigMatchSrcPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppConfigMatchSrcPortValue1.setStatus("current")


class _AluSecAppConfigMatchSrcPortValue2_Type(TTcpUdpPort):
    """Custom type aluSecAppConfigMatchSrcPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_AluSecAppConfigMatchSrcPortValue2_Type.__name__ = "TTcpUdpPort"
_AluSecAppConfigMatchSrcPortValue2_Object = MibTableColumn
aluSecAppConfigMatchSrcPortValue2 = _AluSecAppConfigMatchSrcPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24, 1, 5),
    _AluSecAppConfigMatchSrcPortValue2_Type()
)
aluSecAppConfigMatchSrcPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppConfigMatchSrcPortValue2.setStatus("current")


class _AluSecAppConfigMatchSrcPortOp_Type(TOperator):
    """Custom type aluSecAppConfigMatchSrcPortOp based on TOperator"""
    defaultValue = 0


_AluSecAppConfigMatchSrcPortOp_Type.__name__ = "TOperator"
_AluSecAppConfigMatchSrcPortOp_Object = MibTableColumn
aluSecAppConfigMatchSrcPortOp = _AluSecAppConfigMatchSrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24, 1, 6),
    _AluSecAppConfigMatchSrcPortOp_Type()
)
aluSecAppConfigMatchSrcPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppConfigMatchSrcPortOp.setStatus("current")


class _AluSecAppConfigMatchDstPortValue1_Type(TTcpUdpPort):
    """Custom type aluSecAppConfigMatchDstPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_AluSecAppConfigMatchDstPortValue1_Type.__name__ = "TTcpUdpPort"
_AluSecAppConfigMatchDstPortValue1_Object = MibTableColumn
aluSecAppConfigMatchDstPortValue1 = _AluSecAppConfigMatchDstPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24, 1, 7),
    _AluSecAppConfigMatchDstPortValue1_Type()
)
aluSecAppConfigMatchDstPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppConfigMatchDstPortValue1.setStatus("current")


class _AluSecAppConfigMatchDstPortValue2_Type(TTcpUdpPort):
    """Custom type aluSecAppConfigMatchDstPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_AluSecAppConfigMatchDstPortValue2_Type.__name__ = "TTcpUdpPort"
_AluSecAppConfigMatchDstPortValue2_Object = MibTableColumn
aluSecAppConfigMatchDstPortValue2 = _AluSecAppConfigMatchDstPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24, 1, 8),
    _AluSecAppConfigMatchDstPortValue2_Type()
)
aluSecAppConfigMatchDstPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppConfigMatchDstPortValue2.setStatus("current")


class _AluSecAppConfigMatchDstPortOp_Type(TOperator):
    """Custom type aluSecAppConfigMatchDstPortOp based on TOperator"""
    defaultValue = 0


_AluSecAppConfigMatchDstPortOp_Type.__name__ = "TOperator"
_AluSecAppConfigMatchDstPortOp_Object = MibTableColumn
aluSecAppConfigMatchDstPortOp = _AluSecAppConfigMatchDstPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24, 1, 9),
    _AluSecAppConfigMatchDstPortOp_Type()
)
aluSecAppConfigMatchDstPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppConfigMatchDstPortOp.setStatus("current")


class _AluSecAppConfigMatchIcmpCode_Type(Integer32):
    """Custom type aluSecAppConfigMatchIcmpCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AluSecAppConfigMatchIcmpCode_Type.__name__ = "Integer32"
_AluSecAppConfigMatchIcmpCode_Object = MibTableColumn
aluSecAppConfigMatchIcmpCode = _AluSecAppConfigMatchIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24, 1, 10),
    _AluSecAppConfigMatchIcmpCode_Type()
)
aluSecAppConfigMatchIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppConfigMatchIcmpCode.setStatus("current")


class _AluSecAppConfigMatchIcmpType_Type(Integer32):
    """Custom type aluSecAppConfigMatchIcmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AluSecAppConfigMatchIcmpType_Type.__name__ = "Integer32"
_AluSecAppConfigMatchIcmpType_Object = MibTableColumn
aluSecAppConfigMatchIcmpType = _AluSecAppConfigMatchIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 24, 1, 11),
    _AluSecAppConfigMatchIcmpType_Type()
)
aluSecAppConfigMatchIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecAppConfigMatchIcmpType.setStatus("current")
_AluSecPolicerGrpConfigTable_Object = MibTable
aluSecPolicerGrpConfigTable = _AluSecPolicerGrpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 25)
)
if mibBuilder.loadTexts:
    aluSecPolicerGrpConfigTable.setStatus("current")
_AluSecPolicerGrpConfigEntry_Object = MibTableRow
aluSecPolicerGrpConfigEntry = _AluSecPolicerGrpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 25, 1)
)
aluSecPolicerGrpConfigEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecPolicerGrpConfigId"),
)
if mibBuilder.loadTexts:
    aluSecPolicerGrpConfigEntry.setStatus("current")


class _AluSecPolicerGrpConfigId_Type(Unsigned32):
    """Custom type aluSecPolicerGrpConfigId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_AluSecPolicerGrpConfigId_Type.__name__ = "Unsigned32"
_AluSecPolicerGrpConfigId_Object = MibTableColumn
aluSecPolicerGrpConfigId = _AluSecPolicerGrpConfigId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 25, 1, 1),
    _AluSecPolicerGrpConfigId_Type()
)
aluSecPolicerGrpConfigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecPolicerGrpConfigId.setStatus("current")
_AluSecPolicerGrpConfigRowStatus_Type = RowStatus
_AluSecPolicerGrpConfigRowStatus_Object = MibTableColumn
aluSecPolicerGrpConfigRowStatus = _AluSecPolicerGrpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 25, 1, 2),
    _AluSecPolicerGrpConfigRowStatus_Type()
)
aluSecPolicerGrpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPolicerGrpConfigRowStatus.setStatus("current")


class _AluSecPolicerGrpConfigName_Type(TNamedItemOrEmpty):
    """Custom type aluSecPolicerGrpConfigName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSecPolicerGrpConfigName_Type.__name__ = "TNamedItemOrEmpty"
_AluSecPolicerGrpConfigName_Object = MibTableColumn
aluSecPolicerGrpConfigName = _AluSecPolicerGrpConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 25, 1, 3),
    _AluSecPolicerGrpConfigName_Type()
)
aluSecPolicerGrpConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPolicerGrpConfigName.setStatus("current")


class _AluSecPolicerGrpConfigDescription_Type(TItemDescription):
    """Custom type aluSecPolicerGrpConfigDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecPolicerGrpConfigDescription_Type.__name__ = "TItemDescription"
_AluSecPolicerGrpConfigDescription_Object = MibTableColumn
aluSecPolicerGrpConfigDescription = _AluSecPolicerGrpConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 25, 1, 4),
    _AluSecPolicerGrpConfigDescription_Type()
)
aluSecPolicerGrpConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPolicerGrpConfigDescription.setStatus("current")


class _AluSecPolicerGrpConfigRate_Type(Integer32):
    """Custom type aluSecPolicerGrpConfigRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000),
    )


_AluSecPolicerGrpConfigRate_Type.__name__ = "Integer32"
_AluSecPolicerGrpConfigRate_Object = MibTableColumn
aluSecPolicerGrpConfigRate = _AluSecPolicerGrpConfigRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 25, 1, 14),
    _AluSecPolicerGrpConfigRate_Type()
)
aluSecPolicerGrpConfigRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPolicerGrpConfigRate.setStatus("current")
if mibBuilder.loadTexts:
    aluSecPolicerGrpConfigRate.setUnits("mega-bits per second")


class _AluSecPolicerGrpConfigRateCbs_Type(Unsigned32):
    """Custom type aluSecPolicerGrpConfigRateCbs based on Unsigned32"""
    defaultValue = 130816

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 130816),
    )


_AluSecPolicerGrpConfigRateCbs_Type.__name__ = "Unsigned32"
_AluSecPolicerGrpConfigRateCbs_Object = MibTableColumn
aluSecPolicerGrpConfigRateCbs = _AluSecPolicerGrpConfigRateCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 25, 1, 17),
    _AluSecPolicerGrpConfigRateCbs_Type()
)
aluSecPolicerGrpConfigRateCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecPolicerGrpConfigRateCbs.setStatus("current")
if mibBuilder.loadTexts:
    aluSecPolicerGrpConfigRateCbs.setUnits("bytes")
_AluSecTotalSessionCount_Type = Counter64
_AluSecTotalSessionCount_Object = MibScalar
aluSecTotalSessionCount = _AluSecTotalSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 1, 26),
    _AluSecTotalSessionCount_Type()
)
aluSecTotalSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecTotalSessionCount.setStatus("current")
_AluSecurityOperObjs_ObjectIdentity = ObjectIdentity
aluSecurityOperObjs = _AluSecurityOperObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2)
)
_AluZoneOperTable_Object = MibTable
aluZoneOperTable = _AluZoneOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1)
)
if mibBuilder.loadTexts:
    aluZoneOperTable.setStatus("current")
_AluZoneOperEntry_Object = MibTableRow
aluZoneOperEntry = _AluZoneOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1)
)
aluZoneOperEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluZoneOperId"),
)
if mibBuilder.loadTexts:
    aluZoneOperEntry.setStatus("current")


class _AluZoneOperId_Type(Unsigned32):
    """Custom type aluZoneOperId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZoneOperId_Type.__name__ = "Unsigned32"
_AluZoneOperId_Object = MibTableColumn
aluZoneOperId = _AluZoneOperId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 1),
    _AluZoneOperId_Type()
)
aluZoneOperId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluZoneOperId.setStatus("current")
_AluZoneOperName_Type = TNamedItemOrEmpty
_AluZoneOperName_Object = MibTableColumn
aluZoneOperName = _AluZoneOperName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 2),
    _AluZoneOperName_Type()
)
aluZoneOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperName.setStatus("current")
_AluZoneOperBypass_Type = TruthValue
_AluZoneOperBypass_Object = MibTableColumn
aluZoneOperBypass = _AluZoneOperBypass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 3),
    _AluZoneOperBypass_Type()
)
aluZoneOperBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperBypass.setStatus("current")
_AluZoneOperDescription_Type = TItemDescription
_AluZoneOperDescription_Object = MibTableColumn
aluZoneOperDescription = _AluZoneOperDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 4),
    _AluZoneOperDescription_Type()
)
aluZoneOperDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperDescription.setStatus("current")
_AluZoneOperPlcyRuleCount_Type = Gauge32
_AluZoneOperPlcyRuleCount_Object = MibTableColumn
aluZoneOperPlcyRuleCount = _AluZoneOperPlcyRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 5),
    _AluZoneOperPlcyRuleCount_Type()
)
aluZoneOperPlcyRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperPlcyRuleCount.setStatus("current")
_AluZoneOperType_Type = TZoneType
_AluZoneOperType_Object = MibTableColumn
aluZoneOperType = _AluZoneOperType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 6),
    _AluZoneOperType_Type()
)
aluZoneOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperType.setStatus("current")
_AluZoneOperSvcId_Type = TmnxServId
_AluZoneOperSvcId_Object = MibTableColumn
aluZoneOperSvcId = _AluZoneOperSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 7),
    _AluZoneOperSvcId_Type()
)
aluZoneOperSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperSvcId.setStatus("current")
_AluZoneOperInSessionCount_Type = Counter64
_AluZoneOperInSessionCount_Object = MibTableColumn
aluZoneOperInSessionCount = _AluZoneOperInSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 8),
    _AluZoneOperInSessionCount_Type()
)
aluZoneOperInSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInSessionCount.setStatus("current")
_AluZoneOperInActiveSessions_Type = Gauge32
_AluZoneOperInActiveSessions_Object = MibTableColumn
aluZoneOperInActiveSessions = _AluZoneOperInActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 9),
    _AluZoneOperInActiveSessions_Type()
)
aluZoneOperInActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInActiveSessions.setStatus("current")
_AluZoneOperOutSessionCount_Type = Counter64
_AluZoneOperOutSessionCount_Object = MibTableColumn
aluZoneOperOutSessionCount = _AluZoneOperOutSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 10),
    _AluZoneOperOutSessionCount_Type()
)
aluZoneOperOutSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutSessionCount.setStatus("current")
_AluZoneOperOutActiveSessions_Type = Gauge32
_AluZoneOperOutActiveSessions_Object = MibTableColumn
aluZoneOperOutActiveSessions = _AluZoneOperOutActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 11),
    _AluZoneOperOutActiveSessions_Type()
)
aluZoneOperOutActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutActiveSessions.setStatus("current")
_AluZoneOperInPktsDropped_Type = Counter64
_AluZoneOperInPktsDropped_Object = MibTableColumn
aluZoneOperInPktsDropped = _AluZoneOperInPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 12),
    _AluZoneOperInPktsDropped_Type()
)
aluZoneOperInPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInPktsDropped.setStatus("current")
_AluZoneOperInBytesDropped_Type = Counter64
_AluZoneOperInBytesDropped_Object = MibTableColumn
aluZoneOperInBytesDropped = _AluZoneOperInBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 13),
    _AluZoneOperInBytesDropped_Type()
)
aluZoneOperInBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInBytesDropped.setStatus("obsolete")
_AluZoneOperOutPktsDropped_Type = Counter64
_AluZoneOperOutPktsDropped_Object = MibTableColumn
aluZoneOperOutPktsDropped = _AluZoneOperOutPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 14),
    _AluZoneOperOutPktsDropped_Type()
)
aluZoneOperOutPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutPktsDropped.setStatus("current")
_AluZoneOperOutBytesDropped_Type = Counter64
_AluZoneOperOutBytesDropped_Object = MibTableColumn
aluZoneOperOutBytesDropped = _AluZoneOperOutBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 15),
    _AluZoneOperOutBytesDropped_Type()
)
aluZoneOperOutBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutBytesDropped.setStatus("obsolete")
_AluZoneOperInPktsDefAction_Type = Counter64
_AluZoneOperInPktsDefAction_Object = MibTableColumn
aluZoneOperInPktsDefAction = _AluZoneOperInPktsDefAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 16),
    _AluZoneOperInPktsDefAction_Type()
)
aluZoneOperInPktsDefAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInPktsDefAction.setStatus("current")
_AluZoneOperInBytesDefAction_Type = Counter64
_AluZoneOperInBytesDefAction_Object = MibTableColumn
aluZoneOperInBytesDefAction = _AluZoneOperInBytesDefAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 17),
    _AluZoneOperInBytesDefAction_Type()
)
aluZoneOperInBytesDefAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInBytesDefAction.setStatus("obsolete")
_AluZoneOperOutPktsDefAction_Type = Counter64
_AluZoneOperOutPktsDefAction_Object = MibTableColumn
aluZoneOperOutPktsDefAction = _AluZoneOperOutPktsDefAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 18),
    _AluZoneOperOutPktsDefAction_Type()
)
aluZoneOperOutPktsDefAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutPktsDefAction.setStatus("current")
_AluZoneOperOutBytesDefAction_Type = Counter64
_AluZoneOperOutBytesDefAction_Object = MibTableColumn
aluZoneOperOutBytesDefAction = _AluZoneOperOutBytesDefAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 19),
    _AluZoneOperOutBytesDefAction_Type()
)
aluZoneOperOutBytesDefAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutBytesDefAction.setStatus("obsolete")
_AluZoneOperPlcyLastCommit_Type = TimeStamp
_AluZoneOperPlcyLastCommit_Object = MibTableColumn
aluZoneOperPlcyLastCommit = _AluZoneOperPlcyLastCommit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 20),
    _AluZoneOperPlcyLastCommit_Type()
)
aluZoneOperPlcyLastCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperPlcyLastCommit.setStatus("current")
_AluZoneOperInTcpSessLimit_Type = Unsigned32
_AluZoneOperInTcpSessLimit_Object = MibTableColumn
aluZoneOperInTcpSessLimit = _AluZoneOperInTcpSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 21),
    _AluZoneOperInTcpSessLimit_Type()
)
aluZoneOperInTcpSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInTcpSessLimit.setStatus("current")
_AluZoneOperInUdpSessLimit_Type = Unsigned32
_AluZoneOperInUdpSessLimit_Object = MibTableColumn
aluZoneOperInUdpSessLimit = _AluZoneOperInUdpSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 22),
    _AluZoneOperInUdpSessLimit_Type()
)
aluZoneOperInUdpSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInUdpSessLimit.setStatus("current")
_AluZoneOperInIcmpSessLimit_Type = Unsigned32
_AluZoneOperInIcmpSessLimit_Object = MibTableColumn
aluZoneOperInIcmpSessLimit = _AluZoneOperInIcmpSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 23),
    _AluZoneOperInIcmpSessLimit_Type()
)
aluZoneOperInIcmpSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInIcmpSessLimit.setStatus("current")
_AluZoneOperInOthSessLimit_Type = Unsigned32
_AluZoneOperInOthSessLimit_Object = MibTableColumn
aluZoneOperInOthSessLimit = _AluZoneOperInOthSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 24),
    _AluZoneOperInOthSessLimit_Type()
)
aluZoneOperInOthSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInOthSessLimit.setStatus("current")
_AluZoneOperOutTcpSessLimit_Type = Unsigned32
_AluZoneOperOutTcpSessLimit_Object = MibTableColumn
aluZoneOperOutTcpSessLimit = _AluZoneOperOutTcpSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 25),
    _AluZoneOperOutTcpSessLimit_Type()
)
aluZoneOperOutTcpSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutTcpSessLimit.setStatus("current")
_AluZoneOperOutUdpSessLimit_Type = Unsigned32
_AluZoneOperOutUdpSessLimit_Object = MibTableColumn
aluZoneOperOutUdpSessLimit = _AluZoneOperOutUdpSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 26),
    _AluZoneOperOutUdpSessLimit_Type()
)
aluZoneOperOutUdpSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutUdpSessLimit.setStatus("current")
_AluZoneOperOutIcmpSessLimit_Type = Unsigned32
_AluZoneOperOutIcmpSessLimit_Object = MibTableColumn
aluZoneOperOutIcmpSessLimit = _AluZoneOperOutIcmpSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 27),
    _AluZoneOperOutIcmpSessLimit_Type()
)
aluZoneOperOutIcmpSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutIcmpSessLimit.setStatus("current")
_AluZoneOperOutOthSessLimit_Type = Unsigned32
_AluZoneOperOutOthSessLimit_Object = MibTableColumn
aluZoneOperOutOthSessLimit = _AluZoneOperOutOthSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 28),
    _AluZoneOperOutOthSessLimit_Type()
)
aluZoneOperOutOthSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutOthSessLimit.setStatus("current")
_AluZoneOperInTcpActSessions_Type = Gauge32
_AluZoneOperInTcpActSessions_Object = MibTableColumn
aluZoneOperInTcpActSessions = _AluZoneOperInTcpActSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 29),
    _AluZoneOperInTcpActSessions_Type()
)
aluZoneOperInTcpActSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInTcpActSessions.setStatus("current")
_AluZoneOperInUdpActSessions_Type = Gauge32
_AluZoneOperInUdpActSessions_Object = MibTableColumn
aluZoneOperInUdpActSessions = _AluZoneOperInUdpActSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 30),
    _AluZoneOperInUdpActSessions_Type()
)
aluZoneOperInUdpActSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInUdpActSessions.setStatus("current")
_AluZoneOperInIcmpActSessions_Type = Gauge32
_AluZoneOperInIcmpActSessions_Object = MibTableColumn
aluZoneOperInIcmpActSessions = _AluZoneOperInIcmpActSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 31),
    _AluZoneOperInIcmpActSessions_Type()
)
aluZoneOperInIcmpActSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInIcmpActSessions.setStatus("current")
_AluZoneOperInOthActSessions_Type = Gauge32
_AluZoneOperInOthActSessions_Object = MibTableColumn
aluZoneOperInOthActSessions = _AluZoneOperInOthActSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 32),
    _AluZoneOperInOthActSessions_Type()
)
aluZoneOperInOthActSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInOthActSessions.setStatus("current")
_AluZoneOperOutTcpActSessions_Type = Gauge32
_AluZoneOperOutTcpActSessions_Object = MibTableColumn
aluZoneOperOutTcpActSessions = _AluZoneOperOutTcpActSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 33),
    _AluZoneOperOutTcpActSessions_Type()
)
aluZoneOperOutTcpActSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutTcpActSessions.setStatus("current")
_AluZoneOperOutUdpActSessions_Type = Gauge32
_AluZoneOperOutUdpActSessions_Object = MibTableColumn
aluZoneOperOutUdpActSessions = _AluZoneOperOutUdpActSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 34),
    _AluZoneOperOutUdpActSessions_Type()
)
aluZoneOperOutUdpActSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutUdpActSessions.setStatus("current")
_AluZoneOperOutIcmpActSessions_Type = Gauge32
_AluZoneOperOutIcmpActSessions_Object = MibTableColumn
aluZoneOperOutIcmpActSessions = _AluZoneOperOutIcmpActSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 35),
    _AluZoneOperOutIcmpActSessions_Type()
)
aluZoneOperOutIcmpActSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutIcmpActSessions.setStatus("current")
_AluZoneOperOutOthActSessions_Type = Gauge32
_AluZoneOperOutOthActSessions_Object = MibTableColumn
aluZoneOperOutOthActSessions = _AluZoneOperOutOthActSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 36),
    _AluZoneOperOutOthActSessions_Type()
)
aluZoneOperOutOthActSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutOthActSessions.setStatus("current")


class _AluZoneOperLogId_Type(Unsigned32):
    """Custom type aluZoneOperLogId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluZoneOperLogId_Type.__name__ = "Unsigned32"
_AluZoneOperLogId_Object = MibTableColumn
aluZoneOperLogId = _AluZoneOperLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 38),
    _AluZoneOperLogId_Type()
)
aluZoneOperLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperLogId.setStatus("current")
_AluZoneOperAutoBind_Type = TruthValue
_AluZoneOperAutoBind_Object = MibTableColumn
aluZoneOperAutoBind = _AluZoneOperAutoBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 39),
    _AluZoneOperAutoBind_Type()
)
aluZoneOperAutoBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperAutoBind.setStatus("current")
_AluZoneOperInFwdAction_Type = Counter64
_AluZoneOperInFwdAction_Object = MibTableColumn
aluZoneOperInFwdAction = _AluZoneOperInFwdAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 40),
    _AluZoneOperInFwdAction_Type()
)
aluZoneOperInFwdAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInFwdAction.setStatus("current")
_AluZoneOperOutFwdAction_Type = Counter64
_AluZoneOperOutFwdAction_Object = MibTableColumn
aluZoneOperOutFwdAction = _AluZoneOperOutFwdAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 41),
    _AluZoneOperOutFwdAction_Type()
)
aluZoneOperOutFwdAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutFwdAction.setStatus("current")
_AluZoneOperInNatAction_Type = Counter64
_AluZoneOperInNatAction_Object = MibTableColumn
aluZoneOperInNatAction = _AluZoneOperInNatAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 42),
    _AluZoneOperInNatAction_Type()
)
aluZoneOperInNatAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInNatAction.setStatus("current")
_AluZoneOperOutNatAction_Type = Counter64
_AluZoneOperOutNatAction_Object = MibTableColumn
aluZoneOperOutNatAction = _AluZoneOperOutNatAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 43),
    _AluZoneOperOutNatAction_Type()
)
aluZoneOperOutNatAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutNatAction.setStatus("current")
_AluZoneOperInDropAction_Type = Counter64
_AluZoneOperInDropAction_Object = MibTableColumn
aluZoneOperInDropAction = _AluZoneOperInDropAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 44),
    _AluZoneOperInDropAction_Type()
)
aluZoneOperInDropAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperInDropAction.setStatus("current")
_AluZoneOperOutDropAction_Type = Counter64
_AluZoneOperOutDropAction_Object = MibTableColumn
aluZoneOperOutDropAction = _AluZoneOperOutDropAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 1, 1, 45),
    _AluZoneOperOutDropAction_Type()
)
aluZoneOperOutDropAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOperOutDropAction.setStatus("current")
_AluZonePlcyOperTable_Object = MibTable
aluZonePlcyOperTable = _AluZonePlcyOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 2)
)
if mibBuilder.loadTexts:
    aluZonePlcyOperTable.setStatus("current")
_AluZonePlcyOperEntry_Object = MibTableRow
aluZonePlcyOperEntry = _AluZonePlcyOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 2, 1)
)
aluZonePlcyOperEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluZoneOperId"),
    (0, "ALU-SECURITY-MIB", "aluZonePlcyOperRuleId"),
)
if mibBuilder.loadTexts:
    aluZonePlcyOperEntry.setStatus("current")


class _AluZonePlcyOperRuleId_Type(Unsigned32):
    """Custom type aluZonePlcyOperRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZonePlcyOperRuleId_Type.__name__ = "Unsigned32"
_AluZonePlcyOperRuleId_Object = MibTableColumn
aluZonePlcyOperRuleId = _AluZonePlcyOperRuleId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 2, 1, 1),
    _AluZonePlcyOperRuleId_Type()
)
aluZonePlcyOperRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluZonePlcyOperRuleId.setStatus("current")


class _AluZonePlcyOperEntryId_Type(Unsigned32):
    """Custom type aluZonePlcyOperEntryId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZonePlcyOperEntryId_Type.__name__ = "Unsigned32"
_AluZonePlcyOperEntryId_Object = MibTableColumn
aluZonePlcyOperEntryId = _AluZonePlcyOperEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 2, 1, 2),
    _AluZonePlcyOperEntryId_Type()
)
aluZonePlcyOperEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZonePlcyOperEntryId.setStatus("current")
_AluZonePlcyOperActive_Type = TruthValue
_AluZonePlcyOperActive_Object = MibTableColumn
aluZonePlcyOperActive = _AluZonePlcyOperActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 2, 1, 3),
    _AluZonePlcyOperActive_Type()
)
aluZonePlcyOperActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZonePlcyOperActive.setStatus("current")


class _AluZonePlcyOperFlags_Type(Bits):
    """Custom type aluZonePlcyOperFlags based on Bits"""
    namedValues = NamedValues(
        ("noNatPool", 0)
    )

_AluZonePlcyOperFlags_Type.__name__ = "Bits"
_AluZonePlcyOperFlags_Object = MibTableColumn
aluZonePlcyOperFlags = _AluZonePlcyOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 2, 1, 4),
    _AluZonePlcyOperFlags_Type()
)
aluZonePlcyOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZonePlcyOperFlags.setStatus("current")


class _AluZonePlcyOperSecPlcyId_Type(Unsigned32):
    """Custom type aluZonePlcyOperSecPlcyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZonePlcyOperSecPlcyId_Type.__name__ = "Unsigned32"
_AluZonePlcyOperSecPlcyId_Object = MibTableColumn
aluZonePlcyOperSecPlcyId = _AluZonePlcyOperSecPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 2, 1, 5),
    _AluZonePlcyOperSecPlcyId_Type()
)
aluZonePlcyOperSecPlcyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZonePlcyOperSecPlcyId.setStatus("current")


class _AluZonePlcyOperSecPlcyRuleId_Type(Unsigned32):
    """Custom type aluZonePlcyOperSecPlcyRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZonePlcyOperSecPlcyRuleId_Type.__name__ = "Unsigned32"
_AluZonePlcyOperSecPlcyRuleId_Object = MibTableColumn
aluZonePlcyOperSecPlcyRuleId = _AluZonePlcyOperSecPlcyRuleId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 2, 1, 6),
    _AluZonePlcyOperSecPlcyRuleId_Type()
)
aluZonePlcyOperSecPlcyRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZonePlcyOperSecPlcyRuleId.setStatus("current")


class _AluZonePlcyOperNatPoolId_Type(Unsigned32):
    """Custom type aluZonePlcyOperNatPoolId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZonePlcyOperNatPoolId_Type.__name__ = "Unsigned32"
_AluZonePlcyOperNatPoolId_Object = MibTableColumn
aluZonePlcyOperNatPoolId = _AluZonePlcyOperNatPoolId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 2, 1, 7),
    _AluZonePlcyOperNatPoolId_Type()
)
aluZonePlcyOperNatPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZonePlcyOperNatPoolId.setStatus("current")
_AluZonePlcyOperRuleHitCount_Type = Counter64
_AluZonePlcyOperRuleHitCount_Object = MibTableColumn
aluZonePlcyOperRuleHitCount = _AluZonePlcyOperRuleHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 2, 1, 8),
    _AluZonePlcyOperRuleHitCount_Type()
)
aluZonePlcyOperRuleHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZonePlcyOperRuleHitCount.setStatus("current")
_AluZonePlcyOperRuleActiveSessions_Type = Gauge32
_AluZonePlcyOperRuleActiveSessions_Object = MibTableColumn
aluZonePlcyOperRuleActiveSessions = _AluZonePlcyOperRuleActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 2, 1, 9),
    _AluZonePlcyOperRuleActiveSessions_Type()
)
aluZonePlcyOperRuleActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZonePlcyOperRuleActiveSessions.setStatus("current")
_AluZoneNatPoolOperTable_Object = MibTable
aluZoneNatPoolOperTable = _AluZoneNatPoolOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 3)
)
if mibBuilder.loadTexts:
    aluZoneNatPoolOperTable.setStatus("current")
_AluZoneNatPoolOperEntry_Object = MibTableRow
aluZoneNatPoolOperEntry = _AluZoneNatPoolOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 3, 1)
)
aluZoneNatPoolOperEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluZoneOperId"),
    (0, "ALU-SECURITY-MIB", "aluZoneNatPoolOperId"),
)
if mibBuilder.loadTexts:
    aluZoneNatPoolOperEntry.setStatus("current")


class _AluZoneNatPoolOperId_Type(Unsigned32):
    """Custom type aluZoneNatPoolOperId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZoneNatPoolOperId_Type.__name__ = "Unsigned32"
_AluZoneNatPoolOperId_Object = MibTableColumn
aluZoneNatPoolOperId = _AluZoneNatPoolOperId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 3, 1, 1),
    _AluZoneNatPoolOperId_Type()
)
aluZoneNatPoolOperId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluZoneNatPoolOperId.setStatus("current")
_AluZoneNatPoolOperName_Type = TNamedItemOrEmpty
_AluZoneNatPoolOperName_Object = MibTableColumn
aluZoneNatPoolOperName = _AluZoneNatPoolOperName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 3, 1, 2),
    _AluZoneNatPoolOperName_Type()
)
aluZoneNatPoolOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneNatPoolOperName.setStatus("current")


class _AluZoneNatPoolOperDescription_Type(TItemDescription):
    """Custom type aluZoneNatPoolOperDescription based on TItemDescription"""
    defaultHexValue = ""


_AluZoneNatPoolOperDescription_Type.__name__ = "TItemDescription"
_AluZoneNatPoolOperDescription_Object = MibTableColumn
aluZoneNatPoolOperDescription = _AluZoneNatPoolOperDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 3, 1, 3),
    _AluZoneNatPoolOperDescription_Type()
)
aluZoneNatPoolOperDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneNatPoolOperDescription.setStatus("current")
_AluZoneNatPoolOperType_Type = TPoolType
_AluZoneNatPoolOperType_Object = MibTableColumn
aluZoneNatPoolOperType = _AluZoneNatPoolOperType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 3, 1, 4),
    _AluZoneNatPoolOperType_Type()
)
aluZoneNatPoolOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneNatPoolOperType.setStatus("current")


class _AluZoneNatPoolOperDirection_Type(Integer32):
    """Custom type aluZoneNatPoolOperDirection based on Integer32"""
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
          ("zoneInbound", 1),
          ("zoneOutbound", 2))
    )


_AluZoneNatPoolOperDirection_Type.__name__ = "Integer32"
_AluZoneNatPoolOperDirection_Object = MibTableColumn
aluZoneNatPoolOperDirection = _AluZoneNatPoolOperDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 3, 1, 5),
    _AluZoneNatPoolOperDirection_Type()
)
aluZoneNatPoolOperDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneNatPoolOperDirection.setStatus("current")
_AluZoneNatPoolParamsOperTable_Object = MibTable
aluZoneNatPoolParamsOperTable = _AluZoneNatPoolParamsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 4)
)
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsOperTable.setStatus("current")
_AluZoneNatPoolParamsOperEntry_Object = MibTableRow
aluZoneNatPoolParamsOperEntry = _AluZoneNatPoolParamsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 4, 1)
)
aluZoneNatPoolParamsOperEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluZoneOperId"),
    (0, "ALU-SECURITY-MIB", "aluZoneNatPoolOperId"),
    (0, "ALU-SECURITY-MIB", "aluZoneNatPoolParamsOperEntryId"),
)
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsOperEntry.setStatus("current")


class _AluZoneNatPoolParamsOperEntryId_Type(Unsigned32):
    """Custom type aluZoneNatPoolParamsOperEntryId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZoneNatPoolParamsOperEntryId_Type.__name__ = "Unsigned32"
_AluZoneNatPoolParamsOperEntryId_Object = MibTableColumn
aluZoneNatPoolParamsOperEntryId = _AluZoneNatPoolParamsOperEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 4, 1, 1),
    _AluZoneNatPoolParamsOperEntryId_Type()
)
aluZoneNatPoolParamsOperEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsOperEntryId.setStatus("current")


class _AluZoneNatPoolParamsOperIPAddrValue1_Type(IpAddress):
    """Custom type aluZoneNatPoolParamsOperIPAddrValue1 based on IpAddress"""
    defaultHexValue = "00000000"


_AluZoneNatPoolParamsOperIPAddrValue1_Type.__name__ = "IpAddress"
_AluZoneNatPoolParamsOperIPAddrValue1_Object = MibTableColumn
aluZoneNatPoolParamsOperIPAddrValue1 = _AluZoneNatPoolParamsOperIPAddrValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 4, 1, 2),
    _AluZoneNatPoolParamsOperIPAddrValue1_Type()
)
aluZoneNatPoolParamsOperIPAddrValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsOperIPAddrValue1.setStatus("current")


class _AluZoneNatPoolParamsOperIPAddrValue2_Type(IpAddress):
    """Custom type aluZoneNatPoolParamsOperIPAddrValue2 based on IpAddress"""
    defaultHexValue = "00000000"


_AluZoneNatPoolParamsOperIPAddrValue2_Type.__name__ = "IpAddress"
_AluZoneNatPoolParamsOperIPAddrValue2_Object = MibTableColumn
aluZoneNatPoolParamsOperIPAddrValue2 = _AluZoneNatPoolParamsOperIPAddrValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 4, 1, 3),
    _AluZoneNatPoolParamsOperIPAddrValue2_Type()
)
aluZoneNatPoolParamsOperIPAddrValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsOperIPAddrValue2.setStatus("current")


class _AluZoneNatPoolParamsOperIPOperator_Type(TIPOperator):
    """Custom type aluZoneNatPoolParamsOperIPOperator based on TIPOperator"""
    defaultValue = 0


_AluZoneNatPoolParamsOperIPOperator_Type.__name__ = "TIPOperator"
_AluZoneNatPoolParamsOperIPOperator_Object = MibTableColumn
aluZoneNatPoolParamsOperIPOperator = _AluZoneNatPoolParamsOperIPOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 4, 1, 4),
    _AluZoneNatPoolParamsOperIPOperator_Type()
)
aluZoneNatPoolParamsOperIPOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsOperIPOperator.setStatus("current")


class _AluZoneNatPoolParamsOperIPInterfaceIndex_Type(InterfaceIndexOrZero):
    """Custom type aluZoneNatPoolParamsOperIPInterfaceIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_AluZoneNatPoolParamsOperIPInterfaceIndex_Type.__name__ = "InterfaceIndexOrZero"
_AluZoneNatPoolParamsOperIPInterfaceIndex_Object = MibTableColumn
aluZoneNatPoolParamsOperIPInterfaceIndex = _AluZoneNatPoolParamsOperIPInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 4, 1, 5),
    _AluZoneNatPoolParamsOperIPInterfaceIndex_Type()
)
aluZoneNatPoolParamsOperIPInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsOperIPInterfaceIndex.setStatus("current")


class _AluZoneNatPoolParamsOperPortOperator_Type(TTcpUdpPortOperator):
    """Custom type aluZoneNatPoolParamsOperPortOperator based on TTcpUdpPortOperator"""
    defaultValue = 0


_AluZoneNatPoolParamsOperPortOperator_Type.__name__ = "TTcpUdpPortOperator"
_AluZoneNatPoolParamsOperPortOperator_Object = MibTableColumn
aluZoneNatPoolParamsOperPortOperator = _AluZoneNatPoolParamsOperPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 4, 1, 6),
    _AluZoneNatPoolParamsOperPortOperator_Type()
)
aluZoneNatPoolParamsOperPortOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsOperPortOperator.setStatus("current")


class _AluZoneNatPoolParamsOperPortValue1_Type(TTcpUdpPort):
    """Custom type aluZoneNatPoolParamsOperPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_AluZoneNatPoolParamsOperPortValue1_Type.__name__ = "TTcpUdpPort"
_AluZoneNatPoolParamsOperPortValue1_Object = MibTableColumn
aluZoneNatPoolParamsOperPortValue1 = _AluZoneNatPoolParamsOperPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 4, 1, 7),
    _AluZoneNatPoolParamsOperPortValue1_Type()
)
aluZoneNatPoolParamsOperPortValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsOperPortValue1.setStatus("current")


class _AluZoneNatPoolParamsOperPortValue2_Type(TTcpUdpPort):
    """Custom type aluZoneNatPoolParamsOperPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_AluZoneNatPoolParamsOperPortValue2_Type.__name__ = "TTcpUdpPort"
_AluZoneNatPoolParamsOperPortValue2_Object = MibTableColumn
aluZoneNatPoolParamsOperPortValue2 = _AluZoneNatPoolParamsOperPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 4, 1, 8),
    _AluZoneNatPoolParamsOperPortValue2_Type()
)
aluZoneNatPoolParamsOperPortValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneNatPoolParamsOperPortValue2.setStatus("current")
_AluSecPlcyOperTable_Object = MibTable
aluSecPlcyOperTable = _AluSecPlcyOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 5)
)
if mibBuilder.loadTexts:
    aluSecPlcyOperTable.setStatus("current")
_AluSecPlcyOperEntry_Object = MibTableRow
aluSecPlcyOperEntry = _AluSecPlcyOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 5, 1)
)
aluSecPlcyOperEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecPlcyOperId"),
)
if mibBuilder.loadTexts:
    aluSecPlcyOperEntry.setStatus("current")


class _AluSecPlcyOperId_Type(Unsigned32):
    """Custom type aluSecPlcyOperId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecPlcyOperId_Type.__name__ = "Unsigned32"
_AluSecPlcyOperId_Object = MibTableColumn
aluSecPlcyOperId = _AluSecPlcyOperId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 5, 1, 1),
    _AluSecPlcyOperId_Type()
)
aluSecPlcyOperId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecPlcyOperId.setStatus("current")
_AluSecPlcyOperName_Type = TNamedItemOrEmpty
_AluSecPlcyOperName_Object = MibTableColumn
aluSecPlcyOperName = _AluSecPlcyOperName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 5, 1, 2),
    _AluSecPlcyOperName_Type()
)
aluSecPlcyOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyOperName.setStatus("current")
_AluSecPlcyOperDescription_Type = TItemDescription
_AluSecPlcyOperDescription_Object = MibTableColumn
aluSecPlcyOperDescription = _AluSecPlcyOperDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 5, 1, 3),
    _AluSecPlcyOperDescription_Type()
)
aluSecPlcyOperDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyOperDescription.setStatus("current")
_AluSecPlcyOperRuleCount_Type = Gauge32
_AluSecPlcyOperRuleCount_Object = MibTableColumn
aluSecPlcyOperRuleCount = _AluSecPlcyOperRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 5, 1, 4),
    _AluSecPlcyOperRuleCount_Type()
)
aluSecPlcyOperRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyOperRuleCount.setStatus("current")
_AluSecPlcyOperZoneRefCount_Type = Gauge32
_AluSecPlcyOperZoneRefCount_Object = MibTableColumn
aluSecPlcyOperZoneRefCount = _AluSecPlcyOperZoneRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 5, 1, 5),
    _AluSecPlcyOperZoneRefCount_Type()
)
aluSecPlcyOperZoneRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyOperZoneRefCount.setStatus("current")
_AluSecPlcyParamsOperTable_Object = MibTable
aluSecPlcyParamsOperTable = _AluSecPlcyParamsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6)
)
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperTable.setStatus("current")
_AluSecPlcyParamsOperEntry_Object = MibTableRow
aluSecPlcyParamsOperEntry = _AluSecPlcyParamsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1)
)
aluSecPlcyParamsOperEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecPlcyOperId"),
    (0, "ALU-SECURITY-MIB", "aluSecPlcyParamsOperRuleId"),
)
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperEntry.setStatus("current")


class _AluSecPlcyParamsOperRuleId_Type(Unsigned32):
    """Custom type aluSecPlcyParamsOperRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecPlcyParamsOperRuleId_Type.__name__ = "Unsigned32"
_AluSecPlcyParamsOperRuleId_Object = MibTableColumn
aluSecPlcyParamsOperRuleId = _AluSecPlcyParamsOperRuleId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 1),
    _AluSecPlcyParamsOperRuleId_Type()
)
aluSecPlcyParamsOperRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperRuleId.setStatus("current")
_AluSecPlcyParamsOperDescription_Type = TItemDescription
_AluSecPlcyParamsOperDescription_Object = MibTableColumn
aluSecPlcyParamsOperDescription = _AluSecPlcyParamsOperDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 2),
    _AluSecPlcyParamsOperDescription_Type()
)
aluSecPlcyParamsOperDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperDescription.setStatus("current")


class _AluSecPlcyParamsOperMatchSrcIPAddrValue1_Type(IpAddress):
    """Custom type aluSecPlcyParamsOperMatchSrcIPAddrValue1 based on IpAddress"""
    defaultHexValue = "00000000"


_AluSecPlcyParamsOperMatchSrcIPAddrValue1_Type.__name__ = "IpAddress"
_AluSecPlcyParamsOperMatchSrcIPAddrValue1_Object = MibTableColumn
aluSecPlcyParamsOperMatchSrcIPAddrValue1 = _AluSecPlcyParamsOperMatchSrcIPAddrValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 3),
    _AluSecPlcyParamsOperMatchSrcIPAddrValue1_Type()
)
aluSecPlcyParamsOperMatchSrcIPAddrValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchSrcIPAddrValue1.setStatus("current")


class _AluSecPlcyParamsOperMatchSrcIPAddrValue2_Type(IpAddress):
    """Custom type aluSecPlcyParamsOperMatchSrcIPAddrValue2 based on IpAddress"""
    defaultHexValue = "00000000"


_AluSecPlcyParamsOperMatchSrcIPAddrValue2_Type.__name__ = "IpAddress"
_AluSecPlcyParamsOperMatchSrcIPAddrValue2_Object = MibTableColumn
aluSecPlcyParamsOperMatchSrcIPAddrValue2 = _AluSecPlcyParamsOperMatchSrcIPAddrValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 4),
    _AluSecPlcyParamsOperMatchSrcIPAddrValue2_Type()
)
aluSecPlcyParamsOperMatchSrcIPAddrValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchSrcIPAddrValue2.setStatus("current")


class _AluSecPlcyParamsOperMatchSrcIPOperator_Type(TIPOperator):
    """Custom type aluSecPlcyParamsOperMatchSrcIPOperator based on TIPOperator"""
    defaultValue = 0


_AluSecPlcyParamsOperMatchSrcIPOperator_Type.__name__ = "TIPOperator"
_AluSecPlcyParamsOperMatchSrcIPOperator_Object = MibTableColumn
aluSecPlcyParamsOperMatchSrcIPOperator = _AluSecPlcyParamsOperMatchSrcIPOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 5),
    _AluSecPlcyParamsOperMatchSrcIPOperator_Type()
)
aluSecPlcyParamsOperMatchSrcIPOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchSrcIPOperator.setStatus("current")


class _AluSecPlcyParamsOperMatchSrcIPHostGroup_Type(Unsigned32):
    """Custom type aluSecPlcyParamsOperMatchSrcIPHostGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecPlcyParamsOperMatchSrcIPHostGroup_Type.__name__ = "Unsigned32"
_AluSecPlcyParamsOperMatchSrcIPHostGroup_Object = MibTableColumn
aluSecPlcyParamsOperMatchSrcIPHostGroup = _AluSecPlcyParamsOperMatchSrcIPHostGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 6),
    _AluSecPlcyParamsOperMatchSrcIPHostGroup_Type()
)
aluSecPlcyParamsOperMatchSrcIPHostGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchSrcIPHostGroup.setStatus("current")


class _AluSecPlcyParamsOperMatchDstIPAddrValue1_Type(IpAddress):
    """Custom type aluSecPlcyParamsOperMatchDstIPAddrValue1 based on IpAddress"""
    defaultHexValue = "00000000"


_AluSecPlcyParamsOperMatchDstIPAddrValue1_Type.__name__ = "IpAddress"
_AluSecPlcyParamsOperMatchDstIPAddrValue1_Object = MibTableColumn
aluSecPlcyParamsOperMatchDstIPAddrValue1 = _AluSecPlcyParamsOperMatchDstIPAddrValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 7),
    _AluSecPlcyParamsOperMatchDstIPAddrValue1_Type()
)
aluSecPlcyParamsOperMatchDstIPAddrValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchDstIPAddrValue1.setStatus("current")


class _AluSecPlcyParamsOperMatchDstIPAddrValue2_Type(IpAddress):
    """Custom type aluSecPlcyParamsOperMatchDstIPAddrValue2 based on IpAddress"""
    defaultHexValue = "00000000"


_AluSecPlcyParamsOperMatchDstIPAddrValue2_Type.__name__ = "IpAddress"
_AluSecPlcyParamsOperMatchDstIPAddrValue2_Object = MibTableColumn
aluSecPlcyParamsOperMatchDstIPAddrValue2 = _AluSecPlcyParamsOperMatchDstIPAddrValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 8),
    _AluSecPlcyParamsOperMatchDstIPAddrValue2_Type()
)
aluSecPlcyParamsOperMatchDstIPAddrValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchDstIPAddrValue2.setStatus("current")


class _AluSecPlcyParamsOperMatchDstIPOperator_Type(TIPOperator):
    """Custom type aluSecPlcyParamsOperMatchDstIPOperator based on TIPOperator"""
    defaultValue = 0


_AluSecPlcyParamsOperMatchDstIPOperator_Type.__name__ = "TIPOperator"
_AluSecPlcyParamsOperMatchDstIPOperator_Object = MibTableColumn
aluSecPlcyParamsOperMatchDstIPOperator = _AluSecPlcyParamsOperMatchDstIPOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 9),
    _AluSecPlcyParamsOperMatchDstIPOperator_Type()
)
aluSecPlcyParamsOperMatchDstIPOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchDstIPOperator.setStatus("current")


class _AluSecPlcyParamsOperMatchDstIPHostGroup_Type(Unsigned32):
    """Custom type aluSecPlcyParamsOperMatchDstIPHostGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecPlcyParamsOperMatchDstIPHostGroup_Type.__name__ = "Unsigned32"
_AluSecPlcyParamsOperMatchDstIPHostGroup_Object = MibTableColumn
aluSecPlcyParamsOperMatchDstIPHostGroup = _AluSecPlcyParamsOperMatchDstIPHostGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 10),
    _AluSecPlcyParamsOperMatchDstIPHostGroup_Type()
)
aluSecPlcyParamsOperMatchDstIPHostGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchDstIPHostGroup.setStatus("current")
_AluSecPlcyParamsOperMatchProtocol_Type = TIpProtocol
_AluSecPlcyParamsOperMatchProtocol_Object = MibTableColumn
aluSecPlcyParamsOperMatchProtocol = _AluSecPlcyParamsOperMatchProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 11),
    _AluSecPlcyParamsOperMatchProtocol_Type()
)
aluSecPlcyParamsOperMatchProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchProtocol.setStatus("current")
_AluSecPlcyParamsOperMatchSrcPortValue1_Type = TTcpUdpPort
_AluSecPlcyParamsOperMatchSrcPortValue1_Object = MibTableColumn
aluSecPlcyParamsOperMatchSrcPortValue1 = _AluSecPlcyParamsOperMatchSrcPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 12),
    _AluSecPlcyParamsOperMatchSrcPortValue1_Type()
)
aluSecPlcyParamsOperMatchSrcPortValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchSrcPortValue1.setStatus("current")
_AluSecPlcyParamsOperMatchSrcPortValue2_Type = TTcpUdpPort
_AluSecPlcyParamsOperMatchSrcPortValue2_Object = MibTableColumn
aluSecPlcyParamsOperMatchSrcPortValue2 = _AluSecPlcyParamsOperMatchSrcPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 13),
    _AluSecPlcyParamsOperMatchSrcPortValue2_Type()
)
aluSecPlcyParamsOperMatchSrcPortValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchSrcPortValue2.setStatus("current")
_AluSecPlcyParamsOperMatchSrcPortOp_Type = TOperator
_AluSecPlcyParamsOperMatchSrcPortOp_Object = MibTableColumn
aluSecPlcyParamsOperMatchSrcPortOp = _AluSecPlcyParamsOperMatchSrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 14),
    _AluSecPlcyParamsOperMatchSrcPortOp_Type()
)
aluSecPlcyParamsOperMatchSrcPortOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchSrcPortOp.setStatus("current")
_AluSecPlcyParamsOperMatchDstPortValue1_Type = TTcpUdpPort
_AluSecPlcyParamsOperMatchDstPortValue1_Object = MibTableColumn
aluSecPlcyParamsOperMatchDstPortValue1 = _AluSecPlcyParamsOperMatchDstPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 15),
    _AluSecPlcyParamsOperMatchDstPortValue1_Type()
)
aluSecPlcyParamsOperMatchDstPortValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchDstPortValue1.setStatus("current")
_AluSecPlcyParamsOperMatchDstPortValue2_Type = TTcpUdpPort
_AluSecPlcyParamsOperMatchDstPortValue2_Object = MibTableColumn
aluSecPlcyParamsOperMatchDstPortValue2 = _AluSecPlcyParamsOperMatchDstPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 16),
    _AluSecPlcyParamsOperMatchDstPortValue2_Type()
)
aluSecPlcyParamsOperMatchDstPortValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchDstPortValue2.setStatus("current")
_AluSecPlcyParamsOperMatchDstPortOp_Type = TOperator
_AluSecPlcyParamsOperMatchDstPortOp_Object = MibTableColumn
aluSecPlcyParamsOperMatchDstPortOp = _AluSecPlcyParamsOperMatchDstPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 17),
    _AluSecPlcyParamsOperMatchDstPortOp_Type()
)
aluSecPlcyParamsOperMatchDstPortOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchDstPortOp.setStatus("current")


class _AluSecPlcyParamsOperMatchAppGroup_Type(Unsigned32):
    """Custom type aluSecPlcyParamsOperMatchAppGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecPlcyParamsOperMatchAppGroup_Type.__name__ = "Unsigned32"
_AluSecPlcyParamsOperMatchAppGroup_Object = MibTableColumn
aluSecPlcyParamsOperMatchAppGroup = _AluSecPlcyParamsOperMatchAppGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 18),
    _AluSecPlcyParamsOperMatchAppGroup_Type()
)
aluSecPlcyParamsOperMatchAppGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchAppGroup.setStatus("current")


class _AluSecPlcyParamsOperMatchIcmpCode_Type(Integer32):
    """Custom type aluSecPlcyParamsOperMatchIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AluSecPlcyParamsOperMatchIcmpCode_Type.__name__ = "Integer32"
_AluSecPlcyParamsOperMatchIcmpCode_Object = MibTableColumn
aluSecPlcyParamsOperMatchIcmpCode = _AluSecPlcyParamsOperMatchIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 19),
    _AluSecPlcyParamsOperMatchIcmpCode_Type()
)
aluSecPlcyParamsOperMatchIcmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchIcmpCode.setStatus("current")


class _AluSecPlcyParamsOperMatchIcmpType_Type(Integer32):
    """Custom type aluSecPlcyParamsOperMatchIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AluSecPlcyParamsOperMatchIcmpType_Type.__name__ = "Integer32"
_AluSecPlcyParamsOperMatchIcmpType_Object = MibTableColumn
aluSecPlcyParamsOperMatchIcmpType = _AluSecPlcyParamsOperMatchIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 20),
    _AluSecPlcyParamsOperMatchIcmpType_Type()
)
aluSecPlcyParamsOperMatchIcmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchIcmpType.setStatus("current")


class _AluSecPlcyParamsOperMatchIgmpType_Type(Integer32):
    """Custom type aluSecPlcyParamsOperMatchIgmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AluSecPlcyParamsOperMatchIgmpType_Type.__name__ = "Integer32"
_AluSecPlcyParamsOperMatchIgmpType_Object = MibTableColumn
aluSecPlcyParamsOperMatchIgmpType = _AluSecPlcyParamsOperMatchIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 21),
    _AluSecPlcyParamsOperMatchIgmpType_Type()
)
aluSecPlcyParamsOperMatchIgmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchIgmpType.setStatus("current")


class _AluSecPlcyParamsOperMatchFlowDirection_Type(Integer32):
    """Custom type aluSecPlcyParamsOperMatchFlowDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("zoneInbound", 1),
          ("zoneOutbound", 2),
          ("both", 3))
    )


_AluSecPlcyParamsOperMatchFlowDirection_Type.__name__ = "Integer32"
_AluSecPlcyParamsOperMatchFlowDirection_Object = MibTableColumn
aluSecPlcyParamsOperMatchFlowDirection = _AluSecPlcyParamsOperMatchFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 22),
    _AluSecPlcyParamsOperMatchFlowDirection_Type()
)
aluSecPlcyParamsOperMatchFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchFlowDirection.setStatus("current")


class _AluSecPlcyParamsOperProfileId_Type(Unsigned32):
    """Custom type aluSecPlcyParamsOperProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AluSecPlcyParamsOperProfileId_Type.__name__ = "Unsigned32"
_AluSecPlcyParamsOperProfileId_Object = MibTableColumn
aluSecPlcyParamsOperProfileId = _AluSecPlcyParamsOperProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 23),
    _AluSecPlcyParamsOperProfileId_Type()
)
aluSecPlcyParamsOperProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperProfileId.setStatus("current")


class _AluSecPlcyParamsOperConcurrentFlowLimit_Type(Unsigned32):
    """Custom type aluSecPlcyParamsOperConcurrentFlowLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AluSecPlcyParamsOperConcurrentFlowLimit_Type.__name__ = "Unsigned32"
_AluSecPlcyParamsOperConcurrentFlowLimit_Object = MibTableColumn
aluSecPlcyParamsOperConcurrentFlowLimit = _AluSecPlcyParamsOperConcurrentFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 24),
    _AluSecPlcyParamsOperConcurrentFlowLimit_Type()
)
aluSecPlcyParamsOperConcurrentFlowLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperConcurrentFlowLimit.setStatus("current")
_AluSecPlcyParamsOperCreateRevDirFlow_Type = TruthValue
_AluSecPlcyParamsOperCreateRevDirFlow_Object = MibTableColumn
aluSecPlcyParamsOperCreateRevDirFlow = _AluSecPlcyParamsOperCreateRevDirFlow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 25),
    _AluSecPlcyParamsOperCreateRevDirFlow_Type()
)
aluSecPlcyParamsOperCreateRevDirFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperCreateRevDirFlow.setStatus("current")


class _AluSecPlcyParamsOperAction_Type(Integer32):
    """Custom type aluSecPlcyParamsOperAction based on Integer32"""
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
        *(("forward", 0),
          ("drop", 1),
          ("nat", 2),
          ("reject", 3))
    )


_AluSecPlcyParamsOperAction_Type.__name__ = "Integer32"
_AluSecPlcyParamsOperAction_Object = MibTableColumn
aluSecPlcyParamsOperAction = _AluSecPlcyParamsOperAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 26),
    _AluSecPlcyParamsOperAction_Type()
)
aluSecPlcyParamsOperAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperAction.setStatus("current")


class _AluSecPlcyParamsOperMatchLocal_Type(TruthValue):
    """Custom type aluSecPlcyParamsOperMatchLocal based on TruthValue"""
    defaultValue = 2


_AluSecPlcyParamsOperMatchLocal_Type.__name__ = "TruthValue"
_AluSecPlcyParamsOperMatchLocal_Object = MibTableColumn
aluSecPlcyParamsOperMatchLocal = _AluSecPlcyParamsOperMatchLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 27),
    _AluSecPlcyParamsOperMatchLocal_Type()
)
aluSecPlcyParamsOperMatchLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperMatchLocal.setStatus("current")


class _AluSecPlcyParamsOperActionNatDstIPAddr_Type(IpAddress):
    """Custom type aluSecPlcyParamsOperActionNatDstIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AluSecPlcyParamsOperActionNatDstIPAddr_Type.__name__ = "IpAddress"
_AluSecPlcyParamsOperActionNatDstIPAddr_Object = MibTableColumn
aluSecPlcyParamsOperActionNatDstIPAddr = _AluSecPlcyParamsOperActionNatDstIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 28),
    _AluSecPlcyParamsOperActionNatDstIPAddr_Type()
)
aluSecPlcyParamsOperActionNatDstIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperActionNatDstIPAddr.setStatus("current")


class _AluSecPlcyParamsOperActionNatDstPort_Type(TTcpUdpPort):
    """Custom type aluSecPlcyParamsOperActionNatDstPort based on TTcpUdpPort"""
    defaultValue = 0


_AluSecPlcyParamsOperActionNatDstPort_Type.__name__ = "TTcpUdpPort"
_AluSecPlcyParamsOperActionNatDstPort_Object = MibTableColumn
aluSecPlcyParamsOperActionNatDstPort = _AluSecPlcyParamsOperActionNatDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 39),
    _AluSecPlcyParamsOperActionNatDstPort_Type()
)
aluSecPlcyParamsOperActionNatDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperActionNatDstPort.setStatus("current")
_AluSecPlcyParamsOperLogControl_Type = Integer32
_AluSecPlcyParamsOperLogControl_Object = MibTableColumn
aluSecPlcyParamsOperLogControl = _AluSecPlcyParamsOperLogControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 40),
    _AluSecPlcyParamsOperLogControl_Type()
)
aluSecPlcyParamsOperLogControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperLogControl.setStatus("current")
_AluSecPlcyParamsOperLogId_Type = TSecurityLogId
_AluSecPlcyParamsOperLogId_Object = MibTableColumn
aluSecPlcyParamsOperLogId = _AluSecPlcyParamsOperLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 6, 1, 41),
    _AluSecPlcyParamsOperLogId_Type()
)
aluSecPlcyParamsOperLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPlcyParamsOperLogId.setStatus("current")
_AluSecProfileOperTable_Object = MibTable
aluSecProfileOperTable = _AluSecProfileOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7)
)
if mibBuilder.loadTexts:
    aluSecProfileOperTable.setStatus("current")
_AluSecProfileOperEntry_Object = MibTableRow
aluSecProfileOperEntry = _AluSecProfileOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1)
)
aluSecProfileOperEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecProfileOperId"),
)
if mibBuilder.loadTexts:
    aluSecProfileOperEntry.setStatus("current")


class _AluSecProfileOperId_Type(Unsigned32):
    """Custom type aluSecProfileOperId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecProfileOperId_Type.__name__ = "Unsigned32"
_AluSecProfileOperId_Object = MibTableColumn
aluSecProfileOperId = _AluSecProfileOperId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 1),
    _AluSecProfileOperId_Type()
)
aluSecProfileOperId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecProfileOperId.setStatus("current")


class _AluSecProfileOperName_Type(TNamedItemOrEmpty):
    """Custom type aluSecProfileOperName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSecProfileOperName_Type.__name__ = "TNamedItemOrEmpty"
_AluSecProfileOperName_Object = MibTableColumn
aluSecProfileOperName = _AluSecProfileOperName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 2),
    _AluSecProfileOperName_Type()
)
aluSecProfileOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperName.setStatus("current")


class _AluSecProfileOperDescription_Type(TItemDescription):
    """Custom type aluSecProfileOperDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecProfileOperDescription_Type.__name__ = "TItemDescription"
_AluSecProfileOperDescription_Object = MibTableColumn
aluSecProfileOperDescription = _AluSecProfileOperDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 3),
    _AluSecProfileOperDescription_Type()
)
aluSecProfileOperDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperDescription.setStatus("current")
_AluSecProfileOperPlcyRefCount_Type = Unsigned32
_AluSecProfileOperPlcyRefCount_Object = MibTableColumn
aluSecProfileOperPlcyRefCount = _AluSecProfileOperPlcyRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 4),
    _AluSecProfileOperPlcyRefCount_Type()
)
aluSecProfileOperPlcyRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperPlcyRefCount.setStatus("current")
_AluSecProfileOperTcpSynTimeout_Type = Unsigned32
_AluSecProfileOperTcpSynTimeout_Object = MibTableColumn
aluSecProfileOperTcpSynTimeout = _AluSecProfileOperTcpSynTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 5),
    _AluSecProfileOperTcpSynTimeout_Type()
)
aluSecProfileOperTcpSynTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperTcpSynTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileOperTcpSynTimeout.setUnits("seconds")
_AluSecProfileOperTcpWaitTimeout_Type = Unsigned32
_AluSecProfileOperTcpWaitTimeout_Object = MibTableColumn
aluSecProfileOperTcpWaitTimeout = _AluSecProfileOperTcpWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 6),
    _AluSecProfileOperTcpWaitTimeout_Type()
)
aluSecProfileOperTcpWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperTcpWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileOperTcpWaitTimeout.setUnits("seconds")
_AluSecProfileOperTcpTransTimeout_Type = Unsigned32
_AluSecProfileOperTcpTransTimeout_Object = MibTableColumn
aluSecProfileOperTcpTransTimeout = _AluSecProfileOperTcpTransTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 7),
    _AluSecProfileOperTcpTransTimeout_Type()
)
aluSecProfileOperTcpTransTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperTcpTransTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileOperTcpTransTimeout.setUnits("seconds")
_AluSecProfileOperTcpEstTimeout_Type = Unsigned32
_AluSecProfileOperTcpEstTimeout_Object = MibTableColumn
aluSecProfileOperTcpEstTimeout = _AluSecProfileOperTcpEstTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 8),
    _AluSecProfileOperTcpEstTimeout_Type()
)
aluSecProfileOperTcpEstTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperTcpEstTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileOperTcpEstTimeout.setUnits("seconds")
_AluSecProfileOperUdpTimeout_Type = Unsigned32
_AluSecProfileOperUdpTimeout_Object = MibTableColumn
aluSecProfileOperUdpTimeout = _AluSecProfileOperUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 9),
    _AluSecProfileOperUdpTimeout_Type()
)
aluSecProfileOperUdpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperUdpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileOperUdpTimeout.setUnits("seconds")
_AluSecProfileOperUdpInitTimeout_Type = Unsigned32
_AluSecProfileOperUdpInitTimeout_Object = MibTableColumn
aluSecProfileOperUdpInitTimeout = _AluSecProfileOperUdpInitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 10),
    _AluSecProfileOperUdpInitTimeout_Type()
)
aluSecProfileOperUdpInitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperUdpInitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileOperUdpInitTimeout.setUnits("seconds")
_AluSecProfileOperUdpDnsTimeout_Type = Unsigned32
_AluSecProfileOperUdpDnsTimeout_Object = MibTableColumn
aluSecProfileOperUdpDnsTimeout = _AluSecProfileOperUdpDnsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 11),
    _AluSecProfileOperUdpDnsTimeout_Type()
)
aluSecProfileOperUdpDnsTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperUdpDnsTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileOperUdpDnsTimeout.setUnits("seconds")
_AluSecProfileOperIcmpTimeout_Type = Unsigned32
_AluSecProfileOperIcmpTimeout_Object = MibTableColumn
aluSecProfileOperIcmpTimeout = _AluSecProfileOperIcmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 12),
    _AluSecProfileOperIcmpTimeout_Type()
)
aluSecProfileOperIcmpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperIcmpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileOperIcmpTimeout.setUnits("seconds")
_AluSecProfileOperOtherTimeout_Type = Unsigned32
_AluSecProfileOperOtherTimeout_Object = MibTableColumn
aluSecProfileOperOtherTimeout = _AluSecProfileOperOtherTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 13),
    _AluSecProfileOperOtherTimeout_Type()
)
aluSecProfileOperOtherTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperOtherTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileOperOtherTimeout.setUnits("seconds")


class _AluSecProfileOperAppInspect_Type(TruthValue):
    """Custom type aluSecProfileOperAppInspect based on TruthValue"""
    defaultValue = 2


_AluSecProfileOperAppInspect_Type.__name__ = "TruthValue"
_AluSecProfileOperAppInspect_Object = MibTableColumn
aluSecProfileOperAppInspect = _AluSecProfileOperAppInspect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 14),
    _AluSecProfileOperAppInspect_Type()
)
aluSecProfileOperAppInspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperAppInspect.setStatus("current")


class _AluSecProfileOperInspectTcp_Type(TruthValue):
    """Custom type aluSecProfileOperInspectTcp based on TruthValue"""
    defaultValue = 2


_AluSecProfileOperInspectTcp_Type.__name__ = "TruthValue"
_AluSecProfileOperInspectTcp_Object = MibTableColumn
aluSecProfileOperInspectTcp = _AluSecProfileOperInspectTcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 15),
    _AluSecProfileOperInspectTcp_Type()
)
aluSecProfileOperInspectTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperInspectTcp.setStatus("current")


class _AluSecProfileOperInspectIpOpt_Type(TruthValue):
    """Custom type aluSecProfileOperInspectIpOpt based on TruthValue"""
    defaultValue = 2


_AluSecProfileOperInspectIpOpt_Type.__name__ = "TruthValue"
_AluSecProfileOperInspectIpOpt_Object = MibTableColumn
aluSecProfileOperInspectIpOpt = _AluSecProfileOperInspectIpOpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 16),
    _AluSecProfileOperInspectIpOpt_Type()
)
aluSecProfileOperInspectIpOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperInspectIpOpt.setStatus("current")
_AluSecProfileOperAllowedIpOpt_Type = Unsigned32
_AluSecProfileOperAllowedIpOpt_Object = MibTableColumn
aluSecProfileOperAllowedIpOpt = _AluSecProfileOperAllowedIpOpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 17),
    _AluSecProfileOperAllowedIpOpt_Type()
)
aluSecProfileOperAllowedIpOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperAllowedIpOpt.setStatus("current")


class _AluSecProfileOperAllowPktFrag_Type(TruthValue):
    """Custom type aluSecProfileOperAllowPktFrag based on TruthValue"""
    defaultValue = 1


_AluSecProfileOperAllowPktFrag_Type.__name__ = "TruthValue"
_AluSecProfileOperAllowPktFrag_Object = MibTableColumn
aluSecProfileOperAllowPktFrag = _AluSecProfileOperAllowPktFrag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 18),
    _AluSecProfileOperAllowPktFrag_Type()
)
aluSecProfileOperAllowPktFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperAllowPktFrag.setStatus("current")


class _AluSecProfileOperAlg_Type(TAlgType):
    """Custom type aluSecProfileOperAlg based on TAlgType"""
    defaultValue = 1


_AluSecProfileOperAlg_Type.__name__ = "TAlgType"
_AluSecProfileOperAlg_Object = MibTableColumn
aluSecProfileOperAlg = _AluSecProfileOperAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 19),
    _AluSecProfileOperAlg_Type()
)
aluSecProfileOperAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperAlg.setStatus("current")


class _AluSecProfileOperIcmpReqLimit_Type(Unsigned32):
    """Custom type aluSecProfileOperIcmpReqLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_AluSecProfileOperIcmpReqLimit_Type.__name__ = "Unsigned32"
_AluSecProfileOperIcmpReqLimit_Object = MibTableColumn
aluSecProfileOperIcmpReqLimit = _AluSecProfileOperIcmpReqLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 20),
    _AluSecProfileOperIcmpReqLimit_Type()
)
aluSecProfileOperIcmpReqLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperIcmpReqLimit.setStatus("current")
if mibBuilder.loadTexts:
    aluSecProfileOperIcmpReqLimit.setUnits("packets")


class _AluSecProfileOperIcmpErrLimit_Type(TruthValue):
    """Custom type aluSecProfileOperIcmpErrLimit based on TruthValue"""
    defaultValue = 2


_AluSecProfileOperIcmpErrLimit_Type.__name__ = "TruthValue"
_AluSecProfileOperIcmpErrLimit_Object = MibTableColumn
aluSecProfileOperIcmpErrLimit = _AluSecProfileOperIcmpErrLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 21),
    _AluSecProfileOperIcmpErrLimit_Type()
)
aluSecProfileOperIcmpErrLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperIcmpErrLimit.setStatus("current")


class _AluSecProfileOperDnsReplyOnly_Type(TruthValue):
    """Custom type aluSecProfileOperDnsReplyOnly based on TruthValue"""
    defaultValue = 2


_AluSecProfileOperDnsReplyOnly_Type.__name__ = "TruthValue"
_AluSecProfileOperDnsReplyOnly_Object = MibTableColumn
aluSecProfileOperDnsReplyOnly = _AluSecProfileOperDnsReplyOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 22),
    _AluSecProfileOperDnsReplyOnly_Type()
)
aluSecProfileOperDnsReplyOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperDnsReplyOnly.setStatus("current")
_AluSecProfileOperTcpTmoStrict_Type = TruthValue
_AluSecProfileOperTcpTmoStrict_Object = MibTableColumn
aluSecProfileOperTcpTmoStrict = _AluSecProfileOperTcpTmoStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 23),
    _AluSecProfileOperTcpTmoStrict_Type()
)
aluSecProfileOperTcpTmoStrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperTcpTmoStrict.setStatus("current")
_AluSecProfileOperUdpTmoStrict_Type = TruthValue
_AluSecProfileOperUdpTmoStrict_Object = MibTableColumn
aluSecProfileOperUdpTmoStrict = _AluSecProfileOperUdpTmoStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 24),
    _AluSecProfileOperUdpTmoStrict_Type()
)
aluSecProfileOperUdpTmoStrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperUdpTmoStrict.setStatus("current")
_AluSecProfileOperIcmpTmoStrict_Type = TruthValue
_AluSecProfileOperIcmpTmoStrict_Object = MibTableColumn
aluSecProfileOperIcmpTmoStrict = _AluSecProfileOperIcmpTmoStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 25),
    _AluSecProfileOperIcmpTmoStrict_Type()
)
aluSecProfileOperIcmpTmoStrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperIcmpTmoStrict.setStatus("current")
_AluSecProfileOperDnsTmoStrict_Type = TruthValue
_AluSecProfileOperDnsTmoStrict_Object = MibTableColumn
aluSecProfileOperDnsTmoStrict = _AluSecProfileOperDnsTmoStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 26),
    _AluSecProfileOperDnsTmoStrict_Type()
)
aluSecProfileOperDnsTmoStrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperDnsTmoStrict.setStatus("current")


class _AluSecProfileOperOthTmoStrict_Type(TruthValue):
    """Custom type aluSecProfileOperOthTmoStrict based on TruthValue"""
    defaultValue = 2


_AluSecProfileOperOthTmoStrict_Type.__name__ = "TruthValue"
_AluSecProfileOperOthTmoStrict_Object = MibTableColumn
aluSecProfileOperOthTmoStrict = _AluSecProfileOperOthTmoStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 27),
    _AluSecProfileOperOthTmoStrict_Type()
)
aluSecProfileOperOthTmoStrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperOthTmoStrict.setStatus("current")
_AluSecProfileOperFwdPolicerId_Type = TSecurityPolicerId
_AluSecProfileOperFwdPolicerId_Object = MibTableColumn
aluSecProfileOperFwdPolicerId = _AluSecProfileOperFwdPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 28),
    _AluSecProfileOperFwdPolicerId_Type()
)
aluSecProfileOperFwdPolicerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperFwdPolicerId.setStatus("current")
_AluSecProfileOperRevPolicerId_Type = TSecurityPolicerId
_AluSecProfileOperRevPolicerId_Object = MibTableColumn
aluSecProfileOperRevPolicerId = _AluSecProfileOperRevPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 7, 1, 29),
    _AluSecProfileOperRevPolicerId_Type()
)
aluSecProfileOperRevPolicerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecProfileOperRevPolicerId.setStatus("current")
_AluZoneInboundSessionTable_Object = MibTable
aluZoneInboundSessionTable = _AluZoneInboundSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8)
)
if mibBuilder.loadTexts:
    aluZoneInboundSessionTable.setStatus("current")
_AluZoneInboundSessionEntry_Object = MibTableRow
aluZoneInboundSessionEntry = _AluZoneInboundSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1)
)
aluZoneInboundSessionEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluZoneOperId"),
    (0, "ALU-SECURITY-MIB", "aluZoneSessionId"),
)
if mibBuilder.loadTexts:
    aluZoneInboundSessionEntry.setStatus("current")


class _AluZoneSessionId_Type(Unsigned32):
    """Custom type aluZoneSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZoneSessionId_Type.__name__ = "Unsigned32"
_AluZoneSessionId_Object = MibTableColumn
aluZoneSessionId = _AluZoneSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 1),
    _AluZoneSessionId_Type()
)
aluZoneSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluZoneSessionId.setStatus("current")
_AluZoneInboundSessionProtocol_Type = TIpProtocol
_AluZoneInboundSessionProtocol_Object = MibTableColumn
aluZoneInboundSessionProtocol = _AluZoneInboundSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 2),
    _AluZoneInboundSessionProtocol_Type()
)
aluZoneInboundSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionProtocol.setStatus("current")


class _AluZoneInboundSessionSrcZoneId_Type(Unsigned32):
    """Custom type aluZoneInboundSessionSrcZoneId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZoneInboundSessionSrcZoneId_Type.__name__ = "Unsigned32"
_AluZoneInboundSessionSrcZoneId_Object = MibTableColumn
aluZoneInboundSessionSrcZoneId = _AluZoneInboundSessionSrcZoneId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 3),
    _AluZoneInboundSessionSrcZoneId_Type()
)
aluZoneInboundSessionSrcZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionSrcZoneId.setStatus("current")
_AluZoneInboundSessionSrcIPAddrValue_Type = IpAddress
_AluZoneInboundSessionSrcIPAddrValue_Object = MibTableColumn
aluZoneInboundSessionSrcIPAddrValue = _AluZoneInboundSessionSrcIPAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 4),
    _AluZoneInboundSessionSrcIPAddrValue_Type()
)
aluZoneInboundSessionSrcIPAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionSrcIPAddrValue.setStatus("current")
_AluZoneInboundSessionSrcPortValue_Type = TTcpUdpPort
_AluZoneInboundSessionSrcPortValue_Object = MibTableColumn
aluZoneInboundSessionSrcPortValue = _AluZoneInboundSessionSrcPortValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 5),
    _AluZoneInboundSessionSrcPortValue_Type()
)
aluZoneInboundSessionSrcPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionSrcPortValue.setStatus("current")
_AluZoneInboundSessionDstIPAddrValue_Type = IpAddress
_AluZoneInboundSessionDstIPAddrValue_Object = MibTableColumn
aluZoneInboundSessionDstIPAddrValue = _AluZoneInboundSessionDstIPAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 6),
    _AluZoneInboundSessionDstIPAddrValue_Type()
)
aluZoneInboundSessionDstIPAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionDstIPAddrValue.setStatus("current")
_AluZoneInboundSessionDstPortValue_Type = TTcpUdpPort
_AluZoneInboundSessionDstPortValue_Object = MibTableColumn
aluZoneInboundSessionDstPortValue = _AluZoneInboundSessionDstPortValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 7),
    _AluZoneInboundSessionDstPortValue_Type()
)
aluZoneInboundSessionDstPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionDstPortValue.setStatus("current")
_AluZoneInboundSessionRevDirCreated_Type = TruthValue
_AluZoneInboundSessionRevDirCreated_Object = MibTableColumn
aluZoneInboundSessionRevDirCreated = _AluZoneInboundSessionRevDirCreated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 8),
    _AluZoneInboundSessionRevDirCreated_Type()
)
aluZoneInboundSessionRevDirCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionRevDirCreated.setStatus("current")


class _AluZoneInboundSessionAction_Type(Integer32):
    """Custom type aluZoneInboundSessionAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 0),
          ("drop", 1),
          ("nat", 2))
    )


_AluZoneInboundSessionAction_Type.__name__ = "Integer32"
_AluZoneInboundSessionAction_Object = MibTableColumn
aluZoneInboundSessionAction = _AluZoneInboundSessionAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 9),
    _AluZoneInboundSessionAction_Type()
)
aluZoneInboundSessionAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionAction.setStatus("current")
_AluZoneInboundSessionNatSrcIPAddrValue_Type = IpAddress
_AluZoneInboundSessionNatSrcIPAddrValue_Object = MibTableColumn
aluZoneInboundSessionNatSrcIPAddrValue = _AluZoneInboundSessionNatSrcIPAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 10),
    _AluZoneInboundSessionNatSrcIPAddrValue_Type()
)
aluZoneInboundSessionNatSrcIPAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionNatSrcIPAddrValue.setStatus("current")
_AluZoneInboundSessionNatSrcPortValue_Type = TTcpUdpPort
_AluZoneInboundSessionNatSrcPortValue_Object = MibTableColumn
aluZoneInboundSessionNatSrcPortValue = _AluZoneInboundSessionNatSrcPortValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 11),
    _AluZoneInboundSessionNatSrcPortValue_Type()
)
aluZoneInboundSessionNatSrcPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionNatSrcPortValue.setStatus("current")
_AluZoneInboundSessionNatDstIPAddrValue_Type = IpAddress
_AluZoneInboundSessionNatDstIPAddrValue_Object = MibTableColumn
aluZoneInboundSessionNatDstIPAddrValue = _AluZoneInboundSessionNatDstIPAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 12),
    _AluZoneInboundSessionNatDstIPAddrValue_Type()
)
aluZoneInboundSessionNatDstIPAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionNatDstIPAddrValue.setStatus("current")
_AluZoneInboundSessionNatDstPortValue_Type = TTcpUdpPort
_AluZoneInboundSessionNatDstPortValue_Object = MibTableColumn
aluZoneInboundSessionNatDstPortValue = _AluZoneInboundSessionNatDstPortValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 13),
    _AluZoneInboundSessionNatDstPortValue_Type()
)
aluZoneInboundSessionNatDstPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionNatDstPortValue.setStatus("current")
_AluZoneInboundSessionEstablished_Type = TimeStamp
_AluZoneInboundSessionEstablished_Object = MibTableColumn
aluZoneInboundSessionEstablished = _AluZoneInboundSessionEstablished_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 14),
    _AluZoneInboundSessionEstablished_Type()
)
aluZoneInboundSessionEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionEstablished.setStatus("current")


class _AluZoneInboundSessionAlg_Type(Integer32):
    """Custom type aluZoneInboundSessionAlg based on Integer32"""
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
          ("algRule", 1),
          ("ftp", 2))
    )


_AluZoneInboundSessionAlg_Type.__name__ = "Integer32"
_AluZoneInboundSessionAlg_Object = MibTableColumn
aluZoneInboundSessionAlg = _AluZoneInboundSessionAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 15),
    _AluZoneInboundSessionAlg_Type()
)
aluZoneInboundSessionAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionAlg.setStatus("current")
_AluZoneInboundSessionInspect_Type = TruthValue
_AluZoneInboundSessionInspect_Object = MibTableColumn
aluZoneInboundSessionInspect = _AluZoneInboundSessionInspect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 16),
    _AluZoneInboundSessionInspect_Type()
)
aluZoneInboundSessionInspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionInspect.setStatus("current")
_AluZoneInboundSessionFwdPolicerId_Type = TSecurityPolicerId
_AluZoneInboundSessionFwdPolicerId_Object = MibTableColumn
aluZoneInboundSessionFwdPolicerId = _AluZoneInboundSessionFwdPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 17),
    _AluZoneInboundSessionFwdPolicerId_Type()
)
aluZoneInboundSessionFwdPolicerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionFwdPolicerId.setStatus("current")
_AluZoneInboundSessionRevPolicerId_Type = TSecurityPolicerId
_AluZoneInboundSessionRevPolicerId_Object = MibTableColumn
aluZoneInboundSessionRevPolicerId = _AluZoneInboundSessionRevPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 18),
    _AluZoneInboundSessionRevPolicerId_Type()
)
aluZoneInboundSessionRevPolicerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionRevPolicerId.setStatus("current")
_AluZoneInboundSessionCreator_Type = Unsigned32
_AluZoneInboundSessionCreator_Object = MibTableColumn
aluZoneInboundSessionCreator = _AluZoneInboundSessionCreator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 8, 1, 19),
    _AluZoneInboundSessionCreator_Type()
)
aluZoneInboundSessionCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneInboundSessionCreator.setStatus("current")
_AluZoneOutboundSessionTable_Object = MibTable
aluZoneOutboundSessionTable = _AluZoneOutboundSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9)
)
if mibBuilder.loadTexts:
    aluZoneOutboundSessionTable.setStatus("current")
_AluZoneOutboundSessionEntry_Object = MibTableRow
aluZoneOutboundSessionEntry = _AluZoneOutboundSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1)
)
aluZoneOutboundSessionEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluZoneOperId"),
    (0, "ALU-SECURITY-MIB", "aluZoneSessionId"),
)
if mibBuilder.loadTexts:
    aluZoneOutboundSessionEntry.setStatus("current")
_AluZoneOutboundSessionProtocol_Type = TIpProtocol
_AluZoneOutboundSessionProtocol_Object = MibTableColumn
aluZoneOutboundSessionProtocol = _AluZoneOutboundSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 1),
    _AluZoneOutboundSessionProtocol_Type()
)
aluZoneOutboundSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionProtocol.setStatus("current")
_AluZoneOutboundSessionSrcIPAddrValue_Type = IpAddress
_AluZoneOutboundSessionSrcIPAddrValue_Object = MibTableColumn
aluZoneOutboundSessionSrcIPAddrValue = _AluZoneOutboundSessionSrcIPAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 2),
    _AluZoneOutboundSessionSrcIPAddrValue_Type()
)
aluZoneOutboundSessionSrcIPAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionSrcIPAddrValue.setStatus("current")
_AluZoneOutboundSessionSrcPortValue_Type = TTcpUdpPort
_AluZoneOutboundSessionSrcPortValue_Object = MibTableColumn
aluZoneOutboundSessionSrcPortValue = _AluZoneOutboundSessionSrcPortValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 3),
    _AluZoneOutboundSessionSrcPortValue_Type()
)
aluZoneOutboundSessionSrcPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionSrcPortValue.setStatus("current")
_AluZoneOutboundSessionDstIPAddrValue_Type = IpAddress
_AluZoneOutboundSessionDstIPAddrValue_Object = MibTableColumn
aluZoneOutboundSessionDstIPAddrValue = _AluZoneOutboundSessionDstIPAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 4),
    _AluZoneOutboundSessionDstIPAddrValue_Type()
)
aluZoneOutboundSessionDstIPAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionDstIPAddrValue.setStatus("current")
_AluZoneOutboundSessionDstPortValue_Type = TTcpUdpPort
_AluZoneOutboundSessionDstPortValue_Object = MibTableColumn
aluZoneOutboundSessionDstPortValue = _AluZoneOutboundSessionDstPortValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 5),
    _AluZoneOutboundSessionDstPortValue_Type()
)
aluZoneOutboundSessionDstPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionDstPortValue.setStatus("current")


class _AluZoneOutboundSessionDstZoneId_Type(Unsigned32):
    """Custom type aluZoneOutboundSessionDstZoneId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluZoneOutboundSessionDstZoneId_Type.__name__ = "Unsigned32"
_AluZoneOutboundSessionDstZoneId_Object = MibTableColumn
aluZoneOutboundSessionDstZoneId = _AluZoneOutboundSessionDstZoneId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 6),
    _AluZoneOutboundSessionDstZoneId_Type()
)
aluZoneOutboundSessionDstZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionDstZoneId.setStatus("current")
_AluZoneOutboundSessionRevDirCreated_Type = TruthValue
_AluZoneOutboundSessionRevDirCreated_Object = MibTableColumn
aluZoneOutboundSessionRevDirCreated = _AluZoneOutboundSessionRevDirCreated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 7),
    _AluZoneOutboundSessionRevDirCreated_Type()
)
aluZoneOutboundSessionRevDirCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionRevDirCreated.setStatus("current")


class _AluZoneOutboundSessionAction_Type(Integer32):
    """Custom type aluZoneOutboundSessionAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 0),
          ("drop", 1),
          ("nat", 2))
    )


_AluZoneOutboundSessionAction_Type.__name__ = "Integer32"
_AluZoneOutboundSessionAction_Object = MibTableColumn
aluZoneOutboundSessionAction = _AluZoneOutboundSessionAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 8),
    _AluZoneOutboundSessionAction_Type()
)
aluZoneOutboundSessionAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionAction.setStatus("current")
_AluZoneOutboundSessionNatSrcIPAddrValue_Type = IpAddress
_AluZoneOutboundSessionNatSrcIPAddrValue_Object = MibTableColumn
aluZoneOutboundSessionNatSrcIPAddrValue = _AluZoneOutboundSessionNatSrcIPAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 9),
    _AluZoneOutboundSessionNatSrcIPAddrValue_Type()
)
aluZoneOutboundSessionNatSrcIPAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionNatSrcIPAddrValue.setStatus("current")
_AluZoneOutboundSessionNatSrcPortValue_Type = TTcpUdpPort
_AluZoneOutboundSessionNatSrcPortValue_Object = MibTableColumn
aluZoneOutboundSessionNatSrcPortValue = _AluZoneOutboundSessionNatSrcPortValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 10),
    _AluZoneOutboundSessionNatSrcPortValue_Type()
)
aluZoneOutboundSessionNatSrcPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionNatSrcPortValue.setStatus("current")
_AluZoneOutboundSessionNatDstIPAddrValue_Type = IpAddress
_AluZoneOutboundSessionNatDstIPAddrValue_Object = MibTableColumn
aluZoneOutboundSessionNatDstIPAddrValue = _AluZoneOutboundSessionNatDstIPAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 11),
    _AluZoneOutboundSessionNatDstIPAddrValue_Type()
)
aluZoneOutboundSessionNatDstIPAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionNatDstIPAddrValue.setStatus("current")
_AluZoneOutboundSessionNatDstPortValue_Type = TTcpUdpPort
_AluZoneOutboundSessionNatDstPortValue_Object = MibTableColumn
aluZoneOutboundSessionNatDstPortValue = _AluZoneOutboundSessionNatDstPortValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 12),
    _AluZoneOutboundSessionNatDstPortValue_Type()
)
aluZoneOutboundSessionNatDstPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionNatDstPortValue.setStatus("current")
_AluZoneOutboundSessionEstablished_Type = TimeStamp
_AluZoneOutboundSessionEstablished_Object = MibTableColumn
aluZoneOutboundSessionEstablished = _AluZoneOutboundSessionEstablished_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 13),
    _AluZoneOutboundSessionEstablished_Type()
)
aluZoneOutboundSessionEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionEstablished.setStatus("current")


class _AluZoneOutboundSessionAlg_Type(Integer32):
    """Custom type aluZoneOutboundSessionAlg based on Integer32"""
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
          ("algRule", 1),
          ("ftp", 2))
    )


_AluZoneOutboundSessionAlg_Type.__name__ = "Integer32"
_AluZoneOutboundSessionAlg_Object = MibTableColumn
aluZoneOutboundSessionAlg = _AluZoneOutboundSessionAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 14),
    _AluZoneOutboundSessionAlg_Type()
)
aluZoneOutboundSessionAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionAlg.setStatus("current")
_AluZoneOutboundSessionInspect_Type = TruthValue
_AluZoneOutboundSessionInspect_Object = MibTableColumn
aluZoneOutboundSessionInspect = _AluZoneOutboundSessionInspect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 15),
    _AluZoneOutboundSessionInspect_Type()
)
aluZoneOutboundSessionInspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionInspect.setStatus("current")
_AluZoneOutboundSessionFwdPolicerId_Type = TSecurityPolicerId
_AluZoneOutboundSessionFwdPolicerId_Object = MibTableColumn
aluZoneOutboundSessionFwdPolicerId = _AluZoneOutboundSessionFwdPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 16),
    _AluZoneOutboundSessionFwdPolicerId_Type()
)
aluZoneOutboundSessionFwdPolicerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionFwdPolicerId.setStatus("current")
_AluZoneOutboundSessionRevPolicerId_Type = TSecurityPolicerId
_AluZoneOutboundSessionRevPolicerId_Object = MibTableColumn
aluZoneOutboundSessionRevPolicerId = _AluZoneOutboundSessionRevPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 17),
    _AluZoneOutboundSessionRevPolicerId_Type()
)
aluZoneOutboundSessionRevPolicerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionRevPolicerId.setStatus("current")
_AluZoneOutboundSessionCreator_Type = Unsigned32
_AluZoneOutboundSessionCreator_Object = MibTableColumn
aluZoneOutboundSessionCreator = _AluZoneOutboundSessionCreator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 9, 1, 18),
    _AluZoneOutboundSessionCreator_Type()
)
aluZoneOutboundSessionCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluZoneOutboundSessionCreator.setStatus("current")
_AluSecHostGrpOperTable_Object = MibTable
aluSecHostGrpOperTable = _AluSecHostGrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 10)
)
if mibBuilder.loadTexts:
    aluSecHostGrpOperTable.setStatus("current")
_AluSecHostGrpOperEntry_Object = MibTableRow
aluSecHostGrpOperEntry = _AluSecHostGrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 10, 1)
)
aluSecHostGrpOperEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecHostGrpOperId"),
)
if mibBuilder.loadTexts:
    aluSecHostGrpOperEntry.setStatus("current")


class _AluSecHostGrpOperId_Type(Unsigned32):
    """Custom type aluSecHostGrpOperId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AluSecHostGrpOperId_Type.__name__ = "Unsigned32"
_AluSecHostGrpOperId_Object = MibTableColumn
aluSecHostGrpOperId = _AluSecHostGrpOperId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 10, 1, 1),
    _AluSecHostGrpOperId_Type()
)
aluSecHostGrpOperId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecHostGrpOperId.setStatus("current")


class _AluSecHostGrpOperName_Type(TNamedItemOrEmpty):
    """Custom type aluSecHostGrpOperName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSecHostGrpOperName_Type.__name__ = "TNamedItemOrEmpty"
_AluSecHostGrpOperName_Object = MibTableColumn
aluSecHostGrpOperName = _AluSecHostGrpOperName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 10, 1, 2),
    _AluSecHostGrpOperName_Type()
)
aluSecHostGrpOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecHostGrpOperName.setStatus("current")


class _AluSecHostGrpOperDescription_Type(TItemDescription):
    """Custom type aluSecHostGrpOperDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecHostGrpOperDescription_Type.__name__ = "TItemDescription"
_AluSecHostGrpOperDescription_Object = MibTableColumn
aluSecHostGrpOperDescription = _AluSecHostGrpOperDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 10, 1, 3),
    _AluSecHostGrpOperDescription_Type()
)
aluSecHostGrpOperDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecHostGrpOperDescription.setStatus("current")
_AluSecHostGrpOperPlcyRefCount_Type = Unsigned32
_AluSecHostGrpOperPlcyRefCount_Object = MibTableColumn
aluSecHostGrpOperPlcyRefCount = _AluSecHostGrpOperPlcyRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 10, 1, 4),
    _AluSecHostGrpOperPlcyRefCount_Type()
)
aluSecHostGrpOperPlcyRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecHostGrpOperPlcyRefCount.setStatus("current")
_AluSecHostOperTable_Object = MibTable
aluSecHostOperTable = _AluSecHostOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 11)
)
if mibBuilder.loadTexts:
    aluSecHostOperTable.setStatus("current")
_AluSecHostOperEntry_Object = MibTableRow
aluSecHostOperEntry = _AluSecHostOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 11, 1)
)
aluSecHostOperEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecHostGrpOperId"),
    (0, "ALU-SECURITY-MIB", "aluSecHostOperIPAddrValue1"),
)
if mibBuilder.loadTexts:
    aluSecHostOperEntry.setStatus("current")
_AluSecHostOperIPAddrValue1_Type = IpAddress
_AluSecHostOperIPAddrValue1_Object = MibTableColumn
aluSecHostOperIPAddrValue1 = _AluSecHostOperIPAddrValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 11, 1, 1),
    _AluSecHostOperIPAddrValue1_Type()
)
aluSecHostOperIPAddrValue1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecHostOperIPAddrValue1.setStatus("current")


class _AluSecHostOperIPAddrValue2_Type(IpAddress):
    """Custom type aluSecHostOperIPAddrValue2 based on IpAddress"""
    defaultHexValue = "00000000"


_AluSecHostOperIPAddrValue2_Type.__name__ = "IpAddress"
_AluSecHostOperIPAddrValue2_Object = MibTableColumn
aluSecHostOperIPAddrValue2 = _AluSecHostOperIPAddrValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 11, 1, 2),
    _AluSecHostOperIPAddrValue2_Type()
)
aluSecHostOperIPAddrValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecHostOperIPAddrValue2.setStatus("current")


class _AluSecHostOperIPOperator_Type(TIPOperator):
    """Custom type aluSecHostOperIPOperator based on TIPOperator"""
    defaultValue = 0


_AluSecHostOperIPOperator_Type.__name__ = "TIPOperator"
_AluSecHostOperIPOperator_Object = MibTableColumn
aluSecHostOperIPOperator = _AluSecHostOperIPOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 11, 1, 3),
    _AluSecHostOperIPOperator_Type()
)
aluSecHostOperIPOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecHostOperIPOperator.setStatus("current")
_AluSecAppGrpOperTable_Object = MibTable
aluSecAppGrpOperTable = _AluSecAppGrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 12)
)
if mibBuilder.loadTexts:
    aluSecAppGrpOperTable.setStatus("current")
_AluSecAppGrpOperEntry_Object = MibTableRow
aluSecAppGrpOperEntry = _AluSecAppGrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 12, 1)
)
aluSecAppGrpOperEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecAppGrpOperId"),
)
if mibBuilder.loadTexts:
    aluSecAppGrpOperEntry.setStatus("current")


class _AluSecAppGrpOperId_Type(Unsigned32):
    """Custom type aluSecAppGrpOperId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AluSecAppGrpOperId_Type.__name__ = "Unsigned32"
_AluSecAppGrpOperId_Object = MibTableColumn
aluSecAppGrpOperId = _AluSecAppGrpOperId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 12, 1, 1),
    _AluSecAppGrpOperId_Type()
)
aluSecAppGrpOperId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecAppGrpOperId.setStatus("current")


class _AluSecAppGrpOperName_Type(TNamedItemOrEmpty):
    """Custom type aluSecAppGrpOperName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSecAppGrpOperName_Type.__name__ = "TNamedItemOrEmpty"
_AluSecAppGrpOperName_Object = MibTableColumn
aluSecAppGrpOperName = _AluSecAppGrpOperName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 12, 1, 2),
    _AluSecAppGrpOperName_Type()
)
aluSecAppGrpOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecAppGrpOperName.setStatus("current")


class _AluSecAppGrpOperDescription_Type(TItemDescription):
    """Custom type aluSecAppGrpOperDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecAppGrpOperDescription_Type.__name__ = "TItemDescription"
_AluSecAppGrpOperDescription_Object = MibTableColumn
aluSecAppGrpOperDescription = _AluSecAppGrpOperDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 12, 1, 3),
    _AluSecAppGrpOperDescription_Type()
)
aluSecAppGrpOperDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecAppGrpOperDescription.setStatus("current")
_AluSecAppGrpOperPlcyRefCount_Type = Unsigned32
_AluSecAppGrpOperPlcyRefCount_Object = MibTableColumn
aluSecAppGrpOperPlcyRefCount = _AluSecAppGrpOperPlcyRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 12, 1, 4),
    _AluSecAppGrpOperPlcyRefCount_Type()
)
aluSecAppGrpOperPlcyRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecAppGrpOperPlcyRefCount.setStatus("current")
_AluSecAppOperTable_Object = MibTable
aluSecAppOperTable = _AluSecAppOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 13)
)
if mibBuilder.loadTexts:
    aluSecAppOperTable.setStatus("current")
_AluSecAppOperEntry_Object = MibTableRow
aluSecAppOperEntry = _AluSecAppOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 13, 1)
)
aluSecAppOperEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecAppGrpOperId"),
    (0, "ALU-SECURITY-MIB", "aluSecAppOperEntryId"),
)
if mibBuilder.loadTexts:
    aluSecAppOperEntry.setStatus("current")


class _AluSecAppOperEntryId_Type(Unsigned32):
    """Custom type aluSecAppOperEntryId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecAppOperEntryId_Type.__name__ = "Unsigned32"
_AluSecAppOperEntryId_Object = MibTableColumn
aluSecAppOperEntryId = _AluSecAppOperEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 13, 1, 1),
    _AluSecAppOperEntryId_Type()
)
aluSecAppOperEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecAppOperEntryId.setStatus("current")


class _AluSecAppOperMatchProtocol_Type(TIpProtocol):
    """Custom type aluSecAppOperMatchProtocol based on TIpProtocol"""
    defaultValue = -1


_AluSecAppOperMatchProtocol_Type.__name__ = "TIpProtocol"
_AluSecAppOperMatchProtocol_Object = MibTableColumn
aluSecAppOperMatchProtocol = _AluSecAppOperMatchProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 13, 1, 2),
    _AluSecAppOperMatchProtocol_Type()
)
aluSecAppOperMatchProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecAppOperMatchProtocol.setStatus("current")


class _AluSecAppOperMatchSrcPortValue1_Type(TTcpUdpPort):
    """Custom type aluSecAppOperMatchSrcPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_AluSecAppOperMatchSrcPortValue1_Type.__name__ = "TTcpUdpPort"
_AluSecAppOperMatchSrcPortValue1_Object = MibTableColumn
aluSecAppOperMatchSrcPortValue1 = _AluSecAppOperMatchSrcPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 13, 1, 3),
    _AluSecAppOperMatchSrcPortValue1_Type()
)
aluSecAppOperMatchSrcPortValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecAppOperMatchSrcPortValue1.setStatus("current")


class _AluSecAppOperMatchSrcPortValue2_Type(TTcpUdpPort):
    """Custom type aluSecAppOperMatchSrcPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_AluSecAppOperMatchSrcPortValue2_Type.__name__ = "TTcpUdpPort"
_AluSecAppOperMatchSrcPortValue2_Object = MibTableColumn
aluSecAppOperMatchSrcPortValue2 = _AluSecAppOperMatchSrcPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 13, 1, 4),
    _AluSecAppOperMatchSrcPortValue2_Type()
)
aluSecAppOperMatchSrcPortValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecAppOperMatchSrcPortValue2.setStatus("current")


class _AluSecAppOperMatchSrcPortOp_Type(TOperator):
    """Custom type aluSecAppOperMatchSrcPortOp based on TOperator"""
    defaultValue = 0


_AluSecAppOperMatchSrcPortOp_Type.__name__ = "TOperator"
_AluSecAppOperMatchSrcPortOp_Object = MibTableColumn
aluSecAppOperMatchSrcPortOp = _AluSecAppOperMatchSrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 13, 1, 5),
    _AluSecAppOperMatchSrcPortOp_Type()
)
aluSecAppOperMatchSrcPortOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecAppOperMatchSrcPortOp.setStatus("current")


class _AluSecAppOperMatchDstPortValue1_Type(TTcpUdpPort):
    """Custom type aluSecAppOperMatchDstPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_AluSecAppOperMatchDstPortValue1_Type.__name__ = "TTcpUdpPort"
_AluSecAppOperMatchDstPortValue1_Object = MibTableColumn
aluSecAppOperMatchDstPortValue1 = _AluSecAppOperMatchDstPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 13, 1, 6),
    _AluSecAppOperMatchDstPortValue1_Type()
)
aluSecAppOperMatchDstPortValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecAppOperMatchDstPortValue1.setStatus("current")


class _AluSecAppOperMatchDstPortValue2_Type(TTcpUdpPort):
    """Custom type aluSecAppOperMatchDstPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_AluSecAppOperMatchDstPortValue2_Type.__name__ = "TTcpUdpPort"
_AluSecAppOperMatchDstPortValue2_Object = MibTableColumn
aluSecAppOperMatchDstPortValue2 = _AluSecAppOperMatchDstPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 13, 1, 7),
    _AluSecAppOperMatchDstPortValue2_Type()
)
aluSecAppOperMatchDstPortValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecAppOperMatchDstPortValue2.setStatus("current")


class _AluSecAppOperMatchDstPortOp_Type(TOperator):
    """Custom type aluSecAppOperMatchDstPortOp based on TOperator"""
    defaultValue = 0


_AluSecAppOperMatchDstPortOp_Type.__name__ = "TOperator"
_AluSecAppOperMatchDstPortOp_Object = MibTableColumn
aluSecAppOperMatchDstPortOp = _AluSecAppOperMatchDstPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 13, 1, 8),
    _AluSecAppOperMatchDstPortOp_Type()
)
aluSecAppOperMatchDstPortOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecAppOperMatchDstPortOp.setStatus("current")


class _AluSecAppOperMatchIcmpCode_Type(Integer32):
    """Custom type aluSecAppOperMatchIcmpCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AluSecAppOperMatchIcmpCode_Type.__name__ = "Integer32"
_AluSecAppOperMatchIcmpCode_Object = MibTableColumn
aluSecAppOperMatchIcmpCode = _AluSecAppOperMatchIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 13, 1, 9),
    _AluSecAppOperMatchIcmpCode_Type()
)
aluSecAppOperMatchIcmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecAppOperMatchIcmpCode.setStatus("current")


class _AluSecAppOperMatchIcmpType_Type(Integer32):
    """Custom type aluSecAppOperMatchIcmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AluSecAppOperMatchIcmpType_Type.__name__ = "Integer32"
_AluSecAppOperMatchIcmpType_Object = MibTableColumn
aluSecAppOperMatchIcmpType = _AluSecAppOperMatchIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 13, 1, 10),
    _AluSecAppOperMatchIcmpType_Type()
)
aluSecAppOperMatchIcmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecAppOperMatchIcmpType.setStatus("current")
_AluSecPolicerGrpOperTable_Object = MibTable
aluSecPolicerGrpOperTable = _AluSecPolicerGrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14)
)
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperTable.setStatus("current")
_AluSecPolicerGrpOperEntry_Object = MibTableRow
aluSecPolicerGrpOperEntry = _AluSecPolicerGrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1)
)
aluSecPolicerGrpOperEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecPolicerGrpOperId"),
)
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperEntry.setStatus("current")


class _AluSecPolicerGrpOperId_Type(Unsigned32):
    """Custom type aluSecPolicerGrpOperId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_AluSecPolicerGrpOperId_Type.__name__ = "Unsigned32"
_AluSecPolicerGrpOperId_Object = MibTableColumn
aluSecPolicerGrpOperId = _AluSecPolicerGrpOperId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1, 1),
    _AluSecPolicerGrpOperId_Type()
)
aluSecPolicerGrpOperId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperId.setStatus("current")


class _AluSecPolicerGrpOperName_Type(TNamedItemOrEmpty):
    """Custom type aluSecPolicerGrpOperName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSecPolicerGrpOperName_Type.__name__ = "TNamedItemOrEmpty"
_AluSecPolicerGrpOperName_Object = MibTableColumn
aluSecPolicerGrpOperName = _AluSecPolicerGrpOperName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1, 2),
    _AluSecPolicerGrpOperName_Type()
)
aluSecPolicerGrpOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperName.setStatus("current")


class _AluSecPolicerGrpOperDescription_Type(TItemDescription):
    """Custom type aluSecPolicerGrpOperDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecPolicerGrpOperDescription_Type.__name__ = "TItemDescription"
_AluSecPolicerGrpOperDescription_Object = MibTableColumn
aluSecPolicerGrpOperDescription = _AluSecPolicerGrpOperDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1, 3),
    _AluSecPolicerGrpOperDescription_Type()
)
aluSecPolicerGrpOperDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperDescription.setStatus("current")


class _AluSecPolicerGrpOperRate_Type(Integer32):
    """Custom type aluSecPolicerGrpOperRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000),
    )


_AluSecPolicerGrpOperRate_Type.__name__ = "Integer32"
_AluSecPolicerGrpOperRate_Object = MibTableColumn
aluSecPolicerGrpOperRate = _AluSecPolicerGrpOperRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1, 4),
    _AluSecPolicerGrpOperRate_Type()
)
aluSecPolicerGrpOperRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperRate.setStatus("current")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperRate.setUnits("mega-bits per second")


class _AluSecPolicerGrpOperRateCbs_Type(Unsigned32):
    """Custom type aluSecPolicerGrpOperRateCbs based on Unsigned32"""
    defaultValue = 130816

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 130816),
    )


_AluSecPolicerGrpOperRateCbs_Type.__name__ = "Unsigned32"
_AluSecPolicerGrpOperRateCbs_Object = MibTableColumn
aluSecPolicerGrpOperRateCbs = _AluSecPolicerGrpOperRateCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1, 5),
    _AluSecPolicerGrpOperRateCbs_Type()
)
aluSecPolicerGrpOperRateCbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperRateCbs.setStatus("current")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperRateCbs.setUnits("bytes")
_AluSecPolicerGrpOperPlcyRefCount_Type = Unsigned32
_AluSecPolicerGrpOperPlcyRefCount_Object = MibTableColumn
aluSecPolicerGrpOperPlcyRefCount = _AluSecPolicerGrpOperPlcyRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1, 6),
    _AluSecPolicerGrpOperPlcyRefCount_Type()
)
aluSecPolicerGrpOperPlcyRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperPlcyRefCount.setStatus("current")
_AluSecPolicerGrpOperFwdPktsPassed_Type = Counter64
_AluSecPolicerGrpOperFwdPktsPassed_Object = MibTableColumn
aluSecPolicerGrpOperFwdPktsPassed = _AluSecPolicerGrpOperFwdPktsPassed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1, 7),
    _AluSecPolicerGrpOperFwdPktsPassed_Type()
)
aluSecPolicerGrpOperFwdPktsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperFwdPktsPassed.setStatus("current")
_AluSecPolicerGrpOperFwdBytesPassed_Type = Counter64
_AluSecPolicerGrpOperFwdBytesPassed_Object = MibTableColumn
aluSecPolicerGrpOperFwdBytesPassed = _AluSecPolicerGrpOperFwdBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1, 8),
    _AluSecPolicerGrpOperFwdBytesPassed_Type()
)
aluSecPolicerGrpOperFwdBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperFwdBytesPassed.setStatus("current")
_AluSecPolicerGrpOperFwdPktsDrop_Type = Counter64
_AluSecPolicerGrpOperFwdPktsDrop_Object = MibTableColumn
aluSecPolicerGrpOperFwdPktsDrop = _AluSecPolicerGrpOperFwdPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1, 9),
    _AluSecPolicerGrpOperFwdPktsDrop_Type()
)
aluSecPolicerGrpOperFwdPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperFwdPktsDrop.setStatus("current")
_AluSecPolicerGrpOperRevPktsPassed_Type = Counter64
_AluSecPolicerGrpOperRevPktsPassed_Object = MibTableColumn
aluSecPolicerGrpOperRevPktsPassed = _AluSecPolicerGrpOperRevPktsPassed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1, 10),
    _AluSecPolicerGrpOperRevPktsPassed_Type()
)
aluSecPolicerGrpOperRevPktsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperRevPktsPassed.setStatus("current")
_AluSecPolicerGrpOperRevBytesPassed_Type = Counter64
_AluSecPolicerGrpOperRevBytesPassed_Object = MibTableColumn
aluSecPolicerGrpOperRevBytesPassed = _AluSecPolicerGrpOperRevBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1, 11),
    _AluSecPolicerGrpOperRevBytesPassed_Type()
)
aluSecPolicerGrpOperRevBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperRevBytesPassed.setStatus("current")
_AluSecPolicerGrpOperRevPktsDrop_Type = Counter64
_AluSecPolicerGrpOperRevPktsDrop_Object = MibTableColumn
aluSecPolicerGrpOperRevPktsDrop = _AluSecPolicerGrpOperRevPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 2, 14, 1, 12),
    _AluSecPolicerGrpOperRevPktsDrop_Type()
)
aluSecPolicerGrpOperRevPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecPolicerGrpOperRevPktsDrop.setStatus("current")
_AluSecurityStatsObjs_ObjectIdentity = ObjectIdentity
aluSecurityStatsObjs = _AluSecurityStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3)
)
_AluSecSessionStatsTable_Object = MibTable
aluSecSessionStatsTable = _AluSecSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1)
)
if mibBuilder.loadTexts:
    aluSecSessionStatsTable.setStatus("current")
_AluSecSessionStatsEntry_Object = MibTableRow
aluSecSessionStatsEntry = _AluSecSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1)
)
aluSecSessionStatsEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecSessionId"),
)
if mibBuilder.loadTexts:
    aluSecSessionStatsEntry.setStatus("current")


class _AluSecSessionId_Type(Unsigned32):
    """Custom type aluSecSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecSessionId_Type.__name__ = "Unsigned32"
_AluSecSessionId_Object = MibTableColumn
aluSecSessionId = _AluSecSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 1),
    _AluSecSessionId_Type()
)
aluSecSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecSessionId.setStatus("current")
_AluSecSessionOutboundZoneId_Type = Unsigned32
_AluSecSessionOutboundZoneId_Object = MibTableColumn
aluSecSessionOutboundZoneId = _AluSecSessionOutboundZoneId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 2),
    _AluSecSessionOutboundZoneId_Type()
)
aluSecSessionOutboundZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionOutboundZoneId.setStatus("current")
_AluSecSessionInboundZoneId_Type = Unsigned32
_AluSecSessionInboundZoneId_Object = MibTableColumn
aluSecSessionInboundZoneId = _AluSecSessionInboundZoneId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 3),
    _AluSecSessionInboundZoneId_Type()
)
aluSecSessionInboundZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionInboundZoneId.setStatus("current")
_AluSecSessionFwdPktsPassed_Type = Counter64
_AluSecSessionFwdPktsPassed_Object = MibTableColumn
aluSecSessionFwdPktsPassed = _AluSecSessionFwdPktsPassed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 4),
    _AluSecSessionFwdPktsPassed_Type()
)
aluSecSessionFwdPktsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionFwdPktsPassed.setStatus("current")
_AluSecSessionFwdBytesPassed_Type = Counter64
_AluSecSessionFwdBytesPassed_Object = MibTableColumn
aluSecSessionFwdBytesPassed = _AluSecSessionFwdBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 5),
    _AluSecSessionFwdBytesPassed_Type()
)
aluSecSessionFwdBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionFwdBytesPassed.setStatus("current")
_AluSecSessionRevPktsPassed_Type = Counter64
_AluSecSessionRevPktsPassed_Object = MibTableColumn
aluSecSessionRevPktsPassed = _AluSecSessionRevPktsPassed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 6),
    _AluSecSessionRevPktsPassed_Type()
)
aluSecSessionRevPktsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionRevPktsPassed.setStatus("current")
_AluSecSessionRevBytesPassed_Type = Counter64
_AluSecSessionRevBytesPassed_Object = MibTableColumn
aluSecSessionRevBytesPassed = _AluSecSessionRevBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 7),
    _AluSecSessionRevBytesPassed_Type()
)
aluSecSessionRevBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionRevBytesPassed.setStatus("current")
_AluSecSessionFwdDropActionPkts_Type = Counter64
_AluSecSessionFwdDropActionPkts_Object = MibTableColumn
aluSecSessionFwdDropActionPkts = _AluSecSessionFwdDropActionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 8),
    _AluSecSessionFwdDropActionPkts_Type()
)
aluSecSessionFwdDropActionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionFwdDropActionPkts.setStatus("current")
_AluSecSessionFwdDropIpOptPkts_Type = Counter64
_AluSecSessionFwdDropIpOptPkts_Object = MibTableColumn
aluSecSessionFwdDropIpOptPkts = _AluSecSessionFwdDropIpOptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 9),
    _AluSecSessionFwdDropIpOptPkts_Type()
)
aluSecSessionFwdDropIpOptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionFwdDropIpOptPkts.setStatus("current")
_AluSecSessionRevDropIpOptPkts_Type = Counter64
_AluSecSessionRevDropIpOptPkts_Object = MibTableColumn
aluSecSessionRevDropIpOptPkts = _AluSecSessionRevDropIpOptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 10),
    _AluSecSessionRevDropIpOptPkts_Type()
)
aluSecSessionRevDropIpOptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionRevDropIpOptPkts.setStatus("current")
_AluSecSessionFwdDropMaxPkts_Type = Counter64
_AluSecSessionFwdDropMaxPkts_Object = MibTableColumn
aluSecSessionFwdDropMaxPkts = _AluSecSessionFwdDropMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 11),
    _AluSecSessionFwdDropMaxPkts_Type()
)
aluSecSessionFwdDropMaxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionFwdDropMaxPkts.setStatus("current")
_AluSecSessionRevDropMaxPkts_Type = Counter64
_AluSecSessionRevDropMaxPkts_Object = MibTableColumn
aluSecSessionRevDropMaxPkts = _AluSecSessionRevDropMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 12),
    _AluSecSessionRevDropMaxPkts_Type()
)
aluSecSessionRevDropMaxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionRevDropMaxPkts.setStatus("current")
_AluSecSessionFwdDropMaxIcmpErr_Type = Counter64
_AluSecSessionFwdDropMaxIcmpErr_Object = MibTableColumn
aluSecSessionFwdDropMaxIcmpErr = _AluSecSessionFwdDropMaxIcmpErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 13),
    _AluSecSessionFwdDropMaxIcmpErr_Type()
)
aluSecSessionFwdDropMaxIcmpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionFwdDropMaxIcmpErr.setStatus("current")
_AluSecSessionRevDropMaxIcmpErr_Type = Counter64
_AluSecSessionRevDropMaxIcmpErr_Object = MibTableColumn
aluSecSessionRevDropMaxIcmpErr = _AluSecSessionRevDropMaxIcmpErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 14),
    _AluSecSessionRevDropMaxIcmpErr_Type()
)
aluSecSessionRevDropMaxIcmpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionRevDropMaxIcmpErr.setStatus("current")
_AluSecSessionFwdSecurityDrop_Type = Counter64
_AluSecSessionFwdSecurityDrop_Object = MibTableColumn
aluSecSessionFwdSecurityDrop = _AluSecSessionFwdSecurityDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 15),
    _AluSecSessionFwdSecurityDrop_Type()
)
aluSecSessionFwdSecurityDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionFwdSecurityDrop.setStatus("current")
_AluSecSessionRevSecurityDrop_Type = Counter64
_AluSecSessionRevSecurityDrop_Object = MibTableColumn
aluSecSessionRevSecurityDrop = _AluSecSessionRevSecurityDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 16),
    _AluSecSessionRevSecurityDrop_Type()
)
aluSecSessionRevSecurityDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionRevSecurityDrop.setStatus("current")
_AluSecSessionFwdPolicerDrop_Type = Counter64
_AluSecSessionFwdPolicerDrop_Object = MibTableColumn
aluSecSessionFwdPolicerDrop = _AluSecSessionFwdPolicerDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 17),
    _AluSecSessionFwdPolicerDrop_Type()
)
aluSecSessionFwdPolicerDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionFwdPolicerDrop.setStatus("current")
_AluSecSessionRevPolicerDrop_Type = Counter64
_AluSecSessionRevPolicerDrop_Object = MibTableColumn
aluSecSessionRevPolicerDrop = _AluSecSessionRevPolicerDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 18),
    _AluSecSessionRevPolicerDrop_Type()
)
aluSecSessionRevPolicerDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionRevPolicerDrop.setStatus("current")
_AluSecSessionRevDropActionPkts_Type = Counter64
_AluSecSessionRevDropActionPkts_Object = MibTableColumn
aluSecSessionRevDropActionPkts = _AluSecSessionRevDropActionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 1, 1, 19),
    _AluSecSessionRevDropActionPkts_Type()
)
aluSecSessionRevDropActionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecSessionRevDropActionPkts.setStatus("current")
_AluSecZoneStatsTable_Object = MibTable
aluSecZoneStatsTable = _AluSecZoneStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 2)
)
if mibBuilder.loadTexts:
    aluSecZoneStatsTable.setStatus("current")
_AluSecZoneStatsEntry_Object = MibTableRow
aluSecZoneStatsEntry = _AluSecZoneStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 2, 1)
)
aluSecZoneStatsEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecZoneId"),
)
if mibBuilder.loadTexts:
    aluSecZoneStatsEntry.setStatus("current")


class _AluSecZoneId_Type(Unsigned32):
    """Custom type aluSecZoneId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_AluSecZoneId_Type.__name__ = "Unsigned32"
_AluSecZoneId_Object = MibTableColumn
aluSecZoneId = _AluSecZoneId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 2, 1, 1),
    _AluSecZoneId_Type()
)
aluSecZoneId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecZoneId.setStatus("current")
_AluSecZoneRxCtrlQueueFwdPkts_Type = Counter64
_AluSecZoneRxCtrlQueueFwdPkts_Object = MibTableColumn
aluSecZoneRxCtrlQueueFwdPkts = _AluSecZoneRxCtrlQueueFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 2, 1, 2),
    _AluSecZoneRxCtrlQueueFwdPkts_Type()
)
aluSecZoneRxCtrlQueueFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecZoneRxCtrlQueueFwdPkts.setStatus("current")
_AluSecZoneRxCtrlQueueFwdBytes_Type = Counter64
_AluSecZoneRxCtrlQueueFwdBytes_Object = MibTableColumn
aluSecZoneRxCtrlQueueFwdBytes = _AluSecZoneRxCtrlQueueFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 2, 1, 3),
    _AluSecZoneRxCtrlQueueFwdBytes_Type()
)
aluSecZoneRxCtrlQueueFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecZoneRxCtrlQueueFwdBytes.setStatus("current")
_AluSecZoneRxCtrlQueueDroPkts_Type = Counter64
_AluSecZoneRxCtrlQueueDroPkts_Object = MibTableColumn
aluSecZoneRxCtrlQueueDroPkts = _AluSecZoneRxCtrlQueueDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 2, 1, 4),
    _AluSecZoneRxCtrlQueueDroPkts_Type()
)
aluSecZoneRxCtrlQueueDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecZoneRxCtrlQueueDroPkts.setStatus("current")
_AluSecZoneRxCtrlQueueDroBytes_Type = Counter64
_AluSecZoneRxCtrlQueueDroBytes_Object = MibTableColumn
aluSecZoneRxCtrlQueueDroBytes = _AluSecZoneRxCtrlQueueDroBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 2, 1, 5),
    _AluSecZoneRxCtrlQueueDroBytes_Type()
)
aluSecZoneRxCtrlQueueDroBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecZoneRxCtrlQueueDroBytes.setStatus("current")
_AluSecZoneRxCtrlQueueAutoBind_Type = TruthValue
_AluSecZoneRxCtrlQueueAutoBind_Object = MibTableColumn
aluSecZoneRxCtrlQueueAutoBind = _AluSecZoneRxCtrlQueueAutoBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 2, 1, 6),
    _AluSecZoneRxCtrlQueueAutoBind_Type()
)
aluSecZoneRxCtrlQueueAutoBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecZoneRxCtrlQueueAutoBind.setStatus("current")
_AluSecEngineStatsTable_Object = MibTable
aluSecEngineStatsTable = _AluSecEngineStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 3)
)
if mibBuilder.loadTexts:
    aluSecEngineStatsTable.setStatus("current")
_AluSecEngineStatsEntry_Object = MibTableRow
aluSecEngineStatsEntry = _AluSecEngineStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 3, 1)
)
aluSecEngineStatsEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecEngineId"),
)
if mibBuilder.loadTexts:
    aluSecEngineStatsEntry.setStatus("current")


class _AluSecEngineId_Type(Unsigned32):
    """Custom type aluSecEngineId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AluSecEngineId_Type.__name__ = "Unsigned32"
_AluSecEngineId_Object = MibTableColumn
aluSecEngineId = _AluSecEngineId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 3, 1, 1),
    _AluSecEngineId_Type()
)
aluSecEngineId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecEngineId.setStatus("current")
_AluSecEngineUtilization_Type = Unsigned32
_AluSecEngineUtilization_Object = MibTableColumn
aluSecEngineUtilization = _AluSecEngineUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 3, 1, 2),
    _AluSecEngineUtilization_Type()
)
aluSecEngineUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecEngineUtilization.setStatus("current")
if mibBuilder.loadTexts:
    aluSecEngineUtilization.setUnits("percent")
_AluSecEngineRxQueueCtrlPkts_Type = Counter64
_AluSecEngineRxQueueCtrlPkts_Object = MibTableColumn
aluSecEngineRxQueueCtrlPkts = _AluSecEngineRxQueueCtrlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 3, 1, 3),
    _AluSecEngineRxQueueCtrlPkts_Type()
)
aluSecEngineRxQueueCtrlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecEngineRxQueueCtrlPkts.setStatus("current")
_AluSecEngineRxQueueDataPkts_Type = Counter64
_AluSecEngineRxQueueDataPkts_Object = MibTableColumn
aluSecEngineRxQueueDataPkts = _AluSecEngineRxQueueDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 3, 1, 4),
    _AluSecEngineRxQueueDataPkts_Type()
)
aluSecEngineRxQueueDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecEngineRxQueueDataPkts.setStatus("current")
_AluSecEngineRxQueueDropPkts_Type = Counter64
_AluSecEngineRxQueueDropPkts_Object = MibTableColumn
aluSecEngineRxQueueDropPkts = _AluSecEngineRxQueueDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 3, 1, 5),
    _AluSecEngineRxQueueDropPkts_Type()
)
aluSecEngineRxQueueDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecEngineRxQueueDropPkts.setStatus("current")
_AluSecEngineDropPkts_Type = Counter64
_AluSecEngineDropPkts_Object = MibTableColumn
aluSecEngineDropPkts = _AluSecEngineDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 3, 3, 1, 6),
    _AluSecEngineDropPkts_Type()
)
aluSecEngineDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecEngineDropPkts.setStatus("current")
_AluSecurityNotifyObjs_ObjectIdentity = ObjectIdentity
aluSecurityNotifyObjs = _AluSecurityNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 4)
)
_AluSecNotifyZoneId_Type = Unsigned32
_AluSecNotifyZoneId_Object = MibScalar
aluSecNotifyZoneId = _AluSecNotifyZoneId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 4, 1),
    _AluSecNotifyZoneId_Type()
)
aluSecNotifyZoneId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluSecNotifyZoneId.setStatus("current")
_AluSecNotifyZoneRuleId_Type = Unsigned32
_AluSecNotifyZoneRuleId_Object = MibScalar
aluSecNotifyZoneRuleId = _AluSecNotifyZoneRuleId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 4, 2),
    _AluSecNotifyZoneRuleId_Type()
)
aluSecNotifyZoneRuleId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluSecNotifyZoneRuleId.setStatus("current")


class _AluSecNotifyPlcyAction_Type(Integer32):
    """Custom type aluSecNotifyPlcyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("draft", 1),
          ("commit", 2),
          ("abort", 3))
    )


_AluSecNotifyPlcyAction_Type.__name__ = "Integer32"
_AluSecNotifyPlcyAction_Object = MibScalar
aluSecNotifyPlcyAction = _AluSecNotifyPlcyAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 4, 3),
    _AluSecNotifyPlcyAction_Type()
)
aluSecNotifyPlcyAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluSecNotifyPlcyAction.setStatus("current")
_AluSecNotifyRuleActive_Type = TruthValue
_AluSecNotifyRuleActive_Object = MibScalar
aluSecNotifyRuleActive = _AluSecNotifyRuleActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 4, 4),
    _AluSecNotifyRuleActive_Type()
)
aluSecNotifyRuleActive.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluSecNotifyRuleActive.setStatus("current")
_AluSecurityLogObjs_ObjectIdentity = ObjectIdentity
aluSecurityLogObjs = _AluSecurityLogObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5)
)
_AluSecLogTable_Object = MibTable
aluSecLogTable = _AluSecLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1)
)
if mibBuilder.loadTexts:
    aluSecLogTable.setStatus("current")
_AluSecLogEntry_Object = MibTableRow
aluSecLogEntry = _AluSecLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1)
)
aluSecLogEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecLogId"),
)
if mibBuilder.loadTexts:
    aluSecLogEntry.setStatus("current")
_AluSecLogId_Type = TSecurityLogId
_AluSecLogId_Object = MibTableColumn
aluSecLogId = _AluSecLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1, 1),
    _AluSecLogId_Type()
)
aluSecLogId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecLogId.setStatus("current")


class _AluSecLogName_Type(TNamedItemOrEmpty):
    """Custom type aluSecLogName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSecLogName_Type.__name__ = "TNamedItemOrEmpty"
_AluSecLogName_Object = MibTableColumn
aluSecLogName = _AluSecLogName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1, 2),
    _AluSecLogName_Type()
)
aluSecLogName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecLogName.setStatus("current")
_AluSecLogRowStatus_Type = RowStatus
_AluSecLogRowStatus_Object = MibTableColumn
aluSecLogRowStatus = _AluSecLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1, 3),
    _AluSecLogRowStatus_Type()
)
aluSecLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecLogRowStatus.setStatus("current")


class _AluSecLogDescription_Type(TItemDescription):
    """Custom type aluSecLogDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecLogDescription_Type.__name__ = "TItemDescription"
_AluSecLogDescription_Object = MibTableColumn
aluSecLogDescription = _AluSecLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1, 4),
    _AluSecLogDescription_Type()
)
aluSecLogDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecLogDescription.setStatus("current")


class _AluSecLogEnabled_Type(TruthValue):
    """Custom type aluSecLogEnabled based on TruthValue"""
    defaultValue = 2


_AluSecLogEnabled_Type.__name__ = "TruthValue"
_AluSecLogEnabled_Object = MibTableColumn
aluSecLogEnabled = _AluSecLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1, 5),
    _AluSecLogEnabled_Type()
)
aluSecLogEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecLogEnabled.setStatus("current")


class _AluSecLogDestination_Type(Integer32):
    """Custom type aluSecLogDestination based on Integer32"""
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
          ("memory", 1),
          ("syslog", 2))
    )


_AluSecLogDestination_Type.__name__ = "Integer32"
_AluSecLogDestination_Object = MibTableColumn
aluSecLogDestination = _AluSecLogDestination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1, 6),
    _AluSecLogDestination_Type()
)
aluSecLogDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecLogDestination.setStatus("current")


class _AluSecLogMemSize_Type(Unsigned32):
    """Custom type aluSecLogMemSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_AluSecLogMemSize_Type.__name__ = "Unsigned32"
_AluSecLogMemSize_Object = MibTableColumn
aluSecLogMemSize = _AluSecLogMemSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1, 7),
    _AluSecLogMemSize_Type()
)
aluSecLogMemSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecLogMemSize.setStatus("current")


class _AluSecLogMemWrap_Type(TruthValue):
    """Custom type aluSecLogMemWrap based on TruthValue"""
    defaultValue = 1


_AluSecLogMemWrap_Type.__name__ = "TruthValue"
_AluSecLogMemWrap_Object = MibTableColumn
aluSecLogMemWrap = _AluSecLogMemWrap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1, 8),
    _AluSecLogMemWrap_Type()
)
aluSecLogMemWrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecLogMemWrap.setStatus("current")


class _AluSecLogSysLogId_Type(Unsigned32):
    """Custom type aluSecLogSysLogId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSecLogSysLogId_Type.__name__ = "Unsigned32"
_AluSecLogSysLogId_Object = MibTableColumn
aluSecLogSysLogId = _AluSecLogSysLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1, 9),
    _AluSecLogSysLogId_Type()
)
aluSecLogSysLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecLogSysLogId.setStatus("current")


class _AluSecLogLogProfileId_Type(TSecurityLogProfileId):
    """Custom type aluSecLogLogProfileId based on TSecurityLogProfileId"""
    defaultValue = 1


_AluSecLogLogProfileId_Type.__name__ = "TSecurityLogProfileId"
_AluSecLogLogProfileId_Object = MibTableColumn
aluSecLogLogProfileId = _AluSecLogLogProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1, 10),
    _AluSecLogLogProfileId_Type()
)
aluSecLogLogProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecLogLogProfileId.setStatus("current")
_AluSecLogApplied_Type = TruthValue
_AluSecLogApplied_Object = MibTableColumn
aluSecLogApplied = _AluSecLogApplied_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1, 11),
    _AluSecLogApplied_Type()
)
aluSecLogApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecLogApplied.setStatus("current")
_AluSecLogNextEventNum_Type = Unsigned32
_AluSecLogNextEventNum_Object = MibTableColumn
aluSecLogNextEventNum = _AluSecLogNextEventNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 1, 1, 12),
    _AluSecLogNextEventNum_Type()
)
aluSecLogNextEventNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecLogNextEventNum.setStatus("current")
_AluSecLogProfileTable_Object = MibTable
aluSecLogProfileTable = _AluSecLogProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 2)
)
if mibBuilder.loadTexts:
    aluSecLogProfileTable.setStatus("current")
_AluSecLogProfileEntry_Object = MibTableRow
aluSecLogProfileEntry = _AluSecLogProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 2, 1)
)
aluSecLogProfileEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecLogProfileId"),
)
if mibBuilder.loadTexts:
    aluSecLogProfileEntry.setStatus("current")
_AluSecLogProfileId_Type = TSecurityLogProfileId
_AluSecLogProfileId_Object = MibTableColumn
aluSecLogProfileId = _AluSecLogProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 2, 1, 1),
    _AluSecLogProfileId_Type()
)
aluSecLogProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecLogProfileId.setStatus("current")


class _AluSecLogProfileName_Type(TNamedItemOrEmpty):
    """Custom type aluSecLogProfileName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSecLogProfileName_Type.__name__ = "TNamedItemOrEmpty"
_AluSecLogProfileName_Object = MibTableColumn
aluSecLogProfileName = _AluSecLogProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 2, 1, 2),
    _AluSecLogProfileName_Type()
)
aluSecLogProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecLogProfileName.setStatus("current")
_AluSecLogProfileRowStatus_Type = RowStatus
_AluSecLogProfileRowStatus_Object = MibTableColumn
aluSecLogProfileRowStatus = _AluSecLogProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 2, 1, 3),
    _AluSecLogProfileRowStatus_Type()
)
aluSecLogProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecLogProfileRowStatus.setStatus("current")


class _AluSecLogProfileDescription_Type(TItemDescription):
    """Custom type aluSecLogProfileDescription based on TItemDescription"""
    defaultHexValue = ""


_AluSecLogProfileDescription_Type.__name__ = "TItemDescription"
_AluSecLogProfileDescription_Object = MibTableColumn
aluSecLogProfileDescription = _AluSecLogProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 2, 1, 4),
    _AluSecLogProfileDescription_Type()
)
aluSecLogProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSecLogProfileDescription.setStatus("current")
_AluSecLogProfileApplied_Type = TruthValue
_AluSecLogProfileApplied_Object = MibTableColumn
aluSecLogProfileApplied = _AluSecLogProfileApplied_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 2, 1, 5),
    _AluSecLogProfileApplied_Type()
)
aluSecLogProfileApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecLogProfileApplied.setStatus("current")
_AluSecLogEventTable_Object = MibTable
aluSecLogEventTable = _AluSecLogEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 3)
)
if mibBuilder.loadTexts:
    aluSecLogEventTable.setStatus("current")
_AluSecLogEventEntry_Object = MibTableRow
aluSecLogEventEntry = _AluSecLogEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 3, 1)
)
aluSecLogEventEntry.setIndexNames(
    (0, "ALU-SECURITY-MIB", "aluSecLogProfileId"),
    (0, "ALU-SECURITY-MIB", "aluSecLogEventType"),
    (0, "ALU-SECURITY-MIB", "aluSecLogEventId"),
)
if mibBuilder.loadTexts:
    aluSecLogEventEntry.setStatus("current")


class _AluSecLogEventType_Type(Integer32):
    """Custom type aluSecLogEventType based on Integer32"""
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
        *(("packet", 1),
          ("zone", 2),
          ("policy", 3),
          ("session", 4),
          ("application", 5),
          ("alg", 6))
    )


_AluSecLogEventType_Type.__name__ = "Integer32"
_AluSecLogEventType_Object = MibTableColumn
aluSecLogEventType = _AluSecLogEventType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 3, 1, 1),
    _AluSecLogEventType_Type()
)
aluSecLogEventType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecLogEventType.setStatus("current")
_AluSecLogEventId_Type = Unsigned32
_AluSecLogEventId_Object = MibTableColumn
aluSecLogEventId = _AluSecLogEventId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 3, 1, 2),
    _AluSecLogEventId_Type()
)
aluSecLogEventId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecLogEventId.setStatus("current")
_AluSecLogEventName_Type = TNamedItemOrEmpty
_AluSecLogEventName_Object = MibTableColumn
aluSecLogEventName = _AluSecLogEventName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 3, 1, 3),
    _AluSecLogEventName_Type()
)
aluSecLogEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecLogEventName.setStatus("current")


class _AluSecLogEventControl_Type(Integer32):
    """Custom type aluSecLogEventControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("throttled", 2),
          ("suppressed", 3))
    )


_AluSecLogEventControl_Type.__name__ = "Integer32"
_AluSecLogEventControl_Object = MibTableColumn
aluSecLogEventControl = _AluSecLogEventControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 5, 3, 1, 4),
    _AluSecLogEventControl_Type()
)
aluSecLogEventControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSecLogEventControl.setStatus("current")
_AluSecMcRedundancyObjs_ObjectIdentity = ObjectIdentity
aluSecMcRedundancyObjs = _AluSecMcRedundancyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6)
)
_AluMcPeerFwTableLastChanged_Type = TimeStamp
_AluMcPeerFwTableLastChanged_Object = MibScalar
aluMcPeerFwTableLastChanged = _AluMcPeerFwTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 1),
    _AluMcPeerFwTableLastChanged_Type()
)
aluMcPeerFwTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcPeerFwTableLastChanged.setStatus("current")
_AluMcPeerFwTable_Object = MibTable
aluMcPeerFwTable = _AluMcPeerFwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2)
)
if mibBuilder.loadTexts:
    aluMcPeerFwTable.setStatus("current")
_AluMcPeerFwEntry_Object = MibTableRow
aluMcPeerFwEntry = _AluMcPeerFwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1)
)
aluMcPeerFwEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    aluMcPeerFwEntry.setStatus("current")
_AluMcPeerFwRowStatus_Type = RowStatus
_AluMcPeerFwRowStatus_Object = MibTableColumn
aluMcPeerFwRowStatus = _AluMcPeerFwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 1),
    _AluMcPeerFwRowStatus_Type()
)
aluMcPeerFwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwRowStatus.setStatus("current")
_AluMcPeerFwLastChanged_Type = TimeStamp
_AluMcPeerFwLastChanged_Object = MibTableColumn
aluMcPeerFwLastChanged = _AluMcPeerFwLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 2),
    _AluMcPeerFwLastChanged_Type()
)
aluMcPeerFwLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcPeerFwLastChanged.setStatus("current")


class _AluMcPeerFwAdminState_Type(TmnxAdminState):
    """Custom type aluMcPeerFwAdminState based on TmnxAdminState"""
    defaultValue = 3


_AluMcPeerFwAdminState_Type.__name__ = "TmnxAdminState"
_AluMcPeerFwAdminState_Object = MibTableColumn
aluMcPeerFwAdminState = _AluMcPeerFwAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 3),
    _AluMcPeerFwAdminState_Type()
)
aluMcPeerFwAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwAdminState.setStatus("current")


class _AluMcPeerFwSysPriority_Type(Unsigned32):
    """Custom type aluMcPeerFwSysPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AluMcPeerFwSysPriority_Type.__name__ = "Unsigned32"
_AluMcPeerFwSysPriority_Object = MibTableColumn
aluMcPeerFwSysPriority = _AluMcPeerFwSysPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 4),
    _AluMcPeerFwSysPriority_Type()
)
aluMcPeerFwSysPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwSysPriority.setStatus("current")


class _AluMcPeerFwKeepAliveIntvl_Type(Unsigned32):
    """Custom type aluMcPeerFwKeepAliveIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 500),
    )


_AluMcPeerFwKeepAliveIntvl_Type.__name__ = "Unsigned32"
_AluMcPeerFwKeepAliveIntvl_Object = MibTableColumn
aluMcPeerFwKeepAliveIntvl = _AluMcPeerFwKeepAliveIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 5),
    _AluMcPeerFwKeepAliveIntvl_Type()
)
aluMcPeerFwKeepAliveIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwKeepAliveIntvl.setStatus("current")
if mibBuilder.loadTexts:
    aluMcPeerFwKeepAliveIntvl.setUnits("deci-seconds")


class _AluMcPeerFwHoldOnNbrFail_Type(Unsigned32):
    """Custom type aluMcPeerFwHoldOnNbrFail based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 25),
    )


_AluMcPeerFwHoldOnNbrFail_Type.__name__ = "Unsigned32"
_AluMcPeerFwHoldOnNbrFail_Object = MibTableColumn
aluMcPeerFwHoldOnNbrFail = _AluMcPeerFwHoldOnNbrFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 6),
    _AluMcPeerFwHoldOnNbrFail_Type()
)
aluMcPeerFwHoldOnNbrFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwHoldOnNbrFail.setStatus("current")


class _AluMcPeerFwBootTimer_Type(Unsigned32):
    """Custom type aluMcPeerFwBootTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_AluMcPeerFwBootTimer_Type.__name__ = "Unsigned32"
_AluMcPeerFwBootTimer_Object = MibTableColumn
aluMcPeerFwBootTimer = _AluMcPeerFwBootTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 7),
    _AluMcPeerFwBootTimer_Type()
)
aluMcPeerFwBootTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwBootTimer.setStatus("current")
if mibBuilder.loadTexts:
    aluMcPeerFwBootTimer.setUnits("seconds")


class _AluMcPeerFwBfd_Type(TmnxEnabledDisabled):
    """Custom type aluMcPeerFwBfd based on TmnxEnabledDisabled"""
    defaultValue = 2


_AluMcPeerFwBfd_Type.__name__ = "TmnxEnabledDisabled"
_AluMcPeerFwBfd_Object = MibTableColumn
aluMcPeerFwBfd = _AluMcPeerFwBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 8),
    _AluMcPeerFwBfd_Type()
)
aluMcPeerFwBfd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwBfd.setStatus("current")


class _AluMcPeerFwOperState_Type(Integer32):
    """Custom type aluMcPeerFwOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inService", 0),
          ("outOfService", 1))
    )


_AluMcPeerFwOperState_Type.__name__ = "Integer32"
_AluMcPeerFwOperState_Object = MibTableColumn
aluMcPeerFwOperState = _AluMcPeerFwOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 9),
    _AluMcPeerFwOperState_Type()
)
aluMcPeerFwOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcPeerFwOperState.setStatus("current")
_AluMcPeerFwPeerLastStateChge_Type = TimeStamp
_AluMcPeerFwPeerLastStateChge_Object = MibTableColumn
aluMcPeerFwPeerLastStateChge = _AluMcPeerFwPeerLastStateChge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 10),
    _AluMcPeerFwPeerLastStateChge_Type()
)
aluMcPeerFwPeerLastStateChge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcPeerFwPeerLastStateChge.setStatus("current")
_AluMcPeerFwRefCount_Type = Unsigned32
_AluMcPeerFwRefCount_Object = MibTableColumn
aluMcPeerFwRefCount = _AluMcPeerFwRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 11),
    _AluMcPeerFwRefCount_Type()
)
aluMcPeerFwRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcPeerFwRefCount.setStatus("current")


class _AluMcPeerFwEncryption_Type(TmnxEnabledDisabled):
    """Custom type aluMcPeerFwEncryption based on TmnxEnabledDisabled"""
    defaultValue = 2


_AluMcPeerFwEncryption_Type.__name__ = "TmnxEnabledDisabled"
_AluMcPeerFwEncryption_Object = MibTableColumn
aluMcPeerFwEncryption = _AluMcPeerFwEncryption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 12),
    _AluMcPeerFwEncryption_Type()
)
aluMcPeerFwEncryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwEncryption.setStatus("current")


class _AluMcPeerFwEncryptionAuthAlg_Type(AluMcFwAuthAlgorithm):
    """Custom type aluMcPeerFwEncryptionAuthAlg based on AluMcFwAuthAlgorithm"""
    defaultValue = 1


_AluMcPeerFwEncryptionAuthAlg_Type.__name__ = "AluMcFwAuthAlgorithm"
_AluMcPeerFwEncryptionAuthAlg_Object = MibTableColumn
aluMcPeerFwEncryptionAuthAlg = _AluMcPeerFwEncryptionAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 13),
    _AluMcPeerFwEncryptionAuthAlg_Type()
)
aluMcPeerFwEncryptionAuthAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwEncryptionAuthAlg.setStatus("current")


class _AluMcPeerFwEncryptionEncrAlg_Type(AluMcFwEncrAlgorithm):
    """Custom type aluMcPeerFwEncryptionEncrAlg based on AluMcFwEncrAlgorithm"""
    defaultValue = 1


_AluMcPeerFwEncryptionEncrAlg_Type.__name__ = "AluMcFwEncrAlgorithm"
_AluMcPeerFwEncryptionEncrAlg_Object = MibTableColumn
aluMcPeerFwEncryptionEncrAlg = _AluMcPeerFwEncryptionEncrAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 14),
    _AluMcPeerFwEncryptionEncrAlg_Type()
)
aluMcPeerFwEncryptionEncrAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwEncryptionEncrAlg.setStatus("current")


class _AluMcPeerFwEncryptionActOutSa_Type(Unsigned32):
    """Custom type aluMcPeerFwEncryptionActOutSa based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AluMcPeerFwEncryptionActOutSa_Type.__name__ = "Unsigned32"
_AluMcPeerFwEncryptionActOutSa_Object = MibTableColumn
aluMcPeerFwEncryptionActOutSa = _AluMcPeerFwEncryptionActOutSa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 15),
    _AluMcPeerFwEncryptionActOutSa_Type()
)
aluMcPeerFwEncryptionActOutSa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwEncryptionActOutSa.setStatus("current")


class _AluMcPeerFwEncryptionSpi1_Type(Unsigned32):
    """Custom type aluMcPeerFwEncryptionSpi1 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AluMcPeerFwEncryptionSpi1_Type.__name__ = "Unsigned32"
_AluMcPeerFwEncryptionSpi1_Object = MibTableColumn
aluMcPeerFwEncryptionSpi1 = _AluMcPeerFwEncryptionSpi1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 16),
    _AluMcPeerFwEncryptionSpi1_Type()
)
aluMcPeerFwEncryptionSpi1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwEncryptionSpi1.setStatus("current")


class _AluMcPeerFwEncryptionSpiAuthKey1_Type(OctetString):
    """Custom type aluMcPeerFwEncryptionSpiAuthKey1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AluMcPeerFwEncryptionSpiAuthKey1_Type.__name__ = "OctetString"
_AluMcPeerFwEncryptionSpiAuthKey1_Object = MibTableColumn
aluMcPeerFwEncryptionSpiAuthKey1 = _AluMcPeerFwEncryptionSpiAuthKey1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 17),
    _AluMcPeerFwEncryptionSpiAuthKey1_Type()
)
aluMcPeerFwEncryptionSpiAuthKey1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwEncryptionSpiAuthKey1.setStatus("current")


class _AluMcPeerFwEncryptionSpiEncrKey1_Type(OctetString):
    """Custom type aluMcPeerFwEncryptionSpiEncrKey1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AluMcPeerFwEncryptionSpiEncrKey1_Type.__name__ = "OctetString"
_AluMcPeerFwEncryptionSpiEncrKey1_Object = MibTableColumn
aluMcPeerFwEncryptionSpiEncrKey1 = _AluMcPeerFwEncryptionSpiEncrKey1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 18),
    _AluMcPeerFwEncryptionSpiEncrKey1_Type()
)
aluMcPeerFwEncryptionSpiEncrKey1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwEncryptionSpiEncrKey1.setStatus("current")


class _AluMcPeerFwEncryptionSpi2_Type(Unsigned32):
    """Custom type aluMcPeerFwEncryptionSpi2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AluMcPeerFwEncryptionSpi2_Type.__name__ = "Unsigned32"
_AluMcPeerFwEncryptionSpi2_Object = MibTableColumn
aluMcPeerFwEncryptionSpi2 = _AluMcPeerFwEncryptionSpi2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 19),
    _AluMcPeerFwEncryptionSpi2_Type()
)
aluMcPeerFwEncryptionSpi2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwEncryptionSpi2.setStatus("current")


class _AluMcPeerFwEncryptionSpiAuthKey2_Type(OctetString):
    """Custom type aluMcPeerFwEncryptionSpiAuthKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AluMcPeerFwEncryptionSpiAuthKey2_Type.__name__ = "OctetString"
_AluMcPeerFwEncryptionSpiAuthKey2_Object = MibTableColumn
aluMcPeerFwEncryptionSpiAuthKey2 = _AluMcPeerFwEncryptionSpiAuthKey2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 20),
    _AluMcPeerFwEncryptionSpiAuthKey2_Type()
)
aluMcPeerFwEncryptionSpiAuthKey2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwEncryptionSpiAuthKey2.setStatus("current")


class _AluMcPeerFwEncryptionSpiEncrKey2_Type(OctetString):
    """Custom type aluMcPeerFwEncryptionSpiEncrKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AluMcPeerFwEncryptionSpiEncrKey2_Type.__name__ = "OctetString"
_AluMcPeerFwEncryptionSpiEncrKey2_Object = MibTableColumn
aluMcPeerFwEncryptionSpiEncrKey2 = _AluMcPeerFwEncryptionSpiEncrKey2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 21),
    _AluMcPeerFwEncryptionSpiEncrKey2_Type()
)
aluMcPeerFwEncryptionSpiEncrKey2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMcPeerFwEncryptionSpiEncrKey2.setStatus("current")


class _AluMcPeerFwElectionRole_Type(Integer32):
    """Custom type aluMcPeerFwElectionRole based on Integer32"""
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
        *(("not-applicable", 0),
          ("master", 1),
          ("slave", 2),
          ("standalone-master", 3))
    )


_AluMcPeerFwElectionRole_Type.__name__ = "Integer32"
_AluMcPeerFwElectionRole_Object = MibTableColumn
aluMcPeerFwElectionRole = _AluMcPeerFwElectionRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 22),
    _AluMcPeerFwElectionRole_Type()
)
aluMcPeerFwElectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcPeerFwElectionRole.setStatus("current")


class _AluMcPeerFwPolicySync_Type(Integer32):
    """Custom type aluMcPeerFwPolicySync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("synced", 1),
          ("out-of-sync", 2))
    )


_AluMcPeerFwPolicySync_Type.__name__ = "Integer32"
_AluMcPeerFwPolicySync_Object = MibTableColumn
aluMcPeerFwPolicySync = _AluMcPeerFwPolicySync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 23),
    _AluMcPeerFwPolicySync_Type()
)
aluMcPeerFwPolicySync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcPeerFwPolicySync.setStatus("current")


class _AluMcPeerFwSessionDBSync_Type(Integer32):
    """Custom type aluMcPeerFwSessionDBSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("synced", 1),
          ("out-of-sync", 2))
    )


_AluMcPeerFwSessionDBSync_Type.__name__ = "Integer32"
_AluMcPeerFwSessionDBSync_Object = MibTableColumn
aluMcPeerFwSessionDBSync = _AluMcPeerFwSessionDBSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 6, 2, 1, 24),
    _AluMcPeerFwSessionDBSync_Type()
)
aluMcPeerFwSessionDBSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcPeerFwSessionDBSync.setStatus("current")
_AluSecMcRedStatsObjs_ObjectIdentity = ObjectIdentity
aluSecMcRedStatsObjs = _AluSecMcRedStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7)
)
_AluMcFwPeerStatsTable_Object = MibTable
aluMcFwPeerStatsTable = _AluMcFwPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1)
)
if mibBuilder.loadTexts:
    aluMcFwPeerStatsTable.setStatus("current")
_AluMcFwPeerStatsEntry_Object = MibTableRow
aluMcFwPeerStatsEntry = _AluMcFwPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1)
)
aluMcFwPeerStatsEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    aluMcFwPeerStatsEntry.setStatus("current")
_AluMcFwPeerStatsPktsRx_Type = Counter32
_AluMcFwPeerStatsPktsRx_Object = MibTableColumn
aluMcFwPeerStatsPktsRx = _AluMcFwPeerStatsPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 1),
    _AluMcFwPeerStatsPktsRx_Type()
)
aluMcFwPeerStatsPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsPktsRx.setStatus("current")
_AluMcFwPeerStatsPktsRxKpalive_Type = Counter32
_AluMcFwPeerStatsPktsRxKpalive_Object = MibTableColumn
aluMcFwPeerStatsPktsRxKpalive = _AluMcFwPeerStatsPktsRxKpalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 2),
    _AluMcFwPeerStatsPktsRxKpalive_Type()
)
aluMcFwPeerStatsPktsRxKpalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsPktsRxKpalive.setStatus("current")
_AluMcFwPeerStatsPktsRxPeerCfg_Type = Counter32
_AluMcFwPeerStatsPktsRxPeerCfg_Object = MibTableColumn
aluMcFwPeerStatsPktsRxPeerCfg = _AluMcFwPeerStatsPktsRxPeerCfg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 3),
    _AluMcFwPeerStatsPktsRxPeerCfg_Type()
)
aluMcFwPeerStatsPktsRxPeerCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsPktsRxPeerCfg.setStatus("current")
_AluMcFwPeerStatsPktsRxPeerData_Type = Counter32
_AluMcFwPeerStatsPktsRxPeerData_Object = MibTableColumn
aluMcFwPeerStatsPktsRxPeerData = _AluMcFwPeerStatsPktsRxPeerData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 4),
    _AluMcFwPeerStatsPktsRxPeerData_Type()
)
aluMcFwPeerStatsPktsRxPeerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsPktsRxPeerData.setStatus("current")
_AluMcFwPeerStatsDropRxPeerData_Type = Counter32
_AluMcFwPeerStatsDropRxPeerData_Object = MibTableColumn
aluMcFwPeerStatsDropRxPeerData = _AluMcFwPeerStatsDropRxPeerData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 5),
    _AluMcFwPeerStatsDropRxPeerData_Type()
)
aluMcFwPeerStatsDropRxPeerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsDropRxPeerData.setStatus("current")
_AluMcFwPeerStatsDropStateDsbld_Type = Counter32
_AluMcFwPeerStatsDropStateDsbld_Object = MibTableColumn
aluMcFwPeerStatsDropStateDsbld = _AluMcFwPeerStatsDropStateDsbld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 6),
    _AluMcFwPeerStatsDropStateDsbld_Type()
)
aluMcFwPeerStatsDropStateDsbld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsDropStateDsbld.setStatus("current")
_AluMcFwPeerStatsDropPktTooShrt_Type = Counter32
_AluMcFwPeerStatsDropPktTooShrt_Object = MibTableColumn
aluMcFwPeerStatsDropPktTooShrt = _AluMcFwPeerStatsDropPktTooShrt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 7),
    _AluMcFwPeerStatsDropPktTooShrt_Type()
)
aluMcFwPeerStatsDropPktTooShrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsDropPktTooShrt.setStatus("current")
_AluMcFwPeerStatsDropTlvInvldSz_Type = Counter32
_AluMcFwPeerStatsDropTlvInvldSz_Object = MibTableColumn
aluMcFwPeerStatsDropTlvInvldSz = _AluMcFwPeerStatsDropTlvInvldSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 8),
    _AluMcFwPeerStatsDropTlvInvldSz_Type()
)
aluMcFwPeerStatsDropTlvInvldSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsDropTlvInvldSz.setStatus("current")
_AluMcFwPeerStatsDropOutOfSeq_Type = Counter32
_AluMcFwPeerStatsDropOutOfSeq_Object = MibTableColumn
aluMcFwPeerStatsDropOutOfSeq = _AluMcFwPeerStatsDropOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 9),
    _AluMcFwPeerStatsDropOutOfSeq_Type()
)
aluMcFwPeerStatsDropOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsDropOutOfSeq.setStatus("current")
_AluMcFwPeerStatsDropUnknownTlv_Type = Counter32
_AluMcFwPeerStatsDropUnknownTlv_Object = MibTableColumn
aluMcFwPeerStatsDropUnknownTlv = _AluMcFwPeerStatsDropUnknownTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 10),
    _AluMcFwPeerStatsDropUnknownTlv_Type()
)
aluMcFwPeerStatsDropUnknownTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsDropUnknownTlv.setStatus("current")
_AluMcFwPeerStatsDropMD5_Type = Counter32
_AluMcFwPeerStatsDropMD5_Object = MibTableColumn
aluMcFwPeerStatsDropMD5 = _AluMcFwPeerStatsDropMD5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 11),
    _AluMcFwPeerStatsDropMD5_Type()
)
aluMcFwPeerStatsDropMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsDropMD5.setStatus("current")
_AluMcFwPeerStatsPktsTx_Type = Counter32
_AluMcFwPeerStatsPktsTx_Object = MibTableColumn
aluMcFwPeerStatsPktsTx = _AluMcFwPeerStatsPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 12),
    _AluMcFwPeerStatsPktsTx_Type()
)
aluMcFwPeerStatsPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsPktsTx.setStatus("current")
_AluMcFwPeerStatsPktsTxKpalive_Type = Counter32
_AluMcFwPeerStatsPktsTxKpalive_Object = MibTableColumn
aluMcFwPeerStatsPktsTxKpalive = _AluMcFwPeerStatsPktsTxKpalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 13),
    _AluMcFwPeerStatsPktsTxKpalive_Type()
)
aluMcFwPeerStatsPktsTxKpalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsPktsTxKpalive.setStatus("current")
_AluMcFwPeerStatsPktsTxPeerCfg_Type = Counter32
_AluMcFwPeerStatsPktsTxPeerCfg_Object = MibTableColumn
aluMcFwPeerStatsPktsTxPeerCfg = _AluMcFwPeerStatsPktsTxPeerCfg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 14),
    _AluMcFwPeerStatsPktsTxPeerCfg_Type()
)
aluMcFwPeerStatsPktsTxPeerCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsPktsTxPeerCfg.setStatus("current")
_AluMcFwPeerStatsPktsTxPeerData_Type = Counter32
_AluMcFwPeerStatsPktsTxPeerData_Object = MibTableColumn
aluMcFwPeerStatsPktsTxPeerData = _AluMcFwPeerStatsPktsTxPeerData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 15),
    _AluMcFwPeerStatsPktsTxPeerData_Type()
)
aluMcFwPeerStatsPktsTxPeerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsPktsTxPeerData.setStatus("current")
_AluMcFwPeerStatsPktsTxFailed_Type = Counter32
_AluMcFwPeerStatsPktsTxFailed_Object = MibTableColumn
aluMcFwPeerStatsPktsTxFailed = _AluMcFwPeerStatsPktsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 16),
    _AluMcFwPeerStatsPktsTxFailed_Type()
)
aluMcFwPeerStatsPktsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsPktsTxFailed.setStatus("current")
_AluMcFwPeerStatsDropFwNoPeer_Type = Counter32
_AluMcFwPeerStatsDropFwNoPeer_Object = MibTableColumn
aluMcFwPeerStatsDropFwNoPeer = _AluMcFwPeerStatsDropFwNoPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 1, 1, 17),
    _AluMcFwPeerStatsDropFwNoPeer_Type()
)
aluMcFwPeerStatsDropFwNoPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwPeerStatsDropFwNoPeer.setStatus("current")
_AluMcFwGlobalStats_ObjectIdentity = ObjectIdentity
aluMcFwGlobalStats = _AluMcFwGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2)
)
_AluMcFwStatsPktsRx_Type = Counter32
_AluMcFwStatsPktsRx_Object = MibScalar
aluMcFwStatsPktsRx = _AluMcFwStatsPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 1),
    _AluMcFwStatsPktsRx_Type()
)
aluMcFwStatsPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsPktsRx.setStatus("current")
_AluMcFwStatsPktsRxKeepalive_Type = Counter32
_AluMcFwStatsPktsRxKeepalive_Object = MibScalar
aluMcFwStatsPktsRxKeepalive = _AluMcFwStatsPktsRxKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 2),
    _AluMcFwStatsPktsRxKeepalive_Type()
)
aluMcFwStatsPktsRxKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsPktsRxKeepalive.setStatus("current")
_AluMcFwStatsPktsRxPeerConfig_Type = Counter32
_AluMcFwStatsPktsRxPeerConfig_Object = MibScalar
aluMcFwStatsPktsRxPeerConfig = _AluMcFwStatsPktsRxPeerConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 3),
    _AluMcFwStatsPktsRxPeerConfig_Type()
)
aluMcFwStatsPktsRxPeerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsPktsRxPeerConfig.setStatus("current")
_AluMcFwStatsPktsRxPeerData_Type = Counter32
_AluMcFwStatsPktsRxPeerData_Object = MibScalar
aluMcFwStatsPktsRxPeerData = _AluMcFwStatsPktsRxPeerData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 4),
    _AluMcFwStatsPktsRxPeerData_Type()
)
aluMcFwStatsPktsRxPeerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsPktsRxPeerData.setStatus("current")
_AluMcFwStatsDropRxPeerData_Type = Counter32
_AluMcFwStatsDropRxPeerData_Object = MibScalar
aluMcFwStatsDropRxPeerData = _AluMcFwStatsDropRxPeerData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 5),
    _AluMcFwStatsDropRxPeerData_Type()
)
aluMcFwStatsDropRxPeerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsDropRxPeerData.setStatus("current")
_AluMcFwStatsDropPktKpaliveTask_Type = Counter32
_AluMcFwStatsDropPktKpaliveTask_Object = MibScalar
aluMcFwStatsDropPktKpaliveTask = _AluMcFwStatsDropPktKpaliveTask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 6),
    _AluMcFwStatsDropPktKpaliveTask_Type()
)
aluMcFwStatsDropPktKpaliveTask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsDropPktKpaliveTask.setStatus("current")
_AluMcFwStatsDropPktTooShort_Type = Counter32
_AluMcFwStatsDropPktTooShort_Object = MibScalar
aluMcFwStatsDropPktTooShort = _AluMcFwStatsDropPktTooShort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 7),
    _AluMcFwStatsDropPktTooShort_Type()
)
aluMcFwStatsDropPktTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsDropPktTooShort.setStatus("current")
_AluMcFwStatsDropPktVerifyFailed_Type = Counter32
_AluMcFwStatsDropPktVerifyFailed_Object = MibScalar
aluMcFwStatsDropPktVerifyFailed = _AluMcFwStatsDropPktVerifyFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 8),
    _AluMcFwStatsDropPktVerifyFailed_Type()
)
aluMcFwStatsDropPktVerifyFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsDropPktVerifyFailed.setStatus("current")
_AluMcFwStatsDropTlvInvalidSize_Type = Counter32
_AluMcFwStatsDropTlvInvalidSize_Object = MibScalar
aluMcFwStatsDropTlvInvalidSize = _AluMcFwStatsDropTlvInvalidSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 9),
    _AluMcFwStatsDropTlvInvalidSize_Type()
)
aluMcFwStatsDropTlvInvalidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsDropTlvInvalidSize.setStatus("current")
_AluMcFwStatsDropOutOfSeq_Type = Counter32
_AluMcFwStatsDropOutOfSeq_Object = MibScalar
aluMcFwStatsDropOutOfSeq = _AluMcFwStatsDropOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 10),
    _AluMcFwStatsDropOutOfSeq_Type()
)
aluMcFwStatsDropOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsDropOutOfSeq.setStatus("current")
_AluMcFwStatsDropUnknownTlv_Type = Counter32
_AluMcFwStatsDropUnknownTlv_Object = MibScalar
aluMcFwStatsDropUnknownTlv = _AluMcFwStatsDropUnknownTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 11),
    _AluMcFwStatsDropUnknownTlv_Type()
)
aluMcFwStatsDropUnknownTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsDropUnknownTlv.setStatus("current")
_AluMcFwStatsDropMD5_Type = Counter32
_AluMcFwStatsDropMD5_Object = MibScalar
aluMcFwStatsDropMD5 = _AluMcFwStatsDropMD5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 12),
    _AluMcFwStatsDropMD5_Type()
)
aluMcFwStatsDropMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsDropMD5.setStatus("current")
_AluMcFwStatsDropUnknownPeer_Type = Counter32
_AluMcFwStatsDropUnknownPeer_Object = MibScalar
aluMcFwStatsDropUnknownPeer = _AluMcFwStatsDropUnknownPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 13),
    _AluMcFwStatsDropUnknownPeer_Type()
)
aluMcFwStatsDropUnknownPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsDropUnknownPeer.setStatus("current")
_AluMcFwStatsPktsTx_Type = Counter32
_AluMcFwStatsPktsTx_Object = MibScalar
aluMcFwStatsPktsTx = _AluMcFwStatsPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 14),
    _AluMcFwStatsPktsTx_Type()
)
aluMcFwStatsPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsPktsTx.setStatus("current")
_AluMcFwStatsPktsTxKeepalive_Type = Counter32
_AluMcFwStatsPktsTxKeepalive_Object = MibScalar
aluMcFwStatsPktsTxKeepalive = _AluMcFwStatsPktsTxKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 15),
    _AluMcFwStatsPktsTxKeepalive_Type()
)
aluMcFwStatsPktsTxKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsPktsTxKeepalive.setStatus("current")
_AluMcFwStatsPktsTxPeerConfig_Type = Counter32
_AluMcFwStatsPktsTxPeerConfig_Object = MibScalar
aluMcFwStatsPktsTxPeerConfig = _AluMcFwStatsPktsTxPeerConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 16),
    _AluMcFwStatsPktsTxPeerConfig_Type()
)
aluMcFwStatsPktsTxPeerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsPktsTxPeerConfig.setStatus("current")
_AluMcFwStatsPktsTxPeerData_Type = Counter32
_AluMcFwStatsPktsTxPeerData_Object = MibScalar
aluMcFwStatsPktsTxPeerData = _AluMcFwStatsPktsTxPeerData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 17),
    _AluMcFwStatsPktsTxPeerData_Type()
)
aluMcFwStatsPktsTxPeerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsPktsTxPeerData.setStatus("current")
_AluMcFwStatsPktsTxFailed_Type = Counter32
_AluMcFwStatsPktsTxFailed_Object = MibScalar
aluMcFwStatsPktsTxFailed = _AluMcFwStatsPktsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 18),
    _AluMcFwStatsPktsTxFailed_Type()
)
aluMcFwStatsPktsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsPktsTxFailed.setStatus("current")
_AluMcFwStatsDropFwNoPeer_Type = Counter32
_AluMcFwStatsDropFwNoPeer_Object = MibScalar
aluMcFwStatsDropFwNoPeer = _AluMcFwStatsDropFwNoPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 7, 2, 19),
    _AluMcFwStatsDropFwNoPeer_Type()
)
aluMcFwStatsDropFwNoPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMcFwStatsDropFwNoPeer.setStatus("current")
_AluSecMcRedNotifObjs_ObjectIdentity = ObjectIdentity
aluSecMcRedNotifObjs = _AluSecMcRedNotifObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 8)
)


class _AluMcPeerFwBfdSessionOpenStatus_Type(Integer32):
    """Custom type aluMcPeerFwBfdSessionOpenStatus based on Integer32"""
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
        *(("ok", 0),
          ("invalidSrcAddr", 1),
          ("nonSysLoopbackIf", 2),
          ("clientUseSessionFail", 3),
          ("clientAppUseIfFail", 4))
    )


_AluMcPeerFwBfdSessionOpenStatus_Type.__name__ = "Integer32"
_AluMcPeerFwBfdSessionOpenStatus_Object = MibScalar
aluMcPeerFwBfdSessionOpenStatus = _AluMcPeerFwBfdSessionOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 17, 8, 1),
    _AluMcPeerFwBfdSessionOpenStatus_Type()
)
aluMcPeerFwBfdSessionOpenStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMcPeerFwBfdSessionOpenStatus.setStatus("current")
_AluSecurityNotifyPrefix_ObjectIdentity = ObjectIdentity
aluSecurityNotifyPrefix = _AluSecurityNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14)
)
_AluSecurityNotification_ObjectIdentity = ObjectIdentity
aluSecurityNotification = _AluSecurityNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0)
)

# Managed Objects groups

aluSecPlcyAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 2, 1)
)
aluSecPlcyAdminGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecPlcyAdminControlApply"),
        ("ALU-SECURITY-MIB", "aluSecPlcyBypass"),
        ("ALU-SECURITY-MIB", "aluSecPlcyLastCommit"),
        ("ALU-SECURITY-MIB", "aluSecPlcyCount"),
        ("ALU-SECURITY-MIB", "aluSecPlcyProfileCount"),
        ("ALU-SECURITY-MIB", "aluSecPlcyZoneCount"),
        ("ALU-SECURITY-MIB", "aluSecActiveSessionCount"),
        ("ALU-SECURITY-MIB", "aluSecActiveSessionLimit"),
        ("ALU-SECURITY-MIB", "aluSecActiveSessionHiWtrMrk"),
        ("ALU-SECURITY-MIB", "aluSecActiveSessionLoWtrMrk"),
        ("ALU-SECURITY-MIB", "aluSecPlcyState"),
        ("ALU-SECURITY-MIB", "aluSecSessionResourceState"))
)
if mibBuilder.loadTexts:
    aluSecPlcyAdminGroup.setStatus("current")

aluZonePlcyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 2, 2)
)
aluZonePlcyConfigGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluZoneConfigName"),
        ("ALU-SECURITY-MIB", "aluZoneConfigRowStatus"),
        ("ALU-SECURITY-MIB", "aluZoneConfigDescription"),
        ("ALU-SECURITY-MIB", "aluZoneConfigControlApply"),
        ("ALU-SECURITY-MIB", "aluZoneConfigType"),
        ("ALU-SECURITY-MIB", "aluZoneConfigSvcId"),
        ("ALU-SECURITY-MIB", "aluZoneConfigState"),
        ("ALU-SECURITY-MIB", "aluZoneConfigBypass"),
        ("ALU-SECURITY-MIB", "aluZonePlcyConfigRowStatus"),
        ("ALU-SECURITY-MIB", "aluZonePlcyConfigSecPlcyId"))
)
if mibBuilder.loadTexts:
    aluZonePlcyConfigGroup.setStatus("current")

aluSecPlcyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 2, 3)
)
aluSecPlcyConfigGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecPlcyConfigRowStatus"),
        ("ALU-SECURITY-MIB", "aluSecPlcyConfigName"),
        ("ALU-SECURITY-MIB", "aluSecPlcyConfigDescription"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigRowStatus"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigDescription"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchSrcIPAddrValue1"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchSrcIPAddrValue2"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchSrcIPOperator"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchSrcIPHostGroup"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchDstIPAddrValue1"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchDstIPAddrValue2"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchDstIPOperator"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchDstIPHostGroup"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchProtocol"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchSrcPortValue1"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchSrcPortValue2"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchSrcPortOp"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchDstPortValue1"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchDstPortValue2"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchDstPortOp"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchAppGroup"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchIcmpCode"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchIcmpType"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchIgmpType"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchFlowDirection"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigProfileId"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigConcurrentFlowLimit"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigCreateRevDirFlow"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigAction"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolConfigName"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolConfigRowStatus"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolConfigDescription"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolConfigType"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolConfigDirection"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsConfigRowStatus"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsConfigIPAddrValue1"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsConfigIPAddrValue2"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsConfigIPOperator"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsConfigIPInterfaceIndex"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsConfigPortOperator"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsConfigPortValue1"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsConfigPortValue2"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigRowStatus"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigName"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigDescription"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigTcpSynTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigTcpWaitTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigTcpTransTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigTcpEstTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigUdpTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigUdpInitTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigUdpDnsTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigIcmpTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigOtherTimeout"))
)
if mibBuilder.loadTexts:
    aluSecPlcyConfigGroup.setStatus("current")

aluSecPlcyDstNatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 2, 4)
)
aluSecPlcyDstNatGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigMatchLocal"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigActionNatDstIPAddr"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigActionNatDstPort"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchLocal"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperActionNatDstIPAddr"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperActionNatDstPort"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionNatDstIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionNatDstPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionNatDstIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionNatDstPortValue"))
)
if mibBuilder.loadTexts:
    aluSecPlcyDstNatGroup.setStatus("current")

aluSecFirewallAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 2, 5)
)
aluSecFirewallAdminGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecProfileConfigAppInspect"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigInspectTcp"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigInspectIpOpt"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigAllowedIpOpt"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigAllowPktFrag"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigAlg"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigIcmpReqLimit"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigIcmpErrLimit"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigDnsReplyOnly"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigTcpTmoStrict"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigUdpTmoStrict"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigIcmpTmoStrict"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigDnsTmoStrict"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigOthTmoStrict"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigFwdPolicerId"),
        ("ALU-SECURITY-MIB", "aluSecProfileConfigRevPolicerId"),
        ("ALU-SECURITY-MIB", "aluZoneConfigInTcpSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneConfigInUdpSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneConfigInIcmpSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneConfigInOthSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneConfigOutTcpSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneConfigOutUdpSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneConfigOutIcmpSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneConfigOutOthSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneConfigLogId"),
        ("ALU-SECURITY-MIB", "aluZoneConfigAutoBind"))
)
if mibBuilder.loadTexts:
    aluSecFirewallAdminGroup.setStatus("current")

aluSecGroupConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 2, 6)
)
aluSecGroupConfigGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecHostGrpConfigRowStatus"),
        ("ALU-SECURITY-MIB", "aluSecHostGrpConfigName"),
        ("ALU-SECURITY-MIB", "aluSecHostGrpConfigDescription"),
        ("ALU-SECURITY-MIB", "aluSecHostConfigRowStatus"),
        ("ALU-SECURITY-MIB", "aluSecHostConfigIPAddrValue2"),
        ("ALU-SECURITY-MIB", "aluSecHostConfigIPOperator"),
        ("ALU-SECURITY-MIB", "aluSecAppGrpConfigRowStatus"),
        ("ALU-SECURITY-MIB", "aluSecAppGrpConfigName"),
        ("ALU-SECURITY-MIB", "aluSecAppGrpConfigDescription"),
        ("ALU-SECURITY-MIB", "aluSecAppConfigRowStatus"),
        ("ALU-SECURITY-MIB", "aluSecAppConfigMatchProtocol"),
        ("ALU-SECURITY-MIB", "aluSecAppConfigMatchSrcPortValue1"),
        ("ALU-SECURITY-MIB", "aluSecAppConfigMatchSrcPortValue2"),
        ("ALU-SECURITY-MIB", "aluSecAppConfigMatchSrcPortOp"),
        ("ALU-SECURITY-MIB", "aluSecAppConfigMatchDstPortValue1"),
        ("ALU-SECURITY-MIB", "aluSecAppConfigMatchDstPortValue2"),
        ("ALU-SECURITY-MIB", "aluSecAppConfigMatchDstPortOp"),
        ("ALU-SECURITY-MIB", "aluSecAppConfigMatchIcmpCode"),
        ("ALU-SECURITY-MIB", "aluSecAppConfigMatchIcmpType"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpConfigRowStatus"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpConfigName"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpConfigDescription"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpConfigRate"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpConfigRateCbs"))
)
if mibBuilder.loadTexts:
    aluSecGroupConfigGroup.setStatus("current")

aluSecLogObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 3, 1)
)
aluSecLogObjsGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecLogName"),
        ("ALU-SECURITY-MIB", "aluSecLogRowStatus"),
        ("ALU-SECURITY-MIB", "aluSecLogDescription"),
        ("ALU-SECURITY-MIB", "aluSecLogEnabled"),
        ("ALU-SECURITY-MIB", "aluSecLogDestination"),
        ("ALU-SECURITY-MIB", "aluSecLogMemSize"),
        ("ALU-SECURITY-MIB", "aluSecLogMemWrap"),
        ("ALU-SECURITY-MIB", "aluSecLogSysLogId"),
        ("ALU-SECURITY-MIB", "aluSecLogLogProfileId"),
        ("ALU-SECURITY-MIB", "aluSecLogApplied"),
        ("ALU-SECURITY-MIB", "aluSecLogNextEventNum"),
        ("ALU-SECURITY-MIB", "aluSecLogEventName"),
        ("ALU-SECURITY-MIB", "aluSecLogEventControl"),
        ("ALU-SECURITY-MIB", "aluSecLogProfileName"),
        ("ALU-SECURITY-MIB", "aluSecLogProfileRowStatus"),
        ("ALU-SECURITY-MIB", "aluSecLogProfileDescription"),
        ("ALU-SECURITY-MIB", "aluSecLogProfileApplied"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigLogControl"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsConfigLogId"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperLogControl"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperLogId"))
)
if mibBuilder.loadTexts:
    aluSecLogObjsGroup.setStatus("current")

aluMcPeerFwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 4, 1)
)
aluMcPeerFwGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluMcPeerFwAdminState"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwBootTimer"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwHoldOnNbrFail"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwKeepAliveIntvl"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwLastChanged"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwRefCount"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwBfd"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwRowStatus"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwSysPriority"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwTableLastChanged"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsDropMD5"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsDropRxPeerData"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsDropOutOfSeq"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsDropPktTooShrt"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsDropStateDsbld"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsDropTlvInvldSz"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsDropUnknownTlv"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsPktsRx"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsPktsRxKpalive"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsPktsRxPeerCfg"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsPktsRxPeerData"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsPktsTx"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsPktsTxFailed"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsPktsTxKpalive"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsPktsTxPeerCfg"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsPktsTxPeerData"),
        ("ALU-SECURITY-MIB", "aluMcFwPeerStatsDropFwNoPeer"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwOperState"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwPeerLastStateChge"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsDropFwNoPeer"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsDropMD5"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsDropOutOfSeq"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsDropPktKpaliveTask"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsDropRxPeerData"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsDropPktTooShort"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsDropPktVerifyFailed"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsDropTlvInvalidSize"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsDropUnknownPeer"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsDropUnknownTlv"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsPktsRx"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsPktsRxKeepalive"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsPktsRxPeerConfig"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsPktsRxPeerData"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsPktsTx"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsPktsTxFailed"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsPktsTxKeepalive"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsPktsTxPeerConfig"),
        ("ALU-SECURITY-MIB", "aluMcFwStatsPktsTxPeerData"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwRefCount"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwEncryption"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwEncryptionAuthAlg"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwEncryptionEncrAlg"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwEncryptionActOutSa"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwEncryptionSpi1"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwEncryptionSpiAuthKey1"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwEncryptionSpiEncrKey1"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwEncryptionSpi2"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwEncryptionSpiAuthKey2"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwEncryptionSpiEncrKey2"))
)
if mibBuilder.loadTexts:
    aluMcPeerFwGroup.setStatus("current")

aluMcPeerFwNotifyObjsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 4, 2)
)
aluMcPeerFwNotifyObjsV7v0Group.setObjects(
    ("ALU-SECURITY-MIB", "aluMcPeerFwBfdSessionOpenStatus")
)
if mibBuilder.loadTexts:
    aluMcPeerFwNotifyObjsV7v0Group.setStatus("current")

aluZoneOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2, 2, 1)
)
aluZoneOperGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluZoneOperName"),
        ("ALU-SECURITY-MIB", "aluZoneOperDescription"),
        ("ALU-SECURITY-MIB", "aluZoneOperPlcyRuleCount"),
        ("ALU-SECURITY-MIB", "aluZoneOperType"),
        ("ALU-SECURITY-MIB", "aluZoneOperSvcId"),
        ("ALU-SECURITY-MIB", "aluZoneOperBypass"),
        ("ALU-SECURITY-MIB", "aluZoneOperInSessionCount"),
        ("ALU-SECURITY-MIB", "aluZoneOperInActiveSessions"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutSessionCount"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutActiveSessions"),
        ("ALU-SECURITY-MIB", "aluZoneOperInPktsDropped"),
        ("ALU-SECURITY-MIB", "aluZoneOperInBytesDropped"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutPktsDropped"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutBytesDropped"),
        ("ALU-SECURITY-MIB", "aluZoneOperInPktsDefAction"),
        ("ALU-SECURITY-MIB", "aluZoneOperInBytesDefAction"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutPktsDefAction"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutBytesDefAction"),
        ("ALU-SECURITY-MIB", "aluZoneOperPlcyLastCommit"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperEntryId"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperActive"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperFlags"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperSecPlcyId"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperSecPlcyRuleId"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperNatPoolId"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperRuleHitCount"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperRuleActiveSessions"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionProtocol"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionSrcZoneId"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionSrcIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionSrcPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionDstIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionDstPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionRevDirCreated"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionAction"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionNatSrcIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionNatSrcPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionEstablished"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionProtocol"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionDstZoneId"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionSrcIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionSrcPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionDstIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionDstPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionRevDirCreated"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionAction"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionNatSrcIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionNatSrcPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionEstablished"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperName"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperDescription"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperPlcyRefCount"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperTcpSynTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperTcpWaitTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperTcpTransTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperTcpEstTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperUdpTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperUdpInitTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperUdpDnsTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperIcmpTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperOtherTimeout"))
)
if mibBuilder.loadTexts:
    aluZoneOperGroup.setStatus("obsolete")

aluSecPlcyOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2, 2, 2)
)
aluSecPlcyOperGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecPlcyOperName"),
        ("ALU-SECURITY-MIB", "aluSecPlcyOperDescription"),
        ("ALU-SECURITY-MIB", "aluSecPlcyOperRuleCount"),
        ("ALU-SECURITY-MIB", "aluSecPlcyOperZoneRefCount"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperDescription"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchSrcIPAddrValue1"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchSrcIPAddrValue2"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchSrcIPOperator"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchSrcIPHostGroup"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchDstIPAddrValue1"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchDstIPAddrValue2"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchDstIPOperator"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchDstIPHostGroup"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchProtocol"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchSrcPortValue1"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchSrcPortValue2"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchSrcPortOp"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchDstPortValue1"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchDstPortValue2"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchDstPortOp"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchAppGroup"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchIcmpCode"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchIcmpType"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchIgmpType"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperMatchFlowDirection"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperProfileId"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperConcurrentFlowLimit"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperCreateRevDirFlow"),
        ("ALU-SECURITY-MIB", "aluSecPlcyParamsOperAction"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolOperName"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolOperDescription"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolOperType"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolOperDirection"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsOperIPAddrValue1"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsOperIPAddrValue2"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsOperIPOperator"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsOperIPInterfaceIndex"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsOperPortOperator"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsOperPortValue1"),
        ("ALU-SECURITY-MIB", "aluZoneNatPoolParamsOperPortValue2"))
)
if mibBuilder.loadTexts:
    aluSecPlcyOperGroup.setStatus("current")

aluSecStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2, 2, 3)
)
aluSecStatsGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecSessionOutboundZoneId"),
        ("ALU-SECURITY-MIB", "aluSecSessionInboundZoneId"),
        ("ALU-SECURITY-MIB", "aluSecSessionFwdPktsPassed"),
        ("ALU-SECURITY-MIB", "aluSecSessionFwdBytesPassed"),
        ("ALU-SECURITY-MIB", "aluSecSessionRevPktsPassed"),
        ("ALU-SECURITY-MIB", "aluSecSessionRevBytesPassed"))
)
if mibBuilder.loadTexts:
    aluSecStatsGroup.setStatus("current")

aluSecFirewallOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2, 2, 4)
)
aluSecFirewallOperGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecProfileOperAppInspect"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperInspectTcp"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperInspectIpOpt"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperAllowedIpOpt"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperAllowPktFrag"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperAlg"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperIcmpReqLimit"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperIcmpErrLimit"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperDnsReplyOnly"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperTcpTmoStrict"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperUdpTmoStrict"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperIcmpTmoStrict"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperDnsTmoStrict"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperOthTmoStrict"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperFwdPolicerId"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperRevPolicerId"),
        ("ALU-SECURITY-MIB", "aluZoneOperInTcpSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneOperInUdpSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneOperInIcmpSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneOperInOthSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneOperInTcpActSessions"),
        ("ALU-SECURITY-MIB", "aluZoneOperInUdpActSessions"),
        ("ALU-SECURITY-MIB", "aluZoneOperInIcmpActSessions"),
        ("ALU-SECURITY-MIB", "aluZoneOperInOthActSessions"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutTcpSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutUdpSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutIcmpSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutOthSessLimit"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutTcpActSessions"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutUdpActSessions"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutIcmpActSessions"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutOthActSessions"),
        ("ALU-SECURITY-MIB", "aluZoneOperLogId"),
        ("ALU-SECURITY-MIB", "aluZoneOperAutoBind"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionAlg"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionInspect"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionCreator"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionAlg"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionInspect"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionFwdPolicerId"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionRevPolicerId"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionFwdPolicerId"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionRevPolicerId"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionCreator"))
)
if mibBuilder.loadTexts:
    aluSecFirewallOperGroup.setStatus("current")

aluSecStatsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2, 2, 5)
)
aluSecStatsV7v0Group.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecZoneRxCtrlQueueFwdPkts"),
        ("ALU-SECURITY-MIB", "aluSecZoneRxCtrlQueueFwdBytes"),
        ("ALU-SECURITY-MIB", "aluSecZoneRxCtrlQueueDroPkts"),
        ("ALU-SECURITY-MIB", "aluSecZoneRxCtrlQueueDroBytes"),
        ("ALU-SECURITY-MIB", "aluSecZoneRxCtrlQueueAutoBind"),
        ("ALU-SECURITY-MIB", "aluSecSessionFwdDropActionPkts"),
        ("ALU-SECURITY-MIB", "aluSecSessionFwdDropIpOptPkts"),
        ("ALU-SECURITY-MIB", "aluSecSessionRevDropIpOptPkts"),
        ("ALU-SECURITY-MIB", "aluSecSessionFwdDropMaxPkts"),
        ("ALU-SECURITY-MIB", "aluSecSessionRevDropMaxPkts"),
        ("ALU-SECURITY-MIB", "aluSecSessionFwdDropMaxIcmpErr"),
        ("ALU-SECURITY-MIB", "aluSecSessionRevDropMaxIcmpErr"),
        ("ALU-SECURITY-MIB", "aluSecSessionFwdSecurityDrop"),
        ("ALU-SECURITY-MIB", "aluSecSessionRevSecurityDrop"),
        ("ALU-SECURITY-MIB", "aluSecSessionFwdPolicerDrop"),
        ("ALU-SECURITY-MIB", "aluSecSessionRevPolicerDrop"),
        ("ALU-SECURITY-MIB", "aluSecEngineUtilization"),
        ("ALU-SECURITY-MIB", "aluSecEngineRxQueueCtrlPkts"),
        ("ALU-SECURITY-MIB", "aluSecEngineRxQueueDataPkts"),
        ("ALU-SECURITY-MIB", "aluSecEngineRxQueueDropPkts"),
        ("ALU-SECURITY-MIB", "aluSecEngineDropPkts"),
        ("ALU-SECURITY-MIB", "aluSecTotalSessionCount"),
        ("ALU-SECURITY-MIB", "aluSecSessionRevDropActionPkts"))
)
if mibBuilder.loadTexts:
    aluSecStatsV7v0Group.setStatus("current")

aluSecGroupOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2, 2, 6)
)
aluSecGroupOperGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecHostGrpOperName"),
        ("ALU-SECURITY-MIB", "aluSecHostGrpOperDescription"),
        ("ALU-SECURITY-MIB", "aluSecHostGrpOperPlcyRefCount"),
        ("ALU-SECURITY-MIB", "aluSecHostOperIPAddrValue2"),
        ("ALU-SECURITY-MIB", "aluSecHostOperIPOperator"),
        ("ALU-SECURITY-MIB", "aluSecAppGrpOperName"),
        ("ALU-SECURITY-MIB", "aluSecAppGrpOperDescription"),
        ("ALU-SECURITY-MIB", "aluSecAppGrpOperPlcyRefCount"),
        ("ALU-SECURITY-MIB", "aluSecAppOperMatchProtocol"),
        ("ALU-SECURITY-MIB", "aluSecAppOperMatchSrcPortValue1"),
        ("ALU-SECURITY-MIB", "aluSecAppOperMatchSrcPortValue2"),
        ("ALU-SECURITY-MIB", "aluSecAppOperMatchSrcPortOp"),
        ("ALU-SECURITY-MIB", "aluSecAppOperMatchDstPortValue1"),
        ("ALU-SECURITY-MIB", "aluSecAppOperMatchDstPortValue2"),
        ("ALU-SECURITY-MIB", "aluSecAppOperMatchDstPortOp"),
        ("ALU-SECURITY-MIB", "aluSecAppOperMatchIcmpCode"),
        ("ALU-SECURITY-MIB", "aluSecAppOperMatchIcmpType"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpOperName"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpOperDescription"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpOperRate"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpOperRateCbs"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpOperPlcyRefCount"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpOperFwdPktsPassed"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpOperFwdBytesPassed"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpOperFwdPktsDrop"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpOperRevPktsPassed"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpOperRevBytesPassed"),
        ("ALU-SECURITY-MIB", "aluSecPolicerGrpOperRevPktsDrop"))
)
if mibBuilder.loadTexts:
    aluSecGroupOperGroup.setStatus("current")

aluZoneOperGroupV7v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2, 2, 7)
)
aluZoneOperGroupV7v0.setObjects(
      *(("ALU-SECURITY-MIB", "aluZoneOperName"),
        ("ALU-SECURITY-MIB", "aluZoneOperDescription"),
        ("ALU-SECURITY-MIB", "aluZoneOperPlcyRuleCount"),
        ("ALU-SECURITY-MIB", "aluZoneOperType"),
        ("ALU-SECURITY-MIB", "aluZoneOperSvcId"),
        ("ALU-SECURITY-MIB", "aluZoneOperBypass"),
        ("ALU-SECURITY-MIB", "aluZoneOperInSessionCount"),
        ("ALU-SECURITY-MIB", "aluZoneOperInActiveSessions"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutSessionCount"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutActiveSessions"),
        ("ALU-SECURITY-MIB", "aluZoneOperInPktsDropped"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutPktsDropped"),
        ("ALU-SECURITY-MIB", "aluZoneOperInPktsDefAction"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutPktsDefAction"),
        ("ALU-SECURITY-MIB", "aluZoneOperPlcyLastCommit"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperEntryId"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperActive"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperFlags"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperSecPlcyId"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperSecPlcyRuleId"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperNatPoolId"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperRuleHitCount"),
        ("ALU-SECURITY-MIB", "aluZonePlcyOperRuleActiveSessions"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionProtocol"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionSrcZoneId"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionSrcIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionSrcPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionDstIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionDstPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionRevDirCreated"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionAction"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionNatSrcIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionNatSrcPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneInboundSessionEstablished"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionProtocol"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionDstZoneId"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionSrcIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionSrcPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionDstIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionDstPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionRevDirCreated"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionAction"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionNatSrcIPAddrValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionNatSrcPortValue"),
        ("ALU-SECURITY-MIB", "aluZoneOutboundSessionEstablished"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperName"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperDescription"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperPlcyRefCount"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperTcpSynTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperTcpWaitTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperTcpTransTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperTcpEstTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperUdpTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperUdpInitTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperUdpDnsTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperIcmpTimeout"),
        ("ALU-SECURITY-MIB", "aluSecProfileOperOtherTimeout"),
        ("ALU-SECURITY-MIB", "aluZoneOperInFwdAction"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutFwdAction"),
        ("ALU-SECURITY-MIB", "aluZoneOperInNatAction"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutNatAction"),
        ("ALU-SECURITY-MIB", "aluZoneOperInDropAction"),
        ("ALU-SECURITY-MIB", "aluZoneOperOutDropAction"))
)
if mibBuilder.loadTexts:
    aluZoneOperGroupV7v0.setStatus("current")

aluSecNotificationObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2, 3, 2)
)
aluSecNotificationObjsGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecNotifyPlcyAction"),
        ("ALU-SECURITY-MIB", "aluSecNotifyRuleActive"),
        ("ALU-SECURITY-MIB", "aluSecNotifyZoneId"),
        ("ALU-SECURITY-MIB", "aluSecNotifyZoneRuleId"))
)
if mibBuilder.loadTexts:
    aluSecNotificationObjsGroup.setStatus("current")


# Notification objects

aluSecPlcyActionPerformed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 1)
)
aluSecPlcyActionPerformed.setObjects(
    ("ALU-SECURITY-MIB", "aluSecNotifyPlcyAction")
)
if mibBuilder.loadTexts:
    aluSecPlcyActionPerformed.setStatus(
        "current"
    )

aluSecZonePlcyActionPerformed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 2)
)
aluSecZonePlcyActionPerformed.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecNotifyZoneId"),
        ("ALU-SECURITY-MIB", "aluSecNotifyPlcyAction"))
)
if mibBuilder.loadTexts:
    aluSecZonePlcyActionPerformed.setStatus(
        "current"
    )

aluSecSessionWtrMrkModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 3)
)
aluSecSessionWtrMrkModified.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecActiveSessionHiWtrMrk"),
        ("ALU-SECURITY-MIB", "aluSecActiveSessionLoWtrMrk"))
)
if mibBuilder.loadTexts:
    aluSecSessionWtrMrkModified.setStatus(
        "current"
    )

aluSecSessionHiWtrMrkCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 4)
)
aluSecSessionHiWtrMrkCrossed.setObjects(
    ("ALU-SECURITY-MIB", "aluSecActiveSessionCount")
)
if mibBuilder.loadTexts:
    aluSecSessionHiWtrMrkCrossed.setStatus(
        "current"
    )

aluSecSessionLoWtrMrkCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 5)
)
aluSecSessionLoWtrMrkCrossed.setObjects(
    ("ALU-SECURITY-MIB", "aluSecActiveSessionCount")
)
if mibBuilder.loadTexts:
    aluSecSessionLoWtrMrkCrossed.setStatus(
        "current"
    )

aluSecSessionsExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 6)
)
aluSecSessionsExhausted.setObjects(
    ("ALU-SECURITY-MIB", "aluSecActiveSessionCount")
)
if mibBuilder.loadTexts:
    aluSecSessionsExhausted.setStatus(
        "current"
    )

aluSecZonePlcyRuleStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 7)
)
aluSecZonePlcyRuleStateChange.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecNotifyZoneId"),
        ("ALU-SECURITY-MIB", "aluSecNotifyZoneRuleId"),
        ("ALU-SECURITY-MIB", "aluSecNotifyRuleActive"))
)
if mibBuilder.loadTexts:
    aluSecZonePlcyRuleStateChange.setStatus(
        "current"
    )

aluMcPeerFwBfdSessionOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 8)
)
aluMcPeerFwBfdSessionOpen.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwBfdSessionOpenStatus"))
)
if mibBuilder.loadTexts:
    aluMcPeerFwBfdSessionOpen.setStatus(
        "current"
    )

aluMcPeerFwBfdSessionClose = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 9)
)
aluMcPeerFwBfdSessionClose.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwBfdSessionClose.setStatus(
        "current"
    )

aluMcPeerFwBfdSessionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 10)
)
aluMcPeerFwBfdSessionUp.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwBfdSessionUp.setStatus(
        "current"
    )

aluMcPeerFwBfdSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 11)
)
aluMcPeerFwBfdSessionDown.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwBfdSessionDown.setStatus(
        "current"
    )

aluMcPeerFwOperDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 12)
)
aluMcPeerFwOperDown.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwOperDown.setStatus(
        "current"
    )

aluMcPeerFwOperUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 13)
)
aluMcPeerFwOperUp.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwOperUp.setStatus(
        "current"
    )

aluMcPeerFwElectionMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 14)
)
aluMcPeerFwElectionMaster.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwElectionMaster.setStatus(
        "current"
    )

aluMcPeerFwElectionSlave = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 15)
)
aluMcPeerFwElectionSlave.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwElectionSlave.setStatus(
        "current"
    )

aluMcPeerFwMasterPolicySyncClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 16)
)
aluMcPeerFwMasterPolicySyncClr.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwMasterPolicySyncClr.setStatus(
        "current"
    )

aluMcPeerFwMasterPolicySyncSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 17)
)
aluMcPeerFwMasterPolicySyncSet.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwMasterPolicySyncSet.setStatus(
        "current"
    )

aluMcPeerFwSlavePolicySyncClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 18)
)
aluMcPeerFwSlavePolicySyncClr.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwSlavePolicySyncClr.setStatus(
        "current"
    )

aluMcPeerFwSlavePolicySyncSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 19)
)
aluMcPeerFwSlavePolicySyncSet.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwSlavePolicySyncSet.setStatus(
        "current"
    )

aluMcPeerFwSessionDbSyncClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 20)
)
aluMcPeerFwSessionDbSyncClr.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwSessionDbSyncClr.setStatus(
        "current"
    )

aluMcPeerFwSessionDbSyncSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 14, 0, 21)
)
aluMcPeerFwSessionDbSyncSet.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    aluMcPeerFwSessionDbSyncSet.setStatus(
        "current"
    )


# Notifications groups

aluMcPeerFwV7v0NotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 4, 3)
)
aluMcPeerFwV7v0NotifGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluMcPeerFwBfdSessionClose"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwBfdSessionOpen"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwBfdSessionDown"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwBfdSessionUp"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwOperDown"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwOperUp"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwElectionMaster"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwElectionSlave"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwMasterPolicySyncClr"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwMasterPolicySyncSet"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwSlavePolicySyncClr"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwSlavePolicySyncSet"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwSessionDbSyncClr"),
        ("ALU-SECURITY-MIB", "aluMcPeerFwSessionDbSyncSet"))
)
if mibBuilder.loadTexts:
    aluMcPeerFwV7v0NotifGroup.setStatus(
        "current"
    )

aluSecNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 2, 3, 1)
)
aluSecNotificationGroup.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecPlcyActionPerformed"),
        ("ALU-SECURITY-MIB", "aluSecZonePlcyActionPerformed"),
        ("ALU-SECURITY-MIB", "aluSecSessionWtrMrkModified"),
        ("ALU-SECURITY-MIB", "aluSecSessionHiWtrMrkCrossed"),
        ("ALU-SECURITY-MIB", "aluSecSessionLoWtrMrkCrossed"),
        ("ALU-SECURITY-MIB", "aluSecSessionsExhausted"),
        ("ALU-SECURITY-MIB", "aluSecZonePlcyRuleStateChange"))
)
if mibBuilder.loadTexts:
    aluSecNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluSecurity7705V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 17, 1, 1, 1)
)
aluSecurity7705V6v1Compliance.setObjects(
      *(("ALU-SECURITY-MIB", "aluSecPlcyAdminGroup"),
        ("ALU-SECURITY-MIB", "aluZonePlcyConfigGroup"),
        ("ALU-SECURITY-MIB", "aluSecPlcyConfigGroup"),
        ("ALU-SECURITY-MIB", "aluZoneOperGroup"),
        ("ALU-SECURITY-MIB", "aluSecPlcyOperGroup"),
        ("ALU-SECURITY-MIB", "aluSecStatsGroup"),
        ("ALU-SECURITY-MIB", "aluSecStatsV7v0Group"),
        ("ALU-SECURITY-MIB", "aluSecNotificationGroup"))
)
if mibBuilder.loadTexts:
    aluSecurity7705V6v1Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-SECURITY-MIB",
    **{"TSecurityLogId": TSecurityLogId,
       "TSecurityLogProfileId": TSecurityLogProfileId,
       "TIPOperator": TIPOperator,
       "TZoneType": TZoneType,
       "TPlcyState": TPlcyState,
       "TPoolType": TPoolType,
       "TAlgType": TAlgType,
       "TSecurityPolicerId": TSecurityPolicerId,
       "AluMcFwAuthAlgorithm": AluMcFwAuthAlgorithm,
       "AluMcFwEncrAlgorithm": AluMcFwEncrAlgorithm,
       "aluZoneModule": aluZoneModule,
       "aluSecurityMIBConformance": aluSecurityMIBConformance,
       "aluSecurityAdminConformance": aluSecurityAdminConformance,
       "aluSecurityAdminCompliances": aluSecurityAdminCompliances,
       "aluSecurity7705V6v1Compliance": aluSecurity7705V6v1Compliance,
       "aluSecurityAdminGroups": aluSecurityAdminGroups,
       "aluSecPlcyAdminGroup": aluSecPlcyAdminGroup,
       "aluZonePlcyConfigGroup": aluZonePlcyConfigGroup,
       "aluSecPlcyConfigGroup": aluSecPlcyConfigGroup,
       "aluSecPlcyDstNatGroup": aluSecPlcyDstNatGroup,
       "aluSecFirewallAdminGroup": aluSecFirewallAdminGroup,
       "aluSecGroupConfigGroup": aluSecGroupConfigGroup,
       "aluSecurityLogGroups": aluSecurityLogGroups,
       "aluSecLogObjsGroup": aluSecLogObjsGroup,
       "aluSecurityMcGroups": aluSecurityMcGroups,
       "aluMcPeerFwGroup": aluMcPeerFwGroup,
       "aluMcPeerFwNotifyObjsV7v0Group": aluMcPeerFwNotifyObjsV7v0Group,
       "aluMcPeerFwV7v0NotifGroup": aluMcPeerFwV7v0NotifGroup,
       "aluSecurityOperConformance": aluSecurityOperConformance,
       "aluSecurityOperCompliances": aluSecurityOperCompliances,
       "aluSecurityOperGroups": aluSecurityOperGroups,
       "aluZoneOperGroup": aluZoneOperGroup,
       "aluSecPlcyOperGroup": aluSecPlcyOperGroup,
       "aluSecStatsGroup": aluSecStatsGroup,
       "aluSecFirewallOperGroup": aluSecFirewallOperGroup,
       "aluSecStatsV7v0Group": aluSecStatsV7v0Group,
       "aluSecGroupOperGroup": aluSecGroupOperGroup,
       "aluZoneOperGroupV7v0": aluZoneOperGroupV7v0,
       "aluSecurityNotifyGroups": aluSecurityNotifyGroups,
       "aluSecNotificationGroup": aluSecNotificationGroup,
       "aluSecNotificationObjsGroup": aluSecNotificationObjsGroup,
       "aluSecurityStatsConformance": aluSecurityStatsConformance,
       "aluSecurityObjs": aluSecurityObjs,
       "aluSecurityAdminObjs": aluSecurityAdminObjs,
       "aluSecPlcyAdminControlApply": aluSecPlcyAdminControlApply,
       "aluSecPlcyBypass": aluSecPlcyBypass,
       "aluZoneConfigTable": aluZoneConfigTable,
       "aluZoneConfigEntry": aluZoneConfigEntry,
       "aluZoneConfigId": aluZoneConfigId,
       "aluZoneConfigName": aluZoneConfigName,
       "aluZoneConfigRowStatus": aluZoneConfigRowStatus,
       "aluZoneConfigDescription": aluZoneConfigDescription,
       "aluZoneConfigControlApply": aluZoneConfigControlApply,
       "aluZoneConfigType": aluZoneConfigType,
       "aluZoneConfigSvcId": aluZoneConfigSvcId,
       "aluZoneConfigState": aluZoneConfigState,
       "aluZoneConfigBypass": aluZoneConfigBypass,
       "aluZoneConfigInTcpSessLimit": aluZoneConfigInTcpSessLimit,
       "aluZoneConfigInUdpSessLimit": aluZoneConfigInUdpSessLimit,
       "aluZoneConfigInIcmpSessLimit": aluZoneConfigInIcmpSessLimit,
       "aluZoneConfigInOthSessLimit": aluZoneConfigInOthSessLimit,
       "aluZoneConfigOutTcpSessLimit": aluZoneConfigOutTcpSessLimit,
       "aluZoneConfigOutUdpSessLimit": aluZoneConfigOutUdpSessLimit,
       "aluZoneConfigOutIcmpSessLimit": aluZoneConfigOutIcmpSessLimit,
       "aluZoneConfigOutOthSessLimit": aluZoneConfigOutOthSessLimit,
       "aluZoneConfigLogId": aluZoneConfigLogId,
       "aluZoneConfigAutoBind": aluZoneConfigAutoBind,
       "aluZonePlcyConfigTable": aluZonePlcyConfigTable,
       "aluZonePlcyConfigEntry": aluZonePlcyConfigEntry,
       "aluZonePlcyConfigEntryId": aluZonePlcyConfigEntryId,
       "aluZonePlcyConfigRowStatus": aluZonePlcyConfigRowStatus,
       "aluZonePlcyConfigSecPlcyId": aluZonePlcyConfigSecPlcyId,
       "aluZoneNatPoolConfigTable": aluZoneNatPoolConfigTable,
       "aluZoneNatPoolConfigEntry": aluZoneNatPoolConfigEntry,
       "aluZoneNatPoolConfigId": aluZoneNatPoolConfigId,
       "aluZoneNatPoolConfigName": aluZoneNatPoolConfigName,
       "aluZoneNatPoolConfigRowStatus": aluZoneNatPoolConfigRowStatus,
       "aluZoneNatPoolConfigDescription": aluZoneNatPoolConfigDescription,
       "aluZoneNatPoolConfigType": aluZoneNatPoolConfigType,
       "aluZoneNatPoolConfigDirection": aluZoneNatPoolConfigDirection,
       "aluZoneNatPoolParamsConfigTable": aluZoneNatPoolParamsConfigTable,
       "aluZoneNatPoolParamsConfigEntry": aluZoneNatPoolParamsConfigEntry,
       "aluZoneNatPoolParamsConfigEntryId": aluZoneNatPoolParamsConfigEntryId,
       "aluZoneNatPoolParamsConfigRowStatus": aluZoneNatPoolParamsConfigRowStatus,
       "aluZoneNatPoolParamsConfigIPAddrValue1": aluZoneNatPoolParamsConfigIPAddrValue1,
       "aluZoneNatPoolParamsConfigIPAddrValue2": aluZoneNatPoolParamsConfigIPAddrValue2,
       "aluZoneNatPoolParamsConfigIPOperator": aluZoneNatPoolParamsConfigIPOperator,
       "aluZoneNatPoolParamsConfigIPInterfaceIndex": aluZoneNatPoolParamsConfigIPInterfaceIndex,
       "aluZoneNatPoolParamsConfigPortOperator": aluZoneNatPoolParamsConfigPortOperator,
       "aluZoneNatPoolParamsConfigPortValue1": aluZoneNatPoolParamsConfigPortValue1,
       "aluZoneNatPoolParamsConfigPortValue2": aluZoneNatPoolParamsConfigPortValue2,
       "aluSecPlcyConfigTable": aluSecPlcyConfigTable,
       "aluSecPlcyConfigEntry": aluSecPlcyConfigEntry,
       "aluSecPlcyConfigId": aluSecPlcyConfigId,
       "aluSecPlcyConfigRowStatus": aluSecPlcyConfigRowStatus,
       "aluSecPlcyConfigName": aluSecPlcyConfigName,
       "aluSecPlcyConfigDescription": aluSecPlcyConfigDescription,
       "aluSecPlcyParamsConfigTable": aluSecPlcyParamsConfigTable,
       "aluSecPlcyParamsConfigEntry": aluSecPlcyParamsConfigEntry,
       "aluSecPlcyParamsConfigRuleId": aluSecPlcyParamsConfigRuleId,
       "aluSecPlcyParamsConfigRowStatus": aluSecPlcyParamsConfigRowStatus,
       "aluSecPlcyParamsConfigDescription": aluSecPlcyParamsConfigDescription,
       "aluSecPlcyParamsConfigMatchSrcIPAddrValue1": aluSecPlcyParamsConfigMatchSrcIPAddrValue1,
       "aluSecPlcyParamsConfigMatchSrcIPAddrValue2": aluSecPlcyParamsConfigMatchSrcIPAddrValue2,
       "aluSecPlcyParamsConfigMatchSrcIPOperator": aluSecPlcyParamsConfigMatchSrcIPOperator,
       "aluSecPlcyParamsConfigMatchSrcIPHostGroup": aluSecPlcyParamsConfigMatchSrcIPHostGroup,
       "aluSecPlcyParamsConfigMatchDstIPAddrValue1": aluSecPlcyParamsConfigMatchDstIPAddrValue1,
       "aluSecPlcyParamsConfigMatchDstIPAddrValue2": aluSecPlcyParamsConfigMatchDstIPAddrValue2,
       "aluSecPlcyParamsConfigMatchDstIPOperator": aluSecPlcyParamsConfigMatchDstIPOperator,
       "aluSecPlcyParamsConfigMatchDstIPHostGroup": aluSecPlcyParamsConfigMatchDstIPHostGroup,
       "aluSecPlcyParamsConfigMatchProtocol": aluSecPlcyParamsConfigMatchProtocol,
       "aluSecPlcyParamsConfigMatchSrcPortValue1": aluSecPlcyParamsConfigMatchSrcPortValue1,
       "aluSecPlcyParamsConfigMatchSrcPortValue2": aluSecPlcyParamsConfigMatchSrcPortValue2,
       "aluSecPlcyParamsConfigMatchSrcPortOp": aluSecPlcyParamsConfigMatchSrcPortOp,
       "aluSecPlcyParamsConfigMatchDstPortValue1": aluSecPlcyParamsConfigMatchDstPortValue1,
       "aluSecPlcyParamsConfigMatchDstPortValue2": aluSecPlcyParamsConfigMatchDstPortValue2,
       "aluSecPlcyParamsConfigMatchDstPortOp": aluSecPlcyParamsConfigMatchDstPortOp,
       "aluSecPlcyParamsConfigMatchAppGroup": aluSecPlcyParamsConfigMatchAppGroup,
       "aluSecPlcyParamsConfigMatchIcmpCode": aluSecPlcyParamsConfigMatchIcmpCode,
       "aluSecPlcyParamsConfigMatchIcmpType": aluSecPlcyParamsConfigMatchIcmpType,
       "aluSecPlcyParamsConfigMatchIgmpType": aluSecPlcyParamsConfigMatchIgmpType,
       "aluSecPlcyParamsConfigMatchFlowDirection": aluSecPlcyParamsConfigMatchFlowDirection,
       "aluSecPlcyParamsConfigProfileId": aluSecPlcyParamsConfigProfileId,
       "aluSecPlcyParamsConfigConcurrentFlowLimit": aluSecPlcyParamsConfigConcurrentFlowLimit,
       "aluSecPlcyParamsConfigCreateRevDirFlow": aluSecPlcyParamsConfigCreateRevDirFlow,
       "aluSecPlcyParamsConfigAction": aluSecPlcyParamsConfigAction,
       "aluSecPlcyParamsConfigMatchLocal": aluSecPlcyParamsConfigMatchLocal,
       "aluSecPlcyParamsConfigActionNatDstIPAddr": aluSecPlcyParamsConfigActionNatDstIPAddr,
       "aluSecPlcyParamsConfigActionNatDstPort": aluSecPlcyParamsConfigActionNatDstPort,
       "aluSecPlcyParamsConfigLogControl": aluSecPlcyParamsConfigLogControl,
       "aluSecPlcyParamsConfigLogId": aluSecPlcyParamsConfigLogId,
       "aluSecProfileConfigTable": aluSecProfileConfigTable,
       "aluSecProfileConfigEntry": aluSecProfileConfigEntry,
       "aluSecProfileConfigId": aluSecProfileConfigId,
       "aluSecProfileConfigRowStatus": aluSecProfileConfigRowStatus,
       "aluSecProfileConfigName": aluSecProfileConfigName,
       "aluSecProfileConfigDescription": aluSecProfileConfigDescription,
       "aluSecProfileConfigTcpSynTimeout": aluSecProfileConfigTcpSynTimeout,
       "aluSecProfileConfigTcpWaitTimeout": aluSecProfileConfigTcpWaitTimeout,
       "aluSecProfileConfigTcpTransTimeout": aluSecProfileConfigTcpTransTimeout,
       "aluSecProfileConfigTcpEstTimeout": aluSecProfileConfigTcpEstTimeout,
       "aluSecProfileConfigUdpTimeout": aluSecProfileConfigUdpTimeout,
       "aluSecProfileConfigUdpInitTimeout": aluSecProfileConfigUdpInitTimeout,
       "aluSecProfileConfigUdpDnsTimeout": aluSecProfileConfigUdpDnsTimeout,
       "aluSecProfileConfigIcmpTimeout": aluSecProfileConfigIcmpTimeout,
       "aluSecProfileConfigOtherTimeout": aluSecProfileConfigOtherTimeout,
       "aluSecProfileConfigAppInspect": aluSecProfileConfigAppInspect,
       "aluSecProfileConfigInspectTcp": aluSecProfileConfigInspectTcp,
       "aluSecProfileConfigInspectIpOpt": aluSecProfileConfigInspectIpOpt,
       "aluSecProfileConfigAllowedIpOpt": aluSecProfileConfigAllowedIpOpt,
       "aluSecProfileConfigAllowPktFrag": aluSecProfileConfigAllowPktFrag,
       "aluSecProfileConfigAlg": aluSecProfileConfigAlg,
       "aluSecProfileConfigIcmpReqLimit": aluSecProfileConfigIcmpReqLimit,
       "aluSecProfileConfigIcmpErrLimit": aluSecProfileConfigIcmpErrLimit,
       "aluSecProfileConfigDnsReplyOnly": aluSecProfileConfigDnsReplyOnly,
       "aluSecProfileConfigTcpTmoStrict": aluSecProfileConfigTcpTmoStrict,
       "aluSecProfileConfigUdpTmoStrict": aluSecProfileConfigUdpTmoStrict,
       "aluSecProfileConfigIcmpTmoStrict": aluSecProfileConfigIcmpTmoStrict,
       "aluSecProfileConfigDnsTmoStrict": aluSecProfileConfigDnsTmoStrict,
       "aluSecProfileConfigOthTmoStrict": aluSecProfileConfigOthTmoStrict,
       "aluSecProfileConfigFwdPolicerId": aluSecProfileConfigFwdPolicerId,
       "aluSecProfileConfigRevPolicerId": aluSecProfileConfigRevPolicerId,
       "aluSecPlcyLastCommit": aluSecPlcyLastCommit,
       "aluSecPlcyCount": aluSecPlcyCount,
       "aluSecPlcyProfileCount": aluSecPlcyProfileCount,
       "aluSecPlcyZoneCount": aluSecPlcyZoneCount,
       "aluSecActiveSessionCount": aluSecActiveSessionCount,
       "aluSecActiveSessionLimit": aluSecActiveSessionLimit,
       "aluSecActiveSessionHiWtrMrk": aluSecActiveSessionHiWtrMrk,
       "aluSecActiveSessionLoWtrMrk": aluSecActiveSessionLoWtrMrk,
       "aluSecPlcyState": aluSecPlcyState,
       "aluSecSessionResourceState": aluSecSessionResourceState,
       "aluSecHostGrpConfigTable": aluSecHostGrpConfigTable,
       "aluSecHostGrpConfigEntry": aluSecHostGrpConfigEntry,
       "aluSecHostGrpConfigId": aluSecHostGrpConfigId,
       "aluSecHostGrpConfigRowStatus": aluSecHostGrpConfigRowStatus,
       "aluSecHostGrpConfigName": aluSecHostGrpConfigName,
       "aluSecHostGrpConfigDescription": aluSecHostGrpConfigDescription,
       "aluSecHostConfigTable": aluSecHostConfigTable,
       "aluSecHostConfigEntry": aluSecHostConfigEntry,
       "aluSecHostConfigIPAddrValue1": aluSecHostConfigIPAddrValue1,
       "aluSecHostConfigRowStatus": aluSecHostConfigRowStatus,
       "aluSecHostConfigIPAddrValue2": aluSecHostConfigIPAddrValue2,
       "aluSecHostConfigIPOperator": aluSecHostConfigIPOperator,
       "aluSecAppGrpConfigTable": aluSecAppGrpConfigTable,
       "aluSecAppGrpConfigEntry": aluSecAppGrpConfigEntry,
       "aluSecAppGrpConfigId": aluSecAppGrpConfigId,
       "aluSecAppGrpConfigRowStatus": aluSecAppGrpConfigRowStatus,
       "aluSecAppGrpConfigName": aluSecAppGrpConfigName,
       "aluSecAppGrpConfigDescription": aluSecAppGrpConfigDescription,
       "aluSecAppConfigTable": aluSecAppConfigTable,
       "aluSecAppConfigEntry": aluSecAppConfigEntry,
       "aluSecAppConfigEntryId": aluSecAppConfigEntryId,
       "aluSecAppConfigRowStatus": aluSecAppConfigRowStatus,
       "aluSecAppConfigMatchProtocol": aluSecAppConfigMatchProtocol,
       "aluSecAppConfigMatchSrcPortValue1": aluSecAppConfigMatchSrcPortValue1,
       "aluSecAppConfigMatchSrcPortValue2": aluSecAppConfigMatchSrcPortValue2,
       "aluSecAppConfigMatchSrcPortOp": aluSecAppConfigMatchSrcPortOp,
       "aluSecAppConfigMatchDstPortValue1": aluSecAppConfigMatchDstPortValue1,
       "aluSecAppConfigMatchDstPortValue2": aluSecAppConfigMatchDstPortValue2,
       "aluSecAppConfigMatchDstPortOp": aluSecAppConfigMatchDstPortOp,
       "aluSecAppConfigMatchIcmpCode": aluSecAppConfigMatchIcmpCode,
       "aluSecAppConfigMatchIcmpType": aluSecAppConfigMatchIcmpType,
       "aluSecPolicerGrpConfigTable": aluSecPolicerGrpConfigTable,
       "aluSecPolicerGrpConfigEntry": aluSecPolicerGrpConfigEntry,
       "aluSecPolicerGrpConfigId": aluSecPolicerGrpConfigId,
       "aluSecPolicerGrpConfigRowStatus": aluSecPolicerGrpConfigRowStatus,
       "aluSecPolicerGrpConfigName": aluSecPolicerGrpConfigName,
       "aluSecPolicerGrpConfigDescription": aluSecPolicerGrpConfigDescription,
       "aluSecPolicerGrpConfigRate": aluSecPolicerGrpConfigRate,
       "aluSecPolicerGrpConfigRateCbs": aluSecPolicerGrpConfigRateCbs,
       "aluSecTotalSessionCount": aluSecTotalSessionCount,
       "aluSecurityOperObjs": aluSecurityOperObjs,
       "aluZoneOperTable": aluZoneOperTable,
       "aluZoneOperEntry": aluZoneOperEntry,
       "aluZoneOperId": aluZoneOperId,
       "aluZoneOperName": aluZoneOperName,
       "aluZoneOperBypass": aluZoneOperBypass,
       "aluZoneOperDescription": aluZoneOperDescription,
       "aluZoneOperPlcyRuleCount": aluZoneOperPlcyRuleCount,
       "aluZoneOperType": aluZoneOperType,
       "aluZoneOperSvcId": aluZoneOperSvcId,
       "aluZoneOperInSessionCount": aluZoneOperInSessionCount,
       "aluZoneOperInActiveSessions": aluZoneOperInActiveSessions,
       "aluZoneOperOutSessionCount": aluZoneOperOutSessionCount,
       "aluZoneOperOutActiveSessions": aluZoneOperOutActiveSessions,
       "aluZoneOperInPktsDropped": aluZoneOperInPktsDropped,
       "aluZoneOperInBytesDropped": aluZoneOperInBytesDropped,
       "aluZoneOperOutPktsDropped": aluZoneOperOutPktsDropped,
       "aluZoneOperOutBytesDropped": aluZoneOperOutBytesDropped,
       "aluZoneOperInPktsDefAction": aluZoneOperInPktsDefAction,
       "aluZoneOperInBytesDefAction": aluZoneOperInBytesDefAction,
       "aluZoneOperOutPktsDefAction": aluZoneOperOutPktsDefAction,
       "aluZoneOperOutBytesDefAction": aluZoneOperOutBytesDefAction,
       "aluZoneOperPlcyLastCommit": aluZoneOperPlcyLastCommit,
       "aluZoneOperInTcpSessLimit": aluZoneOperInTcpSessLimit,
       "aluZoneOperInUdpSessLimit": aluZoneOperInUdpSessLimit,
       "aluZoneOperInIcmpSessLimit": aluZoneOperInIcmpSessLimit,
       "aluZoneOperInOthSessLimit": aluZoneOperInOthSessLimit,
       "aluZoneOperOutTcpSessLimit": aluZoneOperOutTcpSessLimit,
       "aluZoneOperOutUdpSessLimit": aluZoneOperOutUdpSessLimit,
       "aluZoneOperOutIcmpSessLimit": aluZoneOperOutIcmpSessLimit,
       "aluZoneOperOutOthSessLimit": aluZoneOperOutOthSessLimit,
       "aluZoneOperInTcpActSessions": aluZoneOperInTcpActSessions,
       "aluZoneOperInUdpActSessions": aluZoneOperInUdpActSessions,
       "aluZoneOperInIcmpActSessions": aluZoneOperInIcmpActSessions,
       "aluZoneOperInOthActSessions": aluZoneOperInOthActSessions,
       "aluZoneOperOutTcpActSessions": aluZoneOperOutTcpActSessions,
       "aluZoneOperOutUdpActSessions": aluZoneOperOutUdpActSessions,
       "aluZoneOperOutIcmpActSessions": aluZoneOperOutIcmpActSessions,
       "aluZoneOperOutOthActSessions": aluZoneOperOutOthActSessions,
       "aluZoneOperLogId": aluZoneOperLogId,
       "aluZoneOperAutoBind": aluZoneOperAutoBind,
       "aluZoneOperInFwdAction": aluZoneOperInFwdAction,
       "aluZoneOperOutFwdAction": aluZoneOperOutFwdAction,
       "aluZoneOperInNatAction": aluZoneOperInNatAction,
       "aluZoneOperOutNatAction": aluZoneOperOutNatAction,
       "aluZoneOperInDropAction": aluZoneOperInDropAction,
       "aluZoneOperOutDropAction": aluZoneOperOutDropAction,
       "aluZonePlcyOperTable": aluZonePlcyOperTable,
       "aluZonePlcyOperEntry": aluZonePlcyOperEntry,
       "aluZonePlcyOperRuleId": aluZonePlcyOperRuleId,
       "aluZonePlcyOperEntryId": aluZonePlcyOperEntryId,
       "aluZonePlcyOperActive": aluZonePlcyOperActive,
       "aluZonePlcyOperFlags": aluZonePlcyOperFlags,
       "aluZonePlcyOperSecPlcyId": aluZonePlcyOperSecPlcyId,
       "aluZonePlcyOperSecPlcyRuleId": aluZonePlcyOperSecPlcyRuleId,
       "aluZonePlcyOperNatPoolId": aluZonePlcyOperNatPoolId,
       "aluZonePlcyOperRuleHitCount": aluZonePlcyOperRuleHitCount,
       "aluZonePlcyOperRuleActiveSessions": aluZonePlcyOperRuleActiveSessions,
       "aluZoneNatPoolOperTable": aluZoneNatPoolOperTable,
       "aluZoneNatPoolOperEntry": aluZoneNatPoolOperEntry,
       "aluZoneNatPoolOperId": aluZoneNatPoolOperId,
       "aluZoneNatPoolOperName": aluZoneNatPoolOperName,
       "aluZoneNatPoolOperDescription": aluZoneNatPoolOperDescription,
       "aluZoneNatPoolOperType": aluZoneNatPoolOperType,
       "aluZoneNatPoolOperDirection": aluZoneNatPoolOperDirection,
       "aluZoneNatPoolParamsOperTable": aluZoneNatPoolParamsOperTable,
       "aluZoneNatPoolParamsOperEntry": aluZoneNatPoolParamsOperEntry,
       "aluZoneNatPoolParamsOperEntryId": aluZoneNatPoolParamsOperEntryId,
       "aluZoneNatPoolParamsOperIPAddrValue1": aluZoneNatPoolParamsOperIPAddrValue1,
       "aluZoneNatPoolParamsOperIPAddrValue2": aluZoneNatPoolParamsOperIPAddrValue2,
       "aluZoneNatPoolParamsOperIPOperator": aluZoneNatPoolParamsOperIPOperator,
       "aluZoneNatPoolParamsOperIPInterfaceIndex": aluZoneNatPoolParamsOperIPInterfaceIndex,
       "aluZoneNatPoolParamsOperPortOperator": aluZoneNatPoolParamsOperPortOperator,
       "aluZoneNatPoolParamsOperPortValue1": aluZoneNatPoolParamsOperPortValue1,
       "aluZoneNatPoolParamsOperPortValue2": aluZoneNatPoolParamsOperPortValue2,
       "aluSecPlcyOperTable": aluSecPlcyOperTable,
       "aluSecPlcyOperEntry": aluSecPlcyOperEntry,
       "aluSecPlcyOperId": aluSecPlcyOperId,
       "aluSecPlcyOperName": aluSecPlcyOperName,
       "aluSecPlcyOperDescription": aluSecPlcyOperDescription,
       "aluSecPlcyOperRuleCount": aluSecPlcyOperRuleCount,
       "aluSecPlcyOperZoneRefCount": aluSecPlcyOperZoneRefCount,
       "aluSecPlcyParamsOperTable": aluSecPlcyParamsOperTable,
       "aluSecPlcyParamsOperEntry": aluSecPlcyParamsOperEntry,
       "aluSecPlcyParamsOperRuleId": aluSecPlcyParamsOperRuleId,
       "aluSecPlcyParamsOperDescription": aluSecPlcyParamsOperDescription,
       "aluSecPlcyParamsOperMatchSrcIPAddrValue1": aluSecPlcyParamsOperMatchSrcIPAddrValue1,
       "aluSecPlcyParamsOperMatchSrcIPAddrValue2": aluSecPlcyParamsOperMatchSrcIPAddrValue2,
       "aluSecPlcyParamsOperMatchSrcIPOperator": aluSecPlcyParamsOperMatchSrcIPOperator,
       "aluSecPlcyParamsOperMatchSrcIPHostGroup": aluSecPlcyParamsOperMatchSrcIPHostGroup,
       "aluSecPlcyParamsOperMatchDstIPAddrValue1": aluSecPlcyParamsOperMatchDstIPAddrValue1,
       "aluSecPlcyParamsOperMatchDstIPAddrValue2": aluSecPlcyParamsOperMatchDstIPAddrValue2,
       "aluSecPlcyParamsOperMatchDstIPOperator": aluSecPlcyParamsOperMatchDstIPOperator,
       "aluSecPlcyParamsOperMatchDstIPHostGroup": aluSecPlcyParamsOperMatchDstIPHostGroup,
       "aluSecPlcyParamsOperMatchProtocol": aluSecPlcyParamsOperMatchProtocol,
       "aluSecPlcyParamsOperMatchSrcPortValue1": aluSecPlcyParamsOperMatchSrcPortValue1,
       "aluSecPlcyParamsOperMatchSrcPortValue2": aluSecPlcyParamsOperMatchSrcPortValue2,
       "aluSecPlcyParamsOperMatchSrcPortOp": aluSecPlcyParamsOperMatchSrcPortOp,
       "aluSecPlcyParamsOperMatchDstPortValue1": aluSecPlcyParamsOperMatchDstPortValue1,
       "aluSecPlcyParamsOperMatchDstPortValue2": aluSecPlcyParamsOperMatchDstPortValue2,
       "aluSecPlcyParamsOperMatchDstPortOp": aluSecPlcyParamsOperMatchDstPortOp,
       "aluSecPlcyParamsOperMatchAppGroup": aluSecPlcyParamsOperMatchAppGroup,
       "aluSecPlcyParamsOperMatchIcmpCode": aluSecPlcyParamsOperMatchIcmpCode,
       "aluSecPlcyParamsOperMatchIcmpType": aluSecPlcyParamsOperMatchIcmpType,
       "aluSecPlcyParamsOperMatchIgmpType": aluSecPlcyParamsOperMatchIgmpType,
       "aluSecPlcyParamsOperMatchFlowDirection": aluSecPlcyParamsOperMatchFlowDirection,
       "aluSecPlcyParamsOperProfileId": aluSecPlcyParamsOperProfileId,
       "aluSecPlcyParamsOperConcurrentFlowLimit": aluSecPlcyParamsOperConcurrentFlowLimit,
       "aluSecPlcyParamsOperCreateRevDirFlow": aluSecPlcyParamsOperCreateRevDirFlow,
       "aluSecPlcyParamsOperAction": aluSecPlcyParamsOperAction,
       "aluSecPlcyParamsOperMatchLocal": aluSecPlcyParamsOperMatchLocal,
       "aluSecPlcyParamsOperActionNatDstIPAddr": aluSecPlcyParamsOperActionNatDstIPAddr,
       "aluSecPlcyParamsOperActionNatDstPort": aluSecPlcyParamsOperActionNatDstPort,
       "aluSecPlcyParamsOperLogControl": aluSecPlcyParamsOperLogControl,
       "aluSecPlcyParamsOperLogId": aluSecPlcyParamsOperLogId,
       "aluSecProfileOperTable": aluSecProfileOperTable,
       "aluSecProfileOperEntry": aluSecProfileOperEntry,
       "aluSecProfileOperId": aluSecProfileOperId,
       "aluSecProfileOperName": aluSecProfileOperName,
       "aluSecProfileOperDescription": aluSecProfileOperDescription,
       "aluSecProfileOperPlcyRefCount": aluSecProfileOperPlcyRefCount,
       "aluSecProfileOperTcpSynTimeout": aluSecProfileOperTcpSynTimeout,
       "aluSecProfileOperTcpWaitTimeout": aluSecProfileOperTcpWaitTimeout,
       "aluSecProfileOperTcpTransTimeout": aluSecProfileOperTcpTransTimeout,
       "aluSecProfileOperTcpEstTimeout": aluSecProfileOperTcpEstTimeout,
       "aluSecProfileOperUdpTimeout": aluSecProfileOperUdpTimeout,
       "aluSecProfileOperUdpInitTimeout": aluSecProfileOperUdpInitTimeout,
       "aluSecProfileOperUdpDnsTimeout": aluSecProfileOperUdpDnsTimeout,
       "aluSecProfileOperIcmpTimeout": aluSecProfileOperIcmpTimeout,
       "aluSecProfileOperOtherTimeout": aluSecProfileOperOtherTimeout,
       "aluSecProfileOperAppInspect": aluSecProfileOperAppInspect,
       "aluSecProfileOperInspectTcp": aluSecProfileOperInspectTcp,
       "aluSecProfileOperInspectIpOpt": aluSecProfileOperInspectIpOpt,
       "aluSecProfileOperAllowedIpOpt": aluSecProfileOperAllowedIpOpt,
       "aluSecProfileOperAllowPktFrag": aluSecProfileOperAllowPktFrag,
       "aluSecProfileOperAlg": aluSecProfileOperAlg,
       "aluSecProfileOperIcmpReqLimit": aluSecProfileOperIcmpReqLimit,
       "aluSecProfileOperIcmpErrLimit": aluSecProfileOperIcmpErrLimit,
       "aluSecProfileOperDnsReplyOnly": aluSecProfileOperDnsReplyOnly,
       "aluSecProfileOperTcpTmoStrict": aluSecProfileOperTcpTmoStrict,
       "aluSecProfileOperUdpTmoStrict": aluSecProfileOperUdpTmoStrict,
       "aluSecProfileOperIcmpTmoStrict": aluSecProfileOperIcmpTmoStrict,
       "aluSecProfileOperDnsTmoStrict": aluSecProfileOperDnsTmoStrict,
       "aluSecProfileOperOthTmoStrict": aluSecProfileOperOthTmoStrict,
       "aluSecProfileOperFwdPolicerId": aluSecProfileOperFwdPolicerId,
       "aluSecProfileOperRevPolicerId": aluSecProfileOperRevPolicerId,
       "aluZoneInboundSessionTable": aluZoneInboundSessionTable,
       "aluZoneInboundSessionEntry": aluZoneInboundSessionEntry,
       "aluZoneSessionId": aluZoneSessionId,
       "aluZoneInboundSessionProtocol": aluZoneInboundSessionProtocol,
       "aluZoneInboundSessionSrcZoneId": aluZoneInboundSessionSrcZoneId,
       "aluZoneInboundSessionSrcIPAddrValue": aluZoneInboundSessionSrcIPAddrValue,
       "aluZoneInboundSessionSrcPortValue": aluZoneInboundSessionSrcPortValue,
       "aluZoneInboundSessionDstIPAddrValue": aluZoneInboundSessionDstIPAddrValue,
       "aluZoneInboundSessionDstPortValue": aluZoneInboundSessionDstPortValue,
       "aluZoneInboundSessionRevDirCreated": aluZoneInboundSessionRevDirCreated,
       "aluZoneInboundSessionAction": aluZoneInboundSessionAction,
       "aluZoneInboundSessionNatSrcIPAddrValue": aluZoneInboundSessionNatSrcIPAddrValue,
       "aluZoneInboundSessionNatSrcPortValue": aluZoneInboundSessionNatSrcPortValue,
       "aluZoneInboundSessionNatDstIPAddrValue": aluZoneInboundSessionNatDstIPAddrValue,
       "aluZoneInboundSessionNatDstPortValue": aluZoneInboundSessionNatDstPortValue,
       "aluZoneInboundSessionEstablished": aluZoneInboundSessionEstablished,
       "aluZoneInboundSessionAlg": aluZoneInboundSessionAlg,
       "aluZoneInboundSessionInspect": aluZoneInboundSessionInspect,
       "aluZoneInboundSessionFwdPolicerId": aluZoneInboundSessionFwdPolicerId,
       "aluZoneInboundSessionRevPolicerId": aluZoneInboundSessionRevPolicerId,
       "aluZoneInboundSessionCreator": aluZoneInboundSessionCreator,
       "aluZoneOutboundSessionTable": aluZoneOutboundSessionTable,
       "aluZoneOutboundSessionEntry": aluZoneOutboundSessionEntry,
       "aluZoneOutboundSessionProtocol": aluZoneOutboundSessionProtocol,
       "aluZoneOutboundSessionSrcIPAddrValue": aluZoneOutboundSessionSrcIPAddrValue,
       "aluZoneOutboundSessionSrcPortValue": aluZoneOutboundSessionSrcPortValue,
       "aluZoneOutboundSessionDstIPAddrValue": aluZoneOutboundSessionDstIPAddrValue,
       "aluZoneOutboundSessionDstPortValue": aluZoneOutboundSessionDstPortValue,
       "aluZoneOutboundSessionDstZoneId": aluZoneOutboundSessionDstZoneId,
       "aluZoneOutboundSessionRevDirCreated": aluZoneOutboundSessionRevDirCreated,
       "aluZoneOutboundSessionAction": aluZoneOutboundSessionAction,
       "aluZoneOutboundSessionNatSrcIPAddrValue": aluZoneOutboundSessionNatSrcIPAddrValue,
       "aluZoneOutboundSessionNatSrcPortValue": aluZoneOutboundSessionNatSrcPortValue,
       "aluZoneOutboundSessionNatDstIPAddrValue": aluZoneOutboundSessionNatDstIPAddrValue,
       "aluZoneOutboundSessionNatDstPortValue": aluZoneOutboundSessionNatDstPortValue,
       "aluZoneOutboundSessionEstablished": aluZoneOutboundSessionEstablished,
       "aluZoneOutboundSessionAlg": aluZoneOutboundSessionAlg,
       "aluZoneOutboundSessionInspect": aluZoneOutboundSessionInspect,
       "aluZoneOutboundSessionFwdPolicerId": aluZoneOutboundSessionFwdPolicerId,
       "aluZoneOutboundSessionRevPolicerId": aluZoneOutboundSessionRevPolicerId,
       "aluZoneOutboundSessionCreator": aluZoneOutboundSessionCreator,
       "aluSecHostGrpOperTable": aluSecHostGrpOperTable,
       "aluSecHostGrpOperEntry": aluSecHostGrpOperEntry,
       "aluSecHostGrpOperId": aluSecHostGrpOperId,
       "aluSecHostGrpOperName": aluSecHostGrpOperName,
       "aluSecHostGrpOperDescription": aluSecHostGrpOperDescription,
       "aluSecHostGrpOperPlcyRefCount": aluSecHostGrpOperPlcyRefCount,
       "aluSecHostOperTable": aluSecHostOperTable,
       "aluSecHostOperEntry": aluSecHostOperEntry,
       "aluSecHostOperIPAddrValue1": aluSecHostOperIPAddrValue1,
       "aluSecHostOperIPAddrValue2": aluSecHostOperIPAddrValue2,
       "aluSecHostOperIPOperator": aluSecHostOperIPOperator,
       "aluSecAppGrpOperTable": aluSecAppGrpOperTable,
       "aluSecAppGrpOperEntry": aluSecAppGrpOperEntry,
       "aluSecAppGrpOperId": aluSecAppGrpOperId,
       "aluSecAppGrpOperName": aluSecAppGrpOperName,
       "aluSecAppGrpOperDescription": aluSecAppGrpOperDescription,
       "aluSecAppGrpOperPlcyRefCount": aluSecAppGrpOperPlcyRefCount,
       "aluSecAppOperTable": aluSecAppOperTable,
       "aluSecAppOperEntry": aluSecAppOperEntry,
       "aluSecAppOperEntryId": aluSecAppOperEntryId,
       "aluSecAppOperMatchProtocol": aluSecAppOperMatchProtocol,
       "aluSecAppOperMatchSrcPortValue1": aluSecAppOperMatchSrcPortValue1,
       "aluSecAppOperMatchSrcPortValue2": aluSecAppOperMatchSrcPortValue2,
       "aluSecAppOperMatchSrcPortOp": aluSecAppOperMatchSrcPortOp,
       "aluSecAppOperMatchDstPortValue1": aluSecAppOperMatchDstPortValue1,
       "aluSecAppOperMatchDstPortValue2": aluSecAppOperMatchDstPortValue2,
       "aluSecAppOperMatchDstPortOp": aluSecAppOperMatchDstPortOp,
       "aluSecAppOperMatchIcmpCode": aluSecAppOperMatchIcmpCode,
       "aluSecAppOperMatchIcmpType": aluSecAppOperMatchIcmpType,
       "aluSecPolicerGrpOperTable": aluSecPolicerGrpOperTable,
       "aluSecPolicerGrpOperEntry": aluSecPolicerGrpOperEntry,
       "aluSecPolicerGrpOperId": aluSecPolicerGrpOperId,
       "aluSecPolicerGrpOperName": aluSecPolicerGrpOperName,
       "aluSecPolicerGrpOperDescription": aluSecPolicerGrpOperDescription,
       "aluSecPolicerGrpOperRate": aluSecPolicerGrpOperRate,
       "aluSecPolicerGrpOperRateCbs": aluSecPolicerGrpOperRateCbs,
       "aluSecPolicerGrpOperPlcyRefCount": aluSecPolicerGrpOperPlcyRefCount,
       "aluSecPolicerGrpOperFwdPktsPassed": aluSecPolicerGrpOperFwdPktsPassed,
       "aluSecPolicerGrpOperFwdBytesPassed": aluSecPolicerGrpOperFwdBytesPassed,
       "aluSecPolicerGrpOperFwdPktsDrop": aluSecPolicerGrpOperFwdPktsDrop,
       "aluSecPolicerGrpOperRevPktsPassed": aluSecPolicerGrpOperRevPktsPassed,
       "aluSecPolicerGrpOperRevBytesPassed": aluSecPolicerGrpOperRevBytesPassed,
       "aluSecPolicerGrpOperRevPktsDrop": aluSecPolicerGrpOperRevPktsDrop,
       "aluSecurityStatsObjs": aluSecurityStatsObjs,
       "aluSecSessionStatsTable": aluSecSessionStatsTable,
       "aluSecSessionStatsEntry": aluSecSessionStatsEntry,
       "aluSecSessionId": aluSecSessionId,
       "aluSecSessionOutboundZoneId": aluSecSessionOutboundZoneId,
       "aluSecSessionInboundZoneId": aluSecSessionInboundZoneId,
       "aluSecSessionFwdPktsPassed": aluSecSessionFwdPktsPassed,
       "aluSecSessionFwdBytesPassed": aluSecSessionFwdBytesPassed,
       "aluSecSessionRevPktsPassed": aluSecSessionRevPktsPassed,
       "aluSecSessionRevBytesPassed": aluSecSessionRevBytesPassed,
       "aluSecSessionFwdDropActionPkts": aluSecSessionFwdDropActionPkts,
       "aluSecSessionFwdDropIpOptPkts": aluSecSessionFwdDropIpOptPkts,
       "aluSecSessionRevDropIpOptPkts": aluSecSessionRevDropIpOptPkts,
       "aluSecSessionFwdDropMaxPkts": aluSecSessionFwdDropMaxPkts,
       "aluSecSessionRevDropMaxPkts": aluSecSessionRevDropMaxPkts,
       "aluSecSessionFwdDropMaxIcmpErr": aluSecSessionFwdDropMaxIcmpErr,
       "aluSecSessionRevDropMaxIcmpErr": aluSecSessionRevDropMaxIcmpErr,
       "aluSecSessionFwdSecurityDrop": aluSecSessionFwdSecurityDrop,
       "aluSecSessionRevSecurityDrop": aluSecSessionRevSecurityDrop,
       "aluSecSessionFwdPolicerDrop": aluSecSessionFwdPolicerDrop,
       "aluSecSessionRevPolicerDrop": aluSecSessionRevPolicerDrop,
       "aluSecSessionRevDropActionPkts": aluSecSessionRevDropActionPkts,
       "aluSecZoneStatsTable": aluSecZoneStatsTable,
       "aluSecZoneStatsEntry": aluSecZoneStatsEntry,
       "aluSecZoneId": aluSecZoneId,
       "aluSecZoneRxCtrlQueueFwdPkts": aluSecZoneRxCtrlQueueFwdPkts,
       "aluSecZoneRxCtrlQueueFwdBytes": aluSecZoneRxCtrlQueueFwdBytes,
       "aluSecZoneRxCtrlQueueDroPkts": aluSecZoneRxCtrlQueueDroPkts,
       "aluSecZoneRxCtrlQueueDroBytes": aluSecZoneRxCtrlQueueDroBytes,
       "aluSecZoneRxCtrlQueueAutoBind": aluSecZoneRxCtrlQueueAutoBind,
       "aluSecEngineStatsTable": aluSecEngineStatsTable,
       "aluSecEngineStatsEntry": aluSecEngineStatsEntry,
       "aluSecEngineId": aluSecEngineId,
       "aluSecEngineUtilization": aluSecEngineUtilization,
       "aluSecEngineRxQueueCtrlPkts": aluSecEngineRxQueueCtrlPkts,
       "aluSecEngineRxQueueDataPkts": aluSecEngineRxQueueDataPkts,
       "aluSecEngineRxQueueDropPkts": aluSecEngineRxQueueDropPkts,
       "aluSecEngineDropPkts": aluSecEngineDropPkts,
       "aluSecurityNotifyObjs": aluSecurityNotifyObjs,
       "aluSecNotifyZoneId": aluSecNotifyZoneId,
       "aluSecNotifyZoneRuleId": aluSecNotifyZoneRuleId,
       "aluSecNotifyPlcyAction": aluSecNotifyPlcyAction,
       "aluSecNotifyRuleActive": aluSecNotifyRuleActive,
       "aluSecurityLogObjs": aluSecurityLogObjs,
       "aluSecLogTable": aluSecLogTable,
       "aluSecLogEntry": aluSecLogEntry,
       "aluSecLogId": aluSecLogId,
       "aluSecLogName": aluSecLogName,
       "aluSecLogRowStatus": aluSecLogRowStatus,
       "aluSecLogDescription": aluSecLogDescription,
       "aluSecLogEnabled": aluSecLogEnabled,
       "aluSecLogDestination": aluSecLogDestination,
       "aluSecLogMemSize": aluSecLogMemSize,
       "aluSecLogMemWrap": aluSecLogMemWrap,
       "aluSecLogSysLogId": aluSecLogSysLogId,
       "aluSecLogLogProfileId": aluSecLogLogProfileId,
       "aluSecLogApplied": aluSecLogApplied,
       "aluSecLogNextEventNum": aluSecLogNextEventNum,
       "aluSecLogProfileTable": aluSecLogProfileTable,
       "aluSecLogProfileEntry": aluSecLogProfileEntry,
       "aluSecLogProfileId": aluSecLogProfileId,
       "aluSecLogProfileName": aluSecLogProfileName,
       "aluSecLogProfileRowStatus": aluSecLogProfileRowStatus,
       "aluSecLogProfileDescription": aluSecLogProfileDescription,
       "aluSecLogProfileApplied": aluSecLogProfileApplied,
       "aluSecLogEventTable": aluSecLogEventTable,
       "aluSecLogEventEntry": aluSecLogEventEntry,
       "aluSecLogEventType": aluSecLogEventType,
       "aluSecLogEventId": aluSecLogEventId,
       "aluSecLogEventName": aluSecLogEventName,
       "aluSecLogEventControl": aluSecLogEventControl,
       "aluSecMcRedundancyObjs": aluSecMcRedundancyObjs,
       "aluMcPeerFwTableLastChanged": aluMcPeerFwTableLastChanged,
       "aluMcPeerFwTable": aluMcPeerFwTable,
       "aluMcPeerFwEntry": aluMcPeerFwEntry,
       "aluMcPeerFwRowStatus": aluMcPeerFwRowStatus,
       "aluMcPeerFwLastChanged": aluMcPeerFwLastChanged,
       "aluMcPeerFwAdminState": aluMcPeerFwAdminState,
       "aluMcPeerFwSysPriority": aluMcPeerFwSysPriority,
       "aluMcPeerFwKeepAliveIntvl": aluMcPeerFwKeepAliveIntvl,
       "aluMcPeerFwHoldOnNbrFail": aluMcPeerFwHoldOnNbrFail,
       "aluMcPeerFwBootTimer": aluMcPeerFwBootTimer,
       "aluMcPeerFwBfd": aluMcPeerFwBfd,
       "aluMcPeerFwOperState": aluMcPeerFwOperState,
       "aluMcPeerFwPeerLastStateChge": aluMcPeerFwPeerLastStateChge,
       "aluMcPeerFwRefCount": aluMcPeerFwRefCount,
       "aluMcPeerFwEncryption": aluMcPeerFwEncryption,
       "aluMcPeerFwEncryptionAuthAlg": aluMcPeerFwEncryptionAuthAlg,
       "aluMcPeerFwEncryptionEncrAlg": aluMcPeerFwEncryptionEncrAlg,
       "aluMcPeerFwEncryptionActOutSa": aluMcPeerFwEncryptionActOutSa,
       "aluMcPeerFwEncryptionSpi1": aluMcPeerFwEncryptionSpi1,
       "aluMcPeerFwEncryptionSpiAuthKey1": aluMcPeerFwEncryptionSpiAuthKey1,
       "aluMcPeerFwEncryptionSpiEncrKey1": aluMcPeerFwEncryptionSpiEncrKey1,
       "aluMcPeerFwEncryptionSpi2": aluMcPeerFwEncryptionSpi2,
       "aluMcPeerFwEncryptionSpiAuthKey2": aluMcPeerFwEncryptionSpiAuthKey2,
       "aluMcPeerFwEncryptionSpiEncrKey2": aluMcPeerFwEncryptionSpiEncrKey2,
       "aluMcPeerFwElectionRole": aluMcPeerFwElectionRole,
       "aluMcPeerFwPolicySync": aluMcPeerFwPolicySync,
       "aluMcPeerFwSessionDBSync": aluMcPeerFwSessionDBSync,
       "aluSecMcRedStatsObjs": aluSecMcRedStatsObjs,
       "aluMcFwPeerStatsTable": aluMcFwPeerStatsTable,
       "aluMcFwPeerStatsEntry": aluMcFwPeerStatsEntry,
       "aluMcFwPeerStatsPktsRx": aluMcFwPeerStatsPktsRx,
       "aluMcFwPeerStatsPktsRxKpalive": aluMcFwPeerStatsPktsRxKpalive,
       "aluMcFwPeerStatsPktsRxPeerCfg": aluMcFwPeerStatsPktsRxPeerCfg,
       "aluMcFwPeerStatsPktsRxPeerData": aluMcFwPeerStatsPktsRxPeerData,
       "aluMcFwPeerStatsDropRxPeerData": aluMcFwPeerStatsDropRxPeerData,
       "aluMcFwPeerStatsDropStateDsbld": aluMcFwPeerStatsDropStateDsbld,
       "aluMcFwPeerStatsDropPktTooShrt": aluMcFwPeerStatsDropPktTooShrt,
       "aluMcFwPeerStatsDropTlvInvldSz": aluMcFwPeerStatsDropTlvInvldSz,
       "aluMcFwPeerStatsDropOutOfSeq": aluMcFwPeerStatsDropOutOfSeq,
       "aluMcFwPeerStatsDropUnknownTlv": aluMcFwPeerStatsDropUnknownTlv,
       "aluMcFwPeerStatsDropMD5": aluMcFwPeerStatsDropMD5,
       "aluMcFwPeerStatsPktsTx": aluMcFwPeerStatsPktsTx,
       "aluMcFwPeerStatsPktsTxKpalive": aluMcFwPeerStatsPktsTxKpalive,
       "aluMcFwPeerStatsPktsTxPeerCfg": aluMcFwPeerStatsPktsTxPeerCfg,
       "aluMcFwPeerStatsPktsTxPeerData": aluMcFwPeerStatsPktsTxPeerData,
       "aluMcFwPeerStatsPktsTxFailed": aluMcFwPeerStatsPktsTxFailed,
       "aluMcFwPeerStatsDropFwNoPeer": aluMcFwPeerStatsDropFwNoPeer,
       "aluMcFwGlobalStats": aluMcFwGlobalStats,
       "aluMcFwStatsPktsRx": aluMcFwStatsPktsRx,
       "aluMcFwStatsPktsRxKeepalive": aluMcFwStatsPktsRxKeepalive,
       "aluMcFwStatsPktsRxPeerConfig": aluMcFwStatsPktsRxPeerConfig,
       "aluMcFwStatsPktsRxPeerData": aluMcFwStatsPktsRxPeerData,
       "aluMcFwStatsDropRxPeerData": aluMcFwStatsDropRxPeerData,
       "aluMcFwStatsDropPktKpaliveTask": aluMcFwStatsDropPktKpaliveTask,
       "aluMcFwStatsDropPktTooShort": aluMcFwStatsDropPktTooShort,
       "aluMcFwStatsDropPktVerifyFailed": aluMcFwStatsDropPktVerifyFailed,
       "aluMcFwStatsDropTlvInvalidSize": aluMcFwStatsDropTlvInvalidSize,
       "aluMcFwStatsDropOutOfSeq": aluMcFwStatsDropOutOfSeq,
       "aluMcFwStatsDropUnknownTlv": aluMcFwStatsDropUnknownTlv,
       "aluMcFwStatsDropMD5": aluMcFwStatsDropMD5,
       "aluMcFwStatsDropUnknownPeer": aluMcFwStatsDropUnknownPeer,
       "aluMcFwStatsPktsTx": aluMcFwStatsPktsTx,
       "aluMcFwStatsPktsTxKeepalive": aluMcFwStatsPktsTxKeepalive,
       "aluMcFwStatsPktsTxPeerConfig": aluMcFwStatsPktsTxPeerConfig,
       "aluMcFwStatsPktsTxPeerData": aluMcFwStatsPktsTxPeerData,
       "aluMcFwStatsPktsTxFailed": aluMcFwStatsPktsTxFailed,
       "aluMcFwStatsDropFwNoPeer": aluMcFwStatsDropFwNoPeer,
       "aluSecMcRedNotifObjs": aluSecMcRedNotifObjs,
       "aluMcPeerFwBfdSessionOpenStatus": aluMcPeerFwBfdSessionOpenStatus,
       "aluSecurityNotifyPrefix": aluSecurityNotifyPrefix,
       "aluSecurityNotification": aluSecurityNotification,
       "aluSecPlcyActionPerformed": aluSecPlcyActionPerformed,
       "aluSecZonePlcyActionPerformed": aluSecZonePlcyActionPerformed,
       "aluSecSessionWtrMrkModified": aluSecSessionWtrMrkModified,
       "aluSecSessionHiWtrMrkCrossed": aluSecSessionHiWtrMrkCrossed,
       "aluSecSessionLoWtrMrkCrossed": aluSecSessionLoWtrMrkCrossed,
       "aluSecSessionsExhausted": aluSecSessionsExhausted,
       "aluSecZonePlcyRuleStateChange": aluSecZonePlcyRuleStateChange,
       "aluMcPeerFwBfdSessionOpen": aluMcPeerFwBfdSessionOpen,
       "aluMcPeerFwBfdSessionClose": aluMcPeerFwBfdSessionClose,
       "aluMcPeerFwBfdSessionUp": aluMcPeerFwBfdSessionUp,
       "aluMcPeerFwBfdSessionDown": aluMcPeerFwBfdSessionDown,
       "aluMcPeerFwOperDown": aluMcPeerFwOperDown,
       "aluMcPeerFwOperUp": aluMcPeerFwOperUp,
       "aluMcPeerFwElectionMaster": aluMcPeerFwElectionMaster,
       "aluMcPeerFwElectionSlave": aluMcPeerFwElectionSlave,
       "aluMcPeerFwMasterPolicySyncClr": aluMcPeerFwMasterPolicySyncClr,
       "aluMcPeerFwMasterPolicySyncSet": aluMcPeerFwMasterPolicySyncSet,
       "aluMcPeerFwSlavePolicySyncClr": aluMcPeerFwSlavePolicySyncClr,
       "aluMcPeerFwSlavePolicySyncSet": aluMcPeerFwSlavePolicySyncSet,
       "aluMcPeerFwSessionDbSyncClr": aluMcPeerFwSessionDbSyncClr,
       "aluMcPeerFwSessionDbSyncSet": aluMcPeerFwSessionDbSyncSet}
)
