# SNMP MIB module (Aricent-L2VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/Aricent-L2VPN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:41:59 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(MplsLdpIdentifier,
 MplsLsrIdentifier) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLdpIdentifier",
    "MplsLsrIdentifier")

(pwIndex,) = mibBuilder.importSymbols(
    "PW-STD-MIB",
    "pwIndex")

(PwGroupID,
 PwIDType,
 PwIndexOrZeroType,
 PwOperStatusTC) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwGroupID",
    "PwIDType",
    "PwIndexOrZeroType",
    "PwOperStatusTC")

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


# MODULE-IDENTITY

fsL2VpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72)
)
if mibBuilder.loadTexts:
    fsL2VpnMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VplsBgpRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VplsBgpRouteTarget(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VplsBgpRouteTargetType(TextualConvention, Integer32):
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
        *(("import", 1),
          ("export", 2),
          ("both", 3))
    )



class VPNIdOrZero(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 7),
    )



class FsL2VpnPwStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("pwNotForwarding", 0),
          ("servicePwRxFault", 1),
          ("servicePwTxFault", 2),
          ("psnPwRxFault", 3),
          ("psnPwTxFault", 4),
          ("pwForwardingStandby", 5),
          ("pwSwitchoverRequest", 6))
    )


# MIB Managed Objects in the order of their OIDs

_VplsNotifications_ObjectIdentity = ObjectIdentity
vplsNotifications = _VplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 0)
)
_VplsObjects_ObjectIdentity = ObjectIdentity
vplsObjects = _VplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1)
)
_VplsConfigIndexNext_Type = Unsigned32
_VplsConfigIndexNext_Object = MibScalar
vplsConfigIndexNext = _VplsConfigIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 1),
    _VplsConfigIndexNext_Type()
)
vplsConfigIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsConfigIndexNext.setStatus("current")
_VplsConfigTable_Object = MibTable
vplsConfigTable = _VplsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2)
)
if mibBuilder.loadTexts:
    vplsConfigTable.setStatus("current")
_VplsConfigEntry_Object = MibTableRow
vplsConfigEntry = _VplsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1)
)
vplsConfigEntry.setIndexNames(
    (0, "Aricent-L2VPN-MIB", "vplsConfigIndex"),
)
if mibBuilder.loadTexts:
    vplsConfigEntry.setStatus("current")


class _VplsConfigIndex_Type(Unsigned32):
    """Custom type vplsConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VplsConfigIndex_Type.__name__ = "Unsigned32"
_VplsConfigIndex_Object = MibTableColumn
vplsConfigIndex = _VplsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 1),
    _VplsConfigIndex_Type()
)
vplsConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vplsConfigIndex.setStatus("current")


class _VplsConfigName_Type(SnmpAdminString):
    """Custom type vplsConfigName based on SnmpAdminString"""
    defaultValue = OctetString("")


_VplsConfigName_Type.__name__ = "SnmpAdminString"
_VplsConfigName_Object = MibTableColumn
vplsConfigName = _VplsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 2),
    _VplsConfigName_Type()
)
vplsConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigName.setStatus("current")


class _VplsConfigDescr_Type(SnmpAdminString):
    """Custom type vplsConfigDescr based on SnmpAdminString"""
    defaultValue = OctetString("")


_VplsConfigDescr_Type.__name__ = "SnmpAdminString"
_VplsConfigDescr_Object = MibTableColumn
vplsConfigDescr = _VplsConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 3),
    _VplsConfigDescr_Type()
)
vplsConfigDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigDescr.setStatus("current")


class _VplsConfigAdminStatus_Type(Integer32):
    """Custom type vplsConfigAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_VplsConfigAdminStatus_Type.__name__ = "Integer32"
_VplsConfigAdminStatus_Object = MibTableColumn
vplsConfigAdminStatus = _VplsConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 4),
    _VplsConfigAdminStatus_Type()
)
vplsConfigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigAdminStatus.setStatus("current")


class _VplsConfigMacLearning_Type(TruthValue):
    """Custom type vplsConfigMacLearning based on TruthValue"""
    defaultValue = 1


_VplsConfigMacLearning_Type.__name__ = "TruthValue"
_VplsConfigMacLearning_Object = MibTableColumn
vplsConfigMacLearning = _VplsConfigMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 6),
    _VplsConfigMacLearning_Type()
)
vplsConfigMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMacLearning.setStatus("current")


class _VplsConfigDiscardUnknownDest_Type(TruthValue):
    """Custom type vplsConfigDiscardUnknownDest based on TruthValue"""
    defaultValue = 2


_VplsConfigDiscardUnknownDest_Type.__name__ = "TruthValue"
_VplsConfigDiscardUnknownDest_Object = MibTableColumn
vplsConfigDiscardUnknownDest = _VplsConfigDiscardUnknownDest_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 7),
    _VplsConfigDiscardUnknownDest_Type()
)
vplsConfigDiscardUnknownDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigDiscardUnknownDest.setStatus("current")


class _VplsConfigMacAging_Type(TruthValue):
    """Custom type vplsConfigMacAging based on TruthValue"""
    defaultValue = 1


_VplsConfigMacAging_Type.__name__ = "TruthValue"
_VplsConfigMacAging_Object = MibTableColumn
vplsConfigMacAging = _VplsConfigMacAging_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 8),
    _VplsConfigMacAging_Type()
)
vplsConfigMacAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMacAging.setStatus("current")


class _VplsConfigFwdFullHighWatermark_Type(Unsigned32):
    """Custom type vplsConfigFwdFullHighWatermark based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VplsConfigFwdFullHighWatermark_Type.__name__ = "Unsigned32"
_VplsConfigFwdFullHighWatermark_Object = MibTableColumn
vplsConfigFwdFullHighWatermark = _VplsConfigFwdFullHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 10),
    _VplsConfigFwdFullHighWatermark_Type()
)
vplsConfigFwdFullHighWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigFwdFullHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    vplsConfigFwdFullHighWatermark.setUnits("percentage")


class _VplsConfigFwdFullLowWatermark_Type(Unsigned32):
    """Custom type vplsConfigFwdFullLowWatermark based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VplsConfigFwdFullLowWatermark_Type.__name__ = "Unsigned32"
_VplsConfigFwdFullLowWatermark_Object = MibTableColumn
vplsConfigFwdFullLowWatermark = _VplsConfigFwdFullLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 11),
    _VplsConfigFwdFullLowWatermark_Type()
)
vplsConfigFwdFullLowWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigFwdFullLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    vplsConfigFwdFullLowWatermark.setUnits("percentage")
_VplsConfigRowStatus_Type = RowStatus
_VplsConfigRowStatus_Object = MibTableColumn
vplsConfigRowStatus = _VplsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 12),
    _VplsConfigRowStatus_Type()
)
vplsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigRowStatus.setStatus("current")


class _VplsConfigMtu_Type(Unsigned32):
    """Custom type vplsConfigMtu based on Unsigned32"""
    defaultValue = 1518

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_VplsConfigMtu_Type.__name__ = "Unsigned32"
_VplsConfigMtu_Object = MibTableColumn
vplsConfigMtu = _VplsConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 13),
    _VplsConfigMtu_Type()
)
vplsConfigMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMtu.setStatus("current")
_VplsConfigVpnId_Type = VPNIdOrZero
_VplsConfigVpnId_Object = MibTableColumn
vplsConfigVpnId = _VplsConfigVpnId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 14),
    _VplsConfigVpnId_Type()
)
vplsConfigVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsConfigVpnId.setStatus("current")


class _VplsConfigStorageType_Type(StorageType):
    """Custom type vplsConfigStorageType based on StorageType"""
    defaultValue = 2


_VplsConfigStorageType_Type.__name__ = "StorageType"
_VplsConfigStorageType_Object = MibTableColumn
vplsConfigStorageType = _VplsConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 15),
    _VplsConfigStorageType_Type()
)
vplsConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigStorageType.setStatus("current")


class _VplsConfigSignalingType_Type(Integer32):
    """Custom type vplsConfigSignalingType based on Integer32"""
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
        *(("ldp", 1),
          ("bgp", 2),
          ("none", 3))
    )


