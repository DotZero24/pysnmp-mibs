# SNMP MIB module (TN-SDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-SDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:02:16 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(L2RouteOrigin,
 LspIdList,
 PWTemplateId,
 SdpBindBandwidth,
 SdpBindVcType,
 SdpId,
 ServObjName,
 TlsLimitMacMove,
 VpnId,
 tnServObjs,
 tnSvcId) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "L2RouteOrigin",
    "LspIdList",
    "PWTemplateId",
    "SdpBindBandwidth",
    "SdpBindVcType",
    "SdpId",
    "ServObjName",
    "TlsLimitMacMove",
    "VpnId",
    "tnServObjs",
    "tnSvcId")

(SdpBindId,
 ServObjDesc,
 ServiceAdminStatus,
 TCpmProtPolicyID,
 TFdbTableSizeProfileID,
 TFilterID,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TQosQGrpInstanceIDorZero,
 TSdpEgressPolicyID,
 TSdpIngressPolicyID,
 TmnxBsxAarpIdOrZero,
 TmnxBsxAarpServiceRefType,
 TmnxBsxTransPrefPolicyIdOrZero,
 TmnxBsxTransitIpPolicyIdOrZero,
 TmnxCustId,
 TmnxEnabledDisabled,
 TmnxIgmpVersion,
 TmnxMplsTpGlobalID,
 TmnxMplsTpNodeID,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrMplsLspID,
 TmnxVcId) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "SdpBindId",
    "ServObjDesc",
    "ServiceAdminStatus",
    "TCpmProtPolicyID",
    "TFdbTableSizeProfileID",
    "TFilterID",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TQosQGrpInstanceIDorZero",
    "TSdpEgressPolicyID",
    "TSdpIngressPolicyID",
    "TmnxBsxAarpIdOrZero",
    "TmnxBsxAarpServiceRefType",
    "TmnxBsxTransPrefPolicyIdOrZero",
    "TmnxBsxTransitIpPolicyIdOrZero",
    "TmnxCustId",
    "TmnxEnabledDisabled",
    "TmnxIgmpVersion",
    "TmnxMplsTpGlobalID",
    "TmnxMplsTpNodeID",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrMplsLspID",
    "TmnxVcId")

(tnSRMIBModules,) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnServicesSdpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 56)
)
if mibBuilder.loadTexts:
    tnServicesSdpMIBModule.setRevisions(
        ("2020-08-21 00:00",
         "2019-08-30 00:00",
         "2019-08-16 00:00",
         "2018-12-21 00:00",
         "2018-08-31 00:00",
         "2018-07-20 00:00",
         "2015-08-13 00:00",
         "2015-06-16 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2007-10-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnSdpObjs_ObjectIdentity = ObjectIdentity
tnSdpObjs = _TnSdpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4)
)
_SdpNumEntries_Type = Integer32
_SdpNumEntries_Object = MibScalar
sdpNumEntries = _SdpNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 1),
    _SdpNumEntries_Type()
)
sdpNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpNumEntries.setStatus("current")
_SdpNextFreeId_Type = SdpId
_SdpNextFreeId_Object = MibScalar
sdpNextFreeId = _SdpNextFreeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 2),
    _SdpNextFreeId_Type()
)
sdpNextFreeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpNextFreeId.setStatus("current")
_SdpInfoTable_Object = MibTable
sdpInfoTable = _SdpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3)
)
if mibBuilder.loadTexts:
    sdpInfoTable.setStatus("current")
_SdpInfoEntry_Object = MibTableRow
sdpInfoEntry = _SdpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1)
)
sdpInfoEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SDP-MIB", "sdpId"),
)
if mibBuilder.loadTexts:
    sdpInfoEntry.setStatus("current")
_SdpId_Type = SdpId
_SdpId_Object = MibTableColumn
sdpId = _SdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 1),
    _SdpId_Type()
)
sdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpId.setStatus("current")
_SdpRowStatus_Type = RowStatus
_SdpRowStatus_Object = MibTableColumn
sdpRowStatus = _SdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 2),
    _SdpRowStatus_Type()
)
sdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpRowStatus.setStatus("current")


class _SdpDelivery_Type(Integer32):
    """Custom type sdpDelivery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("mpls", 2))
    )


_SdpDelivery_Type.__name__ = "Integer32"
_SdpDelivery_Object = MibTableColumn
sdpDelivery = _SdpDelivery_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 3),
    _SdpDelivery_Type()
)
sdpDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpDelivery.setStatus("current")
_SdpFarEndIpAddress_Type = IpAddress
_SdpFarEndIpAddress_Object = MibTableColumn
sdpFarEndIpAddress = _SdpFarEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 4),
    _SdpFarEndIpAddress_Type()
)
sdpFarEndIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFarEndIpAddress.setStatus("current")
_SdpLspList_Type = LspIdList
_SdpLspList_Object = MibTableColumn
sdpLspList = _SdpLspList_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 5),
    _SdpLspList_Type()
)
sdpLspList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLspList.setStatus("current")


class _SdpDescription_Type(ServObjDesc):
    """Custom type sdpDescription based on ServObjDesc"""
    defaultValue = OctetString("")


_SdpDescription_Type.__name__ = "ServObjDesc"
_SdpDescription_Object = MibTableColumn
sdpDescription = _SdpDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 6),
    _SdpDescription_Type()
)
sdpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpDescription.setStatus("current")


class _SdpLabelSignaling_Type(Integer32):
    """Custom type sdpLabelSignaling based on Integer32"""
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
          ("tldp", 2),
          ("bgp", 3))
    )


_SdpLabelSignaling_Type.__name__ = "Integer32"
_SdpLabelSignaling_Object = MibTableColumn
sdpLabelSignaling = _SdpLabelSignaling_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 7),
    _SdpLabelSignaling_Type()
)
sdpLabelSignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLabelSignaling.setStatus("current")


class _SdpAdminStatus_Type(ServiceAdminStatus):
    """Custom type sdpAdminStatus based on ServiceAdminStatus"""
    defaultValue = 2


_SdpAdminStatus_Type.__name__ = "ServiceAdminStatus"
_SdpAdminStatus_Object = MibTableColumn
sdpAdminStatus = _SdpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 8),
    _SdpAdminStatus_Type()
)
sdpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAdminStatus.setStatus("current")


class _SdpOperStatus_Type(Integer32):
    """Custom type sdpOperStatus based on Integer32"""
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
        *(("up", 1),
          ("notAlive", 2),
          ("notReady", 3),
          ("invalidEgressInterface", 4),
          ("transportTunnelDown", 5),
          ("down", 6))
    )


_SdpOperStatus_Type.__name__ = "Integer32"
_SdpOperStatus_Object = MibTableColumn
sdpOperStatus = _SdpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 9),
    _SdpOperStatus_Type()
)
sdpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperStatus.setStatus("current")


class _SdpAdminPathMtu_Type(Integer32):
    """Custom type sdpAdminPathMtu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1518, 9586),
    )


_SdpAdminPathMtu_Type.__name__ = "Integer32"
_SdpAdminPathMtu_Object = MibTableColumn
sdpAdminPathMtu = _SdpAdminPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 10),
    _SdpAdminPathMtu_Type()
)
sdpAdminPathMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAdminPathMtu.setStatus("current")
_SdpOperPathMtu_Type = Integer32
_SdpOperPathMtu_Object = MibTableColumn
sdpOperPathMtu = _SdpOperPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 11),
    _SdpOperPathMtu_Type()
)
sdpOperPathMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperPathMtu.setStatus("current")


class _SdpKeepAliveAdminStatus_Type(Integer32):
    """Custom type sdpKeepAliveAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SdpKeepAliveAdminStatus_Type.__name__ = "Integer32"
_SdpKeepAliveAdminStatus_Object = MibTableColumn
sdpKeepAliveAdminStatus = _SdpKeepAliveAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 12),
    _SdpKeepAliveAdminStatus_Type()
)
sdpKeepAliveAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveAdminStatus.setStatus("current")


class _SdpKeepAliveOperStatus_Type(Integer32):
    """Custom type sdpKeepAliveOperStatus based on Integer32"""
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
        *(("alive", 1),
          ("noResponse", 2),
          ("senderIdInvalid", 3),
          ("responderIdError", 4),
          ("disabled", 5))
    )


_SdpKeepAliveOperStatus_Type.__name__ = "Integer32"
_SdpKeepAliveOperStatus_Object = MibTableColumn
sdpKeepAliveOperStatus = _SdpKeepAliveOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 13),
    _SdpKeepAliveOperStatus_Type()
)
sdpKeepAliveOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpKeepAliveOperStatus.setStatus("current")


class _SdpKeepAliveHelloTime_Type(Integer32):
    """Custom type sdpKeepAliveHelloTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SdpKeepAliveHelloTime_Type.__name__ = "Integer32"
_SdpKeepAliveHelloTime_Object = MibTableColumn
sdpKeepAliveHelloTime = _SdpKeepAliveHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 14),
    _SdpKeepAliveHelloTime_Type()
)
sdpKeepAliveHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveHelloTime.setStatus("current")


class _SdpKeepAliveMaxDropCount_Type(Integer32):
    """Custom type sdpKeepAliveMaxDropCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SdpKeepAliveMaxDropCount_Type.__name__ = "Integer32"
_SdpKeepAliveMaxDropCount_Object = MibTableColumn
sdpKeepAliveMaxDropCount = _SdpKeepAliveMaxDropCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 15),
    _SdpKeepAliveMaxDropCount_Type()
)
sdpKeepAliveMaxDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveMaxDropCount.setStatus("current")


class _SdpKeepAliveHoldDownTime_Type(Integer32):
    """Custom type sdpKeepAliveHoldDownTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SdpKeepAliveHoldDownTime_Type.__name__ = "Integer32"
_SdpKeepAliveHoldDownTime_Object = MibTableColumn
sdpKeepAliveHoldDownTime = _SdpKeepAliveHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 16),
    _SdpKeepAliveHoldDownTime_Type()
)
sdpKeepAliveHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveHoldDownTime.setStatus("current")
_SdpLastMgmtChange_Type = TimeStamp
_SdpLastMgmtChange_Object = MibTableColumn
sdpLastMgmtChange = _SdpLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 17),
    _SdpLastMgmtChange_Type()
)
sdpLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLastMgmtChange.setStatus("current")


class _SdpKeepAliveHelloMessageLength_Type(Integer32):
    """Custom type sdpKeepAliveHelloMessageLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 9198),
    )


_SdpKeepAliveHelloMessageLength_Type.__name__ = "Integer32"
_SdpKeepAliveHelloMessageLength_Object = MibTableColumn
sdpKeepAliveHelloMessageLength = _SdpKeepAliveHelloMessageLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 18),
    _SdpKeepAliveHelloMessageLength_Type()
)
sdpKeepAliveHelloMessageLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveHelloMessageLength.setStatus("current")
_SdpKeepAliveNumHelloRequestMessages_Type = Unsigned32
_SdpKeepAliveNumHelloRequestMessages_Object = MibTableColumn
sdpKeepAliveNumHelloRequestMessages = _SdpKeepAliveNumHelloRequestMessages_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 19),
    _SdpKeepAliveNumHelloRequestMessages_Type()
)
sdpKeepAliveNumHelloRequestMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpKeepAliveNumHelloRequestMessages.setStatus("current")
_SdpKeepAliveNumHelloResponseMessages_Type = Unsigned32
_SdpKeepAliveNumHelloResponseMessages_Object = MibTableColumn
sdpKeepAliveNumHelloResponseMessages = _SdpKeepAliveNumHelloResponseMessages_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 20),
    _SdpKeepAliveNumHelloResponseMessages_Type()
)
sdpKeepAliveNumHelloResponseMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpKeepAliveNumHelloResponseMessages.setStatus("current")
_SdpKeepAliveNumLateHelloResponseMessages_Type = Unsigned32
_SdpKeepAliveNumLateHelloResponseMessages_Object = MibTableColumn
sdpKeepAliveNumLateHelloResponseMessages = _SdpKeepAliveNumLateHelloResponseMessages_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 21),
    _SdpKeepAliveNumLateHelloResponseMessages_Type()
)
sdpKeepAliveNumLateHelloResponseMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpKeepAliveNumLateHelloResponseMessages.setStatus("current")


class _SdpKeepAliveHelloRequestTimeout_Type(Integer32):
    """Custom type sdpKeepAliveHelloRequestTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SdpKeepAliveHelloRequestTimeout_Type.__name__ = "Integer32"
_SdpKeepAliveHelloRequestTimeout_Object = MibTableColumn
sdpKeepAliveHelloRequestTimeout = _SdpKeepAliveHelloRequestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 22),
    _SdpKeepAliveHelloRequestTimeout_Type()
)
sdpKeepAliveHelloRequestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveHelloRequestTimeout.setStatus("current")


class _SdpLdpEnabled_Type(TruthValue):
    """Custom type sdpLdpEnabled based on TruthValue"""
    defaultValue = 2


_SdpLdpEnabled_Type.__name__ = "TruthValue"
_SdpLdpEnabled_Object = MibTableColumn
sdpLdpEnabled = _SdpLdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 23),
    _SdpLdpEnabled_Type()
)
sdpLdpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLdpEnabled.setStatus("current")


class _SdpVlanVcEtype_Type(Unsigned32):
    """Custom type sdpVlanVcEtype based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_SdpVlanVcEtype_Type.__name__ = "Unsigned32"
_SdpVlanVcEtype_Object = MibTableColumn
sdpVlanVcEtype = _SdpVlanVcEtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 24),
    _SdpVlanVcEtype_Type()
)
sdpVlanVcEtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpVlanVcEtype.setStatus("current")


class _SdpAdvertisedVllMtuOverride_Type(TruthValue):
    """Custom type sdpAdvertisedVllMtuOverride based on TruthValue"""
    defaultValue = 2


_SdpAdvertisedVllMtuOverride_Type.__name__ = "TruthValue"
_SdpAdvertisedVllMtuOverride_Object = MibTableColumn
sdpAdvertisedVllMtuOverride = _SdpAdvertisedVllMtuOverride_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 25),
    _SdpAdvertisedVllMtuOverride_Type()
)
sdpAdvertisedVllMtuOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAdvertisedVllMtuOverride.setStatus("current")


class _SdpOperFlags_Type(Bits):
    """Custom type sdpOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("sdpAdminDown", 0),
          ("signalingSessionDown", 1),
          ("transportTunnelDown", 2),
          ("keepaliveFailure", 3),
          ("invalidEgressInterface", 4),
          ("noSystemIpAddress", 5),
          ("transportTunnelUnstable", 6),
          ("notOnBindingPort", 7))
    )

