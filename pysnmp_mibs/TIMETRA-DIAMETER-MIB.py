# SNMP MIB module (TIMETRA-DIAMETER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-DIAMETER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:03:08 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TEgressPolicerIdOrNone,
 TEgressQueueId,
 TIngressPolicerIdOrNone,
 TIngressQueueId,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAuthPassword,
 TmnxBinarySpecification,
 TmnxDiamCcFailureHndlng,
 TmnxEnabledDisabledAdminState,
 TmnxMacSpecification,
 TmnxSubAuthPlcyUserNameOp,
 TmnxSubCallingStationIdType,
 TmnxSubCreditVolumeUnit,
 TmnxSubHostGrouping,
 TmnxSubNasPortPrefixType,
 TmnxSubNasPortSuffixType,
 TmnxSubNasPortTypeType,
 TmnxVRtrID,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TEgressPolicerIdOrNone",
    "TEgressQueueId",
    "TIngressPolicerIdOrNone",
    "TIngressQueueId",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAuthPassword",
    "TmnxBinarySpecification",
    "TmnxDiamCcFailureHndlng",
    "TmnxEnabledDisabledAdminState",
    "TmnxMacSpecification",
    "TmnxSubAuthPlcyUserNameOp",
    "TmnxSubCallingStationIdType",
    "TmnxSubCreditVolumeUnit",
    "TmnxSubHostGrouping",
    "TmnxSubNasPortPrefixType",
    "TmnxSubNasPortSuffixType",
    "TmnxSubNasPortTypeType",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero")


# MODULE-IDENTITY

timetraDiameterMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 58)
)
if mibBuilder.loadTexts:
    timetraDiameterMIBModule.setRevisions(
        ("2019-03-15 00:00",
         "2017-01-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2012-02-28 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxDiamPeerTransportProt(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tcp", 1)
    )



class TmnxDiamDccaApplicationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vfDccaV2", 1),
          ("gx", 2))
    )



class TmnxDiamPeerState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("wait-conn-ack", 1),
          ("wait-i-cea", 2),
          ("i-open", 3),
          ("closing", 4),
          ("r-open", 5),
          ("wait-r-cer", 6))
    )



class TmnxDiamPlcyVendorSupportType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vodafone", 1),
          ("threeGpp", 2))
    )



class TmnxDiamPlcyDccaAvpOriginType(TextualConvention, Integer32):
    status = "current"
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
        *(("disabled", 0),
          ("subscriberId", 1),
          ("circuitId", 2),
          ("imsi", 3),
          ("msisdn", 4),
          ("imei", 5),
          ("dualStackRemoteId", 6),
          ("mac", 7),
          ("username", 8),
          ("nasPortId", 9))
    )



class TmnxDiamProxyState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("active", 2),
          ("standby", 3),
          ("activeWait", 4),
          ("standbyWait", 5),
          ("proxySwitchoverReq", 6))
    )



class TmnxDiamSessionId(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 102),
    )



class TmnxDiamFqdn(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )



class TmnxDiamFqdnOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class TmnxDiamApGx3gqmAADlMappingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noMapping", 0),
          ("arbiter", 1),
          ("policer", 2),
          ("queue", 3),
          ("scheduler", 4),
          ("aggregateRate", 5),
          ("hsSlaAggregateRate", 6))
    )



class TmnxDiamApGx3gqmAAUlMappingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noMapping", 0),
          ("arbiter", 1),
          ("policer", 2),
          ("queue", 3),
          ("scheduler", 4))
    )



class TmnxDiamNdPeerMcState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("init", 1),
          ("waitLocal", 2),
          ("waitRemote", 3),
          ("active", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxDiameterConformance_ObjectIdentity = ObjectIdentity
tmnxDiameterConformance = _TmnxDiameterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58)
)
_TmnxDiameterCompliances_ObjectIdentity = ObjectIdentity
tmnxDiameterCompliances = _TmnxDiameterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1)
)
_TmnxDiameterGroups_ObjectIdentity = ObjectIdentity
tmnxDiameterGroups = _TmnxDiameterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2)
)
_TmnxDiameter_ObjectIdentity = ObjectIdentity
tmnxDiameter = _TmnxDiameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58)
)
_TmnxDiameterBaseObjects_ObjectIdentity = ObjectIdentity
tmnxDiameterBaseObjects = _TmnxDiameterBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1)
)
_TmnxDiameterPlcyTableLastChngd_Type = TimeStamp
_TmnxDiameterPlcyTableLastChngd_Object = MibScalar
tmnxDiameterPlcyTableLastChngd = _TmnxDiameterPlcyTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 1),
    _TmnxDiameterPlcyTableLastChngd_Type()
)
tmnxDiameterPlcyTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiameterPlcyTableLastChngd.setStatus("current")
_TmnxDiameterPlcyTable_Object = MibTable
tmnxDiameterPlcyTable = _TmnxDiameterPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxDiameterPlcyTable.setStatus("current")
_TmnxDiameterPlcyEntry_Object = MibTableRow
tmnxDiameterPlcyEntry = _TmnxDiameterPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1)
)
tmnxDiameterPlcyEntry.setIndexNames(
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxDiameterPlcyEntry.setStatus("current")
_TmnxDiamPlcyName_Type = TNamedItem
_TmnxDiamPlcyName_Object = MibTableColumn
tmnxDiamPlcyName = _TmnxDiamPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 1),
    _TmnxDiamPlcyName_Type()
)
tmnxDiamPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPlcyName.setStatus("current")
_TmnxDiamPlcyRowStatus_Type = RowStatus
_TmnxDiamPlcyRowStatus_Object = MibTableColumn
tmnxDiamPlcyRowStatus = _TmnxDiamPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 2),
    _TmnxDiamPlcyRowStatus_Type()
)
tmnxDiamPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyRowStatus.setStatus("current")
_TmnxDiamPlcyLastMgmtChange_Type = TimeStamp
_TmnxDiamPlcyLastMgmtChange_Object = MibTableColumn
tmnxDiamPlcyLastMgmtChange = _TmnxDiamPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 3),
    _TmnxDiamPlcyLastMgmtChange_Type()
)
tmnxDiamPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPlcyLastMgmtChange.setStatus("current")


class _TmnxDiamPlcyDescription_Type(TItemDescription):
    """Custom type tmnxDiamPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxDiamPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxDiamPlcyDescription_Object = MibTableColumn
tmnxDiamPlcyDescription = _TmnxDiamPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 4),
    _TmnxDiamPlcyDescription_Type()
)
tmnxDiamPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDescription.setStatus("current")


class _TmnxDiamPlcyOriginHost_Type(DisplayString):
    """Custom type tmnxDiamPlcyOriginHost based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxDiamPlcyOriginHost_Type.__name__ = "DisplayString"
_TmnxDiamPlcyOriginHost_Object = MibTableColumn
tmnxDiamPlcyOriginHost = _TmnxDiamPlcyOriginHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 5),
    _TmnxDiamPlcyOriginHost_Type()
)
tmnxDiamPlcyOriginHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyOriginHost.setStatus("current")


class _TmnxDiamPlcyOriginRealm_Type(DisplayString):
    """Custom type tmnxDiamPlcyOriginRealm based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxDiamPlcyOriginRealm_Type.__name__ = "DisplayString"
_TmnxDiamPlcyOriginRealm_Object = MibTableColumn
tmnxDiamPlcyOriginRealm = _TmnxDiamPlcyOriginRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 6),
    _TmnxDiamPlcyOriginRealm_Type()
)
tmnxDiamPlcyOriginRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyOriginRealm.setStatus("current")


class _TmnxDiamPlcyRouter_Type(TmnxVRtrID):
    """Custom type tmnxDiamPlcyRouter based on TmnxVRtrID"""
    defaultValue = 1


_TmnxDiamPlcyRouter_Type.__name__ = "TmnxVRtrID"
_TmnxDiamPlcyRouter_Object = MibTableColumn
tmnxDiamPlcyRouter = _TmnxDiamPlcyRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 7),
    _TmnxDiamPlcyRouter_Type()
)
tmnxDiamPlcyRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyRouter.setStatus("current")


class _TmnxDiamPlcySourceAddrType_Type(InetAddressType):
    """Custom type tmnxDiamPlcySourceAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxDiamPlcySourceAddrType_Type.__name__ = "InetAddressType"
_TmnxDiamPlcySourceAddrType_Object = MibTableColumn
tmnxDiamPlcySourceAddrType = _TmnxDiamPlcySourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 8),
    _TmnxDiamPlcySourceAddrType_Type()
)
tmnxDiamPlcySourceAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcySourceAddrType.setStatus("current")


class _TmnxDiamPlcySourceAddr_Type(InetAddress):
    """Custom type tmnxDiamPlcySourceAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxDiamPlcySourceAddr_Type.__name__ = "InetAddress"
_TmnxDiamPlcySourceAddr_Object = MibTableColumn
tmnxDiamPlcySourceAddr = _TmnxDiamPlcySourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 9),
    _TmnxDiamPlcySourceAddr_Type()
)
tmnxDiamPlcySourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcySourceAddr.setStatus("current")


class _TmnxDiamPlcyWatchdogTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyWatchdogTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxDiamPlcyWatchdogTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyWatchdogTimer_Object = MibTableColumn
tmnxDiamPlcyWatchdogTimer = _TmnxDiamPlcyWatchdogTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 10),
    _TmnxDiamPlcyWatchdogTimer_Type()
)
tmnxDiamPlcyWatchdogTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyWatchdogTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamPlcyWatchdogTimer.setUnits("seconds")


class _TmnxDiamPlcyConnectionTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyConnectionTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxDiamPlcyConnectionTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyConnectionTimer_Object = MibTableColumn
tmnxDiamPlcyConnectionTimer = _TmnxDiamPlcyConnectionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 11),
    _TmnxDiamPlcyConnectionTimer_Type()
)
tmnxDiamPlcyConnectionTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyConnectionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamPlcyConnectionTimer.setUnits("seconds")


class _TmnxDiamPlcyTransactionTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyTransactionTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxDiamPlcyTransactionTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyTransactionTimer_Object = MibTableColumn
tmnxDiamPlcyTransactionTimer = _TmnxDiamPlcyTransactionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 12),
    _TmnxDiamPlcyTransactionTimer_Type()
)
tmnxDiamPlcyTransactionTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyTransactionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamPlcyTransactionTimer.setUnits("seconds")


class _TmnxDiamPlcyVendorSupport_Type(TmnxDiamPlcyVendorSupportType):
    """Custom type tmnxDiamPlcyVendorSupport based on TmnxDiamPlcyVendorSupportType"""
    defaultValue = 2


_TmnxDiamPlcyVendorSupport_Type.__name__ = "TmnxDiamPlcyVendorSupportType"
_TmnxDiamPlcyVendorSupport_Object = MibTableColumn
tmnxDiamPlcyVendorSupport = _TmnxDiamPlcyVendorSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 13),
    _TmnxDiamPlcyVendorSupport_Type()
)
tmnxDiamPlcyVendorSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyVendorSupport.setStatus("current")


class _TmnxDiamPlcyApplications_Type(Bits):
    """Custom type tmnxDiamPlcyApplications based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("gx", 0),
          ("gy", 1),
          ("nasreq", 2))
    )

_TmnxDiamPlcyApplications_Type.__name__ = "Bits"
_TmnxDiamPlcyApplications_Object = MibTableColumn
tmnxDiamPlcyApplications = _TmnxDiamPlcyApplications_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 15),
    _TmnxDiamPlcyApplications_Type()
)
tmnxDiamPlcyApplications.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyApplications.setStatus("current")


class _TmnxDiamPlcyPythonPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxDiamPlcyPythonPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDiamPlcyPythonPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDiamPlcyPythonPolicy_Object = MibTableColumn
tmnxDiamPlcyPythonPolicy = _TmnxDiamPlcyPythonPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 16),
    _TmnxDiamPlcyPythonPolicy_Type()
)
tmnxDiamPlcyPythonPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPythonPolicy.setStatus("current")


class _TmnxDiamPlcyRole_Type(Integer32):
    """Custom type tmnxDiamPlcyRole based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("client", 0),
          ("proxy", 1))
    )


_TmnxDiamPlcyRole_Type.__name__ = "Integer32"
_TmnxDiamPlcyRole_Object = MibTableColumn
tmnxDiamPlcyRole = _TmnxDiamPlcyRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 17),
    _TmnxDiamPlcyRole_Type()
)
tmnxDiamPlcyRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyRole.setStatus("current")


class _TmnxDiamPlcyV6SourceAddrType_Type(InetAddressType):
    """Custom type tmnxDiamPlcyV6SourceAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxDiamPlcyV6SourceAddrType_Type.__name__ = "InetAddressType"
_TmnxDiamPlcyV6SourceAddrType_Object = MibTableColumn
tmnxDiamPlcyV6SourceAddrType = _TmnxDiamPlcyV6SourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 18),
    _TmnxDiamPlcyV6SourceAddrType_Type()
)
tmnxDiamPlcyV6SourceAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyV6SourceAddrType.setStatus("current")


class _TmnxDiamPlcyV6SourceAddr_Type(InetAddress):
    """Custom type tmnxDiamPlcyV6SourceAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxDiamPlcyV6SourceAddr_Type.__name__ = "InetAddress"
_TmnxDiamPlcyV6SourceAddr_Object = MibTableColumn
tmnxDiamPlcyV6SourceAddr = _TmnxDiamPlcyV6SourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 2, 1, 19),
    _TmnxDiamPlcyV6SourceAddr_Type()
)
tmnxDiamPlcyV6SourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyV6SourceAddr.setStatus("current")
_TmnxDiamPlcyPeerTableLastChngd_Type = TimeStamp
_TmnxDiamPlcyPeerTableLastChngd_Object = MibScalar
tmnxDiamPlcyPeerTableLastChngd = _TmnxDiamPlcyPeerTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 3),
    _TmnxDiamPlcyPeerTableLastChngd_Type()
)
tmnxDiamPlcyPeerTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerTableLastChngd.setStatus("current")
_TmnxDiameterPlcyPeerTable_Object = MibTable
tmnxDiameterPlcyPeerTable = _TmnxDiameterPlcyPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxDiameterPlcyPeerTable.setStatus("current")
_TmnxDiameterPlcyPeerEntry_Object = MibTableRow
tmnxDiameterPlcyPeerEntry = _TmnxDiameterPlcyPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1)
)
tmnxDiameterPlcyPeerEntry.setIndexNames(
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyName"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerName"),
)
if mibBuilder.loadTexts:
    tmnxDiameterPlcyPeerEntry.setStatus("current")
_TmnxDiamPlcyPeerName_Type = TNamedItem
_TmnxDiamPlcyPeerName_Object = MibTableColumn
tmnxDiamPlcyPeerName = _TmnxDiamPlcyPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 1),
    _TmnxDiamPlcyPeerName_Type()
)
tmnxDiamPlcyPeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerName.setStatus("current")
_TmnxDiamPlcyPeerRowStatus_Type = RowStatus
_TmnxDiamPlcyPeerRowStatus_Object = MibTableColumn
tmnxDiamPlcyPeerRowStatus = _TmnxDiamPlcyPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 2),
    _TmnxDiamPlcyPeerRowStatus_Type()
)
tmnxDiamPlcyPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerRowStatus.setStatus("current")
_TmnxDiamPlcyPeerLastMgmtChange_Type = TimeStamp
_TmnxDiamPlcyPeerLastMgmtChange_Object = MibTableColumn
tmnxDiamPlcyPeerLastMgmtChange = _TmnxDiamPlcyPeerLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 3),
    _TmnxDiamPlcyPeerLastMgmtChange_Type()
)
tmnxDiamPlcyPeerLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerLastMgmtChange.setStatus("current")


class _TmnxDiamPlcyPeerAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxDiamPlcyPeerAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxDiamPlcyPeerAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxDiamPlcyPeerAdminState_Object = MibTableColumn
tmnxDiamPlcyPeerAdminState = _TmnxDiamPlcyPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 4),
    _TmnxDiamPlcyPeerAdminState_Type()
)
tmnxDiamPlcyPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerAdminState.setStatus("current")


class _TmnxDiamPlcyPeerAddrType_Type(InetAddressType):
    """Custom type tmnxDiamPlcyPeerAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxDiamPlcyPeerAddrType_Type.__name__ = "InetAddressType"
_TmnxDiamPlcyPeerAddrType_Object = MibTableColumn
tmnxDiamPlcyPeerAddrType = _TmnxDiamPlcyPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 5),
    _TmnxDiamPlcyPeerAddrType_Type()
)
tmnxDiamPlcyPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerAddrType.setStatus("current")


class _TmnxDiamPlcyPeerAddr_Type(InetAddress):
    """Custom type tmnxDiamPlcyPeerAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDiamPlcyPeerAddr_Type.__name__ = "InetAddress"
_TmnxDiamPlcyPeerAddr_Object = MibTableColumn
tmnxDiamPlcyPeerAddr = _TmnxDiamPlcyPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 6),
    _TmnxDiamPlcyPeerAddr_Type()
)
tmnxDiamPlcyPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerAddr.setStatus("current")


class _TmnxDiamPlcyPeerTransportProt_Type(TmnxDiamPeerTransportProt):
    """Custom type tmnxDiamPlcyPeerTransportProt based on TmnxDiamPeerTransportProt"""
    defaultValue = 1


_TmnxDiamPlcyPeerTransportProt_Type.__name__ = "TmnxDiamPeerTransportProt"
_TmnxDiamPlcyPeerTransportProt_Object = MibTableColumn
tmnxDiamPlcyPeerTransportProt = _TmnxDiamPlcyPeerTransportProt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 7),
    _TmnxDiamPlcyPeerTransportProt_Type()
)
tmnxDiamPlcyPeerTransportProt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerTransportProt.setStatus("current")


class _TmnxDiamPlcyPeerTransportPort_Type(Unsigned32):
    """Custom type tmnxDiamPlcyPeerTransportPort based on Unsigned32"""
    defaultValue = 3868

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxDiamPlcyPeerTransportPort_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyPeerTransportPort_Object = MibTableColumn
tmnxDiamPlcyPeerTransportPort = _TmnxDiamPlcyPeerTransportPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 8),
    _TmnxDiamPlcyPeerTransportPort_Type()
)
tmnxDiamPlcyPeerTransportPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerTransportPort.setStatus("current")


class _TmnxDiamPlcyPeerDestHost_Type(DisplayString):
    """Custom type tmnxDiamPlcyPeerDestHost based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxDiamPlcyPeerDestHost_Type.__name__ = "DisplayString"
_TmnxDiamPlcyPeerDestHost_Object = MibTableColumn
tmnxDiamPlcyPeerDestHost = _TmnxDiamPlcyPeerDestHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 9),
    _TmnxDiamPlcyPeerDestHost_Type()
)
tmnxDiamPlcyPeerDestHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerDestHost.setStatus("current")


class _TmnxDiamPlcyPeerDestRealm_Type(DisplayString):
    """Custom type tmnxDiamPlcyPeerDestRealm based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxDiamPlcyPeerDestRealm_Type.__name__ = "DisplayString"
_TmnxDiamPlcyPeerDestRealm_Object = MibTableColumn
tmnxDiamPlcyPeerDestRealm = _TmnxDiamPlcyPeerDestRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 10),
    _TmnxDiamPlcyPeerDestRealm_Type()
)
tmnxDiamPlcyPeerDestRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerDestRealm.setStatus("current")


class _TmnxDiamPlcyPeerWatchdogTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyPeerWatchdogTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxDiamPlcyPeerWatchdogTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyPeerWatchdogTimer_Object = MibTableColumn
tmnxDiamPlcyPeerWatchdogTimer = _TmnxDiamPlcyPeerWatchdogTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 11),
    _TmnxDiamPlcyPeerWatchdogTimer_Type()
)
tmnxDiamPlcyPeerWatchdogTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerWatchdogTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerWatchdogTimer.setUnits("seconds")


class _TmnxDiamPlcyPeerConnectionTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyPeerConnectionTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxDiamPlcyPeerConnectionTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyPeerConnectionTimer_Object = MibTableColumn
tmnxDiamPlcyPeerConnectionTimer = _TmnxDiamPlcyPeerConnectionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 12),
    _TmnxDiamPlcyPeerConnectionTimer_Type()
)
tmnxDiamPlcyPeerConnectionTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerConnectionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerConnectionTimer.setUnits("seconds")


class _TmnxDiamPlcyPeerTransactTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyPeerTransactTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxDiamPlcyPeerTransactTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyPeerTransactTimer_Object = MibTableColumn
tmnxDiamPlcyPeerTransactTimer = _TmnxDiamPlcyPeerTransactTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 13),
    _TmnxDiamPlcyPeerTransactTimer_Type()
)
tmnxDiamPlcyPeerTransactTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerTransactTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerTransactTimer.setUnits("seconds")


class _TmnxDiamPlcyPeerPreference_Type(Unsigned32):
    """Custom type tmnxDiamPlcyPeerPreference based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxDiamPlcyPeerPreference_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyPeerPreference_Object = MibTableColumn
tmnxDiamPlcyPeerPreference = _TmnxDiamPlcyPeerPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 4, 1, 14),
    _TmnxDiamPlcyPeerPreference_Type()
)
tmnxDiamPlcyPeerPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerPreference.setStatus("current")
_TmnxDiamPlcyPeerInfoTable_Object = MibTable
tmnxDiamPlcyPeerInfoTable = _TmnxDiamPlcyPeerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerInfoTable.setStatus("current")
_TmnxDiamPlcyPeerInfoEntry_Object = MibTableRow
tmnxDiamPlcyPeerInfoEntry = _TmnxDiamPlcyPeerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerInfoEntry.setStatus("current")
_TmnxDiamPeerPsmState_Type = TmnxDiamPeerState
_TmnxDiamPeerPsmState_Object = MibTableColumn
tmnxDiamPeerPsmState = _TmnxDiamPeerPsmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 1),
    _TmnxDiamPeerPsmState_Type()
)
tmnxDiamPeerPsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerPsmState.setStatus("current")
_TmnxDiamPeerConnectionSuspended_Type = TruthValue
_TmnxDiamPeerConnectionSuspended_Object = MibTableColumn
tmnxDiamPeerConnectionSuspended = _TmnxDiamPeerConnectionSuspended_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 2),
    _TmnxDiamPeerConnectionSuspended_Type()
)
tmnxDiamPeerConnectionSuspended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerConnectionSuspended.setStatus("current")


class _TmnxDiamPeerCooldownSeqStage_Type(Integer32):
    """Custom type tmnxDiamPeerCooldownSeqStage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stage1", 0),
          ("stage2", 1),
          ("stage3", 2))
    )


_TmnxDiamPeerCooldownSeqStage_Type.__name__ = "Integer32"
_TmnxDiamPeerCooldownSeqStage_Object = MibTableColumn
tmnxDiamPeerCooldownSeqStage = _TmnxDiamPeerCooldownSeqStage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 3),
    _TmnxDiamPeerCooldownSeqStage_Type()
)
tmnxDiamPeerCooldownSeqStage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerCooldownSeqStage.setStatus("current")
_TmnxDiamPeerOrder_Type = Unsigned32
_TmnxDiamPeerOrder_Object = MibTableColumn
tmnxDiamPeerOrder = _TmnxDiamPeerOrder_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 4),
    _TmnxDiamPeerOrder_Type()
)
tmnxDiamPeerOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerOrder.setStatus("current")


class _TmnxDiamPeerPrimarySecondary_Type(Integer32):
    """Custom type tmnxDiamPeerPrimarySecondary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_TmnxDiamPeerPrimarySecondary_Type.__name__ = "Integer32"
_TmnxDiamPeerPrimarySecondary_Object = MibTableColumn
tmnxDiamPeerPrimarySecondary = _TmnxDiamPeerPrimarySecondary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 5),
    _TmnxDiamPeerPrimarySecondary_Type()
)
tmnxDiamPeerPrimarySecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerPrimarySecondary.setStatus("current")
_TmnxDiamPeerTcTimerTimeLeft_Type = Unsigned32
_TmnxDiamPeerTcTimerTimeLeft_Object = MibTableColumn
tmnxDiamPeerTcTimerTimeLeft = _TmnxDiamPeerTcTimerTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 6),
    _TmnxDiamPeerTcTimerTimeLeft_Type()
)
tmnxDiamPeerTcTimerTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerTcTimerTimeLeft.setStatus("current")
_TmnxDiamPeerTtTimerTimeLeft_Type = Unsigned32
_TmnxDiamPeerTtTimerTimeLeft_Object = MibTableColumn
tmnxDiamPeerTtTimerTimeLeft = _TmnxDiamPeerTtTimerTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 7),
    _TmnxDiamPeerTtTimerTimeLeft_Type()
)
tmnxDiamPeerTtTimerTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerTtTimerTimeLeft.setStatus("current")
_TmnxDiamPeerTwTimerTimeLeft_Type = Unsigned32
_TmnxDiamPeerTwTimerTimeLeft_Object = MibTableColumn
tmnxDiamPeerTwTimerTimeLeft = _TmnxDiamPeerTwTimerTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 8),
    _TmnxDiamPeerTwTimerTimeLeft_Type()
)
tmnxDiamPeerTwTimerTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerTwTimerTimeLeft.setStatus("current")
_TmnxDiamPeerWatchdogAlgActive_Type = TruthValue
_TmnxDiamPeerWatchdogAlgActive_Object = MibTableColumn
tmnxDiamPeerWatchdogAlgActive = _TmnxDiamPeerWatchdogAlgActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 9),
    _TmnxDiamPeerWatchdogAlgActive_Type()
)
tmnxDiamPeerWatchdogAlgActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerWatchdogAlgActive.setStatus("current")
_TmnxDiamPeerWatchdogAnswPending_Type = TruthValue
_TmnxDiamPeerWatchdogAnswPending_Object = MibTableColumn
tmnxDiamPeerWatchdogAnswPending = _TmnxDiamPeerWatchdogAnswPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 10),
    _TmnxDiamPeerWatchdogAnswPending_Type()
)
tmnxDiamPeerWatchdogAnswPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerWatchdogAnswPending.setStatus("current")
_TmnxDiamPeerCooldownSeqPending_Type = TruthValue
_TmnxDiamPeerCooldownSeqPending_Object = MibTableColumn
tmnxDiamPeerCooldownSeqPending = _TmnxDiamPeerCooldownSeqPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 11),
    _TmnxDiamPeerCooldownSeqPending_Type()
)
tmnxDiamPeerCooldownSeqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerCooldownSeqPending.setStatus("current")
_TmnxDiamPeerCooldownSeqActive_Type = TruthValue
_TmnxDiamPeerCooldownSeqActive_Object = MibTableColumn
tmnxDiamPeerCooldownSeqActive = _TmnxDiamPeerCooldownSeqActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 12),
    _TmnxDiamPeerCooldownSeqActive_Type()
)
tmnxDiamPeerCooldownSeqActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerCooldownSeqActive.setStatus("current")
_TmnxDiamPeerPeerRemovalPending_Type = TruthValue
_TmnxDiamPeerPeerRemovalPending_Object = MibTableColumn
tmnxDiamPeerPeerRemovalPending = _TmnxDiamPeerPeerRemovalPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 13),
    _TmnxDiamPeerPeerRemovalPending_Type()
)
tmnxDiamPeerPeerRemovalPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerPeerRemovalPending.setStatus("current")
_TmnxDiamPeerPendingMsgsPMQ_Type = Gauge32
_TmnxDiamPeerPendingMsgsPMQ_Object = MibTableColumn
tmnxDiamPeerPendingMsgsPMQ = _TmnxDiamPeerPendingMsgsPMQ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 5, 1, 14),
    _TmnxDiamPeerPendingMsgsPMQ_Type()
)
tmnxDiamPeerPendingMsgsPMQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerPendingMsgsPMQ.setStatus("current")
_TmnxDiamPlcyPeerStatsTable_Object = MibTable
tmnxDiamPlcyPeerStatsTable = _TmnxDiamPlcyPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerStatsTable.setStatus("obsolete")
_TmnxDiamPlcyPeerStatsEntry_Object = MibTableRow
tmnxDiamPlcyPeerStatsEntry = _TmnxDiamPlcyPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamPlcyPeerStatsEntry.setStatus("obsolete")
_TmnxDiamPeerStatsLastClearTime_Type = TimeStamp
_TmnxDiamPeerStatsLastClearTime_Object = MibTableColumn
tmnxDiamPeerStatsLastClearTime = _TmnxDiamPeerStatsLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 1),
    _TmnxDiamPeerStatsLastClearTime_Type()
)
tmnxDiamPeerStatsLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsLastClearTime.setStatus("obsolete")
_TmnxDiamPeerStCiTcpSendFailed_Type = Counter32
_TmnxDiamPeerStCiTcpSendFailed_Object = MibTableColumn
tmnxDiamPeerStCiTcpSendFailed = _TmnxDiamPeerStCiTcpSendFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 2),
    _TmnxDiamPeerStCiTcpSendFailed_Type()
)
tmnxDiamPeerStCiTcpSendFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCiTcpSendFailed.setStatus("obsolete")
_TmnxDiamPeerStCiDiamRxDropCnt_Type = Counter32
_TmnxDiamPeerStCiDiamRxDropCnt_Object = MibTableColumn
tmnxDiamPeerStCiDiamRxDropCnt = _TmnxDiamPeerStCiDiamRxDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 3),
    _TmnxDiamPeerStCiDiamRxDropCnt_Type()
)
tmnxDiamPeerStCiDiamRxDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCiDiamRxDropCnt.setStatus("obsolete")
_TmnxDiamPeerStCiDiamTxReqs_Type = Counter32
_TmnxDiamPeerStCiDiamTxReqs_Object = MibTableColumn
tmnxDiamPeerStCiDiamTxReqs = _TmnxDiamPeerStCiDiamTxReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 4),
    _TmnxDiamPeerStCiDiamTxReqs_Type()
)
tmnxDiamPeerStCiDiamTxReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCiDiamTxReqs.setStatus("obsolete")
_TmnxDiamPeerStCiDiamRxResps_Type = Counter32
_TmnxDiamPeerStCiDiamRxResps_Object = MibTableColumn
tmnxDiamPeerStCiDiamRxResps = _TmnxDiamPeerStCiDiamRxResps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 5),
    _TmnxDiamPeerStCiDiamRxResps_Type()
)
tmnxDiamPeerStCiDiamRxResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCiDiamRxResps.setStatus("obsolete")
_TmnxDiamPeerStCiPendMsgsPMQ_Type = Counter32
_TmnxDiamPeerStCiPendMsgsPMQ_Object = MibTableColumn
tmnxDiamPeerStCiPendMsgsPMQ = _TmnxDiamPeerStCiPendMsgsPMQ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 6),
    _TmnxDiamPeerStCiPendMsgsPMQ_Type()
)
tmnxDiamPeerStCiPendMsgsPMQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCiPendMsgsPMQ.setStatus("obsolete")
_TmnxDiamPeerStCiReqTimeoutsPMQ_Type = Counter32
_TmnxDiamPeerStCiReqTimeoutsPMQ_Object = MibTableColumn
tmnxDiamPeerStCiReqTimeoutsPMQ = _TmnxDiamPeerStCiReqTimeoutsPMQ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 7),
    _TmnxDiamPeerStCiReqTimeoutsPMQ_Type()
)
tmnxDiamPeerStCiReqTimeoutsPMQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCiReqTimeoutsPMQ.setStatus("obsolete")
_TmnxDiamPeerStSiTcpSendFailed_Type = Counter32
_TmnxDiamPeerStSiTcpSendFailed_Object = MibTableColumn
tmnxDiamPeerStSiTcpSendFailed = _TmnxDiamPeerStSiTcpSendFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 8),
    _TmnxDiamPeerStSiTcpSendFailed_Type()
)
tmnxDiamPeerStSiTcpSendFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStSiTcpSendFailed.setStatus("obsolete")
_TmnxDiamPeerStSiDiamRxDropCnt_Type = Counter32
_TmnxDiamPeerStSiDiamRxDropCnt_Object = MibTableColumn
tmnxDiamPeerStSiDiamRxDropCnt = _TmnxDiamPeerStSiDiamRxDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 9),
    _TmnxDiamPeerStSiDiamRxDropCnt_Type()
)
tmnxDiamPeerStSiDiamRxDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStSiDiamRxDropCnt.setStatus("obsolete")
_TmnxDiamPeerStSiDiamRxReqs_Type = Counter32
_TmnxDiamPeerStSiDiamRxReqs_Object = MibTableColumn
tmnxDiamPeerStSiDiamRxReqs = _TmnxDiamPeerStSiDiamRxReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 10),
    _TmnxDiamPeerStSiDiamRxReqs_Type()
)
tmnxDiamPeerStSiDiamRxReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStSiDiamRxReqs.setStatus("obsolete")
_TmnxDiamPeerStSiDiamTxResps_Type = Counter32
_TmnxDiamPeerStSiDiamTxResps_Object = MibTableColumn
tmnxDiamPeerStSiDiamTxResps = _TmnxDiamPeerStSiDiamTxResps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 11),
    _TmnxDiamPeerStSiDiamTxResps_Type()
)
tmnxDiamPeerStSiDiamTxResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStSiDiamTxResps.setStatus("obsolete")
_TmnxDiamPeerStErrHdlDiamTxErrCnt_Type = Counter32
_TmnxDiamPeerStErrHdlDiamTxErrCnt_Object = MibTableColumn
tmnxDiamPeerStErrHdlDiamTxErrCnt = _TmnxDiamPeerStErrHdlDiamTxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 12),
    _TmnxDiamPeerStErrHdlDiamTxErrCnt_Type()
)
tmnxDiamPeerStErrHdlDiamTxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStErrHdlDiamTxErrCnt.setStatus("obsolete")
_TmnxDiamPeerStErrHdlDiamRxErrCnt_Type = Counter32
_TmnxDiamPeerStErrHdlDiamRxErrCnt_Object = MibTableColumn
tmnxDiamPeerStErrHdlDiamRxErrCnt = _TmnxDiamPeerStErrHdlDiamRxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 13),
    _TmnxDiamPeerStErrHdlDiamRxErrCnt_Type()
)
tmnxDiamPeerStErrHdlDiamRxErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStErrHdlDiamRxErrCnt.setStatus("obsolete")
_TmnxDiamPeerStCcrInitialTx_Type = Counter32
_TmnxDiamPeerStCcrInitialTx_Object = MibTableColumn
tmnxDiamPeerStCcrInitialTx = _TmnxDiamPeerStCcrInitialTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 14),
    _TmnxDiamPeerStCcrInitialTx_Type()
)
tmnxDiamPeerStCcrInitialTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCcrInitialTx.setStatus("obsolete")
_TmnxDiamPeerStCcaInitialRx_Type = Counter32
_TmnxDiamPeerStCcaInitialRx_Object = MibTableColumn
tmnxDiamPeerStCcaInitialRx = _TmnxDiamPeerStCcaInitialRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 15),
    _TmnxDiamPeerStCcaInitialRx_Type()
)
tmnxDiamPeerStCcaInitialRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCcaInitialRx.setStatus("obsolete")
_TmnxDiamPeerStCcrUpdateTx_Type = Counter32
_TmnxDiamPeerStCcrUpdateTx_Object = MibTableColumn
tmnxDiamPeerStCcrUpdateTx = _TmnxDiamPeerStCcrUpdateTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 16),
    _TmnxDiamPeerStCcrUpdateTx_Type()
)
tmnxDiamPeerStCcrUpdateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCcrUpdateTx.setStatus("obsolete")
_TmnxDiamPeerStCcaUpdateRx_Type = Counter32
_TmnxDiamPeerStCcaUpdateRx_Object = MibTableColumn
tmnxDiamPeerStCcaUpdateRx = _TmnxDiamPeerStCcaUpdateRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 17),
    _TmnxDiamPeerStCcaUpdateRx_Type()
)
tmnxDiamPeerStCcaUpdateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCcaUpdateRx.setStatus("obsolete")
_TmnxDiamPeerStCcrTerminateTx_Type = Counter32
_TmnxDiamPeerStCcrTerminateTx_Object = MibTableColumn
tmnxDiamPeerStCcrTerminateTx = _TmnxDiamPeerStCcrTerminateTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 18),
    _TmnxDiamPeerStCcrTerminateTx_Type()
)
tmnxDiamPeerStCcrTerminateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCcrTerminateTx.setStatus("obsolete")
_TmnxDiamPeerStCcaTerminateRx_Type = Counter32
_TmnxDiamPeerStCcaTerminateRx_Object = MibTableColumn
tmnxDiamPeerStCcaTerminateRx = _TmnxDiamPeerStCcaTerminateRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 19),
    _TmnxDiamPeerStCcaTerminateRx_Type()
)
tmnxDiamPeerStCcaTerminateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCcaTerminateRx.setStatus("obsolete")
_TmnxDiamPeerStCerTx_Type = Counter32
_TmnxDiamPeerStCerTx_Object = MibTableColumn
tmnxDiamPeerStCerTx = _TmnxDiamPeerStCerTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 20),
    _TmnxDiamPeerStCerTx_Type()
)
tmnxDiamPeerStCerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCerTx.setStatus("obsolete")
_TmnxDiamPeerStCeaRx_Type = Counter32
_TmnxDiamPeerStCeaRx_Object = MibTableColumn
tmnxDiamPeerStCeaRx = _TmnxDiamPeerStCeaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 21),
    _TmnxDiamPeerStCeaRx_Type()
)
tmnxDiamPeerStCeaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStCeaRx.setStatus("obsolete")
_TmnxDiamPeerStWdrTx_Type = Counter32
_TmnxDiamPeerStWdrTx_Object = MibTableColumn
tmnxDiamPeerStWdrTx = _TmnxDiamPeerStWdrTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 24),
    _TmnxDiamPeerStWdrTx_Type()
)
tmnxDiamPeerStWdrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStWdrTx.setStatus("obsolete")
_TmnxDiamPeerStWdaRx_Type = Counter32
_TmnxDiamPeerStWdaRx_Object = MibTableColumn
tmnxDiamPeerStWdaRx = _TmnxDiamPeerStWdaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 25),
    _TmnxDiamPeerStWdaRx_Type()
)
tmnxDiamPeerStWdaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStWdaRx.setStatus("obsolete")
_TmnxDiamPeerStWdrRx_Type = Counter32
_TmnxDiamPeerStWdrRx_Object = MibTableColumn
tmnxDiamPeerStWdrRx = _TmnxDiamPeerStWdrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 26),
    _TmnxDiamPeerStWdrRx_Type()
)
tmnxDiamPeerStWdrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStWdrRx.setStatus("obsolete")
_TmnxDiamPeerStWdaTx_Type = Counter32
_TmnxDiamPeerStWdaTx_Object = MibTableColumn
tmnxDiamPeerStWdaTx = _TmnxDiamPeerStWdaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 27),
    _TmnxDiamPeerStWdaTx_Type()
)
tmnxDiamPeerStWdaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStWdaTx.setStatus("obsolete")
_TmnxDiamPeerStAsrRx_Type = Counter32
_TmnxDiamPeerStAsrRx_Object = MibTableColumn
tmnxDiamPeerStAsrRx = _TmnxDiamPeerStAsrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 30),
    _TmnxDiamPeerStAsrRx_Type()
)
tmnxDiamPeerStAsrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStAsrRx.setStatus("obsolete")
_TmnxDiamPeerStAsaTx_Type = Counter32
_TmnxDiamPeerStAsaTx_Object = MibTableColumn
tmnxDiamPeerStAsaTx = _TmnxDiamPeerStAsaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 31),
    _TmnxDiamPeerStAsaTx_Type()
)
tmnxDiamPeerStAsaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStAsaTx.setStatus("obsolete")
_TmnxDiamPeerStRarRx_Type = Counter32
_TmnxDiamPeerStRarRx_Object = MibTableColumn
tmnxDiamPeerStRarRx = _TmnxDiamPeerStRarRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 34),
    _TmnxDiamPeerStRarRx_Type()
)
tmnxDiamPeerStRarRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStRarRx.setStatus("obsolete")
_TmnxDiamPeerStRaaTx_Type = Counter32
_TmnxDiamPeerStRaaTx_Object = MibTableColumn
tmnxDiamPeerStRaaTx = _TmnxDiamPeerStRaaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 35),
    _TmnxDiamPeerStRaaTx_Type()
)
tmnxDiamPeerStRaaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStRaaTx.setStatus("obsolete")
_TmnxDiamPeerStDprTx_Type = Counter32
_TmnxDiamPeerStDprTx_Object = MibTableColumn
tmnxDiamPeerStDprTx = _TmnxDiamPeerStDprTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 36),
    _TmnxDiamPeerStDprTx_Type()
)
tmnxDiamPeerStDprTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStDprTx.setStatus("obsolete")
_TmnxDiamPeerStDpaRx_Type = Counter32
_TmnxDiamPeerStDpaRx_Object = MibTableColumn
tmnxDiamPeerStDpaRx = _TmnxDiamPeerStDpaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 37),
    _TmnxDiamPeerStDpaRx_Type()
)
tmnxDiamPeerStDpaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStDpaRx.setStatus("obsolete")
_TmnxDiamPeerStDprRx_Type = Counter32
_TmnxDiamPeerStDprRx_Object = MibTableColumn
tmnxDiamPeerStDprRx = _TmnxDiamPeerStDprRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 38),
    _TmnxDiamPeerStDprRx_Type()
)
tmnxDiamPeerStDprRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStDprRx.setStatus("obsolete")
_TmnxDiamPeerStDpaTx_Type = Counter32
_TmnxDiamPeerStDpaTx_Object = MibTableColumn
tmnxDiamPeerStDpaTx = _TmnxDiamPeerStDpaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 39),
    _TmnxDiamPeerStDpaTx_Type()
)
tmnxDiamPeerStDpaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStDpaTx.setStatus("obsolete")
_TmnxDiamPeerStAarTx_Type = Counter32
_TmnxDiamPeerStAarTx_Object = MibTableColumn
tmnxDiamPeerStAarTx = _TmnxDiamPeerStAarTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 40),
    _TmnxDiamPeerStAarTx_Type()
)
tmnxDiamPeerStAarTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStAarTx.setStatus("obsolete")
_TmnxDiamPeerStAaaRx_Type = Counter32
_TmnxDiamPeerStAaaRx_Object = MibTableColumn
tmnxDiamPeerStAaaRx = _TmnxDiamPeerStAaaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 6, 1, 41),
    _TmnxDiamPeerStAaaRx_Type()
)
tmnxDiamPeerStAaaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStAaaRx.setStatus("obsolete")
_TmnxDiameterNodeTableLastChngd_Type = TimeStamp
_TmnxDiameterNodeTableLastChngd_Object = MibScalar
tmnxDiameterNodeTableLastChngd = _TmnxDiameterNodeTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 7),
    _TmnxDiameterNodeTableLastChngd_Type()
)
tmnxDiameterNodeTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiameterNodeTableLastChngd.setStatus("current")
_TmnxDiameterNodeTable_Object = MibTable
tmnxDiameterNodeTable = _TmnxDiameterNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxDiameterNodeTable.setStatus("current")
_TmnxDiameterNodeEntry_Object = MibTableRow
tmnxDiameterNodeEntry = _TmnxDiameterNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1)
)
tmnxDiameterNodeEntry.setIndexNames(
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamNodeOriginHost"),
)
if mibBuilder.loadTexts:
    tmnxDiameterNodeEntry.setStatus("current")
