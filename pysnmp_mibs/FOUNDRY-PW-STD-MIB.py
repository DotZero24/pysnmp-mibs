# SNMP MIB module (FOUNDRY-PW-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/FOUNDRY-PW-STD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:02:38 2025
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

(IANAPwCapabilities,
 IANAPwPsnTypeTC,
 IANAPwTypeTC) = mibBuilder.importSymbols(
    "FOUNDRY-IANA-PWE3-MIB",
    "IANAPwCapabilities",
    "IANAPwPsnTypeTC",
    "IANAPwTypeTC")

(PwAttachmentIdentifierType,
 PwCwStatusTC,
 PwFragSize,
 PwFragStatus,
 PwGroupID,
 PwIDType,
 PwIndexOrZeroType,
 PwIndexType,
 PwOperStatusTC,
 PwStatus) = mibBuilder.importSymbols(
    "FOUNDRY-PW-TC-STD-MIB",
    "PwAttachmentIdentifierType",
    "PwCwStatusTC",
    "PwFragSize",
    "PwFragStatus",
    "PwGroupID",
    "PwIDType",
    "PwIndexOrZeroType",
    "PwIndexType",
    "PwOperStatusTC",
    "PwStatus")

(snAgGblTrapMessage,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "snAgGblTrapMessage")

(pwe3,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "pwe3")

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfTimeElapsed,
 HCPerfValidIntervals) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfTimeElapsed",
    "HCPerfValidIntervals")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pwStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2)
)
if mibBuilder.loadTexts:
    pwStdMIB.setRevisions(
        ("2007-05-31 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FdryPwServiceType(TextualConvention, Integer32):
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
        *(("vll", 1),
          ("vllLocal", 2),
          ("vpls", 3))
    )



# MIB Managed Objects in the order of their OIDs

_PwNotifications_ObjectIdentity = ObjectIdentity
pwNotifications = _PwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 0)
)
_PwObjects_ObjectIdentity = ObjectIdentity
pwObjects = _PwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1)
)
_PwIndexNext_Type = Unsigned32
_PwIndexNext_Object = MibScalar
pwIndexNext = _PwIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 1),
    _PwIndexNext_Type()
)
pwIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwIndexNext.setStatus("current")
_PwTable_Object = MibTable
pwTable = _PwTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pwTable.setStatus("current")
_PwEntry_Object = MibTableRow
pwEntry = _PwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1)
)
pwEntry.setIndexNames(
    (0, "FOUNDRY-PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwEntry.setStatus("current")
_PwIndex_Type = PwIndexType
_PwIndex_Object = MibTableColumn
pwIndex = _PwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 1),
    _PwIndex_Type()
)
pwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwIndex.setStatus("current")
_PwType_Type = IANAPwTypeTC
_PwType_Object = MibTableColumn
pwType = _PwType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 2),
    _PwType_Type()
)
pwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwType.setStatus("current")


class _PwOwner_Type(Integer32):
    """Custom type pwOwner based on Integer32"""
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
        *(("manual", 1),
          ("pwIdFecSignaling", 2),
          ("genFecSignaling", 3),
          ("l2tpControlProtocol", 4),
          ("other", 5))
    )


_PwOwner_Type.__name__ = "Integer32"
_PwOwner_Object = MibTableColumn
pwOwner = _PwOwner_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 3),
    _PwOwner_Type()
)
pwOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwOwner.setStatus("current")
_PwPsnType_Type = IANAPwPsnTypeTC
_PwPsnType_Object = MibTableColumn
pwPsnType = _PwPsnType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 4),
    _PwPsnType_Type()
)
pwPsnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwPsnType.setStatus("current")


class _PwSetUpPriority_Type(Integer32):
    """Custom type pwSetUpPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PwSetUpPriority_Type.__name__ = "Integer32"
_PwSetUpPriority_Object = MibTableColumn
pwSetUpPriority = _PwSetUpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 5),
    _PwSetUpPriority_Type()
)
pwSetUpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwSetUpPriority.setStatus("current")


class _PwHoldingPriority_Type(Integer32):
    """Custom type pwHoldingPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PwHoldingPriority_Type.__name__ = "Integer32"
_PwHoldingPriority_Object = MibTableColumn
pwHoldingPriority = _PwHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 6),
    _PwHoldingPriority_Type()
)
pwHoldingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwHoldingPriority.setStatus("current")


class _PwPeerAddrType_Type(InetAddressType):
    """Custom type pwPeerAddrType based on InetAddressType"""
    defaultValue = 1


_PwPeerAddrType_Type.__name__ = "InetAddressType"
_PwPeerAddrType_Object = MibTableColumn
pwPeerAddrType = _PwPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 8),
    _PwPeerAddrType_Type()
)
pwPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwPeerAddrType.setStatus("current")
_PwPeerAddr_Type = InetAddress
_PwPeerAddr_Object = MibTableColumn
pwPeerAddr = _PwPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 9),
    _PwPeerAddr_Type()
)
pwPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwPeerAddr.setStatus("current")


class _PwAttachedPwIndex_Type(PwIndexOrZeroType):
    """Custom type pwAttachedPwIndex based on PwIndexOrZeroType"""
    defaultValue = 0


_PwAttachedPwIndex_Type.__name__ = "PwIndexOrZeroType"
_PwAttachedPwIndex_Object = MibTableColumn
pwAttachedPwIndex = _PwAttachedPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 10),
    _PwAttachedPwIndex_Type()
)
pwAttachedPwIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAttachedPwIndex.setStatus("current")


class _PwIfIndex_Type(InterfaceIndexOrZero):
    """Custom type pwIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_PwIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_PwIfIndex_Object = MibTableColumn
pwIfIndex = _PwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 11),
    _PwIfIndex_Type()
)
pwIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwIfIndex.setStatus("current")
_PwID_Type = PwIDType
_PwID_Object = MibTableColumn
pwID = _PwID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 12),
    _PwID_Type()
)
pwID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwID.setStatus("current")
_PwLocalGroupID_Type = PwGroupID
_PwLocalGroupID_Object = MibTableColumn
pwLocalGroupID = _PwLocalGroupID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 13),
    _PwLocalGroupID_Type()
)
pwLocalGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwLocalGroupID.setStatus("current")
_PwGroupAttachmentID_Type = PwAttachmentIdentifierType
_PwGroupAttachmentID_Object = MibTableColumn
pwGroupAttachmentID = _PwGroupAttachmentID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 14),
    _PwGroupAttachmentID_Type()
)
pwGroupAttachmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwGroupAttachmentID.setStatus("current")
_PwLocalAttachmentID_Type = PwAttachmentIdentifierType
_PwLocalAttachmentID_Object = MibTableColumn
pwLocalAttachmentID = _PwLocalAttachmentID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 15),
    _PwLocalAttachmentID_Type()
)
pwLocalAttachmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwLocalAttachmentID.setStatus("current")
_PwPeerAttachmentID_Type = PwAttachmentIdentifierType
_PwPeerAttachmentID_Object = MibTableColumn
pwPeerAttachmentID = _PwPeerAttachmentID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 16),
    _PwPeerAttachmentID_Type()
)
pwPeerAttachmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwPeerAttachmentID.setStatus("current")


class _PwCwPreference_Type(TruthValue):
    """Custom type pwCwPreference based on TruthValue"""
    defaultValue = 2


_PwCwPreference_Type.__name__ = "TruthValue"
_PwCwPreference_Object = MibTableColumn
pwCwPreference = _PwCwPreference_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 17),
    _PwCwPreference_Type()
)
pwCwPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCwPreference.setStatus("current")


class _PwLocalIfMtu_Type(Unsigned32):
    """Custom type pwLocalIfMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PwLocalIfMtu_Type.__name__ = "Unsigned32"
