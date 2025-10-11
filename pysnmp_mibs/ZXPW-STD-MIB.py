# SNMP MIB module (ZXPW-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXPW-STD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:42 2025
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

(HCPerfTimeElapsed,
 HCPerfValidIntervals) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(zxAnCesMib,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxAnCesMib")

(IANAPwPsnTypeTC,
 IANAPwTypeTC) = mibBuilder.importSymbols(
    "ZX-PWE3-MIB",
    "IANAPwPsnTypeTC",
    "IANAPwTypeTC")

(PwAttachmentIdentifierType,
 PwCapabilities,
 PwCwStatusTC,
 PwFragSize,
 PwFragStatus,
 PwGroupID,
 PwIDType,
 PwIndexType,
 PwOperStatusTC,
 PwStatus) = mibBuilder.importSymbols(
    "ZXPW-TC-STD-MIB",
    "PwAttachmentIdentifierType",
    "PwCapabilities",
    "PwCwStatusTC",
    "PwFragSize",
    "PwFragStatus",
    "PwGroupID",
    "PwIDType",
    "PwIndexType",
    "PwOperStatusTC",
    "PwStatus")


# MODULE-IDENTITY

zxPwStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxPwObjects_ObjectIdentity = ObjectIdentity
zxPwObjects = _ZxPwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1)
)
_ZxPwIndexNext_Type = Unsigned32
_ZxPwIndexNext_Object = MibScalar
zxPwIndexNext = _ZxPwIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 1),
    _ZxPwIndexNext_Type()
)
zxPwIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwIndexNext.setStatus("current")
_ZxPwTable_Object = MibTable
zxPwTable = _ZxPwTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2)
)
if mibBuilder.loadTexts:
    zxPwTable.setStatus("current")
_ZxPwEntry_Object = MibTableRow
zxPwEntry = _ZxPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1)
)
zxPwEntry.setIndexNames(
    (0, "ZXPW-STD-MIB", "zxPwIndex"),
)
if mibBuilder.loadTexts:
    zxPwEntry.setStatus("current")
_ZxPwIndex_Type = PwIndexType
_ZxPwIndex_Object = MibTableColumn
zxPwIndex = _ZxPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 1),
    _ZxPwIndex_Type()
)
zxPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxPwIndex.setStatus("current")
_ZxPwType_Type = IANAPwTypeTC
_ZxPwType_Object = MibTableColumn
zxPwType = _ZxPwType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 2),
    _ZxPwType_Type()
)
zxPwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwType.setStatus("current")


class _ZxPwOwner_Type(Integer32):
    """Custom type zxPwOwner based on Integer32"""
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


_ZxPwOwner_Type.__name__ = "Integer32"
_ZxPwOwner_Object = MibTableColumn
zxPwOwner = _ZxPwOwner_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 3),
    _ZxPwOwner_Type()
)
zxPwOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwOwner.setStatus("current")
_ZxPwPsnType_Type = IANAPwPsnTypeTC
_ZxPwPsnType_Object = MibTableColumn
zxPwPsnType = _ZxPwPsnType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 4),
    _ZxPwPsnType_Type()
)
zxPwPsnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwPsnType.setStatus("current")


class _ZxPwSetUpPriority_Type(Integer32):
    """Custom type zxPwSetUpPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxPwSetUpPriority_Type.__name__ = "Integer32"
_ZxPwSetUpPriority_Object = MibTableColumn
zxPwSetUpPriority = _ZxPwSetUpPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 5),
    _ZxPwSetUpPriority_Type()
)
zxPwSetUpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwSetUpPriority.setStatus("current")


class _ZxPwHoldingPriority_Type(Integer32):
    """Custom type zxPwHoldingPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxPwHoldingPriority_Type.__name__ = "Integer32"
_ZxPwHoldingPriority_Object = MibTableColumn
zxPwHoldingPriority = _ZxPwHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 6),
    _ZxPwHoldingPriority_Type()
)
zxPwHoldingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwHoldingPriority.setStatus("current")


class _ZxPwPeerAddrType_Type(InetAddressType):
    """Custom type zxPwPeerAddrType based on InetAddressType"""
    defaultValue = 1


