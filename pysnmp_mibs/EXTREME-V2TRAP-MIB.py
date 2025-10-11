# SNMP MIB module (EXTREME-V2TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/extreme/EXTREME-V2TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:16:56 2025
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

(bgpPeerRemoteAddr,) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgpPeerRemoteAddr")

(ClientAuthType,
 extremenetworks) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "ClientAuthType",
    "extremenetworks")

(extremeBgp4V2PeerLocalAddr,
 extremeBgp4V2PeerLocalAddrType,
 extremeBgp4V2PeerRemoteAddr,
 extremeBgp4V2PeerRemoteAddrType) = mibBuilder.importSymbols(
    "EXTREME-BGP4V2-MIB",
    "extremeBgp4V2PeerLocalAddr",
    "extremeBgp4V2PeerLocalAddrType",
    "extremeBgp4V2PeerRemoteAddr",
    "extremeBgp4V2PeerRemoteAddrType")

(EapsRingPort,
 extremeEapsFailedFlag,
 extremeEapsLastConfigurationChange,
 extremeEapsLastStatusChange,
 extremeEapsMode,
 extremeEapsName,
 extremeEapsPrevState,
 extremeEapsPrimaryStatus,
 extremeEapsSecondaryStatus,
 extremeEapsSharedPortIfIndex,
 extremeEapsSharedPortLinkId,
 extremeEapsSharedPortNbrStatus,
 extremeEapsSharedPortRootBlockerId,
 extremeEapsSharedPortRootBlockerStatus,
 extremeEapsSharedPortState,
 extremeEapsState,
 extremeEapsStatusTrapCount) = mibBuilder.importSymbols(
    "EXTREME-EAPS-MIB",
    "EapsRingPort",
    "extremeEapsFailedFlag",
    "extremeEapsLastConfigurationChange",
    "extremeEapsLastStatusChange",
    "extremeEapsMode",
    "extremeEapsName",
    "extremeEapsPrevState",
    "extremeEapsPrimaryStatus",
    "extremeEapsSecondaryStatus",
    "extremeEapsSharedPortIfIndex",
    "extremeEapsSharedPortLinkId",
    "extremeEapsSharedPortNbrStatus",
    "extremeEapsSharedPortRootBlockerId",
    "extremeEapsSharedPortRootBlockerStatus",
    "extremeEapsSharedPortState",
    "extremeEapsState",
    "extremeEapsStatusTrapCount")

(extremeEdpEntryAge,
 extremeEdpNeighborId,
 extremeEdpPortIfIndex) = mibBuilder.importSymbols(
    "EXTREME-EDP-MIB",
    "extremeEdpEntryAge",
    "extremeEdpNeighborId",
    "extremeEdpPortIfIndex")

(extremeEsrpGroup,
 extremeEsrpState) = mibBuilder.importSymbols(
    "EXTREME-ESRP-MIB",
    "extremeEsrpGroup",
    "extremeEsrpState")

(extremeLacpGroup,
 extremeLacpMemberPort) = mibBuilder.importSymbols(
    "EXTREME-LACP-MIB",
    "extremeLacpGroup",
    "extremeLacpMemberPort")

(extremeNPModuleProcessorState,) = mibBuilder.importSymbols(
    "EXTREME-NP-MIB",
    "extremeNPModuleProcessorState")

(extremePethSlotMainPseIndex,
 extremePethSlotPSUActive) = mibBuilder.importSymbols(
    "EXTREME-POE-MIB",
    "extremePethSlotMainPseIndex",
    "extremePethSlotPSUActive")

(extremeIQosProfileIndex,) = mibBuilder.importSymbols(
    "EXTREME-QOS-MIB",
    "extremeIQosProfileIndex")

(extremeCpuAggregateUtilization,
 extremeCpuTaskUtilPair,
 extremeCpuUtilRisingThreshold,
 extremeCurrentTemperature,
 extremeFanNumber,
 extremeHealthCheckAction,
 extremeHealthCheckErrorType,
 extremeHealthCheckMaxRetries,
 extremeMasterMSMSlot,
 extremeMsmFailoverCause,
 extremePowerSupplyNumber,
 extremeSlotModuleConfiguredType,
 extremeSlotModuleInsertedType,
 extremeSlotModuleState,
 extremeSlotNumber) = mibBuilder.importSymbols(
    "EXTREME-SYSTEM-MIB",
    "extremeCpuAggregateUtilization",
    "extremeCpuTaskUtilPair",
    "extremeCpuUtilRisingThreshold",
    "extremeCurrentTemperature",
    "extremeFanNumber",
    "extremeHealthCheckAction",
    "extremeHealthCheckErrorType",
    "extremeHealthCheckMaxRetries",
    "extremeMasterMSMSlot",
    "extremeMsmFailoverCause",
    "extremePowerSupplyNumber",
    "extremeSlotModuleConfiguredType",
    "extremeSlotModuleInsertedType",
    "extremeSlotModuleState",
    "extremeSlotNumber")

(extremeVlanIfDescr,
 extremeVlanIfIndex) = mibBuilder.importSymbols(
    "EXTREME-VLAN-MIB",
    "extremeVlanIfDescr",
    "extremeVlanIfIndex")

(ifAlias,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias",
    "ifDescr",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysUpTime")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

extremeV2Traps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeV1Traps_ObjectIdentity = ObjectIdentity
extremeV1Traps = _ExtremeV1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 0)
)
_ExtremeCoreSCTraps_ObjectIdentity = ObjectIdentity
extremeCoreSCTraps = _ExtremeCoreSCTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1)
)
_ExtremeCoreSCTrapPrefix_ObjectIdentity = ObjectIdentity
extremeCoreSCTrapPrefix = _ExtremeCoreSCTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0)
)