_VplsConfigSignalingType_Type.__name__ = "Integer32"
_VplsConfigSignalingType_Object = MibTableColumn
vplsConfigSignalingType = _VplsConfigSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 2, 1, 16),
    _VplsConfigSignalingType_Type()
)
vplsConfigSignalingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigSignalingType.setStatus("current")
_VplsStatusTable_Object = MibTable
vplsStatusTable = _VplsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 3)
)
if mibBuilder.loadTexts:
    vplsStatusTable.setStatus("current")
_VplsStatusEntry_Object = MibTableRow
vplsStatusEntry = _VplsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 3, 1)
)
vplsStatusEntry.setIndexNames(
    (0, "Aricent-L2VPN-MIB", "vplsConfigIndex"),
)
if mibBuilder.loadTexts:
    vplsStatusEntry.setStatus("current")


class _VplsStatusOperStatus_Type(Integer32):
    """Custom type vplsStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("up", 1),
          ("down", 2))
    )


_VplsStatusOperStatus_Type.__name__ = "Integer32"
_VplsStatusOperStatus_Object = MibTableColumn
vplsStatusOperStatus = _VplsStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 3, 1, 1),
    _VplsStatusOperStatus_Type()
)
vplsStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusOperStatus.setStatus("current")
_VplsStatusPeerCount_Type = Counter32
_VplsStatusPeerCount_Object = MibTableColumn
vplsStatusPeerCount = _VplsStatusPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 3, 1, 2),
    _VplsStatusPeerCount_Type()
)
vplsStatusPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusPeerCount.setStatus("current")
_VplsPwBindTable_Object = MibTable
vplsPwBindTable = _VplsPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 4)
)
if mibBuilder.loadTexts:
    vplsPwBindTable.setStatus("current")
_VplsPwBindEntry_Object = MibTableRow
vplsPwBindEntry = _VplsPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 4, 1)
)
vplsPwBindEntry.setIndexNames(
    (0, "Aricent-L2VPN-MIB", "vplsConfigIndex"),
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    vplsPwBindEntry.setStatus("current")


class _VplsPwBindConfigType_Type(Integer32):
    """Custom type vplsPwBindConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("autodiscovery", 2))
    )


_VplsPwBindConfigType_Type.__name__ = "Integer32"
_VplsPwBindConfigType_Object = MibTableColumn
vplsPwBindConfigType = _VplsPwBindConfigType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 4, 1, 1),
    _VplsPwBindConfigType_Type()
)
vplsPwBindConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwBindConfigType.setStatus("current")


class _VplsPwBindType_Type(Integer32):
    """Custom type vplsPwBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mesh", 1),
          ("spoke", 2))
    )


_VplsPwBindType_Type.__name__ = "Integer32"
_VplsPwBindType_Object = MibTableColumn
vplsPwBindType = _VplsPwBindType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 4, 1, 2),
    _VplsPwBindType_Type()
)
vplsPwBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwBindType.setStatus("current")
_VplsPwBindRowStatus_Type = RowStatus
_VplsPwBindRowStatus_Object = MibTableColumn
vplsPwBindRowStatus = _VplsPwBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 4, 1, 3),
    _VplsPwBindRowStatus_Type()
)
vplsPwBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwBindRowStatus.setStatus("current")


class _VplsPwBindStorageType_Type(StorageType):
    """Custom type vplsPwBindStorageType based on StorageType"""
    defaultValue = 2


_VplsPwBindStorageType_Type.__name__ = "StorageType"
_VplsPwBindStorageType_Object = MibTableColumn
vplsPwBindStorageType = _VplsPwBindStorageType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 4, 1, 4),
    _VplsPwBindStorageType_Type()
)
vplsPwBindStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwBindStorageType.setStatus("current")
_VplsBgpADConfigTable_Object = MibTable
vplsBgpADConfigTable = _VplsBgpADConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 5)
)
if mibBuilder.loadTexts:
    vplsBgpADConfigTable.setStatus("current")
_VplsBgpADConfigEntry_Object = MibTableRow
vplsBgpADConfigEntry = _VplsBgpADConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 5, 1)
)
vplsBgpADConfigEntry.setIndexNames(
    (0, "Aricent-L2VPN-MIB", "vplsConfigIndex"),
)
if mibBuilder.loadTexts:
    vplsBgpADConfigEntry.setStatus("current")
_VplsBgpADConfigRouteDistinguisher_Type = VplsBgpRouteDistinguisher
_VplsBgpADConfigRouteDistinguisher_Object = MibTableColumn
vplsBgpADConfigRouteDistinguisher = _VplsBgpADConfigRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 5, 1, 1),
    _VplsBgpADConfigRouteDistinguisher_Type()
)
vplsBgpADConfigRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpADConfigRouteDistinguisher.setStatus("current")


class _VplsBgpADConfigPrefix_Type(Unsigned32):
    """Custom type vplsBgpADConfigPrefix based on Unsigned32"""
    defaultValue = 0


_VplsBgpADConfigPrefix_Type.__name__ = "Unsigned32"
_VplsBgpADConfigPrefix_Object = MibTableColumn
vplsBgpADConfigPrefix = _VplsBgpADConfigPrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 5, 1, 2),
    _VplsBgpADConfigPrefix_Type()
)
vplsBgpADConfigPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpADConfigPrefix.setStatus("current")
_VplsBgpADConfigVplsId_Type = VplsBgpRouteDistinguisher
_VplsBgpADConfigVplsId_Object = MibTableColumn
vplsBgpADConfigVplsId = _VplsBgpADConfigVplsId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 5, 1, 3),
    _VplsBgpADConfigVplsId_Type()
)
vplsBgpADConfigVplsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpADConfigVplsId.setStatus("current")
_VplsBgpADConfigRowStatus_Type = RowStatus
_VplsBgpADConfigRowStatus_Object = MibTableColumn
vplsBgpADConfigRowStatus = _VplsBgpADConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 5, 1, 4),
    _VplsBgpADConfigRowStatus_Type()
)
vplsBgpADConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpADConfigRowStatus.setStatus("current")


class _VplsBgpADConfigStorageType_Type(StorageType):
    """Custom type vplsBgpADConfigStorageType based on StorageType"""
    defaultValue = 3


_VplsBgpADConfigStorageType_Type.__name__ = "StorageType"
_VplsBgpADConfigStorageType_Object = MibTableColumn
vplsBgpADConfigStorageType = _VplsBgpADConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 5, 1, 5),
    _VplsBgpADConfigStorageType_Type()
)
vplsBgpADConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpADConfigStorageType.setStatus("current")
_VplsBgpRteTargetTable_Object = MibTable
vplsBgpRteTargetTable = _VplsBgpRteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 6)
)
if mibBuilder.loadTexts:
    vplsBgpRteTargetTable.setStatus("current")
_VplsBgpRteTargetEntry_Object = MibTableRow
vplsBgpRteTargetEntry = _VplsBgpRteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 6, 1)
)
vplsBgpRteTargetEntry.setIndexNames(
    (0, "Aricent-L2VPN-MIB", "vplsConfigIndex"),
    (0, "Aricent-L2VPN-MIB", "vplsBgpRteTargetIndex"),
)
if mibBuilder.loadTexts:
    vplsBgpRteTargetEntry.setStatus("current")
_VplsBgpRteTargetIndex_Type = Unsigned32
_VplsBgpRteTargetIndex_Object = MibTableColumn
vplsBgpRteTargetIndex = _VplsBgpRteTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 6, 1, 1),
    _VplsBgpRteTargetIndex_Type()
)
vplsBgpRteTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vplsBgpRteTargetIndex.setStatus("current")
_VplsBgpRteTargetRTType_Type = VplsBgpRouteTargetType
_VplsBgpRteTargetRTType_Object = MibTableColumn
vplsBgpRteTargetRTType = _VplsBgpRteTargetRTType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 6, 1, 2),
    _VplsBgpRteTargetRTType_Type()
)
vplsBgpRteTargetRTType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpRteTargetRTType.setStatus("current")
_VplsBgpRteTargetRT_Type = VplsBgpRouteTarget
_VplsBgpRteTargetRT_Object = MibTableColumn
vplsBgpRteTargetRT = _VplsBgpRteTargetRT_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 6, 1, 3),
    _VplsBgpRteTargetRT_Type()
)
vplsBgpRteTargetRT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpRteTargetRT.setStatus("current")
_VplsBgpRteTargetRTRowStatus_Type = RowStatus
_VplsBgpRteTargetRTRowStatus_Object = MibTableColumn
vplsBgpRteTargetRTRowStatus = _VplsBgpRteTargetRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 6, 1, 4),
    _VplsBgpRteTargetRTRowStatus_Type()
)
vplsBgpRteTargetRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpRteTargetRTRowStatus.setStatus("current")


class _VplsBgpRteTargetStorageType_Type(StorageType):
    """Custom type vplsBgpRteTargetStorageType based on StorageType"""
    defaultValue = 2


_VplsBgpRteTargetStorageType_Type.__name__ = "StorageType"
_VplsBgpRteTargetStorageType_Object = MibTableColumn
vplsBgpRteTargetStorageType = _VplsBgpRteTargetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 6, 1, 5),
    _VplsBgpRteTargetStorageType_Type()
)
vplsBgpRteTargetStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpRteTargetStorageType.setStatus("current")


class _VplsStatusNotifEnable_Type(TruthValue):
    """Custom type vplsStatusNotifEnable based on TruthValue"""
    defaultValue = 2


_VplsStatusNotifEnable_Type.__name__ = "TruthValue"
_VplsStatusNotifEnable_Object = MibScalar
vplsStatusNotifEnable = _VplsStatusNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 7),
    _VplsStatusNotifEnable_Type()
)
vplsStatusNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vplsStatusNotifEnable.setStatus("current")


class _VplsNotificationMaxRate_Type(Unsigned32):
    """Custom type vplsNotificationMaxRate based on Unsigned32"""
    defaultValue = 0


_VplsNotificationMaxRate_Type.__name__ = "Unsigned32"
_VplsNotificationMaxRate_Object = MibScalar
vplsNotificationMaxRate = _VplsNotificationMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 1, 8),
    _VplsNotificationMaxRate_Type()
)
vplsNotificationMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vplsNotificationMaxRate.setStatus("current")
_VplsConformance_ObjectIdentity = ObjectIdentity
vplsConformance = _VplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 2)
)
_VplsCompliances_ObjectIdentity = ObjectIdentity
vplsCompliances = _VplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 2, 1)
)
_VplsGroups_ObjectIdentity = ObjectIdentity
vplsGroups = _VplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 2, 2)
)
_PwRedundancyScalar_ObjectIdentity = ObjectIdentity
pwRedundancyScalar = _PwRedundancyScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 3)
)


class _FsL2VpnPwRedundancyStatus_Type(Integer32):
    """Custom type fsL2VpnPwRedundancyStatus based on Integer32"""
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


_FsL2VpnPwRedundancyStatus_Type.__name__ = "Integer32"
_FsL2VpnPwRedundancyStatus_Object = MibScalar
fsL2VpnPwRedundancyStatus = _FsL2VpnPwRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 3, 1),
    _FsL2VpnPwRedundancyStatus_Type()
)
fsL2VpnPwRedundancyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsL2VpnPwRedundancyStatus.setStatus("current")


class _FsL2VpnPwRedNegotiationTimeOut_Type(Unsigned32):
    """Custom type fsL2VpnPwRedNegotiationTimeOut based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsL2VpnPwRedNegotiationTimeOut_Type.__name__ = "Unsigned32"
