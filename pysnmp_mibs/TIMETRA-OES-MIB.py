# SNMP MIB module (TIMETRA-OES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-OES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:03:20 2025
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
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(TmnxDeviceState,
 TmnxHwIndexOrZero,
 tmnxHwClass) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxDeviceState",
    "TmnxHwIndexOrZero",
    "tmnxHwClass")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TNamedItemOrEmpty,
 TmnxActionType,
 TmnxDisplayStringURL,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxDisplayStringURL",
    "TmnxOperState")


# MODULE-IDENTITY

timetraOesMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 98)
)
if mibBuilder.loadTexts:
    timetraOesMIBModule.setRevisions(
        ("2016-01-01 00:00",
         "2013-08-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxOesSWMgmtStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("unknown", 1),
          ("inProgress", 2),
          ("successful", 3),
          ("failed", 4),
          ("paused", 5))
    )



class TmnxOesEventReason(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxOesConformance_ObjectIdentity = ObjectIdentity
tmnxOesConformance = _TmnxOesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 98)
)
_TmnxOesCompliances_ObjectIdentity = ObjectIdentity
tmnxOesCompliances = _TmnxOesCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 98, 1)
)
_TmnxOesGroups_ObjectIdentity = ObjectIdentity
tmnxOesGroups = _TmnxOesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 98, 2)
)
_TmnxOesV14v0Groups_ObjectIdentity = ObjectIdentity
tmnxOesV14v0Groups = _TmnxOesV14v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 98, 2, 1)
)
_TmnxOesObjs_ObjectIdentity = ObjectIdentity
tmnxOesObjs = _TmnxOesObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98)
)
_TmnxOesConfigObjs_ObjectIdentity = ObjectIdentity
tmnxOesConfigObjs = _TmnxOesConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 1)
)


class _TmnxOesCfCache_Type(Integer32):
    """Custom type tmnxOesCfCache based on Integer32"""
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
        *(("cf1", 1),
          ("cf2", 2),
          ("cf3", 3))
    )


_TmnxOesCfCache_Type.__name__ = "Integer32"
_TmnxOesCfCache_Object = MibScalar
tmnxOesCfCache = _TmnxOesCfCache_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 1, 1),
    _TmnxOesCfCache_Type()
)
tmnxOesCfCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOesCfCache.setStatus("current")


class _TmnxOesReboot_Type(Integer32):
    """Custom type tmnxOesReboot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("coldReset", 1))
    )


_TmnxOesReboot_Type.__name__ = "Integer32"
_TmnxOesReboot_Object = MibScalar
tmnxOesReboot = _TmnxOesReboot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 1, 2),
    _TmnxOesReboot_Type()
)
tmnxOesReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOesReboot.setStatus("current")


class _TmnxOesSwUpgrade_Type(TmnxActionType):
    """Custom type tmnxOesSwUpgrade based on TmnxActionType"""
    defaultValue = 2


_TmnxOesSwUpgrade_Type.__name__ = "TmnxActionType"
_TmnxOesSwUpgrade_Object = MibScalar
tmnxOesSwUpgrade = _TmnxOesSwUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 1, 3),
    _TmnxOesSwUpgrade_Type()
)
tmnxOesSwUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOesSwUpgrade.setStatus("current")


class _TmnxOesSoftwareRepository_Type(TNamedItemOrEmpty):
    """Custom type tmnxOesSoftwareRepository based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOesSoftwareRepository_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOesSoftwareRepository_Object = MibScalar
tmnxOesSoftwareRepository = _TmnxOesSoftwareRepository_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 1, 4),
    _TmnxOesSoftwareRepository_Type()
)
tmnxOesSoftwareRepository.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOesSoftwareRepository.setStatus("current")


class _TmnxOesCtlCommsVRtrName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOesCtlCommsVRtrName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOesCtlCommsVRtrName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOesCtlCommsVRtrName_Object = MibScalar
tmnxOesCtlCommsVRtrName = _TmnxOesCtlCommsVRtrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 1, 5),
    _TmnxOesCtlCommsVRtrName_Type()
)
tmnxOesCtlCommsVRtrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOesCtlCommsVRtrName.setStatus("current")