class _ExtremeRateLimitExceededTrapType_Type(Integer32):
    """Custom type extremeRateLimitExceededTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exceededCIR", 1),
          ("droppedBytes", 2))
    )


_ExtremeRateLimitExceededTrapType_Type.__name__ = "Integer32"
_ExtremeRateLimitExceededTrapType_Object = MibScalar
extremeRateLimitExceededTrapType = _ExtremeRateLimitExceededTrapType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 7, 1),
    _ExtremeRateLimitExceededTrapType_Type()
)
extremeRateLimitExceededTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeRateLimitExceededTrapType.setStatus("current")


class _ExtremeRateLimitExceededTrapIndicator_Type(Integer32):
    """Custom type extremeRateLimitExceededTrapIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("set", 1))
    )


_ExtremeRateLimitExceededTrapIndicator_Type.__name__ = "Integer32"
_ExtremeRateLimitExceededTrapIndicator_Object = MibScalar
extremeRateLimitExceededTrapIndicator = _ExtremeRateLimitExceededTrapIndicator_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 7, 2),
    _ExtremeRateLimitExceededTrapIndicator_Type()
)
extremeRateLimitExceededTrapIndicator.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeRateLimitExceededTrapIndicator.setStatus("current")
_ExtremeExceededByteCount_Type = Integer32
_ExtremeExceededByteCount_Object = MibScalar
extremeExceededByteCount = _ExtremeExceededByteCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 7, 4),
    _ExtremeExceededByteCount_Type()
)
extremeExceededByteCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeExceededByteCount.setStatus("current")
_ExtremeBgpTraps_ObjectIdentity = ObjectIdentity
extremeBgpTraps = _ExtremeBgpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 2)
)
_ExtremeBgpTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeBgpTrapsPrefix = _ExtremeBgpTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 2, 0)
)
_ExtremeSecurityTraps_ObjectIdentity = ObjectIdentity
extremeSecurityTraps = _ExtremeSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3)
)
_ExtremeSecurityTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeSecurityTrapsPrefix = _ExtremeSecurityTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0)
)
_ExtremeMacSecurityVlanIfIndex_Type = Integer32
_ExtremeMacSecurityVlanIfIndex_Object = MibScalar
extremeMacSecurityVlanIfIndex = _ExtremeMacSecurityVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 1),
    _ExtremeMacSecurityVlanIfIndex_Type()
)
extremeMacSecurityVlanIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMacSecurityVlanIfIndex.setStatus("current")


class _ExtremeMacSecurityVlanDescr_Type(DisplayString):
    """Custom type extremeMacSecurityVlanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeMacSecurityVlanDescr_Type.__name__ = "DisplayString"
_ExtremeMacSecurityVlanDescr_Object = MibScalar
extremeMacSecurityVlanDescr = _ExtremeMacSecurityVlanDescr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 2),
    _ExtremeMacSecurityVlanDescr_Type()
)
extremeMacSecurityVlanDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMacSecurityVlanDescr.setStatus("current")
_ExtremeMacSecurityMacAddress_Type = MacAddress
_ExtremeMacSecurityMacAddress_Object = MibScalar
extremeMacSecurityMacAddress = _ExtremeMacSecurityMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 3),
    _ExtremeMacSecurityMacAddress_Type()
)
extremeMacSecurityMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMacSecurityMacAddress.setStatus("current")
_ExtremeMacSecurityPortIfIndex_Type = Integer32
_ExtremeMacSecurityPortIfIndex_Object = MibScalar
extremeMacSecurityPortIfIndex = _ExtremeMacSecurityPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 4),
    _ExtremeMacSecurityPortIfIndex_Type()
)
extremeMacSecurityPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMacSecurityPortIfIndex.setStatus("current")
_ExtremeMacSecurityVlanId_Type = Integer32
_ExtremeMacSecurityVlanId_Object = MibScalar
extremeMacSecurityVlanId = _ExtremeMacSecurityVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 5),
    _ExtremeMacSecurityVlanId_Type()
)
extremeMacSecurityVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMacSecurityVlanId.setStatus("current")
_ExtremeNetloginStationMac_Type = MacAddress
_ExtremeNetloginStationMac_Object = MibScalar
extremeNetloginStationMac = _ExtremeNetloginStationMac_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 6),
    _ExtremeNetloginStationMac_Type()
)
extremeNetloginStationMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginStationMac.setStatus("current")
_ExtremeNetloginStationAddr_Type = IpAddress
_ExtremeNetloginStationAddr_Object = MibScalar
extremeNetloginStationAddr = _ExtremeNetloginStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 7),
    _ExtremeNetloginStationAddr_Type()
)
extremeNetloginStationAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginStationAddr.setStatus("current")
_ExtremeNetloginPortIfIndex_Type = Integer32
_ExtremeNetloginPortIfIndex_Object = MibScalar
extremeNetloginPortIfIndex = _ExtremeNetloginPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 8),
    _ExtremeNetloginPortIfIndex_Type()
)
extremeNetloginPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginPortIfIndex.setStatus("current")
_ExtremeNetloginAuthType_Type = ClientAuthType
_ExtremeNetloginAuthType_Object = MibScalar
extremeNetloginAuthType = _ExtremeNetloginAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 9),
    _ExtremeNetloginAuthType_Type()
)
extremeNetloginAuthType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginAuthType.setStatus("current")
_ExtremeNetloginSystemTime_Type = TimeStamp
_ExtremeNetloginSystemTime_Object = MibScalar
extremeNetloginSystemTime = _ExtremeNetloginSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 10),
    _ExtremeNetloginSystemTime_Type()
)
extremeNetloginSystemTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginSystemTime.setStatus("current")


class _ExtremeNetloginUser_Type(DisplayString):
    """Custom type extremeNetloginUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ExtremeNetloginUser_Type.__name__ = "DisplayString"