_ZxPwPeerAddrType_Type.__name__ = "InetAddressType"
_ZxPwPeerAddrType_Object = MibTableColumn
zxPwPeerAddrType = _ZxPwPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 8),
    _ZxPwPeerAddrType_Type()
)
zxPwPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwPeerAddrType.setStatus("current")
_ZxPwPeerAddr_Type = InetAddress
_ZxPwPeerAddr_Object = MibTableColumn
zxPwPeerAddr = _ZxPwPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 9),
    _ZxPwPeerAddr_Type()
)
zxPwPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwPeerAddr.setStatus("current")


class _ZxPwAttachedPwIndex_Type(PwIndexType):
    """Custom type zxPwAttachedPwIndex based on PwIndexType"""
    defaultValue = 0


_ZxPwAttachedPwIndex_Type.__name__ = "PwIndexType"
_ZxPwAttachedPwIndex_Object = MibTableColumn
zxPwAttachedPwIndex = _ZxPwAttachedPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 10),
    _ZxPwAttachedPwIndex_Type()
)
zxPwAttachedPwIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwAttachedPwIndex.setStatus("current")


class _ZxPwIfIndex_Type(InterfaceIndexOrZero):
    """Custom type zxPwIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_ZxPwIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_ZxPwIfIndex_Object = MibTableColumn
zxPwIfIndex = _ZxPwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 11),
    _ZxPwIfIndex_Type()
)
zxPwIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwIfIndex.setStatus("current")
_ZxPwID_Type = PwIDType
_ZxPwID_Object = MibTableColumn
zxPwID = _ZxPwID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 12),
    _ZxPwID_Type()
)
zxPwID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwID.setStatus("current")
_ZxPwLocalGroupID_Type = PwGroupID
_ZxPwLocalGroupID_Object = MibTableColumn
zxPwLocalGroupID = _ZxPwLocalGroupID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 13),
    _ZxPwLocalGroupID_Type()
)
zxPwLocalGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwLocalGroupID.setStatus("current")
_ZxPwGroupAttachmentID_Type = PwAttachmentIdentifierType
_ZxPwGroupAttachmentID_Object = MibTableColumn
zxPwGroupAttachmentID = _ZxPwGroupAttachmentID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 14),
    _ZxPwGroupAttachmentID_Type()
)
zxPwGroupAttachmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwGroupAttachmentID.setStatus("current")
_ZxPwLocalAttachmentID_Type = PwAttachmentIdentifierType
_ZxPwLocalAttachmentID_Object = MibTableColumn
zxPwLocalAttachmentID = _ZxPwLocalAttachmentID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 15),
    _ZxPwLocalAttachmentID_Type()
)
zxPwLocalAttachmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwLocalAttachmentID.setStatus("current")
_ZxPwPeerAttachmentID_Type = PwAttachmentIdentifierType
_ZxPwPeerAttachmentID_Object = MibTableColumn
zxPwPeerAttachmentID = _ZxPwPeerAttachmentID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 16),
    _ZxPwPeerAttachmentID_Type()
)
zxPwPeerAttachmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwPeerAttachmentID.setStatus("current")


class _ZxPwCwPreference_Type(TruthValue):
    """Custom type zxPwCwPreference based on TruthValue"""
    defaultValue = 2


_ZxPwCwPreference_Type.__name__ = "TruthValue"
_ZxPwCwPreference_Object = MibTableColumn
zxPwCwPreference = _ZxPwCwPreference_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 17),
    _ZxPwCwPreference_Type()
)
zxPwCwPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCwPreference.setStatus("current")


class _ZxPwLocalIfMtu_Type(Unsigned32):
    """Custom type zxPwLocalIfMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxPwLocalIfMtu_Type.__name__ = "Unsigned32"
_ZxPwLocalIfMtu_Object = MibTableColumn
zxPwLocalIfMtu = _ZxPwLocalIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 18),
    _ZxPwLocalIfMtu_Type()
)
zxPwLocalIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwLocalIfMtu.setStatus("current")


class _ZxPwLocalIfString_Type(TruthValue):
    """Custom type zxPwLocalIfString based on TruthValue"""
    defaultValue = 2


