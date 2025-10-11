# SNMP MIB module (TIMETRA-MIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-MIRROR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:57:39 2025
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

(TEntryId,
 TEntryIdOrZero,
 TFilterID,
 TFilterType,
 TLimitedEntryId) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TEntryId",
    "TEntryIdOrZero",
    "TFilterID",
    "TFilterType",
    "TLimitedEntryId")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(SdpId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "SdpId")

(SdpBindId,
 ServiceAdminStatus,
 ServiceOperStatus,
 TDirection,
 TFCSet,
 TItemDescription,
 TLNamedItem,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyID,
 TQosQGrpInstanceIDorZero,
 TSubHostId,
 TmnxAdminState,
 TmnxCreateOrigin,
 TmnxEncapVal,
 TmnxIsaBbGrpId,
 TmnxLongDisplayString,
 TmnxPortID,
 TmnxPppoeSessionId,
 TmnxServId,
 TmnxSubIdentString,
 TmnxVRtrID,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "SdpBindId",
    "ServiceAdminStatus",
    "ServiceOperStatus",
    "TDirection",
    "TFCSet",
    "TItemDescription",
    "TLNamedItem",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyID",
    "TQosQGrpInstanceIDorZero",
    "TSubHostId",
    "TmnxAdminState",
    "TmnxCreateOrigin",
    "TmnxEncapVal",
    "TmnxIsaBbGrpId",
    "TmnxLongDisplayString",
    "TmnxPortID",
    "TmnxPppoeSessionId",
    "TmnxServId",
    "TmnxSubIdentString",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraMirrorMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 18)
)
if mibBuilder.loadTexts:
    timetraMirrorMIBModule.setRevisions(
        ("2017-03-15 00:00",
         "2016-02-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2011-02-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2002-03-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TMplsLabel(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )



class TEtherType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )



class TSessionId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxMirrorEncapType(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("ether", 1),
          ("frameRelay", 2),
          ("ppp", 3),
          ("atmSdu", 4),
          ("satopE1", 5),
          ("satopT1", 6),
          ("satopE3", 7),
          ("satopT3", 8),
          ("cesopsn", 9),
          ("cesopsnCas", 10),
          ("ipOnly", 11))
    )



class TmnxMirrorDestinationHeaderType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipUdpShim", 1),
          ("ipGre", 2),
          ("ipUdpShimSampled", 4))
    )



class TmnxMirrorGatewayRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )



class TmnxInterceptionIdentifier(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1073741823),
    )



class TmnxMirrorLiXIfCorrelationIdOrg(TextualConvention, Integer32):
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
        *(("host", 1),
          ("queue", 2),
          ("session", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TMirrorConformance_ObjectIdentity = ObjectIdentity
tMirrorConformance = _TMirrorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18)
)
_TMirrorCompliances_ObjectIdentity = ObjectIdentity
tMirrorCompliances = _TMirrorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1)
)
_TMirrorGroups_ObjectIdentity = ObjectIdentity
tMirrorGroups = _TMirrorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2)
)
_TMirrorObjects_ObjectIdentity = ObjectIdentity
tMirrorObjects = _TMirrorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18)
)
_TMirrorDestinationObjects_ObjectIdentity = ObjectIdentity
tMirrorDestinationObjects = _TMirrorDestinationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1)
)
_TMirrorDestinationTable_Object = MibTable
tMirrorDestinationTable = _TMirrorDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1)
)
if mibBuilder.loadTexts:
    tMirrorDestinationTable.setStatus("current")
_TMirrorDestinationEntry_Object = MibTableRow
tMirrorDestinationEntry = _TMirrorDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1)
)
tMirrorDestinationEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorDestinationIndex"),
)
if mibBuilder.loadTexts:
    tMirrorDestinationEntry.setStatus("current")
_TMirrorDestinationIndex_Type = TmnxServId
_TMirrorDestinationIndex_Object = MibTableColumn
tMirrorDestinationIndex = _TMirrorDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 1),
    _TMirrorDestinationIndex_Type()
)
tMirrorDestinationIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorDestinationIndex.setStatus("current")
_TMirrorDestinationRowStatus_Type = RowStatus
_TMirrorDestinationRowStatus_Object = MibTableColumn
tMirrorDestinationRowStatus = _TMirrorDestinationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 2),
    _TMirrorDestinationRowStatus_Type()
)
tMirrorDestinationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationRowStatus.setStatus("current")


class _TMirrorDestinationDescription_Type(TItemDescription):
    """Custom type tMirrorDestinationDescription based on TItemDescription"""
    defaultHexValue = ""


_TMirrorDestinationDescription_Type.__name__ = "TItemDescription"
_TMirrorDestinationDescription_Object = MibTableColumn
tMirrorDestinationDescription = _TMirrorDestinationDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 3),
    _TMirrorDestinationDescription_Type()
)
tMirrorDestinationDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationDescription.setStatus("current")


class _TMirrorDestinationFC_Type(TNamedItem):
    """Custom type tMirrorDestinationFC based on TNamedItem"""
    defaultHexValue = "be"


_TMirrorDestinationFC_Type.__name__ = "TNamedItem"
_TMirrorDestinationFC_Object = MibTableColumn
tMirrorDestinationFC = _TMirrorDestinationFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 4),
    _TMirrorDestinationFC_Type()
)
tMirrorDestinationFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationFC.setStatus("current")


class _TMirrorDestinationRemoteSource_Type(TruthValue):
    """Custom type tMirrorDestinationRemoteSource based on TruthValue"""
    defaultValue = 2


_TMirrorDestinationRemoteSource_Type.__name__ = "TruthValue"
_TMirrorDestinationRemoteSource_Object = MibTableColumn
tMirrorDestinationRemoteSource = _TMirrorDestinationRemoteSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 5),
    _TMirrorDestinationRemoteSource_Type()
)
tMirrorDestinationRemoteSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationRemoteSource.setStatus("current")


class _TMirrorDestinationSapPortId_Type(TmnxPortID):
    """Custom type tMirrorDestinationSapPortId based on TmnxPortID"""
    defaultValue = 503316480


_TMirrorDestinationSapPortId_Type.__name__ = "TmnxPortID"
_TMirrorDestinationSapPortId_Object = MibTableColumn
tMirrorDestinationSapPortId = _TMirrorDestinationSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 6),
    _TMirrorDestinationSapPortId_Type()
)
tMirrorDestinationSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationSapPortId.setStatus("current")


class _TMirrorDestinationSapEncapValue_Type(TmnxEncapVal):
    """Custom type tMirrorDestinationSapEncapValue based on TmnxEncapVal"""
    defaultValue = 0


_TMirrorDestinationSapEncapValue_Type.__name__ = "TmnxEncapVal"
_TMirrorDestinationSapEncapValue_Object = MibTableColumn
tMirrorDestinationSapEncapValue = _TMirrorDestinationSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 7),
    _TMirrorDestinationSapEncapValue_Type()
)
tMirrorDestinationSapEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationSapEncapValue.setStatus("current")


class _TMirrorDestinationSdpNumber_Type(SdpId):
    """Custom type tMirrorDestinationSdpNumber based on SdpId"""
    defaultValue = 0


_TMirrorDestinationSdpNumber_Type.__name__ = "SdpId"
_TMirrorDestinationSdpNumber_Object = MibTableColumn
tMirrorDestinationSdpNumber = _TMirrorDestinationSdpNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 8),
    _TMirrorDestinationSdpNumber_Type()
)
tMirrorDestinationSdpNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationSdpNumber.setStatus("obsolete")


class _TMirrorDestinationSdpDestEncap_Type(Integer32):
    """Custom type tMirrorDestinationSdpDestEncap based on Integer32"""
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
        *(("none", 1),
          ("pos", 2),
          ("ethernet", 3))
    )


_TMirrorDestinationSdpDestEncap_Type.__name__ = "Integer32"
_TMirrorDestinationSdpDestEncap_Object = MibTableColumn
tMirrorDestinationSdpDestEncap = _TMirrorDestinationSdpDestEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 9),
    _TMirrorDestinationSdpDestEncap_Type()
)
tMirrorDestinationSdpDestEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationSdpDestEncap.setStatus("obsolete")


class _TMirrorDestinationAdminStatus_Type(ServiceAdminStatus):
    """Custom type tMirrorDestinationAdminStatus based on ServiceAdminStatus"""
    defaultValue = 2


_TMirrorDestinationAdminStatus_Type.__name__ = "ServiceAdminStatus"
_TMirrorDestinationAdminStatus_Object = MibTableColumn
tMirrorDestinationAdminStatus = _TMirrorDestinationAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 10),
    _TMirrorDestinationAdminStatus_Type()
)
tMirrorDestinationAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationAdminStatus.setStatus("current")
_TMirrorDestinationOperStatus_Type = ServiceOperStatus
_TMirrorDestinationOperStatus_Object = MibTableColumn
tMirrorDestinationOperStatus = _TMirrorDestinationOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 11),
    _TMirrorDestinationOperStatus_Type()
)
tMirrorDestinationOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestinationOperStatus.setStatus("current")


class _TMirrorDestinationTranslateDisable_Type(TruthValue):
    """Custom type tMirrorDestinationTranslateDisable based on TruthValue"""
    defaultValue = 2


_TMirrorDestinationTranslateDisable_Type.__name__ = "TruthValue"
_TMirrorDestinationTranslateDisable_Object = MibTableColumn
tMirrorDestinationTranslateDisable = _TMirrorDestinationTranslateDisable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 12),
    _TMirrorDestinationTranslateDisable_Type()
)
tMirrorDestinationTranslateDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationTranslateDisable.setStatus("obsolete")


class _TMirrorDestinationSliceSize_Type(Unsigned32):
    """Custom type tMirrorDestinationSliceSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 9216),
    )


_TMirrorDestinationSliceSize_Type.__name__ = "Unsigned32"
_TMirrorDestinationSliceSize_Object = MibTableColumn
tMirrorDestinationSliceSize = _TMirrorDestinationSliceSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 13),
    _TMirrorDestinationSliceSize_Type()
)
tMirrorDestinationSliceSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationSliceSize.setStatus("current")


class _TMirrorDestinationPppoeDestMacAddr_Type(MacAddress):
    """Custom type tMirrorDestinationPppoeDestMacAddr based on MacAddress"""
    defaultHexValue = "0003f8000000"


_TMirrorDestinationPppoeDestMacAddr_Type.__name__ = "MacAddress"
_TMirrorDestinationPppoeDestMacAddr_Object = MibTableColumn
tMirrorDestinationPppoeDestMacAddr = _TMirrorDestinationPppoeDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 14),
    _TMirrorDestinationPppoeDestMacAddr_Type()
)
tMirrorDestinationPppoeDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationPppoeDestMacAddr.setStatus("obsolete")


class _TMirrorDestinationPppoeSrcMacAddr_Type(MacAddress):
    """Custom type tMirrorDestinationPppoeSrcMacAddr based on MacAddress"""
    defaultHexValue = "0003f8000001"


_TMirrorDestinationPppoeSrcMacAddr_Type.__name__ = "MacAddress"
_TMirrorDestinationPppoeSrcMacAddr_Object = MibTableColumn
tMirrorDestinationPppoeSrcMacAddr = _TMirrorDestinationPppoeSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 15),
    _TMirrorDestinationPppoeSrcMacAddr_Type()
)
tMirrorDestinationPppoeSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationPppoeSrcMacAddr.setStatus("obsolete")


class _TMirrorDestinationPppoeEtype_Type(TEtherType):
    """Custom type tMirrorDestinationPppoeEtype based on TEtherType"""
    defaultValue = 34916


_TMirrorDestinationPppoeEtype_Type.__name__ = "TEtherType"
_TMirrorDestinationPppoeEtype_Object = MibTableColumn
tMirrorDestinationPppoeEtype = _TMirrorDestinationPppoeEtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 16),
    _TMirrorDestinationPppoeEtype_Type()
)
tMirrorDestinationPppoeEtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationPppoeEtype.setStatus("obsolete")


class _TMirrorDestinationPppoeSessionId_Type(TSessionId):
    """Custom type tMirrorDestinationPppoeSessionId based on TSessionId"""
    defaultValue = 1


_TMirrorDestinationPppoeSessionId_Type.__name__ = "TSessionId"
_TMirrorDestinationPppoeSessionId_Object = MibTableColumn
tMirrorDestinationPppoeSessionId = _TMirrorDestinationPppoeSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 17),
    _TMirrorDestinationPppoeSessionId_Type()
)
tMirrorDestinationPppoeSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationPppoeSessionId.setStatus("obsolete")


class _TMirrorDestinationSdpEgrSvcLabel_Type(TMplsLabel):
    """Custom type tMirrorDestinationSdpEgrSvcLabel based on TMplsLabel"""
    defaultValue = 0

    subtypeSpec = TMplsLabel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_TMirrorDestinationSdpEgrSvcLabel_Type.__name__ = "TMplsLabel"
_TMirrorDestinationSdpEgrSvcLabel_Object = MibTableColumn
tMirrorDestinationSdpEgrSvcLabel = _TMirrorDestinationSdpEgrSvcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 18),
    _TMirrorDestinationSdpEgrSvcLabel_Type()
)
tMirrorDestinationSdpEgrSvcLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationSdpEgrSvcLabel.setStatus("obsolete")


class _TMirrorDestinationSapEgressQosPolicyId_Type(TPolicyID):
    """Custom type tMirrorDestinationSapEgressQosPolicyId based on TPolicyID"""
    defaultValue = 1


_TMirrorDestinationSapEgressQosPolicyId_Type.__name__ = "TPolicyID"
_TMirrorDestinationSapEgressQosPolicyId_Object = MibTableColumn
tMirrorDestinationSapEgressQosPolicyId = _TMirrorDestinationSapEgressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 19),
    _TMirrorDestinationSapEgressQosPolicyId_Type()
)
tMirrorDestinationSapEgressQosPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationSapEgressQosPolicyId.setStatus("current")


class _TMirrorDestinationEncapsulation_Type(TmnxMirrorEncapType):
    """Custom type tMirrorDestinationEncapsulation based on TmnxMirrorEncapType"""
    defaultValue = 1


_TMirrorDestinationEncapsulation_Type.__name__ = "TmnxMirrorEncapType"
_TMirrorDestinationEncapsulation_Object = MibTableColumn
tMirrorDestinationEncapsulation = _TMirrorDestinationEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 20),
    _TMirrorDestinationEncapsulation_Type()
)
tMirrorDestinationEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationEncapsulation.setStatus("current")
_TMirrorDestinationSdpOperEgrSvcLabel_Type = TMplsLabel
_TMirrorDestinationSdpOperEgrSvcLabel_Object = MibTableColumn
tMirrorDestinationSdpOperEgrSvcLabel = _TMirrorDestinationSdpOperEgrSvcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 21),
    _TMirrorDestinationSdpOperEgrSvcLabel_Type()
)
tMirrorDestinationSdpOperEgrSvcLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestinationSdpOperEgrSvcLabel.setStatus("obsolete")


class _TMirrorDestinationEnablePortId_Type(TruthValue):
    """Custom type tMirrorDestinationEnablePortId based on TruthValue"""
    defaultValue = 2


_TMirrorDestinationEnablePortId_Type.__name__ = "TruthValue"
_TMirrorDestinationEnablePortId_Object = MibTableColumn
tMirrorDestinationEnablePortId = _TMirrorDestinationEnablePortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 22),
    _TMirrorDestinationEnablePortId_Type()
)
tMirrorDestinationEnablePortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationEnablePortId.setStatus("current")


class _TMirrorDestSapEgrIpMirrorSA_Type(MacAddress):
    """Custom type tMirrorDestSapEgrIpMirrorSA based on MacAddress"""
    defaultHexValue = "000000000000"


_TMirrorDestSapEgrIpMirrorSA_Type.__name__ = "MacAddress"
_TMirrorDestSapEgrIpMirrorSA_Object = MibTableColumn
tMirrorDestSapEgrIpMirrorSA = _TMirrorDestSapEgrIpMirrorSA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 23),
    _TMirrorDestSapEgrIpMirrorSA_Type()
)
tMirrorDestSapEgrIpMirrorSA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestSapEgrIpMirrorSA.setStatus("current")


class _TMirrorDestSapEgrIpMirrorDA_Type(MacAddress):
    """Custom type tMirrorDestSapEgrIpMirrorDA based on MacAddress"""
    defaultHexValue = "000000000000"


_TMirrorDestSapEgrIpMirrorDA_Type.__name__ = "MacAddress"
_TMirrorDestSapEgrIpMirrorDA_Object = MibTableColumn
tMirrorDestSapEgrIpMirrorDA = _TMirrorDestSapEgrIpMirrorDA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 24),
    _TMirrorDestSapEgrIpMirrorDA_Type()
)
tMirrorDestSapEgrIpMirrorDA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestSapEgrIpMirrorDA.setStatus("current")
_TMirrorDestLastChanged_Type = TimeStamp
_TMirrorDestLastChanged_Object = MibTableColumn
tMirrorDestLastChanged = _TMirrorDestLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 25),
    _TMirrorDestLastChanged_Type()
)
tMirrorDestLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestLastChanged.setStatus("current")


class _TMirrorDestSapEgrPortQGrp_Type(TNamedItemOrEmpty):
    """Custom type tMirrorDestSapEgrPortQGrp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TMirrorDestSapEgrPortQGrp_Type.__name__ = "TNamedItemOrEmpty"
_TMirrorDestSapEgrPortQGrp_Object = MibTableColumn
tMirrorDestSapEgrPortQGrp = _TMirrorDestSapEgrPortQGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 26),
    _TMirrorDestSapEgrPortQGrp_Type()
)
tMirrorDestSapEgrPortQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestSapEgrPortQGrp.setStatus("current")


class _TMirrorDestSapEgrPortQGrpInstId_Type(TQosQGrpInstanceIDorZero):
    """Custom type tMirrorDestSapEgrPortQGrpInstId based on TQosQGrpInstanceIDorZero"""
    defaultValue = 0


_TMirrorDestSapEgrPortQGrpInstId_Type.__name__ = "TQosQGrpInstanceIDorZero"
_TMirrorDestSapEgrPortQGrpInstId_Object = MibTableColumn
tMirrorDestSapEgrPortQGrpInstId = _TMirrorDestSapEgrPortQGrpInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 27),
    _TMirrorDestSapEgrPortQGrpInstId_Type()
)
tMirrorDestSapEgrPortQGrpInstId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestSapEgrPortQGrpInstId.setStatus("current")
_TMirrorDestCreationOrigin_Type = TmnxCreateOrigin
_TMirrorDestCreationOrigin_Object = MibTableColumn
tMirrorDestCreationOrigin = _TMirrorDestCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 28),
    _TMirrorDestCreationOrigin_Type()
)
tMirrorDestCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestCreationOrigin.setStatus("current")


class _TMirrorDestinationName_Type(TLNamedItemOrEmpty):
    """Custom type tMirrorDestinationName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TMirrorDestinationName_Type.__name__ = "TLNamedItemOrEmpty"
_TMirrorDestinationName_Object = MibTableColumn
tMirrorDestinationName = _TMirrorDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 29),
    _TMirrorDestinationName_Type()
)
tMirrorDestinationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationName.setStatus("current")
_TMirrorDestPcapSessionName_Type = TNamedItemOrEmpty
_TMirrorDestPcapSessionName_Object = MibTableColumn
tMirrorDestPcapSessionName = _TMirrorDestPcapSessionName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 30),
    _TMirrorDestPcapSessionName_Type()
)
tMirrorDestPcapSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestPcapSessionName.setStatus("current")


class _TMirrorDestSamplingRate_Type(Unsigned32):
    """Custom type tMirrorDestSamplingRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(256, 10000),
    )


_TMirrorDestSamplingRate_Type.__name__ = "Unsigned32"
_TMirrorDestSamplingRate_Object = MibTableColumn
tMirrorDestSamplingRate = _TMirrorDestSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 1, 1, 31),
    _TMirrorDestSamplingRate_Type()
)
tMirrorDestSamplingRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestSamplingRate.setStatus("current")
_TMirrorDestinationRemoteSourceTable_Object = MibTable
tMirrorDestinationRemoteSourceTable = _TMirrorDestinationRemoteSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 2)
)
if mibBuilder.loadTexts:
    tMirrorDestinationRemoteSourceTable.setStatus("current")
_TMirrorDestinationRemoteSourceEntry_Object = MibTableRow
tMirrorDestinationRemoteSourceEntry = _TMirrorDestinationRemoteSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 2, 1)
)
tMirrorDestinationRemoteSourceEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorDestinationIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorDestinationRemoteSourceAddr"),
)
if mibBuilder.loadTexts:
    tMirrorDestinationRemoteSourceEntry.setStatus("current")
_TMirrorDestinationRemoteSourceAddr_Type = IpAddress
_TMirrorDestinationRemoteSourceAddr_Object = MibTableColumn
tMirrorDestinationRemoteSourceAddr = _TMirrorDestinationRemoteSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 2, 1, 1),
    _TMirrorDestinationRemoteSourceAddr_Type()
)
tMirrorDestinationRemoteSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestinationRemoteSourceAddr.setStatus("current")


class _TMirrorDestinationRemoteSourceLabelSignaling_Type(Integer32):
    """Custom type tMirrorDestinationRemoteSourceLabelSignaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tldp", 2))
    )


_TMirrorDestinationRemoteSourceLabelSignaling_Type.__name__ = "Integer32"
_TMirrorDestinationRemoteSourceLabelSignaling_Object = MibTableColumn
tMirrorDestinationRemoteSourceLabelSignaling = _TMirrorDestinationRemoteSourceLabelSignaling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 2, 1, 2),
    _TMirrorDestinationRemoteSourceLabelSignaling_Type()
)
tMirrorDestinationRemoteSourceLabelSignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationRemoteSourceLabelSignaling.setStatus("current")


class _TMirrorDestinationRemoteSourceIngSvcLabel_Type(TMplsLabel):
    """Custom type tMirrorDestinationRemoteSourceIngSvcLabel based on TMplsLabel"""
    defaultValue = 0

    subtypeSpec = TMplsLabel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 1048575),
    )


_TMirrorDestinationRemoteSourceIngSvcLabel_Type.__name__ = "TMplsLabel"
_TMirrorDestinationRemoteSourceIngSvcLabel_Object = MibTableColumn
tMirrorDestinationRemoteSourceIngSvcLabel = _TMirrorDestinationRemoteSourceIngSvcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 2, 1, 3),
    _TMirrorDestinationRemoteSourceIngSvcLabel_Type()
)
tMirrorDestinationRemoteSourceIngSvcLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationRemoteSourceIngSvcLabel.setStatus("current")
_TMirrorDestinationRemoteSourceRowStatus_Type = RowStatus
_TMirrorDestinationRemoteSourceRowStatus_Object = MibTableColumn
tMirrorDestinationRemoteSourceRowStatus = _TMirrorDestinationRemoteSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 2, 1, 4),
    _TMirrorDestinationRemoteSourceRowStatus_Type()
)
tMirrorDestinationRemoteSourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestinationRemoteSourceRowStatus.setStatus("current")
_TMirrorDestinationRemoteSourceOperIngSvcLabel_Type = TMplsLabel
_TMirrorDestinationRemoteSourceOperIngSvcLabel_Object = MibTableColumn
tMirrorDestinationRemoteSourceOperIngSvcLabel = _TMirrorDestinationRemoteSourceOperIngSvcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 2, 1, 5),
    _TMirrorDestinationRemoteSourceOperIngSvcLabel_Type()
)
tMirrorDestinationRemoteSourceOperIngSvcLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestinationRemoteSourceOperIngSvcLabel.setStatus("current")
_TMirrorDestRemoteSrcLastChgd_Type = TimeStamp
_TMirrorDestRemoteSrcLastChgd_Object = MibTableColumn
tMirrorDestRemoteSrcLastChgd = _TMirrorDestRemoteSrcLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 2, 1, 6),
    _TMirrorDestRemoteSrcLastChgd_Type()
)
tMirrorDestRemoteSrcLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestRemoteSrcLastChgd.setStatus("current")


class _TMirrorDestRemoteSrcIsICB_Type(TruthValue):
    """Custom type tMirrorDestRemoteSrcIsICB based on TruthValue"""
    defaultValue = 2


_TMirrorDestRemoteSrcIsICB_Type.__name__ = "TruthValue"
_TMirrorDestRemoteSrcIsICB_Object = MibTableColumn
tMirrorDestRemoteSrcIsICB = _TMirrorDestRemoteSrcIsICB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 2, 1, 7),
    _TMirrorDestRemoteSrcIsICB_Type()
)
tMirrorDestRemoteSrcIsICB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestRemoteSrcIsICB.setStatus("current")


class _TMirrorDestRemoteSrcVcId_Type(Unsigned32):
    """Custom type tMirrorDestRemoteSrcVcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TMirrorDestRemoteSrcVcId_Type.__name__ = "Unsigned32"
_TMirrorDestRemoteSrcVcId_Object = MibTableColumn
tMirrorDestRemoteSrcVcId = _TMirrorDestRemoteSrcVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 2, 1, 8),
    _TMirrorDestRemoteSrcVcId_Type()
)
tMirrorDestRemoteSrcVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestRemoteSrcVcId.setStatus("current")
_TMirrorDestTableLastChnged_Type = TimeStamp
_TMirrorDestTableLastChnged_Object = MibScalar
tMirrorDestTableLastChnged = _TMirrorDestTableLastChnged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 3),
    _TMirrorDestTableLastChnged_Type()
)
tMirrorDestTableLastChnged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestTableLastChnged.setStatus("current")
_TMirrorDestRemSrcTblLastChgd_Type = TimeStamp
_TMirrorDestRemSrcTblLastChgd_Object = MibScalar
tMirrorDestRemSrcTblLastChgd = _TMirrorDestRemSrcTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 4),
    _TMirrorDestRemSrcTblLastChgd_Type()
)
tMirrorDestRemSrcTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestRemSrcTblLastChgd.setStatus("current")
_TMirrorDestL3EncTableLastCh_Type = TimeStamp
_TMirrorDestL3EncTableLastCh_Object = MibScalar
tMirrorDestL3EncTableLastCh = _TMirrorDestL3EncTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 5),
    _TMirrorDestL3EncTableLastCh_Type()
)
tMirrorDestL3EncTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestL3EncTableLastCh.setStatus("current")
_TMirrorDestL3EncTable_Object = MibTable
tMirrorDestL3EncTable = _TMirrorDestL3EncTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 6)
)
if mibBuilder.loadTexts:
    tMirrorDestL3EncTable.setStatus("current")
_TMirrorDestL3EncEntry_Object = MibTableRow
tMirrorDestL3EncEntry = _TMirrorDestL3EncEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 6, 1)
)
tMirrorDestL3EncEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorDestinationIndex"),
)
if mibBuilder.loadTexts:
    tMirrorDestL3EncEntry.setStatus("current")
_TMirrorDestL3EncRowStatus_Type = RowStatus
_TMirrorDestL3EncRowStatus_Object = MibTableColumn
tMirrorDestL3EncRowStatus = _TMirrorDestL3EncRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 6, 1, 1),
    _TMirrorDestL3EncRowStatus_Type()
)
tMirrorDestL3EncRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestL3EncRowStatus.setStatus("current")
_TMirrorDestL3EncLastCh_Type = TimeStamp
_TMirrorDestL3EncLastCh_Object = MibTableColumn
tMirrorDestL3EncLastCh = _TMirrorDestL3EncLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 6, 1, 2),
    _TMirrorDestL3EncLastCh_Type()
)
tMirrorDestL3EncLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestL3EncLastCh.setStatus("current")
_TMirrorDestL3EncHeaderType_Type = TmnxMirrorDestinationHeaderType
_TMirrorDestL3EncHeaderType_Object = MibTableColumn
tMirrorDestL3EncHeaderType = _TMirrorDestL3EncHeaderType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 6, 1, 3),
    _TMirrorDestL3EncHeaderType_Type()
)
tMirrorDestL3EncHeaderType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestL3EncHeaderType.setStatus("current")


class _TMirrorDestL3EncRouter_Type(TmnxVRtrID):
    """Custom type tMirrorDestL3EncRouter based on TmnxVRtrID"""
    defaultValue = 1


_TMirrorDestL3EncRouter_Type.__name__ = "TmnxVRtrID"
_TMirrorDestL3EncRouter_Object = MibTableColumn
tMirrorDestL3EncRouter = _TMirrorDestL3EncRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 6, 1, 4),
    _TMirrorDestL3EncRouter_Type()
)
tMirrorDestL3EncRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestL3EncRouter.setStatus("current")


class _TMirrorDestL3EncUseDirectionBit_Type(TruthValue):
    """Custom type tMirrorDestL3EncUseDirectionBit based on TruthValue"""
    defaultValue = 2


_TMirrorDestL3EncUseDirectionBit_Type.__name__ = "TruthValue"
_TMirrorDestL3EncUseDirectionBit_Object = MibTableColumn
tMirrorDestL3EncUseDirectionBit = _TMirrorDestL3EncUseDirectionBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 6, 1, 5),
    _TMirrorDestL3EncUseDirectionBit_Type()
)
tMirrorDestL3EncUseDirectionBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestL3EncUseDirectionBit.setStatus("current")
_TMirrorDestL3GwTableLastCh_Type = TimeStamp
_TMirrorDestL3GwTableLastCh_Object = MibScalar
tMirrorDestL3GwTableLastCh = _TMirrorDestL3GwTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 7),
    _TMirrorDestL3GwTableLastCh_Type()
)
tMirrorDestL3GwTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestL3GwTableLastCh.setStatus("current")
_TMirrorDestL3GwTable_Object = MibTable
tMirrorDestL3GwTable = _TMirrorDestL3GwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 8)
)
if mibBuilder.loadTexts:
    tMirrorDestL3GwTable.setStatus("current")
_TMirrorDestL3GwEntry_Object = MibTableRow
tMirrorDestL3GwEntry = _TMirrorDestL3GwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 8, 1)
)
tMirrorDestL3GwEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorDestinationIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorDestL3GwRole"),
)
if mibBuilder.loadTexts:
    tMirrorDestL3GwEntry.setStatus("current")


class _TMirrorDestL3GwRole_Type(TmnxMirrorGatewayRole):
    """Custom type tMirrorDestL3GwRole based on TmnxMirrorGatewayRole"""
    subtypeSpec = TmnxMirrorGatewayRole.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("primary", 1)
    )


_TMirrorDestL3GwRole_Type.__name__ = "TmnxMirrorGatewayRole"
_TMirrorDestL3GwRole_Object = MibTableColumn
tMirrorDestL3GwRole = _TMirrorDestL3GwRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 8, 1, 1),
    _TMirrorDestL3GwRole_Type()
)
tMirrorDestL3GwRole.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorDestL3GwRole.setStatus("current")
_TMirrorDestL3GwRowStatus_Type = RowStatus
_TMirrorDestL3GwRowStatus_Object = MibTableColumn
tMirrorDestL3GwRowStatus = _TMirrorDestL3GwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 8, 1, 2),
    _TMirrorDestL3GwRowStatus_Type()
)
tMirrorDestL3GwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestL3GwRowStatus.setStatus("current")
_TMirrorDestL3GwLastCh_Type = TimeStamp
_TMirrorDestL3GwLastCh_Object = MibTableColumn
tMirrorDestL3GwLastCh = _TMirrorDestL3GwLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 8, 1, 3),
    _TMirrorDestL3GwLastCh_Type()
)
tMirrorDestL3GwLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorDestL3GwLastCh.setStatus("current")


class _TMirrorDestL3GwSrcAddrType_Type(InetAddressType):
    """Custom type tMirrorDestL3GwSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TMirrorDestL3GwSrcAddrType_Type.__name__ = "InetAddressType"
_TMirrorDestL3GwSrcAddrType_Object = MibTableColumn
tMirrorDestL3GwSrcAddrType = _TMirrorDestL3GwSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 8, 1, 4),
    _TMirrorDestL3GwSrcAddrType_Type()
)
tMirrorDestL3GwSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestL3GwSrcAddrType.setStatus("current")


class _TMirrorDestL3GwSrcAddr_Type(InetAddress):
    """Custom type tMirrorDestL3GwSrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TMirrorDestL3GwSrcAddr_Type.__name__ = "InetAddress"
_TMirrorDestL3GwSrcAddr_Object = MibTableColumn
tMirrorDestL3GwSrcAddr = _TMirrorDestL3GwSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 8, 1, 5),
    _TMirrorDestL3GwSrcAddr_Type()
)
tMirrorDestL3GwSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestL3GwSrcAddr.setStatus("current")


class _TMirrorDestL3GwDstAddrType_Type(InetAddressType):
    """Custom type tMirrorDestL3GwDstAddrType based on InetAddressType"""
    defaultValue = 0


_TMirrorDestL3GwDstAddrType_Type.__name__ = "InetAddressType"
_TMirrorDestL3GwDstAddrType_Object = MibTableColumn
tMirrorDestL3GwDstAddrType = _TMirrorDestL3GwDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 8, 1, 6),
    _TMirrorDestL3GwDstAddrType_Type()
)
tMirrorDestL3GwDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestL3GwDstAddrType.setStatus("current")