_SdpOperFlags_Type.__name__ = "Bits"
_SdpOperFlags_Object = MibTableColumn
sdpOperFlags = _SdpOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 26),
    _SdpOperFlags_Type()
)
sdpOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperFlags.setStatus("current")
_SdpLastStatusChange_Type = TimeStamp
_SdpLastStatusChange_Object = MibTableColumn
sdpLastStatusChange = _SdpLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 27),
    _SdpLastStatusChange_Type()
)
sdpLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLastStatusChange.setStatus("current")
_SdpMvplsMgmtService_Type = TmnxServId
_SdpMvplsMgmtService_Object = MibTableColumn
sdpMvplsMgmtService = _SdpMvplsMgmtService_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 28),
    _SdpMvplsMgmtService_Type()
)
sdpMvplsMgmtService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpMvplsMgmtService.setStatus("current")
_SdpMvplsMgmtSdpBndId_Type = SdpBindId
_SdpMvplsMgmtSdpBndId_Object = MibTableColumn
sdpMvplsMgmtSdpBndId = _SdpMvplsMgmtSdpBndId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 29),
    _SdpMvplsMgmtSdpBndId_Type()
)
sdpMvplsMgmtSdpBndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpMvplsMgmtSdpBndId.setStatus("current")


class _SdpCollectAcctStats_Type(TruthValue):
    """Custom type sdpCollectAcctStats based on TruthValue"""
    defaultValue = 2


_SdpCollectAcctStats_Type.__name__ = "TruthValue"
_SdpCollectAcctStats_Object = MibTableColumn
sdpCollectAcctStats = _SdpCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 30),
    _SdpCollectAcctStats_Type()
)
sdpCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpCollectAcctStats.setStatus("current")


class _SdpAccountingPolicyId_Type(Unsigned32):
    """Custom type sdpAccountingPolicyId based on Unsigned32"""
    defaultValue = 0


_SdpAccountingPolicyId_Type.__name__ = "Unsigned32"
_SdpAccountingPolicyId_Object = MibTableColumn
sdpAccountingPolicyId = _SdpAccountingPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 31),
    _SdpAccountingPolicyId_Type()
)
sdpAccountingPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAccountingPolicyId.setStatus("current")


class _SdpClassFwdingEnabled_Type(TruthValue):
    """Custom type sdpClassFwdingEnabled based on TruthValue"""
    defaultValue = 2


_SdpClassFwdingEnabled_Type.__name__ = "TruthValue"
_SdpClassFwdingEnabled_Object = MibTableColumn
sdpClassFwdingEnabled = _SdpClassFwdingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 32),
    _SdpClassFwdingEnabled_Type()
)
sdpClassFwdingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpClassFwdingEnabled.setStatus("current")


class _SdpClassFwdingDefaultLsp_Type(TmnxVRtrMplsLspID):
    """Custom type sdpClassFwdingDefaultLsp based on TmnxVRtrMplsLspID"""
    defaultValue = 0


_SdpClassFwdingDefaultLsp_Type.__name__ = "TmnxVRtrMplsLspID"
_SdpClassFwdingDefaultLsp_Object = MibTableColumn
sdpClassFwdingDefaultLsp = _SdpClassFwdingDefaultLsp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 33),
    _SdpClassFwdingDefaultLsp_Type()
)
sdpClassFwdingDefaultLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpClassFwdingDefaultLsp.setStatus("current")


class _SdpClassFwdingMcLsp_Type(TmnxVRtrMplsLspID):
    """Custom type sdpClassFwdingMcLsp based on TmnxVRtrMplsLspID"""
    defaultValue = 0


_SdpClassFwdingMcLsp_Type.__name__ = "TmnxVRtrMplsLspID"
_SdpClassFwdingMcLsp_Object = MibTableColumn
sdpClassFwdingMcLsp = _SdpClassFwdingMcLsp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 34),
    _SdpClassFwdingMcLsp_Type()
)
sdpClassFwdingMcLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpClassFwdingMcLsp.setStatus("current")


class _SdpMetric_Type(Unsigned32):
    """Custom type sdpMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdpMetric_Type.__name__ = "Unsigned32"
_SdpMetric_Object = MibTableColumn
sdpMetric = _SdpMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 35),
    _SdpMetric_Type()
)
sdpMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpMetric.setStatus("current")
_SdpAutoSdp_Type = TruthValue
_SdpAutoSdp_Object = MibTableColumn
sdpAutoSdp = _SdpAutoSdp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 36),
    _SdpAutoSdp_Type()
)
sdpAutoSdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoSdp.setStatus("current")
_SdpSnmpAllowed_Type = TruthValue
_SdpSnmpAllowed_Object = MibTableColumn
sdpSnmpAllowed = _SdpSnmpAllowed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 37),
    _SdpSnmpAllowed_Type()
)
sdpSnmpAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSnmpAllowed.setStatus("current")


class _SdpPBBEtype_Type(Unsigned32):
    """Custom type sdpPBBEtype based on Unsigned32"""
    defaultValue = 35047

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_SdpPBBEtype_Type.__name__ = "Unsigned32"
_SdpPBBEtype_Object = MibTableColumn
sdpPBBEtype = _SdpPBBEtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 38),
    _SdpPBBEtype_Type()
)
sdpPBBEtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPBBEtype.setStatus("current")


class _SdpBandwidthBookingFactor_Type(Unsigned32):
    """Custom type sdpBandwidthBookingFactor based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SdpBandwidthBookingFactor_Type.__name__ = "Unsigned32"
_SdpBandwidthBookingFactor_Object = MibTableColumn
sdpBandwidthBookingFactor = _SdpBandwidthBookingFactor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 39),
    _SdpBandwidthBookingFactor_Type()
)
sdpBandwidthBookingFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBandwidthBookingFactor.setStatus("current")
_SdpOperBandwidth_Type = Unsigned32
_SdpOperBandwidth_Object = MibTableColumn
sdpOperBandwidth = _SdpOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 40),
    _SdpOperBandwidth_Type()
)
sdpOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpOperBandwidth.setUnits("kilo-bits per second")
_SdpAvailableBandwidth_Type = Unsigned32
_SdpAvailableBandwidth_Object = MibTableColumn
sdpAvailableBandwidth = _SdpAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 41),
    _SdpAvailableBandwidth_Type()
)
sdpAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAvailableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpAvailableBandwidth.setUnits("kilo-bits per second")
_SdpMaxBookableBandwidth_Type = Unsigned32
_SdpMaxBookableBandwidth_Object = MibTableColumn
sdpMaxBookableBandwidth = _SdpMaxBookableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 42),
    _SdpMaxBookableBandwidth_Type()
)
sdpMaxBookableBandwidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpMaxBookableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpMaxBookableBandwidth.setUnits("kilo-bits per second")
_SdpBookedBandwidth_Type = Unsigned32
_SdpBookedBandwidth_Object = MibTableColumn
sdpBookedBandwidth = _SdpBookedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 43),
    _SdpBookedBandwidth_Type()
)
sdpBookedBandwidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpBookedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpBookedBandwidth.setUnits("kilo-bits per second")
_SdpCreationOrigin_Type = L2RouteOrigin
_SdpCreationOrigin_Object = MibTableColumn
sdpCreationOrigin = _SdpCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 44),
    _SdpCreationOrigin_Type()
)
sdpCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpCreationOrigin.setStatus("current")


class _SdpEnforceDiffServLspFc_Type(TruthValue):
    """Custom type sdpEnforceDiffServLspFc based on TruthValue"""
    defaultValue = 2


_SdpEnforceDiffServLspFc_Type.__name__ = "TruthValue"
_SdpEnforceDiffServLspFc_Object = MibTableColumn
sdpEnforceDiffServLspFc = _SdpEnforceDiffServLspFc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 45),
    _SdpEnforceDiffServLspFc_Type()
)
sdpEnforceDiffServLspFc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpEnforceDiffServLspFc.setStatus("current")


class _SdpMixedLspModeEnabled_Type(TruthValue):
    """Custom type sdpMixedLspModeEnabled based on TruthValue"""
    defaultValue = 2


_SdpMixedLspModeEnabled_Type.__name__ = "TruthValue"
_SdpMixedLspModeEnabled_Object = MibTableColumn
sdpMixedLspModeEnabled = _SdpMixedLspModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 46),
    _SdpMixedLspModeEnabled_Type()
)
sdpMixedLspModeEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpMixedLspModeEnabled.setStatus("current")


class _SdpLspRevertTime_Type(Integer32):
    """Custom type sdpLspRevertTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 600),
    )


_SdpLspRevertTime_Type.__name__ = "Integer32"
_SdpLspRevertTime_Object = MibTableColumn
sdpLspRevertTime = _SdpLspRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 47),
    _SdpLspRevertTime_Type()
)
sdpLspRevertTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLspRevertTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpLspRevertTime.setUnits("seconds")


class _SdpLspRevertTimeCountDown_Type(Integer32):
    """Custom type sdpLspRevertTimeCountDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 600),
    )


_SdpLspRevertTimeCountDown_Type.__name__ = "Integer32"
_SdpLspRevertTimeCountDown_Object = MibTableColumn
sdpLspRevertTimeCountDown = _SdpLspRevertTimeCountDown_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 48),
    _SdpLspRevertTimeCountDown_Type()
)
sdpLspRevertTimeCountDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLspRevertTimeCountDown.setStatus("current")
if mibBuilder.loadTexts:
    sdpLspRevertTimeCountDown.setUnits("seconds")
_SdpLdpLspId_Type = Unsigned32
_SdpLdpLspId_Object = MibTableColumn
sdpLdpLspId = _SdpLdpLspId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 49),
    _SdpLdpLspId_Type()
)
sdpLdpLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLdpLspId.setStatus("current")
_SdpLdpActive_Type = TruthValue
_SdpLdpActive_Object = MibTableColumn
sdpLdpActive = _SdpLdpActive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 50),
    _SdpLdpActive_Type()
)
sdpLdpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLdpActive.setStatus("obsolete")


class _SdpNetDomainName_Type(TNamedItemOrEmpty):
    """Custom type sdpNetDomainName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("default")


_SdpNetDomainName_Type.__name__ = "TNamedItemOrEmpty"
_SdpNetDomainName_Object = MibTableColumn
sdpNetDomainName = _SdpNetDomainName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 51),
    _SdpNetDomainName_Type()
)
sdpNetDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpNetDomainName.setStatus("current")


class _SdpEgressIfsNetDomainConsistent_Type(Integer32):
    """Custom type sdpEgressIfsNetDomainConsistent based on Integer32"""
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
          ("consistent", 2),
          ("inconsistent", 3))
    )


_SdpEgressIfsNetDomainConsistent_Type.__name__ = "Integer32"
_SdpEgressIfsNetDomainConsistent_Object = MibTableColumn
sdpEgressIfsNetDomainConsistent = _SdpEgressIfsNetDomainConsistent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 52),
    _SdpEgressIfsNetDomainConsistent_Type()
)
sdpEgressIfsNetDomainConsistent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpEgressIfsNetDomainConsistent.setStatus("current")


class _SdpBgpTunnelEnabled_Type(TruthValue):
    """Custom type sdpBgpTunnelEnabled based on TruthValue"""
    defaultValue = 2


_SdpBgpTunnelEnabled_Type.__name__ = "TruthValue"
_SdpBgpTunnelEnabled_Object = MibTableColumn
sdpBgpTunnelEnabled = _SdpBgpTunnelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 53),
    _SdpBgpTunnelEnabled_Type()
)
sdpBgpTunnelEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBgpTunnelEnabled.setStatus("current")
_SdpBgpTunnelLspId_Type = Unsigned32
_SdpBgpTunnelLspId_Object = MibTableColumn
sdpBgpTunnelLspId = _SdpBgpTunnelLspId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 54),
    _SdpBgpTunnelLspId_Type()
)
sdpBgpTunnelLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBgpTunnelLspId.setStatus("current")
_SdpTunnelFarEndIpAddress_Type = IpAddress
_SdpTunnelFarEndIpAddress_Object = MibTableColumn
sdpTunnelFarEndIpAddress = _SdpTunnelFarEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 55),
    _SdpTunnelFarEndIpAddress_Type()
)
sdpTunnelFarEndIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpTunnelFarEndIpAddress.setStatus("current")


class _SdpActiveLspType_Type(Integer32):
    """Custom type sdpActiveLspType based on Integer32"""
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
        *(("not-applicable", 0),
          ("rsvp", 1),
          ("ldp", 2),
          ("bgp", 3),
          ("none", 4))
    )


_SdpActiveLspType_Type.__name__ = "Integer32"
_SdpActiveLspType_Object = MibTableColumn
sdpActiveLspType = _SdpActiveLspType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 56),
    _SdpActiveLspType_Type()
)
sdpActiveLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpActiveLspType.setStatus("current")


class _SdpBindingPort_Type(TmnxPortID):
    """Custom type sdpBindingPort based on TmnxPortID"""
    defaultValue = 503316480


_SdpBindingPort_Type.__name__ = "TmnxPortID"
_SdpBindingPort_Object = MibTableColumn
sdpBindingPort = _SdpBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 57),
    _SdpBindingPort_Type()
)
sdpBindingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindingPort.setStatus("current")


class _SdpFarEndNodeId_Type(TmnxMplsTpNodeID):
    """Custom type sdpFarEndNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_SdpFarEndNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_SdpFarEndNodeId_Object = MibTableColumn
sdpFarEndNodeId = _SdpFarEndNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 58),
    _SdpFarEndNodeId_Type()
)
sdpFarEndNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFarEndNodeId.setStatus("current")


class _SdpFarEndGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type sdpFarEndGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_SdpFarEndGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_SdpFarEndGlobalId_Object = MibTableColumn
sdpFarEndGlobalId = _SdpFarEndGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 3, 1, 59),
    _SdpFarEndGlobalId_Type()
)
sdpFarEndGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFarEndGlobalId.setStatus("current")
_SdpBindTable_Object = MibTable
sdpBindTable = _SdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4)
)
if mibBuilder.loadTexts:
    sdpBindTable.setStatus("current")
_SdpBindEntry_Object = MibTableRow
sdpBindEntry = _SdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1)
)
sdpBindEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindEntry.setStatus("current")
_SdpBindId_Type = SdpBindId
_SdpBindId_Object = MibTableColumn
sdpBindId = _SdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 1),
    _SdpBindId_Type()
)
sdpBindId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBindId.setStatus("current")
_SdpBindRowStatus_Type = RowStatus
_SdpBindRowStatus_Object = MibTableColumn
sdpBindRowStatus = _SdpBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 2),
    _SdpBindRowStatus_Type()
)
sdpBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindRowStatus.setStatus("current")


class _SdpBindAdminIngressLabel_Type(Unsigned32):
    """Custom type sdpBindAdminIngressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2048, 18431),
    )


_SdpBindAdminIngressLabel_Type.__name__ = "Unsigned32"
_SdpBindAdminIngressLabel_Object = MibTableColumn
sdpBindAdminIngressLabel = _SdpBindAdminIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 3),
    _SdpBindAdminIngressLabel_Type()
)
sdpBindAdminIngressLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAdminIngressLabel.setStatus("current")


class _SdpBindAdminEgressLabel_Type(Unsigned32):
    """Custom type sdpBindAdminEgressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_SdpBindAdminEgressLabel_Type.__name__ = "Unsigned32"