_ZxPwLocalIfString_Type.__name__ = "TruthValue"
_ZxPwLocalIfString_Object = MibTableColumn
zxPwLocalIfString = _ZxPwLocalIfString_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 19),
    _ZxPwLocalIfString_Type()
)
zxPwLocalIfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwLocalIfString.setStatus("current")
_ZxPwLocalCapabAdvert_Type = PwCapabilities
_ZxPwLocalCapabAdvert_Object = MibTableColumn
zxPwLocalCapabAdvert = _ZxPwLocalCapabAdvert_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 20),
    _ZxPwLocalCapabAdvert_Type()
)
zxPwLocalCapabAdvert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwLocalCapabAdvert.setStatus("current")
_ZxPwRemoteGroupID_Type = PwGroupID
_ZxPwRemoteGroupID_Object = MibTableColumn
zxPwRemoteGroupID = _ZxPwRemoteGroupID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 21),
    _ZxPwRemoteGroupID_Type()
)
zxPwRemoteGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwRemoteGroupID.setStatus("current")
_ZxPwCwStatus_Type = PwCwStatusTC
_ZxPwCwStatus_Object = MibTableColumn
zxPwCwStatus = _ZxPwCwStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 22),
    _ZxPwCwStatus_Type()
)
zxPwCwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwCwStatus.setStatus("current")
_ZxPwRemoteIfMtu_Type = Unsigned32
_ZxPwRemoteIfMtu_Object = MibTableColumn
zxPwRemoteIfMtu = _ZxPwRemoteIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 23),
    _ZxPwRemoteIfMtu_Type()
)
zxPwRemoteIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwRemoteIfMtu.setStatus("current")


class _ZxPwRemoteIfString_Type(SnmpAdminString):
    """Custom type zxPwRemoteIfString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ZxPwRemoteIfString_Type.__name__ = "SnmpAdminString"
_ZxPwRemoteIfString_Object = MibTableColumn
zxPwRemoteIfString = _ZxPwRemoteIfString_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 24),
    _ZxPwRemoteIfString_Type()
)
zxPwRemoteIfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwRemoteIfString.setStatus("current")
_ZxPwRemoteCapabilities_Type = PwCapabilities
_ZxPwRemoteCapabilities_Object = MibTableColumn
zxPwRemoteCapabilities = _ZxPwRemoteCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 25),
    _ZxPwRemoteCapabilities_Type()
)
zxPwRemoteCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwRemoteCapabilities.setStatus("current")


class _ZxPwFragmentCfgSize_Type(PwFragSize):
    """Custom type zxPwFragmentCfgSize based on PwFragSize"""
    defaultValue = 0


_ZxPwFragmentCfgSize_Type.__name__ = "PwFragSize"
_ZxPwFragmentCfgSize_Object = MibTableColumn
zxPwFragmentCfgSize = _ZxPwFragmentCfgSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 26),
    _ZxPwFragmentCfgSize_Type()
)
zxPwFragmentCfgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwFragmentCfgSize.setStatus("current")
_ZxPwRmtFragCapability_Type = PwFragStatus
_ZxPwRmtFragCapability_Object = MibTableColumn
zxPwRmtFragCapability = _ZxPwRmtFragCapability_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 27),
    _ZxPwRmtFragCapability_Type()
)
zxPwRmtFragCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwRmtFragCapability.setStatus("current")


class _ZxPwFcsRetentioncfg_Type(Integer32):
    """Custom type zxPwFcsRetentioncfg based on Integer32"""
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


_ZxPwFcsRetentioncfg_Type.__name__ = "Integer32"
_ZxPwFcsRetentioncfg_Object = MibTableColumn
zxPwFcsRetentioncfg = _ZxPwFcsRetentioncfg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 28),
    _ZxPwFcsRetentioncfg_Type()
)
zxPwFcsRetentioncfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwFcsRetentioncfg.setStatus("current")


class _ZxPwFcsRetentionStatus_Type(Bits):
    """Custom type zxPwFcsRetentionStatus based on Bits"""
    namedValues = NamedValues(
        *(("remoteIndicationUnknown", 0),
          ("remoteRequestFcsRetention", 1),
          ("fcsRetentionEnabled", 2),
          ("fcsRetentionDisabled", 3),
          ("localFcsRetentionCfgErr", 4),
          ("fcsRetentionFcsSizeMismatch", 5))
    )

_ZxPwFcsRetentionStatus_Type.__name__ = "Bits"
_ZxPwFcsRetentionStatus_Object = MibTableColumn
zxPwFcsRetentionStatus = _ZxPwFcsRetentionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 29),
    _ZxPwFcsRetentionStatus_Type()
)
zxPwFcsRetentionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwFcsRetentionStatus.setStatus("current")
_ZxPwOutboundLabel_Type = Unsigned32
_ZxPwOutboundLabel_Object = MibTableColumn
zxPwOutboundLabel = _ZxPwOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 30),
    _ZxPwOutboundLabel_Type()
)
zxPwOutboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwOutboundLabel.setStatus("current")
_ZxPwInboundLabel_Type = Unsigned32
_ZxPwInboundLabel_Object = MibTableColumn
zxPwInboundLabel = _ZxPwInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 31),
    _ZxPwInboundLabel_Type()
)
zxPwInboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwInboundLabel.setStatus("current")
_ZxPwName_Type = SnmpAdminString
_ZxPwName_Object = MibTableColumn
zxPwName = _ZxPwName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 32),
    _ZxPwName_Type()
)
zxPwName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwName.setStatus("current")
_ZxPwDescr_Type = SnmpAdminString
_ZxPwDescr_Object = MibTableColumn
zxPwDescr = _ZxPwDescr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 33),
    _ZxPwDescr_Type()
)
zxPwDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwDescr.setStatus("current")


class _ZxPwCreateTime_Type(DisplayString):
    """Custom type zxPwCreateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_ZxPwCreateTime_Type.__name__ = "DisplayString"
