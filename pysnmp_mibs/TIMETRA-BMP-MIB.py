# SNMP MIB module (TIMETRA-BMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-BMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:01:40 2025
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
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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

(TmnxIpFamily,) = mibBuilder.importSymbols(
    "TIMETRA-BGP-MIB",
    "TmnxIpFamily")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TItemDescription,
 TLNamedItemOrEmpty,
 TNamedItem,
 TmnxAdminState,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TmnxAdminState",
    "TmnxVRtrID")


# MODULE-IDENTITY

timetraBmpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 108)
)
if mibBuilder.loadTexts:
    timetraBmpMIBModule.setRevisions(
        ("2016-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxBmpConnectionMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )



class TmnxBgpMonitorType(TextualConvention, Integer32):
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
        *(("bgpInstance", 0),
          ("bgpPeerGroup", 1),
          ("bgpNeighbor", 2))
    )



class TmnxBgpMonitorRouteMonitoring(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("prePolicy", 0),
          ("postPolicy", 1))
    )


class TmnxBmpSessionConnectionState(TextualConvention, Integer32):
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
        *(("inactive", 0),
          ("shutdown", 1),
          ("idle", 2),
          ("connecting", 3),
          ("welcoming", 4),
          ("established", 5))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxBmpConformance_ObjectIdentity = ObjectIdentity
tmnxBmpConformance = _TmnxBmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108)
)
_TmnxBmpCompliances_ObjectIdentity = ObjectIdentity
tmnxBmpCompliances = _TmnxBmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 1)
)
_TmnxBmpGroups_ObjectIdentity = ObjectIdentity
tmnxBmpGroups = _TmnxBmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 2)
)
_TmnxBmpV15v0Groups_ObjectIdentity = ObjectIdentity
tmnxBmpV15v0Groups = _TmnxBmpV15v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 2, 1)
)
_TmnxBmpV16v0Groups_ObjectIdentity = ObjectIdentity
tmnxBmpV16v0Groups = _TmnxBmpV16v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 2, 2)
)
_TmnxBmpV19v0Groups_ObjectIdentity = ObjectIdentity
tmnxBmpV19v0Groups = _TmnxBmpV19v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 2, 3)
)
_TmnxBmpObjs_ObjectIdentity = ObjectIdentity
tmnxBmpObjs = _TmnxBmpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108)
)
_TmnxBmpParameterObjs_ObjectIdentity = ObjectIdentity
tmnxBmpParameterObjs = _TmnxBmpParameterObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 1)
)


class _TmnxBmpAdminState_Type(TmnxAdminState):
    """Custom type tmnxBmpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxBmpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxBmpAdminState_Object = MibScalar
tmnxBmpAdminState = _TmnxBmpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 1, 1),
    _TmnxBmpAdminState_Type()
)
tmnxBmpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBmpAdminState.setStatus("current")
_TmnxBmpStationTableLastCh_Type = TimeStamp
_TmnxBmpStationTableLastCh_Object = MibScalar
tmnxBmpStationTableLastCh = _TmnxBmpStationTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 1, 2),
    _TmnxBmpStationTableLastCh_Type()
)
tmnxBmpStationTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpStationTableLastCh.setStatus("current")
_TmnxBgpMonitorTableLastCh_Type = TimeStamp
_TmnxBgpMonitorTableLastCh_Object = MibScalar
tmnxBgpMonitorTableLastCh = _TmnxBgpMonitorTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 1, 3),
    _TmnxBgpMonitorTableLastCh_Type()
)
tmnxBgpMonitorTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBgpMonitorTableLastCh.setStatus("current")
_TmnxBmpStationObjs_ObjectIdentity = ObjectIdentity
tmnxBmpStationObjs = _TmnxBmpStationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2)
)
_TmnxBmpStationTable_Object = MibTable
tmnxBmpStationTable = _TmnxBmpStationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxBmpStationTable.setStatus("current")
_TmnxBmpStationEntry_Object = MibTableRow
tmnxBmpStationEntry = _TmnxBmpStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1)
)
tmnxBmpStationEntry.setIndexNames(
    (1, "TIMETRA-BMP-MIB", "tmnxBmpStationName"),
)
if mibBuilder.loadTexts:
    tmnxBmpStationEntry.setStatus("current")
_TmnxBmpStationName_Type = TNamedItem
_TmnxBmpStationName_Object = MibTableColumn
tmnxBmpStationName = _TmnxBmpStationName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 1),
    _TmnxBmpStationName_Type()
)
tmnxBmpStationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBmpStationName.setStatus("current")
_TmnxBmpStationRowStatus_Type = RowStatus
_TmnxBmpStationRowStatus_Object = MibTableColumn
tmnxBmpStationRowStatus = _TmnxBmpStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 2),
    _TmnxBmpStationRowStatus_Type()
)
tmnxBmpStationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationRowStatus.setStatus("current")
_TmnxBmpStationLastChanged_Type = TimeStamp
_TmnxBmpStationLastChanged_Object = MibTableColumn
tmnxBmpStationLastChanged = _TmnxBmpStationLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 3),
    _TmnxBmpStationLastChanged_Type()
)
tmnxBmpStationLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpStationLastChanged.setStatus("current")


class _TmnxBmpStationAdminState_Type(TmnxAdminState):
    """Custom type tmnxBmpStationAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxBmpStationAdminState_Type.__name__ = "TmnxAdminState"
_TmnxBmpStationAdminState_Object = MibTableColumn
tmnxBmpStationAdminState = _TmnxBmpStationAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 4),
    _TmnxBmpStationAdminState_Type()
)
tmnxBmpStationAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationAdminState.setStatus("current")


class _TmnxBmpStationDescr_Type(TItemDescription):
    """Custom type tmnxBmpStationDescr based on TItemDescription"""
    defaultHexValue = ""


_TmnxBmpStationDescr_Type.__name__ = "TItemDescription"
_TmnxBmpStationDescr_Object = MibTableColumn
tmnxBmpStationDescr = _TmnxBmpStationDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 5),
    _TmnxBmpStationDescr_Type()
)
tmnxBmpStationDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationDescr.setStatus("current")


class _TmnxBmpStationConnectRetry_Type(Unsigned32):
    """Custom type tmnxBmpStationConnectRetry based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxBmpStationConnectRetry_Type.__name__ = "Unsigned32"
_TmnxBmpStationConnectRetry_Object = MibTableColumn
tmnxBmpStationConnectRetry = _TmnxBmpStationConnectRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 7),
    _TmnxBmpStationConnectRetry_Type()
)
tmnxBmpStationConnectRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationConnectRetry.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBmpStationConnectRetry.setUnits("seconds")


class _TmnxBmpStationInitialWaitTime_Type(Unsigned32):
    """Custom type tmnxBmpStationInitialWaitTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_TmnxBmpStationInitialWaitTime_Type.__name__ = "Unsigned32"
_TmnxBmpStationInitialWaitTime_Object = MibTableColumn
tmnxBmpStationInitialWaitTime = _TmnxBmpStationInitialWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 8),
    _TmnxBmpStationInitialWaitTime_Type()
)
tmnxBmpStationInitialWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationInitialWaitTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxBmpStationInitialWaitTime.setUnits("minutes")