_PwLocalIfMtu_Object = MibTableColumn
pwLocalIfMtu = _PwLocalIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 18),
    _PwLocalIfMtu_Type()
)
pwLocalIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwLocalIfMtu.setStatus("current")


class _PwLocalIfString_Type(TruthValue):
    """Custom type pwLocalIfString based on TruthValue"""
    defaultValue = 2


_PwLocalIfString_Type.__name__ = "TruthValue"
_PwLocalIfString_Object = MibTableColumn
pwLocalIfString = _PwLocalIfString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 19),
    _PwLocalIfString_Type()
)
pwLocalIfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwLocalIfString.setStatus("current")
_PwLocalCapabAdvert_Type = IANAPwCapabilities
_PwLocalCapabAdvert_Object = MibTableColumn
pwLocalCapabAdvert = _PwLocalCapabAdvert_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 20),
    _PwLocalCapabAdvert_Type()
)
pwLocalCapabAdvert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwLocalCapabAdvert.setStatus("current")
_PwRemoteGroupID_Type = PwGroupID
_PwRemoteGroupID_Object = MibTableColumn
pwRemoteGroupID = _PwRemoteGroupID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 21),
    _PwRemoteGroupID_Type()
)
pwRemoteGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRemoteGroupID.setStatus("current")
_PwCwStatus_Type = PwCwStatusTC
_PwCwStatus_Object = MibTableColumn
pwCwStatus = _PwCwStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 22),
    _PwCwStatus_Type()
)
pwCwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCwStatus.setStatus("current")
_PwRemoteIfMtu_Type = Unsigned32
_PwRemoteIfMtu_Object = MibTableColumn
pwRemoteIfMtu = _PwRemoteIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 23),
    _PwRemoteIfMtu_Type()
)
pwRemoteIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRemoteIfMtu.setStatus("current")


class _PwRemoteIfString_Type(SnmpAdminString):
    """Custom type pwRemoteIfString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PwRemoteIfString_Type.__name__ = "SnmpAdminString"
_PwRemoteIfString_Object = MibTableColumn
pwRemoteIfString = _PwRemoteIfString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 24),
    _PwRemoteIfString_Type()
)
pwRemoteIfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRemoteIfString.setStatus("current")
_PwRemoteCapabilities_Type = IANAPwCapabilities
_PwRemoteCapabilities_Object = MibTableColumn
pwRemoteCapabilities = _PwRemoteCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 25),
    _PwRemoteCapabilities_Type()
)
pwRemoteCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRemoteCapabilities.setStatus("current")


class _PwFragmentCfgSize_Type(PwFragSize):
    """Custom type pwFragmentCfgSize based on PwFragSize"""
    defaultValue = 0


_PwFragmentCfgSize_Type.__name__ = "PwFragSize"
_PwFragmentCfgSize_Object = MibTableColumn
pwFragmentCfgSize = _PwFragmentCfgSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 26),
    _PwFragmentCfgSize_Type()
)
pwFragmentCfgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwFragmentCfgSize.setStatus("current")
if mibBuilder.loadTexts:
    pwFragmentCfgSize.setUnits("bytes")
_PwRmtFragCapability_Type = PwFragStatus
_PwRmtFragCapability_Object = MibTableColumn
pwRmtFragCapability = _PwRmtFragCapability_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 27),
    _PwRmtFragCapability_Type()
)
pwRmtFragCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRmtFragCapability.setStatus("current")


class _PwFcsRetentionCfg_Type(Integer32):
    """Custom type pwFcsRetentionCfg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcsRetentionDisable", 1),
          ("fcsRetentionEnable", 2))
    )


_PwFcsRetentionCfg_Type.__name__ = "Integer32"
_PwFcsRetentionCfg_Object = MibTableColumn
pwFcsRetentionCfg = _PwFcsRetentionCfg_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 28),
    _PwFcsRetentionCfg_Type()
)
pwFcsRetentionCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwFcsRetentionCfg.setStatus("current")


class _PwFcsRetentionStatus_Type(Bits):
    """Custom type pwFcsRetentionStatus based on Bits"""
    namedValues = NamedValues(
        *(("remoteIndicationUnknown", 0),
          ("remoteRequestFcsRetention", 1),
          ("fcsRetentionEnabled", 2),
          ("fcsRetentionDisabled", 3),
          ("localFcsRetentionCfgErr", 4),
          ("fcsRetentionFcsSizeMismatch", 5))
    )

_PwFcsRetentionStatus_Type.__name__ = "Bits"
_PwFcsRetentionStatus_Object = MibTableColumn
pwFcsRetentionStatus = _PwFcsRetentionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 29),
    _PwFcsRetentionStatus_Type()
)
pwFcsRetentionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwFcsRetentionStatus.setStatus("current")
_PwOutboundLabel_Type = Unsigned32
_PwOutboundLabel_Object = MibTableColumn
pwOutboundLabel = _PwOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 30),
    _PwOutboundLabel_Type()
)
pwOutboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwOutboundLabel.setStatus("current")
_PwInboundLabel_Type = Unsigned32
_PwInboundLabel_Object = MibTableColumn
pwInboundLabel = _PwInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 31),
    _PwInboundLabel_Type()
)
pwInboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwInboundLabel.setStatus("current")
_PwName_Type = SnmpAdminString
_PwName_Object = MibTableColumn
pwName = _PwName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 32),
    _PwName_Type()
)
pwName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwName.setStatus("current")
_PwDescr_Type = SnmpAdminString
_PwDescr_Object = MibTableColumn
pwDescr = _PwDescr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 33),
    _PwDescr_Type()
)
pwDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwDescr.setStatus("current")
_PwCreateTime_Type = TimeStamp
_PwCreateTime_Object = MibTableColumn
pwCreateTime = _PwCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 34),
    _PwCreateTime_Type()
)
pwCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCreateTime.setStatus("current")
_PwUpTime_Type = TimeTicks
_PwUpTime_Object = MibTableColumn
pwUpTime = _PwUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 35),
    _PwUpTime_Type()
)
pwUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwUpTime.setStatus("current")
_PwLastChange_Type = TimeTicks
_PwLastChange_Object = MibTableColumn
pwLastChange = _PwLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 36),
    _PwLastChange_Type()
)
pwLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwLastChange.setStatus("current")