_TmnxDiamNodeOriginHost_Type = TmnxDiamFqdn
_TmnxDiamNodeOriginHost_Object = MibTableColumn
tmnxDiamNodeOriginHost = _TmnxDiamNodeOriginHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 1),
    _TmnxDiamNodeOriginHost_Type()
)
tmnxDiamNodeOriginHost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamNodeOriginHost.setStatus("current")
_TmnxDiamNodeRowStatus_Type = RowStatus
_TmnxDiamNodeRowStatus_Object = MibTableColumn
tmnxDiamNodeRowStatus = _TmnxDiamNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 2),
    _TmnxDiamNodeRowStatus_Type()
)
tmnxDiamNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodeRowStatus.setStatus("current")
_TmnxDiamNodeLastMgmtChange_Type = TimeStamp
_TmnxDiamNodeLastMgmtChange_Object = MibTableColumn
tmnxDiamNodeLastMgmtChange = _TmnxDiamNodeLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 3),
    _TmnxDiamNodeLastMgmtChange_Type()
)
tmnxDiamNodeLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNodeLastMgmtChange.setStatus("current")


class _TmnxDiamNodeOriginRealm_Type(TmnxDiamFqdnOrEmpty):
    """Custom type tmnxDiamNodeOriginRealm based on TmnxDiamFqdnOrEmpty"""
    defaultValue = OctetString("")


_TmnxDiamNodeOriginRealm_Type.__name__ = "TmnxDiamFqdnOrEmpty"
_TmnxDiamNodeOriginRealm_Object = MibTableColumn
tmnxDiamNodeOriginRealm = _TmnxDiamNodeOriginRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 4),
    _TmnxDiamNodeOriginRealm_Type()
)
tmnxDiamNodeOriginRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodeOriginRealm.setStatus("current")


class _TmnxDiamNodeDescription_Type(TItemDescription):
    """Custom type tmnxDiamNodeDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxDiamNodeDescription_Type.__name__ = "TItemDescription"
_TmnxDiamNodeDescription_Object = MibTableColumn
tmnxDiamNodeDescription = _TmnxDiamNodeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 5),
    _TmnxDiamNodeDescription_Type()
)
tmnxDiamNodeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodeDescription.setStatus("current")


class _TmnxDiamNodeConnectionTimer_Type(Unsigned32):
    """Custom type tmnxDiamNodeConnectionTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxDiamNodeConnectionTimer_Type.__name__ = "Unsigned32"
_TmnxDiamNodeConnectionTimer_Object = MibTableColumn
tmnxDiamNodeConnectionTimer = _TmnxDiamNodeConnectionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 6),
    _TmnxDiamNodeConnectionTimer_Type()
)
tmnxDiamNodeConnectionTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodeConnectionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamNodeConnectionTimer.setUnits("seconds")


class _TmnxDiamNodeSourceAddrType_Type(InetAddressType):
    """Custom type tmnxDiamNodeSourceAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxDiamNodeSourceAddrType_Type.__name__ = "InetAddressType"
_TmnxDiamNodeSourceAddrType_Object = MibTableColumn
tmnxDiamNodeSourceAddrType = _TmnxDiamNodeSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 7),
    _TmnxDiamNodeSourceAddrType_Type()
)
tmnxDiamNodeSourceAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodeSourceAddrType.setStatus("current")


class _TmnxDiamNodeSourceAddr_Type(InetAddress):
    """Custom type tmnxDiamNodeSourceAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxDiamNodeSourceAddr_Type.__name__ = "InetAddress"
_TmnxDiamNodeSourceAddr_Object = MibTableColumn
tmnxDiamNodeSourceAddr = _TmnxDiamNodeSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 8),
    _TmnxDiamNodeSourceAddr_Type()
)
tmnxDiamNodeSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodeSourceAddr.setStatus("current")


class _TmnxDiamNodeV6SourceAddrType_Type(InetAddressType):
    """Custom type tmnxDiamNodeV6SourceAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxDiamNodeV6SourceAddrType_Type.__name__ = "InetAddressType"
_TmnxDiamNodeV6SourceAddrType_Object = MibTableColumn
tmnxDiamNodeV6SourceAddrType = _TmnxDiamNodeV6SourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 9),
    _TmnxDiamNodeV6SourceAddrType_Type()
)
tmnxDiamNodeV6SourceAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodeV6SourceAddrType.setStatus("current")


class _TmnxDiamNodeV6SourceAddr_Type(InetAddress):
    """Custom type tmnxDiamNodeV6SourceAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxDiamNodeV6SourceAddr_Type.__name__ = "InetAddress"
_TmnxDiamNodeV6SourceAddr_Object = MibTableColumn
tmnxDiamNodeV6SourceAddr = _TmnxDiamNodeV6SourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 10),
    _TmnxDiamNodeV6SourceAddr_Type()
)
tmnxDiamNodeV6SourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodeV6SourceAddr.setStatus("current")


class _TmnxDiamNodeRouter_Type(TmnxVRtrID):
    """Custom type tmnxDiamNodeRouter based on TmnxVRtrID"""
    defaultValue = 1


_TmnxDiamNodeRouter_Type.__name__ = "TmnxVRtrID"
_TmnxDiamNodeRouter_Object = MibTableColumn
tmnxDiamNodeRouter = _TmnxDiamNodeRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 11),
    _TmnxDiamNodeRouter_Type()
)
tmnxDiamNodeRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodeRouter.setStatus("current")


class _TmnxDiamNodePythonPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxDiamNodePythonPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDiamNodePythonPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDiamNodePythonPolicy_Object = MibTableColumn
tmnxDiamNodePythonPolicy = _TmnxDiamNodePythonPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 12),
    _TmnxDiamNodePythonPolicy_Type()
)
tmnxDiamNodePythonPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodePythonPolicy.setStatus("current")


class _TmnxDiamNodeAllowConn_Type(TruthValue):
    """Custom type tmnxDiamNodeAllowConn based on TruthValue"""
    defaultValue = 2


_TmnxDiamNodeAllowConn_Type.__name__ = "TruthValue"
_TmnxDiamNodeAllowConn_Object = MibTableColumn
tmnxDiamNodeAllowConn = _TmnxDiamNodeAllowConn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 13),
    _TmnxDiamNodeAllowConn_Type()
)
tmnxDiamNodeAllowConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodeAllowConn.setStatus("current")


class _TmnxDiamNodeV6AllowConn_Type(TruthValue):
    """Custom type tmnxDiamNodeV6AllowConn based on TruthValue"""
    defaultValue = 2


_TmnxDiamNodeV6AllowConn_Type.__name__ = "TruthValue"
_TmnxDiamNodeV6AllowConn_Object = MibTableColumn
tmnxDiamNodeV6AllowConn = _TmnxDiamNodeV6AllowConn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 8, 1, 14),
    _TmnxDiamNodeV6AllowConn_Type()
)
tmnxDiamNodeV6AllowConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodeV6AllowConn.setStatus("current")
_TmnxDiamNodePeerTableLastChngd_Type = TimeStamp
_TmnxDiamNodePeerTableLastChngd_Object = MibScalar
tmnxDiamNodePeerTableLastChngd = _TmnxDiamNodePeerTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 9),
    _TmnxDiamNodePeerTableLastChngd_Type()
)
tmnxDiamNodePeerTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerTableLastChngd.setStatus("current")
_TmnxDiameterNodePeerTable_Object = MibTable
tmnxDiameterNodePeerTable = _TmnxDiameterNodePeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxDiameterNodePeerTable.setStatus("current")
_TmnxDiameterNodePeerEntry_Object = MibTableRow
tmnxDiameterNodePeerEntry = _TmnxDiameterNodePeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10, 1)
)
tmnxDiameterNodePeerEntry.setIndexNames(
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamNodeOriginHost"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamNodePeerIndex"),
)
if mibBuilder.loadTexts:
    tmnxDiameterNodePeerEntry.setStatus("current")


class _TmnxDiamNodePeerIndex_Type(Unsigned32):
    """Custom type tmnxDiamNodePeerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxDiamNodePeerIndex_Type.__name__ = "Unsigned32"
_TmnxDiamNodePeerIndex_Object = MibTableColumn
tmnxDiamNodePeerIndex = _TmnxDiamNodePeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10, 1, 1),
    _TmnxDiamNodePeerIndex_Type()
)
tmnxDiamNodePeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerIndex.setStatus("current")
_TmnxDiamNodePeerRowStatus_Type = RowStatus
_TmnxDiamNodePeerRowStatus_Object = MibTableColumn
tmnxDiamNodePeerRowStatus = _TmnxDiamNodePeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10, 1, 2),
    _TmnxDiamNodePeerRowStatus_Type()
)
tmnxDiamNodePeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerRowStatus.setStatus("current")
_TmnxDiamNodePeerLastMgmtChange_Type = TimeStamp
_TmnxDiamNodePeerLastMgmtChange_Object = MibTableColumn
tmnxDiamNodePeerLastMgmtChange = _TmnxDiamNodePeerLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10, 1, 3),
    _TmnxDiamNodePeerLastMgmtChange_Type()
)
tmnxDiamNodePeerLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerLastMgmtChange.setStatus("current")


class _TmnxDiamNodePeerAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxDiamNodePeerAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxDiamNodePeerAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxDiamNodePeerAdminState_Object = MibTableColumn
tmnxDiamNodePeerAdminState = _TmnxDiamNodePeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10, 1, 4),
    _TmnxDiamNodePeerAdminState_Type()
)
tmnxDiamNodePeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerAdminState.setStatus("current")
_TmnxDiamNodeDestinationHost_Type = TmnxDiamFqdn
_TmnxDiamNodeDestinationHost_Object = MibTableColumn
tmnxDiamNodeDestinationHost = _TmnxDiamNodeDestinationHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10, 1, 5),
    _TmnxDiamNodeDestinationHost_Type()
)
tmnxDiamNodeDestinationHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodeDestinationHost.setStatus("current")


class _TmnxDiamNodePeerAddrType_Type(InetAddressType):
    """Custom type tmnxDiamNodePeerAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxDiamNodePeerAddrType_Type.__name__ = "InetAddressType"
_TmnxDiamNodePeerAddrType_Object = MibTableColumn
tmnxDiamNodePeerAddrType = _TmnxDiamNodePeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10, 1, 6),
    _TmnxDiamNodePeerAddrType_Type()
)
tmnxDiamNodePeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerAddrType.setStatus("current")


class _TmnxDiamNodePeerAddr_Type(InetAddress):
    """Custom type tmnxDiamNodePeerAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDiamNodePeerAddr_Type.__name__ = "InetAddress"
_TmnxDiamNodePeerAddr_Object = MibTableColumn
tmnxDiamNodePeerAddr = _TmnxDiamNodePeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10, 1, 7),
    _TmnxDiamNodePeerAddr_Type()
)
tmnxDiamNodePeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerAddr.setStatus("current")


class _TmnxDiamNodePeerConnectionTimer_Type(Unsigned32):
    """Custom type tmnxDiamNodePeerConnectionTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxDiamNodePeerConnectionTimer_Type.__name__ = "Unsigned32"
_TmnxDiamNodePeerConnectionTimer_Object = MibTableColumn
tmnxDiamNodePeerConnectionTimer = _TmnxDiamNodePeerConnectionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10, 1, 8),
    _TmnxDiamNodePeerConnectionTimer_Type()
)
tmnxDiamNodePeerConnectionTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerConnectionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerConnectionTimer.setUnits("seconds")


class _TmnxDiamNodePeerWatchdogTimer_Type(Unsigned32):
    """Custom type tmnxDiamNodePeerWatchdogTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxDiamNodePeerWatchdogTimer_Type.__name__ = "Unsigned32"
_TmnxDiamNodePeerWatchdogTimer_Object = MibTableColumn
tmnxDiamNodePeerWatchdogTimer = _TmnxDiamNodePeerWatchdogTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10, 1, 9),
    _TmnxDiamNodePeerWatchdogTimer_Type()
)
tmnxDiamNodePeerWatchdogTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerWatchdogTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerWatchdogTimer.setUnits("seconds")


class _TmnxDiamNodePeerPreference_Type(Unsigned32):
    """Custom type tmnxDiamNodePeerPreference based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxDiamNodePeerPreference_Type.__name__ = "Unsigned32"
_TmnxDiamNodePeerPreference_Object = MibTableColumn
tmnxDiamNodePeerPreference = _TmnxDiamNodePeerPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10, 1, 10),
    _TmnxDiamNodePeerPreference_Type()
)
tmnxDiamNodePeerPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerPreference.setStatus("current")


class _TmnxDiamNodePeerDefaultPeer_Type(TruthValue):
    """Custom type tmnxDiamNodePeerDefaultPeer based on TruthValue"""
    defaultValue = 2


_TmnxDiamNodePeerDefaultPeer_Type.__name__ = "TruthValue"
_TmnxDiamNodePeerDefaultPeer_Object = MibTableColumn
tmnxDiamNodePeerDefaultPeer = _TmnxDiamNodePeerDefaultPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 10, 1, 11),
    _TmnxDiamNodePeerDefaultPeer_Type()
)
tmnxDiamNodePeerDefaultPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNodePeerDefaultPeer.setStatus("current")
_TmnxDiamNdPeerStatTable_Object = MibTable
tmnxDiamNdPeerStatTable = _TmnxDiamNdPeerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatTable.setStatus("current")
_TmnxDiamNdPeerStatEntry_Object = MibTableRow
tmnxDiamNdPeerStatEntry = _TmnxDiamNdPeerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatEntry.setStatus("current")
_TmnxDiamNdPeerStatState_Type = TmnxDiamPeerState
_TmnxDiamNdPeerStatState_Object = MibTableColumn
tmnxDiamNdPeerStatState = _TmnxDiamNdPeerStatState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 1),
    _TmnxDiamNdPeerStatState_Type()
)
tmnxDiamNdPeerStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatState.setStatus("current")
_TmnxDiamNdPeerStatActive_Type = TruthValue
_TmnxDiamNdPeerStatActive_Object = MibTableColumn
tmnxDiamNdPeerStatActive = _TmnxDiamNdPeerStatActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 2),
    _TmnxDiamNdPeerStatActive_Type()
)
tmnxDiamNdPeerStatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatActive.setStatus("current")
_TmnxDiamNdPeerStatRemoteRealm_Type = TmnxDiamFqdnOrEmpty
_TmnxDiamNdPeerStatRemoteRealm_Object = MibTableColumn
tmnxDiamNdPeerStatRemoteRealm = _TmnxDiamNdPeerStatRemoteRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 3),
    _TmnxDiamNdPeerStatRemoteRealm_Type()
)
tmnxDiamNdPeerStatRemoteRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatRemoteRealm.setStatus("current")
_TmnxDiamNdPeerStatRemOrigStateId_Type = Unsigned32
_TmnxDiamNdPeerStatRemOrigStateId_Object = MibTableColumn
tmnxDiamNdPeerStatRemOrigStateId = _TmnxDiamNdPeerStatRemOrigStateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 4),
    _TmnxDiamNdPeerStatRemOrigStateId_Type()
)
tmnxDiamNdPeerStatRemOrigStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatRemOrigStateId.setStatus("current")
_TmnxDiamNdPeerStatLocAddrType_Type = InetAddressType
_TmnxDiamNdPeerStatLocAddrType_Object = MibTableColumn
tmnxDiamNdPeerStatLocAddrType = _TmnxDiamNdPeerStatLocAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 5),
    _TmnxDiamNdPeerStatLocAddrType_Type()
)
tmnxDiamNdPeerStatLocAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatLocAddrType.setStatus("current")


class _TmnxDiamNdPeerStatLocAddr_Type(InetAddress):
    """Custom type tmnxDiamNdPeerStatLocAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDiamNdPeerStatLocAddr_Type.__name__ = "InetAddress"
_TmnxDiamNdPeerStatLocAddr_Object = MibTableColumn
tmnxDiamNdPeerStatLocAddr = _TmnxDiamNdPeerStatLocAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 6),
    _TmnxDiamNdPeerStatLocAddr_Type()
)
tmnxDiamNdPeerStatLocAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatLocAddr.setStatus("current")
_TmnxDiamNdPeerStatLocTcpPort_Type = InetPortNumber
_TmnxDiamNdPeerStatLocTcpPort_Object = MibTableColumn
tmnxDiamNdPeerStatLocTcpPort = _TmnxDiamNdPeerStatLocTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 7),
    _TmnxDiamNdPeerStatLocTcpPort_Type()
)
tmnxDiamNdPeerStatLocTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatLocTcpPort.setStatus("current")


class _TmnxDiamNdPeerStatApplications_Type(Bits):
    """Custom type tmnxDiamNdPeerStatApplications based on Bits"""
    namedValues = NamedValues(
        *(("nasreq", 0),
          ("gy", 1),
          ("gx", 2))
    )

_TmnxDiamNdPeerStatApplications_Type.__name__ = "Bits"
_TmnxDiamNdPeerStatApplications_Object = MibTableColumn
tmnxDiamNdPeerStatApplications = _TmnxDiamNdPeerStatApplications_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 8),
    _TmnxDiamNdPeerStatApplications_Type()
)
tmnxDiamNdPeerStatApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatApplications.setStatus("current")
_TmnxDiamNdPeerStatRelay_Type = TruthValue
_TmnxDiamNdPeerStatRelay_Object = MibTableColumn
tmnxDiamNdPeerStatRelay = _TmnxDiamNdPeerStatRelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 9),
    _TmnxDiamNdPeerStatRelay_Type()
)
tmnxDiamNdPeerStatRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatRelay.setStatus("current")


class _TmnxDiamNdPeerStatDiscCause_Type(Integer32):
    """Custom type tmnxDiamNdPeerStatDiscCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", -1),
          ("rebooting", 0),
          ("busy", 1),
          ("stop", 2))
    )


_TmnxDiamNdPeerStatDiscCause_Type.__name__ = "Integer32"
_TmnxDiamNdPeerStatDiscCause_Object = MibTableColumn
tmnxDiamNdPeerStatDiscCause = _TmnxDiamNdPeerStatDiscCause_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 10),
    _TmnxDiamNdPeerStatDiscCause_Type()
)
tmnxDiamNdPeerStatDiscCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatDiscCause.setStatus("current")
_TmnxDiamNdPeerStatTcTimeLeft_Type = Unsigned32
_TmnxDiamNdPeerStatTcTimeLeft_Object = MibTableColumn
tmnxDiamNdPeerStatTcTimeLeft = _TmnxDiamNdPeerStatTcTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 11),
    _TmnxDiamNdPeerStatTcTimeLeft_Type()
)
tmnxDiamNdPeerStatTcTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatTcTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatTcTimeLeft.setUnits("seconds")
_TmnxDiamNdPeerStatTwTimeLeft_Type = Unsigned32
_TmnxDiamNdPeerStatTwTimeLeft_Object = MibTableColumn
tmnxDiamNdPeerStatTwTimeLeft = _TmnxDiamNdPeerStatTwTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 12),
    _TmnxDiamNdPeerStatTwTimeLeft_Type()
)
tmnxDiamNdPeerStatTwTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatTwTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatTwTimeLeft.setUnits("seconds")
_TmnxDiamNdPeerStatPendingMsgsPmq_Type = Gauge32
_TmnxDiamNdPeerStatPendingMsgsPmq_Object = MibTableColumn
tmnxDiamNdPeerStatPendingMsgsPmq = _TmnxDiamNdPeerStatPendingMsgsPmq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 13),
    _TmnxDiamNdPeerStatPendingMsgsPmq_Type()
)
tmnxDiamNdPeerStatPendingMsgsPmq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatPendingMsgsPmq.setStatus("current")
_TmnxDiamNdPeerStatRemAddrType_Type = InetAddressType
_TmnxDiamNdPeerStatRemAddrType_Object = MibTableColumn
tmnxDiamNdPeerStatRemAddrType = _TmnxDiamNdPeerStatRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 14),
    _TmnxDiamNdPeerStatRemAddrType_Type()
)
tmnxDiamNdPeerStatRemAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatRemAddrType.setStatus("current")


class _TmnxDiamNdPeerStatRemAddr_Type(InetAddress):
    """Custom type tmnxDiamNdPeerStatRemAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDiamNdPeerStatRemAddr_Type.__name__ = "InetAddress"
_TmnxDiamNdPeerStatRemAddr_Object = MibTableColumn
tmnxDiamNdPeerStatRemAddr = _TmnxDiamNdPeerStatRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 15),
    _TmnxDiamNdPeerStatRemAddr_Type()
)
tmnxDiamNdPeerStatRemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatRemAddr.setStatus("current")
_TmnxDiamNdPeerStatRemTcpPort_Type = InetPortNumber
_TmnxDiamNdPeerStatRemTcpPort_Object = MibTableColumn
tmnxDiamNdPeerStatRemTcpPort = _TmnxDiamNdPeerStatRemTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 16),
    _TmnxDiamNdPeerStatRemTcpPort_Type()
)
tmnxDiamNdPeerStatRemTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatRemTcpPort.setStatus("current")
_TmnxDiamNdPeerStatMcLocOSI_Type = Unsigned32
_TmnxDiamNdPeerStatMcLocOSI_Object = MibTableColumn
tmnxDiamNdPeerStatMcLocOSI = _TmnxDiamNdPeerStatMcLocOSI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 17),
    _TmnxDiamNdPeerStatMcLocOSI_Type()
)
tmnxDiamNdPeerStatMcLocOSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatMcLocOSI.setStatus("current")
_TmnxDiamNdPeerStatMcRemOSI_Type = Unsigned32
_TmnxDiamNdPeerStatMcRemOSI_Object = MibTableColumn
tmnxDiamNdPeerStatMcRemOSI = _TmnxDiamNdPeerStatMcRemOSI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 18),
    _TmnxDiamNdPeerStatMcRemOSI_Type()
)
tmnxDiamNdPeerStatMcRemOSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatMcRemOSI.setStatus("current")
_TmnxDiamNdPeerStatMcLocState_Type = TmnxDiamNdPeerMcState
_TmnxDiamNdPeerStatMcLocState_Object = MibTableColumn
tmnxDiamNdPeerStatMcLocState = _TmnxDiamNdPeerStatMcLocState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 19),
    _TmnxDiamNdPeerStatMcLocState_Type()
)
tmnxDiamNdPeerStatMcLocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatMcLocState.setStatus("current")
_TmnxDiamNdPeerStatMcRemState_Type = TmnxDiamNdPeerMcState
_TmnxDiamNdPeerStatMcRemState_Object = MibTableColumn
tmnxDiamNdPeerStatMcRemState = _TmnxDiamNdPeerStatMcRemState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 11, 1, 20),
    _TmnxDiamNdPeerStatMcRemState_Type()
)
tmnxDiamNdPeerStatMcRemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatMcRemState.setStatus("current")
_TmnxDiamNdPeerStatsTable_Object = MibTable
tmnxDiamNdPeerStatsTable = _TmnxDiamNdPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsTable.setStatus("current")
_TmnxDiamNdPeerStatsEntry_Object = MibTableRow
tmnxDiamNdPeerStatsEntry = _TmnxDiamNdPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsEntry.setStatus("current")
_TmnxDiamNdPeerStatsLastCleared_Type = TimeStamp
_TmnxDiamNdPeerStatsLastCleared_Object = MibTableColumn
tmnxDiamNdPeerStatsLastCleared = _TmnxDiamNdPeerStatsLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 1),
    _TmnxDiamNdPeerStatsLastCleared_Type()
)
tmnxDiamNdPeerStatsLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsLastCleared.setStatus("current")
_TmnxDiamNdPeerStatsCerTx_Type = Counter64
_TmnxDiamNdPeerStatsCerTx_Object = MibTableColumn
tmnxDiamNdPeerStatsCerTx = _TmnxDiamNdPeerStatsCerTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 2),
    _TmnxDiamNdPeerStatsCerTx_Type()
)
tmnxDiamNdPeerStatsCerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsCerTx.setStatus("current")
_TmnxDiamNdPeerStatsCeaRx_Type = Counter64
_TmnxDiamNdPeerStatsCeaRx_Object = MibTableColumn
tmnxDiamNdPeerStatsCeaRx = _TmnxDiamNdPeerStatsCeaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 3),
    _TmnxDiamNdPeerStatsCeaRx_Type()
)
tmnxDiamNdPeerStatsCeaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsCeaRx.setStatus("current")
_TmnxDiamNdPeerStatsCerRx_Type = Counter64
_TmnxDiamNdPeerStatsCerRx_Object = MibTableColumn
tmnxDiamNdPeerStatsCerRx = _TmnxDiamNdPeerStatsCerRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 4),
    _TmnxDiamNdPeerStatsCerRx_Type()
)
tmnxDiamNdPeerStatsCerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsCerRx.setStatus("current")
_TmnxDiamNdPeerStatsCeaTx_Type = Counter64
_TmnxDiamNdPeerStatsCeaTx_Object = MibTableColumn
tmnxDiamNdPeerStatsCeaTx = _TmnxDiamNdPeerStatsCeaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 5),
    _TmnxDiamNdPeerStatsCeaTx_Type()
)
tmnxDiamNdPeerStatsCeaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsCeaTx.setStatus("current")
_TmnxDiamNdPeerStatsDprTx_Type = Counter64
_TmnxDiamNdPeerStatsDprTx_Object = MibTableColumn
tmnxDiamNdPeerStatsDprTx = _TmnxDiamNdPeerStatsDprTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 6),
    _TmnxDiamNdPeerStatsDprTx_Type()
)
tmnxDiamNdPeerStatsDprTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsDprTx.setStatus("current")
_TmnxDiamNdPeerStatsDpaRx_Type = Counter64
_TmnxDiamNdPeerStatsDpaRx_Object = MibTableColumn
tmnxDiamNdPeerStatsDpaRx = _TmnxDiamNdPeerStatsDpaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 7),
    _TmnxDiamNdPeerStatsDpaRx_Type()
)
tmnxDiamNdPeerStatsDpaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsDpaRx.setStatus("current")
_TmnxDiamNdPeerStatsDprRx_Type = Counter64
_TmnxDiamNdPeerStatsDprRx_Object = MibTableColumn
tmnxDiamNdPeerStatsDprRx = _TmnxDiamNdPeerStatsDprRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 8),
    _TmnxDiamNdPeerStatsDprRx_Type()
)
tmnxDiamNdPeerStatsDprRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsDprRx.setStatus("current")
_TmnxDiamNdPeerStatsDpaTx_Type = Counter64
_TmnxDiamNdPeerStatsDpaTx_Object = MibTableColumn
tmnxDiamNdPeerStatsDpaTx = _TmnxDiamNdPeerStatsDpaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 9),
    _TmnxDiamNdPeerStatsDpaTx_Type()
)
tmnxDiamNdPeerStatsDpaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsDpaTx.setStatus("current")
_TmnxDiamNdPeerStatsDwrTx_Type = Counter64
_TmnxDiamNdPeerStatsDwrTx_Object = MibTableColumn
tmnxDiamNdPeerStatsDwrTx = _TmnxDiamNdPeerStatsDwrTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 10),
    _TmnxDiamNdPeerStatsDwrTx_Type()
)
tmnxDiamNdPeerStatsDwrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsDwrTx.setStatus("current")
_TmnxDiamNdPeerStatsDwaRx_Type = Counter64
_TmnxDiamNdPeerStatsDwaRx_Object = MibTableColumn
tmnxDiamNdPeerStatsDwaRx = _TmnxDiamNdPeerStatsDwaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 11),
    _TmnxDiamNdPeerStatsDwaRx_Type()
)
tmnxDiamNdPeerStatsDwaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsDwaRx.setStatus("current")
_TmnxDiamNdPeerStatsDwrRx_Type = Counter64
_TmnxDiamNdPeerStatsDwrRx_Object = MibTableColumn
tmnxDiamNdPeerStatsDwrRx = _TmnxDiamNdPeerStatsDwrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 12),
    _TmnxDiamNdPeerStatsDwrRx_Type()
)
tmnxDiamNdPeerStatsDwrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsDwrRx.setStatus("current")
_TmnxDiamNdPeerStatsDwaTx_Type = Counter64
_TmnxDiamNdPeerStatsDwaTx_Object = MibTableColumn
tmnxDiamNdPeerStatsDwaTx = _TmnxDiamNdPeerStatsDwaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 13),
    _TmnxDiamNdPeerStatsDwaTx_Type()
)
tmnxDiamNdPeerStatsDwaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsDwaTx.setStatus("current")
_TmnxDiamNdPeerStatsAppReqTx_Type = Counter64
_TmnxDiamNdPeerStatsAppReqTx_Object = MibTableColumn
tmnxDiamNdPeerStatsAppReqTx = _TmnxDiamNdPeerStatsAppReqTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 14),
    _TmnxDiamNdPeerStatsAppReqTx_Type()
)
tmnxDiamNdPeerStatsAppReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsAppReqTx.setStatus("current")
_TmnxDiamNdPeerStatsAppAnswerRx_Type = Counter64
_TmnxDiamNdPeerStatsAppAnswerRx_Object = MibTableColumn
tmnxDiamNdPeerStatsAppAnswerRx = _TmnxDiamNdPeerStatsAppAnswerRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 15),
    _TmnxDiamNdPeerStatsAppAnswerRx_Type()
)
tmnxDiamNdPeerStatsAppAnswerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsAppAnswerRx.setStatus("current")
_TmnxDiamNdPeerStatsAppReqRx_Type = Counter64
_TmnxDiamNdPeerStatsAppReqRx_Object = MibTableColumn
tmnxDiamNdPeerStatsAppReqRx = _TmnxDiamNdPeerStatsAppReqRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 16),
    _TmnxDiamNdPeerStatsAppReqRx_Type()
)
tmnxDiamNdPeerStatsAppReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsAppReqRx.setStatus("current")
_TmnxDiamNdPeerStatsAppAnswerTx_Type = Counter64
_TmnxDiamNdPeerStatsAppAnswerTx_Object = MibTableColumn
tmnxDiamNdPeerStatsAppAnswerTx = _TmnxDiamNdPeerStatsAppAnswerTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 12, 1, 17),
    _TmnxDiamNdPeerStatsAppAnswerTx_Type()
)
tmnxDiamNdPeerStatsAppAnswerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatsAppAnswerTx.setStatus("current")
_TmnxDiamNdStatTable_Object = MibTable
tmnxDiamNdStatTable = _TmnxDiamNdStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxDiamNdStatTable.setStatus("current")
_TmnxDiamNdStatEntry_Object = MibTableRow
tmnxDiamNdStatEntry = _TmnxDiamNdStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 13, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamNdStatEntry.setStatus("current")
_TmnxDiamNdStatOriginRealm_Type = TmnxDiamFqdnOrEmpty
_TmnxDiamNdStatOriginRealm_Object = MibTableColumn
tmnxDiamNdStatOriginRealm = _TmnxDiamNdStatOriginRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 13, 1, 1),
    _TmnxDiamNdStatOriginRealm_Type()
)
tmnxDiamNdStatOriginRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdStatOriginRealm.setStatus("current")
_TmnxDiamNdPeerRtTableLastChngd_Type = TimeStamp
_TmnxDiamNdPeerRtTableLastChngd_Object = MibScalar
tmnxDiamNdPeerRtTableLastChngd = _TmnxDiamNdPeerRtTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 14),
    _TmnxDiamNdPeerRtTableLastChngd_Type()
)
tmnxDiamNdPeerRtTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerRtTableLastChngd.setStatus("current")
_TmnxDiamNdPeerRouteTable_Object = MibTable
tmnxDiamNdPeerRouteTable = _TmnxDiamNdPeerRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxDiamNdPeerRouteTable.setStatus("current")
_TmnxDiamNdPeerRouteEntry_Object = MibTableRow
tmnxDiamNdPeerRouteEntry = _TmnxDiamNdPeerRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 15, 1)
)
tmnxDiamNdPeerRouteEntry.setIndexNames(
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamNodeOriginHost"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamNodePeerIndex"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerRouteIndex"),
)
if mibBuilder.loadTexts:
    tmnxDiamNdPeerRouteEntry.setStatus("current")


class _TmnxDiamNdPeerRouteIndex_Type(Unsigned32):
    """Custom type tmnxDiamNdPeerRouteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TmnxDiamNdPeerRouteIndex_Type.__name__ = "Unsigned32"
