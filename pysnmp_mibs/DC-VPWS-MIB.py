# SNMP MIB module (DC-VPWS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/DC-VPWS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:11 2025
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
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
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

vpwsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_Opx_ObjectIdentity = ObjectIdentity
opx = _Opx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10)
)
_VpwsObjects_ObjectIdentity = ObjectIdentity
vpwsObjects = _VpwsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1)
)
_VpwsConfigTable_Object = MibTable
vpwsConfigTable = _VpwsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1)
)
if mibBuilder.loadTexts:
    vpwsConfigTable.setStatus("current")
_VpwsConfigEntry_Object = MibTableRow
vpwsConfigEntry = _VpwsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1)
)
vpwsConfigEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "DC-VPWS-MIB", "vpwsIndex"),
)
if mibBuilder.loadTexts:
    vpwsConfigEntry.setStatus("current")
_VpwsIndex_Type = NumericIndex
_VpwsIndex_Object = MibTableColumn
vpwsIndex = _VpwsIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 2),
    _VpwsIndex_Type()
)
vpwsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vpwsIndex.setStatus("current")
_VpwsConfigRowStatus_Type = RowStatus
_VpwsConfigRowStatus_Object = MibTableColumn
vpwsConfigRowStatus = _VpwsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 3),
    _VpwsConfigRowStatus_Type()
)
vpwsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigRowStatus.setStatus("current")


class _VpwsConfigAdminStatus_Type(AdminStatus):
    """Custom type vpwsConfigAdminStatus based on AdminStatus"""
    defaultValue = 1


_VpwsConfigAdminStatus_Type.__name__ = "AdminStatus"
_VpwsConfigAdminStatus_Object = MibTableColumn
vpwsConfigAdminStatus = _VpwsConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 4),
    _VpwsConfigAdminStatus_Type()
)
vpwsConfigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigAdminStatus.setStatus("current")
_VpwsConfigOperStatus_Type = NpgOperStatus
_VpwsConfigOperStatus_Object = MibTableColumn
vpwsConfigOperStatus = _VpwsConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 5),
    _VpwsConfigOperStatus_Type()
)
vpwsConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsConfigOperStatus.setStatus("current")
_VpwsConfigName_Type = SnmpAdminString
_VpwsConfigName_Object = MibTableColumn
vpwsConfigName = _VpwsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 6),
    _VpwsConfigName_Type()
)
vpwsConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigName.setStatus("current")
_VpwsConfigDescr_Type = SnmpAdminString
_VpwsConfigDescr_Object = MibTableColumn
vpwsConfigDescr = _VpwsConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 7),
    _VpwsConfigDescr_Type()
)
vpwsConfigDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigDescr.setStatus("current")


class _VpwsConfigADType_Type(L2vpnADType):
    """Custom type vpwsConfigADType based on L2vpnADType"""
    defaultValue = 1


_VpwsConfigADType_Type.__name__ = "L2vpnADType"
_VpwsConfigADType_Object = MibTableColumn
vpwsConfigADType = _VpwsConfigADType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 8),
    _VpwsConfigADType_Type()
)
vpwsConfigADType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigADType.setStatus("current")


class _VpwsConfigSigType_Type(L2vpnSigType):
    """Custom type vpwsConfigSigType based on L2vpnSigType"""
    defaultValue = 1


_VpwsConfigSigType_Type.__name__ = "L2vpnSigType"
_VpwsConfigSigType_Object = MibTableColumn
vpwsConfigSigType = _VpwsConfigSigType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 9),
    _VpwsConfigSigType_Type()
)
vpwsConfigSigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigSigType.setStatus("current")


class _VpwsConfigPwEncapType_Type(IANAPwTypeTC):
    """Custom type vpwsConfigPwEncapType based on IANAPwTypeTC"""
    defaultValue = 5


_VpwsConfigPwEncapType_Type.__name__ = "IANAPwTypeTC"
_VpwsConfigPwEncapType_Object = MibTableColumn
vpwsConfigPwEncapType = _VpwsConfigPwEncapType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 10),
    _VpwsConfigPwEncapType_Type()
)
vpwsConfigPwEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigPwEncapType.setStatus("current")