class _PwAdminStatus_Type(Integer32):
    """Custom type pwAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_PwAdminStatus_Type.__name__ = "Integer32"
_PwAdminStatus_Object = MibTableColumn
pwAdminStatus = _PwAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 37),
    _PwAdminStatus_Type()
)
pwAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAdminStatus.setStatus("current")
_PwOperStatus_Type = PwOperStatusTC
_PwOperStatus_Object = MibTableColumn
pwOperStatus = _PwOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 38),
    _PwOperStatus_Type()
)
pwOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwOperStatus.setStatus("current")
_PwLocalStatus_Type = PwStatus
_PwLocalStatus_Object = MibTableColumn
pwLocalStatus = _PwLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 39),
    _PwLocalStatus_Type()
)
pwLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwLocalStatus.setStatus("current")


class _PwRemoteStatusCapable_Type(Integer32):
    """Custom type pwRemoteStatusCapable based on Integer32"""
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
          ("notYetKnown", 2),
          ("remoteCapable", 3),
          ("remoteNotCapable", 4))
    )


_PwRemoteStatusCapable_Type.__name__ = "Integer32"
_PwRemoteStatusCapable_Object = MibTableColumn
pwRemoteStatusCapable = _PwRemoteStatusCapable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 40),
    _PwRemoteStatusCapable_Type()
)
pwRemoteStatusCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRemoteStatusCapable.setStatus("current")
_PwRemoteStatus_Type = PwStatus
_PwRemoteStatus_Object = MibTableColumn
pwRemoteStatus = _PwRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 41),
    _PwRemoteStatus_Type()
)
pwRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRemoteStatus.setStatus("current")
_PwTimeElapsed_Type = HCPerfTimeElapsed
_PwTimeElapsed_Object = MibTableColumn
pwTimeElapsed = _PwTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 42),
    _PwTimeElapsed_Type()
)
pwTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTimeElapsed.setStatus("current")
_PwValidIntervals_Type = HCPerfValidIntervals
_PwValidIntervals_Object = MibTableColumn
pwValidIntervals = _PwValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 43),
    _PwValidIntervals_Type()
)
pwValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwValidIntervals.setStatus("current")
_PwRowStatus_Type = RowStatus
_PwRowStatus_Object = MibTableColumn
pwRowStatus = _PwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 44),
    _PwRowStatus_Type()
)
pwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwRowStatus.setStatus("current")


class _PwStorageType_Type(StorageType):
    """Custom type pwStorageType based on StorageType"""
    defaultValue = 3


_PwStorageType_Type.__name__ = "StorageType"
_PwStorageType_Object = MibTableColumn
pwStorageType = _PwStorageType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 45),
    _PwStorageType_Type()
)
pwStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwStorageType.setStatus("current")


class _PwOamEnable_Type(TruthValue):
    """Custom type pwOamEnable based on TruthValue"""
    defaultValue = 1


_PwOamEnable_Type.__name__ = "TruthValue"
_PwOamEnable_Object = MibTableColumn
pwOamEnable = _PwOamEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 2, 1, 46),
    _PwOamEnable_Type()
)
pwOamEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwOamEnable.setStatus("current")
_PwPerfCurrentTable_Object = MibTable
pwPerfCurrentTable = _PwPerfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pwPerfCurrentTable.setStatus("current")
_PwPerfCurrentEntry_Object = MibTableRow
pwPerfCurrentEntry = _PwPerfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 3, 1)
)
pwPerfCurrentEntry.setIndexNames(
    (0, "FOUNDRY-PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwPerfCurrentEntry.setStatus("current")
_PwPerfCurrentInHCPackets_Type = HCPerfCurrentCount
_PwPerfCurrentInHCPackets_Object = MibTableColumn
pwPerfCurrentInHCPackets = _PwPerfCurrentInHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 3, 1, 1),
    _PwPerfCurrentInHCPackets_Type()
)
pwPerfCurrentInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentInHCPackets.setStatus("current")
_PwPerfCurrentInHCBytes_Type = HCPerfCurrentCount
_PwPerfCurrentInHCBytes_Object = MibTableColumn
pwPerfCurrentInHCBytes = _PwPerfCurrentInHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 3, 1, 2),
    _PwPerfCurrentInHCBytes_Type()
)
pwPerfCurrentInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentInHCBytes.setStatus("current")
_PwPerfCurrentOutHCPackets_Type = HCPerfCurrentCount
_PwPerfCurrentOutHCPackets_Object = MibTableColumn
pwPerfCurrentOutHCPackets = _PwPerfCurrentOutHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 3, 1, 3),
    _PwPerfCurrentOutHCPackets_Type()
)
pwPerfCurrentOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentOutHCPackets.setStatus("current")
_PwPerfCurrentOutHCBytes_Type = HCPerfCurrentCount
_PwPerfCurrentOutHCBytes_Object = MibTableColumn
pwPerfCurrentOutHCBytes = _PwPerfCurrentOutHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 3, 1, 4),
    _PwPerfCurrentOutHCBytes_Type()
)
pwPerfCurrentOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentOutHCBytes.setStatus("current")
_PwPerfCurrentInPackets_Type = PerfCurrentCount
_PwPerfCurrentInPackets_Object = MibTableColumn
pwPerfCurrentInPackets = _PwPerfCurrentInPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 3, 1, 5),
    _PwPerfCurrentInPackets_Type()
)
pwPerfCurrentInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentInPackets.setStatus("current")
_PwPerfCurrentInBytes_Type = PerfCurrentCount
_PwPerfCurrentInBytes_Object = MibTableColumn
pwPerfCurrentInBytes = _PwPerfCurrentInBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 3, 1, 6),
    _PwPerfCurrentInBytes_Type()
)
pwPerfCurrentInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentInBytes.setStatus("current")
_PwPerfCurrentOutPackets_Type = PerfCurrentCount
_PwPerfCurrentOutPackets_Object = MibTableColumn
pwPerfCurrentOutPackets = _PwPerfCurrentOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 3, 1, 7),
    _PwPerfCurrentOutPackets_Type()
)
pwPerfCurrentOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentOutPackets.setStatus("current")
_PwPerfCurrentOutBytes_Type = PerfCurrentCount
_PwPerfCurrentOutBytes_Object = MibTableColumn
pwPerfCurrentOutBytes = _PwPerfCurrentOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 3, 1, 8),
    _PwPerfCurrentOutBytes_Type()
)
pwPerfCurrentOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfCurrentOutBytes.setStatus("current")
_PwPerfIntervalTable_Object = MibTable
pwPerfIntervalTable = _PwPerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    pwPerfIntervalTable.setStatus("current")
_PwPerfIntervalEntry_Object = MibTableRow
pwPerfIntervalEntry = _PwPerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4, 1)
)
pwPerfIntervalEntry.setIndexNames(
    (0, "FOUNDRY-PW-STD-MIB", "pwIndex"),
    (0, "FOUNDRY-PW-STD-MIB", "pwPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    pwPerfIntervalEntry.setStatus("current")


class _PwPerfIntervalNumber_Type(Integer32):
    """Custom type pwPerfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PwPerfIntervalNumber_Type.__name__ = "Integer32"
