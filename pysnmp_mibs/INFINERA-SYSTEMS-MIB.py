# SNMP MIB module (INFINERA-SYSTEMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-SYSTEMS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:03 2025
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

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(infnNE,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "infnNE")

(InfnALSAdminPolicy,
 InfnAdminState,
 InfnArc,
 InfnCurrentDcnGatewayType,
 InfnEnableDisable,
 InfnMigrationStatus,
 InfnNeType,
 InfnPhyConnDcnGwType,
 InfnSysArcBehaviour,
 InfnSysEnableAuxTosByteAlteration,
 InfnSysTermLoopBackBehaviour,
 InfnSyslogFeature,
 InfnUpgradePrepStatus) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnALSAdminPolicy",
    "InfnAdminState",
    "InfnArc",
    "InfnCurrentDcnGatewayType",
    "InfnEnableDisable",
    "InfnMigrationStatus",
    "InfnNeType",
    "InfnPhyConnDcnGwType",
    "InfnSysArcBehaviour",
    "InfnSysEnableAuxTosByteAlteration",
    "InfnSysTermLoopBackBehaviour",
    "InfnSyslogFeature",
    "InfnUpgradePrepStatus")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

infnSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_InfnSystemMoId_Type = DisplayString
_InfnSystemMoId_Object = MibScalar
infnSystemMoId = _InfnSystemMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 1),
    _InfnSystemMoId_Type()
)
infnSystemMoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemMoId.setStatus("current")


class _InfnSystemLabel_Type(DisplayString):
    """Custom type infnSystemLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_InfnSystemLabel_Type.__name__ = "DisplayString"
_InfnSystemLabel_Object = MibScalar
infnSystemLabel = _InfnSystemLabel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 2),
    _InfnSystemLabel_Type()
)
infnSystemLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemLabel.setStatus("current")


class _InfnSystemAlarmReportControl_Type(InfnArc):
    """Custom type infnSystemAlarmReportControl based on InfnArc"""
    defaultValue = 1


_InfnSystemAlarmReportControl_Type.__name__ = "InfnArc"
_InfnSystemAlarmReportControl_Object = MibScalar
infnSystemAlarmReportControl = _InfnSystemAlarmReportControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 3),
    _InfnSystemAlarmReportControl_Type()
)
infnSystemAlarmReportControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemAlarmReportControl.setStatus("current")
_InfnSystemAlarmInhibitState_Type = InfnArc
_InfnSystemAlarmInhibitState_Object = MibScalar
infnSystemAlarmInhibitState = _InfnSystemAlarmInhibitState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 4),
    _InfnSystemAlarmInhibitState_Type()
)
infnSystemAlarmInhibitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemAlarmInhibitState.setStatus("current")
_InfnSystemNodeId_Type = DisplayString
_InfnSystemNodeId_Object = MibScalar
infnSystemNodeId = _InfnSystemNodeId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 5),
    _InfnSystemNodeId_Type()
)
infnSystemNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemNodeId.setStatus("current")


class _InfnSystemNeName_Type(DisplayString):
    """Custom type infnSystemNeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_InfnSystemNeName_Type.__name__ = "DisplayString"
_InfnSystemNeName_Object = MibScalar
infnSystemNeName = _InfnSystemNeName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 6),
    _InfnSystemNeName_Type()
)
infnSystemNeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemNeName.setStatus("current")
_InfnSystemNeType_Type = InfnNeType
_InfnSystemNeType_Object = MibScalar
infnSystemNeType = _InfnSystemNeType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 7),
    _InfnSystemNeType_Type()
)
infnSystemNeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemNeType.setStatus("current")


class _InfnSystemArcBehaviour_Type(InfnSysArcBehaviour):
    """Custom type infnSystemArcBehaviour based on InfnSysArcBehaviour"""
    defaultValue = 2


_InfnSystemArcBehaviour_Type.__name__ = "InfnSysArcBehaviour"
_InfnSystemArcBehaviour_Object = MibScalar
infnSystemArcBehaviour = _InfnSystemArcBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 8),
    _InfnSystemArcBehaviour_Type()
)
infnSystemArcBehaviour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemArcBehaviour.setStatus("current")


