# SNMP MIB module (DC-VPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/DC-VPLS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:46 2025
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

(BgpExtendedCommunity,
 BgpRouteDistinguisher,
 L2vpnADType,
 L2vpnPwBindType,
 L2vpnSigType,
 L2vpnVeIdOrZero,
 l2vmEntityIndex) = mibBuilder.importSymbols(
    "DC-L2VPN-MIB",
    "BgpExtendedCommunity",
    "BgpRouteDistinguisher",
    "L2vpnADType",
    "L2vpnPwBindType",
    "L2vpnSigType",
    "L2vpnVeIdOrZero",
    "l2vmEntityIndex")

(AdminStatus,
 NpgOperStatus,
 NumericIndex,
 NumericIndexOrZero) = mibBuilder.importSymbols(
    "DC-MASTER-TC",
    "AdminStatus",
    "NpgOperStatus",
    "NumericIndex",
    "NumericIndexOrZero")

(IANAPwTypeTC,) = mibBuilder.importSymbols(
    "IANA-PWE3-MIB",
    "IANAPwTypeTC")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

vplsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VplsAcStatus(TextualConvention, Integer32):
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
          ("active", 1),
          ("standby", 2))
    )



class VplsMCFloodMode(TextualConvention, Integer32):
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
        *(("all", 1),
          ("unknown", 2),
          ("none", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_Opx_ObjectIdentity = ObjectIdentity
opx = _Opx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10)
)
_VplsNotifications_ObjectIdentity = ObjectIdentity
vplsNotifications = _VplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 0)
)
_VplsObjects_ObjectIdentity = ObjectIdentity
vplsObjects = _VplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1)
)
_VplsConfigTable_Object = MibTable
vplsConfigTable = _VplsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1)
)
if mibBuilder.loadTexts:
    vplsConfigTable.setStatus("current")
_VplsConfigEntry_Object = MibTableRow
vplsConfigEntry = _VplsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1)
)
vplsConfigEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "DC-VPLS-MIB", "vplsIndex"),
)
if mibBuilder.loadTexts:
    vplsConfigEntry.setStatus("current")
_VplsIndex_Type = NumericIndex
_VplsIndex_Object = MibTableColumn
vplsIndex = _VplsIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 2),
    _VplsIndex_Type()
)
vplsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vplsIndex.setStatus("current")
_VplsConfigRowStatus_Type = RowStatus
_VplsConfigRowStatus_Object = MibTableColumn
vplsConfigRowStatus = _VplsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 3),
    _VplsConfigRowStatus_Type()
)
vplsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigRowStatus.setStatus("current")


class _VplsConfigAdminStatus_Type(AdminStatus):
    """Custom type vplsConfigAdminStatus based on AdminStatus"""
    defaultValue = 1


_VplsConfigAdminStatus_Type.__name__ = "AdminStatus"
_VplsConfigAdminStatus_Object = MibTableColumn
vplsConfigAdminStatus = _VplsConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 4),
    _VplsConfigAdminStatus_Type()
)
vplsConfigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigAdminStatus.setStatus("current")
_VplsConfigOperStatus_Type = NpgOperStatus
_VplsConfigOperStatus_Object = MibTableColumn
vplsConfigOperStatus = _VplsConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 5),
    _VplsConfigOperStatus_Type()
)
vplsConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsConfigOperStatus.setStatus("current")
_VplsConfigName_Type = SnmpAdminString
_VplsConfigName_Object = MibTableColumn
vplsConfigName = _VplsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 6),
    _VplsConfigName_Type()
)
vplsConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigName.setStatus("current")
_VplsConfigDescr_Type = SnmpAdminString
_VplsConfigDescr_Object = MibTableColumn
vplsConfigDescr = _VplsConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 7),
    _VplsConfigDescr_Type()
)
vplsConfigDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigDescr.setStatus("current")


class _VplsConfigADType_Type(L2vpnADType):
    """Custom type vplsConfigADType based on L2vpnADType"""
    defaultValue = 1


_VplsConfigADType_Type.__name__ = "L2vpnADType"
_VplsConfigADType_Object = MibTableColumn
vplsConfigADType = _VplsConfigADType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 8),
    _VplsConfigADType_Type()
)
vplsConfigADType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigADType.setStatus("current")


class _VplsConfigSigType_Type(L2vpnSigType):
    """Custom type vplsConfigSigType based on L2vpnSigType"""
    defaultValue = 1


_VplsConfigSigType_Type.__name__ = "L2vpnSigType"
_VplsConfigSigType_Object = MibTableColumn
vplsConfigSigType = _VplsConfigSigType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 9),
    _VplsConfigSigType_Type()
)
vplsConfigSigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigSigType.setStatus("current")


class _VplsConfigPwEncapType_Type(IANAPwTypeTC):
    """Custom type vplsConfigPwEncapType based on IANAPwTypeTC"""
    defaultValue = 5


_VplsConfigPwEncapType_Type.__name__ = "IANAPwTypeTC"
_VplsConfigPwEncapType_Object = MibTableColumn
vplsConfigPwEncapType = _VplsConfigPwEncapType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 10),
    _VplsConfigPwEncapType_Type()
)
vplsConfigPwEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigPwEncapType.setStatus("current")


class _VplsConfigMacLearning_Type(TruthValue):
    """Custom type vplsConfigMacLearning based on TruthValue"""
    defaultValue = 1


_VplsConfigMacLearning_Type.__name__ = "TruthValue"
_VplsConfigMacLearning_Object = MibTableColumn
vplsConfigMacLearning = _VplsConfigMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 12),
    _VplsConfigDiscardUnknownDest_Type()
)
vplsConfigDiscardUnknownDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigDiscardUnknownDest.setStatus("current")