_TmnxDiamNdPeerRouteIndex_Object = MibTableColumn
tmnxDiamNdPeerRouteIndex = _TmnxDiamNdPeerRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 15, 1, 1),
    _TmnxDiamNdPeerRouteIndex_Type()
)
tmnxDiamNdPeerRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerRouteIndex.setStatus("current")
_TmnxDiamNdPeerRouteRowStatus_Type = RowStatus
_TmnxDiamNdPeerRouteRowStatus_Object = MibTableColumn
tmnxDiamNdPeerRouteRowStatus = _TmnxDiamNdPeerRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 15, 1, 2),
    _TmnxDiamNdPeerRouteRowStatus_Type()
)
tmnxDiamNdPeerRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerRouteRowStatus.setStatus("current")
_TmnxDiamNdPeerRtLastMgmtChange_Type = TimeStamp
_TmnxDiamNdPeerRtLastMgmtChange_Object = MibTableColumn
tmnxDiamNdPeerRtLastMgmtChange = _TmnxDiamNdPeerRtLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 15, 1, 3),
    _TmnxDiamNdPeerRtLastMgmtChange_Type()
)
tmnxDiamNdPeerRtLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerRtLastMgmtChange.setStatus("current")
_TmnxDiamNdPeerRouteRealm_Type = TmnxDiamFqdn
_TmnxDiamNdPeerRouteRealm_Object = MibTableColumn
tmnxDiamNdPeerRouteRealm = _TmnxDiamNdPeerRouteRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 15, 1, 4),
    _TmnxDiamNdPeerRouteRealm_Type()
)
tmnxDiamNdPeerRouteRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerRouteRealm.setStatus("current")


class _TmnxDiamNdPeerRouteAppId_Type(Integer32):
    """Custom type tmnxDiamNdPeerRouteAppId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              16777238)
        )
    )
    namedValues = NamedValues(
        *(("nasreq", 1),
          ("gy", 4),
          ("gx", 16777238))
    )


_TmnxDiamNdPeerRouteAppId_Type.__name__ = "Integer32"
_TmnxDiamNdPeerRouteAppId_Object = MibTableColumn
tmnxDiamNdPeerRouteAppId = _TmnxDiamNdPeerRouteAppId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 15, 1, 5),
    _TmnxDiamNdPeerRouteAppId_Type()
)
tmnxDiamNdPeerRouteAppId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerRouteAppId.setStatus("current")


class _TmnxDiamNdPeerRoutePreference_Type(Unsigned32):
    """Custom type tmnxDiamNdPeerRoutePreference based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxDiamNdPeerRoutePreference_Type.__name__ = "Unsigned32"
_TmnxDiamNdPeerRoutePreference_Object = MibTableColumn
tmnxDiamNdPeerRoutePreference = _TmnxDiamNdPeerRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 1, 15, 1, 6),
    _TmnxDiamNdPeerRoutePreference_Type()
)
tmnxDiamNdPeerRoutePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamNdPeerRoutePreference.setStatus("current")
_TmnxDiameterDccaObjects_ObjectIdentity = ObjectIdentity
tmnxDiameterDccaObjects = _TmnxDiameterDccaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2)
)
_TmnxDiamPlcyDccaTableLastChngd_Type = TimeStamp
_TmnxDiamPlcyDccaTableLastChngd_Object = MibScalar
tmnxDiamPlcyDccaTableLastChngd = _TmnxDiamPlcyDccaTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 1),
    _TmnxDiamPlcyDccaTableLastChngd_Type()
)
tmnxDiamPlcyDccaTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaTableLastChngd.setStatus("obsolete")
_TmnxDiameterPlcyDccaTable_Object = MibTable
tmnxDiameterPlcyDccaTable = _TmnxDiameterPlcyDccaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxDiameterPlcyDccaTable.setStatus("obsolete")
_TmnxDiameterPlcyDccaEntry_Object = MibTableRow
tmnxDiameterPlcyDccaEntry = _TmnxDiameterPlcyDccaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxDiameterPlcyDccaEntry.setStatus("obsolete")
_TmnxDiamPlcyDccaLastMgmtChange_Type = TimeStamp
_TmnxDiamPlcyDccaLastMgmtChange_Object = MibTableColumn
tmnxDiamPlcyDccaLastMgmtChange = _TmnxDiamPlcyDccaLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 1),
    _TmnxDiamPlcyDccaLastMgmtChange_Type()
)
tmnxDiamPlcyDccaLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaLastMgmtChange.setStatus("obsolete")


class _TmnxDiamPlcyDccaFailover_Type(TruthValue):
    """Custom type tmnxDiamPlcyDccaFailover based on TruthValue"""
    defaultValue = 1


_TmnxDiamPlcyDccaFailover_Type.__name__ = "TruthValue"
_TmnxDiamPlcyDccaFailover_Object = MibTableColumn
tmnxDiamPlcyDccaFailover = _TmnxDiamPlcyDccaFailover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 2),
    _TmnxDiamPlcyDccaFailover_Type()
)
tmnxDiamPlcyDccaFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaFailover.setStatus("obsolete")


class _TmnxDiamPlcyDccaFailureHndlng_Type(TmnxDiamCcFailureHndlng):
    """Custom type tmnxDiamPlcyDccaFailureHndlng based on TmnxDiamCcFailureHndlng"""
    defaultValue = 1


_TmnxDiamPlcyDccaFailureHndlng_Type.__name__ = "TmnxDiamCcFailureHndlng"
_TmnxDiamPlcyDccaFailureHndlng_Object = MibTableColumn
tmnxDiamPlcyDccaFailureHndlng = _TmnxDiamPlcyDccaFailureHndlng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 3),
    _TmnxDiamPlcyDccaFailureHndlng_Type()
)
tmnxDiamPlcyDccaFailureHndlng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaFailureHndlng.setStatus("obsolete")


class _TmnxDiamPlcyDccaTxTimer_Type(Unsigned32):
    """Custom type tmnxDiamPlcyDccaTxTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TmnxDiamPlcyDccaTxTimer_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyDccaTxTimer_Object = MibTableColumn
tmnxDiamPlcyDccaTxTimer = _TmnxDiamPlcyDccaTxTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 4),
    _TmnxDiamPlcyDccaTxTimer_Type()
)
tmnxDiamPlcyDccaTxTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaTxTimer.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaTxTimer.setUnits("seconds")


class _TmnxDiamPlcyDccaAvpServCntxtId_Type(DisplayString):
    """Custom type tmnxDiamPlcyDccaAvpServCntxtId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxDiamPlcyDccaAvpServCntxtId_Type.__name__ = "DisplayString"
_TmnxDiamPlcyDccaAvpServCntxtId_Object = MibTableColumn
tmnxDiamPlcyDccaAvpServCntxtId = _TmnxDiamPlcyDccaAvpServCntxtId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 5),
    _TmnxDiamPlcyDccaAvpServCntxtId_Type()
)
tmnxDiamPlcyDccaAvpServCntxtId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpServCntxtId.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpCldStationId_Type(DisplayString):
    """Custom type tmnxDiamPlcyDccaAvpCldStationId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxDiamPlcyDccaAvpCldStationId_Type.__name__ = "DisplayString"
_TmnxDiamPlcyDccaAvpCldStationId_Object = MibTableColumn
tmnxDiamPlcyDccaAvpCldStationId = _TmnxDiamPlcyDccaAvpCldStationId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 6),
    _TmnxDiamPlcyDccaAvpCldStationId_Type()
)
tmnxDiamPlcyDccaAvpCldStationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpCldStationId.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpRadiusUsrNme_Type(TruthValue):
    """Custom type tmnxDiamPlcyDccaAvpRadiusUsrNme based on TruthValue"""
    defaultValue = 2


_TmnxDiamPlcyDccaAvpRadiusUsrNme_Type.__name__ = "TruthValue"
_TmnxDiamPlcyDccaAvpRadiusUsrNme_Object = MibTableColumn
tmnxDiamPlcyDccaAvpRadiusUsrNme = _TmnxDiamPlcyDccaAvpRadiusUsrNme_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 7),
    _TmnxDiamPlcyDccaAvpRadiusUsrNme_Type()
)
tmnxDiamPlcyDccaAvpRadiusUsrNme.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpRadiusUsrNme.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpSubIdOrg_Type(TmnxDiamPlcyDccaAvpOriginType):
    """Custom type tmnxDiamPlcyDccaAvpSubIdOrg based on TmnxDiamPlcyDccaAvpOriginType"""
    defaultValue = 1


_TmnxDiamPlcyDccaAvpSubIdOrg_Type.__name__ = "TmnxDiamPlcyDccaAvpOriginType"
_TmnxDiamPlcyDccaAvpSubIdOrg_Object = MibTableColumn
tmnxDiamPlcyDccaAvpSubIdOrg = _TmnxDiamPlcyDccaAvpSubIdOrg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 8),
    _TmnxDiamPlcyDccaAvpSubIdOrg_Type()
)
tmnxDiamPlcyDccaAvpSubIdOrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpSubIdOrg.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpSubIdType_Type(Integer32):
    """Custom type tmnxDiamPlcyDccaAvpSubIdType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("endUserE164", 0),
          ("endUserImsi", 1),
          ("endUserPrivate", 4))
    )


_TmnxDiamPlcyDccaAvpSubIdType_Type.__name__ = "Integer32"
_TmnxDiamPlcyDccaAvpSubIdType_Object = MibTableColumn
tmnxDiamPlcyDccaAvpSubIdType = _TmnxDiamPlcyDccaAvpSubIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 9),
    _TmnxDiamPlcyDccaAvpSubIdType_Type()
)
tmnxDiamPlcyDccaAvpSubIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpSubIdType.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpNasP_Type(TruthValue):
    """Custom type tmnxDiamPlcyDccaAvpNasP based on TruthValue"""
    defaultValue = 2


_TmnxDiamPlcyDccaAvpNasP_Type.__name__ = "TruthValue"
_TmnxDiamPlcyDccaAvpNasP_Object = MibTableColumn
tmnxDiamPlcyDccaAvpNasP = _TmnxDiamPlcyDccaAvpNasP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 10),
    _TmnxDiamPlcyDccaAvpNasP_Type()
)
tmnxDiamPlcyDccaAvpNasP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpNasP.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpNasPPfixType_Type(TmnxSubNasPortPrefixType):
    """Custom type tmnxDiamPlcyDccaAvpNasPPfixType based on TmnxSubNasPortPrefixType"""
    defaultValue = 0


_TmnxDiamPlcyDccaAvpNasPPfixType_Type.__name__ = "TmnxSubNasPortPrefixType"
_TmnxDiamPlcyDccaAvpNasPPfixType_Object = MibTableColumn
tmnxDiamPlcyDccaAvpNasPPfixType = _TmnxDiamPlcyDccaAvpNasPPfixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 11),
    _TmnxDiamPlcyDccaAvpNasPPfixType_Type()
)
tmnxDiamPlcyDccaAvpNasPPfixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpNasPPfixType.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpNasPPfixStr_Type(DisplayString):
    """Custom type tmnxDiamPlcyDccaAvpNasPPfixStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxDiamPlcyDccaAvpNasPPfixStr_Type.__name__ = "DisplayString"
_TmnxDiamPlcyDccaAvpNasPPfixStr_Object = MibTableColumn
tmnxDiamPlcyDccaAvpNasPPfixStr = _TmnxDiamPlcyDccaAvpNasPPfixStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 12),
    _TmnxDiamPlcyDccaAvpNasPPfixStr_Type()
)
tmnxDiamPlcyDccaAvpNasPPfixStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpNasPPfixStr.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpNasPSfixType_Type(TmnxSubNasPortSuffixType):
    """Custom type tmnxDiamPlcyDccaAvpNasPSfixType based on TmnxSubNasPortSuffixType"""
    defaultValue = 0


_TmnxDiamPlcyDccaAvpNasPSfixType_Type.__name__ = "TmnxSubNasPortSuffixType"
_TmnxDiamPlcyDccaAvpNasPSfixType_Object = MibTableColumn
tmnxDiamPlcyDccaAvpNasPSfixType = _TmnxDiamPlcyDccaAvpNasPSfixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 13),
    _TmnxDiamPlcyDccaAvpNasPSfixType_Type()
)
tmnxDiamPlcyDccaAvpNasPSfixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpNasPSfixType.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpNasPType_Type(TruthValue):
    """Custom type tmnxDiamPlcyDccaAvpNasPType based on TruthValue"""
    defaultValue = 2


_TmnxDiamPlcyDccaAvpNasPType_Type.__name__ = "TruthValue"
_TmnxDiamPlcyDccaAvpNasPType_Object = MibTableColumn
tmnxDiamPlcyDccaAvpNasPType = _TmnxDiamPlcyDccaAvpNasPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 14),
    _TmnxDiamPlcyDccaAvpNasPType_Type()
)
tmnxDiamPlcyDccaAvpNasPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpNasPType.setStatus("obsolete")


class _TmnxDiamPlcyDccaAvpImsiOrg_Type(TmnxDiamPlcyDccaAvpOriginType):
    """Custom type tmnxDiamPlcyDccaAvpImsiOrg based on TmnxDiamPlcyDccaAvpOriginType"""
    defaultValue = 1


_TmnxDiamPlcyDccaAvpImsiOrg_Type.__name__ = "TmnxDiamPlcyDccaAvpOriginType"
_TmnxDiamPlcyDccaAvpImsiOrg_Object = MibTableColumn
tmnxDiamPlcyDccaAvpImsiOrg = _TmnxDiamPlcyDccaAvpImsiOrg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 15),
    _TmnxDiamPlcyDccaAvpImsiOrg_Type()
)
tmnxDiamPlcyDccaAvpImsiOrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaAvpImsiOrg.setStatus("obsolete")


class _TmnxDiamPlcyDccaApplicationType_Type(TmnxDiamDccaApplicationType):
    """Custom type tmnxDiamPlcyDccaApplicationType based on TmnxDiamDccaApplicationType"""
    defaultValue = 1


_TmnxDiamPlcyDccaApplicationType_Type.__name__ = "TmnxDiamDccaApplicationType"
_TmnxDiamPlcyDccaApplicationType_Object = MibTableColumn
tmnxDiamPlcyDccaApplicationType = _TmnxDiamPlcyDccaApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 50),
    _TmnxDiamPlcyDccaApplicationType_Type()
)
tmnxDiamPlcyDccaApplicationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaApplicationType.setStatus("obsolete")


class _TmnxDiamPlcyDccaMaxPendingReq_Type(Unsigned32):
    """Custom type tmnxDiamPlcyDccaMaxPendingReq based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 131072),
    )


_TmnxDiamPlcyDccaMaxPendingReq_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyDccaMaxPendingReq_Object = MibTableColumn
tmnxDiamPlcyDccaMaxPendingReq = _TmnxDiamPlcyDccaMaxPendingReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 51),
    _TmnxDiamPlcyDccaMaxPendingReq_Type()
)
tmnxDiamPlcyDccaMaxPendingReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaMaxPendingReq.setStatus("obsolete")


class _TmnxDiamPlcyDccaTxRetryLimit_Type(Unsigned32):
    """Custom type tmnxDiamPlcyDccaTxRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TmnxDiamPlcyDccaTxRetryLimit_Type.__name__ = "Unsigned32"
_TmnxDiamPlcyDccaTxRetryLimit_Object = MibTableColumn
tmnxDiamPlcyDccaTxRetryLimit = _TmnxDiamPlcyDccaTxRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 52),
    _TmnxDiamPlcyDccaTxRetryLimit_Type()
)
tmnxDiamPlcyDccaTxRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaTxRetryLimit.setStatus("obsolete")


class _TmnxDiamPlcyDccaOutOfCreditRep_Type(Integer32):
    """Custom type tmnxDiamPlcyDccaOutOfCreditRep based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("final", 1),
          ("quotaExhausted", 2))
    )


_TmnxDiamPlcyDccaOutOfCreditRep_Type.__name__ = "Integer32"
_TmnxDiamPlcyDccaOutOfCreditRep_Object = MibTableColumn
tmnxDiamPlcyDccaOutOfCreditRep = _TmnxDiamPlcyDccaOutOfCreditRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 2, 2, 1, 53),
    _TmnxDiamPlcyDccaOutOfCreditRep_Type()
)
tmnxDiamPlcyDccaOutOfCreditRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPlcyDccaOutOfCreditRep.setStatus("obsolete")
_TmnxDiameterObjects_ObjectIdentity = ObjectIdentity
tmnxDiameterObjects = _TmnxDiameterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3)
)
_TmnxDiamAppPlcyTableLastCh_Type = TimeStamp
_TmnxDiamAppPlcyTableLastCh_Object = MibScalar
tmnxDiamAppPlcyTableLastCh = _TmnxDiamAppPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 1),
    _TmnxDiamAppPlcyTableLastCh_Type()
)
tmnxDiamAppPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyTableLastCh.setStatus("current")
_TmnxDiamAppPlcyTable_Object = MibTable
tmnxDiamAppPlcyTable = _TmnxDiamAppPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyTable.setStatus("current")
_TmnxDiamAppPlcyEntry_Object = MibTableRow
tmnxDiamAppPlcyEntry = _TmnxDiamAppPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1)
)
tmnxDiamAppPlcyEntry.setIndexNames(
    (1, "TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyId"),
)
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyEntry.setStatus("current")
_TmnxDiamAppPlcyId_Type = TNamedItem
_TmnxDiamAppPlcyId_Object = MibTableColumn
tmnxDiamAppPlcyId = _TmnxDiamAppPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 1),
    _TmnxDiamAppPlcyId_Type()
)
tmnxDiamAppPlcyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyId.setStatus("current")
_TmnxDiamAppPlcyRowStatus_Type = RowStatus
_TmnxDiamAppPlcyRowStatus_Object = MibTableColumn
tmnxDiamAppPlcyRowStatus = _TmnxDiamAppPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 2),
    _TmnxDiamAppPlcyRowStatus_Type()
)
tmnxDiamAppPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyRowStatus.setStatus("current")
_TmnxDiamAppPlcyLastMgmtChange_Type = TimeStamp
_TmnxDiamAppPlcyLastMgmtChange_Object = MibTableColumn
tmnxDiamAppPlcyLastMgmtChange = _TmnxDiamAppPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 3),
    _TmnxDiamAppPlcyLastMgmtChange_Type()
)
tmnxDiamAppPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyLastMgmtChange.setStatus("current")


class _TmnxDiamAppPlcyFailover_Type(TruthValue):
    """Custom type tmnxDiamAppPlcyFailover based on TruthValue"""
    defaultValue = 1


_TmnxDiamAppPlcyFailover_Type.__name__ = "TruthValue"
_TmnxDiamAppPlcyFailover_Object = MibTableColumn
tmnxDiamAppPlcyFailover = _TmnxDiamAppPlcyFailover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 4),
    _TmnxDiamAppPlcyFailover_Type()
)
tmnxDiamAppPlcyFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyFailover.setStatus("current")


class _TmnxDiamAppPlcyFailureHndlng_Type(TmnxDiamCcFailureHndlng):
    """Custom type tmnxDiamAppPlcyFailureHndlng based on TmnxDiamCcFailureHndlng"""
    defaultValue = 1


_TmnxDiamAppPlcyFailureHndlng_Type.__name__ = "TmnxDiamCcFailureHndlng"
_TmnxDiamAppPlcyFailureHndlng_Object = MibTableColumn
tmnxDiamAppPlcyFailureHndlng = _TmnxDiamAppPlcyFailureHndlng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 5),
    _TmnxDiamAppPlcyFailureHndlng_Type()
)
tmnxDiamAppPlcyFailureHndlng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyFailureHndlng.setStatus("current")


class _TmnxDiamAppPlcyPeerPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxDiamAppPlcyPeerPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDiamAppPlcyPeerPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDiamAppPlcyPeerPlcy_Object = MibTableColumn
tmnxDiamAppPlcyPeerPlcy = _TmnxDiamAppPlcyPeerPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 6),
    _TmnxDiamAppPlcyPeerPlcy_Type()
)
tmnxDiamAppPlcyPeerPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyPeerPlcy.setStatus("current")


class _TmnxDiamAppPlcyApplication_Type(Integer32):
    """Custom type tmnxDiamAppPlcyApplication based on Integer32"""
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
        *(("none", 0),
          ("gx", 1),
          ("gy", 2),
          ("nasreq", 3))
    )


_TmnxDiamAppPlcyApplication_Type.__name__ = "Integer32"
_TmnxDiamAppPlcyApplication_Object = MibTableColumn
tmnxDiamAppPlcyApplication = _TmnxDiamAppPlcyApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 7),
    _TmnxDiamAppPlcyApplication_Type()
)
tmnxDiamAppPlcyApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyApplication.setStatus("current")


class _TmnxDiamAppPlcyTxTimer_Type(Unsigned32):
    """Custom type tmnxDiamAppPlcyTxTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TmnxDiamAppPlcyTxTimer_Type.__name__ = "Unsigned32"
_TmnxDiamAppPlcyTxTimer_Object = MibTableColumn
tmnxDiamAppPlcyTxTimer = _TmnxDiamAppPlcyTxTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 8),
    _TmnxDiamAppPlcyTxTimer_Type()
)
tmnxDiamAppPlcyTxTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyTxTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyTxTimer.setUnits("seconds")


class _TmnxDiamAppPlcyDescription_Type(TItemDescription):
    """Custom type tmnxDiamAppPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxDiamAppPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxDiamAppPlcyDescription_Object = MibTableColumn
tmnxDiamAppPlcyDescription = _TmnxDiamAppPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 9),
    _TmnxDiamAppPlcyDescription_Type()
)
tmnxDiamAppPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyDescription.setStatus("current")


class _TmnxDiamAppPlcyNodeOriginHost_Type(TmnxDiamFqdnOrEmpty):
    """Custom type tmnxDiamAppPlcyNodeOriginHost based on TmnxDiamFqdnOrEmpty"""
    defaultValue = OctetString("")


_TmnxDiamAppPlcyNodeOriginHost_Type.__name__ = "TmnxDiamFqdnOrEmpty"
_TmnxDiamAppPlcyNodeOriginHost_Object = MibTableColumn
tmnxDiamAppPlcyNodeOriginHost = _TmnxDiamAppPlcyNodeOriginHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 10),
    _TmnxDiamAppPlcyNodeOriginHost_Type()
)
tmnxDiamAppPlcyNodeOriginHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyNodeOriginHost.setStatus("current")


class _TmnxDiamAppPlcyNodeDestRealm_Type(TmnxDiamFqdnOrEmpty):
    """Custom type tmnxDiamAppPlcyNodeDestRealm based on TmnxDiamFqdnOrEmpty"""
    defaultValue = OctetString("")


_TmnxDiamAppPlcyNodeDestRealm_Type.__name__ = "TmnxDiamFqdnOrEmpty"
_TmnxDiamAppPlcyNodeDestRealm_Object = MibTableColumn
tmnxDiamAppPlcyNodeDestRealm = _TmnxDiamAppPlcyNodeDestRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 11),
    _TmnxDiamAppPlcyNodeDestRealm_Type()
)
tmnxDiamAppPlcyNodeDestRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyNodeDestRealm.setStatus("current")


class _TmnxDiamAppPlcyNodeDestRealmLrng_Type(TruthValue):
    """Custom type tmnxDiamAppPlcyNodeDestRealmLrng based on TruthValue"""
    defaultValue = 1


_TmnxDiamAppPlcyNodeDestRealmLrng_Type.__name__ = "TruthValue"
_TmnxDiamAppPlcyNodeDestRealmLrng_Object = MibTableColumn
tmnxDiamAppPlcyNodeDestRealmLrng = _TmnxDiamAppPlcyNodeDestRealmLrng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 2, 1, 12),
    _TmnxDiamAppPlcyNodeDestRealmLrng_Type()
)
tmnxDiamAppPlcyNodeDestRealmLrng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyNodeDestRealmLrng.setStatus("current")
_TmnxDiamApGyTableLastCh_Type = TimeStamp
_TmnxDiamApGyTableLastCh_Object = MibScalar
tmnxDiamApGyTableLastCh = _TmnxDiamApGyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 3),
    _TmnxDiamApGyTableLastCh_Type()
)
tmnxDiamApGyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApGyTableLastCh.setStatus("current")
_TmnxDiamApGyTable_Object = MibTable
tmnxDiamApGyTable = _TmnxDiamApGyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxDiamApGyTable.setStatus("current")
_TmnxDiamApGyEntry_Object = MibTableRow
tmnxDiamApGyEntry = _TmnxDiamApGyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1)
)
tmnxDiamApGyEntry.setIndexNames(
    (1, "TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyId"),
)
if mibBuilder.loadTexts:
    tmnxDiamApGyEntry.setStatus("current")
_TmnxDiamApGyLastMgmtChange_Type = TimeStamp
_TmnxDiamApGyLastMgmtChange_Object = MibTableColumn
tmnxDiamApGyLastMgmtChange = _TmnxDiamApGyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 1),
    _TmnxDiamApGyLastMgmtChange_Type()
)
tmnxDiamApGyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApGyLastMgmtChange.setStatus("current")


class _TmnxDiamApGyAvpServCntxtId_Type(DisplayString):
    """Custom type tmnxDiamApGyAvpServCntxtId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxDiamApGyAvpServCntxtId_Type.__name__ = "DisplayString"
_TmnxDiamApGyAvpServCntxtId_Object = MibTableColumn
tmnxDiamApGyAvpServCntxtId = _TmnxDiamApGyAvpServCntxtId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 2),
    _TmnxDiamApGyAvpServCntxtId_Type()
)
tmnxDiamApGyAvpServCntxtId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyAvpServCntxtId.setStatus("current")


class _TmnxDiamApGyAvpCldStationId_Type(DisplayString):
    """Custom type tmnxDiamApGyAvpCldStationId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxDiamApGyAvpCldStationId_Type.__name__ = "DisplayString"
_TmnxDiamApGyAvpCldStationId_Object = MibTableColumn
tmnxDiamApGyAvpCldStationId = _TmnxDiamApGyAvpCldStationId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 3),
    _TmnxDiamApGyAvpCldStationId_Type()
)
tmnxDiamApGyAvpCldStationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyAvpCldStationId.setStatus("current")


class _TmnxDiamApGyAvpRadiusUsrNme_Type(TruthValue):
    """Custom type tmnxDiamApGyAvpRadiusUsrNme based on TruthValue"""
    defaultValue = 2


_TmnxDiamApGyAvpRadiusUsrNme_Type.__name__ = "TruthValue"
_TmnxDiamApGyAvpRadiusUsrNme_Object = MibTableColumn
tmnxDiamApGyAvpRadiusUsrNme = _TmnxDiamApGyAvpRadiusUsrNme_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 4),
    _TmnxDiamApGyAvpRadiusUsrNme_Type()
)
tmnxDiamApGyAvpRadiusUsrNme.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyAvpRadiusUsrNme.setStatus("current")


class _TmnxDiamApGyAvpImsiOrg_Type(TmnxDiamPlcyDccaAvpOriginType):
    """Custom type tmnxDiamApGyAvpImsiOrg based on TmnxDiamPlcyDccaAvpOriginType"""
    defaultValue = 1

    subtypeSpec = TmnxDiamPlcyDccaAvpOriginType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("subscriberId", 1),
          ("circuitId", 2),
          ("imsi", 3))
    )


_TmnxDiamApGyAvpImsiOrg_Type.__name__ = "TmnxDiamPlcyDccaAvpOriginType"
_TmnxDiamApGyAvpImsiOrg_Object = MibTableColumn
tmnxDiamApGyAvpImsiOrg = _TmnxDiamApGyAvpImsiOrg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 5),
    _TmnxDiamApGyAvpImsiOrg_Type()
)
tmnxDiamApGyAvpImsiOrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyAvpImsiOrg.setStatus("current")


class _TmnxDiamApGyOutOfCreditRep_Type(Integer32):
    """Custom type tmnxDiamApGyOutOfCreditRep based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("final", 1),
          ("quotaExhausted", 2))
    )


_TmnxDiamApGyOutOfCreditRep_Type.__name__ = "Integer32"
_TmnxDiamApGyOutOfCreditRep_Object = MibTableColumn
tmnxDiamApGyOutOfCreditRep = _TmnxDiamApGyOutOfCreditRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 6),
    _TmnxDiamApGyOutOfCreditRep_Type()
)
tmnxDiamApGyOutOfCreditRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyOutOfCreditRep.setStatus("current")


class _TmnxDiamApGyVendorSupport_Type(TmnxDiamPlcyVendorSupportType):
    """Custom type tmnxDiamApGyVendorSupport based on TmnxDiamPlcyVendorSupportType"""
    defaultValue = 2


_TmnxDiamApGyVendorSupport_Type.__name__ = "TmnxDiamPlcyVendorSupportType"
_TmnxDiamApGyVendorSupport_Object = MibTableColumn
tmnxDiamApGyVendorSupport = _TmnxDiamApGyVendorSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 7),
    _TmnxDiamApGyVendorSupport_Type()
)
tmnxDiamApGyVendorSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyVendorSupport.setStatus("current")


class _TmnxDiamApGySubIdOrg_Type(TmnxDiamPlcyDccaAvpOriginType):
    """Custom type tmnxDiamApGySubIdOrg based on TmnxDiamPlcyDccaAvpOriginType"""
    defaultValue = 1

    subtypeSpec = TmnxDiamPlcyDccaAvpOriginType.subtypeSpec
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("subscriberId", 1),
          ("circuitId", 2),
          ("imsi", 3),
          ("msisdn", 4),
          ("imei", 5),
          ("dualStackRemoteId", 6),
          ("mac", 7),
          ("username", 8),
          ("nasPortId", 9))
    )


_TmnxDiamApGySubIdOrg_Type.__name__ = "TmnxDiamPlcyDccaAvpOriginType"
_TmnxDiamApGySubIdOrg_Object = MibTableColumn
tmnxDiamApGySubIdOrg = _TmnxDiamApGySubIdOrg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 8),
    _TmnxDiamApGySubIdOrg_Type()
)
tmnxDiamApGySubIdOrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGySubIdOrg.setStatus("current")


class _TmnxDiamApGySubIdType_Type(Integer32):
    """Custom type tmnxDiamApGySubIdType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e164", 0),
          ("imsi", 1),
          ("nai", 3),
          ("private", 4))
    )


_TmnxDiamApGySubIdType_Type.__name__ = "Integer32"
_TmnxDiamApGySubIdType_Object = MibTableColumn
tmnxDiamApGySubIdType = _TmnxDiamApGySubIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 9),
    _TmnxDiamApGySubIdType_Type()
)
tmnxDiamApGySubIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGySubIdType.setStatus("current")


class _TmnxDiamApGyInc3GppGgsnAddr_Type(TruthValue):
    """Custom type tmnxDiamApGyInc3GppGgsnAddr based on TruthValue"""
    defaultValue = 1


_TmnxDiamApGyInc3GppGgsnAddr_Type.__name__ = "TruthValue"
_TmnxDiamApGyInc3GppGgsnAddr_Object = MibTableColumn
tmnxDiamApGyInc3GppGgsnAddr = _TmnxDiamApGyInc3GppGgsnAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 10),
    _TmnxDiamApGyInc3GppGgsnAddr_Type()
)
tmnxDiamApGyInc3GppGgsnAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyInc3GppGgsnAddr.setStatus("current")


class _TmnxDiamApGyInc3GppGgsnIPv6Addr_Type(TruthValue):
    """Custom type tmnxDiamApGyInc3GppGgsnIPv6Addr based on TruthValue"""
    defaultValue = 2


_TmnxDiamApGyInc3GppGgsnIPv6Addr_Type.__name__ = "TruthValue"
_TmnxDiamApGyInc3GppGgsnIPv6Addr_Object = MibTableColumn
tmnxDiamApGyInc3GppGgsnIPv6Addr = _TmnxDiamApGyInc3GppGgsnIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 11),
    _TmnxDiamApGyInc3GppGgsnIPv6Addr_Type()
)
tmnxDiamApGyInc3GppGgsnIPv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyInc3GppGgsnIPv6Addr.setStatus("current")


class _TmnxDiamApGyMacFormat_Type(TmnxMacSpecification):
    """Custom type tmnxDiamApGyMacFormat based on TmnxMacSpecification"""
    defaultValue = OctetString("aa:")

    subtypeSpec = TmnxMacSpecification.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 7),
    )


_TmnxDiamApGyMacFormat_Type.__name__ = "TmnxMacSpecification"
_TmnxDiamApGyMacFormat_Object = MibTableColumn
tmnxDiamApGyMacFormat = _TmnxDiamApGyMacFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 12),
    _TmnxDiamApGyMacFormat_Type()
)
tmnxDiamApGyMacFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyMacFormat.setStatus("current")


class _TmnxDiamApGyIncAddressAvp_Type(TruthValue):
    """Custom type tmnxDiamApGyIncAddressAvp based on TruthValue"""
    defaultValue = 1


_TmnxDiamApGyIncAddressAvp_Type.__name__ = "TruthValue"
_TmnxDiamApGyIncAddressAvp_Object = MibTableColumn
tmnxDiamApGyIncAddressAvp = _TmnxDiamApGyIncAddressAvp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 13),
    _TmnxDiamApGyIncAddressAvp_Type()
)
tmnxDiamApGyIncAddressAvp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyIncAddressAvp.setStatus("current")