class _VpwsConfigMtu_Type(Unsigned32):
    """Custom type vpwsConfigMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9192),
    )


_VpwsConfigMtu_Type.__name__ = "Unsigned32"
_VpwsConfigMtu_Object = MibTableColumn
vpwsConfigMtu = _VpwsConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 11),
    _VpwsConfigMtu_Type()
)
vpwsConfigMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigMtu.setStatus("current")


class _VpwsConfigControlWord_Type(TruthValue):
    """Custom type vpwsConfigControlWord based on TruthValue"""
    defaultValue = 2


_VpwsConfigControlWord_Type.__name__ = "TruthValue"
_VpwsConfigControlWord_Object = MibTableColumn
vpwsConfigControlWord = _VpwsConfigControlWord_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 12),
    _VpwsConfigControlWord_Type()
)
vpwsConfigControlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigControlWord.setStatus("current")


class _VpwsConfigSeqDelivery_Type(TruthValue):
    """Custom type vpwsConfigSeqDelivery based on TruthValue"""
    defaultValue = 2


_VpwsConfigSeqDelivery_Type.__name__ = "TruthValue"
_VpwsConfigSeqDelivery_Object = MibTableColumn
vpwsConfigSeqDelivery = _VpwsConfigSeqDelivery_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 13),
    _VpwsConfigSeqDelivery_Type()
)
vpwsConfigSeqDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigSeqDelivery.setStatus("current")


class _VpwsConfigRouteDistinguisher_Type(BgpRouteDistinguisher):
    """Custom type vpwsConfigRouteDistinguisher based on BgpRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_VpwsConfigRouteDistinguisher_Type.__name__ = "BgpRouteDistinguisher"
_VpwsConfigRouteDistinguisher_Object = MibTableColumn
vpwsConfigRouteDistinguisher = _VpwsConfigRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 14),
    _VpwsConfigRouteDistinguisher_Type()
)
vpwsConfigRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigRouteDistinguisher.setStatus("current")


class _VpwsConfigVpnId_Type(BgpExtendedCommunity):
    """Custom type vpwsConfigVpnId based on BgpExtendedCommunity"""
    defaultHexValue = "0000000000000000"


_VpwsConfigVpnId_Type.__name__ = "BgpExtendedCommunity"
_VpwsConfigVpnId_Object = MibTableColumn
vpwsConfigVpnId = _VpwsConfigVpnId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 15),
    _VpwsConfigVpnId_Type()
)
vpwsConfigVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigVpnId.setStatus("current")


class _VpwsConfigLocalSiteID_Type(L2vpnVeIdOrZero):
    """Custom type vpwsConfigLocalSiteID based on L2vpnVeIdOrZero"""
    defaultValue = 0


_VpwsConfigLocalSiteID_Type.__name__ = "L2vpnVeIdOrZero"
_VpwsConfigLocalSiteID_Object = MibTableColumn
vpwsConfigLocalSiteID = _VpwsConfigLocalSiteID_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 16),
    _VpwsConfigLocalSiteID_Type()
)
vpwsConfigLocalSiteID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigLocalSiteID.setStatus("current")


class _VpwsConfigLocalPreference_Type(Unsigned32):
    """Custom type vpwsConfigLocalPreference based on Unsigned32"""
    defaultValue = 100


_VpwsConfigLocalPreference_Type.__name__ = "Unsigned32"
_VpwsConfigLocalPreference_Object = MibTableColumn
vpwsConfigLocalPreference = _VpwsConfigLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 17),
    _VpwsConfigLocalPreference_Type()
)
vpwsConfigLocalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigLocalPreference.setStatus("current")