_PwPerfIntervalNumber_Object = MibTableColumn
pwPerfIntervalNumber = _PwPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4, 1, 1),
    _PwPerfIntervalNumber_Type()
)
pwPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwPerfIntervalNumber.setStatus("current")
_PwPerfIntervalValidData_Type = TruthValue
_PwPerfIntervalValidData_Object = MibTableColumn
pwPerfIntervalValidData = _PwPerfIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4, 1, 2),
    _PwPerfIntervalValidData_Type()
)
pwPerfIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalValidData.setStatus("current")
_PwPerfIntervalTimeElapsed_Type = HCPerfTimeElapsed
_PwPerfIntervalTimeElapsed_Object = MibTableColumn
pwPerfIntervalTimeElapsed = _PwPerfIntervalTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4, 1, 3),
    _PwPerfIntervalTimeElapsed_Type()
)
pwPerfIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalTimeElapsed.setStatus("current")
_PwPerfIntervalInHCPackets_Type = HCPerfIntervalCount
_PwPerfIntervalInHCPackets_Object = MibTableColumn
pwPerfIntervalInHCPackets = _PwPerfIntervalInHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4, 1, 4),
    _PwPerfIntervalInHCPackets_Type()
)
pwPerfIntervalInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalInHCPackets.setStatus("current")
_PwPerfIntervalInHCBytes_Type = HCPerfIntervalCount
_PwPerfIntervalInHCBytes_Object = MibTableColumn
pwPerfIntervalInHCBytes = _PwPerfIntervalInHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4, 1, 5),
    _PwPerfIntervalInHCBytes_Type()
)
pwPerfIntervalInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalInHCBytes.setStatus("current")
_PwPerfIntervalOutHCPackets_Type = HCPerfIntervalCount
_PwPerfIntervalOutHCPackets_Object = MibTableColumn
pwPerfIntervalOutHCPackets = _PwPerfIntervalOutHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4, 1, 6),
    _PwPerfIntervalOutHCPackets_Type()
)
pwPerfIntervalOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalOutHCPackets.setStatus("current")
_PwPerfIntervalOutHCBytes_Type = HCPerfIntervalCount
_PwPerfIntervalOutHCBytes_Object = MibTableColumn
pwPerfIntervalOutHCBytes = _PwPerfIntervalOutHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4, 1, 7),
    _PwPerfIntervalOutHCBytes_Type()
)
pwPerfIntervalOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalOutHCBytes.setStatus("current")
_PwPerfIntervalInPackets_Type = PerfIntervalCount
_PwPerfIntervalInPackets_Object = MibTableColumn
pwPerfIntervalInPackets = _PwPerfIntervalInPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4, 1, 8),
    _PwPerfIntervalInPackets_Type()
)
pwPerfIntervalInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalInPackets.setStatus("current")
_PwPerfIntervalInBytes_Type = PerfIntervalCount
_PwPerfIntervalInBytes_Object = MibTableColumn
pwPerfIntervalInBytes = _PwPerfIntervalInBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4, 1, 9),
    _PwPerfIntervalInBytes_Type()
)
pwPerfIntervalInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalInBytes.setStatus("current")
_PwPerfIntervalOutPackets_Type = PerfIntervalCount
_PwPerfIntervalOutPackets_Object = MibTableColumn
pwPerfIntervalOutPackets = _PwPerfIntervalOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4, 1, 10),
    _PwPerfIntervalOutPackets_Type()
)
pwPerfIntervalOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalOutPackets.setStatus("current")
_PwPerfIntervalOutBytes_Type = PerfIntervalCount
_PwPerfIntervalOutBytes_Object = MibTableColumn
pwPerfIntervalOutBytes = _PwPerfIntervalOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 4, 1, 11),
    _PwPerfIntervalOutBytes_Type()
)
pwPerfIntervalOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfIntervalOutBytes.setStatus("current")
_PwPerfTotalTable_Object = MibTable
pwPerfTotalTable = _PwPerfTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    pwPerfTotalTable.setStatus("current")
_PwPerfTotalEntry_Object = MibTableRow
pwPerfTotalEntry = _PwPerfTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 5, 1)
)
pwPerfTotalEntry.setIndexNames(
    (0, "FOUNDRY-PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwPerfTotalEntry.setStatus("current")
_PwPerfTotalInHCPackets_Type = Counter64
_PwPerfTotalInHCPackets_Object = MibTableColumn
pwPerfTotalInHCPackets = _PwPerfTotalInHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 5, 1, 1),
    _PwPerfTotalInHCPackets_Type()
)
pwPerfTotalInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfTotalInHCPackets.setStatus("current")
_PwPerfTotalInHCBytes_Type = Counter64
_PwPerfTotalInHCBytes_Object = MibTableColumn
pwPerfTotalInHCBytes = _PwPerfTotalInHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 5, 1, 2),
    _PwPerfTotalInHCBytes_Type()
)
pwPerfTotalInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfTotalInHCBytes.setStatus("current")
_PwPerfTotalOutHCPackets_Type = Counter64
_PwPerfTotalOutHCPackets_Object = MibTableColumn
pwPerfTotalOutHCPackets = _PwPerfTotalOutHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 5, 1, 3),
    _PwPerfTotalOutHCPackets_Type()
)
pwPerfTotalOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfTotalOutHCPackets.setStatus("current")
_PwPerfTotalOutHCBytes_Type = Counter64
_PwPerfTotalOutHCBytes_Object = MibTableColumn
pwPerfTotalOutHCBytes = _PwPerfTotalOutHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 5, 1, 4),
    _PwPerfTotalOutHCBytes_Type()
)
pwPerfTotalOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfTotalOutHCBytes.setStatus("current")
_PwPerfTotalInPackets_Type = Counter32
_PwPerfTotalInPackets_Object = MibTableColumn
pwPerfTotalInPackets = _PwPerfTotalInPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 5, 1, 5),
    _PwPerfTotalInPackets_Type()
)
pwPerfTotalInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfTotalInPackets.setStatus("current")
_PwPerfTotalInBytes_Type = Counter32
_PwPerfTotalInBytes_Object = MibTableColumn
pwPerfTotalInBytes = _PwPerfTotalInBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 5, 1, 6),
    _PwPerfTotalInBytes_Type()
)
pwPerfTotalInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfTotalInBytes.setStatus("current")
_PwPerfTotalOutPackets_Type = Counter32
_PwPerfTotalOutPackets_Object = MibTableColumn
pwPerfTotalOutPackets = _PwPerfTotalOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 5, 1, 7),
    _PwPerfTotalOutPackets_Type()
)
pwPerfTotalOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfTotalOutPackets.setStatus("current")
_PwPerfTotalOutBytes_Type = Counter32
_PwPerfTotalOutBytes_Object = MibTableColumn
pwPerfTotalOutBytes = _PwPerfTotalOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 5, 1, 8),
    _PwPerfTotalOutBytes_Type()
)
pwPerfTotalOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfTotalOutBytes.setStatus("current")
_PwPerfTotalDiscontinuityTime_Type = TimeStamp
_PwPerfTotalDiscontinuityTime_Object = MibTableColumn
pwPerfTotalDiscontinuityTime = _PwPerfTotalDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 5, 1, 9),
    _PwPerfTotalDiscontinuityTime_Type()
)
pwPerfTotalDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfTotalDiscontinuityTime.setStatus("current")
_PwPerfTotalErrorPackets_Type = Counter32
_PwPerfTotalErrorPackets_Object = MibScalar
pwPerfTotalErrorPackets = _PwPerfTotalErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 6),
    _PwPerfTotalErrorPackets_Type()
)
pwPerfTotalErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPerfTotalErrorPackets.setStatus("current")
_PwIndexMappingTable_Object = MibTable
pwIndexMappingTable = _PwIndexMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    pwIndexMappingTable.setStatus("current")
_PwIndexMappingEntry_Object = MibTableRow
pwIndexMappingEntry = _PwIndexMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 7, 1)
)
pwIndexMappingEntry.setIndexNames(
    (0, "FOUNDRY-PW-STD-MIB", "pwIndexMappingPwType"),
    (0, "FOUNDRY-PW-STD-MIB", "pwIndexMappingPwID"),
    (0, "FOUNDRY-PW-STD-MIB", "pwIndexMappingPeerAddrType"),
    (0, "FOUNDRY-PW-STD-MIB", "pwIndexMappingPeerAddr"),
)
if mibBuilder.loadTexts:
    pwIndexMappingEntry.setStatus("current")