_ExtremeNetloginUser_Object = MibScalar
extremeNetloginUser = _ExtremeNetloginUser_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 11),
    _ExtremeNetloginUser_Type()
)
extremeNetloginUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginUser.setStatus("current")


class _ExtremeNetloginSrcVlan_Type(DisplayString):
    """Custom type extremeNetloginSrcVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ExtremeNetloginSrcVlan_Type.__name__ = "DisplayString"
_ExtremeNetloginSrcVlan_Object = MibScalar
extremeNetloginSrcVlan = _ExtremeNetloginSrcVlan_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 12),
    _ExtremeNetloginSrcVlan_Type()
)
extremeNetloginSrcVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginSrcVlan.setStatus("current")


class _ExtremeNetloginDestVlan_Type(DisplayString):
    """Custom type extremeNetloginDestVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ExtremeNetloginDestVlan_Type.__name__ = "DisplayString"
_ExtremeNetloginDestVlan_Object = MibScalar
extremeNetloginDestVlan = _ExtremeNetloginDestVlan_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 13),
    _ExtremeNetloginDestVlan_Type()
)
extremeNetloginDestVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginDestVlan.setStatus("current")


class _ExtremeNetloginSessionStatus_Type(Integer32):
    """Custom type extremeNetloginSessionStatus based on Integer32"""
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("sessionReset", 2),
          ("fDBAgingInitiatedLogout", 3),
          ("userInitiatedLogout", 4),
          ("sessionRefreshInitiatedLogout", 5),
          ("authenticationFailure", 6),
          ("remoteAuthenticationServerFailure", 7),
          ("fDBDeleteInitiatedLogout", 8),
          ("linkDownInitiatedLogout", 9),
          ("reauthenticationFailure", 10),
          ("successWithRestrictedAccess", 11),
          ("successWithTimeLimitedAccess", 12),
          ("frameworkInitiatedLogout", 13),
          ("l2ProtoInitiatedLogout", 14),
          ("preferredProtocolInitiatedLogout", 15))
    )


_ExtremeNetloginSessionStatus_Type.__name__ = "Integer32"
_ExtremeNetloginSessionStatus_Object = MibScalar
extremeNetloginSessionStatus = _ExtremeNetloginSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 14),
    _ExtremeNetloginSessionStatus_Type()
)
extremeNetloginSessionStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginSessionStatus.setStatus("current")
_ExtremeArpSecurityVlanIfIndex_Type = Integer32
_ExtremeArpSecurityVlanIfIndex_Object = MibScalar
extremeArpSecurityVlanIfIndex = _ExtremeArpSecurityVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 15),
    _ExtremeArpSecurityVlanIfIndex_Type()
)
extremeArpSecurityVlanIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeArpSecurityVlanIfIndex.setStatus("current")


class _ExtremeArpSecurityVlanDescr_Type(DisplayString):
    """Custom type extremeArpSecurityVlanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeArpSecurityVlanDescr_Type.__name__ = "DisplayString"
_ExtremeArpSecurityVlanDescr_Object = MibScalar
extremeArpSecurityVlanDescr = _ExtremeArpSecurityVlanDescr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 16),
    _ExtremeArpSecurityVlanDescr_Type()
)
extremeArpSecurityVlanDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeArpSecurityVlanDescr.setStatus("current")
_ExtremeArpSecurityPortIfIndex_Type = Integer32
_ExtremeArpSecurityPortIfIndex_Object = MibScalar
extremeArpSecurityPortIfIndex = _ExtremeArpSecurityPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 17),
    _ExtremeArpSecurityPortIfIndex_Type()
)
extremeArpSecurityPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeArpSecurityPortIfIndex.setStatus("current")
_ExtremeArpSecurityIpAddr_Type = IpAddress
_ExtremeArpSecurityIpAddr_Object = MibScalar
extremeArpSecurityIpAddr = _ExtremeArpSecurityIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 18),
    _ExtremeArpSecurityIpAddr_Type()
)
extremeArpSecurityIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeArpSecurityIpAddr.setStatus("current")
_ExtremeArpSecurityMacAddress_Type = MacAddress
_ExtremeArpSecurityMacAddress_Object = MibScalar
extremeArpSecurityMacAddress = _ExtremeArpSecurityMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 19),
    _ExtremeArpSecurityMacAddress_Type()
)
extremeArpSecurityMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeArpSecurityMacAddress.setStatus("current")


class _ExtremeNetloginAuthDataBase_Type(DisplayString):
    """Custom type extremeNetloginAuthDataBase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ExtremeNetloginAuthDataBase_Type.__name__ = "DisplayString"
_ExtremeNetloginAuthDataBase_Object = MibScalar
extremeNetloginAuthDataBase = _ExtremeNetloginAuthDataBase_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 20),
    _ExtremeNetloginAuthDataBase_Type()
)
extremeNetloginAuthDataBase.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginAuthDataBase.setStatus("current")


class _ExtremeNetloginMoveFromVlanList_Type(DisplayString):
    """Custom type extremeNetloginMoveFromVlanList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ExtremeNetloginMoveFromVlanList_Type.__name__ = "DisplayString"
_ExtremeNetloginMoveFromVlanList_Object = MibScalar
extremeNetloginMoveFromVlanList = _ExtremeNetloginMoveFromVlanList_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 21),
    _ExtremeNetloginMoveFromVlanList_Type()
)
extremeNetloginMoveFromVlanList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginMoveFromVlanList.setStatus("current")


class _ExtremeNetloginMoveToVlanList_Type(DisplayString):
    """Custom type extremeNetloginMoveToVlanList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ExtremeNetloginMoveToVlanList_Type.__name__ = "DisplayString"