class _TmnxDiamApGyInc3GppChargingId_Type(Integer32):
    """Custom type tmnxDiamApGyInc3GppChargingId based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 0),
          ("auto", 1),
          ("esmInfo", 2),
          ("id", 3))
    )


_TmnxDiamApGyInc3GppChargingId_Type.__name__ = "Integer32"
_TmnxDiamApGyInc3GppChargingId_Object = MibTableColumn
tmnxDiamApGyInc3GppChargingId = _TmnxDiamApGyInc3GppChargingId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 14),
    _TmnxDiamApGyInc3GppChargingId_Type()
)
tmnxDiamApGyInc3GppChargingId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyInc3GppChargingId.setStatus("current")


class _TmnxDiamApGyInc3GppGprsNQosProf_Type(TruthValue):
    """Custom type tmnxDiamApGyInc3GppGprsNQosProf based on TruthValue"""
    defaultValue = 1


_TmnxDiamApGyInc3GppGprsNQosProf_Type.__name__ = "TruthValue"
_TmnxDiamApGyInc3GppGprsNQosProf_Object = MibTableColumn
tmnxDiamApGyInc3GppGprsNQosProf = _TmnxDiamApGyInc3GppGprsNQosProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 15),
    _TmnxDiamApGyInc3GppGprsNQosProf_Type()
)
tmnxDiamApGyInc3GppGprsNQosProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyInc3GppGprsNQosProf.setStatus("current")


class _TmnxDiamApGyInc3GppNsapi_Type(TruthValue):
    """Custom type tmnxDiamApGyInc3GppNsapi based on TruthValue"""
    defaultValue = 1


_TmnxDiamApGyInc3GppNsapi_Type.__name__ = "TruthValue"
_TmnxDiamApGyInc3GppNsapi_Object = MibTableColumn
tmnxDiamApGyInc3GppNsapi = _TmnxDiamApGyInc3GppNsapi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 16),
    _TmnxDiamApGyInc3GppNsapi_Type()
)
tmnxDiamApGyInc3GppNsapi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyInc3GppNsapi.setStatus("current")


class _TmnxDiamApGyInc3GppSessionStopIn_Type(TruthValue):
    """Custom type tmnxDiamApGyInc3GppSessionStopIn based on TruthValue"""
    defaultValue = 1


_TmnxDiamApGyInc3GppSessionStopIn_Type.__name__ = "TruthValue"
_TmnxDiamApGyInc3GppSessionStopIn_Object = MibTableColumn
tmnxDiamApGyInc3GppSessionStopIn = _TmnxDiamApGyInc3GppSessionStopIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 17),
    _TmnxDiamApGyInc3GppSessionStopIn_Type()
)
tmnxDiamApGyInc3GppSessionStopIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyInc3GppSessionStopIn.setStatus("current")


class _TmnxDiamApGyInc3GppSelectionMode_Type(TruthValue):
    """Custom type tmnxDiamApGyInc3GppSelectionMode based on TruthValue"""
    defaultValue = 1


_TmnxDiamApGyInc3GppSelectionMode_Type.__name__ = "TruthValue"
_TmnxDiamApGyInc3GppSelectionMode_Object = MibTableColumn
tmnxDiamApGyInc3GppSelectionMode = _TmnxDiamApGyInc3GppSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 18),
    _TmnxDiamApGyInc3GppSelectionMode_Type()
)
tmnxDiamApGyInc3GppSelectionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyInc3GppSelectionMode.setStatus("current")


class _TmnxDiamApGyInc3GppChargingChara_Type(TruthValue):
    """Custom type tmnxDiamApGyInc3GppChargingChara based on TruthValue"""
    defaultValue = 1


_TmnxDiamApGyInc3GppChargingChara_Type.__name__ = "TruthValue"
_TmnxDiamApGyInc3GppChargingChara_Object = MibTableColumn
tmnxDiamApGyInc3GppChargingChara = _TmnxDiamApGyInc3GppChargingChara_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 19),
    _TmnxDiamApGyInc3GppChargingChara_Type()
)
tmnxDiamApGyInc3GppChargingChara.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyInc3GppChargingChara.setStatus("current")


class _TmnxDiamApGyInc3GppRatType_Type(Unsigned32):
    """Custom type tmnxDiamApGyInc3GppRatType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TmnxDiamApGyInc3GppRatType_Type.__name__ = "Unsigned32"
_TmnxDiamApGyInc3GppRatType_Object = MibTableColumn
tmnxDiamApGyInc3GppRatType = _TmnxDiamApGyInc3GppRatType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 20),
    _TmnxDiamApGyInc3GppRatType_Type()
)
tmnxDiamApGyInc3GppRatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyInc3GppRatType.setStatus("current")


class _TmnxDiamApGyIncGgsnAddress_Type(Integer32):
    """Custom type tmnxDiamApGyIncGgsnAddress based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ipv4", 1),
          ("ipv6", 2))
    )


_TmnxDiamApGyIncGgsnAddress_Type.__name__ = "Integer32"
_TmnxDiamApGyIncGgsnAddress_Object = MibTableColumn
tmnxDiamApGyIncGgsnAddress = _TmnxDiamApGyIncGgsnAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 21),
    _TmnxDiamApGyIncGgsnAddress_Type()
)
tmnxDiamApGyIncGgsnAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyIncGgsnAddress.setStatus("current")


class _TmnxDiamApGyIncPsInformation_Type(TruthValue):
    """Custom type tmnxDiamApGyIncPsInformation based on TruthValue"""
    defaultValue = 2


_TmnxDiamApGyIncPsInformation_Type.__name__ = "TruthValue"
_TmnxDiamApGyIncPsInformation_Object = MibTableColumn
tmnxDiamApGyIncPsInformation = _TmnxDiamApGyIncPsInformation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 22),
    _TmnxDiamApGyIncPsInformation_Type()
)
tmnxDiamApGyIncPsInformation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyIncPsInformation.setStatus("current")


class _TmnxDiamApGyIncChargingRBaseName_Type(TruthValue):
    """Custom type tmnxDiamApGyIncChargingRBaseName based on TruthValue"""
    defaultValue = 1


_TmnxDiamApGyIncChargingRBaseName_Type.__name__ = "TruthValue"
_TmnxDiamApGyIncChargingRBaseName_Object = MibTableColumn
tmnxDiamApGyIncChargingRBaseName = _TmnxDiamApGyIncChargingRBaseName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 23),
    _TmnxDiamApGyIncChargingRBaseName_Type()
)
tmnxDiamApGyIncChargingRBaseName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyIncChargingRBaseName.setStatus("current")


class _TmnxDiamApGyChargingRuleBaseName_Type(DisplayString):
    """Custom type tmnxDiamApGyChargingRuleBaseName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxDiamApGyChargingRuleBaseName_Type.__name__ = "DisplayString"
_TmnxDiamApGyChargingRuleBaseName_Object = MibTableColumn
tmnxDiamApGyChargingRuleBaseName = _TmnxDiamApGyChargingRuleBaseName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 24),
    _TmnxDiamApGyChargingRuleBaseName_Type()
)
tmnxDiamApGyChargingRuleBaseName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyChargingRuleBaseName.setStatus("current")


class _TmnxDiamApGyIncPdpContextType_Type(TruthValue):
    """Custom type tmnxDiamApGyIncPdpContextType based on TruthValue"""
    defaultValue = 1


_TmnxDiamApGyIncPdpContextType_Type.__name__ = "TruthValue"
_TmnxDiamApGyIncPdpContextType_Object = MibTableColumn
tmnxDiamApGyIncPdpContextType = _TmnxDiamApGyIncPdpContextType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 25),
    _TmnxDiamApGyIncPdpContextType_Type()
)
tmnxDiamApGyIncPdpContextType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyIncPdpContextType.setStatus("current")


class _TmnxDiamApGyIncUserEqInfoType_Type(Integer32):
    """Custom type tmnxDiamApGyIncUserEqInfoType based on Integer32"""
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
          ("imeisv", 1))
    )


_TmnxDiamApGyIncUserEqInfoType_Type.__name__ = "Integer32"
_TmnxDiamApGyIncUserEqInfoType_Object = MibTableColumn
tmnxDiamApGyIncUserEqInfoType = _TmnxDiamApGyIncUserEqInfoType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 26),
    _TmnxDiamApGyIncUserEqInfoType_Type()
)
tmnxDiamApGyIncUserEqInfoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyIncUserEqInfoType.setStatus("current")


class _TmnxDiamApGyInc3GppUserLocInfo_Type(TruthValue):
    """Custom type tmnxDiamApGyInc3GppUserLocInfo based on TruthValue"""
    defaultValue = 2


_TmnxDiamApGyInc3GppUserLocInfo_Type.__name__ = "TruthValue"
_TmnxDiamApGyInc3GppUserLocInfo_Object = MibTableColumn
tmnxDiamApGyInc3GppUserLocInfo = _TmnxDiamApGyInc3GppUserLocInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 4, 1, 27),
    _TmnxDiamApGyInc3GppUserLocInfo_Type()
)
tmnxDiamApGyInc3GppUserLocInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGyInc3GppUserLocInfo.setStatus("current")
_TmnxDiamApGxTableLastCh_Type = TimeStamp
_TmnxDiamApGxTableLastCh_Object = MibScalar
tmnxDiamApGxTableLastCh = _TmnxDiamApGxTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 5),
    _TmnxDiamApGxTableLastCh_Type()
)
tmnxDiamApGxTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApGxTableLastCh.setStatus("current")
_TmnxDiamApGxTable_Object = MibTable
tmnxDiamApGxTable = _TmnxDiamApGxTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxDiamApGxTable.setStatus("current")
_TmnxDiamApGxEntry_Object = MibTableRow
tmnxDiamApGxEntry = _TmnxDiamApGxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1)
)
tmnxDiamApGxEntry.setIndexNames(
    (1, "TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyId"),
)
if mibBuilder.loadTexts:
    tmnxDiamApGxEntry.setStatus("current")
_TmnxDiamApGxLastMgmtChange_Type = TimeStamp
_TmnxDiamApGxLastMgmtChange_Object = MibTableColumn
tmnxDiamApGxLastMgmtChange = _TmnxDiamApGxLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 1),
    _TmnxDiamApGxLastMgmtChange_Type()
)
tmnxDiamApGxLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApGxLastMgmtChange.setStatus("current")


class _TmnxDiamApGxAvp_Type(Bits):
    """Custom type tmnxDiamApGxAvp based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("anGwAddress", 0),
          ("callingStationId", 1),
          ("calledStationId", 2),
          ("ipCanType", 3),
          ("logicalAccessId", 4),
          ("nasPort", 5),
          ("nasPortId", 6),
          ("nasPortType", 7),
          ("physicalAccessId", 8),
          ("ratType", 9),
          ("supportedFeatures", 10),
          ("userEquipmentInfo", 11),
          ("apnAmbr", 12),
          ("reserved13", 13),
          ("reserved14", 14),
          ("pdnConnectionId", 15),
          ("rai", 16),
          ("reserved17", 17),
          ("sgsnMccMnc", 18),
          ("userLocationInfo", 19))
    )

_TmnxDiamApGxAvp_Type.__name__ = "Bits"
_TmnxDiamApGxAvp_Object = MibTableColumn
tmnxDiamApGxAvp = _TmnxDiamApGxAvp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 2),
    _TmnxDiamApGxAvp_Type()
)
tmnxDiamApGxAvp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvp.setStatus("current")


class _TmnxDiamApGxAvpClngStationIdType_Type(TmnxSubCallingStationIdType):
    """Custom type tmnxDiamApGxAvpClngStationIdType based on TmnxSubCallingStationIdType"""
    defaultValue = 1


_TmnxDiamApGxAvpClngStationIdType_Type.__name__ = "TmnxSubCallingStationIdType"
_TmnxDiamApGxAvpClngStationIdType_Object = MibTableColumn
tmnxDiamApGxAvpClngStationIdType = _TmnxDiamApGxAvpClngStationIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 3),
    _TmnxDiamApGxAvpClngStationIdType_Type()
)
tmnxDiamApGxAvpClngStationIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpClngStationIdType.setStatus("current")


class _TmnxDiamApGxAvpNasPortBitspec_Type(TmnxBinarySpecification):
    """Custom type tmnxDiamApGxAvpNasPortBitspec based on TmnxBinarySpecification"""
    defaultValue = OctetString("")


_TmnxDiamApGxAvpNasPortBitspec_Type.__name__ = "TmnxBinarySpecification"
_TmnxDiamApGxAvpNasPortBitspec_Object = MibTableColumn
tmnxDiamApGxAvpNasPortBitspec = _TmnxDiamApGxAvpNasPortBitspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 4),
    _TmnxDiamApGxAvpNasPortBitspec_Type()
)
tmnxDiamApGxAvpNasPortBitspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpNasPortBitspec.setStatus("current")


class _TmnxDiamApGxAvpNasPortIdPfixType_Type(TmnxSubNasPortPrefixType):
    """Custom type tmnxDiamApGxAvpNasPortIdPfixType based on TmnxSubNasPortPrefixType"""
    defaultValue = 0


_TmnxDiamApGxAvpNasPortIdPfixType_Type.__name__ = "TmnxSubNasPortPrefixType"
_TmnxDiamApGxAvpNasPortIdPfixType_Object = MibTableColumn
tmnxDiamApGxAvpNasPortIdPfixType = _TmnxDiamApGxAvpNasPortIdPfixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 5),
    _TmnxDiamApGxAvpNasPortIdPfixType_Type()
)
tmnxDiamApGxAvpNasPortIdPfixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpNasPortIdPfixType.setStatus("current")


class _TmnxDiamApGxAvpNasPortIdPfixStr_Type(DisplayString):
    """Custom type tmnxDiamApGxAvpNasPortIdPfixStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxDiamApGxAvpNasPortIdPfixStr_Type.__name__ = "DisplayString"
_TmnxDiamApGxAvpNasPortIdPfixStr_Object = MibTableColumn
tmnxDiamApGxAvpNasPortIdPfixStr = _TmnxDiamApGxAvpNasPortIdPfixStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 6),
    _TmnxDiamApGxAvpNasPortIdPfixStr_Type()
)
tmnxDiamApGxAvpNasPortIdPfixStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpNasPortIdPfixStr.setStatus("current")


class _TmnxDiamApGxAvpNasPortIdSfixType_Type(Integer32):
    """Custom type tmnxDiamApGxAvpNasPortIdSfixType based on Integer32"""
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
        *(("none", 0),
          ("circuitId", 1),
          ("remoteId", 2),
          ("userString", 3))
    )


_TmnxDiamApGxAvpNasPortIdSfixType_Type.__name__ = "Integer32"
_TmnxDiamApGxAvpNasPortIdSfixType_Object = MibTableColumn
tmnxDiamApGxAvpNasPortIdSfixType = _TmnxDiamApGxAvpNasPortIdSfixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 7),
    _TmnxDiamApGxAvpNasPortIdSfixType_Type()
)
tmnxDiamApGxAvpNasPortIdSfixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpNasPortIdSfixType.setStatus("current")


class _TmnxDiamApGxAvpNasPortTypeValue_Type(Unsigned32):
    """Custom type tmnxDiamApGxAvpNasPortTypeValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxDiamApGxAvpNasPortTypeValue_Type.__name__ = "Unsigned32"
_TmnxDiamApGxAvpNasPortTypeValue_Object = MibTableColumn
tmnxDiamApGxAvpNasPortTypeValue = _TmnxDiamApGxAvpNasPortTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 8),
    _TmnxDiamApGxAvpNasPortTypeValue_Type()
)
tmnxDiamApGxAvpNasPortTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpNasPortTypeValue.setStatus("current")


class _TmnxDiamApGxAvpUeInfoType_Type(Integer32):
    """Custom type tmnxDiamApGxAvpUeInfoType based on Integer32"""
    defaultValue = 1

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
        *(("imeisv", 0),
          ("mac", 1),
          ("eui64", 2),
          ("modifiedEui64", 3))
    )


_TmnxDiamApGxAvpUeInfoType_Type.__name__ = "Integer32"
_TmnxDiamApGxAvpUeInfoType_Object = MibTableColumn
tmnxDiamApGxAvpUeInfoType = _TmnxDiamApGxAvpUeInfoType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 9),
    _TmnxDiamApGxAvpUeInfoType_Type()
)
tmnxDiamApGxAvpUeInfoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpUeInfoType.setStatus("current")


class _TmnxDiamApGxSubIdOrg_Type(TmnxDiamPlcyDccaAvpOriginType):
    """Custom type tmnxDiamApGxSubIdOrg based on TmnxDiamPlcyDccaAvpOriginType"""
    defaultValue = 1

    subtypeSpec = TmnxDiamPlcyDccaAvpOriginType.subtypeSpec
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("subscriberId", 1),
          ("circuitId", 2),
          ("imsi", 3),
          ("msisdn", 4),
          ("imei", 5),
          ("dualStackRemoteId", 6),
          ("mac", 7),
          ("username", 8),
          ("nasPortId", 9))
    )


_TmnxDiamApGxSubIdOrg_Type.__name__ = "TmnxDiamPlcyDccaAvpOriginType"
_TmnxDiamApGxSubIdOrg_Object = MibTableColumn
tmnxDiamApGxSubIdOrg = _TmnxDiamApGxSubIdOrg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 10),
    _TmnxDiamApGxSubIdOrg_Type()
)
tmnxDiamApGxSubIdOrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxSubIdOrg.setStatus("current")


class _TmnxDiamApGxSubIdType_Type(Integer32):
    """Custom type tmnxDiamApGxSubIdType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e164", 0),
          ("imsi", 1),
          ("nai", 3),
          ("private", 4))
    )


_TmnxDiamApGxSubIdType_Type.__name__ = "Integer32"
_TmnxDiamApGxSubIdType_Object = MibTableColumn
tmnxDiamApGxSubIdType = _TmnxDiamApGxSubIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 11),
    _TmnxDiamApGxSubIdType_Type()
)
tmnxDiamApGxSubIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxSubIdType.setStatus("current")


class _TmnxDiamApGxMacFormat_Type(TmnxMacSpecification):
    """Custom type tmnxDiamApGxMacFormat based on TmnxMacSpecification"""
    defaultValue = OctetString("aa:")

    subtypeSpec = TmnxMacSpecification.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 7),
    )


_TmnxDiamApGxMacFormat_Type.__name__ = "TmnxMacSpecification"
_TmnxDiamApGxMacFormat_Object = MibTableColumn
tmnxDiamApGxMacFormat = _TmnxDiamApGxMacFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 12),
    _TmnxDiamApGxMacFormat_Type()
)
tmnxDiamApGxMacFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxMacFormat.setStatus("current")


class _TmnxDiamApGxReportIpAddrEvent_Type(TruthValue):
    """Custom type tmnxDiamApGxReportIpAddrEvent based on TruthValue"""
    defaultValue = 1


_TmnxDiamApGxReportIpAddrEvent_Type.__name__ = "TruthValue"
_TmnxDiamApGxReportIpAddrEvent_Object = MibTableColumn
tmnxDiamApGxReportIpAddrEvent = _TmnxDiamApGxReportIpAddrEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 13),
    _TmnxDiamApGxReportIpAddrEvent_Type()
)
tmnxDiamApGxReportIpAddrEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxReportIpAddrEvent.setStatus("current")


class _TmnxDiamApGxAvpNasPortIdSfixStr_Type(DisplayString):
    """Custom type tmnxDiamApGxAvpNasPortIdSfixStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxDiamApGxAvpNasPortIdSfixStr_Type.__name__ = "DisplayString"
_TmnxDiamApGxAvpNasPortIdSfixStr_Object = MibTableColumn
tmnxDiamApGxAvpNasPortIdSfixStr = _TmnxDiamApGxAvpNasPortIdSfixStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 14),
    _TmnxDiamApGxAvpNasPortIdSfixStr_Type()
)
tmnxDiamApGxAvpNasPortIdSfixStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxAvpNasPortIdSfixStr.setStatus("current")


class _TmnxDiamApGxCcrtReplayInterval_Type(Unsigned32):
    """Custom type tmnxDiamApGxCcrtReplayInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 86400),
    )


_TmnxDiamApGxCcrtReplayInterval_Type.__name__ = "Unsigned32"
_TmnxDiamApGxCcrtReplayInterval_Object = MibTableColumn
tmnxDiamApGxCcrtReplayInterval = _TmnxDiamApGxCcrtReplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 15),
    _TmnxDiamApGxCcrtReplayInterval_Type()
)
tmnxDiamApGxCcrtReplayInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxCcrtReplayInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxDiamApGxCcrtReplayInterval.setUnits("seconds")


class _TmnxDiamApGxCreditMcsInterval_Type(Unsigned32):
    """Custom type tmnxDiamApGxCreditMcsInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_TmnxDiamApGxCreditMcsInterval_Type.__name__ = "Unsigned32"
_TmnxDiamApGxCreditMcsInterval_Object = MibTableColumn
tmnxDiamApGxCreditMcsInterval = _TmnxDiamApGxCreditMcsInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 16),
    _TmnxDiamApGxCreditMcsInterval_Type()
)
tmnxDiamApGxCreditMcsInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxCreditMcsInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamApGxCreditMcsInterval.setUnits("minutes")


class _TmnxDiamApGxExtendedBw_Type(TruthValue):
    """Custom type tmnxDiamApGxExtendedBw based on TruthValue"""
    defaultValue = 2


_TmnxDiamApGxExtendedBw_Type.__name__ = "TruthValue"
_TmnxDiamApGxExtendedBw_Object = MibTableColumn
tmnxDiamApGxExtendedBw = _TmnxDiamApGxExtendedBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 6, 1, 17),
    _TmnxDiamApGxExtendedBw_Type()
)
tmnxDiamApGxExtendedBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGxExtendedBw.setStatus("current")
_TmnxDiamApNqTableLastCh_Type = TimeStamp
_TmnxDiamApNqTableLastCh_Object = MibScalar
tmnxDiamApNqTableLastCh = _TmnxDiamApNqTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 7),
    _TmnxDiamApNqTableLastCh_Type()
)
tmnxDiamApNqTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApNqTableLastCh.setStatus("current")
_TmnxDiamApNqTable_Object = MibTable
tmnxDiamApNqTable = _TmnxDiamApNqTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8)
)
if mibBuilder.loadTexts:
    tmnxDiamApNqTable.setStatus("current")
_TmnxDiamApNqEntry_Object = MibTableRow
tmnxDiamApNqEntry = _TmnxDiamApNqEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1)
)
tmnxDiamApNqEntry.setIndexNames(
    (1, "TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyId"),
)
if mibBuilder.loadTexts:
    tmnxDiamApNqEntry.setStatus("current")
_TmnxDiamApNqLastMgmtChange_Type = TimeStamp
_TmnxDiamApNqLastMgmtChange_Object = MibTableColumn
tmnxDiamApNqLastMgmtChange = _TmnxDiamApNqLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 1),
    _TmnxDiamApNqLastMgmtChange_Type()
)
tmnxDiamApNqLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApNqLastMgmtChange.setStatus("current")


class _TmnxDiamApNqAvp_Type(Bits):
    """Custom type tmnxDiamApNqAvp based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("circuitId", 0),
          ("remote-id", 1),
          ("calledStationId", 2),
          ("callingStationId", 3),
          ("nasPort", 4),
          ("nasPortId", 5),
          ("nasPortType", 6),
          ("imei", 7),
          ("ratType", 8),
          ("userLocationInfo", 9))
    )

_TmnxDiamApNqAvp_Type.__name__ = "Bits"
_TmnxDiamApNqAvp_Object = MibTableColumn
tmnxDiamApNqAvp = _TmnxDiamApNqAvp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 2),
    _TmnxDiamApNqAvp_Type()
)
tmnxDiamApNqAvp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqAvp.setStatus("current")


class _TmnxDiamApNqAvpClngStationIdType_Type(TmnxSubCallingStationIdType):
    """Custom type tmnxDiamApNqAvpClngStationIdType based on TmnxSubCallingStationIdType"""
    defaultValue = 1


_TmnxDiamApNqAvpClngStationIdType_Type.__name__ = "TmnxSubCallingStationIdType"
_TmnxDiamApNqAvpClngStationIdType_Object = MibTableColumn
tmnxDiamApNqAvpClngStationIdType = _TmnxDiamApNqAvpClngStationIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 3),
    _TmnxDiamApNqAvpClngStationIdType_Type()
)
tmnxDiamApNqAvpClngStationIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqAvpClngStationIdType.setStatus("current")


class _TmnxDiamApNqAvpNasPortBitspec_Type(TmnxBinarySpecification):
    """Custom type tmnxDiamApNqAvpNasPortBitspec based on TmnxBinarySpecification"""
    defaultValue = OctetString("")


_TmnxDiamApNqAvpNasPortBitspec_Type.__name__ = "TmnxBinarySpecification"
_TmnxDiamApNqAvpNasPortBitspec_Object = MibTableColumn
tmnxDiamApNqAvpNasPortBitspec = _TmnxDiamApNqAvpNasPortBitspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 4),
    _TmnxDiamApNqAvpNasPortBitspec_Type()
)
tmnxDiamApNqAvpNasPortBitspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqAvpNasPortBitspec.setStatus("current")


class _TmnxDiamApNqAvpNasPortIdPfixType_Type(TmnxSubNasPortPrefixType):
    """Custom type tmnxDiamApNqAvpNasPortIdPfixType based on TmnxSubNasPortPrefixType"""
    defaultValue = 0


_TmnxDiamApNqAvpNasPortIdPfixType_Type.__name__ = "TmnxSubNasPortPrefixType"
_TmnxDiamApNqAvpNasPortIdPfixType_Object = MibTableColumn
tmnxDiamApNqAvpNasPortIdPfixType = _TmnxDiamApNqAvpNasPortIdPfixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 5),
    _TmnxDiamApNqAvpNasPortIdPfixType_Type()
)
tmnxDiamApNqAvpNasPortIdPfixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqAvpNasPortIdPfixType.setStatus("current")


class _TmnxDiamApNqAvpNasPortIdPfixStr_Type(DisplayString):
    """Custom type tmnxDiamApNqAvpNasPortIdPfixStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxDiamApNqAvpNasPortIdPfixStr_Type.__name__ = "DisplayString"
_TmnxDiamApNqAvpNasPortIdPfixStr_Object = MibTableColumn
tmnxDiamApNqAvpNasPortIdPfixStr = _TmnxDiamApNqAvpNasPortIdPfixStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 6),
    _TmnxDiamApNqAvpNasPortIdPfixStr_Type()
)
tmnxDiamApNqAvpNasPortIdPfixStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqAvpNasPortIdPfixStr.setStatus("current")


class _TmnxDiamApNqAvpNasPortIdSfixType_Type(Integer32):
    """Custom type tmnxDiamApNqAvpNasPortIdSfixType based on Integer32"""
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
        *(("none", 0),
          ("circuitId", 1),
          ("remoteId", 2),
          ("userString", 3))
    )


_TmnxDiamApNqAvpNasPortIdSfixType_Type.__name__ = "Integer32"
_TmnxDiamApNqAvpNasPortIdSfixType_Object = MibTableColumn
tmnxDiamApNqAvpNasPortIdSfixType = _TmnxDiamApNqAvpNasPortIdSfixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 7),
    _TmnxDiamApNqAvpNasPortIdSfixType_Type()
)
tmnxDiamApNqAvpNasPortIdSfixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqAvpNasPortIdSfixType.setStatus("current")


class _TmnxDiamApNqAvpNasPortIdSfixStr_Type(DisplayString):
    """Custom type tmnxDiamApNqAvpNasPortIdSfixStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxDiamApNqAvpNasPortIdSfixStr_Type.__name__ = "DisplayString"
_TmnxDiamApNqAvpNasPortIdSfixStr_Object = MibTableColumn
tmnxDiamApNqAvpNasPortIdSfixStr = _TmnxDiamApNqAvpNasPortIdSfixStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 8),
    _TmnxDiamApNqAvpNasPortIdSfixStr_Type()
)
tmnxDiamApNqAvpNasPortIdSfixStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqAvpNasPortIdSfixStr.setStatus("current")


class _TmnxDiamApNqAvpNasPortTypeType_Type(TmnxSubNasPortTypeType):
    """Custom type tmnxDiamApNqAvpNasPortTypeType based on TmnxSubNasPortTypeType"""
    defaultValue = 1


_TmnxDiamApNqAvpNasPortTypeType_Type.__name__ = "TmnxSubNasPortTypeType"
_TmnxDiamApNqAvpNasPortTypeType_Object = MibTableColumn
tmnxDiamApNqAvpNasPortTypeType = _TmnxDiamApNqAvpNasPortTypeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 9),
    _TmnxDiamApNqAvpNasPortTypeType_Type()
)
tmnxDiamApNqAvpNasPortTypeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqAvpNasPortTypeType.setStatus("current")


class _TmnxDiamApNqAvpNasPortTypeValue_Type(Unsigned32):
    """Custom type tmnxDiamApNqAvpNasPortTypeValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxDiamApNqAvpNasPortTypeValue_Type.__name__ = "Unsigned32"
_TmnxDiamApNqAvpNasPortTypeValue_Object = MibTableColumn
tmnxDiamApNqAvpNasPortTypeValue = _TmnxDiamApNqAvpNasPortTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 10),
    _TmnxDiamApNqAvpNasPortTypeValue_Type()
)
tmnxDiamApNqAvpNasPortTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqAvpNasPortTypeValue.setStatus("current")


class _TmnxDiamApNqPassword_Type(TmnxAuthPassword):
    """Custom type tmnxDiamApNqPassword based on TmnxAuthPassword"""
    defaultValue = OctetString("")


_TmnxDiamApNqPassword_Type.__name__ = "TmnxAuthPassword"
_TmnxDiamApNqPassword_Object = MibTableColumn
tmnxDiamApNqPassword = _TmnxDiamApNqPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 11),
    _TmnxDiamApNqPassword_Type()
)
tmnxDiamApNqPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqPassword.setStatus("current")


class _TmnxDiamApNqUserNameFormat_Type(Integer32):
    """Custom type tmnxDiamApNqUserNameFormat based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("circuitId", 2),
          ("tuple", 3),
          ("asciiConvertedCircuitId", 4),
          ("asciiConvertedTuple", 5),
          ("dhcpClientVendorOpts", 6),
          ("macGiaddr", 7),
          ("nasPortId", 8))
    )


_TmnxDiamApNqUserNameFormat_Type.__name__ = "Integer32"
_TmnxDiamApNqUserNameFormat_Object = MibTableColumn
tmnxDiamApNqUserNameFormat = _TmnxDiamApNqUserNameFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 12),
    _TmnxDiamApNqUserNameFormat_Type()
)
tmnxDiamApNqUserNameFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqUserNameFormat.setStatus("current")


class _TmnxDiamApNqUserNameOp_Type(TmnxSubAuthPlcyUserNameOp):
    """Custom type tmnxDiamApNqUserNameOp based on TmnxSubAuthPlcyUserNameOp"""
    defaultValue = 0


_TmnxDiamApNqUserNameOp_Type.__name__ = "TmnxSubAuthPlcyUserNameOp"
_TmnxDiamApNqUserNameOp_Object = MibTableColumn
tmnxDiamApNqUserNameOp = _TmnxDiamApNqUserNameOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 13),
    _TmnxDiamApNqUserNameOp_Type()
)
tmnxDiamApNqUserNameOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqUserNameOp.setStatus("current")


class _TmnxDiamApNqDomain_Type(DisplayString):
    """Custom type tmnxDiamApNqDomain based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TmnxDiamApNqDomain_Type.__name__ = "DisplayString"
_TmnxDiamApNqDomain_Object = MibTableColumn
tmnxDiamApNqDomain = _TmnxDiamApNqDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 14),
    _TmnxDiamApNqDomain_Type()
)
tmnxDiamApNqDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqDomain.setStatus("current")


class _TmnxDiamApNqMacFormat_Type(TmnxMacSpecification):
    """Custom type tmnxDiamApNqMacFormat based on TmnxMacSpecification"""
    defaultValue = OctetString("aa:")

    subtypeSpec = TmnxMacSpecification.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 7),
    )


_TmnxDiamApNqMacFormat_Type.__name__ = "TmnxMacSpecification"
_TmnxDiamApNqMacFormat_Object = MibTableColumn
tmnxDiamApNqMacFormat = _TmnxDiamApNqMacFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 8, 1, 15),
    _TmnxDiamApNqMacFormat_Type()
)
tmnxDiamApNqMacFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApNqMacFormat.setStatus("current")
_TmnxDiamPpPrxTableLastCh_Type = TimeStamp
_TmnxDiamPpPrxTableLastCh_Object = MibScalar
tmnxDiamPpPrxTableLastCh = _TmnxDiamPpPrxTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 9),
    _TmnxDiamPpPrxTableLastCh_Type()
)
tmnxDiamPpPrxTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxTableLastCh.setStatus("current")
_TmnxDiamPpPrxTable_Object = MibTable
tmnxDiamPpPrxTable = _TmnxDiamPpPrxTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10)
)
if mibBuilder.loadTexts:
    tmnxDiamPpPrxTable.setStatus("current")
_TmnxDiamPpPrxEntry_Object = MibTableRow
tmnxDiamPpPrxEntry = _TmnxDiamPpPrxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1)
)
tmnxDiamPpPrxEntry.setIndexNames(
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxDiamPpPrxEntry.setStatus("current")
_TmnxDiamPpPrxLastMgmtChange_Type = TimeStamp
_TmnxDiamPpPrxLastMgmtChange_Object = MibTableColumn
tmnxDiamPpPrxLastMgmtChange = _TmnxDiamPpPrxLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 1),
    _TmnxDiamPpPrxLastMgmtChange_Type()
)
tmnxDiamPpPrxLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxLastMgmtChange.setStatus("current")


class _TmnxDiamPpPrxAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxDiamPpPrxAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxDiamPpPrxAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxDiamPpPrxAdminState_Object = MibTableColumn
tmnxDiamPpPrxAdminState = _TmnxDiamPpPrxAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 2),
    _TmnxDiamPpPrxAdminState_Type()
)
tmnxDiamPpPrxAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxAdminState.setStatus("current")


class _TmnxDiamPpPrxRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxDiamPpPrxRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxDiamPpPrxRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxDiamPpPrxRouter_Object = MibTableColumn
tmnxDiamPpPrxRouter = _TmnxDiamPpPrxRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 3),
    _TmnxDiamPpPrxRouter_Type()
)
tmnxDiamPpPrxRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxRouter.setStatus("current")


class _TmnxDiamPpPrxAddrType_Type(InetAddressType):
    """Custom type tmnxDiamPpPrxAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxDiamPpPrxAddrType_Type.__name__ = "InetAddressType"
_TmnxDiamPpPrxAddrType_Object = MibTableColumn
tmnxDiamPpPrxAddrType = _TmnxDiamPpPrxAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 4),
    _TmnxDiamPpPrxAddrType_Type()
)
tmnxDiamPpPrxAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxAddrType.setStatus("current")


class _TmnxDiamPpPrxAddr_Type(InetAddress):
    """Custom type tmnxDiamPpPrxAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDiamPpPrxAddr_Type.__name__ = "InetAddress"
_TmnxDiamPpPrxAddr_Object = MibTableColumn
tmnxDiamPpPrxAddr = _TmnxDiamPpPrxAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 5),
    _TmnxDiamPpPrxAddr_Type()
)
tmnxDiamPpPrxAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxAddr.setStatus("current")


class _TmnxDiamPpPrxOperState_Type(Integer32):
    """Custom type tmnxDiamPpPrxOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_TmnxDiamPpPrxOperState_Type.__name__ = "Integer32"