_SdpBindAdminEgressLabel_Object = MibTableColumn
sdpBindAdminEgressLabel = _SdpBindAdminEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 4),
    _SdpBindAdminEgressLabel_Type()
)
sdpBindAdminEgressLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAdminEgressLabel.setStatus("current")


class _SdpBindOperIngressLabel_Type(Unsigned32):
    """Custom type sdpBindOperIngressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1048575),
    )


_SdpBindOperIngressLabel_Type.__name__ = "Unsigned32"
_SdpBindOperIngressLabel_Object = MibTableColumn
sdpBindOperIngressLabel = _SdpBindOperIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 5),
    _SdpBindOperIngressLabel_Type()
)
sdpBindOperIngressLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperIngressLabel.setStatus("current")


class _SdpBindOperEgressLabel_Type(Unsigned32):
    """Custom type sdpBindOperEgressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1048575),
    )


_SdpBindOperEgressLabel_Type.__name__ = "Unsigned32"
_SdpBindOperEgressLabel_Object = MibTableColumn
sdpBindOperEgressLabel = _SdpBindOperEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 6),
    _SdpBindOperEgressLabel_Type()
)
sdpBindOperEgressLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperEgressLabel.setStatus("current")


class _SdpBindAdminStatus_Type(ServiceAdminStatus):
    """Custom type sdpBindAdminStatus based on ServiceAdminStatus"""
    defaultValue = 1


_SdpBindAdminStatus_Type.__name__ = "ServiceAdminStatus"
_SdpBindAdminStatus_Object = MibTableColumn
sdpBindAdminStatus = _SdpBindAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 7),
    _SdpBindAdminStatus_Type()
)
sdpBindAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAdminStatus.setStatus("current")


class _SdpBindOperStatus_Type(Integer32):
    """Custom type sdpBindOperStatus based on Integer32"""
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
        *(("up", 1),
          ("noEgressLabel", 2),
          ("noIngressLabel", 3),
          ("noLabels", 4),
          ("down", 5),
          ("svcMtuMismatch", 6),
          ("sdpPathMtuTooSmall", 7),
          ("sdpNotReady", 8),
          ("sdpDown", 9),
          ("sapDown", 10))
    )


_SdpBindOperStatus_Type.__name__ = "Integer32"
_SdpBindOperStatus_Object = MibTableColumn
sdpBindOperStatus = _SdpBindOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 8),
    _SdpBindOperStatus_Type()
)
sdpBindOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperStatus.setStatus("current")
_SdpBindLastMgmtChange_Type = TimeStamp
_SdpBindLastMgmtChange_Object = MibTableColumn
sdpBindLastMgmtChange = _SdpBindLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 9),
    _SdpBindLastMgmtChange_Type()
)
sdpBindLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindLastMgmtChange.setStatus("current")


class _SdpBindType_Type(Integer32):
    """Custom type sdpBindType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spoke", 1),
          ("mesh", 2))
    )


_SdpBindType_Type.__name__ = "Integer32"
_SdpBindType_Object = MibTableColumn
sdpBindType = _SdpBindType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 10),
    _SdpBindType_Type()
)
sdpBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindType.setStatus("current")


class _SdpBindIngressMacFilterId_Type(TFilterID):
    """Custom type sdpBindIngressMacFilterId based on TFilterID"""
    defaultValue = 0


_SdpBindIngressMacFilterId_Type.__name__ = "TFilterID"
_SdpBindIngressMacFilterId_Object = MibTableColumn
sdpBindIngressMacFilterId = _SdpBindIngressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 11),
    _SdpBindIngressMacFilterId_Type()
)
sdpBindIngressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressMacFilterId.setStatus("current")


class _SdpBindIngressIpFilterId_Type(TFilterID):
    """Custom type sdpBindIngressIpFilterId based on TFilterID"""
    defaultValue = 0


_SdpBindIngressIpFilterId_Type.__name__ = "TFilterID"
_SdpBindIngressIpFilterId_Object = MibTableColumn
sdpBindIngressIpFilterId = _SdpBindIngressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 12),
    _SdpBindIngressIpFilterId_Type()
)
sdpBindIngressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressIpFilterId.setStatus("current")


class _SdpBindEgressMacFilterId_Type(TFilterID):
    """Custom type sdpBindEgressMacFilterId based on TFilterID"""
    defaultValue = 0


_SdpBindEgressMacFilterId_Type.__name__ = "TFilterID"
_SdpBindEgressMacFilterId_Object = MibTableColumn
sdpBindEgressMacFilterId = _SdpBindEgressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 13),
    _SdpBindEgressMacFilterId_Type()
)
sdpBindEgressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressMacFilterId.setStatus("current")


class _SdpBindEgressIpFilterId_Type(TFilterID):
    """Custom type sdpBindEgressIpFilterId based on TFilterID"""
    defaultValue = 0


_SdpBindEgressIpFilterId_Type.__name__ = "TFilterID"
_SdpBindEgressIpFilterId_Object = MibTableColumn
sdpBindEgressIpFilterId = _SdpBindEgressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 14),
    _SdpBindEgressIpFilterId_Type()
)
sdpBindEgressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressIpFilterId.setStatus("current")
_SdpBindVpnId_Type = VpnId
_SdpBindVpnId_Object = MibTableColumn
sdpBindVpnId = _SdpBindVpnId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 15),
    _SdpBindVpnId_Type()
)
sdpBindVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindVpnId.setStatus("current")
_SdpBindCustId_Type = TmnxCustId
_SdpBindCustId_Object = MibTableColumn
sdpBindCustId = _SdpBindCustId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 16),
    _SdpBindCustId_Type()
)
sdpBindCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCustId.setStatus("current")
_SdpBindVcType_Type = SdpBindVcType
_SdpBindVcType_Object = MibTableColumn
sdpBindVcType = _SdpBindVcType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 17),
    _SdpBindVcType_Type()
)
sdpBindVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindVcType.setStatus("current")


class _SdpBindVlanVcTag_Type(Unsigned32):
    """Custom type sdpBindVlanVcTag based on Unsigned32"""
    defaultValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SdpBindVlanVcTag_Type.__name__ = "Unsigned32"
_SdpBindVlanVcTag_Object = MibTableColumn
sdpBindVlanVcTag = _SdpBindVlanVcTag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 18),
    _SdpBindVlanVcTag_Type()
)
sdpBindVlanVcTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindVlanVcTag.setStatus("current")


class _SdpBindSplitHorizonGrp_Type(ServObjName):
    """Custom type sdpBindSplitHorizonGrp based on ServObjName"""
    defaultValue = OctetString("")


_SdpBindSplitHorizonGrp_Type.__name__ = "ServObjName"
_SdpBindSplitHorizonGrp_Object = MibTableColumn
sdpBindSplitHorizonGrp = _SdpBindSplitHorizonGrp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 19),
    _SdpBindSplitHorizonGrp_Type()
)
sdpBindSplitHorizonGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindSplitHorizonGrp.setStatus("current")


class _SdpBindOperFlags_Type(Bits):
    """Custom type sdpBindOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("sdpBindAdminDown", 0),
          ("svcAdminDown", 1),
          ("sapOperDown", 2),
          ("sdpOperDown", 3),
          ("sdpPathMtuTooSmall", 4),
          ("noIngressVcLabel", 5),
          ("noEgressVcLabel", 6),
          ("svcMtuMismatch", 7),
          ("vcTypeMismatch", 8),
          ("relearnLimitExceeded", 9),
          ("iesIfAdminDown", 10),
          ("releasedIngressVcLabel", 11),
          ("labelsExhausted", 12),
          ("svcParamMismatch", 13),
          ("insufficientBandwidth", 14),
          ("pwPeerFaultStatusBits", 15),
          ("meshSdpDown", 16),
          ("notManagedByMcRing", 17),
          ("outOfResource", 18),
          ("mhStandby", 19),
          ("oamDownMepFault", 20),
          ("oamUpMepFault", 21),
          ("standbySigSlaveTxDown", 22),
          ("operGrpDown", 23),
          ("withdrawnIngressVcLabel", 24),
          ("vplsPmsiDown", 25),
          ("recProtSrcMac", 26),
          ("peerFaultStatusTxDown", 27))
    )

_SdpBindOperFlags_Type.__name__ = "Bits"
_SdpBindOperFlags_Object = MibTableColumn
sdpBindOperFlags = _SdpBindOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 20),
    _SdpBindOperFlags_Type()
)
sdpBindOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperFlags.setStatus("current")
_SdpBindLastStatusChange_Type = TimeStamp
_SdpBindLastStatusChange_Object = MibTableColumn
sdpBindLastStatusChange = _SdpBindLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 21),
    _SdpBindLastStatusChange_Type()
)
sdpBindLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindLastStatusChange.setStatus("current")
_SdpBindIesIfIndex_Type = InterfaceIndexOrZero
_SdpBindIesIfIndex_Object = MibTableColumn
sdpBindIesIfIndex = _SdpBindIesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 22),
    _SdpBindIesIfIndex_Type()
)
sdpBindIesIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIesIfIndex.setStatus("current")
_SdpBindMacPinning_Type = TmnxEnabledDisabled
_SdpBindMacPinning_Object = MibTableColumn
sdpBindMacPinning = _SdpBindMacPinning_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 23),
    _SdpBindMacPinning_Type()
)
sdpBindMacPinning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindMacPinning.setStatus("current")


class _SdpBindIngressIpv6FilterId_Type(TFilterID):
    """Custom type sdpBindIngressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_SdpBindIngressIpv6FilterId_Type.__name__ = "TFilterID"
_SdpBindIngressIpv6FilterId_Object = MibTableColumn
sdpBindIngressIpv6FilterId = _SdpBindIngressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 24),
    _SdpBindIngressIpv6FilterId_Type()
)
sdpBindIngressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressIpv6FilterId.setStatus("current")


class _SdpBindEgressIpv6FilterId_Type(TFilterID):
    """Custom type sdpBindEgressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_SdpBindEgressIpv6FilterId_Type.__name__ = "TFilterID"
_SdpBindEgressIpv6FilterId_Object = MibTableColumn
sdpBindEgressIpv6FilterId = _SdpBindEgressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 25),
    _SdpBindEgressIpv6FilterId_Type()
)
sdpBindEgressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressIpv6FilterId.setStatus("current")


class _SdpBindCollectAcctStats_Type(TruthValue):
    """Custom type sdpBindCollectAcctStats based on TruthValue"""
    defaultValue = 2


_SdpBindCollectAcctStats_Type.__name__ = "TruthValue"
_SdpBindCollectAcctStats_Object = MibTableColumn
sdpBindCollectAcctStats = _SdpBindCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 26),
    _SdpBindCollectAcctStats_Type()
)
sdpBindCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindCollectAcctStats.setStatus("current")


class _SdpBindAccountingPolicyId_Type(Unsigned32):
    """Custom type sdpBindAccountingPolicyId based on Unsigned32"""
    defaultValue = 0


_SdpBindAccountingPolicyId_Type.__name__ = "Unsigned32"
_SdpBindAccountingPolicyId_Object = MibTableColumn
sdpBindAccountingPolicyId = _SdpBindAccountingPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 27),
    _SdpBindAccountingPolicyId_Type()
)
sdpBindAccountingPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAccountingPolicyId.setStatus("current")


class _SdpBindPwPeerStatusBits_Type(Bits):
    """Custom type sdpBindPwPeerStatusBits based on Bits"""
    namedValues = NamedValues(
        *(("pwNotForwarding", 0),
          ("lacIngressFault", 1),
          ("lacEgresssFault", 2),
          ("psnIngressFault", 3),
          ("psnEgressFault", 4),
          ("pwFwdingStandby", 5))
    )

_SdpBindPwPeerStatusBits_Type.__name__ = "Bits"
_SdpBindPwPeerStatusBits_Object = MibTableColumn
sdpBindPwPeerStatusBits = _SdpBindPwPeerStatusBits_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 28),
    _SdpBindPwPeerStatusBits_Type()
)
sdpBindPwPeerStatusBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwPeerStatusBits.setStatus("current")


class _SdpBindPeerVccvCvBits_Type(Bits):
    """Custom type sdpBindPeerVccvCvBits based on Bits"""
    namedValues = NamedValues(
        *(("icmpPing", 0),
          ("lspPing", 1),
          ("bfdFaultDetection", 2),
          ("bfdFaultDetectionAndSignalling", 3))
    )

_SdpBindPeerVccvCvBits_Type.__name__ = "Bits"
_SdpBindPeerVccvCvBits_Object = MibTableColumn
sdpBindPeerVccvCvBits = _SdpBindPeerVccvCvBits_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 29),
    _SdpBindPeerVccvCvBits_Type()
)
sdpBindPeerVccvCvBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPeerVccvCvBits.setStatus("current")


class _SdpBindPeerVccvCcBits_Type(Bits):
    """Custom type sdpBindPeerVccvCcBits based on Bits"""
    namedValues = NamedValues(
        *(("pwe3ControlWord", 0),
          ("mplsRouterAlertLabel", 1),
          ("mplsPwDemultiplexorLabel", 2))
    )

_SdpBindPeerVccvCcBits_Type.__name__ = "Bits"
_SdpBindPeerVccvCcBits_Object = MibTableColumn
sdpBindPeerVccvCcBits = _SdpBindPeerVccvCcBits_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 30),
    _SdpBindPeerVccvCcBits_Type()
)
sdpBindPeerVccvCcBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPeerVccvCcBits.setStatus("current")
_SdpBindControlWordBit_Type = TruthValue
_SdpBindControlWordBit_Object = MibTableColumn
sdpBindControlWordBit = _SdpBindControlWordBit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 31),
    _SdpBindControlWordBit_Type()
)
sdpBindControlWordBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindControlWordBit.setStatus("current")
_SdpBindOperControlWord_Type = TruthValue
_SdpBindOperControlWord_Object = MibTableColumn
sdpBindOperControlWord = _SdpBindOperControlWord_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 32),
    _SdpBindOperControlWord_Type()
)
sdpBindOperControlWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperControlWord.setStatus("current")


class _SdpBindEndPoint_Type(ServObjName):
    """Custom type sdpBindEndPoint based on ServObjName"""
    defaultValue = OctetString("")


_SdpBindEndPoint_Type.__name__ = "ServObjName"
_SdpBindEndPoint_Object = MibTableColumn
sdpBindEndPoint = _SdpBindEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 33),
    _SdpBindEndPoint_Type()
)
sdpBindEndPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEndPoint.setStatus("current")