class _TMirrorDestL3GwDstAddr_Type(InetAddress):
    """Custom type tMirrorDestL3GwDstAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TMirrorDestL3GwDstAddr_Type.__name__ = "InetAddress"
_TMirrorDestL3GwDstAddr_Object = MibTableColumn
tMirrorDestL3GwDstAddr = _TMirrorDestL3GwDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 8, 1, 7),
    _TMirrorDestL3GwDstAddr_Type()
)
tMirrorDestL3GwDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestL3GwDstAddr.setStatus("current")


class _TMirrorDestL3GwUdpSrcPort_Type(InetPortNumber):
    """Custom type tMirrorDestL3GwUdpSrcPort based on InetPortNumber"""
    defaultValue = 0


_TMirrorDestL3GwUdpSrcPort_Type.__name__ = "InetPortNumber"
_TMirrorDestL3GwUdpSrcPort_Object = MibTableColumn
tMirrorDestL3GwUdpSrcPort = _TMirrorDestL3GwUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 8, 1, 8),
    _TMirrorDestL3GwUdpSrcPort_Type()
)
tMirrorDestL3GwUdpSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestL3GwUdpSrcPort.setStatus("current")


class _TMirrorDestL3GwUdpDstPort_Type(InetPortNumber):
    """Custom type tMirrorDestL3GwUdpDstPort based on InetPortNumber"""
    defaultValue = 0


_TMirrorDestL3GwUdpDstPort_Type.__name__ = "InetPortNumber"
_TMirrorDestL3GwUdpDstPort_Object = MibTableColumn
tMirrorDestL3GwUdpDstPort = _TMirrorDestL3GwUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 1, 8, 1, 9),
    _TMirrorDestL3GwUdpDstPort_Type()
)
tMirrorDestL3GwUdpDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorDestL3GwUdpDstPort.setStatus("current")
_TMirrorSourceObjects_ObjectIdentity = ObjectIdentity
tMirrorSourceObjects = _TMirrorSourceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2)
)
_TMirrorSourceTable_Object = MibTable
tMirrorSourceTable = _TMirrorSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    tMirrorSourceTable.setStatus("current")
_TMirrorSourceEntry_Object = MibTableRow
tMirrorSourceEntry = _TMirrorSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 1, 1)
)
tMirrorSourceEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
)
if mibBuilder.loadTexts:
    tMirrorSourceEntry.setStatus("current")
_TMirrorSourceIndex_Type = TmnxServId
_TMirrorSourceIndex_Object = MibTableColumn
tMirrorSourceIndex = _TMirrorSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 1, 1, 1),
    _TMirrorSourceIndex_Type()
)
tMirrorSourceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorSourceIndex.setStatus("current")


class _TMirrorSourceAdminStatus_Type(ServiceAdminStatus):
    """Custom type tMirrorSourceAdminStatus based on ServiceAdminStatus"""
    defaultValue = 1


_TMirrorSourceAdminStatus_Type.__name__ = "ServiceAdminStatus"
_TMirrorSourceAdminStatus_Object = MibTableColumn
tMirrorSourceAdminStatus = _TMirrorSourceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 1, 1, 2),
    _TMirrorSourceAdminStatus_Type()
)
tMirrorSourceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceAdminStatus.setStatus("current")
_TMirrorSourceRowStatus_Type = RowStatus
_TMirrorSourceRowStatus_Object = MibTableColumn
tMirrorSourceRowStatus = _TMirrorSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 1, 1, 3),
    _TMirrorSourceRowStatus_Type()
)
tMirrorSourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceRowStatus.setStatus("current")
_TMirrorSourceLastChgd_Type = TimeStamp
_TMirrorSourceLastChgd_Object = MibTableColumn
tMirrorSourceLastChgd = _TMirrorSourceLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 1, 1, 4),
    _TMirrorSourceLastChgd_Type()
)
tMirrorSourceLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceLastChgd.setStatus("current")


class _TMirrorSourceCreationOrigin_Type(Integer32):
    """Custom type tMirrorSourceCreationOrigin based on Integer32"""
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
        *(("debug", 1),
          ("li", 2),
          ("config", 3))
    )


_TMirrorSourceCreationOrigin_Type.__name__ = "Integer32"
_TMirrorSourceCreationOrigin_Object = MibTableColumn
tMirrorSourceCreationOrigin = _TMirrorSourceCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 1, 1, 5),
    _TMirrorSourceCreationOrigin_Type()
)
tMirrorSourceCreationOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceCreationOrigin.setStatus("current")


class _TMirrorSourceName_Type(TLNamedItemOrEmpty):
    """Custom type tMirrorSourceName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TMirrorSourceName_Type.__name__ = "TLNamedItemOrEmpty"
_TMirrorSourceName_Object = MibTableColumn
tMirrorSourceName = _TMirrorSourceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 1, 1, 6),
    _TMirrorSourceName_Type()
)
tMirrorSourceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceName.setStatus("current")
_TMirrorSourceIpFilterTable_Object = MibTable
tMirrorSourceIpFilterTable = _TMirrorSourceIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    tMirrorSourceIpFilterTable.setStatus("current")
_TMirrorSourceIpFilterEntry_Object = MibTableRow
tMirrorSourceIpFilterEntry = _TMirrorSourceIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 2, 1)
)
tMirrorSourceIpFilterEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIpFilter"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIpFilterParams"),
)
if mibBuilder.loadTexts:
    tMirrorSourceIpFilterEntry.setStatus("current")


class _TMirrorSourceIpFilter_Type(TFilterID):
    """Custom type tMirrorSourceIpFilter based on TFilterID"""
    subtypeSpec = TFilterID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TMirrorSourceIpFilter_Type.__name__ = "TFilterID"
_TMirrorSourceIpFilter_Object = MibTableColumn
tMirrorSourceIpFilter = _TMirrorSourceIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 2, 1, 1),
    _TMirrorSourceIpFilter_Type()
)
tMirrorSourceIpFilter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceIpFilter.setStatus("current")
_TMirrorSourceIpFilterParams_Type = TEntryId
_TMirrorSourceIpFilterParams_Object = MibTableColumn
tMirrorSourceIpFilterParams = _TMirrorSourceIpFilterParams_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 2, 1, 2),
    _TMirrorSourceIpFilterParams_Type()
)
tMirrorSourceIpFilterParams.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceIpFilterParams.setStatus("current")
_TMirrorSourceIpFilterRowStatus_Type = RowStatus
_TMirrorSourceIpFilterRowStatus_Object = MibTableColumn
tMirrorSourceIpFilterRowStatus = _TMirrorSourceIpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 2, 1, 3),
    _TMirrorSourceIpFilterRowStatus_Type()
)
tMirrorSourceIpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceIpFilterRowStatus.setStatus("current")
_TMirrorSourceIpFilterLastChgd_Type = TimeStamp
_TMirrorSourceIpFilterLastChgd_Object = MibTableColumn
tMirrorSourceIpFilterLastChgd = _TMirrorSourceIpFilterLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 2, 1, 4),
    _TMirrorSourceIpFilterLastChgd_Type()
)
tMirrorSourceIpFilterLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceIpFilterLastChgd.setStatus("current")


class _TMirrorSourceIpFilterIntceptId_Type(TmnxInterceptionIdentifier):
    """Custom type tMirrorSourceIpFilterIntceptId based on TmnxInterceptionIdentifier"""
    defaultValue = 0


_TMirrorSourceIpFilterIntceptId_Type.__name__ = "TmnxInterceptionIdentifier"
_TMirrorSourceIpFilterIntceptId_Object = MibTableColumn
tMirrorSourceIpFilterIntceptId = _TMirrorSourceIpFilterIntceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 2, 1, 5),
    _TMirrorSourceIpFilterIntceptId_Type()
)
tMirrorSourceIpFilterIntceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceIpFilterIntceptId.setStatus("current")


class _TMirrorSourceIpFilterSessionId_Type(Unsigned32):
    """Custom type tMirrorSourceIpFilterSessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorSourceIpFilterSessionId_Type.__name__ = "Unsigned32"
_TMirrorSourceIpFilterSessionId_Object = MibTableColumn
tMirrorSourceIpFilterSessionId = _TMirrorSourceIpFilterSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 2, 1, 6),
    _TMirrorSourceIpFilterSessionId_Type()
)
tMirrorSourceIpFilterSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceIpFilterSessionId.setStatus("current")
_TMirrorSourceMacFilterTable_Object = MibTable
tMirrorSourceMacFilterTable = _TMirrorSourceMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 3)
)
if mibBuilder.loadTexts:
    tMirrorSourceMacFilterTable.setStatus("current")
_TMirrorSourceMacFilterEntry_Object = MibTableRow
tMirrorSourceMacFilterEntry = _TMirrorSourceMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 3, 1)
)
tMirrorSourceMacFilterEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceMacFilter"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceMacFilterParams"),
)
if mibBuilder.loadTexts:
    tMirrorSourceMacFilterEntry.setStatus("current")


class _TMirrorSourceMacFilter_Type(TFilterID):
    """Custom type tMirrorSourceMacFilter based on TFilterID"""
    subtypeSpec = TFilterID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TMirrorSourceMacFilter_Type.__name__ = "TFilterID"
_TMirrorSourceMacFilter_Object = MibTableColumn
tMirrorSourceMacFilter = _TMirrorSourceMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 3, 1, 1),
    _TMirrorSourceMacFilter_Type()
)
tMirrorSourceMacFilter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceMacFilter.setStatus("current")
_TMirrorSourceMacFilterParams_Type = TEntryId
_TMirrorSourceMacFilterParams_Object = MibTableColumn
tMirrorSourceMacFilterParams = _TMirrorSourceMacFilterParams_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 3, 1, 2),
    _TMirrorSourceMacFilterParams_Type()
)
tMirrorSourceMacFilterParams.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceMacFilterParams.setStatus("current")
_TMirrorSourceMacFilterRowStatus_Type = RowStatus
_TMirrorSourceMacFilterRowStatus_Object = MibTableColumn
tMirrorSourceMacFilterRowStatus = _TMirrorSourceMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 3, 1, 3),
    _TMirrorSourceMacFilterRowStatus_Type()
)
tMirrorSourceMacFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceMacFilterRowStatus.setStatus("current")
_TMirrorSourceMacFilterLastChgd_Type = TimeStamp
_TMirrorSourceMacFilterLastChgd_Object = MibTableColumn
tMirrorSourceMacFilterLastChgd = _TMirrorSourceMacFilterLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 3, 1, 4),
    _TMirrorSourceMacFilterLastChgd_Type()
)
tMirrorSourceMacFilterLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceMacFilterLastChgd.setStatus("current")


class _TMirrorSourceMacFilterIntceptId_Type(TmnxInterceptionIdentifier):
    """Custom type tMirrorSourceMacFilterIntceptId based on TmnxInterceptionIdentifier"""
    defaultValue = 0


_TMirrorSourceMacFilterIntceptId_Type.__name__ = "TmnxInterceptionIdentifier"
_TMirrorSourceMacFilterIntceptId_Object = MibTableColumn
tMirrorSourceMacFilterIntceptId = _TMirrorSourceMacFilterIntceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 3, 1, 5),
    _TMirrorSourceMacFilterIntceptId_Type()
)
tMirrorSourceMacFilterIntceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceMacFilterIntceptId.setStatus("current")


class _TMirrorSourceMacFilterSessionId_Type(Unsigned32):
    """Custom type tMirrorSourceMacFilterSessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorSourceMacFilterSessionId_Type.__name__ = "Unsigned32"
_TMirrorSourceMacFilterSessionId_Object = MibTableColumn
tMirrorSourceMacFilterSessionId = _TMirrorSourceMacFilterSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 3, 1, 6),
    _TMirrorSourceMacFilterSessionId_Type()
)
tMirrorSourceMacFilterSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceMacFilterSessionId.setStatus("current")
_TMirrorSourceIngressLabelTable_Object = MibTable
tMirrorSourceIngressLabelTable = _TMirrorSourceIngressLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 4)
)
if mibBuilder.loadTexts:
    tMirrorSourceIngressLabelTable.setStatus("current")
_TMirrorSourceIngressLabelEntry_Object = MibTableRow
tMirrorSourceIngressLabelEntry = _TMirrorSourceIngressLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 4, 1)
)
tMirrorSourceIngressLabelEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIngressLabelIndex"),
)
if mibBuilder.loadTexts:
    tMirrorSourceIngressLabelEntry.setStatus("current")
_TMirrorSourceIngressLabelIndex_Type = TMplsLabel
_TMirrorSourceIngressLabelIndex_Object = MibTableColumn
tMirrorSourceIngressLabelIndex = _TMirrorSourceIngressLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 4, 1, 1),
    _TMirrorSourceIngressLabelIndex_Type()
)
tMirrorSourceIngressLabelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceIngressLabelIndex.setStatus("current")
_TMirrorSourceIngressLabelRowStatus_Type = RowStatus
_TMirrorSourceIngressLabelRowStatus_Object = MibTableColumn
tMirrorSourceIngressLabelRowStatus = _TMirrorSourceIngressLabelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 4, 1, 2),
    _TMirrorSourceIngressLabelRowStatus_Type()
)
tMirrorSourceIngressLabelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceIngressLabelRowStatus.setStatus("current")
_TMirrorSourceIngLabelLastChgd_Type = TimeStamp
_TMirrorSourceIngLabelLastChgd_Object = MibTableColumn
tMirrorSourceIngLabelLastChgd = _TMirrorSourceIngLabelLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 4, 1, 3),
    _TMirrorSourceIngLabelLastChgd_Type()
)
tMirrorSourceIngLabelLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceIngLabelLastChgd.setStatus("current")
_TMirrorSourcePortTable_Object = MibTable
tMirrorSourcePortTable = _TMirrorSourcePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 5)
)
if mibBuilder.loadTexts:
    tMirrorSourcePortTable.setStatus("current")
_TMirrorSourcePortEntry_Object = MibTableRow
tMirrorSourcePortEntry = _TMirrorSourcePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 5, 1)
)
tMirrorSourcePortEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourcePortIndex"),
)
if mibBuilder.loadTexts:
    tMirrorSourcePortEntry.setStatus("current")
_TMirrorSourcePortIndex_Type = TmnxPortID
_TMirrorSourcePortIndex_Object = MibTableColumn
tMirrorSourcePortIndex = _TMirrorSourcePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 5, 1, 1),
    _TMirrorSourcePortIndex_Type()
)
tMirrorSourcePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourcePortIndex.setStatus("current")
_TMirrorSourcePortRowStatus_Type = RowStatus
_TMirrorSourcePortRowStatus_Object = MibTableColumn
tMirrorSourcePortRowStatus = _TMirrorSourcePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 5, 1, 2),
    _TMirrorSourcePortRowStatus_Type()
)
tMirrorSourcePortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourcePortRowStatus.setStatus("current")


class _TMirrorSourcePortEgressEnabled_Type(TruthValue):
    """Custom type tMirrorSourcePortEgressEnabled based on TruthValue"""
    defaultValue = 2


_TMirrorSourcePortEgressEnabled_Type.__name__ = "TruthValue"
_TMirrorSourcePortEgressEnabled_Object = MibTableColumn
tMirrorSourcePortEgressEnabled = _TMirrorSourcePortEgressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 5, 1, 3),
    _TMirrorSourcePortEgressEnabled_Type()
)
tMirrorSourcePortEgressEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourcePortEgressEnabled.setStatus("current")


class _TMirrorSourcePortIngressEnabled_Type(TruthValue):
    """Custom type tMirrorSourcePortIngressEnabled based on TruthValue"""
    defaultValue = 2


_TMirrorSourcePortIngressEnabled_Type.__name__ = "TruthValue"
_TMirrorSourcePortIngressEnabled_Object = MibTableColumn
tMirrorSourcePortIngressEnabled = _TMirrorSourcePortIngressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 5, 1, 4),
    _TMirrorSourcePortIngressEnabled_Type()
)
tMirrorSourcePortIngressEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourcePortIngressEnabled.setStatus("current")
_TMirrorSourcePortLastChgd_Type = TimeStamp
_TMirrorSourcePortLastChgd_Object = MibTableColumn
tMirrorSourcePortLastChgd = _TMirrorSourcePortLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 5, 1, 5),
    _TMirrorSourcePortLastChgd_Type()
)
tMirrorSourcePortLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourcePortLastChgd.setStatus("current")


class _TMirrorSourcePortLicenseState_Type(Integer32):
    """Custom type tMirrorSourcePortLicenseState based on Integer32"""
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
        *(("unknown", 0),
          ("ok", 1),
          ("insufficient", 2),
          ("violation", 3))
    )


_TMirrorSourcePortLicenseState_Type.__name__ = "Integer32"
_TMirrorSourcePortLicenseState_Object = MibTableColumn
tMirrorSourcePortLicenseState = _TMirrorSourcePortLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 5, 1, 6),
    _TMirrorSourcePortLicenseState_Type()
)
tMirrorSourcePortLicenseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourcePortLicenseState.setStatus("current")
_TMirrorSourceSapTable_Object = MibTable
tMirrorSourceSapTable = _TMirrorSourceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 6)
)
if mibBuilder.loadTexts:
    tMirrorSourceSapTable.setStatus("current")
_TMirrorSourceSapEntry_Object = MibTableRow
tMirrorSourceSapEntry = _TMirrorSourceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 6, 1)
)
tMirrorSourceSapEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceSapPortId"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceSapEncapValue"),
)
if mibBuilder.loadTexts:
    tMirrorSourceSapEntry.setStatus("current")
_TMirrorSourceSapPortId_Type = TmnxPortID
_TMirrorSourceSapPortId_Object = MibTableColumn
tMirrorSourceSapPortId = _TMirrorSourceSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 6, 1, 2),
    _TMirrorSourceSapPortId_Type()
)
tMirrorSourceSapPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorSourceSapPortId.setStatus("current")
_TMirrorSourceSapEncapValue_Type = TmnxEncapVal
_TMirrorSourceSapEncapValue_Object = MibTableColumn
tMirrorSourceSapEncapValue = _TMirrorSourceSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 6, 1, 3),
    _TMirrorSourceSapEncapValue_Type()
)
tMirrorSourceSapEncapValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorSourceSapEncapValue.setStatus("current")
_TMirrorSourceSapRowStatus_Type = RowStatus
_TMirrorSourceSapRowStatus_Object = MibTableColumn
tMirrorSourceSapRowStatus = _TMirrorSourceSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 6, 1, 4),
    _TMirrorSourceSapRowStatus_Type()
)
tMirrorSourceSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSapRowStatus.setStatus("current")


class _TMirrorSourceSapEgressEnabled_Type(TruthValue):
    """Custom type tMirrorSourceSapEgressEnabled based on TruthValue"""
    defaultValue = 2


_TMirrorSourceSapEgressEnabled_Type.__name__ = "TruthValue"
_TMirrorSourceSapEgressEnabled_Object = MibTableColumn
tMirrorSourceSapEgressEnabled = _TMirrorSourceSapEgressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 6, 1, 5),
    _TMirrorSourceSapEgressEnabled_Type()
)
tMirrorSourceSapEgressEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSapEgressEnabled.setStatus("current")


class _TMirrorSourceSapIngressEnabled_Type(TruthValue):
    """Custom type tMirrorSourceSapIngressEnabled based on TruthValue"""
    defaultValue = 2


_TMirrorSourceSapIngressEnabled_Type.__name__ = "TruthValue"
_TMirrorSourceSapIngressEnabled_Object = MibTableColumn
tMirrorSourceSapIngressEnabled = _TMirrorSourceSapIngressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 6, 1, 6),
    _TMirrorSourceSapIngressEnabled_Type()
)
tMirrorSourceSapIngressEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSapIngressEnabled.setStatus("current")
_TMirrorSourceSapLastChgd_Type = TimeStamp
_TMirrorSourceSapLastChgd_Object = MibTableColumn
tMirrorSourceSapLastChgd = _TMirrorSourceSapLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 6, 1, 7),
    _TMirrorSourceSapLastChgd_Type()
)
tMirrorSourceSapLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceSapLastChgd.setStatus("current")


class _TMirrorSourceSapIntceptId_Type(TmnxInterceptionIdentifier):
    """Custom type tMirrorSourceSapIntceptId based on TmnxInterceptionIdentifier"""
    defaultValue = 0


_TMirrorSourceSapIntceptId_Type.__name__ = "TmnxInterceptionIdentifier"
_TMirrorSourceSapIntceptId_Object = MibTableColumn
tMirrorSourceSapIntceptId = _TMirrorSourceSapIntceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 6, 1, 8),
    _TMirrorSourceSapIntceptId_Type()
)
tMirrorSourceSapIntceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSapIntceptId.setStatus("current")


class _TMirrorSourceSapSessionId_Type(Unsigned32):
    """Custom type tMirrorSourceSapSessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorSourceSapSessionId_Type.__name__ = "Unsigned32"
_TMirrorSourceSapSessionId_Object = MibTableColumn
tMirrorSourceSapSessionId = _TMirrorSourceSapSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 6, 1, 9),
    _TMirrorSourceSapSessionId_Type()
)
tMirrorSourceSapSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSapSessionId.setStatus("current")
_TMirrorSourceSubTableLastChnged_Type = TimeStamp
_TMirrorSourceSubTableLastChnged_Object = MibScalar
tMirrorSourceSubTableLastChnged = _TMirrorSourceSubTableLastChnged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 7),
    _TMirrorSourceSubTableLastChnged_Type()
)
tMirrorSourceSubTableLastChnged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceSubTableLastChnged.setStatus("current")
_TMirrorSourceSubscriberTable_Object = MibTable
tMirrorSourceSubscriberTable = _TMirrorSourceSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8)
)
if mibBuilder.loadTexts:
    tMirrorSourceSubscriberTable.setStatus("current")
_TMirrorSourceSubscriberEntry_Object = MibTableRow
tMirrorSourceSubscriberEntry = _TMirrorSourceSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1)
)
tMirrorSourceSubscriberEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceSubIdent"),
)
if mibBuilder.loadTexts:
    tMirrorSourceSubscriberEntry.setStatus("current")
_TMirrorSourceSubIdent_Type = TLNamedItem
_TMirrorSourceSubIdent_Object = MibTableColumn
tMirrorSourceSubIdent = _TMirrorSourceSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 1),
    _TMirrorSourceSubIdent_Type()
)
tMirrorSourceSubIdent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorSourceSubIdent.setStatus("current")
_TMirrorSourceSubRowStatus_Type = RowStatus
_TMirrorSourceSubRowStatus_Object = MibTableColumn
tMirrorSourceSubRowStatus = _TMirrorSourceSubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 2),
    _TMirrorSourceSubRowStatus_Type()
)
tMirrorSourceSubRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubRowStatus.setStatus("current")
_TMirrorSourceSubLastChanged_Type = TimeStamp
_TMirrorSourceSubLastChanged_Object = MibTableColumn
tMirrorSourceSubLastChanged = _TMirrorSourceSubLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 3),
    _TMirrorSourceSubLastChanged_Type()
)
tMirrorSourceSubLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceSubLastChanged.setStatus("current")


class _TMirrorSourceSubPortId_Type(TmnxPortID):
    """Custom type tMirrorSourceSubPortId based on TmnxPortID"""
    defaultValue = 0


_TMirrorSourceSubPortId_Type.__name__ = "TmnxPortID"
_TMirrorSourceSubPortId_Object = MibTableColumn
tMirrorSourceSubPortId = _TMirrorSourceSubPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 4),
    _TMirrorSourceSubPortId_Type()
)
tMirrorSourceSubPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubPortId.setStatus("current")


class _TMirrorSourceSubEncapValue_Type(TmnxEncapVal):
    """Custom type tMirrorSourceSubEncapValue based on TmnxEncapVal"""
    defaultValue = 0


_TMirrorSourceSubEncapValue_Type.__name__ = "TmnxEncapVal"
_TMirrorSourceSubEncapValue_Object = MibTableColumn
tMirrorSourceSubEncapValue = _TMirrorSourceSubEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 5),
    _TMirrorSourceSubEncapValue_Type()
)
tMirrorSourceSubEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubEncapValue.setStatus("current")


class _TMirrorSourceSubIpAddrType_Type(InetAddressType):
    """Custom type tMirrorSourceSubIpAddrType based on InetAddressType"""
    defaultValue = 0


_TMirrorSourceSubIpAddrType_Type.__name__ = "InetAddressType"
_TMirrorSourceSubIpAddrType_Object = MibTableColumn
tMirrorSourceSubIpAddrType = _TMirrorSourceSubIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 6),
    _TMirrorSourceSubIpAddrType_Type()
)
tMirrorSourceSubIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubIpAddrType.setStatus("current")


class _TMirrorSourceSubIpAddr_Type(InetAddress):
    """Custom type tMirrorSourceSubIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TMirrorSourceSubIpAddr_Type.__name__ = "InetAddress"
_TMirrorSourceSubIpAddr_Object = MibTableColumn
tMirrorSourceSubIpAddr = _TMirrorSourceSubIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 7),
    _TMirrorSourceSubIpAddr_Type()
)
tMirrorSourceSubIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubIpAddr.setStatus("current")


class _TMirrorSourceSubMacAddr_Type(MacAddress):
    """Custom type tMirrorSourceSubMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TMirrorSourceSubMacAddr_Type.__name__ = "MacAddress"
_TMirrorSourceSubMacAddr_Object = MibTableColumn
tMirrorSourceSubMacAddr = _TMirrorSourceSubMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 8),
    _TMirrorSourceSubMacAddr_Type()
)
tMirrorSourceSubMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubMacAddr.setStatus("current")


class _TMirrorSourceSubSLAProfName_Type(TNamedItemOrEmpty):
    """Custom type tMirrorSourceSubSLAProfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TMirrorSourceSubSLAProfName_Type.__name__ = "TNamedItemOrEmpty"
_TMirrorSourceSubSLAProfName_Object = MibTableColumn
tMirrorSourceSubSLAProfName = _TMirrorSourceSubSLAProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 9),
    _TMirrorSourceSubSLAProfName_Type()
)
tMirrorSourceSubSLAProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubSLAProfName.setStatus("current")


class _TMirrorSourceSubFC_Type(TFCSet):
    """Custom type tMirrorSourceSubFC based on TFCSet"""
    defaultBinValue = "0"


_TMirrorSourceSubFC_Type.__name__ = "TFCSet"
_TMirrorSourceSubFC_Object = MibTableColumn
tMirrorSourceSubFC = _TMirrorSourceSubFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 10),
    _TMirrorSourceSubFC_Type()
)
tMirrorSourceSubFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubFC.setStatus("current")


class _TMirrorSourceSubEgressEnabled_Type(TruthValue):
    """Custom type tMirrorSourceSubEgressEnabled based on TruthValue"""
    defaultValue = 2


_TMirrorSourceSubEgressEnabled_Type.__name__ = "TruthValue"
_TMirrorSourceSubEgressEnabled_Object = MibTableColumn
tMirrorSourceSubEgressEnabled = _TMirrorSourceSubEgressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 11),
    _TMirrorSourceSubEgressEnabled_Type()
)
tMirrorSourceSubEgressEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubEgressEnabled.setStatus("current")


class _TMirrorSourceSubIngressEnabled_Type(TruthValue):
    """Custom type tMirrorSourceSubIngressEnabled based on TruthValue"""
    defaultValue = 2


_TMirrorSourceSubIngressEnabled_Type.__name__ = "TruthValue"
_TMirrorSourceSubIngressEnabled_Object = MibTableColumn
tMirrorSourceSubIngressEnabled = _TMirrorSourceSubIngressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 12),
    _TMirrorSourceSubIngressEnabled_Type()
)
tMirrorSourceSubIngressEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubIngressEnabled.setStatus("current")


class _TMirrorSourceSubIntceptId_Type(TmnxInterceptionIdentifier):
    """Custom type tMirrorSourceSubIntceptId based on TmnxInterceptionIdentifier"""
    defaultValue = 0


_TMirrorSourceSubIntceptId_Type.__name__ = "TmnxInterceptionIdentifier"
_TMirrorSourceSubIntceptId_Object = MibTableColumn
tMirrorSourceSubIntceptId = _TMirrorSourceSubIntceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 13),
    _TMirrorSourceSubIntceptId_Type()
)
tMirrorSourceSubIntceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubIntceptId.setStatus("current")


class _TMirrorSourceSubSessionId_Type(Unsigned32):
    """Custom type tMirrorSourceSubSessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorSourceSubSessionId_Type.__name__ = "Unsigned32"
_TMirrorSourceSubSessionId_Object = MibTableColumn
tMirrorSourceSubSessionId = _TMirrorSourceSubSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 14),
    _TMirrorSourceSubSessionId_Type()
)
tMirrorSourceSubSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubSessionId.setStatus("current")


class _TMirrorSourceSubHostType_Type(Integer32):
    """Custom type tMirrorSourceSubHostType based on Integer32"""
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
        *(("any", 1),
          ("ipoe", 2),
          ("ppp", 3))
    )


_TMirrorSourceSubHostType_Type.__name__ = "Integer32"
_TMirrorSourceSubHostType_Object = MibTableColumn
tMirrorSourceSubHostType = _TMirrorSourceSubHostType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 15),
    _TMirrorSourceSubHostType_Type()
)
tMirrorSourceSubHostType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubHostType.setStatus("current")


class _TMirrorSourceSubIpFamily_Type(Integer32):
    """Custom type tMirrorSourceSubIpFamily based on Integer32"""
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
        *(("any", 1),
          ("ipv4", 2),
          ("ipv6", 3))
    )


_TMirrorSourceSubIpFamily_Type.__name__ = "Integer32"
_TMirrorSourceSubIpFamily_Object = MibTableColumn
tMirrorSourceSubIpFamily = _TMirrorSourceSubIpFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 8, 1, 16),
    _TMirrorSourceSubIpFamily_Type()
)
tMirrorSourceSubIpFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceSubIpFamily.setStatus("current")
_TMirrorSourceIsaAaGrpTable_Object = MibTable
tMirrorSourceIsaAaGrpTable = _TMirrorSourceIsaAaGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 9)
)
if mibBuilder.loadTexts:
    tMirrorSourceIsaAaGrpTable.setStatus("current")
_TMirrorSourceIsaAaGrpEntry_Object = MibTableRow
tMirrorSourceIsaAaGrpEntry = _TMirrorSourceIsaAaGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 9, 1)
)
tMirrorSourceIsaAaGrpEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIsaAaGrpIndex"),
)
if mibBuilder.loadTexts:
    tMirrorSourceIsaAaGrpEntry.setStatus("current")
_TMirrorSourceIsaAaGrpIndex_Type = Integer32
_TMirrorSourceIsaAaGrpIndex_Object = MibTableColumn
tMirrorSourceIsaAaGrpIndex = _TMirrorSourceIsaAaGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 9, 1, 1),
    _TMirrorSourceIsaAaGrpIndex_Type()
)
tMirrorSourceIsaAaGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceIsaAaGrpIndex.setStatus("current")
_TMirrorSourceIsaAaGrpRowStatus_Type = RowStatus
_TMirrorSourceIsaAaGrpRowStatus_Object = MibTableColumn
tMirrorSourceIsaAaGrpRowStatus = _TMirrorSourceIsaAaGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 9, 1, 2),
    _TMirrorSourceIsaAaGrpRowStatus_Type()
)
tMirrorSourceIsaAaGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceIsaAaGrpRowStatus.setStatus("current")


class _TMirrorSourceIsaAaGrpUnknownOnly_Type(TruthValue):
    """Custom type tMirrorSourceIsaAaGrpUnknownOnly based on TruthValue"""
    defaultValue = 1


_TMirrorSourceIsaAaGrpUnknownOnly_Type.__name__ = "TruthValue"
_TMirrorSourceIsaAaGrpUnknownOnly_Object = MibTableColumn
tMirrorSourceIsaAaGrpUnknownOnly = _TMirrorSourceIsaAaGrpUnknownOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 9, 1, 3),
    _TMirrorSourceIsaAaGrpUnknownOnly_Type()
)
tMirrorSourceIsaAaGrpUnknownOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceIsaAaGrpUnknownOnly.setStatus("current")
_TMirrorSourceIsaAaGrpLastChgd_Type = TimeStamp
_TMirrorSourceIsaAaGrpLastChgd_Object = MibTableColumn
tMirrorSourceIsaAaGrpLastChgd = _TMirrorSourceIsaAaGrpLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 9, 1, 4),
    _TMirrorSourceIsaAaGrpLastChgd_Type()
)
tMirrorSourceIsaAaGrpLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceIsaAaGrpLastChgd.setStatus("current")
_TMirrorSrcTblLastChgd_Type = TimeStamp
_TMirrorSrcTblLastChgd_Object = MibScalar
tMirrorSrcTblLastChgd = _TMirrorSrcTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 10),
    _TMirrorSrcTblLastChgd_Type()
)
tMirrorSrcTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSrcTblLastChgd.setStatus("current")
_TMirrorSrcIpFltrTblLastChgd_Type = TimeStamp
_TMirrorSrcIpFltrTblLastChgd_Object = MibScalar
tMirrorSrcIpFltrTblLastChgd = _TMirrorSrcIpFltrTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 11),
    _TMirrorSrcIpFltrTblLastChgd_Type()
)
tMirrorSrcIpFltrTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSrcIpFltrTblLastChgd.setStatus("current")
_TMirrorSrcMacFltrTblLastChgd_Type = TimeStamp
_TMirrorSrcMacFltrTblLastChgd_Object = MibScalar
tMirrorSrcMacFltrTblLastChgd = _TMirrorSrcMacFltrTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 12),
    _TMirrorSrcMacFltrTblLastChgd_Type()
)
tMirrorSrcMacFltrTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSrcMacFltrTblLastChgd.setStatus("current")
_TMirrorSrcIngLblTblLastChgd_Type = TimeStamp
_TMirrorSrcIngLblTblLastChgd_Object = MibScalar
tMirrorSrcIngLblTblLastChgd = _TMirrorSrcIngLblTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 13),
    _TMirrorSrcIngLblTblLastChgd_Type()
)
tMirrorSrcIngLblTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSrcIngLblTblLastChgd.setStatus("current")
_TMirrorSrcPortTblLastChgd_Type = TimeStamp
_TMirrorSrcPortTblLastChgd_Object = MibScalar
tMirrorSrcPortTblLastChgd = _TMirrorSrcPortTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 14),
    _TMirrorSrcPortTblLastChgd_Type()
)
tMirrorSrcPortTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSrcPortTblLastChgd.setStatus("current")
_TMirrorSrcSapTblLastChgd_Type = TimeStamp
_TMirrorSrcSapTblLastChgd_Object = MibScalar
tMirrorSrcSapTblLastChgd = _TMirrorSrcSapTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 15),
    _TMirrorSrcSapTblLastChgd_Type()
)
tMirrorSrcSapTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSrcSapTblLastChgd.setStatus("current")
_TMirrorSrcIsaAaGrpTblLastChgd_Type = TimeStamp
_TMirrorSrcIsaAaGrpTblLastChgd_Object = MibScalar
tMirrorSrcIsaAaGrpTblLastChgd = _TMirrorSrcIsaAaGrpTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 16),
    _TMirrorSrcIsaAaGrpTblLastChgd_Type()
)
tMirrorSrcIsaAaGrpTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSrcIsaAaGrpTblLastChgd.setStatus("current")
_TMirrorSourceIpv6FilterTable_Object = MibTable
tMirrorSourceIpv6FilterTable = _TMirrorSourceIpv6FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 17)
)
if mibBuilder.loadTexts:
    tMirrorSourceIpv6FilterTable.setStatus("current")
_TMirrorSourceIpv6FilterEntry_Object = MibTableRow
tMirrorSourceIpv6FilterEntry = _TMirrorSourceIpv6FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 17, 1)
)
tMirrorSourceIpv6FilterEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIpv6Filter"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIpv6FilterParams"),
)
if mibBuilder.loadTexts:
    tMirrorSourceIpv6FilterEntry.setStatus("current")


class _TMirrorSourceIpv6Filter_Type(TFilterID):
    """Custom type tMirrorSourceIpv6Filter based on TFilterID"""
    subtypeSpec = TFilterID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TMirrorSourceIpv6Filter_Type.__name__ = "TFilterID"
_TMirrorSourceIpv6Filter_Object = MibTableColumn
tMirrorSourceIpv6Filter = _TMirrorSourceIpv6Filter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 17, 1, 1),
    _TMirrorSourceIpv6Filter_Type()
)
tMirrorSourceIpv6Filter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceIpv6Filter.setStatus("current")
_TMirrorSourceIpv6FilterParams_Type = TEntryId
_TMirrorSourceIpv6FilterParams_Object = MibTableColumn
tMirrorSourceIpv6FilterParams = _TMirrorSourceIpv6FilterParams_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 17, 1, 2),
    _TMirrorSourceIpv6FilterParams_Type()
)
tMirrorSourceIpv6FilterParams.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceIpv6FilterParams.setStatus("current")
_TMirrorSourceIpv6FilterRowStatus_Type = RowStatus
_TMirrorSourceIpv6FilterRowStatus_Object = MibTableColumn
tMirrorSourceIpv6FilterRowStatus = _TMirrorSourceIpv6FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 17, 1, 3),
    _TMirrorSourceIpv6FilterRowStatus_Type()
)
tMirrorSourceIpv6FilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceIpv6FilterRowStatus.setStatus("current")
_TMirrorSourceIpv6FilterLastChgd_Type = TimeStamp
_TMirrorSourceIpv6FilterLastChgd_Object = MibTableColumn
tMirrorSourceIpv6FilterLastChgd = _TMirrorSourceIpv6FilterLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 17, 1, 4),
    _TMirrorSourceIpv6FilterLastChgd_Type()
)
tMirrorSourceIpv6FilterLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceIpv6FilterLastChgd.setStatus("current")


class _TMirrorSourceIpv6FilterIntceptId_Type(TmnxInterceptionIdentifier):
    """Custom type tMirrorSourceIpv6FilterIntceptId based on TmnxInterceptionIdentifier"""
    defaultValue = 0


_TMirrorSourceIpv6FilterIntceptId_Type.__name__ = "TmnxInterceptionIdentifier"
_TMirrorSourceIpv6FilterIntceptId_Object = MibTableColumn
tMirrorSourceIpv6FilterIntceptId = _TMirrorSourceIpv6FilterIntceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 17, 1, 5),
    _TMirrorSourceIpv6FilterIntceptId_Type()
)
tMirrorSourceIpv6FilterIntceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceIpv6FilterIntceptId.setStatus("current")


class _TMirrorSourceIpv6FilterSessionId_Type(Unsigned32):
    """Custom type tMirrorSourceIpv6FilterSessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorSourceIpv6FilterSessionId_Type.__name__ = "Unsigned32"