_TmnxDiamPpPrxOperState_Object = MibTableColumn
tmnxDiamPpPrxOperState = _TmnxDiamPpPrxOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 6),
    _TmnxDiamPpPrxOperState_Type()
)
tmnxDiamPpPrxOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxOperState.setStatus("current")
_TmnxDiamPpPrxMcLocState_Type = TmnxDiamProxyState
_TmnxDiamPpPrxMcLocState_Object = MibTableColumn
tmnxDiamPpPrxMcLocState = _TmnxDiamPpPrxMcLocState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 7),
    _TmnxDiamPpPrxMcLocState_Type()
)
tmnxDiamPpPrxMcLocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxMcLocState.setStatus("current")
_TmnxDiamPpPrxMcLocOriginStateId_Type = Unsigned32
_TmnxDiamPpPrxMcLocOriginStateId_Object = MibTableColumn
tmnxDiamPpPrxMcLocOriginStateId = _TmnxDiamPpPrxMcLocOriginStateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 8),
    _TmnxDiamPpPrxMcLocOriginStateId_Type()
)
tmnxDiamPpPrxMcLocOriginStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxMcLocOriginStateId.setStatus("current")
_TmnxDiamPpPrxMcLocMacAddress_Type = MacAddress
_TmnxDiamPpPrxMcLocMacAddress_Object = MibTableColumn
tmnxDiamPpPrxMcLocMacAddress = _TmnxDiamPpPrxMcLocMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 9),
    _TmnxDiamPpPrxMcLocMacAddress_Type()
)
tmnxDiamPpPrxMcLocMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxMcLocMacAddress.setStatus("current")
_TmnxDiamPpPrxMcLocCtrlMacAddress_Type = MacAddress
_TmnxDiamPpPrxMcLocCtrlMacAddress_Object = MibTableColumn
tmnxDiamPpPrxMcLocCtrlMacAddress = _TmnxDiamPpPrxMcLocCtrlMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 10),
    _TmnxDiamPpPrxMcLocCtrlMacAddress_Type()
)
tmnxDiamPpPrxMcLocCtrlMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxMcLocCtrlMacAddress.setStatus("current")
_TmnxDiamPpPrxMcRemState_Type = TmnxDiamProxyState
_TmnxDiamPpPrxMcRemState_Object = MibTableColumn
tmnxDiamPpPrxMcRemState = _TmnxDiamPpPrxMcRemState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 11),
    _TmnxDiamPpPrxMcRemState_Type()
)
tmnxDiamPpPrxMcRemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxMcRemState.setStatus("current")
_TmnxDiamPpPrxMcRemOriginStateId_Type = Unsigned32
_TmnxDiamPpPrxMcRemOriginStateId_Object = MibTableColumn
tmnxDiamPpPrxMcRemOriginStateId = _TmnxDiamPpPrxMcRemOriginStateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 12),
    _TmnxDiamPpPrxMcRemOriginStateId_Type()
)
tmnxDiamPpPrxMcRemOriginStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxMcRemOriginStateId.setStatus("current")
_TmnxDiamPpPrxMcRemMacAddress_Type = MacAddress
_TmnxDiamPpPrxMcRemMacAddress_Object = MibTableColumn
tmnxDiamPpPrxMcRemMacAddress = _TmnxDiamPpPrxMcRemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 13),
    _TmnxDiamPpPrxMcRemMacAddress_Type()
)
tmnxDiamPpPrxMcRemMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxMcRemMacAddress.setStatus("current")
_TmnxDiamPpPrxMcRemCtrlMacAddress_Type = MacAddress
_TmnxDiamPpPrxMcRemCtrlMacAddress_Object = MibTableColumn
tmnxDiamPpPrxMcRemCtrlMacAddress = _TmnxDiamPpPrxMcRemCtrlMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 10, 1, 14),
    _TmnxDiamPpPrxMcRemCtrlMacAddress_Type()
)
tmnxDiamPpPrxMcRemCtrlMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxMcRemCtrlMacAddress.setStatus("current")
_TmnxDiamPpPrxClientTable_Object = MibTable
tmnxDiamPpPrxClientTable = _TmnxDiamPpPrxClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 11)
)
if mibBuilder.loadTexts:
    tmnxDiamPpPrxClientTable.setStatus("current")
_TmnxDiamPpPrxClientEntry_Object = MibTableRow
tmnxDiamPpPrxClientEntry = _TmnxDiamPpPrxClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 11, 1)
)
tmnxDiamPpPrxClientEntry.setIndexNames(
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyName"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxClientIpAddrType"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxClientIpAddr"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxClientPort"),
)
if mibBuilder.loadTexts:
    tmnxDiamPpPrxClientEntry.setStatus("current")
_TmnxDiamPpPrxClientIpAddrType_Type = InetAddressType
_TmnxDiamPpPrxClientIpAddrType_Object = MibTableColumn
tmnxDiamPpPrxClientIpAddrType = _TmnxDiamPpPrxClientIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 11, 1, 1),
    _TmnxDiamPpPrxClientIpAddrType_Type()
)
tmnxDiamPpPrxClientIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxClientIpAddrType.setStatus("current")


class _TmnxDiamPpPrxClientIpAddr_Type(InetAddress):
    """Custom type tmnxDiamPpPrxClientIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDiamPpPrxClientIpAddr_Type.__name__ = "InetAddress"
_TmnxDiamPpPrxClientIpAddr_Object = MibTableColumn
tmnxDiamPpPrxClientIpAddr = _TmnxDiamPpPrxClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 11, 1, 2),
    _TmnxDiamPpPrxClientIpAddr_Type()
)
tmnxDiamPpPrxClientIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxClientIpAddr.setStatus("current")
_TmnxDiamPpPrxClientPort_Type = InetPortNumber
_TmnxDiamPpPrxClientPort_Object = MibTableColumn
tmnxDiamPpPrxClientPort = _TmnxDiamPpPrxClientPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 11, 1, 3),
    _TmnxDiamPpPrxClientPort_Type()
)
tmnxDiamPpPrxClientPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxClientPort.setStatus("current")


class _TmnxDiamPpPrxClientPsmState_Type(Integer32):
    """Custom type tmnxDiamPpPrxClientPsmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rOpen", 1),
          ("waitRcer", 2))
    )


_TmnxDiamPpPrxClientPsmState_Type.__name__ = "Integer32"
_TmnxDiamPpPrxClientPsmState_Object = MibTableColumn
tmnxDiamPpPrxClientPsmState = _TmnxDiamPpPrxClientPsmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 11, 1, 4),
    _TmnxDiamPpPrxClientPsmState_Type()
)
tmnxDiamPpPrxClientPsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxClientPsmState.setStatus("current")
_TmnxDiamPpPrxClientTransactions_Type = Gauge32
_TmnxDiamPpPrxClientTransactions_Object = MibTableColumn
tmnxDiamPpPrxClientTransactions = _TmnxDiamPpPrxClientTransactions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 11, 1, 5),
    _TmnxDiamPpPrxClientTransactions_Type()
)
tmnxDiamPpPrxClientTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPpPrxClientTransactions.setStatus("current")
_TmnxDiamPrxClStTable_Object = MibTable
tmnxDiamPrxClStTable = _TmnxDiamPrxClStTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12)
)
if mibBuilder.loadTexts:
    tmnxDiamPrxClStTable.setStatus("obsolete")
_TmnxDiamPrxClStEntry_Object = MibTableRow
tmnxDiamPrxClStEntry = _TmnxDiamPrxClStEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamPrxClStEntry.setStatus("obsolete")
_TmnxDiamPrxClStLastClearedTime_Type = TimeStamp
_TmnxDiamPrxClStLastClearedTime_Object = MibTableColumn
tmnxDiamPrxClStLastClearedTime = _TmnxDiamPrxClStLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 1),
    _TmnxDiamPrxClStLastClearedTime_Type()
)
tmnxDiamPrxClStLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStLastClearedTime.setStatus("obsolete")
_TmnxDiamPrxClStCiTcpSendFailed_Type = Counter32
_TmnxDiamPrxClStCiTcpSendFailed_Object = MibTableColumn
tmnxDiamPrxClStCiTcpSendFailed = _TmnxDiamPrxClStCiTcpSendFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 2),
    _TmnxDiamPrxClStCiTcpSendFailed_Type()
)
tmnxDiamPrxClStCiTcpSendFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCiTcpSendFailed.setStatus("obsolete")
_TmnxDiamPrxClStCiDiamRxDropCnt_Type = Counter32
_TmnxDiamPrxClStCiDiamRxDropCnt_Object = MibTableColumn
tmnxDiamPrxClStCiDiamRxDropCnt = _TmnxDiamPrxClStCiDiamRxDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 3),
    _TmnxDiamPrxClStCiDiamRxDropCnt_Type()
)
tmnxDiamPrxClStCiDiamRxDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCiDiamRxDropCnt.setStatus("obsolete")
_TmnxDiamPrxClStCiDiamRxReqs_Type = Counter32
_TmnxDiamPrxClStCiDiamRxReqs_Object = MibTableColumn
tmnxDiamPrxClStCiDiamRxReqs = _TmnxDiamPrxClStCiDiamRxReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 4),
    _TmnxDiamPrxClStCiDiamRxReqs_Type()
)
tmnxDiamPrxClStCiDiamRxReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCiDiamRxReqs.setStatus("obsolete")
_TmnxDiamPrxClStCiDiamTxResps_Type = Counter32
_TmnxDiamPrxClStCiDiamTxResps_Object = MibTableColumn
tmnxDiamPrxClStCiDiamTxResps = _TmnxDiamPrxClStCiDiamTxResps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 5),
    _TmnxDiamPrxClStCiDiamTxResps_Type()
)
tmnxDiamPrxClStCiDiamTxResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCiDiamTxResps.setStatus("obsolete")
_TmnxDiamPrxClStCiPendMsgsPmq_Type = Counter32
_TmnxDiamPrxClStCiPendMsgsPmq_Object = MibTableColumn
tmnxDiamPrxClStCiPendMsgsPmq = _TmnxDiamPrxClStCiPendMsgsPmq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 6),
    _TmnxDiamPrxClStCiPendMsgsPmq_Type()
)
tmnxDiamPrxClStCiPendMsgsPmq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCiPendMsgsPmq.setStatus("obsolete")
_TmnxDiamPrxClStCiReqTimeoutsPmq_Type = Counter32
_TmnxDiamPrxClStCiReqTimeoutsPmq_Object = MibTableColumn
tmnxDiamPrxClStCiReqTimeoutsPmq = _TmnxDiamPrxClStCiReqTimeoutsPmq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 7),
    _TmnxDiamPrxClStCiReqTimeoutsPmq_Type()
)
tmnxDiamPrxClStCiReqTimeoutsPmq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCiReqTimeoutsPmq.setStatus("obsolete")
_TmnxDiamPrxClStSiTcpSendFailed_Type = Counter32
_TmnxDiamPrxClStSiTcpSendFailed_Object = MibTableColumn
tmnxDiamPrxClStSiTcpSendFailed = _TmnxDiamPrxClStSiTcpSendFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 8),
    _TmnxDiamPrxClStSiTcpSendFailed_Type()
)
tmnxDiamPrxClStSiTcpSendFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStSiTcpSendFailed.setStatus("obsolete")
_TmnxDiamPrxClStSiDiamRxDropCnt_Type = Counter32
_TmnxDiamPrxClStSiDiamRxDropCnt_Object = MibTableColumn
tmnxDiamPrxClStSiDiamRxDropCnt = _TmnxDiamPrxClStSiDiamRxDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 9),
    _TmnxDiamPrxClStSiDiamRxDropCnt_Type()
)
tmnxDiamPrxClStSiDiamRxDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStSiDiamRxDropCnt.setStatus("obsolete")
_TmnxDiamPrxClStSiDiamTxReqs_Type = Counter32
_TmnxDiamPrxClStSiDiamTxReqs_Object = MibTableColumn
tmnxDiamPrxClStSiDiamTxReqs = _TmnxDiamPrxClStSiDiamTxReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 10),
    _TmnxDiamPrxClStSiDiamTxReqs_Type()
)
tmnxDiamPrxClStSiDiamTxReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStSiDiamTxReqs.setStatus("obsolete")
_TmnxDiamPrxClStSiDiamRxResps_Type = Counter32
_TmnxDiamPrxClStSiDiamRxResps_Object = MibTableColumn
tmnxDiamPrxClStSiDiamRxResps = _TmnxDiamPrxClStSiDiamRxResps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 11),
    _TmnxDiamPrxClStSiDiamRxResps_Type()
)
tmnxDiamPrxClStSiDiamRxResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStSiDiamRxResps.setStatus("obsolete")
_TmnxDiamPrxClStCcrInitialRx_Type = Counter32
_TmnxDiamPrxClStCcrInitialRx_Object = MibTableColumn
tmnxDiamPrxClStCcrInitialRx = _TmnxDiamPrxClStCcrInitialRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 14),
    _TmnxDiamPrxClStCcrInitialRx_Type()
)
tmnxDiamPrxClStCcrInitialRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCcrInitialRx.setStatus("obsolete")
_TmnxDiamPrxClStCcaInitialTx_Type = Counter32
_TmnxDiamPrxClStCcaInitialTx_Object = MibTableColumn
tmnxDiamPrxClStCcaInitialTx = _TmnxDiamPrxClStCcaInitialTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 15),
    _TmnxDiamPrxClStCcaInitialTx_Type()
)
tmnxDiamPrxClStCcaInitialTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCcaInitialTx.setStatus("obsolete")
_TmnxDiamPrxClStCcrUpdateRx_Type = Counter32
_TmnxDiamPrxClStCcrUpdateRx_Object = MibTableColumn
tmnxDiamPrxClStCcrUpdateRx = _TmnxDiamPrxClStCcrUpdateRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 16),
    _TmnxDiamPrxClStCcrUpdateRx_Type()
)
tmnxDiamPrxClStCcrUpdateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCcrUpdateRx.setStatus("obsolete")
_TmnxDiamPrxClStCcaUpdateTx_Type = Counter32
_TmnxDiamPrxClStCcaUpdateTx_Object = MibTableColumn
tmnxDiamPrxClStCcaUpdateTx = _TmnxDiamPrxClStCcaUpdateTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 17),
    _TmnxDiamPrxClStCcaUpdateTx_Type()
)
tmnxDiamPrxClStCcaUpdateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCcaUpdateTx.setStatus("obsolete")
_TmnxDiamPrxClStCcrTerminateRx_Type = Counter32
_TmnxDiamPrxClStCcrTerminateRx_Object = MibTableColumn
tmnxDiamPrxClStCcrTerminateRx = _TmnxDiamPrxClStCcrTerminateRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 18),
    _TmnxDiamPrxClStCcrTerminateRx_Type()
)
tmnxDiamPrxClStCcrTerminateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCcrTerminateRx.setStatus("obsolete")
_TmnxDiamPrxClStCcaTerminateTx_Type = Counter32
_TmnxDiamPrxClStCcaTerminateTx_Object = MibTableColumn
tmnxDiamPrxClStCcaTerminateTx = _TmnxDiamPrxClStCcaTerminateTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 19),
    _TmnxDiamPrxClStCcaTerminateTx_Type()
)
tmnxDiamPrxClStCcaTerminateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCcaTerminateTx.setStatus("obsolete")
_TmnxDiamPrxClStCerRx_Type = Counter32
_TmnxDiamPrxClStCerRx_Object = MibTableColumn
tmnxDiamPrxClStCerRx = _TmnxDiamPrxClStCerRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 20),
    _TmnxDiamPrxClStCerRx_Type()
)
tmnxDiamPrxClStCerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCerRx.setStatus("obsolete")
_TmnxDiamPrxClStCeaTx_Type = Counter32
_TmnxDiamPrxClStCeaTx_Object = MibTableColumn
tmnxDiamPrxClStCeaTx = _TmnxDiamPrxClStCeaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 21),
    _TmnxDiamPrxClStCeaTx_Type()
)
tmnxDiamPrxClStCeaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStCeaTx.setStatus("obsolete")
_TmnxDiamPrxClStDwrRx_Type = Counter32
_TmnxDiamPrxClStDwrRx_Object = MibTableColumn
tmnxDiamPrxClStDwrRx = _TmnxDiamPrxClStDwrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 22),
    _TmnxDiamPrxClStDwrRx_Type()
)
tmnxDiamPrxClStDwrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStDwrRx.setStatus("obsolete")
_TmnxDiamPrxClStDwaTx_Type = Counter32
_TmnxDiamPrxClStDwaTx_Object = MibTableColumn
tmnxDiamPrxClStDwaTx = _TmnxDiamPrxClStDwaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 23),
    _TmnxDiamPrxClStDwaTx_Type()
)
tmnxDiamPrxClStDwaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStDwaTx.setStatus("obsolete")
_TmnxDiamPrxClStDwrTx_Type = Counter32
_TmnxDiamPrxClStDwrTx_Object = MibTableColumn
tmnxDiamPrxClStDwrTx = _TmnxDiamPrxClStDwrTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 24),
    _TmnxDiamPrxClStDwrTx_Type()
)
tmnxDiamPrxClStDwrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStDwrTx.setStatus("obsolete")
_TmnxDiamPrxClStDwaRx_Type = Counter32
_TmnxDiamPrxClStDwaRx_Object = MibTableColumn
tmnxDiamPrxClStDwaRx = _TmnxDiamPrxClStDwaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 25),
    _TmnxDiamPrxClStDwaRx_Type()
)
tmnxDiamPrxClStDwaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStDwaRx.setStatus("obsolete")
_TmnxDiamPrxClStAsrTx_Type = Counter32
_TmnxDiamPrxClStAsrTx_Object = MibTableColumn
tmnxDiamPrxClStAsrTx = _TmnxDiamPrxClStAsrTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 26),
    _TmnxDiamPrxClStAsrTx_Type()
)
tmnxDiamPrxClStAsrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStAsrTx.setStatus("obsolete")
_TmnxDiamPrxClStAsaRx_Type = Counter32
_TmnxDiamPrxClStAsaRx_Object = MibTableColumn
tmnxDiamPrxClStAsaRx = _TmnxDiamPrxClStAsaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 27),
    _TmnxDiamPrxClStAsaRx_Type()
)
tmnxDiamPrxClStAsaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStAsaRx.setStatus("obsolete")
_TmnxDiamPrxClStRarTx_Type = Counter32
_TmnxDiamPrxClStRarTx_Object = MibTableColumn
tmnxDiamPrxClStRarTx = _TmnxDiamPrxClStRarTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 28),
    _TmnxDiamPrxClStRarTx_Type()
)
tmnxDiamPrxClStRarTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStRarTx.setStatus("obsolete")
_TmnxDiamPrxClStRaaRx_Type = Counter32
_TmnxDiamPrxClStRaaRx_Object = MibTableColumn
tmnxDiamPrxClStRaaRx = _TmnxDiamPrxClStRaaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 29),
    _TmnxDiamPrxClStRaaRx_Type()
)
tmnxDiamPrxClStRaaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStRaaRx.setStatus("obsolete")
_TmnxDiamPrxClStDprTx_Type = Counter32
_TmnxDiamPrxClStDprTx_Object = MibTableColumn
tmnxDiamPrxClStDprTx = _TmnxDiamPrxClStDprTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 30),
    _TmnxDiamPrxClStDprTx_Type()
)
tmnxDiamPrxClStDprTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStDprTx.setStatus("obsolete")
_TmnxDiamPrxClStDpaRx_Type = Counter32
_TmnxDiamPrxClStDpaRx_Object = MibTableColumn
tmnxDiamPrxClStDpaRx = _TmnxDiamPrxClStDpaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 31),
    _TmnxDiamPrxClStDpaRx_Type()
)
tmnxDiamPrxClStDpaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStDpaRx.setStatus("obsolete")
_TmnxDiamPrxClStDprRx_Type = Counter32
_TmnxDiamPrxClStDprRx_Object = MibTableColumn
tmnxDiamPrxClStDprRx = _TmnxDiamPrxClStDprRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 32),
    _TmnxDiamPrxClStDprRx_Type()
)
tmnxDiamPrxClStDprRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStDprRx.setStatus("obsolete")
_TmnxDiamPrxClStDpaTx_Type = Counter32
_TmnxDiamPrxClStDpaTx_Object = MibTableColumn
tmnxDiamPrxClStDpaTx = _TmnxDiamPrxClStDpaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 33),
    _TmnxDiamPrxClStDpaTx_Type()
)
tmnxDiamPrxClStDpaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStDpaTx.setStatus("obsolete")
_TmnxDiamPrxClStAarRx_Type = Counter32
_TmnxDiamPrxClStAarRx_Object = MibTableColumn
tmnxDiamPrxClStAarRx = _TmnxDiamPrxClStAarRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 40),
    _TmnxDiamPrxClStAarRx_Type()
)
tmnxDiamPrxClStAarRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStAarRx.setStatus("obsolete")
_TmnxDiamPrxClStAaaTx_Type = Counter32
_TmnxDiamPrxClStAaaTx_Object = MibTableColumn
tmnxDiamPrxClStAaaTx = _TmnxDiamPrxClStAaaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 12, 1, 41),
    _TmnxDiamPrxClStAaaTx_Type()
)
tmnxDiamPrxClStAaaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPrxClStAaaTx.setStatus("obsolete")
_TmnxDiamPeerStatsTable_Object = MibTable
tmnxDiamPeerStatsTable = _TmnxDiamPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13)
)
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsTable.setStatus("current")
_TmnxDiamPeerStatsEntry_Object = MibTableRow
tmnxDiamPeerStatsEntry = _TmnxDiamPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1)
)
tmnxDiamPeerStatsEntry.setIndexNames(
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyName"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsPeerName"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsPeerIpAddrType"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsPeerIpAddr"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsPeerPort"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsDirection"),
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsMessageType"),
)
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsEntry.setStatus("current")
_TmnxDiamPeerStatsPeerName_Type = TNamedItemOrEmpty
_TmnxDiamPeerStatsPeerName_Object = MibTableColumn
tmnxDiamPeerStatsPeerName = _TmnxDiamPeerStatsPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 1),
    _TmnxDiamPeerStatsPeerName_Type()
)
tmnxDiamPeerStatsPeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsPeerName.setStatus("current")
_TmnxDiamPeerStatsPeerIpAddrType_Type = InetAddressType
_TmnxDiamPeerStatsPeerIpAddrType_Object = MibTableColumn
tmnxDiamPeerStatsPeerIpAddrType = _TmnxDiamPeerStatsPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 2),
    _TmnxDiamPeerStatsPeerIpAddrType_Type()
)
tmnxDiamPeerStatsPeerIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsPeerIpAddrType.setStatus("current")


class _TmnxDiamPeerStatsPeerIpAddr_Type(InetAddress):
    """Custom type tmnxDiamPeerStatsPeerIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDiamPeerStatsPeerIpAddr_Type.__name__ = "InetAddress"
_TmnxDiamPeerStatsPeerIpAddr_Object = MibTableColumn
tmnxDiamPeerStatsPeerIpAddr = _TmnxDiamPeerStatsPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 3),
    _TmnxDiamPeerStatsPeerIpAddr_Type()
)
tmnxDiamPeerStatsPeerIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsPeerIpAddr.setStatus("current")
_TmnxDiamPeerStatsPeerPort_Type = InetPortNumber
_TmnxDiamPeerStatsPeerPort_Object = MibTableColumn
tmnxDiamPeerStatsPeerPort = _TmnxDiamPeerStatsPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 4),
    _TmnxDiamPeerStatsPeerPort_Type()
)
tmnxDiamPeerStatsPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsPeerPort.setStatus("current")


class _TmnxDiamPeerStatsDirection_Type(Integer32):
    """Custom type tmnxDiamPeerStatsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_TmnxDiamPeerStatsDirection_Type.__name__ = "Integer32"
_TmnxDiamPeerStatsDirection_Object = MibTableColumn
tmnxDiamPeerStatsDirection = _TmnxDiamPeerStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 5),
    _TmnxDiamPeerStatsDirection_Type()
)
tmnxDiamPeerStatsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsDirection.setStatus("current")


class _TmnxDiamPeerStatsMessageType_Type(Integer32):
    """Custom type tmnxDiamPeerStatsMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("request", 1),
          ("answer", 2))
    )


_TmnxDiamPeerStatsMessageType_Type.__name__ = "Integer32"
_TmnxDiamPeerStatsMessageType_Object = MibTableColumn
tmnxDiamPeerStatsMessageType = _TmnxDiamPeerStatsMessageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 6),
    _TmnxDiamPeerStatsMessageType_Type()
)
tmnxDiamPeerStatsMessageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsMessageType.setStatus("current")
_TmnxDiamPeerStatsLastClearedTime_Type = TimeStamp
_TmnxDiamPeerStatsLastClearedTime_Object = MibTableColumn
tmnxDiamPeerStatsLastClearedTime = _TmnxDiamPeerStatsLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 7),
    _TmnxDiamPeerStatsLastClearedTime_Type()
)
tmnxDiamPeerStatsLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsLastClearedTime.setStatus("current")
_TmnxDiamPeerStatsTotalMessages_Type = Counter32
_TmnxDiamPeerStatsTotalMessages_Object = MibTableColumn
tmnxDiamPeerStatsTotalMessages = _TmnxDiamPeerStatsTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 10),
    _TmnxDiamPeerStatsTotalMessages_Type()
)
tmnxDiamPeerStatsTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsTotalMessages.setStatus("current")
_TmnxDiamPeerStatsFailedMessages_Type = Counter32
_TmnxDiamPeerStatsFailedMessages_Object = MibTableColumn
tmnxDiamPeerStatsFailedMessages = _TmnxDiamPeerStatsFailedMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 11),
    _TmnxDiamPeerStatsFailedMessages_Type()
)
tmnxDiamPeerStatsFailedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsFailedMessages.setStatus("current")
_TmnxDiamPeerStatsBaseCe_Type = Counter32
_TmnxDiamPeerStatsBaseCe_Object = MibTableColumn
tmnxDiamPeerStatsBaseCe = _TmnxDiamPeerStatsBaseCe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 20),
    _TmnxDiamPeerStatsBaseCe_Type()
)
tmnxDiamPeerStatsBaseCe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsBaseCe.setStatus("current")
_TmnxDiamPeerStatsBaseDp_Type = Counter32
_TmnxDiamPeerStatsBaseDp_Object = MibTableColumn
tmnxDiamPeerStatsBaseDp = _TmnxDiamPeerStatsBaseDp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 21),
    _TmnxDiamPeerStatsBaseDp_Type()
)
tmnxDiamPeerStatsBaseDp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsBaseDp.setStatus("current")
_TmnxDiamPeerStatsBaseDw_Type = Counter32
_TmnxDiamPeerStatsBaseDw_Object = MibTableColumn
tmnxDiamPeerStatsBaseDw = _TmnxDiamPeerStatsBaseDw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 22),
    _TmnxDiamPeerStatsBaseDw_Type()
)
tmnxDiamPeerStatsBaseDw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsBaseDw.setStatus("current")
_TmnxDiamPeerStatsNqAa_Type = Counter32
_TmnxDiamPeerStatsNqAa_Object = MibTableColumn
tmnxDiamPeerStatsNqAa = _TmnxDiamPeerStatsNqAa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 30),
    _TmnxDiamPeerStatsNqAa_Type()
)
tmnxDiamPeerStatsNqAa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsNqAa.setStatus("current")
_TmnxDiamPeerStatsGyCcI_Type = Counter32
_TmnxDiamPeerStatsGyCcI_Object = MibTableColumn
tmnxDiamPeerStatsGyCcI = _TmnxDiamPeerStatsGyCcI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 40),
    _TmnxDiamPeerStatsGyCcI_Type()
)
tmnxDiamPeerStatsGyCcI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsGyCcI.setStatus("current")
_TmnxDiamPeerStatsGyCcU_Type = Counter32
_TmnxDiamPeerStatsGyCcU_Object = MibTableColumn
tmnxDiamPeerStatsGyCcU = _TmnxDiamPeerStatsGyCcU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 41),
    _TmnxDiamPeerStatsGyCcU_Type()
)
tmnxDiamPeerStatsGyCcU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsGyCcU.setStatus("current")
_TmnxDiamPeerStatsGyCcT_Type = Counter32
_TmnxDiamPeerStatsGyCcT_Object = MibTableColumn
tmnxDiamPeerStatsGyCcT = _TmnxDiamPeerStatsGyCcT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 42),
    _TmnxDiamPeerStatsGyCcT_Type()
)
tmnxDiamPeerStatsGyCcT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsGyCcT.setStatus("current")
_TmnxDiamPeerStatsGyRa_Type = Counter32
_TmnxDiamPeerStatsGyRa_Object = MibTableColumn
tmnxDiamPeerStatsGyRa = _TmnxDiamPeerStatsGyRa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 43),
    _TmnxDiamPeerStatsGyRa_Type()
)
tmnxDiamPeerStatsGyRa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsGyRa.setStatus("current")
_TmnxDiamPeerStatsGyAs_Type = Counter32
_TmnxDiamPeerStatsGyAs_Object = MibTableColumn
tmnxDiamPeerStatsGyAs = _TmnxDiamPeerStatsGyAs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 44),
    _TmnxDiamPeerStatsGyAs_Type()
)
tmnxDiamPeerStatsGyAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsGyAs.setStatus("current")
_TmnxDiamPeerStatsGxCcI_Type = Counter32
_TmnxDiamPeerStatsGxCcI_Object = MibTableColumn
tmnxDiamPeerStatsGxCcI = _TmnxDiamPeerStatsGxCcI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 50),
    _TmnxDiamPeerStatsGxCcI_Type()
)
tmnxDiamPeerStatsGxCcI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsGxCcI.setStatus("current")
_TmnxDiamPeerStatsGxCcU_Type = Counter32
_TmnxDiamPeerStatsGxCcU_Object = MibTableColumn
tmnxDiamPeerStatsGxCcU = _TmnxDiamPeerStatsGxCcU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 51),
    _TmnxDiamPeerStatsGxCcU_Type()
)
tmnxDiamPeerStatsGxCcU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsGxCcU.setStatus("current")
_TmnxDiamPeerStatsGxCcT_Type = Counter32
_TmnxDiamPeerStatsGxCcT_Object = MibTableColumn
tmnxDiamPeerStatsGxCcT = _TmnxDiamPeerStatsGxCcT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 52),
    _TmnxDiamPeerStatsGxCcT_Type()
)
tmnxDiamPeerStatsGxCcT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsGxCcT.setStatus("current")
_TmnxDiamPeerStatsGxRa_Type = Counter32
_TmnxDiamPeerStatsGxRa_Object = MibTableColumn
tmnxDiamPeerStatsGxRa = _TmnxDiamPeerStatsGxRa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 53),
    _TmnxDiamPeerStatsGxRa_Type()
)
tmnxDiamPeerStatsGxRa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsGxRa.setStatus("current")
_TmnxDiamPeerStatsGxAs_Type = Counter32
_TmnxDiamPeerStatsGxAs_Object = MibTableColumn
tmnxDiamPeerStatsGxAs = _TmnxDiamPeerStatsGxAs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 13, 1, 54),
    _TmnxDiamPeerStatsGxAs_Type()
)
tmnxDiamPeerStatsGxAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamPeerStatsGxAs.setStatus("current")
_TmnxDiamGyEfhTable_Object = MibTable
tmnxDiamGyEfhTable = _TmnxDiamGyEfhTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 14)
)
if mibBuilder.loadTexts:
    tmnxDiamGyEfhTable.setStatus("current")
_TmnxDiamGyEfhEntry_Object = MibTableRow
tmnxDiamGyEfhEntry = _TmnxDiamGyEfhEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 14, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamGyEfhEntry.setStatus("current")


class _TmnxDiamGyEfhAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxDiamGyEfhAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxDiamGyEfhAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxDiamGyEfhAdminState_Object = MibTableColumn
tmnxDiamGyEfhAdminState = _TmnxDiamGyEfhAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 14, 1, 1),
    _TmnxDiamGyEfhAdminState_Type()
)
tmnxDiamGyEfhAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGyEfhAdminState.setStatus("current")


class _TmnxDiamGyEfhNewSessionId_Type(TruthValue):
    """Custom type tmnxDiamGyEfhNewSessionId based on TruthValue"""
    defaultValue = 2


_TmnxDiamGyEfhNewSessionId_Type.__name__ = "TruthValue"
_TmnxDiamGyEfhNewSessionId_Object = MibTableColumn
tmnxDiamGyEfhNewSessionId = _TmnxDiamGyEfhNewSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 14, 1, 2),
    _TmnxDiamGyEfhNewSessionId_Type()
)
tmnxDiamGyEfhNewSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGyEfhNewSessionId.setStatus("current")


class _TmnxDiamGyEfhInterimCreditReport_Type(TruthValue):
    """Custom type tmnxDiamGyEfhInterimCreditReport based on TruthValue"""
    defaultValue = 2


_TmnxDiamGyEfhInterimCreditReport_Type.__name__ = "TruthValue"
_TmnxDiamGyEfhInterimCreditReport_Object = MibTableColumn
tmnxDiamGyEfhInterimCreditReport = _TmnxDiamGyEfhInterimCreditReport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 14, 1, 3),
    _TmnxDiamGyEfhInterimCreditReport_Type()
)
tmnxDiamGyEfhInterimCreditReport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGyEfhInterimCreditReport.setStatus("current")


class _TmnxDiamGyEfhInterimCreditVolume_Type(Unsigned32):
    """Custom type tmnxDiamGyEfhInterimCreditVolume based on Unsigned32"""
    defaultValue = 500


_TmnxDiamGyEfhInterimCreditVolume_Type.__name__ = "Unsigned32"
_TmnxDiamGyEfhInterimCreditVolume_Object = MibTableColumn
tmnxDiamGyEfhInterimCreditVolume = _TmnxDiamGyEfhInterimCreditVolume_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 14, 1, 4),
    _TmnxDiamGyEfhInterimCreditVolume_Type()
)
tmnxDiamGyEfhInterimCreditVolume.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGyEfhInterimCreditVolume.setStatus("current")


class _TmnxDiamGyEfhInterimCVolumeUnit_Type(TmnxSubCreditVolumeUnit):
    """Custom type tmnxDiamGyEfhInterimCVolumeUnit based on TmnxSubCreditVolumeUnit"""
    defaultValue = 2


_TmnxDiamGyEfhInterimCVolumeUnit_Type.__name__ = "TmnxSubCreditVolumeUnit"
_TmnxDiamGyEfhInterimCVolumeUnit_Object = MibTableColumn
tmnxDiamGyEfhInterimCVolumeUnit = _TmnxDiamGyEfhInterimCVolumeUnit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 14, 1, 5),
    _TmnxDiamGyEfhInterimCVolumeUnit_Type()
)
tmnxDiamGyEfhInterimCVolumeUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGyEfhInterimCVolumeUnit.setStatus("current")


class _TmnxDiamGyEfhInterimCredValTime_Type(Unsigned32):
    """Custom type tmnxDiamGyEfhInterimCredValTime based on Unsigned32"""
    defaultValue = 1800


_TmnxDiamGyEfhInterimCredValTime_Type.__name__ = "Unsigned32"
_TmnxDiamGyEfhInterimCredValTime_Object = MibTableColumn
tmnxDiamGyEfhInterimCredValTime = _TmnxDiamGyEfhInterimCredValTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 14, 1, 6),
    _TmnxDiamGyEfhInterimCredValTime_Type()
)
tmnxDiamGyEfhInterimCredValTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGyEfhInterimCredValTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamGyEfhInterimCredValTime.setUnits("seconds")


class _TmnxDiamGyEfhInterimCMaxAttempts_Type(Unsigned32):
    """Custom type tmnxDiamGyEfhInterimCMaxAttempts based on Unsigned32"""
    defaultValue = 10


_TmnxDiamGyEfhInterimCMaxAttempts_Type.__name__ = "Unsigned32"
_TmnxDiamGyEfhInterimCMaxAttempts_Object = MibTableColumn
tmnxDiamGyEfhInterimCMaxAttempts = _TmnxDiamGyEfhInterimCMaxAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 14, 1, 7),
    _TmnxDiamGyEfhInterimCMaxAttempts_Type()
)
tmnxDiamGyEfhInterimCMaxAttempts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGyEfhInterimCMaxAttempts.setStatus("current")
_TmnxDiamGyCcrtReplayTable_Object = MibTable
tmnxDiamGyCcrtReplayTable = _TmnxDiamGyCcrtReplayTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 15)
)
if mibBuilder.loadTexts:
    tmnxDiamGyCcrtReplayTable.setStatus("current")
_TmnxDiamGyCcrtReplayEntry_Object = MibTableRow
tmnxDiamGyCcrtReplayEntry = _TmnxDiamGyCcrtReplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 15, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamGyCcrtReplayEntry.setStatus("current")


class _TmnxDiamGyCcrtReplayAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxDiamGyCcrtReplayAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxDiamGyCcrtReplayAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxDiamGyCcrtReplayAdminState_Object = MibTableColumn
tmnxDiamGyCcrtReplayAdminState = _TmnxDiamGyCcrtReplayAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 15, 1, 1),
    _TmnxDiamGyCcrtReplayAdminState_Type()
)
tmnxDiamGyCcrtReplayAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGyCcrtReplayAdminState.setStatus("current")


class _TmnxDiamGyCcrtReplayInterval_Type(Unsigned32):
    """Custom type tmnxDiamGyCcrtReplayInterval based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_TmnxDiamGyCcrtReplayInterval_Type.__name__ = "Unsigned32"
_TmnxDiamGyCcrtReplayInterval_Object = MibTableColumn
tmnxDiamGyCcrtReplayInterval = _TmnxDiamGyCcrtReplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 15, 1, 2),
    _TmnxDiamGyCcrtReplayInterval_Type()
)
tmnxDiamGyCcrtReplayInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGyCcrtReplayInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamGyCcrtReplayInterval.setUnits("seconds")