class _SdpBindEndPointPrecedence_Type(Unsigned32):
    """Custom type sdpBindEndPointPrecedence based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SdpBindEndPointPrecedence_Type.__name__ = "Unsigned32"
_SdpBindEndPointPrecedence_Object = MibTableColumn
sdpBindEndPointPrecedence = _SdpBindEndPointPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 34),
    _SdpBindEndPointPrecedence_Type()
)
sdpBindEndPointPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEndPointPrecedence.setStatus("current")


class _SdpBindIsICB_Type(TruthValue):
    """Custom type sdpBindIsICB based on TruthValue"""
    defaultValue = 2


_SdpBindIsICB_Type.__name__ = "TruthValue"
_SdpBindIsICB_Object = MibTableColumn
sdpBindIsICB = _SdpBindIsICB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 35),
    _SdpBindIsICB_Type()
)
sdpBindIsICB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIsICB.setStatus("current")
_SdpBindPwFaultInetAddressType_Type = InetAddressType
_SdpBindPwFaultInetAddressType_Object = MibTableColumn
sdpBindPwFaultInetAddressType = _SdpBindPwFaultInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 36),
    _SdpBindPwFaultInetAddressType_Type()
)
sdpBindPwFaultInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwFaultInetAddressType.setStatus("current")


class _SdpBindPwFaultInetAddress_Type(InetAddress):
    """Custom type sdpBindPwFaultInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpBindPwFaultInetAddress_Type.__name__ = "InetAddress"
_SdpBindPwFaultInetAddress_Object = MibTableColumn
sdpBindPwFaultInetAddress = _SdpBindPwFaultInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 37),
    _SdpBindPwFaultInetAddress_Type()
)
sdpBindPwFaultInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwFaultInetAddress.setStatus("current")
_SdpBindClassFwdingOperState_Type = TmnxOperState
_SdpBindClassFwdingOperState_Object = MibTableColumn
sdpBindClassFwdingOperState = _SdpBindClassFwdingOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 38),
    _SdpBindClassFwdingOperState_Type()
)
sdpBindClassFwdingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindClassFwdingOperState.setStatus("current")


class _SdpBindForceVlanVcForwarding_Type(TruthValue):
    """Custom type sdpBindForceVlanVcForwarding based on TruthValue"""
    defaultValue = 2


_SdpBindForceVlanVcForwarding_Type.__name__ = "TruthValue"
_SdpBindForceVlanVcForwarding_Object = MibTableColumn
sdpBindForceVlanVcForwarding = _SdpBindForceVlanVcForwarding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 39),
    _SdpBindForceVlanVcForwarding_Type()
)
sdpBindForceVlanVcForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindForceVlanVcForwarding.setStatus("current")


class _SdpBindAdminBandwidth_Type(SdpBindBandwidth):
    """Custom type sdpBindAdminBandwidth based on SdpBindBandwidth"""
    defaultValue = 0


_SdpBindAdminBandwidth_Type.__name__ = "SdpBindBandwidth"
_SdpBindAdminBandwidth_Object = MibTableColumn
sdpBindAdminBandwidth = _SdpBindAdminBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 40),
    _SdpBindAdminBandwidth_Type()
)
sdpBindAdminBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAdminBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindAdminBandwidth.setUnits("kilo-bits per second")
_SdpBindOperBandwidth_Type = SdpBindBandwidth
_SdpBindOperBandwidth_Object = MibTableColumn
sdpBindOperBandwidth = _SdpBindOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 41),
    _SdpBindOperBandwidth_Type()
)
sdpBindOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindOperBandwidth.setUnits("kilo-bits per second")
_SdpBindCreationOrigin_Type = L2RouteOrigin
_SdpBindCreationOrigin_Object = MibTableColumn
sdpBindCreationOrigin = _SdpBindCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 42),
    _SdpBindCreationOrigin_Type()
)
sdpBindCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCreationOrigin.setStatus("current")


class _SdpBindDescription_Type(TItemDescription):
    """Custom type sdpBindDescription based on TItemDescription"""
    defaultValue = OctetString("")


_SdpBindDescription_Type.__name__ = "TItemDescription"
_SdpBindDescription_Object = MibTableColumn
sdpBindDescription = _SdpBindDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 43),
    _SdpBindDescription_Type()
)
sdpBindDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindDescription.setStatus("current")
_SdpBindSiteName_Type = TNamedItemOrEmpty
_SdpBindSiteName_Object = MibTableColumn
sdpBindSiteName = _SdpBindSiteName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 44),
    _SdpBindSiteName_Type()
)
sdpBindSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindSiteName.setStatus("current")


class _SdpBindHashLabel_Type(TruthValue):
    """Custom type sdpBindHashLabel based on TruthValue"""
    defaultValue = 2


_SdpBindHashLabel_Type.__name__ = "TruthValue"
_SdpBindHashLabel_Object = MibTableColumn
sdpBindHashLabel = _SdpBindHashLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 45),
    _SdpBindHashLabel_Type()
)
sdpBindHashLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindHashLabel.setStatus("current")


class _SdpBindIsaAaApplicationProfile_Type(ServObjName):
    """Custom type sdpBindIsaAaApplicationProfile based on ServObjName"""
    defaultValue = OctetString("")


_SdpBindIsaAaApplicationProfile_Type.__name__ = "ServObjName"
_SdpBindIsaAaApplicationProfile_Object = MibTableColumn
sdpBindIsaAaApplicationProfile = _SdpBindIsaAaApplicationProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 46),
    _SdpBindIsaAaApplicationProfile_Type()
)
sdpBindIsaAaApplicationProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIsaAaApplicationProfile.setStatus("current")


class _SdpBindStandbySigSlave_Type(TruthValue):
    """Custom type sdpBindStandbySigSlave based on TruthValue"""
    defaultValue = 2


_SdpBindStandbySigSlave_Type.__name__ = "TruthValue"
_SdpBindStandbySigSlave_Object = MibTableColumn
sdpBindStandbySigSlave = _SdpBindStandbySigSlave_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 47),
    _SdpBindStandbySigSlave_Type()
)
sdpBindStandbySigSlave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindStandbySigSlave.setStatus("current")


class _SdpBindHashLabelSignalCapability_Type(TruthValue):
    """Custom type sdpBindHashLabelSignalCapability based on TruthValue"""
    defaultValue = 2


_SdpBindHashLabelSignalCapability_Type.__name__ = "TruthValue"
_SdpBindHashLabelSignalCapability_Object = MibTableColumn
sdpBindHashLabelSignalCapability = _SdpBindHashLabelSignalCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 48),
    _SdpBindHashLabelSignalCapability_Type()
)
sdpBindHashLabelSignalCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindHashLabelSignalCapability.setStatus("current")


class _SdpBindIngressFlowspec_Type(TruthValue):
    """Custom type sdpBindIngressFlowspec based on TruthValue"""
    defaultValue = 2


_SdpBindIngressFlowspec_Type.__name__ = "TruthValue"
_SdpBindIngressFlowspec_Object = MibTableColumn
sdpBindIngressFlowspec = _SdpBindIngressFlowspec_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 49),
    _SdpBindIngressFlowspec_Type()
)
sdpBindIngressFlowspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressFlowspec.setStatus("current")


class _SdpBindCpmProtPolicyId_Type(TCpmProtPolicyID):
    """Custom type sdpBindCpmProtPolicyId based on TCpmProtPolicyID"""
    defaultValue = 255


_SdpBindCpmProtPolicyId_Type.__name__ = "TCpmProtPolicyID"
_SdpBindCpmProtPolicyId_Object = MibTableColumn
sdpBindCpmProtPolicyId = _SdpBindCpmProtPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 50),
    _SdpBindCpmProtPolicyId_Type()
)
sdpBindCpmProtPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindCpmProtPolicyId.setStatus("current")


class _SdpBindCpmProtMonitorMac_Type(TruthValue):
    """Custom type sdpBindCpmProtMonitorMac based on TruthValue"""
    defaultValue = 2


_SdpBindCpmProtMonitorMac_Type.__name__ = "TruthValue"
_SdpBindCpmProtMonitorMac_Object = MibTableColumn
sdpBindCpmProtMonitorMac = _SdpBindCpmProtMonitorMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 51),
    _SdpBindCpmProtMonitorMac_Type()
)
sdpBindCpmProtMonitorMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindCpmProtMonitorMac.setStatus("current")


class _SdpBindCpmProtEthCfmMonitorFlags_Type(Bits):
    """Custom type sdpBindCpmProtEthCfmMonitorFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("ethCfmMonitor", 0),
          ("ethCfmMonitorAggregate", 1),
          ("ethCfmMonitorCommittedAccessRate", 2))
    )

_SdpBindCpmProtEthCfmMonitorFlags_Type.__name__ = "Bits"
_SdpBindCpmProtEthCfmMonitorFlags_Object = MibTableColumn
sdpBindCpmProtEthCfmMonitorFlags = _SdpBindCpmProtEthCfmMonitorFlags_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 52),
    _SdpBindCpmProtEthCfmMonitorFlags_Type()
)
sdpBindCpmProtEthCfmMonitorFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindCpmProtEthCfmMonitorFlags.setStatus("current")


class _SdpBindTransitIpPolicyId_Type(TmnxBsxTransitIpPolicyIdOrZero):
    """Custom type sdpBindTransitIpPolicyId based on TmnxBsxTransitIpPolicyIdOrZero"""
    defaultValue = 0


_SdpBindTransitIpPolicyId_Type.__name__ = "TmnxBsxTransitIpPolicyIdOrZero"
_SdpBindTransitIpPolicyId_Object = MibTableColumn
sdpBindTransitIpPolicyId = _SdpBindTransitIpPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 53),
    _SdpBindTransitIpPolicyId_Type()
)
sdpBindTransitIpPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindTransitIpPolicyId.setStatus("current")
_SdpBindPwStatusSignaling_Type = TruthValue
_SdpBindPwStatusSignaling_Object = MibTableColumn
sdpBindPwStatusSignaling = _SdpBindPwStatusSignaling_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 54),
    _SdpBindPwStatusSignaling_Type()
)
sdpBindPwStatusSignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwStatusSignaling.setStatus("current")


class _SdpBindOperGrp_Type(TNamedItemOrEmpty):
    """Custom type sdpBindOperGrp based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SdpBindOperGrp_Type.__name__ = "TNamedItemOrEmpty"
_SdpBindOperGrp_Object = MibTableColumn
sdpBindOperGrp = _SdpBindOperGrp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 55),
    _SdpBindOperGrp_Type()
)
sdpBindOperGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindOperGrp.setStatus("current")


class _SdpBindMonitorOperGrp_Type(TNamedItemOrEmpty):
    """Custom type sdpBindMonitorOperGrp based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SdpBindMonitorOperGrp_Type.__name__ = "TNamedItemOrEmpty"
_SdpBindMonitorOperGrp_Object = MibTableColumn
sdpBindMonitorOperGrp = _SdpBindMonitorOperGrp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 56),
    _SdpBindMonitorOperGrp_Type()
)
sdpBindMonitorOperGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindMonitorOperGrp.setStatus("current")
_SdpBindOperHashLabel_Type = TruthValue
_SdpBindOperHashLabel_Object = MibTableColumn
sdpBindOperHashLabel = _SdpBindOperHashLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 57),
    _SdpBindOperHashLabel_Type()
)
sdpBindOperHashLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperHashLabel.setStatus("current")


class _SdpBindTransitPrefixPolicyId_Type(TmnxBsxTransPrefPolicyIdOrZero):
    """Custom type sdpBindTransitPrefixPolicyId based on TmnxBsxTransPrefPolicyIdOrZero"""
    defaultValue = 0


_SdpBindTransitPrefixPolicyId_Type.__name__ = "TmnxBsxTransPrefPolicyIdOrZero"
_SdpBindTransitPrefixPolicyId_Object = MibTableColumn
sdpBindTransitPrefixPolicyId = _SdpBindTransitPrefixPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 58),
    _SdpBindTransitPrefixPolicyId_Type()
)
sdpBindTransitPrefixPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindTransitPrefixPolicyId.setStatus("current")


class _SdpBindAarpId_Type(TmnxBsxAarpIdOrZero):
    """Custom type sdpBindAarpId based on TmnxBsxAarpIdOrZero"""
    defaultValue = 0


_SdpBindAarpId_Type.__name__ = "TmnxBsxAarpIdOrZero"
_SdpBindAarpId_Object = MibTableColumn
sdpBindAarpId = _SdpBindAarpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 59),
    _SdpBindAarpId_Type()
)
sdpBindAarpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAarpId.setStatus("current")


class _SdpBindIngressQoSNetworkPlcyId_Type(TSdpIngressPolicyID):
    """Custom type sdpBindIngressQoSNetworkPlcyId based on TSdpIngressPolicyID"""
    defaultValue = 0


_SdpBindIngressQoSNetworkPlcyId_Type.__name__ = "TSdpIngressPolicyID"
_SdpBindIngressQoSNetworkPlcyId_Object = MibTableColumn
sdpBindIngressQoSNetworkPlcyId = _SdpBindIngressQoSNetworkPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 60),
    _SdpBindIngressQoSNetworkPlcyId_Type()
)
sdpBindIngressQoSNetworkPlcyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressQoSNetworkPlcyId.setStatus("current")


class _SdpBindEgressQoSNetworkPlcyId_Type(TSdpEgressPolicyID):
    """Custom type sdpBindEgressQoSNetworkPlcyId based on TSdpEgressPolicyID"""
    defaultValue = 0


_SdpBindEgressQoSNetworkPlcyId_Type.__name__ = "TSdpEgressPolicyID"
_SdpBindEgressQoSNetworkPlcyId_Object = MibTableColumn
sdpBindEgressQoSNetworkPlcyId = _SdpBindEgressQoSNetworkPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 61),
    _SdpBindEgressQoSNetworkPlcyId_Type()
)
sdpBindEgressQoSNetworkPlcyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressQoSNetworkPlcyId.setStatus("current")


class _SdpBindIngressQoSFpRedirectQGrp_Type(TNamedItemOrEmpty):
    """Custom type sdpBindIngressQoSFpRedirectQGrp based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SdpBindIngressQoSFpRedirectQGrp_Type.__name__ = "TNamedItemOrEmpty"
_SdpBindIngressQoSFpRedirectQGrp_Object = MibTableColumn
sdpBindIngressQoSFpRedirectQGrp = _SdpBindIngressQoSFpRedirectQGrp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 62),
    _SdpBindIngressQoSFpRedirectQGrp_Type()
)
sdpBindIngressQoSFpRedirectQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressQoSFpRedirectQGrp.setStatus("current")