_TMirrorSourceIpv6FilterSessionId_Object = MibTableColumn
tMirrorSourceIpv6FilterSessionId = _TMirrorSourceIpv6FilterSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 17, 1, 6),
    _TMirrorSourceIpv6FilterSessionId_Type()
)
tMirrorSourceIpv6FilterSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceIpv6FilterSessionId.setStatus("current")
_TMirrorSourceStatsTable_Object = MibTable
tMirrorSourceStatsTable = _TMirrorSourceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 18)
)
if mibBuilder.loadTexts:
    tMirrorSourceStatsTable.setStatus("current")
_TMirrorSourceStatsEntry_Object = MibTableRow
tMirrorSourceStatsEntry = _TMirrorSourceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 18, 1)
)
tMirrorSourceStatsEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
)
if mibBuilder.loadTexts:
    tMirrorSourceStatsEntry.setStatus("current")
_TMirrorSourceStatsTotalSrc_Type = Unsigned32
_TMirrorSourceStatsTotalSrc_Object = MibTableColumn
tMirrorSourceStatsTotalSrc = _TMirrorSourceStatsTotalSrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 18, 1, 1),
    _TMirrorSourceStatsTotalSrc_Type()
)
tMirrorSourceStatsTotalSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceStatsTotalSrc.setStatus("current")
_TMirrorSourcePortVlanTable_Object = MibTable
tMirrorSourcePortVlanTable = _TMirrorSourcePortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 19)
)
if mibBuilder.loadTexts:
    tMirrorSourcePortVlanTable.setStatus("current")
_TMirrorSourcePortVlanEntry_Object = MibTableRow
tMirrorSourcePortVlanEntry = _TMirrorSourcePortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 19, 1)
)
tMirrorSourcePortVlanEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourcePortVlanPortId"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourcePortVlanVlan"),
)
if mibBuilder.loadTexts:
    tMirrorSourcePortVlanEntry.setStatus("current")
_TMirrorSourcePortVlanPortId_Type = TmnxPortID
_TMirrorSourcePortVlanPortId_Object = MibTableColumn
tMirrorSourcePortVlanPortId = _TMirrorSourcePortVlanPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 19, 1, 1),
    _TMirrorSourcePortVlanPortId_Type()
)
tMirrorSourcePortVlanPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourcePortVlanPortId.setStatus("current")


class _TMirrorSourcePortVlanVlan_Type(Unsigned32):
    """Custom type tMirrorSourcePortVlanVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TMirrorSourcePortVlanVlan_Type.__name__ = "Unsigned32"
_TMirrorSourcePortVlanVlan_Object = MibTableColumn
tMirrorSourcePortVlanVlan = _TMirrorSourcePortVlanVlan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 19, 1, 2),
    _TMirrorSourcePortVlanVlan_Type()
)
tMirrorSourcePortVlanVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourcePortVlanVlan.setStatus("current")
_TMirrorSourcePortVlanRowStatus_Type = RowStatus
_TMirrorSourcePortVlanRowStatus_Object = MibTableColumn
tMirrorSourcePortVlanRowStatus = _TMirrorSourcePortVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 19, 1, 3),
    _TMirrorSourcePortVlanRowStatus_Type()
)
tMirrorSourcePortVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourcePortVlanRowStatus.setStatus("current")


class _TMirrorSourcePortVlanEgrEnabled_Type(TruthValue):
    """Custom type tMirrorSourcePortVlanEgrEnabled based on TruthValue"""
    defaultValue = 2


_TMirrorSourcePortVlanEgrEnabled_Type.__name__ = "TruthValue"
_TMirrorSourcePortVlanEgrEnabled_Object = MibTableColumn
tMirrorSourcePortVlanEgrEnabled = _TMirrorSourcePortVlanEgrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 19, 1, 4),
    _TMirrorSourcePortVlanEgrEnabled_Type()
)
tMirrorSourcePortVlanEgrEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourcePortVlanEgrEnabled.setStatus("current")


class _TMirrorSourcePortVlanIngEnabled_Type(TruthValue):
    """Custom type tMirrorSourcePortVlanIngEnabled based on TruthValue"""
    defaultValue = 2


_TMirrorSourcePortVlanIngEnabled_Type.__name__ = "TruthValue"
_TMirrorSourcePortVlanIngEnabled_Object = MibTableColumn
tMirrorSourcePortVlanIngEnabled = _TMirrorSourcePortVlanIngEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 19, 1, 5),
    _TMirrorSourcePortVlanIngEnabled_Type()
)
tMirrorSourcePortVlanIngEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourcePortVlanIngEnabled.setStatus("current")
_TMirrorSourcePortVlanLastChgd_Type = TimeStamp
_TMirrorSourcePortVlanLastChgd_Object = MibTableColumn
tMirrorSourcePortVlanLastChgd = _TMirrorSourcePortVlanLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 19, 1, 6),
    _TMirrorSourcePortVlanLastChgd_Type()
)
tMirrorSourcePortVlanLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourcePortVlanLastChgd.setStatus("current")
_TMirrorSrcPortVlanTblLastChgd_Type = TimeStamp
_TMirrorSrcPortVlanTblLastChgd_Object = MibScalar
tMirrorSrcPortVlanTblLastChgd = _TMirrorSrcPortVlanTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 20),
    _TMirrorSrcPortVlanTblLastChgd_Type()
)
tMirrorSrcPortVlanTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSrcPortVlanTblLastChgd.setStatus("current")
_TMirrorSourceSapShimTable_Object = MibTable
tMirrorSourceSapShimTable = _TMirrorSourceSapShimTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 21)
)
if mibBuilder.loadTexts:
    tMirrorSourceSapShimTable.setStatus("current")
_TMirrorSourceSapShimEntry_Object = MibTableRow
tMirrorSourceSapShimEntry = _TMirrorSourceSapShimEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 21, 1)
)
tMirrorSourceSapShimEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceSapShimPortId"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceSapShimEncapValue"),
)
if mibBuilder.loadTexts:
    tMirrorSourceSapShimEntry.setStatus("current")
_TMirrorSourceSapShimPortId_Type = TmnxPortID
_TMirrorSourceSapShimPortId_Object = MibTableColumn
tMirrorSourceSapShimPortId = _TMirrorSourceSapShimPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 21, 1, 1),
    _TMirrorSourceSapShimPortId_Type()
)
tMirrorSourceSapShimPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceSapShimPortId.setStatus("current")
_TMirrorSourceSapShimEncapValue_Type = TmnxEncapVal
_TMirrorSourceSapShimEncapValue_Object = MibTableColumn
tMirrorSourceSapShimEncapValue = _TMirrorSourceSapShimEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 21, 1, 2),
    _TMirrorSourceSapShimEncapValue_Type()
)
tMirrorSourceSapShimEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceSapShimEncapValue.setStatus("current")


class _TMirrorSourceSapShimId_Type(Unsigned32):
    """Custom type tMirrorSourceSapShimId based on Unsigned32"""
    defaultValue = 0


_TMirrorSourceSapShimId_Type.__name__ = "Unsigned32"
_TMirrorSourceSapShimId_Object = MibTableColumn
tMirrorSourceSapShimId = _TMirrorSourceSapShimId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 2, 21, 1, 3),
    _TMirrorSourceSapShimId_Type()
)
tMirrorSourceSapShimId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceSapShimId.setStatus("current")
_TMirrorSourceNotifyObjects_ObjectIdentity = ObjectIdentity
tMirrorSourceNotifyObjects = _TMirrorSourceNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3)
)


class _TMirrorSourceChangeType_Type(Integer32):
    """Custom type tMirrorSourceChangeType based on Integer32"""
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
        *(("modified", 1),
          ("deleted", 2),
          ("activated", 3),
          ("deactivated", 4))
    )


_TMirrorSourceChangeType_Type.__name__ = "Integer32"
_TMirrorSourceChangeType_Object = MibScalar
tMirrorSourceChangeType = _TMirrorSourceChangeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 1),
    _TMirrorSourceChangeType_Type()
)
tMirrorSourceChangeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorSourceChangeType.setStatus("current")
_TMirrorSourceFilterId_Type = TFilterID
_TMirrorSourceFilterId_Object = MibScalar
tMirrorSourceFilterId = _TMirrorSourceFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 3),
    _TMirrorSourceFilterId_Type()
)
tMirrorSourceFilterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorSourceFilterId.setStatus("current")
_TMirrorSourceFilterEntryId_Type = TEntryIdOrZero
_TMirrorSourceFilterEntryId_Object = MibScalar
tMirrorSourceFilterEntryId = _TMirrorSourceFilterEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 4),
    _TMirrorSourceFilterEntryId_Type()
)
tMirrorSourceFilterEntryId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorSourceFilterEntryId.setStatus("current")
_TMirrorSourceFilterObject_Type = ObjectIdentifier
_TMirrorSourceFilterObject_Object = MibScalar
tMirrorSourceFilterObject = _TMirrorSourceFilterObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 7),
    _TMirrorSourceFilterObject_Type()
)
tMirrorSourceFilterObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorSourceFilterObject.setStatus("current")
_TMirrorSourceFilterDescr_Type = DisplayString
_TMirrorSourceFilterDescr_Object = MibScalar
tMirrorSourceFilterDescr = _TMirrorSourceFilterDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 8),
    _TMirrorSourceFilterDescr_Type()
)
tMirrorSourceFilterDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorSourceFilterDescr.setStatus("current")
_TMirrorFilterSvcId_Type = TmnxServId
_TMirrorFilterSvcId_Object = MibScalar
tMirrorFilterSvcId = _TMirrorFilterSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 9),
    _TMirrorFilterSvcId_Type()
)
tMirrorFilterSvcId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorFilterSvcId.setStatus("current")
_TMirrorFilterPortId_Type = TmnxPortID
_TMirrorFilterPortId_Object = MibScalar
tMirrorFilterPortId = _TMirrorFilterPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 10),
    _TMirrorFilterPortId_Type()
)
tMirrorFilterPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorFilterPortId.setStatus("current")
_TMirrorFilterSapEncapValue_Type = TmnxEncapVal
_TMirrorFilterSapEncapValue_Object = MibScalar
tMirrorFilterSapEncapValue = _TMirrorFilterSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 11),
    _TMirrorFilterSapEncapValue_Type()
)
tMirrorFilterSapEncapValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorFilterSapEncapValue.setStatus("current")
_TMirrorFilterSdpBindId_Type = SdpBindId
_TMirrorFilterSdpBindId_Object = MibScalar
tMirrorFilterSdpBindId = _TMirrorFilterSdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 12),
    _TMirrorFilterSdpBindId_Type()
)
tMirrorFilterSdpBindId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorFilterSdpBindId.setStatus("current")
_TMirrorFilterType_Type = TFilterType
_TMirrorFilterType_Object = MibScalar
tMirrorFilterType = _TMirrorFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 13),
    _TMirrorFilterType_Type()
)
tMirrorFilterType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorFilterType.setStatus("current")


class _TMirrorFilterDirection_Type(Integer32):
    """Custom type tMirrorFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_TMirrorFilterDirection_Type.__name__ = "Integer32"
_TMirrorFilterDirection_Object = MibScalar
tMirrorFilterDirection = _TMirrorFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 14),
    _TMirrorFilterDirection_Type()
)
tMirrorFilterDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorFilterDirection.setStatus("current")
_TMirrorFilterId_Type = TFilterID
_TMirrorFilterId_Object = MibScalar
tMirrorFilterId = _TMirrorFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 15),
    _TMirrorFilterId_Type()
)
tMirrorFilterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorFilterId.setStatus("current")
_TMirrorFilterIfIndex_Type = InterfaceIndexOrZero
_TMirrorFilterIfIndex_Object = MibScalar
tMirrorFilterIfIndex = _TMirrorFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 16),
    _TMirrorFilterIfIndex_Type()
)
tMirrorFilterIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorFilterIfIndex.setStatus("current")
_TMirrorFilterIfName_Type = TNamedItem
_TMirrorFilterIfName_Object = MibScalar
tMirrorFilterIfName = _TMirrorFilterIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 3, 17),
    _TMirrorFilterIfName_Type()
)
tMirrorFilterIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorFilterIfName.setStatus("current")
_TMirrorRadiusLiObjects_ObjectIdentity = ObjectIdentity
tMirrorRadiusLiObjects = _TMirrorRadiusLiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4)
)
_TMirrorRadiusLiTable_Object = MibTable
tMirrorRadiusLiTable = _TMirrorRadiusLiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1)
)
if mibBuilder.loadTexts:
    tMirrorRadiusLiTable.setStatus("current")
_TMirrorRadiusLiEntry_Object = MibTableRow
tMirrorRadiusLiEntry = _TMirrorRadiusLiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1)
)
tMirrorRadiusLiEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tRadiusLiMirrorDestinationIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tRadiusLiSrcHostServiceId"),
    (0, "TIMETRA-MIRROR-MIB", "tRadiusLiSrcHostSapPortId"),
    (0, "TIMETRA-MIRROR-MIB", "tRadiusLiSrcHostsapEncapValue"),
    (0, "TIMETRA-MIRROR-MIB", "tRadiusLiSrcHostIpAddrType"),
    (0, "TIMETRA-MIRROR-MIB", "tRadiusLiSrcHostIpAddr"),
    (0, "TIMETRA-MIRROR-MIB", "tRadiusLiSrcHostMacAddr"),
    (0, "TIMETRA-MIRROR-MIB", "tRadiusLiSrcHostPppoeSessionId"),
)
if mibBuilder.loadTexts:
    tMirrorRadiusLiEntry.setStatus("current")
_TRadiusLiMirrorDestinationIndex_Type = TmnxServId
_TRadiusLiMirrorDestinationIndex_Object = MibTableColumn
tRadiusLiMirrorDestinationIndex = _TRadiusLiMirrorDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 1),
    _TRadiusLiMirrorDestinationIndex_Type()
)
tRadiusLiMirrorDestinationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRadiusLiMirrorDestinationIndex.setStatus("current")
_TRadiusLiSrcHostServiceId_Type = TmnxServId
_TRadiusLiSrcHostServiceId_Object = MibTableColumn
tRadiusLiSrcHostServiceId = _TRadiusLiSrcHostServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 2),
    _TRadiusLiSrcHostServiceId_Type()
)
tRadiusLiSrcHostServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRadiusLiSrcHostServiceId.setStatus("current")
_TRadiusLiSrcHostSapPortId_Type = TmnxPortID
_TRadiusLiSrcHostSapPortId_Object = MibTableColumn
tRadiusLiSrcHostSapPortId = _TRadiusLiSrcHostSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 3),
    _TRadiusLiSrcHostSapPortId_Type()
)
tRadiusLiSrcHostSapPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRadiusLiSrcHostSapPortId.setStatus("current")
_TRadiusLiSrcHostsapEncapValue_Type = TmnxEncapVal
_TRadiusLiSrcHostsapEncapValue_Object = MibTableColumn
tRadiusLiSrcHostsapEncapValue = _TRadiusLiSrcHostsapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 4),
    _TRadiusLiSrcHostsapEncapValue_Type()
)
tRadiusLiSrcHostsapEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRadiusLiSrcHostsapEncapValue.setStatus("current")
_TRadiusLiSrcHostIpAddrType_Type = InetAddressType
_TRadiusLiSrcHostIpAddrType_Object = MibTableColumn
tRadiusLiSrcHostIpAddrType = _TRadiusLiSrcHostIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 5),
    _TRadiusLiSrcHostIpAddrType_Type()
)
tRadiusLiSrcHostIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRadiusLiSrcHostIpAddrType.setStatus("current")


class _TRadiusLiSrcHostIpAddr_Type(InetAddress):
    """Custom type tRadiusLiSrcHostIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TRadiusLiSrcHostIpAddr_Type.__name__ = "InetAddress"
_TRadiusLiSrcHostIpAddr_Object = MibTableColumn
tRadiusLiSrcHostIpAddr = _TRadiusLiSrcHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 6),
    _TRadiusLiSrcHostIpAddr_Type()
)
tRadiusLiSrcHostIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRadiusLiSrcHostIpAddr.setStatus("current")
_TRadiusLiSrcHostMacAddr_Type = MacAddress
_TRadiusLiSrcHostMacAddr_Object = MibTableColumn
tRadiusLiSrcHostMacAddr = _TRadiusLiSrcHostMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 7),
    _TRadiusLiSrcHostMacAddr_Type()
)
tRadiusLiSrcHostMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRadiusLiSrcHostMacAddr.setStatus("current")
_TRadiusLiSrcHostPppoeSessionId_Type = TmnxPppoeSessionId
_TRadiusLiSrcHostPppoeSessionId_Object = MibTableColumn
tRadiusLiSrcHostPppoeSessionId = _TRadiusLiSrcHostPppoeSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 8),
    _TRadiusLiSrcHostPppoeSessionId_Type()
)
tRadiusLiSrcHostPppoeSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRadiusLiSrcHostPppoeSessionId.setStatus("current")
_TRadiusLiSrcHostId_Type = TSubHostId
_TRadiusLiSrcHostId_Object = MibTableColumn
tRadiusLiSrcHostId = _TRadiusLiSrcHostId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 9),
    _TRadiusLiSrcHostId_Type()
)
tRadiusLiSrcHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRadiusLiSrcHostId.setStatus("current")
_TRadiusLiMirrorDirection_Type = TDirection
_TRadiusLiMirrorDirection_Object = MibTableColumn
tRadiusLiMirrorDirection = _TRadiusLiMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 10),
    _TRadiusLiMirrorDirection_Type()
)
tRadiusLiMirrorDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRadiusLiMirrorDirection.setStatus("current")
_TRadiusLiMirrorForwClassMap_Type = TFCSet
_TRadiusLiMirrorForwClassMap_Object = MibTableColumn
tRadiusLiMirrorForwClassMap = _TRadiusLiMirrorForwClassMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 11),
    _TRadiusLiMirrorForwClassMap_Type()
)
tRadiusLiMirrorForwClassMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRadiusLiMirrorForwClassMap.setStatus("current")
_TRadiusLiSrcIntceptId_Type = TmnxInterceptionIdentifier
_TRadiusLiSrcIntceptId_Object = MibTableColumn
tRadiusLiSrcIntceptId = _TRadiusLiSrcIntceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 12),
    _TRadiusLiSrcIntceptId_Type()
)
tRadiusLiSrcIntceptId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRadiusLiSrcIntceptId.setStatus("current")
_TRadiusLiSrcSessionId_Type = Unsigned32
_TRadiusLiSrcSessionId_Object = MibTableColumn
tRadiusLiSrcSessionId = _TRadiusLiSrcSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 13),
    _TRadiusLiSrcSessionId_Type()
)
tRadiusLiSrcSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRadiusLiSrcSessionId.setStatus("current")
_TRadiusLiSrcNatUsingOutsideIp_Type = TruthValue
_TRadiusLiSrcNatUsingOutsideIp_Object = MibTableColumn
tRadiusLiSrcNatUsingOutsideIp = _TRadiusLiSrcNatUsingOutsideIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 1, 1, 14),
    _TRadiusLiSrcNatUsingOutsideIp_Type()
)
tRadiusLiSrcNatUsingOutsideIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRadiusLiSrcNatUsingOutsideIp.setStatus("current")
_TMirrorLiDestTmplTable_Object = MibTable
tMirrorLiDestTmplTable = _TMirrorLiDestTmplTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4)
)
if mibBuilder.loadTexts:
    tMirrorLiDestTmplTable.setStatus("current")
_TMirrorLiDestTmplEntry_Object = MibTableRow
tMirrorLiDestTmplEntry = _TMirrorLiDestTmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1)
)
tMirrorLiDestTmplEntry.setIndexNames(
    (1, "TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplName"),
)
if mibBuilder.loadTexts:
    tMirrorLiDestTmplEntry.setStatus("current")
_TMirrorLiDestTmplName_Type = TNamedItem
_TMirrorLiDestTmplName_Object = MibTableColumn
tMirrorLiDestTmplName = _TMirrorLiDestTmplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1, 1),
    _TMirrorLiDestTmplName_Type()
)
tMirrorLiDestTmplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplName.setStatus("current")
_TMirrorLiDestTmplLastChanged_Type = TimeStamp
_TMirrorLiDestTmplLastChanged_Object = MibTableColumn
tMirrorLiDestTmplLastChanged = _TMirrorLiDestTmplLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1, 2),
    _TMirrorLiDestTmplLastChanged_Type()
)
tMirrorLiDestTmplLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplLastChanged.setStatus("current")
_TMirrorLiDestTmplRowStatus_Type = RowStatus
_TMirrorLiDestTmplRowStatus_Object = MibTableColumn
tMirrorLiDestTmplRowStatus = _TMirrorLiDestTmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1, 3),
    _TMirrorLiDestTmplRowStatus_Type()
)
tMirrorLiDestTmplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplRowStatus.setStatus("current")


class _TMirrorLiDestTmplEncapsulation_Type(TmnxMirrorEncapType):
    """Custom type tMirrorLiDestTmplEncapsulation based on TmnxMirrorEncapType"""
    defaultValue = 1


_TMirrorLiDestTmplEncapsulation_Type.__name__ = "TmnxMirrorEncapType"
_TMirrorLiDestTmplEncapsulation_Object = MibTableColumn
tMirrorLiDestTmplEncapsulation = _TMirrorLiDestTmplEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1, 4),
    _TMirrorLiDestTmplEncapsulation_Type()
)
tMirrorLiDestTmplEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplEncapsulation.setStatus("current")


class _TMirrorLiDestTmplL3EncHeaderType_Type(TmnxMirrorDestinationHeaderType):
    """Custom type tMirrorLiDestTmplL3EncHeaderType based on TmnxMirrorDestinationHeaderType"""
    defaultValue = 1


_TMirrorLiDestTmplL3EncHeaderType_Type.__name__ = "TmnxMirrorDestinationHeaderType"
_TMirrorLiDestTmplL3EncHeaderType_Object = MibTableColumn
tMirrorLiDestTmplL3EncHeaderType = _TMirrorLiDestTmplL3EncHeaderType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1, 5),
    _TMirrorLiDestTmplL3EncHeaderType_Type()
)
tMirrorLiDestTmplL3EncHeaderType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplL3EncHeaderType.setStatus("current")


class _TMirrorLiDestTmplL3EncUseDirect_Type(TruthValue):
    """Custom type tMirrorLiDestTmplL3EncUseDirect based on TruthValue"""
    defaultValue = 2


_TMirrorLiDestTmplL3EncUseDirect_Type.__name__ = "TruthValue"
_TMirrorLiDestTmplL3EncUseDirect_Object = MibTableColumn
tMirrorLiDestTmplL3EncUseDirect = _TMirrorLiDestTmplL3EncUseDirect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1, 6),
    _TMirrorLiDestTmplL3EncUseDirect_Type()
)
tMirrorLiDestTmplL3EncUseDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplL3EncUseDirect.setStatus("current")


class _TMirrorLiDestTmplL3EncRouter_Type(TmnxVRtrID):
    """Custom type tMirrorLiDestTmplL3EncRouter based on TmnxVRtrID"""
    defaultValue = 1


_TMirrorLiDestTmplL3EncRouter_Type.__name__ = "TmnxVRtrID"
_TMirrorLiDestTmplL3EncRouter_Object = MibTableColumn
tMirrorLiDestTmplL3EncRouter = _TMirrorLiDestTmplL3EncRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1, 7),
    _TMirrorLiDestTmplL3EncRouter_Type()
)
tMirrorLiDestTmplL3EncRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplL3EncRouter.setStatus("current")


class _TMirrorLiDestTmplL3SrcAddrType_Type(InetAddressType):
    """Custom type tMirrorLiDestTmplL3SrcAddrType based on InetAddressType"""
    defaultValue = 0


_TMirrorLiDestTmplL3SrcAddrType_Type.__name__ = "InetAddressType"
_TMirrorLiDestTmplL3SrcAddrType_Object = MibTableColumn
tMirrorLiDestTmplL3SrcAddrType = _TMirrorLiDestTmplL3SrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1, 8),
    _TMirrorLiDestTmplL3SrcAddrType_Type()
)
tMirrorLiDestTmplL3SrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplL3SrcAddrType.setStatus("current")


class _TMirrorLiDestTmplL3SrcAddr_Type(InetAddress):
    """Custom type tMirrorLiDestTmplL3SrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TMirrorLiDestTmplL3SrcAddr_Type.__name__ = "InetAddress"
_TMirrorLiDestTmplL3SrcAddr_Object = MibTableColumn
tMirrorLiDestTmplL3SrcAddr = _TMirrorLiDestTmplL3SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1, 9),
    _TMirrorLiDestTmplL3SrcAddr_Type()
)
tMirrorLiDestTmplL3SrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplL3SrcAddr.setStatus("current")


class _TMirrorLiDestTmplL3UdpSrcPort_Type(InetPortNumber):
    """Custom type tMirrorLiDestTmplL3UdpSrcPort based on InetPortNumber"""
    defaultValue = 0


_TMirrorLiDestTmplL3UdpSrcPort_Type.__name__ = "InetPortNumber"
_TMirrorLiDestTmplL3UdpSrcPort_Object = MibTableColumn
tMirrorLiDestTmplL3UdpSrcPort = _TMirrorLiDestTmplL3UdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1, 10),
    _TMirrorLiDestTmplL3UdpSrcPort_Type()
)
tMirrorLiDestTmplL3UdpSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplL3UdpSrcPort.setStatus("current")


class _TMirrorLiDestTmplL3UdpDstPort_Type(InetPortNumber):
    """Custom type tMirrorLiDestTmplL3UdpDstPort based on InetPortNumber"""
    defaultValue = 0


_TMirrorLiDestTmplL3UdpDstPort_Type.__name__ = "InetPortNumber"
_TMirrorLiDestTmplL3UdpDstPort_Object = MibTableColumn
tMirrorLiDestTmplL3UdpDstPort = _TMirrorLiDestTmplL3UdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1, 11),
    _TMirrorLiDestTmplL3UdpDstPort_Type()
)
tMirrorLiDestTmplL3UdpDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplL3UdpDstPort.setStatus("current")


class _TMirrorLiDestTmplL3EncRouterName_Type(TLNamedItemOrEmpty):
    """Custom type tMirrorLiDestTmplL3EncRouterName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("Base")


_TMirrorLiDestTmplL3EncRouterName_Type.__name__ = "TLNamedItemOrEmpty"
_TMirrorLiDestTmplL3EncRouterName_Object = MibTableColumn
tMirrorLiDestTmplL3EncRouterName = _TMirrorLiDestTmplL3EncRouterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 4, 1, 12),
    _TMirrorLiDestTmplL3EncRouterName_Type()
)
tMirrorLiDestTmplL3EncRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplL3EncRouterName.setStatus("current")
_TMirrorLiDestServiceRange_ObjectIdentity = ObjectIdentity
tMirrorLiDestServiceRange = _TMirrorLiDestServiceRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 5)
)


class _TMirrorLiDestServiceRangeStart_Type(TmnxServId):
    """Custom type tMirrorLiDestServiceRangeStart based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_TMirrorLiDestServiceRangeStart_Type.__name__ = "TmnxServId"
_TMirrorLiDestServiceRangeStart_Object = MibScalar
tMirrorLiDestServiceRangeStart = _TMirrorLiDestServiceRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 5, 1),
    _TMirrorLiDestServiceRangeStart_Type()
)
tMirrorLiDestServiceRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMirrorLiDestServiceRangeStart.setStatus("current")


class _TMirrorLiDestServiceRangeEnd_Type(TmnxServId):
    """Custom type tMirrorLiDestServiceRangeEnd based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_TMirrorLiDestServiceRangeEnd_Type.__name__ = "TmnxServId"
_TMirrorLiDestServiceRangeEnd_Object = MibScalar
tMirrorLiDestServiceRangeEnd = _TMirrorLiDestServiceRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 5, 2),
    _TMirrorLiDestServiceRangeEnd_Type()
)
tMirrorLiDestServiceRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMirrorLiDestServiceRangeEnd.setStatus("current")
_TMirrorRadiusLiCfg_ObjectIdentity = ObjectIdentity
tMirrorRadiusLiCfg = _TMirrorRadiusLiCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 6)
)


class _TMirrorRadiusLiCfgDestTmpl_Type(TNamedItemOrEmpty):
    """Custom type tMirrorRadiusLiCfgDestTmpl based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TMirrorRadiusLiCfgDestTmpl_Type.__name__ = "TNamedItemOrEmpty"