class _VplsConfigMacAge_Type(Unsigned32):
    """Custom type vplsConfigMacAge based on Unsigned32"""
    defaultValue = 0


_VplsConfigMacAge_Type.__name__ = "Unsigned32"
_VplsConfigMacAge_Object = MibTableColumn
vplsConfigMacAge = _VplsConfigMacAge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 13),
    _VplsConfigMacAge_Type()
)
vplsConfigMacAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMacAge.setStatus("current")
if mibBuilder.loadTexts:
    vplsConfigMacAge.setUnits("seconds")


class _VplsConfigMtu_Type(Unsigned32):
    """Custom type vplsConfigMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9192),
    )


_VplsConfigMtu_Type.__name__ = "Unsigned32"
_VplsConfigMtu_Object = MibTableColumn
vplsConfigMtu = _VplsConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 14),
    _VplsConfigMtu_Type()
)
vplsConfigMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMtu.setStatus("current")
if mibBuilder.loadTexts:
    vplsConfigMtu.setUnits("bytes")


class _VplsConfigMacSize_Type(Unsigned32):
    """Custom type vplsConfigMacSize based on Unsigned32"""
    defaultValue = 0


_VplsConfigMacSize_Type.__name__ = "Unsigned32"
_VplsConfigMacSize_Object = MibTableColumn
vplsConfigMacSize = _VplsConfigMacSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 15),
    _VplsConfigMacSize_Type()
)
vplsConfigMacSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMacSize.setStatus("current")


class _VplsConfigPwMacAddressLimit_Type(Unsigned32):
    """Custom type vplsConfigPwMacAddressLimit based on Unsigned32"""
    defaultValue = 0


_VplsConfigPwMacAddressLimit_Type.__name__ = "Unsigned32"
_VplsConfigPwMacAddressLimit_Object = MibTableColumn
vplsConfigPwMacAddressLimit = _VplsConfigPwMacAddressLimit_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 16),
    _VplsConfigPwMacAddressLimit_Type()
)
vplsConfigPwMacAddressLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigPwMacAddressLimit.setStatus("current")


class _VplsConfigControlWord_Type(TruthValue):
    """Custom type vplsConfigControlWord based on TruthValue"""
    defaultValue = 2


_VplsConfigControlWord_Type.__name__ = "TruthValue"
_VplsConfigControlWord_Object = MibTableColumn
vplsConfigControlWord = _VplsConfigControlWord_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 17),
    _VplsConfigControlWord_Type()
)
vplsConfigControlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigControlWord.setStatus("current")


class _VplsConfigSeqDelivery_Type(TruthValue):
    """Custom type vplsConfigSeqDelivery based on TruthValue"""
    defaultValue = 2


_VplsConfigSeqDelivery_Type.__name__ = "TruthValue"
_VplsConfigSeqDelivery_Object = MibTableColumn
vplsConfigSeqDelivery = _VplsConfigSeqDelivery_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 18),
    _VplsConfigSeqDelivery_Type()
)
vplsConfigSeqDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigSeqDelivery.setStatus("current")


class _VplsConfigRouteDistinguisher_Type(BgpRouteDistinguisher):
    """Custom type vplsConfigRouteDistinguisher based on BgpRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_VplsConfigRouteDistinguisher_Type.__name__ = "BgpRouteDistinguisher"
_VplsConfigRouteDistinguisher_Object = MibTableColumn
vplsConfigRouteDistinguisher = _VplsConfigRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 19),
    _VplsConfigRouteDistinguisher_Type()
)
vplsConfigRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigRouteDistinguisher.setStatus("current")


class _VplsConfigVpnId_Type(BgpExtendedCommunity):
    """Custom type vplsConfigVpnId based on BgpExtendedCommunity"""
    defaultHexValue = "0000000000000000"


_VplsConfigVpnId_Type.__name__ = "BgpExtendedCommunity"
_VplsConfigVpnId_Object = MibTableColumn
vplsConfigVpnId = _VplsConfigVpnId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 20),
    _VplsConfigVpnId_Type()
)
vplsConfigVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigVpnId.setStatus("current")


class _VplsConfigLocalVeID_Type(L2vpnVeIdOrZero):
    """Custom type vplsConfigLocalVeID based on L2vpnVeIdOrZero"""
    defaultValue = 0


_VplsConfigLocalVeID_Type.__name__ = "L2vpnVeIdOrZero"
_VplsConfigLocalVeID_Object = MibTableColumn
vplsConfigLocalVeID = _VplsConfigLocalVeID_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 21),
    _VplsConfigLocalVeID_Type()
)
vplsConfigLocalVeID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigLocalVeID.setStatus("current")


class _VplsConfigLocalPreference_Type(Unsigned32):
    """Custom type vplsConfigLocalPreference based on Unsigned32"""
    defaultValue = 100


_VplsConfigLocalPreference_Type.__name__ = "Unsigned32"
_VplsConfigLocalPreference_Object = MibTableColumn
vplsConfigLocalPreference = _VplsConfigLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 22),
    _VplsConfigLocalPreference_Type()
)
vplsConfigLocalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigLocalPreference.setStatus("current")