class _TmnxBmpStationSecondWaitTime_Type(Unsigned32):
    """Custom type tmnxBmpStationSecondWaitTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_TmnxBmpStationSecondWaitTime_Type.__name__ = "Unsigned32"
_TmnxBmpStationSecondWaitTime_Object = MibTableColumn
tmnxBmpStationSecondWaitTime = _TmnxBmpStationSecondWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 9),
    _TmnxBmpStationSecondWaitTime_Type()
)
tmnxBmpStationSecondWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationSecondWaitTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxBmpStationSecondWaitTime.setUnits("minutes")


class _TmnxBmpStationMaxWaitTime_Type(Unsigned32):
    """Custom type tmnxBmpStationMaxWaitTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_TmnxBmpStationMaxWaitTime_Type.__name__ = "Unsigned32"
_TmnxBmpStationMaxWaitTime_Object = MibTableColumn
tmnxBmpStationMaxWaitTime = _TmnxBmpStationMaxWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 10),
    _TmnxBmpStationMaxWaitTime_Type()
)
tmnxBmpStationMaxWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationMaxWaitTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxBmpStationMaxWaitTime.setUnits("minutes")


class _TmnxBmpStationErrorInterval_Type(Unsigned32):
    """Custom type tmnxBmpStationErrorInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_TmnxBmpStationErrorInterval_Type.__name__ = "Unsigned32"
_TmnxBmpStationErrorInterval_Object = MibTableColumn
tmnxBmpStationErrorInterval = _TmnxBmpStationErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 11),
    _TmnxBmpStationErrorInterval_Type()
)
tmnxBmpStationErrorInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationErrorInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxBmpStationErrorInterval.setUnits("minutes")


class _TmnxBmpStationLocalIpAddrType_Type(InetAddressType):
    """Custom type tmnxBmpStationLocalIpAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxBmpStationLocalIpAddrType_Type.__name__ = "InetAddressType"
_TmnxBmpStationLocalIpAddrType_Object = MibTableColumn
tmnxBmpStationLocalIpAddrType = _TmnxBmpStationLocalIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 12),
    _TmnxBmpStationLocalIpAddrType_Type()
)
tmnxBmpStationLocalIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationLocalIpAddrType.setStatus("current")


class _TmnxBmpStationLocalIpAddress_Type(InetAddress):
    """Custom type tmnxBmpStationLocalIpAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBmpStationLocalIpAddress_Type.__name__ = "InetAddress"
_TmnxBmpStationLocalIpAddress_Object = MibTableColumn
tmnxBmpStationLocalIpAddress = _TmnxBmpStationLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 13),
    _TmnxBmpStationLocalIpAddress_Type()
)
tmnxBmpStationLocalIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationLocalIpAddress.setStatus("current")


class _TmnxBmpStationRemoteIpAddrType_Type(InetAddressType):
    """Custom type tmnxBmpStationRemoteIpAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxBmpStationRemoteIpAddrType_Type.__name__ = "InetAddressType"
_TmnxBmpStationRemoteIpAddrType_Object = MibTableColumn
tmnxBmpStationRemoteIpAddrType = _TmnxBmpStationRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 14),
    _TmnxBmpStationRemoteIpAddrType_Type()
)
tmnxBmpStationRemoteIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationRemoteIpAddrType.setStatus("current")


class _TmnxBmpStationRemoteIpAddress_Type(InetAddress):
    """Custom type tmnxBmpStationRemoteIpAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBmpStationRemoteIpAddress_Type.__name__ = "InetAddress"
_TmnxBmpStationRemoteIpAddress_Object = MibTableColumn
tmnxBmpStationRemoteIpAddress = _TmnxBmpStationRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 15),
    _TmnxBmpStationRemoteIpAddress_Type()
)
tmnxBmpStationRemoteIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationRemoteIpAddress.setStatus("current")


class _TmnxBmpStationRemotePort_Type(InetPortNumber):
    """Custom type tmnxBmpStationRemotePort based on InetPortNumber"""
    defaultValue = 0


_TmnxBmpStationRemotePort_Type.__name__ = "InetPortNumber"
_TmnxBmpStationRemotePort_Object = MibTableColumn
tmnxBmpStationRemotePort = _TmnxBmpStationRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 16),
    _TmnxBmpStationRemotePort_Type()
)
tmnxBmpStationRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationRemotePort.setStatus("current")


class _TmnxBmpStationMode_Type(TmnxBmpConnectionMode):
    """Custom type tmnxBmpStationMode based on TmnxBmpConnectionMode"""
    defaultValue = 1


_TmnxBmpStationMode_Type.__name__ = "TmnxBmpConnectionMode"
_TmnxBmpStationMode_Object = MibTableColumn
tmnxBmpStationMode = _TmnxBmpStationMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 17),
    _TmnxBmpStationMode_Type()
)
tmnxBmpStationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationMode.setStatus("obsolete")


class _TmnxBmpStationRouter_Type(TmnxVRtrID):
    """Custom type tmnxBmpStationRouter based on TmnxVRtrID"""
    defaultValue = 1


_TmnxBmpStationRouter_Type.__name__ = "TmnxVRtrID"
_TmnxBmpStationRouter_Object = MibTableColumn
tmnxBmpStationRouter = _TmnxBmpStationRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 18),
    _TmnxBmpStationRouter_Type()
)
tmnxBmpStationRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationRouter.setStatus("current")


class _TmnxBmpStationInitiationMessage_Type(DisplayString):
    """Custom type tmnxBmpStationInitiationMessage based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxBmpStationInitiationMessage_Type.__name__ = "DisplayString"
_TmnxBmpStationInitiationMessage_Object = MibTableColumn
tmnxBmpStationInitiationMessage = _TmnxBmpStationInitiationMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 19),
    _TmnxBmpStationInitiationMessage_Type()
)
tmnxBmpStationInitiationMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationInitiationMessage.setStatus("current")


class _TmnxBmpStationStatsReportIvl_Type(Unsigned32):
    """Custom type tmnxBmpStationStatsReportIvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(15, 65535),
    )


_TmnxBmpStationStatsReportIvl_Type.__name__ = "Unsigned32"
_TmnxBmpStationStatsReportIvl_Object = MibTableColumn
tmnxBmpStationStatsReportIvl = _TmnxBmpStationStatsReportIvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 20),
    _TmnxBmpStationStatsReportIvl_Type()
)
tmnxBmpStationStatsReportIvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationStatsReportIvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBmpStationStatsReportIvl.setUnits("seconds")


class _TmnxBmpStationTcpKaAdminState_Type(TmnxAdminState):
    """Custom type tmnxBmpStationTcpKaAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxBmpStationTcpKaAdminState_Type.__name__ = "TmnxAdminState"
_TmnxBmpStationTcpKaAdminState_Object = MibTableColumn
tmnxBmpStationTcpKaAdminState = _TmnxBmpStationTcpKaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 21),
    _TmnxBmpStationTcpKaAdminState_Type()
)
tmnxBmpStationTcpKaAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationTcpKaAdminState.setStatus("current")