_TMirrorRadiusLiCfgDestTmpl_Object = MibScalar
tMirrorRadiusLiCfgDestTmpl = _TMirrorRadiusLiCfgDestTmpl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 4, 6, 1),
    _TMirrorRadiusLiCfgDestTmpl_Type()
)
tMirrorRadiusLiCfgDestTmpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMirrorRadiusLiCfgDestTmpl.setStatus("current")
_TMirrorLiObjects_ObjectIdentity = ObjectIdentity
tMirrorLiObjects = _TMirrorLiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5)
)
_TMirrorLiSourceNatTableLastCh_Type = TimeStamp
_TMirrorLiSourceNatTableLastCh_Object = MibScalar
tMirrorLiSourceNatTableLastCh = _TMirrorLiSourceNatTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 1),
    _TMirrorLiSourceNatTableLastCh_Type()
)
tMirrorLiSourceNatTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiSourceNatTableLastCh.setStatus("current")
_TMirrorLiNatLsnSubTableLastCh_Type = TimeStamp
_TMirrorLiNatLsnSubTableLastCh_Object = MibScalar
tMirrorLiNatLsnSubTableLastCh = _TMirrorLiNatLsnSubTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 2),
    _TMirrorLiNatLsnSubTableLastCh_Type()
)
tMirrorLiNatLsnSubTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSubTableLastCh.setStatus("current")
_TMirrorLiNatL2awSubTableLastCh_Type = TimeStamp
_TMirrorLiNatL2awSubTableLastCh_Object = MibScalar
tMirrorLiNatL2awSubTableLastCh = _TMirrorLiNatL2awSubTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 3),
    _TMirrorLiNatL2awSubTableLastCh_Type()
)
tMirrorLiNatL2awSubTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNatL2awSubTableLastCh.setStatus("current")
_TMirrorSourceLiMacFltrTableLstCh_Type = TimeStamp
_TMirrorSourceLiMacFltrTableLstCh_Object = MibScalar
tMirrorSourceLiMacFltrTableLstCh = _TMirrorSourceLiMacFltrTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 4),
    _TMirrorSourceLiMacFltrTableLstCh_Type()
)
tMirrorSourceLiMacFltrTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceLiMacFltrTableLstCh.setStatus("current")
_TMirrorLiNat64SubTableLastCh_Type = TimeStamp
_TMirrorLiNat64SubTableLastCh_Object = MibScalar
tMirrorLiNat64SubTableLastCh = _TMirrorLiNat64SubTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 5),
    _TMirrorLiNat64SubTableLastCh_Type()
)
tMirrorLiNat64SubTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNat64SubTableLastCh.setStatus("current")
_TMirrorSourceLiIpFltrTableLstCh_Type = TimeStamp
_TMirrorSourceLiIpFltrTableLstCh_Object = MibScalar
tMirrorSourceLiIpFltrTableLstCh = _TMirrorSourceLiIpFltrTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 6),
    _TMirrorSourceLiIpFltrTableLstCh_Type()
)
tMirrorSourceLiIpFltrTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceLiIpFltrTableLstCh.setStatus("current")
_TMirrorLiDsmSubTableLastCh_Type = TimeStamp
_TMirrorLiDsmSubTableLastCh_Object = MibScalar
tMirrorLiDsmSubTableLastCh = _TMirrorLiDsmSubTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 7),
    _TMirrorLiDsmSubTableLastCh_Type()
)
tMirrorLiDsmSubTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiDsmSubTableLastCh.setStatus("current")
_TMirrorLiDestTmplTableLastCh_Type = TimeStamp
_TMirrorLiDestTmplTableLastCh_Object = MibScalar
tMirrorLiDestTmplTableLastCh = _TMirrorLiDestTmplTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 30),
    _TMirrorLiDestTmplTableLastCh_Type()
)
tMirrorLiDestTmplTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiDestTmplTableLastCh.setStatus("current")
_TMirrorLiSourceNatTable_Object = MibTable
tMirrorLiSourceNatTable = _TMirrorLiSourceNatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 100)
)
if mibBuilder.loadTexts:
    tMirrorLiSourceNatTable.setStatus("current")
_TMirrorLiSourceNatEntry_Object = MibTableRow
tMirrorLiSourceNatEntry = _TMirrorLiSourceNatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 100, 1)
)
tMirrorLiSourceNatEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
)
if mibBuilder.loadTexts:
    tMirrorLiSourceNatEntry.setStatus("current")
_TMirrorLiSourceNatLastChanged_Type = TimeStamp
_TMirrorLiSourceNatLastChanged_Object = MibTableColumn
tMirrorLiSourceNatLastChanged = _TMirrorLiSourceNatLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 100, 1, 2),
    _TMirrorLiSourceNatLastChanged_Type()
)
tMirrorLiSourceNatLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiSourceNatLastChanged.setStatus("current")
_TMirrorLiSourceNatDestMacAddr_Type = MacAddress
_TMirrorLiSourceNatDestMacAddr_Object = MibTableColumn
tMirrorLiSourceNatDestMacAddr = _TMirrorLiSourceNatDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 100, 1, 3),
    _TMirrorLiSourceNatDestMacAddr_Type()
)
tMirrorLiSourceNatDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiSourceNatDestMacAddr.setStatus("current")
_TMirrorLiSourceNatSrcMacAddr_Type = MacAddress
_TMirrorLiSourceNatSrcMacAddr_Object = MibTableColumn
tMirrorLiSourceNatSrcMacAddr = _TMirrorLiSourceNatSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 100, 1, 4),
    _TMirrorLiSourceNatSrcMacAddr_Type()
)
tMirrorLiSourceNatSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiSourceNatSrcMacAddr.setStatus("current")


class _TMirrorLiSourceNatEthertype_Type(TEtherType):
    """Custom type tMirrorLiSourceNatEthertype based on TEtherType"""
    defaultValue = 1792


_TMirrorLiSourceNatEthertype_Type.__name__ = "TEtherType"
_TMirrorLiSourceNatEthertype_Object = MibTableColumn
tMirrorLiSourceNatEthertype = _TMirrorLiSourceNatEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 100, 1, 5),
    _TMirrorLiSourceNatEthertype_Type()
)
tMirrorLiSourceNatEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiSourceNatEthertype.setStatus("current")
_TMirrorLiNatLsnSubTable_Object = MibTable
tMirrorLiNatLsnSubTable = _TMirrorLiNatLsnSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 101)
)
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSubTable.setStatus("current")
_TMirrorLiNatLsnSubEntry_Object = MibTableRow
tMirrorLiNatLsnSubEntry = _TMirrorLiNatLsnSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 101, 1)
)
tMirrorLiNatLsnSubEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSubAddrType"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSubAddr"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSubPrefixLength"),
)
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSubEntry.setStatus("current")
_TMirrorLiNatLsnSubAddrType_Type = InetAddressType
_TMirrorLiNatLsnSubAddrType_Object = MibTableColumn
tMirrorLiNatLsnSubAddrType = _TMirrorLiNatLsnSubAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 101, 1, 1),
    _TMirrorLiNatLsnSubAddrType_Type()
)
tMirrorLiNatLsnSubAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSubAddrType.setStatus("current")


class _TMirrorLiNatLsnSubAddr_Type(InetAddress):
    """Custom type tMirrorLiNatLsnSubAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TMirrorLiNatLsnSubAddr_Type.__name__ = "InetAddress"
_TMirrorLiNatLsnSubAddr_Object = MibTableColumn
tMirrorLiNatLsnSubAddr = _TMirrorLiNatLsnSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 101, 1, 2),
    _TMirrorLiNatLsnSubAddr_Type()
)
tMirrorLiNatLsnSubAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSubAddr.setStatus("current")


class _TMirrorLiNatLsnSubPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tMirrorLiNatLsnSubPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TMirrorLiNatLsnSubPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TMirrorLiNatLsnSubPrefixLength_Object = MibTableColumn
tMirrorLiNatLsnSubPrefixLength = _TMirrorLiNatLsnSubPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 101, 1, 3),
    _TMirrorLiNatLsnSubPrefixLength_Type()
)
tMirrorLiNatLsnSubPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSubPrefixLength.setStatus("current")
_TMirrorLiNatLsnSubRowStatus_Type = RowStatus
_TMirrorLiNatLsnSubRowStatus_Object = MibTableColumn
tMirrorLiNatLsnSubRowStatus = _TMirrorLiNatLsnSubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 101, 1, 4),
    _TMirrorLiNatLsnSubRowStatus_Type()
)
tMirrorLiNatLsnSubRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSubRowStatus.setStatus("current")
_TMirrorLiNatLsnSubLastChanged_Type = TimeStamp
_TMirrorLiNatLsnSubLastChanged_Object = MibTableColumn
tMirrorLiNatLsnSubLastChanged = _TMirrorLiNatLsnSubLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 101, 1, 5),
    _TMirrorLiNatLsnSubLastChanged_Type()
)
tMirrorLiNatLsnSubLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSubLastChanged.setStatus("current")


class _TMirrorLiNatLsnSubInterceptId_Type(Unsigned32):
    """Custom type tMirrorLiNatLsnSubInterceptId based on Unsigned32"""
    defaultValue = 0


_TMirrorLiNatLsnSubInterceptId_Type.__name__ = "Unsigned32"
_TMirrorLiNatLsnSubInterceptId_Object = MibTableColumn
tMirrorLiNatLsnSubInterceptId = _TMirrorLiNatLsnSubInterceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 101, 1, 6),
    _TMirrorLiNatLsnSubInterceptId_Type()
)
tMirrorLiNatLsnSubInterceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSubInterceptId.setStatus("current")


class _TMirrorLiNatLsnSubSessionId_Type(Unsigned32):
    """Custom type tMirrorLiNatLsnSubSessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorLiNatLsnSubSessionId_Type.__name__ = "Unsigned32"
_TMirrorLiNatLsnSubSessionId_Object = MibTableColumn
tMirrorLiNatLsnSubSessionId = _TMirrorLiNatLsnSubSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 101, 1, 7),
    _TMirrorLiNatLsnSubSessionId_Type()
)
tMirrorLiNatLsnSubSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSubSessionId.setStatus("current")
_TMirrorLiNatLsnSubOperState_Type = ServiceOperStatus
_TMirrorLiNatLsnSubOperState_Object = MibTableColumn
tMirrorLiNatLsnSubOperState = _TMirrorLiNatLsnSubOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 101, 1, 8),
    _TMirrorLiNatLsnSubOperState_Type()
)
tMirrorLiNatLsnSubOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSubOperState.setStatus("current")
_TMirrorLiNatL2awSubTable_Object = MibTable
tMirrorLiNatL2awSubTable = _TMirrorLiNatL2awSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 102)
)
if mibBuilder.loadTexts:
    tMirrorLiNatL2awSubTable.setStatus("current")
_TMirrorLiNatL2awSubEntry_Object = MibTableRow
tMirrorLiNatL2awSubEntry = _TMirrorLiNatL2awSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 102, 1)
)
tMirrorLiNatL2awSubEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNatL2awSubIdent"),
)
if mibBuilder.loadTexts:
    tMirrorLiNatL2awSubEntry.setStatus("current")
_TMirrorLiNatL2awSubIdent_Type = TmnxSubIdentString
_TMirrorLiNatL2awSubIdent_Object = MibTableColumn
tMirrorLiNatL2awSubIdent = _TMirrorLiNatL2awSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 102, 1, 1),
    _TMirrorLiNatL2awSubIdent_Type()
)
tMirrorLiNatL2awSubIdent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNatL2awSubIdent.setStatus("current")
_TMirrorLiNatL2awSubRowStatus_Type = RowStatus
_TMirrorLiNatL2awSubRowStatus_Object = MibTableColumn
tMirrorLiNatL2awSubRowStatus = _TMirrorLiNatL2awSubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 102, 1, 2),
    _TMirrorLiNatL2awSubRowStatus_Type()
)
tMirrorLiNatL2awSubRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNatL2awSubRowStatus.setStatus("current")
_TMirrorLiNatL2awSubLastChanged_Type = TimeStamp
_TMirrorLiNatL2awSubLastChanged_Object = MibTableColumn
tMirrorLiNatL2awSubLastChanged = _TMirrorLiNatL2awSubLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 102, 1, 3),
    _TMirrorLiNatL2awSubLastChanged_Type()
)
tMirrorLiNatL2awSubLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNatL2awSubLastChanged.setStatus("current")


class _TMirrorLiNatL2awSubInterceptId_Type(Unsigned32):
    """Custom type tMirrorLiNatL2awSubInterceptId based on Unsigned32"""
    defaultValue = 0


_TMirrorLiNatL2awSubInterceptId_Type.__name__ = "Unsigned32"
_TMirrorLiNatL2awSubInterceptId_Object = MibTableColumn
tMirrorLiNatL2awSubInterceptId = _TMirrorLiNatL2awSubInterceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 102, 1, 4),
    _TMirrorLiNatL2awSubInterceptId_Type()
)
tMirrorLiNatL2awSubInterceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNatL2awSubInterceptId.setStatus("current")


class _TMirrorLiNatL2awSubSessionId_Type(Unsigned32):
    """Custom type tMirrorLiNatL2awSubSessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorLiNatL2awSubSessionId_Type.__name__ = "Unsigned32"
_TMirrorLiNatL2awSubSessionId_Object = MibTableColumn
tMirrorLiNatL2awSubSessionId = _TMirrorLiNatL2awSubSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 102, 1, 5),
    _TMirrorLiNatL2awSubSessionId_Type()
)
tMirrorLiNatL2awSubSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNatL2awSubSessionId.setStatus("current")
_TMirrorLiNatL2awSubOperState_Type = ServiceOperStatus
_TMirrorLiNatL2awSubOperState_Object = MibTableColumn
tMirrorLiNatL2awSubOperState = _TMirrorLiNatL2awSubOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 102, 1, 6),
    _TMirrorLiNatL2awSubOperState_Type()
)
tMirrorLiNatL2awSubOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNatL2awSubOperState.setStatus("current")
_TMirrorSourceLiMacFltrTable_Object = MibTable
tMirrorSourceLiMacFltrTable = _TMirrorSourceLiMacFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 103)
)
if mibBuilder.loadTexts:
    tMirrorSourceLiMacFltrTable.setStatus("current")
_TMirrorSourceLiMacFltrEntry_Object = MibTableRow
tMirrorSourceLiMacFltrEntry = _TMirrorSourceLiMacFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 103, 1)
)
tMirrorSourceLiMacFltrEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceLiMacFltr"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceLiMacFltrParams"),
)
if mibBuilder.loadTexts:
    tMirrorSourceLiMacFltrEntry.setStatus("current")
_TMirrorSourceLiMacFltr_Type = TNamedItem
_TMirrorSourceLiMacFltr_Object = MibTableColumn
tMirrorSourceLiMacFltr = _TMirrorSourceLiMacFltr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 103, 1, 1),
    _TMirrorSourceLiMacFltr_Type()
)
tMirrorSourceLiMacFltr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceLiMacFltr.setStatus("current")
_TMirrorSourceLiMacFltrParams_Type = TLimitedEntryId
_TMirrorSourceLiMacFltrParams_Object = MibTableColumn
tMirrorSourceLiMacFltrParams = _TMirrorSourceLiMacFltrParams_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 103, 1, 2),
    _TMirrorSourceLiMacFltrParams_Type()
)
tMirrorSourceLiMacFltrParams.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceLiMacFltrParams.setStatus("current")
_TMirrorSourceLiMacFltrRowStatus_Type = RowStatus
_TMirrorSourceLiMacFltrRowStatus_Object = MibTableColumn
tMirrorSourceLiMacFltrRowStatus = _TMirrorSourceLiMacFltrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 103, 1, 3),
    _TMirrorSourceLiMacFltrRowStatus_Type()
)
tMirrorSourceLiMacFltrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceLiMacFltrRowStatus.setStatus("current")
_TMirrorSourceLiMacFltrLastChgd_Type = TimeStamp
_TMirrorSourceLiMacFltrLastChgd_Object = MibTableColumn
tMirrorSourceLiMacFltrLastChgd = _TMirrorSourceLiMacFltrLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 103, 1, 4),
    _TMirrorSourceLiMacFltrLastChgd_Type()
)
tMirrorSourceLiMacFltrLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceLiMacFltrLastChgd.setStatus("current")


class _TMirrorSourceLiMacFltrIntceptId_Type(TmnxInterceptionIdentifier):
    """Custom type tMirrorSourceLiMacFltrIntceptId based on TmnxInterceptionIdentifier"""
    defaultValue = 0


_TMirrorSourceLiMacFltrIntceptId_Type.__name__ = "TmnxInterceptionIdentifier"
_TMirrorSourceLiMacFltrIntceptId_Object = MibTableColumn
tMirrorSourceLiMacFltrIntceptId = _TMirrorSourceLiMacFltrIntceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 103, 1, 5),
    _TMirrorSourceLiMacFltrIntceptId_Type()
)
tMirrorSourceLiMacFltrIntceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceLiMacFltrIntceptId.setStatus("current")


class _TMirrorSourceLiMacFltrSessionId_Type(Unsigned32):
    """Custom type tMirrorSourceLiMacFltrSessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorSourceLiMacFltrSessionId_Type.__name__ = "Unsigned32"
_TMirrorSourceLiMacFltrSessionId_Object = MibTableColumn
tMirrorSourceLiMacFltrSessionId = _TMirrorSourceLiMacFltrSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 103, 1, 6),
    _TMirrorSourceLiMacFltrSessionId_Type()
)
tMirrorSourceLiMacFltrSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceLiMacFltrSessionId.setStatus("current")
_TMirrorLiNat64SubTable_Object = MibTable
tMirrorLiNat64SubTable = _TMirrorLiNat64SubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 104)
)
if mibBuilder.loadTexts:
    tMirrorLiNat64SubTable.setStatus("current")
_TMirrorLiNat64SubEntry_Object = MibTableRow
tMirrorLiNat64SubEntry = _TMirrorLiNat64SubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 104, 1)
)
tMirrorLiNat64SubEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubAddrType"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubAddr"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubPrefixLength"),
)
if mibBuilder.loadTexts:
    tMirrorLiNat64SubEntry.setStatus("current")
_TMirrorLiNat64SubAddrType_Type = InetAddressType
_TMirrorLiNat64SubAddrType_Object = MibTableColumn
tMirrorLiNat64SubAddrType = _TMirrorLiNat64SubAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 104, 1, 1),
    _TMirrorLiNat64SubAddrType_Type()
)
tMirrorLiNat64SubAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNat64SubAddrType.setStatus("current")


class _TMirrorLiNat64SubAddr_Type(InetAddress):
    """Custom type tMirrorLiNat64SubAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TMirrorLiNat64SubAddr_Type.__name__ = "InetAddress"
_TMirrorLiNat64SubAddr_Object = MibTableColumn
tMirrorLiNat64SubAddr = _TMirrorLiNat64SubAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 104, 1, 2),
    _TMirrorLiNat64SubAddr_Type()
)
tMirrorLiNat64SubAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNat64SubAddr.setStatus("current")


class _TMirrorLiNat64SubPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tMirrorLiNat64SubPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TMirrorLiNat64SubPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TMirrorLiNat64SubPrefixLength_Object = MibTableColumn
tMirrorLiNat64SubPrefixLength = _TMirrorLiNat64SubPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 104, 1, 3),
    _TMirrorLiNat64SubPrefixLength_Type()
)
tMirrorLiNat64SubPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNat64SubPrefixLength.setStatus("current")
_TMirrorLiNat64SubRowStatus_Type = RowStatus
_TMirrorLiNat64SubRowStatus_Object = MibTableColumn
tMirrorLiNat64SubRowStatus = _TMirrorLiNat64SubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 104, 1, 4),
    _TMirrorLiNat64SubRowStatus_Type()
)
tMirrorLiNat64SubRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNat64SubRowStatus.setStatus("current")
_TMirrorLiNat64SubLastChanged_Type = TimeStamp
_TMirrorLiNat64SubLastChanged_Object = MibTableColumn
tMirrorLiNat64SubLastChanged = _TMirrorLiNat64SubLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 104, 1, 5),
    _TMirrorLiNat64SubLastChanged_Type()
)
tMirrorLiNat64SubLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNat64SubLastChanged.setStatus("current")


class _TMirrorLiNat64SubInterceptId_Type(Unsigned32):
    """Custom type tMirrorLiNat64SubInterceptId based on Unsigned32"""
    defaultValue = 0


_TMirrorLiNat64SubInterceptId_Type.__name__ = "Unsigned32"
_TMirrorLiNat64SubInterceptId_Object = MibTableColumn
tMirrorLiNat64SubInterceptId = _TMirrorLiNat64SubInterceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 104, 1, 6),
    _TMirrorLiNat64SubInterceptId_Type()
)
tMirrorLiNat64SubInterceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNat64SubInterceptId.setStatus("current")


class _TMirrorLiNat64SubSessionId_Type(Unsigned32):
    """Custom type tMirrorLiNat64SubSessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorLiNat64SubSessionId_Type.__name__ = "Unsigned32"
_TMirrorLiNat64SubSessionId_Object = MibTableColumn
tMirrorLiNat64SubSessionId = _TMirrorLiNat64SubSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 104, 1, 7),
    _TMirrorLiNat64SubSessionId_Type()
)
tMirrorLiNat64SubSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNat64SubSessionId.setStatus("current")
_TMirrorLiNat64SubOperState_Type = ServiceOperStatus
_TMirrorLiNat64SubOperState_Object = MibTableColumn
tMirrorLiNat64SubOperState = _TMirrorLiNat64SubOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 104, 1, 8),
    _TMirrorLiNat64SubOperState_Type()
)
tMirrorLiNat64SubOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNat64SubOperState.setStatus("current")
_TMirrorLiNatLsnSub2TableLastCh_Type = TimeStamp
_TMirrorLiNatLsnSub2TableLastCh_Object = MibScalar
tMirrorLiNatLsnSub2TableLastCh = _TMirrorLiNatLsnSub2TableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 105),
    _TMirrorLiNatLsnSub2TableLastCh_Type()
)
tMirrorLiNatLsnSub2TableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSub2TableLastCh.setStatus("current")
_TMirrorLiNatLsnSub2Table_Object = MibTable
tMirrorLiNatLsnSub2Table = _TMirrorLiNatLsnSub2Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 106)
)
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSub2Table.setStatus("current")
_TMirrorLiNatLsnSub2Entry_Object = MibTableRow
tMirrorLiNatLsnSub2Entry = _TMirrorLiNatLsnSub2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 106, 1)
)
tMirrorLiNatLsnSub2Entry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSub2RouterName"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSub2AddrType"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSub2Addr"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSub2PrefixLength"),
)
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSub2Entry.setStatus("current")
_TMirrorLiNatLsnSub2RouterName_Type = TLNamedItem
_TMirrorLiNatLsnSub2RouterName_Object = MibTableColumn
tMirrorLiNatLsnSub2RouterName = _TMirrorLiNatLsnSub2RouterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 106, 1, 1),
    _TMirrorLiNatLsnSub2RouterName_Type()
)
tMirrorLiNatLsnSub2RouterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSub2RouterName.setStatus("current")
_TMirrorLiNatLsnSub2AddrType_Type = InetAddressType
_TMirrorLiNatLsnSub2AddrType_Object = MibTableColumn
tMirrorLiNatLsnSub2AddrType = _TMirrorLiNatLsnSub2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 106, 1, 2),
    _TMirrorLiNatLsnSub2AddrType_Type()
)
tMirrorLiNatLsnSub2AddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSub2AddrType.setStatus("current")


class _TMirrorLiNatLsnSub2Addr_Type(InetAddress):
    """Custom type tMirrorLiNatLsnSub2Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TMirrorLiNatLsnSub2Addr_Type.__name__ = "InetAddress"
_TMirrorLiNatLsnSub2Addr_Object = MibTableColumn
tMirrorLiNatLsnSub2Addr = _TMirrorLiNatLsnSub2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 106, 1, 3),
    _TMirrorLiNatLsnSub2Addr_Type()
)
tMirrorLiNatLsnSub2Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSub2Addr.setStatus("current")


class _TMirrorLiNatLsnSub2PrefixLength_Type(InetAddressPrefixLength):
    """Custom type tMirrorLiNatLsnSub2PrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TMirrorLiNatLsnSub2PrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TMirrorLiNatLsnSub2PrefixLength_Object = MibTableColumn
tMirrorLiNatLsnSub2PrefixLength = _TMirrorLiNatLsnSub2PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 106, 1, 4),
    _TMirrorLiNatLsnSub2PrefixLength_Type()
)
tMirrorLiNatLsnSub2PrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSub2PrefixLength.setStatus("current")
_TMirrorLiNatLsnSub2RowStatus_Type = RowStatus
_TMirrorLiNatLsnSub2RowStatus_Object = MibTableColumn
tMirrorLiNatLsnSub2RowStatus = _TMirrorLiNatLsnSub2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 106, 1, 5),
    _TMirrorLiNatLsnSub2RowStatus_Type()
)
tMirrorLiNatLsnSub2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSub2RowStatus.setStatus("current")
_TMirrorLiNatLsnSub2LastChanged_Type = TimeStamp
_TMirrorLiNatLsnSub2LastChanged_Object = MibTableColumn
tMirrorLiNatLsnSub2LastChanged = _TMirrorLiNatLsnSub2LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 106, 1, 6),
    _TMirrorLiNatLsnSub2LastChanged_Type()
)
tMirrorLiNatLsnSub2LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSub2LastChanged.setStatus("current")


class _TMirrorLiNatLsnSub2InterceptId_Type(Unsigned32):
    """Custom type tMirrorLiNatLsnSub2InterceptId based on Unsigned32"""
    defaultValue = 0


_TMirrorLiNatLsnSub2InterceptId_Type.__name__ = "Unsigned32"
_TMirrorLiNatLsnSub2InterceptId_Object = MibTableColumn
tMirrorLiNatLsnSub2InterceptId = _TMirrorLiNatLsnSub2InterceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 106, 1, 7),
    _TMirrorLiNatLsnSub2InterceptId_Type()
)
tMirrorLiNatLsnSub2InterceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSub2InterceptId.setStatus("current")


class _TMirrorLiNatLsnSub2SessionId_Type(Unsigned32):
    """Custom type tMirrorLiNatLsnSub2SessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorLiNatLsnSub2SessionId_Type.__name__ = "Unsigned32"
_TMirrorLiNatLsnSub2SessionId_Object = MibTableColumn
tMirrorLiNatLsnSub2SessionId = _TMirrorLiNatLsnSub2SessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 106, 1, 8),
    _TMirrorLiNatLsnSub2SessionId_Type()
)
tMirrorLiNatLsnSub2SessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSub2SessionId.setStatus("current")
_TMirrorLiNatLsnSub2OperState_Type = ServiceOperStatus
_TMirrorLiNatLsnSub2OperState_Object = MibTableColumn
tMirrorLiNatLsnSub2OperState = _TMirrorLiNatLsnSub2OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 106, 1, 9),
    _TMirrorLiNatLsnSub2OperState_Type()
)
tMirrorLiNatLsnSub2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSub2OperState.setStatus("current")
_TMirrorLiNat64Sub2TableLastCh_Type = TimeStamp
_TMirrorLiNat64Sub2TableLastCh_Object = MibScalar
tMirrorLiNat64Sub2TableLastCh = _TMirrorLiNat64Sub2TableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 107),
    _TMirrorLiNat64Sub2TableLastCh_Type()
)
tMirrorLiNat64Sub2TableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNat64Sub2TableLastCh.setStatus("current")
_TMirrorLiNat64Sub2Table_Object = MibTable
tMirrorLiNat64Sub2Table = _TMirrorLiNat64Sub2Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 108)
)
if mibBuilder.loadTexts:
    tMirrorLiNat64Sub2Table.setStatus("current")
_TMirrorLiNat64Sub2Entry_Object = MibTableRow
tMirrorLiNat64Sub2Entry = _TMirrorLiNat64Sub2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 108, 1)
)
tMirrorLiNat64Sub2Entry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNat64Sub2RouterName"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNat64Sub2AddrType"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNat64Sub2Addr"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiNat64Sub2PrefixLength"),
)
if mibBuilder.loadTexts:
    tMirrorLiNat64Sub2Entry.setStatus("current")
_TMirrorLiNat64Sub2RouterName_Type = TLNamedItem
_TMirrorLiNat64Sub2RouterName_Object = MibTableColumn
tMirrorLiNat64Sub2RouterName = _TMirrorLiNat64Sub2RouterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 108, 1, 1),
    _TMirrorLiNat64Sub2RouterName_Type()
)
tMirrorLiNat64Sub2RouterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNat64Sub2RouterName.setStatus("current")
_TMirrorLiNat64Sub2AddrType_Type = InetAddressType
_TMirrorLiNat64Sub2AddrType_Object = MibTableColumn
tMirrorLiNat64Sub2AddrType = _TMirrorLiNat64Sub2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 108, 1, 2),
    _TMirrorLiNat64Sub2AddrType_Type()
)
tMirrorLiNat64Sub2AddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNat64Sub2AddrType.setStatus("current")


class _TMirrorLiNat64Sub2Addr_Type(InetAddress):
    """Custom type tMirrorLiNat64Sub2Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TMirrorLiNat64Sub2Addr_Type.__name__ = "InetAddress"
_TMirrorLiNat64Sub2Addr_Object = MibTableColumn
tMirrorLiNat64Sub2Addr = _TMirrorLiNat64Sub2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 108, 1, 3),
    _TMirrorLiNat64Sub2Addr_Type()
)
tMirrorLiNat64Sub2Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNat64Sub2Addr.setStatus("current")


class _TMirrorLiNat64Sub2PrefixLength_Type(InetAddressPrefixLength):
    """Custom type tMirrorLiNat64Sub2PrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TMirrorLiNat64Sub2PrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TMirrorLiNat64Sub2PrefixLength_Object = MibTableColumn
tMirrorLiNat64Sub2PrefixLength = _TMirrorLiNat64Sub2PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 108, 1, 4),
    _TMirrorLiNat64Sub2PrefixLength_Type()
)
tMirrorLiNat64Sub2PrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiNat64Sub2PrefixLength.setStatus("current")
_TMirrorLiNat64Sub2RowStatus_Type = RowStatus
_TMirrorLiNat64Sub2RowStatus_Object = MibTableColumn
tMirrorLiNat64Sub2RowStatus = _TMirrorLiNat64Sub2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 108, 1, 5),
    _TMirrorLiNat64Sub2RowStatus_Type()
)
tMirrorLiNat64Sub2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNat64Sub2RowStatus.setStatus("current")
_TMirrorLiNat64Sub2LastChanged_Type = TimeStamp
_TMirrorLiNat64Sub2LastChanged_Object = MibTableColumn
tMirrorLiNat64Sub2LastChanged = _TMirrorLiNat64Sub2LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 108, 1, 6),
    _TMirrorLiNat64Sub2LastChanged_Type()
)
tMirrorLiNat64Sub2LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNat64Sub2LastChanged.setStatus("current")


class _TMirrorLiNat64Sub2InterceptId_Type(Unsigned32):
    """Custom type tMirrorLiNat64Sub2InterceptId based on Unsigned32"""
    defaultValue = 0


_TMirrorLiNat64Sub2InterceptId_Type.__name__ = "Unsigned32"
_TMirrorLiNat64Sub2InterceptId_Object = MibTableColumn
tMirrorLiNat64Sub2InterceptId = _TMirrorLiNat64Sub2InterceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 108, 1, 7),
    _TMirrorLiNat64Sub2InterceptId_Type()
)
tMirrorLiNat64Sub2InterceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNat64Sub2InterceptId.setStatus("current")


class _TMirrorLiNat64Sub2SessionId_Type(Unsigned32):
    """Custom type tMirrorLiNat64Sub2SessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorLiNat64Sub2SessionId_Type.__name__ = "Unsigned32"
_TMirrorLiNat64Sub2SessionId_Object = MibTableColumn
tMirrorLiNat64Sub2SessionId = _TMirrorLiNat64Sub2SessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 108, 1, 8),
    _TMirrorLiNat64Sub2SessionId_Type()
)
tMirrorLiNat64Sub2SessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiNat64Sub2SessionId.setStatus("current")
_TMirrorLiNat64Sub2OperState_Type = ServiceOperStatus
_TMirrorLiNat64Sub2OperState_Object = MibTableColumn
tMirrorLiNat64Sub2OperState = _TMirrorLiNat64Sub2OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 108, 1, 9),
    _TMirrorLiNat64Sub2OperState_Type()
)
tMirrorLiNat64Sub2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiNat64Sub2OperState.setStatus("current")
_TMirrorSourceLiIpFltrTable_Object = MibTable
tMirrorSourceLiIpFltrTable = _TMirrorSourceLiIpFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 151)
)
if mibBuilder.loadTexts:
    tMirrorSourceLiIpFltrTable.setStatus("current")
_TMirrorSourceLiIpFltrEntry_Object = MibTableRow
tMirrorSourceLiIpFltrEntry = _TMirrorSourceLiIpFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 151, 1)
)
tMirrorSourceLiIpFltrEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceLiIpFltrType"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceLiIpFltr"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceLiIpFltrParams"),
)
if mibBuilder.loadTexts:
    tMirrorSourceLiIpFltrEntry.setStatus("current")