class _SdpBindEgressQoSPortRedirectQGrp_Type(TNamedItemOrEmpty):
    """Custom type sdpBindEgressQoSPortRedirectQGrp based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_SdpBindEgressQoSPortRedirectQGrp_Type.__name__ = "TNamedItemOrEmpty"
_SdpBindEgressQoSPortRedirectQGrp_Object = MibTableColumn
sdpBindEgressQoSPortRedirectQGrp = _SdpBindEgressQoSPortRedirectQGrp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 63),
    _SdpBindEgressQoSPortRedirectQGrp_Type()
)
sdpBindEgressQoSPortRedirectQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressQoSPortRedirectQGrp.setStatus("current")


class _SdpBindIngressQoSInstanceId_Type(TQosQGrpInstanceIDorZero):
    """Custom type sdpBindIngressQoSInstanceId based on TQosQGrpInstanceIDorZero"""
    defaultValue = 0


_SdpBindIngressQoSInstanceId_Type.__name__ = "TQosQGrpInstanceIDorZero"
_SdpBindIngressQoSInstanceId_Object = MibTableColumn
sdpBindIngressQoSInstanceId = _SdpBindIngressQoSInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 64),
    _SdpBindIngressQoSInstanceId_Type()
)
sdpBindIngressQoSInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressQoSInstanceId.setStatus("current")


class _SdpBindEgressQoSInstanceId_Type(TQosQGrpInstanceIDorZero):
    """Custom type sdpBindEgressQoSInstanceId based on TQosQGrpInstanceIDorZero"""
    defaultValue = 0


_SdpBindEgressQoSInstanceId_Type.__name__ = "TQosQGrpInstanceIDorZero"
_SdpBindEgressQoSInstanceId_Object = MibTableColumn
sdpBindEgressQoSInstanceId = _SdpBindEgressQoSInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 65),
    _SdpBindEgressQoSInstanceId_Type()
)
sdpBindEgressQoSInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressQoSInstanceId.setStatus("current")


class _SdpBindAarpServRefType_Type(TmnxBsxAarpServiceRefType):
    """Custom type sdpBindAarpServRefType based on TmnxBsxAarpServiceRefType"""
    defaultValue = 0


_SdpBindAarpServRefType_Type.__name__ = "TmnxBsxAarpServiceRefType"
_SdpBindAarpServRefType_Object = MibTableColumn
sdpBindAarpServRefType = _SdpBindAarpServRefType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 66),
    _SdpBindAarpServRefType_Type()
)
sdpBindAarpServRefType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAarpServRefType.setStatus("current")


class _SdpBindPwLocalStatusBits_Type(Bits):
    """Custom type sdpBindPwLocalStatusBits based on Bits"""
    namedValues = NamedValues(
        *(("pwNotForwarding", 0),
          ("lacIngressFault", 1),
          ("lacEgresssFault", 2),
          ("psnIngressFault", 3),
          ("psnEgressFault", 4),
          ("pwFwdingStandby", 5))
    )

_SdpBindPwLocalStatusBits_Type.__name__ = "Bits"
_SdpBindPwLocalStatusBits_Object = MibTableColumn
sdpBindPwLocalStatusBits = _SdpBindPwLocalStatusBits_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 67),
    _SdpBindPwLocalStatusBits_Type()
)
sdpBindPwLocalStatusBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwLocalStatusBits.setStatus("current")


class _SdpBindBlockOnPeerFault_Type(TruthValue):
    """Custom type sdpBindBlockOnPeerFault based on TruthValue"""
    defaultValue = 2


_SdpBindBlockOnPeerFault_Type.__name__ = "TruthValue"
_SdpBindBlockOnPeerFault_Object = MibTableColumn
sdpBindBlockOnPeerFault = _SdpBindBlockOnPeerFault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 68),
    _SdpBindBlockOnPeerFault_Type()
)
sdpBindBlockOnPeerFault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindBlockOnPeerFault.setStatus("current")


class _SdpBindStatsCounterEnable_Type(TruthValue):
    """Custom type sdpBindStatsCounterEnable based on TruthValue"""
    defaultValue = 1


_SdpBindStatsCounterEnable_Type.__name__ = "TruthValue"
_SdpBindStatsCounterEnable_Object = MibTableColumn
sdpBindStatsCounterEnable = _SdpBindStatsCounterEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 4, 1, 69),
    _SdpBindStatsCounterEnable_Type()
)
sdpBindStatsCounterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindStatsCounterEnable.setStatus("deprecated")
_SdpBindBaseStatsTable_Object = MibTable
sdpBindBaseStatsTable = _SdpBindBaseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 5)
)
if mibBuilder.loadTexts:
    sdpBindBaseStatsTable.setStatus("current")
_SdpBindBaseStatsEntry_Object = MibTableRow
sdpBindBaseStatsEntry = _SdpBindBaseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 5, 1)
)
sdpBindBaseStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindBaseStatsEntry.setStatus("current")
_SdpBindBaseStatsIngressForwardedPackets_Type = Counter64
_SdpBindBaseStatsIngressForwardedPackets_Object = MibTableColumn
sdpBindBaseStatsIngressForwardedPackets = _SdpBindBaseStatsIngressForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 5, 1, 1),
    _SdpBindBaseStatsIngressForwardedPackets_Type()
)
sdpBindBaseStatsIngressForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsIngressForwardedPackets.setStatus("current")
_SdpBindBaseStatsIngressDroppedPackets_Type = Counter64
_SdpBindBaseStatsIngressDroppedPackets_Object = MibTableColumn
sdpBindBaseStatsIngressDroppedPackets = _SdpBindBaseStatsIngressDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 5, 1, 2),
    _SdpBindBaseStatsIngressDroppedPackets_Type()
)
sdpBindBaseStatsIngressDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsIngressDroppedPackets.setStatus("current")
_SdpBindBaseStatsEgressForwardedPackets_Type = Counter64
_SdpBindBaseStatsEgressForwardedPackets_Object = MibTableColumn
sdpBindBaseStatsEgressForwardedPackets = _SdpBindBaseStatsEgressForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 5, 1, 3),
    _SdpBindBaseStatsEgressForwardedPackets_Type()
)
sdpBindBaseStatsEgressForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsEgressForwardedPackets.setStatus("current")
_SdpBindBaseStatsEgressForwardedOctets_Type = Counter64
_SdpBindBaseStatsEgressForwardedOctets_Object = MibTableColumn
sdpBindBaseStatsEgressForwardedOctets = _SdpBindBaseStatsEgressForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 5, 1, 4),
    _SdpBindBaseStatsEgressForwardedOctets_Type()
)
sdpBindBaseStatsEgressForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsEgressForwardedOctets.setStatus("current")
_SdpBindBaseStatsCustId_Type = TmnxCustId
_SdpBindBaseStatsCustId_Object = MibTableColumn
sdpBindBaseStatsCustId = _SdpBindBaseStatsCustId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 5, 1, 5),
    _SdpBindBaseStatsCustId_Type()
)
sdpBindBaseStatsCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsCustId.setStatus("current")
_SdpBindBaseStatsIngFwdOctets_Type = Counter64
_SdpBindBaseStatsIngFwdOctets_Object = MibTableColumn
sdpBindBaseStatsIngFwdOctets = _SdpBindBaseStatsIngFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 5, 1, 6),
    _SdpBindBaseStatsIngFwdOctets_Type()
)
sdpBindBaseStatsIngFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsIngFwdOctets.setStatus("current")
_SdpBindBaseStatsIngDropOctets_Type = Counter64
_SdpBindBaseStatsIngDropOctets_Object = MibTableColumn
sdpBindBaseStatsIngDropOctets = _SdpBindBaseStatsIngDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 5, 1, 7),
    _SdpBindBaseStatsIngDropOctets_Type()
)
sdpBindBaseStatsIngDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsIngDropOctets.setStatus("current")
_SdpBindTlsTable_Object = MibTable
sdpBindTlsTable = _SdpBindTlsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6)
)
if mibBuilder.loadTexts:
    sdpBindTlsTable.setStatus("current")
_SdpBindTlsEntry_Object = MibTableRow
sdpBindTlsEntry = _SdpBindTlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6, 1)
)
sdpBindTlsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindTlsEntry.setStatus("current")


class _SdpBindTlsMacAddressLimit_Type(Integer32):
    """Custom type sdpBindTlsMacAddressLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511999),
    )


_SdpBindTlsMacAddressLimit_Type.__name__ = "Integer32"
_SdpBindTlsMacAddressLimit_Object = MibTableColumn
sdpBindTlsMacAddressLimit = _SdpBindTlsMacAddressLimit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6, 1, 19),
    _SdpBindTlsMacAddressLimit_Type()
)
sdpBindTlsMacAddressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMacAddressLimit.setStatus("current")
_SdpBindTlsNumMacAddresses_Type = Integer32
_SdpBindTlsNumMacAddresses_Object = MibTableColumn
sdpBindTlsNumMacAddresses = _SdpBindTlsNumMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6, 1, 20),
    _SdpBindTlsNumMacAddresses_Type()
)
sdpBindTlsNumMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsNumMacAddresses.setStatus("current")
_SdpBindTlsNumStaticMacAddresses_Type = Integer32
_SdpBindTlsNumStaticMacAddresses_Object = MibTableColumn
sdpBindTlsNumStaticMacAddresses = _SdpBindTlsNumStaticMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6, 1, 21),
    _SdpBindTlsNumStaticMacAddresses_Type()
)
sdpBindTlsNumStaticMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsNumStaticMacAddresses.setStatus("current")


class _SdpBindTlsMacLearning_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsMacLearning based on TmnxEnabledDisabled"""
    defaultValue = 1


_SdpBindTlsMacLearning_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindTlsMacLearning_Object = MibTableColumn
sdpBindTlsMacLearning = _SdpBindTlsMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6, 1, 22),
    _SdpBindTlsMacLearning_Type()
)
sdpBindTlsMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMacLearning.setStatus("current")


class _SdpBindTlsMacAgeing_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsMacAgeing based on TmnxEnabledDisabled"""
    defaultValue = 1


_SdpBindTlsMacAgeing_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindTlsMacAgeing_Object = MibTableColumn
sdpBindTlsMacAgeing = _SdpBindTlsMacAgeing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6, 1, 23),
    _SdpBindTlsMacAgeing_Type()
)
sdpBindTlsMacAgeing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMacAgeing.setStatus("current")


class _SdpBindTlsLimitMacMove_Type(TlsLimitMacMove):
    """Custom type sdpBindTlsLimitMacMove based on TlsLimitMacMove"""
    defaultValue = 1


_SdpBindTlsLimitMacMove_Type.__name__ = "TlsLimitMacMove"
_SdpBindTlsLimitMacMove_Object = MibTableColumn
sdpBindTlsLimitMacMove = _SdpBindTlsLimitMacMove_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6, 1, 31),
    _SdpBindTlsLimitMacMove_Type()
)
sdpBindTlsLimitMacMove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsLimitMacMove.setStatus("current")


class _SdpBindTlsDiscardUnknownSource_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsDiscardUnknownSource based on TmnxEnabledDisabled"""
    defaultValue = 2


_SdpBindTlsDiscardUnknownSource_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindTlsDiscardUnknownSource_Object = MibTableColumn
sdpBindTlsDiscardUnknownSource = _SdpBindTlsDiscardUnknownSource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6, 1, 32),
    _SdpBindTlsDiscardUnknownSource_Type()
)
sdpBindTlsDiscardUnknownSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsDiscardUnknownSource.setStatus("current")


class _SdpBindTlsL2ptTermination_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsL2ptTermination based on TmnxEnabledDisabled"""
    defaultValue = 2


_SdpBindTlsL2ptTermination_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindTlsL2ptTermination_Object = MibTableColumn
sdpBindTlsL2ptTermination = _SdpBindTlsL2ptTermination_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6, 1, 37),
    _SdpBindTlsL2ptTermination_Type()
)
sdpBindTlsL2ptTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptTermination.setStatus("current")


class _SdpBindTlsIgnoreStandbySig_Type(TruthValue):
    """Custom type sdpBindTlsIgnoreStandbySig based on TruthValue"""
    defaultValue = 2


_SdpBindTlsIgnoreStandbySig_Type.__name__ = "TruthValue"
_SdpBindTlsIgnoreStandbySig_Object = MibTableColumn
sdpBindTlsIgnoreStandbySig = _SdpBindTlsIgnoreStandbySig_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6, 1, 48),
    _SdpBindTlsIgnoreStandbySig_Type()
)
sdpBindTlsIgnoreStandbySig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsIgnoreStandbySig.setStatus("current")


class _SdpBindTlsBlockOnMeshFail_Type(TruthValue):
    """Custom type sdpBindTlsBlockOnMeshFail based on TruthValue"""
    defaultValue = 2


_SdpBindTlsBlockOnMeshFail_Type.__name__ = "TruthValue"
_SdpBindTlsBlockOnMeshFail_Object = MibTableColumn
sdpBindTlsBlockOnMeshFail = _SdpBindTlsBlockOnMeshFail_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6, 1, 49),
    _SdpBindTlsBlockOnMeshFail_Type()
)
sdpBindTlsBlockOnMeshFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsBlockOnMeshFail.setStatus("current")


class _SdpBindTlsFdbTableSizeProfId_Type(TFdbTableSizeProfileID):
    """Custom type sdpBindTlsFdbTableSizeProfId based on TFdbTableSizeProfileID"""
    defaultValue = 1


_SdpBindTlsFdbTableSizeProfId_Type.__name__ = "TFdbTableSizeProfileID"
_SdpBindTlsFdbTableSizeProfId_Object = MibTableColumn
sdpBindTlsFdbTableSizeProfId = _SdpBindTlsFdbTableSizeProfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 6, 1, 55),
    _SdpBindTlsFdbTableSizeProfId_Type()
)
sdpBindTlsFdbTableSizeProfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsFdbTableSizeProfId.setStatus("deprecated")
_SdpFCMappingTable_Object = MibTable
sdpFCMappingTable = _SdpFCMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 12)
)
if mibBuilder.loadTexts:
    sdpFCMappingTable.setStatus("current")
_SdpFCMappingEntry_Object = MibTableRow
sdpFCMappingEntry = _SdpFCMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 12, 1)
)
sdpFCMappingEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SDP-MIB", "sdpId"),
    (0, "TN-SDP-MIB", "sdpFCMappingFCName"),
)
if mibBuilder.loadTexts:
    sdpFCMappingEntry.setStatus("current")
_SdpFCMappingFCName_Type = TNamedItem
_SdpFCMappingFCName_Object = MibTableColumn
sdpFCMappingFCName = _SdpFCMappingFCName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 12, 1, 1),
    _SdpFCMappingFCName_Type()
)
sdpFCMappingFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpFCMappingFCName.setStatus("current")
_SdpFCMappingRowStatus_Type = RowStatus
_SdpFCMappingRowStatus_Object = MibTableColumn
sdpFCMappingRowStatus = _SdpFCMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 12, 1, 2),
    _SdpFCMappingRowStatus_Type()
)
sdpFCMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFCMappingRowStatus.setStatus("current")
_SdpFCMappingLspId_Type = TmnxVRtrMplsLspID
_SdpFCMappingLspId_Object = MibTableColumn
sdpFCMappingLspId = _SdpFCMappingLspId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 12, 1, 3),
    _SdpFCMappingLspId_Type()
)
sdpFCMappingLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFCMappingLspId.setStatus("current")
_PwTemplateTableLastChanged_Type = TimeStamp
_PwTemplateTableLastChanged_Object = MibScalar
pwTemplateTableLastChanged = _PwTemplateTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 17),
    _PwTemplateTableLastChanged_Type()
)
pwTemplateTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateTableLastChanged.setStatus("current")
_PwTemplateTable_Object = MibTable
pwTemplateTable = _PwTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 18)
)
if mibBuilder.loadTexts:
    pwTemplateTable.setStatus("current")
_PwTemplateEntry_Object = MibTableRow
pwTemplateEntry = _PwTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 18, 1)
)
pwTemplateEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SDP-MIB", "pwTemplateId"),
)
if mibBuilder.loadTexts:
    pwTemplateEntry.setStatus("current")