class _TmnxBmpStationTcpKaIdle_Type(Unsigned32):
    """Custom type tmnxBmpStationTcpKaIdle based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxBmpStationTcpKaIdle_Type.__name__ = "Unsigned32"
_TmnxBmpStationTcpKaIdle_Object = MibTableColumn
tmnxBmpStationTcpKaIdle = _TmnxBmpStationTcpKaIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 22),
    _TmnxBmpStationTcpKaIdle_Type()
)
tmnxBmpStationTcpKaIdle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationTcpKaIdle.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBmpStationTcpKaIdle.setUnits("seconds")


class _TmnxBmpStationTcpKaInterval_Type(Unsigned32):
    """Custom type tmnxBmpStationTcpKaInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxBmpStationTcpKaInterval_Type.__name__ = "Unsigned32"
_TmnxBmpStationTcpKaInterval_Object = MibTableColumn
tmnxBmpStationTcpKaInterval = _TmnxBmpStationTcpKaInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 23),
    _TmnxBmpStationTcpKaInterval_Type()
)
tmnxBmpStationTcpKaInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationTcpKaInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBmpStationTcpKaInterval.setUnits("seconds")


class _TmnxBmpStationTcpKaCount_Type(Unsigned32):
    """Custom type tmnxBmpStationTcpKaCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_TmnxBmpStationTcpKaCount_Type.__name__ = "Unsigned32"
_TmnxBmpStationTcpKaCount_Object = MibTableColumn
tmnxBmpStationTcpKaCount = _TmnxBmpStationTcpKaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 24),
    _TmnxBmpStationTcpKaCount_Type()
)
tmnxBmpStationTcpKaCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationTcpKaCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBmpStationTcpKaCount.setUnits("seconds")


class _TmnxBmpStationRoutesReportIvl_Type(Unsigned32):
    """Custom type tmnxBmpStationRoutesReportIvl based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TmnxBmpStationRoutesReportIvl_Type.__name__ = "Unsigned32"
_TmnxBmpStationRoutesReportIvl_Object = MibTableColumn
tmnxBmpStationRoutesReportIvl = _TmnxBmpStationRoutesReportIvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 25),
    _TmnxBmpStationRoutesReportIvl_Type()
)
tmnxBmpStationRoutesReportIvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationRoutesReportIvl.setStatus("deprecated")
if mibBuilder.loadTexts:
    tmnxBmpStationRoutesReportIvl.setUnits("seconds")


class _TmnxBmpStationReportLocalRoutes_Type(TruthValue):
    """Custom type tmnxBmpStationReportLocalRoutes based on TruthValue"""
    defaultValue = 2


_TmnxBmpStationReportLocalRoutes_Type.__name__ = "TruthValue"
_TmnxBmpStationReportLocalRoutes_Object = MibTableColumn
tmnxBmpStationReportLocalRoutes = _TmnxBmpStationReportLocalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 26),
    _TmnxBmpStationReportLocalRoutes_Type()
)
tmnxBmpStationReportLocalRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationReportLocalRoutes.setStatus("current")


class _TmnxBmpStationFamily_Type(TmnxIpFamily):
    """Custom type tmnxBmpStationFamily based on TmnxIpFamily"""
    defaultBinValue = "01"


_TmnxBmpStationFamily_Type.__name__ = "TmnxIpFamily"
_TmnxBmpStationFamily_Object = MibTableColumn
tmnxBmpStationFamily = _TmnxBmpStationFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 1, 1, 27),
    _TmnxBmpStationFamily_Type()
)
tmnxBmpStationFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBmpStationFamily.setStatus("current")
_TmnxBgpMonitorTable_Object = MibTable
tmnxBgpMonitorTable = _TmnxBgpMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxBgpMonitorTable.setStatus("current")
_TmnxBgpMonitorEntry_Object = MibTableRow
tmnxBgpMonitorEntry = _TmnxBgpMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 2, 1)
)
tmnxBgpMonitorEntry.setIndexNames(
    (0, "TIMETRA-BMP-MIB", "tmnxBgpMonitorType"),
    (0, "TIMETRA-BMP-MIB", "tmnxBgpMonitorVRtrID"),
    (0, "TIMETRA-BMP-MIB", "tmnxBgpMonitorPeerGroup"),
    (0, "TIMETRA-BMP-MIB", "tmnxBgpMonitorPeerType"),
    (0, "TIMETRA-BMP-MIB", "tmnxBgpMonitorPeer"),
)
if mibBuilder.loadTexts:
    tmnxBgpMonitorEntry.setStatus("current")
_TmnxBgpMonitorType_Type = TmnxBgpMonitorType
_TmnxBgpMonitorType_Object = MibTableColumn
tmnxBgpMonitorType = _TmnxBgpMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 2, 1, 1),
    _TmnxBgpMonitorType_Type()
)
tmnxBgpMonitorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBgpMonitorType.setStatus("current")
_TmnxBgpMonitorVRtrID_Type = TmnxVRtrID
_TmnxBgpMonitorVRtrID_Object = MibTableColumn
tmnxBgpMonitorVRtrID = _TmnxBgpMonitorVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 2, 1, 2),
    _TmnxBgpMonitorVRtrID_Type()
)
tmnxBgpMonitorVRtrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBgpMonitorVRtrID.setStatus("current")
_TmnxBgpMonitorPeerGroup_Type = TLNamedItemOrEmpty
_TmnxBgpMonitorPeerGroup_Object = MibTableColumn
tmnxBgpMonitorPeerGroup = _TmnxBgpMonitorPeerGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 2, 1, 3),
    _TmnxBgpMonitorPeerGroup_Type()
)
tmnxBgpMonitorPeerGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBgpMonitorPeerGroup.setStatus("current")


class _TmnxBgpMonitorPeerType_Type(InetAddressType):
    """Custom type tmnxBgpMonitorPeerType based on InetAddressType"""
    defaultValue = 0


_TmnxBgpMonitorPeerType_Type.__name__ = "InetAddressType"
_TmnxBgpMonitorPeerType_Object = MibTableColumn
tmnxBgpMonitorPeerType = _TmnxBgpMonitorPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 2, 1, 4),
    _TmnxBgpMonitorPeerType_Type()
)
tmnxBgpMonitorPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBgpMonitorPeerType.setStatus("current")


class _TmnxBgpMonitorPeer_Type(InetAddress):
    """Custom type tmnxBgpMonitorPeer based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxBgpMonitorPeer_Type.__name__ = "InetAddress"
_TmnxBgpMonitorPeer_Object = MibTableColumn
tmnxBgpMonitorPeer = _TmnxBgpMonitorPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 2, 1, 5),
    _TmnxBgpMonitorPeer_Type()
)
tmnxBgpMonitorPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBgpMonitorPeer.setStatus("current")
_TmnxBgpMonitorRowStatus_Type = RowStatus
_TmnxBgpMonitorRowStatus_Object = MibTableColumn
tmnxBgpMonitorRowStatus = _TmnxBgpMonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 2, 1, 6),
    _TmnxBgpMonitorRowStatus_Type()
)
tmnxBgpMonitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBgpMonitorRowStatus.setStatus("current")


class _TmnxBgpMonitorAdminState_Type(TmnxAdminState):
    """Custom type tmnxBgpMonitorAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxBgpMonitorAdminState_Type.__name__ = "TmnxAdminState"