class _VpwsConfigLabelBlockSize_Type(Unsigned32):
    """Custom type vpwsConfigLabelBlockSize based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
    )


_VpwsConfigLabelBlockSize_Type.__name__ = "Unsigned32"
_VpwsConfigLabelBlockSize_Object = MibTableColumn
vpwsConfigLabelBlockSize = _VpwsConfigLabelBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 18),
    _VpwsConfigLabelBlockSize_Type()
)
vpwsConfigLabelBlockSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigLabelBlockSize.setStatus("current")


class _VpwsConfigIncludeCSV_Type(TruthValue):
    """Custom type vpwsConfigIncludeCSV based on TruthValue"""
    defaultValue = 2


_VpwsConfigIncludeCSV_Type.__name__ = "TruthValue"
_VpwsConfigIncludeCSV_Object = MibTableColumn
vpwsConfigIncludeCSV = _VpwsConfigIncludeCSV_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 19),
    _VpwsConfigIncludeCSV_Type()
)
vpwsConfigIncludeCSV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigIncludeCSV.setStatus("current")


class _VpwsConfigIgnoreMtuMismatch_Type(TruthValue):
    """Custom type vpwsConfigIgnoreMtuMismatch based on TruthValue"""
    defaultValue = 2


_VpwsConfigIgnoreMtuMismatch_Type.__name__ = "TruthValue"
_VpwsConfigIgnoreMtuMismatch_Object = MibTableColumn
vpwsConfigIgnoreMtuMismatch = _VpwsConfigIgnoreMtuMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 20),
    _VpwsConfigIgnoreMtuMismatch_Type()
)
vpwsConfigIgnoreMtuMismatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigIgnoreMtuMismatch.setStatus("current")


class _VpwsConfigIgnoreEncapsMismatch_Type(TruthValue):
    """Custom type vpwsConfigIgnoreEncapsMismatch based on TruthValue"""
    defaultValue = 2


_VpwsConfigIgnoreEncapsMismatch_Type.__name__ = "TruthValue"
_VpwsConfigIgnoreEncapsMismatch_Object = MibTableColumn
vpwsConfigIgnoreEncapsMismatch = _VpwsConfigIgnoreEncapsMismatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 1, 1, 21),
    _VpwsConfigIgnoreEncapsMismatch_Type()
)
vpwsConfigIgnoreEncapsMismatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsConfigIgnoreEncapsMismatch.setStatus("current")
_VpwsStatusTable_Object = MibTable
vpwsStatusTable = _VpwsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 2)
)
if mibBuilder.loadTexts:
    vpwsStatusTable.setStatus("current")
_VpwsStatusEntry_Object = MibTableRow
vpwsStatusEntry = _VpwsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 2, 1)
)
vpwsStatusEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "DC-VPWS-MIB", "vpwsIndex"),
)
if mibBuilder.loadTexts:
    vpwsStatusEntry.setStatus("current")
_VpwsStatusOperStatus_Type = NpgOperStatus
_VpwsStatusOperStatus_Object = MibTableColumn
vpwsStatusOperStatus = _VpwsStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 2, 1, 3),
    _VpwsStatusOperStatus_Type()
)
vpwsStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsStatusOperStatus.setStatus("current")
_VpwsStatusVcCount_Type = Gauge32
_VpwsStatusVcCount_Object = MibTableColumn
vpwsStatusVcCount = _VpwsStatusVcCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 2, 1, 4),
    _VpwsStatusVcCount_Type()
)
vpwsStatusVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsStatusVcCount.setStatus("current")
_VpwsStatusDesignatedForwarder_Type = TruthValue
_VpwsStatusDesignatedForwarder_Object = MibTableColumn
vpwsStatusDesignatedForwarder = _VpwsStatusDesignatedForwarder_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 2, 1, 5),
    _VpwsStatusDesignatedForwarder_Type()
)
vpwsStatusDesignatedForwarder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsStatusDesignatedForwarder.setStatus("current")
_VpwsBindCfgTable_Object = MibTable
vpwsBindCfgTable = _VpwsBindCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 3)
)
if mibBuilder.loadTexts:
    vpwsBindCfgTable.setStatus("current")
_VpwsBindCfgEntry_Object = MibTableRow
vpwsBindCfgEntry = _VpwsBindCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 3, 1)
)
vpwsBindCfgEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vpwsBindCfgEntry.setStatus("current")
_VpwsBindCfgRowStatus_Type = RowStatus
_VpwsBindCfgRowStatus_Object = MibTableColumn
vpwsBindCfgRowStatus = _VpwsBindCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 3, 1, 3),
    _VpwsBindCfgRowStatus_Type()
)
vpwsBindCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsBindCfgRowStatus.setStatus("current")


class _VpwsBindCfgAdminStatus_Type(AdminStatus):
    """Custom type vpwsBindCfgAdminStatus based on AdminStatus"""
    defaultValue = 1


_VpwsBindCfgAdminStatus_Type.__name__ = "AdminStatus"
_VpwsBindCfgAdminStatus_Object = MibTableColumn
vpwsBindCfgAdminStatus = _VpwsBindCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 3, 1, 4),
    _VpwsBindCfgAdminStatus_Type()
)
vpwsBindCfgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsBindCfgAdminStatus.setStatus("current")
_VpwsBindCfgOperStatus_Type = NpgOperStatus
_VpwsBindCfgOperStatus_Object = MibTableColumn
vpwsBindCfgOperStatus = _VpwsBindCfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 3, 1, 5),
    _VpwsBindCfgOperStatus_Type()
)
vpwsBindCfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsBindCfgOperStatus.setStatus("current")


class _VpwsBindCfgVpwsIndex_Type(NumericIndexOrZero):
    """Custom type vpwsBindCfgVpwsIndex based on NumericIndexOrZero"""
    defaultValue = 0


_VpwsBindCfgVpwsIndex_Type.__name__ = "NumericIndexOrZero"
_VpwsBindCfgVpwsIndex_Object = MibTableColumn
vpwsBindCfgVpwsIndex = _VpwsBindCfgVpwsIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 3, 1, 6),
    _VpwsBindCfgVpwsIndex_Type()
)
vpwsBindCfgVpwsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsBindCfgVpwsIndex.setStatus("current")


class _VpwsBindCfgPwBindType_Type(L2vpnPwBindType):
    """Custom type vpwsBindCfgPwBindType based on L2vpnPwBindType"""
    defaultValue = 1


_VpwsBindCfgPwBindType_Type.__name__ = "L2vpnPwBindType"
_VpwsBindCfgPwBindType_Object = MibTableColumn
vpwsBindCfgPwBindType = _VpwsBindCfgPwBindType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 3, 1, 7),
    _VpwsBindCfgPwBindType_Type()
)
vpwsBindCfgPwBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsBindCfgPwBindType.setStatus("current")


class _VpwsBindCfgPwSetIndex_Type(Unsigned32):
    """Custom type vpwsBindCfgPwSetIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1073741823),
    )