class _InfnSystemLocation_Type(DisplayString):
    """Custom type infnSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InfnSystemLocation_Type.__name__ = "DisplayString"
_InfnSystemLocation_Object = MibScalar
infnSystemLocation = _InfnSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 9),
    _InfnSystemLocation_Type()
)
infnSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemLocation.setStatus("current")


class _InfnSystemLatitude_Type(DisplayString):
    """Custom type infnSystemLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InfnSystemLatitude_Type.__name__ = "DisplayString"
_InfnSystemLatitude_Object = MibScalar
infnSystemLatitude = _InfnSystemLatitude_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 10),
    _InfnSystemLatitude_Type()
)
infnSystemLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemLatitude.setStatus("current")


class _InfnSystemLongitude_Type(DisplayString):
    """Custom type infnSystemLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InfnSystemLongitude_Type.__name__ = "DisplayString"
_InfnSystemLongitude_Object = MibScalar
infnSystemLongitude = _InfnSystemLongitude_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 11),
    _InfnSystemLongitude_Type()
)
infnSystemLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemLongitude.setStatus("current")
_InfnSystemTime_Type = DisplayString
_InfnSystemTime_Object = MibScalar
infnSystemTime = _InfnSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 12),
    _InfnSystemTime_Type()
)
infnSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemTime.setStatus("current")
_InfnSystemTimeZoneOffset_Type = Integer32
_InfnSystemTimeZoneOffset_Object = MibScalar
infnSystemTimeZoneOffset = _InfnSystemTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 13),
    _InfnSystemTimeZoneOffset_Type()
)
infnSystemTimeZoneOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemTimeZoneOffset.setStatus("current")
_InfnSystemActiveTime_Type = DisplayString
_InfnSystemActiveTime_Object = MibScalar
infnSystemActiveTime = _InfnSystemActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 14),
    _InfnSystemActiveTime_Type()
)
infnSystemActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemActiveTime.setStatus("current")
_InfnSystemDbVer_Type = DisplayString
_InfnSystemDbVer_Object = MibScalar
infnSystemDbVer = _InfnSystemDbVer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 15),
    _InfnSystemDbVer_Type()
)
infnSystemDbVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDbVer.setStatus("current")
_InfnSystemSwGenVer_Type = DisplayString
_InfnSystemSwGenVer_Object = MibScalar
infnSystemSwGenVer = _InfnSystemSwGenVer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 16),
    _InfnSystemSwGenVer_Type()
)
infnSystemSwGenVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemSwGenVer.setStatus("current")
_InfnSystemRouterId_Type = InetAddressIPv4
_InfnSystemRouterId_Object = MibScalar
infnSystemRouterId = _InfnSystemRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 17),
    _InfnSystemRouterId_Type()
)
infnSystemRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemRouterId.setStatus("current")
_InfnSystemDcnIp_Type = InetAddressIPv4
_InfnSystemDcnIp_Object = MibScalar
infnSystemDcnIp = _InfnSystemDcnIp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 18),
    _InfnSystemDcnIp_Type()
)
infnSystemDcnIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDcnIp.setStatus("current")
_InfnSystemDcnIpNetMask_Type = InetAddressIPv4
_InfnSystemDcnIpNetMask_Object = MibScalar
infnSystemDcnIpNetMask = _InfnSystemDcnIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 19),
    _InfnSystemDcnIpNetMask_Type()
)
infnSystemDcnIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDcnIpNetMask.setStatus("current")
_InfnSystemDcnDestination_Type = InetAddressIPv4
_InfnSystemDcnDestination_Object = MibScalar
infnSystemDcnDestination = _InfnSystemDcnDestination_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 20),
    _InfnSystemDcnDestination_Type()
)
infnSystemDcnDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDcnDestination.setStatus("current")
_InfnSystemDcnGateway_Type = InetAddressIPv4
_InfnSystemDcnGateway_Object = MibScalar
infnSystemDcnGateway = _InfnSystemDcnGateway_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 21),
    _InfnSystemDcnGateway_Type()
)
infnSystemDcnGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDcnGateway.setStatus("current")
_InfnSystemDcnPrefixLen_Type = Integer32
_InfnSystemDcnPrefixLen_Object = MibScalar
infnSystemDcnPrefixLen = _InfnSystemDcnPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 22),
    _InfnSystemDcnPrefixLen_Type()
)
infnSystemDcnPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDcnPrefixLen.setStatus("current")
_InfnSystemDcnGlobalRoute_Type = TruthValue
_InfnSystemDcnGlobalRoute_Object = MibScalar
infnSystemDcnGlobalRoute = _InfnSystemDcnGlobalRoute_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 23),
    _InfnSystemDcnGlobalRoute_Type()
)
infnSystemDcnGlobalRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDcnGlobalRoute.setStatus("current")
_InfnSystemSwBuildInfo_Type = DisplayString
_InfnSystemSwBuildInfo_Object = MibScalar
infnSystemSwBuildInfo = _InfnSystemSwBuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 24),
    _InfnSystemSwBuildInfo_Type()
)
infnSystemSwBuildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemSwBuildInfo.setStatus("current")
_InfnSystemCraftIp_Type = InetAddressIPv4
_InfnSystemCraftIp_Object = MibScalar
infnSystemCraftIp = _InfnSystemCraftIp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 25),
    _InfnSystemCraftIp_Type()
)
infnSystemCraftIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemCraftIp.setStatus("current")
_InfnSystemCraftIpNetMask_Type = InetAddressIPv4
_InfnSystemCraftIpNetMask_Object = MibScalar
infnSystemCraftIpNetMask = _InfnSystemCraftIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 26),
    _InfnSystemCraftIpNetMask_Type()
)
infnSystemCraftIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemCraftIpNetMask.setStatus("current")
_InfnSystemCraftIPInterfaceAdministrativeState_Type = InfnAdminState
_InfnSystemCraftIPInterfaceAdministrativeState_Object = MibScalar
infnSystemCraftIPInterfaceAdministrativeState = _InfnSystemCraftIPInterfaceAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 27),
    _InfnSystemCraftIPInterfaceAdministrativeState_Type()
)
infnSystemCraftIPInterfaceAdministrativeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemCraftIPInterfaceAdministrativeState.setStatus("current")
_InfnSystemAuxIp_Type = InetAddressIPv4
_InfnSystemAuxIp_Object = MibScalar
infnSystemAuxIp = _InfnSystemAuxIp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 28),
    _InfnSystemAuxIp_Type()
)
infnSystemAuxIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemAuxIp.setStatus("current")
_InfnSystemAuxIpNetMask_Type = InetAddressIPv4
_InfnSystemAuxIpNetMask_Object = MibScalar
infnSystemAuxIpNetMask = _InfnSystemAuxIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 29),
    _InfnSystemAuxIpNetMask_Type()
)
infnSystemAuxIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemAuxIpNetMask.setStatus("current")
_InfnSystemAuxIPInterfaceAdministrativeState_Type = InfnAdminState
_InfnSystemAuxIPInterfaceAdministrativeState_Object = MibScalar
infnSystemAuxIPInterfaceAdministrativeState = _InfnSystemAuxIPInterfaceAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 30),
    _InfnSystemAuxIPInterfaceAdministrativeState_Type()
)
infnSystemAuxIPInterfaceAdministrativeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemAuxIPInterfaceAdministrativeState.setStatus("current")
_InfnSystemDetectedSerialNumberList_Type = DisplayString
_InfnSystemDetectedSerialNumberList_Object = MibScalar
infnSystemDetectedSerialNumberList = _InfnSystemDetectedSerialNumberList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 31),
    _InfnSystemDetectedSerialNumberList_Type()
)
infnSystemDetectedSerialNumberList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDetectedSerialNumberList.setStatus("current")
_InfnSystemAvailPersistentSpace_Type = DisplayString
_InfnSystemAvailPersistentSpace_Object = MibScalar
infnSystemAvailPersistentSpace = _InfnSystemAvailPersistentSpace_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 32),
    _InfnSystemAvailPersistentSpace_Type()
)
infnSystemAvailPersistentSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemAvailPersistentSpace.setStatus("current")
if mibBuilder.loadTexts:
    infnSystemAvailPersistentSpace.setUnits("Bytes")
_InfnSystemTotalPersistentSpace_Type = DisplayString
_InfnSystemTotalPersistentSpace_Object = MibScalar
infnSystemTotalPersistentSpace = _InfnSystemTotalPersistentSpace_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 33),
    _InfnSystemTotalPersistentSpace_Type()
)
infnSystemTotalPersistentSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemTotalPersistentSpace.setStatus("current")
if mibBuilder.loadTexts:
    infnSystemTotalPersistentSpace.setUnits("Bytes")
_InfnSystemGatewayProxyEnabled_Type = TruthValue
_InfnSystemGatewayProxyEnabled_Object = MibScalar
infnSystemGatewayProxyEnabled = _InfnSystemGatewayProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 34),
    _InfnSystemGatewayProxyEnabled_Type()
)
infnSystemGatewayProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemGatewayProxyEnabled.setStatus("current")
_InfnSystemPrimaryGneIp_Type = InetAddressIPv4
_InfnSystemPrimaryGneIp_Object = MibScalar
infnSystemPrimaryGneIp = _InfnSystemPrimaryGneIp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 35),
    _InfnSystemPrimaryGneIp_Type()
)
infnSystemPrimaryGneIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemPrimaryGneIp.setStatus("current")
_InfnSystemSecondaryGneIp_Type = InetAddressIPv4
_InfnSystemSecondaryGneIp_Object = MibScalar
infnSystemSecondaryGneIp = _InfnSystemSecondaryGneIp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 36),
    _InfnSystemSecondaryGneIp_Type()
)
infnSystemSecondaryGneIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemSecondaryGneIp.setStatus("current")
_InfnSystemMaxNoOfChassisSupported_Type = Integer32
_InfnSystemMaxNoOfChassisSupported_Object = MibScalar
infnSystemMaxNoOfChassisSupported = _InfnSystemMaxNoOfChassisSupported_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 37),
    _InfnSystemMaxNoOfChassisSupported_Type()
)
infnSystemMaxNoOfChassisSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemMaxNoOfChassisSupported.setStatus("current")
_InfnSystemIsForcedSyncNeeded_Type = TruthValue
_InfnSystemIsForcedSyncNeeded_Object = MibScalar
infnSystemIsForcedSyncNeeded = _InfnSystemIsForcedSyncNeeded_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 38),
    _InfnSystemIsForcedSyncNeeded_Type()
)
infnSystemIsForcedSyncNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemIsForcedSyncNeeded.setStatus("current")
_InfnSystemEnableAuxTosByteAlteration_Type = InfnSysEnableAuxTosByteAlteration
_InfnSystemEnableAuxTosByteAlteration_Object = MibScalar
infnSystemEnableAuxTosByteAlteration = _InfnSystemEnableAuxTosByteAlteration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 39),
    _InfnSystemEnableAuxTosByteAlteration_Type()
)
infnSystemEnableAuxTosByteAlteration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemEnableAuxTosByteAlteration.setStatus("current")
_InfnSystemAuxPortRate_Type = Integer32
_InfnSystemAuxPortRate_Object = MibScalar
infnSystemAuxPortRate = _InfnSystemAuxPortRate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 40),
    _InfnSystemAuxPortRate_Type()
)
infnSystemAuxPortRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemAuxPortRate.setStatus("current")


class _InfnSystemClli_Type(DisplayString):
    """Custom type infnSystemClli based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_InfnSystemClli_Type.__name__ = "DisplayString"