_TmnxBgpMonitorAdminState_Object = MibTableColumn
tmnxBgpMonitorAdminState = _TmnxBgpMonitorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 2, 1, 7),
    _TmnxBgpMonitorAdminState_Type()
)
tmnxBgpMonitorAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBgpMonitorAdminState.setStatus("current")
_TmnxBgpMonitorLastChanged_Type = TimeStamp
_TmnxBgpMonitorLastChanged_Object = MibTableColumn
tmnxBgpMonitorLastChanged = _TmnxBgpMonitorLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 2, 1, 8),
    _TmnxBgpMonitorLastChanged_Type()
)
tmnxBgpMonitorLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBgpMonitorLastChanged.setStatus("current")
_TmnxBgpMonitorAllStations_Type = TruthValue
_TmnxBgpMonitorAllStations_Object = MibTableColumn
tmnxBgpMonitorAllStations = _TmnxBgpMonitorAllStations_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 2, 1, 9),
    _TmnxBgpMonitorAllStations_Type()
)
tmnxBgpMonitorAllStations.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBgpMonitorAllStations.setStatus("current")


class _TmnxBgpMonitorRouteMonitoring_Type(TmnxBgpMonitorRouteMonitoring):
    """Custom type tmnxBgpMonitorRouteMonitoring based on TmnxBgpMonitorRouteMonitoring"""
    defaultBinValue = "0"


_TmnxBgpMonitorRouteMonitoring_Type.__name__ = "TmnxBgpMonitorRouteMonitoring"
_TmnxBgpMonitorRouteMonitoring_Object = MibTableColumn
tmnxBgpMonitorRouteMonitoring = _TmnxBgpMonitorRouteMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 2, 1, 10),
    _TmnxBgpMonitorRouteMonitoring_Type()
)
tmnxBgpMonitorRouteMonitoring.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBgpMonitorRouteMonitoring.setStatus("current")
_TmnxBgpMonitorStationTable_Object = MibTable
tmnxBgpMonitorStationTable = _TmnxBgpMonitorStationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxBgpMonitorStationTable.setStatus("current")
_TmnxBgpMonitorStationEntry_Object = MibTableRow
tmnxBgpMonitorStationEntry = _TmnxBgpMonitorStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 3, 1)
)
tmnxBgpMonitorStationEntry.setIndexNames(
    (0, "TIMETRA-BMP-MIB", "tmnxBgpMonitorStationType"),
    (0, "TIMETRA-BMP-MIB", "tmnxBgpMonitorStationVRtrID"),
    (0, "TIMETRA-BMP-MIB", "tmnxBgpMonitorStationPeerGroup"),
    (0, "TIMETRA-BMP-MIB", "tmnxBgpMonitorStationPeerType"),
    (0, "TIMETRA-BMP-MIB", "tmnxBgpMonitorStationPeer"),
    (1, "TIMETRA-BMP-MIB", "tmnxBgpMonitorStationName"),
)
if mibBuilder.loadTexts:
    tmnxBgpMonitorStationEntry.setStatus("current")
_TmnxBgpMonitorStationType_Type = TmnxBgpMonitorType
_TmnxBgpMonitorStationType_Object = MibTableColumn
tmnxBgpMonitorStationType = _TmnxBgpMonitorStationType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 3, 1, 1),
    _TmnxBgpMonitorStationType_Type()
)
tmnxBgpMonitorStationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBgpMonitorStationType.setStatus("current")
_TmnxBgpMonitorStationVRtrID_Type = TmnxVRtrID
_TmnxBgpMonitorStationVRtrID_Object = MibTableColumn
tmnxBgpMonitorStationVRtrID = _TmnxBgpMonitorStationVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 3, 1, 2),
    _TmnxBgpMonitorStationVRtrID_Type()
)
tmnxBgpMonitorStationVRtrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBgpMonitorStationVRtrID.setStatus("current")
_TmnxBgpMonitorStationPeerGroup_Type = TLNamedItemOrEmpty
_TmnxBgpMonitorStationPeerGroup_Object = MibTableColumn
tmnxBgpMonitorStationPeerGroup = _TmnxBgpMonitorStationPeerGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 3, 1, 3),
    _TmnxBgpMonitorStationPeerGroup_Type()
)
tmnxBgpMonitorStationPeerGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBgpMonitorStationPeerGroup.setStatus("current")


class _TmnxBgpMonitorStationPeerType_Type(InetAddressType):
    """Custom type tmnxBgpMonitorStationPeerType based on InetAddressType"""
    defaultValue = 0


_TmnxBgpMonitorStationPeerType_Type.__name__ = "InetAddressType"
_TmnxBgpMonitorStationPeerType_Object = MibTableColumn
tmnxBgpMonitorStationPeerType = _TmnxBgpMonitorStationPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 3, 1, 4),
    _TmnxBgpMonitorStationPeerType_Type()
)
tmnxBgpMonitorStationPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBgpMonitorStationPeerType.setStatus("current")


class _TmnxBgpMonitorStationPeer_Type(InetAddress):
    """Custom type tmnxBgpMonitorStationPeer based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxBgpMonitorStationPeer_Type.__name__ = "InetAddress"
_TmnxBgpMonitorStationPeer_Object = MibTableColumn
tmnxBgpMonitorStationPeer = _TmnxBgpMonitorStationPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 3, 1, 5),
    _TmnxBgpMonitorStationPeer_Type()
)
tmnxBgpMonitorStationPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBgpMonitorStationPeer.setStatus("current")
_TmnxBgpMonitorStationName_Type = TNamedItem
_TmnxBgpMonitorStationName_Object = MibTableColumn
tmnxBgpMonitorStationName = _TmnxBgpMonitorStationName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 3, 1, 6),
    _TmnxBgpMonitorStationName_Type()
)
tmnxBgpMonitorStationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBgpMonitorStationName.setStatus("current")
_TmnxBgpMonitorStationRowStatus_Type = RowStatus
_TmnxBgpMonitorStationRowStatus_Object = MibTableColumn
tmnxBgpMonitorStationRowStatus = _TmnxBgpMonitorStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 3, 1, 7),
    _TmnxBgpMonitorStationRowStatus_Type()
)
tmnxBgpMonitorStationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBgpMonitorStationRowStatus.setStatus("current")
_TmnxBmpSessionTable_Object = MibTable
tmnxBmpSessionTable = _TmnxBmpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxBmpSessionTable.setStatus("current")
_TmnxBmpSessionEntry_Object = MibTableRow
tmnxBmpSessionEntry = _TmnxBmpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1)
)
tmnxBmpSessionEntry.setIndexNames(
    (0, "TIMETRA-BMP-MIB", "tmnxBmpSessionVRtrID"),
    (1, "TIMETRA-BMP-MIB", "tmnxBmpSessionStationName"),
)
if mibBuilder.loadTexts:
    tmnxBmpSessionEntry.setStatus("current")
_TmnxBmpSessionVRtrID_Type = TmnxVRtrID
_TmnxBmpSessionVRtrID_Object = MibTableColumn
tmnxBmpSessionVRtrID = _TmnxBmpSessionVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 1),
    _TmnxBmpSessionVRtrID_Type()
)
tmnxBmpSessionVRtrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBmpSessionVRtrID.setStatus("current")
_TmnxBmpSessionStationName_Type = TNamedItem
_TmnxBmpSessionStationName_Object = MibTableColumn
tmnxBmpSessionStationName = _TmnxBmpSessionStationName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 2),
    _TmnxBmpSessionStationName_Type()
)
tmnxBmpSessionStationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBmpSessionStationName.setStatus("current")
_TmnxBmpSessionConnectionState_Type = TmnxBmpSessionConnectionState
_TmnxBmpSessionConnectionState_Object = MibTableColumn
tmnxBmpSessionConnectionState = _TmnxBmpSessionConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 3),
    _TmnxBmpSessionConnectionState_Type()
)
tmnxBmpSessionConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionConnectionState.setStatus("current")
_TmnxBmpSessionLocalAddrType_Type = InetAddressType
_TmnxBmpSessionLocalAddrType_Object = MibTableColumn
tmnxBmpSessionLocalAddrType = _TmnxBmpSessionLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 4),
    _TmnxBmpSessionLocalAddrType_Type()
)
tmnxBmpSessionLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionLocalAddrType.setStatus("current")


class _TmnxBmpSessionLocalAddr_Type(InetAddress):
    """Custom type tmnxBmpSessionLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxBmpSessionLocalAddr_Type.__name__ = "InetAddress"