_FsL2VpnPwRedNegotiationTimeOut_Object = MibScalar
fsL2VpnPwRedNegotiationTimeOut = _FsL2VpnPwRedNegotiationTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 3, 2),
    _FsL2VpnPwRedNegotiationTimeOut_Type()
)
fsL2VpnPwRedNegotiationTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsL2VpnPwRedNegotiationTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    fsL2VpnPwRedNegotiationTimeOut.setUnits("seconds")


class _FsL2VpnPwRedundancySyncFailNotifyEnable_Type(TruthValue):
    """Custom type fsL2VpnPwRedundancySyncFailNotifyEnable based on TruthValue"""
    defaultValue = 2


_FsL2VpnPwRedundancySyncFailNotifyEnable_Type.__name__ = "TruthValue"
_FsL2VpnPwRedundancySyncFailNotifyEnable_Object = MibScalar
fsL2VpnPwRedundancySyncFailNotifyEnable = _FsL2VpnPwRedundancySyncFailNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 3, 3),
    _FsL2VpnPwRedundancySyncFailNotifyEnable_Type()
)
fsL2VpnPwRedundancySyncFailNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsL2VpnPwRedundancySyncFailNotifyEnable.setStatus("current")


class _FsL2VpnPwRedundancyPwStatusNotifyEnable_Type(TruthValue):
    """Custom type fsL2VpnPwRedundancyPwStatusNotifyEnable based on TruthValue"""
    defaultValue = 2


_FsL2VpnPwRedundancyPwStatusNotifyEnable_Type.__name__ = "TruthValue"
_FsL2VpnPwRedundancyPwStatusNotifyEnable_Object = MibScalar
fsL2VpnPwRedundancyPwStatusNotifyEnable = _FsL2VpnPwRedundancyPwStatusNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 3, 4),
    _FsL2VpnPwRedundancyPwStatusNotifyEnable_Type()
)
fsL2VpnPwRedundancyPwStatusNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsL2VpnPwRedundancyPwStatusNotifyEnable.setStatus("current")
_PwRedundancyObjects_ObjectIdentity = ObjectIdentity
pwRedundancyObjects = _PwRedundancyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4)
)
_FsL2VpnPwRedTraps_ObjectIdentity = ObjectIdentity
fsL2VpnPwRedTraps = _FsL2VpnPwRedTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 0)
)
_FsL2VpnPwRedGroupTable_Object = MibTable
fsL2VpnPwRedGroupTable = _FsL2VpnPwRedGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1)
)
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupTable.setStatus("current")
_FsL2VpnPwRedGroupEntry_Object = MibTableRow
fsL2VpnPwRedGroupEntry = _FsL2VpnPwRedGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1)
)
fsL2VpnPwRedGroupEntry.setIndexNames(
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedGroupIndex"),
)
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupEntry.setStatus("current")
_FsL2VpnPwRedGroupIndex_Type = Unsigned32
_FsL2VpnPwRedGroupIndex_Object = MibTableColumn
fsL2VpnPwRedGroupIndex = _FsL2VpnPwRedGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 1),
    _FsL2VpnPwRedGroupIndex_Type()
)
fsL2VpnPwRedGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupIndex.setStatus("current")


class _FsL2VpnPwRedGroupProtType_Type(Integer32):
    """Custom type fsL2VpnPwRedGroupProtType based on Integer32"""
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
        *(("onePlusOne", 1),
          ("oneIsToOne", 2),
          ("oneIsToN", 3))
    )


_FsL2VpnPwRedGroupProtType_Type.__name__ = "Integer32"
_FsL2VpnPwRedGroupProtType_Object = MibTableColumn
fsL2VpnPwRedGroupProtType = _FsL2VpnPwRedGroupProtType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 2),
    _FsL2VpnPwRedGroupProtType_Type()
)
fsL2VpnPwRedGroupProtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupProtType.setStatus("current")


class _FsL2VpnPwRedGroupReversionType_Type(Integer32):
    """Custom type fsL2VpnPwRedGroupReversionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("revertive", 1),
          ("nonRevertive", 2))
    )


_FsL2VpnPwRedGroupReversionType_Type.__name__ = "Integer32"
_FsL2VpnPwRedGroupReversionType_Object = MibTableColumn
fsL2VpnPwRedGroupReversionType = _FsL2VpnPwRedGroupReversionType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 3),
    _FsL2VpnPwRedGroupReversionType_Type()
)
fsL2VpnPwRedGroupReversionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupReversionType.setStatus("current")


class _FsL2VpnPwRedGroupContentionResolutionMethod_Type(Integer32):
    """Custom type fsL2VpnPwRedGroupContentionResolutionMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("masterslave", 2))
    )


_FsL2VpnPwRedGroupContentionResolutionMethod_Type.__name__ = "Integer32"
_FsL2VpnPwRedGroupContentionResolutionMethod_Object = MibTableColumn
fsL2VpnPwRedGroupContentionResolutionMethod = _FsL2VpnPwRedGroupContentionResolutionMethod_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 4),
    _FsL2VpnPwRedGroupContentionResolutionMethod_Type()
)
fsL2VpnPwRedGroupContentionResolutionMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupContentionResolutionMethod.setStatus("current")