class _VplsConfigLabelBlockSize_Type(Unsigned32):
    """Custom type vplsConfigLabelBlockSize based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
    )


_VplsConfigLabelBlockSize_Type.__name__ = "Unsigned32"
_VplsConfigLabelBlockSize_Object = MibTableColumn
vplsConfigLabelBlockSize = _VplsConfigLabelBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 23),
    _VplsConfigLabelBlockSize_Type()
)
vplsConfigLabelBlockSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigLabelBlockSize.setStatus("current")


class _VplsConfigADPwMacLearning_Type(TruthValue):
    """Custom type vplsConfigADPwMacLearning based on TruthValue"""
    defaultValue = 1


_VplsConfigADPwMacLearning_Type.__name__ = "TruthValue"
_VplsConfigADPwMacLearning_Object = MibTableColumn
vplsConfigADPwMacLearning = _VplsConfigADPwMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 24),
    _VplsConfigADPwMacLearning_Type()
)
vplsConfigADPwMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigADPwMacLearning.setStatus("current")


class _VplsConfigMultiCastFloodMode_Type(VplsMCFloodMode):
    """Custom type vplsConfigMultiCastFloodMode based on VplsMCFloodMode"""
    defaultValue = 1


_VplsConfigMultiCastFloodMode_Type.__name__ = "VplsMCFloodMode"
_VplsConfigMultiCastFloodMode_Object = MibTableColumn
vplsConfigMultiCastFloodMode = _VplsConfigMultiCastFloodMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 25),
    _VplsConfigMultiCastFloodMode_Type()
)
vplsConfigMultiCastFloodMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMultiCastFloodMode.setStatus("current")


class _VplsConfigIgnoreMtuMismatch_Type(TruthValue):
    """Custom type vplsConfigIgnoreMtuMismatch based on TruthValue"""
    defaultValue = 2


_VplsConfigIgnoreMtuMismatch_Type.__name__ = "TruthValue"
_VplsConfigIgnoreMtuMismatch_Object = MibTableColumn
vplsConfigIgnoreMtuMismatch = _VplsConfigIgnoreMtuMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 26),
    _VplsConfigIgnoreMtuMismatch_Type()
)
vplsConfigIgnoreMtuMismatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigIgnoreMtuMismatch.setStatus("current")


class _VplsConfigIgnoreEncapsMismatch_Type(TruthValue):
    """Custom type vplsConfigIgnoreEncapsMismatch based on TruthValue"""
    defaultValue = 2


_VplsConfigIgnoreEncapsMismatch_Type.__name__ = "TruthValue"
_VplsConfigIgnoreEncapsMismatch_Object = MibTableColumn
vplsConfigIgnoreEncapsMismatch = _VplsConfigIgnoreEncapsMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 1, 1, 27),
    _VplsConfigIgnoreEncapsMismatch_Type()
)
vplsConfigIgnoreEncapsMismatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigIgnoreEncapsMismatch.setStatus("current")
_VplsStatusTable_Object = MibTable
vplsStatusTable = _VplsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2)
)
if mibBuilder.loadTexts:
    vplsStatusTable.setStatus("current")
_VplsStatusEntry_Object = MibTableRow
vplsStatusEntry = _VplsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1)
)
vplsStatusEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "DC-VPLS-MIB", "vplsIndex"),
)
if mibBuilder.loadTexts:
    vplsStatusEntry.setStatus("current")
_VplsStatusOperStatus_Type = NpgOperStatus
_VplsStatusOperStatus_Object = MibTableColumn
vplsStatusOperStatus = _VplsStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1, 3),
    _VplsStatusOperStatus_Type()
)
vplsStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusOperStatus.setStatus("current")
_VplsStatusPwSetDownGauge_Type = Gauge32
_VplsStatusPwSetDownGauge_Object = MibTableColumn
vplsStatusPwSetDownGauge = _VplsStatusPwSetDownGauge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1, 4),
    _VplsStatusPwSetDownGauge_Type()
)
vplsStatusPwSetDownGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusPwSetDownGauge.setStatus("current")
_VplsStatusPwSetGoingUpGauge_Type = Gauge32
_VplsStatusPwSetGoingUpGauge_Object = MibTableColumn
vplsStatusPwSetGoingUpGauge = _VplsStatusPwSetGoingUpGauge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1, 5),
    _VplsStatusPwSetGoingUpGauge_Type()
)
vplsStatusPwSetGoingUpGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusPwSetGoingUpGauge.setStatus("current")
_VplsStatusPwSetUpGauge_Type = Gauge32
_VplsStatusPwSetUpGauge_Object = MibTableColumn
vplsStatusPwSetUpGauge = _VplsStatusPwSetUpGauge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1, 6),
    _VplsStatusPwSetUpGauge_Type()
)
vplsStatusPwSetUpGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusPwSetUpGauge.setStatus("current")
_VplsStatusPwSetFailGauge_Type = Gauge32
_VplsStatusPwSetFailGauge_Object = MibTableColumn
vplsStatusPwSetFailGauge = _VplsStatusPwSetFailGauge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1, 7),
    _VplsStatusPwSetFailGauge_Type()
)
vplsStatusPwSetFailGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusPwSetFailGauge.setStatus("current")
_VplsStatusPwSetFailPermGauge_Type = Gauge32
_VplsStatusPwSetFailPermGauge_Object = MibTableColumn
vplsStatusPwSetFailPermGauge = _VplsStatusPwSetFailPermGauge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1, 8),
    _VplsStatusPwSetFailPermGauge_Type()
)
vplsStatusPwSetFailPermGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusPwSetFailPermGauge.setStatus("current")
_VplsStatusAcDownGauge_Type = Gauge32
_VplsStatusAcDownGauge_Object = MibTableColumn
vplsStatusAcDownGauge = _VplsStatusAcDownGauge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1, 9),
    _VplsStatusAcDownGauge_Type()
)
vplsStatusAcDownGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusAcDownGauge.setStatus("current")
_VplsStatusAcGoingUpGauge_Type = Gauge32
_VplsStatusAcGoingUpGauge_Object = MibTableColumn
vplsStatusAcGoingUpGauge = _VplsStatusAcGoingUpGauge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1, 10),
    _VplsStatusAcGoingUpGauge_Type()
)
vplsStatusAcGoingUpGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusAcGoingUpGauge.setStatus("current")
_VplsStatusAcUpGauge_Type = Gauge32
_VplsStatusAcUpGauge_Object = MibTableColumn
vplsStatusAcUpGauge = _VplsStatusAcUpGauge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1, 11),
    _VplsStatusAcUpGauge_Type()
)
vplsStatusAcUpGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusAcUpGauge.setStatus("current")
_VplsStatusAcFailGauge_Type = Gauge32
_VplsStatusAcFailGauge_Object = MibTableColumn
vplsStatusAcFailGauge = _VplsStatusAcFailGauge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1, 12),
    _VplsStatusAcFailGauge_Type()
)
vplsStatusAcFailGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusAcFailGauge.setStatus("current")
_VplsStatusAcFailPermGauge_Type = Gauge32
_VplsStatusAcFailPermGauge_Object = MibTableColumn
vplsStatusAcFailPermGauge = _VplsStatusAcFailPermGauge_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1, 13),
    _VplsStatusAcFailPermGauge_Type()
)
vplsStatusAcFailPermGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusAcFailPermGauge.setStatus("current")
_VplsStatusDesignatedForwarder_Type = TruthValue
_VplsStatusDesignatedForwarder_Object = MibTableColumn
vplsStatusDesignatedForwarder = _VplsStatusDesignatedForwarder_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 2, 1, 14),
    _VplsStatusDesignatedForwarder_Type()
)
vplsStatusDesignatedForwarder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusDesignatedForwarder.setStatus("current")
_VplsAcBindCfgTable_Object = MibTable
vplsAcBindCfgTable = _VplsAcBindCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 3)
)
if mibBuilder.loadTexts:
    vplsAcBindCfgTable.setStatus("current")
_VplsAcBindCfgEntry_Object = MibTableRow
vplsAcBindCfgEntry = _VplsAcBindCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 3, 1)
)
vplsAcBindCfgEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vplsAcBindCfgEntry.setStatus("current")
_VplsAcBindCfgRowStatus_Type = RowStatus
_VplsAcBindCfgRowStatus_Object = MibTableColumn
vplsAcBindCfgRowStatus = _VplsAcBindCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 3, 1, 3),
    _VplsAcBindCfgRowStatus_Type()
)
vplsAcBindCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsAcBindCfgRowStatus.setStatus("current")


class _VplsAcBindCfgAdminStatus_Type(AdminStatus):
    """Custom type vplsAcBindCfgAdminStatus based on AdminStatus"""
    defaultValue = 1


_VplsAcBindCfgAdminStatus_Type.__name__ = "AdminStatus"
_VplsAcBindCfgAdminStatus_Object = MibTableColumn
vplsAcBindCfgAdminStatus = _VplsAcBindCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 3, 1, 4),
    _VplsAcBindCfgAdminStatus_Type()
)
vplsAcBindCfgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsAcBindCfgAdminStatus.setStatus("current")
_VplsAcBindCfgOperStatus_Type = NpgOperStatus
_VplsAcBindCfgOperStatus_Object = MibTableColumn
vplsAcBindCfgOperStatus = _VplsAcBindCfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 3, 1, 5),
    _VplsAcBindCfgOperStatus_Type()
)
vplsAcBindCfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsAcBindCfgOperStatus.setStatus("current")


class _VplsAcBindCfgVplsIndex_Type(NumericIndexOrZero):
    """Custom type vplsAcBindCfgVplsIndex based on NumericIndexOrZero"""
    defaultValue = 0


_VplsAcBindCfgVplsIndex_Type.__name__ = "NumericIndexOrZero"
_VplsAcBindCfgVplsIndex_Object = MibTableColumn
vplsAcBindCfgVplsIndex = _VplsAcBindCfgVplsIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 3, 1, 6),
    _VplsAcBindCfgVplsIndex_Type()
)
vplsAcBindCfgVplsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsAcBindCfgVplsIndex.setStatus("current")


class _VplsAcBindCfgMacAddrLimit_Type(Unsigned32):
    """Custom type vplsAcBindCfgMacAddrLimit based on Unsigned32"""
    defaultValue = 0


_VplsAcBindCfgMacAddrLimit_Type.__name__ = "Unsigned32"
_VplsAcBindCfgMacAddrLimit_Object = MibTableColumn
vplsAcBindCfgMacAddrLimit = _VplsAcBindCfgMacAddrLimit_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 3, 1, 7),
    _VplsAcBindCfgMacAddrLimit_Type()
)
vplsAcBindCfgMacAddrLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsAcBindCfgMacAddrLimit.setStatus("current")


class _VplsAcBindCfgMacLearning_Type(TruthValue):
    """Custom type vplsAcBindCfgMacLearning based on TruthValue"""
    defaultValue = 1


_VplsAcBindCfgMacLearning_Type.__name__ = "TruthValue"
_VplsAcBindCfgMacLearning_Object = MibTableColumn
vplsAcBindCfgMacLearning = _VplsAcBindCfgMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 3, 1, 8),
    _VplsAcBindCfgMacLearning_Type()
)
vplsAcBindCfgMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsAcBindCfgMacLearning.setStatus("current")
_VplsPwSetBindCfgTable_Object = MibTable
vplsPwSetBindCfgTable = _VplsPwSetBindCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 4)
)
if mibBuilder.loadTexts:
    vplsPwSetBindCfgTable.setStatus("current")
_VplsPwSetBindCfgEntry_Object = MibTableRow
vplsPwSetBindCfgEntry = _VplsPwSetBindCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 4, 1)
)
vplsPwSetBindCfgEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "DC-VPLS-MIB", "vplsPwSetBindCfgIndex"),
)
if mibBuilder.loadTexts:
    vplsPwSetBindCfgEntry.setStatus("current")
_VplsPwSetBindCfgIndex_Type = NumericIndex
_VplsPwSetBindCfgIndex_Object = MibTableColumn
vplsPwSetBindCfgIndex = _VplsPwSetBindCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 4, 1, 2),
    _VplsPwSetBindCfgIndex_Type()
)
vplsPwSetBindCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vplsPwSetBindCfgIndex.setStatus("current")
_VplsPwSetBindCfgRowStatus_Type = RowStatus
_VplsPwSetBindCfgRowStatus_Object = MibTableColumn
vplsPwSetBindCfgRowStatus = _VplsPwSetBindCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 4, 1, 3),
    _VplsPwSetBindCfgRowStatus_Type()
)
vplsPwSetBindCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwSetBindCfgRowStatus.setStatus("current")


class _VplsPwSetBindCfgAdminStatus_Type(AdminStatus):
    """Custom type vplsPwSetBindCfgAdminStatus based on AdminStatus"""
    defaultValue = 1


_VplsPwSetBindCfgAdminStatus_Type.__name__ = "AdminStatus"
_VplsPwSetBindCfgAdminStatus_Object = MibTableColumn
vplsPwSetBindCfgAdminStatus = _VplsPwSetBindCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 4, 1, 4),
    _VplsPwSetBindCfgAdminStatus_Type()
)
vplsPwSetBindCfgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwSetBindCfgAdminStatus.setStatus("current")
_VplsPwSetBindCfgOperStatus_Type = NpgOperStatus
_VplsPwSetBindCfgOperStatus_Object = MibTableColumn
vplsPwSetBindCfgOperStatus = _VplsPwSetBindCfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 4, 1, 5),
    _VplsPwSetBindCfgOperStatus_Type()
)
vplsPwSetBindCfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsPwSetBindCfgOperStatus.setStatus("current")


class _VplsPwSetBindCfgVplsIndex_Type(NumericIndexOrZero):
    """Custom type vplsPwSetBindCfgVplsIndex based on NumericIndexOrZero"""
    defaultValue = 0


_VplsPwSetBindCfgVplsIndex_Type.__name__ = "NumericIndexOrZero"
_VplsPwSetBindCfgVplsIndex_Object = MibTableColumn
vplsPwSetBindCfgVplsIndex = _VplsPwSetBindCfgVplsIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 4, 1, 6),
    _VplsPwSetBindCfgVplsIndex_Type()
)
vplsPwSetBindCfgVplsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwSetBindCfgVplsIndex.setStatus("current")


class _VplsPwSetBindCfgSpltHznGrp_Type(Unsigned32):
    """Custom type vplsPwSetBindCfgSpltHznGrp based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VplsPwSetBindCfgSpltHznGrp_Type.__name__ = "Unsigned32"