_TmnxBmpSessionLocalAddr_Object = MibTableColumn
tmnxBmpSessionLocalAddr = _TmnxBmpSessionLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 5),
    _TmnxBmpSessionLocalAddr_Type()
)
tmnxBmpSessionLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionLocalAddr.setStatus("current")
_TmnxBmpSessionLocalAddrPort_Type = InetPortNumber
_TmnxBmpSessionLocalAddrPort_Object = MibTableColumn
tmnxBmpSessionLocalAddrPort = _TmnxBmpSessionLocalAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 6),
    _TmnxBmpSessionLocalAddrPort_Type()
)
tmnxBmpSessionLocalAddrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionLocalAddrPort.setStatus("current")
_TmnxBmpSessionConnStateChanged_Type = TimeStamp
_TmnxBmpSessionConnStateChanged_Object = MibTableColumn
tmnxBmpSessionConnStateChanged = _TmnxBmpSessionConnStateChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 7),
    _TmnxBmpSessionConnStateChanged_Type()
)
tmnxBmpSessionConnStateChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionConnStateChanged.setStatus("current")
_TmnxBmpSessionLastMsgSent_Type = TimeStamp
_TmnxBmpSessionLastMsgSent_Object = MibTableColumn
tmnxBmpSessionLastMsgSent = _TmnxBmpSessionLastMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 8),
    _TmnxBmpSessionLastMsgSent_Type()
)
tmnxBmpSessionLastMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionLastMsgSent.setStatus("current")
_TmnxBmpSessionBytesSent_Type = Counter64
_TmnxBmpSessionBytesSent_Object = MibTableColumn
tmnxBmpSessionBytesSent = _TmnxBmpSessionBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 9),
    _TmnxBmpSessionBytesSent_Type()
)
tmnxBmpSessionBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionBytesSent.setStatus("current")
_TmnxBmpSessionRouteMonitorMsgs_Type = Counter64
_TmnxBmpSessionRouteMonitorMsgs_Object = MibTableColumn
tmnxBmpSessionRouteMonitorMsgs = _TmnxBmpSessionRouteMonitorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 10),
    _TmnxBmpSessionRouteMonitorMsgs_Type()
)
tmnxBmpSessionRouteMonitorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionRouteMonitorMsgs.setStatus("current")
_TmnxBmpSessionStatisticsMsgs_Type = Counter64
_TmnxBmpSessionStatisticsMsgs_Object = MibTableColumn
tmnxBmpSessionStatisticsMsgs = _TmnxBmpSessionStatisticsMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 11),
    _TmnxBmpSessionStatisticsMsgs_Type()
)
tmnxBmpSessionStatisticsMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionStatisticsMsgs.setStatus("current")
_TmnxBmpSessionPeerUpMsgs_Type = Counter64
_TmnxBmpSessionPeerUpMsgs_Object = MibTableColumn
tmnxBmpSessionPeerUpMsgs = _TmnxBmpSessionPeerUpMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 12),
    _TmnxBmpSessionPeerUpMsgs_Type()
)
tmnxBmpSessionPeerUpMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionPeerUpMsgs.setStatus("current")
_TmnxBmpSessionPeerDownMsgs_Type = Counter64
_TmnxBmpSessionPeerDownMsgs_Object = MibTableColumn
tmnxBmpSessionPeerDownMsgs = _TmnxBmpSessionPeerDownMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 13),
    _TmnxBmpSessionPeerDownMsgs_Type()
)
tmnxBmpSessionPeerDownMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionPeerDownMsgs.setStatus("current")
_TmnxBmpSessionInitiationMsgs_Type = Counter64
_TmnxBmpSessionInitiationMsgs_Object = MibTableColumn
tmnxBmpSessionInitiationMsgs = _TmnxBmpSessionInitiationMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 14),
    _TmnxBmpSessionInitiationMsgs_Type()
)
tmnxBmpSessionInitiationMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionInitiationMsgs.setStatus("current")
_TmnxBmpSessionTerminationMsgs_Type = Counter64
_TmnxBmpSessionTerminationMsgs_Object = MibTableColumn
tmnxBmpSessionTerminationMsgs = _TmnxBmpSessionTerminationMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 15),
    _TmnxBmpSessionTerminationMsgs_Type()
)
tmnxBmpSessionTerminationMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionTerminationMsgs.setStatus("current")
_TmnxBmpSessionRouteMirrorMsgs_Type = Counter64
_TmnxBmpSessionRouteMirrorMsgs_Object = MibTableColumn
tmnxBmpSessionRouteMirrorMsgs = _TmnxBmpSessionRouteMirrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 4, 1, 16),
    _TmnxBmpSessionRouteMirrorMsgs_Type()
)
tmnxBmpSessionRouteMirrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBmpSessionRouteMirrorMsgs.setStatus("current")
_TmnxBmpCollectorObjs_ObjectIdentity = ObjectIdentity
tmnxBmpCollectorObjs = _TmnxBmpCollectorObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 5)
)


class _TmnxBmpCollectorAdminState_Type(TmnxAdminState):
    """Custom type tmnxBmpCollectorAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxBmpCollectorAdminState_Type.__name__ = "TmnxAdminState"
_TmnxBmpCollectorAdminState_Object = MibScalar
tmnxBmpCollectorAdminState = _TmnxBmpCollectorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 5, 1),
    _TmnxBmpCollectorAdminState_Type()
)
tmnxBmpCollectorAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBmpCollectorAdminState.setStatus("current")


class _TmnxBmpCollectorIpv4AddrType_Type(InetAddressType):
    """Custom type tmnxBmpCollectorIpv4AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxBmpCollectorIpv4AddrType_Type.__name__ = "InetAddressType"
_TmnxBmpCollectorIpv4AddrType_Object = MibScalar
tmnxBmpCollectorIpv4AddrType = _TmnxBmpCollectorIpv4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 5, 2),
    _TmnxBmpCollectorIpv4AddrType_Type()
)
tmnxBmpCollectorIpv4AddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBmpCollectorIpv4AddrType.setStatus("current")