_PwTemplateId_Type = PWTemplateId
_PwTemplateId_Object = MibTableColumn
pwTemplateId = _PwTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 18, 1, 1),
    _PwTemplateId_Type()
)
pwTemplateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateId.setStatus("current")
_PwTemplateLastChanged_Type = TimeStamp
_PwTemplateLastChanged_Object = MibTableColumn
pwTemplateLastChanged = _PwTemplateLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 18, 1, 3),
    _PwTemplateLastChanged_Type()
)
pwTemplateLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateLastChanged.setStatus("current")


class _PwTemplateIgmpFastLeave_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateIgmpFastLeave based on TmnxEnabledDisabled"""
    defaultValue = 2


_PwTemplateIgmpFastLeave_Type.__name__ = "TmnxEnabledDisabled"
_PwTemplateIgmpFastLeave_Object = MibTableColumn
pwTemplateIgmpFastLeave = _PwTemplateIgmpFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 18, 1, 25),
    _PwTemplateIgmpFastLeave_Type()
)
pwTemplateIgmpFastLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpFastLeave.setStatus("current")


class _PwTemplateIgmpLastMembIntvl_Type(Unsigned32):
    """Custom type pwTemplateIgmpLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_PwTemplateIgmpLastMembIntvl_Type.__name__ = "Unsigned32"
_PwTemplateIgmpLastMembIntvl_Object = MibTableColumn
pwTemplateIgmpLastMembIntvl = _PwTemplateIgmpLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 18, 1, 27),
    _PwTemplateIgmpLastMembIntvl_Type()
)
pwTemplateIgmpLastMembIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    pwTemplateIgmpLastMembIntvl.setUnits("deci-seconds")


class _PwTemplateIgmpMaxNbrGrps_Type(Unsigned32):
    """Custom type pwTemplateIgmpMaxNbrGrps based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PwTemplateIgmpMaxNbrGrps_Type.__name__ = "Unsigned32"
_PwTemplateIgmpMaxNbrGrps_Object = MibTableColumn
pwTemplateIgmpMaxNbrGrps = _PwTemplateIgmpMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 18, 1, 28),
    _PwTemplateIgmpMaxNbrGrps_Type()
)
pwTemplateIgmpMaxNbrGrps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpMaxNbrGrps.setStatus("current")


class _PwTemplateIgmpGenQueryIntvl_Type(Unsigned32):
    """Custom type pwTemplateIgmpGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_PwTemplateIgmpGenQueryIntvl_Type.__name__ = "Unsigned32"
_PwTemplateIgmpGenQueryIntvl_Object = MibTableColumn
pwTemplateIgmpGenQueryIntvl = _PwTemplateIgmpGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 18, 1, 29),
    _PwTemplateIgmpGenQueryIntvl_Type()
)
pwTemplateIgmpGenQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    pwTemplateIgmpGenQueryIntvl.setUnits("seconds")


class _PwTemplateIgmpQueryRespIntvl_Type(Unsigned32):
    """Custom type pwTemplateIgmpQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_PwTemplateIgmpQueryRespIntvl_Type.__name__ = "Unsigned32"
_PwTemplateIgmpQueryRespIntvl_Object = MibTableColumn
pwTemplateIgmpQueryRespIntvl = _PwTemplateIgmpQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 18, 1, 30),
    _PwTemplateIgmpQueryRespIntvl_Type()
)
pwTemplateIgmpQueryRespIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    pwTemplateIgmpQueryRespIntvl.setUnits("seconds")


class _PwTemplateIgmpRobustCount_Type(Unsigned32):
    """Custom type pwTemplateIgmpRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_PwTemplateIgmpRobustCount_Type.__name__ = "Unsigned32"
_PwTemplateIgmpRobustCount_Object = MibTableColumn
pwTemplateIgmpRobustCount = _PwTemplateIgmpRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 18, 1, 31),
    _PwTemplateIgmpRobustCount_Type()
)
pwTemplateIgmpRobustCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpRobustCount.setStatus("current")


class _PwTemplateIgmpSendQueries_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateIgmpSendQueries based on TmnxEnabledDisabled"""
    defaultValue = 2


_PwTemplateIgmpSendQueries_Type.__name__ = "TmnxEnabledDisabled"
_PwTemplateIgmpSendQueries_Object = MibTableColumn
pwTemplateIgmpSendQueries = _PwTemplateIgmpSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 18, 1, 32),
    _PwTemplateIgmpSendQueries_Type()
)
pwTemplateIgmpSendQueries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpSendQueries.setStatus("current")


class _PwTemplateIgmpVersion_Type(TmnxIgmpVersion):
    """Custom type pwTemplateIgmpVersion based on TmnxIgmpVersion"""
    defaultValue = 3


_PwTemplateIgmpVersion_Type.__name__ = "TmnxIgmpVersion"
_PwTemplateIgmpVersion_Object = MibTableColumn
pwTemplateIgmpVersion = _PwTemplateIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 18, 1, 36),
    _PwTemplateIgmpVersion_Type()
)
pwTemplateIgmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpVersion.setStatus("current")
_PwTemplateIgmpSnpgGrpSrcTblLC_Type = TimeStamp
_PwTemplateIgmpSnpgGrpSrcTblLC_Object = MibScalar
pwTemplateIgmpSnpgGrpSrcTblLC = _PwTemplateIgmpSnpgGrpSrcTblLC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 19),
    _PwTemplateIgmpSnpgGrpSrcTblLC_Type()
)
pwTemplateIgmpSnpgGrpSrcTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpSrcTblLC.setStatus("current")
_PwTemplateIgmpSnpgGrpSrcTable_Object = MibTable
pwTemplateIgmpSnpgGrpSrcTable = _PwTemplateIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 20)
)
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpSrcTable.setStatus("current")
_PwTemplateIgmpSnpgGrpSrcEntry_Object = MibTableRow
pwTemplateIgmpSnpgGrpSrcEntry = _PwTemplateIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 20, 1)
)
pwTemplateIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SDP-MIB", "pwTemplateId"),
    (0, "TN-SDP-MIB", "pwTemplateIgmpSnpgGrpAddrType"),
    (0, "TN-SDP-MIB", "pwTemplateIgmpSnpgGrpAddr"),
    (0, "TN-SDP-MIB", "pwTemplateIgmpSnpgSrcAddrType"),
    (0, "TN-SDP-MIB", "pwTemplateIgmpSnpgSrcAddr"),
)
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpSrcEntry.setStatus("current")
_PwTemplateIgmpSnpgGrpAddrType_Type = InetAddressType
_PwTemplateIgmpSnpgGrpAddrType_Object = MibTableColumn
pwTemplateIgmpSnpgGrpAddrType = _PwTemplateIgmpSnpgGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 20, 1, 1),
    _PwTemplateIgmpSnpgGrpAddrType_Type()
)
pwTemplateIgmpSnpgGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpAddrType.setStatus("current")


class _PwTemplateIgmpSnpgGrpAddr_Type(InetAddress):
    """Custom type pwTemplateIgmpSnpgGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_PwTemplateIgmpSnpgGrpAddr_Type.__name__ = "InetAddress"
_PwTemplateIgmpSnpgGrpAddr_Object = MibTableColumn
pwTemplateIgmpSnpgGrpAddr = _PwTemplateIgmpSnpgGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 20, 1, 2),
    _PwTemplateIgmpSnpgGrpAddr_Type()
)
pwTemplateIgmpSnpgGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpAddr.setStatus("current")
_PwTemplateIgmpSnpgSrcAddrType_Type = InetAddressType
_PwTemplateIgmpSnpgSrcAddrType_Object = MibTableColumn
pwTemplateIgmpSnpgSrcAddrType = _PwTemplateIgmpSnpgSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 20, 1, 3),
    _PwTemplateIgmpSnpgSrcAddrType_Type()
)
pwTemplateIgmpSnpgSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgSrcAddrType.setStatus("current")


class _PwTemplateIgmpSnpgSrcAddr_Type(InetAddress):
    """Custom type pwTemplateIgmpSnpgSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_PwTemplateIgmpSnpgSrcAddr_Type.__name__ = "InetAddress"
_PwTemplateIgmpSnpgSrcAddr_Object = MibTableColumn
pwTemplateIgmpSnpgSrcAddr = _PwTemplateIgmpSnpgSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 20, 1, 4),
    _PwTemplateIgmpSnpgSrcAddr_Type()
)
pwTemplateIgmpSnpgSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgSrcAddr.setStatus("current")
_PwTemplateIgmpSnpgRowStatus_Type = RowStatus
_PwTemplateIgmpSnpgRowStatus_Object = MibTableColumn
pwTemplateIgmpSnpgRowStatus = _PwTemplateIgmpSnpgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 20, 1, 5),
    _PwTemplateIgmpSnpgRowStatus_Type()
)
pwTemplateIgmpSnpgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgRowStatus.setStatus("current")
_PwTemplateIgmpSnpgLastChngd_Type = TimeStamp
_PwTemplateIgmpSnpgLastChngd_Object = MibTableColumn
pwTemplateIgmpSnpgLastChngd = _PwTemplateIgmpSnpgLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 20, 1, 6),
    _PwTemplateIgmpSnpgLastChngd_Type()
)
pwTemplateIgmpSnpgLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgLastChngd.setStatus("current")
_SdpPwPortTblLastChanged_Type = TimeStamp
_SdpPwPortTblLastChanged_Object = MibScalar
sdpPwPortTblLastChanged = _SdpPwPortTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 40),
    _SdpPwPortTblLastChanged_Type()
)
sdpPwPortTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpPwPortTblLastChanged.setStatus("current")
_SdpPwPortTable_Object = MibTable
sdpPwPortTable = _SdpPwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41)
)
if mibBuilder.loadTexts:
    sdpPwPortTable.setStatus("current")
_SdpPwPortEntry_Object = MibTableRow
sdpPwPortEntry = _SdpPwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1)
)
sdpPwPortEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SDP-MIB", "sdpId"),
    (0, "TN-SDP-MIB", "sdpPwPortId"),
)
if mibBuilder.loadTexts:
    sdpPwPortEntry.setStatus("current")


class _SdpPwPortId_Type(Unsigned32):
    """Custom type sdpPwPortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10239),
    )


_SdpPwPortId_Type.__name__ = "Unsigned32"
_SdpPwPortId_Object = MibTableColumn
sdpPwPortId = _SdpPwPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1, 1),
    _SdpPwPortId_Type()
)
sdpPwPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpPwPortId.setStatus("current")
_SdpPwPortRowStatus_Type = RowStatus
_SdpPwPortRowStatus_Object = MibTableColumn
sdpPwPortRowStatus = _SdpPwPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1, 2),
    _SdpPwPortRowStatus_Type()
)
sdpPwPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortRowStatus.setStatus("current")
_SdpPwPortLastChgd_Type = TimeStamp
_SdpPwPortLastChgd_Object = MibTableColumn
sdpPwPortLastChgd = _SdpPwPortLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1, 3),
    _SdpPwPortLastChgd_Type()
)
sdpPwPortLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpPwPortLastChgd.setStatus("current")


class _SdpPwPortAdminStatus_Type(ServiceAdminStatus):
    """Custom type sdpPwPortAdminStatus based on ServiceAdminStatus"""
    defaultValue = 2


_SdpPwPortAdminStatus_Type.__name__ = "ServiceAdminStatus"
_SdpPwPortAdminStatus_Object = MibTableColumn
sdpPwPortAdminStatus = _SdpPwPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1, 4),
    _SdpPwPortAdminStatus_Type()
)
sdpPwPortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortAdminStatus.setStatus("current")
_SdpPwPortVcId_Type = TmnxVcId
_SdpPwPortVcId_Object = MibTableColumn
sdpPwPortVcId = _SdpPwPortVcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1, 5),
    _SdpPwPortVcId_Type()
)
sdpPwPortVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortVcId.setStatus("current")


class _SdpPwPortEncapType_Type(Integer32):
    """Custom type sdpPwPortEncapType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dot1q", 2),
          ("qinq", 10))
    )


_SdpPwPortEncapType_Type.__name__ = "Integer32"
_SdpPwPortEncapType_Object = MibTableColumn
sdpPwPortEncapType = _SdpPwPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1, 6),
    _SdpPwPortEncapType_Type()
)
sdpPwPortEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortEncapType.setStatus("current")


class _SdpPwPortOperStatus_Type(Integer32):
    """Custom type sdpPwPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 5))
    )


_SdpPwPortOperStatus_Type.__name__ = "Integer32"
_SdpPwPortOperStatus_Object = MibTableColumn
sdpPwPortOperStatus = _SdpPwPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1, 7),
    _SdpPwPortOperStatus_Type()
)
sdpPwPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpPwPortOperStatus.setStatus("current")


class _SdpPwPortOperFlags_Type(Bits):
    """Custom type sdpPwPortOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("sdpBindAdminDown", 0),
          ("svcAdminDown", 1),
          ("sapOperDown", 2),
          ("sdpOperDown", 3),
          ("sdpPathMtuTooSmall", 4),
          ("noIngressVcLabel", 5),
          ("noEgressVcLabel", 6),
          ("svcMtuMismatch", 7),
          ("vcTypeMismatch", 8),
          ("relearnLimitExceeded", 9),
          ("iesIfAdminDown", 10),
          ("releasedIngressVcLabel", 11),
          ("labelsExhausted", 12),
          ("svcParamMismatch", 13),
          ("insufficientBandwidth", 14),
          ("pwPeerFaultStatusBits", 15),
          ("meshSdpDown", 16),
          ("notManagedByMcRing", 17),
          ("outOfResource", 18),
          ("mhStandby", 19),
          ("oamDownMepFault", 20),
          ("oamUpMepFault", 21),
          ("standbySigSlaveTxDown", 22),
          ("operGrpDown", 23),
          ("withdrawnIngressVcLabel", 24))
    )

_SdpPwPortOperFlags_Type.__name__ = "Bits"
_SdpPwPortOperFlags_Object = MibTableColumn
sdpPwPortOperFlags = _SdpPwPortOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1, 8),
    _SdpPwPortOperFlags_Type()
)
sdpPwPortOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpPwPortOperFlags.setStatus("current")


class _SdpPwPortVcType_Type(SdpBindVcType):
    """Custom type sdpPwPortVcType based on SdpBindVcType"""
    defaultValue = 2


_SdpPwPortVcType_Type.__name__ = "SdpBindVcType"
_SdpPwPortVcType_Object = MibTableColumn
sdpPwPortVcType = _SdpPwPortVcType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1, 9),
    _SdpPwPortVcType_Type()
)
sdpPwPortVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortVcType.setStatus("current")


class _SdpPwPortVlanVcTag_Type(Unsigned32):
    """Custom type sdpPwPortVlanVcTag based on Unsigned32"""
    defaultValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SdpPwPortVlanVcTag_Type.__name__ = "Unsigned32"
_SdpPwPortVlanVcTag_Object = MibTableColumn
sdpPwPortVlanVcTag = _SdpPwPortVlanVcTag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1, 10),
    _SdpPwPortVlanVcTag_Type()
)
sdpPwPortVlanVcTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortVlanVcTag.setStatus("current")


class _SdpPwPortEgrShapVPort_Type(TNamedItemOrEmpty):
    """Custom type sdpPwPortEgrShapVPort based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SdpPwPortEgrShapVPort_Type.__name__ = "TNamedItemOrEmpty"