_VplsPwSetBindCfgSpltHznGrp_Object = MibTableColumn
vplsPwSetBindCfgSpltHznGrp = _VplsPwSetBindCfgSpltHznGrp_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 4, 1, 7),
    _VplsPwSetBindCfgSpltHznGrp_Type()
)
vplsPwSetBindCfgSpltHznGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwSetBindCfgSpltHznGrp.setStatus("current")


class _VplsPwSetBindCfgMacLearning_Type(TruthValue):
    """Custom type vplsPwSetBindCfgMacLearning based on TruthValue"""
    defaultValue = 1


_VplsPwSetBindCfgMacLearning_Type.__name__ = "TruthValue"
_VplsPwSetBindCfgMacLearning_Object = MibTableColumn
vplsPwSetBindCfgMacLearning = _VplsPwSetBindCfgMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 4, 1, 8),
    _VplsPwSetBindCfgMacLearning_Type()
)
vplsPwSetBindCfgMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwSetBindCfgMacLearning.setStatus("current")
_VplsAcBindTable_Object = MibTable
vplsAcBindTable = _VplsAcBindTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 5)
)
if mibBuilder.loadTexts:
    vplsAcBindTable.setStatus("current")
_VplsAcBindEntry_Object = MibTableRow
vplsAcBindEntry = _VplsAcBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 5, 1)
)
vplsAcBindEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "DC-VPLS-MIB", "vplsIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vplsAcBindEntry.setStatus("current")
_VplsAcBindOperStatus_Type = NpgOperStatus
_VplsAcBindOperStatus_Object = MibTableColumn
vplsAcBindOperStatus = _VplsAcBindOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 5, 1, 4),
    _VplsAcBindOperStatus_Type()
)
vplsAcBindOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsAcBindOperStatus.setStatus("current")
_VplsAcBindAcStatus_Type = VplsAcStatus
_VplsAcBindAcStatus_Object = MibTableColumn
vplsAcBindAcStatus = _VplsAcBindAcStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 5, 1, 5),
    _VplsAcBindAcStatus_Type()
)
vplsAcBindAcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsAcBindAcStatus.setStatus("current")
_VplsPwSetBindTable_Object = MibTable
vplsPwSetBindTable = _VplsPwSetBindTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 6)
)
if mibBuilder.loadTexts:
    vplsPwSetBindTable.setStatus("current")