_TMirrorSourceLiIpFltrType_Type = TFilterType
_TMirrorSourceLiIpFltrType_Object = MibTableColumn
tMirrorSourceLiIpFltrType = _TMirrorSourceLiIpFltrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 151, 1, 1),
    _TMirrorSourceLiIpFltrType_Type()
)
tMirrorSourceLiIpFltrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceLiIpFltrType.setStatus("current")
_TMirrorSourceLiIpFltr_Type = TNamedItem
_TMirrorSourceLiIpFltr_Object = MibTableColumn
tMirrorSourceLiIpFltr = _TMirrorSourceLiIpFltr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 151, 1, 2),
    _TMirrorSourceLiIpFltr_Type()
)
tMirrorSourceLiIpFltr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceLiIpFltr.setStatus("current")
_TMirrorSourceLiIpFltrParams_Type = TLimitedEntryId
_TMirrorSourceLiIpFltrParams_Object = MibTableColumn
tMirrorSourceLiIpFltrParams = _TMirrorSourceLiIpFltrParams_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 151, 1, 3),
    _TMirrorSourceLiIpFltrParams_Type()
)
tMirrorSourceLiIpFltrParams.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorSourceLiIpFltrParams.setStatus("current")
_TMirrorSourceLiIpFltrRowStatus_Type = RowStatus
_TMirrorSourceLiIpFltrRowStatus_Object = MibTableColumn
tMirrorSourceLiIpFltrRowStatus = _TMirrorSourceLiIpFltrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 151, 1, 4),
    _TMirrorSourceLiIpFltrRowStatus_Type()
)
tMirrorSourceLiIpFltrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceLiIpFltrRowStatus.setStatus("current")
_TMirrorSourceLiIpFltrLastChgd_Type = TimeStamp
_TMirrorSourceLiIpFltrLastChgd_Object = MibTableColumn
tMirrorSourceLiIpFltrLastChgd = _TMirrorSourceLiIpFltrLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 151, 1, 5),
    _TMirrorSourceLiIpFltrLastChgd_Type()
)
tMirrorSourceLiIpFltrLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorSourceLiIpFltrLastChgd.setStatus("current")


class _TMirrorSourceLiIpFltrIntceptId_Type(TmnxInterceptionIdentifier):
    """Custom type tMirrorSourceLiIpFltrIntceptId based on TmnxInterceptionIdentifier"""
    defaultValue = 0


_TMirrorSourceLiIpFltrIntceptId_Type.__name__ = "TmnxInterceptionIdentifier"
_TMirrorSourceLiIpFltrIntceptId_Object = MibTableColumn
tMirrorSourceLiIpFltrIntceptId = _TMirrorSourceLiIpFltrIntceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 151, 1, 6),
    _TMirrorSourceLiIpFltrIntceptId_Type()
)
tMirrorSourceLiIpFltrIntceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceLiIpFltrIntceptId.setStatus("current")


class _TMirrorSourceLiIpFltrSessionId_Type(Unsigned32):
    """Custom type tMirrorSourceLiIpFltrSessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorSourceLiIpFltrSessionId_Type.__name__ = "Unsigned32"
_TMirrorSourceLiIpFltrSessionId_Object = MibTableColumn
tMirrorSourceLiIpFltrSessionId = _TMirrorSourceLiIpFltrSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 151, 1, 7),
    _TMirrorSourceLiIpFltrSessionId_Type()
)
tMirrorSourceLiIpFltrSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorSourceLiIpFltrSessionId.setStatus("current")
_TMirrorLiDsmSubTable_Object = MibTable
tMirrorLiDsmSubTable = _TMirrorLiDsmSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 152)
)
if mibBuilder.loadTexts:
    tMirrorLiDsmSubTable.setStatus("current")
_TMirrorLiDsmSubEntry_Object = MibTableRow
tMirrorLiDsmSubEntry = _TMirrorLiDsmSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 152, 1)
)
tMirrorLiDsmSubEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiDsmSubMacAddress"),
)
if mibBuilder.loadTexts:
    tMirrorLiDsmSubEntry.setStatus("current")
_TMirrorLiDsmSubMacAddress_Type = MacAddress
_TMirrorLiDsmSubMacAddress_Object = MibTableColumn
tMirrorLiDsmSubMacAddress = _TMirrorLiDsmSubMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 152, 1, 1),
    _TMirrorLiDsmSubMacAddress_Type()
)
tMirrorLiDsmSubMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiDsmSubMacAddress.setStatus("current")
_TMirrorLiDsmSubRowStatus_Type = RowStatus
_TMirrorLiDsmSubRowStatus_Object = MibTableColumn
tMirrorLiDsmSubRowStatus = _TMirrorLiDsmSubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 152, 1, 2),
    _TMirrorLiDsmSubRowStatus_Type()
)
tMirrorLiDsmSubRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDsmSubRowStatus.setStatus("current")
_TMirrorLiDsmSubLastChanged_Type = TimeStamp
_TMirrorLiDsmSubLastChanged_Object = MibTableColumn
tMirrorLiDsmSubLastChanged = _TMirrorLiDsmSubLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 152, 1, 3),
    _TMirrorLiDsmSubLastChanged_Type()
)
tMirrorLiDsmSubLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiDsmSubLastChanged.setStatus("current")


class _TMirrorLiDsmSubInterceptId_Type(Unsigned32):
    """Custom type tMirrorLiDsmSubInterceptId based on Unsigned32"""
    defaultValue = 0


_TMirrorLiDsmSubInterceptId_Type.__name__ = "Unsigned32"
_TMirrorLiDsmSubInterceptId_Object = MibTableColumn
tMirrorLiDsmSubInterceptId = _TMirrorLiDsmSubInterceptId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 152, 1, 4),
    _TMirrorLiDsmSubInterceptId_Type()
)
tMirrorLiDsmSubInterceptId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDsmSubInterceptId.setStatus("current")


class _TMirrorLiDsmSubSessionId_Type(Unsigned32):
    """Custom type tMirrorLiDsmSubSessionId based on Unsigned32"""
    defaultValue = 0


_TMirrorLiDsmSubSessionId_Type.__name__ = "Unsigned32"
_TMirrorLiDsmSubSessionId_Object = MibTableColumn
tMirrorLiDsmSubSessionId = _TMirrorLiDsmSubSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 152, 1, 5),
    _TMirrorLiDsmSubSessionId_Type()
)
tMirrorLiDsmSubSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiDsmSubSessionId.setStatus("current")
_TMirrorLiCfg_ObjectIdentity = ObjectIdentity
tMirrorLiCfg = _TMirrorLiCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 300)
)


class _TMirrorLiCfgNatUseOutsideIpAddr_Type(TruthValue):
    """Custom type tMirrorLiCfgNatUseOutsideIpAddr based on TruthValue"""
    defaultValue = 2


_TMirrorLiCfgNatUseOutsideIpAddr_Type.__name__ = "TruthValue"
_TMirrorLiCfgNatUseOutsideIpAddr_Object = MibScalar
tMirrorLiCfgNatUseOutsideIpAddr = _TMirrorLiCfgNatUseOutsideIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 300, 1),
    _TMirrorLiCfgNatUseOutsideIpAddr_Type()
)
tMirrorLiCfgNatUseOutsideIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMirrorLiCfgNatUseOutsideIpAddr.setStatus("current")


class _TMirrorLiCfgXIfTgtPersistFileLoc_Type(Unsigned32):
    """Custom type tMirrorLiCfgXIfTgtPersistFileLoc based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TMirrorLiCfgXIfTgtPersistFileLoc_Type.__name__ = "Unsigned32"
_TMirrorLiCfgXIfTgtPersistFileLoc_Object = MibScalar
tMirrorLiCfgXIfTgtPersistFileLoc = _TMirrorLiCfgXIfTgtPersistFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 300, 2),
    _TMirrorLiCfgXIfTgtPersistFileLoc_Type()
)
tMirrorLiCfgXIfTgtPersistFileLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMirrorLiCfgXIfTgtPersistFileLoc.setStatus("current")
_TMirrorLiXIf_ObjectIdentity = ObjectIdentity
tMirrorLiXIf = _TMirrorLiXIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301)
)
_TMirrorLicTableLastCh_Type = TimeStamp
_TMirrorLicTableLastCh_Object = MibScalar
tMirrorLicTableLastCh = _TMirrorLicTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 1),
    _TMirrorLicTableLastCh_Type()
)
tMirrorLicTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLicTableLastCh.setStatus("current")
_TMirrorLicTable_Object = MibTable
tMirrorLicTable = _TMirrorLicTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2)
)
if mibBuilder.loadTexts:
    tMirrorLicTable.setStatus("current")
_TMirrorLicEntry_Object = MibTableRow
tMirrorLicEntry = _TMirrorLicEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1)
)
tMirrorLicEntry.setIndexNames(
    (1, "TIMETRA-MIRROR-MIB", "tMirrorLicName"),
)
if mibBuilder.loadTexts:
    tMirrorLicEntry.setStatus("current")
_TMirrorLicName_Type = TNamedItem
_TMirrorLicName_Object = MibTableColumn
tMirrorLicName = _TMirrorLicName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1, 1),
    _TMirrorLicName_Type()
)
tMirrorLicName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLicName.setStatus("current")
_TMirrorLicLastChanged_Type = TimeStamp
_TMirrorLicLastChanged_Object = MibTableColumn
tMirrorLicLastChanged = _TMirrorLicLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1, 2),
    _TMirrorLicLastChanged_Type()
)
tMirrorLicLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLicLastChanged.setStatus("current")
_TMirrorLicRowStatus_Type = RowStatus
_TMirrorLicRowStatus_Object = MibTableColumn
tMirrorLicRowStatus = _TMirrorLicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1, 3),
    _TMirrorLicRowStatus_Type()
)
tMirrorLicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLicRowStatus.setStatus("current")


class _TMirrorLicDescription_Type(TItemDescription):
    """Custom type tMirrorLicDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TMirrorLicDescription_Type.__name__ = "TItemDescription"
_TMirrorLicDescription_Object = MibTableColumn
tMirrorLicDescription = _TMirrorLicDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1, 4),
    _TMirrorLicDescription_Type()
)
tMirrorLicDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLicDescription.setStatus("current")


class _TMirrorLicIdentifier_Type(TNamedItemOrEmpty):
    """Custom type tMirrorLicIdentifier based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TMirrorLicIdentifier_Type.__name__ = "TNamedItemOrEmpty"
_TMirrorLicIdentifier_Object = MibTableColumn
tMirrorLicIdentifier = _TMirrorLicIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1, 5),
    _TMirrorLicIdentifier_Type()
)
tMirrorLicIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLicIdentifier.setStatus("current")


class _TMirrorLicRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tMirrorLicRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TMirrorLicRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TMirrorLicRouter_Object = MibTableColumn
tMirrorLicRouter = _TMirrorLicRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1, 6),
    _TMirrorLicRouter_Type()
)
tMirrorLicRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLicRouter.setStatus("current")


class _TMirrorLicIpAddrType_Type(InetAddressType):
    """Custom type tMirrorLicIpAddrType based on InetAddressType"""
    defaultValue = 0


_TMirrorLicIpAddrType_Type.__name__ = "InetAddressType"
_TMirrorLicIpAddrType_Object = MibTableColumn
tMirrorLicIpAddrType = _TMirrorLicIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1, 7),
    _TMirrorLicIpAddrType_Type()
)
tMirrorLicIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLicIpAddrType.setStatus("current")


class _TMirrorLicIpAddr_Type(InetAddress):
    """Custom type tMirrorLicIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TMirrorLicIpAddr_Type.__name__ = "InetAddress"
_TMirrorLicIpAddr_Object = MibTableColumn
tMirrorLicIpAddr = _TMirrorLicIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1, 8),
    _TMirrorLicIpAddr_Type()
)
tMirrorLicIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLicIpAddr.setStatus("current")


class _TMirrorLicPort_Type(Unsigned32):
    """Custom type tMirrorLicPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TMirrorLicPort_Type.__name__ = "Unsigned32"
_TMirrorLicPort_Object = MibTableColumn
tMirrorLicPort = _TMirrorLicPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1, 9),
    _TMirrorLicPort_Type()
)
tMirrorLicPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLicPort.setStatus("current")


class _TMirrorLicAuthPrivateKi_Type(OctetString):
    """Custom type tMirrorLicAuthPrivateKi based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TMirrorLicAuthPrivateKi_Type.__name__ = "OctetString"
_TMirrorLicAuthPrivateKi_Object = MibTableColumn
tMirrorLicAuthPrivateKi = _TMirrorLicAuthPrivateKi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1, 10),
    _TMirrorLicAuthPrivateKi_Type()
)
tMirrorLicAuthPrivateKi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLicAuthPrivateKi.setStatus("current")


class _TMirrorLicAuthPassword_Type(OctetString):
    """Custom type tMirrorLicAuthPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TMirrorLicAuthPassword_Type.__name__ = "OctetString"
_TMirrorLicAuthPassword_Object = MibTableColumn
tMirrorLicAuthPassword = _TMirrorLicAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1, 11),
    _TMirrorLicAuthPassword_Type()
)
tMirrorLicAuthPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLicAuthPassword.setStatus("current")


class _TMirrorLicAuthSequenceGroup_Type(Unsigned32):
    """Custom type tMirrorLicAuthSequenceGroup based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4294967295),
    )


_TMirrorLicAuthSequenceGroup_Type.__name__ = "Unsigned32"
_TMirrorLicAuthSequenceGroup_Object = MibTableColumn
tMirrorLicAuthSequenceGroup = _TMirrorLicAuthSequenceGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 2, 1, 12),
    _TMirrorLicAuthSequenceGroup_Type()
)
tMirrorLicAuthSequenceGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLicAuthSequenceGroup.setStatus("current")


class _TMirrorIneIdentifier_Type(TNamedItemOrEmpty):
    """Custom type tMirrorIneIdentifier based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TMirrorIneIdentifier_Type.__name__ = "TNamedItemOrEmpty"
_TMirrorIneIdentifier_Object = MibScalar
tMirrorIneIdentifier = _TMirrorIneIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 3),
    _TMirrorIneIdentifier_Type()
)
tMirrorIneIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMirrorIneIdentifier.setStatus("current")


class _TMirrorLiXIfAdminState_Type(TmnxAdminState):
    """Custom type tMirrorLiXIfAdminState based on TmnxAdminState"""
    defaultValue = 3


_TMirrorLiXIfAdminState_Type.__name__ = "TmnxAdminState"
_TMirrorLiXIfAdminState_Object = MibScalar
tMirrorLiXIfAdminState = _TMirrorLiXIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 4),
    _TMirrorLiXIfAdminState_Type()
)
tMirrorLiXIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMirrorLiXIfAdminState.setStatus("current")


class _TMirrorLiXIfUserDb_Type(TNamedItemOrEmpty):
    """Custom type tMirrorLiXIfUserDb based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TMirrorLiXIfUserDb_Type.__name__ = "TNamedItemOrEmpty"
_TMirrorLiXIfUserDb_Object = MibScalar
tMirrorLiXIfUserDb = _TMirrorLiXIfUserDb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 5),
    _TMirrorLiXIfUserDb_Type()
)
tMirrorLiXIfUserDb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMirrorLiXIfUserDb.setStatus("current")


class _TMirrorLiXIfCorrelationIdIpoe_Type(TmnxMirrorLiXIfCorrelationIdOrg):
    """Custom type tMirrorLiXIfCorrelationIdIpoe based on TmnxMirrorLiXIfCorrelationIdOrg"""
    defaultValue = 1


_TMirrorLiXIfCorrelationIdIpoe_Type.__name__ = "TmnxMirrorLiXIfCorrelationIdOrg"
_TMirrorLiXIfCorrelationIdIpoe_Object = MibScalar
tMirrorLiXIfCorrelationIdIpoe = _TMirrorLiXIfCorrelationIdIpoe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 6),
    _TMirrorLiXIfCorrelationIdIpoe_Type()
)
tMirrorLiXIfCorrelationIdIpoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMirrorLiXIfCorrelationIdIpoe.setStatus("current")


class _TMirrorLiXIfCorrelationIdPppoe_Type(TmnxMirrorLiXIfCorrelationIdOrg):
    """Custom type tMirrorLiXIfCorrelationIdPppoe based on TmnxMirrorLiXIfCorrelationIdOrg"""
    defaultValue = 1


_TMirrorLiXIfCorrelationIdPppoe_Type.__name__ = "TmnxMirrorLiXIfCorrelationIdOrg"
_TMirrorLiXIfCorrelationIdPppoe_Object = MibScalar
tMirrorLiXIfCorrelationIdPppoe = _TMirrorLiXIfCorrelationIdPppoe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 7),
    _TMirrorLiXIfCorrelationIdPppoe_Type()
)
tMirrorLiXIfCorrelationIdPppoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMirrorLiXIfCorrelationIdPppoe.setStatus("current")
_TMirrorLiX1_ObjectIdentity = ObjectIdentity
tMirrorLiX1 = _TMirrorLiX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 101)
)
_TMirrorLiX1LastCh_Type = TimeStamp
_TMirrorLiX1LastCh_Object = MibScalar
tMirrorLiX1LastCh = _TMirrorLiX1LastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 101, 1),
    _TMirrorLiX1LastCh_Type()
)
tMirrorLiX1LastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX1LastCh.setStatus("current")


class _TMirrorLiX1PeerLic_Type(TNamedItemOrEmpty):
    """Custom type tMirrorLiX1PeerLic based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TMirrorLiX1PeerLic_Type.__name__ = "TNamedItemOrEmpty"
_TMirrorLiX1PeerLic_Object = MibScalar
tMirrorLiX1PeerLic = _TMirrorLiX1PeerLic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 101, 2),
    _TMirrorLiX1PeerLic_Type()
)
tMirrorLiX1PeerLic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMirrorLiX1PeerLic.setStatus("current")


class _TMirrorLiX1IpAddrType_Type(InetAddressType):
    """Custom type tMirrorLiX1IpAddrType based on InetAddressType"""
    defaultValue = 0


_TMirrorLiX1IpAddrType_Type.__name__ = "InetAddressType"
_TMirrorLiX1IpAddrType_Object = MibScalar
tMirrorLiX1IpAddrType = _TMirrorLiX1IpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 101, 3),
    _TMirrorLiX1IpAddrType_Type()
)
tMirrorLiX1IpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX1IpAddrType.setStatus("current")


class _TMirrorLiX1IpAddr_Type(InetAddress):
    """Custom type tMirrorLiX1IpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TMirrorLiX1IpAddr_Type.__name__ = "InetAddress"
_TMirrorLiX1IpAddr_Object = MibScalar
tMirrorLiX1IpAddr = _TMirrorLiX1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 101, 4),
    _TMirrorLiX1IpAddr_Type()
)
tMirrorLiX1IpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX1IpAddr.setStatus("current")


class _TMirrorLiX1Port_Type(Unsigned32):
    """Custom type tMirrorLiX1Port based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TMirrorLiX1Port_Type.__name__ = "Unsigned32"
_TMirrorLiX1Port_Object = MibScalar
tMirrorLiX1Port = _TMirrorLiX1Port_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 101, 5),
    _TMirrorLiX1Port_Type()
)
tMirrorLiX1Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX1Port.setStatus("current")


class _TMirrorLiX1ToNoMsg_Type(Unsigned32):
    """Custom type tMirrorLiX1ToNoMsg based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 300),
    )


_TMirrorLiX1ToNoMsg_Type.__name__ = "Unsigned32"
_TMirrorLiX1ToNoMsg_Object = MibScalar
tMirrorLiX1ToNoMsg = _TMirrorLiX1ToNoMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 101, 6),
    _TMirrorLiX1ToNoMsg_Type()
)
tMirrorLiX1ToNoMsg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX1ToNoMsg.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX1ToNoMsg.setUnits("seconds")


class _TMirrorLiX1OperState_Type(Integer32):
    """Custom type tMirrorLiX1OperState based on Integer32"""
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
        *(("inService", 2),
          ("outOfService", 3),
          ("transition", 4),
          ("waitPersistence", 5))
    )


_TMirrorLiX1OperState_Type.__name__ = "Integer32"
_TMirrorLiX1OperState_Object = MibScalar
tMirrorLiX1OperState = _TMirrorLiX1OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 101, 21),
    _TMirrorLiX1OperState_Type()
)
tMirrorLiX1OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX1OperState.setStatus("current")
_TMirrorLiX2_ObjectIdentity = ObjectIdentity
tMirrorLiX2 = _TMirrorLiX2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 102)
)
_TMirrorLiX2LastCh_Type = TimeStamp
_TMirrorLiX2LastCh_Object = MibScalar
tMirrorLiX2LastCh = _TMirrorLiX2LastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 102, 1),
    _TMirrorLiX2LastCh_Type()
)
tMirrorLiX2LastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX2LastCh.setStatus("current")


class _TMirrorLiX2PeerLic_Type(TNamedItemOrEmpty):
    """Custom type tMirrorLiX2PeerLic based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TMirrorLiX2PeerLic_Type.__name__ = "TNamedItemOrEmpty"
_TMirrorLiX2PeerLic_Object = MibScalar
tMirrorLiX2PeerLic = _TMirrorLiX2PeerLic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 102, 2),
    _TMirrorLiX2PeerLic_Type()
)
tMirrorLiX2PeerLic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMirrorLiX2PeerLic.setStatus("current")


class _TMirrorLiX2IpAddrType_Type(InetAddressType):
    """Custom type tMirrorLiX2IpAddrType based on InetAddressType"""
    defaultValue = 0


_TMirrorLiX2IpAddrType_Type.__name__ = "InetAddressType"
_TMirrorLiX2IpAddrType_Object = MibScalar
tMirrorLiX2IpAddrType = _TMirrorLiX2IpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 102, 3),
    _TMirrorLiX2IpAddrType_Type()
)
tMirrorLiX2IpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX2IpAddrType.setStatus("current")


class _TMirrorLiX2IpAddr_Type(InetAddress):
    """Custom type tMirrorLiX2IpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TMirrorLiX2IpAddr_Type.__name__ = "InetAddress"
_TMirrorLiX2IpAddr_Object = MibScalar
tMirrorLiX2IpAddr = _TMirrorLiX2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 102, 4),
    _TMirrorLiX2IpAddr_Type()
)
tMirrorLiX2IpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX2IpAddr.setStatus("current")


class _TMirrorLiX2ToConnectionReq_Type(Unsigned32):
    """Custom type tMirrorLiX2ToConnectionReq based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_TMirrorLiX2ToConnectionReq_Type.__name__ = "Unsigned32"
_TMirrorLiX2ToConnectionReq_Object = MibScalar
tMirrorLiX2ToConnectionReq = _TMirrorLiX2ToConnectionReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 102, 5),
    _TMirrorLiX2ToConnectionReq_Type()
)
tMirrorLiX2ToConnectionReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX2ToConnectionReq.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX2ToConnectionReq.setUnits("seconds")


class _TMirrorLiX2ToKeepalive_Type(Unsigned32):
    """Custom type tMirrorLiX2ToKeepalive based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 600),
    )


_TMirrorLiX2ToKeepalive_Type.__name__ = "Unsigned32"
_TMirrorLiX2ToKeepalive_Object = MibScalar
tMirrorLiX2ToKeepalive = _TMirrorLiX2ToKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 102, 6),
    _TMirrorLiX2ToKeepalive_Type()
)
tMirrorLiX2ToKeepalive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX2ToKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX2ToKeepalive.setUnits("seconds")


class _TMirrorLiX2OperState_Type(Integer32):
    """Custom type tMirrorLiX2OperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("outOfService", 3),
          ("transition", 4))
    )


_TMirrorLiX2OperState_Type.__name__ = "Integer32"
_TMirrorLiX2OperState_Object = MibScalar
tMirrorLiX2OperState = _TMirrorLiX2OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 102, 21),
    _TMirrorLiX2OperState_Type()
)
tMirrorLiX2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX2OperState.setStatus("current")
_TMirrorLiX3_ObjectIdentity = ObjectIdentity
tMirrorLiX3 = _TMirrorLiX3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103)
)
_TMirrorLiX3LastCh_Type = TimeStamp
_TMirrorLiX3LastCh_Object = MibScalar
tMirrorLiX3LastCh = _TMirrorLiX3LastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 1),
    _TMirrorLiX3LastCh_Type()
)
tMirrorLiX3LastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX3LastCh.setStatus("current")


class _TMirrorLiX3LiGroup_Type(TmnxIsaBbGrpId):
    """Custom type tMirrorLiX3LiGroup based on TmnxIsaBbGrpId"""
    defaultValue = 0


_TMirrorLiX3LiGroup_Type.__name__ = "TmnxIsaBbGrpId"
_TMirrorLiX3LiGroup_Object = MibScalar
tMirrorLiX3LiGroup = _TMirrorLiX3LiGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 2),
    _TMirrorLiX3LiGroup_Type()
)
tMirrorLiX3LiGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3LiGroup.setStatus("current")


class _TMirrorLiX3StartIpAddrType_Type(InetAddressType):
    """Custom type tMirrorLiX3StartIpAddrType based on InetAddressType"""
    defaultValue = 0


_TMirrorLiX3StartIpAddrType_Type.__name__ = "InetAddressType"
_TMirrorLiX3StartIpAddrType_Object = MibScalar
tMirrorLiX3StartIpAddrType = _TMirrorLiX3StartIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 3),
    _TMirrorLiX3StartIpAddrType_Type()
)
tMirrorLiX3StartIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3StartIpAddrType.setStatus("current")


class _TMirrorLiX3StartIpAddr_Type(InetAddress):
    """Custom type tMirrorLiX3StartIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TMirrorLiX3StartIpAddr_Type.__name__ = "InetAddress"
_TMirrorLiX3StartIpAddr_Object = MibScalar
tMirrorLiX3StartIpAddr = _TMirrorLiX3StartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 4),
    _TMirrorLiX3StartIpAddr_Type()
)
tMirrorLiX3StartIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3StartIpAddr.setStatus("current")


class _TMirrorLiX3EndIpAddrType_Type(InetAddressType):
    """Custom type tMirrorLiX3EndIpAddrType based on InetAddressType"""
    defaultValue = 0


_TMirrorLiX3EndIpAddrType_Type.__name__ = "InetAddressType"
_TMirrorLiX3EndIpAddrType_Object = MibScalar
tMirrorLiX3EndIpAddrType = _TMirrorLiX3EndIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 5),
    _TMirrorLiX3EndIpAddrType_Type()
)
tMirrorLiX3EndIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3EndIpAddrType.setStatus("current")


class _TMirrorLiX3EndIpAddr_Type(InetAddress):
    """Custom type tMirrorLiX3EndIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TMirrorLiX3EndIpAddr_Type.__name__ = "InetAddress"
_TMirrorLiX3EndIpAddr_Object = MibScalar
tMirrorLiX3EndIpAddr = _TMirrorLiX3EndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 6),
    _TMirrorLiX3EndIpAddr_Type()
)
tMirrorLiX3EndIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3EndIpAddr.setStatus("current")


class _TMirrorLiX3MaxNumSessions_Type(Unsigned32):
    """Custom type tMirrorLiX3MaxNumSessions based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TMirrorLiX3MaxNumSessions_Type.__name__ = "Unsigned32"
_TMirrorLiX3MaxNumSessions_Object = MibScalar
tMirrorLiX3MaxNumSessions = _TMirrorLiX3MaxNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 7),
    _TMirrorLiX3MaxNumSessions_Type()
)
tMirrorLiX3MaxNumSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3MaxNumSessions.setStatus("current")


class _TMirrorLiX3ToTunnelReq_Type(Unsigned32):
    """Custom type tMirrorLiX3ToTunnelReq based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_TMirrorLiX3ToTunnelReq_Type.__name__ = "Unsigned32"
_TMirrorLiX3ToTunnelReq_Object = MibScalar
tMirrorLiX3ToTunnelReq = _TMirrorLiX3ToTunnelReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 10),
    _TMirrorLiX3ToTunnelReq_Type()
)
tMirrorLiX3ToTunnelReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3ToTunnelReq.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX3ToTunnelReq.setUnits("seconds")


class _TMirrorLiX3ToKeepalive_Type(Unsigned32):
    """Custom type tMirrorLiX3ToKeepalive based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 600),
    )


_TMirrorLiX3ToKeepalive_Type.__name__ = "Unsigned32"
_TMirrorLiX3ToKeepalive_Object = MibScalar
tMirrorLiX3ToKeepalive = _TMirrorLiX3ToKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 11),
    _TMirrorLiX3ToKeepalive_Type()
)
tMirrorLiX3ToKeepalive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3ToKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX3ToKeepalive.setUnits("seconds")


class _TMirrorLiX3ToTargetRetryWait_Type(Unsigned32):
    """Custom type tMirrorLiX3ToTargetRetryWait based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1200),
    )


_TMirrorLiX3ToTargetRetryWait_Type.__name__ = "Unsigned32"
_TMirrorLiX3ToTargetRetryWait_Object = MibScalar
tMirrorLiX3ToTargetRetryWait = _TMirrorLiX3ToTargetRetryWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 12),
    _TMirrorLiX3ToTargetRetryWait_Type()
)
tMirrorLiX3ToTargetRetryWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3ToTargetRetryWait.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX3ToTargetRetryWait.setUnits("seconds")


class _TMirrorLiX3CpuAlarm_Type(TruthValue):
    """Custom type tMirrorLiX3CpuAlarm based on TruthValue"""
    defaultValue = 2


_TMirrorLiX3CpuAlarm_Type.__name__ = "TruthValue"
_TMirrorLiX3CpuAlarm_Object = MibScalar
tMirrorLiX3CpuAlarm = _TMirrorLiX3CpuAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 13),
    _TMirrorLiX3CpuAlarm_Type()
)
tMirrorLiX3CpuAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3CpuAlarm.setStatus("current")


class _TMirrorLiX3CpuAlarmHighThreshold_Type(Unsigned32):
    """Custom type tMirrorLiX3CpuAlarmHighThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TMirrorLiX3CpuAlarmHighThreshold_Type.__name__ = "Unsigned32"
_TMirrorLiX3CpuAlarmHighThreshold_Object = MibScalar
tMirrorLiX3CpuAlarmHighThreshold = _TMirrorLiX3CpuAlarmHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 14),
    _TMirrorLiX3CpuAlarmHighThreshold_Type()
)
tMirrorLiX3CpuAlarmHighThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3CpuAlarmHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX3CpuAlarmHighThreshold.setUnits("percent")


class _TMirrorLiX3CpuAlarmLowThreshold_Type(Unsigned32):
    """Custom type tMirrorLiX3CpuAlarmLowThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TMirrorLiX3CpuAlarmLowThreshold_Type.__name__ = "Unsigned32"
_TMirrorLiX3CpuAlarmLowThreshold_Object = MibScalar
tMirrorLiX3CpuAlarmLowThreshold = _TMirrorLiX3CpuAlarmLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 15),
    _TMirrorLiX3CpuAlarmLowThreshold_Type()
)
tMirrorLiX3CpuAlarmLowThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3CpuAlarmLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX3CpuAlarmLowThreshold.setUnits("percent")


class _TMirrorLiX3MemAlarm_Type(TruthValue):
    """Custom type tMirrorLiX3MemAlarm based on TruthValue"""
    defaultValue = 2


_TMirrorLiX3MemAlarm_Type.__name__ = "TruthValue"
_TMirrorLiX3MemAlarm_Object = MibScalar
tMirrorLiX3MemAlarm = _TMirrorLiX3MemAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 16),
    _TMirrorLiX3MemAlarm_Type()
)
tMirrorLiX3MemAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3MemAlarm.setStatus("current")


class _TMirrorLiX3MemAlarmHighThreshold_Type(Unsigned32):
    """Custom type tMirrorLiX3MemAlarmHighThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TMirrorLiX3MemAlarmHighThreshold_Type.__name__ = "Unsigned32"
_TMirrorLiX3MemAlarmHighThreshold_Object = MibScalar
tMirrorLiX3MemAlarmHighThreshold = _TMirrorLiX3MemAlarmHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 17),
    _TMirrorLiX3MemAlarmHighThreshold_Type()
)
tMirrorLiX3MemAlarmHighThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3MemAlarmHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX3MemAlarmHighThreshold.setUnits("percent")


class _TMirrorLiX3MemAlarmLowThreshold_Type(Unsigned32):
    """Custom type tMirrorLiX3MemAlarmLowThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TMirrorLiX3MemAlarmLowThreshold_Type.__name__ = "Unsigned32"
_TMirrorLiX3MemAlarmLowThreshold_Object = MibScalar
tMirrorLiX3MemAlarmLowThreshold = _TMirrorLiX3MemAlarmLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 18),
    _TMirrorLiX3MemAlarmLowThreshold_Type()
)
tMirrorLiX3MemAlarmLowThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3MemAlarmLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX3MemAlarmLowThreshold.setUnits("percent")


class _TMirrorLiX3BwAlarm_Type(TruthValue):
    """Custom type tMirrorLiX3BwAlarm based on TruthValue"""
    defaultValue = 2


_TMirrorLiX3BwAlarm_Type.__name__ = "TruthValue"
_TMirrorLiX3BwAlarm_Object = MibScalar
tMirrorLiX3BwAlarm = _TMirrorLiX3BwAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 19),
    _TMirrorLiX3BwAlarm_Type()
)
tMirrorLiX3BwAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3BwAlarm.setStatus("current")


class _TMirrorLiX3BwAlarmHighThreshold_Type(Unsigned32):
    """Custom type tMirrorLiX3BwAlarmHighThreshold based on Unsigned32"""
    defaultValue = 0