class _TmnxBmpCollectorIpv4Addr_Type(InetAddress):
    """Custom type tmnxBmpCollectorIpv4Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxBmpCollectorIpv4Addr_Type.__name__ = "InetAddress"
_TmnxBmpCollectorIpv4Addr_Object = MibScalar
tmnxBmpCollectorIpv4Addr = _TmnxBmpCollectorIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 5, 3),
    _TmnxBmpCollectorIpv4Addr_Type()
)
tmnxBmpCollectorIpv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBmpCollectorIpv4Addr.setStatus("current")


class _TmnxBmpCollectorIpv4Port_Type(InetPortNumber):
    """Custom type tmnxBmpCollectorIpv4Port based on InetPortNumber"""
    defaultValue = 4210


_TmnxBmpCollectorIpv4Port_Type.__name__ = "InetPortNumber"
_TmnxBmpCollectorIpv4Port_Object = MibScalar
tmnxBmpCollectorIpv4Port = _TmnxBmpCollectorIpv4Port_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 5, 4),
    _TmnxBmpCollectorIpv4Port_Type()
)
tmnxBmpCollectorIpv4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBmpCollectorIpv4Port.setStatus("current")


class _TmnxBmpCollectorIpv6AddrType_Type(InetAddressType):
    """Custom type tmnxBmpCollectorIpv6AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxBmpCollectorIpv6AddrType_Type.__name__ = "InetAddressType"
_TmnxBmpCollectorIpv6AddrType_Object = MibScalar
tmnxBmpCollectorIpv6AddrType = _TmnxBmpCollectorIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 5, 5),
    _TmnxBmpCollectorIpv6AddrType_Type()
)
tmnxBmpCollectorIpv6AddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBmpCollectorIpv6AddrType.setStatus("current")


class _TmnxBmpCollectorIpv6Addr_Type(InetAddress):
    """Custom type tmnxBmpCollectorIpv6Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxBmpCollectorIpv6Addr_Type.__name__ = "InetAddress"
_TmnxBmpCollectorIpv6Addr_Object = MibScalar
tmnxBmpCollectorIpv6Addr = _TmnxBmpCollectorIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 5, 6),
    _TmnxBmpCollectorIpv6Addr_Type()
)
tmnxBmpCollectorIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBmpCollectorIpv6Addr.setStatus("current")


class _TmnxBmpCollectorIpv6Port_Type(InetPortNumber):
    """Custom type tmnxBmpCollectorIpv6Port based on InetPortNumber"""
    defaultValue = 4210


_TmnxBmpCollectorIpv6Port_Type.__name__ = "InetPortNumber"
_TmnxBmpCollectorIpv6Port_Object = MibScalar
tmnxBmpCollectorIpv6Port = _TmnxBmpCollectorIpv6Port_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 2, 5, 7),
    _TmnxBmpCollectorIpv6Port_Type()
)
tmnxBmpCollectorIpv6Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBmpCollectorIpv6Port.setStatus("current")
_TmnxBmpNotifObjects_ObjectIdentity = ObjectIdentity
tmnxBmpNotifObjects = _TmnxBmpNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 100)
)
_TmnxBmpSessionChangeVRtrID_Type = TmnxVRtrID
_TmnxBmpSessionChangeVRtrID_Object = MibScalar
tmnxBmpSessionChangeVRtrID = _TmnxBmpSessionChangeVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 100, 1),
    _TmnxBmpSessionChangeVRtrID_Type()
)
tmnxBmpSessionChangeVRtrID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBmpSessionChangeVRtrID.setStatus("current")
_TmnxBmpSessionChangeStationName_Type = TNamedItem
_TmnxBmpSessionChangeStationName_Object = MibScalar
tmnxBmpSessionChangeStationName = _TmnxBmpSessionChangeStationName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 100, 2),
    _TmnxBmpSessionChangeStationName_Type()
)
tmnxBmpSessionChangeStationName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBmpSessionChangeStationName.setStatus("current")
_TmnxBmpSessionChangeOldState_Type = TmnxBmpSessionConnectionState
_TmnxBmpSessionChangeOldState_Object = MibScalar
tmnxBmpSessionChangeOldState = _TmnxBmpSessionChangeOldState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 100, 3),
    _TmnxBmpSessionChangeOldState_Type()
)
tmnxBmpSessionChangeOldState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBmpSessionChangeOldState.setStatus("current")
_TmnxBmpSessionChangeNewState_Type = TmnxBmpSessionConnectionState
_TmnxBmpSessionChangeNewState_Object = MibScalar
tmnxBmpSessionChangeNewState = _TmnxBmpSessionChangeNewState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 100, 4),
    _TmnxBmpSessionChangeNewState_Type()
)
tmnxBmpSessionChangeNewState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBmpSessionChangeNewState.setStatus("current")


class _TmnxBmpSessionChangeReason_Type(DisplayString):
    """Custom type tmnxBmpSessionChangeReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxBmpSessionChangeReason_Type.__name__ = "DisplayString"
_TmnxBmpSessionChangeReason_Object = MibScalar
tmnxBmpSessionChangeReason = _TmnxBmpSessionChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 108, 100, 5),
    _TmnxBmpSessionChangeReason_Type()
)
tmnxBmpSessionChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBmpSessionChangeReason.setStatus("current")
_TmnxBmpNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxBmpNotifyPrefix = _TmnxBmpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 108)
)
_TmnxBmpNotifications_ObjectIdentity = ObjectIdentity
tmnxBmpNotifications = _TmnxBmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 108, 0)
)

# Managed Objects groups

tmnxBmpConfigV15Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 2, 1, 1)
)
tmnxBmpConfigV15Group.setObjects(
      *(("TIMETRA-BMP-MIB", "tmnxBmpAdminState"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationTableLastCh"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationRowStatus"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationLastChanged"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationAdminState"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationDescr"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationConnectRetry"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationInitialWaitTime"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationSecondWaitTime"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationMaxWaitTime"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationErrorInterval"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationLocalIpAddrType"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationLocalIpAddress"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationRemoteIpAddrType"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationRemoteIpAddress"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationRemotePort"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationMode"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationRouter"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationInitiationMessage"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationStatsReportIvl"),
        ("TIMETRA-BMP-MIB", "tmnxBgpMonitorTableLastCh"),
        ("TIMETRA-BMP-MIB", "tmnxBgpMonitorRowStatus"),
        ("TIMETRA-BMP-MIB", "tmnxBgpMonitorAdminState"),
        ("TIMETRA-BMP-MIB", "tmnxBgpMonitorLastChanged"),
        ("TIMETRA-BMP-MIB", "tmnxBgpMonitorAllStations"),
        ("TIMETRA-BMP-MIB", "tmnxBgpMonitorRouteMonitoring"),
        ("TIMETRA-BMP-MIB", "tmnxBgpMonitorStationRowStatus"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationTcpKaAdminState"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationTcpKaIdle"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationTcpKaInterval"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationTcpKaCount"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionConnectionState"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionLocalAddrType"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionLocalAddr"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionLocalAddrPort"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionConnStateChanged"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionLastMsgSent"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionBytesSent"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionRouteMonitorMsgs"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionStatisticsMsgs"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionPeerUpMsgs"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionPeerDownMsgs"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionInitiationMsgs"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionTerminationMsgs"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionRouteMirrorMsgs"))
)
if mibBuilder.loadTexts:
    tmnxBmpConfigV15Group.setStatus("current")

tmnxBmpConfigV16Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 2, 2, 1)
)
tmnxBmpConfigV16Group.setObjects(
      *(("TIMETRA-BMP-MIB", "tmnxBmpStationRoutesReportIvl"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationReportLocalRoutes"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationFamily"))
)
if mibBuilder.loadTexts:
    tmnxBmpConfigV16Group.setStatus("current")