class _FsL2VpnPwRedGroupLockoutProtection_Type(Integer32):
    """Custom type fsL2VpnPwRedGroupLockoutProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FsL2VpnPwRedGroupLockoutProtection_Type.__name__ = "Integer32"
_FsL2VpnPwRedGroupLockoutProtection_Object = MibTableColumn
fsL2VpnPwRedGroupLockoutProtection = _FsL2VpnPwRedGroupLockoutProtection_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 5),
    _FsL2VpnPwRedGroupLockoutProtection_Type()
)
fsL2VpnPwRedGroupLockoutProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupLockoutProtection.setStatus("current")


class _FsL2VpnPwRedGroupMasterSlaveMode_Type(Integer32):
    """Custom type fsL2VpnPwRedGroupMasterSlaveMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_FsL2VpnPwRedGroupMasterSlaveMode_Type.__name__ = "Integer32"
_FsL2VpnPwRedGroupMasterSlaveMode_Object = MibTableColumn
fsL2VpnPwRedGroupMasterSlaveMode = _FsL2VpnPwRedGroupMasterSlaveMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 6),
    _FsL2VpnPwRedGroupMasterSlaveMode_Type()
)
fsL2VpnPwRedGroupMasterSlaveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupMasterSlaveMode.setStatus("current")


class _FsL2VpnPwRedGroupDualHomeApps_Type(Bits):
    """Custom type fsL2VpnPwRedGroupDualHomeApps based on Bits"""
    defaultHexValue = ""

    namedValues = NamedValues(
        ("lagg", 0)
    )

_FsL2VpnPwRedGroupDualHomeApps_Type.__name__ = "Bits"
_FsL2VpnPwRedGroupDualHomeApps_Object = MibTableColumn
fsL2VpnPwRedGroupDualHomeApps = _FsL2VpnPwRedGroupDualHomeApps_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 7),
    _FsL2VpnPwRedGroupDualHomeApps_Type()
)
fsL2VpnPwRedGroupDualHomeApps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupDualHomeApps.setStatus("current")


class _FsL2VpnPwRedGroupName_Type(DisplayString):
    """Custom type fsL2VpnPwRedGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsL2VpnPwRedGroupName_Type.__name__ = "DisplayString"
_FsL2VpnPwRedGroupName_Object = MibTableColumn
fsL2VpnPwRedGroupName = _FsL2VpnPwRedGroupName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 8),
    _FsL2VpnPwRedGroupName_Type()
)
fsL2VpnPwRedGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupName.setStatus("current")


class _FsL2VpnPwRedGroupStatus_Type(Bits):
    """Custom type fsL2VpnPwRedGroupStatus based on Bits"""
    namedValues = NamedValues(
        *(("forwardingNegotiaton", 0),
          ("switchoverNegotiaton", 1),
          ("negotiatonSuccess", 2),
          ("waitingToRestore", 3),
          ("redundancyUnAvailable", 4))
    )

_FsL2VpnPwRedGroupStatus_Type.__name__ = "Bits"
_FsL2VpnPwRedGroupStatus_Object = MibTableColumn
fsL2VpnPwRedGroupStatus = _FsL2VpnPwRedGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 9),
    _FsL2VpnPwRedGroupStatus_Type()
)
fsL2VpnPwRedGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupStatus.setStatus("current")
_FsL2VpnPwRedGroupOperActivePw_Type = PwIndexOrZeroType
_FsL2VpnPwRedGroupOperActivePw_Object = MibTableColumn
fsL2VpnPwRedGroupOperActivePw = _FsL2VpnPwRedGroupOperActivePw_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 10),
    _FsL2VpnPwRedGroupOperActivePw_Type()
)
fsL2VpnPwRedGroupOperActivePw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupOperActivePw.setStatus("current")


class _FsL2VpnPwRedGroupWtrTimer_Type(Unsigned32):
    """Custom type fsL2VpnPwRedGroupWtrTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_FsL2VpnPwRedGroupWtrTimer_Type.__name__ = "Unsigned32"
_FsL2VpnPwRedGroupWtrTimer_Object = MibTableColumn
fsL2VpnPwRedGroupWtrTimer = _FsL2VpnPwRedGroupWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 11),
    _FsL2VpnPwRedGroupWtrTimer_Type()
)
fsL2VpnPwRedGroupWtrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupWtrTimer.setStatus("current")


class _FsL2VpnPwRedGroupAdminCmd_Type(Integer32):
    """Custom type fsL2VpnPwRedGroupAdminCmd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockOutProtection", 1),
          ("clear", 2))
    )


_FsL2VpnPwRedGroupAdminCmd_Type.__name__ = "Integer32"
_FsL2VpnPwRedGroupAdminCmd_Object = MibTableColumn
fsL2VpnPwRedGroupAdminCmd = _FsL2VpnPwRedGroupAdminCmd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 12),
    _FsL2VpnPwRedGroupAdminCmd_Type()
)
fsL2VpnPwRedGroupAdminCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupAdminCmd.setStatus("current")
_FsL2VpnPwRedGroupAdminActivePw_Type = PwIndexOrZeroType
_FsL2VpnPwRedGroupAdminActivePw_Object = MibTableColumn
fsL2VpnPwRedGroupAdminActivePw = _FsL2VpnPwRedGroupAdminActivePw_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 13),
    _FsL2VpnPwRedGroupAdminActivePw_Type()
)
fsL2VpnPwRedGroupAdminActivePw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupAdminActivePw.setStatus("current")


class _FsL2VpnPwRedGroupAdminCmdStatus_Type(Integer32):
    """Custom type fsL2VpnPwRedGroupAdminCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 1),
          ("notApplicable", 2),
          ("rejected", 3))
    )


_FsL2VpnPwRedGroupAdminCmdStatus_Type.__name__ = "Integer32"
_FsL2VpnPwRedGroupAdminCmdStatus_Object = MibTableColumn
fsL2VpnPwRedGroupAdminCmdStatus = _FsL2VpnPwRedGroupAdminCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 14),
    _FsL2VpnPwRedGroupAdminCmdStatus_Type()
)
fsL2VpnPwRedGroupAdminCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupAdminCmdStatus.setStatus("current")
_FsL2VpnPwRedGroupRowStatus_Type = RowStatus
_FsL2VpnPwRedGroupRowStatus_Object = MibTableColumn
fsL2VpnPwRedGroupRowStatus = _FsL2VpnPwRedGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 1, 1, 15),
    _FsL2VpnPwRedGroupRowStatus_Type()
)
fsL2VpnPwRedGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsL2VpnPwRedGroupRowStatus.setStatus("current")
_FsL2VpnPwRedNodeTable_Object = MibTable
fsL2VpnPwRedNodeTable = _FsL2VpnPwRedNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 2)
)
if mibBuilder.loadTexts:
    fsL2VpnPwRedNodeTable.setStatus("current")
_FsL2VpnPwRedNodeEntry_Object = MibTableRow
fsL2VpnPwRedNodeEntry = _FsL2VpnPwRedNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 2, 1)
)
fsL2VpnPwRedNodeEntry.setIndexNames(
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedGroupIndex"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedNodeAddrType"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedNodeAddr"),
)
if mibBuilder.loadTexts:
    fsL2VpnPwRedNodeEntry.setStatus("current")
_FsL2VpnPwRedNodeAddrType_Type = InetAddressType
_FsL2VpnPwRedNodeAddrType_Object = MibTableColumn
fsL2VpnPwRedNodeAddrType = _FsL2VpnPwRedNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 2, 1, 1),
    _FsL2VpnPwRedNodeAddrType_Type()
)
fsL2VpnPwRedNodeAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedNodeAddrType.setStatus("current")