_PwIndexMappingPwType_Type = IANAPwTypeTC
_PwIndexMappingPwType_Object = MibTableColumn
pwIndexMappingPwType = _PwIndexMappingPwType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 7, 1, 1),
    _PwIndexMappingPwType_Type()
)
pwIndexMappingPwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwIndexMappingPwType.setStatus("current")
_PwIndexMappingPwID_Type = PwIDType
_PwIndexMappingPwID_Object = MibTableColumn
pwIndexMappingPwID = _PwIndexMappingPwID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 7, 1, 2),
    _PwIndexMappingPwID_Type()
)
pwIndexMappingPwID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwIndexMappingPwID.setStatus("current")
_PwIndexMappingPeerAddrType_Type = InetAddressType
_PwIndexMappingPeerAddrType_Object = MibTableColumn
pwIndexMappingPeerAddrType = _PwIndexMappingPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 7, 1, 3),
    _PwIndexMappingPeerAddrType_Type()
)
pwIndexMappingPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwIndexMappingPeerAddrType.setStatus("current")
_PwIndexMappingPeerAddr_Type = InetAddress
_PwIndexMappingPeerAddr_Object = MibTableColumn
pwIndexMappingPeerAddr = _PwIndexMappingPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 7, 1, 4),
    _PwIndexMappingPeerAddr_Type()
)
pwIndexMappingPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwIndexMappingPeerAddr.setStatus("current")
_PwIndexMappingPwIndex_Type = PwIndexType
_PwIndexMappingPwIndex_Object = MibTableColumn
pwIndexMappingPwIndex = _PwIndexMappingPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 7, 1, 5),
    _PwIndexMappingPwIndex_Type()
)
pwIndexMappingPwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwIndexMappingPwIndex.setStatus("current")
_PwPeerMappingTable_Object = MibTable
pwPeerMappingTable = _PwPeerMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    pwPeerMappingTable.setStatus("current")
_PwPeerMappingEntry_Object = MibTableRow
pwPeerMappingEntry = _PwPeerMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 8, 1)
)
pwPeerMappingEntry.setIndexNames(
    (0, "FOUNDRY-PW-STD-MIB", "pwPeerMappingPeerAddrType"),
    (0, "FOUNDRY-PW-STD-MIB", "pwPeerMappingPeerAddr"),
    (0, "FOUNDRY-PW-STD-MIB", "pwPeerMappingPwType"),
    (0, "FOUNDRY-PW-STD-MIB", "pwPeerMappingPwID"),
)
if mibBuilder.loadTexts:
    pwPeerMappingEntry.setStatus("current")
_PwPeerMappingPeerAddrType_Type = InetAddressType
_PwPeerMappingPeerAddrType_Object = MibTableColumn
pwPeerMappingPeerAddrType = _PwPeerMappingPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 8, 1, 1),
    _PwPeerMappingPeerAddrType_Type()
)
pwPeerMappingPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwPeerMappingPeerAddrType.setStatus("current")
_PwPeerMappingPeerAddr_Type = InetAddress
_PwPeerMappingPeerAddr_Object = MibTableColumn
pwPeerMappingPeerAddr = _PwPeerMappingPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 8, 1, 2),
    _PwPeerMappingPeerAddr_Type()
)
pwPeerMappingPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwPeerMappingPeerAddr.setStatus("current")
_PwPeerMappingPwType_Type = IANAPwTypeTC
_PwPeerMappingPwType_Object = MibTableColumn
pwPeerMappingPwType = _PwPeerMappingPwType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 8, 1, 3),
    _PwPeerMappingPwType_Type()
)
pwPeerMappingPwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwPeerMappingPwType.setStatus("current")
_PwPeerMappingPwID_Type = PwIDType
_PwPeerMappingPwID_Object = MibTableColumn
pwPeerMappingPwID = _PwPeerMappingPwID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 8, 1, 4),
    _PwPeerMappingPwID_Type()
)
pwPeerMappingPwID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwPeerMappingPwID.setStatus("current")
_PwPeerMappingPwIndex_Type = PwIndexType
_PwPeerMappingPwIndex_Object = MibTableColumn
pwPeerMappingPwIndex = _PwPeerMappingPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 8, 1, 5),
    _PwPeerMappingPwIndex_Type()
)
pwPeerMappingPwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwPeerMappingPwIndex.setStatus("current")