_ZxPwCreateTime_Object = MibTableColumn
zxPwCreateTime = _ZxPwCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 34),
    _ZxPwCreateTime_Type()
)
zxPwCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwCreateTime.setStatus("current")


class _ZxPwUpTime_Type(DisplayString):
    """Custom type zxPwUpTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_ZxPwUpTime_Type.__name__ = "DisplayString"
_ZxPwUpTime_Object = MibTableColumn
zxPwUpTime = _ZxPwUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 35),
    _ZxPwUpTime_Type()
)
zxPwUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwUpTime.setStatus("current")
_ZxPwLastChange_Type = TimeTicks
_ZxPwLastChange_Object = MibTableColumn
zxPwLastChange = _ZxPwLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 36),
    _ZxPwLastChange_Type()
)
zxPwLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwLastChange.setStatus("current")


class _ZxPwAdminStatus_Type(Integer32):
    """Custom type zxPwAdminStatus based on Integer32"""
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


_ZxPwAdminStatus_Type.__name__ = "Integer32"
_ZxPwAdminStatus_Object = MibTableColumn
zxPwAdminStatus = _ZxPwAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 37),
    _ZxPwAdminStatus_Type()
)
zxPwAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwAdminStatus.setStatus("current")
_ZxPwOperStatus_Type = PwOperStatusTC
_ZxPwOperStatus_Object = MibTableColumn
zxPwOperStatus = _ZxPwOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 38),
    _ZxPwOperStatus_Type()
)
zxPwOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwOperStatus.setStatus("current")
_ZxPwLocalStatus_Type = PwStatus
_ZxPwLocalStatus_Object = MibTableColumn
zxPwLocalStatus = _ZxPwLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 39),
    _ZxPwLocalStatus_Type()
)
zxPwLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwLocalStatus.setStatus("current")


class _ZxPwRemoteStatusCapable_Type(Integer32):
    """Custom type zxPwRemoteStatusCapable based on Integer32"""
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


_ZxPwRemoteStatusCapable_Type.__name__ = "Integer32"
_ZxPwRemoteStatusCapable_Object = MibTableColumn
zxPwRemoteStatusCapable = _ZxPwRemoteStatusCapable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 40),
    _ZxPwRemoteStatusCapable_Type()
)
zxPwRemoteStatusCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwRemoteStatusCapable.setStatus("current")
_ZxPwRemoteStatus_Type = PwStatus
_ZxPwRemoteStatus_Object = MibTableColumn
zxPwRemoteStatus = _ZxPwRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 41),
    _ZxPwRemoteStatus_Type()
)
zxPwRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwRemoteStatus.setStatus("current")
_ZxPwTimeElapsed_Type = HCPerfTimeElapsed
_ZxPwTimeElapsed_Object = MibTableColumn
zxPwTimeElapsed = _ZxPwTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 42),
    _ZxPwTimeElapsed_Type()
)
zxPwTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwTimeElapsed.setStatus("current")
_ZxPwValidIntervals_Type = HCPerfValidIntervals
_ZxPwValidIntervals_Object = MibTableColumn
zxPwValidIntervals = _ZxPwValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 43),
    _ZxPwValidIntervals_Type()
)
zxPwValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwValidIntervals.setStatus("current")
_ZxPwRowStatus_Type = RowStatus
_ZxPwRowStatus_Object = MibTableColumn
zxPwRowStatus = _ZxPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 44),
    _ZxPwRowStatus_Type()
)
zxPwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwRowStatus.setStatus("current")
_ZxPwStorageType_Type = StorageType
_ZxPwStorageType_Object = MibTableColumn
zxPwStorageType = _ZxPwStorageType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 45),
    _ZxPwStorageType_Type()
)
zxPwStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwStorageType.setStatus("current")


class _ZxPwPeerTos_Type(Integer32):
    """Custom type zxPwPeerTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ZxPwPeerTos_Type.__name__ = "Integer32"