class _FsL2VpnPwRedNodeAddr_Type(InetAddress):
    """Custom type fsL2VpnPwRedNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_FsL2VpnPwRedNodeAddr_Type.__name__ = "InetAddress"
_FsL2VpnPwRedNodeAddr_Object = MibTableColumn
fsL2VpnPwRedNodeAddr = _FsL2VpnPwRedNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 2, 1, 2),
    _FsL2VpnPwRedNodeAddr_Type()
)
fsL2VpnPwRedNodeAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedNodeAddr.setStatus("current")
_FsL2VpnPwRedNodeLocalLdpID_Type = MplsLdpIdentifier
_FsL2VpnPwRedNodeLocalLdpID_Object = MibTableColumn
fsL2VpnPwRedNodeLocalLdpID = _FsL2VpnPwRedNodeLocalLdpID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 2, 1, 3),
    _FsL2VpnPwRedNodeLocalLdpID_Type()
)
fsL2VpnPwRedNodeLocalLdpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedNodeLocalLdpID.setStatus("current")
_FsL2VpnPwRedNodeLocalLdpEntityIndex_Type = Unsigned32
_FsL2VpnPwRedNodeLocalLdpEntityIndex_Object = MibTableColumn
fsL2VpnPwRedNodeLocalLdpEntityIndex = _FsL2VpnPwRedNodeLocalLdpEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 2, 1, 4),
    _FsL2VpnPwRedNodeLocalLdpEntityIndex_Type()
)
fsL2VpnPwRedNodeLocalLdpEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedNodeLocalLdpEntityIndex.setStatus("current")
_FsL2VpnPwRedNodePeerLdpID_Type = MplsLdpIdentifier
_FsL2VpnPwRedNodePeerLdpID_Object = MibTableColumn
fsL2VpnPwRedNodePeerLdpID = _FsL2VpnPwRedNodePeerLdpID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 2, 1, 5),
    _FsL2VpnPwRedNodePeerLdpID_Type()
)
fsL2VpnPwRedNodePeerLdpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedNodePeerLdpID.setStatus("current")


class _FsL2VpnPwRedNodeStatus_Type(Bits):
    """Custom type fsL2VpnPwRedNodeStatus based on Bits"""
    namedValues = NamedValues(
        *(("connected", 0),
          ("localSync", 1))
    )

_FsL2VpnPwRedNodeStatus_Type.__name__ = "Bits"
_FsL2VpnPwRedNodeStatus_Object = MibTableColumn
fsL2VpnPwRedNodeStatus = _FsL2VpnPwRedNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 2, 1, 6),
    _FsL2VpnPwRedNodeStatus_Type()
)
fsL2VpnPwRedNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedNodeStatus.setStatus("current")
_FsL2VpnPwRedNodeRowStatus_Type = RowStatus
_FsL2VpnPwRedNodeRowStatus_Object = MibTableColumn
fsL2VpnPwRedNodeRowStatus = _FsL2VpnPwRedNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 2, 1, 7),
    _FsL2VpnPwRedNodeRowStatus_Type()
)
fsL2VpnPwRedNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsL2VpnPwRedNodeRowStatus.setStatus("current")
_FsL2VpnPwRedPwTable_Object = MibTable
fsL2VpnPwRedPwTable = _FsL2VpnPwRedPwTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 3)
)
if mibBuilder.loadTexts:
    fsL2VpnPwRedPwTable.setStatus("current")
_FsL2VpnPwRedPwEntry_Object = MibTableRow
fsL2VpnPwRedPwEntry = _FsL2VpnPwRedPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 3, 1)
)
fsL2VpnPwRedPwEntry.setIndexNames(
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedGroupIndex"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedPwIndex"),
)
if mibBuilder.loadTexts:
    fsL2VpnPwRedPwEntry.setStatus("current")
_FsL2VpnPwRedPwIndex_Type = PwIndexOrZeroType
_FsL2VpnPwRedPwIndex_Object = MibTableColumn
fsL2VpnPwRedPwIndex = _FsL2VpnPwRedPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 3, 1, 1),
    _FsL2VpnPwRedPwIndex_Type()
)
fsL2VpnPwRedPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedPwIndex.setStatus("current")


class _FsL2VpnPwRedPwPreferance_Type(Integer32):
    """Custom type fsL2VpnPwRedPwPreferance based on Integer32"""
    defaultValue = 2

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


_FsL2VpnPwRedPwPreferance_Type.__name__ = "Integer32"
_FsL2VpnPwRedPwPreferance_Object = MibTableColumn
fsL2VpnPwRedPwPreferance = _FsL2VpnPwRedPwPreferance_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 3, 1, 2),
    _FsL2VpnPwRedPwPreferance_Type()
)
fsL2VpnPwRedPwPreferance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsL2VpnPwRedPwPreferance.setStatus("current")
_FsL2VpnPwRedPwLocalStatus_Type = FsL2VpnPwStatus
_FsL2VpnPwRedPwLocalStatus_Object = MibTableColumn
fsL2VpnPwRedPwLocalStatus = _FsL2VpnPwRedPwLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 3, 1, 3),
    _FsL2VpnPwRedPwLocalStatus_Type()
)
fsL2VpnPwRedPwLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedPwLocalStatus.setStatus("current")
_FsL2VpnPwRedPwRemoteStatus_Type = FsL2VpnPwStatus
_FsL2VpnPwRedPwRemoteStatus_Object = MibTableColumn
fsL2VpnPwRedPwRemoteStatus = _FsL2VpnPwRedPwRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 3, 1, 4),
    _FsL2VpnPwRedPwRemoteStatus_Type()
)
fsL2VpnPwRedPwRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedPwRemoteStatus.setStatus("current")
_FsL2VpnPwRedPwOperStatus_Type = PwOperStatusTC
_FsL2VpnPwRedPwOperStatus_Object = MibTableColumn
fsL2VpnPwRedPwOperStatus = _FsL2VpnPwRedPwOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 3, 1, 5),
    _FsL2VpnPwRedPwOperStatus_Type()
)
fsL2VpnPwRedPwOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedPwOperStatus.setStatus("current")
_FsL2VpnPwRedPwRowStatus_Type = RowStatus
_FsL2VpnPwRedPwRowStatus_Object = MibTableColumn
fsL2VpnPwRedPwRowStatus = _FsL2VpnPwRedPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 3, 1, 6),
    _FsL2VpnPwRedPwRowStatus_Type()
)
fsL2VpnPwRedPwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsL2VpnPwRedPwRowStatus.setStatus("current")
_FsL2VpnPwRedIccpPwTable_Object = MibTable
fsL2VpnPwRedIccpPwTable = _FsL2VpnPwRedIccpPwTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4)
)
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwTable.setStatus("current")
_FsL2VpnPwRedIccpPwEntry_Object = MibTableRow
fsL2VpnPwRedIccpPwEntry = _FsL2VpnPwRedIccpPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1)
)
fsL2VpnPwRedIccpPwEntry.setIndexNames(
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedIccpPwRgIndex"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedIccpPwHeadLsr"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedIccpPwFecType"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedIccpPwTailLsr"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedIccpPwGroup"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedIccpPwId"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedIccpPwAgiType"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedIccpPwAgi"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedIccpPwLocalAiiType"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedIccpPwLocalAii"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedIccpPwRemoteAiiType"),
    (0, "Aricent-L2VPN-MIB", "fsL2VpnPwRedIccpPwRemoteAii"),
)
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwEntry.setStatus("current")
_FsL2VpnPwRedIccpPwRgIndex_Type = Unsigned32
_FsL2VpnPwRedIccpPwRgIndex_Object = MibTableColumn
fsL2VpnPwRedIccpPwRgIndex = _FsL2VpnPwRedIccpPwRgIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 1),
    _FsL2VpnPwRedIccpPwRgIndex_Type()
)
fsL2VpnPwRedIccpPwRgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwRgIndex.setStatus("current")
_FsL2VpnPwRedIccpPwHeadLsr_Type = MplsLsrIdentifier
_FsL2VpnPwRedIccpPwHeadLsr_Object = MibTableColumn
fsL2VpnPwRedIccpPwHeadLsr = _FsL2VpnPwRedIccpPwHeadLsr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 2),
    _FsL2VpnPwRedIccpPwHeadLsr_Type()
)
fsL2VpnPwRedIccpPwHeadLsr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwHeadLsr.setStatus("current")


class _FsL2VpnPwRedIccpPwFecType_Type(Integer32):
    """Custom type fsL2VpnPwRedIccpPwFecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("pwIdFecSignaling", 2),
          ("genFecSignaling", 3))
    )