_ExtremeNetloginMoveToVlanList_Object = MibScalar
extremeNetloginMoveToVlanList = _ExtremeNetloginMoveToVlanList_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 22),
    _ExtremeNetloginMoveToVlanList_Type()
)
extremeNetloginMoveToVlanList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginMoveToVlanList.setStatus("current")
_ExtremeNMSTraps_ObjectIdentity = ObjectIdentity
extremeNMSTraps = _ExtremeNMSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 4)
)
_ExtremeNMSTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeNMSTrapsPrefix = _ExtremeNMSTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 4, 0)
)
_ExtremeNMSDeviceAddress_Type = IpAddress
_ExtremeNMSDeviceAddress_Object = MibScalar
extremeNMSDeviceAddress = _ExtremeNMSDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 4, 1),
    _ExtremeNMSDeviceAddress_Type()
)
extremeNMSDeviceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNMSDeviceAddress.setStatus("current")
_ExtremeElrpTraps_ObjectIdentity = ObjectIdentity
extremeElrpTraps = _ExtremeElrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 6)
)
_ExtremeElrpTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeElrpTrapsPrefix = _ExtremeElrpTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 6, 0)
)
_ExtremeEapsTraps_ObjectIdentity = ObjectIdentity
extremeEapsTraps = _ExtremeEapsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7)
)
_ExtremeEapsTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeEapsTrapsPrefix = _ExtremeEapsTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0)
)
_ExtremeBgpM2Traps_ObjectIdentity = ObjectIdentity
extremeBgpM2Traps = _ExtremeBgpM2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 8)
)
_ExtremeBgpM2TrapsPrefix_ObjectIdentity = ObjectIdentity
extremeBgpM2TrapsPrefix = _ExtremeBgpM2TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 8, 0)
)
_ExtremeEapsSharedLinkTraps_ObjectIdentity = ObjectIdentity
extremeEapsSharedLinkTraps = _ExtremeEapsSharedLinkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9)
)
_ExtremeEapsSharedLinkTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeEapsSharedLinkTrapsPrefix = _ExtremeEapsSharedLinkTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9, 0)
)
_ExtremeSegmentPort_Type = EapsRingPort
_ExtremeSegmentPort_Object = MibScalar
extremeSegmentPort = _ExtremeSegmentPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9, 1),
    _ExtremeSegmentPort_Type()
)
extremeSegmentPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeSegmentPort.setStatus("current")
_ExtremeSharedPort_Type = EapsRingPort
_ExtremeSharedPort_Object = MibScalar
extremeSharedPort = _ExtremeSharedPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9, 2),
    _ExtremeSharedPort_Type()
)
extremeSharedPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeSharedPort.setStatus("current")
_ExtremePethTraps_ObjectIdentity = ObjectIdentity
extremePethTraps = _ExtremePethTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 12)
)
_ExtremePethNotificationPrefix_ObjectIdentity = ObjectIdentity
extremePethNotificationPrefix = _ExtremePethNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 12, 0)
)
_ExtremeLacpTraps_ObjectIdentity = ObjectIdentity
extremeLacpTraps = _ExtremeLacpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 13)
)
_ExtremeLacpNotificationPrefix_ObjectIdentity = ObjectIdentity
extremeLacpNotificationPrefix = _ExtremeLacpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 13, 0)
)

# Managed Objects groups


# Notification objects

extremeOverheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 6)
)
extremeOverheat.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeCurrentTemperature"))
)
if mibBuilder.loadTexts:
    extremeOverheat.setStatus(
        "current"
    )

extremeFanfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 7)
)
extremeFanfailed.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeFanNumber"))
)
if mibBuilder.loadTexts:
    extremeFanfailed.setStatus(
        "current"
    )

extremeFanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 8)
)
extremeFanOK.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeFanNumber"))
)
if mibBuilder.loadTexts:
    extremeFanOK.setStatus(
        "current"
    )

extremeInvalidLoginAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 9)
)
extremeInvalidLoginAttempt.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    extremeInvalidLoginAttempt.setStatus(
        "current"
    )

extremePowerSupplyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 10)
)
extremePowerSupplyFail.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremePowerSupplyNumber"))
)
if mibBuilder.loadTexts:
    extremePowerSupplyFail.setStatus(
        "current"
    )

extremePowerSupplyGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 11)
)
extremePowerSupplyGood.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremePowerSupplyNumber"))
)
if mibBuilder.loadTexts:
    extremePowerSupplyGood.setStatus(
        "current"
    )

extremeSmartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 14)
)
extremeSmartTrap.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    extremeSmartTrap.setStatus(
        "current"
    )

extremeModuleStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 15)
)
extremeModuleStateChanged.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("EXTREME-SYSTEM-MIB", "extremeSlotNumber"),
        ("EXTREME-SYSTEM-MIB", "extremeSlotModuleConfiguredType"),
        ("EXTREME-SYSTEM-MIB", "extremeSlotModuleInsertedType"),
        ("EXTREME-SYSTEM-MIB", "extremeSlotModuleState"))
)
if mibBuilder.loadTexts:
    extremeModuleStateChanged.setStatus(
        "current"
    )

extremeEdpNeighborAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 20)
)
extremeEdpNeighborAdded.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("EXTREME-EDP-MIB", "extremeEdpPortIfIndex"),
        ("EXTREME-EDP-MIB", "extremeEdpNeighborId"),
        ("EXTREME-EDP-MIB", "extremeEdpEntryAge"),
        ("IF-MIB", "ifAlias"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    extremeEdpNeighborAdded.setStatus(
        "current"
    )

extremeEdpNeighborRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 21)
)
extremeEdpNeighborRemoved.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("EXTREME-EDP-MIB", "extremeEdpPortIfIndex"),
        ("EXTREME-EDP-MIB", "extremeEdpNeighborId"),
        ("EXTREME-EDP-MIB", "extremeEdpEntryAge"),
        ("IF-MIB", "ifAlias"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    extremeEdpNeighborRemoved.setStatus(
        "current"
    )

extremeHealthCheckFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 1)
)
extremeHealthCheckFailed.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeSlotNumber"),
        ("EXTREME-SYSTEM-MIB", "extremeHealthCheckErrorType"),
        ("EXTREME-SYSTEM-MIB", "extremeHealthCheckAction"),
        ("EXTREME-SYSTEM-MIB", "extremeHealthCheckMaxRetries"))
)
if mibBuilder.loadTexts:
    extremeHealthCheckFailed.setStatus(
        "current"
    )

extremeCpuUtilizationRisingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 2)
)
extremeCpuUtilizationRisingTrap.setObjects(
      *(("EXTREME-SYSTEM-MIB", "extremeCpuTaskUtilPair"),
        ("EXTREME-SYSTEM-MIB", "extremeCpuAggregateUtilization"),
        ("EXTREME-SYSTEM-MIB", "extremeCpuUtilRisingThreshold"))
)
if mibBuilder.loadTexts:
    extremeCpuUtilizationRisingTrap.setStatus(
        "current"
    )

extremeCpuUtilizationFallingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 3)
)
extremeCpuUtilizationFallingTrap.setObjects(
      *(("EXTREME-SYSTEM-MIB", "extremeCpuTaskUtilPair"),
        ("EXTREME-SYSTEM-MIB", "extremeCpuAggregateUtilization"),
        ("EXTREME-SYSTEM-MIB", "extremeCpuUtilRisingThreshold"))
)
if mibBuilder.loadTexts:
    extremeCpuUtilizationFallingTrap.setStatus(
        "current"
    )

extremeProcessorStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 4)
)
extremeProcessorStateChangeTrap.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeSlotNumber"),
        ("EXTREME-NP-MIB", "extremeNPModuleProcessorState"))
)
if mibBuilder.loadTexts:
    extremeProcessorStateChangeTrap.setStatus(
        "current"
    )

extremeMsmFailoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 5)
)
extremeMsmFailoverTrap.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeMasterMSMSlot"),
        ("EXTREME-SYSTEM-MIB", "extremeMsmFailoverCause"))
)
if mibBuilder.loadTexts:
    extremeMsmFailoverTrap.setStatus(
        "current"
    )

extremeEsrpTimedOutFailedOverMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 6)
)
extremeEsrpTimedOutFailedOverMaster.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
        ("EXTREME-VLAN-MIB", "extremeVlanIfDescr"),
        ("EXTREME-ESRP-MIB", "extremeEsrpState"))
)
if mibBuilder.loadTexts:
    extremeEsrpTimedOutFailedOverMaster.setStatus(
        "current"
    )

extremeRateLimitExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 7)
)
extremeRateLimitExceededTrap.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeRateLimitExceededTrapType"),
        ("EXTREME-V2TRAP-MIB", "extremeRateLimitExceededTrapIndicator"),
        ("IF-MIB", "ifIndex"),
        ("EXTREME-QOS-MIB", "extremeIQosProfileIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeExceededByteCount"))
)
if mibBuilder.loadTexts:
    extremeRateLimitExceededTrap.setStatus(
        "current"
    )

extremeOverheatNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 8)
)
extremeOverheatNormal.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeCurrentTemperature"))
)
if mibBuilder.loadTexts:
    extremeOverheatNormal.setStatus(
        "current"
    )

extremeBgpPrefixReachedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 2, 0, 1)
)
extremeBgpPrefixReachedThreshold.setObjects(
    ("BGP4-MIB", "bgpPeerRemoteAddr")
)
if mibBuilder.loadTexts:
    extremeBgpPrefixReachedThreshold.setStatus(
        "current"
    )

extremeBgpPrefixMaxExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 2, 0, 2)
)
extremeBgpPrefixMaxExceeded.setObjects(
    ("BGP4-MIB", "bgpPeerRemoteAddr")
)
if mibBuilder.loadTexts:
    extremeBgpPrefixMaxExceeded.setStatus(
        "current"
    )

extremeMacLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 1)
)
extremeMacLimitExceeded.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanDescr"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityMacAddress"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityPortIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanId"))
)
if mibBuilder.loadTexts:
    extremeMacLimitExceeded.setStatus(
        "current"
    )

extremeUnauthorizedPortForMacDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 2)
)
extremeUnauthorizedPortForMacDetected.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanDescr"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanId"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityMacAddress"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityPortIfIndex"))
)
if mibBuilder.loadTexts:
    extremeUnauthorizedPortForMacDetected.setStatus(
        "current"
    )

extremeMacDetectedOnLockedPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 3)
)
extremeMacDetectedOnLockedPort.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanDescr"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanId"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityMacAddress"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityPortIfIndex"))
)
if mibBuilder.loadTexts:
    extremeMacDetectedOnLockedPort.setStatus(
        "current"
    )

extremeNetloginUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 4)
)
extremeNetloginUserLogin.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeNetloginStationMac"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginStationAddr"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginPortIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginAuthType"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSystemTime"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginUser"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSrcVlan"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginDestVlan"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSessionStatus"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginAuthDataBase"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginMoveFromVlanList"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginMoveToVlanList"))
)
if mibBuilder.loadTexts:
    extremeNetloginUserLogin.setStatus(
        "current"
    )

extremeNetloginUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 5)
)
extremeNetloginUserLogout.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeNetloginStationMac"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginStationAddr"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginPortIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginAuthType"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSystemTime"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginUser"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSrcVlan"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginDestVlan"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSessionStatus"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginMoveFromVlanList"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginMoveToVlanList"))
)
if mibBuilder.loadTexts:
    extremeNetloginUserLogout.setStatus(
        "current"
    )

extremeNetloginAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 6)
)
extremeNetloginAuthFailure.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeNetloginStationMac"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginStationAddr"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginPortIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginAuthType"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSystemTime"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginUser"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSrcVlan"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginDestVlan"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSessionStatus"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginMoveFromVlanList"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginMoveToVlanList"))
)
if mibBuilder.loadTexts:
    extremeNetloginAuthFailure.setStatus(
        "current"
    )

extremeGratuitousArpViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 7)
)
extremeGratuitousArpViolation.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeArpSecurityVlanIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeArpSecurityVlanDescr"),
        ("EXTREME-V2TRAP-MIB", "extremeArpSecurityPortIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeArpSecurityIpAddr"),
        ("EXTREME-V2TRAP-MIB", "extremeArpSecurityMacAddress"))
)
if mibBuilder.loadTexts:
    extremeGratuitousArpViolation.setStatus(
        "current"
    )

extremeNMSInventoryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 4, 0, 1)
)
extremeNMSInventoryChanged.setObjects(
    ("EXTREME-V2TRAP-MIB", "extremeNMSDeviceAddress")
)
if mibBuilder.loadTexts:
    extremeNMSInventoryChanged.setStatus(
        "current"
    )

extremeNMSTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 4, 0, 2)
)
if mibBuilder.loadTexts:
    extremeNMSTopologyChanged.setStatus(
        "current"
    )

extremeElrpVlanLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 6, 0, 1)
)
extremeElrpVlanLoopDetected.setObjects(
    ("EXTREME-VLAN-MIB", "extremeVlanIfDescr")
)
if mibBuilder.loadTexts:
    extremeElrpVlanLoopDetected.setStatus(
        "current"
    )

extremeEapsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0, 1)
)
extremeEapsStateChange.setObjects(
      *(("EXTREME-EAPS-MIB", "extremeEapsName"),
        ("EXTREME-EAPS-MIB", "extremeEapsMode"),
        ("EXTREME-EAPS-MIB", "extremeEapsPrevState"),
        ("EXTREME-EAPS-MIB", "extremeEapsState"),
        ("EXTREME-EAPS-MIB", "extremeEapsFailedFlag"),
        ("EXTREME-EAPS-MIB", "extremeEapsPrimaryStatus"),
        ("EXTREME-EAPS-MIB", "extremeEapsSecondaryStatus"))
)
if mibBuilder.loadTexts:
    extremeEapsStateChange.setStatus(
        "current"
    )

extremeEapsFailTimerExpFlagSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0, 2)
)
extremeEapsFailTimerExpFlagSet.setObjects(
      *(("EXTREME-EAPS-MIB", "extremeEapsName"),
        ("EXTREME-EAPS-MIB", "extremeEapsMode"),
        ("EXTREME-EAPS-MIB", "extremeEapsPrevState"),
        ("EXTREME-EAPS-MIB", "extremeEapsState"))
)
if mibBuilder.loadTexts:
    extremeEapsFailTimerExpFlagSet.setStatus(
        "current"
    )

extremeEapsFailTimerExpFlagClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0, 3)
)
extremeEapsFailTimerExpFlagClear.setObjects(
      *(("EXTREME-EAPS-MIB", "extremeEapsName"),
        ("EXTREME-EAPS-MIB", "extremeEapsMode"),
        ("EXTREME-EAPS-MIB", "extremeEapsPrevState"),
        ("EXTREME-EAPS-MIB", "extremeEapsState"),
        ("EXTREME-EAPS-MIB", "extremeEapsFailedFlag"),
        ("EXTREME-EAPS-MIB", "extremeEapsPrimaryStatus"),
        ("EXTREME-EAPS-MIB", "extremeEapsSecondaryStatus"))
)
if mibBuilder.loadTexts:
    extremeEapsFailTimerExpFlagClear.setStatus(
        "current"
    )

extremeEapsLinkDownRingComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0, 4)
)
extremeEapsLinkDownRingComplete.setObjects(
      *(("EXTREME-EAPS-MIB", "extremeEapsName"),
        ("EXTREME-EAPS-MIB", "extremeEapsMode"),
        ("EXTREME-EAPS-MIB", "extremeEapsPrevState"),
        ("EXTREME-EAPS-MIB", "extremeEapsState"),
        ("EXTREME-EAPS-MIB", "extremeEapsFailedFlag"),
        ("EXTREME-EAPS-MIB", "extremeEapsPrimaryStatus"),
        ("EXTREME-EAPS-MIB", "extremeEapsSecondaryStatus"))
)
if mibBuilder.loadTexts:
    extremeEapsLinkDownRingComplete.setStatus(
        "current"
    )

extremeEapsPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0, 5)
)
extremeEapsPortStatusChange.setObjects(
      *(("EXTREME-EAPS-MIB", "extremeEapsName"),
        ("EXTREME-EAPS-MIB", "extremeEapsPrimaryStatus"),
        ("EXTREME-EAPS-MIB", "extremeEapsSecondaryStatus"),
        ("EXTREME-EAPS-MIB", "extremeEapsLastStatusChange"))
)
if mibBuilder.loadTexts:
    extremeEapsPortStatusChange.setStatus(
        "current"
    )

extremeEapsConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0, 6)
)
extremeEapsConfigChange.setObjects(
    ("EXTREME-EAPS-MIB", "extremeEapsLastConfigurationChange")
)
if mibBuilder.loadTexts:
    extremeEapsConfigChange.setStatus(
        "current"
    )

extremeEapsLastStatusChangeTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0, 7)
)
extremeEapsLastStatusChangeTime.setObjects(
      *(("EXTREME-EAPS-MIB", "extremeEapsLastStatusChange"),
        ("EXTREME-EAPS-MIB", "extremeEapsStatusTrapCount"))
)
if mibBuilder.loadTexts:
    extremeEapsLastStatusChangeTime.setStatus(
        "current"
    )