_VpwsBindCfgPwSetIndex_Type.__name__ = "Unsigned32"
_VpwsBindCfgPwSetIndex_Object = MibTableColumn
vpwsBindCfgPwSetIndex = _VpwsBindCfgPwSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 3, 1, 8),
    _VpwsBindCfgPwSetIndex_Type()
)
vpwsBindCfgPwSetIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsBindCfgPwSetIndex.setStatus("current")


class _VpwsBindCfgRemoteSiteID_Type(L2vpnVeIdOrZero):
    """Custom type vpwsBindCfgRemoteSiteID based on L2vpnVeIdOrZero"""
    defaultValue = 0


_VpwsBindCfgRemoteSiteID_Type.__name__ = "L2vpnVeIdOrZero"
_VpwsBindCfgRemoteSiteID_Object = MibTableColumn
vpwsBindCfgRemoteSiteID = _VpwsBindCfgRemoteSiteID_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 3, 1, 9),
    _VpwsBindCfgRemoteSiteID_Type()
)
vpwsBindCfgRemoteSiteID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsBindCfgRemoteSiteID.setStatus("current")


class _VpwsBindCfgLclSwitchIfIndex_Type(InterfaceIndexOrZero):
    """Custom type vpwsBindCfgLclSwitchIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_VpwsBindCfgLclSwitchIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_VpwsBindCfgLclSwitchIfIndex_Object = MibTableColumn
vpwsBindCfgLclSwitchIfIndex = _VpwsBindCfgLclSwitchIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 3, 1, 10),
    _VpwsBindCfgLclSwitchIfIndex_Type()
)
vpwsBindCfgLclSwitchIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpwsBindCfgLclSwitchIfIndex.setStatus("current")
_VpwsBindTable_Object = MibTable
vpwsBindTable = _VpwsBindTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 4)
)
if mibBuilder.loadTexts:
    vpwsBindTable.setStatus("current")
_VpwsBindEntry_Object = MibTableRow
vpwsBindEntry = _VpwsBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 4, 1)
)
vpwsBindEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "DC-VPWS-MIB", "vpwsIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vpwsBindEntry.setStatus("current")
_VpwsBindOperStatus_Type = NpgOperStatus
_VpwsBindOperStatus_Object = MibTableColumn
vpwsBindOperStatus = _VpwsBindOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 4, 1, 4),
    _VpwsBindOperStatus_Type()
)
vpwsBindOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsBindOperStatus.setStatus("current")
_VpwsBindPwBindType_Type = L2vpnPwBindType
_VpwsBindPwBindType_Object = MibTableColumn
vpwsBindPwBindType = _VpwsBindPwBindType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 4, 1, 5),
    _VpwsBindPwBindType_Type()
)
vpwsBindPwBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsBindPwBindType.setStatus("current")
_VpwsBindPwSetIndex_Type = NumericIndex
_VpwsBindPwSetIndex_Object = MibTableColumn
vpwsBindPwSetIndex = _VpwsBindPwSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 4, 1, 6),
    _VpwsBindPwSetIndex_Type()
)
vpwsBindPwSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsBindPwSetIndex.setStatus("current")
_VpwsBindPwIfIndex_Type = InterfaceIndex
_VpwsBindPwIfIndex_Object = MibTableColumn
vpwsBindPwIfIndex = _VpwsBindPwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 4, 1, 7),
    _VpwsBindPwIfIndex_Type()
)
vpwsBindPwIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsBindPwIfIndex.setStatus("current")
_VpwsBindLocalSiteID_Type = L2vpnVeIdOrZero
_VpwsBindLocalSiteID_Object = MibTableColumn
vpwsBindLocalSiteID = _VpwsBindLocalSiteID_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 4, 1, 8),
    _VpwsBindLocalSiteID_Type()
)
vpwsBindLocalSiteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsBindLocalSiteID.setStatus("current")
_VpwsBindRemoteSiteID_Type = L2vpnVeIdOrZero
_VpwsBindRemoteSiteID_Object = MibTableColumn
vpwsBindRemoteSiteID = _VpwsBindRemoteSiteID_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 4, 1, 9),
    _VpwsBindRemoteSiteID_Type()
)
vpwsBindRemoteSiteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsBindRemoteSiteID.setStatus("current")
_VpwsBindLclSwitchIfIndex_Type = InterfaceIndex
_VpwsBindLclSwitchIfIndex_Object = MibTableColumn
vpwsBindLclSwitchIfIndex = _VpwsBindLclSwitchIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 4, 1, 10),
    _VpwsBindLclSwitchIfIndex_Type()
)
vpwsBindLclSwitchIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsBindLclSwitchIfIndex.setStatus("current")
_VpwsBindRemoteRD_Type = BgpRouteDistinguisher
_VpwsBindRemoteRD_Object = MibTableColumn
vpwsBindRemoteRD = _VpwsBindRemoteRD_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 4, 1, 11),
    _VpwsBindRemoteRD_Type()
)
vpwsBindRemoteRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsBindRemoteRD.setStatus("current")
_VpwsBindRemoteAddrType_Type = InetAddressType
_VpwsBindRemoteAddrType_Object = MibTableColumn
vpwsBindRemoteAddrType = _VpwsBindRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 4, 1, 12),
    _VpwsBindRemoteAddrType_Type()
)
vpwsBindRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsBindRemoteAddrType.setStatus("current")
_VpwsBindRemoteAddr_Type = InetAddress
_VpwsBindRemoteAddr_Object = MibTableColumn
vpwsBindRemoteAddr = _VpwsBindRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 1, 4, 1, 13),
    _VpwsBindRemoteAddr_Type()
)
vpwsBindRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwsBindRemoteAddr.setStatus("current")
_VpwsConformance_ObjectIdentity = ObjectIdentity
vpwsConformance = _VpwsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 2)
)
_VpwsCompliances_ObjectIdentity = ObjectIdentity
vpwsCompliances = _VpwsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 2, 1)
)
_VpwsGroups_ObjectIdentity = ObjectIdentity
vpwsGroups = _VpwsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 2, 2)
)

# Managed Objects groups

vpwsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 2, 2, 1)
)
vpwsBaseGroup.setObjects(
      *(("DC-VPWS-MIB", "vpwsConfigRowStatus"),
        ("DC-VPWS-MIB", "vpwsConfigAdminStatus"),
        ("DC-VPWS-MIB", "vpwsConfigOperStatus"),
        ("DC-VPWS-MIB", "vpwsConfigName"),
        ("DC-VPWS-MIB", "vpwsConfigDescr"),
        ("DC-VPWS-MIB", "vpwsConfigADType"),
        ("DC-VPWS-MIB", "vpwsConfigSigType"),
        ("DC-VPWS-MIB", "vpwsConfigPwEncapType"),
        ("DC-VPWS-MIB", "vpwsConfigMtu"),
        ("DC-VPWS-MIB", "vpwsConfigControlWord"),
        ("DC-VPWS-MIB", "vpwsConfigSeqDelivery"),
        ("DC-VPWS-MIB", "vpwsStatusOperStatus"),
        ("DC-VPWS-MIB", "vpwsStatusVcCount"),
        ("DC-VPWS-MIB", "vpwsStatusDesignatedForwarder"),
        ("DC-VPWS-MIB", "vpwsBindCfgRowStatus"),
        ("DC-VPWS-MIB", "vpwsBindCfgAdminStatus"),
        ("DC-VPWS-MIB", "vpwsBindCfgOperStatus"),
        ("DC-VPWS-MIB", "vpwsBindCfgVpwsIndex"),
        ("DC-VPWS-MIB", "vpwsBindCfgPwBindType"),
        ("DC-VPWS-MIB", "vpwsBindCfgPwSetIndex"),
        ("DC-VPWS-MIB", "vpwsBindOperStatus"),
        ("DC-VPWS-MIB", "vpwsBindPwBindType"),
        ("DC-VPWS-MIB", "vpwsBindPwSetIndex"),
        ("DC-VPWS-MIB", "vpwsBindPwIfIndex"),
        ("DC-VPWS-MIB", "vpwsBindLclSwitchIfIndex"),
        ("DC-VPWS-MIB", "vpwsBindRemoteRD"),
        ("DC-VPWS-MIB", "vpwsBindRemoteAddrType"),
        ("DC-VPWS-MIB", "vpwsBindRemoteAddr"))
)
if mibBuilder.loadTexts:
    vpwsBaseGroup.setStatus("current")

vpwsDoubleSidedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 2, 2, 2)
)
vpwsDoubleSidedGroup.setObjects(
      *(("DC-VPWS-MIB", "vpwsBindCfgPwSetIndex"),
        ("DC-VPWS-MIB", "vpwsBindCfgLclSwitchIfIndex"))
)
if mibBuilder.loadTexts:
    vpwsDoubleSidedGroup.setStatus("current")

vpwsBgpADGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 2, 2, 3)
)
vpwsBgpADGroup.setObjects(
      *(("DC-VPWS-MIB", "vpwsConfigRouteDistinguisher"),
        ("DC-VPWS-MIB", "vpwsConfigVpnId"),
        ("DC-VPWS-MIB", "vpwsConfigLocalSiteID"),
        ("DC-VPWS-MIB", "vpwsConfigLocalPreference"),
        ("DC-VPWS-MIB", "vpwsConfigLabelBlockSize"),
        ("DC-VPWS-MIB", "vpwsConfigIncludeCSV"),
        ("DC-VPWS-MIB", "vpwsConfigIgnoreMtuMismatch"),
        ("DC-VPWS-MIB", "vpwsConfigIgnoreEncapsMismatch"),
        ("DC-VPWS-MIB", "vpwsBindCfgRemoteSiteID"),
        ("DC-VPWS-MIB", "vpwsBindLocalSiteID"),
        ("DC-VPWS-MIB", "vpwsBindRemoteSiteID"))
)
if mibBuilder.loadTexts:
    vpwsBgpADGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vpwsFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 2, 1, 1)
)
vpwsFullCompliance.setObjects(
      *(("DC-VPWS-MIB", "vpwsBaseGroup"),
        ("DC-VPWS-MIB", "vpwsDoubleSidedGroup"),
        ("DC-VPWS-MIB", "vpwsBgpADGroup"))
)
if mibBuilder.loadTexts:
    vpwsFullCompliance.setStatus(
        "current"
    )

vpwsDoubleSidedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 2, 1, 2)
)
vpwsDoubleSidedCompliance.setObjects(
      *(("DC-VPWS-MIB", "vpwsBaseGroup"),
        ("DC-VPWS-MIB", "vpwsDoubleSidedGroup"))
)
if mibBuilder.loadTexts:
    vpwsDoubleSidedCompliance.setStatus(
        "current"
    )

vpwsBgpADCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 19, 2, 1, 3)
)
vpwsBgpADCompliance.setObjects(
      *(("DC-VPWS-MIB", "vpwsBaseGroup"),
        ("DC-VPWS-MIB", "vpwsBgpADGroup"))
)
if mibBuilder.loadTexts:
    vpwsBgpADCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-VPWS-MIB",
    **{"nbase": nbase,
       "opx": opx,
       "vpwsMib": vpwsMib,
       "vpwsObjects": vpwsObjects,
       "vpwsConfigTable": vpwsConfigTable,
       "vpwsConfigEntry": vpwsConfigEntry,
       "vpwsIndex": vpwsIndex,
       "vpwsConfigRowStatus": vpwsConfigRowStatus,
       "vpwsConfigAdminStatus": vpwsConfigAdminStatus,
       "vpwsConfigOperStatus": vpwsConfigOperStatus,
       "vpwsConfigName": vpwsConfigName,
       "vpwsConfigDescr": vpwsConfigDescr,
       "vpwsConfigADType": vpwsConfigADType,
       "vpwsConfigSigType": vpwsConfigSigType,
       "vpwsConfigPwEncapType": vpwsConfigPwEncapType,
       "vpwsConfigMtu": vpwsConfigMtu,
       "vpwsConfigControlWord": vpwsConfigControlWord,
       "vpwsConfigSeqDelivery": vpwsConfigSeqDelivery,
       "vpwsConfigRouteDistinguisher": vpwsConfigRouteDistinguisher,
       "vpwsConfigVpnId": vpwsConfigVpnId,
       "vpwsConfigLocalSiteID": vpwsConfigLocalSiteID,
       "vpwsConfigLocalPreference": vpwsConfigLocalPreference,
       "vpwsConfigLabelBlockSize": vpwsConfigLabelBlockSize,
       "vpwsConfigIncludeCSV": vpwsConfigIncludeCSV,
       "vpwsConfigIgnoreMtuMismatch": vpwsConfigIgnoreMtuMismatch,
       "vpwsConfigIgnoreEncapsMismatch": vpwsConfigIgnoreEncapsMismatch,
       "vpwsStatusTable": vpwsStatusTable,
       "vpwsStatusEntry": vpwsStatusEntry,
       "vpwsStatusOperStatus": vpwsStatusOperStatus,
       "vpwsStatusVcCount": vpwsStatusVcCount,
       "vpwsStatusDesignatedForwarder": vpwsStatusDesignatedForwarder,
       "vpwsBindCfgTable": vpwsBindCfgTable,
       "vpwsBindCfgEntry": vpwsBindCfgEntry,
       "vpwsBindCfgRowStatus": vpwsBindCfgRowStatus,
       "vpwsBindCfgAdminStatus": vpwsBindCfgAdminStatus,
       "vpwsBindCfgOperStatus": vpwsBindCfgOperStatus,
       "vpwsBindCfgVpwsIndex": vpwsBindCfgVpwsIndex,
       "vpwsBindCfgPwBindType": vpwsBindCfgPwBindType,
       "vpwsBindCfgPwSetIndex": vpwsBindCfgPwSetIndex,
       "vpwsBindCfgRemoteSiteID": vpwsBindCfgRemoteSiteID,
       "vpwsBindCfgLclSwitchIfIndex": vpwsBindCfgLclSwitchIfIndex,
       "vpwsBindTable": vpwsBindTable,
       "vpwsBindEntry": vpwsBindEntry,
       "vpwsBindOperStatus": vpwsBindOperStatus,
       "vpwsBindPwBindType": vpwsBindPwBindType,
       "vpwsBindPwSetIndex": vpwsBindPwSetIndex,
       "vpwsBindPwIfIndex": vpwsBindPwIfIndex,
       "vpwsBindLocalSiteID": vpwsBindLocalSiteID,
       "vpwsBindRemoteSiteID": vpwsBindRemoteSiteID,
       "vpwsBindLclSwitchIfIndex": vpwsBindLclSwitchIfIndex,
       "vpwsBindRemoteRD": vpwsBindRemoteRD,
       "vpwsBindRemoteAddrType": vpwsBindRemoteAddrType,
       "vpwsBindRemoteAddr": vpwsBindRemoteAddr,
       "vpwsConformance": vpwsConformance,
       "vpwsCompliances": vpwsCompliances,
       "vpwsFullCompliance": vpwsFullCompliance,
       "vpwsDoubleSidedCompliance": vpwsDoubleSidedCompliance,
       "vpwsBgpADCompliance": vpwsBgpADCompliance,
       "vpwsGroups": vpwsGroups,
       "vpwsBaseGroup": vpwsBaseGroup,
       "vpwsDoubleSidedGroup": vpwsDoubleSidedGroup,
       "vpwsBgpADGroup": vpwsBgpADGroup}
)