_TMirrorLiX3BwAlarmHighThreshold_Type.__name__ = "Unsigned32"
_TMirrorLiX3BwAlarmHighThreshold_Object = MibScalar
tMirrorLiX3BwAlarmHighThreshold = _TMirrorLiX3BwAlarmHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 20),
    _TMirrorLiX3BwAlarmHighThreshold_Type()
)
tMirrorLiX3BwAlarmHighThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3BwAlarmHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX3BwAlarmHighThreshold.setUnits("megabps")


class _TMirrorLiX3BwAlarmLowThreshold_Type(Unsigned32):
    """Custom type tMirrorLiX3BwAlarmLowThreshold based on Unsigned32"""
    defaultValue = 0


_TMirrorLiX3BwAlarmLowThreshold_Type.__name__ = "Unsigned32"
_TMirrorLiX3BwAlarmLowThreshold_Object = MibScalar
tMirrorLiX3BwAlarmLowThreshold = _TMirrorLiX3BwAlarmLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 21),
    _TMirrorLiX3BwAlarmLowThreshold_Type()
)
tMirrorLiX3BwAlarmLowThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3BwAlarmLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX3BwAlarmLowThreshold.setUnits("Mpbs")


class _TMirrorLiX3OperState_Type(Integer32):
    """Custom type tMirrorLiX3OperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("outOfService", 3),
          ("transition", 4))
    )


_TMirrorLiX3OperState_Type.__name__ = "Integer32"
_TMirrorLiX3OperState_Object = MibScalar
tMirrorLiX3OperState = _TMirrorLiX3OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 103, 31),
    _TMirrorLiX3OperState_Type()
)
tMirrorLiX3OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX3OperState.setStatus("current")
_TMirrorLiX3PeerTableLastCh_Type = TimeStamp
_TMirrorLiX3PeerTableLastCh_Object = MibScalar
tMirrorLiX3PeerTableLastCh = _TMirrorLiX3PeerTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 104),
    _TMirrorLiX3PeerTableLastCh_Type()
)
tMirrorLiX3PeerTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX3PeerTableLastCh.setStatus("current")
_TMirrorLiX3PeerTable_Object = MibTable
tMirrorLiX3PeerTable = _TMirrorLiX3PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 105)
)
if mibBuilder.loadTexts:
    tMirrorLiX3PeerTable.setStatus("current")
_TMirrorLiX3PeerEntry_Object = MibTableRow
tMirrorLiX3PeerEntry = _TMirrorLiX3PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 105, 1)
)
tMirrorLiX3PeerEntry.setIndexNames(
    (1, "TIMETRA-MIRROR-MIB", "tMirrorLiX3PeerName"),
)
if mibBuilder.loadTexts:
    tMirrorLiX3PeerEntry.setStatus("current")
_TMirrorLiX3PeerName_Type = TNamedItem
_TMirrorLiX3PeerName_Object = MibTableColumn
tMirrorLiX3PeerName = _TMirrorLiX3PeerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 105, 1, 1),
    _TMirrorLiX3PeerName_Type()
)
tMirrorLiX3PeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiX3PeerName.setStatus("current")
_TMirrorLiX3PeerLastChanged_Type = TimeStamp
_TMirrorLiX3PeerLastChanged_Object = MibTableColumn
tMirrorLiX3PeerLastChanged = _TMirrorLiX3PeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 105, 1, 2),
    _TMirrorLiX3PeerLastChanged_Type()
)
tMirrorLiX3PeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX3PeerLastChanged.setStatus("current")
_TMirrorLiX3PeerRowStatus_Type = RowStatus
_TMirrorLiX3PeerRowStatus_Object = MibTableColumn
tMirrorLiX3PeerRowStatus = _TMirrorLiX3PeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 105, 1, 3),
    _TMirrorLiX3PeerRowStatus_Type()
)
tMirrorLiX3PeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMirrorLiX3PeerRowStatus.setStatus("current")
_TMirrorLiX1StatsTable_Object = MibTable
tMirrorLiX1StatsTable = _TMirrorLiX1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 201)
)
if mibBuilder.loadTexts:
    tMirrorLiX1StatsTable.setStatus("current")
_TMirrorLiX1StatsEntry_Object = MibTableRow
tMirrorLiX1StatsEntry = _TMirrorLiX1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 201, 1)
)
tMirrorLiX1StatsEntry.setIndexNames(
    (1, "TIMETRA-MIRROR-MIB", "tMirrorLicName"),
)
if mibBuilder.loadTexts:
    tMirrorLiX1StatsEntry.setStatus("current")
_TMirrorLiX1RxMessages_Type = Counter32
_TMirrorLiX1RxMessages_Object = MibTableColumn
tMirrorLiX1RxMessages = _TMirrorLiX1RxMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 201, 1, 1),
    _TMirrorLiX1RxMessages_Type()
)
tMirrorLiX1RxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX1RxMessages.setStatus("current")
_TMirrorLiX1TxMessages_Type = Counter32
_TMirrorLiX1TxMessages_Object = MibTableColumn
tMirrorLiX1TxMessages = _TMirrorLiX1TxMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 201, 1, 2),
    _TMirrorLiX1TxMessages_Type()
)
tMirrorLiX1TxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX1TxMessages.setStatus("current")
_TMirrorLiX1RxKBytes_Type = Counter64
_TMirrorLiX1RxKBytes_Object = MibTableColumn
tMirrorLiX1RxKBytes = _TMirrorLiX1RxKBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 201, 1, 3),
    _TMirrorLiX1RxKBytes_Type()
)
tMirrorLiX1RxKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX1RxKBytes.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX1RxKBytes.setUnits("kilobytes")
_TMirrorLiX1TxKBytes_Type = Counter64
_TMirrorLiX1TxKBytes_Object = MibTableColumn
tMirrorLiX1TxKBytes = _TMirrorLiX1TxKBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 201, 1, 4),
    _TMirrorLiX1TxKBytes_Type()
)
tMirrorLiX1TxKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX1TxKBytes.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX1TxKBytes.setUnits("kilobytes")
_TMirrorLiX2StatsTable_Object = MibTable
tMirrorLiX2StatsTable = _TMirrorLiX2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 202)
)
if mibBuilder.loadTexts:
    tMirrorLiX2StatsTable.setStatus("current")
_TMirrorLiX2StatsEntry_Object = MibTableRow
tMirrorLiX2StatsEntry = _TMirrorLiX2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 202, 1)
)
tMirrorLiX2StatsEntry.setIndexNames(
    (1, "TIMETRA-MIRROR-MIB", "tMirrorLicName"),
)
if mibBuilder.loadTexts:
    tMirrorLiX2StatsEntry.setStatus("current")
_TMirrorLiX2RxMessages_Type = Counter32
_TMirrorLiX2RxMessages_Object = MibTableColumn
tMirrorLiX2RxMessages = _TMirrorLiX2RxMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 202, 1, 1),
    _TMirrorLiX2RxMessages_Type()
)
tMirrorLiX2RxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX2RxMessages.setStatus("current")
_TMirrorLiX2TxMessages_Type = Counter32
_TMirrorLiX2TxMessages_Object = MibTableColumn
tMirrorLiX2TxMessages = _TMirrorLiX2TxMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 202, 1, 2),
    _TMirrorLiX2TxMessages_Type()
)
tMirrorLiX2TxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX2TxMessages.setStatus("current")
_TMirrorLiX2RxKBytes_Type = Counter64
_TMirrorLiX2RxKBytes_Object = MibTableColumn
tMirrorLiX2RxKBytes = _TMirrorLiX2RxKBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 202, 1, 3),
    _TMirrorLiX2RxKBytes_Type()
)
tMirrorLiX2RxKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX2RxKBytes.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX2RxKBytes.setUnits("kilobytes")
_TMirrorLiX2TxKBytes_Type = Counter64
_TMirrorLiX2TxKBytes_Object = MibTableColumn
tMirrorLiX2TxKBytes = _TMirrorLiX2TxKBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 202, 1, 4),
    _TMirrorLiX2TxKBytes_Type()
)
tMirrorLiX2TxKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX2TxKBytes.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX2TxKBytes.setUnits("kilobytes")
_TMirrorLiX3StatsTable_Object = MibTable
tMirrorLiX3StatsTable = _TMirrorLiX3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 203)
)
if mibBuilder.loadTexts:
    tMirrorLiX3StatsTable.setStatus("current")
_TMirrorLiX3StatsEntry_Object = MibTableRow
tMirrorLiX3StatsEntry = _TMirrorLiX3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 203, 1)
)
tMirrorLiX3StatsEntry.setIndexNames(
    (1, "TIMETRA-MIRROR-MIB", "tMirrorLicName"),
)
if mibBuilder.loadTexts:
    tMirrorLiX3StatsEntry.setStatus("current")
_TMirrorLiX3RxMessages_Type = Counter32
_TMirrorLiX3RxMessages_Object = MibTableColumn
tMirrorLiX3RxMessages = _TMirrorLiX3RxMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 203, 1, 1),
    _TMirrorLiX3RxMessages_Type()
)
tMirrorLiX3RxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX3RxMessages.setStatus("current")
_TMirrorLiX3TxMessages_Type = Counter32
_TMirrorLiX3TxMessages_Object = MibTableColumn
tMirrorLiX3TxMessages = _TMirrorLiX3TxMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 203, 1, 2),
    _TMirrorLiX3TxMessages_Type()
)
tMirrorLiX3TxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX3TxMessages.setStatus("current")
_TMirrorLiX3LicTAttempts_Type = Counter32
_TMirrorLiX3LicTAttempts_Object = MibTableColumn
tMirrorLiX3LicTAttempts = _TMirrorLiX3LicTAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 203, 1, 3),
    _TMirrorLiX3LicTAttempts_Type()
)
tMirrorLiX3LicTAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX3LicTAttempts.setStatus("current")
_TMirrorLiX3LicTSuccess_Type = Counter32
_TMirrorLiX3LicTSuccess_Object = MibTableColumn
tMirrorLiX3LicTSuccess = _TMirrorLiX3LicTSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 203, 1, 4),
    _TMirrorLiX3LicTSuccess_Type()
)
tMirrorLiX3LicTSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX3LicTSuccess.setStatus("current")
_TMirrorLiX3RxKBytes_Type = Counter64
_TMirrorLiX3RxKBytes_Object = MibTableColumn
tMirrorLiX3RxKBytes = _TMirrorLiX3RxKBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 203, 1, 5),
    _TMirrorLiX3RxKBytes_Type()
)
tMirrorLiX3RxKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX3RxKBytes.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX3RxKBytes.setUnits("kilobytes")
_TMirrorLiX3TxKBytes_Type = Counter64
_TMirrorLiX3TxKBytes_Object = MibTableColumn
tMirrorLiX3TxKBytes = _TMirrorLiX3TxKBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 203, 1, 6),
    _TMirrorLiX3TxKBytes_Type()
)
tMirrorLiX3TxKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiX3TxKBytes.setStatus("current")
if mibBuilder.loadTexts:
    tMirrorLiX3TxKBytes.setUnits("kilobytes")
_TMirrorLiXTgtTable_Object = MibTable
tMirrorLiXTgtTable = _TMirrorLiXTgtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204)
)
if mibBuilder.loadTexts:
    tMirrorLiXTgtTable.setStatus("obsolete")
_TMirrorLiXTgtEntry_Object = MibTableRow
tMirrorLiXTgtEntry = _TMirrorLiXTgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1)
)
tMirrorLiXTgtEntry.setIndexNames(
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiXTgtType"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiXTgtAddrType"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiXTgtAddr"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiXTgtPrefixLength"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiXTgtPort"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiXTgtVisitAddressType"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiXTgtVisitAddrType"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiXTgtVisitAddr"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiXTgtVisitPrefixLength"),
    (0, "TIMETRA-MIRROR-MIB", "tMirrorLiXTgtVisitPort"),
)
if mibBuilder.loadTexts:
    tMirrorLiXTgtEntry.setStatus("obsolete")


class _TMirrorLiXTgtType_Type(Integer32):
    """Custom type tMirrorLiXTgtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipField", 2),
          ("ipPort", 7),
          ("all", 255))
    )


_TMirrorLiXTgtType_Type.__name__ = "Integer32"
_TMirrorLiXTgtType_Object = MibTableColumn
tMirrorLiXTgtType = _TMirrorLiXTgtType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 1),
    _TMirrorLiXTgtType_Type()
)
tMirrorLiXTgtType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiXTgtType.setStatus("obsolete")
_TMirrorLiXTgtAddrType_Type = InetAddressType
_TMirrorLiXTgtAddrType_Object = MibTableColumn
tMirrorLiXTgtAddrType = _TMirrorLiXTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 2),
    _TMirrorLiXTgtAddrType_Type()
)
tMirrorLiXTgtAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiXTgtAddrType.setStatus("obsolete")


class _TMirrorLiXTgtAddr_Type(InetAddress):
    """Custom type tMirrorLiXTgtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TMirrorLiXTgtAddr_Type.__name__ = "InetAddress"
_TMirrorLiXTgtAddr_Object = MibTableColumn
tMirrorLiXTgtAddr = _TMirrorLiXTgtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 3),
    _TMirrorLiXTgtAddr_Type()
)
tMirrorLiXTgtAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiXTgtAddr.setStatus("obsolete")


class _TMirrorLiXTgtPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tMirrorLiXTgtPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TMirrorLiXTgtPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TMirrorLiXTgtPrefixLength_Object = MibTableColumn
tMirrorLiXTgtPrefixLength = _TMirrorLiXTgtPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 4),
    _TMirrorLiXTgtPrefixLength_Type()
)
tMirrorLiXTgtPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiXTgtPrefixLength.setStatus("obsolete")
_TMirrorLiXTgtPort_Type = InetPortNumber
_TMirrorLiXTgtPort_Object = MibTableColumn
tMirrorLiXTgtPort = _TMirrorLiXTgtPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 5),
    _TMirrorLiXTgtPort_Type()
)
tMirrorLiXTgtPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiXTgtPort.setStatus("obsolete")


class _TMirrorLiXTgtVisitAddressType_Type(Integer32):
    """Custom type tMirrorLiXTgtVisitAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("ip", 1),
          ("ipPort", 2),
          ("ipField", 3),
          ("dstPort", 5))
    )


_TMirrorLiXTgtVisitAddressType_Type.__name__ = "Integer32"
_TMirrorLiXTgtVisitAddressType_Object = MibTableColumn
tMirrorLiXTgtVisitAddressType = _TMirrorLiXTgtVisitAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 6),
    _TMirrorLiXTgtVisitAddressType_Type()
)
tMirrorLiXTgtVisitAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiXTgtVisitAddressType.setStatus("obsolete")
_TMirrorLiXTgtVisitAddrType_Type = InetAddressType
_TMirrorLiXTgtVisitAddrType_Object = MibTableColumn
tMirrorLiXTgtVisitAddrType = _TMirrorLiXTgtVisitAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 7),
    _TMirrorLiXTgtVisitAddrType_Type()
)
tMirrorLiXTgtVisitAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiXTgtVisitAddrType.setStatus("obsolete")


class _TMirrorLiXTgtVisitAddr_Type(InetAddress):
    """Custom type tMirrorLiXTgtVisitAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TMirrorLiXTgtVisitAddr_Type.__name__ = "InetAddress"
_TMirrorLiXTgtVisitAddr_Object = MibTableColumn
tMirrorLiXTgtVisitAddr = _TMirrorLiXTgtVisitAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 8),
    _TMirrorLiXTgtVisitAddr_Type()
)
tMirrorLiXTgtVisitAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiXTgtVisitAddr.setStatus("obsolete")


class _TMirrorLiXTgtVisitPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tMirrorLiXTgtVisitPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TMirrorLiXTgtVisitPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TMirrorLiXTgtVisitPrefixLength_Object = MibTableColumn
tMirrorLiXTgtVisitPrefixLength = _TMirrorLiXTgtVisitPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 9),
    _TMirrorLiXTgtVisitPrefixLength_Type()
)
tMirrorLiXTgtVisitPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiXTgtVisitPrefixLength.setStatus("obsolete")
_TMirrorLiXTgtVisitPort_Type = InetPortNumber
_TMirrorLiXTgtVisitPort_Object = MibTableColumn
tMirrorLiXTgtVisitPort = _TMirrorLiXTgtVisitPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 10),
    _TMirrorLiXTgtVisitPort_Type()
)
tMirrorLiXTgtVisitPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMirrorLiXTgtVisitPort.setStatus("obsolete")


class _TMirrorLiXTgtCreateTime_Type(DateAndTime):
    """Custom type tMirrorLiXTgtCreateTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TMirrorLiXTgtCreateTime_Type.__name__ = "DateAndTime"
_TMirrorLiXTgtCreateTime_Object = MibTableColumn
tMirrorLiXTgtCreateTime = _TMirrorLiXTgtCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 12),
    _TMirrorLiXTgtCreateTime_Type()
)
tMirrorLiXTgtCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiXTgtCreateTime.setStatus("obsolete")


class _TMirrorLiXTgtTransLayerProtocol_Type(Integer32):
    """Custom type tMirrorLiXTgtTransLayerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("tcp", 1),
          ("udp", 2))
    )


_TMirrorLiXTgtTransLayerProtocol_Type.__name__ = "Integer32"
_TMirrorLiXTgtTransLayerProtocol_Object = MibTableColumn
tMirrorLiXTgtTransLayerProtocol = _TMirrorLiXTgtTransLayerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 13),
    _TMirrorLiXTgtTransLayerProtocol_Type()
)
tMirrorLiXTgtTransLayerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiXTgtTransLayerProtocol.setStatus("obsolete")
_TMirrorLiXTgtVolatile_Type = TruthValue
_TMirrorLiXTgtVolatile_Object = MibTableColumn
tMirrorLiXTgtVolatile = _TMirrorLiXTgtVolatile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 5, 301, 204, 1, 14),
    _TMirrorLiXTgtVolatile_Type()
)
tMirrorLiXTgtVolatile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMirrorLiXTgtVolatile.setStatus("obsolete")
_TMirrorLiNotifyObjects_ObjectIdentity = ObjectIdentity
tMirrorLiNotifyObjects = _TMirrorLiNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 6)
)
_TMirrorNotifyLiSvcId_Type = TmnxServId
_TMirrorNotifyLiSvcId_Object = MibScalar
tMirrorNotifyLiSvcId = _TMirrorNotifyLiSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 6, 1),
    _TMirrorNotifyLiSvcId_Type()
)
tMirrorNotifyLiSvcId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorNotifyLiSvcId.setStatus("current")
_TMirrorNotifyLiPortId_Type = TmnxPortID
_TMirrorNotifyLiPortId_Object = MibScalar
tMirrorNotifyLiPortId = _TMirrorNotifyLiPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 6, 2),
    _TMirrorNotifyLiPortId_Type()
)
tMirrorNotifyLiPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorNotifyLiPortId.setStatus("current")
_TMirrorNotifyLiSapEncapValue_Type = TmnxEncapVal
_TMirrorNotifyLiSapEncapValue_Object = MibScalar
tMirrorNotifyLiSapEncapValue = _TMirrorNotifyLiSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 6, 3),
    _TMirrorNotifyLiSapEncapValue_Type()
)
tMirrorNotifyLiSapEncapValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorNotifyLiSapEncapValue.setStatus("current")


class _TMirrorNotifyLiDescription_Type(DisplayString):
    """Custom type tMirrorNotifyLiDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TMirrorNotifyLiDescription_Type.__name__ = "DisplayString"
_TMirrorNotifyLiDescription_Object = MibScalar
tMirrorNotifyLiDescription = _TMirrorNotifyLiDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 6, 4),
    _TMirrorNotifyLiDescription_Type()
)
tMirrorNotifyLiDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorNotifyLiDescription.setStatus("current")
_TMirrorLiNotifyIneIdentifier_Type = TNamedItem
_TMirrorLiNotifyIneIdentifier_Object = MibScalar
tMirrorLiNotifyIneIdentifier = _TMirrorLiNotifyIneIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 6, 5),
    _TMirrorLiNotifyIneIdentifier_Type()
)
tMirrorLiNotifyIneIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorLiNotifyIneIdentifier.setStatus("current")


class _TMirrorLiNotifyX2AlarmRank_Type(Integer32):
    """Custom type tMirrorLiNotifyX2AlarmRank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("serious", 1),
          ("urgent", 2))
    )


_TMirrorLiNotifyX2AlarmRank_Type.__name__ = "Integer32"
_TMirrorLiNotifyX2AlarmRank_Object = MibScalar
tMirrorLiNotifyX2AlarmRank = _TMirrorLiNotifyX2AlarmRank_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 6, 6),
    _TMirrorLiNotifyX2AlarmRank_Type()
)
tMirrorLiNotifyX2AlarmRank.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorLiNotifyX2AlarmRank.setStatus("current")


class _TMirrorLiNotifyX2AlarmFlag_Type(Integer32):
    """Custom type tMirrorLiNotifyX2AlarmFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("elimination", 1))
    )


_TMirrorLiNotifyX2AlarmFlag_Type.__name__ = "Integer32"
_TMirrorLiNotifyX2AlarmFlag_Object = MibScalar
tMirrorLiNotifyX2AlarmFlag = _TMirrorLiNotifyX2AlarmFlag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 6, 7),
    _TMirrorLiNotifyX2AlarmFlag_Type()
)
tMirrorLiNotifyX2AlarmFlag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorLiNotifyX2AlarmFlag.setStatus("current")