_VplsPwSetBindEntry_Object = MibTableRow
vplsPwSetBindEntry = _VplsPwSetBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 6, 1)
)
vplsPwSetBindEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "DC-VPLS-MIB", "vplsIndex"),
    (0, "DC-VPLS-MIB", "vplsPwSetBindIndex"),
)
if mibBuilder.loadTexts:
    vplsPwSetBindEntry.setStatus("current")
_VplsPwSetBindIndex_Type = NumericIndex
_VplsPwSetBindIndex_Object = MibTableColumn
vplsPwSetBindIndex = _VplsPwSetBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 6, 1, 3),
    _VplsPwSetBindIndex_Type()
)
vplsPwSetBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vplsPwSetBindIndex.setStatus("current")
_VplsPwSetBindOperStatus_Type = NpgOperStatus
_VplsPwSetBindOperStatus_Object = MibTableColumn
vplsPwSetBindOperStatus = _VplsPwSetBindOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 6, 1, 4),
    _VplsPwSetBindOperStatus_Type()
)
vplsPwSetBindOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsPwSetBindOperStatus.setStatus("current")
_VplsPwSetBindConfigType_Type = L2vpnPwBindType
_VplsPwSetBindConfigType_Object = MibTableColumn
vplsPwSetBindConfigType = _VplsPwSetBindConfigType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 6, 1, 5),
    _VplsPwSetBindConfigType_Type()
)
vplsPwSetBindConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsPwSetBindConfigType.setStatus("current")
_VplsPwSetBindIfIndex_Type = InterfaceIndex
_VplsPwSetBindIfIndex_Object = MibTableColumn
vplsPwSetBindIfIndex = _VplsPwSetBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 6, 1, 6),
    _VplsPwSetBindIfIndex_Type()
)
vplsPwSetBindIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsPwSetBindIfIndex.setStatus("current")
_VplsPwSetBindRemoteRD_Type = BgpRouteDistinguisher
_VplsPwSetBindRemoteRD_Object = MibTableColumn
vplsPwSetBindRemoteRD = _VplsPwSetBindRemoteRD_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 6, 1, 7),
    _VplsPwSetBindRemoteRD_Type()
)
vplsPwSetBindRemoteRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsPwSetBindRemoteRD.setStatus("current")
_VplsPwSetBindRemoteAddrType_Type = InetAddressType
_VplsPwSetBindRemoteAddrType_Object = MibTableColumn
vplsPwSetBindRemoteAddrType = _VplsPwSetBindRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 6, 1, 8),
    _VplsPwSetBindRemoteAddrType_Type()
)
vplsPwSetBindRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsPwSetBindRemoteAddrType.setStatus("current")
_VplsPwSetBindRemoteAddr_Type = InetAddress
_VplsPwSetBindRemoteAddr_Object = MibTableColumn
vplsPwSetBindRemoteAddr = _VplsPwSetBindRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 1, 6, 1, 9),
    _VplsPwSetBindRemoteAddr_Type()
)
vplsPwSetBindRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsPwSetBindRemoteAddr.setStatus("current")
_VplsConformance_ObjectIdentity = ObjectIdentity
vplsConformance = _VplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 2)
)
_VplsCompliances_ObjectIdentity = ObjectIdentity
vplsCompliances = _VplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 2, 1)
)
_VplsGroups_ObjectIdentity = ObjectIdentity
vplsGroups = _VplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 2, 2)
)