_FsL2VpnPwRedIccpPwFecType_Type.__name__ = "Integer32"
_FsL2VpnPwRedIccpPwFecType_Object = MibTableColumn
fsL2VpnPwRedIccpPwFecType = _FsL2VpnPwRedIccpPwFecType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 3),
    _FsL2VpnPwRedIccpPwFecType_Type()
)
fsL2VpnPwRedIccpPwFecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwFecType.setStatus("current")
_FsL2VpnPwRedIccpPwTailLsr_Type = MplsLsrIdentifier
_FsL2VpnPwRedIccpPwTailLsr_Object = MibTableColumn
fsL2VpnPwRedIccpPwTailLsr = _FsL2VpnPwRedIccpPwTailLsr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 4),
    _FsL2VpnPwRedIccpPwTailLsr_Type()
)
fsL2VpnPwRedIccpPwTailLsr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwTailLsr.setStatus("current")
_FsL2VpnPwRedIccpPwGroup_Type = PwGroupID
_FsL2VpnPwRedIccpPwGroup_Object = MibTableColumn
fsL2VpnPwRedIccpPwGroup = _FsL2VpnPwRedIccpPwGroup_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 5),
    _FsL2VpnPwRedIccpPwGroup_Type()
)
fsL2VpnPwRedIccpPwGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwGroup.setStatus("current")
_FsL2VpnPwRedIccpPwId_Type = PwIDType
_FsL2VpnPwRedIccpPwId_Object = MibTableColumn
fsL2VpnPwRedIccpPwId = _FsL2VpnPwRedIccpPwId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 6),
    _FsL2VpnPwRedIccpPwId_Type()
)
fsL2VpnPwRedIccpPwId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwId.setStatus("current")


class _FsL2VpnPwRedIccpPwAgiType_Type(Integer32):
    """Custom type fsL2VpnPwRedIccpPwAgiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("type1", 1)
    )


_FsL2VpnPwRedIccpPwAgiType_Type.__name__ = "Integer32"
_FsL2VpnPwRedIccpPwAgiType_Object = MibTableColumn
fsL2VpnPwRedIccpPwAgiType = _FsL2VpnPwRedIccpPwAgiType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 7),
    _FsL2VpnPwRedIccpPwAgiType_Type()
)
fsL2VpnPwRedIccpPwAgiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwAgiType.setStatus("current")


class _FsL2VpnPwRedIccpPwAgi_Type(OctetString):
    """Custom type fsL2VpnPwRedIccpPwAgi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsL2VpnPwRedIccpPwAgi_Type.__name__ = "OctetString"
_FsL2VpnPwRedIccpPwAgi_Object = MibTableColumn
fsL2VpnPwRedIccpPwAgi = _FsL2VpnPwRedIccpPwAgi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 8),
    _FsL2VpnPwRedIccpPwAgi_Type()
)
fsL2VpnPwRedIccpPwAgi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwAgi.setStatus("current")


class _FsL2VpnPwRedIccpPwLocalAiiType_Type(Integer32):
    """Custom type fsL2VpnPwRedIccpPwLocalAiiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_FsL2VpnPwRedIccpPwLocalAiiType_Type.__name__ = "Integer32"
_FsL2VpnPwRedIccpPwLocalAiiType_Object = MibTableColumn
fsL2VpnPwRedIccpPwLocalAiiType = _FsL2VpnPwRedIccpPwLocalAiiType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 9),
    _FsL2VpnPwRedIccpPwLocalAiiType_Type()
)
fsL2VpnPwRedIccpPwLocalAiiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwLocalAiiType.setStatus("current")


class _FsL2VpnPwRedIccpPwLocalAii_Type(OctetString):
    """Custom type fsL2VpnPwRedIccpPwLocalAii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 12),
    )


_FsL2VpnPwRedIccpPwLocalAii_Type.__name__ = "OctetString"
_FsL2VpnPwRedIccpPwLocalAii_Object = MibTableColumn
fsL2VpnPwRedIccpPwLocalAii = _FsL2VpnPwRedIccpPwLocalAii_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 10),
    _FsL2VpnPwRedIccpPwLocalAii_Type()
)
fsL2VpnPwRedIccpPwLocalAii.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwLocalAii.setStatus("current")


class _FsL2VpnPwRedIccpPwRemoteAiiType_Type(Integer32):
    """Custom type fsL2VpnPwRedIccpPwRemoteAiiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_FsL2VpnPwRedIccpPwRemoteAiiType_Type.__name__ = "Integer32"
_FsL2VpnPwRedIccpPwRemoteAiiType_Object = MibTableColumn
fsL2VpnPwRedIccpPwRemoteAiiType = _FsL2VpnPwRedIccpPwRemoteAiiType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 11),
    _FsL2VpnPwRedIccpPwRemoteAiiType_Type()
)
fsL2VpnPwRedIccpPwRemoteAiiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwRemoteAiiType.setStatus("current")


class _FsL2VpnPwRedIccpPwRemoteAii_Type(OctetString):
    """Custom type fsL2VpnPwRedIccpPwRemoteAii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 12),
    )


_FsL2VpnPwRedIccpPwRemoteAii_Type.__name__ = "OctetString"
_FsL2VpnPwRedIccpPwRemoteAii_Object = MibTableColumn
fsL2VpnPwRedIccpPwRemoteAii = _FsL2VpnPwRedIccpPwRemoteAii_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 12),
    _FsL2VpnPwRedIccpPwRemoteAii_Type()
)
fsL2VpnPwRedIccpPwRemoteAii.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwRemoteAii.setStatus("current")


class _FsL2VpnPwRedIccpPwRoId_Type(OctetString):
    """Custom type fsL2VpnPwRedIccpPwRoId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsL2VpnPwRedIccpPwRoId_Type.__name__ = "OctetString"
_FsL2VpnPwRedIccpPwRoId_Object = MibTableColumn
fsL2VpnPwRedIccpPwRoId = _FsL2VpnPwRedIccpPwRoId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 13),
    _FsL2VpnPwRedIccpPwRoId_Type()
)
fsL2VpnPwRedIccpPwRoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwRoId.setStatus("current")


class _FsL2VpnPwRedIccpPwPriority_Type(Unsigned32):
    """Custom type fsL2VpnPwRedIccpPwPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsL2VpnPwRedIccpPwPriority_Type.__name__ = "Unsigned32"
_FsL2VpnPwRedIccpPwPriority_Object = MibTableColumn
fsL2VpnPwRedIccpPwPriority = _FsL2VpnPwRedIccpPwPriority_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 14),
    _FsL2VpnPwRedIccpPwPriority_Type()
)
fsL2VpnPwRedIccpPwPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwPriority.setStatus("current")


class _FsL2VpnPwRedIccpPwStatus_Type(Bits):
    """Custom type fsL2VpnPwRedIccpPwStatus based on Bits"""
    namedValues = NamedValues(
        *(("localForward", 0),
          ("localStandby", 1),
          ("localSwitchover", 2),
          ("remoteSwitchover", 3),
          ("remoteAwaited", 4),
          ("nodeSwitchover", 6),
          ("localUpdated", 7))
    )

_FsL2VpnPwRedIccpPwStatus_Type.__name__ = "Bits"
_FsL2VpnPwRedIccpPwStatus_Object = MibTableColumn
fsL2VpnPwRedIccpPwStatus = _FsL2VpnPwRedIccpPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 4, 1, 15),
    _FsL2VpnPwRedIccpPwStatus_Type()
)
fsL2VpnPwRedIccpPwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2VpnPwRedIccpPwStatus.setStatus("current")
_FsL2VpnPwRedTestObjects_ObjectIdentity = ObjectIdentity
fsL2VpnPwRedTestObjects = _FsL2VpnPwRedTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 5)
)


class _FsL2VpnPwRedSimulateFailure_Type(Integer32):
    """Custom type fsL2VpnPwRedSimulateFailure based on Integer32"""
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
        *(("noRgIdTlv", 1),
          ("invalidRgIdTlvLen", 2),
          ("rqstNumZero", 3),
          ("cAndSBitClear", 4),
          ("noPwIdOrGenPwIdTlv", 5))
    )


_FsL2VpnPwRedSimulateFailure_Type.__name__ = "Integer32"
_FsL2VpnPwRedSimulateFailure_Object = MibScalar
fsL2VpnPwRedSimulateFailure = _FsL2VpnPwRedSimulateFailure_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 5, 1),
    _FsL2VpnPwRedSimulateFailure_Type()
)
fsL2VpnPwRedSimulateFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsL2VpnPwRedSimulateFailure.setStatus("current")
_FsL2VpnPwRedSimulateFailureForNbr_Type = IpAddress
_FsL2VpnPwRedSimulateFailureForNbr_Object = MibScalar
fsL2VpnPwRedSimulateFailureForNbr = _FsL2VpnPwRedSimulateFailureForNbr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 5, 2),
    _FsL2VpnPwRedSimulateFailureForNbr_Type()
)
fsL2VpnPwRedSimulateFailureForNbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsL2VpnPwRedSimulateFailureForNbr.setStatus("current")