class _PwUpDownNotifEnable_Type(TruthValue):
    """Custom type pwUpDownNotifEnable based on TruthValue"""
    defaultValue = 2


_PwUpDownNotifEnable_Type.__name__ = "TruthValue"
_PwUpDownNotifEnable_Object = MibScalar
pwUpDownNotifEnable = _PwUpDownNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 9),
    _PwUpDownNotifEnable_Type()
)
pwUpDownNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwUpDownNotifEnable.setStatus("current")


class _PwDeletedNotifEnable_Type(TruthValue):
    """Custom type pwDeletedNotifEnable based on TruthValue"""
    defaultValue = 2


_PwDeletedNotifEnable_Type.__name__ = "TruthValue"
_PwDeletedNotifEnable_Object = MibScalar
pwDeletedNotifEnable = _PwDeletedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 10),
    _PwDeletedNotifEnable_Type()
)
pwDeletedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwDeletedNotifEnable.setStatus("current")
_PwNotifRate_Type = Unsigned32
_PwNotifRate_Object = MibScalar
pwNotifRate = _PwNotifRate_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 11),
    _PwNotifRate_Type()
)
pwNotifRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwNotifRate.setStatus("current")
_FdryPwServiceType_Type = FdryPwServiceType
_FdryPwServiceType_Object = MibScalar
fdryPwServiceType = _FdryPwServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 1, 20),
    _FdryPwServiceType_Type()
)
fdryPwServiceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fdryPwServiceType.setStatus("current")
_PwConformance_ObjectIdentity = ObjectIdentity
pwConformance = _PwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2)
)
_PwGroups_ObjectIdentity = ObjectIdentity
pwGroups = _PwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1)
)
_PwCompliances_ObjectIdentity = ObjectIdentity
pwCompliances = _PwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 2)
)

# Managed Objects groups

pwBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 1)
)
pwBasicGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwType"),
        ("FOUNDRY-PW-STD-MIB", "pwOwner"),
        ("FOUNDRY-PW-STD-MIB", "pwPsnType"),
        ("FOUNDRY-PW-STD-MIB", "pwIfIndex"),
        ("FOUNDRY-PW-STD-MIB", "pwCwPreference"),
        ("FOUNDRY-PW-STD-MIB", "pwLocalIfMtu"),
        ("FOUNDRY-PW-STD-MIB", "pwOutboundLabel"),
        ("FOUNDRY-PW-STD-MIB", "pwInboundLabel"),
        ("FOUNDRY-PW-STD-MIB", "pwName"),
        ("FOUNDRY-PW-STD-MIB", "pwDescr"),
        ("FOUNDRY-PW-STD-MIB", "pwCreateTime"),
        ("FOUNDRY-PW-STD-MIB", "pwUpTime"),
        ("FOUNDRY-PW-STD-MIB", "pwLastChange"),
        ("FOUNDRY-PW-STD-MIB", "pwAdminStatus"),
        ("FOUNDRY-PW-STD-MIB", "pwOperStatus"),
        ("FOUNDRY-PW-STD-MIB", "pwLocalStatus"),
        ("FOUNDRY-PW-STD-MIB", "pwRowStatus"),
        ("FOUNDRY-PW-STD-MIB", "pwStorageType"),
        ("FOUNDRY-PW-STD-MIB", "pwOamEnable"))
)
if mibBuilder.loadTexts:
    pwBasicGroup.setStatus("current")

pwPwIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 2)
)
pwPwIdGroup.setObjects(
    ("FOUNDRY-PW-STD-MIB", "pwID")
)
if mibBuilder.loadTexts:
    pwPwIdGroup.setStatus("current")

pwGeneralizedFecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 3)
)
pwGeneralizedFecGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwGroupAttachmentID"),
        ("FOUNDRY-PW-STD-MIB", "pwLocalAttachmentID"),
        ("FOUNDRY-PW-STD-MIB", "pwPeerAttachmentID"))
)
if mibBuilder.loadTexts:
    pwGeneralizedFecGroup.setStatus("current")

pwFcsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 4)
)
pwFcsGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwFcsRetentionCfg"),
        ("FOUNDRY-PW-STD-MIB", "pwFcsRetentionStatus"))
)
if mibBuilder.loadTexts:
    pwFcsGroup.setStatus("current")

pwFragGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 5)
)
pwFragGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwFragmentCfgSize"),
        ("FOUNDRY-PW-STD-MIB", "pwRmtFragCapability"))
)
if mibBuilder.loadTexts:
    pwFragGroup.setStatus("current")

pwPwStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 6)
)
pwPwStatusGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwRemoteCapabilities"),
        ("FOUNDRY-PW-STD-MIB", "pwRemoteStatusCapable"),
        ("FOUNDRY-PW-STD-MIB", "pwRemoteStatus"))
)
if mibBuilder.loadTexts:
    pwPwStatusGroup.setStatus("current")

pwGetNextGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 7)
)
pwGetNextGroup.setObjects(
    ("FOUNDRY-PW-STD-MIB", "pwIndexNext")
)
if mibBuilder.loadTexts:
    pwGetNextGroup.setStatus("current")

pwPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 8)
)
pwPriorityGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwSetUpPriority"),
        ("FOUNDRY-PW-STD-MIB", "pwHoldingPriority"))
)
if mibBuilder.loadTexts:
    pwPriorityGroup.setStatus("current")

pwAttachmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 9)
)
pwAttachmentGroup.setObjects(
    ("FOUNDRY-PW-STD-MIB", "pwAttachedPwIndex")
)
if mibBuilder.loadTexts:
    pwAttachmentGroup.setStatus("current")

pwPerformanceGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 10)
)
pwPerformanceGeneralGroup.setObjects(
    ("FOUNDRY-PW-STD-MIB", "pwPerfTotalErrorPackets")
)
if mibBuilder.loadTexts:
    pwPerformanceGeneralGroup.setStatus("current")

pwPeformanceTotalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 11)
)
pwPeformanceTotalGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwPerfTotalInPackets"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfTotalInBytes"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfTotalOutPackets"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfTotalOutBytes"))
)
if mibBuilder.loadTexts:
    pwPeformanceTotalGroup.setStatus("current")

pwPerformanceIntervalGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 12)
)
pwPerformanceIntervalGeneralGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwTimeElapsed"),
        ("FOUNDRY-PW-STD-MIB", "pwValidIntervals"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfIntervalValidData"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfIntervalTimeElapsed"))
)
if mibBuilder.loadTexts:
    pwPerformanceIntervalGeneralGroup.setStatus("current")

pwPeformanceIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 13)
)
pwPeformanceIntervalGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwPerfCurrentInPackets"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfCurrentInBytes"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfCurrentOutPackets"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfCurrentOutBytes"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfIntervalInPackets"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfIntervalInBytes"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfIntervalOutPackets"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfIntervalOutBytes"))
)
if mibBuilder.loadTexts:
    pwPeformanceIntervalGroup.setStatus("current")

pwHCPeformanceIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 14)
)
pwHCPeformanceIntervalGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwPerfCurrentInHCPackets"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfCurrentInHCBytes"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfCurrentOutHCPackets"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfCurrentOutHCBytes"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfIntervalInHCPackets"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfIntervalInHCBytes"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfIntervalOutHCPackets"),
        ("FOUNDRY-PW-STD-MIB", "pwPerfIntervalOutHCBytes"))
)
if mibBuilder.loadTexts:
    pwHCPeformanceIntervalGroup.setStatus("current")

pwMappingTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 15)
)
pwMappingTablesGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwIndexMappingPwIndex"),
        ("FOUNDRY-PW-STD-MIB", "pwPeerMappingPwIndex"))
)
if mibBuilder.loadTexts:
    pwMappingTablesGroup.setStatus("current")

pwNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 16)
)
pwNotificationControlGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwUpDownNotifEnable"),
        ("FOUNDRY-PW-STD-MIB", "pwDeletedNotifEnable"),
        ("FOUNDRY-PW-STD-MIB", "pwNotifRate"))
)
if mibBuilder.loadTexts:
    pwNotificationControlGroup.setStatus("current")

pwSignalingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 18)
)
pwSignalingGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwPeerAddrType"),
        ("FOUNDRY-PW-STD-MIB", "pwPeerAddr"),
        ("FOUNDRY-PW-STD-MIB", "pwLocalGroupID"),
        ("FOUNDRY-PW-STD-MIB", "pwLocalIfString"),
        ("FOUNDRY-PW-STD-MIB", "pwLocalCapabAdvert"),
        ("FOUNDRY-PW-STD-MIB", "pwRemoteGroupID"),
        ("FOUNDRY-PW-STD-MIB", "pwCwStatus"),
        ("FOUNDRY-PW-STD-MIB", "pwRemoteIfMtu"),
        ("FOUNDRY-PW-STD-MIB", "pwRemoteIfString"))
)
if mibBuilder.loadTexts:
    pwSignalingGroup.setStatus("current")


# Notification objects

pwDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 0, 1)
)
pwDown.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwOperStatus"),
        ("FOUNDRY-PW-STD-MIB", "pwOperStatus"),
        ("FOUNDRY-PW-STD-MIB", "fdryPwServiceType"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    pwDown.setStatus(
        "current"
    )

pwUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 0, 2)
)
pwUp.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwOperStatus"),
        ("FOUNDRY-PW-STD-MIB", "pwOperStatus"),
        ("FOUNDRY-PW-STD-MIB", "fdryPwServiceType"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    pwUp.setStatus(
        "current"
    )

pwDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 0, 3)
)
pwDeleted.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwType"),
        ("FOUNDRY-PW-STD-MIB", "pwID"),
        ("FOUNDRY-PW-STD-MIB", "pwPeerAddrType"),
        ("FOUNDRY-PW-STD-MIB", "pwPeerAddr"),
        ("FOUNDRY-PW-STD-MIB", "fdryPwServiceType"),
        ("FOUNDRY-PW-STD-MIB", "pwName"))
)
if mibBuilder.loadTexts:
    pwDeleted.setStatus(
        "current"
    )


# Notifications groups

pwNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 1, 17)
)
pwNotificationGroup.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwUp"),
        ("FOUNDRY-PW-STD-MIB", "pwDown"),
        ("FOUNDRY-PW-STD-MIB", "pwDeleted"))
)
if mibBuilder.loadTexts:
    pwNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pwModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 2, 1)
)
pwModuleFullCompliance.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwBasicGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPerformanceGeneralGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPeformanceTotalGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwNotificationGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPwIdGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwGeneralizedFecGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwFcsGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwFragGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPwStatusGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwGetNextGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPriorityGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwAttachmentGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPerformanceIntervalGeneralGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPeformanceIntervalGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwHCPeformanceIntervalGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwMappingTablesGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwSignalingGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwNotificationControlGroup"))
)
if mibBuilder.loadTexts:
    pwModuleFullCompliance.setStatus(
        "current"
    )

pwModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 2, 2, 2, 2)
)
pwModuleReadOnlyCompliance.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "pwBasicGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPeformanceTotalGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwNotificationGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPwIdGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwGeneralizedFecGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwFcsGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwFragGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPwStatusGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwGetNextGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPriorityGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwAttachmentGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPerformanceIntervalGeneralGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwPeformanceIntervalGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwHCPeformanceIntervalGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwMappingTablesGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwSignalingGroup"),
        ("FOUNDRY-PW-STD-MIB", "pwNotificationControlGroup"))
)
if mibBuilder.loadTexts:
    pwModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-PW-STD-MIB",
    **{"FdryPwServiceType": FdryPwServiceType,
       "pwStdMIB": pwStdMIB,
       "pwNotifications": pwNotifications,
       "pwDown": pwDown,
       "pwUp": pwUp,
       "pwDeleted": pwDeleted,
       "pwObjects": pwObjects,
       "pwIndexNext": pwIndexNext,
       "pwTable": pwTable,
       "pwEntry": pwEntry,
       "pwIndex": pwIndex,
       "pwType": pwType,
       "pwOwner": pwOwner,
       "pwPsnType": pwPsnType,
       "pwSetUpPriority": pwSetUpPriority,
       "pwHoldingPriority": pwHoldingPriority,
       "pwPeerAddrType": pwPeerAddrType,
       "pwPeerAddr": pwPeerAddr,
       "pwAttachedPwIndex": pwAttachedPwIndex,
       "pwIfIndex": pwIfIndex,
       "pwID": pwID,
       "pwLocalGroupID": pwLocalGroupID,
       "pwGroupAttachmentID": pwGroupAttachmentID,
       "pwLocalAttachmentID": pwLocalAttachmentID,
       "pwPeerAttachmentID": pwPeerAttachmentID,
       "pwCwPreference": pwCwPreference,
       "pwLocalIfMtu": pwLocalIfMtu,
       "pwLocalIfString": pwLocalIfString,
       "pwLocalCapabAdvert": pwLocalCapabAdvert,
       "pwRemoteGroupID": pwRemoteGroupID,
       "pwCwStatus": pwCwStatus,
       "pwRemoteIfMtu": pwRemoteIfMtu,
       "pwRemoteIfString": pwRemoteIfString,
       "pwRemoteCapabilities": pwRemoteCapabilities,
       "pwFragmentCfgSize": pwFragmentCfgSize,
       "pwRmtFragCapability": pwRmtFragCapability,
       "pwFcsRetentionCfg": pwFcsRetentionCfg,
       "pwFcsRetentionStatus": pwFcsRetentionStatus,
       "pwOutboundLabel": pwOutboundLabel,
       "pwInboundLabel": pwInboundLabel,
       "pwName": pwName,
       "pwDescr": pwDescr,
       "pwCreateTime": pwCreateTime,
       "pwUpTime": pwUpTime,
       "pwLastChange": pwLastChange,
       "pwAdminStatus": pwAdminStatus,
       "pwOperStatus": pwOperStatus,
       "pwLocalStatus": pwLocalStatus,
       "pwRemoteStatusCapable": pwRemoteStatusCapable,
       "pwRemoteStatus": pwRemoteStatus,
       "pwTimeElapsed": pwTimeElapsed,
       "pwValidIntervals": pwValidIntervals,
       "pwRowStatus": pwRowStatus,
       "pwStorageType": pwStorageType,
       "pwOamEnable": pwOamEnable,
       "pwPerfCurrentTable": pwPerfCurrentTable,
       "pwPerfCurrentEntry": pwPerfCurrentEntry,
       "pwPerfCurrentInHCPackets": pwPerfCurrentInHCPackets,
       "pwPerfCurrentInHCBytes": pwPerfCurrentInHCBytes,
       "pwPerfCurrentOutHCPackets": pwPerfCurrentOutHCPackets,
       "pwPerfCurrentOutHCBytes": pwPerfCurrentOutHCBytes,
       "pwPerfCurrentInPackets": pwPerfCurrentInPackets,
       "pwPerfCurrentInBytes": pwPerfCurrentInBytes,
       "pwPerfCurrentOutPackets": pwPerfCurrentOutPackets,
       "pwPerfCurrentOutBytes": pwPerfCurrentOutBytes,
       "pwPerfIntervalTable": pwPerfIntervalTable,
       "pwPerfIntervalEntry": pwPerfIntervalEntry,
       "pwPerfIntervalNumber": pwPerfIntervalNumber,
       "pwPerfIntervalValidData": pwPerfIntervalValidData,
       "pwPerfIntervalTimeElapsed": pwPerfIntervalTimeElapsed,
       "pwPerfIntervalInHCPackets": pwPerfIntervalInHCPackets,
       "pwPerfIntervalInHCBytes": pwPerfIntervalInHCBytes,
       "pwPerfIntervalOutHCPackets": pwPerfIntervalOutHCPackets,
       "pwPerfIntervalOutHCBytes": pwPerfIntervalOutHCBytes,
       "pwPerfIntervalInPackets": pwPerfIntervalInPackets,
       "pwPerfIntervalInBytes": pwPerfIntervalInBytes,
       "pwPerfIntervalOutPackets": pwPerfIntervalOutPackets,
       "pwPerfIntervalOutBytes": pwPerfIntervalOutBytes,
       "pwPerfTotalTable": pwPerfTotalTable,
       "pwPerfTotalEntry": pwPerfTotalEntry,
       "pwPerfTotalInHCPackets": pwPerfTotalInHCPackets,
       "pwPerfTotalInHCBytes": pwPerfTotalInHCBytes,
       "pwPerfTotalOutHCPackets": pwPerfTotalOutHCPackets,
       "pwPerfTotalOutHCBytes": pwPerfTotalOutHCBytes,
       "pwPerfTotalInPackets": pwPerfTotalInPackets,
       "pwPerfTotalInBytes": pwPerfTotalInBytes,
       "pwPerfTotalOutPackets": pwPerfTotalOutPackets,
       "pwPerfTotalOutBytes": pwPerfTotalOutBytes,
       "pwPerfTotalDiscontinuityTime": pwPerfTotalDiscontinuityTime,
       "pwPerfTotalErrorPackets": pwPerfTotalErrorPackets,
       "pwIndexMappingTable": pwIndexMappingTable,
       "pwIndexMappingEntry": pwIndexMappingEntry,
       "pwIndexMappingPwType": pwIndexMappingPwType,
       "pwIndexMappingPwID": pwIndexMappingPwID,
       "pwIndexMappingPeerAddrType": pwIndexMappingPeerAddrType,
       "pwIndexMappingPeerAddr": pwIndexMappingPeerAddr,
       "pwIndexMappingPwIndex": pwIndexMappingPwIndex,
       "pwPeerMappingTable": pwPeerMappingTable,
       "pwPeerMappingEntry": pwPeerMappingEntry,
       "pwPeerMappingPeerAddrType": pwPeerMappingPeerAddrType,
       "pwPeerMappingPeerAddr": pwPeerMappingPeerAddr,
       "pwPeerMappingPwType": pwPeerMappingPwType,
       "pwPeerMappingPwID": pwPeerMappingPwID,
       "pwPeerMappingPwIndex": pwPeerMappingPwIndex,
       "pwUpDownNotifEnable": pwUpDownNotifEnable,
       "pwDeletedNotifEnable": pwDeletedNotifEnable,
       "pwNotifRate": pwNotifRate,
       "fdryPwServiceType": fdryPwServiceType,
       "pwConformance": pwConformance,
       "pwGroups": pwGroups,
       "pwBasicGroup": pwBasicGroup,
       "pwPwIdGroup": pwPwIdGroup,
       "pwGeneralizedFecGroup": pwGeneralizedFecGroup,
       "pwFcsGroup": pwFcsGroup,
       "pwFragGroup": pwFragGroup,
       "pwPwStatusGroup": pwPwStatusGroup,
       "pwGetNextGroup": pwGetNextGroup,
       "pwPriorityGroup": pwPriorityGroup,
       "pwAttachmentGroup": pwAttachmentGroup,
       "pwPerformanceGeneralGroup": pwPerformanceGeneralGroup,
       "pwPeformanceTotalGroup": pwPeformanceTotalGroup,
       "pwPerformanceIntervalGeneralGroup": pwPerformanceIntervalGeneralGroup,
       "pwPeformanceIntervalGroup": pwPeformanceIntervalGroup,
       "pwHCPeformanceIntervalGroup": pwHCPeformanceIntervalGroup,
       "pwMappingTablesGroup": pwMappingTablesGroup,
       "pwNotificationControlGroup": pwNotificationControlGroup,
       "pwNotificationGroup": pwNotificationGroup,
       "pwSignalingGroup": pwSignalingGroup,
       "pwCompliances": pwCompliances,
       "pwModuleFullCompliance": pwModuleFullCompliance,
       "pwModuleReadOnlyCompliance": pwModuleReadOnlyCompliance}
)