_SdpPwPortEgrShapVPort_Object = MibTableColumn
sdpPwPortEgrShapVPort = _SdpPwPortEgrShapVPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1, 11),
    _SdpPwPortEgrShapVPort_Type()
)
sdpPwPortEgrShapVPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortEgrShapVPort.setStatus("current")


class _SdpPwPortEgrShapDefIntDestId_Type(TNamedItemOrEmpty):
    """Custom type sdpPwPortEgrShapDefIntDestId based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SdpPwPortEgrShapDefIntDestId_Type.__name__ = "TNamedItemOrEmpty"
_SdpPwPortEgrShapDefIntDestId_Object = MibTableColumn
sdpPwPortEgrShapDefIntDestId = _SdpPwPortEgrShapDefIntDestId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 41, 1, 12),
    _SdpPwPortEgrShapDefIntDestId_Type()
)
sdpPwPortEgrShapDefIntDestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPwPortEgrShapDefIntDestId.setStatus("current")
_SdpBindPwPathTableLastChanged_Type = TimeStamp
_SdpBindPwPathTableLastChanged_Object = MibScalar
sdpBindPwPathTableLastChanged = _SdpBindPwPathTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 50),
    _SdpBindPwPathTableLastChanged_Type()
)
sdpBindPwPathTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwPathTableLastChanged.setStatus("current")
_SdpBindPwPathTable_Object = MibTable
sdpBindPwPathTable = _SdpBindPwPathTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 51)
)
if mibBuilder.loadTexts:
    sdpBindPwPathTable.setStatus("current")
_SdpBindPwPathEntry_Object = MibTableRow
sdpBindPwPathEntry = _SdpBindPwPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 51, 1)
)
sdpBindPwPathEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindPwPathEntry.setStatus("current")
_SdpBindPwPathRowStatus_Type = RowStatus
_SdpBindPwPathRowStatus_Object = MibTableColumn
sdpBindPwPathRowStatus = _SdpBindPwPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 51, 1, 1),
    _SdpBindPwPathRowStatus_Type()
)
sdpBindPwPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindPwPathRowStatus.setStatus("current")
_SdpBindPwPathLastChanged_Type = TimeStamp
_SdpBindPwPathLastChanged_Object = MibTableColumn
sdpBindPwPathLastChanged = _SdpBindPwPathLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 51, 1, 2),
    _SdpBindPwPathLastChanged_Type()
)
sdpBindPwPathLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwPathLastChanged.setStatus("current")


class _SdpBindPwPathAgi_Type(TmnxVPNRouteDistinguisher):
    """Custom type sdpBindPwPathAgi based on TmnxVPNRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_SdpBindPwPathAgi_Type.__name__ = "TmnxVPNRouteDistinguisher"
_SdpBindPwPathAgi_Object = MibTableColumn
sdpBindPwPathAgi = _SdpBindPwPathAgi_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 51, 1, 3),
    _SdpBindPwPathAgi_Type()
)
sdpBindPwPathAgi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindPwPathAgi.setStatus("current")


class _SdpBindPwPathSaiiGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type sdpBindPwPathSaiiGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_SdpBindPwPathSaiiGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_SdpBindPwPathSaiiGlobalId_Object = MibTableColumn
sdpBindPwPathSaiiGlobalId = _SdpBindPwPathSaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 51, 1, 4),
    _SdpBindPwPathSaiiGlobalId_Type()
)
sdpBindPwPathSaiiGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindPwPathSaiiGlobalId.setStatus("current")


class _SdpBindPwPathSaiiNodeId_Type(TmnxMplsTpNodeID):
    """Custom type sdpBindPwPathSaiiNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_SdpBindPwPathSaiiNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_SdpBindPwPathSaiiNodeId_Object = MibTableColumn
sdpBindPwPathSaiiNodeId = _SdpBindPwPathSaiiNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 51, 1, 5),
    _SdpBindPwPathSaiiNodeId_Type()
)
sdpBindPwPathSaiiNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindPwPathSaiiNodeId.setStatus("current")


class _SdpBindPwPathSaiiAcId_Type(Unsigned32):
    """Custom type sdpBindPwPathSaiiAcId based on Unsigned32"""
    defaultValue = 0


_SdpBindPwPathSaiiAcId_Type.__name__ = "Unsigned32"
_SdpBindPwPathSaiiAcId_Object = MibTableColumn
sdpBindPwPathSaiiAcId = _SdpBindPwPathSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 51, 1, 6),
    _SdpBindPwPathSaiiAcId_Type()
)
sdpBindPwPathSaiiAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindPwPathSaiiAcId.setStatus("current")


class _SdpBindPwPathTaiiGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type sdpBindPwPathTaiiGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_SdpBindPwPathTaiiGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_SdpBindPwPathTaiiGlobalId_Object = MibTableColumn
sdpBindPwPathTaiiGlobalId = _SdpBindPwPathTaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 51, 1, 7),
    _SdpBindPwPathTaiiGlobalId_Type()
)
sdpBindPwPathTaiiGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindPwPathTaiiGlobalId.setStatus("current")


class _SdpBindPwPathTaiiNodeId_Type(TmnxMplsTpNodeID):
    """Custom type sdpBindPwPathTaiiNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_SdpBindPwPathTaiiNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_SdpBindPwPathTaiiNodeId_Object = MibTableColumn
sdpBindPwPathTaiiNodeId = _SdpBindPwPathTaiiNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 51, 1, 8),
    _SdpBindPwPathTaiiNodeId_Type()
)
sdpBindPwPathTaiiNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindPwPathTaiiNodeId.setStatus("current")


class _SdpBindPwPathTaiiAcId_Type(Unsigned32):
    """Custom type sdpBindPwPathTaiiAcId based on Unsigned32"""
    defaultValue = 0


_SdpBindPwPathTaiiAcId_Type.__name__ = "Unsigned32"
_SdpBindPwPathTaiiAcId_Object = MibTableColumn
sdpBindPwPathTaiiAcId = _SdpBindPwPathTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 51, 1, 9),
    _SdpBindPwPathTaiiAcId_Type()
)
sdpBindPwPathTaiiAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindPwPathTaiiAcId.setStatus("current")
_SdpBindCtrlChanPwTableLastChgd_Type = TimeStamp
_SdpBindCtrlChanPwTableLastChgd_Object = MibScalar
sdpBindCtrlChanPwTableLastChgd = _SdpBindCtrlChanPwTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 52),
    _SdpBindCtrlChanPwTableLastChgd_Type()
)
sdpBindCtrlChanPwTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwTableLastChgd.setStatus("current")
_SdpBindCtrlChanPwTable_Object = MibTable
sdpBindCtrlChanPwTable = _SdpBindCtrlChanPwTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 53)
)
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwTable.setStatus("current")
_SdpBindCtrlChanPwEntry_Object = MibTableRow
sdpBindCtrlChanPwEntry = _SdpBindCtrlChanPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 53, 1)
)
sdpBindCtrlChanPwEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwEntry.setStatus("current")
_SdpBindCtrlChanPwLastChanged_Type = TimeStamp
_SdpBindCtrlChanPwLastChanged_Object = MibTableColumn
sdpBindCtrlChanPwLastChanged = _SdpBindCtrlChanPwLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 53, 1, 1),
    _SdpBindCtrlChanPwLastChanged_Type()
)
sdpBindCtrlChanPwLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwLastChanged.setStatus("current")


class _SdpBindCtrlChanPwStatus_Type(TmnxEnabledDisabled):
    """Custom type sdpBindCtrlChanPwStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_SdpBindCtrlChanPwStatus_Type.__name__ = "TmnxEnabledDisabled"
_SdpBindCtrlChanPwStatus_Object = MibTableColumn
sdpBindCtrlChanPwStatus = _SdpBindCtrlChanPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 53, 1, 2),
    _SdpBindCtrlChanPwStatus_Type()
)
sdpBindCtrlChanPwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwStatus.setStatus("current")


class _SdpBindCtrlChanPwRefreshTimer_Type(Unsigned32):
    """Custom type sdpBindCtrlChanPwRefreshTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 65535),
    )


_SdpBindCtrlChanPwRefreshTimer_Type.__name__ = "Unsigned32"
_SdpBindCtrlChanPwRefreshTimer_Object = MibTableColumn
sdpBindCtrlChanPwRefreshTimer = _SdpBindCtrlChanPwRefreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 53, 1, 3),
    _SdpBindCtrlChanPwRefreshTimer_Type()
)
sdpBindCtrlChanPwRefreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwRefreshTimer.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwRefreshTimer.setUnits("seconds")
_SdpBindCtrlChanPwPeerExpired_Type = TruthValue
_SdpBindCtrlChanPwPeerExpired_Object = MibTableColumn
sdpBindCtrlChanPwPeerExpired = _SdpBindCtrlChanPwPeerExpired_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 53, 1, 4),
    _SdpBindCtrlChanPwPeerExpired_Type()
)
sdpBindCtrlChanPwPeerExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwPeerExpired.setStatus("current")


class _SdpBindCtrlChanPwRequestTimer_Type(Unsigned32):
    """Custom type sdpBindCtrlChanPwRequestTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 65535),
    )


_SdpBindCtrlChanPwRequestTimer_Type.__name__ = "Unsigned32"
_SdpBindCtrlChanPwRequestTimer_Object = MibTableColumn
sdpBindCtrlChanPwRequestTimer = _SdpBindCtrlChanPwRequestTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 53, 1, 5),
    _SdpBindCtrlChanPwRequestTimer_Type()
)
sdpBindCtrlChanPwRequestTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwRequestTimer.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwRequestTimer.setUnits("seconds")


class _SdpBindCtrlChanPwRetryTimer_Type(Unsigned32):
    """Custom type sdpBindCtrlChanPwRetryTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 60),
    )


_SdpBindCtrlChanPwRetryTimer_Type.__name__ = "Unsigned32"
_SdpBindCtrlChanPwRetryTimer_Object = MibTableColumn
sdpBindCtrlChanPwRetryTimer = _SdpBindCtrlChanPwRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 53, 1, 6),
    _SdpBindCtrlChanPwRetryTimer_Type()
)
sdpBindCtrlChanPwRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwRetryTimer.setUnits("seconds")