class _TmnxDiamGyCcrtReplayMaxLifeTime_Type(Unsigned32):
    """Custom type tmnxDiamGyCcrtReplayMaxLifeTime based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_TmnxDiamGyCcrtReplayMaxLifeTime_Type.__name__ = "Unsigned32"
_TmnxDiamGyCcrtReplayMaxLifeTime_Object = MibTableColumn
tmnxDiamGyCcrtReplayMaxLifeTime = _TmnxDiamGyCcrtReplayMaxLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 15, 1, 3),
    _TmnxDiamGyCcrtReplayMaxLifeTime_Type()
)
tmnxDiamGyCcrtReplayMaxLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGyCcrtReplayMaxLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamGyCcrtReplayMaxLifeTime.setUnits("hours")
_TmnxDiamApGx3gppQosMapTable_Object = MibTable
tmnxDiamApGx3gppQosMapTable = _TmnxDiamApGx3gppQosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 16)
)
if mibBuilder.loadTexts:
    tmnxDiamApGx3gppQosMapTable.setStatus("current")
_TmnxDiamApGx3gppQosMapEntry_Object = MibTableRow
tmnxDiamApGx3gppQosMapEntry = _TmnxDiamApGx3gppQosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 16, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamApGx3gppQosMapEntry.setStatus("current")


class _TmnxDiamApGx3gqmAADlMappingType_Type(TmnxDiamApGx3gqmAADlMappingType):
    """Custom type tmnxDiamApGx3gqmAADlMappingType based on TmnxDiamApGx3gqmAADlMappingType"""
    defaultValue = 0


_TmnxDiamApGx3gqmAADlMappingType_Type.__name__ = "TmnxDiamApGx3gqmAADlMappingType"
_TmnxDiamApGx3gqmAADlMappingType_Object = MibTableColumn
tmnxDiamApGx3gqmAADlMappingType = _TmnxDiamApGx3gqmAADlMappingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 16, 1, 1),
    _TmnxDiamApGx3gqmAADlMappingType_Type()
)
tmnxDiamApGx3gqmAADlMappingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGx3gqmAADlMappingType.setStatus("current")


class _TmnxDiamApGx3gqmAADlArbiterName_Type(TNamedItemOrEmpty):
    """Custom type tmnxDiamApGx3gqmAADlArbiterName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDiamApGx3gqmAADlArbiterName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDiamApGx3gqmAADlArbiterName_Object = MibTableColumn
tmnxDiamApGx3gqmAADlArbiterName = _TmnxDiamApGx3gqmAADlArbiterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 16, 1, 2),
    _TmnxDiamApGx3gqmAADlArbiterName_Type()
)
tmnxDiamApGx3gqmAADlArbiterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGx3gqmAADlArbiterName.setStatus("current")


class _TmnxDiamApGx3gqmAADlSchedulrName_Type(TNamedItemOrEmpty):
    """Custom type tmnxDiamApGx3gqmAADlSchedulrName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDiamApGx3gqmAADlSchedulrName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDiamApGx3gqmAADlSchedulrName_Object = MibTableColumn
tmnxDiamApGx3gqmAADlSchedulrName = _TmnxDiamApGx3gqmAADlSchedulrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 16, 1, 3),
    _TmnxDiamApGx3gqmAADlSchedulrName_Type()
)
tmnxDiamApGx3gqmAADlSchedulrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGx3gqmAADlSchedulrName.setStatus("current")


class _TmnxDiamApGx3gqmAADlPolicerId_Type(TEgressPolicerIdOrNone):
    """Custom type tmnxDiamApGx3gqmAADlPolicerId based on TEgressPolicerIdOrNone"""
    defaultValue = 0


_TmnxDiamApGx3gqmAADlPolicerId_Type.__name__ = "TEgressPolicerIdOrNone"
_TmnxDiamApGx3gqmAADlPolicerId_Object = MibTableColumn
tmnxDiamApGx3gqmAADlPolicerId = _TmnxDiamApGx3gqmAADlPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 16, 1, 4),
    _TmnxDiamApGx3gqmAADlPolicerId_Type()
)
tmnxDiamApGx3gqmAADlPolicerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGx3gqmAADlPolicerId.setStatus("current")


class _TmnxDiamApGx3gqmAADlQueueId_Type(TEgressQueueId):
    """Custom type tmnxDiamApGx3gqmAADlQueueId based on TEgressQueueId"""
    defaultValue = 0


_TmnxDiamApGx3gqmAADlQueueId_Type.__name__ = "TEgressQueueId"
_TmnxDiamApGx3gqmAADlQueueId_Object = MibTableColumn
tmnxDiamApGx3gqmAADlQueueId = _TmnxDiamApGx3gqmAADlQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 16, 1, 5),
    _TmnxDiamApGx3gqmAADlQueueId_Type()
)
tmnxDiamApGx3gqmAADlQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGx3gqmAADlQueueId.setStatus("current")


class _TmnxDiamApGx3gqmAAUlMappingType_Type(TmnxDiamApGx3gqmAAUlMappingType):
    """Custom type tmnxDiamApGx3gqmAAUlMappingType based on TmnxDiamApGx3gqmAAUlMappingType"""
    defaultValue = 0


_TmnxDiamApGx3gqmAAUlMappingType_Type.__name__ = "TmnxDiamApGx3gqmAAUlMappingType"
_TmnxDiamApGx3gqmAAUlMappingType_Object = MibTableColumn
tmnxDiamApGx3gqmAAUlMappingType = _TmnxDiamApGx3gqmAAUlMappingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 16, 1, 6),
    _TmnxDiamApGx3gqmAAUlMappingType_Type()
)
tmnxDiamApGx3gqmAAUlMappingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGx3gqmAAUlMappingType.setStatus("current")


class _TmnxDiamApGx3gqmAAUlArbiterName_Type(TNamedItemOrEmpty):
    """Custom type tmnxDiamApGx3gqmAAUlArbiterName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDiamApGx3gqmAAUlArbiterName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDiamApGx3gqmAAUlArbiterName_Object = MibTableColumn
tmnxDiamApGx3gqmAAUlArbiterName = _TmnxDiamApGx3gqmAAUlArbiterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 16, 1, 7),
    _TmnxDiamApGx3gqmAAUlArbiterName_Type()
)
tmnxDiamApGx3gqmAAUlArbiterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGx3gqmAAUlArbiterName.setStatus("current")


class _TmnxDiamApGx3gqmAAUlSchedulrName_Type(TNamedItemOrEmpty):
    """Custom type tmnxDiamApGx3gqmAAUlSchedulrName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDiamApGx3gqmAAUlSchedulrName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDiamApGx3gqmAAUlSchedulrName_Object = MibTableColumn
tmnxDiamApGx3gqmAAUlSchedulrName = _TmnxDiamApGx3gqmAAUlSchedulrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 16, 1, 8),
    _TmnxDiamApGx3gqmAAUlSchedulrName_Type()
)
tmnxDiamApGx3gqmAAUlSchedulrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGx3gqmAAUlSchedulrName.setStatus("current")


class _TmnxDiamApGx3gqmAAUlPolicerId_Type(TIngressPolicerIdOrNone):
    """Custom type tmnxDiamApGx3gqmAAUlPolicerId based on TIngressPolicerIdOrNone"""
    defaultValue = 0


_TmnxDiamApGx3gqmAAUlPolicerId_Type.__name__ = "TIngressPolicerIdOrNone"
_TmnxDiamApGx3gqmAAUlPolicerId_Object = MibTableColumn
tmnxDiamApGx3gqmAAUlPolicerId = _TmnxDiamApGx3gqmAAUlPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 16, 1, 9),
    _TmnxDiamApGx3gqmAAUlPolicerId_Type()
)
tmnxDiamApGx3gqmAAUlPolicerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGx3gqmAAUlPolicerId.setStatus("current")


class _TmnxDiamApGx3gqmAAUlQueueId_Type(TIngressQueueId):
    """Custom type tmnxDiamApGx3gqmAAUlQueueId based on TIngressQueueId"""
    defaultValue = 0


_TmnxDiamApGx3gqmAAUlQueueId_Type.__name__ = "TIngressQueueId"
_TmnxDiamApGx3gqmAAUlQueueId_Object = MibTableColumn
tmnxDiamApGx3gqmAAUlQueueId = _TmnxDiamApGx3gqmAAUlQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 16, 1, 10),
    _TmnxDiamApGx3gqmAAUlQueueId_Type()
)
tmnxDiamApGx3gqmAAUlQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamApGx3gqmAAUlQueueId.setStatus("current")
_TmnxDiamApStatsTable_Object = MibTable
tmnxDiamApStatsTable = _TmnxDiamApStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17)
)
if mibBuilder.loadTexts:
    tmnxDiamApStatsTable.setStatus("current")
_TmnxDiamApStatsEntry_Object = MibTableRow
tmnxDiamApStatsEntry = _TmnxDiamApStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1)
)
tmnxDiamApStatsEntry.setIndexNames(
    (1, "TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyId"),
)
if mibBuilder.loadTexts:
    tmnxDiamApStatsEntry.setStatus("current")
_TmnxDiamApStatsLastCleared_Type = TimeStamp
_TmnxDiamApStatsLastCleared_Object = MibTableColumn
tmnxDiamApStatsLastCleared = _TmnxDiamApStatsLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 1),
    _TmnxDiamApStatsLastCleared_Type()
)
tmnxDiamApStatsLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsLastCleared.setStatus("current")
_TmnxDiamApStatsCciRequests_Type = Counter64
_TmnxDiamApStatsCciRequests_Object = MibTableColumn
tmnxDiamApStatsCciRequests = _TmnxDiamApStatsCciRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 2),
    _TmnxDiamApStatsCciRequests_Type()
)
tmnxDiamApStatsCciRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsCciRequests.setStatus("current")
_TmnxDiamApStatsCciAnswers_Type = Counter64
_TmnxDiamApStatsCciAnswers_Object = MibTableColumn
tmnxDiamApStatsCciAnswers = _TmnxDiamApStatsCciAnswers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 3),
    _TmnxDiamApStatsCciAnswers_Type()
)
tmnxDiamApStatsCciAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsCciAnswers.setStatus("current")
_TmnxDiamApStatsCcuRequests_Type = Counter64
_TmnxDiamApStatsCcuRequests_Object = MibTableColumn
tmnxDiamApStatsCcuRequests = _TmnxDiamApStatsCcuRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 4),
    _TmnxDiamApStatsCcuRequests_Type()
)
tmnxDiamApStatsCcuRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsCcuRequests.setStatus("current")
_TmnxDiamApStatsCcuAnswers_Type = Counter64
_TmnxDiamApStatsCcuAnswers_Object = MibTableColumn
tmnxDiamApStatsCcuAnswers = _TmnxDiamApStatsCcuAnswers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 5),
    _TmnxDiamApStatsCcuAnswers_Type()
)
tmnxDiamApStatsCcuAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsCcuAnswers.setStatus("current")
_TmnxDiamApStatsCctRequests_Type = Counter64
_TmnxDiamApStatsCctRequests_Object = MibTableColumn
tmnxDiamApStatsCctRequests = _TmnxDiamApStatsCctRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 6),
    _TmnxDiamApStatsCctRequests_Type()
)
tmnxDiamApStatsCctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsCctRequests.setStatus("current")
_TmnxDiamApStatsCctAnswers_Type = Counter64
_TmnxDiamApStatsCctAnswers_Object = MibTableColumn
tmnxDiamApStatsCctAnswers = _TmnxDiamApStatsCctAnswers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 7),
    _TmnxDiamApStatsCctAnswers_Type()
)
tmnxDiamApStatsCctAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsCctAnswers.setStatus("current")
_TmnxDiamApStatsAsrRx_Type = Counter64
_TmnxDiamApStatsAsrRx_Object = MibTableColumn
tmnxDiamApStatsAsrRx = _TmnxDiamApStatsAsrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 8),
    _TmnxDiamApStatsAsrRx_Type()
)
tmnxDiamApStatsAsrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsAsrRx.setStatus("current")
_TmnxDiamApStatsAsaTx_Type = Counter64
_TmnxDiamApStatsAsaTx_Object = MibTableColumn
tmnxDiamApStatsAsaTx = _TmnxDiamApStatsAsaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 9),
    _TmnxDiamApStatsAsaTx_Type()
)
tmnxDiamApStatsAsaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsAsaTx.setStatus("current")
_TmnxDiamApStatsRarRx_Type = Counter64
_TmnxDiamApStatsRarRx_Object = MibTableColumn
tmnxDiamApStatsRarRx = _TmnxDiamApStatsRarRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 10),
    _TmnxDiamApStatsRarRx_Type()
)
tmnxDiamApStatsRarRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsRarRx.setStatus("current")
_TmnxDiamApStatsRaaTx_Type = Counter64
_TmnxDiamApStatsRaaTx_Object = MibTableColumn
tmnxDiamApStatsRaaTx = _TmnxDiamApStatsRaaTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 11),
    _TmnxDiamApStatsRaaTx_Type()
)
tmnxDiamApStatsRaaTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsRaaTx.setStatus("current")
_TmnxDiamApStatsAarTx_Type = Counter64
_TmnxDiamApStatsAarTx_Object = MibTableColumn
tmnxDiamApStatsAarTx = _TmnxDiamApStatsAarTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 12),
    _TmnxDiamApStatsAarTx_Type()
)
tmnxDiamApStatsAarTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsAarTx.setStatus("current")
_TmnxDiamApStatsAaaRx_Type = Counter64
_TmnxDiamApStatsAaaRx_Object = MibTableColumn
tmnxDiamApStatsAaaRx = _TmnxDiamApStatsAaaRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 13),
    _TmnxDiamApStatsAaaRx_Type()
)
tmnxDiamApStatsAaaRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsAaaRx.setStatus("current")
_TmnxDiamApStatsReqFailed_Type = Counter64
_TmnxDiamApStatsReqFailed_Object = MibTableColumn
tmnxDiamApStatsReqFailed = _TmnxDiamApStatsReqFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 14),
    _TmnxDiamApStatsReqFailed_Type()
)
tmnxDiamApStatsReqFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsReqFailed.setStatus("current")
_TmnxDiamApStatsReqRetransmits_Type = Counter64
_TmnxDiamApStatsReqRetransmits_Object = MibTableColumn
tmnxDiamApStatsReqRetransmits = _TmnxDiamApStatsReqRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 15),
    _TmnxDiamApStatsReqRetransmits_Type()
)
tmnxDiamApStatsReqRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsReqRetransmits.setStatus("current")
_TmnxDiamApStatsResultInfoTx_Type = Counter64
_TmnxDiamApStatsResultInfoTx_Object = MibTableColumn
tmnxDiamApStatsResultInfoTx = _TmnxDiamApStatsResultInfoTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 16),
    _TmnxDiamApStatsResultInfoTx_Type()
)
tmnxDiamApStatsResultInfoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsResultInfoTx.setStatus("current")
_TmnxDiamApStatsResultInfoRx_Type = Counter64
_TmnxDiamApStatsResultInfoRx_Object = MibTableColumn
tmnxDiamApStatsResultInfoRx = _TmnxDiamApStatsResultInfoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 17),
    _TmnxDiamApStatsResultInfoRx_Type()
)
tmnxDiamApStatsResultInfoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsResultInfoRx.setStatus("current")
_TmnxDiamApStatsResultSuccessTx_Type = Counter64
_TmnxDiamApStatsResultSuccessTx_Object = MibTableColumn
tmnxDiamApStatsResultSuccessTx = _TmnxDiamApStatsResultSuccessTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 18),
    _TmnxDiamApStatsResultSuccessTx_Type()
)
tmnxDiamApStatsResultSuccessTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsResultSuccessTx.setStatus("current")
_TmnxDiamApStatsResultSuccessRx_Type = Counter64
_TmnxDiamApStatsResultSuccessRx_Object = MibTableColumn
tmnxDiamApStatsResultSuccessRx = _TmnxDiamApStatsResultSuccessRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 19),
    _TmnxDiamApStatsResultSuccessRx_Type()
)
tmnxDiamApStatsResultSuccessRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsResultSuccessRx.setStatus("current")
_TmnxDiamApStatsResultProtErrTx_Type = Counter64
_TmnxDiamApStatsResultProtErrTx_Object = MibTableColumn
tmnxDiamApStatsResultProtErrTx = _TmnxDiamApStatsResultProtErrTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 20),
    _TmnxDiamApStatsResultProtErrTx_Type()
)
tmnxDiamApStatsResultProtErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsResultProtErrTx.setStatus("current")
_TmnxDiamApStatsResultProtErrRx_Type = Counter64
_TmnxDiamApStatsResultProtErrRx_Object = MibTableColumn
tmnxDiamApStatsResultProtErrRx = _TmnxDiamApStatsResultProtErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 21),
    _TmnxDiamApStatsResultProtErrRx_Type()
)
tmnxDiamApStatsResultProtErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsResultProtErrRx.setStatus("current")
_TmnxDiamApStatsResultTransFailTx_Type = Counter64
_TmnxDiamApStatsResultTransFailTx_Object = MibTableColumn
tmnxDiamApStatsResultTransFailTx = _TmnxDiamApStatsResultTransFailTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 22),
    _TmnxDiamApStatsResultTransFailTx_Type()
)
tmnxDiamApStatsResultTransFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsResultTransFailTx.setStatus("current")
_TmnxDiamApStatsResultTransFailRx_Type = Counter64
_TmnxDiamApStatsResultTransFailRx_Object = MibTableColumn
tmnxDiamApStatsResultTransFailRx = _TmnxDiamApStatsResultTransFailRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 23),
    _TmnxDiamApStatsResultTransFailRx_Type()
)
tmnxDiamApStatsResultTransFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsResultTransFailRx.setStatus("current")
_TmnxDiamApStatsResultPermFailTx_Type = Counter64
_TmnxDiamApStatsResultPermFailTx_Object = MibTableColumn
tmnxDiamApStatsResultPermFailTx = _TmnxDiamApStatsResultPermFailTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 24),
    _TmnxDiamApStatsResultPermFailTx_Type()
)
tmnxDiamApStatsResultPermFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsResultPermFailTx.setStatus("current")
_TmnxDiamApStatsResultPermFailRx_Type = Counter64
_TmnxDiamApStatsResultPermFailRx_Object = MibTableColumn
tmnxDiamApStatsResultPermFailRx = _TmnxDiamApStatsResultPermFailRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 17, 1, 25),
    _TmnxDiamApStatsResultPermFailRx_Type()
)
tmnxDiamApStatsResultPermFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamApStatsResultPermFailRx.setStatus("current")
_TmnxDiamCcrtRStatTable_Object = MibTable
tmnxDiamCcrtRStatTable = _TmnxDiamCcrtRStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 18)
)
if mibBuilder.loadTexts:
    tmnxDiamCcrtRStatTable.setStatus("current")
_TmnxDiamCcrtRStatEntry_Object = MibTableRow
tmnxDiamCcrtRStatEntry = _TmnxDiamCcrtRStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 18, 1)
)
tmnxDiamCcrtRStatEntry.setIndexNames(
    (1, "TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyId"),
)
if mibBuilder.loadTexts:
    tmnxDiamCcrtRStatEntry.setStatus("current")
_TmnxDiamCcrtRStatLastCleared_Type = TimeStamp
_TmnxDiamCcrtRStatLastCleared_Object = MibTableColumn
tmnxDiamCcrtRStatLastCleared = _TmnxDiamCcrtRStatLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 18, 1, 1),
    _TmnxDiamCcrtRStatLastCleared_Type()
)
tmnxDiamCcrtRStatLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamCcrtRStatLastCleared.setStatus("current")
_TmnxDiamCcrtRStatSessions_Type = CounterBasedGauge64
_TmnxDiamCcrtRStatSessions_Object = MibTableColumn
tmnxDiamCcrtRStatSessions = _TmnxDiamCcrtRStatSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 18, 1, 2),
    _TmnxDiamCcrtRStatSessions_Type()
)
tmnxDiamCcrtRStatSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamCcrtRStatSessions.setStatus("current")
_TmnxDiamCcrtRStatDroppedMlt_Type = Counter64
_TmnxDiamCcrtRStatDroppedMlt_Object = MibTableColumn
tmnxDiamCcrtRStatDroppedMlt = _TmnxDiamCcrtRStatDroppedMlt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 18, 1, 3),
    _TmnxDiamCcrtRStatDroppedMlt_Type()
)
tmnxDiamCcrtRStatDroppedMlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamCcrtRStatDroppedMlt.setStatus("current")
_TmnxDiamCcrtRStatDroppedNew_Type = Counter64
_TmnxDiamCcrtRStatDroppedNew_Object = MibTableColumn
tmnxDiamCcrtRStatDroppedNew = _TmnxDiamCcrtRStatDroppedNew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 18, 1, 4),
    _TmnxDiamCcrtRStatDroppedNew_Type()
)
tmnxDiamCcrtRStatDroppedNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamCcrtRStatDroppedNew.setStatus("current")
_TmnxDiamCcrtRStatDroppedCleared_Type = Counter64
_TmnxDiamCcrtRStatDroppedCleared_Object = MibTableColumn
tmnxDiamCcrtRStatDroppedCleared = _TmnxDiamCcrtRStatDroppedCleared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 18, 1, 5),
    _TmnxDiamCcrtRStatDroppedCleared_Type()
)
tmnxDiamCcrtRStatDroppedCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamCcrtRStatDroppedCleared.setStatus("current")
_TmnxDiamCcrtRStatTerminatedCcat_Type = Counter64
_TmnxDiamCcrtRStatTerminatedCcat_Object = MibTableColumn
tmnxDiamCcrtRStatTerminatedCcat = _TmnxDiamCcrtRStatTerminatedCcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 18, 1, 6),
    _TmnxDiamCcrtRStatTerminatedCcat_Type()
)
tmnxDiamCcrtRStatTerminatedCcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamCcrtRStatTerminatedCcat.setStatus("current")
_TmnxDiamGxCcrtReplayTable_Object = MibTable
tmnxDiamGxCcrtReplayTable = _TmnxDiamGxCcrtReplayTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 19)
)
if mibBuilder.loadTexts:
    tmnxDiamGxCcrtReplayTable.setStatus("current")
_TmnxDiamGxCcrtReplayEntry_Object = MibTableRow
tmnxDiamGxCcrtReplayEntry = _TmnxDiamGxCcrtReplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 19, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamGxCcrtReplayEntry.setStatus("current")


class _TmnxDiamGxCcrtReplayAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxDiamGxCcrtReplayAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxDiamGxCcrtReplayAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxDiamGxCcrtReplayAdminState_Object = MibTableColumn
tmnxDiamGxCcrtReplayAdminState = _TmnxDiamGxCcrtReplayAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 19, 1, 1),
    _TmnxDiamGxCcrtReplayAdminState_Type()
)
tmnxDiamGxCcrtReplayAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGxCcrtReplayAdminState.setStatus("current")


class _TmnxDiamGxCcrtReplayInterval_Type(Unsigned32):
    """Custom type tmnxDiamGxCcrtReplayInterval based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_TmnxDiamGxCcrtReplayInterval_Type.__name__ = "Unsigned32"
_TmnxDiamGxCcrtReplayInterval_Object = MibTableColumn
tmnxDiamGxCcrtReplayInterval = _TmnxDiamGxCcrtReplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 19, 1, 2),
    _TmnxDiamGxCcrtReplayInterval_Type()
)
tmnxDiamGxCcrtReplayInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGxCcrtReplayInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamGxCcrtReplayInterval.setUnits("seconds")


class _TmnxDiamGxCcrtReplayMaxLifeTime_Type(Unsigned32):
    """Custom type tmnxDiamGxCcrtReplayMaxLifeTime based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_TmnxDiamGxCcrtReplayMaxLifeTime_Type.__name__ = "Unsigned32"
_TmnxDiamGxCcrtReplayMaxLifeTime_Object = MibTableColumn
tmnxDiamGxCcrtReplayMaxLifeTime = _TmnxDiamGxCcrtReplayMaxLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 3, 19, 1, 3),
    _TmnxDiamGxCcrtReplayMaxLifeTime_Type()
)
tmnxDiamGxCcrtReplayMaxLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDiamGxCcrtReplayMaxLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamGxCcrtReplayMaxLifeTime.setUnits("hours")
_TmnxDiameterSessionObjects_ObjectIdentity = ObjectIdentity
tmnxDiameterSessionObjects = _TmnxDiameterSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 4)
)
_TmnxDiamSeGxCcrtReplayTable_Object = MibTable
tmnxDiamSeGxCcrtReplayTable = _TmnxDiamSeGxCcrtReplayTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxDiamSeGxCcrtReplayTable.setStatus("current")
_TmnxDiamSeGxCcrtReplayEntry_Object = MibTableRow
tmnxDiamSeGxCcrtReplayEntry = _TmnxDiamSeGxCcrtReplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 4, 1, 1)
)
tmnxDiamSeGxCcrtReplayEntry.setIndexNames(
    (0, "TIMETRA-DIAMETER-MIB", "tmnxDiamSeGxCcrtReplayIndex"),
)
if mibBuilder.loadTexts:
    tmnxDiamSeGxCcrtReplayEntry.setStatus("current")
_TmnxDiamSeGxCcrtReplayIndex_Type = Unsigned32
_TmnxDiamSeGxCcrtReplayIndex_Object = MibTableColumn
tmnxDiamSeGxCcrtReplayIndex = _TmnxDiamSeGxCcrtReplayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 4, 1, 1, 1),
    _TmnxDiamSeGxCcrtReplayIndex_Type()
)
tmnxDiamSeGxCcrtReplayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDiamSeGxCcrtReplayIndex.setStatus("current")
_TmnxDiamSeGxCcrtReplaySessionId_Type = TmnxDiamSessionId
_TmnxDiamSeGxCcrtReplaySessionId_Object = MibTableColumn
tmnxDiamSeGxCcrtReplaySessionId = _TmnxDiamSeGxCcrtReplaySessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 4, 1, 1, 2),
    _TmnxDiamSeGxCcrtReplaySessionId_Type()
)
tmnxDiamSeGxCcrtReplaySessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamSeGxCcrtReplaySessionId.setStatus("current")
_TmnxDiamSeGxCcrtReplayAppPolicy_Type = TNamedItem
_TmnxDiamSeGxCcrtReplayAppPolicy_Object = MibTableColumn
tmnxDiamSeGxCcrtReplayAppPolicy = _TmnxDiamSeGxCcrtReplayAppPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 4, 1, 1, 3),
    _TmnxDiamSeGxCcrtReplayAppPolicy_Type()
)
tmnxDiamSeGxCcrtReplayAppPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamSeGxCcrtReplayAppPolicy.setStatus("current")
_TmnxDiamSeGxCcrtReplayExpiryTime_Type = Unsigned32
_TmnxDiamSeGxCcrtReplayExpiryTime_Object = MibTableColumn
tmnxDiamSeGxCcrtReplayExpiryTime = _TmnxDiamSeGxCcrtReplayExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 4, 1, 1, 4),
    _TmnxDiamSeGxCcrtReplayExpiryTime_Type()
)
tmnxDiamSeGxCcrtReplayExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiamSeGxCcrtReplayExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDiamSeGxCcrtReplayExpiryTime.setUnits("seconds")
_TmnxDiameterNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxDiameterNotificationObjs = _TmnxDiameterNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100)
)
_TmnxDiamAppPlcyName_Type = TNamedItem
_TmnxDiamAppPlcyName_Object = MibScalar
tmnxDiamAppPlcyName = _TmnxDiamAppPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 1),
    _TmnxDiamAppPlcyName_Type()
)
tmnxDiamAppPlcyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppPlcyName.setStatus("current")
_TmnxDiamAppPeerName_Type = TNamedItem
_TmnxDiamAppPeerName_Object = MibScalar
tmnxDiamAppPeerName = _TmnxDiamAppPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 2),
    _TmnxDiamAppPeerName_Type()
)
tmnxDiamAppPeerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppPeerName.setStatus("current")
_TmnxDiamAppTrapDescription_Type = TItemDescription
_TmnxDiamAppTrapDescription_Object = MibScalar
tmnxDiamAppTrapDescription = _TmnxDiamAppTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 3),
    _TmnxDiamAppTrapDescription_Type()
)
tmnxDiamAppTrapDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppTrapDescription.setStatus("current")
_TmnxDiamAppSessionId_Type = TmnxDiamSessionId
_TmnxDiamAppSessionId_Object = MibScalar
tmnxDiamAppSessionId = _TmnxDiamAppSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 4),
    _TmnxDiamAppSessionId_Type()
)
tmnxDiamAppSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppSessionId.setStatus("current")


class _TmnxDiamAppSubscrId_Type(DisplayString):
    """Custom type tmnxDiamAppSubscrId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxDiamAppSubscrId_Type.__name__ = "DisplayString"
_TmnxDiamAppSubscrId_Object = MibScalar
tmnxDiamAppSubscrId = _TmnxDiamAppSubscrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 5),
    _TmnxDiamAppSubscrId_Type()
)
tmnxDiamAppSubscrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppSubscrId.setStatus("current")


class _TmnxDiamAppSapId_Type(DisplayString):
    """Custom type tmnxDiamAppSapId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxDiamAppSapId_Type.__name__ = "DisplayString"
_TmnxDiamAppSapId_Object = MibScalar
tmnxDiamAppSapId = _TmnxDiamAppSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 6),
    _TmnxDiamAppSapId_Type()
)
tmnxDiamAppSapId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppSapId.setStatus("current")
_TmnxDiamAppSLAProfName_Type = TNamedItem
_TmnxDiamAppSLAProfName_Object = MibScalar
tmnxDiamAppSLAProfName = _TmnxDiamAppSLAProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 7),
    _TmnxDiamAppSLAProfName_Type()
)
tmnxDiamAppSLAProfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamAppSLAProfName.setStatus("current")


class _TmnxDiamNotifyEventId_Type(Integer32):
    """Custom type tmnxDiamNotifyEventId based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknownApplicationPolicy", 1),
          ("unknownPeerPolicy", 2),
          ("noOperationalPeers", 3),
          ("txError", 4),
          ("rxError", 5),
          ("txTimeout", 6),
          ("txTimeoutPendingQ", 7),
          ("txRetriesExceeded", 8),
          ("ccrtReplayLifetimeExceeded", 9),
          ("ccrtReplayTooManySessions", 10))
    )


_TmnxDiamNotifyEventId_Type.__name__ = "Integer32"
_TmnxDiamNotifyEventId_Object = MibScalar
tmnxDiamNotifyEventId = _TmnxDiamNotifyEventId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 8),
    _TmnxDiamNotifyEventId_Type()
)
tmnxDiamNotifyEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamNotifyEventId.setStatus("current")
_TmnxDiamNotifySpiShareType_Type = TmnxSubHostGrouping
_TmnxDiamNotifySpiShareType_Object = MibScalar
tmnxDiamNotifySpiShareType = _TmnxDiamNotifySpiShareType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 9),
    _TmnxDiamNotifySpiShareType_Type()
)
tmnxDiamNotifySpiShareType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamNotifySpiShareType.setStatus("current")
_TmnxDiamNotifySpiShareId_Type = Unsigned32
_TmnxDiamNotifySpiShareId_Object = MibScalar
tmnxDiamNotifySpiShareId = _TmnxDiamNotifySpiShareId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 58, 100, 10),
    _TmnxDiamNotifySpiShareId_Type()
)
tmnxDiamNotifySpiShareId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDiamNotifySpiShareId.setStatus("current")
_TmnxDiameterNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxDiameterNotifyPrefix = _TmnxDiameterNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58)
)
_TmnxDiameterNotifications_ObjectIdentity = ObjectIdentity
tmnxDiameterNotifications = _TmnxDiameterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0)
)
tmnxDiameterPlcyPeerEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiamPlcyPeerInfoEntry")
)
tmnxDiamPlcyPeerInfoEntry.setIndexNames(*tmnxDiameterPlcyPeerEntry.getIndexNames())
tmnxDiameterPlcyPeerEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiamPlcyPeerStatsEntry")
)
tmnxDiamPlcyPeerStatsEntry.setIndexNames(*tmnxDiameterPlcyPeerEntry.getIndexNames())
tmnxDiameterNodePeerEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiamNdPeerStatEntry")
)
tmnxDiamNdPeerStatEntry.setIndexNames(*tmnxDiameterNodePeerEntry.getIndexNames())
tmnxDiameterNodePeerEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiamNdPeerStatsEntry")
)
tmnxDiamNdPeerStatsEntry.setIndexNames(*tmnxDiameterNodePeerEntry.getIndexNames())
tmnxDiameterNodeEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiamNdStatEntry")
)
tmnxDiamNdStatEntry.setIndexNames(*tmnxDiameterNodeEntry.getIndexNames())
tmnxDiameterPlcyEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiameterPlcyDccaEntry")
)
tmnxDiameterPlcyDccaEntry.setIndexNames(*tmnxDiameterPlcyEntry.getIndexNames())
tmnxDiamPpPrxClientEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiamPrxClStEntry")
)
tmnxDiamPrxClStEntry.setIndexNames(*tmnxDiamPpPrxClientEntry.getIndexNames())
tmnxDiamApGyEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiamGyEfhEntry")
)
tmnxDiamGyEfhEntry.setIndexNames(*tmnxDiamApGyEntry.getIndexNames())
tmnxDiamApGyEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiamGyCcrtReplayEntry")
)
tmnxDiamGyCcrtReplayEntry.setIndexNames(*tmnxDiamApGyEntry.getIndexNames())
tmnxDiamApGxEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiamApGx3gppQosMapEntry")
)
tmnxDiamApGx3gppQosMapEntry.setIndexNames(*tmnxDiamApGxEntry.getIndexNames())
tmnxDiamApGxEntry.registerAugmentions(
    ("TIMETRA-DIAMETER-MIB",
     "tmnxDiamGxCcrtReplayEntry")
)
tmnxDiamGxCcrtReplayEntry.setIndexNames(*tmnxDiamApGxEntry.getIndexNames())

# Managed Objects groups

tmnxDiameterBaseV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 1)
)
tmnxDiameterBaseV7v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterPlcyTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDescription"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyOriginHost"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyOriginRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyRouter"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcySourceAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcySourceAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyWatchdogTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyConnectionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyTransactionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAdminState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransportProt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransportPort"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerDestHost"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerDestRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerWatchdogTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerConnectionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransactTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerPreference"))
)
if mibBuilder.loadTexts:
    tmnxDiameterBaseV7v0Group.setStatus("obsolete")

tmnxDiameterDccaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 2)
)
tmnxDiameterDccaGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaFailover"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaFailureHndlng"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaTxTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpServCntxtId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpCldStationId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpRadiusUsrNme"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpSubIdOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpSubIdType"))
)
if mibBuilder.loadTexts:
    tmnxDiameterDccaGroup.setStatus("obsolete")

tmnxDiameterBaseV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 3)
)
tmnxDiameterBaseV8v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterPlcyTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDescription"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyOriginHost"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyOriginRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyRouter"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcySourceAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcySourceAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyWatchdogTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyConnectionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyTransactionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAdminState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransportProt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransportPort"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerDestHost"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerDestRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerWatchdogTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerConnectionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransactTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerPreference"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerPsmState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerConnectionSuspended"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerCooldownSeqStage"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerOrder"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerPrimarySecondary"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerTcTimerTimeLeft"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerTtTimerTimeLeft"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerTwTimerTimeLeft"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerWatchdogAlgActive"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerWatchdogAnswPending"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerCooldownSeqPending"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerCooldownSeqActive"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerPeerRemovalPending"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsLastClearTime"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiTcpSendFailed"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiDiamRxDropCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiDiamTxReqs"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiDiamRxResps"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiPendMsgsPMQ"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiReqTimeoutsPMQ"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStSiTcpSendFailed"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStSiDiamRxDropCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStSiDiamRxReqs"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStSiDiamTxResps"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStErrHdlDiamTxErrCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStErrHdlDiamRxErrCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcrInitialTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcaInitialRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcrUpdateTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcaUpdateRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcrTerminateTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcaTerminateRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCerTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCeaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStWdrTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStWdaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStWdrRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStWdaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStAsrRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStAsaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStRarRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStRaaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStDprTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStDpaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStDprRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStDpaTx"))
)
if mibBuilder.loadTexts:
    tmnxDiameterBaseV8v0Group.setStatus("obsolete")

tmnxDiameterV8v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 5)
)
tmnxDiameterV8v0NotifyObjsGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPeerName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV8v0NotifyObjsGroup.setStatus("obsolete")

tmnxDiameterDccaGxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 6)
)
tmnxDiameterDccaGxGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasP"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPPfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPPfixStr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPSfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaApplicationType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpImsiOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaMaxPendingReq"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaTxRetryLimit"))
)
if mibBuilder.loadTexts:
    tmnxDiameterDccaGxGroup.setStatus("obsolete")