class _TMirrorLiNotifyDateAndTime_Type(DateAndTime):
    """Custom type tMirrorLiNotifyDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TMirrorLiNotifyDateAndTime_Type.__name__ = "DateAndTime"
_TMirrorLiNotifyDateAndTime_Object = MibScalar
tMirrorLiNotifyDateAndTime = _TMirrorLiNotifyDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 6, 8),
    _TMirrorLiNotifyDateAndTime_Type()
)
tMirrorLiNotifyDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorLiNotifyDateAndTime.setStatus("current")
_TMirrorLiNotifyLongDescription_Type = TmnxLongDisplayString
_TMirrorLiNotifyLongDescription_Object = MibScalar
tMirrorLiNotifyLongDescription = _TMirrorLiNotifyLongDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 18, 6, 9),
    _TMirrorLiNotifyLongDescription_Type()
)
tMirrorLiNotifyLongDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMirrorLiNotifyLongDescription.setStatus("current")
_TMirrorNotifyPrefix_ObjectIdentity = ObjectIdentity
tMirrorNotifyPrefix = _TMirrorNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18)
)
_TMirrorNotifications_ObjectIdentity = ObjectIdentity
tMirrorNotifications = _TMirrorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0)
)

# Managed Objects groups

tMirrorSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 3)
)
tMirrorSourceGroup.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceAdminStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIpFilterRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceMacFilterRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIngressLabelRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortEgressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortIngressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapEgressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapIngressEnabled"))
)
if mibBuilder.loadTexts:
    tMirrorSourceGroup.setStatus("obsolete")

tMirrorDestinationR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 5)
)
tMirrorDestinationR2r1Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationDescription"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationFC"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationRemoteSource"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSapPortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSapEncapValue"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSdpNumber"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationAdminStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationOperStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSliceSize"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSdpEgrSvcLabel"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSapEgressQosPolicyId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationEncapsulation"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSdpOperEgrSvcLabel"))
)
if mibBuilder.loadTexts:
    tMirrorDestinationR2r1Group.setStatus("obsolete")

tMirrorDestinationR2r1RemoteSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 6)
)
tMirrorDestinationR2r1RemoteSourceGroup.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationRemoteSourceAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationRemoteSourceLabelSignaling"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationRemoteSourceIngSvcLabel"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationRemoteSourceRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationRemoteSourceOperIngSvcLabel"))
)
if mibBuilder.loadTexts:
    tMirrorDestinationR2r1RemoteSourceGroup.setStatus("current")

tMirrorR2r1ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 7)
)
tMirrorR2r1ObsoleteGroup.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationSdpDestEncap"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationTranslateDisable"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationPppoeDestMacAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationPppoeSrcMacAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationPppoeEtype"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationPppoeSessionId"))
)
if mibBuilder.loadTexts:
    tMirrorR2r1ObsoleteGroup.setStatus("current")

tMirrorNotifyObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 8)
)
tMirrorNotifyObjsV5v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"))
)
if mibBuilder.loadTexts:
    tMirrorNotifyObjsV5v0Group.setStatus("obsolete")

tMirrorDestinationV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 9)
)
tMirrorDestinationV6v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationDescription"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationFC"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationRemoteSource"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSapPortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSapEncapValue"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationAdminStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationOperStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSliceSize"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSapEgressQosPolicyId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationEncapsulation"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationEnablePortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestSapEgrIpMirrorSA"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestSapEgrIpMirrorDA"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestTableLastChnged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestRemoteSrcLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestRemSrcTblLastChgd"))
)
if mibBuilder.loadTexts:
    tMirrorDestinationV6v0Group.setStatus("obsolete")

tMirrorSourceV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 10)
)
tMirrorSourceV6v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceAdminStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIpFilterRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceMacFilterRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIngressLabelRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortEgressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortIngressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapEgressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapIngressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubTableLastChnged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubPortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubEncapValue"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubIpAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubIpAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubMacAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubSLAProfName"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubFC"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubEgressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubIngressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIpFilterLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceMacFilterLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIngLabelLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcTblLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcIpFltrTblLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcMacFltrTblLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcIngLblTblLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcPortTblLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcSapTblLastChgd"))
)
if mibBuilder.loadTexts:
    tMirrorSourceV6v0Group.setStatus("obsolete")

tMirrorNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 11)
)
tMirrorNotifyObjsV6v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapPortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapEncapValue"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubIdent"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceChangeType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterEntryId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterObject"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterDescr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterSvcId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterPortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterSapEncapValue"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterSdpBindId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterDirection"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterIfIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterIfName"))
)
if mibBuilder.loadTexts:
    tMirrorNotifyObjsV6v0Group.setStatus("current")

tMirrorBsxV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 13)
)
tMirrorBsxV6v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIsaAaGrpRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIsaAaGrpUnknownOnly"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIsaAaGrpLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcIsaAaGrpTblLastChgd"))
)
if mibBuilder.loadTexts:
    tMirrorBsxV6v0Group.setStatus("current")

tMirrorDestV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 14)
)
tMirrorDestV8v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestRemoteSrcIsICB"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestRemoteSrcVcId"))
)
if mibBuilder.loadTexts:
    tMirrorDestV8v0Group.setStatus("current")

tMirrorObsoletedV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 15)
)
tMirrorObsoletedV8v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationSdpNumber"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSdpEgrSvcLabel"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSdpOperEgrSvcLabel"))
)
if mibBuilder.loadTexts:
    tMirrorObsoletedV8v0Group.setStatus("current")

tMirrorDestinationV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 16)
)
tMirrorDestinationV8v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationDescription"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationFC"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationRemoteSource"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSapPortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSapEncapValue"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationAdminStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationOperStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSliceSize"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationSapEgressQosPolicyId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationEncapsulation"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationEnablePortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestSapEgrIpMirrorSA"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestSapEgrIpMirrorDA"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestTableLastChnged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestRemoteSrcLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestRemSrcTblLastChgd"))
)
if mibBuilder.loadTexts:
    tMirrorDestinationV8v0Group.setStatus("current")

tMirrorRadiusLiV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 17)
)
tMirrorRadiusLiV8v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tRadiusLiSrcHostId"),
        ("TIMETRA-MIRROR-MIB", "tRadiusLiMirrorDirection"),
        ("TIMETRA-MIRROR-MIB", "tRadiusLiMirrorForwClassMap"))
)
if mibBuilder.loadTexts:
    tMirrorRadiusLiV8v0Group.setStatus("current")

tMirrorLiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 20)
)
tMirrorLiGroup.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorLiSourceNatTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSubTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceNatLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceNatDestMacAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceNatSrcMacAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceNatEthertype"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSubRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSubLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSubInterceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatL2awSubTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatL2awSubRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatL2awSubLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatL2awSubInterceptId"))
)
if mibBuilder.loadTexts:
    tMirrorLiGroup.setStatus("current")

tMirrorEncapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 21)
)
tMirrorEncapGroup.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIpFilterIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceMacFilterIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tRadiusLiSrcIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIpFilterSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceMacFilterSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubSessionId"),
        ("TIMETRA-MIRROR-MIB", "tRadiusLiSrcSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSubSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatL2awSubSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3EncTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3EncRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3EncLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3EncHeaderType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3EncRouter"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3EncUseDirectionBit"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwSrcAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwSrcAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwDstAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwDstAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwUdpSrcPort"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwUdpDstPort"))
)
if mibBuilder.loadTexts:
    tMirrorEncapGroup.setStatus("obsolete")

tMirrorNotifyObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 22)
)
tMirrorNotifyObjsV10v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorNotifyLiDescription"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifyLiPortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifyLiSapEncapValue"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifyLiSvcId"))
)
if mibBuilder.loadTexts:
    tMirrorNotifyObjsV10v0Group.setStatus("current")

tMirrorSourceV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 24)
)
tMirrorSourceV10v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceAdminStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIpFilterRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceMacFilterRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIngressLabelRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortEgressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortIngressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapEgressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapIngressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubTableLastChnged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubPortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubEncapValue"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubIpAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubIpAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubMacAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubSLAProfName"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubFC"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubEgressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubIngressEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIpFilterLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceMacFilterLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIngLabelLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcTblLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcIpFltrTblLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcMacFltrTblLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcIngLblTblLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcPortTblLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcSapTblLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIpv6FilterRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIpv6FilterLastChgd"))
)
if mibBuilder.loadTexts:
    tMirrorSourceV10v0Group.setStatus("current")

tMirrorEncapV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 25)
)
tMirrorEncapV10v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIpFilterIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceMacFilterIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tRadiusLiSrcIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIpFilterSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceMacFilterSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubSessionId"),
        ("TIMETRA-MIRROR-MIB", "tRadiusLiSrcSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSubSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatL2awSubSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3EncTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3EncRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3EncLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3EncHeaderType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3EncRouter"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3EncUseDirectionBit"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwSrcAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwSrcAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwDstAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwDstAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwUdpSrcPort"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestL3GwUdpDstPort"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIpv6FilterIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIpv6FilterSessionId"))
)
if mibBuilder.loadTexts:
    tMirrorEncapV10v0Group.setStatus("current")

tMirrorLiSourceV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 26)
)
tMirrorLiSourceV10v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceLiMacFltrTableLstCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiMacFltrRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiMacFltrLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiMacFltrIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiMacFltrSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubInterceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubSessionId"))
)
if mibBuilder.loadTexts:
    tMirrorLiSourceV10v0Group.setStatus("obsolete")

tMirrorDestinationV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 27)
)
tMirrorDestinationV11v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestSapEgrPortQGrp"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestSapEgrPortQGrpInstId"))
)
if mibBuilder.loadTexts:
    tMirrorDestinationV11v0Group.setStatus("current")

tMirrorLiSourceV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 28)
)
tMirrorLiSourceV12v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceLiMacFltrTableLstCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiMacFltrRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiMacFltrLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiMacFltrIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiMacFltrSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubInterceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiIpFltrTableLstCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiIpFltrRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiIpFltrLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiIpFltrIntceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiIpFltrSessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDsmSubTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDsmSubRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDsmSubLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDsmSubInterceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDsmSubSessionId"))
)
if mibBuilder.loadTexts:
    tMirrorLiSourceV12v0Group.setStatus("current")

tMirrorLiSourceV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 29)
)
tMirrorLiSourceV13v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSubOperState"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatL2awSubOperState"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubOperState"))
)
if mibBuilder.loadTexts:
    tMirrorLiSourceV13v0Group.setStatus("current")

tMirrorLiV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 31)
)
tMirrorLiV14v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestCreationOrigin"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplEncapsulation"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplEncapsulation"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplL3EncHeaderType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplL3EncUseDirect"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplL3EncRouter"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplL3SrcAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplL3SrcAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplL3UdpSrcPort"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplL3UdpDstPort"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestServiceRangeStart"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiDestServiceRangeEnd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorRadiusLiCfgDestTmpl"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiCfgNatUseOutsideIpAddr"),
        ("TIMETRA-MIRROR-MIB", "tRadiusLiSrcNatUsingOutsideIp"))
)
if mibBuilder.loadTexts:
    tMirrorLiV14v0Group.setStatus("current")

tMirrorSourceSubHostTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 32)
)
tMirrorSourceSubHostTypeGroup.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceSubHostType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubIpFamily"))
)
if mibBuilder.loadTexts:
    tMirrorSourceSubHostTypeGroup.setStatus("current")

tMirrorSourceStatsV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 33)
)
tMirrorSourceStatsV15v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceStatsTotalSrc"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceCreationOrigin"))
)
if mibBuilder.loadTexts:
    tMirrorSourceStatsV15v0Group.setStatus("current")

tMirrorLicV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 34)
)
tMirrorLicV15v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorLiCfgXIfTgtPersistFileLoc"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicDescription"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicIdentifier"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicRouter"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicIpAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicIpAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicPort"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicAuthPrivateKi"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicAuthPassword"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicAuthSequenceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorIneIdentifier"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiXIfAdminState"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiXIfUserDb"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1LastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1PeerLic"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1IpAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1IpAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1Port"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1ToNoMsg"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1OperState"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2LastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2PeerLic"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2IpAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2IpAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2ToConnectionReq"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2ToKeepalive"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2OperState"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3LastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3LiGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3StartIpAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3StartIpAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3EndIpAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3EndIpAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3MaxNumSessions"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3ToTunnelReq"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3ToKeepalive"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3ToTargetRetryWait"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3CpuAlarm"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3CpuAlarmHighThreshold"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3CpuAlarmLowThreshold"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3MemAlarm"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3MemAlarmHighThreshold"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3MemAlarmLowThreshold"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3BwAlarm"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3BwAlarmHighThreshold"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3BwAlarmLowThreshold"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3OperState"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3PeerTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3PeerRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3PeerLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1RxMessages"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1TxMessages"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1RxKBytes"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1TxKBytes"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2RxKBytes"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2TxKBytes"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2RxMessages"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2TxMessages"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3RxMessages"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3TxMessages"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3LicTAttempts"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3LicTSuccess"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3RxKBytes"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3TxKBytes"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiXTgtCreateTime"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiXTgtTransLayerProtocol"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiXTgtVolatile"))
)
if mibBuilder.loadTexts:
    tMirrorLicV15v0Group.setStatus("obsolete")

tMirrorNotifyObjsV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 36)
)
tMirrorNotifyObjsV15v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorLiNotifyIneIdentifier"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNotifyX2AlarmRank"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNotifyX2AlarmFlag"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNotifyDateAndTime"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNotifyLongDescription"))
)
if mibBuilder.loadTexts:
    tMirrorNotifyObjsV15v0Group.setStatus("current")

tMirrorServiceNameV15v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 37)
)
tMirrorServiceNameV15v1Group.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorDestinationName")
)
if mibBuilder.loadTexts:
    tMirrorServiceNameV15v1Group.setStatus("current")

tMirrorLicV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 40)
)
tMirrorLicV16v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorLiXIfCorrelationIdIpoe"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiXIfCorrelationIdPppoe"))
)
if mibBuilder.loadTexts:
    tMirrorLicV16v0Group.setStatus("current")

tMirrorDestPcapV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 41)
)
tMirrorDestPcapV16v0Group.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorDestPcapSessionName")
)
if mibBuilder.loadTexts:
    tMirrorDestPcapV16v0Group.setStatus("current")

tMirrorSourceV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 42)
)
tMirrorSourceV19v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourcePortVlanRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortVlanEgrEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortVlanIngEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortVlanLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSrcPortVlanTblLastChgd"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceName"))
)
if mibBuilder.loadTexts:
    tMirrorSourceV19v0Group.setStatus("current")

tMirrorLicV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 43)
)
tMirrorLicV19v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorLiCfgXIfTgtPersistFileLoc"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicDescription"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicIdentifier"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicRouter"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicIpAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicIpAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicPort"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicAuthPrivateKi"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicAuthPassword"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicAuthSequenceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorIneIdentifier"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiXIfAdminState"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiXIfUserDb"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1LastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1PeerLic"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1IpAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1IpAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1Port"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1ToNoMsg"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1OperState"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2LastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2PeerLic"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2IpAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2IpAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2ToConnectionReq"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2ToKeepalive"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2OperState"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3LastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3LiGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3StartIpAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3StartIpAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3EndIpAddrType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3EndIpAddr"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3MaxNumSessions"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3ToTunnelReq"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3ToKeepalive"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3ToTargetRetryWait"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3CpuAlarm"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3CpuAlarmHighThreshold"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3CpuAlarmLowThreshold"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3MemAlarm"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3MemAlarmHighThreshold"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3MemAlarmLowThreshold"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3BwAlarm"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3BwAlarmHighThreshold"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3BwAlarmLowThreshold"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3OperState"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3PeerTableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3PeerRowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3PeerLastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1RxMessages"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1TxMessages"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1RxKBytes"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX1TxKBytes"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2RxKBytes"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2TxKBytes"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2RxMessages"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX2TxMessages"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3RxMessages"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3TxMessages"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3LicTAttempts"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3LicTSuccess"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3RxKBytes"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiX3TxKBytes"))
)
if mibBuilder.loadTexts:
    tMirrorLicV19v0Group.setStatus("current")

tMirrorObsoletedV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 44)
)
tMirrorObsoletedV19v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorLiXTgtCreateTime"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiXTgtTransLayerProtocol"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiXTgtVolatile"))
)
if mibBuilder.loadTexts:
    tMirrorObsoletedV19v0Group.setStatus("current")

tMirrorLiV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 45)
)
tMirrorLiV19v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorLiDestTmplL3EncRouterName"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSub2TableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSub2RowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSub2LastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSub2InterceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSub2SessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSub2OperState"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64Sub2TableLastCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64Sub2RowStatus"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64Sub2LastChanged"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64Sub2InterceptId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64Sub2SessionId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64Sub2OperState"))
)
if mibBuilder.loadTexts:
    tMirrorLiV19v0Group.setStatus("current")

tMirrorDestV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 46)
)
tMirrorDestV20v0Group.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorDestSamplingRate")
)
if mibBuilder.loadTexts:
    tMirrorDestV20v0Group.setStatus("current")

tMirrorSourceV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 47)
)
tMirrorSourceV20v0Group.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapShimId")
)
if mibBuilder.loadTexts:
    tMirrorSourceV20v0Group.setStatus("current")

tMirrorLiSourcePortLicV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 49)
)
tMirrorLiSourcePortLicV20v0Group.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortLicenseState")
)
if mibBuilder.loadTexts:
    tMirrorLiSourcePortLicV20v0Group.setStatus("current")


# Notification objects

tMirrorSourceEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 1)
)
tMirrorSourceEnabled.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex")
)
if mibBuilder.loadTexts:
    tMirrorSourceEnabled.setStatus(
        "current"
    )

tMirrorSourceDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 2)
)
tMirrorSourceDisabled.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex")
)
if mibBuilder.loadTexts:
    tMirrorSourceDisabled.setStatus(
        "current"
    )

tMirrorDestinationEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 3)
)
tMirrorDestinationEnabled.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorDestinationIndex")
)
if mibBuilder.loadTexts:
    tMirrorDestinationEnabled.setStatus(
        "current"
    )

tMirrorDestinationDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 4)
)
tMirrorDestinationDisabled.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorDestinationIndex")
)
if mibBuilder.loadTexts:
    tMirrorDestinationDisabled.setStatus(
        "current"
    )

tMirrorSourceRemovedBySystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 5)
)
tMirrorSourceRemovedBySystem.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex")
)
if mibBuilder.loadTexts:
    tMirrorSourceRemovedBySystem.setStatus(
        "current"
    )

tMirrorSourceIpFilterChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 6)
)
tMirrorSourceIpFilterChange.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterEntryId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceChangeType"))
)
if mibBuilder.loadTexts:
    tMirrorSourceIpFilterChange.setStatus(
        "current"
    )

tMirrorSourceMacFilterChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 7)
)
tMirrorSourceMacFilterChange.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterEntryId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceChangeType"))
)
if mibBuilder.loadTexts:
    tMirrorSourceMacFilterChange.setStatus(
        "current"
    )

tMirrorSourceSapChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 8)
)
tMirrorSourceSapChange.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapPortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapEncapValue"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceChangeType"))
)
if mibBuilder.loadTexts:
    tMirrorSourceSapChange.setStatus(
        "current"
    )

tMirrorSourceSubChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 9)
)
tMirrorSourceSubChange.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubIdent"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceChangeType"))
)
if mibBuilder.loadTexts:
    tMirrorSourceSubChange.setStatus(
        "current"
    )

tMirrorSourceIPFltrChangeReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 10)
)
tMirrorSourceIPFltrChangeReject.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterEntryId"))
)
if mibBuilder.loadTexts:
    tMirrorSourceIPFltrChangeReject.setStatus(
        "current"
    )

tMirrorSourceIP6FltrChangeReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 11)
)
tMirrorSourceIP6FltrChangeReject.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterEntryId"))
)
if mibBuilder.loadTexts:
    tMirrorSourceIP6FltrChangeReject.setStatus(
        "current"
    )

tMirrorSourceMacFltrChangeReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 12)
)
tMirrorSourceMacFltrChangeReject.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterEntryId"))
)
if mibBuilder.loadTexts:
    tMirrorSourceMacFltrChangeReject.setStatus(
        "current"
    )

tMirrorSourceFilterAssignReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 13)
)
tMirrorSourceFilterAssignReject.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterObject"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterDescr"))
)
if mibBuilder.loadTexts:
    tMirrorSourceFilterAssignReject.setStatus(
        "current"
    )

tMirrorDestinationChangeReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 14)
)
tMirrorDestinationChangeReject.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorDestinationIndex")
)
if mibBuilder.loadTexts:
    tMirrorDestinationChangeReject.setStatus(
        "current"
    )

tMirrorSourceFilterOverruled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 15)
)
tMirrorSourceFilterOverruled.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterObject"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterDescr"))
)
if mibBuilder.loadTexts:
    tMirrorSourceFilterOverruled.setStatus(
        "current"
    )

tMirrorSourceFilterAssignWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 16)
)
tMirrorSourceFilterAssignWarn.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterObject"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterDescr"))
)
if mibBuilder.loadTexts:
    tMirrorSourceFilterAssignWarn.setStatus(
        "current"
    )

tMirrorFilterAssignToSapWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 17)
)
tMirrorFilterAssignToSapWarn.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorFilterSvcId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterPortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterSapEncapValue"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterDirection"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterId"))
)
if mibBuilder.loadTexts:
    tMirrorFilterAssignToSapWarn.setStatus(
        "current"
    )

tMirrorFilterAssignToSdpWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 18)
)
tMirrorFilterAssignToSdpWarn.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorFilterSvcId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterSdpBindId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterDirection"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterId"))
)
if mibBuilder.loadTexts:
    tMirrorFilterAssignToSdpWarn.setStatus(
        "current"
    )

tMirrorFilterAssignToItfWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 19)
)
tMirrorFilterAssignToItfWarn.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorFilterIfIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterIfName"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterType"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterDirection"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterId"))
)
if mibBuilder.loadTexts:
    tMirrorFilterAssignToItfWarn.setStatus(
        "current"
    )

tMirrorSourceLiFilterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 20)
)
tMirrorSourceLiFilterChanged.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterObject"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterDescr"))
)
if mibBuilder.loadTexts:
    tMirrorSourceLiFilterChanged.setStatus(
        "current"
    )

tMirrorSourceLiSubProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 21)
)
tMirrorSourceLiSubProblem.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceSubIdent"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifyLiSvcId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifyLiPortId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifyLiSapEncapValue"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifyLiDescription"))
)
if mibBuilder.loadTexts:
    tMirrorSourceLiSubProblem.setStatus(
        "current"
    )

tMirrorSourceIpv6FilterChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 22)
)
tMirrorSourceIpv6FilterChange.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterEntryId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceChangeType"))
)
if mibBuilder.loadTexts:
    tMirrorSourceIpv6FilterChange.setStatus(
        "current"
    )

tMirrorSourceIPv6FltrChangeRej = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 23)
)
tMirrorSourceIPv6FltrChangeRej.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIndex"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterId"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterEntryId"))
)
if mibBuilder.loadTexts:
    tMirrorSourceIPv6FltrChangeRej.setStatus(
        "current"
    )

tMirrorLiNatLsnSubOperStateCh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 24)
)
tMirrorLiNatLsnSubOperStateCh.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSubOperState")
)
if mibBuilder.loadTexts:
    tMirrorLiNatLsnSubOperStateCh.setStatus(
        "current"
    )

tMirrorLiNatL2awSubOperStateCh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 25)
)
tMirrorLiNatL2awSubOperStateCh.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorLiNatL2awSubOperState")
)
if mibBuilder.loadTexts:
    tMirrorLiNatL2awSubOperStateCh.setStatus(
        "current"
    )

tMirrorLiNat64SubOperStateCh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 26)
)
tMirrorLiNat64SubOperStateCh.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubOperState")
)
if mibBuilder.loadTexts:
    tMirrorLiNat64SubOperStateCh.setStatus(
        "current"
    )

tMirrorLiX2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 27)
)
tMirrorLiX2Alarm.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorLiNotifyIneIdentifier"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNotifyX2AlarmRank"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNotifyX2AlarmFlag"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNotifyDateAndTime"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNotifyLongDescription"))
)
if mibBuilder.loadTexts:
    tMirrorLiX2Alarm.setStatus(
        "current"
    )

radiusFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 28)
)
radiusFailed.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorNotifyLiDescription")
)
if mibBuilder.loadTexts:
    radiusFailed.setStatus(
        "current"
    )

tMirrorLiSrcPortLicInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 18, 0, 29)
)
tMirrorLiSrcPortLicInvalid.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorSourcePortLicenseState")
)
if mibBuilder.loadTexts:
    tMirrorLiSrcPortLicInvalid.setStatus(
        "current"
    )


# Notifications groups

tMirrorNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 4)
)
tMirrorNotificationsGroup.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceDisabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationEnabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationDisabled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceRemovedBySystem"))
)
if mibBuilder.loadTexts:
    tMirrorNotificationsGroup.setStatus(
        "current"
    )

tMirrorSourceNotificationsV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 12)
)
tMirrorSourceNotificationsV6v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceIpFilterChange"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceMacFilterChange"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSapChange"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubChange"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIPFltrChangeReject"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIP6FltrChangeReject"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceMacFltrChangeReject"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterAssignReject"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationChangeReject"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterOverruled"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceFilterAssignWarn"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterAssignToSapWarn"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterAssignToSdpWarn"),
        ("TIMETRA-MIRROR-MIB", "tMirrorFilterAssignToItfWarn"))
)
if mibBuilder.loadTexts:
    tMirrorSourceNotificationsV6v0Group.setStatus(
        "current"
    )

tMirrorSourceNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 18)
)
tMirrorSourceNotifGroup.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorSourceLiFilterChanged")
)
if mibBuilder.loadTexts:
    tMirrorSourceNotifGroup.setStatus(
        "current"
    )

tMirrorNotifV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 23)
)
tMirrorNotifV10v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorSourceLiSubProblem"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIpv6FilterChange"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceIPv6FltrChangeRej"))
)
if mibBuilder.loadTexts:
    tMirrorNotifV10v0Group.setStatus(
        "current"
    )

tMirrorNotifV13v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 30)
)
tMirrorNotifV13v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorLiNatLsnSubOperStateCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNatL2awSubOperStateCh"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiNat64SubOperStateCh"))
)
if mibBuilder.loadTexts:
    tMirrorNotifV13v0Group.setStatus(
        "current"
    )

tMirrorNotifV15v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 35)
)
tMirrorNotifV15v0Group.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorLiX2Alarm"),
        ("TIMETRA-MIRROR-MIB", "radiusFailed"))
)
if mibBuilder.loadTexts:
    tMirrorNotifV15v0Group.setStatus(
        "current"
    )

tMirrorLiPrtLicNotifV20v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 2, 50)
)
tMirrorLiPrtLicNotifV20v0Group.setObjects(
    ("TIMETRA-MIRROR-MIB", "tMirrorLiSrcPortLicInvalid")
)
if mibBuilder.loadTexts:
    tMirrorLiPrtLicNotifV20v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tMirrorR2r1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1, 2)
)
tMirrorR2r1Compliance.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1RemoteSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotificationsGroup"))
)
if mibBuilder.loadTexts:
    tMirrorR2r1Compliance.setStatus(
        "obsolete"
    )

tMirrorV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1, 3)
)
tMirrorV6v0Compliance.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1RemoteSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorBsxV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotificationsGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotificationsV6v0Group"))
)
if mibBuilder.loadTexts:
    tMirrorV6v0Compliance.setStatus(
        "obsolete"
    )

tMirrorV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1, 4)
)
tMirrorV8v0Compliance.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1RemoteSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorBsxV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotificationsGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotificationsV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorObsoletedV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorRadiusLiV8v0Group"))
)
if mibBuilder.loadTexts:
    tMirrorV8v0Compliance.setStatus(
        "obsolete"
    )

tMirrorV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1, 5)
)
tMirrorV9v0Compliance.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1RemoteSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorBsxV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotificationsGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotificationsV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorObsoletedV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorRadiusLiV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotifGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiGroup"))
)
if mibBuilder.loadTexts:
    tMirrorV9v0Compliance.setStatus(
        "obsolete"
    )

tMirrorV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1, 6)
)
tMirrorV10v0Compliance.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1RemoteSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorBsxV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotificationsGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotificationsV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorObsoletedV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorRadiusLiV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotifGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorEncapV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationV11v0Group"))
)
if mibBuilder.loadTexts:
    tMirrorV10v0Compliance.setStatus(
        "obsolete"
    )

tMirrorV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1, 7)
)
tMirrorV12v0Compliance.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1RemoteSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorBsxV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotificationsGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotificationsV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorObsoletedV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorRadiusLiV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotifGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorEncapV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV12v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationV11v0Group"))
)
if mibBuilder.loadTexts:
    tMirrorV12v0Compliance.setStatus(
        "obsolete"
    )

tMirrorV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1, 8)
)
tMirrorV13v0Compliance.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1RemoteSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorBsxV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotificationsGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotificationsV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorObsoletedV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorRadiusLiV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotifGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorEncapV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV12v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationV11v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV13v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV13v0Group"))
)
if mibBuilder.loadTexts:
    tMirrorV13v0Compliance.setStatus(
        "obsolete"
    )

tMirrorV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1, 9)
)
tMirrorV14v0Compliance.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1RemoteSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorBsxV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotificationsGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotificationsV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorObsoletedV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorRadiusLiV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotifGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorEncapV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV12v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationV11v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV13v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV13v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiV14v0Group"))
)
if mibBuilder.loadTexts:
    tMirrorV14v0Compliance.setStatus(
        "obsolete"
    )

tMirrorV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1, 10)
)
tMirrorV15v0Compliance.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1RemoteSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorBsxV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotificationsGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotificationsV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorObsoletedV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorRadiusLiV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotifGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorEncapV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV12v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationV11v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV13v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV13v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiV14v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubHostTypeGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceStatsV15v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicV15v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV15v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorServiceNameV15v1Group"))
)
if mibBuilder.loadTexts:
    tMirrorV15v0Compliance.setStatus(
        "obsolete"
    )

tMirrorV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1, 11)
)
tMirrorV16v0Compliance.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1RemoteSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorBsxV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotificationsGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotificationsV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorObsoletedV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorRadiusLiV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotifGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorEncapV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV12v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationV11v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV13v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV13v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiV14v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubHostTypeGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceStatsV15v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicV15v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV15v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorServiceNameV15v1Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicV16v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestPcapV16v0Group"))
)
if mibBuilder.loadTexts:
    tMirrorV16v0Compliance.setStatus(
        "obsolete"
    )

tMirrorV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1, 12)
)
tMirrorV19v0Compliance.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1RemoteSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorBsxV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotificationsGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotificationsV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorObsoletedV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorRadiusLiV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotifGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorEncapV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV12v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationV11v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV13v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV13v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiV14v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubHostTypeGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceStatsV15v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV15v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorServiceNameV15v1Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicV16v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestPcapV16v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV19v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicV19v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiV19v0Group"))
)
if mibBuilder.loadTexts:
    tMirrorV19v0Compliance.setStatus(
        "current"
    )

tMirrorV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 18, 1, 13)
)
tMirrorV20v0Compliance.setObjects(
      *(("TIMETRA-MIRROR-MIB", "tMirrorDestinationV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationR2r1RemoteSourceGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorBsxV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotificationsGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotificationsV6v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorObsoletedV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorRadiusLiV8v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceNotifGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorEncapV10v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV12v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestinationV11v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourceV13v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV13v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiV14v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceSubHostTypeGroup"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceStatsV15v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorNotifV15v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorServiceNameV15v1Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicV16v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestPcapV16v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV19v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLicV19v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiV19v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorDestV20v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorSourceV20v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiSourcePortLicV20v0Group"),
        ("TIMETRA-MIRROR-MIB", "tMirrorLiPrtLicNotifV20v0Group"))
)
if mibBuilder.loadTexts:
    tMirrorV20v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MIRROR-MIB",
    **{"TMplsLabel": TMplsLabel,
       "TEtherType": TEtherType,
       "TSessionId": TSessionId,
       "TmnxMirrorEncapType": TmnxMirrorEncapType,
       "TmnxMirrorDestinationHeaderType": TmnxMirrorDestinationHeaderType,
       "TmnxMirrorGatewayRole": TmnxMirrorGatewayRole,
       "TmnxInterceptionIdentifier": TmnxInterceptionIdentifier,
       "TmnxMirrorLiXIfCorrelationIdOrg": TmnxMirrorLiXIfCorrelationIdOrg,
       "timetraMirrorMIBModule": timetraMirrorMIBModule,
       "tMirrorConformance": tMirrorConformance,
       "tMirrorCompliances": tMirrorCompliances,
       "tMirrorR2r1Compliance": tMirrorR2r1Compliance,
       "tMirrorV6v0Compliance": tMirrorV6v0Compliance,
       "tMirrorV8v0Compliance": tMirrorV8v0Compliance,
       "tMirrorV9v0Compliance": tMirrorV9v0Compliance,
       "tMirrorV10v0Compliance": tMirrorV10v0Compliance,
       "tMirrorV12v0Compliance": tMirrorV12v0Compliance,
       "tMirrorV13v0Compliance": tMirrorV13v0Compliance,
       "tMirrorV14v0Compliance": tMirrorV14v0Compliance,
       "tMirrorV15v0Compliance": tMirrorV15v0Compliance,
       "tMirrorV16v0Compliance": tMirrorV16v0Compliance,
       "tMirrorV19v0Compliance": tMirrorV19v0Compliance,
       "tMirrorV20v0Compliance": tMirrorV20v0Compliance,
       "tMirrorGroups": tMirrorGroups,
       "tMirrorSourceGroup": tMirrorSourceGroup,
       "tMirrorNotificationsGroup": tMirrorNotificationsGroup,
       "tMirrorDestinationR2r1Group": tMirrorDestinationR2r1Group,
       "tMirrorDestinationR2r1RemoteSourceGroup": tMirrorDestinationR2r1RemoteSourceGroup,
       "tMirrorR2r1ObsoleteGroup": tMirrorR2r1ObsoleteGroup,
       "tMirrorNotifyObjsV5v0Group": tMirrorNotifyObjsV5v0Group,
       "tMirrorDestinationV6v0Group": tMirrorDestinationV6v0Group,
       "tMirrorSourceV6v0Group": tMirrorSourceV6v0Group,
       "tMirrorNotifyObjsV6v0Group": tMirrorNotifyObjsV6v0Group,
       "tMirrorSourceNotificationsV6v0Group": tMirrorSourceNotificationsV6v0Group,
       "tMirrorBsxV6v0Group": tMirrorBsxV6v0Group,
       "tMirrorDestV8v0Group": tMirrorDestV8v0Group,
       "tMirrorObsoletedV8v0Group": tMirrorObsoletedV8v0Group,
       "tMirrorDestinationV8v0Group": tMirrorDestinationV8v0Group,
       "tMirrorRadiusLiV8v0Group": tMirrorRadiusLiV8v0Group,
       "tMirrorSourceNotifGroup": tMirrorSourceNotifGroup,
       "tMirrorLiGroup": tMirrorLiGroup,
       "tMirrorEncapGroup": tMirrorEncapGroup,
       "tMirrorNotifyObjsV10v0Group": tMirrorNotifyObjsV10v0Group,
       "tMirrorNotifV10v0Group": tMirrorNotifV10v0Group,
       "tMirrorSourceV10v0Group": tMirrorSourceV10v0Group,
       "tMirrorEncapV10v0Group": tMirrorEncapV10v0Group,
       "tMirrorLiSourceV10v0Group": tMirrorLiSourceV10v0Group,
       "tMirrorDestinationV11v0Group": tMirrorDestinationV11v0Group,
       "tMirrorLiSourceV12v0Group": tMirrorLiSourceV12v0Group,
       "tMirrorLiSourceV13v0Group": tMirrorLiSourceV13v0Group,
       "tMirrorNotifV13v0Group": tMirrorNotifV13v0Group,
       "tMirrorLiV14v0Group": tMirrorLiV14v0Group,
       "tMirrorSourceSubHostTypeGroup": tMirrorSourceSubHostTypeGroup,
       "tMirrorSourceStatsV15v0Group": tMirrorSourceStatsV15v0Group,
       "tMirrorLicV15v0Group": tMirrorLicV15v0Group,
       "tMirrorNotifV15v0Group": tMirrorNotifV15v0Group,
       "tMirrorNotifyObjsV15v0Group": tMirrorNotifyObjsV15v0Group,
       "tMirrorServiceNameV15v1Group": tMirrorServiceNameV15v1Group,
       "tMirrorLicV16v0Group": tMirrorLicV16v0Group,
       "tMirrorDestPcapV16v0Group": tMirrorDestPcapV16v0Group,
       "tMirrorSourceV19v0Group": tMirrorSourceV19v0Group,
       "tMirrorLicV19v0Group": tMirrorLicV19v0Group,
       "tMirrorObsoletedV19v0Group": tMirrorObsoletedV19v0Group,
       "tMirrorLiV19v0Group": tMirrorLiV19v0Group,
       "tMirrorDestV20v0Group": tMirrorDestV20v0Group,
       "tMirrorSourceV20v0Group": tMirrorSourceV20v0Group,
       "tMirrorLiSourcePortLicV20v0Group": tMirrorLiSourcePortLicV20v0Group,
       "tMirrorLiPrtLicNotifV20v0Group": tMirrorLiPrtLicNotifV20v0Group,
       "tMirrorObjects": tMirrorObjects,
       "tMirrorDestinationObjects": tMirrorDestinationObjects,
       "tMirrorDestinationTable": tMirrorDestinationTable,
       "tMirrorDestinationEntry": tMirrorDestinationEntry,
       "tMirrorDestinationIndex": tMirrorDestinationIndex,
       "tMirrorDestinationRowStatus": tMirrorDestinationRowStatus,
       "tMirrorDestinationDescription": tMirrorDestinationDescription,
       "tMirrorDestinationFC": tMirrorDestinationFC,
       "tMirrorDestinationRemoteSource": tMirrorDestinationRemoteSource,
       "tMirrorDestinationSapPortId": tMirrorDestinationSapPortId,
       "tMirrorDestinationSapEncapValue": tMirrorDestinationSapEncapValue,
       "tMirrorDestinationSdpNumber": tMirrorDestinationSdpNumber,
       "tMirrorDestinationSdpDestEncap": tMirrorDestinationSdpDestEncap,
       "tMirrorDestinationAdminStatus": tMirrorDestinationAdminStatus,
       "tMirrorDestinationOperStatus": tMirrorDestinationOperStatus,
       "tMirrorDestinationTranslateDisable": tMirrorDestinationTranslateDisable,
       "tMirrorDestinationSliceSize": tMirrorDestinationSliceSize,
       "tMirrorDestinationPppoeDestMacAddr": tMirrorDestinationPppoeDestMacAddr,
       "tMirrorDestinationPppoeSrcMacAddr": tMirrorDestinationPppoeSrcMacAddr,
       "tMirrorDestinationPppoeEtype": tMirrorDestinationPppoeEtype,
       "tMirrorDestinationPppoeSessionId": tMirrorDestinationPppoeSessionId,
       "tMirrorDestinationSdpEgrSvcLabel": tMirrorDestinationSdpEgrSvcLabel,
       "tMirrorDestinationSapEgressQosPolicyId": tMirrorDestinationSapEgressQosPolicyId,
       "tMirrorDestinationEncapsulation": tMirrorDestinationEncapsulation,
       "tMirrorDestinationSdpOperEgrSvcLabel": tMirrorDestinationSdpOperEgrSvcLabel,
       "tMirrorDestinationEnablePortId": tMirrorDestinationEnablePortId,
       "tMirrorDestSapEgrIpMirrorSA": tMirrorDestSapEgrIpMirrorSA,
       "tMirrorDestSapEgrIpMirrorDA": tMirrorDestSapEgrIpMirrorDA,
       "tMirrorDestLastChanged": tMirrorDestLastChanged,
       "tMirrorDestSapEgrPortQGrp": tMirrorDestSapEgrPortQGrp,
       "tMirrorDestSapEgrPortQGrpInstId": tMirrorDestSapEgrPortQGrpInstId,
       "tMirrorDestCreationOrigin": tMirrorDestCreationOrigin,
       "tMirrorDestinationName": tMirrorDestinationName,
       "tMirrorDestPcapSessionName": tMirrorDestPcapSessionName,
       "tMirrorDestSamplingRate": tMirrorDestSamplingRate,
       "tMirrorDestinationRemoteSourceTable": tMirrorDestinationRemoteSourceTable,
       "tMirrorDestinationRemoteSourceEntry": tMirrorDestinationRemoteSourceEntry,
       "tMirrorDestinationRemoteSourceAddr": tMirrorDestinationRemoteSourceAddr,
       "tMirrorDestinationRemoteSourceLabelSignaling": tMirrorDestinationRemoteSourceLabelSignaling,
       "tMirrorDestinationRemoteSourceIngSvcLabel": tMirrorDestinationRemoteSourceIngSvcLabel,
       "tMirrorDestinationRemoteSourceRowStatus": tMirrorDestinationRemoteSourceRowStatus,
       "tMirrorDestinationRemoteSourceOperIngSvcLabel": tMirrorDestinationRemoteSourceOperIngSvcLabel,
       "tMirrorDestRemoteSrcLastChgd": tMirrorDestRemoteSrcLastChgd,
       "tMirrorDestRemoteSrcIsICB": tMirrorDestRemoteSrcIsICB,
       "tMirrorDestRemoteSrcVcId": tMirrorDestRemoteSrcVcId,
       "tMirrorDestTableLastChnged": tMirrorDestTableLastChnged,
       "tMirrorDestRemSrcTblLastChgd": tMirrorDestRemSrcTblLastChgd,
       "tMirrorDestL3EncTableLastCh": tMirrorDestL3EncTableLastCh,
       "tMirrorDestL3EncTable": tMirrorDestL3EncTable,
       "tMirrorDestL3EncEntry": tMirrorDestL3EncEntry,
       "tMirrorDestL3EncRowStatus": tMirrorDestL3EncRowStatus,
       "tMirrorDestL3EncLastCh": tMirrorDestL3EncLastCh,
       "tMirrorDestL3EncHeaderType": tMirrorDestL3EncHeaderType,
       "tMirrorDestL3EncRouter": tMirrorDestL3EncRouter,
       "tMirrorDestL3EncUseDirectionBit": tMirrorDestL3EncUseDirectionBit,
       "tMirrorDestL3GwTableLastCh": tMirrorDestL3GwTableLastCh,
       "tMirrorDestL3GwTable": tMirrorDestL3GwTable,
       "tMirrorDestL3GwEntry": tMirrorDestL3GwEntry,
       "tMirrorDestL3GwRole": tMirrorDestL3GwRole,
       "tMirrorDestL3GwRowStatus": tMirrorDestL3GwRowStatus,
       "tMirrorDestL3GwLastCh": tMirrorDestL3GwLastCh,
       "tMirrorDestL3GwSrcAddrType": tMirrorDestL3GwSrcAddrType,
       "tMirrorDestL3GwSrcAddr": tMirrorDestL3GwSrcAddr,
       "tMirrorDestL3GwDstAddrType": tMirrorDestL3GwDstAddrType,
       "tMirrorDestL3GwDstAddr": tMirrorDestL3GwDstAddr,
       "tMirrorDestL3GwUdpSrcPort": tMirrorDestL3GwUdpSrcPort,
       "tMirrorDestL3GwUdpDstPort": tMirrorDestL3GwUdpDstPort,
       "tMirrorSourceObjects": tMirrorSourceObjects,
       "tMirrorSourceTable": tMirrorSourceTable,
       "tMirrorSourceEntry": tMirrorSourceEntry,
       "tMirrorSourceIndex": tMirrorSourceIndex,
       "tMirrorSourceAdminStatus": tMirrorSourceAdminStatus,
       "tMirrorSourceRowStatus": tMirrorSourceRowStatus,
       "tMirrorSourceLastChgd": tMirrorSourceLastChgd,
       "tMirrorSourceCreationOrigin": tMirrorSourceCreationOrigin,
       "tMirrorSourceName": tMirrorSourceName,
       "tMirrorSourceIpFilterTable": tMirrorSourceIpFilterTable,
       "tMirrorSourceIpFilterEntry": tMirrorSourceIpFilterEntry,
       "tMirrorSourceIpFilter": tMirrorSourceIpFilter,
       "tMirrorSourceIpFilterParams": tMirrorSourceIpFilterParams,
       "tMirrorSourceIpFilterRowStatus": tMirrorSourceIpFilterRowStatus,
       "tMirrorSourceIpFilterLastChgd": tMirrorSourceIpFilterLastChgd,
       "tMirrorSourceIpFilterIntceptId": tMirrorSourceIpFilterIntceptId,
       "tMirrorSourceIpFilterSessionId": tMirrorSourceIpFilterSessionId,
       "tMirrorSourceMacFilterTable": tMirrorSourceMacFilterTable,
       "tMirrorSourceMacFilterEntry": tMirrorSourceMacFilterEntry,
       "tMirrorSourceMacFilter": tMirrorSourceMacFilter,
       "tMirrorSourceMacFilterParams": tMirrorSourceMacFilterParams,
       "tMirrorSourceMacFilterRowStatus": tMirrorSourceMacFilterRowStatus,
       "tMirrorSourceMacFilterLastChgd": tMirrorSourceMacFilterLastChgd,
       "tMirrorSourceMacFilterIntceptId": tMirrorSourceMacFilterIntceptId,
       "tMirrorSourceMacFilterSessionId": tMirrorSourceMacFilterSessionId,
       "tMirrorSourceIngressLabelTable": tMirrorSourceIngressLabelTable,
       "tMirrorSourceIngressLabelEntry": tMirrorSourceIngressLabelEntry,
       "tMirrorSourceIngressLabelIndex": tMirrorSourceIngressLabelIndex,
       "tMirrorSourceIngressLabelRowStatus": tMirrorSourceIngressLabelRowStatus,
       "tMirrorSourceIngLabelLastChgd": tMirrorSourceIngLabelLastChgd,
       "tMirrorSourcePortTable": tMirrorSourcePortTable,
       "tMirrorSourcePortEntry": tMirrorSourcePortEntry,
       "tMirrorSourcePortIndex": tMirrorSourcePortIndex,
       "tMirrorSourcePortRowStatus": tMirrorSourcePortRowStatus,
       "tMirrorSourcePortEgressEnabled": tMirrorSourcePortEgressEnabled,
       "tMirrorSourcePortIngressEnabled": tMirrorSourcePortIngressEnabled,
       "tMirrorSourcePortLastChgd": tMirrorSourcePortLastChgd,
       "tMirrorSourcePortLicenseState": tMirrorSourcePortLicenseState,
       "tMirrorSourceSapTable": tMirrorSourceSapTable,
       "tMirrorSourceSapEntry": tMirrorSourceSapEntry,
       "tMirrorSourceSapPortId": tMirrorSourceSapPortId,
       "tMirrorSourceSapEncapValue": tMirrorSourceSapEncapValue,
       "tMirrorSourceSapRowStatus": tMirrorSourceSapRowStatus,
       "tMirrorSourceSapEgressEnabled": tMirrorSourceSapEgressEnabled,
       "tMirrorSourceSapIngressEnabled": tMirrorSourceSapIngressEnabled,
       "tMirrorSourceSapLastChgd": tMirrorSourceSapLastChgd,
       "tMirrorSourceSapIntceptId": tMirrorSourceSapIntceptId,
       "tMirrorSourceSapSessionId": tMirrorSourceSapSessionId,
       "tMirrorSourceSubTableLastChnged": tMirrorSourceSubTableLastChnged,
       "tMirrorSourceSubscriberTable": tMirrorSourceSubscriberTable,
       "tMirrorSourceSubscriberEntry": tMirrorSourceSubscriberEntry,
       "tMirrorSourceSubIdent": tMirrorSourceSubIdent,
       "tMirrorSourceSubRowStatus": tMirrorSourceSubRowStatus,
       "tMirrorSourceSubLastChanged": tMirrorSourceSubLastChanged,
       "tMirrorSourceSubPortId": tMirrorSourceSubPortId,
       "tMirrorSourceSubEncapValue": tMirrorSourceSubEncapValue,
       "tMirrorSourceSubIpAddrType": tMirrorSourceSubIpAddrType,
       "tMirrorSourceSubIpAddr": tMirrorSourceSubIpAddr,
       "tMirrorSourceSubMacAddr": tMirrorSourceSubMacAddr,
       "tMirrorSourceSubSLAProfName": tMirrorSourceSubSLAProfName,
       "tMirrorSourceSubFC": tMirrorSourceSubFC,
       "tMirrorSourceSubEgressEnabled": tMirrorSourceSubEgressEnabled,
       "tMirrorSourceSubIngressEnabled": tMirrorSourceSubIngressEnabled,
       "tMirrorSourceSubIntceptId": tMirrorSourceSubIntceptId,
       "tMirrorSourceSubSessionId": tMirrorSourceSubSessionId,
       "tMirrorSourceSubHostType": tMirrorSourceSubHostType,
       "tMirrorSourceSubIpFamily": tMirrorSourceSubIpFamily,
       "tMirrorSourceIsaAaGrpTable": tMirrorSourceIsaAaGrpTable,
       "tMirrorSourceIsaAaGrpEntry": tMirrorSourceIsaAaGrpEntry,
       "tMirrorSourceIsaAaGrpIndex": tMirrorSourceIsaAaGrpIndex,
       "tMirrorSourceIsaAaGrpRowStatus": tMirrorSourceIsaAaGrpRowStatus,
       "tMirrorSourceIsaAaGrpUnknownOnly": tMirrorSourceIsaAaGrpUnknownOnly,
       "tMirrorSourceIsaAaGrpLastChgd": tMirrorSourceIsaAaGrpLastChgd,
       "tMirrorSrcTblLastChgd": tMirrorSrcTblLastChgd,
       "tMirrorSrcIpFltrTblLastChgd": tMirrorSrcIpFltrTblLastChgd,
       "tMirrorSrcMacFltrTblLastChgd": tMirrorSrcMacFltrTblLastChgd,
       "tMirrorSrcIngLblTblLastChgd": tMirrorSrcIngLblTblLastChgd,
       "tMirrorSrcPortTblLastChgd": tMirrorSrcPortTblLastChgd,
       "tMirrorSrcSapTblLastChgd": tMirrorSrcSapTblLastChgd,
       "tMirrorSrcIsaAaGrpTblLastChgd": tMirrorSrcIsaAaGrpTblLastChgd,
       "tMirrorSourceIpv6FilterTable": tMirrorSourceIpv6FilterTable,
       "tMirrorSourceIpv6FilterEntry": tMirrorSourceIpv6FilterEntry,
       "tMirrorSourceIpv6Filter": tMirrorSourceIpv6Filter,
       "tMirrorSourceIpv6FilterParams": tMirrorSourceIpv6FilterParams,
       "tMirrorSourceIpv6FilterRowStatus": tMirrorSourceIpv6FilterRowStatus,
       "tMirrorSourceIpv6FilterLastChgd": tMirrorSourceIpv6FilterLastChgd,
       "tMirrorSourceIpv6FilterIntceptId": tMirrorSourceIpv6FilterIntceptId,
       "tMirrorSourceIpv6FilterSessionId": tMirrorSourceIpv6FilterSessionId,
       "tMirrorSourceStatsTable": tMirrorSourceStatsTable,
       "tMirrorSourceStatsEntry": tMirrorSourceStatsEntry,
       "tMirrorSourceStatsTotalSrc": tMirrorSourceStatsTotalSrc,
       "tMirrorSourcePortVlanTable": tMirrorSourcePortVlanTable,
       "tMirrorSourcePortVlanEntry": tMirrorSourcePortVlanEntry,
       "tMirrorSourcePortVlanPortId": tMirrorSourcePortVlanPortId,
       "tMirrorSourcePortVlanVlan": tMirrorSourcePortVlanVlan,
       "tMirrorSourcePortVlanRowStatus": tMirrorSourcePortVlanRowStatus,
       "tMirrorSourcePortVlanEgrEnabled": tMirrorSourcePortVlanEgrEnabled,
       "tMirrorSourcePortVlanIngEnabled": tMirrorSourcePortVlanIngEnabled,
       "tMirrorSourcePortVlanLastChgd": tMirrorSourcePortVlanLastChgd,
       "tMirrorSrcPortVlanTblLastChgd": tMirrorSrcPortVlanTblLastChgd,
       "tMirrorSourceSapShimTable": tMirrorSourceSapShimTable,
       "tMirrorSourceSapShimEntry": tMirrorSourceSapShimEntry,
       "tMirrorSourceSapShimPortId": tMirrorSourceSapShimPortId,
       "tMirrorSourceSapShimEncapValue": tMirrorSourceSapShimEncapValue,
       "tMirrorSourceSapShimId": tMirrorSourceSapShimId,
       "tMirrorSourceNotifyObjects": tMirrorSourceNotifyObjects,
       "tMirrorSourceChangeType": tMirrorSourceChangeType,
       "tMirrorSourceFilterId": tMirrorSourceFilterId,
       "tMirrorSourceFilterEntryId": tMirrorSourceFilterEntryId,
       "tMirrorSourceFilterObject": tMirrorSourceFilterObject,
       "tMirrorSourceFilterDescr": tMirrorSourceFilterDescr,
       "tMirrorFilterSvcId": tMirrorFilterSvcId,
       "tMirrorFilterPortId": tMirrorFilterPortId,
       "tMirrorFilterSapEncapValue": tMirrorFilterSapEncapValue,
       "tMirrorFilterSdpBindId": tMirrorFilterSdpBindId,
       "tMirrorFilterType": tMirrorFilterType,
       "tMirrorFilterDirection": tMirrorFilterDirection,
       "tMirrorFilterId": tMirrorFilterId,
       "tMirrorFilterIfIndex": tMirrorFilterIfIndex,
       "tMirrorFilterIfName": tMirrorFilterIfName,
       "tMirrorRadiusLiObjects": tMirrorRadiusLiObjects,
       "tMirrorRadiusLiTable": tMirrorRadiusLiTable,
       "tMirrorRadiusLiEntry": tMirrorRadiusLiEntry,
       "tRadiusLiMirrorDestinationIndex": tRadiusLiMirrorDestinationIndex,
       "tRadiusLiSrcHostServiceId": tRadiusLiSrcHostServiceId,
       "tRadiusLiSrcHostSapPortId": tRadiusLiSrcHostSapPortId,
       "tRadiusLiSrcHostsapEncapValue": tRadiusLiSrcHostsapEncapValue,
       "tRadiusLiSrcHostIpAddrType": tRadiusLiSrcHostIpAddrType,
       "tRadiusLiSrcHostIpAddr": tRadiusLiSrcHostIpAddr,
       "tRadiusLiSrcHostMacAddr": tRadiusLiSrcHostMacAddr,
       "tRadiusLiSrcHostPppoeSessionId": tRadiusLiSrcHostPppoeSessionId,
       "tRadiusLiSrcHostId": tRadiusLiSrcHostId,
       "tRadiusLiMirrorDirection": tRadiusLiMirrorDirection,
       "tRadiusLiMirrorForwClassMap": tRadiusLiMirrorForwClassMap,
       "tRadiusLiSrcIntceptId": tRadiusLiSrcIntceptId,
       "tRadiusLiSrcSessionId": tRadiusLiSrcSessionId,
       "tRadiusLiSrcNatUsingOutsideIp": tRadiusLiSrcNatUsingOutsideIp,
       "tMirrorLiDestTmplTable": tMirrorLiDestTmplTable,
       "tMirrorLiDestTmplEntry": tMirrorLiDestTmplEntry,
       "tMirrorLiDestTmplName": tMirrorLiDestTmplName,
       "tMirrorLiDestTmplLastChanged": tMirrorLiDestTmplLastChanged,
       "tMirrorLiDestTmplRowStatus": tMirrorLiDestTmplRowStatus,
       "tMirrorLiDestTmplEncapsulation": tMirrorLiDestTmplEncapsulation,
       "tMirrorLiDestTmplL3EncHeaderType": tMirrorLiDestTmplL3EncHeaderType,
       "tMirrorLiDestTmplL3EncUseDirect": tMirrorLiDestTmplL3EncUseDirect,
       "tMirrorLiDestTmplL3EncRouter": tMirrorLiDestTmplL3EncRouter,
       "tMirrorLiDestTmplL3SrcAddrType": tMirrorLiDestTmplL3SrcAddrType,
       "tMirrorLiDestTmplL3SrcAddr": tMirrorLiDestTmplL3SrcAddr,
       "tMirrorLiDestTmplL3UdpSrcPort": tMirrorLiDestTmplL3UdpSrcPort,
       "tMirrorLiDestTmplL3UdpDstPort": tMirrorLiDestTmplL3UdpDstPort,
       "tMirrorLiDestTmplL3EncRouterName": tMirrorLiDestTmplL3EncRouterName,
       "tMirrorLiDestServiceRange": tMirrorLiDestServiceRange,
       "tMirrorLiDestServiceRangeStart": tMirrorLiDestServiceRangeStart,
       "tMirrorLiDestServiceRangeEnd": tMirrorLiDestServiceRangeEnd,
       "tMirrorRadiusLiCfg": tMirrorRadiusLiCfg,
       "tMirrorRadiusLiCfgDestTmpl": tMirrorRadiusLiCfgDestTmpl,
       "tMirrorLiObjects": tMirrorLiObjects,
       "tMirrorLiSourceNatTableLastCh": tMirrorLiSourceNatTableLastCh,
       "tMirrorLiNatLsnSubTableLastCh": tMirrorLiNatLsnSubTableLastCh,
       "tMirrorLiNatL2awSubTableLastCh": tMirrorLiNatL2awSubTableLastCh,
       "tMirrorSourceLiMacFltrTableLstCh": tMirrorSourceLiMacFltrTableLstCh,
       "tMirrorLiNat64SubTableLastCh": tMirrorLiNat64SubTableLastCh,
       "tMirrorSourceLiIpFltrTableLstCh": tMirrorSourceLiIpFltrTableLstCh,
       "tMirrorLiDsmSubTableLastCh": tMirrorLiDsmSubTableLastCh,
       "tMirrorLiDestTmplTableLastCh": tMirrorLiDestTmplTableLastCh,
       "tMirrorLiSourceNatTable": tMirrorLiSourceNatTable,
       "tMirrorLiSourceNatEntry": tMirrorLiSourceNatEntry,
       "tMirrorLiSourceNatLastChanged": tMirrorLiSourceNatLastChanged,
       "tMirrorLiSourceNatDestMacAddr": tMirrorLiSourceNatDestMacAddr,
       "tMirrorLiSourceNatSrcMacAddr": tMirrorLiSourceNatSrcMacAddr,
       "tMirrorLiSourceNatEthertype": tMirrorLiSourceNatEthertype,
       "tMirrorLiNatLsnSubTable": tMirrorLiNatLsnSubTable,
       "tMirrorLiNatLsnSubEntry": tMirrorLiNatLsnSubEntry,
       "tMirrorLiNatLsnSubAddrType": tMirrorLiNatLsnSubAddrType,
       "tMirrorLiNatLsnSubAddr": tMirrorLiNatLsnSubAddr,
       "tMirrorLiNatLsnSubPrefixLength": tMirrorLiNatLsnSubPrefixLength,
       "tMirrorLiNatLsnSubRowStatus": tMirrorLiNatLsnSubRowStatus,
       "tMirrorLiNatLsnSubLastChanged": tMirrorLiNatLsnSubLastChanged,
       "tMirrorLiNatLsnSubInterceptId": tMirrorLiNatLsnSubInterceptId,
       "tMirrorLiNatLsnSubSessionId": tMirrorLiNatLsnSubSessionId,
       "tMirrorLiNatLsnSubOperState": tMirrorLiNatLsnSubOperState,
       "tMirrorLiNatL2awSubTable": tMirrorLiNatL2awSubTable,
       "tMirrorLiNatL2awSubEntry": tMirrorLiNatL2awSubEntry,
       "tMirrorLiNatL2awSubIdent": tMirrorLiNatL2awSubIdent,
       "tMirrorLiNatL2awSubRowStatus": tMirrorLiNatL2awSubRowStatus,
       "tMirrorLiNatL2awSubLastChanged": tMirrorLiNatL2awSubLastChanged,
       "tMirrorLiNatL2awSubInterceptId": tMirrorLiNatL2awSubInterceptId,
       "tMirrorLiNatL2awSubSessionId": tMirrorLiNatL2awSubSessionId,
       "tMirrorLiNatL2awSubOperState": tMirrorLiNatL2awSubOperState,
       "tMirrorSourceLiMacFltrTable": tMirrorSourceLiMacFltrTable,
       "tMirrorSourceLiMacFltrEntry": tMirrorSourceLiMacFltrEntry,
       "tMirrorSourceLiMacFltr": tMirrorSourceLiMacFltr,
       "tMirrorSourceLiMacFltrParams": tMirrorSourceLiMacFltrParams,
       "tMirrorSourceLiMacFltrRowStatus": tMirrorSourceLiMacFltrRowStatus,
       "tMirrorSourceLiMacFltrLastChgd": tMirrorSourceLiMacFltrLastChgd,
       "tMirrorSourceLiMacFltrIntceptId": tMirrorSourceLiMacFltrIntceptId,
       "tMirrorSourceLiMacFltrSessionId": tMirrorSourceLiMacFltrSessionId,
       "tMirrorLiNat64SubTable": tMirrorLiNat64SubTable,
       "tMirrorLiNat64SubEntry": tMirrorLiNat64SubEntry,
       "tMirrorLiNat64SubAddrType": tMirrorLiNat64SubAddrType,
       "tMirrorLiNat64SubAddr": tMirrorLiNat64SubAddr,
       "tMirrorLiNat64SubPrefixLength": tMirrorLiNat64SubPrefixLength,
       "tMirrorLiNat64SubRowStatus": tMirrorLiNat64SubRowStatus,
       "tMirrorLiNat64SubLastChanged": tMirrorLiNat64SubLastChanged,
       "tMirrorLiNat64SubInterceptId": tMirrorLiNat64SubInterceptId,
       "tMirrorLiNat64SubSessionId": tMirrorLiNat64SubSessionId,
       "tMirrorLiNat64SubOperState": tMirrorLiNat64SubOperState,
       "tMirrorLiNatLsnSub2TableLastCh": tMirrorLiNatLsnSub2TableLastCh,
       "tMirrorLiNatLsnSub2Table": tMirrorLiNatLsnSub2Table,
       "tMirrorLiNatLsnSub2Entry": tMirrorLiNatLsnSub2Entry,
       "tMirrorLiNatLsnSub2RouterName": tMirrorLiNatLsnSub2RouterName,
       "tMirrorLiNatLsnSub2AddrType": tMirrorLiNatLsnSub2AddrType,
       "tMirrorLiNatLsnSub2Addr": tMirrorLiNatLsnSub2Addr,
       "tMirrorLiNatLsnSub2PrefixLength": tMirrorLiNatLsnSub2PrefixLength,
       "tMirrorLiNatLsnSub2RowStatus": tMirrorLiNatLsnSub2RowStatus,
       "tMirrorLiNatLsnSub2LastChanged": tMirrorLiNatLsnSub2LastChanged,
       "tMirrorLiNatLsnSub2InterceptId": tMirrorLiNatLsnSub2InterceptId,
       "tMirrorLiNatLsnSub2SessionId": tMirrorLiNatLsnSub2SessionId,
       "tMirrorLiNatLsnSub2OperState": tMirrorLiNatLsnSub2OperState,
       "tMirrorLiNat64Sub2TableLastCh": tMirrorLiNat64Sub2TableLastCh,
       "tMirrorLiNat64Sub2Table": tMirrorLiNat64Sub2Table,
       "tMirrorLiNat64Sub2Entry": tMirrorLiNat64Sub2Entry,
       "tMirrorLiNat64Sub2RouterName": tMirrorLiNat64Sub2RouterName,
       "tMirrorLiNat64Sub2AddrType": tMirrorLiNat64Sub2AddrType,
       "tMirrorLiNat64Sub2Addr": tMirrorLiNat64Sub2Addr,
       "tMirrorLiNat64Sub2PrefixLength": tMirrorLiNat64Sub2PrefixLength,
       "tMirrorLiNat64Sub2RowStatus": tMirrorLiNat64Sub2RowStatus,
       "tMirrorLiNat64Sub2LastChanged": tMirrorLiNat64Sub2LastChanged,
       "tMirrorLiNat64Sub2InterceptId": tMirrorLiNat64Sub2InterceptId,
       "tMirrorLiNat64Sub2SessionId": tMirrorLiNat64Sub2SessionId,
       "tMirrorLiNat64Sub2OperState": tMirrorLiNat64Sub2OperState,
       "tMirrorSourceLiIpFltrTable": tMirrorSourceLiIpFltrTable,
       "tMirrorSourceLiIpFltrEntry": tMirrorSourceLiIpFltrEntry,
       "tMirrorSourceLiIpFltrType": tMirrorSourceLiIpFltrType,
       "tMirrorSourceLiIpFltr": tMirrorSourceLiIpFltr,
       "tMirrorSourceLiIpFltrParams": tMirrorSourceLiIpFltrParams,
       "tMirrorSourceLiIpFltrRowStatus": tMirrorSourceLiIpFltrRowStatus,
       "tMirrorSourceLiIpFltrLastChgd": tMirrorSourceLiIpFltrLastChgd,
       "tMirrorSourceLiIpFltrIntceptId": tMirrorSourceLiIpFltrIntceptId,
       "tMirrorSourceLiIpFltrSessionId": tMirrorSourceLiIpFltrSessionId,
       "tMirrorLiDsmSubTable": tMirrorLiDsmSubTable,
       "tMirrorLiDsmSubEntry": tMirrorLiDsmSubEntry,
       "tMirrorLiDsmSubMacAddress": tMirrorLiDsmSubMacAddress,
       "tMirrorLiDsmSubRowStatus": tMirrorLiDsmSubRowStatus,
       "tMirrorLiDsmSubLastChanged": tMirrorLiDsmSubLastChanged,
       "tMirrorLiDsmSubInterceptId": tMirrorLiDsmSubInterceptId,
       "tMirrorLiDsmSubSessionId": tMirrorLiDsmSubSessionId,
       "tMirrorLiCfg": tMirrorLiCfg,
       "tMirrorLiCfgNatUseOutsideIpAddr": tMirrorLiCfgNatUseOutsideIpAddr,
       "tMirrorLiCfgXIfTgtPersistFileLoc": tMirrorLiCfgXIfTgtPersistFileLoc,
       "tMirrorLiXIf": tMirrorLiXIf,
       "tMirrorLicTableLastCh": tMirrorLicTableLastCh,
       "tMirrorLicTable": tMirrorLicTable,
       "tMirrorLicEntry": tMirrorLicEntry,
       "tMirrorLicName": tMirrorLicName,
       "tMirrorLicLastChanged": tMirrorLicLastChanged,
       "tMirrorLicRowStatus": tMirrorLicRowStatus,
       "tMirrorLicDescription": tMirrorLicDescription,
       "tMirrorLicIdentifier": tMirrorLicIdentifier,
       "tMirrorLicRouter": tMirrorLicRouter,
       "tMirrorLicIpAddrType": tMirrorLicIpAddrType,
       "tMirrorLicIpAddr": tMirrorLicIpAddr,
       "tMirrorLicPort": tMirrorLicPort,
       "tMirrorLicAuthPrivateKi": tMirrorLicAuthPrivateKi,
       "tMirrorLicAuthPassword": tMirrorLicAuthPassword,
       "tMirrorLicAuthSequenceGroup": tMirrorLicAuthSequenceGroup,
       "tMirrorIneIdentifier": tMirrorIneIdentifier,
       "tMirrorLiXIfAdminState": tMirrorLiXIfAdminState,
       "tMirrorLiXIfUserDb": tMirrorLiXIfUserDb,
       "tMirrorLiXIfCorrelationIdIpoe": tMirrorLiXIfCorrelationIdIpoe,
       "tMirrorLiXIfCorrelationIdPppoe": tMirrorLiXIfCorrelationIdPppoe,
       "tMirrorLiX1": tMirrorLiX1,
       "tMirrorLiX1LastCh": tMirrorLiX1LastCh,
       "tMirrorLiX1PeerLic": tMirrorLiX1PeerLic,
       "tMirrorLiX1IpAddrType": tMirrorLiX1IpAddrType,
       "tMirrorLiX1IpAddr": tMirrorLiX1IpAddr,
       "tMirrorLiX1Port": tMirrorLiX1Port,
       "tMirrorLiX1ToNoMsg": tMirrorLiX1ToNoMsg,
       "tMirrorLiX1OperState": tMirrorLiX1OperState,
       "tMirrorLiX2": tMirrorLiX2,
       "tMirrorLiX2LastCh": tMirrorLiX2LastCh,
       "tMirrorLiX2PeerLic": tMirrorLiX2PeerLic,
       "tMirrorLiX2IpAddrType": tMirrorLiX2IpAddrType,
       "tMirrorLiX2IpAddr": tMirrorLiX2IpAddr,
       "tMirrorLiX2ToConnectionReq": tMirrorLiX2ToConnectionReq,
       "tMirrorLiX2ToKeepalive": tMirrorLiX2ToKeepalive,
       "tMirrorLiX2OperState": tMirrorLiX2OperState,
       "tMirrorLiX3": tMirrorLiX3,
       "tMirrorLiX3LastCh": tMirrorLiX3LastCh,
       "tMirrorLiX3LiGroup": tMirrorLiX3LiGroup,
       "tMirrorLiX3StartIpAddrType": tMirrorLiX3StartIpAddrType,
       "tMirrorLiX3StartIpAddr": tMirrorLiX3StartIpAddr,
       "tMirrorLiX3EndIpAddrType": tMirrorLiX3EndIpAddrType,
       "tMirrorLiX3EndIpAddr": tMirrorLiX3EndIpAddr,
       "tMirrorLiX3MaxNumSessions": tMirrorLiX3MaxNumSessions,
       "tMirrorLiX3ToTunnelReq": tMirrorLiX3ToTunnelReq,
       "tMirrorLiX3ToKeepalive": tMirrorLiX3ToKeepalive,
       "tMirrorLiX3ToTargetRetryWait": tMirrorLiX3ToTargetRetryWait,
       "tMirrorLiX3CpuAlarm": tMirrorLiX3CpuAlarm,
       "tMirrorLiX3CpuAlarmHighThreshold": tMirrorLiX3CpuAlarmHighThreshold,
       "tMirrorLiX3CpuAlarmLowThreshold": tMirrorLiX3CpuAlarmLowThreshold,
       "tMirrorLiX3MemAlarm": tMirrorLiX3MemAlarm,
       "tMirrorLiX3MemAlarmHighThreshold": tMirrorLiX3MemAlarmHighThreshold,
       "tMirrorLiX3MemAlarmLowThreshold": tMirrorLiX3MemAlarmLowThreshold,
       "tMirrorLiX3BwAlarm": tMirrorLiX3BwAlarm,
       "tMirrorLiX3BwAlarmHighThreshold": tMirrorLiX3BwAlarmHighThreshold,
       "tMirrorLiX3BwAlarmLowThreshold": tMirrorLiX3BwAlarmLowThreshold,
       "tMirrorLiX3OperState": tMirrorLiX3OperState,
       "tMirrorLiX3PeerTableLastCh": tMirrorLiX3PeerTableLastCh,
       "tMirrorLiX3PeerTable": tMirrorLiX3PeerTable,
       "tMirrorLiX3PeerEntry": tMirrorLiX3PeerEntry,
       "tMirrorLiX3PeerName": tMirrorLiX3PeerName,
       "tMirrorLiX3PeerLastChanged": tMirrorLiX3PeerLastChanged,
       "tMirrorLiX3PeerRowStatus": tMirrorLiX3PeerRowStatus,
       "tMirrorLiX1StatsTable": tMirrorLiX1StatsTable,
       "tMirrorLiX1StatsEntry": tMirrorLiX1StatsEntry,
       "tMirrorLiX1RxMessages": tMirrorLiX1RxMessages,
       "tMirrorLiX1TxMessages": tMirrorLiX1TxMessages,
       "tMirrorLiX1RxKBytes": tMirrorLiX1RxKBytes,
       "tMirrorLiX1TxKBytes": tMirrorLiX1TxKBytes,
       "tMirrorLiX2StatsTable": tMirrorLiX2StatsTable,
       "tMirrorLiX2StatsEntry": tMirrorLiX2StatsEntry,
       "tMirrorLiX2RxMessages": tMirrorLiX2RxMessages,
       "tMirrorLiX2TxMessages": tMirrorLiX2TxMessages,
       "tMirrorLiX2RxKBytes": tMirrorLiX2RxKBytes,
       "tMirrorLiX2TxKBytes": tMirrorLiX2TxKBytes,
       "tMirrorLiX3StatsTable": tMirrorLiX3StatsTable,
       "tMirrorLiX3StatsEntry": tMirrorLiX3StatsEntry,
       "tMirrorLiX3RxMessages": tMirrorLiX3RxMessages,
       "tMirrorLiX3TxMessages": tMirrorLiX3TxMessages,
       "tMirrorLiX3LicTAttempts": tMirrorLiX3LicTAttempts,
       "tMirrorLiX3LicTSuccess": tMirrorLiX3LicTSuccess,
       "tMirrorLiX3RxKBytes": tMirrorLiX3RxKBytes,
       "tMirrorLiX3TxKBytes": tMirrorLiX3TxKBytes,
       "tMirrorLiXTgtTable": tMirrorLiXTgtTable,
       "tMirrorLiXTgtEntry": tMirrorLiXTgtEntry,
       "tMirrorLiXTgtType": tMirrorLiXTgtType,
       "tMirrorLiXTgtAddrType": tMirrorLiXTgtAddrType,
       "tMirrorLiXTgtAddr": tMirrorLiXTgtAddr,
       "tMirrorLiXTgtPrefixLength": tMirrorLiXTgtPrefixLength,
       "tMirrorLiXTgtPort": tMirrorLiXTgtPort,
       "tMirrorLiXTgtVisitAddressType": tMirrorLiXTgtVisitAddressType,
       "tMirrorLiXTgtVisitAddrType": tMirrorLiXTgtVisitAddrType,
       "tMirrorLiXTgtVisitAddr": tMirrorLiXTgtVisitAddr,
       "tMirrorLiXTgtVisitPrefixLength": tMirrorLiXTgtVisitPrefixLength,
       "tMirrorLiXTgtVisitPort": tMirrorLiXTgtVisitPort,
       "tMirrorLiXTgtCreateTime": tMirrorLiXTgtCreateTime,
       "tMirrorLiXTgtTransLayerProtocol": tMirrorLiXTgtTransLayerProtocol,
       "tMirrorLiXTgtVolatile": tMirrorLiXTgtVolatile,
       "tMirrorLiNotifyObjects": tMirrorLiNotifyObjects,
       "tMirrorNotifyLiSvcId": tMirrorNotifyLiSvcId,
       "tMirrorNotifyLiPortId": tMirrorNotifyLiPortId,
       "tMirrorNotifyLiSapEncapValue": tMirrorNotifyLiSapEncapValue,
       "tMirrorNotifyLiDescription": tMirrorNotifyLiDescription,
       "tMirrorLiNotifyIneIdentifier": tMirrorLiNotifyIneIdentifier,
       "tMirrorLiNotifyX2AlarmRank": tMirrorLiNotifyX2AlarmRank,
       "tMirrorLiNotifyX2AlarmFlag": tMirrorLiNotifyX2AlarmFlag,
       "tMirrorLiNotifyDateAndTime": tMirrorLiNotifyDateAndTime,
       "tMirrorLiNotifyLongDescription": tMirrorLiNotifyLongDescription,
       "tMirrorNotifyPrefix": tMirrorNotifyPrefix,
       "tMirrorNotifications": tMirrorNotifications,
       "tMirrorSourceEnabled": tMirrorSourceEnabled,
       "tMirrorSourceDisabled": tMirrorSourceDisabled,
       "tMirrorDestinationEnabled": tMirrorDestinationEnabled,
       "tMirrorDestinationDisabled": tMirrorDestinationDisabled,
       "tMirrorSourceRemovedBySystem": tMirrorSourceRemovedBySystem,
       "tMirrorSourceIpFilterChange": tMirrorSourceIpFilterChange,
       "tMirrorSourceMacFilterChange": tMirrorSourceMacFilterChange,
       "tMirrorSourceSapChange": tMirrorSourceSapChange,
       "tMirrorSourceSubChange": tMirrorSourceSubChange,
       "tMirrorSourceIPFltrChangeReject": tMirrorSourceIPFltrChangeReject,
       "tMirrorSourceIP6FltrChangeReject": tMirrorSourceIP6FltrChangeReject,
       "tMirrorSourceMacFltrChangeReject": tMirrorSourceMacFltrChangeReject,
       "tMirrorSourceFilterAssignReject": tMirrorSourceFilterAssignReject,
       "tMirrorDestinationChangeReject": tMirrorDestinationChangeReject,
       "tMirrorSourceFilterOverruled": tMirrorSourceFilterOverruled,
       "tMirrorSourceFilterAssignWarn": tMirrorSourceFilterAssignWarn,
       "tMirrorFilterAssignToSapWarn": tMirrorFilterAssignToSapWarn,
       "tMirrorFilterAssignToSdpWarn": tMirrorFilterAssignToSdpWarn,
       "tMirrorFilterAssignToItfWarn": tMirrorFilterAssignToItfWarn,
       "tMirrorSourceLiFilterChanged": tMirrorSourceLiFilterChanged,
       "tMirrorSourceLiSubProblem": tMirrorSourceLiSubProblem,
       "tMirrorSourceIpv6FilterChange": tMirrorSourceIpv6FilterChange,
       "tMirrorSourceIPv6FltrChangeRej": tMirrorSourceIPv6FltrChangeRej,
       "tMirrorLiNatLsnSubOperStateCh": tMirrorLiNatLsnSubOperStateCh,
       "tMirrorLiNatL2awSubOperStateCh": tMirrorLiNatL2awSubOperStateCh,
       "tMirrorLiNat64SubOperStateCh": tMirrorLiNat64SubOperStateCh,
       "tMirrorLiX2Alarm": tMirrorLiX2Alarm,
       "radiusFailed": radiusFailed,
       "tMirrorLiSrcPortLicInvalid": tMirrorLiSrcPortLicInvalid}
)