# Managed Objects groups

vplsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 2, 2, 1)
)
vplsBaseGroup.setObjects(
      *(("DC-VPLS-MIB", "vplsConfigRowStatus"),
        ("DC-VPLS-MIB", "vplsConfigAdminStatus"),
        ("DC-VPLS-MIB", "vplsConfigOperStatus"),
        ("DC-VPLS-MIB", "vplsConfigName"),
        ("DC-VPLS-MIB", "vplsConfigDescr"),
        ("DC-VPLS-MIB", "vplsConfigADType"),
        ("DC-VPLS-MIB", "vplsConfigSigType"),
        ("DC-VPLS-MIB", "vplsConfigPwEncapType"),
        ("DC-VPLS-MIB", "vplsConfigMacLearning"),
        ("DC-VPLS-MIB", "vplsConfigDiscardUnknownDest"),
        ("DC-VPLS-MIB", "vplsConfigMacAge"),
        ("DC-VPLS-MIB", "vplsConfigMtu"),
        ("DC-VPLS-MIB", "vplsConfigMacSize"),
        ("DC-VPLS-MIB", "vplsConfigPwMacAddressLimit"),
        ("DC-VPLS-MIB", "vplsConfigControlWord"),
        ("DC-VPLS-MIB", "vplsConfigSeqDelivery"),
        ("DC-VPLS-MIB", "vplsConfigMultiCastFloodMode"),
        ("DC-VPLS-MIB", "vplsStatusOperStatus"),
        ("DC-VPLS-MIB", "vplsStatusPwSetDownGauge"),
        ("DC-VPLS-MIB", "vplsStatusPwSetGoingUpGauge"),
        ("DC-VPLS-MIB", "vplsStatusPwSetUpGauge"),
        ("DC-VPLS-MIB", "vplsStatusPwSetFailGauge"),
        ("DC-VPLS-MIB", "vplsStatusPwSetFailPermGauge"),
        ("DC-VPLS-MIB", "vplsStatusAcDownGauge"),
        ("DC-VPLS-MIB", "vplsStatusAcGoingUpGauge"),
        ("DC-VPLS-MIB", "vplsStatusAcUpGauge"),
        ("DC-VPLS-MIB", "vplsStatusAcFailGauge"),
        ("DC-VPLS-MIB", "vplsStatusAcFailPermGauge"),
        ("DC-VPLS-MIB", "vplsAcBindCfgRowStatus"),
        ("DC-VPLS-MIB", "vplsAcBindCfgAdminStatus"),
        ("DC-VPLS-MIB", "vplsAcBindCfgOperStatus"),
        ("DC-VPLS-MIB", "vplsAcBindCfgVplsIndex"),
        ("DC-VPLS-MIB", "vplsAcBindCfgMacAddrLimit"),
        ("DC-VPLS-MIB", "vplsAcBindCfgMacLearning"),
        ("DC-VPLS-MIB", "vplsAcBindOperStatus"),
        ("DC-VPLS-MIB", "vplsAcBindAcStatus"),
        ("DC-VPLS-MIB", "vplsPwSetBindOperStatus"),
        ("DC-VPLS-MIB", "vplsPwSetBindConfigType"),
        ("DC-VPLS-MIB", "vplsPwSetBindIfIndex"))
)
if mibBuilder.loadTexts:
    vplsBaseGroup.setStatus("current")

vplsManualPwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 2, 2, 2)
)
vplsManualPwGroup.setObjects(
      *(("DC-VPLS-MIB", "vplsPwSetBindCfgRowStatus"),
        ("DC-VPLS-MIB", "vplsPwSetBindCfgAdminStatus"),
        ("DC-VPLS-MIB", "vplsPwSetBindCfgOperStatus"),
        ("DC-VPLS-MIB", "vplsPwSetBindCfgVplsIndex"),
        ("DC-VPLS-MIB", "vplsPwSetBindCfgSpltHznGrp"),
        ("DC-VPLS-MIB", "vplsPwSetBindCfgMacLearning"))
)
if mibBuilder.loadTexts:
    vplsManualPwGroup.setStatus("current")

vplsAutoPwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 2, 2, 3)
)
vplsAutoPwGroup.setObjects(
      *(("DC-VPLS-MIB", "vplsStatusDesignatedForwarder"),
        ("DC-VPLS-MIB", "vplsConfigRouteDistinguisher"),
        ("DC-VPLS-MIB", "vplsConfigVpnId"),
        ("DC-VPLS-MIB", "vplsConfigLocalVeID"),
        ("DC-VPLS-MIB", "vplsConfigLocalPreference"),
        ("DC-VPLS-MIB", "vplsConfigLabelBlockSize"),
        ("DC-VPLS-MIB", "vplsConfigADPwMacLearning"),
        ("DC-VPLS-MIB", "vplsConfigIgnoreMtuMismatch"),
        ("DC-VPLS-MIB", "vplsConfigIgnoreEncapsMismatch"),
        ("DC-VPLS-MIB", "vplsPwSetBindRemoteRD"),
        ("DC-VPLS-MIB", "vplsPwSetBindRemoteAddrType"),
        ("DC-VPLS-MIB", "vplsPwSetBindRemoteAddr"))
)
if mibBuilder.loadTexts:
    vplsAutoPwGroup.setStatus("current")


# Notification objects

vplsStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 0, 1)
)
vplsStatusChanged.setObjects(
      *(("DC-VPLS-MIB", "vplsConfigName"),
        ("DC-VPLS-MIB", "vplsConfigVpnId"),
        ("DC-VPLS-MIB", "vplsConfigAdminStatus"),
        ("DC-VPLS-MIB", "vplsStatusOperStatus"))
)
if mibBuilder.loadTexts:
    vplsStatusChanged.setStatus(
        "current"
    )


# Notifications groups

vplsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 2, 2, 4)
)
vplsNotificationGroup.setObjects(
    ("DC-VPLS-MIB", "vplsStatusChanged")
)
if mibBuilder.loadTexts:
    vplsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vplsFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 2, 1, 1)
)
vplsFullCompliance.setObjects(
      *(("DC-VPLS-MIB", "vplsBaseGroup"),
        ("DC-VPLS-MIB", "vplsNotificationGroup"),
        ("DC-VPLS-MIB", "vplsManualPwGroup"),
        ("DC-VPLS-MIB", "vplsAutoPwGroup"))
)
if mibBuilder.loadTexts:
    vplsFullCompliance.setStatus(
        "current"
    )

vplsManualPwCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 2, 1, 2)
)
vplsManualPwCompliance.setObjects(
      *(("DC-VPLS-MIB", "vplsBaseGroup"),
        ("DC-VPLS-MIB", "vplsNotificationGroup"),
        ("DC-VPLS-MIB", "vplsManualPwGroup"))
)
if mibBuilder.loadTexts:
    vplsManualPwCompliance.setStatus(
        "current"
    )

vplsAutoPwCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 18, 2, 1, 3)
)
vplsAutoPwCompliance.setObjects(
      *(("DC-VPLS-MIB", "vplsBaseGroup"),
        ("DC-VPLS-MIB", "vplsNotificationGroup"),
        ("DC-VPLS-MIB", "vplsAutoPwGroup"))
)
if mibBuilder.loadTexts:
    vplsAutoPwCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-VPLS-MIB",
    **{"VplsAcStatus": VplsAcStatus,
       "VplsMCFloodMode": VplsMCFloodMode,
       "nbase": nbase,
       "opx": opx,
       "vplsMib": vplsMib,
       "vplsNotifications": vplsNotifications,
       "vplsStatusChanged": vplsStatusChanged,
       "vplsObjects": vplsObjects,
       "vplsConfigTable": vplsConfigTable,
       "vplsConfigEntry": vplsConfigEntry,
       "vplsIndex": vplsIndex,
       "vplsConfigRowStatus": vplsConfigRowStatus,
       "vplsConfigAdminStatus": vplsConfigAdminStatus,
       "vplsConfigOperStatus": vplsConfigOperStatus,
       "vplsConfigName": vplsConfigName,
       "vplsConfigDescr": vplsConfigDescr,
       "vplsConfigADType": vplsConfigADType,
       "vplsConfigSigType": vplsConfigSigType,
       "vplsConfigPwEncapType": vplsConfigPwEncapType,
       "vplsConfigMacLearning": vplsConfigMacLearning,
       "vplsConfigDiscardUnknownDest": vplsConfigDiscardUnknownDest,
       "vplsConfigMacAge": vplsConfigMacAge,
       "vplsConfigMtu": vplsConfigMtu,
       "vplsConfigMacSize": vplsConfigMacSize,
       "vplsConfigPwMacAddressLimit": vplsConfigPwMacAddressLimit,
       "vplsConfigControlWord": vplsConfigControlWord,
       "vplsConfigSeqDelivery": vplsConfigSeqDelivery,
       "vplsConfigRouteDistinguisher": vplsConfigRouteDistinguisher,
       "vplsConfigVpnId": vplsConfigVpnId,
       "vplsConfigLocalVeID": vplsConfigLocalVeID,
       "vplsConfigLocalPreference": vplsConfigLocalPreference,
       "vplsConfigLabelBlockSize": vplsConfigLabelBlockSize,
       "vplsConfigADPwMacLearning": vplsConfigADPwMacLearning,
       "vplsConfigMultiCastFloodMode": vplsConfigMultiCastFloodMode,
       "vplsConfigIgnoreMtuMismatch": vplsConfigIgnoreMtuMismatch,
       "vplsConfigIgnoreEncapsMismatch": vplsConfigIgnoreEncapsMismatch,
       "vplsStatusTable": vplsStatusTable,
       "vplsStatusEntry": vplsStatusEntry,
       "vplsStatusOperStatus": vplsStatusOperStatus,
       "vplsStatusPwSetDownGauge": vplsStatusPwSetDownGauge,
       "vplsStatusPwSetGoingUpGauge": vplsStatusPwSetGoingUpGauge,
       "vplsStatusPwSetUpGauge": vplsStatusPwSetUpGauge,
       "vplsStatusPwSetFailGauge": vplsStatusPwSetFailGauge,
       "vplsStatusPwSetFailPermGauge": vplsStatusPwSetFailPermGauge,
       "vplsStatusAcDownGauge": vplsStatusAcDownGauge,
       "vplsStatusAcGoingUpGauge": vplsStatusAcGoingUpGauge,
       "vplsStatusAcUpGauge": vplsStatusAcUpGauge,
       "vplsStatusAcFailGauge": vplsStatusAcFailGauge,
       "vplsStatusAcFailPermGauge": vplsStatusAcFailPermGauge,
       "vplsStatusDesignatedForwarder": vplsStatusDesignatedForwarder,
       "vplsAcBindCfgTable": vplsAcBindCfgTable,
       "vplsAcBindCfgEntry": vplsAcBindCfgEntry,
       "vplsAcBindCfgRowStatus": vplsAcBindCfgRowStatus,
       "vplsAcBindCfgAdminStatus": vplsAcBindCfgAdminStatus,
       "vplsAcBindCfgOperStatus": vplsAcBindCfgOperStatus,
       "vplsAcBindCfgVplsIndex": vplsAcBindCfgVplsIndex,
       "vplsAcBindCfgMacAddrLimit": vplsAcBindCfgMacAddrLimit,
       "vplsAcBindCfgMacLearning": vplsAcBindCfgMacLearning,
       "vplsPwSetBindCfgTable": vplsPwSetBindCfgTable,
       "vplsPwSetBindCfgEntry": vplsPwSetBindCfgEntry,
       "vplsPwSetBindCfgIndex": vplsPwSetBindCfgIndex,
       "vplsPwSetBindCfgRowStatus": vplsPwSetBindCfgRowStatus,
       "vplsPwSetBindCfgAdminStatus": vplsPwSetBindCfgAdminStatus,
       "vplsPwSetBindCfgOperStatus": vplsPwSetBindCfgOperStatus,
       "vplsPwSetBindCfgVplsIndex": vplsPwSetBindCfgVplsIndex,
       "vplsPwSetBindCfgSpltHznGrp": vplsPwSetBindCfgSpltHznGrp,
       "vplsPwSetBindCfgMacLearning": vplsPwSetBindCfgMacLearning,
       "vplsAcBindTable": vplsAcBindTable,
       "vplsAcBindEntry": vplsAcBindEntry,
       "vplsAcBindOperStatus": vplsAcBindOperStatus,
       "vplsAcBindAcStatus": vplsAcBindAcStatus,
       "vplsPwSetBindTable": vplsPwSetBindTable,
       "vplsPwSetBindEntry": vplsPwSetBindEntry,
       "vplsPwSetBindIndex": vplsPwSetBindIndex,
       "vplsPwSetBindOperStatus": vplsPwSetBindOperStatus,
       "vplsPwSetBindConfigType": vplsPwSetBindConfigType,
       "vplsPwSetBindIfIndex": vplsPwSetBindIfIndex,
       "vplsPwSetBindRemoteRD": vplsPwSetBindRemoteRD,
       "vplsPwSetBindRemoteAddrType": vplsPwSetBindRemoteAddrType,
       "vplsPwSetBindRemoteAddr": vplsPwSetBindRemoteAddr,
       "vplsConformance": vplsConformance,
       "vplsCompliances": vplsCompliances,
       "vplsFullCompliance": vplsFullCompliance,
       "vplsManualPwCompliance": vplsManualPwCompliance,
       "vplsAutoPwCompliance": vplsAutoPwCompliance,
       "vplsGroups": vplsGroups,
       "vplsBaseGroup": vplsBaseGroup,
       "vplsManualPwGroup": vplsManualPwGroup,
       "vplsAutoPwGroup": vplsAutoPwGroup,
       "vplsNotificationGroup": vplsNotificationGroup}
)