_ZxPwPeerTos_Object = MibTableColumn
zxPwPeerTos = _ZxPwPeerTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 1, 1, 2, 1, 46),
    _ZxPwPeerTos_Type()
)
zxPwPeerTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwPeerTos.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXPW-STD-MIB",
    **{"zxPwStdMIB": zxPwStdMIB,
       "zxPwObjects": zxPwObjects,
       "zxPwIndexNext": zxPwIndexNext,
       "zxPwTable": zxPwTable,
       "zxPwEntry": zxPwEntry,
       "zxPwIndex": zxPwIndex,
       "zxPwType": zxPwType,
       "zxPwOwner": zxPwOwner,
       "zxPwPsnType": zxPwPsnType,
       "zxPwSetUpPriority": zxPwSetUpPriority,
       "zxPwHoldingPriority": zxPwHoldingPriority,
       "zxPwPeerAddrType": zxPwPeerAddrType,
       "zxPwPeerAddr": zxPwPeerAddr,
       "zxPwAttachedPwIndex": zxPwAttachedPwIndex,
       "zxPwIfIndex": zxPwIfIndex,
       "zxPwID": zxPwID,
       "zxPwLocalGroupID": zxPwLocalGroupID,
       "zxPwGroupAttachmentID": zxPwGroupAttachmentID,
       "zxPwLocalAttachmentID": zxPwLocalAttachmentID,
       "zxPwPeerAttachmentID": zxPwPeerAttachmentID,
       "zxPwCwPreference": zxPwCwPreference,
       "zxPwLocalIfMtu": zxPwLocalIfMtu,
       "zxPwLocalIfString": zxPwLocalIfString,
       "zxPwLocalCapabAdvert": zxPwLocalCapabAdvert,
       "zxPwRemoteGroupID": zxPwRemoteGroupID,
       "zxPwCwStatus": zxPwCwStatus,
       "zxPwRemoteIfMtu": zxPwRemoteIfMtu,
       "zxPwRemoteIfString": zxPwRemoteIfString,
       "zxPwRemoteCapabilities": zxPwRemoteCapabilities,
       "zxPwFragmentCfgSize": zxPwFragmentCfgSize,
       "zxPwRmtFragCapability": zxPwRmtFragCapability,
       "zxPwFcsRetentioncfg": zxPwFcsRetentioncfg,
       "zxPwFcsRetentionStatus": zxPwFcsRetentionStatus,
       "zxPwOutboundLabel": zxPwOutboundLabel,
       "zxPwInboundLabel": zxPwInboundLabel,
       "zxPwName": zxPwName,
       "zxPwDescr": zxPwDescr,
       "zxPwCreateTime": zxPwCreateTime,
       "zxPwUpTime": zxPwUpTime,
       "zxPwLastChange": zxPwLastChange,
       "zxPwAdminStatus": zxPwAdminStatus,
       "zxPwOperStatus": zxPwOperStatus,
       "zxPwLocalStatus": zxPwLocalStatus,
       "zxPwRemoteStatusCapable": zxPwRemoteStatusCapable,
       "zxPwRemoteStatus": zxPwRemoteStatus,
       "zxPwTimeElapsed": zxPwTimeElapsed,
       "zxPwValidIntervals": zxPwValidIntervals,
       "zxPwRowStatus": zxPwRowStatus,
       "zxPwStorageType": zxPwStorageType,
       "zxPwPeerTos": zxPwPeerTos}
)