class _TmnxOesCtlCommsAddressType_Type(InetAddressType):
    """Custom type tmnxOesCtlCommsAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxOesCtlCommsAddressType_Type.__name__ = "InetAddressType"
_TmnxOesCtlCommsAddressType_Object = MibScalar
tmnxOesCtlCommsAddressType = _TmnxOesCtlCommsAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 1, 6),
    _TmnxOesCtlCommsAddressType_Type()
)
tmnxOesCtlCommsAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOesCtlCommsAddressType.setStatus("current")


class _TmnxOesCtlCommsAddress_Type(InetAddress):
    """Custom type tmnxOesCtlCommsAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOesCtlCommsAddress_Type.__name__ = "InetAddress"
_TmnxOesCtlCommsAddress_Object = MibScalar
tmnxOesCtlCommsAddress = _TmnxOesCtlCommsAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 1, 7),
    _TmnxOesCtlCommsAddress_Type()
)
tmnxOesCtlCommsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOesCtlCommsAddress.setStatus("current")


class _TmnxOesCtlCommsTimeout_Type(Unsigned32):
    """Custom type tmnxOesCtlCommsTimeout based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_TmnxOesCtlCommsTimeout_Type.__name__ = "Unsigned32"
_TmnxOesCtlCommsTimeout_Object = MibScalar
tmnxOesCtlCommsTimeout = _TmnxOesCtlCommsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 1, 8),
    _TmnxOesCtlCommsTimeout_Type()
)
tmnxOesCtlCommsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOesCtlCommsTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOesCtlCommsTimeout.setUnits("seconds")


class _TmnxOesCtlCommsRetryLimit_Type(Unsigned32):
    """Custom type tmnxOesCtlCommsRetryLimit based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxOesCtlCommsRetryLimit_Type.__name__ = "Unsigned32"
_TmnxOesCtlCommsRetryLimit_Object = MibScalar
tmnxOesCtlCommsRetryLimit = _TmnxOesCtlCommsRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 1, 9),
    _TmnxOesCtlCommsRetryLimit_Type()
)
tmnxOesCtlCommsRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOesCtlCommsRetryLimit.setStatus("current")
_TmnxOesStatObjs_ObjectIdentity = ObjectIdentity
tmnxOesStatObjs = _TmnxOesStatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2)
)
_TmnxOesRunningSwImage_Type = DisplayString
_TmnxOesRunningSwImage_Object = MibScalar
tmnxOesRunningSwImage = _TmnxOesRunningSwImage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2, 1),
    _TmnxOesRunningSwImage_Type()
)
tmnxOesRunningSwImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesRunningSwImage.setStatus("current")


class _TmnxOesCtlCommsStatus_Type(Integer32):
    """Custom type tmnxOesCtlCommsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )


_TmnxOesCtlCommsStatus_Type.__name__ = "Integer32"
_TmnxOesCtlCommsStatus_Object = MibScalar
tmnxOesCtlCommsStatus = _TmnxOesCtlCommsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2, 2),
    _TmnxOesCtlCommsStatus_Type()
)
tmnxOesCtlCommsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCtlCommsStatus.setStatus("current")


class _TmnxOesStatus_Type(Integer32):
    """Custom type tmnxOesStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unprovisioned", 0),
          ("discovering", 1),
          ("active", 2),
          ("inactive", 3),
          ("provInProgress", 4),
          ("swUpgradeInProgress", 5))
    )


_TmnxOesStatus_Type.__name__ = "Integer32"
_TmnxOesStatus_Object = MibScalar
tmnxOesStatus = _TmnxOesStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2, 3),
    _TmnxOesStatus_Type()
)
tmnxOesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesStatus.setStatus("current")


class _TmnxOesNtpStatus_Type(Integer32):
    """Custom type tmnxOesNtpStatus based on Integer32"""
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
        *(("unknown", 1),
          ("freerun", 2),
          ("holdover", 3),
          ("sync", 4))
    )