class _SdpBindCtrlChanPwTimeoutMult_Type(Unsigned32):
    """Custom type sdpBindCtrlChanPwTimeoutMult based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 15),
    )


_SdpBindCtrlChanPwTimeoutMult_Type.__name__ = "Unsigned32"
_SdpBindCtrlChanPwTimeoutMult_Object = MibTableColumn
sdpBindCtrlChanPwTimeoutMult = _SdpBindCtrlChanPwTimeoutMult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 53, 1, 7),
    _SdpBindCtrlChanPwTimeoutMult_Type()
)
sdpBindCtrlChanPwTimeoutMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwTimeoutMult.setStatus("current")


class _SdpBindCtrlChanPwAck_Type(TruthValue):
    """Custom type sdpBindCtrlChanPwAck based on TruthValue"""
    defaultValue = 2


_SdpBindCtrlChanPwAck_Type.__name__ = "TruthValue"
_SdpBindCtrlChanPwAck_Object = MibTableColumn
sdpBindCtrlChanPwAck = _SdpBindCtrlChanPwAck_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 53, 1, 8),
    _SdpBindCtrlChanPwAck_Type()
)
sdpBindCtrlChanPwAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindCtrlChanPwAck.setStatus("current")
_SdpInfoScalar1_Type = Unsigned32
_SdpInfoScalar1_Object = MibScalar
sdpInfoScalar1 = _SdpInfoScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 101),
    _SdpInfoScalar1_Type()
)
sdpInfoScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpInfoScalar1.setStatus("current")
_SdpInfoScalar2_Type = Unsigned32
_SdpInfoScalar2_Object = MibScalar
sdpInfoScalar2 = _SdpInfoScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 4, 4, 102),
    _SdpInfoScalar2_Type()
)
sdpInfoScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpInfoScalar2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SDP-MIB",
    **{"tnServicesSdpMIBModule": tnServicesSdpMIBModule,
       "tnSdpObjs": tnSdpObjs,
       "sdpNumEntries": sdpNumEntries,
       "sdpNextFreeId": sdpNextFreeId,
       "sdpInfoTable": sdpInfoTable,
       "sdpInfoEntry": sdpInfoEntry,
       "sdpId": sdpId,
       "sdpRowStatus": sdpRowStatus,
       "sdpDelivery": sdpDelivery,
       "sdpFarEndIpAddress": sdpFarEndIpAddress,
       "sdpLspList": sdpLspList,
       "sdpDescription": sdpDescription,
       "sdpLabelSignaling": sdpLabelSignaling,
       "sdpAdminStatus": sdpAdminStatus,
       "sdpOperStatus": sdpOperStatus,
       "sdpAdminPathMtu": sdpAdminPathMtu,
       "sdpOperPathMtu": sdpOperPathMtu,
       "sdpKeepAliveAdminStatus": sdpKeepAliveAdminStatus,
       "sdpKeepAliveOperStatus": sdpKeepAliveOperStatus,
       "sdpKeepAliveHelloTime": sdpKeepAliveHelloTime,
       "sdpKeepAliveMaxDropCount": sdpKeepAliveMaxDropCount,
       "sdpKeepAliveHoldDownTime": sdpKeepAliveHoldDownTime,
       "sdpLastMgmtChange": sdpLastMgmtChange,
       "sdpKeepAliveHelloMessageLength": sdpKeepAliveHelloMessageLength,
       "sdpKeepAliveNumHelloRequestMessages": sdpKeepAliveNumHelloRequestMessages,
       "sdpKeepAliveNumHelloResponseMessages": sdpKeepAliveNumHelloResponseMessages,
       "sdpKeepAliveNumLateHelloResponseMessages": sdpKeepAliveNumLateHelloResponseMessages,
       "sdpKeepAliveHelloRequestTimeout": sdpKeepAliveHelloRequestTimeout,
       "sdpLdpEnabled": sdpLdpEnabled,
       "sdpVlanVcEtype": sdpVlanVcEtype,
       "sdpAdvertisedVllMtuOverride": sdpAdvertisedVllMtuOverride,
       "sdpOperFlags": sdpOperFlags,
       "sdpLastStatusChange": sdpLastStatusChange,
       "sdpMvplsMgmtService": sdpMvplsMgmtService,
       "sdpMvplsMgmtSdpBndId": sdpMvplsMgmtSdpBndId,
       "sdpCollectAcctStats": sdpCollectAcctStats,
       "sdpAccountingPolicyId": sdpAccountingPolicyId,
       "sdpClassFwdingEnabled": sdpClassFwdingEnabled,
       "sdpClassFwdingDefaultLsp": sdpClassFwdingDefaultLsp,
       "sdpClassFwdingMcLsp": sdpClassFwdingMcLsp,
       "sdpMetric": sdpMetric,
       "sdpAutoSdp": sdpAutoSdp,
       "sdpSnmpAllowed": sdpSnmpAllowed,
       "sdpPBBEtype": sdpPBBEtype,
       "sdpBandwidthBookingFactor": sdpBandwidthBookingFactor,
       "sdpOperBandwidth": sdpOperBandwidth,
       "sdpAvailableBandwidth": sdpAvailableBandwidth,
       "sdpMaxBookableBandwidth": sdpMaxBookableBandwidth,
       "sdpBookedBandwidth": sdpBookedBandwidth,
       "sdpCreationOrigin": sdpCreationOrigin,
       "sdpEnforceDiffServLspFc": sdpEnforceDiffServLspFc,
       "sdpMixedLspModeEnabled": sdpMixedLspModeEnabled,
       "sdpLspRevertTime": sdpLspRevertTime,
       "sdpLspRevertTimeCountDown": sdpLspRevertTimeCountDown,
       "sdpLdpLspId": sdpLdpLspId,
       "sdpLdpActive": sdpLdpActive,
       "sdpNetDomainName": sdpNetDomainName,
       "sdpEgressIfsNetDomainConsistent": sdpEgressIfsNetDomainConsistent,
       "sdpBgpTunnelEnabled": sdpBgpTunnelEnabled,
       "sdpBgpTunnelLspId": sdpBgpTunnelLspId,
       "sdpTunnelFarEndIpAddress": sdpTunnelFarEndIpAddress,
       "sdpActiveLspType": sdpActiveLspType,
       "sdpBindingPort": sdpBindingPort,
       "sdpFarEndNodeId": sdpFarEndNodeId,
       "sdpFarEndGlobalId": sdpFarEndGlobalId,
       "sdpBindTable": sdpBindTable,
       "sdpBindEntry": sdpBindEntry,
       "sdpBindId": sdpBindId,
       "sdpBindRowStatus": sdpBindRowStatus,
       "sdpBindAdminIngressLabel": sdpBindAdminIngressLabel,
       "sdpBindAdminEgressLabel": sdpBindAdminEgressLabel,
       "sdpBindOperIngressLabel": sdpBindOperIngressLabel,
       "sdpBindOperEgressLabel": sdpBindOperEgressLabel,
       "sdpBindAdminStatus": sdpBindAdminStatus,
       "sdpBindOperStatus": sdpBindOperStatus,
       "sdpBindLastMgmtChange": sdpBindLastMgmtChange,
       "sdpBindType": sdpBindType,
       "sdpBindIngressMacFilterId": sdpBindIngressMacFilterId,
       "sdpBindIngressIpFilterId": sdpBindIngressIpFilterId,
       "sdpBindEgressMacFilterId": sdpBindEgressMacFilterId,
       "sdpBindEgressIpFilterId": sdpBindEgressIpFilterId,
       "sdpBindVpnId": sdpBindVpnId,
       "sdpBindCustId": sdpBindCustId,
       "sdpBindVcType": sdpBindVcType,
       "sdpBindVlanVcTag": sdpBindVlanVcTag,
       "sdpBindSplitHorizonGrp": sdpBindSplitHorizonGrp,
       "sdpBindOperFlags": sdpBindOperFlags,
       "sdpBindLastStatusChange": sdpBindLastStatusChange,
       "sdpBindIesIfIndex": sdpBindIesIfIndex,
       "sdpBindMacPinning": sdpBindMacPinning,
       "sdpBindIngressIpv6FilterId": sdpBindIngressIpv6FilterId,
       "sdpBindEgressIpv6FilterId": sdpBindEgressIpv6FilterId,
       "sdpBindCollectAcctStats": sdpBindCollectAcctStats,
       "sdpBindAccountingPolicyId": sdpBindAccountingPolicyId,
       "sdpBindPwPeerStatusBits": sdpBindPwPeerStatusBits,
       "sdpBindPeerVccvCvBits": sdpBindPeerVccvCvBits,
       "sdpBindPeerVccvCcBits": sdpBindPeerVccvCcBits,
       "sdpBindControlWordBit": sdpBindControlWordBit,
       "sdpBindOperControlWord": sdpBindOperControlWord,
       "sdpBindEndPoint": sdpBindEndPoint,
       "sdpBindEndPointPrecedence": sdpBindEndPointPrecedence,
       "sdpBindIsICB": sdpBindIsICB,
       "sdpBindPwFaultInetAddressType": sdpBindPwFaultInetAddressType,
       "sdpBindPwFaultInetAddress": sdpBindPwFaultInetAddress,
       "sdpBindClassFwdingOperState": sdpBindClassFwdingOperState,
       "sdpBindForceVlanVcForwarding": sdpBindForceVlanVcForwarding,
       "sdpBindAdminBandwidth": sdpBindAdminBandwidth,
       "sdpBindOperBandwidth": sdpBindOperBandwidth,
       "sdpBindCreationOrigin": sdpBindCreationOrigin,
       "sdpBindDescription": sdpBindDescription,
       "sdpBindSiteName": sdpBindSiteName,
       "sdpBindHashLabel": sdpBindHashLabel,
       "sdpBindIsaAaApplicationProfile": sdpBindIsaAaApplicationProfile,
       "sdpBindStandbySigSlave": sdpBindStandbySigSlave,
       "sdpBindHashLabelSignalCapability": sdpBindHashLabelSignalCapability,
       "sdpBindIngressFlowspec": sdpBindIngressFlowspec,
       "sdpBindCpmProtPolicyId": sdpBindCpmProtPolicyId,
       "sdpBindCpmProtMonitorMac": sdpBindCpmProtMonitorMac,
       "sdpBindCpmProtEthCfmMonitorFlags": sdpBindCpmProtEthCfmMonitorFlags,
       "sdpBindTransitIpPolicyId": sdpBindTransitIpPolicyId,
       "sdpBindPwStatusSignaling": sdpBindPwStatusSignaling,
       "sdpBindOperGrp": sdpBindOperGrp,
       "sdpBindMonitorOperGrp": sdpBindMonitorOperGrp,
       "sdpBindOperHashLabel": sdpBindOperHashLabel,
       "sdpBindTransitPrefixPolicyId": sdpBindTransitPrefixPolicyId,
       "sdpBindAarpId": sdpBindAarpId,
       "sdpBindIngressQoSNetworkPlcyId": sdpBindIngressQoSNetworkPlcyId,
       "sdpBindEgressQoSNetworkPlcyId": sdpBindEgressQoSNetworkPlcyId,
       "sdpBindIngressQoSFpRedirectQGrp": sdpBindIngressQoSFpRedirectQGrp,
       "sdpBindEgressQoSPortRedirectQGrp": sdpBindEgressQoSPortRedirectQGrp,
       "sdpBindIngressQoSInstanceId": sdpBindIngressQoSInstanceId,
       "sdpBindEgressQoSInstanceId": sdpBindEgressQoSInstanceId,
       "sdpBindAarpServRefType": sdpBindAarpServRefType,
       "sdpBindPwLocalStatusBits": sdpBindPwLocalStatusBits,
       "sdpBindBlockOnPeerFault": sdpBindBlockOnPeerFault,
       "sdpBindStatsCounterEnable": sdpBindStatsCounterEnable,
       "sdpBindBaseStatsTable": sdpBindBaseStatsTable,
       "sdpBindBaseStatsEntry": sdpBindBaseStatsEntry,
       "sdpBindBaseStatsIngressForwardedPackets": sdpBindBaseStatsIngressForwardedPackets,
       "sdpBindBaseStatsIngressDroppedPackets": sdpBindBaseStatsIngressDroppedPackets,
       "sdpBindBaseStatsEgressForwardedPackets": sdpBindBaseStatsEgressForwardedPackets,
       "sdpBindBaseStatsEgressForwardedOctets": sdpBindBaseStatsEgressForwardedOctets,
       "sdpBindBaseStatsCustId": sdpBindBaseStatsCustId,
       "sdpBindBaseStatsIngFwdOctets": sdpBindBaseStatsIngFwdOctets,
       "sdpBindBaseStatsIngDropOctets": sdpBindBaseStatsIngDropOctets,
       "sdpBindTlsTable": sdpBindTlsTable,
       "sdpBindTlsEntry": sdpBindTlsEntry,
       "sdpBindTlsMacAddressLimit": sdpBindTlsMacAddressLimit,
       "sdpBindTlsNumMacAddresses": sdpBindTlsNumMacAddresses,
       "sdpBindTlsNumStaticMacAddresses": sdpBindTlsNumStaticMacAddresses,
       "sdpBindTlsMacLearning": sdpBindTlsMacLearning,
       "sdpBindTlsMacAgeing": sdpBindTlsMacAgeing,
       "sdpBindTlsLimitMacMove": sdpBindTlsLimitMacMove,
       "sdpBindTlsDiscardUnknownSource": sdpBindTlsDiscardUnknownSource,
       "sdpBindTlsL2ptTermination": sdpBindTlsL2ptTermination,
       "sdpBindTlsIgnoreStandbySig": sdpBindTlsIgnoreStandbySig,
       "sdpBindTlsBlockOnMeshFail": sdpBindTlsBlockOnMeshFail,
       "sdpBindTlsFdbTableSizeProfId": sdpBindTlsFdbTableSizeProfId,
       "sdpFCMappingTable": sdpFCMappingTable,
       "sdpFCMappingEntry": sdpFCMappingEntry,
       "sdpFCMappingFCName": sdpFCMappingFCName,
       "sdpFCMappingRowStatus": sdpFCMappingRowStatus,
       "sdpFCMappingLspId": sdpFCMappingLspId,
       "pwTemplateTableLastChanged": pwTemplateTableLastChanged,
       "pwTemplateTable": pwTemplateTable,
       "pwTemplateEntry": pwTemplateEntry,
       "pwTemplateId": pwTemplateId,
       "pwTemplateLastChanged": pwTemplateLastChanged,
       "pwTemplateIgmpFastLeave": pwTemplateIgmpFastLeave,
       "pwTemplateIgmpLastMembIntvl": pwTemplateIgmpLastMembIntvl,
       "pwTemplateIgmpMaxNbrGrps": pwTemplateIgmpMaxNbrGrps,
       "pwTemplateIgmpGenQueryIntvl": pwTemplateIgmpGenQueryIntvl,
       "pwTemplateIgmpQueryRespIntvl": pwTemplateIgmpQueryRespIntvl,
       "pwTemplateIgmpRobustCount": pwTemplateIgmpRobustCount,
       "pwTemplateIgmpSendQueries": pwTemplateIgmpSendQueries,
       "pwTemplateIgmpVersion": pwTemplateIgmpVersion,
       "pwTemplateIgmpSnpgGrpSrcTblLC": pwTemplateIgmpSnpgGrpSrcTblLC,
       "pwTemplateIgmpSnpgGrpSrcTable": pwTemplateIgmpSnpgGrpSrcTable,
       "pwTemplateIgmpSnpgGrpSrcEntry": pwTemplateIgmpSnpgGrpSrcEntry,
       "pwTemplateIgmpSnpgGrpAddrType": pwTemplateIgmpSnpgGrpAddrType,
       "pwTemplateIgmpSnpgGrpAddr": pwTemplateIgmpSnpgGrpAddr,
       "pwTemplateIgmpSnpgSrcAddrType": pwTemplateIgmpSnpgSrcAddrType,
       "pwTemplateIgmpSnpgSrcAddr": pwTemplateIgmpSnpgSrcAddr,
       "pwTemplateIgmpSnpgRowStatus": pwTemplateIgmpSnpgRowStatus,
       "pwTemplateIgmpSnpgLastChngd": pwTemplateIgmpSnpgLastChngd,
       "sdpPwPortTblLastChanged": sdpPwPortTblLastChanged,
       "sdpPwPortTable": sdpPwPortTable,
       "sdpPwPortEntry": sdpPwPortEntry,
       "sdpPwPortId": sdpPwPortId,
       "sdpPwPortRowStatus": sdpPwPortRowStatus,
       "sdpPwPortLastChgd": sdpPwPortLastChgd,
       "sdpPwPortAdminStatus": sdpPwPortAdminStatus,
       "sdpPwPortVcId": sdpPwPortVcId,
       "sdpPwPortEncapType": sdpPwPortEncapType,
       "sdpPwPortOperStatus": sdpPwPortOperStatus,
       "sdpPwPortOperFlags": sdpPwPortOperFlags,
       "sdpPwPortVcType": sdpPwPortVcType,
       "sdpPwPortVlanVcTag": sdpPwPortVlanVcTag,
       "sdpPwPortEgrShapVPort": sdpPwPortEgrShapVPort,
       "sdpPwPortEgrShapDefIntDestId": sdpPwPortEgrShapDefIntDestId,
       "sdpBindPwPathTableLastChanged": sdpBindPwPathTableLastChanged,
       "sdpBindPwPathTable": sdpBindPwPathTable,
       "sdpBindPwPathEntry": sdpBindPwPathEntry,
       "sdpBindPwPathRowStatus": sdpBindPwPathRowStatus,
       "sdpBindPwPathLastChanged": sdpBindPwPathLastChanged,
       "sdpBindPwPathAgi": sdpBindPwPathAgi,
       "sdpBindPwPathSaiiGlobalId": sdpBindPwPathSaiiGlobalId,
       "sdpBindPwPathSaiiNodeId": sdpBindPwPathSaiiNodeId,
       "sdpBindPwPathSaiiAcId": sdpBindPwPathSaiiAcId,
       "sdpBindPwPathTaiiGlobalId": sdpBindPwPathTaiiGlobalId,
       "sdpBindPwPathTaiiNodeId": sdpBindPwPathTaiiNodeId,
       "sdpBindPwPathTaiiAcId": sdpBindPwPathTaiiAcId,
       "sdpBindCtrlChanPwTableLastChgd": sdpBindCtrlChanPwTableLastChgd,
       "sdpBindCtrlChanPwTable": sdpBindCtrlChanPwTable,
       "sdpBindCtrlChanPwEntry": sdpBindCtrlChanPwEntry,
       "sdpBindCtrlChanPwLastChanged": sdpBindCtrlChanPwLastChanged,
       "sdpBindCtrlChanPwStatus": sdpBindCtrlChanPwStatus,
       "sdpBindCtrlChanPwRefreshTimer": sdpBindCtrlChanPwRefreshTimer,
       "sdpBindCtrlChanPwPeerExpired": sdpBindCtrlChanPwPeerExpired,
       "sdpBindCtrlChanPwRequestTimer": sdpBindCtrlChanPwRequestTimer,
       "sdpBindCtrlChanPwRetryTimer": sdpBindCtrlChanPwRetryTimer,
       "sdpBindCtrlChanPwTimeoutMult": sdpBindCtrlChanPwTimeoutMult,
       "sdpBindCtrlChanPwAck": sdpBindCtrlChanPwAck,
       "sdpInfoScalar1": sdpInfoScalar1,
       "sdpInfoScalar2": sdpInfoScalar2}
)