_InfnSystemClli_Object = MibScalar
infnSystemClli = _InfnSystemClli_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 41),
    _InfnSystemClli_Type()
)
infnSystemClli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemClli.setStatus("current")


class _InfnSystemLocation2_Type(DisplayString):
    """Custom type infnSystemLocation2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InfnSystemLocation2_Type.__name__ = "DisplayString"
_InfnSystemLocation2_Object = MibScalar
infnSystemLocation2 = _InfnSystemLocation2_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 42),
    _InfnSystemLocation2_Type()
)
infnSystemLocation2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemLocation2.setStatus("current")
_InfnSystemCliPortId_Type = Integer32
_InfnSystemCliPortId_Object = MibScalar
infnSystemCliPortId = _InfnSystemCliPortId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 43),
    _InfnSystemCliPortId_Type()
)
infnSystemCliPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemCliPortId.setStatus("current")
_InfnSystemLayer2Enabled_Type = TruthValue
_InfnSystemLayer2Enabled_Object = MibScalar
infnSystemLayer2Enabled = _InfnSystemLayer2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 44),
    _InfnSystemLayer2Enabled_Type()
)
infnSystemLayer2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemLayer2Enabled.setStatus("current")
_InfnSystemSecondaryDcnIp_Type = InetAddressIPv4
_InfnSystemSecondaryDcnIp_Object = MibScalar
infnSystemSecondaryDcnIp = _InfnSystemSecondaryDcnIp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 45),
    _InfnSystemSecondaryDcnIp_Type()
)
infnSystemSecondaryDcnIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemSecondaryDcnIp.setStatus("current")
_InfnSystemSecondaryDcnIpNetMask_Type = InetAddressIPv4
_InfnSystemSecondaryDcnIpNetMask_Object = MibScalar
infnSystemSecondaryDcnIpNetMask = _InfnSystemSecondaryDcnIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 46),
    _InfnSystemSecondaryDcnIpNetMask_Type()
)
infnSystemSecondaryDcnIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemSecondaryDcnIpNetMask.setStatus("current")
_InfnSystemSecondaryDcnGateway_Type = InetAddressIPv4
_InfnSystemSecondaryDcnGateway_Object = MibScalar
infnSystemSecondaryDcnGateway = _InfnSystemSecondaryDcnGateway_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 47),
    _InfnSystemSecondaryDcnGateway_Type()
)
infnSystemSecondaryDcnGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemSecondaryDcnGateway.setStatus("current")
_InfnSystemCurrentDcnGateway_Type = InfnCurrentDcnGatewayType
_InfnSystemCurrentDcnGateway_Object = MibScalar
infnSystemCurrentDcnGateway = _InfnSystemCurrentDcnGateway_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 48),
    _InfnSystemCurrentDcnGateway_Type()
)
infnSystemCurrentDcnGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemCurrentDcnGateway.setStatus("current")
_InfnSystemPhyConnDcnGw_Type = InfnPhyConnDcnGwType
_InfnSystemPhyConnDcnGw_Object = MibScalar
infnSystemPhyConnDcnGw = _InfnSystemPhyConnDcnGw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 49),
    _InfnSystemPhyConnDcnGw_Type()
)
infnSystemPhyConnDcnGw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemPhyConnDcnGw.setStatus("current")
_InfnSystemTermLoopBackBehaviour_Type = InfnSysTermLoopBackBehaviour
_InfnSystemTermLoopBackBehaviour_Object = MibScalar
infnSystemTermLoopBackBehaviour = _InfnSystemTermLoopBackBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 50),
    _InfnSystemTermLoopBackBehaviour_Type()
)
infnSystemTermLoopBackBehaviour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemTermLoopBackBehaviour.setStatus("current")


class _InfnSystemOscOobEnable_Type(DisplayString):
    """Custom type infnSystemOscOobEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InfnSystemOscOobEnable_Type.__name__ = "DisplayString"