tmnxBmpObsoletedConfigV16Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 2, 2, 2)
)
tmnxBmpObsoletedConfigV16Group.setObjects(
      *(("TIMETRA-BMP-MIB", "tmnxBmpStationMode"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationInitialWaitTime"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationSecondWaitTime"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationMaxWaitTime"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationErrorInterval"),
        ("TIMETRA-BMP-MIB", "tmnxBmpStationRoutesReportIvl"))
)
if mibBuilder.loadTexts:
    tmnxBmpObsoletedConfigV16Group.setStatus("current")

tmnxBmpNotificationObjs = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 2, 2, 3)
)
tmnxBmpNotificationObjs.setObjects(
      *(("TIMETRA-BMP-MIB", "tmnxBmpSessionChangeVRtrID"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionChangeStationName"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionChangeOldState"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionChangeNewState"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionChangeReason"))
)
if mibBuilder.loadTexts:
    tmnxBmpNotificationObjs.setStatus("current")

tmnxBmpConfigV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 2, 3, 1)
)
tmnxBmpConfigV19v0Group.setObjects(
      *(("TIMETRA-BMP-MIB", "tmnxBmpCollectorAdminState"),
        ("TIMETRA-BMP-MIB", "tmnxBmpCollectorIpv4AddrType"),
        ("TIMETRA-BMP-MIB", "tmnxBmpCollectorIpv4Addr"),
        ("TIMETRA-BMP-MIB", "tmnxBmpCollectorIpv4Port"),
        ("TIMETRA-BMP-MIB", "tmnxBmpCollectorIpv6AddrType"),
        ("TIMETRA-BMP-MIB", "tmnxBmpCollectorIpv6Addr"),
        ("TIMETRA-BMP-MIB", "tmnxBmpCollectorIpv6Port"))
)
if mibBuilder.loadTexts:
    tmnxBmpConfigV19v0Group.setStatus("current")


# Notification objects

tmnxBmpSessionStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 108, 0, 1)
)
tmnxBmpSessionStatusChange.setObjects(
      *(("TIMETRA-BMP-MIB", "tmnxBmpSessionChangeVRtrID"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionChangeStationName"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionChangeOldState"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionChangeNewState"),
        ("TIMETRA-BMP-MIB", "tmnxBmpSessionChangeReason"))
)
if mibBuilder.loadTexts:
    tmnxBmpSessionStatusChange.setStatus(
        "current"
    )


# Notifications groups

tmnxBmpNotificationV16Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 2, 2, 4)
)
tmnxBmpNotificationV16Group.setObjects(
    ("TIMETRA-BMP-MIB", "tmnxBmpSessionStatusChange")
)
if mibBuilder.loadTexts:
    tmnxBmpNotificationV16Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxBmpComplianceV15v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 1, 1)
)
tmnxBmpComplianceV15v0.setObjects(
    ("TIMETRA-BMP-MIB", "tmnxBmpConfigV15Group")
)
if mibBuilder.loadTexts:
    tmnxBmpComplianceV15v0.setStatus(
        "current"
    )

tmnxBmpComplianceV16v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 1, 2)
)
tmnxBmpComplianceV16v0.setObjects(
      *(("TIMETRA-BMP-MIB", "tmnxBmpConfigV16Group"),
        ("TIMETRA-BMP-MIB", "tmnxBmpNotificationObjs"),
        ("TIMETRA-BMP-MIB", "tmnxBmpNotificationV16Group"))
)
if mibBuilder.loadTexts:
    tmnxBmpComplianceV16v0.setStatus(
        "current"
    )