_TmnxOesNtpStatus_Type.__name__ = "Integer32"
_TmnxOesNtpStatus_Object = MibScalar
tmnxOesNtpStatus = _TmnxOesNtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2, 4),
    _TmnxOesNtpStatus_Type()
)
tmnxOesNtpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesNtpStatus.setStatus("current")
_TmnxOesUserPanelHwIndex_Type = TmnxHwIndexOrZero
_TmnxOesUserPanelHwIndex_Object = MibScalar
tmnxOesUserPanelHwIndex = _TmnxOesUserPanelHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2, 5),
    _TmnxOesUserPanelHwIndex_Type()
)
tmnxOesUserPanelHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesUserPanelHwIndex.setStatus("current")
_TmnxOesUserPanelState_Type = TmnxDeviceState
_TmnxOesUserPanelState_Object = MibScalar
tmnxOesUserPanelState = _TmnxOesUserPanelState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2, 6),
    _TmnxOesUserPanelState_Type()
)
tmnxOesUserPanelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesUserPanelState.setStatus("current")


class _TmnxOesCtlCommsDownReason_Type(Integer32):
    """Custom type tmnxOesCtlCommsDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknownReason", 0),
          ("adminReboot", 1),
          ("noResponse", 2),
          ("configFailed", 3),
          ("invalidSystem", 4),
          ("invalidSoftware", 5),
          ("oesUnreachable", 6),
          ("adminEcSwitchOver", 7),
          ("ctlCommsUnprov", 8),
          ("clearActiveEcCard", 9))
    )


_TmnxOesCtlCommsDownReason_Type.__name__ = "Integer32"
_TmnxOesCtlCommsDownReason_Object = MibScalar
tmnxOesCtlCommsDownReason = _TmnxOesCtlCommsDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2, 7),
    _TmnxOesCtlCommsDownReason_Type()
)
tmnxOesCtlCommsDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCtlCommsDownReason.setStatus("current")
_TmnxOesSwUpgradeLastStatus_Type = TmnxOesSWMgmtStatus
_TmnxOesSwUpgradeLastStatus_Object = MibScalar
tmnxOesSwUpgradeLastStatus = _TmnxOesSwUpgradeLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2, 10),
    _TmnxOesSwUpgradeLastStatus_Type()
)
tmnxOesSwUpgradeLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesSwUpgradeLastStatus.setStatus("current")
_TmnxOesSwUpgradeLastTime_Type = DateAndTime
_TmnxOesSwUpgradeLastTime_Object = MibScalar
tmnxOesSwUpgradeLastTime = _TmnxOesSwUpgradeLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2, 11),
    _TmnxOesSwUpgradeLastTime_Type()
)
tmnxOesSwUpgradeLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesSwUpgradeLastTime.setStatus("current")
_TmnxOesSwUpgradeCleanupLstStatus_Type = TmnxOesSWMgmtStatus
_TmnxOesSwUpgradeCleanupLstStatus_Object = MibScalar
tmnxOesSwUpgradeCleanupLstStatus = _TmnxOesSwUpgradeCleanupLstStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2, 12),
    _TmnxOesSwUpgradeCleanupLstStatus_Type()
)
tmnxOesSwUpgradeCleanupLstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesSwUpgradeCleanupLstStatus.setStatus("current")
_TmnxOesSwUpgradeLastCompleteTime_Type = DateAndTime
_TmnxOesSwUpgradeLastCompleteTime_Object = MibScalar
tmnxOesSwUpgradeLastCompleteTime = _TmnxOesSwUpgradeLastCompleteTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2, 13),
    _TmnxOesSwUpgradeLastCompleteTime_Type()
)
tmnxOesSwUpgradeLastCompleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesSwUpgradeLastCompleteTime.setStatus("current")
_TmnxOesExpectedSwImage_Type = DisplayString
_TmnxOesExpectedSwImage_Object = MibScalar
tmnxOesExpectedSwImage = _TmnxOesExpectedSwImage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 2, 14),
    _TmnxOesExpectedSwImage_Type()
)
tmnxOesExpectedSwImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesExpectedSwImage.setStatus("current")
_TmnxOesNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxOesNotifyObjs = _TmnxOesNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 3)
)
_TmnxOesEventReason_Type = TmnxOesEventReason
_TmnxOesEventReason_Object = MibScalar
tmnxOesEventReason = _TmnxOesEventReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 98, 3, 1),
    _TmnxOesEventReason_Type()
)
tmnxOesEventReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOesEventReason.setStatus("current")
_TmnxOesMIBNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOesMIBNotifyPrefix = _TmnxOesMIBNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98)
)
_TmnxOesNotifications_ObjectIdentity = ObjectIdentity
tmnxOesNotifications = _TmnxOesNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0)
)

# Managed Objects groups

tmnxOesGroupV14v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 98, 2, 1, 1)
)
tmnxOesGroupV14v0.setObjects(
      *(("TIMETRA-OES-MIB", "tmnxOesCfCache"),
        ("TIMETRA-OES-MIB", "tmnxOesRunningSwImage"),
        ("TIMETRA-OES-MIB", "tmnxOesCtlCommsStatus"),
        ("TIMETRA-OES-MIB", "tmnxOesReboot"),
        ("TIMETRA-OES-MIB", "tmnxOesStatus"),
        ("TIMETRA-OES-MIB", "tmnxOesUserPanelHwIndex"),
        ("TIMETRA-OES-MIB", "tmnxOesUserPanelState"),
        ("TIMETRA-OES-MIB", "tmnxOesCtlCommsDownReason"),
        ("TIMETRA-OES-MIB", "tmnxOesNtpStatus"),
        ("TIMETRA-OES-MIB", "tmnxOesCtlCommsVRtrName"),
        ("TIMETRA-OES-MIB", "tmnxOesCtlCommsAddressType"),
        ("TIMETRA-OES-MIB", "tmnxOesCtlCommsAddress"),
        ("TIMETRA-OES-MIB", "tmnxOesCtlCommsTimeout"),
        ("TIMETRA-OES-MIB", "tmnxOesCtlCommsRetryLimit"),
        ("TIMETRA-OES-MIB", "tmnxOesSwUpgrade"),
        ("TIMETRA-OES-MIB", "tmnxOesSwUpgradeLastStatus"),
        ("TIMETRA-OES-MIB", "tmnxOesSwUpgradeLastTime"),
        ("TIMETRA-OES-MIB", "tmnxOesSwUpgradeCleanupLstStatus"),
        ("TIMETRA-OES-MIB", "tmnxOesSoftwareRepository"),
        ("TIMETRA-OES-MIB", "tmnxOesSwUpgradeLastCompleteTime"),
        ("TIMETRA-OES-MIB", "tmnxOesExpectedSwImage"))
)
if mibBuilder.loadTexts:
    tmnxOesGroupV14v0.setStatus("current")

tmnxOesNotifyObjsGroupV14v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 98, 2, 1, 3)
)
tmnxOesNotifyObjsGroupV14v0.setObjects(
    ("TIMETRA-OES-MIB", "tmnxOesEventReason")
)
if mibBuilder.loadTexts:
    tmnxOesNotifyObjsGroupV14v0.setStatus("current")


# Notification objects

tmnxOesCtlCommsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 1)
)
tmnxOesCtlCommsDown.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-OES-MIB", "tmnxOesCtlCommsDownReason"))
)
if mibBuilder.loadTexts:
    tmnxOesCtlCommsDown.setStatus(
        "current"
    )

tmnxOesCtlCommsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 2)
)
tmnxOesCtlCommsUp.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesCtlCommsUp.setStatus(
        "current"
    )

tmnxOesDbSyncFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 3)
)
tmnxOesDbSyncFailure.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesDbSyncFailure.setStatus(
        "current"
    )

tmnxOesDbSyncFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 4)
)
tmnxOesDbSyncFailureClear.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesDbSyncFailureClear.setStatus(
        "current"
    )

tmnxOesDbInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 5)
)
tmnxOesDbInvalid.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesDbInvalid.setStatus(
        "current"
    )

tmnxOesDbInvalidClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 6)
)
tmnxOesDbInvalidClear.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesDbInvalidClear.setStatus(
        "current"
    )

tmnxOesDbUnsync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 7)
)
tmnxOesDbUnsync.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesDbUnsync.setStatus(
        "current"
    )

tmnxOesDbUnsyncClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 8)
)
tmnxOesDbUnsyncClear.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesDbUnsyncClear.setStatus(
        "current"
    )

tmnxOesSwUpgdFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 9)
)
tmnxOesSwUpgdFailed.setObjects(
      *(("TIMETRA-OES-MIB", "tmnxOesEventReason"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxOesSwUpgdFailed.setStatus(
        "current"
    )

tmnxOesNtpOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 10)
)
tmnxOesNtpOutOfSync.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesNtpOutOfSync.setStatus(
        "current"
    )

tmnxOesNtpSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 11)
)
tmnxOesNtpSync.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesNtpSync.setStatus(
        "current"
    )

tmnxOesSwBelowMinRev = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 12)
)
tmnxOesSwBelowMinRev.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-OES-MIB", "tmnxOesRunningSwImage"),
        ("TIMETRA-OES-MIB", "tmnxOesExpectedSwImage"))
)
if mibBuilder.loadTexts:
    tmnxOesSwBelowMinRev.setStatus(
        "current"
    )

tmnxOesFirmwareCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 13)
)
tmnxOesFirmwareCondition.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-OES-MIB", "tmnxOesEventReason"))
)
if mibBuilder.loadTexts:
    tmnxOesFirmwareCondition.setStatus(
        "current"
    )

tmnxOesCfgFailNoMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 14)
)
tmnxOesCfgFailNoMemory.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesCfgFailNoMemory.setStatus(
        "current"
    )

tmnxOesCfgBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 15)
)
tmnxOesCfgBlocked.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesCfgBlocked.setStatus(
        "current"
    )

tmnxOesSwUpgdCleanupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 98, 0, 16)
)
tmnxOesSwUpgdCleanupFailed.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-OES-MIB", "tmnxOesEventReason"))
)
if mibBuilder.loadTexts:
    tmnxOesSwUpgdCleanupFailed.setStatus(
        "current"
    )


# Notifications groups

tmnxOesNotificationGroupV14v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 98, 2, 1, 2)
)
tmnxOesNotificationGroupV14v0.setObjects(
      *(("TIMETRA-OES-MIB", "tmnxOesCtlCommsDown"),
        ("TIMETRA-OES-MIB", "tmnxOesCtlCommsUp"),
        ("TIMETRA-OES-MIB", "tmnxOesDbSyncFailure"),
        ("TIMETRA-OES-MIB", "tmnxOesDbSyncFailureClear"),
        ("TIMETRA-OES-MIB", "tmnxOesDbInvalid"),
        ("TIMETRA-OES-MIB", "tmnxOesDbInvalidClear"),
        ("TIMETRA-OES-MIB", "tmnxOesDbUnsync"),
        ("TIMETRA-OES-MIB", "tmnxOesDbUnsyncClear"),
        ("TIMETRA-OES-MIB", "tmnxOesSwUpgdCleanupFailed"),
        ("TIMETRA-OES-MIB", "tmnxOesSwUpgdFailed"),
        ("TIMETRA-OES-MIB", "tmnxOesNtpOutOfSync"),
        ("TIMETRA-OES-MIB", "tmnxOesNtpSync"),
        ("TIMETRA-OES-MIB", "tmnxOesSwBelowMinRev"),
        ("TIMETRA-OES-MIB", "tmnxOesCfgFailNoMemory"),
        ("TIMETRA-OES-MIB", "tmnxOesCfgBlocked"),
        ("TIMETRA-OES-MIB", "tmnxOesFirmwareCondition"))
)
if mibBuilder.loadTexts:
    tmnxOesNotificationGroupV14v0.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxOesV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 98, 1, 1)
)
tmnxOesV14v0Compliance.setObjects(
      *(("TIMETRA-OES-MIB", "tmnxOesGroupV14v0"),
        ("TIMETRA-OES-MIB", "tmnxOesNotificationGroupV14v0"),
        ("TIMETRA-OES-MIB", "tmnxOesNotifyObjsGroupV14v0"))
)
if mibBuilder.loadTexts:
    tmnxOesV14v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-OES-MIB",
    **{"TmnxOesSWMgmtStatus": TmnxOesSWMgmtStatus,
       "TmnxOesEventReason": TmnxOesEventReason,
       "timetraOesMIBModule": timetraOesMIBModule,
       "tmnxOesConformance": tmnxOesConformance,
       "tmnxOesCompliances": tmnxOesCompliances,
       "tmnxOesV14v0Compliance": tmnxOesV14v0Compliance,
       "tmnxOesGroups": tmnxOesGroups,
       "tmnxOesV14v0Groups": tmnxOesV14v0Groups,
       "tmnxOesGroupV14v0": tmnxOesGroupV14v0,
       "tmnxOesNotificationGroupV14v0": tmnxOesNotificationGroupV14v0,
       "tmnxOesNotifyObjsGroupV14v0": tmnxOesNotifyObjsGroupV14v0,
       "tmnxOesObjs": tmnxOesObjs,
       "tmnxOesConfigObjs": tmnxOesConfigObjs,
       "tmnxOesCfCache": tmnxOesCfCache,
       "tmnxOesReboot": tmnxOesReboot,
       "tmnxOesSwUpgrade": tmnxOesSwUpgrade,
       "tmnxOesSoftwareRepository": tmnxOesSoftwareRepository,
       "tmnxOesCtlCommsVRtrName": tmnxOesCtlCommsVRtrName,
       "tmnxOesCtlCommsAddressType": tmnxOesCtlCommsAddressType,
       "tmnxOesCtlCommsAddress": tmnxOesCtlCommsAddress,
       "tmnxOesCtlCommsTimeout": tmnxOesCtlCommsTimeout,
       "tmnxOesCtlCommsRetryLimit": tmnxOesCtlCommsRetryLimit,
       "tmnxOesStatObjs": tmnxOesStatObjs,
       "tmnxOesRunningSwImage": tmnxOesRunningSwImage,
       "tmnxOesCtlCommsStatus": tmnxOesCtlCommsStatus,
       "tmnxOesStatus": tmnxOesStatus,
       "tmnxOesNtpStatus": tmnxOesNtpStatus,
       "tmnxOesUserPanelHwIndex": tmnxOesUserPanelHwIndex,
       "tmnxOesUserPanelState": tmnxOesUserPanelState,
       "tmnxOesCtlCommsDownReason": tmnxOesCtlCommsDownReason,
       "tmnxOesSwUpgradeLastStatus": tmnxOesSwUpgradeLastStatus,
       "tmnxOesSwUpgradeLastTime": tmnxOesSwUpgradeLastTime,
       "tmnxOesSwUpgradeCleanupLstStatus": tmnxOesSwUpgradeCleanupLstStatus,
       "tmnxOesSwUpgradeLastCompleteTime": tmnxOesSwUpgradeLastCompleteTime,
       "tmnxOesExpectedSwImage": tmnxOesExpectedSwImage,
       "tmnxOesNotifyObjs": tmnxOesNotifyObjs,
       "tmnxOesEventReason": tmnxOesEventReason,
       "tmnxOesMIBNotifyPrefix": tmnxOesMIBNotifyPrefix,
       "tmnxOesNotifications": tmnxOesNotifications,
       "tmnxOesCtlCommsDown": tmnxOesCtlCommsDown,
       "tmnxOesCtlCommsUp": tmnxOesCtlCommsUp,
       "tmnxOesDbSyncFailure": tmnxOesDbSyncFailure,
       "tmnxOesDbSyncFailureClear": tmnxOesDbSyncFailureClear,
       "tmnxOesDbInvalid": tmnxOesDbInvalid,
       "tmnxOesDbInvalidClear": tmnxOesDbInvalidClear,
       "tmnxOesDbUnsync": tmnxOesDbUnsync,
       "tmnxOesDbUnsyncClear": tmnxOesDbUnsyncClear,
       "tmnxOesSwUpgdFailed": tmnxOesSwUpgdFailed,
       "tmnxOesNtpOutOfSync": tmnxOesNtpOutOfSync,
       "tmnxOesNtpSync": tmnxOesNtpSync,
       "tmnxOesSwBelowMinRev": tmnxOesSwBelowMinRev,
       "tmnxOesFirmwareCondition": tmnxOesFirmwareCondition,
       "tmnxOesCfgFailNoMemory": tmnxOesCfgFailNoMemory,
       "tmnxOesCfgBlocked": tmnxOesCfgBlocked,
       "tmnxOesSwUpgdCleanupFailed": tmnxOesSwUpgdCleanupFailed}
)