_InfnSystemOscOobEnable_Object = MibScalar
infnSystemOscOobEnable = _InfnSystemOscOobEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 51),
    _InfnSystemOscOobEnable_Type()
)
infnSystemOscOobEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemOscOobEnable.setStatus("current")
_InfnLastUpgradeTime_Type = DisplayString
_InfnLastUpgradeTime_Object = MibScalar
infnLastUpgradeTime = _InfnLastUpgradeTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 52),
    _InfnLastUpgradeTime_Type()
)
infnLastUpgradeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnLastUpgradeTime.setStatus("current")
_InfnRestHoldOffTimer0_Type = Integer32
_InfnRestHoldOffTimer0_Object = MibScalar
infnRestHoldOffTimer0 = _InfnRestHoldOffTimer0_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 53),
    _InfnRestHoldOffTimer0_Type()
)
infnRestHoldOffTimer0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnRestHoldOffTimer0.setStatus("current")
_InfnRestHoldOffTimer1_Type = Integer32
_InfnRestHoldOffTimer1_Object = MibScalar
infnRestHoldOffTimer1 = _InfnRestHoldOffTimer1_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 54),
    _InfnRestHoldOffTimer1_Type()
)
infnRestHoldOffTimer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnRestHoldOffTimer1.setStatus("current")
_InfnRestHoldOffTimer2_Type = Integer32
_InfnRestHoldOffTimer2_Object = MibScalar
infnRestHoldOffTimer2 = _InfnRestHoldOffTimer2_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 55),
    _InfnRestHoldOffTimer2_Type()
)
infnRestHoldOffTimer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnRestHoldOffTimer2.setStatus("current")
_InfnRestHoldOffTimer3_Type = Integer32
_InfnRestHoldOffTimer3_Object = MibScalar
infnRestHoldOffTimer3 = _InfnRestHoldOffTimer3_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 56),
    _InfnRestHoldOffTimer3_Type()
)
infnRestHoldOffTimer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnRestHoldOffTimer3.setStatus("current")
_InfnRestHoldOffTimer4_Type = Integer32
_InfnRestHoldOffTimer4_Object = MibScalar
infnRestHoldOffTimer4 = _InfnRestHoldOffTimer4_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 57),
    _InfnRestHoldOffTimer4_Type()
)
infnRestHoldOffTimer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnRestHoldOffTimer4.setStatus("current")
_InfnRestHoldOffTimer5_Type = Integer32
_InfnRestHoldOffTimer5_Object = MibScalar
infnRestHoldOffTimer5 = _InfnRestHoldOffTimer5_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 58),
    _InfnRestHoldOffTimer5_Type()
)
infnRestHoldOffTimer5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnRestHoldOffTimer5.setStatus("current")
_InfnRestHoldOffTimer6_Type = Integer32
_InfnRestHoldOffTimer6_Object = MibScalar
infnRestHoldOffTimer6 = _InfnRestHoldOffTimer6_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 59),
    _InfnRestHoldOffTimer6_Type()
)
infnRestHoldOffTimer6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnRestHoldOffTimer6.setStatus("current")
_InfnRestHoldOffTimer7_Type = Integer32
_InfnRestHoldOffTimer7_Object = MibScalar
infnRestHoldOffTimer7 = _InfnRestHoldOffTimer7_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 60),
    _InfnRestHoldOffTimer7_Type()
)
infnRestHoldOffTimer7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnRestHoldOffTimer7.setStatus("current")
_InfnEnhProtSw_Type = InfnEnableDisable
_InfnEnhProtSw_Object = MibScalar
infnEnhProtSw = _InfnEnhProtSw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 61),
    _InfnEnhProtSw_Type()
)
infnEnhProtSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnEnhProtSw.setStatus("current")
_InfnALSAdministrationPolicy_Type = InfnALSAdminPolicy
_InfnALSAdministrationPolicy_Object = MibScalar
infnALSAdministrationPolicy = _InfnALSAdministrationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 62),
    _InfnALSAdministrationPolicy_Type()
)
infnALSAdministrationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnALSAdministrationPolicy.setStatus("current")
_InfnOpticalGmplsMscId_Type = Integer32
_InfnOpticalGmplsMscId_Object = MibScalar
infnOpticalGmplsMscId = _InfnOpticalGmplsMscId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 63),
    _InfnOpticalGmplsMscId_Type()
)
infnOpticalGmplsMscId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnOpticalGmplsMscId.setStatus("current")
_InfnPrepareUpgradeStatus_Type = InfnUpgradePrepStatus
_InfnPrepareUpgradeStatus_Object = MibScalar
infnPrepareUpgradeStatus = _InfnPrepareUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 64),
    _InfnPrepareUpgradeStatus_Type()
)
infnPrepareUpgradeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnPrepareUpgradeStatus.setStatus("current")
_InfnPreUpgradeLastAttemptedTime_Type = DisplayString
_InfnPreUpgradeLastAttemptedTime_Object = MibScalar
infnPreUpgradeLastAttemptedTime = _InfnPreUpgradeLastAttemptedTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 65),
    _InfnPreUpgradeLastAttemptedTime_Type()
)
infnPreUpgradeLastAttemptedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnPreUpgradeLastAttemptedTime.setStatus("current")
_InfnPreUpgradeLastSuccessfulTime_Type = DisplayString
_InfnPreUpgradeLastSuccessfulTime_Object = MibScalar
infnPreUpgradeLastSuccessfulTime = _InfnPreUpgradeLastSuccessfulTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 66),
    _InfnPreUpgradeLastSuccessfulTime_Type()
)
infnPreUpgradeLastSuccessfulTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnPreUpgradeLastSuccessfulTime.setStatus("current")
_InfnSystemDcnIp6_Type = InetAddressIPv6
_InfnSystemDcnIp6_Object = MibScalar
infnSystemDcnIp6 = _InfnSystemDcnIp6_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 67),
    _InfnSystemDcnIp6_Type()
)
infnSystemDcnIp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDcnIp6.setStatus("current")
_InfnSystemDcnIpNetMask6_Type = Integer32
_InfnSystemDcnIpNetMask6_Object = MibScalar
infnSystemDcnIpNetMask6 = _InfnSystemDcnIpNetMask6_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 68),
    _InfnSystemDcnIpNetMask6_Type()
)
infnSystemDcnIpNetMask6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDcnIpNetMask6.setStatus("current")
_InfnSystemDcnDestination6_Type = InetAddressIPv6
_InfnSystemDcnDestination6_Object = MibScalar
infnSystemDcnDestination6 = _InfnSystemDcnDestination6_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 69),
    _InfnSystemDcnDestination6_Type()
)
infnSystemDcnDestination6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDcnDestination6.setStatus("current")
_InfnSystemDcnGateway6_Type = InetAddressIPv6
_InfnSystemDcnGateway6_Object = MibScalar
infnSystemDcnGateway6 = _InfnSystemDcnGateway6_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 70),
    _InfnSystemDcnGateway6_Type()
)
infnSystemDcnGateway6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDcnGateway6.setStatus("current")
_InfnSystemDcnPrefixLen6_Type = Integer32
_InfnSystemDcnPrefixLen6_Object = MibScalar
infnSystemDcnPrefixLen6 = _InfnSystemDcnPrefixLen6_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 71),
    _InfnSystemDcnPrefixLen6_Type()
)
infnSystemDcnPrefixLen6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDcnPrefixLen6.setStatus("current")
_InfnSystemCraftIp6_Type = InetAddressIPv6
_InfnSystemCraftIp6_Object = MibScalar
infnSystemCraftIp6 = _InfnSystemCraftIp6_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 72),
    _InfnSystemCraftIp6_Type()
)
infnSystemCraftIp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemCraftIp6.setStatus("current")
_InfnSystemDcnLinkLocal_Type = InetAddressIPv6
_InfnSystemDcnLinkLocal_Object = MibScalar
infnSystemDcnLinkLocal = _InfnSystemDcnLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 73),
    _InfnSystemDcnLinkLocal_Type()
)
infnSystemDcnLinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infnSystemDcnLinkLocal.setStatus("current")
_InfnSystemMigrationStatus_Type = InfnMigrationStatus
_InfnSystemMigrationStatus_Object = MibScalar
infnSystemMigrationStatus = _InfnSystemMigrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 74),
    _InfnSystemMigrationStatus_Type()
)
infnSystemMigrationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemMigrationStatus.setStatus("current")
_InfnSystemSysLogFeature_Type = InfnSyslogFeature
_InfnSystemSysLogFeature_Object = MibScalar
infnSystemSysLogFeature = _InfnSystemSysLogFeature_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 1, 75),
    _InfnSystemSysLogFeature_Type()
)
infnSystemSysLogFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infnSystemSysLogFeature.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-SYSTEMS-MIB",
    **{"infnSystem": infnSystem,
       "infnSystemMoId": infnSystemMoId,
       "infnSystemLabel": infnSystemLabel,
       "infnSystemAlarmReportControl": infnSystemAlarmReportControl,
       "infnSystemAlarmInhibitState": infnSystemAlarmInhibitState,
       "infnSystemNodeId": infnSystemNodeId,
       "infnSystemNeName": infnSystemNeName,
       "infnSystemNeType": infnSystemNeType,
       "infnSystemArcBehaviour": infnSystemArcBehaviour,
       "infnSystemLocation": infnSystemLocation,
       "infnSystemLatitude": infnSystemLatitude,
       "infnSystemLongitude": infnSystemLongitude,
       "infnSystemTime": infnSystemTime,
       "infnSystemTimeZoneOffset": infnSystemTimeZoneOffset,
       "infnSystemActiveTime": infnSystemActiveTime,
       "infnSystemDbVer": infnSystemDbVer,
       "infnSystemSwGenVer": infnSystemSwGenVer,
       "infnSystemRouterId": infnSystemRouterId,
       "infnSystemDcnIp": infnSystemDcnIp,
       "infnSystemDcnIpNetMask": infnSystemDcnIpNetMask,
       "infnSystemDcnDestination": infnSystemDcnDestination,
       "infnSystemDcnGateway": infnSystemDcnGateway,
       "infnSystemDcnPrefixLen": infnSystemDcnPrefixLen,
       "infnSystemDcnGlobalRoute": infnSystemDcnGlobalRoute,
       "infnSystemSwBuildInfo": infnSystemSwBuildInfo,
       "infnSystemCraftIp": infnSystemCraftIp,
       "infnSystemCraftIpNetMask": infnSystemCraftIpNetMask,
       "infnSystemCraftIPInterfaceAdministrativeState": infnSystemCraftIPInterfaceAdministrativeState,
       "infnSystemAuxIp": infnSystemAuxIp,
       "infnSystemAuxIpNetMask": infnSystemAuxIpNetMask,
       "infnSystemAuxIPInterfaceAdministrativeState": infnSystemAuxIPInterfaceAdministrativeState,
       "infnSystemDetectedSerialNumberList": infnSystemDetectedSerialNumberList,
       "infnSystemAvailPersistentSpace": infnSystemAvailPersistentSpace,
       "infnSystemTotalPersistentSpace": infnSystemTotalPersistentSpace,
       "infnSystemGatewayProxyEnabled": infnSystemGatewayProxyEnabled,
       "infnSystemPrimaryGneIp": infnSystemPrimaryGneIp,
       "infnSystemSecondaryGneIp": infnSystemSecondaryGneIp,
       "infnSystemMaxNoOfChassisSupported": infnSystemMaxNoOfChassisSupported,
       "infnSystemIsForcedSyncNeeded": infnSystemIsForcedSyncNeeded,
       "infnSystemEnableAuxTosByteAlteration": infnSystemEnableAuxTosByteAlteration,
       "infnSystemAuxPortRate": infnSystemAuxPortRate,
       "infnSystemClli": infnSystemClli,
       "infnSystemLocation2": infnSystemLocation2,
       "infnSystemCliPortId": infnSystemCliPortId,
       "infnSystemLayer2Enabled": infnSystemLayer2Enabled,
       "infnSystemSecondaryDcnIp": infnSystemSecondaryDcnIp,
       "infnSystemSecondaryDcnIpNetMask": infnSystemSecondaryDcnIpNetMask,
       "infnSystemSecondaryDcnGateway": infnSystemSecondaryDcnGateway,
       "infnSystemCurrentDcnGateway": infnSystemCurrentDcnGateway,
       "infnSystemPhyConnDcnGw": infnSystemPhyConnDcnGw,
       "infnSystemTermLoopBackBehaviour": infnSystemTermLoopBackBehaviour,
       "infnSystemOscOobEnable": infnSystemOscOobEnable,
       "infnLastUpgradeTime": infnLastUpgradeTime,
       "infnRestHoldOffTimer0": infnRestHoldOffTimer0,
       "infnRestHoldOffTimer1": infnRestHoldOffTimer1,
       "infnRestHoldOffTimer2": infnRestHoldOffTimer2,
       "infnRestHoldOffTimer3": infnRestHoldOffTimer3,
       "infnRestHoldOffTimer4": infnRestHoldOffTimer4,
       "infnRestHoldOffTimer5": infnRestHoldOffTimer5,
       "infnRestHoldOffTimer6": infnRestHoldOffTimer6,
       "infnRestHoldOffTimer7": infnRestHoldOffTimer7,
       "infnEnhProtSw": infnEnhProtSw,
       "infnALSAdministrationPolicy": infnALSAdministrationPolicy,
       "infnOpticalGmplsMscId": infnOpticalGmplsMscId,
       "infnPrepareUpgradeStatus": infnPrepareUpgradeStatus,
       "infnPreUpgradeLastAttemptedTime": infnPreUpgradeLastAttemptedTime,
       "infnPreUpgradeLastSuccessfulTime": infnPreUpgradeLastSuccessfulTime,
       "infnSystemDcnIp6": infnSystemDcnIp6,
       "infnSystemDcnIpNetMask6": infnSystemDcnIpNetMask6,
       "infnSystemDcnDestination6": infnSystemDcnDestination6,
       "infnSystemDcnGateway6": infnSystemDcnGateway6,
       "infnSystemDcnPrefixLen6": infnSystemDcnPrefixLen6,
       "infnSystemCraftIp6": infnSystemCraftIp6,
       "infnSystemDcnLinkLocal": infnSystemDcnLinkLocal,
       "infnSystemMigrationStatus": infnSystemMigrationStatus,
       "infnSystemSysLogFeature": infnSystemSysLogFeature}
)