extremeBgpM2PrefixReachedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 8, 0, 1)
)
extremeBgpM2PrefixReachedThreshold.setObjects(
      *(("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAddr"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAddrType"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLocalAddr"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLocalAddrType"))
)
if mibBuilder.loadTexts:
    extremeBgpM2PrefixReachedThreshold.setStatus(
        "current"
    )

extremeBgpM2PrefixMaxExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 8, 0, 2)
)
extremeBgpM2PrefixMaxExceeded.setObjects(
      *(("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAddr"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAddrType"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLocalAddr"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLocalAddrType"))
)
if mibBuilder.loadTexts:
    extremeBgpM2PrefixMaxExceeded.setStatus(
        "current"
    )

extremeEapsSegmentTimerExpFlagSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9, 0, 1)
)
extremeEapsSegmentTimerExpFlagSet.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeSegmentPort"),
        ("EXTREME-V2TRAP-MIB", "extremeSharedPort"))
)
if mibBuilder.loadTexts:
    extremeEapsSegmentTimerExpFlagSet.setStatus(
        "current"
    )

extremeEapsSegmentTimerExpFlagClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9, 0, 2)
)
extremeEapsSegmentTimerExpFlagClear.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeSegmentPort"),
        ("EXTREME-V2TRAP-MIB", "extremeSharedPort"))
)
if mibBuilder.loadTexts:
    extremeEapsSegmentTimerExpFlagClear.setStatus(
        "current"
    )

extremeEapsSharedPortStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9, 0, 3)
)
extremeEapsSharedPortStateChange.setObjects(
      *(("EXTREME-EAPS-MIB", "extremeEapsSharedPortIfIndex"),
        ("EXTREME-EAPS-MIB", "extremeEapsSharedPortLinkId"),
        ("EXTREME-EAPS-MIB", "extremeEapsSharedPortState"),
        ("EXTREME-EAPS-MIB", "extremeEapsSharedPortNbrStatus"),
        ("EXTREME-EAPS-MIB", "extremeEapsSharedPortRootBlockerStatus"),
        ("EXTREME-EAPS-MIB", "extremeEapsLastStatusChange"))
)
if mibBuilder.loadTexts:
    extremeEapsSharedPortStateChange.setStatus(
        "current"
    )

extremeEapsRootBlockerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9, 0, 4)
)
extremeEapsRootBlockerStatusChange.setObjects(
      *(("EXTREME-EAPS-MIB", "extremeEapsSharedPortIfIndex"),
        ("EXTREME-EAPS-MIB", "extremeEapsSharedPortRootBlockerStatus"),
        ("EXTREME-EAPS-MIB", "extremeEapsSharedPortRootBlockerId"),
        ("EXTREME-EAPS-MIB", "extremeEapsLastStatusChange"))
)
if mibBuilder.loadTexts:
    extremeEapsRootBlockerStatusChange.setStatus(
        "current"
    )

extremePethPSUStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 12, 0, 1)
)
extremePethPSUStatusNotification.setObjects(
      *(("EXTREME-POE-MIB", "extremePethSlotPSUActive"),
        ("EXTREME-POE-MIB", "extremePethSlotMainPseIndex"))
)
if mibBuilder.loadTexts:
    extremePethPSUStatusNotification.setStatus(
        "current"
    )

extremeLacpAddPortToAggregator = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 13, 0, 1)
)
extremeLacpAddPortToAggregator.setObjects(
      *(("EXTREME-LACP-MIB", "extremeLacpGroup"),
        ("EXTREME-LACP-MIB", "extremeLacpMemberPort"))
)
if mibBuilder.loadTexts:
    extremeLacpAddPortToAggregator.setStatus(
        "current"
    )