tmnxBmpComplianceV19v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 108, 1, 3)
)
tmnxBmpComplianceV19v0.setObjects(
    ("TIMETRA-BMP-MIB", "tmnxBmpConfigV19v0Group")
)
if mibBuilder.loadTexts:
    tmnxBmpComplianceV19v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-BMP-MIB",
    **{"TmnxBmpConnectionMode": TmnxBmpConnectionMode,
       "TmnxBgpMonitorType": TmnxBgpMonitorType,
       "TmnxBgpMonitorRouteMonitoring": TmnxBgpMonitorRouteMonitoring,
       "TmnxBmpSessionConnectionState": TmnxBmpSessionConnectionState,
       "timetraBmpMIBModule": timetraBmpMIBModule,
       "tmnxBmpConformance": tmnxBmpConformance,
       "tmnxBmpCompliances": tmnxBmpCompliances,
       "tmnxBmpComplianceV15v0": tmnxBmpComplianceV15v0,
       "tmnxBmpComplianceV16v0": tmnxBmpComplianceV16v0,
       "tmnxBmpComplianceV19v0": tmnxBmpComplianceV19v0,
       "tmnxBmpGroups": tmnxBmpGroups,
       "tmnxBmpV15v0Groups": tmnxBmpV15v0Groups,
       "tmnxBmpConfigV15Group": tmnxBmpConfigV15Group,
       "tmnxBmpV16v0Groups": tmnxBmpV16v0Groups,
       "tmnxBmpConfigV16Group": tmnxBmpConfigV16Group,
       "tmnxBmpObsoletedConfigV16Group": tmnxBmpObsoletedConfigV16Group,
       "tmnxBmpNotificationObjs": tmnxBmpNotificationObjs,
       "tmnxBmpNotificationV16Group": tmnxBmpNotificationV16Group,
       "tmnxBmpV19v0Groups": tmnxBmpV19v0Groups,
       "tmnxBmpConfigV19v0Group": tmnxBmpConfigV19v0Group,
       "tmnxBmpObjs": tmnxBmpObjs,
       "tmnxBmpParameterObjs": tmnxBmpParameterObjs,
       "tmnxBmpAdminState": tmnxBmpAdminState,
       "tmnxBmpStationTableLastCh": tmnxBmpStationTableLastCh,
       "tmnxBgpMonitorTableLastCh": tmnxBgpMonitorTableLastCh,
       "tmnxBmpStationObjs": tmnxBmpStationObjs,
       "tmnxBmpStationTable": tmnxBmpStationTable,
       "tmnxBmpStationEntry": tmnxBmpStationEntry,
       "tmnxBmpStationName": tmnxBmpStationName,
       "tmnxBmpStationRowStatus": tmnxBmpStationRowStatus,
       "tmnxBmpStationLastChanged": tmnxBmpStationLastChanged,
       "tmnxBmpStationAdminState": tmnxBmpStationAdminState,
       "tmnxBmpStationDescr": tmnxBmpStationDescr,
       "tmnxBmpStationConnectRetry": tmnxBmpStationConnectRetry,
       "tmnxBmpStationInitialWaitTime": tmnxBmpStationInitialWaitTime,
       "tmnxBmpStationSecondWaitTime": tmnxBmpStationSecondWaitTime,
       "tmnxBmpStationMaxWaitTime": tmnxBmpStationMaxWaitTime,
       "tmnxBmpStationErrorInterval": tmnxBmpStationErrorInterval,
       "tmnxBmpStationLocalIpAddrType": tmnxBmpStationLocalIpAddrType,
       "tmnxBmpStationLocalIpAddress": tmnxBmpStationLocalIpAddress,
       "tmnxBmpStationRemoteIpAddrType": tmnxBmpStationRemoteIpAddrType,
       "tmnxBmpStationRemoteIpAddress": tmnxBmpStationRemoteIpAddress,
       "tmnxBmpStationRemotePort": tmnxBmpStationRemotePort,
       "tmnxBmpStationMode": tmnxBmpStationMode,
       "tmnxBmpStationRouter": tmnxBmpStationRouter,
       "tmnxBmpStationInitiationMessage": tmnxBmpStationInitiationMessage,
       "tmnxBmpStationStatsReportIvl": tmnxBmpStationStatsReportIvl,
       "tmnxBmpStationTcpKaAdminState": tmnxBmpStationTcpKaAdminState,
       "tmnxBmpStationTcpKaIdle": tmnxBmpStationTcpKaIdle,
       "tmnxBmpStationTcpKaInterval": tmnxBmpStationTcpKaInterval,
       "tmnxBmpStationTcpKaCount": tmnxBmpStationTcpKaCount,
       "tmnxBmpStationRoutesReportIvl": tmnxBmpStationRoutesReportIvl,
       "tmnxBmpStationReportLocalRoutes": tmnxBmpStationReportLocalRoutes,
       "tmnxBmpStationFamily": tmnxBmpStationFamily,
       "tmnxBgpMonitorTable": tmnxBgpMonitorTable,
       "tmnxBgpMonitorEntry": tmnxBgpMonitorEntry,
       "tmnxBgpMonitorType": tmnxBgpMonitorType,
       "tmnxBgpMonitorVRtrID": tmnxBgpMonitorVRtrID,
       "tmnxBgpMonitorPeerGroup": tmnxBgpMonitorPeerGroup,
       "tmnxBgpMonitorPeerType": tmnxBgpMonitorPeerType,
       "tmnxBgpMonitorPeer": tmnxBgpMonitorPeer,
       "tmnxBgpMonitorRowStatus": tmnxBgpMonitorRowStatus,
       "tmnxBgpMonitorAdminState": tmnxBgpMonitorAdminState,
       "tmnxBgpMonitorLastChanged": tmnxBgpMonitorLastChanged,
       "tmnxBgpMonitorAllStations": tmnxBgpMonitorAllStations,
       "tmnxBgpMonitorRouteMonitoring": tmnxBgpMonitorRouteMonitoring,
       "tmnxBgpMonitorStationTable": tmnxBgpMonitorStationTable,
       "tmnxBgpMonitorStationEntry": tmnxBgpMonitorStationEntry,
       "tmnxBgpMonitorStationType": tmnxBgpMonitorStationType,
       "tmnxBgpMonitorStationVRtrID": tmnxBgpMonitorStationVRtrID,
       "tmnxBgpMonitorStationPeerGroup": tmnxBgpMonitorStationPeerGroup,
       "tmnxBgpMonitorStationPeerType": tmnxBgpMonitorStationPeerType,
       "tmnxBgpMonitorStationPeer": tmnxBgpMonitorStationPeer,
       "tmnxBgpMonitorStationName": tmnxBgpMonitorStationName,
       "tmnxBgpMonitorStationRowStatus": tmnxBgpMonitorStationRowStatus,
       "tmnxBmpSessionTable": tmnxBmpSessionTable,
       "tmnxBmpSessionEntry": tmnxBmpSessionEntry,
       "tmnxBmpSessionVRtrID": tmnxBmpSessionVRtrID,
       "tmnxBmpSessionStationName": tmnxBmpSessionStationName,
       "tmnxBmpSessionConnectionState": tmnxBmpSessionConnectionState,
       "tmnxBmpSessionLocalAddrType": tmnxBmpSessionLocalAddrType,
       "tmnxBmpSessionLocalAddr": tmnxBmpSessionLocalAddr,
       "tmnxBmpSessionLocalAddrPort": tmnxBmpSessionLocalAddrPort,
       "tmnxBmpSessionConnStateChanged": tmnxBmpSessionConnStateChanged,
       "tmnxBmpSessionLastMsgSent": tmnxBmpSessionLastMsgSent,
       "tmnxBmpSessionBytesSent": tmnxBmpSessionBytesSent,
       "tmnxBmpSessionRouteMonitorMsgs": tmnxBmpSessionRouteMonitorMsgs,
       "tmnxBmpSessionStatisticsMsgs": tmnxBmpSessionStatisticsMsgs,
       "tmnxBmpSessionPeerUpMsgs": tmnxBmpSessionPeerUpMsgs,
       "tmnxBmpSessionPeerDownMsgs": tmnxBmpSessionPeerDownMsgs,
       "tmnxBmpSessionInitiationMsgs": tmnxBmpSessionInitiationMsgs,
       "tmnxBmpSessionTerminationMsgs": tmnxBmpSessionTerminationMsgs,
       "tmnxBmpSessionRouteMirrorMsgs": tmnxBmpSessionRouteMirrorMsgs,
       "tmnxBmpCollectorObjs": tmnxBmpCollectorObjs,
       "tmnxBmpCollectorAdminState": tmnxBmpCollectorAdminState,
       "tmnxBmpCollectorIpv4AddrType": tmnxBmpCollectorIpv4AddrType,
       "tmnxBmpCollectorIpv4Addr": tmnxBmpCollectorIpv4Addr,
       "tmnxBmpCollectorIpv4Port": tmnxBmpCollectorIpv4Port,
       "tmnxBmpCollectorIpv6AddrType": tmnxBmpCollectorIpv6AddrType,
       "tmnxBmpCollectorIpv6Addr": tmnxBmpCollectorIpv6Addr,
       "tmnxBmpCollectorIpv6Port": tmnxBmpCollectorIpv6Port,
       "tmnxBmpNotifObjects": tmnxBmpNotifObjects,
       "tmnxBmpSessionChangeVRtrID": tmnxBmpSessionChangeVRtrID,
       "tmnxBmpSessionChangeStationName": tmnxBmpSessionChangeStationName,
       "tmnxBmpSessionChangeOldState": tmnxBmpSessionChangeOldState,
       "tmnxBmpSessionChangeNewState": tmnxBmpSessionChangeNewState,
       "tmnxBmpSessionChangeReason": tmnxBmpSessionChangeReason,
       "tmnxBmpNotifyPrefix": tmnxBmpNotifyPrefix,
       "tmnxBmpNotifications": tmnxBmpNotifications,
       "tmnxBmpSessionStatusChange": tmnxBmpSessionStatusChange}
)