tmnxDiameterDccaV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 7)
)
tmnxDiameterDccaV10v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyVendorSupport"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaOutOfCreditRep"))
)
if mibBuilder.loadTexts:
    tmnxDiameterDccaV10v0Group.setStatus("obsolete")

tmnxDiameterV10v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 9)
)
tmnxDiameterV10v0NotifyObjsGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPeerName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSessionId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSubscrId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSapId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSLAProfName"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV10v0NotifyObjsGroup.setStatus("obsolete")

tmnxDiameterV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 10)
)
tmnxDiameterV12v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyVendorSupport"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyApplications"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyTableLastCh"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyFailover"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyFailureHndlng"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyPeerPlcy"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyApplication"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyTxTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyDescription"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyTableLastCh"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyAvpServCntxtId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyAvpCldStationId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyAvpRadiusUsrNme"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyAvpImsiOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyOutOfCreditRep"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyVendorSupport"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGySubIdOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGySubIdType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxTableLastCh"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvp"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpClngStationIdType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpNasPortBitspec"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpNasPortIdPfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpNasPortIdPfixStr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpNasPortIdSfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpNasPortTypeValue"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpUeInfoType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxSubIdOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxSubIdType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxMacFormat"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxReportIpAddrEvent"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPythonPolicy"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV12v0Group.setStatus("current")

tmnxDiameterNasreqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 11)
)
tmnxDiameterNasreqGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStAarTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStAaaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqTableLastCh"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvp"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpClngStationIdType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortBitspec"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortIdPfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortIdPfixStr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortIdSfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortIdSfixStr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortTypeType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortTypeValue"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqPassword"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqUserNameFormat"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqUserNameOp"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqDomain"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqMacFormat"))
)
if mibBuilder.loadTexts:
    tmnxDiameterNasreqGroup.setStatus("obsolete")

tmnxDiameterProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 12)
)
tmnxDiameterProxyGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyRole"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxAdminState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxRouter"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxOperState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcLocState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcLocOriginStateId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcLocMacAddress"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcLocCtrlMacAddress"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcRemState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcRemOriginStateId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcRemMacAddress"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcRemCtrlMacAddress"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxClientPsmState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStLastClearedTime"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiTcpSendFailed"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiDiamRxDropCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiDiamRxReqs"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiDiamTxResps"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiPendMsgsPmq"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiReqTimeoutsPmq"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStSiTcpSendFailed"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStSiDiamRxDropCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStSiDiamTxReqs"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStSiDiamRxResps"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCcrInitialRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCcaInitialTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCcrUpdateRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCcaUpdateTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCcrTerminateRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCcaTerminateTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCerRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCeaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDwrRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDwaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDwrTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDwaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStAsrTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStAsaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStRarTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStRaaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDprTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDpaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDprRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDpaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStAarRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStAaaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxTableLastCh"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpNasPortIdSfixStr"))
)
if mibBuilder.loadTexts:
    tmnxDiameterProxyGroup.setStatus("obsolete")

tmnxDiameterV13v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 14)
)
tmnxDiameterV13v0NotifyObjsGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPeerName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSessionId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSubscrId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSapId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSLAProfName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNotifyEventId"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV13v0NotifyObjsGroup.setStatus("current")

tmnxDiameterV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 15)
)
tmnxDiameterV13v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxCcrtReplayInterval"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamSeGxCcrtReplaySessionId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamSeGxCcrtReplayAppPolicy"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamSeGxCcrtReplayExpiryTime"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV13v0Group.setStatus("obsolete")

tmnxDiameterV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 16)
)
tmnxDiameterV14v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyV6SourceAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyV6SourceAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyInc3GppGgsnAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyInc3GppGgsnIPv6Addr"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV14v0Group.setStatus("current")

tmnxDiameterPeerStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 17)
)
tmnxDiameterPeerStatsGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsLastClearedTime"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsTotalMessages"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsFailedMessages"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsBaseCe"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsBaseDp"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsBaseDw"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsNqAa"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsGyCcI"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsGyCcU"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsGyCcT"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsGyRa"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsGyAs"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsGxCcI"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsGxCcU"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsGxCcT"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsGxRa"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsGxAs"))
)
if mibBuilder.loadTexts:
    tmnxDiameterPeerStatsGroup.setStatus("current")

tmnxDiameterBaseV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 18)
)
tmnxDiameterBaseV14v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterPlcyTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDescription"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyOriginHost"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyOriginRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyRouter"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcySourceAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcySourceAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyWatchdogTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyConnectionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyTransactionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAdminState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransportProt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransportPort"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerDestHost"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerDestRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerWatchdogTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerConnectionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerTransactTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyPeerPreference"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerPsmState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerConnectionSuspended"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerCooldownSeqStage"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerOrder"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerPrimarySecondary"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerTcTimerTimeLeft"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerTtTimerTimeLeft"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerTwTimerTimeLeft"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerWatchdogAlgActive"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerWatchdogAnswPending"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerCooldownSeqPending"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerCooldownSeqActive"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerPeerRemovalPending"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerPendingMsgsPMQ"))
)
if mibBuilder.loadTexts:
    tmnxDiameterBaseV14v0Group.setStatus("current")

tmnxDiameterNasreqV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 19)
)
tmnxDiameterNasreqV14v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqTableLastCh"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvp"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpClngStationIdType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortBitspec"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortIdPfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortIdPfixStr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortIdSfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortIdSfixStr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortTypeType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqAvpNasPortTypeValue"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqPassword"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqUserNameFormat"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqUserNameOp"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqDomain"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApNqMacFormat"))
)
if mibBuilder.loadTexts:
    tmnxDiameterNasreqV14v0Group.setStatus("current")

tmnxDiameterProxyV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 20)
)
tmnxDiameterProxyV14v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyRole"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxAdminState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxRouter"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxOperState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcLocState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcLocOriginStateId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcLocMacAddress"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcLocCtrlMacAddress"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcRemState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcRemOriginStateId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcRemMacAddress"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcRemCtrlMacAddress"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxClientPsmState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxClientTransactions"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxTableLastCh"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxAvpNasPortIdSfixStr"))
)
if mibBuilder.loadTexts:
    tmnxDiameterProxyV14v0Group.setStatus("current")

tmnxDiameterGyEfhGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 22)
)
tmnxDiameterGyEfhGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamGyEfhAdminState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamGyEfhNewSessionId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamGyEfhInterimCreditReport"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamGyEfhInterimCreditVolume"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamGyEfhInterimCVolumeUnit"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamGyEfhInterimCredValTime"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamGyEfhInterimCMaxAttempts"))
)
if mibBuilder.loadTexts:
    tmnxDiameterGyEfhGroup.setStatus("current")

tmnxDiameterGyCcrtReplayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 23)
)
tmnxDiameterGyCcrtReplayGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamGyCcrtReplayAdminState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamGyCcrtReplayInterval"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamGyCcrtReplayMaxLifeTime"))
)
if mibBuilder.loadTexts:
    tmnxDiameterGyCcrtReplayGroup.setStatus("current")

tmnxDiameterBaseV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 24)
)
tmnxDiameterBaseV15v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterNodeTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeOriginRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeDescription"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeConnectionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeSourceAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeSourceAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeV6SourceAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeV6SourceAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeRouter"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodePythonPolicy"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodePeerTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodePeerRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodePeerLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodePeerAdminState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeDestinationHost"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodePeerAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodePeerAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodePeerConnectionTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodePeerWatchdogTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodePeerPreference"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyNodeOriginHost"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyNodeDestRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyNodeDestRealmLrng"))
)
if mibBuilder.loadTexts:
    tmnxDiameterBaseV15v0Group.setStatus("current")

tmnxDiameterV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 25)
)
tmnxDiameterV15v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyMacFormat"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyMacFormat"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyIncAddressAvp"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyInc3GppChargingId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyInc3GppGprsNQosProf"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyInc3GppNsapi"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyInc3GppSessionStopIn"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyInc3GppSelectionMode"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyInc3GppChargingChara"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyInc3GppRatType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyIncGgsnAddress"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyIncPsInformation"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyIncChargingRBaseName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyChargingRuleBaseName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyIncPdpContextType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyIncUserEqInfoType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGx3gqmAADlMappingType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGx3gqmAADlArbiterName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGx3gqmAADlSchedulrName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGx3gqmAADlPolicerId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGx3gqmAADlQueueId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGx3gqmAAUlMappingType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGx3gqmAAUlArbiterName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGx3gqmAAUlSchedulrName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGx3gqmAAUlPolicerId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGx3gqmAAUlQueueId"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV15v0Group.setStatus("current")

tmnxDiameterGyV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 26)
)
tmnxDiameterGyV16v0Group.setObjects(
    ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGyInc3GppUserLocInfo")
)
if mibBuilder.loadTexts:
    tmnxDiameterGyV16v0Group.setStatus("current")

tmnxDiameterV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 27)
)
tmnxDiameterV16v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsLastCleared"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsCciRequests"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsCciAnswers"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsCcuRequests"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsCcuAnswers"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsCctRequests"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsCctAnswers"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsAsrRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsAsaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsRarRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsRaaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsAarTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsAaaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsReqFailed"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsReqRetransmits"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsResultInfoTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsResultInfoRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsResultSuccessTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsResultSuccessRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsResultProtErrTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsResultProtErrRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsResultTransFailTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsResultTransFailRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsResultPermFailTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApStatsResultPermFailRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatActive"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatRemoteRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatRemOrigStateId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatLocAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatLocAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatLocTcpPort"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatApplications"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatRelay"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatDiscCause"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatTcTimeLeft"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatTwTimeLeft"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatPendingMsgsPmq"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamCcrtRStatLastCleared"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamCcrtRStatSessions"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamCcrtRStatDroppedMlt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamCcrtRStatDroppedNew"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamCcrtRStatDroppedCleared"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamCcrtRStatTerminatedCcat"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsLastCleared"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsCerTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsCeaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsCerRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsCeaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsDprTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsDpaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsDprRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsDpaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsDwrTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsDwaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsDwrRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsDwaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsAppReqTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsAppAnswerRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsAppReqRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatsAppAnswerTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdStatOriginRealm"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV16v0Group.setStatus("current")

tmnxDiameterGxCcrtReplayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 28)
)
tmnxDiameterGxCcrtReplayGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamSeGxCcrtReplaySessionId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamSeGxCcrtReplayAppPolicy"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamSeGxCcrtReplayExpiryTime"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamGxCcrtReplayAdminState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamGxCcrtReplayInterval"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamGxCcrtReplayMaxLifeTime"))
)
if mibBuilder.loadTexts:
    tmnxDiameterGxCcrtReplayGroup.setStatus("current")

tmnxDiameterV16v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 30)
)
tmnxDiameterV16v0NotifyObjsGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamNotifySpiShareType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNotifySpiShareId"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV16v0NotifyObjsGroup.setStatus("current")

tmnxDiameterBaseMcsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 31)
)
tmnxDiameterBaseMcsGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeAllowConn"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeV6AllowConn"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatRemAddrType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatRemAddr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatRemTcpPort"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatMcLocOSI"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatMcRemOSI"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatMcLocState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatMcRemState"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodePeerDefaultPeer"))
)
if mibBuilder.loadTexts:
    tmnxDiameterBaseMcsGroup.setStatus("current")

tmnxDiameterV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 32)
)
tmnxDiameterV19v0Group.setObjects(
    ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxCreditMcsInterval")
)
if mibBuilder.loadTexts:
    tmnxDiameterV19v0Group.setStatus("current")

tmnxDiamBaseStaticRoutes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 33)
)
tmnxDiamBaseStaticRoutes.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerRtTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerRouteRowStatus"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerRtLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerRouteRealm"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerRouteAppId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerRoutePreference"))
)
if mibBuilder.loadTexts:
    tmnxDiamBaseStaticRoutes.setStatus("current")

tmnxDiameterV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 34)
)
tmnxDiameterV20v0Group.setObjects(
    ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxExtendedBw")
)
if mibBuilder.loadTexts:
    tmnxDiameterV20v0Group.setStatus("current")

tmnxDiamObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 98)
)
tmnxDiamObsoleteGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaTableLastChngd"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaLastMgmtChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaFailover"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaFailureHndlng"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaTxTimer"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpServCntxtId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpCldStationId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpRadiusUsrNme"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpSubIdOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpSubIdType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaOutOfCreditRep"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasP"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPPfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPPfixStr"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPSfixType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpNasPType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaApplicationType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaAvpImsiOrg"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaMaxPendingReq"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPlcyDccaTxRetryLimit"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsLastClearTime"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiTcpSendFailed"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiDiamRxDropCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiDiamTxReqs"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiDiamRxResps"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiPendMsgsPMQ"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCiReqTimeoutsPMQ"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStSiTcpSendFailed"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStSiDiamRxDropCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStSiDiamRxReqs"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStSiDiamTxResps"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStErrHdlDiamTxErrCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStErrHdlDiamRxErrCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcrInitialTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcaInitialRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcrUpdateTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcaUpdateRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcrTerminateTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCcaTerminateRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCerTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStCeaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStWdrTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStWdaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStWdrRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStWdaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStAsrRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStAsaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStRarRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStRaaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStDprTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStDpaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStDprRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStDpaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStAarTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStAaaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStLastClearedTime"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiTcpSendFailed"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiDiamRxDropCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiDiamRxReqs"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiDiamTxResps"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiPendMsgsPmq"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiReqTimeoutsPmq"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStSiTcpSendFailed"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStSiDiamRxDropCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStSiDiamTxReqs"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStSiDiamRxResps"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCcrInitialRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCcaInitialTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCcrUpdateRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCcaUpdateTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCcrTerminateRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCcaTerminateTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCerRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCeaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDwrRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDwaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDwrTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDwaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStAsrTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStAsaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStRarTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStRaaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDprTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDpaRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDprRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStDpaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStAarRx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStAaaTx"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamApGxCcrtReplayInterval"))
)
if mibBuilder.loadTexts:
    tmnxDiamObsoleteGroup.setStatus("current")


# Notification objects

tmnxDiamPolicyPeerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0, 1)
)
tmnxDiamPolicyPeerStateChange.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerPrimarySecondary"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerConnectionSuspended"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerCooldownSeqActive"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"))
)
if mibBuilder.loadTexts:
    tmnxDiamPolicyPeerStateChange.setStatus(
        "current"
    )

tmnxDiamAppMessageDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0, 2)
)
tmnxDiamAppMessageDropped.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPeerName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"))
)
if mibBuilder.loadTexts:
    tmnxDiamAppMessageDropped.setStatus(
        "obsolete"
    )

tmnxDiamAppSessionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0, 3)
)
tmnxDiamAppSessionFailure.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSessionId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSubscrId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSapId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSLAProfName"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNotifySpiShareType"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNotifySpiShareId"))
)
if mibBuilder.loadTexts:
    tmnxDiamAppSessionFailure.setStatus(
        "current"
    )

tmnxDiamSessionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0, 4)
)
tmnxDiamSessionEvent.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSessionId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppPlcyApplication"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNotifyEventId"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"))
)
if mibBuilder.loadTexts:
    tmnxDiamSessionEvent.setStatus(
        "current"
    )

tmnxDiamPpPrxMcLocStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0, 5)
)
tmnxDiamPpPrxMcLocStateChanged.setObjects(
    ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcLocState")
)
if mibBuilder.loadTexts:
    tmnxDiamPpPrxMcLocStateChanged.setStatus(
        "current"
    )

tmnxDiamPrxMessageDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0, 6)
)
tmnxDiamPrxMessageDropped.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStCiDiamRxDropCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxClStSiDiamRxDropCnt"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"))
)
if mibBuilder.loadTexts:
    tmnxDiamPrxMessageDropped.setStatus(
        "obsolete"
    )

tmnxDiamMessageDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0, 7)
)
tmnxDiamMessageDropped.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPeerStatsFailedMessages"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppTrapDescription"))
)
if mibBuilder.loadTexts:
    tmnxDiamMessageDropped.setStatus(
        "current"
    )

tmnxDiamNdPeerStatActiveChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 58, 0, 8)
)
tmnxDiamNdPeerStatActiveChanged.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatActive"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNodeDestinationHost"))
)
if mibBuilder.loadTexts:
    tmnxDiamNdPeerStatActiveChanged.setStatus(
        "current"
    )


# Notifications groups

tmnxDiameterNotifyV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 4)
)
tmnxDiameterNotifyV8v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPolicyPeerStateChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppMessageDropped"))
)
if mibBuilder.loadTexts:
    tmnxDiameterNotifyV8v0Group.setStatus(
        "obsolete"
    )

tmnxDiameterNotifyV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 8)
)
tmnxDiameterNotifyV10v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPolicyPeerStateChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppMessageDropped"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSessionFailure"))
)
if mibBuilder.loadTexts:
    tmnxDiameterNotifyV10v0Group.setStatus(
        "obsolete"
    )

tmnxDiameterNotifyV13v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 13)
)
tmnxDiameterNotifyV13v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPolicyPeerStateChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppMessageDropped"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSessionFailure"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamSessionEvent"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcLocStateChanged"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxMessageDropped"))
)
if mibBuilder.loadTexts:
    tmnxDiameterNotifyV13v0Group.setStatus(
        "obsolete"
    )

tmnxDiameterNotifyV14v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 21)
)
tmnxDiameterNotifyV14v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPolicyPeerStateChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSessionFailure"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamSessionEvent"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcLocStateChanged"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamMessageDropped"))
)
if mibBuilder.loadTexts:
    tmnxDiameterNotifyV14v0Group.setStatus(
        "obsolete"
    )

tmnxDiameterNotifyV16v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 29)
)
tmnxDiameterNotifyV16v0Group.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamPolicyPeerStateChange"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamAppSessionFailure"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamSessionEvent"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPpPrxMcLocStateChanged"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamMessageDropped"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamNdPeerStatActiveChanged"))
)
if mibBuilder.loadTexts:
    tmnxDiameterNotifyV16v0Group.setStatus(
        "current"
    )

tmnxDiamObsoleteNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 2, 99)
)
tmnxDiamObsoleteNotifyGroup.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiamAppMessageDropped"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamPrxMessageDropped"))
)
if mibBuilder.loadTexts:
    tmnxDiamObsoleteNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxDiameterV8v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1, 1)
)
tmnxDiameterV8v0MIBCompliance.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV8v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterDccaGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNotifyV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV8v0MIBCompliance.setStatus(
        "obsolete"
    )

tmnxDiameterV10v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1, 2)
)
tmnxDiameterV10v0MIBCompliance.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV8v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterDccaGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNotifyV10v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterDccaGxGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterDccaV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV10v0MIBCompliance.setStatus(
        "obsolete"
    )

tmnxDiameterV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1, 3)
)
tmnxDiameterV12v0Compliance.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV8v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNotifyV10v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV12v0Compliance.setStatus(
        "obsolete"
    )

tmnxDiameterV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1, 4)
)
tmnxDiameterV13v0Compliance.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV8v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNotifyV13v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV12v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV13v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNasreqGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterProxyGroup"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV13v0Compliance.setStatus(
        "obsolete"
    )

tmnxDiameterV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1, 5)
)
tmnxDiameterV14v0Compliance.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNotifyV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV12v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV13v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNasreqV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterProxyV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGyEfhGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGyCcrtReplayGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterPeerStatsGroup"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV14v0Compliance.setStatus(
        "obsolete"
    )

tmnxDiameterV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1, 6)
)
tmnxDiameterV15v0Compliance.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV15v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNotifyV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV12v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV13v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNasreqV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterProxyV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV15v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGyEfhGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGyCcrtReplayGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterPeerStatsGroup"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV15v0Compliance.setStatus(
        "obsolete"
    )

tmnxDiameterV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1, 7)
)
tmnxDiameterV16v0Compliance.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterGyV16v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV16v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGxCcrtReplayGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV16v0NotifyObjsGroup"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV16v0Compliance.setStatus(
        "obsolete"
    )

tmnxDiameterV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1, 8)
)
tmnxDiameterV19v0Compliance.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV15v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNotifyV16v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV16v0NotifyObjsGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV12v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNasreqV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterProxyV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV15v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGyEfhGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGyCcrtReplayGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterPeerStatsGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGyV16v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV16v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGxCcrtReplayGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseMcsGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV19v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV19v0Compliance.setStatus(
        "obsolete"
    )