extremeLacpDeletePortFromAggregator = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 13, 0, 2)
)
extremeLacpDeletePortFromAggregator.setObjects(
      *(("EXTREME-LACP-MIB", "extremeLacpGroup"),
        ("EXTREME-LACP-MIB", "extremeLacpMemberPort"))
)
if mibBuilder.loadTexts:
    extremeLacpDeletePortFromAggregator.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-V2TRAP-MIB",
    **{"extremeV1Traps": extremeV1Traps,
       "extremeOverheat": extremeOverheat,
       "extremeFanfailed": extremeFanfailed,
       "extremeFanOK": extremeFanOK,
       "extremeInvalidLoginAttempt": extremeInvalidLoginAttempt,
       "extremePowerSupplyFail": extremePowerSupplyFail,
       "extremePowerSupplyGood": extremePowerSupplyGood,
       "extremeSmartTrap": extremeSmartTrap,
       "extremeModuleStateChanged": extremeModuleStateChanged,
       "extremeEdpNeighborAdded": extremeEdpNeighborAdded,
       "extremeEdpNeighborRemoved": extremeEdpNeighborRemoved,
       "extremeV2Traps": extremeV2Traps,
       "extremeCoreSCTraps": extremeCoreSCTraps,
       "extremeCoreSCTrapPrefix": extremeCoreSCTrapPrefix,
       "extremeHealthCheckFailed": extremeHealthCheckFailed,
       "extremeCpuUtilizationRisingTrap": extremeCpuUtilizationRisingTrap,
       "extremeCpuUtilizationFallingTrap": extremeCpuUtilizationFallingTrap,
       "extremeProcessorStateChangeTrap": extremeProcessorStateChangeTrap,
       "extremeMsmFailoverTrap": extremeMsmFailoverTrap,
       "extremeEsrpTimedOutFailedOverMaster": extremeEsrpTimedOutFailedOverMaster,
       "extremeRateLimitExceededTrap": extremeRateLimitExceededTrap,
       "extremeRateLimitExceededTrapType": extremeRateLimitExceededTrapType,
       "extremeRateLimitExceededTrapIndicator": extremeRateLimitExceededTrapIndicator,
       "extremeExceededByteCount": extremeExceededByteCount,
       "extremeOverheatNormal": extremeOverheatNormal,
       "extremeBgpTraps": extremeBgpTraps,
       "extremeBgpTrapsPrefix": extremeBgpTrapsPrefix,
       "extremeBgpPrefixReachedThreshold": extremeBgpPrefixReachedThreshold,
       "extremeBgpPrefixMaxExceeded": extremeBgpPrefixMaxExceeded,
       "extremeSecurityTraps": extremeSecurityTraps,
       "extremeSecurityTrapsPrefix": extremeSecurityTrapsPrefix,
       "extremeMacLimitExceeded": extremeMacLimitExceeded,
       "extremeUnauthorizedPortForMacDetected": extremeUnauthorizedPortForMacDetected,
       "extremeMacDetectedOnLockedPort": extremeMacDetectedOnLockedPort,
       "extremeNetloginUserLogin": extremeNetloginUserLogin,
       "extremeNetloginUserLogout": extremeNetloginUserLogout,
       "extremeNetloginAuthFailure": extremeNetloginAuthFailure,
       "extremeGratuitousArpViolation": extremeGratuitousArpViolation,
       "extremeMacSecurityVlanIfIndex": extremeMacSecurityVlanIfIndex,
       "extremeMacSecurityVlanDescr": extremeMacSecurityVlanDescr,
       "extremeMacSecurityMacAddress": extremeMacSecurityMacAddress,
       "extremeMacSecurityPortIfIndex": extremeMacSecurityPortIfIndex,
       "extremeMacSecurityVlanId": extremeMacSecurityVlanId,
       "extremeNetloginStationMac": extremeNetloginStationMac,
       "extremeNetloginStationAddr": extremeNetloginStationAddr,
       "extremeNetloginPortIfIndex": extremeNetloginPortIfIndex,
       "extremeNetloginAuthType": extremeNetloginAuthType,
       "extremeNetloginSystemTime": extremeNetloginSystemTime,
       "extremeNetloginUser": extremeNetloginUser,
       "extremeNetloginSrcVlan": extremeNetloginSrcVlan,
       "extremeNetloginDestVlan": extremeNetloginDestVlan,
       "extremeNetloginSessionStatus": extremeNetloginSessionStatus,
       "extremeArpSecurityVlanIfIndex": extremeArpSecurityVlanIfIndex,
       "extremeArpSecurityVlanDescr": extremeArpSecurityVlanDescr,
       "extremeArpSecurityPortIfIndex": extremeArpSecurityPortIfIndex,
       "extremeArpSecurityIpAddr": extremeArpSecurityIpAddr,
       "extremeArpSecurityMacAddress": extremeArpSecurityMacAddress,
       "extremeNetloginAuthDataBase": extremeNetloginAuthDataBase,
       "extremeNetloginMoveFromVlanList": extremeNetloginMoveFromVlanList,
       "extremeNetloginMoveToVlanList": extremeNetloginMoveToVlanList,
       "extremeNMSTraps": extremeNMSTraps,
       "extremeNMSTrapsPrefix": extremeNMSTrapsPrefix,
       "extremeNMSInventoryChanged": extremeNMSInventoryChanged,
       "extremeNMSTopologyChanged": extremeNMSTopologyChanged,
       "extremeNMSDeviceAddress": extremeNMSDeviceAddress,
       "extremeElrpTraps": extremeElrpTraps,
       "extremeElrpTrapsPrefix": extremeElrpTrapsPrefix,
       "extremeElrpVlanLoopDetected": extremeElrpVlanLoopDetected,
       "extremeEapsTraps": extremeEapsTraps,
       "extremeEapsTrapsPrefix": extremeEapsTrapsPrefix,
       "extremeEapsStateChange": extremeEapsStateChange,
       "extremeEapsFailTimerExpFlagSet": extremeEapsFailTimerExpFlagSet,
       "extremeEapsFailTimerExpFlagClear": extremeEapsFailTimerExpFlagClear,
       "extremeEapsLinkDownRingComplete": extremeEapsLinkDownRingComplete,
       "extremeEapsPortStatusChange": extremeEapsPortStatusChange,
       "extremeEapsConfigChange": extremeEapsConfigChange,
       "extremeEapsLastStatusChangeTime": extremeEapsLastStatusChangeTime,
       "extremeBgpM2Traps": extremeBgpM2Traps,
       "extremeBgpM2TrapsPrefix": extremeBgpM2TrapsPrefix,
       "extremeBgpM2PrefixReachedThreshold": extremeBgpM2PrefixReachedThreshold,
       "extremeBgpM2PrefixMaxExceeded": extremeBgpM2PrefixMaxExceeded,
       "extremeEapsSharedLinkTraps": extremeEapsSharedLinkTraps,
       "extremeEapsSharedLinkTrapsPrefix": extremeEapsSharedLinkTrapsPrefix,
       "extremeEapsSegmentTimerExpFlagSet": extremeEapsSegmentTimerExpFlagSet,
       "extremeEapsSegmentTimerExpFlagClear": extremeEapsSegmentTimerExpFlagClear,
       "extremeEapsSharedPortStateChange": extremeEapsSharedPortStateChange,
       "extremeEapsRootBlockerStatusChange": extremeEapsRootBlockerStatusChange,
       "extremeSegmentPort": extremeSegmentPort,
       "extremeSharedPort": extremeSharedPort,
       "extremePethTraps": extremePethTraps,
       "extremePethNotificationPrefix": extremePethNotificationPrefix,
       "extremePethPSUStatusNotification": extremePethPSUStatusNotification,
       "extremeLacpTraps": extremeLacpTraps,
       "extremeLacpNotificationPrefix": extremeLacpNotificationPrefix,
       "extremeLacpAddPortToAggregator": extremeLacpAddPortToAggregator,
       "extremeLacpDeletePortFromAggregator": extremeLacpDeletePortFromAggregator}
)