# Managed Objects groups

vplsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 2, 2, 1)
)
vplsGroup.setObjects(
      *(("Aricent-L2VPN-MIB", "vplsConfigName"),
        ("Aricent-L2VPN-MIB", "vplsConfigDescr"),
        ("Aricent-L2VPN-MIB", "vplsConfigAdminStatus"),
        ("Aricent-L2VPN-MIB", "vplsConfigMacLearning"),
        ("Aricent-L2VPN-MIB", "vplsConfigDiscardUnknownDest"),
        ("Aricent-L2VPN-MIB", "vplsConfigMacAging"),
        ("Aricent-L2VPN-MIB", "vplsConfigVpnId"),
        ("Aricent-L2VPN-MIB", "vplsConfigFwdFullHighWatermark"),
        ("Aricent-L2VPN-MIB", "vplsConfigFwdFullLowWatermark"),
        ("Aricent-L2VPN-MIB", "vplsConfigRowStatus"),
        ("Aricent-L2VPN-MIB", "vplsConfigIndexNext"),
        ("Aricent-L2VPN-MIB", "vplsConfigMtu"),
        ("Aricent-L2VPN-MIB", "vplsConfigStorageType"),
        ("Aricent-L2VPN-MIB", "vplsConfigSignalingType"),
        ("Aricent-L2VPN-MIB", "vplsStatusOperStatus"),
        ("Aricent-L2VPN-MIB", "vplsStatusPeerCount"),
        ("Aricent-L2VPN-MIB", "vplsStatusNotifEnable"),
        ("Aricent-L2VPN-MIB", "vplsNotificationMaxRate"))
)
if mibBuilder.loadTexts:
    vplsGroup.setStatus("current")

vplsPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 2, 2, 2)
)
vplsPwBindGroup.setObjects(
      *(("Aricent-L2VPN-MIB", "vplsPwBindConfigType"),
        ("Aricent-L2VPN-MIB", "vplsPwBindType"),
        ("Aricent-L2VPN-MIB", "vplsPwBindRowStatus"),
        ("Aricent-L2VPN-MIB", "vplsPwBindStorageType"))
)
if mibBuilder.loadTexts:
    vplsPwBindGroup.setStatus("current")


# Notification objects

vplsStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 0, 1)
)
vplsStatusChanged.setObjects(
      *(("Aricent-L2VPN-MIB", "vplsConfigVpnId"),
        ("Aricent-L2VPN-MIB", "vplsConfigAdminStatus"),
        ("Aricent-L2VPN-MIB", "vplsStatusOperStatus"))
)
if mibBuilder.loadTexts:
    vplsStatusChanged.setStatus(
        "current"
    )

vplsFwdFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 0, 2)
)
vplsFwdFullAlarmRaised.setObjects(
      *(("Aricent-L2VPN-MIB", "vplsConfigVpnId"),
        ("Aricent-L2VPN-MIB", "vplsConfigFwdFullHighWatermark"),
        ("Aricent-L2VPN-MIB", "vplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    vplsFwdFullAlarmRaised.setStatus(
        "current"
    )

vplsFwdFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 0, 3)
)
vplsFwdFullAlarmCleared.setObjects(
      *(("Aricent-L2VPN-MIB", "vplsConfigVpnId"),
        ("Aricent-L2VPN-MIB", "vplsConfigFwdFullHighWatermark"),
        ("Aricent-L2VPN-MIB", "vplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    vplsFwdFullAlarmCleared.setStatus(
        "current"
    )

fsL2VpnPwRedSyncFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 0, 1)
)
fsL2VpnPwRedSyncFail.setObjects(
      *(("Aricent-L2VPN-MIB", "fsL2VpnPwRedGroupAdminActivePw"),
        ("Aricent-L2VPN-MIB", "fsL2VpnPwRedGroupOperActivePw"))
)
if mibBuilder.loadTexts:
    fsL2VpnPwRedSyncFail.setStatus(
        "current"
    )

fsL2VpnPwRedPwStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 4, 0, 2)
)
fsL2VpnPwRedPwStatus.setObjects(
      *(("Aricent-L2VPN-MIB", "fsL2VpnPwRedPwLocalStatus"),
        ("Aricent-L2VPN-MIB", "fsL2VpnPwRedPwRemoteStatus"))
)
if mibBuilder.loadTexts:
    fsL2VpnPwRedPwStatus.setStatus(
        "current"
    )


# Notifications groups

vplsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 2, 2, 3)
)
vplsNotificationGroup.setObjects(
      *(("Aricent-L2VPN-MIB", "vplsStatusChanged"),
        ("Aricent-L2VPN-MIB", "vplsFwdFullAlarmRaised"),
        ("Aricent-L2VPN-MIB", "vplsFwdFullAlarmCleared"))
)
if mibBuilder.loadTexts:
    vplsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vplsModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 2, 1, 1)
)
vplsModuleFullCompliance.setObjects(
      *(("Aricent-L2VPN-MIB", "vplsGroup"),
        ("Aricent-L2VPN-MIB", "vplsPwBindGroup"),
        ("Aricent-L2VPN-MIB", "vplsNotificationGroup"))
)
if mibBuilder.loadTexts:
    vplsModuleFullCompliance.setStatus(
        "current"
    )

vplsModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 29601, 2, 72, 2, 1, 2)
)
vplsModuleReadOnlyCompliance.setObjects(
      *(("Aricent-L2VPN-MIB", "vplsGroup"),
        ("Aricent-L2VPN-MIB", "vplsPwBindGroup"),
        ("Aricent-L2VPN-MIB", "vplsNotificationGroup"))
)
if mibBuilder.loadTexts:
    vplsModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Aricent-L2VPN-MIB",
    **{"VplsBgpRouteDistinguisher": VplsBgpRouteDistinguisher,
       "VplsBgpRouteTarget": VplsBgpRouteTarget,
       "VplsBgpRouteTargetType": VplsBgpRouteTargetType,
       "VPNIdOrZero": VPNIdOrZero,
       "FsL2VpnPwStatus": FsL2VpnPwStatus,
       "fsL2VpnMIB": fsL2VpnMIB,
       "vplsNotifications": vplsNotifications,
       "vplsStatusChanged": vplsStatusChanged,
       "vplsFwdFullAlarmRaised": vplsFwdFullAlarmRaised,
       "vplsFwdFullAlarmCleared": vplsFwdFullAlarmCleared,
       "vplsObjects": vplsObjects,
       "vplsConfigIndexNext": vplsConfigIndexNext,
       "vplsConfigTable": vplsConfigTable,
       "vplsConfigEntry": vplsConfigEntry,
       "vplsConfigIndex": vplsConfigIndex,
       "vplsConfigName": vplsConfigName,
       "vplsConfigDescr": vplsConfigDescr,
       "vplsConfigAdminStatus": vplsConfigAdminStatus,
       "vplsConfigMacLearning": vplsConfigMacLearning,
       "vplsConfigDiscardUnknownDest": vplsConfigDiscardUnknownDest,
       "vplsConfigMacAging": vplsConfigMacAging,
       "vplsConfigFwdFullHighWatermark": vplsConfigFwdFullHighWatermark,
       "vplsConfigFwdFullLowWatermark": vplsConfigFwdFullLowWatermark,
       "vplsConfigRowStatus": vplsConfigRowStatus,
       "vplsConfigMtu": vplsConfigMtu,
       "vplsConfigVpnId": vplsConfigVpnId,
       "vplsConfigStorageType": vplsConfigStorageType,
       "vplsConfigSignalingType": vplsConfigSignalingType,
       "vplsStatusTable": vplsStatusTable,
       "vplsStatusEntry": vplsStatusEntry,
       "vplsStatusOperStatus": vplsStatusOperStatus,
       "vplsStatusPeerCount": vplsStatusPeerCount,
       "vplsPwBindTable": vplsPwBindTable,
       "vplsPwBindEntry": vplsPwBindEntry,
       "vplsPwBindConfigType": vplsPwBindConfigType,
       "vplsPwBindType": vplsPwBindType,
       "vplsPwBindRowStatus": vplsPwBindRowStatus,
       "vplsPwBindStorageType": vplsPwBindStorageType,
       "vplsBgpADConfigTable": vplsBgpADConfigTable,
       "vplsBgpADConfigEntry": vplsBgpADConfigEntry,
       "vplsBgpADConfigRouteDistinguisher": vplsBgpADConfigRouteDistinguisher,
       "vplsBgpADConfigPrefix": vplsBgpADConfigPrefix,
       "vplsBgpADConfigVplsId": vplsBgpADConfigVplsId,
       "vplsBgpADConfigRowStatus": vplsBgpADConfigRowStatus,
       "vplsBgpADConfigStorageType": vplsBgpADConfigStorageType,
       "vplsBgpRteTargetTable": vplsBgpRteTargetTable,
       "vplsBgpRteTargetEntry": vplsBgpRteTargetEntry,
       "vplsBgpRteTargetIndex": vplsBgpRteTargetIndex,
       "vplsBgpRteTargetRTType": vplsBgpRteTargetRTType,
       "vplsBgpRteTargetRT": vplsBgpRteTargetRT,
       "vplsBgpRteTargetRTRowStatus": vplsBgpRteTargetRTRowStatus,
       "vplsBgpRteTargetStorageType": vplsBgpRteTargetStorageType,
       "vplsStatusNotifEnable": vplsStatusNotifEnable,
       "vplsNotificationMaxRate": vplsNotificationMaxRate,
       "vplsConformance": vplsConformance,
       "vplsCompliances": vplsCompliances,
       "vplsModuleFullCompliance": vplsModuleFullCompliance,
       "vplsModuleReadOnlyCompliance": vplsModuleReadOnlyCompliance,
       "vplsGroups": vplsGroups,
       "vplsGroup": vplsGroup,
       "vplsPwBindGroup": vplsPwBindGroup,
       "vplsNotificationGroup": vplsNotificationGroup,
       "pwRedundancyScalar": pwRedundancyScalar,
       "fsL2VpnPwRedundancyStatus": fsL2VpnPwRedundancyStatus,
       "fsL2VpnPwRedNegotiationTimeOut": fsL2VpnPwRedNegotiationTimeOut,
       "fsL2VpnPwRedundancySyncFailNotifyEnable": fsL2VpnPwRedundancySyncFailNotifyEnable,
       "fsL2VpnPwRedundancyPwStatusNotifyEnable": fsL2VpnPwRedundancyPwStatusNotifyEnable,
       "pwRedundancyObjects": pwRedundancyObjects,
       "fsL2VpnPwRedTraps": fsL2VpnPwRedTraps,
       "fsL2VpnPwRedSyncFail": fsL2VpnPwRedSyncFail,
       "fsL2VpnPwRedPwStatus": fsL2VpnPwRedPwStatus,
       "fsL2VpnPwRedGroupTable": fsL2VpnPwRedGroupTable,
       "fsL2VpnPwRedGroupEntry": fsL2VpnPwRedGroupEntry,
       "fsL2VpnPwRedGroupIndex": fsL2VpnPwRedGroupIndex,
       "fsL2VpnPwRedGroupProtType": fsL2VpnPwRedGroupProtType,
       "fsL2VpnPwRedGroupReversionType": fsL2VpnPwRedGroupReversionType,
       "fsL2VpnPwRedGroupContentionResolutionMethod": fsL2VpnPwRedGroupContentionResolutionMethod,
       "fsL2VpnPwRedGroupLockoutProtection": fsL2VpnPwRedGroupLockoutProtection,
       "fsL2VpnPwRedGroupMasterSlaveMode": fsL2VpnPwRedGroupMasterSlaveMode,
       "fsL2VpnPwRedGroupDualHomeApps": fsL2VpnPwRedGroupDualHomeApps,
       "fsL2VpnPwRedGroupName": fsL2VpnPwRedGroupName,
       "fsL2VpnPwRedGroupStatus": fsL2VpnPwRedGroupStatus,
       "fsL2VpnPwRedGroupOperActivePw": fsL2VpnPwRedGroupOperActivePw,
       "fsL2VpnPwRedGroupWtrTimer": fsL2VpnPwRedGroupWtrTimer,
       "fsL2VpnPwRedGroupAdminCmd": fsL2VpnPwRedGroupAdminCmd,
       "fsL2VpnPwRedGroupAdminActivePw": fsL2VpnPwRedGroupAdminActivePw,
       "fsL2VpnPwRedGroupAdminCmdStatus": fsL2VpnPwRedGroupAdminCmdStatus,
       "fsL2VpnPwRedGroupRowStatus": fsL2VpnPwRedGroupRowStatus,
       "fsL2VpnPwRedNodeTable": fsL2VpnPwRedNodeTable,
       "fsL2VpnPwRedNodeEntry": fsL2VpnPwRedNodeEntry,
       "fsL2VpnPwRedNodeAddrType": fsL2VpnPwRedNodeAddrType,
       "fsL2VpnPwRedNodeAddr": fsL2VpnPwRedNodeAddr,
       "fsL2VpnPwRedNodeLocalLdpID": fsL2VpnPwRedNodeLocalLdpID,
       "fsL2VpnPwRedNodeLocalLdpEntityIndex": fsL2VpnPwRedNodeLocalLdpEntityIndex,
       "fsL2VpnPwRedNodePeerLdpID": fsL2VpnPwRedNodePeerLdpID,
       "fsL2VpnPwRedNodeStatus": fsL2VpnPwRedNodeStatus,
       "fsL2VpnPwRedNodeRowStatus": fsL2VpnPwRedNodeRowStatus,
       "fsL2VpnPwRedPwTable": fsL2VpnPwRedPwTable,
       "fsL2VpnPwRedPwEntry": fsL2VpnPwRedPwEntry,
       "fsL2VpnPwRedPwIndex": fsL2VpnPwRedPwIndex,
       "fsL2VpnPwRedPwPreferance": fsL2VpnPwRedPwPreferance,
       "fsL2VpnPwRedPwLocalStatus": fsL2VpnPwRedPwLocalStatus,
       "fsL2VpnPwRedPwRemoteStatus": fsL2VpnPwRedPwRemoteStatus,
       "fsL2VpnPwRedPwOperStatus": fsL2VpnPwRedPwOperStatus,
       "fsL2VpnPwRedPwRowStatus": fsL2VpnPwRedPwRowStatus,
       "fsL2VpnPwRedIccpPwTable": fsL2VpnPwRedIccpPwTable,
       "fsL2VpnPwRedIccpPwEntry": fsL2VpnPwRedIccpPwEntry,
       "fsL2VpnPwRedIccpPwRgIndex": fsL2VpnPwRedIccpPwRgIndex,
       "fsL2VpnPwRedIccpPwHeadLsr": fsL2VpnPwRedIccpPwHeadLsr,
       "fsL2VpnPwRedIccpPwFecType": fsL2VpnPwRedIccpPwFecType,
       "fsL2VpnPwRedIccpPwTailLsr": fsL2VpnPwRedIccpPwTailLsr,
       "fsL2VpnPwRedIccpPwGroup": fsL2VpnPwRedIccpPwGroup,
       "fsL2VpnPwRedIccpPwId": fsL2VpnPwRedIccpPwId,
       "fsL2VpnPwRedIccpPwAgiType": fsL2VpnPwRedIccpPwAgiType,
       "fsL2VpnPwRedIccpPwAgi": fsL2VpnPwRedIccpPwAgi,
       "fsL2VpnPwRedIccpPwLocalAiiType": fsL2VpnPwRedIccpPwLocalAiiType,
       "fsL2VpnPwRedIccpPwLocalAii": fsL2VpnPwRedIccpPwLocalAii,
       "fsL2VpnPwRedIccpPwRemoteAiiType": fsL2VpnPwRedIccpPwRemoteAiiType,
       "fsL2VpnPwRedIccpPwRemoteAii": fsL2VpnPwRedIccpPwRemoteAii,
       "fsL2VpnPwRedIccpPwRoId": fsL2VpnPwRedIccpPwRoId,
       "fsL2VpnPwRedIccpPwPriority": fsL2VpnPwRedIccpPwPriority,
       "fsL2VpnPwRedIccpPwStatus": fsL2VpnPwRedIccpPwStatus,
       "fsL2VpnPwRedTestObjects": fsL2VpnPwRedTestObjects,
       "fsL2VpnPwRedSimulateFailure": fsL2VpnPwRedSimulateFailure,
       "fsL2VpnPwRedSimulateFailureForNbr": fsL2VpnPwRedSimulateFailureForNbr}
)