tmnxDiameterV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 58, 1, 9)
)
tmnxDiameterV20v0Compliance.setObjects(
      *(("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseV15v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNotifyV16v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV16v0NotifyObjsGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV12v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterNasreqV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterProxyV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV14v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV15v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGyEfhGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGyCcrtReplayGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterPeerStatsGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGyV16v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV16v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterGxCcrtReplayGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterBaseMcsGroup"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV19v0Group"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiamBaseStaticRoutes"),
        ("TIMETRA-DIAMETER-MIB", "tmnxDiameterV20v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDiameterV20v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-DIAMETER-MIB",
    **{"TmnxDiamPeerTransportProt": TmnxDiamPeerTransportProt,
       "TmnxDiamDccaApplicationType": TmnxDiamDccaApplicationType,
       "TmnxDiamPeerState": TmnxDiamPeerState,
       "TmnxDiamPlcyVendorSupportType": TmnxDiamPlcyVendorSupportType,
       "TmnxDiamPlcyDccaAvpOriginType": TmnxDiamPlcyDccaAvpOriginType,
       "TmnxDiamProxyState": TmnxDiamProxyState,
       "TmnxDiamSessionId": TmnxDiamSessionId,
       "TmnxDiamFqdn": TmnxDiamFqdn,
       "TmnxDiamFqdnOrEmpty": TmnxDiamFqdnOrEmpty,
       "TmnxDiamApGx3gqmAADlMappingType": TmnxDiamApGx3gqmAADlMappingType,
       "TmnxDiamApGx3gqmAAUlMappingType": TmnxDiamApGx3gqmAAUlMappingType,
       "TmnxDiamNdPeerMcState": TmnxDiamNdPeerMcState,
       "timetraDiameterMIBModule": timetraDiameterMIBModule,
       "tmnxDiameterConformance": tmnxDiameterConformance,
       "tmnxDiameterCompliances": tmnxDiameterCompliances,
       "tmnxDiameterV8v0MIBCompliance": tmnxDiameterV8v0MIBCompliance,
       "tmnxDiameterV10v0MIBCompliance": tmnxDiameterV10v0MIBCompliance,
       "tmnxDiameterV12v0Compliance": tmnxDiameterV12v0Compliance,
       "tmnxDiameterV13v0Compliance": tmnxDiameterV13v0Compliance,
       "tmnxDiameterV14v0Compliance": tmnxDiameterV14v0Compliance,
       "tmnxDiameterV15v0Compliance": tmnxDiameterV15v0Compliance,
       "tmnxDiameterV16v0Compliance": tmnxDiameterV16v0Compliance,
       "tmnxDiameterV19v0Compliance": tmnxDiameterV19v0Compliance,
       "tmnxDiameterV20v0Compliance": tmnxDiameterV20v0Compliance,
       "tmnxDiameterGroups": tmnxDiameterGroups,
       "tmnxDiameterBaseV7v0Group": tmnxDiameterBaseV7v0Group,
       "tmnxDiameterDccaGroup": tmnxDiameterDccaGroup,
       "tmnxDiameterBaseV8v0Group": tmnxDiameterBaseV8v0Group,
       "tmnxDiameterNotifyV8v0Group": tmnxDiameterNotifyV8v0Group,
       "tmnxDiameterV8v0NotifyObjsGroup": tmnxDiameterV8v0NotifyObjsGroup,
       "tmnxDiameterDccaGxGroup": tmnxDiameterDccaGxGroup,
       "tmnxDiameterDccaV10v0Group": tmnxDiameterDccaV10v0Group,
       "tmnxDiameterNotifyV10v0Group": tmnxDiameterNotifyV10v0Group,
       "tmnxDiameterV10v0NotifyObjsGroup": tmnxDiameterV10v0NotifyObjsGroup,
       "tmnxDiameterV12v0Group": tmnxDiameterV12v0Group,
       "tmnxDiameterNasreqGroup": tmnxDiameterNasreqGroup,
       "tmnxDiameterProxyGroup": tmnxDiameterProxyGroup,
       "tmnxDiameterNotifyV13v0Group": tmnxDiameterNotifyV13v0Group,
       "tmnxDiameterV13v0NotifyObjsGroup": tmnxDiameterV13v0NotifyObjsGroup,
       "tmnxDiameterV13v0Group": tmnxDiameterV13v0Group,
       "tmnxDiameterV14v0Group": tmnxDiameterV14v0Group,
       "tmnxDiameterPeerStatsGroup": tmnxDiameterPeerStatsGroup,
       "tmnxDiameterBaseV14v0Group": tmnxDiameterBaseV14v0Group,
       "tmnxDiameterNasreqV14v0Group": tmnxDiameterNasreqV14v0Group,
       "tmnxDiameterProxyV14v0Group": tmnxDiameterProxyV14v0Group,
       "tmnxDiameterNotifyV14v0Group": tmnxDiameterNotifyV14v0Group,
       "tmnxDiameterGyEfhGroup": tmnxDiameterGyEfhGroup,
       "tmnxDiameterGyCcrtReplayGroup": tmnxDiameterGyCcrtReplayGroup,
       "tmnxDiameterBaseV15v0Group": tmnxDiameterBaseV15v0Group,
       "tmnxDiameterV15v0Group": tmnxDiameterV15v0Group,
       "tmnxDiameterGyV16v0Group": tmnxDiameterGyV16v0Group,
       "tmnxDiameterV16v0Group": tmnxDiameterV16v0Group,
       "tmnxDiameterGxCcrtReplayGroup": tmnxDiameterGxCcrtReplayGroup,
       "tmnxDiameterNotifyV16v0Group": tmnxDiameterNotifyV16v0Group,
       "tmnxDiameterV16v0NotifyObjsGroup": tmnxDiameterV16v0NotifyObjsGroup,
       "tmnxDiameterBaseMcsGroup": tmnxDiameterBaseMcsGroup,
       "tmnxDiameterV19v0Group": tmnxDiameterV19v0Group,
       "tmnxDiamBaseStaticRoutes": tmnxDiamBaseStaticRoutes,
       "tmnxDiameterV20v0Group": tmnxDiameterV20v0Group,
       "tmnxDiamObsoleteGroup": tmnxDiamObsoleteGroup,
       "tmnxDiamObsoleteNotifyGroup": tmnxDiamObsoleteNotifyGroup,
       "tmnxDiameter": tmnxDiameter,
       "tmnxDiameterBaseObjects": tmnxDiameterBaseObjects,
       "tmnxDiameterPlcyTableLastChngd": tmnxDiameterPlcyTableLastChngd,
       "tmnxDiameterPlcyTable": tmnxDiameterPlcyTable,
       "tmnxDiameterPlcyEntry": tmnxDiameterPlcyEntry,
       "tmnxDiamPlcyName": tmnxDiamPlcyName,
       "tmnxDiamPlcyRowStatus": tmnxDiamPlcyRowStatus,
       "tmnxDiamPlcyLastMgmtChange": tmnxDiamPlcyLastMgmtChange,
       "tmnxDiamPlcyDescription": tmnxDiamPlcyDescription,
       "tmnxDiamPlcyOriginHost": tmnxDiamPlcyOriginHost,
       "tmnxDiamPlcyOriginRealm": tmnxDiamPlcyOriginRealm,
       "tmnxDiamPlcyRouter": tmnxDiamPlcyRouter,
       "tmnxDiamPlcySourceAddrType": tmnxDiamPlcySourceAddrType,
       "tmnxDiamPlcySourceAddr": tmnxDiamPlcySourceAddr,
       "tmnxDiamPlcyWatchdogTimer": tmnxDiamPlcyWatchdogTimer,
       "tmnxDiamPlcyConnectionTimer": tmnxDiamPlcyConnectionTimer,
       "tmnxDiamPlcyTransactionTimer": tmnxDiamPlcyTransactionTimer,
       "tmnxDiamPlcyVendorSupport": tmnxDiamPlcyVendorSupport,
       "tmnxDiamPlcyApplications": tmnxDiamPlcyApplications,
       "tmnxDiamPlcyPythonPolicy": tmnxDiamPlcyPythonPolicy,
       "tmnxDiamPlcyRole": tmnxDiamPlcyRole,
       "tmnxDiamPlcyV6SourceAddrType": tmnxDiamPlcyV6SourceAddrType,
       "tmnxDiamPlcyV6SourceAddr": tmnxDiamPlcyV6SourceAddr,
       "tmnxDiamPlcyPeerTableLastChngd": tmnxDiamPlcyPeerTableLastChngd,
       "tmnxDiameterPlcyPeerTable": tmnxDiameterPlcyPeerTable,
       "tmnxDiameterPlcyPeerEntry": tmnxDiameterPlcyPeerEntry,
       "tmnxDiamPlcyPeerName": tmnxDiamPlcyPeerName,
       "tmnxDiamPlcyPeerRowStatus": tmnxDiamPlcyPeerRowStatus,
       "tmnxDiamPlcyPeerLastMgmtChange": tmnxDiamPlcyPeerLastMgmtChange,
       "tmnxDiamPlcyPeerAdminState": tmnxDiamPlcyPeerAdminState,
       "tmnxDiamPlcyPeerAddrType": tmnxDiamPlcyPeerAddrType,
       "tmnxDiamPlcyPeerAddr": tmnxDiamPlcyPeerAddr,
       "tmnxDiamPlcyPeerTransportProt": tmnxDiamPlcyPeerTransportProt,
       "tmnxDiamPlcyPeerTransportPort": tmnxDiamPlcyPeerTransportPort,
       "tmnxDiamPlcyPeerDestHost": tmnxDiamPlcyPeerDestHost,
       "tmnxDiamPlcyPeerDestRealm": tmnxDiamPlcyPeerDestRealm,
       "tmnxDiamPlcyPeerWatchdogTimer": tmnxDiamPlcyPeerWatchdogTimer,
       "tmnxDiamPlcyPeerConnectionTimer": tmnxDiamPlcyPeerConnectionTimer,
       "tmnxDiamPlcyPeerTransactTimer": tmnxDiamPlcyPeerTransactTimer,
       "tmnxDiamPlcyPeerPreference": tmnxDiamPlcyPeerPreference,
       "tmnxDiamPlcyPeerInfoTable": tmnxDiamPlcyPeerInfoTable,
       "tmnxDiamPlcyPeerInfoEntry": tmnxDiamPlcyPeerInfoEntry,
       "tmnxDiamPeerPsmState": tmnxDiamPeerPsmState,
       "tmnxDiamPeerConnectionSuspended": tmnxDiamPeerConnectionSuspended,
       "tmnxDiamPeerCooldownSeqStage": tmnxDiamPeerCooldownSeqStage,
       "tmnxDiamPeerOrder": tmnxDiamPeerOrder,
       "tmnxDiamPeerPrimarySecondary": tmnxDiamPeerPrimarySecondary,
       "tmnxDiamPeerTcTimerTimeLeft": tmnxDiamPeerTcTimerTimeLeft,
       "tmnxDiamPeerTtTimerTimeLeft": tmnxDiamPeerTtTimerTimeLeft,
       "tmnxDiamPeerTwTimerTimeLeft": tmnxDiamPeerTwTimerTimeLeft,
       "tmnxDiamPeerWatchdogAlgActive": tmnxDiamPeerWatchdogAlgActive,
       "tmnxDiamPeerWatchdogAnswPending": tmnxDiamPeerWatchdogAnswPending,
       "tmnxDiamPeerCooldownSeqPending": tmnxDiamPeerCooldownSeqPending,
       "tmnxDiamPeerCooldownSeqActive": tmnxDiamPeerCooldownSeqActive,
       "tmnxDiamPeerPeerRemovalPending": tmnxDiamPeerPeerRemovalPending,
       "tmnxDiamPeerPendingMsgsPMQ": tmnxDiamPeerPendingMsgsPMQ,
       "tmnxDiamPlcyPeerStatsTable": tmnxDiamPlcyPeerStatsTable,
       "tmnxDiamPlcyPeerStatsEntry": tmnxDiamPlcyPeerStatsEntry,
       "tmnxDiamPeerStatsLastClearTime": tmnxDiamPeerStatsLastClearTime,
       "tmnxDiamPeerStCiTcpSendFailed": tmnxDiamPeerStCiTcpSendFailed,
       "tmnxDiamPeerStCiDiamRxDropCnt": tmnxDiamPeerStCiDiamRxDropCnt,
       "tmnxDiamPeerStCiDiamTxReqs": tmnxDiamPeerStCiDiamTxReqs,
       "tmnxDiamPeerStCiDiamRxResps": tmnxDiamPeerStCiDiamRxResps,
       "tmnxDiamPeerStCiPendMsgsPMQ": tmnxDiamPeerStCiPendMsgsPMQ,
       "tmnxDiamPeerStCiReqTimeoutsPMQ": tmnxDiamPeerStCiReqTimeoutsPMQ,
       "tmnxDiamPeerStSiTcpSendFailed": tmnxDiamPeerStSiTcpSendFailed,
       "tmnxDiamPeerStSiDiamRxDropCnt": tmnxDiamPeerStSiDiamRxDropCnt,
       "tmnxDiamPeerStSiDiamRxReqs": tmnxDiamPeerStSiDiamRxReqs,
       "tmnxDiamPeerStSiDiamTxResps": tmnxDiamPeerStSiDiamTxResps,
       "tmnxDiamPeerStErrHdlDiamTxErrCnt": tmnxDiamPeerStErrHdlDiamTxErrCnt,
       "tmnxDiamPeerStErrHdlDiamRxErrCnt": tmnxDiamPeerStErrHdlDiamRxErrCnt,
       "tmnxDiamPeerStCcrInitialTx": tmnxDiamPeerStCcrInitialTx,
       "tmnxDiamPeerStCcaInitialRx": tmnxDiamPeerStCcaInitialRx,
       "tmnxDiamPeerStCcrUpdateTx": tmnxDiamPeerStCcrUpdateTx,
       "tmnxDiamPeerStCcaUpdateRx": tmnxDiamPeerStCcaUpdateRx,
       "tmnxDiamPeerStCcrTerminateTx": tmnxDiamPeerStCcrTerminateTx,
       "tmnxDiamPeerStCcaTerminateRx": tmnxDiamPeerStCcaTerminateRx,
       "tmnxDiamPeerStCerTx": tmnxDiamPeerStCerTx,
       "tmnxDiamPeerStCeaRx": tmnxDiamPeerStCeaRx,
       "tmnxDiamPeerStWdrTx": tmnxDiamPeerStWdrTx,
       "tmnxDiamPeerStWdaRx": tmnxDiamPeerStWdaRx,
       "tmnxDiamPeerStWdrRx": tmnxDiamPeerStWdrRx,
       "tmnxDiamPeerStWdaTx": tmnxDiamPeerStWdaTx,
       "tmnxDiamPeerStAsrRx": tmnxDiamPeerStAsrRx,
       "tmnxDiamPeerStAsaTx": tmnxDiamPeerStAsaTx,
       "tmnxDiamPeerStRarRx": tmnxDiamPeerStRarRx,
       "tmnxDiamPeerStRaaTx": tmnxDiamPeerStRaaTx,
       "tmnxDiamPeerStDprTx": tmnxDiamPeerStDprTx,
       "tmnxDiamPeerStDpaRx": tmnxDiamPeerStDpaRx,
       "tmnxDiamPeerStDprRx": tmnxDiamPeerStDprRx,
       "tmnxDiamPeerStDpaTx": tmnxDiamPeerStDpaTx,
       "tmnxDiamPeerStAarTx": tmnxDiamPeerStAarTx,
       "tmnxDiamPeerStAaaRx": tmnxDiamPeerStAaaRx,
       "tmnxDiameterNodeTableLastChngd": tmnxDiameterNodeTableLastChngd,
       "tmnxDiameterNodeTable": tmnxDiameterNodeTable,
       "tmnxDiameterNodeEntry": tmnxDiameterNodeEntry,
       "tmnxDiamNodeOriginHost": tmnxDiamNodeOriginHost,
       "tmnxDiamNodeRowStatus": tmnxDiamNodeRowStatus,
       "tmnxDiamNodeLastMgmtChange": tmnxDiamNodeLastMgmtChange,
       "tmnxDiamNodeOriginRealm": tmnxDiamNodeOriginRealm,
       "tmnxDiamNodeDescription": tmnxDiamNodeDescription,
       "tmnxDiamNodeConnectionTimer": tmnxDiamNodeConnectionTimer,
       "tmnxDiamNodeSourceAddrType": tmnxDiamNodeSourceAddrType,
       "tmnxDiamNodeSourceAddr": tmnxDiamNodeSourceAddr,
       "tmnxDiamNodeV6SourceAddrType": tmnxDiamNodeV6SourceAddrType,
       "tmnxDiamNodeV6SourceAddr": tmnxDiamNodeV6SourceAddr,
       "tmnxDiamNodeRouter": tmnxDiamNodeRouter,
       "tmnxDiamNodePythonPolicy": tmnxDiamNodePythonPolicy,
       "tmnxDiamNodeAllowConn": tmnxDiamNodeAllowConn,
       "tmnxDiamNodeV6AllowConn": tmnxDiamNodeV6AllowConn,
       "tmnxDiamNodePeerTableLastChngd": tmnxDiamNodePeerTableLastChngd,
       "tmnxDiameterNodePeerTable": tmnxDiameterNodePeerTable,
       "tmnxDiameterNodePeerEntry": tmnxDiameterNodePeerEntry,
       "tmnxDiamNodePeerIndex": tmnxDiamNodePeerIndex,
       "tmnxDiamNodePeerRowStatus": tmnxDiamNodePeerRowStatus,
       "tmnxDiamNodePeerLastMgmtChange": tmnxDiamNodePeerLastMgmtChange,
       "tmnxDiamNodePeerAdminState": tmnxDiamNodePeerAdminState,
       "tmnxDiamNodeDestinationHost": tmnxDiamNodeDestinationHost,
       "tmnxDiamNodePeerAddrType": tmnxDiamNodePeerAddrType,
       "tmnxDiamNodePeerAddr": tmnxDiamNodePeerAddr,
       "tmnxDiamNodePeerConnectionTimer": tmnxDiamNodePeerConnectionTimer,
       "tmnxDiamNodePeerWatchdogTimer": tmnxDiamNodePeerWatchdogTimer,
       "tmnxDiamNodePeerPreference": tmnxDiamNodePeerPreference,
       "tmnxDiamNodePeerDefaultPeer": tmnxDiamNodePeerDefaultPeer,
       "tmnxDiamNdPeerStatTable": tmnxDiamNdPeerStatTable,
       "tmnxDiamNdPeerStatEntry": tmnxDiamNdPeerStatEntry,
       "tmnxDiamNdPeerStatState": tmnxDiamNdPeerStatState,
       "tmnxDiamNdPeerStatActive": tmnxDiamNdPeerStatActive,
       "tmnxDiamNdPeerStatRemoteRealm": tmnxDiamNdPeerStatRemoteRealm,
       "tmnxDiamNdPeerStatRemOrigStateId": tmnxDiamNdPeerStatRemOrigStateId,
       "tmnxDiamNdPeerStatLocAddrType": tmnxDiamNdPeerStatLocAddrType,
       "tmnxDiamNdPeerStatLocAddr": tmnxDiamNdPeerStatLocAddr,
       "tmnxDiamNdPeerStatLocTcpPort": tmnxDiamNdPeerStatLocTcpPort,
       "tmnxDiamNdPeerStatApplications": tmnxDiamNdPeerStatApplications,
       "tmnxDiamNdPeerStatRelay": tmnxDiamNdPeerStatRelay,
       "tmnxDiamNdPeerStatDiscCause": tmnxDiamNdPeerStatDiscCause,
       "tmnxDiamNdPeerStatTcTimeLeft": tmnxDiamNdPeerStatTcTimeLeft,
       "tmnxDiamNdPeerStatTwTimeLeft": tmnxDiamNdPeerStatTwTimeLeft,
       "tmnxDiamNdPeerStatPendingMsgsPmq": tmnxDiamNdPeerStatPendingMsgsPmq,
       "tmnxDiamNdPeerStatRemAddrType": tmnxDiamNdPeerStatRemAddrType,
       "tmnxDiamNdPeerStatRemAddr": tmnxDiamNdPeerStatRemAddr,
       "tmnxDiamNdPeerStatRemTcpPort": tmnxDiamNdPeerStatRemTcpPort,
       "tmnxDiamNdPeerStatMcLocOSI": tmnxDiamNdPeerStatMcLocOSI,
       "tmnxDiamNdPeerStatMcRemOSI": tmnxDiamNdPeerStatMcRemOSI,
       "tmnxDiamNdPeerStatMcLocState": tmnxDiamNdPeerStatMcLocState,
       "tmnxDiamNdPeerStatMcRemState": tmnxDiamNdPeerStatMcRemState,
       "tmnxDiamNdPeerStatsTable": tmnxDiamNdPeerStatsTable,
       "tmnxDiamNdPeerStatsEntry": tmnxDiamNdPeerStatsEntry,
       "tmnxDiamNdPeerStatsLastCleared": tmnxDiamNdPeerStatsLastCleared,
       "tmnxDiamNdPeerStatsCerTx": tmnxDiamNdPeerStatsCerTx,
       "tmnxDiamNdPeerStatsCeaRx": tmnxDiamNdPeerStatsCeaRx,
       "tmnxDiamNdPeerStatsCerRx": tmnxDiamNdPeerStatsCerRx,
       "tmnxDiamNdPeerStatsCeaTx": tmnxDiamNdPeerStatsCeaTx,
       "tmnxDiamNdPeerStatsDprTx": tmnxDiamNdPeerStatsDprTx,
       "tmnxDiamNdPeerStatsDpaRx": tmnxDiamNdPeerStatsDpaRx,
       "tmnxDiamNdPeerStatsDprRx": tmnxDiamNdPeerStatsDprRx,
       "tmnxDiamNdPeerStatsDpaTx": tmnxDiamNdPeerStatsDpaTx,
       "tmnxDiamNdPeerStatsDwrTx": tmnxDiamNdPeerStatsDwrTx,
       "tmnxDiamNdPeerStatsDwaRx": tmnxDiamNdPeerStatsDwaRx,
       "tmnxDiamNdPeerStatsDwrRx": tmnxDiamNdPeerStatsDwrRx,
       "tmnxDiamNdPeerStatsDwaTx": tmnxDiamNdPeerStatsDwaTx,
       "tmnxDiamNdPeerStatsAppReqTx": tmnxDiamNdPeerStatsAppReqTx,
       "tmnxDiamNdPeerStatsAppAnswerRx": tmnxDiamNdPeerStatsAppAnswerRx,
       "tmnxDiamNdPeerStatsAppReqRx": tmnxDiamNdPeerStatsAppReqRx,
       "tmnxDiamNdPeerStatsAppAnswerTx": tmnxDiamNdPeerStatsAppAnswerTx,
       "tmnxDiamNdStatTable": tmnxDiamNdStatTable,
       "tmnxDiamNdStatEntry": tmnxDiamNdStatEntry,
       "tmnxDiamNdStatOriginRealm": tmnxDiamNdStatOriginRealm,
       "tmnxDiamNdPeerRtTableLastChngd": tmnxDiamNdPeerRtTableLastChngd,
       "tmnxDiamNdPeerRouteTable": tmnxDiamNdPeerRouteTable,
       "tmnxDiamNdPeerRouteEntry": tmnxDiamNdPeerRouteEntry,
       "tmnxDiamNdPeerRouteIndex": tmnxDiamNdPeerRouteIndex,
       "tmnxDiamNdPeerRouteRowStatus": tmnxDiamNdPeerRouteRowStatus,
       "tmnxDiamNdPeerRtLastMgmtChange": tmnxDiamNdPeerRtLastMgmtChange,
       "tmnxDiamNdPeerRouteRealm": tmnxDiamNdPeerRouteRealm,
       "tmnxDiamNdPeerRouteAppId": tmnxDiamNdPeerRouteAppId,
       "tmnxDiamNdPeerRoutePreference": tmnxDiamNdPeerRoutePreference,
       "tmnxDiameterDccaObjects": tmnxDiameterDccaObjects,
       "tmnxDiamPlcyDccaTableLastChngd": tmnxDiamPlcyDccaTableLastChngd,
       "tmnxDiameterPlcyDccaTable": tmnxDiameterPlcyDccaTable,
       "tmnxDiameterPlcyDccaEntry": tmnxDiameterPlcyDccaEntry,
       "tmnxDiamPlcyDccaLastMgmtChange": tmnxDiamPlcyDccaLastMgmtChange,
       "tmnxDiamPlcyDccaFailover": tmnxDiamPlcyDccaFailover,
       "tmnxDiamPlcyDccaFailureHndlng": tmnxDiamPlcyDccaFailureHndlng,
       "tmnxDiamPlcyDccaTxTimer": tmnxDiamPlcyDccaTxTimer,
       "tmnxDiamPlcyDccaAvpServCntxtId": tmnxDiamPlcyDccaAvpServCntxtId,
       "tmnxDiamPlcyDccaAvpCldStationId": tmnxDiamPlcyDccaAvpCldStationId,
       "tmnxDiamPlcyDccaAvpRadiusUsrNme": tmnxDiamPlcyDccaAvpRadiusUsrNme,
       "tmnxDiamPlcyDccaAvpSubIdOrg": tmnxDiamPlcyDccaAvpSubIdOrg,
       "tmnxDiamPlcyDccaAvpSubIdType": tmnxDiamPlcyDccaAvpSubIdType,
       "tmnxDiamPlcyDccaAvpNasP": tmnxDiamPlcyDccaAvpNasP,
       "tmnxDiamPlcyDccaAvpNasPPfixType": tmnxDiamPlcyDccaAvpNasPPfixType,
       "tmnxDiamPlcyDccaAvpNasPPfixStr": tmnxDiamPlcyDccaAvpNasPPfixStr,
       "tmnxDiamPlcyDccaAvpNasPSfixType": tmnxDiamPlcyDccaAvpNasPSfixType,
       "tmnxDiamPlcyDccaAvpNasPType": tmnxDiamPlcyDccaAvpNasPType,
       "tmnxDiamPlcyDccaAvpImsiOrg": tmnxDiamPlcyDccaAvpImsiOrg,
       "tmnxDiamPlcyDccaApplicationType": tmnxDiamPlcyDccaApplicationType,
       "tmnxDiamPlcyDccaMaxPendingReq": tmnxDiamPlcyDccaMaxPendingReq,
       "tmnxDiamPlcyDccaTxRetryLimit": tmnxDiamPlcyDccaTxRetryLimit,
       "tmnxDiamPlcyDccaOutOfCreditRep": tmnxDiamPlcyDccaOutOfCreditRep,
       "tmnxDiameterObjects": tmnxDiameterObjects,
       "tmnxDiamAppPlcyTableLastCh": tmnxDiamAppPlcyTableLastCh,
       "tmnxDiamAppPlcyTable": tmnxDiamAppPlcyTable,
       "tmnxDiamAppPlcyEntry": tmnxDiamAppPlcyEntry,
       "tmnxDiamAppPlcyId": tmnxDiamAppPlcyId,
       "tmnxDiamAppPlcyRowStatus": tmnxDiamAppPlcyRowStatus,
       "tmnxDiamAppPlcyLastMgmtChange": tmnxDiamAppPlcyLastMgmtChange,
       "tmnxDiamAppPlcyFailover": tmnxDiamAppPlcyFailover,
       "tmnxDiamAppPlcyFailureHndlng": tmnxDiamAppPlcyFailureHndlng,
       "tmnxDiamAppPlcyPeerPlcy": tmnxDiamAppPlcyPeerPlcy,
       "tmnxDiamAppPlcyApplication": tmnxDiamAppPlcyApplication,
       "tmnxDiamAppPlcyTxTimer": tmnxDiamAppPlcyTxTimer,
       "tmnxDiamAppPlcyDescription": tmnxDiamAppPlcyDescription,
       "tmnxDiamAppPlcyNodeOriginHost": tmnxDiamAppPlcyNodeOriginHost,
       "tmnxDiamAppPlcyNodeDestRealm": tmnxDiamAppPlcyNodeDestRealm,
       "tmnxDiamAppPlcyNodeDestRealmLrng": tmnxDiamAppPlcyNodeDestRealmLrng,
       "tmnxDiamApGyTableLastCh": tmnxDiamApGyTableLastCh,
       "tmnxDiamApGyTable": tmnxDiamApGyTable,
       "tmnxDiamApGyEntry": tmnxDiamApGyEntry,
       "tmnxDiamApGyLastMgmtChange": tmnxDiamApGyLastMgmtChange,
       "tmnxDiamApGyAvpServCntxtId": tmnxDiamApGyAvpServCntxtId,
       "tmnxDiamApGyAvpCldStationId": tmnxDiamApGyAvpCldStationId,
       "tmnxDiamApGyAvpRadiusUsrNme": tmnxDiamApGyAvpRadiusUsrNme,
       "tmnxDiamApGyAvpImsiOrg": tmnxDiamApGyAvpImsiOrg,
       "tmnxDiamApGyOutOfCreditRep": tmnxDiamApGyOutOfCreditRep,
       "tmnxDiamApGyVendorSupport": tmnxDiamApGyVendorSupport,
       "tmnxDiamApGySubIdOrg": tmnxDiamApGySubIdOrg,
       "tmnxDiamApGySubIdType": tmnxDiamApGySubIdType,
       "tmnxDiamApGyInc3GppGgsnAddr": tmnxDiamApGyInc3GppGgsnAddr,
       "tmnxDiamApGyInc3GppGgsnIPv6Addr": tmnxDiamApGyInc3GppGgsnIPv6Addr,
       "tmnxDiamApGyMacFormat": tmnxDiamApGyMacFormat,
       "tmnxDiamApGyIncAddressAvp": tmnxDiamApGyIncAddressAvp,
       "tmnxDiamApGyInc3GppChargingId": tmnxDiamApGyInc3GppChargingId,
       "tmnxDiamApGyInc3GppGprsNQosProf": tmnxDiamApGyInc3GppGprsNQosProf,
       "tmnxDiamApGyInc3GppNsapi": tmnxDiamApGyInc3GppNsapi,
       "tmnxDiamApGyInc3GppSessionStopIn": tmnxDiamApGyInc3GppSessionStopIn,
       "tmnxDiamApGyInc3GppSelectionMode": tmnxDiamApGyInc3GppSelectionMode,
       "tmnxDiamApGyInc3GppChargingChara": tmnxDiamApGyInc3GppChargingChara,
       "tmnxDiamApGyInc3GppRatType": tmnxDiamApGyInc3GppRatType,
       "tmnxDiamApGyIncGgsnAddress": tmnxDiamApGyIncGgsnAddress,
       "tmnxDiamApGyIncPsInformation": tmnxDiamApGyIncPsInformation,
       "tmnxDiamApGyIncChargingRBaseName": tmnxDiamApGyIncChargingRBaseName,
       "tmnxDiamApGyChargingRuleBaseName": tmnxDiamApGyChargingRuleBaseName,
       "tmnxDiamApGyIncPdpContextType": tmnxDiamApGyIncPdpContextType,
       "tmnxDiamApGyIncUserEqInfoType": tmnxDiamApGyIncUserEqInfoType,
       "tmnxDiamApGyInc3GppUserLocInfo": tmnxDiamApGyInc3GppUserLocInfo,
       "tmnxDiamApGxTableLastCh": tmnxDiamApGxTableLastCh,
       "tmnxDiamApGxTable": tmnxDiamApGxTable,
       "tmnxDiamApGxEntry": tmnxDiamApGxEntry,
       "tmnxDiamApGxLastMgmtChange": tmnxDiamApGxLastMgmtChange,
       "tmnxDiamApGxAvp": tmnxDiamApGxAvp,
       "tmnxDiamApGxAvpClngStationIdType": tmnxDiamApGxAvpClngStationIdType,
       "tmnxDiamApGxAvpNasPortBitspec": tmnxDiamApGxAvpNasPortBitspec,
       "tmnxDiamApGxAvpNasPortIdPfixType": tmnxDiamApGxAvpNasPortIdPfixType,
       "tmnxDiamApGxAvpNasPortIdPfixStr": tmnxDiamApGxAvpNasPortIdPfixStr,
       "tmnxDiamApGxAvpNasPortIdSfixType": tmnxDiamApGxAvpNasPortIdSfixType,
       "tmnxDiamApGxAvpNasPortTypeValue": tmnxDiamApGxAvpNasPortTypeValue,
       "tmnxDiamApGxAvpUeInfoType": tmnxDiamApGxAvpUeInfoType,
       "tmnxDiamApGxSubIdOrg": tmnxDiamApGxSubIdOrg,
       "tmnxDiamApGxSubIdType": tmnxDiamApGxSubIdType,
       "tmnxDiamApGxMacFormat": tmnxDiamApGxMacFormat,
       "tmnxDiamApGxReportIpAddrEvent": tmnxDiamApGxReportIpAddrEvent,
       "tmnxDiamApGxAvpNasPortIdSfixStr": tmnxDiamApGxAvpNasPortIdSfixStr,
       "tmnxDiamApGxCcrtReplayInterval": tmnxDiamApGxCcrtReplayInterval,
       "tmnxDiamApGxCreditMcsInterval": tmnxDiamApGxCreditMcsInterval,
       "tmnxDiamApGxExtendedBw": tmnxDiamApGxExtendedBw,
       "tmnxDiamApNqTableLastCh": tmnxDiamApNqTableLastCh,
       "tmnxDiamApNqTable": tmnxDiamApNqTable,
       "tmnxDiamApNqEntry": tmnxDiamApNqEntry,
       "tmnxDiamApNqLastMgmtChange": tmnxDiamApNqLastMgmtChange,
       "tmnxDiamApNqAvp": tmnxDiamApNqAvp,
       "tmnxDiamApNqAvpClngStationIdType": tmnxDiamApNqAvpClngStationIdType,
       "tmnxDiamApNqAvpNasPortBitspec": tmnxDiamApNqAvpNasPortBitspec,
       "tmnxDiamApNqAvpNasPortIdPfixType": tmnxDiamApNqAvpNasPortIdPfixType,
       "tmnxDiamApNqAvpNasPortIdPfixStr": tmnxDiamApNqAvpNasPortIdPfixStr,
       "tmnxDiamApNqAvpNasPortIdSfixType": tmnxDiamApNqAvpNasPortIdSfixType,
       "tmnxDiamApNqAvpNasPortIdSfixStr": tmnxDiamApNqAvpNasPortIdSfixStr,
       "tmnxDiamApNqAvpNasPortTypeType": tmnxDiamApNqAvpNasPortTypeType,
       "tmnxDiamApNqAvpNasPortTypeValue": tmnxDiamApNqAvpNasPortTypeValue,
       "tmnxDiamApNqPassword": tmnxDiamApNqPassword,
       "tmnxDiamApNqUserNameFormat": tmnxDiamApNqUserNameFormat,
       "tmnxDiamApNqUserNameOp": tmnxDiamApNqUserNameOp,
       "tmnxDiamApNqDomain": tmnxDiamApNqDomain,
       "tmnxDiamApNqMacFormat": tmnxDiamApNqMacFormat,
       "tmnxDiamPpPrxTableLastCh": tmnxDiamPpPrxTableLastCh,
       "tmnxDiamPpPrxTable": tmnxDiamPpPrxTable,
       "tmnxDiamPpPrxEntry": tmnxDiamPpPrxEntry,
       "tmnxDiamPpPrxLastMgmtChange": tmnxDiamPpPrxLastMgmtChange,
       "tmnxDiamPpPrxAdminState": tmnxDiamPpPrxAdminState,
       "tmnxDiamPpPrxRouter": tmnxDiamPpPrxRouter,
       "tmnxDiamPpPrxAddrType": tmnxDiamPpPrxAddrType,
       "tmnxDiamPpPrxAddr": tmnxDiamPpPrxAddr,
       "tmnxDiamPpPrxOperState": tmnxDiamPpPrxOperState,
       "tmnxDiamPpPrxMcLocState": tmnxDiamPpPrxMcLocState,
       "tmnxDiamPpPrxMcLocOriginStateId": tmnxDiamPpPrxMcLocOriginStateId,
       "tmnxDiamPpPrxMcLocMacAddress": tmnxDiamPpPrxMcLocMacAddress,
       "tmnxDiamPpPrxMcLocCtrlMacAddress": tmnxDiamPpPrxMcLocCtrlMacAddress,
       "tmnxDiamPpPrxMcRemState": tmnxDiamPpPrxMcRemState,
       "tmnxDiamPpPrxMcRemOriginStateId": tmnxDiamPpPrxMcRemOriginStateId,
       "tmnxDiamPpPrxMcRemMacAddress": tmnxDiamPpPrxMcRemMacAddress,
       "tmnxDiamPpPrxMcRemCtrlMacAddress": tmnxDiamPpPrxMcRemCtrlMacAddress,
       "tmnxDiamPpPrxClientTable": tmnxDiamPpPrxClientTable,
       "tmnxDiamPpPrxClientEntry": tmnxDiamPpPrxClientEntry,
       "tmnxDiamPpPrxClientIpAddrType": tmnxDiamPpPrxClientIpAddrType,
       "tmnxDiamPpPrxClientIpAddr": tmnxDiamPpPrxClientIpAddr,
       "tmnxDiamPpPrxClientPort": tmnxDiamPpPrxClientPort,
       "tmnxDiamPpPrxClientPsmState": tmnxDiamPpPrxClientPsmState,
       "tmnxDiamPpPrxClientTransactions": tmnxDiamPpPrxClientTransactions,
       "tmnxDiamPrxClStTable": tmnxDiamPrxClStTable,
       "tmnxDiamPrxClStEntry": tmnxDiamPrxClStEntry,
       "tmnxDiamPrxClStLastClearedTime": tmnxDiamPrxClStLastClearedTime,
       "tmnxDiamPrxClStCiTcpSendFailed": tmnxDiamPrxClStCiTcpSendFailed,
       "tmnxDiamPrxClStCiDiamRxDropCnt": tmnxDiamPrxClStCiDiamRxDropCnt,
       "tmnxDiamPrxClStCiDiamRxReqs": tmnxDiamPrxClStCiDiamRxReqs,
       "tmnxDiamPrxClStCiDiamTxResps": tmnxDiamPrxClStCiDiamTxResps,
       "tmnxDiamPrxClStCiPendMsgsPmq": tmnxDiamPrxClStCiPendMsgsPmq,
       "tmnxDiamPrxClStCiReqTimeoutsPmq": tmnxDiamPrxClStCiReqTimeoutsPmq,
       "tmnxDiamPrxClStSiTcpSendFailed": tmnxDiamPrxClStSiTcpSendFailed,
       "tmnxDiamPrxClStSiDiamRxDropCnt": tmnxDiamPrxClStSiDiamRxDropCnt,
       "tmnxDiamPrxClStSiDiamTxReqs": tmnxDiamPrxClStSiDiamTxReqs,
       "tmnxDiamPrxClStSiDiamRxResps": tmnxDiamPrxClStSiDiamRxResps,
       "tmnxDiamPrxClStCcrInitialRx": tmnxDiamPrxClStCcrInitialRx,
       "tmnxDiamPrxClStCcaInitialTx": tmnxDiamPrxClStCcaInitialTx,
       "tmnxDiamPrxClStCcrUpdateRx": tmnxDiamPrxClStCcrUpdateRx,
       "tmnxDiamPrxClStCcaUpdateTx": tmnxDiamPrxClStCcaUpdateTx,
       "tmnxDiamPrxClStCcrTerminateRx": tmnxDiamPrxClStCcrTerminateRx,
       "tmnxDiamPrxClStCcaTerminateTx": tmnxDiamPrxClStCcaTerminateTx,
       "tmnxDiamPrxClStCerRx": tmnxDiamPrxClStCerRx,
       "tmnxDiamPrxClStCeaTx": tmnxDiamPrxClStCeaTx,
       "tmnxDiamPrxClStDwrRx": tmnxDiamPrxClStDwrRx,
       "tmnxDiamPrxClStDwaTx": tmnxDiamPrxClStDwaTx,
       "tmnxDiamPrxClStDwrTx": tmnxDiamPrxClStDwrTx,
       "tmnxDiamPrxClStDwaRx": tmnxDiamPrxClStDwaRx,
       "tmnxDiamPrxClStAsrTx": tmnxDiamPrxClStAsrTx,
       "tmnxDiamPrxClStAsaRx": tmnxDiamPrxClStAsaRx,
       "tmnxDiamPrxClStRarTx": tmnxDiamPrxClStRarTx,
       "tmnxDiamPrxClStRaaRx": tmnxDiamPrxClStRaaRx,
       "tmnxDiamPrxClStDprTx": tmnxDiamPrxClStDprTx,
       "tmnxDiamPrxClStDpaRx": tmnxDiamPrxClStDpaRx,
       "tmnxDiamPrxClStDprRx": tmnxDiamPrxClStDprRx,
       "tmnxDiamPrxClStDpaTx": tmnxDiamPrxClStDpaTx,
       "tmnxDiamPrxClStAarRx": tmnxDiamPrxClStAarRx,
       "tmnxDiamPrxClStAaaTx": tmnxDiamPrxClStAaaTx,
       "tmnxDiamPeerStatsTable": tmnxDiamPeerStatsTable,
       "tmnxDiamPeerStatsEntry": tmnxDiamPeerStatsEntry,
       "tmnxDiamPeerStatsPeerName": tmnxDiamPeerStatsPeerName,
       "tmnxDiamPeerStatsPeerIpAddrType": tmnxDiamPeerStatsPeerIpAddrType,
       "tmnxDiamPeerStatsPeerIpAddr": tmnxDiamPeerStatsPeerIpAddr,
       "tmnxDiamPeerStatsPeerPort": tmnxDiamPeerStatsPeerPort,
       "tmnxDiamPeerStatsDirection": tmnxDiamPeerStatsDirection,
       "tmnxDiamPeerStatsMessageType": tmnxDiamPeerStatsMessageType,
       "tmnxDiamPeerStatsLastClearedTime": tmnxDiamPeerStatsLastClearedTime,
       "tmnxDiamPeerStatsTotalMessages": tmnxDiamPeerStatsTotalMessages,
       "tmnxDiamPeerStatsFailedMessages": tmnxDiamPeerStatsFailedMessages,
       "tmnxDiamPeerStatsBaseCe": tmnxDiamPeerStatsBaseCe,
       "tmnxDiamPeerStatsBaseDp": tmnxDiamPeerStatsBaseDp,
       "tmnxDiamPeerStatsBaseDw": tmnxDiamPeerStatsBaseDw,
       "tmnxDiamPeerStatsNqAa": tmnxDiamPeerStatsNqAa,
       "tmnxDiamPeerStatsGyCcI": tmnxDiamPeerStatsGyCcI,
       "tmnxDiamPeerStatsGyCcU": tmnxDiamPeerStatsGyCcU,
       "tmnxDiamPeerStatsGyCcT": tmnxDiamPeerStatsGyCcT,
       "tmnxDiamPeerStatsGyRa": tmnxDiamPeerStatsGyRa,
       "tmnxDiamPeerStatsGyAs": tmnxDiamPeerStatsGyAs,
       "tmnxDiamPeerStatsGxCcI": tmnxDiamPeerStatsGxCcI,
       "tmnxDiamPeerStatsGxCcU": tmnxDiamPeerStatsGxCcU,
       "tmnxDiamPeerStatsGxCcT": tmnxDiamPeerStatsGxCcT,
       "tmnxDiamPeerStatsGxRa": tmnxDiamPeerStatsGxRa,
       "tmnxDiamPeerStatsGxAs": tmnxDiamPeerStatsGxAs,
       "tmnxDiamGyEfhTable": tmnxDiamGyEfhTable,
       "tmnxDiamGyEfhEntry": tmnxDiamGyEfhEntry,
       "tmnxDiamGyEfhAdminState": tmnxDiamGyEfhAdminState,
       "tmnxDiamGyEfhNewSessionId": tmnxDiamGyEfhNewSessionId,
       "tmnxDiamGyEfhInterimCreditReport": tmnxDiamGyEfhInterimCreditReport,
       "tmnxDiamGyEfhInterimCreditVolume": tmnxDiamGyEfhInterimCreditVolume,
       "tmnxDiamGyEfhInterimCVolumeUnit": tmnxDiamGyEfhInterimCVolumeUnit,
       "tmnxDiamGyEfhInterimCredValTime": tmnxDiamGyEfhInterimCredValTime,
       "tmnxDiamGyEfhInterimCMaxAttempts": tmnxDiamGyEfhInterimCMaxAttempts,
       "tmnxDiamGyCcrtReplayTable": tmnxDiamGyCcrtReplayTable,
       "tmnxDiamGyCcrtReplayEntry": tmnxDiamGyCcrtReplayEntry,
       "tmnxDiamGyCcrtReplayAdminState": tmnxDiamGyCcrtReplayAdminState,
       "tmnxDiamGyCcrtReplayInterval": tmnxDiamGyCcrtReplayInterval,
       "tmnxDiamGyCcrtReplayMaxLifeTime": tmnxDiamGyCcrtReplayMaxLifeTime,
       "tmnxDiamApGx3gppQosMapTable": tmnxDiamApGx3gppQosMapTable,
       "tmnxDiamApGx3gppQosMapEntry": tmnxDiamApGx3gppQosMapEntry,
       "tmnxDiamApGx3gqmAADlMappingType": tmnxDiamApGx3gqmAADlMappingType,
       "tmnxDiamApGx3gqmAADlArbiterName": tmnxDiamApGx3gqmAADlArbiterName,
       "tmnxDiamApGx3gqmAADlSchedulrName": tmnxDiamApGx3gqmAADlSchedulrName,
       "tmnxDiamApGx3gqmAADlPolicerId": tmnxDiamApGx3gqmAADlPolicerId,
       "tmnxDiamApGx3gqmAADlQueueId": tmnxDiamApGx3gqmAADlQueueId,
       "tmnxDiamApGx3gqmAAUlMappingType": tmnxDiamApGx3gqmAAUlMappingType,
       "tmnxDiamApGx3gqmAAUlArbiterName": tmnxDiamApGx3gqmAAUlArbiterName,
       "tmnxDiamApGx3gqmAAUlSchedulrName": tmnxDiamApGx3gqmAAUlSchedulrName,
       "tmnxDiamApGx3gqmAAUlPolicerId": tmnxDiamApGx3gqmAAUlPolicerId,
       "tmnxDiamApGx3gqmAAUlQueueId": tmnxDiamApGx3gqmAAUlQueueId,
       "tmnxDiamApStatsTable": tmnxDiamApStatsTable,
       "tmnxDiamApStatsEntry": tmnxDiamApStatsEntry,
       "tmnxDiamApStatsLastCleared": tmnxDiamApStatsLastCleared,
       "tmnxDiamApStatsCciRequests": tmnxDiamApStatsCciRequests,
       "tmnxDiamApStatsCciAnswers": tmnxDiamApStatsCciAnswers,
       "tmnxDiamApStatsCcuRequests": tmnxDiamApStatsCcuRequests,
       "tmnxDiamApStatsCcuAnswers": tmnxDiamApStatsCcuAnswers,
       "tmnxDiamApStatsCctRequests": tmnxDiamApStatsCctRequests,
       "tmnxDiamApStatsCctAnswers": tmnxDiamApStatsCctAnswers,
       "tmnxDiamApStatsAsrRx": tmnxDiamApStatsAsrRx,
       "tmnxDiamApStatsAsaTx": tmnxDiamApStatsAsaTx,
       "tmnxDiamApStatsRarRx": tmnxDiamApStatsRarRx,
       "tmnxDiamApStatsRaaTx": tmnxDiamApStatsRaaTx,
       "tmnxDiamApStatsAarTx": tmnxDiamApStatsAarTx,
       "tmnxDiamApStatsAaaRx": tmnxDiamApStatsAaaRx,
       "tmnxDiamApStatsReqFailed": tmnxDiamApStatsReqFailed,
       "tmnxDiamApStatsReqRetransmits": tmnxDiamApStatsReqRetransmits,
       "tmnxDiamApStatsResultInfoTx": tmnxDiamApStatsResultInfoTx,
       "tmnxDiamApStatsResultInfoRx": tmnxDiamApStatsResultInfoRx,
       "tmnxDiamApStatsResultSuccessTx": tmnxDiamApStatsResultSuccessTx,
       "tmnxDiamApStatsResultSuccessRx": tmnxDiamApStatsResultSuccessRx,
       "tmnxDiamApStatsResultProtErrTx": tmnxDiamApStatsResultProtErrTx,
       "tmnxDiamApStatsResultProtErrRx": tmnxDiamApStatsResultProtErrRx,
       "tmnxDiamApStatsResultTransFailTx": tmnxDiamApStatsResultTransFailTx,
       "tmnxDiamApStatsResultTransFailRx": tmnxDiamApStatsResultTransFailRx,
       "tmnxDiamApStatsResultPermFailTx": tmnxDiamApStatsResultPermFailTx,
       "tmnxDiamApStatsResultPermFailRx": tmnxDiamApStatsResultPermFailRx,
       "tmnxDiamCcrtRStatTable": tmnxDiamCcrtRStatTable,
       "tmnxDiamCcrtRStatEntry": tmnxDiamCcrtRStatEntry,
       "tmnxDiamCcrtRStatLastCleared": tmnxDiamCcrtRStatLastCleared,
       "tmnxDiamCcrtRStatSessions": tmnxDiamCcrtRStatSessions,
       "tmnxDiamCcrtRStatDroppedMlt": tmnxDiamCcrtRStatDroppedMlt,
       "tmnxDiamCcrtRStatDroppedNew": tmnxDiamCcrtRStatDroppedNew,
       "tmnxDiamCcrtRStatDroppedCleared": tmnxDiamCcrtRStatDroppedCleared,
       "tmnxDiamCcrtRStatTerminatedCcat": tmnxDiamCcrtRStatTerminatedCcat,
       "tmnxDiamGxCcrtReplayTable": tmnxDiamGxCcrtReplayTable,
       "tmnxDiamGxCcrtReplayEntry": tmnxDiamGxCcrtReplayEntry,
       "tmnxDiamGxCcrtReplayAdminState": tmnxDiamGxCcrtReplayAdminState,
       "tmnxDiamGxCcrtReplayInterval": tmnxDiamGxCcrtReplayInterval,
       "tmnxDiamGxCcrtReplayMaxLifeTime": tmnxDiamGxCcrtReplayMaxLifeTime,
       "tmnxDiameterSessionObjects": tmnxDiameterSessionObjects,
       "tmnxDiamSeGxCcrtReplayTable": tmnxDiamSeGxCcrtReplayTable,
       "tmnxDiamSeGxCcrtReplayEntry": tmnxDiamSeGxCcrtReplayEntry,
       "tmnxDiamSeGxCcrtReplayIndex": tmnxDiamSeGxCcrtReplayIndex,
       "tmnxDiamSeGxCcrtReplaySessionId": tmnxDiamSeGxCcrtReplaySessionId,
       "tmnxDiamSeGxCcrtReplayAppPolicy": tmnxDiamSeGxCcrtReplayAppPolicy,
       "tmnxDiamSeGxCcrtReplayExpiryTime": tmnxDiamSeGxCcrtReplayExpiryTime,
       "tmnxDiameterNotificationObjs": tmnxDiameterNotificationObjs,
       "tmnxDiamAppPlcyName": tmnxDiamAppPlcyName,
       "tmnxDiamAppPeerName": tmnxDiamAppPeerName,
       "tmnxDiamAppTrapDescription": tmnxDiamAppTrapDescription,
       "tmnxDiamAppSessionId": tmnxDiamAppSessionId,
       "tmnxDiamAppSubscrId": tmnxDiamAppSubscrId,
       "tmnxDiamAppSapId": tmnxDiamAppSapId,
       "tmnxDiamAppSLAProfName": tmnxDiamAppSLAProfName,
       "tmnxDiamNotifyEventId": tmnxDiamNotifyEventId,
       "tmnxDiamNotifySpiShareType": tmnxDiamNotifySpiShareType,
       "tmnxDiamNotifySpiShareId": tmnxDiamNotifySpiShareId,
       "tmnxDiameterNotifyPrefix": tmnxDiameterNotifyPrefix,
       "tmnxDiameterNotifications": tmnxDiameterNotifications,
       "tmnxDiamPolicyPeerStateChange": tmnxDiamPolicyPeerStateChange,
       "tmnxDiamAppMessageDropped": tmnxDiamAppMessageDropped,
       "tmnxDiamAppSessionFailure": tmnxDiamAppSessionFailure,
       "tmnxDiamSessionEvent": tmnxDiamSessionEvent,
       "tmnxDiamPpPrxMcLocStateChanged": tmnxDiamPpPrxMcLocStateChanged,
       "tmnxDiamPrxMessageDropped": tmnxDiamPrxMessageDropped,
       "tmnxDiamMessageDropped": tmnxDiamMessageDropped,
       "tmnxDiamNdPeerStatActiveChanged": tmnxDiamNdPeerStatActiveChanged}
)
